# Peer & Positive-Deviant Atlas
**Audience:** strategy team, development staff, research partners | **Length:** ~15 min
**Supersedes:** `04_peer_and_positive_deviant_atlas.TEMPLATE.md`

**Framework authority.** The 9-criterion similarity rubric and the 16-community peer pool in this document are the **client's own canonical framework**, submitted in `Data library/Comparable Communities (1).docx` on 2026-04-21 and captured in [peer_neighborhoods/01_client_canonical_list.md](../peer_neighborhoods/01_client_canonical_list.md). We do not propose a replacement. Our Stream C work below is **tract-level resolution of the client's list** — enumerating the specific census tracts inside each named community that best match the 9-criterion profile — plus descriptive benchmarking of those tracts.

---

## Part 1 — Englewood / Chicago Lawn baseline

Condensed from [peer_neighborhoods/01_iman_baseline.md](../peer_neighborhoods/01_iman_baseline.md). All sources in [verification/claims_log.csv](../verification/claims_log.csv) (Stream C rows).

### Englewood (Community Area 68)
- Population: 21,411 (2023 ACS 5-yr) — down from a 1960 peak of 97,595.
- Race: 88.0% Black, 7.0% Hispanic, 1.4% White.
- Median HH income: $22,228 (2020 ACS).
- Poverty rate: 44–46.6% (2000 & 2008–2012 ACS); ~45% (2022 estimate incl. 1 in 2 children below poverty).
- Unemployment (16+): 28% (2008–2012).
- **Life expectancy: 67.7 yrs (2023, CDPH).** USALEEP (2010–2015): 62–67 tract range.
- Leading causes of death (citywide for Black Chicagoans): heart disease, cancer, homicide, diabetes, stroke.
- Food desert: Yes (USDA LILATracts, 2019).
- HOLC redlining: almost entirely yellow/red (C/D). West Englewood contains both yellowlined and redlined tracts. DePaul IHS: 99% yellow/red on HOLC maps across Englewood, Oakland, Washington Park, Woodlawn.

### Chicago Lawn (Community Area 66)
- Population: 53,460–55,789 (2023).
- Race: 61.7% Hispanic, 33.4% Black, 2.1% White (Hispanic-majority, unlike Englewood).
- Median HH income: $36,278 (2020) / $46,945 (2023 Point2).
- Poverty rate: ~19.2% (2023 ACS).
- **LE [UNVERIFIED]: 72–75 yr estimate** (not on CDPH 2023 priority list; Chicago Health Atlas returned 403 during research; requires direct CDPH pull).
- Food desert: Partial LILATracts.
- Structural note: Chicago Lawn's Hispanic-majority composition aligns it with the Hispanic-paradox comparators (East Boston, Boyle Heights, Little Village); Englewood aligns with the Black-majority disinvested set (Roseland, West Baltimore, West Detroit, Hough, 53206 Milwaukee).

### Chicago citywide context (CDPH 2023)
- Citywide LE: 78.7 yrs.
- Black Chicagoans: 71.8 yrs. Asian/PI: 86.8 yrs. Gap: 10.6–15 yrs.
- CDPH 2023 priority communities (all LE <70): Englewood, West Englewood, North Lawndale, West Garfield Park, East Garfield Park.

---

## Part 2 — Peer pool (Pool A, matched to client's 16 communities)

**Authoritative peer pool.** The client's 16 communities, grouped as submitted:

| Region | Community |
|---|---|
| Midwest — strongest match | Gary IN • East St. Louis IL • Flint MI • Youngstown OH • Toledo OH (select nbhds) • Rockford IL • South Bend IN |
| Large-city low-income nbhds | South Side Chicago • West Detroit • North Milwaukee • West Cleveland |
| South / Sunbelt | Memphis TN • Birmingham AL • Jackson MS • Shreveport LA |

**Client's 9-criterion similarity rubric** (from the same doc; 7–9 = strong, 5–6 = moderate, <5 = weak):

1. Income: median HH $25–40k; wealth index <50.
2. Housing: renter share ≥60%; ownership ≤40%; median home value <$200k.
3. Employment: industrial/manufacturing/service/retail/logistics; limited white-collar.
4. Consumer: discount retailer preference, SNAP/EBT usage, price sensitivity.
5. Demographics: median age 30–40; college <30%; HH size 2–3.
6. Urban form: moderate density; mixed residential + small retail corridors; walkability.
7. Economic growth: −1% to +1% population growth; limited new development.
8. Affordability pressure: housing affordability index <80.
9. Diversity & language: primarily English; 10–20% Spanish.

