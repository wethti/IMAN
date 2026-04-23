# A0 — Cross-Cutting Evaluation Methodology

**Stream A — Master Methods Memo**
**Prepared:** 2026-04-21
**Audience:** IMAN research team, client-facing analysts, institutional-investor committee.

---

## 1. Why life expectancy (LE) itself is the wrong primary outcome

Life expectancy at the tract/community-area level suffers from four problems that make it structurally unsuitable as IMAN's short-horizon evaluation metric:

1. **Latency.** USALEEP tract LE was last published using 2010–2015 deaths [Source: 00_master_plan.md]. Most IMAN programs matured after 2020. Any pre/post on LE is therefore impossible today and will remain impossible until a re-release covers 2020–2025 mortality.
2. **Statistical power.** Englewood has ~24,000 residents [Source: 00_similarity_criteria.md]. A year-over-year LE difference of 0.5 years at this population is within the USALEEP standard error for many tracts. Small-area LE estimates have wide CIs and cannot distinguish programmatic effect from stochastic mortality fluctuation.
3. **Confounding.** LE moves under the combined influence of dozens of upstream determinants. Attribution to any single IMAN initiative is impossible without a comparison design.
4. **Right-censoring.** Effects of programs targeted at children (early childhood education, NFP) only manifest in LE 30–60 years later. Waiting is not a useful evaluation stance.

**Replacement stack (ordered, most proximal first).** Every initiative memo proposes one or more of these:
- **Disease-specific / cause-specific mortality.** CDC WONDER + NCHS compressed mortality files, ICD-10 codes for ischemic heart disease, stroke, diabetes, homicide, drug overdose. Tract-aggregated when n permits; ZIP or community-area when it does not.
- **Amenable mortality (Nolte-McKee list).** Deaths before age 75 from causes treatable by timely healthcare. Moves faster than LE and responds specifically to FQHC/CHW programs.
- **Years of Potential Life Lost before 75 (YPLL-75).** Weighting by age at death amplifies homicide and overdose signal — both are dominant drivers of Englewood's gap. Key metric for violence-intervention memos (A7, A8).
- **Proxy biomarkers / clinical indicators.** HbA1c control, BP control, smoking prevalence, obesity from CDC PLACES (annual tract-level modeled estimates).
- **Behavioral / utilization proxies.** SNAP enrollment rate, ED visits for ACSCs (ambulatory care sensitive conditions), well-child visit rate, prenatal care initiation.
- **Structural proxies.** Vacant-lot rate, 311 complaint density, CTA ridership at Racine, violent-incident rate per Chicago Data Portal.

Rule of thumb per initiative memo: pick the most proximal proxy to the causal mechanism and one "downstream check" that you expect to move later.

---

## 2. Identification strategies — the menu

Each initiative memo selects one of these six designs. Listed in descending order of internal validity:

