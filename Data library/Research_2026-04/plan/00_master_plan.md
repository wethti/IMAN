# IMAN Overnight Research Plan — 2026-04-21

**Author:** Claude (Opus 4.7), on behalf of the IMAN consulting team
**Owner:** dpo120000@gmail.com
**Scope:** End-to-end data science research plan to build an evidence- and data-backed case for IMAN's 2040 strategic plan, targeted at both non-technical consulting clients and institutional investors.

---

## 1. Problem statement

IMAN's 2040 plan asks consultants to quantify the life-expectancy (LE) impact of ~40 ongoing and proposed neighborhood interventions in Englewood and Chicago Lawn. Three problems make this non-trivial:

1. **Attribution.** Life expectancy at the neighborhood scale moves slowly and is jointly determined by dozens of upstream factors; a single program's marginal effect is rarely detectable with a conventional t-test.
2. **Sample size.** Englewood is one community area. A single-unit "case study" cannot by itself establish causal effect on LE without a comparison group.
3. **Data latency.** Neighborhood-level LE (USALEEP) was last published with 2010–2015 data. Most of IMAN's programs matured after that window.

The plan below addresses all three by combining (a) proxy mortality indicators that *do* move on a 2–5 year horizon, (b) a synthetic-control / difference-in-differences design using peer neighborhoods, and (c) a qualitative "positive deviant" overlay that answers the investor question **"show me a place like Englewood that is working, and tell me why."**

## 2. Deliverables

| # | Deliverable | Audience | Format |
|---|---|---|---|
| D1 | Executive brief (3–4 pages) | Non-technical consulting client | Markdown + PPT export |
| D2 | Investor one-pager: the "Positive Deviant" story | Funders / philanthropy | PDF-ready markdown |
| D3 | Peer-neighborhood similarity framework + list | Internal analysts | CSV + methodology memo |
| D4 | Public dataset catalog (every dataset IMAN should use) | Internal analysts | CSV + methodology memo |
| D5 | Per-initiative evaluation playbook | Internal analysts | One memo per domain (9 memos) |
| D6 | Peer-project benchmark library (20+ projects) | Strategy team | Markdown table + short profiles |
| D7 | New literature additions to the Knowledge Map | Research team | Citations list with tier classification |
| D8 | Verification log | Everyone | CSV of every claim with primary source |
| D9 | **Filtered sub-knowledge-map** — research directly relevant to Englewood-like neighborhoods only, drawn from the main Knowledge Map | Research team, strategy team | Markdown index + per-paper filtered tags |

## 2a. Canonical peer pool (added 2026-04-21 PM)

The client added `Data library/Comparable Communities (1).docx` defining the authoritative peer pool. See `peer_neighborhoods/01_client_canonical_list.md`. The 16 canonical communities are the matched peer pool for all downstream work. The positive-deviant overlay (Stream E) is a *reference* set, not a peer set.

## 3. Research streams (run in parallel overnight)

### Stream A — Initiative Evaluation Framework
**Question:** For each of IMAN's ~40 active/proposed initiatives, what is the most defensible quantitative method to evaluate its contribution to the LE gap?

**Approach:**
- For each initiative: identify the *mechanism* (what mortality cause or upstream determinant it touches), the *nearest measurable proxy* (e.g., HbA1c for diabetes-targeted programs; BP control for CHW programs; food-insecurity score for food-access; violent-incident rate for GVI/Cure Violence), the *data source*, and the *identification strategy* (pre/post, DiD, synthetic control, RCT already published, meta-analysis borrow).
- Produce per-domain memos in `initiative_evaluation/`.

### Stream B — Public Dataset Inventory
**Question:** What every public dataset is relevant, where is it, what geographic resolution does it have, and how should IMAN use it?

**Target scope (not exhaustive):**
- CDC PLACES (census-tract health indicators)
- USALEEP (census-tract life expectancy)
- USDA Food Access Research Atlas
- Chicago Data Portal (crime, 311, health, permits)
- Chicago Health Atlas (CDPH)
- County Health Rankings (Robert Wood Johnson)
- US Census ACS 5-year (tract-level demographics)
- HUD datasets (CHAS, HMDA, Picture of Subsidized Households)
- IRS SOI (income by ZIP)
- Opportunity Insights / Opportunity Atlas (Chetty)
- EPA EJScreen (environmental justice indicators)
- CDC Wonder + NCHS mortality
- Illinois Dept of Public Health Vital Statistics
- NaNDA (National Neighborhood Data Archive)
- BRFSS SMART (metro-level health behaviors)
- SAHIE (uninsured rates)
- SNAP retailer-level redemption (USDA)
- NHANES (national nutrition)
- AHRF (provider supply)
- Federal Reserve CDFI data
- Cook County Assessor parcel data
- CTA ridership by station

For each dataset: URL, license, geo-resolution, temporal range, file format, update cadence, and the specific IMAN question it helps answer.

**Downloadable sample:** For the three highest-priority datasets, pull a test extract for Englewood (community area 68) and Chicago Lawn (community area 66) and write a one-page "what it looks like" memo.

### Stream C — Peer Neighborhood Identification
**Question:** What neighborhoods across the US are demographically and structurally comparable to Englewood + Chicago Lawn, and therefore form a valid comparison pool?

**Criteria (weighted):**
- Majority-Black or majority-minority (>60%)
- Median household income in bottom 20% of MSA
- Poverty rate >30%
- Historically redlined (HOLC D-grade)
- Food-desert / limited supermarket access (USDA LILATracts)
- Life expectancy at least 10 years below state mean
- Population 10k–50k (community-area scale)