**Tract-level resolution by Stream C** ([peer_neighborhoods/02_pool_A_matched.md](../peer_neighborhoods/02_pool_A_matched.md)). Highlights:

### Inside Chicago (first-line donor pool — same MSA, CDPH, HOLC history)
| CA | Name | Pop | %Black | Pov | LE (2022–23) | Source |
|---|---|---|---|---|---|---|
| 67 | West Englewood | ~30k | ~93% | ~36% | 66.2 | CDPH 2023 |
| 71 | Auburn Gresham | ~44k | ~96% | ~29% | 66.2 | CDPH 2023 |
| 49 | Roseland | ~38k | ~96% | ~28% | 66.9 | CDPH |
| 29 | North Lawndale | ~34k | ~89% | ~40% | 63.9 | CDPH 2023 |
| 27 | East Garfield Park | ~19k | ~90% | ~34% | <70 | CDPH 2023 |
| 26 | West Garfield Park | ~18k | ~94% | ~35% | <70 | CDPH 2023 |
| 25 | Austin | ~96.5k | ~82% | ~29% | ~68–69 [unverified exact] | CDPH / Axios |

### Rust Belt / Great Lakes (client-named cities)
| Tract/area | City | %Black | Pov | LE | Evidence |
|---|---|---|---|---|---|
| ZIP 53206 | Milwaukee | 91.4% | 37.5% | **71.3** | LeCounte & Swain 2019 |
| Brightmoor | Detroit | ~80% | ~40% | 62–65 | Drawing Detroit |
| Hough | Cleveland | ~85% | >45% | <70 | Community Solutions |
| Central | Cleveland | ~89% | >45% | <70 | Community Solutions |
| East St. Louis | East St. Louis | 96% | 35% | ~67 [unverified exact] | EIG persistent-poverty |
| Highland Park | Detroit | ~88% | 44.7% | ~67 [unverified] | Drawing Detroit |

### Northeast
| Tract/area | City | %Black | Pov | LE |
|---|---|---|---|---|
| Strawberry Mansion (151.02) | N. Philadelphia | ~90% | ~41% | **64 (median)** |

Gary IN, Youngstown OH, Toledo OH, Rockford IL, South Bend IN, Memphis, Birmingham, Jackson MS, and Shreveport all have named tracts inside them that meet ≥7/9 of the client's criteria; specific tract identifiers require the human data-team pull flagged in the measurement plan.

**How the pool is used.** Donor pool for synthetic-control DiD against Englewood (and secondarily Chicago Lawn). The Chicago subset is the first-line choice because it controls for state-level policy and metro geography; the out-of-state subset is the robustness check.

---

## Part 3 — Positive-deviant pool (reference set, NOT peer set)

**Explicitly outside the client's peer framework.** The client's 9 criteria select Rust Belt disinvestment. The positive deviants below share Englewood's income/poverty profile but achieve higher LE — almost always in Latino or Asian immigrant enclaves. They are the **aspirational** comparison, not the matched comparison. Full profiles and caveats in [positive_deviants/](../positive_deviants/).

### Confirmed positive deviants (with primary LE data)

| Neighborhood | City | LE | Residual (after salmon-bias haircut) | Primary source |
|---|---|---|---|---|
| **Little Village / La Villita (CA 30)** | Chicago | ~82 | +7 yrs | CDPH Chicago Health Atlas / CDPH 2023 brief |
| **Washington Heights / Inwood (MN12)** | Manhattan | 84.0 | +6 | NYC DOHMH Community Health Profiles 2018 |
| **Sunset Park** | Brooklyn | 82.6 | +5 | NYC DOHMH |
| **Chinatown / LES (MN03)** | Manhattan | 82.2 | +4.5 | NYC DOHMH |
| **Jackson Heights (QN3)** | Queens | ~83 | +5 | NYC DOHMH |
| **East Boston + Chelsea** | MA | ~78–81 | +4–5 (weaker; MA state-level effect contaminates) | Boston BPHC; state DPH |
| **Boyle Heights / East LA** | LA | ~77–79 | +4 | LA County DPH |
| **Hialeah** | Miami-Dade | ~81 | +3–4 | Miami-Dade proxy |

### Mixed / cautionary

- **Starr County TX.** +9–11 residual but 40–60% salmon-bias artifact; rural, not a template.
- **Cedar-Riverside / Little Mogadishu (Minneapolis).** Does **not** show positive deviance — instructive failure of naive transfer.
- **East Harlem.** Not a deviant (acculturation-erosion case).
- **West Philadelphia (Spring Garden area).** Black-majority tracts do not replicate the Hispanic-paradox pattern — honest caveat for IMAN's transferability claim.