1. **Borrowed RCT effect size.** When a published RCT already answers the causal question (barbershop BP, One Summer Plus, Philly vacant-lot greening, Oregon Medicaid, NFP, HighScope/CPC, READI). Use the published ATE as IMAN's "expected effect if implemented with fidelity." Check fidelity (dose, duration, staffing) against the trial protocol. This is the most defensible frame for investors.
2. **Synthetic control (SCM).** Construct a donor pool from Pool A peer tracts [Source: 00_similarity_criteria.md], fit weights using pre-intervention values of LE, poverty, violence rate. Estimate post-period gap using Abadie-Diamond-Hainmueller and placebo permutations. Best fit for tract-level built-environment interventions (Fresh Market, Griot Plaza, Regenerator) because only one unit is treated.
3. **Difference-in-differences (DiD).** Compare Englewood/Chicago Lawn with matched Chicago community areas on both sides of program rollout. Valid when parallel-trends can be demonstrated 3–5 years pre-treatment. Use event-study specification with staggered treatment (Callaway-Sant'Anna) for programs that rolled out in waves (CHW expansions, Fresh Boost cohorts).
4. **Interrupted time series (ITS).** Single-unit pre/post with segmented regression. Valid for abrupt-onset programs (Green Line reopening 2029, naloxone saturation campaigns). Weaker than DiD/SCM because no counterfactual.
5. **Dose-response / intensity gradient.** Within-Englewood block-level variation in program intensity (CHW contacts per capita, Fresh Market distance, vacant lots greened). Estimate slope. Robust to time-invariant confounders. Best for programs already running.
6. **Case study — no causal claim.** Descriptive only; used when n=1 and no comparison. Acceptable for narrative/investor framing if explicitly labeled.

---

## 3. Synthetic control applied to census-tract interventions

**Procedure.**
1. Define outcome: e.g., tract-level violent-incident rate per 1,000 residents, monthly.
2. Treated unit: Englewood (community area 68) or, for finer resolution, the 10-block Fresh Market / Griot Plaza catchment.
3. Donor pool: Pool A peer tracts (score ≥7 on the 10-point similarity rubric) [Source: 00_similarity_criteria.md]. Drop any tract that implemented a comparable program during the study window.
4. Covariates for weight fitting: pre-treatment outcome trajectory (2015–2021), poverty rate, % Black, median income, vacant-lot rate, housing-vacancy rate, baseline LE.
5. Post-treatment estimator: gap between Englewood observed and synthetic Englewood, cumulated over 24–60 months.
6. Inference: placebo permutations across donor pool; report rank-based p-value. Also compute 90% prediction intervals with block-bootstrap.

**Failure modes.**
- Donor pool too small after exclusions → fall back to DiD with best 5 matches.
- Pre-period trajectory does not stabilize → rule out SCM for this outcome.
- Treated outcome has zero-inflation (homicides, rare months) → aggregate to quarters and use Poisson SCM variant.

---

## 4. Composite neighborhood health score

A single dashboard indicator is useful for investor storytelling and program-manager feedback. Construct:

**Indicator set (normalized to Chicago median = 100):**
- Amenable mortality rate (inverse)
- YPLL-75 (inverse)
- CDC PLACES BP-control prevalence
- CDC PLACES diabetes diagnosed prevalence (inverse)
- Violent-incident rate (inverse)
- Food-insecurity proxy (SNAP enrollment % of eligible)
- Housing cost-burden rate (inverse)
- PM2.5 annual mean (inverse)
- ED-visit rate for ACSCs (inverse)
- Well-child visit rate

**Weighting options (show both to client/investor):**
- **Equal weights.** Transparent, defensible, no latent assumptions.
- **PCA first principal component.** Data-driven. Higher face validity to econometricians. Use as robustness check.
- **LE-contribution weights** derived from published elasticities (see §5). Highest policy relevance but most fragile to source assumptions.

Report all three. Differences across weighting schemes are themselves informative.

---

## 5. Translating short-run proxy effects into long-run LE projections

**The bridge:** we observe, say, a 5 mmHg drop in mean systolic BP at year 3. We want to tell an investor "this is worth X years of LE by year 15." The defensible procedure:

1. **Use published population-level elasticities** rather than inferring our own.
   - PM2.5: 10 µg/m³ reduction = 0.61 yr LE gain [Pope CA et al. NEJM, evidence_base.md Mobility]. Pro-rate linearly over observed PM2.5 delta.
   - Income: +$10,000 annual = ~1 yr LE gain in low-income strata [Chetty et al. JAMA 2016, evidence_base.md Funding].
   - Medicaid coverage: +1 coverage point on 10%+ uninsured population = ~6.1% mortality reduction proxied as ~0.7–1.5 yr LE in 30-yr-gap community [NEJMsa; evidence_base.md Healthcare] — note the derivation step is an assumption.
   - Population mean SBP: a 10 mmHg reduction in mean SBP corresponds to material cardiovascular mortality decline; specific LE coefficient is [DATA GAP — requires primary verification against SPRINT / Lewington meta-analysis; flag for Stream F to pull].

2. **Stack effects additively with an interaction discount.** Naive summation of LE gains across 40 initiatives produces double-counting (Medicaid enrollment and FQHC expansion both work through the healthcare-access pathway). Apply a 30–50% discount to the gross sum when communicating to investors. Defensible procedure: use a Taylor-expansion argument — LE changes are small relative to baseline, so first-order additivity holds for independent pathways but not for shared pathways. Show both the gross and discounted numbers.

3. **Report ranges, not point estimates.** Publication effect sizes vary. Always present low/central/high scenarios. Use the central scenario for narrative and the low scenario for investor financial modeling.

4. **Microsimulation as the ceiling method.** When resources permit, build an agent-based or cohort microsimulation (IMPACT-NCD, CHD Policy Model, or open-source equivalent) parameterized on Englewood demographics. Inject IMAN program effects at their observed proxy magnitudes and forward-project. This is the gold standard for investor reports but is a 6-month engineering project, not an overnight deliverable.

---

## 6. The bundle-effect problem

IMAN runs 10+ programs simultaneously in the same neighborhood, with overlapping populations. Naive "which program caused what" decomposition is not identifiable. Mitigation stack:

1. **Staggered-rollout DiD.** Because IMAN scales programs in cohorts (Fresh Boost cohort 1, then cohort 2; Green Reentry trade additions over time), exploit rollout timing to isolate incremental effects. Use Callaway-Sant'Anna estimator to handle staggered adoption without the negative-weights problem of two-way FE.
2. **Program-intensity gradient.** Every resident lives at a specific distance from the FQHC, Fresh Market, and Griot Plaza. Build a block-level "IMAN intensity index" = weighted sum of program accessibilities. Regress block-level outcomes on index, controlling for demographics. Slope is a "bundle dose-response" estimate.
3. **Mediator analysis.** For individual participants (FQHC patients, Green Reentry grads), decompose the total program-exposure effect into mediator channels (income, food security, BP, BMI) using Baron-Kenny or causal-mediation methods (Imai et al.).
4. **Frame the bundle as the product, not a bug.** IMAN's thesis is that integration multiplies effects. Tell investors: "We are not asking you to fund a single pill. We are funding an ecosystem whose components' effects interact. The bundle is the intervention. We will still decompose where we can, but the primary question is whether the ecosystem outperforms comparable neighborhoods — and synthetic control answers that directly."

---

## 7. Ethics and small-sample considerations

- **No identifiable patient data in public deliverables.** Aggregate to block-group or tract before export.
- **Suppress cells with n<10** on race/sex-stratified mortality (standard NCHS practice).
- **Pre-register evaluation designs** on OSF before the outcome window closes. Prevents specification-searching.
- **Report null results** with the same visual prominence as positive results. Investors who trust IMAN on a null are likely to trust IMAN on the next positive.
- **Community review.** Every evaluation memo passes through IMAN's community engagement team (Daki's team per IMAN_initiatives_profile.md) before external release. Avoids extractive research framing and catches context errors.
- **Multiple-comparison correction** when simultaneously evaluating many proxies: use Benjamini-Hochberg FDR at q=0.1. Do *not* use Bonferroni across all outcomes — it is too conservative for exploratory neighborhood analysis and will cause IMAN to underclaim real effects.

