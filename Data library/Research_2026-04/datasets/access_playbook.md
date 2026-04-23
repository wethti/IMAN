# IMAN Data Access Playbook

*Stream B — verified 2026-04-21. Purpose: practical how-to for every dataset in `catalog.csv`. What you need to access it, what will block you, and what the small-area-suppression rules look like.*

---

## 1. Data that IMAN can pull today, no paperwork

These sources are fully public-domain, require no login, no DUA, and have no suppression issue at the Englewood / Chicago Lawn community-area level.

| Dataset | How to pull | Recommended tool |
|---|---|---|
| CDC PLACES | Socrata API, no key required: `https://data.cdc.gov/resource/cwsq-ngmh.csv?$where=statedesc='Illinois' AND countyname='Cook'` | Python `sodapy` or just `curl` |
| USALEEP | Static CSVs on CDC FTP | `curl` |
| Chicago Data Portal (all City datasets incl. crime, 311, permits, CTA) | Socrata API — 1000-row/page, unauthenticated rate limits; register free app token for higher limits | Python `sodapy` |
| USDA Food Access Research Atlas | Static XLSX download | browser |
| County Health Rankings | Static XLSX per year | browser |
| HUD Picture of Subsidized Households | Static CSV + ZIP | browser |
| HUD Fair Market Rents | Static XLSX + API | browser or requests |
| USDA SNAP Retailer Locator | Static CSV updated quarterly (Dec 31 2025 most recent) | browser |
| USDA Food Environment Atlas | Static XLSX (updated March 2026) | browser |
| Gun Violence Archive | On-site "Export to CSV" button per query | browser (no API) |
| Head Start Service Locations | Dataset-builder on headstart.gov | browser |
| Illinois Vital Statistics | PDF tables on IDPH site | browser |
| Chicago Health Atlas | Bulk CSV / XLSX per indicator | browser |
| Opportunity Atlas / Social Capital Atlas | Static CSV + STATA files | browser |

**Rule of thumb:** anything on `.gov`, on `data.cdc.gov`, on `data.cityofchicago.org`, or on `opportunityinsights.org` can be scripted with standard HTTP.

---

## 2. Data that needs a free account / API key

| Dataset | Registration | Rate limit / notes |
|---|---|---|
| US Census ACS + Decennial | Free Census API key: https://api.census.gov/data/key_signup.html | 500 calls/day per IP unless key is used; then effectively unlimited |
| HUD USER API (CHAS + FMR) | Free HUD USER account: https://www.huduser.gov/portal/dataset/fmr-api.html | no published rate limit |
| CFPB HMDA Data Browser API | no account required for web queries, but annual full LAR is multi-GB | bulk download via HTTP; API: https://ffiec.cfpb.gov/documentation/api/data-browser/ |
| NaNDA via ICPSR | Free ICPSR account (email) | accepts TOU per-download |
| AirNow API | Free key request: https://docs.airnowapi.org/request | 500 calls/hr |
| Eviction Lab data | Email form gate | one-time email confirmation |
| Walk Score API | Free developer key + paid tiers | 5,000/day free tier |

Recommendation: **register the following four accounts in week 1 of the project** and store the keys in a `.env` that is git-ignored:
1. Census API key
2. HUD USER account
3. ICPSR researcher account
4. AirNow API key

---

## 3. Data that requires a Data Use Agreement (DUA) or special access

None of the Tier-1 datasets above require a DUA. However, IMAN should plan for the following if the analysis expands:

| Dataset | Mechanism | Gate-keeper | Typical timeline |
|---|---|---|---|
| NCHS restricted-use mortality micro-data (for tract-level recent-year mortality) | Research Data Center proposal | NCHS RDC | 3-6 months + fee |
| CMS Medicaid / CHIP claims (Medicaid enrollment, HC3 impact) | CMS ResDAC DUA | ResDAC + CMS Privacy Board | 6-12 months + $$$ |
| Illinois All-Payer Claims Database (APCD) | IDPH request | IDPH | variable |
| CPD individual-level arrest / case data (below block masking) | CPD FOIA | CPD | weeks-months |
| CPS student-level outcomes | CPS Research Review Board | CPS | 2-4 months |

For the overnight research stream, IMAN should plan to *not* depend on any DUA-gated data; all Tier-1 questions can be answered from public sources.