### The 7 recurring structural features (full synthesis: [positive_deviants/02_synthesis.md](../positive_deviants/02_synthesis.md))

From the 8 confirmed deviants, 5-of-8 or better:

1. Dense walkable retail corridor + fresh food in 10 minutes. *(Buettner: "Move naturally" / Sallis Lancet 2016.)*
2. Faith institution as simultaneous health/social-services hub. *(VanderWeele JAMA 2017: weekly attendance → +4 to +14 yrs LE.)*
3. Multigenerational household norm. *(Chen & Chen 2019.)*
4. Ethnic-density + small-business ownership — residents own what they shop at. *(Eschbach 2004; Walton 2012.)*
5. Traditional dietary pattern retained at first-generation level. *(Ruiz 2013; Santiago-Torres 2014.)*
6. High collective efficacy. *(Sampson, Raudenbush & Earls, Science 1997.)*
7. Low smoking and alcohol, especially among immigrant women. *(NYC DOHMH CHS; Ruiz 2013.)*

Five of seven are manufacturable by an organization: #1 walkable corridor, #2 faith-health co-location, #3 multigenerational housing, #4 small-business-owner retail, #6 collective efficacy. IMAN's 63rd Street / Chicago Lawn program stack builds all five.

---

## Part 4 — Benchmark projects (25 profiles)

Full profiles: [similar_projects/](../similar_projects/). Categorized by relevance:

### Place-based "three-legged-stool" anchors (housing + education + wellness)
- **Purpose Built Communities / East Lake, Atlanta** — 30-yr anchor model. 90% crime drop, Drew Charter 98% graduation, 542 mixed-income units. **Caveat: 1-for-1 replacement promise failed; only 16% of original public-housing families returned; Black population fell 22%.** Urban Institute 2022 retrospective documents displacement.
- **Harlem Children's Zone** — Zone-wide K–college pipeline. Promise Academy charter grade-level gains.
- **Purpose Built replication network** — 28 sites nationally.
- **Choice Neighborhoods (HUD)** — 9 initial grantees evaluated. Residents saw income/employment gains; neighborhood-level attribution harder.
- **Promise Neighborhoods (federal)** — ~20 sites.

### Community land trust / anti-displacement
- **Dudley Street Neighborhood Initiative (Roxbury, Boston)** — the Boston case the client cited. 1984–present. 40+ year CLT. Only US community-led org granted eminent domain by a city (Boston, 1988). 1,300 vacant parcels → near-zero; 226 permanently affordable homes; Cain (MIT 2015) documents materially lower 2008–10 foreclosure rates vs comparable Boston. **Best single match for IMAN's 63rd/Racine corridor + Regenerator CLT logic.**
- **Healthy Neighborhoods Baltimore** — targeted-investment model.
- **East Baltimore Development Inc.** — mixed track record; displacement concerns.

### Violence interruption
- **READI Chicago** — 2017–present RCT (Bhatt/Heller QJE 2024). Primary outcome null but −65% shooting/homicide arrests in full sample, −79% in outreach-referred subgroup. BCR 4:1 to 18:1.
- **Cure Violence Chicago / systematic review 2025** — mixed fidelity; 37–63% reductions where fidelity high, null elsewhere.
- **Oakland Ceasefire** — peer city GVI.

### Vacant-lot greening
- **Philadelphia LandCare** — Branas 2018 RCT + 2007–2023 DiD (Asa AJPH 2026): −56.6 aggravated-assaults per sq mi per year (95% CI −97.9 to −15.2); −30% aggravated assault overall, −31% firearm aggravated assault, −15% firearm violent crime.

### Healthcare hotspotting / integrated care
- **Camden Coalition Hotspotting** — Finkelstein NEJM 2020 RCT: null on hospital readmission. Informs IMAN on what NOT to scale absent care-navigation enhancement.
- **Pathways Community HUB (Akron)** — CHW coordination model; multiple observational positive signals.
- **Bronx Health REACH** — faith-based SDOH.

### Cash-transfer / financial inclusion
- **Magnolia Community Initiative (LA)** — cross-sector place-based coordination.
- **Jeremiah Program** — single-mother two-gen housing + ed.
- **Mission Asset Fund** — lending circles; financial inclusion as SDOH lever.

