# Top-10 Priority Datasets for IMAN 2040 Life-Expectancy Analysis

*Stream B — verified 2026-04-21. All URLs fetched and confirmed reachable on that date. Where a URL has moved or been removed (notably EPA EJScreen), the replacement / archival source is documented below.*

The ranking below is based on (a) whether the dataset directly measures an outcome IMAN is trying to move, (b) whether it supports the peer-neighborhood matching IMAN's synthetic-control design depends on, and (c) the tract-level resolution IMAN needs for Englewood (CA 68) and Chicago Lawn (CA 66 and adjacent 63).

---

## 1. CDC PLACES — Census Tract Data (2025 release)

- **Landing page:** https://www.cdc.gov/places/index.html
- **Direct dataset:** https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-Census-Tract-D/cwsq-ngmh
- **Geo:** 2020 census-tract geographies (83,522 tracts covered nationally)
- **Temporal:** BRFSS 2022 + ACS 2018-2022 (2025 release); annual
- **What it contains:** 40 measures — 12 health outcomes (diabetes, obesity, CHD, stroke, asthma, mental distress, etc.), 7 preventive-service rates (colonoscopy, flu shot, BP med adherence, Pap/mammo), 4 chronic-disease risk behaviors (smoking, binge drinking, physical inactivity, sleep), 7 disability indicators, 3 self-rated health, 7 social-needs indicators.
- **Why IMAN needs it:** This is the single most important dataset for IMAN. It gives modeled tract-level prevalence for roughly every chronic disease IMAN's health programs address. For the investor narrative ("Englewood's diabetes prevalence is X; after IMAN Health Clinic expansion + Fresh Market we expect Y") this is the benchmark.
- **Englewood/Chicago Lawn first query:** Pull 2025 release for all tracts in Chicago community areas 66, 67, 68, 63 and compute weighted means of: diabetes, obesity, hypertension, current smoking, routine checkup, and frequent mental distress. Compare against (a) city of Chicago mean, (b) Streeterville tracts (CA 8 — the decision-tree comparator), and (c) peer-neighborhood pool from Stream C.
- **Gotchas:** Model-based estimates — NOT direct measurements. Credible-intervals are wide at tract level; small changes year-over-year are often noise, not signal. Starting with the 2024 release geography switched from 2010 to 2020 tracts — crosswalk required for any pre-2024 time series. BRFSS underlying data for Chicago is MMSA-wide; tract-level variation comes from post-stratification modeling, so PLACES cannot be used to detect a tract-level *change* caused by a tract-level intervention within ~3 years.

---

## 2. USALEEP — Life Expectancy at Birth by Census Tract

- **Landing page:** https://www.cdc.gov/nchs/nvss/usaleep/usaleep.html
- **Direct download:** https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NVSS/USALEEP/
- **Geo:** Census tract (2010 geographies)
- **Temporal:** Deaths pooled 2010-2015. **No subsequent refresh has been announced as of the verification date.**
- **What it contains:** Abridged period life tables and life expectancy at birth for almost every U.S. census tract; standard errors included.
- **Why IMAN needs it:** USALEEP is the source of the "30-year life expectancy gap" claim IMAN builds its case on. It is also the outcome variable for the Stream E "positive-deviant" regression (LE regressed on poverty, % Black, % uninsured, unemployment).
- **Englewood/Chicago Lawn first query:** Merge USALEEP to ACS 2013-2017 tract file; compute regression residuals; identify positive-deviant tracts matched on race and poverty; cross-walk Illinois state file (IL_A.CSV) to the specific tracts in CA 68 (Englewood) and CA 66 (Chicago Lawn).
- **Gotchas:** **2010-2015 data pre-dates most IMAN programs.** Cannot serve as an outcome variable for programs launched after 2015. Must be triangulated with newer CDC WONDER cause-specific mortality. NCHS suppresses LE for tracts with < 50 deaths — some Englewood tracts will have missing values. Uses 2010 tract geographies — crosswalk to 2020 tracts required.

