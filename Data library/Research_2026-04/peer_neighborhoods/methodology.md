# Methodology — Peer-Neighborhood Pool Construction

**Stream C.** Reproducible instructions for building Pool A (matched) and Pool B (positive-deviant) end-to-end. A future analyst with moderate SQL/Python skill should be able to produce both pools from scratch using the steps below in <4 hours of compute + human review.

---

## 1. Data sources (all public, no license barrier)

| Dataset | URL | Geo | Years | Format | Key fields |
|---|---|---|---|---|---|
| USALEEP | https://catalog.data.gov/dataset/u-s-life-expectancy-at-birth-by-state-and-census-tract-2010-2015 | Census tract | 2010–2015 | CSV | tract GEOID, `e(0)`, SE |
| CDC NCHS state LE | https://www.cdc.gov/nchs/data-visualization/state-life-expectancy/ | State | annual through 2022 | CSV | state, LE |
| CDPH Life Expectancy by Chicago CA (historical) | https://data.cityofchicago.org/d/qjr3-bm53 | Community Area (77) | 1990–2023 | CSV (Socrata) | CA number, CA name, LE, year |
| CDPH 2023 Life Expectancy Data Brief | https://www.chicago.gov/content/dam/city/depts/cdph/statistics_and_reports/2025/2023-Life-Expectancy-Data-Brief_Final-for-Public-Release-09.10.2025.pdf | CA + citywide + race | 2023 | PDF | LE, 5 priority CAs |
| ACS 5-year (2019–2023) | https://www.census.gov/programs-surveys/acs/ via `tidycensus` R or `censusdata` Python | Tract / ZCTA / Place | 2019–2023 | CSV / API | race (B02001), poverty (S1701), income (S1901), unemployment (S2301), vacancy (DP04), housing age (DP04), foreign-born (S0501) |
| USDA Food Access Research Atlas (FARA) | https://www.ers.usda.gov/data-products/food-access-research-atlas/ | Census tract | 2019 (latest) | XLSX | LILATracts_1And10, LILATracts_halfAnd10, Urban |
| HOLC Mapping Inequality | https://dsl.richmond.edu/panorama/redlining/data | Polygon (1935–1940) | historical | GeoJSON + Shapefile | HOLC grade A/B/C/D |
| CDC PLACES | https://www.cdc.gov/places/ | Census tract | annual | CSV | 40 health indicators |
| NCHS Mortality Multiple Cause | https://www.cdc.gov/nchs/nvss/mortality_public_use_data.htm | County | annual | CSV | cause-of-death codes |
| Baltimore Neighborhood Health Profiles | https://health.baltimorecity.gov/neighborhood-health-profile-reports | Neighborhood (CSA) | 2011–2018 | PDF | LE by CSA |
| Boston Public Health Commission Health of Boston | https://www.boston.gov/sites/default/files/file/2024/03/HOB_Mortality_LE_2023_FINAL_Corr_032524.pdf | Neighborhood | 2023 provisional | PDF | LE |
| NYC DOHMH Community Health Profiles | https://www.nyc.gov/site/doh/data/data-publications/profiles.page | CD (59) | biennial | PDF | LE |
| LA County CCHP Profiles | http://publichealth.lacounty.gov/ohae/cchp.htm | Place / Community | 2018 | PDF | LE |

---

## 2. Reproducible pipeline

### Step 1 — Pull and clean tract-level base table
```sql
-- Postgres + PostGIS assumed; tract shapes loaded as tiger_tract
CREATE TABLE tract_base AS
SELECT
  u.tract_geoid,
  u.e0            AS le_usaleep_2010_2015,
  u.se            AS le_se,
  a.total_pop,
  a.pct_black_nh,
  a.pct_hispanic,
  a.pct_foreign_born,
  a.median_hh_income,
  a.poverty_rate,
  a.unemployment_rate,
  a.vacancy_rate,
  a.pct_housing_pre_1960,
  f.lilatracts_1and10  AS food_desert_flag,
  h.holc_grade         AS historical_holc_grade,
  t.state_abbr
FROM usaleep u
JOIN acs_5yr_2019_2023 a USING (tract_geoid)
LEFT JOIN usda_fara f USING (tract_geoid)
LEFT JOIN holc_tract_overlay h USING (tract_geoid)
JOIN tiger_tract t USING (tract_geoid)
WHERE u.se < 4.0;                                   -- drop high-SE tracts
```

### Step 2 — Build the similarity flags (criteria 1–10)
```python
import pandas as pd

df = pd.read_sql("SELECT * FROM tract_base", con)
state_le = pd.read_csv("nchs_state_le_2022.csv").set_index("state")["le"]

df["c1_race"]     = (df.pct_black_nh > 0.60) | (df.pct_hispanic > 0.80)
df["c2_income"]   = df.median_hh_income < df.groupby("msa").median_hh_income.transform(lambda s: s.quantile(0.20))
df["c3_poverty"]  = df.poverty_rate > 0.25
df["c4_food"]     = df.food_desert_flag == 1
df["c5_unemp"]    = df.unemployment_rate > 1.5 * df.groupby("msa").unemployment_rate.transform("mean")
df["c6_holc"]     = df.historical_holc_grade.isin(["C", "D"])
df["c7_le_gap"]   = df.le_usaleep_2010_2015 < (df.state_abbr.map(state_le) - 5.0)
df["c8_pop"]      = df.total_pop.between(2500, 50000)
df["c9_urban"]    = df.urbanicity == "Urban"
df["c10_housing"] = (df.vacancy_rate > 0.10) | (df.pct_housing_pre_1960 > 0.50)

df["similarity_score"] = df[[f"c{i}_{n}" for i, n in zip(
    range(1,11),
    ["race","income","poverty","food","unemp","holc","le_gap","pop","urban","housing"])]].sum(axis=1)
```

