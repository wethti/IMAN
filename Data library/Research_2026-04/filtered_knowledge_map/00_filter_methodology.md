# Filter Methodology — Sub-Knowledge-Map for Englewood-like Neighborhoods

**Stream G, 2026-04-21**
**Author:** Claude (Opus 4.7)

## Purpose
Build a disciplined subset of the main Knowledge Map (~250 PDFs across 9 domains) limited to studies whose populations, settings, or mechanisms plausibly apply to Englewood-like neighborhoods: low-income, majority-Black, Rust Belt disinvestment or Jim Crow South analog, renter-dominated, urban form with disinvested retail corridors.

## Authoritative peer pool
See `c:/Users/piggl/Documents/IMAN/Data library/Research_2026-04/peer_neighborhoods/01_client_canonical_list.md`. The client's 16 canonical peer communities are:

- **Midwest (strongest match):** Gary IN, East St. Louis IL, Flint MI, Youngstown OH, Toledo OH, Rockford IL, South Bend IN
- **Large city low-income neighborhoods:** South Side Chicago, West Side Detroit, North Side Milwaukee, West Side Cleveland
- **South / Sunbelt:** Memphis TN, Birmingham AL, Jackson MS, Shreveport LA

## The 9-criterion similarity rubric (client, from `01_client_canonical_list.md`)

1. Income: median HH income $25k–$40k; wealth index <50
2. Housing: renter share >=60%; ownership <=40%; median home value <$200k
3. Employment: industrial/manufacturing/service/retail/logistics; limited white-collar
4. Consumer behavior: discount retailer preference, SNAP/EBT usage, price sensitivity
5. Demographics: median age 30–40; college <30%; HH size 2–3
6. Urban form: moderate density; mixed residential + small retail corridors; walkability
7. Economic growth: population growth -1% to +1%; limited new development
8. Affordability pressure: housing affordability index <80
9. Diversity & language: primarily English-speaking; 10–20% Spanish

7–9 = strong match, 5–6 = moderate, <5 = weak. Studies are retained if their study population plausibly scores 5+.

## Retention rules

**Retain (Tier 1 — RCT / quasi-experiment / systematic review with causal ID):**
- Population is US low-income urban, majority Black or majority-minority
- Setting is in a canonical peer community or structurally equivalent
- Systematic review whose at-least-one sub-analysis covers low-income US urban populations

**Retain (Tier 2 — good observational):**
- Stratified by poverty / urbanicity / race in a US context
- Covers a Rust Belt or Jim Crow South historical setting
- Mechanism replicates a peer-setting pathway (e.g., segregation → mortality, redlining → environmental exposure)

**Retain (Tier 3 — descriptive / foundational):**
- Foundational theory papers that frame the mechanism (Link & Phelan, Geronimus, Krieger, Massey, Braveman)
- Descriptive epidemiology of US Black health or segregation effects

**Retain with transferability caveat:**
- RCTs from non-peer settings whose mechanism should generalize: Brazil Bolsa Família → EITC analog; Canadian Mincome → BIG; Finland North Karelia → integrated primary care; Barcelona superblocks → placemaking; Mexico SSB tax → pricing channel.
- These are tagged `[TRANSFERABILITY CAVEAT]` and retained so the researcher sees the mechanism and can judge transfer.

**Retain national studies if they stratify:**
- Chetty income–LE (stratifies by income percentile and urban/rural): retain.
- Pope PM2.5 → LE (US national, but Englewood is in the highest-exposure quartile): retain.
- National SNAP / EITC / WIC evaluations: retain (Englewood households are precisely the eligible population).

**Retain historical studies if:**
- Setting is Rust Belt industrial decline OR Jim Crow South OR redlining-era urban America. Both histories are encoded in the canonical peer pool.

## Exclusion rules

**Exclude outright:**
- Wealthy-country general-population studies with no low-income or minority subgroup analysis
- Biomedical / bench papers about disease mechanisms with no neighborhood policy lever (e.g., HPA axis molecular biology, oxidative stress chemistry, creatine supplementation, CKD molecular mechanisms)
- Rural-only studies from non-peer settings (rural Brazil, rural Finland — unless mechanism is retained under caveat above)
- Disease-specific clinical studies (e.g., eosinophilic GI disease, UC vs Crohn's phenotyping) with no SDOH frame
- Studies whose population or setting cannot be determined from `evidence_base.md` AND filename context — tagged `[POPULATION UNKNOWN — retrieve full PDF]` and excluded pending retrieval

## Systematic-review handling

Default rule: retain a systematic review if at least one of its included studies covers low-income US urban populations OR if its mechanism is explicitly SDOH-relevant. Examples:
- Twohig-Bennett & Jones greenspace meta (103 studies, includes US urban): retain
- Ransford Cure Violence review (Baltimore, Chicago, NYC sites): retain
- Berg Housing First review (includes US inner-city RCTs): retain
- Teng SSB-tax review (multi-country): retain with caveat (mechanism is pricing, applies to SNAP-based price interventions)

## Handling "Unknown Author" entries

Several files in the Knowledge Map have author-unknown metadata. Where `evidence_base.md` identifies the content and population, retain. Where neither filename nor evidence_base yields a clear population, tag `[POPULATION UNKNOWN — retrieve full PDF]`.

## Expected retention rate

The brief anticipates ~40–60% retention. Corpus-wide discipline check:
- If retention exceeds 80%, the filter is too loose — likely retaining biomedical papers that don't inform neighborhood policy.
- If retention drops below 20%, the filter is too tight — likely dropping transferability-caveat studies that the researcher needs.

## Reproducibility

A second analyst applying this methodology to the same `evidence_base.md` summaries should reach ~90% agreement on retain/exclude decisions. Ambiguous cases are flagged in each `<domain>_filtered.md` under a "Borderline retains" section with 1–2 lines of reasoning.

## Anti-hallucination

- Every retained study points to a real file path confirmed via directory listing.
- Every effect size is quoted verbatim from `evidence_base.md` — no rounding, rescaling, or reinterpretation.
- Where `evidence_base.md` gives a range (e.g., "30–60%"), the range is preserved verbatim.
- Every retained study is logged in `c:/Users/piggl/Documents/IMAN/Data library/Research_2026-04/verification/claims_stream_G.csv`.
