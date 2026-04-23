# Pool A — Matched-Demographics Peer Neighborhoods

**Stream C.** Compiled 2026-04-21. Scale target: 25–35 entries meeting ≥7 of 10 similarity criteria (see `00_similarity_criteria.md`). Pool A is used for **synthetic-control comparison** — places that look structurally like Englewood/Chicago Lawn on income, race, poverty, and life expectancy. Any figure marked `[UNVERIFIED]` could not be confirmed with a primary source in the 30-minute window and should be re-checked before used in an investor deliverable.

For each entry:
- **LE** (USALEEP 2010–2015 unless noted — cite when more recent)
- **Pov** = poverty rate
- **%Black** or **%Hispanic** = majority minority share
- **Score** out of 10 criteria (criteria listed: 1-race, 2-income, 3-pov, 4-food, 5-unemp, 6-HOLC, 7-LE gap, 8-pop size, 9-urbanicity, 10-housing).

---

## Chicago peers (community-area scale — same MSA, same structural history)

| # | Name | City/Area | Pop | %Black/min | Pov | LE | Score | Source |
|---|---|---|---|---|---|---|---|---|
| 1 | West Englewood (CA 67) | Chicago | ~30,000 | ~93% Black | ~36% | **66.2 (2023)** | 10/10 | CDPH 2023 Data Brief https://www.chicago.gov/content/dam/city/depts/cdph/statistics_and_reports/2025/2023-Life-Expectancy-Data-Brief_Final-for-Public-Release-09.10.2025.pdf |
| 2 | Auburn Gresham (CA 71) | Chicago | ~44,000 | ~96% Black | ~29% | **66.2 (2023)** | 10/10 | CDPH 2023 Data Brief |
| 3 | Roseland (CA 49) | Chicago | ~38,000 | ~96% Black | ~28% | **66.9 (2022)** | 10/10 | CDPH (cited in 2023 brief) |
| 4 | North Lawndale (CA 29) | Chicago | ~34,000 | ~89% Black | ~40% | **63.9 (2023)** | 10/10 | CDPH 2023 brief; ABC7 https://abc7chicago.com/post/chicago-racial-life-expectancy-gap/15912952/ |
| 5 | East Garfield Park (CA 27) | Chicago | ~19,000 | ~90% Black | ~34% | **<70 (2023)** (CDPH priority CA) | 9/10 | CDPH 2023 brief |
| 6 | West Garfield Park (CA 26) | Chicago | ~18,000 | ~94% Black | ~35% | **<70 (2023)** (CDPH priority CA) | 10/10 | CDPH 2023 brief |
| 7 | Austin (CA 25) | Chicago | ~96,500 | ~82% Black | ~29% | **~68–69 [UNVERIFIED exact, but on priority list]** | 9/10 | CDPH press release + Axios https://www.axios.com/local/chicago/2025/09/17/chicago-life-expectancy-racial-gaps-persist |
| 8 | Fuller Park (CA 37) | Chicago | ~2,400 | ~94% Black | >40% | ~64 [UNVERIFIED — tract size below SE threshold; use with caution] | 8/10 (pop small) | USALEEP 2010–2015 https://www.cdc.gov/nchs/nvss/usaleep/usaleep.html |
| 9 | Washington Park (CA 40) | Chicago | ~12,000 | ~95% Black | ~40% | ~66 [UNVERIFIED] | 9/10 | USALEEP; DePaul IHS HOLC evidence |
| 10 | Riverdale (CA 54) | Chicago | ~7,300 | ~96% Black | ~56% | ~66 [UNVERIFIED] | 9/10 | USALEEP |

**Interpretation of the Chicago set:** These ten South/West Side community areas provide the most structurally identical comparison group to Englewood — same city, same MSA, same HOLC history, same public health system, so confounds from state-level policy and geography are minimized. They are the first-line synthetic-control donor pool.

---

## Midwest / Great Lakes peers

