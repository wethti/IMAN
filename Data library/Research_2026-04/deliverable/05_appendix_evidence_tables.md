# Appendix — Evidence Tables
**Audience:** due-diligence reviewers, researchers | **Format:** reference tables
**Supersedes:** `05_appendix_evidence_tables.TEMPLATE.md`

These tables consolidate the verified evidence base. Every numeric claim in the other deliverable files traces back to one of these rows.

---

## Table 1 — Initiative × Evidence Tier

Rows compiled from [initiative_evaluation/A1_healthcare.md](../initiative_evaluation/A1_healthcare.md) through A9 and cross-walked to [new_literature/](../new_literature/). Expected-LE column reproduces the decision-tree estimate; evidence column names the strongest published anchor.

| Domain | Initiative | Expected LE gain | Strongest evidence anchor | Tier | Identification strategy IMAN will use |
|---|---|---|---|---|---|
| Healthcare | FQHC Expansion (HC1) | ~1.5 yr | Sommers NEJM 2012 (−6.1% near-poor mortality in Medicaid expansion states) | 1 (quasi-exp) | Staggered DiD + SCM on BP-control & ACSC-ED |
| Healthcare | CHW Programs (HC2) | ~1.0 yr | Macinko Brazil Family Health; Van Iseghem 2026 CHW cost-effective in 70% of 50 studies, $3,967 median cost/QALY | 1 (systematic review) | Individual DiD + borrowed effect |
| Healthcare | Medicaid Enrollment (HC3) | ~0.7 yr | Sommers NEJM 2012 (6.1% reduction) | 1 | Borrowed effect size × throughput |
| Healthcare | Barbershop BP (HC4) | ~0.6 yr | Victor NEJM 2018 (+52 pp BP-control ATE) | 1 (RCT) | Direct replication; cluster-wait-list randomize if possible |
| Healthcare | MOUD + Naloxone (HC5) | ~0.8 yr | Walley BMJ 2013 (−46% community overdose mortality); Fischer BMC Pub Health 2025 (98.3% PWUD-administered naloxone survival) | 1 | Pre/post + ITS |
| Healthcare | Cancer screening (HC6) | ~0.3 yr | Sommers / general screening RCT literature | 2 | Panel-level UDS |
| Food | Fresh Market (FA1) | ~0.8 yr | Deng/Mozaffarian Health Affairs 2025 MTM (−47% hosp., 19.7% cost savings, net-saving 49/50 states) | 1 (meta-analysis modeled to 50 states) | DiD on food-insecurity + ACSC |
| Food | Corner Store Campaign (FA2) | ~0.4 yr | Multiple NYC/Philly healthy-corner-store quasi-experiments | 2 | Block-level intensity gradient |
| Food | Fresh Boost / food-is-medicine (FA3) | ~0.4 yr | Hager Health Affairs 2025 MA Flex Services (−23% hosp., −13% ED, −$1,721/member); Doyle JAMA Intern Med 2024 null on HbA1c; Drake JAMA Intern Med 2026 Produce Rx +0.20 pp HbA1c *worse* | 1 mixed | Design with clinical wraparound; do not scale generic produce Rx |
| Food | Oasis Café (FA4) | ~0.2 yr | Café / shared-kitchen workforce-social enterprise literature | 3 | Case study |
| Housing | Permanent supportive housing / Regenerator (HO1) | ~1.0 yr | Housing First RCT literature; Hager 2025 MA Flex housing supports | 1 | Pre/post + borrowed effect |
| Housing | Eviction prevention (HO2) | ~0.8 yr | Graetz Soc Sci Med 2024 (eviction judgment → 40% higher mortality, 95% CI 36–43%) | 1 (quasi-exp, 38M records) | Eviction Lab tract-level DiD |
| Housing | Green ReEntry rehab (HO3) | ~0.5 yr | Philadelphia LandCare + Dudley CLT foreclosure evidence | 2 | Dose-response + synthetic control |
| Housing | CLT / anti-displacement (HO4) | ~0.4 yr | Arcaya J Urban Health 2023 (5 mechanisms linking CLT to health) | 3 (qualitative) | Descriptive |
| Housing | Housing mobility / CMTO (HO5) | ~1.0 yr to mover | Bergman/Chetty AER 2024 CMTO (15%→53% moves to high-opportunity tract) | 1 (RCT) | Borrowed effect |
| Violence | GVI / CP1 | ~1.5 yr | Braga meta; Oakland Ceasefire | 2 | DiD with matched city |
| Violence | READI / CVI (CP2) | ~1.2 yr | Bhatt/Heller QJE 2024 (−65% shooting/homicide arrests; −79% in outreach subgroup; BCR 4:1 to 18:1) | 1 (RCT) | Already RCT-anchored |
| Violence | Cure Violence | ~0.8 yr | Cure Violence systematic review 2025 (37–63% reductions where fidelity high; null elsewhere) | 1 (systematic review) | ITS with fidelity monitoring |
| Violence | Vacant-lot greening (CP3) | ~0.6 yr | Asa AJPH 2026 DiD 2007–2023 (−56.6 agg. assaults/sq mi/yr, 95% CI −97.9 to −15.2; −30% overall) | 1 (quasi-exp) | Borrowed effect + city-scale replication |
| Education | Early childhood (ED1) | ~1.0 yr (long-run) | HighScope / CPC; Aizer NBER 2024 CTC child outcomes | 1 | Cohort tracking |
| Education | NFP home visiting (ED2) | ~0.5 yr (long-run) | Olds NFP RCT | 1 | Borrowed effect |
| Mobility | Green Line / bus electrification (MT1) | ~0.3 yr | EPA RIA 2024 PM2.5 NAAQS (up to 4,500 deaths/yr prevented, $46B net health benefit by 2032); Pope PM2.5 LE | 1 | Pre/post PM2.5 + mortality |
| Mobility | Transit access (MT2) | ~0.2 yr | Chetty Opportunity Atlas | 2 | Distance-based IV |
| Community | Griot Plaza + green space (RC1) | ~0.4 yr | Liu 2024 meta (greenspace → depression OR 0.89, 95% CI 0.86–0.93); Greene 2024 urban canopy −1.0°C summer temps | 1 | Pre/post proxies |
| Community | Regenerator (RC2) | ~0.3 yr | Community-center literature | 3 | Descriptive + dose |
| Community | Organizing / collective efficacy (RC3) | ~0.5 yr | Sampson Science 1997 (+2 SD collective efficacy → −40% homicide) | 1 | PHDCN-instrument 3-yr resurvey |
| Funding | Medicaid 1115 / Flex Services (FU1) | mechanism | Hager Health Affairs 2025 MA; Van Vleet NC Med J 2024 (NC HOPilots: 265k services to 20k enrollees, $85/enrollee/month savings) | 1 | IL 1115 advocacy anchor |
| Funding | Cash transfer / UBI (FU2) | mixed | Vivalt NBER 32719 (−4.1 pp LFP, −1-2 hrs/wk); Bartik NBER 32784 (+$300/mo HH spending); West SEED J Urban Health 2023 (Kessler-10 −2.9, P=.027); Hamad Health Affairs 2023 CTC adult mental health | 1 | Borrowed |
| Funding | CVI Medicaid reimbursement (FU3) | — | Strange INQUIRY 2025 + Multi-state H&J 2025 | 2 | Policy advocacy |

