# A1 — Healthcare Initiative Evaluation

**Stream A** — Per-initiative evaluation designs for the Healthcare domain (decision_tree.md HC1–HC6).
**Rule:** every numeric claim is logged in `verification/claims_stream_A.csv`. Cross-ref §2 and §5 of `A0_cross_cutting_methodology.md` for identification strategy definitions and long-run projection procedures.

---

## HC1 — FQHC Expansion (~1.5 yr LE gain) [Source: decision_tree.md]

**Causal mechanism.** Expanding primary-care capacity in a 30-year-gap neighborhood raises the proportion of residents with a usual source of care, cuts emergency-department substitution for primary care, and enables chronic-disease management (BP, HbA1c, cholesterol) — the three cardiometabolic pathways that account for a large share of Englewood's excess mortality. Behavioral-health co-location (per IMAN's planned build-out) adds depression/SUD management to the same visit. The ACA Medicaid expansion literature produced a 6.1% reduction in all-cause near-poor mortality [Sommers et al., NEJM, evidence_base.md Healthcare], and IMAN's FQHC is the *delivery mechanism* that converts coverage into care.

**Proxy outcome (2-5 yr).** (a) BP-control rate among adult FQHC panel patients — quarterly from UDS reporting. (b) HbA1c <8 rate among diabetic panel patients — quarterly UDS. (c) Tract-level ED-visit rate for ambulatory-care sensitive conditions (ACSCs) from Illinois Hospital Association discharge data, annual. (d) Amenable-mortality rate (Nolte-McKee list) from CDC WONDER, 3-year rolling.

**Identification strategy.** Staggered DiD using the two-building timeline: pre-expansion baseline (current 3,500 sq ft clinic) vs. post-expansion (30,000 sq ft with integrated behavioral health). Comparison group = Pool A Chicago community areas that did not expand FQHC capacity in the study window. Synthetic-control backup using Abadie weights on pre-period BP control and ACSC ED-rate trajectories.

**Minimum detectable effect.** With 15 peer community areas and 5 pre/5 post years, we can detect a ~4-percentage-point relative improvement in BP-control rate or a ~8% relative drop in ACSC ED-rate at 80% power — both well within the range of published FQHC-expansion effects.

**Threats to validity.** Selection (patients choose to enroll) — address with instrumental variable using distance to clinic. Reverse causation (sicker patients drawn in) — address with intent-to-treat at the tract level, not patient level. Spillover (non-patients in catchment still benefit) — this is a *feature* at tract level but contaminates patient-level contrasts. Contamination (Northwestern ACO patients get care elsewhere) — adjust via insurance-type stratification.

**Show the investor:** a synthetic-control chart of Englewood BP-control and ACSC-ED trajectories diverging from matched peer neighborhoods after the 2026 groundbreak.
**Show the client:** a quarterly UDS dashboard of panel BP/HbA1c/tobacco-cessation rates vs. Chicago FQHC median, with drill-down by CHW-assigned cohort.

---

## HC2 — CHW Programs (~1.0 yr LE gain) [Source: decision_tree.md]

**Causal mechanism.** Community Health Workers (CHWs) bridge the clinic-to-home gap: they enroll eligible residents in Medicaid/SNAP/WIC, conduct BP screenings in community settings (Fresh Market, Food and Wellness Center, neighborhood walks), coach self-management for chronic disease, and surface unmet social needs for referral. The Brazil Family Health Strategy evidence [Macinko J, evidence_base.md Healthcare] establishes CHW-model reductions in infant and all-cause mortality in structurally comparable settings.

**Proxy outcome (2-5 yr).** (a) Benefits-enrollment completions per 1,000 eligible residents (IMAN internal + IL Dept of Human Services). (b) Community BP-screening volume and share referred to clinical follow-up (IMAN CHW log). (c) BP control among CHW-coached patients vs. non-coached comparable FQHC patients. (d) 30-day readmission rate among CHW-coached hospital-discharged patients (Northwestern claims share-back).

**Identification strategy.** Individual-level DiD: CHW-enrolled patients vs. propensity-matched non-CHW FQHC patients, outcome = BP control + SNAP enrollment composite, 12-month change. Backup: borrowed effect size from recent CHW meta-analyses (tier-1 systematic reviews; Stream F to pull).