---

## 3. Chicago Health Atlas (CDPH)

- **Landing page:** https://chicagohealthatlas.org/
- **Download portal:** https://chicagohealthatlas.org/download
- **Geo:** 77 Chicago community areas (primary); ZIP; census tract; ward for some indicators
- **Temporal:** Varies by indicator; most 2013-2024
- **What it contains:** 160+ indicators spanning mortality (infant mortality, diabetes deaths, opioid overdose deaths, firearm deaths), chronic disease prevalence, birth outcomes, healthcare access, behavioral health, COVID-era data, and social determinants. Many from CDPH-owned surveillance plus Healthy Chicago Survey.
- **Why IMAN needs it:** Fastest path to an apples-to-apples comparison of Englewood / Chicago Lawn to the rest of Chicago. CDPH publishes community-area-level data that has already been QA'd and suppression-adjusted. The city's own pipeline is usually more current than federal NVSS releases.
- **Englewood/Chicago Lawn first query:** Download the full community-area Excel for all 160 indicators, filter to CA 66 / 67 / 68 / 63, join to CA 8 (Streeterville). Build a one-sheet scorecard: outcome | CA 68 | CA 8 | Chicago mean | gap | trend.
- **Gotchas:** Indicator definitions are CDPH's own — may differ from federal standard (e.g., CDPH firearm-death rates count differently than CDC WONDER). Community-area resolution can mask tract-level variation (Englewood's west side differs from east). Updates are episodic, not calendar-based.

---

## 4. USDA Food Access Research Atlas

- **Landing page:** https://www.ers.usda.gov/data-products/food-access-research-atlas
- **Direct data:** `/download-the-data` subpage
- **Geo:** Census tract
- **Temporal:** 2010, 2015, 2019 vintages (2019 is current)
- **What it contains:** Tract-level flags — LILATracts (low-income and low-access), distance to nearest supermarket at ½-mile, 1-mile, 10-mile, and 20-mile thresholds, vehicle-access indicator, and income eligibility flag.
- **Why IMAN needs it:** Establishes the "food desert" precondition that IMAN Fresh Market + Fresh Boost + WIC Access programs are designed to address. Required as a peer-neighborhood matching variable. Decision tree node FA1-FA4.
- **Englewood/Chicago Lawn first query:** Flag every tract in CA 66, 67, 68 as LILATracts 0/1 and compute % of tract population classified low-access — benchmark against peer-neighborhood pool.
- **Gotchas:** USDA uses a store-level database that can miss recent openings / closings. The 2019 vintage does not capture 2020-2024 grocery-store openings and closures caused by COVID and inflation. Atlas updates on ~5-year cadence — do not use for post-intervention evaluation in a tight time window.

---

## 5. EPA EJScreen (via archival mirror)

- **Original (removed):** https://ejscreen.epa.gov/mapper/ — **EPA removed this tool from its website on 5 February 2025.**
- **Current accessible copies:**
  - Public Environmental Data Partners reconstruction: https://pedp-ejscreen.azurewebsites.net/
  - Harvard Dataverse archive: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/RLR5AX
- **Geo:** Block group and tract
- **Temporal:** EJScreen 2.3 (2015-2023 vintages) is the last EPA-produced version
- **What it contains:** Environmental indicators (PM2.5, ozone, diesel PM, air toxics cancer risk, respiratory hazard index, traffic proximity, lead-paint index, Superfund proximity, RMP-facility proximity, hazardous-waste proximity, UST, wastewater), demographic indicators, and indexes combining them.
- **Why IMAN needs it:** PM2.5 and traffic proximity are the central evidence base for MT1 (bus electrification / PM2.5 reduction) and the environmental-justice framing of IMAN's 2040 plan. Block-group resolution supports finer-grained analysis than PLACES.
- **Englewood/Chicago Lawn first query:** Pull PM2.5, diesel PM, and respiratory hazard index for every block group in CA 68 and CA 66; benchmark against Streeterville (CA 8) and Chicago mean.
- **Gotchas:** **FLAG — tool removed by EPA in 2025.** Use the PEDP / Harvard archive; document provenance in any deliverable. The reconstructed version is unofficial. Updates past 2023 are not guaranteed. For newer PM2.5 data, triangulate with AirNow + EPA AQS.

