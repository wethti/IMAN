# Measurement Plan — How We Will Know Whether It's Working
**Audience:** client analytics lead / IMAN evaluation staff | **Length:** ~15 minutes

## Core design choice
We will not run a single evaluation. We will run three nested layers:

1. **Proxy-outcome quarterly dashboard** (short horizon, high signal-to-noise)
2. **Synthetic-control difference-in-differences vs peer pool** (medium horizon, medium confidence)
3. **Long-run LE residual analysis vs USALEEP-successor tract-level LE release** (long horizon, ambiguous attribution)

Each layer answers a different question. Each layer has a different audience.

## Layer 1 — Proxy quarterly dashboard
[POPULATED FROM STREAM A]: For each of the ~40 initiatives, the measurable proxy, the data source, the cadence, and the minimum detectable effect.

## Layer 2 — Synthetic control
[POPULATED FROM STREAM C + A]: Pool A is the donor pool; Englewood/Chicago Lawn is the treated unit. For each treatment (capital project opening, program launch), we construct a counterfactual Englewood trajectory from a weighted combination of peer tracts. Effect = treated − counterfactual.

## Layer 3 — Long-run LE residual
[POPULATED FROM STREAM E]: When USALEEP's successor release becomes available, we compare Englewood's LE residual (actual − predicted from demographics) at baseline vs post-period. Plus we benchmark against Pool B's positive-deviant residuals.

## Governance
- Quarterly data pull + dashboard update: IMAN data team
- Annual synthetic-control refresh: consulting team
- Red-team review: an outside epidemiologist / evaluation expert on each annual release
- All raw outputs posted to an internal data portal with provenance

## Data quality traps
[POPULATED FROM STREAM B]: suppression thresholds at census-tract scale, geographic cross-walks pre/post 2020 boundary changes, reporting-delay issues in mortality data.