**Minimum detectable effect.** With n≈500 coached patients and a matched comparison, detect a 5-point BP-control percentage-point gap at 80% power.

**Threats to validity.** Selection (CHWs work with motivated patients) — address via propensity matching on demographics, baseline BP, insurance. Contamination (non-coached patients also get some CHW touch at pantry) — inevitable; treat as attenuation bias that biases estimates *toward* null (conservative for investor).

**Show the investor:** "For every dollar of CDPH CHW funding, IMAN delivers X BP screenings, Y SNAP enrollments, Z BP-control improvements — here is the published meta-analytic benchmark we match or beat."
**Show the client:** a monthly CHW-contact-to-outcome pipeline: screenings → referrals → clinic visits → control-rate gains.

---

## HC3 — Medicaid Enrollment (~0.7 yr LE gain) [Source: decision_tree.md]

**Causal mechanism.** Coverage itself is a mortality-reducing intervention: the ACA Medicaid-expansion natural experiment showed 6.1% lower all-cause mortality in near-poor adults in expansion states [Sommers et al. NEJM, evidence_base.md Healthcare]. CHW-led enrollment outreach closes the coverage gap for residents who are eligible but unenrolled.

**Proxy outcome (2-5 yr).** (a) Tract-level uninsured rate from SAHIE (annual). (b) Completed Medicaid enrollments attributable to IMAN CHW outreach (IMAN + IDHS). (c) First-year downstream utilization: primary-care visit rate among newly-enrolled.

**Identification strategy.** Borrowed effect size from the Medicaid-expansion literature scaled to IMAN's actual newly-enrolled volume. Specifically: if IMAN enrolls N residents and the literature predicts a 6.1% mortality reduction, expected deaths averted = baseline mortality rate × N × 0.061. For IMAN-specific incremental identification, use a CHW contact-intensity DiD across Englewood/Chicago Lawn blocks.

**Minimum detectable effect.** Detecting a mortality change from 500 new enrollees is not feasible directly; evaluation must lean on the borrowed effect. Report enrollment throughput and first-year utilization as the observable outcomes, with mortality projection as an inferred downstream claim.

**Threats to validity.** Selection (enrollees are the sickest or the most stable) — split analysis. Churn (Medicaid redetermination post-PHE unwinding re-disenrolls people) — track 12-month retention. Substitution (enrollees would have eventually enrolled via another channel) — acknowledge in investor framing.

**Show the investor:** a monthly ticker of IMAN-attributable new Medicaid enrollments × published mortality-reduction coefficient = projected lives-saved trajectory.
**Show the client:** case-level tracking: enrollment → first PCP visit → chronic-condition identification → control-rate attainment.

---

## HC4 — Barbershop BP Screening (~0.6 yr LE gain) [Source: decision_tree.md]

**Causal mechanism.** Systolic hypertension is the single largest modifiable cardiovascular risk factor in Black men, who are under-engaged by clinical primary care. The Los Angeles barbershop RCT showed pharmacist-led treatment in trusted non-clinical settings achieved BP control in 63.6% of intervention participants vs. 11.7% of controls [Victor et al., NEJM 2018, evidence_base.md Healthcare]. BP control at this level is associated with material reductions in stroke and CV mortality.

**Proxy outcome (2-5 yr).** (a) Share of Black-male participants achieving SBP <130 mmHg at 6 and 12 months (IMAN/barbershop log + FQHC EHR linkage). (b) Stroke hospitalization rate among 45-65yo Black men in the Englewood/Chicago Lawn catchment (IHA discharge data).

**Identification strategy.** Direct replication of published Victor et al. RCT effect size is the default. If IMAN can randomize shop-level (wait-list design: some shops start year 1, others year 2), run a cluster-randomized rollout. Otherwise use pre/post with synthetic-control comparison.

**Minimum detectable effect.** Barbershop trial effect sizes are very large (ATE ≈ 52 percentage points in BP-control rate). Even a quarter of that ATE (~13 pp) is detectable with ~100 participants per arm.