---

## 6. ACS 5-Year Estimates (2020-2024)

- **Landing page:** https://www.census.gov/programs-surveys/acs/data.html
- **Access:** https://data.census.gov (web) + https://api.census.gov/data (API)
- **Geo:** Block / block group / tract / place / county; IMAN will primarily use tract
- **Temporal:** Most recent verified release is 2020-2024 (Dec 2025). Prior vintages accessible back to 2005-2009.
- **What it contains:** Detailed demographics, income, poverty, educational attainment, race / ethnicity / ancestry, nativity / citizenship, housing tenure, housing cost burden, vehicle access, household composition, disability, language spoken at home, veteran status, labor-force participation, commute time, health insurance.
- **Why IMAN needs it:** The denominator for almost every other dataset. Required as covariates for synthetic-control matching, for Stream C peer-neighborhood identification, and for stratified descriptive statistics.
- **Englewood/Chicago Lawn first query:** Pull Tables B19013 (median HH income), B17001 (poverty), B02001 (race), B15003 (educational attainment), B27001 (insurance), B25003 (tenure), B25070 (rent burden), B08201 (vehicle access) for Cook County tracts in CA 66 / 67 / 68 / 63.
- **Gotchas:** Margins of error at tract level can be huge (±$5K-$10K for median income). Always display MOE and avoid ranking tracts by small differences. Variables change between vintages — especially race/ethnicity tables post-2020.

---

## 7. HMDA (Home Mortgage Disclosure Act)

- **Landing page:** https://www.consumerfinance.gov/data-research/hmda/
- **Data Browser:** https://ffiec.cfpb.gov/data-browser/
- **Geo:** Loan records geocoded to census tract
- **Temporal:** 2007-2025; 2025 Modified LAR released April 2026
- **What it contains:** Every mortgage application — action taken, loan amount, applicant income, race, ethnicity, sex, denial reason, lien status, loan purpose, and geocoded tract.
- **Why IMAN needs it:** Structural-disinvestment evidence. Quantifies the denial-rate gap in Englewood vs peer tracts — foundational narrative data for investor pitches and for housing interventions HO3 (CLTs) and HO4 (mixed-income). Also feeds Stream D (comparable disinvested neighborhoods).
- **Englewood/Chicago Lawn first query:** For loan-purpose=home purchase, race=Black, year=2015-2024, Englewood tracts: compute denial rate, median loan amount, and compare to Streeterville tracts.
- **Gotchas:** 2018+ data uses expanded fields; pre-2018 records use a different schema. The "modified LAR" released in spring is missing some fields; the "snapshot" released in late summer is the full file. Geography field uses year-of-submission census tract boundaries — crosswalk required for time-series.

---

## 8. Chicago Data Portal Crime Data (2001–Present)

- **Landing page:** https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2
- **API:** `https://data.cityofchicago.org/resource/ijzp-q8t2.csv` (Socrata)
- **Geo:** Block-masked address + beat + ward + community area + district
- **Temporal:** 2001-present, daily update with 7-day lag
- **What it contains:** Every CPD crime report — primary type, description, arrest flag, domestic flag, lat/lon (block-masked), datetime.
- **Why IMAN needs it:** Central evaluation dataset for CP1 (Group Violence Intervention), CP2 (Cure Violence / READI), IM3 (Green Reentry workforce), and the Chicago-specific violence-interruption narrative. Daily update cadence makes pre/post analysis feasible.
- **Englewood/Chicago Lawn first query:** Filter `community_area IN (66, 67, 68, 63)` and `primary_type IN ('HOMICIDE', 'BATTERY', 'ASSAULT')` for 2015-2025; overlay CP2 Cure Violence program start dates; estimate interrupted-time-series model.
- **Gotchas:** Under-reporting has changed over time (CPD data quality improved post-2016 consent decree). Block-masking of address means spatial analysis inside a beat is noisy. Primary_type field definitions changed (IUCR → NIBRS) — re-map codes when analyzing time series.

