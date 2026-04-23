# Baseline Profile — Englewood & Chicago Lawn (IMAN service area)

**Stream C — peer-neighborhood identification.** Compiled 2026-04-21. All numeric claims appended to `verification/claims_stream_C.csv`.

**Important caveat on sources.** The Chicago Health Atlas site (`chicagohealthatlas.org`) returned HTTP 403 during this research session and could not be scraped; CMAP PDFs returned as binary that could not be parsed live. Where those would have been the canonical source, we cite the next-best publicly available source (Wikipedia community area entries drawing on ACS, CMAP data snapshots, CDPH data briefs, USDA FARA public portal, Mapping Inequality). Any figure flagged `[UNVERIFIED]` needs a second-pass human check against the Chicago Health Atlas direct download.

---

## Englewood (Chicago Community Area 68)

| Indicator | Value | Year | Source |
|---|---|---|---|
| Total population | 21,411 | 2023 (ACS 5-yr) | Wikipedia/ACS — https://en.wikipedia.org/wiki/Englewood,_Chicago |
| Historical peak population | 97,595 | 1960 | Wikipedia/Census |
| % Black / African American | 88.0% | 2023 | Wikipedia/ACS |
| % Hispanic | 7.0% | 2023 | Wikipedia/ACS |
| % White | 1.4% | 2023 | Wikipedia/ACS |
| Median household income | $22,228 | 2020 | Wikipedia/ACS |
| Median household income (alt. ref) | $21,275 | 2021 | Growing Home / National Geographic citation — https://www.nationalgeographic.com/history/article/grassroots-activists-take-on-food-apartheid-in-chicagos-south-side |
| Poverty rate | 44–46.6% | 2000 & 2008–2012 ACS | Wikipedia/ACS |
| Poverty rate (recent cite) | ~45% (incl. 1 in 2 children) | ~2022 | The Click — https://theclick.news/life-expectancy-between-two-chicago-neighborhoods-reveals-years-of-systemic-racism/ |
| Unemployment rate (16+) | 28% | 2008–2012 | Wikipedia/ACS |
| Life expectancy at birth | ~60 years | ~2022 | The Click (citing CDPH) — same URL |
| Life expectancy at birth | <70 years, confirmed on CDPH priority list | 2023 | CDPH Life Expectancy Data Brief 2023 — https://www.chicago.gov/content/dam/city/depts/cdph/statistics_and_reports/2025/2023-Life-Expectancy-Data-Brief_Final-for-Public-Release-09.10.2025.pdf |
| USALEEP LE (original) | 62–67 (tract range) | 2010–2015 | USALEEP (CDC/NAPHSIS/RWJF) — https://www.cdc.gov/nchs/nvss/usaleep/usaleep.html |
| Leading causes of death (citywide for Black Chicagoans, Englewood consistent) | heart disease, cancer, homicide, diabetes, stroke | 2023 | CDPH Data Brief 2023 |
| Food desert status | Yes — USDA LILATracts | 2019 update | USDA FARA |
| HOLC redlining grade | Almost entirely yellow/red (C/D); West Englewood contains both yellowlined and redlined tracts | 1935–1940 maps | DePaul IHS / Mapping Inequality — https://www.housingstudies.org/news/following-yellowlined-road/ |
| Historical segregation context | 99% yellow/red on HOLC maps (Englewood, Oakland, Washington Park, Woodlawn community areas) | 1935–1940 | DePaul IHS |

**Age distribution [DATA GAP at the full detail level]** — source-of-record would be ACS tables B01001 / S0101 for tracts 6801–6809; not fetched in this session. Median age in Chicago overall is ~35; Englewood skews slightly younger with significant population loss among prime-working-age adults.

**Chicago citywide context for interpretation (CDPH 2023):**
- Citywide LE 78.7 years (2023)
- Black Chicagoans LE 71.8 years; Asian/PI 86.8 years; gap = 10.6–15 years
- The five CDPH "priority communities" (Englewood, West Englewood, North Lawndale, West Garfield Park, East Garfield Park) all had LE under 70 in 2023

