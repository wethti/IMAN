# A2 — Food Access Initiative Evaluation

**Stream A** — Per-initiative evaluation designs for the Food Access domain (decision_tree.md FA1–FA5).
Cross-ref `A0_cross_cutting_methodology.md`. All numeric claims logged in `verification/claims_stream_A.csv`.

---

## FA1 — Fresh Boost / SNAP Enrollment (~0.6 yr LE gain) [Source: decision_tree.md]

**Causal mechanism.** SNAP participation is associated with reduced food insecurity, improved dietary quality, and lower rates of low birth weight, obesity, and chronic disease [Bach, evidence_base.md Food access]. Fresh Boost is IMAN's in-store credit program that mechanically replicates SNAP with stronger consumer dignity and choice, delivered inside the Fresh Market. Mortality pathway: reduced food insecurity → better diet quality → lower cardiometabolic risk → lower CVD/diabetes mortality over 10+ years. Short-run: reduced psychosocial stress (cortisol), improved prenatal nutrition, fewer acute hypoglycemic events.

**Proxy outcome (2-5 yr).** (a) USDA 18-item food-insecurity scale for Fresh Boost households at enrollment and at 6/12 months. (b) Dietary-quality score (Healthy Eating Index or short-form FFQ) pre/post. (c) Share of Fresh Market transactions using EBT + Link Match (currently 20% / 23% of revenue per IMAN_initiatives_profile.md). (d) Household HbA1c and BP from FQHC records for the subset of Fresh Boost participants who are also FQHC panel patients (EHR linkage).

**Identification strategy.** Randomized waitlist design for Fresh Boost cohort 2 (100 households on waitlist; stagger admission over 6 months). This is a feasible low-cost randomization and produces a clean RCT-style estimate in-house. For SNAP enrollment impact, use borrowed effect sizes from Bach and the WIC/SNAP literature scaled to IMAN's incremental enrollment volume.

**Minimum detectable effect.** With n=100 Fresh Boost participants and a waitlist control, detect a 0.8-point change on the 18-item food-security scale (roughly one category improvement on the USDA rubric) at 80% power.

**Threats to validity.** Selection (enrolled via Kennedy King College students, not representative of Englewood as a whole) — note in scope limits. Hawthorne effect (participants know they are being studied and improve temporarily) — blind the 12-month outcome measurement if possible. Contamination (non-Fresh Boost residents still shop at Fresh Market) — accept as a feature at tract level; the intervention is both the retail presence *and* the credit.

**Show the investor:** a clean pre/post food-security score with waitlist-comparison chart, plus a "cost per food-insecurity reduction" metric that translates grant dollars into dignity-preserving food spend.
**Show the client:** a household-level dashboard: credit utilization, basket composition shift over time, and linked clinical outcome flags for FQHC-matched participants.

---

## FA2 — WIC Access (~0.5 yr LE gain) [Source: decision_tree.md]

**Causal mechanism.** WIC participation significantly improves birth weight and gestational age among low-income mothers [Hoynes et al.; Stevens et al., evidence_base.md Food access]. Low birth weight is a leading predictor of infant mortality and lifelong cardiometabolic and neurodevelopmental disadvantage. Pathway: WIC enrollment → prenatal nutrition → birth outcomes → reduced infant mortality + improved life-course trajectory → LE gain.

**Proxy outcome (2-5 yr).** (a) WIC enrollment rate among eligible Englewood/Chicago Lawn mothers (IDHS + ACS denominator). (b) Low-birth-weight rate and preterm-birth rate from IDPH Vital Statistics, tract-level. (c) First-trimester prenatal care initiation rate.

**Identification strategy.** Borrowed RCT-quality effect size from the Hoynes WIC papers, scaled to IMAN's marginal enrollment volume. Direct DiD infeasible because WIC is universal; the IMAN incremental intervention is the *enrollment-uptake* component driven by CHW outreach at Fresh Market and Food and Wellness Center.

**Minimum detectable effect.** LBW rates are ~10-12% in high-poverty Black neighborhoods; detecting a 2 percentage-point reduction requires ~2,000 births and is therefore a 5-year observation window.

**Threats to validity.** Concurrent Medicaid outreach (cross-contamination between FA2 and HC3). Reporting selection: mothers who engage CHW-assisted enrollment differ from those who don't.

**Show the investor:** WIC enrollment throughput tied to the published Hoynes et al. birth-weight coefficient.
**Show the client:** monthly WIC enrollments traceable to CHW contact, with downstream birth-outcome linkage via IDPH Vital Statistics.

---

## FA3 — Fresh Market Expansion (~0.8 yr LE gain) [Source: decision_tree.md]

**Causal mechanism.** Introducing a full-service grocery into a USDA-designated food desert (Englewood qualifies [IMAN_initiatives_profile.md]) reduces travel time to fresh produce, lowers the effective price of healthy food (via SNAP match, loyalty discounts, 5% resident discount, and below-cost subsidized staples — 9-10% of sales [IMAN_initiatives_profile.md]), and shifts dietary composition. The PHRESH natural experiment [Dubowitz et al., evidence_base.md Food access] found modest but measurable F&V consumption increases following supermarket introduction. Pathway: store presence + affordability → diet → cardiometabolic outcomes → mortality.

