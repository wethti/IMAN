# Client's Canonical Peer-Community Framework
**Source:** `Data library/Comparable Communities (1).docx`, added by the client on 2026-04-21.
**Status:** AUTHORITATIVE. This supersedes my provisional criteria in `00_similarity_criteria.md`. All downstream work must align to this list.

---

## The canonical peer list

### Midwest (Strongest Match)
- Gary, Indiana
- East St. Louis, Illinois
- Flint, Michigan
- Youngstown, Ohio
- Toledo, Ohio (select neighborhoods)
- Rockford, Illinois
- South Bend, Indiana

### Large City Low-Income Neighborhoods
- South Side, Chicago, Illinois
- West Side, Detroit, Michigan
- North Side, Milwaukee, Wisconsin
- West Side, Cleveland, Ohio

### South / Sunbelt Regions
- Memphis, Tennessee
- Birmingham, Alabama
- Jackson, Mississippi
- Shreveport, Louisiana

## The client's 9-criterion similarity rubric

Communities score 0–9; **7–9 = strong match**, 5–6 = moderate, <5 = weak.

1. **Income.** Median household income $25,000–$40,000; wealth index <50 (US average = 100).
2. **Housing structure.** Renter share ≥60%; ownership ≤40%; median home value <$200k.
3. **Employment profile.** Industrial, manufacturing, service, retail, logistics dominant; limited white-collar.
4. **Consumer behavior.** Preference for discount retailers; high price sensitivity; SNAP/EBT usage; discount retail presence.
5. **Demographics.** Median age 30–40; college-degree attainment <30%; average household size 2–3.
6. **Population density & urban form.** Moderate density; mixed residential and small retail corridors; walkability.
7. **Economic growth.** Population growth −1% to +1%; limited new development.
8. **Affordability pressure.** Housing affordability index <80; high share of income on necessities.
9. **Diversity & language.** Primarily English-speaking; 10–20% Spanish.

## Baseline characteristics of Englewood (from the client's doc)

- Concentrated economic disinvestment
- Low household income + high poverty rates
- High renter share + housing instability
- Limited access to quality healthcare, food, other essential services
- Lower educational + employment outcomes
- Higher exposure to safety, environmental, or chronic health challenges
- Urban neighborhood context (not citywide averages)
- History of structural inequities affecting long-term community wellbeing

---

## Reconciliation with my provisional framework

My earlier `00_similarity_criteria.md` used a 10-criterion rubric that added historical redlining (HOLC D-grade) and USALEEP tract-level life-expectancy thresholds. The client's framework is tighter on economic/consumer-behavior dimensions and does not require LE as an entry criterion.

**Implications for the work:**

- **Stream C (peer pool):** the authoritative matched pool = the 16 communities above. Stream C's own residualized-LE analysis becomes a *secondary* ranking within this pool, not an independent selection mechanism.
- **Stream D (similar projects):** benchmark projects should be re-scored by whether they were implemented in one of the 16 canonical communities. Projects outside this pool (e.g., East Lake Atlanta, Harlem Children's Zone, Dudley Street/Roxbury) remain in the library but are flagged as "cross-pool comparators" with a note about transferability.
- **Stream E (positive deviants):** explicitly *outside* the canonical peer pool. The positive-deviant overlay (East LA, East Boston, Washington Heights, Little Village) is distinct — these are *not* Englewood peers by the client's definition (they are Latino/immigrant neighborhoods with growth dynamics, not Rust Belt disinvestment). I'll reframe Stream E as a "reference set" answering the question: "In what *other* kinds of similar-on-paper neighborhoods do we see unexpectedly good outcomes, and which of those mechanisms are transferable?"

## Key observation for the investor story

The canonical peer list skews heavily toward **Rust Belt industrial decline + historically Black Midwestern cities** (Gary, Flint, East St. Louis, Youngstown, North Milwaukee, West Detroit, West Cleveland). This is demographically *closer* to Englewood than the positive-deviant set would be. The implication for the investor frame:

- The matched peer story: "Of the 16 places in America that most look like Englewood, here is what has and hasn't worked."
- The positive-deviant story: "Of the places in America that are *economically* like Englewood but achieve Streeterville-level life expectancy, here is what's different."

Both stories are needed. The first tells investors what is realistic for Englewood's trajectory; the second tells them what is aspirational.

---

## Tract-level granularity still required

The client's list names cities and large sub-areas (e.g., "South Side, Chicago"). For synthetic-control work we need census-tract specificity. Stream C's follow-on task: take each of the 16 communities and enumerate the specific ZIP codes or census tracts that best match the 9-criterion profile — e.g., "South Side Chicago" = community areas 67 (West Englewood), 68 (Englewood), 69 (Greater Grand Crossing), 71 (Auburn Gresham), 49 (Roseland), etc.