---

## Table 2 — Dataset × Use Case

Condensed from [datasets/top10_priority.md](../datasets/top10_priority.md) and [datasets/catalog.csv](../datasets/catalog.csv). Full 40+ dataset catalog in the CSV.

| Tier | Dataset | Geo | Temporal | IMAN use case |
|---|---|---|---|---|
| 1 | CDC PLACES (tract) | census tract | BRFSS 2022 + ACS 2018–2022 | Primary dashboard input: diabetes, obesity, hypertension, mental distress, smoking |
| 1 | USALEEP | census tract | 2010–2015 | Canonical LE gap; positive-deviant regression |
| 1 | Chicago Health Atlas | CA 77 + ZIP + tract | 2013–2024 | Fastest Englewood / Chicago Lawn vs city comparison; 160+ indicators |
| 1 | USDA Food Access Research Atlas | tract | 2010/2015/2019 | LILATracts flag; food-desert precondition |
| 1 | EPA EJScreen (PEDP / Harvard mirror) | block group | 2015–2023 | PM2.5, traffic proximity, respiratory hazard — MT1 evidence anchor |
| 1 | ACS 5-year (2020–2024) | tract | Dec 2025 release | Workhorse denominator |
| 1 | Chicago Data Portal Crime | block-masked | 2001–present | CP1/CP2/IM3 evaluation |
| 1 | HRSA UDS | health center | 2010–2024 | IMAN Health Clinic benchmark |
| 2 | HMDA | tract-geocoded | 2007–2025 | Structural-disinvestment narrative |
| 2 | Mapping Inequality (HOLC) | polygon | 1935–1940 | Redlining matching variable |
| 2 | CDC WONDER | county (+ ZIP via dashboards) | 1999–present | Cause-specific mortality; USALEEP triangulation |
| 2 | SAHIE | county | 2008–2023 | Uninsured time series |
| 2 | Eviction Lab | tract | 2000–2018 (national) | HO2 eviction-prevention pathway |
| 2 | Opportunity Atlas | tract | cohorts born 1978–1983 | Intergenerational-mobility benchmark (updated 2026 release) |
| 2 | NaNDA (ICPSR) | tract / ZCTA | multi-vintage | Pre-built neighborhood measures |
| 2 | SNAP retailer data (USDA) | retailer | monthly | Fresh Market + corner store tracking |
| 3 | County Health Rankings | county | annual (2026 skipped) | Peer-city benchmark for investor |
| 3 | CTA ridership by station | station | monthly | Green Line reopening impact |
| 3 | Cook County Assessor parcel | parcel | annual | Vacant-lot analysis |