**Proxy outcome (2-5 yr).** (a) Census-tract fruit & vegetable consumption prevalence from CDC PLACES (annual). (b) Adult obesity and diabetes diagnosed rates from PLACES. (c) Fresh Market own-data: per-capita basket composition shift, repeat-visit rates, SNAP-match utilization. (d) Block-level distance-to-healthy-food gradient crossed with clinical outcomes among FQHC patients.

**Identification strategy.** Synthetic control on Englewood tract 68 using Pool A peer tracts. Pre-period 2015–2019 (Fresh Market opened March 2022 [IMAN_initiatives_profile.md]); post-period 2022-ongoing. Outcome = PLACES F&V consumption rate and BMI-based obesity rate. Backup: dose-response regression of distance-to-Fresh-Market on block-level PLACES metrics.

**Minimum detectable effect.** PHRESH's published effects were modest (single-digit percentage-point shifts). Detecting that magnitude in synthetic control requires ≥5 years of post-period data and a tight donor-pool fit; we expect attribution CIs to be wide.

**Threats to validity.** Spillover (non-Englewood residents shop at Fresh Market) — inflates denominator, biases toward null. Selection (motivated residents walk further) — address with intent-to-treat at tract level. Concurrent 63rd/Racine corridor investments (Griot Plaza, Regenerator) — a confound for site-level analysis; handle via the bundle-effect methods in A0 §6.

**Show the investor:** synthetic-control chart of Englewood diet/cardiometabolic proxies diverging from peer neighborhoods after March 2022 store opening. This is the anchor visual of the IMAN narrative.
**Show the client:** internal store metrics (EBT share, subsidized-staple volume, loyalty retention) cross-referenced with FQHC clinical outcomes for matched patients.

---

## FA4 — SSB Tax / Food Pricing Policy (no LE estimate in tree [DATA GAP])

**Causal mechanism.** Sugar-sweetened beverage taxes reduce SSB purchases by 10–50% across jurisdictions [Teng et al., evidence_base.md Food access] and 12% in year 1 in Mexico with larger effects in lower-income households [Colchero et al., evidence_base.md]. Reduced SSB consumption → lower calorie intake + lower glycemic load → reduced obesity and T2D incidence → reduced CVD/diabetes mortality.

**Proxy outcome (2-5 yr).** (a) Share of Fresh Market beverage revenue from SSBs vs. water/healthy drinks. (b) Cook County beverage-tax revenue by ZIP (if reinstated). (c) BMI prevalence from CDC PLACES. Because this is a policy initiative rather than a direct IMAN service, the evaluation is mostly advocacy-tracking rather than program-effect estimation.

**Identification strategy.** Case study / borrowed meta-analytic effect size from Teng et al. and Colchero et al. No direct IMAN attribution design.

**Minimum detectable effect.** Not applicable as direct IMAN intervention.

**Threats to validity.** Cook County's prior SSB tax was repealed in 2017; renewed effort faces the same political economy. Substitution to non-taxed sugary products.

**Show the investor:** policy framework with borrowed meta-analytic mortality projections for a reinstated Cook County SSB tax.
**Show the client:** Fresh Market-level healthy-beverage share as a voluntary pricing experiment, pre/post internal pricing shifts.

---

## FA5 — EITC + Income Transfers (~0.4 yr LE gain) [Source: decision_tree.md]

**Causal mechanism.** EITC expansions produced improvements in infant health outcomes (birth weight) [Hoynes et al., evidence_base.md Food access]. Chetty's work [evidence_base.md Funding] establishes $10,000/yr income ≈ 1 yr LE among low-income adults. Pathway: cash or cash-equivalent → reduced material hardship → reduced stress, better nutrition, better access to care → mortality.

**Proxy outcome (2-5 yr).** (a) EITC uptake rate among eligible Englewood filers (IRS SOI + ACS). (b) VITA tax-prep volume delivered through IMAN/partner sites. (c) Household material-hardship scores.

**Identification strategy.** Borrowed effect sizes from Hoynes and Chetty applied to IMAN-attributable EITC uptake. No direct causal design at IMAN scale.

**Minimum detectable effect.** N/A — evaluation is enrollment-throughput tracking tied to published coefficients.

**Threats to validity.** Policy instability (EITC rules change federally). Take-up rates are already high; marginal uptake is concentrated in hardest-to-reach households.

**Show the investor:** dollars of EITC claimed per IMAN outreach contact, × Chetty income-LE coefficient = projected LE impact.
**Show the client:** VITA-site throughput funnel and post-filing financial-wellbeing survey.

---

## Summary for A2

Five FA initiatives with Fresh Market (FA3) as the anchor of the synthetic-control narrative. FA1 is the cleanest RCT-style in-house evaluation IMAN could run cheaply (waitlist randomization on Fresh Boost cohort 2). FA4 and FA5 are borrowed-effect-size advocacy/policy lines with weaker direct attribution.
