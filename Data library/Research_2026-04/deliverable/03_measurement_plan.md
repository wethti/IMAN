# Measurement Plan — How We Will Know Whether It's Working
**Audience:** IMAN analytics lead / consulting client evaluation staff | **Length:** ~15 min
**Supersedes:** `03_measurement_plan.TEMPLATE.md`

## Core design choice: three nested layers

We will not run a single evaluation. Life expectancy is the wrong primary outcome on a 3-year horizon (latency, power, confounding, right-censoring — see [initiative_evaluation/A0_cross_cutting_methodology.md](../initiative_evaluation/A0_cross_cutting_methodology.md) §1). We run three layers, each answering a different question for a different audience:

| Layer | Horizon | Question | Audience | Confidence |
|---|---|---|---|---|
| 1. Proxy-outcome quarterly dashboard | 0–5 yr | Are the upstream determinants moving? | Client / board | High on each indicator, weak attribution to IMAN |
| 2. Synthetic-control DiD vs client peer pool | 3–7 yr | Is Englewood's trajectory diverging from its 16-community peer pool? | Strategy / funders | Medium, requires parallel-trends demonstration |
| 3. Long-run LE residual | 10–20 yr | Did the LE gap actually close? | Retrospective, historical record | High when data exists (USALEEP-successor); ambiguous attribution |

## Layer 1 — Proxy quarterly dashboard

Per-initiative proxy specifications live in [initiative_evaluation/](../initiative_evaluation/) (9 domain memos covering ~40 programs). Representative anchors:

| Initiative | Proxy outcome | Data source | Cadence | MDE @ 80% power |
|---|---|---|---|---|
| FQHC expansion (HC1) | BP-control rate in adult FQHC panel | HRSA UDS | Quarterly | ~4 pp relative improvement |
| FQHC expansion (HC1) | ACSC ED-visit rate, tract | IL Hospital Association discharges | Annual | ~8% relative drop |
| CHW (HC2) | BP control, CHW-coached vs matched | IMAN EHR | Quarterly | 5 pp gap |
| Medicaid enrollment (HC3) | Tract uninsured rate | SAHIE | Annual | 2 pp |
| Barbershop BP (HC4) | SBP <130 among Black-male participants | IMAN/shop log + FQHC EHR | Quarterly | 13 pp (quarter of Victor ATE) |
| MOUD+Naloxone (HC5) | Overdose mortality per 100k | Cook County ME + CDC WONDER | 3-yr rolling | 20% relative |
| Fresh Market (FA1) | SNAP transactions, fresh-produce share | IMAN POS | Monthly | — (descriptive) |
| Fresh Market (FA1) | Food-insecurity score tract | PLACES modeled | Annual | 3 pp relative |
| Green ReEntry (HO1/IM3) | Employment placement rate | IMAN admin | Monthly | — |
| Green ReEntry housing (HO2) | 3-gen household share | IMAN tenant survey | Annual | — |
| Corner Store (FA2) | Produce SKU count per store | IMAN site audit | Quarterly | — |
| Griot/Plaza/Regenerator (RC1-3) | Corridor foot-traffic | Placer.ai or IMAN camera counts | Monthly | — |
| GVI / READI-style (CP1-2) | Homicide + shooting rate CA 68 | Chicago Data Portal | Monthly | 20% after 2 yr |
| Cure Violence (CP2) | Fidelity score (Skogan instrument) | Internal audit | Annual | — |
| Bus electrification (MT1) | PM2.5 along 63rd | AirNow + IMAN sensors | Continuous | — |
| Organizing (CC1) | Collective efficacy, PHDCN items | IMAN-commissioned community survey | 3-yr | 0.3 SD |

Dashboard governance: IMAN data team owns the quarterly pull and the public dashboard. Consulting team owns the annual synthesis memo. A named external epidemiologist reviews each annual release before publication.

## Layer 2 — Synthetic control vs 16-community peer pool

**Treated unit.** Englewood (CA 68). Chicago Lawn (CA 66) as secondary treated unit with the Hispanic-majority composition caveat noted in [peer_neighborhoods/01_iman_baseline.md](../peer_neighborhoods/01_iman_baseline.md).

**Donor pool.** The client's 16 canonical peer communities ([peer_neighborhoods/01_client_canonical_list.md](../peer_neighborhoods/01_client_canonical_list.md)) — Gary, East St. Louis, Flint, Youngstown, Toledo, Rockford, South Bend, South Side Chicago (ex-CA 68), West Side Detroit, North Milwaukee, West Cleveland, Memphis, Birmingham, Jackson MS, Shreveport. Each name resolved to specific census tracts via Stream C's tract drill-down ([peer_neighborhoods/02_pool_A_matched.md](../peer_neighborhoods/02_pool_A_matched.md)).

**Covariates for weight fitting.** Pre-intervention outcome trajectory (2015–2024 where available), plus: poverty rate, % Black, median HH income, housing-vacancy rate, violent-incident rate, baseline LE, HOLC-D share.