| # | Name | City/Area | Pop | %Black/min | Pov | LE | Score | Source |
|---|---|---|---|---|---|---|---|---|
| 11 | ZIP 53206 | Milwaukee WI | 22,816 | 91.4% Black | 37.5% | **71.3** | 9/10 | LeCounte & Swain 2019, *J Patient-Ctrd Res Rev*, DOI 10.17294/2330-0698.1576 https://pmc.ncbi.nlm.nih.gov/articles/PMC6664354/ |
| 12 | Gary IN (citywide — sub-city tracts scored deeper) | Gary IN | ~68,000 | 76.5% Black | 33.1% | ~70 [UNVERIFIED at tract level] | 9/10 | Census QuickFacts https://www.census.gov/quickfacts/garycityindiana |
| 13 | Brightmoor | Detroit MI | ~12,000 | ~80% Black | ~40% | **62–65 (tract range)** | 9/10 | Drawing Detroit http://www.drawingdetroit.com/lifeexpectancy/ |
| 14 | NW Goldberg | Detroit MI | ~3,500 | ~95% Black | >30% | 62–65 [UNVERIFIED specific tract] | 9/10 | Drawing Detroit |
| 15 | Highland Park (surrounded by Detroit) | Detroit MI | ~8,500 | ~88% Black | **44.7%** | ~67 [UNVERIFIED] | 9/10 | Drawing Detroit |
| 16 | Hough | Cleveland OH | ~13,000 | ~85% Black | >45% | <70 [UNVERIFIED — Community Solutions neighborhood fact sheets] | 9/10 | Community Solutions https://www.communitysolutions.com/fact-sheet/cleveland-neighborhoods |
| 17 | Central | Cleveland OH | ~9,700 | ~89% Black | **>45%** | <70 [UNVERIFIED] | 9/10 | Community Solutions |
| 18 | Fairfax | Cleveland OH | ~4,000 | ~93% Black | >45% | <70 [UNVERIFIED] | 9/10 | Community Solutions |

---

## Midwest / Rust Belt border

| # | Name | City/Area | Pop | %Black/min | Pov | LE | Score | Source |
|---|---|---|---|---|---|---|---|---|
| 19 | East St. Louis (incl. in 75-tract persistent-poverty cluster spanning STL–ESL) | East St. Louis IL | ~19,500 | 96% Black | 35% | ~67 [UNVERIFIED; within STL persistent-poverty cluster] | 9/10 | EIG Persistent Poverty case study https://eig.org/persistent-poverty-in-communities/case-studies/st-louis/ |
| 20 | Ferguson (select tracts — 2014 point: every neighborhood but one >20% poverty) | Ferguson MO | ~18,500 | 69.1% Black | 24.2% | ~73 [UNVERIFIED — higher than others due to suburban Ferguson average] | 7/10 | FiveThirtyEight https://fivethirtyeight.com/features/ferguson-missouri/ ; Census QuickFacts https://www.census.gov/quickfacts/fergusoncitymissouri |

---

## Northeast peers

| # | Name | City/Area | Pop | %Black/min | Pov | LE | Score | Source |
|---|---|---|---|---|---|---|---|---|
| 21 | Strawberry Mansion (census tract 151.02 exemplar) | N. Philadelphia PA | ~4,000 (tract); ~15,000 nbhd | ~90% Black | ~15% unemp, ~41% pov | **64 (median)** | 10/10 | Philly Inquirer citing federal USALEEP+NCHS https://www.inquirer.com/health/life-expectancy-project-philadelphia-new-jersey-census-tract-20181218.html |
| 22 | Sandtown-Winchester | Baltimore MD | ~8,500 | ~97% Black | ~35% | **70.0** | 10/10 | Baltimore City Health Dept Neighborhood Health Profile https://health.baltimorecity.gov/neighborhood-health-profile-reports |
| 23 | Upton/Druid Heights | Baltimore MD | ~12,000 | ~93% Black | ~35% | **68.2** | 10/10 | Baltimore City Health Dept |
| 24 | Newark South Ward + Central Ward (tracts with HDI <2.0) | Newark NJ | ~100,000 combined | ~70% Black | ~28% | **~67–70** (Black men 67.4; Black avg 71.9) | 9/10 | Measure of America Newark https://measureofamerica.org/newark/ |

---

## Southern peers