**EPA EJScreen note (2025-02-05 removal).** Use PEDP mirror (https://pedp-ejscreen.azurewebsites.net) or Harvard Dataverse archive. Document provenance in any deliverable.

---

## Table 3 — Project benchmarks (25 profiles)

Full profiles in [similar_projects/](../similar_projects/). Key outcomes surfaced:

| Project | Years | Tier | Headline outcome | Transferability note |
|---|---|---|---|---|
| Purpose Built East Lake | 1995– | 2 | Crime −90%; employment 13%→70%+; Drew Charter ~98% graduation | **Only 16% of original public-housing families returned; Black pop. fell 22% — displacement caveat** |
| Dudley Street Neighborhood Initiative | 1984– | 2 | 1,300 vacant parcels → ~0; 226 permanently affordable homes under CLT; lower 2008–10 foreclosure rate | **Strongest match for IMAN 63rd/Racine CLT structure** |
| Harlem Children's Zone | 1997– | 2 | Promise Academy grade-level gains | Cradle-to-college pipeline |
| Philadelphia LandCare | 2000– | 1 | Branas 2018 RCT + Asa AJPH 2026 DiD: −30% agg. assault, −31% firearm agg. assault, −15% firearm violent crime | **Direct replicable evidence** |
| READI Chicago | 2017– | 1 | Bhatt QJE 2024: primary outcome null; −65% shooting/homicide arrests; −79% in outreach subgroup; BCR 4:1–18:1 | Chicago co-flagship evidence |
| Cure Violence Chicago | 2000– | 1 (sys review) | 37–63% reductions where fidelity high; null elsewhere | **Pair with fidelity monitoring** |
| Camden Coalition Hotspotting | 2007– | 1 | Finkelstein NEJM 2020 RCT null on readmission | **Do NOT scale absent care-navigation enhancement** |
| Choice Neighborhoods (HUD) | 2010– | 2 | HUD OPDR 2024: residents saw income/employment gains; nbhd-level harder to attribute | Federal program template |
| Promise Neighborhoods (federal) | 2010– | 3 | ~20 sites; mixed | Federal program template |
| Atlanta BeltLine / Westside Future Fund | 2005– | 3 | Corridor-scale anti-displacement pilot | Corridor model |
| Magnolia Community Initiative (LA) | 2008– | 3 | Cross-sector place-based coordination | Governance model |
| Greater University Circle (Cleveland) | 2005– | 2 | Anchor-institution model | Anchor strategy |
| Detroit Michigan Central | 2018– | 3 | Corridor revitalization | Corridor model |
| North Hartford Promise Zone | 2014– | 3 | Federal PZ case | Federal template |
| New Orleans Redevelopment Authority | 2007– | 3 | Blight disposition model | Blight-disposition lever |
| East End Transformation (Richmond) | 2015– | 3 | HUD CN | HUD CN template |
| Watts / Jordan Downs Rising | 2011– | 3 | HUD CN South LA | HUD CN template |
| Oakland Ceasefire | 2012– | 2 | Peer-city GVI | GVI template |
| Skid Row Housing Trust | 1989– | 2 | Housing First at scale | PSH lever |
| Healthy Neighborhoods Baltimore | 2000– | 2 | Targeted-investment model | Investment clustering |
| East Baltimore Development Inc. | 2003– | 3 | Mixed track record; displacement concerns | Cautionary |
| Pathways Community HUB (Akron) | 2002– | 2 | CHW coordination model; observational positive | CHW lever |
| Bronx Health REACH | 2000– | 3 | Faith-based SDOH | Faith-health lever (IMAN peer) |
| Jeremiah Program | 1998– | 3 | Single-mother two-gen housing + ed | Two-gen lever |
| Mission Asset Fund | 2007– | 3 | Lending circles | Financial-inclusion lever |

---

## Table 4 — Positive-deviant mechanism catalog

Full profiles and primary sources: [positive_deviants/](../positive_deviants/) (12 profiles).

| Neighborhood | City | Confirmed LE | Residual (after salmon-bias adj.) | Key mechanism featured |
|---|---|---|---|---|
| Little Village / La Villita (CA 30) | Chicago | ~82 | +7 yrs | **Primary case** — walkable 26th St corridor + faith-health co-location + multi-gen + mercado economy + collective efficacy |
| Washington Heights / Inwood (MN12) | Manhattan | 84.0 | +6 | Dominican enclave + Charles B. Wang CHC analog |
| Sunset Park | Brooklyn | 82.6 | +5 | 8th Ave Chinatown corridor |
| Chinatown / LES (MN03) | Manhattan | 82.2 | +4.5 | Charles B. Wang CHC anchor |
| Jackson Heights (QN3) | Queens | ~83 | +5 | Roosevelt Ave hyper-diverse walkable corridor |
| East Boston + Chelsea | MA | ~78–81 | +4–5 | State MA universal-insurance effect confounds some of the signal |
| Boyle Heights / East LA | LA | ~77–79 | +4 | Cesar Chavez / East LA mercado economy |
| Hialeah | Miami | ~81 | +3–4 | Cuban-American enclave density |
| Starr County TX | rural TX | ~81 | +9–11 but 40–60% salmon-bias artifact | Not a template |
| Cedar-Riverside | Minneapolis | not deviant | — | Instructive failure of naive transfer |
| East Harlem | NYC | not deviant | — | Acculturation-erosion case |
| West Philadelphia (Spring Garden) | Phila | Black-majority; no Hispanic-paradox pattern | — | Transferability caveat |

**7 recurring features (5+ of 8 confirmed):**
1. Walkable retail corridor + fresh food in 10 min
2. Faith institution as health/social-services hub
3. Multigenerational household norm
4. Small-business owner-occupied retail
5. First-generation dietary pattern retained
6. High collective efficacy (Sampson addition — *Science* 1997)
7. Low smoking/alcohol (especially immigrant women)

---

## Table 5 — New literature (2023–2026) additions

Top 20 from [new_literature/00_top20.md](../new_literature/00_top20.md). Full 9-domain collection in the new_literature folder.

| Rank | Paper | Effect size / finding | Tier |
|---|---|---|---|
| 1 | Graetz Soc Sci Med 2024 (rent burden + eviction mortality) | Eviction judgment → +40% mortality (95% CI 36–43%); rent burden +20 pp → +16% mortality. Linked Census → Numident → 38M eviction records. | 1 |
| 2 | Bergman/Chetty AER 2024 (Creating Moves to Opportunity) | Customized housing-search assistance raised share moving to high-opportunity tracts 15% → 53%. | 1 (RCT) |
| 3 | Deng/Mozaffarian Health Affairs 2025 (MTM in 50 states) | −47% hospitalizations (95% CI −36 to −58%); 19.7% cost savings; net-saving in 49/50 states. | 1 (meta + modeling) |
| 4 | Bhatt/Heller QJE 2024 (READI Chicago) | Primary outcome null; −65% shooting/homicide arrests full sample; −79% in outreach-referred subgroup; BCR 4:1 to 18:1. | 1 (RCT) |
| 5 | Hager Health Affairs 2025 (MA Flex Services) | −23% hospitalizations; −13% ED visits; −$1,721/member post-COVID. | 1 (quasi-exp) |
| 6 | Vivalt/Rhodes/Bartik NBER 32719 (UBI employment) | −4.1 pp labor-force participation; −1-2 hrs/week worked; largest US UBI RCT. | 1 (RCT) |
| 7 | Asa AJPH 2026 (Vacant-lot DiD 2007–2023) | −30% aggravated assault; −31% firearm agg. assault; −15% firearm violent crime. Extends Branas 2018. | 1 (quasi-exp) |
| 8 | Doyle/Alsan JAMA Intern Med 2024 (food-as-medicine null) | Adjusted diff on HbA1c −0.10 (95% CI −0.46 to 0.25, P=.57). | 1 (RCT, null) |
| 9 | Drake JAMA Intern Med 2026 (Produce Rx RCT) | HbA1c +0.20 pp *higher* (worse) at 12 mo; only 30% used ≥80% of benefit. | 1 (RCT) |
| 10 | Bartik/Vivalt NBER 32784 (UBI consumption) | +$300/mo HH spending; MPC on non-durables 0.44–0.55. | 1 (RCT) |
| 11 | Van Vleet NC Med J 2024 (NC Healthy Opportunities Pilots) | 265k services to 20k enrollees; $47M reimbursed; $85/enrollee/month savings. | 2 (admin) |
| 12 | Van Iseghem Value in Health 2026 (CHW cost-effective sys review) | 70% of CHW interventions cost-effective; median cost/QALY $3,967 (2024 USD). | 1 (sys review) |
| 13 | Fischer BMC Pub Health 2025 (Naloxone meta) | 98.3% survival when PWUD-administered (95% CI 97.5–98.8%). | 1 (meta) |
| 14 | West & Castro J Urban Health 2023 (Stockton SEED) | Kessler-10 distress 21.3 → 18.4 (P=.027); income volatility 19% vs 26% (P=.039). | 1 (RCT) |
| 15 | Schillok JAMA Psychiatry 2025 (Collaborative Care IPD meta) | 35 datasets, 20k participants; therapeutic-treatment-strategy interaction −0.07 on depression (P<0.001). | 1 (IPD meta) |
| 16 | Hamad Health Affairs 2023 (CTC adult mental health) | Fewer depressive/anxiety symptoms for low-income adults; larger for Black/Hispanic parents. | 1 (quasi-exp) |
| 17 | HUD OPDR 2024 (Choice Neighborhoods) | First 9 grantees: resident income/employment gains; nbhd attribution harder. | 2 |
| 18 | Aizer/Lleras-Muney/Michelmore NBER 2024 (CTC child outcomes) | Short- and long-run child-health gains concentrated in poor children. | 1 |
| 19 | Liu meta 2024 (Green space → psychiatric) | OR 0.89 (95% CI 0.86–0.93) for depression. | 1 (meta) |
| 20 | Cure Violence sys review 2025 | 37–63% reductions where fidelity high; null elsewhere. | 1 (sys review) |

Additional 2023–2026 literature by domain: [new_literature/F1_healthcare.md](../new_literature/F1_healthcare.md) through F9.

---

## Table 6 — Verification trail

Merged from all per-stream verification logs into [verification/claims_log.csv](../verification/claims_log.csv). **234 verified numeric claims** currently in the master log, structured as:

`claim_id, claim_text, source, verifier, status`

Distribution by stream:
- Stream A (initiative evaluation): 92 claims
- Stream B (datasets): 40 claims
- Stream C (peer neighborhoods): 50 claims
- Stream D (similar projects): [CSV empty — profiles cite inline; claim-log back-fill pending, see handoff memo]
- Stream E (positive deviants): 32 claims
- Stream F (new literature): 20 claims

**Verification disciplines applied:**
- Every numeric claim cites DOI or URL
- Effect sizes quoted verbatim from the abstract
- Tier-3 claims (editorial/press-release) flagged and a primary-source replacement noted where possible
- `[UNVERIFIED]` flag on any number where a direct pull could not complete (notably Chicago Health Atlas 403; Boston BPHC binary PDF; several NYC DOHMH PDFs)

**Re-verification priority (next research cycle):**
1. Stream D claims log back-fill from the 25 project profiles (~150 claims to log formally).
2. Chicago Health Atlas direct data pull to verify Chicago Lawn LE + community-area indicators.
3. NYC DOHMH Community Health Profile direct PDF extraction for MN03, MN12, BK07, QN3 (currently verified via search-result excerpting).
4. Boston BPHC direct PDF extraction for East Boston LE (currently via WBUR summary).
5. CDPH community-area-level LE tabulation for CA 66 (Chicago Lawn not on 2023 priority list).