**Threats to validity.** Selection (barbers' regular customers differ from random adult men) — intent-to-treat across all shops in catchment. Contamination (participants still see FQHC doctors) — acceptable; the program is *additive*. Attrition (regimen drop-off at 12 months) — track explicitly.

**Show the investor:** a direct numerical replication of the Victor et al. NEJM trial result in a Chicago African-American population — one of the most investor-legible designs in the portfolio.
**Show the client:** quarterly BP-control-rate by barbershop, with a trigger threshold for re-engagement outreach.

---

## HC5 — MOUD + Naloxone (~0.8 yr LE gain) [Source: decision_tree.md]

**Causal mechanism.** Medication for Opioid Use Disorder (buprenorphine/methadone) reduces all-cause mortality by 50–75% vs. off-treatment [evidence_base.md Healthcare]. Naloxone saturation in Massachusetts was associated with 46% lower community overdose mortality [Walley et al. BMJ 2013, evidence_base.md Healthcare]. The combined program reverses overdoses in the community and routes survivors into maintenance treatment.

**Proxy outcome (2-5 yr).** (a) Opioid-overdose mortality rate per 100,000 in the Englewood/Chicago Lawn catchment (Cook County ME + CDC WONDER). (b) Non-fatal overdose EMS run rate (Chicago EMS). (c) MOUD initiation and 90-day retention among FQHC patients screened positive for OUD. (d) Naloxone kits distributed per 1,000 residents.

**Identification strategy.** Interrupted time series on monthly overdose-mortality rate pre/post naloxone saturation roll-out in the catchment. DiD against Chicago community areas with equivalent baseline overdose rates but no saturation program. Borrowed effect size from Walley et al. as a benchmark.

**Minimum detectable effect.** At Englewood's current overdose-mortality baseline (high), a 20% reduction is detectable at 80% power with 3 years of monthly data.

**Threats to validity.** Secular trend (fentanyl supply shocks drive mortality independently) — address with national trend subtraction or DiD. Displacement (overdoses shift to neighboring tracts) — measure buffer-zone rates. Selection (MOUD-retained patients were predisposed to retention) — not a threat for community-level naloxone; is a threat for MOUD-retention claims.

**Show the investor:** a monthly overdose-mortality line for Englewood vs. synthetic Chicago, with the naloxone-saturation start date marked as a structural break.
**Show the client:** MOUD-initiation pipeline by referral source (street outreach, FQHC screen, post-OD EMS handoff) and retention curves.

---

## HC6 — Integrated Behavioral Health (~0.8 yr LE gain) [Source: decision_tree.md]

**Causal mechanism.** Co-location of behavioral health with primary care (the explicit design of IMAN's expanded FQHC) raises treatment engagement for depression and SUD, which are mortality risk factors directly (suicide, overdose) and indirectly (medication non-adherence, untreated CVD risk factors). Supported by the integrated-care literature [evidence_base.md Healthcare].

**Proxy outcome (2-5 yr).** (a) PHQ-9 screening rate among FQHC primary-care visits. (b) Share of PHQ-9 ≥10 receiving same-visit behavioral-health warm handoff (UDS Clinical Quality Measure 2). (c) Depression remission at 6 months (UDS CQM). (d) Suicide-ideation to ER-visit rate (IHA).

**Identification strategy.** Pre/post the physical co-location (current two-building layout → single-building post-expansion). Use the interrupted-time-series design because the intervention is a discrete structural change. Comparison FQHCs as a DiD control group.

**Minimum detectable effect.** A 15-percentage-point improvement in same-visit-warm-handoff rate is both clinically meaningful and statistically detectable with IMAN's panel size.

**Threats to validity.** History (COVID-era telehealth shifts confound). Staff turnover between buildings pre/post. Panel composition changes.

**Show the investor:** UDS CQM-2 (depression screening + follow-up) rising from pre-expansion baseline to post-expansion rate, benchmarked against national FQHC median.
**Show the client:** warm-handoff rate as a daily operational metric; depression-remission funnel by provider.

---

## Summary for A1

Six HC initiatives with strong evidence-base grounding. Four are suitable for direct borrowed-RCT effect-size framing (HC1, HC3, HC4, HC5); two require observational DiD/ITS designs (HC2, HC6). The barbershop-BP program is the single most investor-legible evaluation in the portfolio — a near-perfect replication of a high-impact NEJM trial in IMAN's target population.