### Economic development / public investment
- **Atlanta BeltLine / Westside Future Fund** — corridor-scale anti-displacement pilot.
- **Greater University Circle, Cleveland** — anchor-institution model.
- **Detroit Michigan Central / Future City** — corridor revitalization.
- **North Hartford Promise Zone** — federal PZ case.
- **New Orleans Redevelopment Authority** — blight disposition model.
- **East End Transformation, Richmond** — HUD CN.
- **Watts Rising / Jordan Downs** — HUD CN South LA.
- **Skid Row Housing Trust** — Housing First at scale.

### IMAN-specific prior art
- **Choice Neighborhoods (HUD)** — framework for IMAN's planning.
- **Cure Violence Chicago** — local antecedent to IMAN's CVI work.

**Most actionable benchmarks for IMAN:**
1. **Dudley Street** (CLT legal structure for 63rd/Racine corridor — avoids East Lake displacement outcome).
2. **Philadelphia LandCare** (vacant-lot greening pre-requisite for the walkable-corridor mechanism).
3. **READI Chicago** (CVI cost-effectiveness anchor; IMAN can cite as co-flagship Chicago evidence).
4. **Purpose Built East Lake** (infrastructure anchor concept + documented displacement cautionary tale).
5. **Hager et al. MA Flex Services 2025** (not a place-based project but the Medicaid-financing blueprint IMAN wants IL to copy).

---

## Part 5 — The Little Village comparison (investor opener)

See [positive_deviants/little-village-chicago.md](../positive_deviants/little-village-chicago.md) and [positive_deviants/01_investor_onepager.md](../positive_deviants/01_investor_onepager.md).

Core numbers: Englewood (CA 68) LE 67.7 yrs (CDPH 2023); Little Village / South Lawndale (CA 30) LE ~82 yrs. Same city, same CDPH pipeline, comparable poverty (Little Village bottom-quartile median HH income, USDA LILATracts flag, pre-1940 housing). Crude gap: ~14 years. After Palloni & Arias salmon-bias adjustment: 9–11 years. Four structural features (walkable 26th St corridor; Our Lady of Tepeyac faith-health-social; multi-generational households above Chicago average; small-business mercado economy) explain most of the gap. Sampson collective-efficacy scores in South Lawndale substantially exceed Englewood's.

**Investor-deck version: [02_investor_onepager.md](02_investor_onepager.md).**

---

## Part 6 — The Dudley Street case

See [similar_projects/dudley_street_neighborhood_initiative.md](../similar_projects/dudley_street_neighborhood_initiative.md). The Boston case the client recalled.

**Setting at 1984 baseline:** Roxbury + North Dorchester, Boston. ~24,000 residents, majority Black and Cape Verdean/Latino. 30% of land (1,300+ parcels) vacant after decades of arson and disinvestment. Poverty rate ~32%. Median HH income ~$15k (1980 dollars). Directly Englewood-analogous on race, vacancy, disinvestment, poverty.

**Mechanism.** Resident-controlled planning via the 1987 Declaration of Community Rights; community land trust chartered 1988; **the only community-led organization in US history to be granted eminent-domain authority by a city** (Boston Redevelopment Authority, 1988); development-without-displacement framework; 226 permanently affordable homes under CLT stewardship (ground lease ~$49/month); plus urban farm, greenhouse, commercial buildings, parks, youth and organizing programs.

**Evidence.** Case-study and thesis literature — not RCT. Most rigorous independent analysis: Cain (MIT 2015). Documented: 1,300 parcels vacant → near-zero; CLT-stewarded homes foreclosed at materially lower rates during 2008–10 than comparable Boston nbhds; majority-minority demographics maintained; lower displacement than citywide for 2010–2020.

**Transferability to IMAN.** Strongest single match for IMAN's Go Green Development Group / 63rd-and-Racine corridor plus Regenerator logic. CLT ground-lease structure is the anti-displacement lever Purpose Built East Lake lacked. DSNI's resident-majority board is a direct model for IMAN's community engagement governance.

---

## Data gaps for the next research cycle

1. Tract-level USALEEP download for Cook County tracts in community areas 66 and 68 (CDC Data.gov).
2. Chicago Health Atlas direct-scrape (403'd during this research session) — need full community-area indicator file.
3. Chicago Lawn 2023 CDPH LE — not on public priority list.
4. Tract-level enumeration inside the 16 client-named communities (Gary specific tracts, Memphis specific tracts, etc.) — required for the Layer-2 synthetic-control donor pool.
5. Positive-deviant LE values for NYC neighborhoods currently verified via search-result excerpting — direct NYC DOHMH PDF pull recommended.
6. Boston BPHC direct PDF pull for East Boston LE (we cited WBUR summary; binary PDF rendered unreadably in research session).