### Step 3 — Split into Pool A vs Pool B
```python
# Pool A: ≥7 criteria met, LE below state mean (c7 TRUE)
pool_A = df[(df.similarity_score >= 7) & (df.c7_le_gap == True)]

# Pool B: demographic match on 2,3,4,5,8,9,10 but LE ABOVE state mean
demo_criteria = df[["c2_income","c3_poverty","c4_food","c5_unemp","c8_pop","c9_urban","c10_housing"]].sum(axis=1)
pool_B = df[(demo_criteria >= 6) & (df.c7_le_gap == False) &
            ((df.pct_hispanic > 0.50) | (df.pct_asian > 0.30) | (df.pct_black_nh > 0.50))]
```

### Step 4 — Compute LE residuals from a regression model
This is how we rank positive deviants rather than just thresholding.
```python
import statsmodels.formula.api as smf

model = smf.ols(
    "le_usaleep_2010_2015 ~ poverty_rate + pct_black_nh + pct_hispanic + pct_foreign_born "
    "+ unemployment_rate + pct_uninsured + vacancy_rate + C(state_abbr)",
    data = df.dropna(subset=["le_usaleep_2010_2015","poverty_rate"])
).fit()

df["le_predicted"] = model.predict(df)
df["le_residual"]  = df.le_usaleep_2010_2015 - df.le_predicted

# Positive deviants: top 5% of residual
top_deviants = df.nlargest(int(0.05 * len(df)), "le_residual")
```

### Step 5 — Narrative layering
For each tract/neighborhood in `top_deviants` with similarity_score ≥5, do qualitative research:
1. Pull city/neighborhood health profile from the relevant municipal DOH.
2. Check academic literature for ethnographic / epidemiological profiles.
3. Verify against local newspaper reporting for recent changes.

### Step 6 — Sensitivity analyses (required for publication)
- **Alternative LE source.** Re-run Step 4 substituting Chetty Opportunity Atlas LE (which is employment-adjusted) where tract-level data available.
- **Drop small tracts.** Re-run with tracts >5,000 population only.
- **Drop COVID years.** Where post-2020 LE is used, provide pre-2020 and post-2020 separately; the Hispanic paradox differs substantially before/after COVID (Bor 2023).
- **HOLC sensitivity.** HOLC coverage is only ~200 cities; rerun for cities with HOLC coverage only and for the full national set.
- **Urbanicity.** Include / exclude rural reference cases (Starr County TX) to see if the Hispanic paradox is urban-only or broader.

---

## 3. Practical notes for the IMAN analyst who will actually do this

1. **Work at the community-area / neighborhood scale where possible, not raw tract.** Cities with strong community-health-planning data (Chicago CDPH, Boston BPHC, NYC DOHMH, Baltimore BCHD, LA County DPH) publish LE at the same scale IMAN operates. Aggregate USALEEP tracts to the reporting polygon using area-weighted population to reconcile.
2. **Don't use the USALEEP tract LE to compare 2024 outcomes.** USALEEP is a 2010–2015 snapshot. For outcome measurement, use:
   - NCHS Wonder mortality (county, annual) as primary
   - CDC PLACES indicators (tract, annual) as upstream proxies
   - State vital records (IL IDPH for Chicago) for tract-level recent mortality where available
3. **Chicago Health Atlas had machine-access issues during this research session (HTTP 403).** The Atlas is the single best interface for Chicago-specific indicators. A human analyst pulling via browser (or API with headers) will retrieve it; our automation could not.
4. **Verification protocol.** Every numeric claim that goes into a final deliverable must appear in `verification/claims_stream_C.csv` (or successor log). If a pool entry cannot provide a primary-source LE after 30 minutes, mark it `[UNVERIFIED CANDIDATE]` and move on — don't fabricate.
5. **Hispanic paradox interpretation.** The Bor et al. 2023 finding that COVID eliminated the Hispanic advantage is important; positive-deviant narratives should separate pre-COVID structural advantages from the pandemic shock, and should note whether the advantage recovered through 2022–2024 in the specific neighborhood.

---

## 4. Outputs the pipeline should produce

- `pool_A.csv` — one row per matched tract with all criterion flags and LE
- `pool_B.csv` — one row per positive-deviant tract with residual and demographic fields
- `pool_B_residual_distribution.png` — histogram of LE residuals with Pool B entries highlighted
- `pool_A_chicago_peer_map.png` — choropleth of Chicago community areas scored
- `methodology.md` (this file)
- `claims_log.csv` — every quantitative claim with URL, access date, verifier