---

## 9. HRSA UDS (Uniform Data System) — FQHC Benchmarking

- **Landing page:** https://data.hrsa.gov/topics/health-centers/uds
- **Download:** https://data.hrsa.gov/data/download
- **Geo:** Health-center-level (some service-area tables)
- **Temporal:** 2010-2024 (2024 data submitted by Feb 15, 2025)
- **What it contains:** Every federally-funded health center's annual performance: total patients, patient demographics, insurance mix, DM control (HbA1c < 9), HTN control (<140/90), depression screening, prenatal / postpartum visits, dental visits, cancer screens, financial performance, staffing FTEs.
- **Why IMAN needs it:** IMAN Health Clinic is a Federally Qualified Health Center — its UDS is its official performance report card. UDS is also the *only* uniform peer-comparable dataset for Tier-1 outcome HC1 (FQHC expansion ~1.5 yr LE gain). Need it to benchmark the IMAN Health Center against other Chicago / national FQHCs.
- **Englewood/Chicago Lawn first query:** Pull IMAN Health Clinic's most recent UDS (by grant number), compute HTN-control and DM-control rates, benchmark against all Illinois FQHCs and against national FQHCs matched on % Medicaid + % Black patient population.
- **Gotchas:** Center-level tables redact some variables for small centers. UDS definitions of HTN/DM control changed in 2017 and again in 2022 — time series must be re-baselined. 2024 data will be definitively available on HRSA Data Warehouse by mid-2025; for 2025 data wait until Q2 2026.

---

## 10. Mapping Inequality (HOLC Redlining)

- **Landing page:** https://dsl.richmond.edu/panorama/redlining/
- **Data downloads:** on the same page, "Downloads" panel — Shapefile + GeoJSON + GeoPackage of all 7,148 neighborhoods across 143 cities
- **Geo:** Polygon (1930s HOLC neighborhood boundaries)
- **Temporal:** 1935-1940 (historical, stable)
- **What it contains:** Every HOLC-graded neighborhood in the 1930s — A (green, "best"), B (blue, "still desirable"), C (yellow, "definitely declining"), D (red, "hazardous"). Chicago is fully mapped.
- **Why IMAN needs it:** Structural-cause narrative anchor. Englewood and Chicago Lawn both contain neighborhoods graded D ("redlined") in the 1930s. This is the single most compelling visual for why today's gap exists. Also a required matching variable in Stream C peer-neighborhood identification.
- **Englewood/Chicago Lawn first query:** Overlay HOLC polygons on modern Chicago tracts; compute % of each tract historically in a D-graded area; use as a binary "redlined" covariate in all regressions.
- **Gotchas:** CC BY-NC-SA license requires share-alike and non-commercial attribution. HOLC boundaries do not align cleanly with modern census tracts — use area-weighted overlay, not a point-in-polygon. Not every city is mapped; Stream D peer projects in non-HOLC cities will lack this covariate.

---

## Honorable mentions (Tier 1+ that didn't make top-10)

- **NaNDA (ICPSR):** labor-saving pre-built neighborhood measures — saves a week of construction.
- **Eviction Lab:** critical for the housing-instability → mortality pathway.
- **Opportunity Atlas:** intergenerational-mobility story for the ED1-ED5 arguments.
- **CDC WONDER:** only source for recent cause-specific mortality at county level — essential supplement to USALEEP.