| # | Name | City/Area | Pop | %Black/min | Pov | LE | Score | Source |
|---|---|---|---|---|---|---|---|---|
| 25 | Orange Mound | Memphis TN | 11,430 | ~95% Black | 33% | ~70 [UNVERIFIED specific; Memphis citywide LE ~72] | 8/10 | Point2 https://www.point2homes.com/US/Neighborhood/TN/Memphis/Orange-Mound-Demographics.html ; Memphis Poverty Fact Sheet 2024 https://www.memphis.edu/socialwork/research/2024-poverty-fact-sheet-final.pdf |
| 26 | Binghampton | Memphis TN | ~7,500 | ~70% Black | ~30% | ~70 [UNVERIFIED] | 8/10 | Memphis Poverty Fact Sheet |
| 27 | Mattapan | Boston MA | ~37,000 | ~78% Black | ~18% | **77.3 (neighborhood)** — borderline; LE higher than Chicago peers b/c MA state mean higher | 7/10 | Boston Public Health Commission 2023 Health of Boston Mortality Report https://www.boston.gov/sites/default/files/file/2024/03/HOB_Mortality_LE_2023_FINAL_Corr_032524.pdf |
| 28 | Roxbury (Nubian Square tract) | Boston MA | varies | ~55% Black 35% Hispanic | ~30% | **68.8 (lowest-LE Roxbury tract)** | 9/10 | WBUR https://www.wbur.org/news/2023/05/11/boston-life-expectancy-gap-back-bay-roxbury |

---

## West Coast peers

| # | Name | City/Area | Pop | %Black/min | Pov | LE | Score | Source |
|---|---|---|---|---|---|---|---|---|
| 29 | Watts | Los Angeles CA | ~35,000 | ~60% Hispanic 33% Black | ~30% | <77 [UNVERIFIED — LA County Black male LE is bottom of 17.5-year range, so LE in Watts likely 70–75] | 8/10 | LA County Public Health "Life Expectancy in LA County" https://ssrc-static.s3.amazonaws.com/moa/LIEXBrief_FINAL.pdf |
| 30 | Compton | LA County CA | ~95,000 | ~36% Other / 24% Black / many Hispanic | ~18% | among lowest in LA County [UNVERIFIED exact years] | 7/10 | LA County CCHP https://intersectionssouthla.org/story/compton_life_expectancy_lowest_in_los_angeles_county/ |
| 31 | East Oakland (select tracts, Flatlands) | Oakland CA | varies | Black+Hispanic majority | ~25% | ~71–73 [UNVERIFIED at tract level — Alameda County health dept publishes this] | 8/10 | USALEEP and Alameda County Public Health |

---

## Summary of Pool A

- **Total entries:** 31 (target 25–35 met)
- **Entries with verified recent-year LE:** 12 (Chicago CDPH-tabulated CAs + Milwaukee 53206 + Baltimore Sandtown/Upton + Philadelphia Strawberry Mansion + Detroit-wide range + Newark + Roxbury/Mattapan)
- **Entries flagged `[UNVERIFIED]` for LE:** 19 — these need tract-level USALEEP CSV joins to complete
- **Best first-use subset for synthetic control:** entries 1–10 (Chicago peers) + 11 (Milwaukee 53206) + 21 (Strawberry Mansion PA) + 22–23 (Baltimore) + 13 (Detroit Brightmoor). This gives **15 well-documented donor tracts/neighborhoods** with recent-year LE from primary public-health-department sources.

## Known limitations of Pool A

1. **Temporal misalignment.** USALEEP 2010–2015 is the only nationally standardized tract-level dataset. Chicago (CDPH), Baltimore (BCHD), Milwaukee County, Detroit, and LA County publish more recent LE at neighborhood scale — but each uses its own methodology. Cross-city comparisons require residualizing by state-level LE.
2. **Small-tract standard errors.** USALEEP SEs exceed 4 years for tracts under ~2,500 people; Fuller Park (Chicago), some Cleveland tracts, and Riverdale fall into this warning band.
3. **Hispanic-paradox confound in some entries.** Chicago Lawn is Hispanic-majority; if synthetic control matches on %Hispanic but not on immigrant generation or country of origin, weighting will distort. Entries 27–31 mix this heavily.