**Outcomes.** Per initiative or per bundle: ACSC-ED rate (tract), homicide rate per 100k, food-insecurity score, uninsured rate, mortality-amenable-to-healthcare rate, YPLL-75.

**Post-treatment estimator.** Gap between Englewood observed and synthetic Englewood, cumulated over 24–60 months.

**Inference.** Placebo permutations across donor pool (Abadie-Diamond-Hainmueller); rank-based p-value. Also block-bootstrap 90% prediction intervals. For rare-event outcomes (homicides) aggregate to quarters and use Poisson SCM variant.

**First credible estimate.** Late 2028 for programs fully launched by end of 2025 (need 2–3 years of post-treatment observation).

**Failure modes.**
- Donor pool shrinks after excluding peers that implemented comparable programs → fall back to DiD with best 5 matches.
- Pre-period trajectory does not stabilize → rule out SCM for this outcome.
- Cross-state data heterogeneity in the donor pool (Rust Belt vs Sunbelt) → stratify weights by region.

## Layer 3 — Long-run LE residual

When USALEEP's successor release becomes available (target: ~2030 covering 2020–2025 deaths), compare Englewood's LE residual (actual LE − predicted from poverty + % Black + % uninsured + unemployment + vacant-lot rate) at baseline (2010–2015) vs post-period (2020–2025). Benchmark against:
- The residuals of the client's 16 peer communities (expected: similar to Englewood baseline)
- The positive-deviant set from [positive_deviants/](../positive_deviants/) (expected: residuals of +3 to +10 years)
- Little Village (CA 30) specifically, since CDPH pipeline makes the Chicago-internal comparison cleanest

## Data quality traps (from Stream B)

- **USALEEP latency.** 2010–2015 data. Cannot serve as outcome for post-2015 programs. Triangulate with CDC WONDER cause-specific mortality.
- **Tract-boundary changes.** 2020 tract definitions differ from 2010. Apply NHGIS crosswalks for any pre/post 2020 time series.
- **PLACES model-based estimates.** Not direct measurements. Credible intervals are wide at tract level. Cannot detect tract-level *change* from a tract-level intervention within ~3 years.
- **PLACES 2024 geography switch.** 2024+ releases use 2020 tracts, earlier releases use 2010. Crosswalk required.
- **Chicago Data Portal homicide coding.** IUCR → NIBRS transition; re-map codes before time series.
- **HMDA schema change.** 2018+ records use expanded fields; pre-2018 uses different schema.
- **UDS definition change.** HTN/DM control definitions changed 2017 and 2022. Re-baseline time series.
- **EPA EJScreen removed 5 Feb 2025.** Use PEDP or Harvard Dataverse mirror; document provenance.
- **Chicago Health Atlas 403'd during this research.** Needs direct human pull from download portal.
- **ACS margins of error.** Tract-level MOE ±$5K–$10K for median income. Always display MOE; avoid ranking tracts by small differences.

## Governance

- **Quarterly.** Data team pulls PLACES, ACS, Chicago Data Portal, IMAN EHR/UDS/POS into the dashboard; publishes update within 30 days of quarter close.
- **Annual.** Consulting team publishes the synthesis memo with per-initiative effect estimates.
- **Annual external review.** Named outside epidemiologist (candidates: someone from the NYU Urban Health Lab, UChicago Crime Lab, Drexel Urban Health Collaborative) reviews each annual release.
- **Provenance.** All raw outputs posted to an internal data portal with dataset version, pull date, and analyst ID.
- **Verification discipline.** Every numeric claim in any external deliverable is logged in [verification/claims_log.csv](../verification/claims_log.csv) with source URL before publication.

## Timeline

| Date | Milestone |
|---|---|
| Q3 2026 | Baseline PLACES + CDPH + Chicago Data Portal pull for IMAN service tracts vs 16 peer communities |
| Q4 2026 | First quarterly dashboard v1 live |
| Q1 2027 | Per-initiative proxy scorecard live with all ~40 initiatives |
| Q3 2027 | First DiD estimate vs matched 5-community subset (pre-SCM pilot) |
| Q4 2028 | First full 16-community synthetic-control estimate |
| 2030+ | USALEEP-successor LE residual analysis when federal release available |

## Threats and mitigations

- **Partial implementation.** If a program doesn't scale as planned, its proxy won't move, and investors may blame the measurement. Mitigation: dose-response analysis within Englewood (block-level intensity gradient); report fidelity alongside effect.
- **Confounding spillover.** City-wide policy changes (CDPH initiatives, CPD consent decree) affect Englewood and its peers differently. Mitigation: include Chicago-wide policy change dummies in all SCM.
- **Hawthorne / measurement reactivity.** Survey-based collective-efficacy scores are sensitive to who asks. Mitigation: same instrument, same contractor, 3-year cadence.
- **Positive-deviant transferability.** Hispanic-paradox evidence may overstate what IMAN can achieve in majority-Black Englewood. Mitigation: conservatively project 3–5 yr LE gain, not 7–10.
