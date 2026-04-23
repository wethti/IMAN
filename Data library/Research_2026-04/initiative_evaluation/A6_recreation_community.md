# A6 — Recreation & Community Initiative Evaluation

Cross-ref `A0_cross_cutting_methodology.md`. Claims logged in `verification/claims_stream_A.csv`.

---

## RC1 — Vacant Lot Greening (~0.5 yr LE gain) [Source: decision_tree.md]

**Causal mechanism.** Branas et al. Philadelphia cluster-randomized trial: greening blighted vacant land produced a 29% reduction in gun violence in surrounding blocks, plus reductions in resident stress and fear [PNAS, evidence_base.md Recreation]. Pathway: environmental-cue change → reduced violence + stress → mortality (homicide, cardiovascular).

**Proxy outcome (2-5 yr).** (a) Block-level shooting incidents (Chicago Data Portal). (b) Self-reported fear/stress (community survey or proxy 311 call patterns). (c) Cortisol-proxy hypertension rate (PLACES). (d) Greened-lot count and total maintained acreage.

**Identification strategy.** Direct replication of the Philadelphia cluster-randomized design if IMAN sequences lot-greening in waves across blocks. Otherwise DiD on treated vs. untreated blocks with parallel-trend verification.

**Minimum detectable effect.** With ~20 treated blocks over 3 years, detection of a 15-25% shooting-incident reduction is feasible (the original Branas trial ATE is very large).

**Threats to validity.** Spillover to neighboring blocks (Branas showed positive spillover, not contamination — a feature). Regression-to-mean on initially-high-violence blocks.

**Show the investor:** direct replication of Branas PNAS trial at Englewood blocks; shootings-averted per greened acre at published elasticity.
**Show the client:** shootings and 311-complaint dashboard per treated block, pre/post greening.

---

## RC2 — Griot Plaza / Community Corridors (no LE estimate in tree [DATA GAP])

**Causal mechanism.** Community corridors with active programming, seating, lighting, wifi, and cultural events create "third places" that reduce isolation, provide surveillance (Jane Jacobs' "eyes on the street"), and concentrate beneficial activity. Evidence base: Barcelona superblocks [Perez et al.]; barbershop-BP RCT as evidence that trusted community settings move health outcomes [Victor et al., evidence_base.md Recreation].

**Proxy outcome (2-5 yr).** (a) Plaza foot-traffic and event-attendance counts (IMAN log). (b) Adjacent-block violent-incident rate (Chicago Data Portal). (c) 311 complaint density and streetlight-outage rate pre/post. (d) Fresh Market same-store sales (spillover metric).

**Identification strategy.** ITS on plaza opening (June 2024 [IMAN_initiatives_profile.md]). DiD vs. comparable corner intersections without equivalent investment. Likely to be entangled with Fresh Market / Regenerator bundle effects — treat as bundle in final report.

**Minimum detectable effect.** Block-level violent-incident rate changes of 20%+ detectable over 3 years with careful parallel-trend analysis.

**Threats to validity.** Entanglement with Fresh Market investment. Plaza's event programming is the active ingredient; static presence alone has weaker effect.

**Show the investor:** plaza as the "community concentrator" node of the IMAN corridor bundle; pair with Branas evidence for violence reduction.
**Show the client:** monthly programming + attendance dashboard with adjacent-block safety and commerce overlays.

---

## RC3 — Park & Greenspace Access (~0.3 yr LE gain) [Source: decision_tree.md]

**Causal mechanism.** Twohig-Bennett & Jones meta-analysis of 103 studies: greenspace exposure is associated with reduced all-cause mortality, CVD mortality, T2D [evidence_base.md Recreation]. Pathway: physical activity + stress reduction + air quality + social cohesion.

**Proxy outcome (2-5 yr).** (a) Greenspace acres per 1,000 residents (Chicago Park District + IMAN corridor lots). (b) Park-visit rate from transit ridership / mobility data. (c) Self-reported physical activity (PLACES).

**Identification strategy.** Dose-response regression across Chicago community areas of greenspace-per-capita on PLACES health indicators. Borrowed meta-analysis effect size.

**Minimum detectable effect.** Cross-sectional regression at 77-community-area scale is well-powered for modest elasticities.

**Threats to validity.** Greenspace quality vs. quantity; co-location with other neighborhood amenities.

**Show the investor:** greenspace-per-capita uplift in Englewood post-IMAN lot conversion × meta-analytic mortality elasticity.
**Show the client:** greenspace inventory dashboard with maintenance-status tracking.

---

## RC4 — Community Health Nodes (~0.6 yr LE gain) [Source: decision_tree.md]

**Causal mechanism.** Co-locating health services (screenings, CHW outreach, food distribution, case management) at trusted community nodes amplifies service utilization beyond traditional clinic settings. Barbershop-BP RCT demonstrates the "trusted setting" multiplier [Victor et al., evidence_base.md Recreation]. IMAN's Food and Wellness Center (BP screenings at every distribution) and Griot Plaza events operationalize this.

**Proxy outcome (2-5 yr).** (a) Screening events and detection volume at non-clinic nodes (IMAN CHW log). (b) Referral-to-clinic conversion rate from community nodes. (c) BP / diabetes control rates for node-referred patients vs. self-referred comparable patients.

**Identification strategy.** Pre/post at each node with propensity-matched comparison patients. Borrowed effect size from Victor barbershop RCT for BP-control ceiling.

**Minimum detectable effect.** 10-percentage-point BP-control gap detectable with 300+ patients per group.

**Threats to validity.** Selection (people attending a node differ from clinic-walk-ins). Contamination (node patients also see FQHC).

**Show the investor:** node-referred-patient BP-control-rate trajectory benchmarked against Victor RCT ceiling.
**Show the client:** per-node referral funnel and downstream clinical outcome dashboard.

---

## Summary for A6

Four RC initiatives. RC1 has the cleanest RCT precedent (Branas) and the most replicable IMAN-scale experiment. RC2 is narratively central but analytically entangled with the Fresh Market bundle. RC3–RC4 are supportive bundle components.
