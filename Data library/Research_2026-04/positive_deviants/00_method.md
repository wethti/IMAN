# Positive Deviant Methodology — "Urban Blue Zones"

**Author:** Stream E (Positive Deviants), IMAN 2040 research, 2026-04-21
**Audience:** Mixed — data team + investor-facing consulting clients
**Purpose:** Make explicit how we decide a neighborhood is a "positive deviant" so the investor-facing claim ("a neighborhood that looks like Englewood but adds 5–10 years of life") rests on reproducible statistics, not on cherry-picking.

---

## 1. What a positive deviant is

A census tract, ZIP, or community-area equivalent is a **positive deviant** if:

1. It **meets the Pool B criteria** (`../peer_neighborhoods/00_similarity_criteria.md`): poverty rate > 25%, median household income in bottom quintile of its MSA, USDA-designated food-access tract, unemployment ≥1.5× MSA mean, built before 1960 or vacant rate ≥10%, principal-city urbanicity.
2. Its **observed life expectancy (LE) is at least +5 years above the LE predicted** for its covariate profile (see §2).
3. The residual is statistically robust: the USALEEP-published standard error for the LE estimate is < 2 years, and the residual exceeds 2× that SE.

Five years is the threshold we will defend to investors because (a) it is roughly the size of the original Hispanic-paradox gap reported by Markides & Coreil 1986 and confirmed by Ruiz et al. 2013, (b) it is larger than most documented single-program effects in the intervention literature (see Stream D), and (c) it exceeds typical USALEEP small-area SE.

## 2. How we estimate predicted LE

For each tract *i* in USALEEP 2010–2015, we fit:

> LE_i = β₀ + β₁·poverty_i + β₂·%Black_i + β₃·%uninsured_i + β₄·unemp_i + β₅·vacant_i + β₆·%<HS_i + β₇·%foreign_born_i + β₈·MSA_FE + ε_i

We report the residual ε_i (observed − predicted). A large positive residual = the tract lives longer than its ACS covariate profile says it should.

Two design choices to flag:

- **We include `%foreign_born` as a covariate.** That is deliberate. We are *not* trying to "explain away" the immigrant enclave effect — we are trying to find tracts that outperform *even* after we account for the demographic composition. Tracts that still show positive residuals after controlling for foreign-born share are the strongest positive deviants. For investor-facing narrative we also show the *uncontrolled* residual (for comparability with published Blue Zones work).
- **We include MSA fixed effects** so that we are comparing tracts within the same housing, healthcare, labor-market, and pollution context. A South Bronx tract is measured against other NYC tracts, not against Atlanta suburbs.

## 3. Why this differs from Buettner's Blue Zones

Dan Buettner's original Blue Zones work (Okinawa, Sardinia, Loma Linda, Nicoya, Ikaria) used **crude life expectancy and crude centenarian rates**. That was defensible for a book-length ethnography because the five chosen regions are famously long-lived and the contrast with average OECD rates was obvious.

For urban American poverty research we **cannot** use crude LE. Every single high-LE ZIP in the US is also high-income — using crude LE would just rediscover that rich neighborhoods live longer. We need to hold income, housing, food access, and race roughly constant and then ask: within this matched-disinvestment cohort, who outperforms, and why?

That is the move this methodology makes: we port Buettner's *method* (find places with surprising longevity and walk through them asking what's different) but we redefine "surprising" as **residual-adjusted**, not crude.

## 4. Data sources

| Variable | Source | Resolution | Vintage |
|---|---|---|---|
| Life expectancy at birth | USALEEP (NCHS / RWJF / NAPHSIS) | Census tract | 2010–2015 |
| Life expectancy (NYC) | NYC DOHMH Community Health Profiles | Community District (59) | 2015, 2018, 2021 |
| Life expectancy (Chicago) | CDPH Data Brief / Chicago Health Atlas | Community Area (77) | 2017–2023 |
| LE, LA County | LA County DPH Community Health Profiles | Community Statistical Area | 2018–2023 |
| LE, Boston | Boston Public Health Commission — Health of Boston | Neighborhood | 2023 report |
| Poverty, income, race, foreign-born, % <HS | ACS 5-year | Tract | 2019–2023 |
| Food access | USDA FARA | Tract | 2019 |
| Uninsured | SAHIE | Tract | 2020 |
| Housing age / vacancy | ACS 5-year | Tract | 2019–2023 |
| Redlining | Mapping Inequality (Nelson et al., Univ. Richmond) | HOLC polygon | 1935–1940 |

NYC, Chicago, Boston, and LA County all publish city/DOH-grade LE estimates that are usually tighter (larger geographic aggregation, bigger denominators) than USALEEP tract estimates. Where both exist we prefer the city-DOH number for the headline and use USALEEP for within-city tract variation.

## 5. Threats to this design (state to the client — don't hide them)

1. **Salmon bias / return migration.** Palloni & Arias 2004 showed that a meaningful share of the Hispanic mortality advantage for foreign-born Mexicans is driven by elderly migrants returning to Mexico to die, so their deaths don't appear in US vital statistics. Any tract with a large foreign-born Mexican population has this artifact baked in. We report both (a) the naive residual and (b) a "Palloni-corrected" sensitivity range that assumes 15–30% of the residual is salmon bias (the range Palloni & Arias estimated).
2. **Healthy migrant selection.** Immigrants are not a random sample of their country of origin; they tend to be healthier at arrival. A neighborhood with mostly first-generation immigrants will look like a positive deviant partly because of selection at the border, not because of anything the neighborhood is doing. The investor claim has to be honest about this.
3. **Small-area estimation noise.** USALEEP tract LE has SEs that can exceed 4 years in small tracts. We drop tracts with SE > 2 years.
4. **Ethnicity mis-coding on death certificates.** About 5% of Hispanic decedents in national data are mis-classified as non-Hispanic white (Arias et al. 2010, NCHS). That inflates the apparent Hispanic advantage by ~1 year. We adjust the residual threshold upward accordingly.
5. **Period effect.** USALEEP 2010–2015 predates COVID. Post-COVID Hispanic LE collapsed disproportionately (Andrasfay & Goldman 2021). The 2023 NYC and Chicago data begin to show recovery. We flag which vintage each claim uses.
6. **Paradox erosion.** Recent work (STAT News 2023 reporting on Fenelon, Garcia and collaborators) questions whether the Hispanic advantage holds for later-generation US-born Hispanics or for younger cohorts. The investor narrative must say "this advantage is well-documented for first-generation immigrant enclaves; the evidence for US-born descendants is weaker and declining."

## 6. How we decide what's "replicable"

Positive-deviant mechanisms qualify as "IMAN-replicable" if all three are true:

- There is published epidemiology linking the mechanism to longer life (not just to the neighborhood).
- The mechanism is about built environment, social structure, or institutional presence — something an organization can manufacture — *not* about genetic ancestry, selection, or return migration.
- The mechanism plausibly maps to one of IMAN's existing or planned programs (Fresh Market, Health Center, Green ReEntry, Arts & Culture, Youth, Organizing / Takaful, Corner Store Campaign, the planned Regenerator / Griot Plaza / Oasis Café).

Three mechanisms that fail the test and we will NOT claim IMAN can replicate: healthy-migrant selection, return migration, Spanish-speaking healthcare staff as a causal mechanism distinct from trust (though IMAN's Clinic does operate multilingually, so some element of this is in play).