Deliver: a ranked list of 30–50 peer tracts/ZCTAs in other MSAs, using USALEEP + ACS + USDA joins. Write the methodology as reproducible code/SQL in `peer_neighborhoods/methodology.md`.

### Stream D — Similar-Neighborhood Project Benchmarks
**Question:** What holistic, place-based community development projects have been implemented in neighborhoods meeting our similarity criteria, and what did rigorous evaluation find?

**Seed list (to be expanded by research):**
- Purpose Built Communities / East Lake, Atlanta
- Harlem Children's Zone
- Dudley Street Neighborhood Initiative (Roxbury, Boston) **← the Boston case the client mentioned**
- Magnolia Community Initiative, Los Angeles
- BeltLine / Westside Future Fund, Atlanta
- Strong Healthy Communities (Cleveland Greater Circle Living)
- Philadelphia LandCare (Branas trial)
- Oakland Ceasefire
- READI Chicago
- Chicago Cure Violence (original site evaluations)
- East Lake Foundation
- Promise Neighborhoods (federal program, ~20 sites)
- Choice Neighborhoods (HUD)
- Jackson Ward / Richmond
- North Hartford Promise Zone
- Newark Community Economic Development Corp
- Build Healthy Places Network portfolio
- Skid Row Housing Trust / LA Homeless Initiative
- Camden Coalition of Healthcare Providers

For each: location, years active, budget, measured outcomes (with effect sizes and confidence intervals where available), evaluation design strength, what worked, what failed.

### Stream E — Positive-Deviant Neighborhoods ("Urban Blue Zones")
**Question:** Which neighborhoods have demographics similar to Englewood's but *better-than-expected* life expectancy, and what explains the gap?

**Method:** Take the full census-tract USALEEP table, regress LE on poverty rate, % Black, % uninsured, unemployment, vacant-lot rate; save the residuals. Neighborhoods with large positive residuals are positive deviants. Cross-reference with qualitative community profiles, ethnographies, and news coverage.

**Known candidates to investigate (investigator will add more):**
- East Boston (large Latino population, lower-income, but LE beats expectations — "Hispanic paradox")
- East Los Angeles
- Chinatown neighborhoods (multiple cities)
- Parts of Jackson Heights, Queens
- Certain Philadelphia and Baltimore tracts
- Coastal Louisiana / Acadiana Latino parishes
- Starr County, TX (Latino, poor, high LE — non-urban comparison)

Output: 8–12 case profiles with demographics, LE residual, and a short "what's different" hypothesis drawing on published community health research. Frame explicitly as Dan Buettner's Blue Zones methodology transferred to urban disinvested neighborhoods.

### Stream F — New Literature Additions
**Question:** What peer-reviewed papers published 2023–2026 should be added to the Knowledge Map that are not already there?

Priority topics:
- Food-is-medicine RCTs (MA flex services, NY Delivering Community Power)
- CHW cost-effectiveness updated meta-analyses
- Supportive housing mortality effects
- READI Chicago long-term follow-up
- Philadelphia LandCare long-term
- Medicaid 1115 waivers for SDOH
- Violence interruption program long-term follow-ups
- Minimum wage and mortality
- EITC and child mortality (new Hoynes work)

Output: one markdown file per domain (9 files) with 5–10 new citations each, tiered by evidence quality.

## 4. Anti-hallucination protocol

**Every numeric claim** that appears in any deliverable must be entered into `verification/claims_log.csv` with columns:
- `claim_id` | `claim_text` | `source_url` | `source_type` (primary / secondary / derived) | `access_date` | `verifier_agent` | `status` (verified / unverified / contested)

Agents are instructed:
- Never fabricate a number. If a number is needed but unavailable, write `[DATA GAP]`.
- Never cite a study without the DOI or URL.
- When summarizing effect sizes, always quote the exact magnitude reported in the abstract.
- Flag any claim that depends on an editorial / blog / press release as `Tier 3` and recommend a primary-source replacement.

## 5. Audience framing

**Client frame (consulting client):** "We built a system that can tell you, for every one of your programs, the best available evidence for its life-expectancy impact, where the uncertainty lies, and what data we'll pull quarterly to track progress."

**Investor frame:** "Neighborhoods that look exactly like Englewood on paper are adding 5–10 years of life expectancy when they do X, Y, Z at scale. IMAN is executing X, Y, Z, and here is the tracking system that will show you results in 18 months, not 20 years."

**Framing check:** every deliverable ends with a "So what for the investor?" paragraph and a "So what for the client?" paragraph.

## 6. Runtime architecture

This research is executed by multiple parallel background agents spawned from this conversation. Each agent:
1. Receives a self-contained brief pointing to a target file path
2. Writes structured markdown output to that path
3. Enters all numeric claims into `verification/claims_log.csv`
4. Returns a short summary of what it wrote and what it could not verify

After all agents complete, the coordinator (main thread) reads each output, resolves conflicts, and assembles the final deliverable package in `deliverable/`.

## 7. Token discipline

- Background agents: 5-8 parallel, each scoped narrowly.
- Main thread reserves tokens for (a) synthesis of findings into investor-ready narrative, (b) verification spot-checks, (c) answering user's follow-up questions.
- No agent reads full PDFs from the 250-paper corpus unless a specific citation is needed — the existing evidence_base.md files already extract the key findings.
