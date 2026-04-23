# A5 — Mobility & Transit Initiative Evaluation

Cross-ref `A0_cross_cutting_methodology.md`. Claims logged in `verification/claims_stream_A.csv`.

---

## MT1 — PM2.5 Reduction / Bus Electrification (~0.4 yr LE gain) [Source: decision_tree.md]

**Causal mechanism.** Pope et al. NEJM: a 10 µg/m³ reduction in PM2.5 is associated with a 0.61-year LE gain [evidence_base.md Mobility]. Englewood is near high-traffic corridors and has legacy redlining-driven air-quality disparity [Lane et al., evidence_base.md Mobility]. Pathway: lower PM2.5 → reduced CVD + respiratory mortality → LE.

**Proxy outcome (2-5 yr).** (a) Annual-mean PM2.5 at EPA EJScreen / Chicago monitors covering Englewood. (b) CTA bus fleet electrification share on routes through CA 68/66. (c) Asthma ED-visit rate for children (IHA).

**Identification strategy.** Direct Pope elasticity applied to observed PM2.5 delta. ITS on monitor readings pre/post electrification milestones. DiD against Chicago tracts without electrified routes.

**Minimum detectable effect.** A 1–2 µg/m³ annual-mean shift is detectable with 3+ years of monitor data.

**Threats to validity.** Regional PM2.5 trends independent of CTA policy; monitor coverage sparsity.

**Show the investor:** Pope coefficient × observed PM2.5 reduction = projected LE-years gained per 1000 residents.
**Show the client:** PM2.5 monitor dashboard tied to CTA fleet composition change dates.

---

## MT2 — CTA Racine Green Line Reopening (no LE estimate in tree [DATA GAP])

**Causal mechanism.** The Racine Green Line station at 63rd/Racine has been closed since 1994; IL transit bill signed Dec 2025 targets 2029 reopening [IMAN_initiatives_profile.md]. Reopening is a multi-pathway intervention: PM2.5 reduction via mode shift, healthcare/employment access improvement, economic-activity spillover to the Fresh Market corridor. Evidence base is cross-domain: Barcelona superblocks [Perez et al., evidence_base.md Mobility]; MESA cohort on neighborhood walkability [Diez Roux, evidence_base.md Mobility]; Chetty Opportunity Atlas on transit-to-mobility links.

**Proxy outcome (2-5 yr).** (a) Pre/post ridership at the reopened station (CTA). (b) Employment rate and commute-time-to-work for Englewood residents (LEHD / ACS). (c) Fresh Market same-store sales and loyalty-program growth. (d) Emergency-room visit access time from Englewood (IHA).

**Identification strategy.** ITS on the 2029 station opening as a structural break. DiD vs. community areas without new rail access. Borrowed elasticities from Opportunity Atlas and transit-intervention literature.

**Minimum detectable effect.** Ridership generates its own pre/post signal; upstream mobility and employment outcomes require 5+ years of follow-up.

**Threats to validity.** Confound with 2029 macro shocks; concurrent Racine corridor investments.

**Show the investor:** the Green Line reopening as the "physical infrastructure completion" of the Racine corridor bundle; projected ridership × time-savings × Chetty commute-mobility elasticity.
**Show the client:** CTA ridership and commute-time dashboard at monthly cadence post-opening.

---

## MT3 — Safe Walking Routes (~0.3 yr LE gain) [Source: decision_tree.md]

**Causal mechanism.** Barcelona superblocks: 665 premature deaths/yr prevented citywide, LE +0.20 yr [Perez et al., evidence_base.md Mobility]. Pathway: reduced traffic + noise + air pollution + more physical activity → CVD + respiratory + injury mortality.

**Proxy outcome (2-5 yr).** (a) Pedestrian injury rate (Chicago Data Portal traffic crashes). (b) Self-reported physical activity (CDC PLACES proxy). (c) Walkability index change (EPA Smart Location or Walk Score) along treated corridors.

**Identification strategy.** DiD on treated vs. untreated corridors within Englewood/Chicago Lawn. Borrowed Perez elasticity.

**Minimum detectable effect.** Pedestrian crash counts are small; detection requires 3+ years of monthly data.

**Threats to validity.** Concurrent Griot Plaza and corridor investments.

**Show the investor:** crashes-averted × Barcelona LE coefficient.
**Show the client:** corridor-level walkability score trajectory.

---

## MT4 — Active Transit Infrastructure (~0.2 yr LE gain) [Source: decision_tree.md]

**Causal mechanism.** Cycling/pedestrian infrastructure drives physical-activity gains and mode shift; Twohig-Bennett/Jones meta-analysis on greenspace exposure shows mortality reductions [evidence_base.md Mobility]. Pathway: active transport → fitness → CVD mortality reduction.

**Proxy outcome (2-5 yr).** (a) Divvy station ridership at Griot Plaza and adjacent stations. (b) Bike-lane-mile coverage in CA 68/66. (c) Self-reported physical-activity rate (PLACES).

**Identification strategy.** ITS on Divvy station openings. Dose-response on bike-lane-mile density.

**Minimum detectable effect.** Ridership signal is direct; physical-activity proxy requires larger scale.

**Threats to validity.** Weather seasonality; Divvy user base skews non-resident.

**Show the investor:** per-capita active-transit minutes × borrowed CVD-risk coefficient.
**Show the client:** station-by-station ridership and infrastructure-completion milestones.

---

## Summary for A5

Four MT initiatives. MT1 (PM2.5/bus electrification) and MT2 (Green Line) have the cleanest causal frames via published elasticities. MT3–MT4 are active-transit proxies that aggregate best into the bundle narrative.