---

## 8. Recommended three evaluation designs for investor storytelling (ranked)

1. **Synthetic control on the Fresh Market catchment, outcome = composite food-security + cardiometabolic proxy.** Defensible, graphical ("here is Englewood vs. its synthetic twin"), tied to the single most public IMAN asset.
2. **Borrowed RCT effect sizes multiplied by IMAN delivery dose (CHW contacts, barbershop-BP equivalents, Fresh Boost households).** Transparent: "the literature says X, we deliver Y doses, so our expected effect is XY." Convert cleanly to a social-ROI number.
3. **Dose-response regression across the 77 Chicago community areas**, positioning Englewood/Chicago Lawn as treatment-intensity leaders and showing the slope of proxy outcomes on IMAN-like program density. Clean investor chart: "neighborhoods that invest in this bundle see these outcomes, and IMAN is pushing Englewood up the curve."

---

## 9. Integration with the full-project pipeline

- Stream B (public datasets) produces the raw data for every proxy in every memo.
- Stream C (peer neighborhoods) produces the donor pool for synthetic control.
- Stream E (positive deviants) provides the "ceiling" estimate — what LE is achievable at Englewood's demographics when every upstream factor aligns.
- Stream F (new literature) is the source for updated effect sizes feeding §5.
- Verification: every numeric claim here is in `verification/claims_stream_A.csv`.

---

## So what for the investor

You will see quarterly dashboards showing proxy indicators that move on a 2-5 year horizon, benchmarked against a synthetic-control peer neighborhood that statistically represents "Englewood without IMAN." Long-run LE projections are derived from published elasticities applied to our observed short-run effects, reported with explicit uncertainty bounds.

## So what for the client

We have stopped asking "did LE go up?" (unanswerable before 2030) and started asking "did the things that *cause* LE to go up — BP control, food security, violent incidents, housing stability — move in your neighborhood faster than in places like it?" Each IMAN program now has a specific, measurable proxy indicator, a named data source, and a causal identification strategy written down in plain language in its domain memo.