---

## 4. Small-area suppression rules that WILL bite IMAN

This is the single biggest technical threat to IMAN's tract-level story.

### CDC WONDER / NVSS

**Rule:** Any count < 10 deaths in a cell is suppressed and rates < 20 deaths are marked as "unreliable."

**Impact on Englewood:**
- Englewood community area population ~24,000. For rare causes of death (suicide, specific drug overdoses by substance, pediatric mortality, pregnancy-related), WONDER will suppress.
- Workaround: aggregate across 3-5 year windows; aggregate across community areas (CA 66 + 67 + 68 + 63 pooled); request restricted-use data.

### NCHS USALEEP

**Rule:** LE is suppressed for tracts with < 50 deaths in the 2010-2015 pool.

**Impact:** Most Englewood tracts have enough deaths to be published, but a handful of low-population tracts will be missing. Check `US_B.CSV` vs `US_A.CSV` for availability.

### ACS (Census)

**Rule:** No hard suppression, but margins of error at tract level are often larger than the point estimate.

**Impact:** Median household income at one Englewood tract may have a 90% MOE of ±$8,000 on a $24,000 estimate. Any ranking or ordering by small differences is noise.

**Workaround:** use 5-year estimates (not 1-year), pool tracts into community areas, display MOE explicitly, use significance tests between estimates.

### CDC PLACES

**Rule:** No suppression (model-based), but credible intervals are wide at tract level. PLACES publishes confidence intervals — USE THEM in every chart.

### HRSA UDS

**Rule:** Center-level tables redact some denominator-small cells (e.g., prenatal visits for centers with fewer than N pregnant patients).

### SAHIE

**Rule:** County only — cannot get tract-level uninsured rate from SAHIE. Use ACS B27001 at tract for IMAN's needs.

### Chicago Crime (CPD via Data Portal)

**Rule:** Address is masked to the block level (final two digits of street number → 00). No small-cell suppression on counts.

### Eviction Lab

**Rule:** Some tract-year cells are suppressed (explicit flag in data) where court data is incomplete.

---

## 5. EPA EJScreen — special handling

EPA removed EJScreen from the EPA website on **5 February 2025**.

**IMAN should NOT cite `ejscreen.epa.gov` in deliverables.** Instead:

1. Use the Public Environmental Data Partners reconstruction: https://pedp-ejscreen.azurewebsites.net/ (hosted on Azure; unofficial)
2. Download the archived GeoPackage from Harvard Dataverse: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/RLR5AX
3. For current air-quality data, use EPA AirNow API (still active) + EPA AQS monitor data as a supplement.

In any investor deck, include a footnote: *"EJScreen indicators here derive from the final 2023 EPA release, accessed via the Public Environmental Data Partners archive after EPA removed the tool in February 2025."*

---

## 6. Recommended pull order for the first week of analysis

This is the order in which the analyst should download data once the project starts:

1. Census ACS 2020-2024 — Cook County, all tracts + CA 66/67/68/63 in specific (foundation)
2. CDC PLACES 2025 release — Cook County tracts (Tier-1 outcomes)
3. USALEEP — Illinois A + B files (LE baseline)
4. Chicago Health Atlas — full community-area CSV bundle (fast comparability)
5. USDA Food Access Research Atlas 2019 — Cook County tracts (food-desert flag)
6. Chicago Crime 2015-2025 — full pull, filter to target community areas
7. HMDA 2018-2024 — Cook County tracts (disinvestment narrative)
8. HRSA UDS 2023-2024 — IMAN Health Clinic + Illinois peer FQHCs
9. Mapping Inequality HOLC shapefile — national, filter to Chicago (structural cause)
10. EJScreen 2023 via PEDP/Harvard — block groups in CA 66/67/68/63 (environmental)

Thereafter, context-only datasets (NaNDA, County Health Rankings, Opportunity Atlas, SAHIE) can be pulled on-demand.

---

## 7. Keeping the catalog current

- Re-verify every URL in `catalog.csv` every 6 months. Federal tool removals (like EJScreen in Feb 2025) can happen fast.
- Subscribe to: CDC PLACES email list; Census data-release email; HUD USER announcements; Chicago Data Portal RSS.
- When a dataset URL moves, update `catalog.csv` and add a row to `verification/claims_stream_B.csv` documenting the change.
