# Handoff Memo — 2026-04-21 Overnight Research Run
**Author:** Claude Opus 4.7 | **Date:** 2026-04-21 | **For:** dpo120000@gmail.com

## What shipped

The 5 client- and investor-facing deliverables are populated:
- [01_executive_brief.md](01_executive_brief.md)
- [02_investor_onepager.md](02_investor_onepager.md)
- [03_measurement_plan.md](03_measurement_plan.md)
- [04_peer_and_positive_deviant_atlas.md](04_peer_and_positive_deviant_atlas.md)
- [05_appendix_evidence_tables.md](05_appendix_evidence_tables.md)

Underlying research artifacts (use as source material):
- [../peer_neighborhoods/](../peer_neighborhoods/) — baseline + client canonical peer list + Pool A tract drill-down
- [../datasets/](../datasets/) — top-10 priority datasets + 40+ catalog + access playbook
- [../initiative_evaluation/](../initiative_evaluation/) — 9 domain memos, ~40 programs
- [../similar_projects/](../similar_projects/) — 25 project profiles
- [../positive_deviants/](../positive_deviants/) — 12 profiles + method + investor one-pager + synthesis
- [../new_literature/](../new_literature/) — 9 domain files + top-20 ranked list
- [../verification/claims_log.csv](../verification/claims_log.csv) — 234 verified numeric claims

## What didn't finish

### Rate limit hit at ~8pm Central 2026-04-21

Two background agents (Stream D similar-projects claim-log back-fill; Stream G filtered knowledge map) were interrupted by the daily usage limit. Limit resets 8pm Central.

### Stream G — filtered Knowledge Map is partial

Complete domains in [../filtered_knowledge_map/](../filtered_knowledge_map/):
- `00_filter_methodology.md` — full methodology
- `healthcare_filtered.md` + `healthcare_excluded.md`
- `food_access_filtered.md` + `food_access_excluded.md`
- `housing_filtered.md` (excluded file not yet written)

Pending domains:
- Education & Youth Development (filtered + excluded)
- Funding (filtered + excluded)
- IMAN initiatives (filtered + excluded)
- Mobility / Transit (filtered + excluded)
- Other city projects (filtered + excluded)
- Recreation + Community (filtered + excluded)
- `housing_excluded.md` back-fill

Source corpora are all available at `c:/Users/piggl/Documents/IMAN/Data library/Knowledge Map/` with each domain subfolder having an `evidence_base.md` summary. The filter methodology applies mechanically once budget resets.

### Stream D — claim log back-fill

[../verification/claims_stream_D.csv](../verification/claims_stream_D.csv) is header-only. The 25 similar-project profiles cite sources inline, but ~150 numeric claims are not yet formally logged into the claims CSV. One agent-run will resolve this.

## Known data gaps (flagged in deliverables)

1. **Chicago Health Atlas** — the CDPH download portal returned HTTP 403 during research. Needs a direct human pull for the Englewood / West Englewood / Chicago Lawn community-area indicator file.
2. **Chicago Lawn LE (CA 66)** — not on CDPH 2023 priority list. Best available estimate (72–75) is bounded inference, not a direct CDPH figure.
3. **Tract-level USALEEP** for Cook County tracts in CA 66 and CA 68 — identified source (CDC Data.gov) but not pulled.
4. **Tract-level enumeration inside client's 16 named communities** — e.g., "South Side Chicago" needs to be resolved to CAs 67/68/69/71/49, "West Detroit" to named tracts, Memphis/Birmingham/Jackson/Shreveport similarly. Required for Layer-2 synthetic-control donor pool.
5. **NYC DOHMH Community Health Profiles** for MN03, MN12, BK07, QN3 — LE figures currently verified via search-result excerpting rather than direct PDF extraction.
6. **Boston BPHC East Boston LE** — binary PDF rendered unreadably in research session. Currently cited via WBUR summary.

## Verification flags that need a second pass

Search [../verification/claims_log.csv](../verification/claims_log.csv) for:
- `[UNVERIFIED]` — figures bounded by inference
- `needs_verification` status rows (mostly Stream A claims derived from `evidence_base.md` rather than direct source)
- `verified_secondary` status rows (Wikipedia-based demographics that should be re-verified against ACS API)

## What to do when budget resets

Priority order (highest leverage first):

1. **Chicago Health Atlas pull** (direct download, no scrape needed once the 403 clears). This unblocks Chicago Lawn LE, CA-level indicator benchmarking, and the first row of the quarterly dashboard. ~1 hour of analyst time.
2. **Stream D claim-log back-fill**. Run one agent to extract numeric claims from the 25 `similar_projects/*.md` files into `claims_stream_D.csv`. ~1 agent-run.
3. **Stream G remaining 6 domains**. Apply `00_filter_methodology.md` to the 6 unfinished domain `evidence_base.md` files. Can be split across 2–3 agent runs.
4. **NYC / Boston PDF direct pulls** for the positive-deviant LE figures. Human browser fetches to `positive_deviants/_raw_pdfs/`, then update citations from "secondary" to "primary."
5. **Tract enumeration** inside the 16 client-named communities. Needs ACS + USALEEP merge; one analyst session with census API.
6. **First PLACES dashboard pull** for the IMAN service-area tracts benchmarked against the 16 client-named peer communities — Q3 2026 milestone per [03_measurement_plan.md](03_measurement_plan.md).

## Framing that's safe to repeat in client / investor meetings now

- Englewood LE 67.7 yrs (CDPH 2023); Chicago citywide 78.7 yrs. Gap 10.6–15 yrs to other racial groups.
- Little Village ~82 yrs, same city, same CDPH pipeline. Crude gap 14 yrs. After Palloni & Arias salmon-bias adjustment, 9–11 yrs. **That adjustment matters — do not cite the 14-year headline without it.**
- Conservative LE gain at full IMAN build-out: **3–5 years over 10–15 years in a majority-Black context**, not the 7–10 seen in first-generation Latino/Asian immigrant enclaves. Do not overclaim.
- Generic Produce Rx without clinical wraparound: cite Doyle 2024 null + Drake 2026 +0.20 pp HbA1c *worse*. IMAN should NOT scale generic produce Rx.
- Anchor evidence for investor headlines: Sommers NEJM (Medicaid), Victor NEJM (barbershop BP), Deng Health Affairs (MTM), Bhatt QJE (READI), Asa AJPH 2026 (Philly LandCare), Graetz SSM (eviction mortality).

## Framing that needs a second verification pass before external use

- "14 more years of life expectancy" for Little Village — verify the exact CDPH figure for CA 30. The 2018 Chicago Magazine article cited 82 yrs; the 2023 CDPH brief is the authoritative current source.
- Chicago Lawn LE bounded estimate (72–75) — needs direct CDPH figure.
- USALEEP tract-level LE for CA 66 and CA 68 — the 62–67 range should be verified tract-by-tract from the CDC file.
- Any tract-level claim citing Wikipedia — re-verify against ACS API.