Source: https://www.chicago.gov/content/dam/city/depts/cdph/statistics_and_reports/2025/2023-Life-Expectancy-Data-Brief_Final-for-Public-Release-09.10.2025.pdf and https://www.axios.com/local/chicago/2025/09/17/chicago-life-expectancy-racial-gaps-persist

---

## Chicago Lawn (Chicago Community Area 66)

| Indicator | Value | Year | Source |
|---|---|---|---|
| Total population | 53,460 (Wikipedia) / 55,789 (Point2) | 2023 | Wikipedia ACS-based — https://en.wikipedia.org/wiki/Chicago_Lawn,_Chicago ; Point2Homes — https://www.point2homes.com/US/Neighborhood/IL/Chicago/Chicago-Lawn-Demographics.html |
| % Hispanic (majority) | 61.7% | 2023 | Wikipedia/ACS |
| % Black / African American | 33.4% | 2023 | Wikipedia/ACS |
| % White | 2.1% | 2023 | Wikipedia/ACS |
| Median household income | $36,278 (2020 Wikipedia) / $46,945 (2023 Point2) | 2020–2023 | Wikipedia, Point2Homes |
| Mean household income (2023) | $74,084 | 2023 | Point2Homes |
| Poverty rate | ~19.2% (locals above line 80.8%) | 2023 | Point2Homes/ACS |
| Historical demographic change | 1990 43% non-Hispanic white → 2000 53% Black, 35% Hispanic, 10% white → 2023 62% Hispanic, 33% Black | — | Wikipedia |
| Life expectancy | [UNVERIFIED — not in CDPH 2023 priority list, but adjoins five priority CAs; Chicago Health Atlas 403'd. Best estimate: 72–75 years based on intermediate positioning between citywide 78.7 and Black South Side 68–72] | 2023 | CDPH 2023 data brief (does not tabulate every CA in scraped summary) |
| Food desert status | Partial LILATracts designation (USDA) | 2019 | USDA FARA — needs tract-level verification |
| HOLC redlining grade | Majority C/D in 1935–1940 HOLC maps for Chicago southwest side; specific block grades vary | 1935–1940 | Mapping Inequality / DePaul IHS |

**Key structural difference from Englewood:** Chicago Lawn is **Hispanic-majority with a substantial Black minority** rather than predominantly Black. This matters for peer matching — Chicago Lawn's demographics align it with Hispanic-paradox comparator neighborhoods (East Boston, Boyle Heights, Little Village) while Englewood's align with the Black-majority disinvested-neighborhood set (Roseland, West Baltimore, Detroit, Cleveland Hough, Milwaukee 53206).

---

## Combined IMAN service area (Englewood + Chicago Lawn)

- Approx. combined population: ~75,000
- Both are in Cook County, Chicago, IL
- Both have poverty rates above the Chicago average (17% citywide)
- Both carry HOLC C/D historical legacy
- Life expectancy gap vs. Streeterville (citywide benchmark with LE ~90): ~30 years in Englewood; likely 15–20 years in Chicago Lawn (unverified)
- Both are designated food-access-limited on USDA FARA (Englewood fully, Chicago Lawn partially)

---

## Data gaps flagged for stream-B / future verification
1. Chicago Health Atlas direct-scrape of Englewood page (403 during this session).
2. Tract-level USALEEP download for Cook County tracts in community areas 66 and 68 (CSV at https://catalog.data.gov/dataset/u-s-life-expectancy-at-birth-by-state-and-census-tract-2010-2015).
3. Tract-level USDA FARA download (2019 revision) to confirm LILATract designations block by block.
4. ACS 5-yr (2019–2023) detailed age distribution for both community areas.
5. Chicago Lawn life expectancy — CDPH's 2023 brief tabulates all 77 community areas but the summary we accessed did not list Chicago Lawn directly; raw data needed.
6. Leading cause of death tables by community area — CDPH publishes these but we could not fetch the full PDF in this session.
