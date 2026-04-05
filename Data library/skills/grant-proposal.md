# /grant-proposal Skill

## Trigger
When user types `/proposal`, "generate a grant proposal", "write a grant proposal", or "create a grant proposal" for a project or initiative.

## Purpose
Generate a complete, funder-ready grant proposal narrative for a new or existing IMAN initiative, following the exact structure and voice of the Crown Family Philanthropies × IMAN Comprehensive Grant Proposal (2025). Output is a full `.md` document that can be immediately handed off or converted to `.docx` using the grant proposal template.

---

## Step 1 — Gather Inputs

When this skill is triggered, ask the user for the following if not already provided. Do not proceed to generation until all required fields are answered:

**Required:**
- **Project / Initiative name** — What is this proposal for?
- **Funder name** — Who is this being submitted to?
- **Grant amount and duration** — e.g., "$2M over 2 years"
- **Focus areas (1–5)** — What are the strategic pillars this proposal covers? (Health, ReEntry, Food, Housing, etc.)
- **Target population** — Who does this serve?
- **Geography** — Which neighborhoods / cities?
- **Long-term vision** — What does success look like in 10 years?

**Optional (improves output significantly):**
- Known outcome metrics for each focus area (actuals or projections)
- Named partners already committed
- Existing funder relationship history
- Any capital or program budget figures
- Current grant funding sources
- Urgency or timing context (e.g., capital campaign underway, legislation pending)

---

## Step 2 — Research Phase

Before writing, read and pull from:

1. **Knowledge Map** (`Data library/Knowledge Map/`) — Find relevant evidence, life-expectancy impact estimates, and intervention data for each focus area named by the user. Pull specific statistics, citations, and impact numbers to use in the proposal body.

2. **IMAN Drive** (`Data library/IMAN Drive/`) — Pull IMAN program data: outcomes, participant counts, program names, dollar figures, and partner lists relevant to the initiative.

3. **Project description** (`Data library/project_description.md`) — For context on IMAN's overall mission and current initiatives.

4. **Crown-IMAN proposal structure** (this skill file) — Follow the section-by-section structure exactly as defined below.

---

## Step 3 — Generate the Proposal

Write the full proposal following this exact structure. Use IMAN's voice throughout (see Voice Guidelines at the bottom). Every section heading must appear in the output, in this order.

---

### COVER BLOCK

```
Comprehensive Grant Proposal
[Funder Name] & IMAN

To:       [Funder Name]
Subject:  [Initiative Name] — Comprehensive Grant Proposal
Amount:   $[X]M over [X] years
Date:     [Month, Year]
Contact:  [Leave blank — for IMAN to fill]
```

---

### TABLE OF CONTENTS

List all sections and focus areas by name. Mirror the original TOC format.

---

### SUMMARY

*Write 3 paragraphs:*

**Paragraph 1:** Open with IMAN's tenure ("For over [X] years..."). Name the core disparity statistic — always lead with the 30-year life expectancy gap between Englewood/South Side and Streeterville if the initiative is Chicago-based. Name the study year. State the urgency this creates.

**Paragraph 2:** Name the strategic plan, its timeframe, and the 3–5 domains this proposal addresses. Connect to the long-term vision of quantitatively reducing the disparity.

**Paragraph 3:** State the ask — dollar amount, duration, funder name — in clear, plain language. Name what this grant will enable. Close with the 10-year vision statement (what changes by [year+10]).

*Do not use bullet points in this section. Prose only.*

---

### BACKGROUND & CONTEXT

*Write 3 paragraphs:*

**Paragraph 1:** IMAN's integrative approach — name the target populations (justice-involved, immigrant, uninsured, food-insecure, etc.), the methods (health center, arts, organizing, workforce), and the framework connecting them.

**Paragraph 2:** Trace the trajectory of IMAN's work in the neighborhood. Name 2–3 specific past investments with dollar figures. Show how small-scale organizing became large-scale transformation. Use real numbers from the IMAN Drive files.

**Paragraph 3:** Name the current strategic plan and how this grant fits into it. End with a transition to the focus areas.

Then add: `~ [STRATEGIC PLAN NAME] ~` as a centered section divider.

Add 1–2 sentences framing the five focus areas and their relationship to the strategic plan.

Add the divider line: `______________________________________________________________________________`

---

### FOCUS AREAS

*For each focus area provided by the user, write one full section using this exact structure:*

#### [Focus Area Name]
*[Goal statement: one sentence. Format: Action verb + what will be built/expanded + for whom + to achieve what outcome. Bold the focus area name at the start.]*

**Current State:**
Describe the existing program or asset. Lead with the most impressive outcome metric. Include:
- Number of unduplicated people served (with year)
- 2–3 specific outcome metrics with numbers (use Knowledge Map data or IMAN program data)
- Any awards, policy recognition, or national attention

**Expansion Plans:**
Name what this grant funds. Break into 2–3 named sub-initiatives. For each:
- Name the sub-initiative
- State the dollar cost ($[X]M)
- State the specific, tangible outcome (units, sq ft, jobs created, people served)
- Name any design partners, policy frameworks, or external validators

Then list the key expansion workstreams in bold:
- **[Workstream name]:** [1-sentence description with a number]
- **[Workstream name]:** [1-sentence description with a number]
- **[Workstream name]:** [1-sentence description with a number]

**PARTNERSHIPS:**
List 5–10 named partners. Include government agencies, hospitals, universities, foundations, and community organizations. Use real partners from IMAN Drive files where possible; label speculative partners as "[target partner]".

*Repeat this block for each focus area. Separate blocks with:*
`______________________________________________________________________________`

---

### BUDGET & SUSTAINABILITY

Write a narrative (no table) covering three categories:

**Earned Revenue**
For each revenue stream, describe: what it is, when it activates, the projected dollar figure or growth trajectory, and any enabling investment (marketing, staffing, etc.).

**Grant Funding**
Name sustaining funders (use IMAN Drive data). Name 2–3 new funding targets or fund types being pursued.

**Operational Optimization**
1–2 sentences on how IMAN will evaluate and optimize operations as programs scale.

Close with: reference to the attached budget document — capital projects tab (sources, uses, gaps per focus area) and comprehensive programmatic budget tab.

---

### [NEIGHBORHOOD]: LEADERSHIP & COALITION

Write 4–6 paragraphs:

1. Frame the neighborhood as a community of resilience and momentum — not deficiency. Acknowledge structural challenges directly but don't lead with them.

2. Data paragraph: Use CMAP or comparable data. Pull 3 metrics showing measurable progress over the last decade (income, unemployment, education). Always cite the source.

3. Name 2–3 cultural leaders, artists, or organizations raising the neighborhood's visibility and fueling investment.

4. List 3–4 catalytic investments already underway with dollar figures. Show IMAN is not alone — it's part of a larger wave.

5. Community governance paragraph: how IMAN navigates political complexity (aldermanic structure, cross-sector coalitions).

6. Closing ask: "With your support, we can accelerate this progress and ensure [neighborhood] thrives as a vibrant, unified community."

---

### SPIRITUAL & CULTURAL IMPERATIVE OF THE WORK

Write 4–5 paragraphs. This is IMAN's most distinctive section — do not make it generic.

1. IMAN's unique position: Muslim values + multifaith coalition + social justice movement. Name the faith-rooted framework.

2. Community organizing as spiritual practice: how IMAN centers communal healing.

3. Specific example of multifaith coalition work: name the partners, the outcome, and its lasting significance. (Use the MLK memorial example if no project-specific example is provided.)

4. The current moment: connect the political, cultural, or communal context to the urgency of this specific partnership. Be direct. Name the context (political uncertainty, community vulnerability, specific events). This paragraph changes with every proposal — never reuse verbatim.

5. The model's significance: IMAN as a replicable model for how people with shared values can address seemingly intractable problems — even amid intensely challenging circumstances.

---

### CASE STUDIES & VALIDATION FOR THE WORK

Open with an academic/expert quote (from a named Northwestern, UChicago, Rush, or other university partner) validating the multilevel approach. If a real quote isn't available, write a placeholder: `"[Quote — request directly from [specific researcher / institution]]"`

Write 1–2 sentences framing the comparable models.

Then list 3–5 organizations in this format:
- **[Org Name]** ([City]): [Focus area]. [1 sentence on why it validates IMAN's approach.]

Close with: "Enclosed with this report are case studies of these and other organizations making deep and lasting change in communities through a comprehensive approach. Also included are summaries of relevant academic journal articles and intersections with IMAN's work."

---

## Step 4 — Save Output

Save the completed proposal to:
```
Data library/Consulting/[current week folder]/[Initiative Name] Grant Proposal.md
```

Then tell the user:
- The file path
- How many focus areas were covered
- Which Knowledge Map domains were drawn on
- Any fields left as placeholders that require IMAN input (metrics, partner names, budget figures)
- Offer to convert to `.docx` using the grant proposal template: "Would you like me to build this into a Word document using the Crown-IMAN template?"

---

## Voice Guidelines

IMAN's grant writing voice has four qualities. Apply all four throughout:

**1. Dignified, not pitying.**
Never frame the community or its residents as victims or as problems to be solved. Frame them as people facing structural barriers that IMAN is dismantling. Wrong: "Englewood residents suffer from poverty and violence." Right: "Englewood residents face systemic disinvestment that IMAN is working to reverse — and the community's resilience and organizing capacity make that reversal possible."

**2. Earned, not aspirational.**
Every claim should be backed by a number or a named partner. The tone is: "We have done this, here is the proof, here is what we'll do next." Avoid: "IMAN hopes to..." or "We believe that..." Use: "IMAN will..." or "IMAN has..."

**3. Integrated, not siloed.**
Always connect the initiative being proposed to at least one other IMAN program or asset (Health Center, Fresh Market, Green ReEntry, Griot Plaza, IMAN Oasis). IMAN's entire model is that programs reinforce each other. Show this.

**4. Urgent, not alarmist.**
The 30-year life expectancy gap is the north star metric. Reference it in the Summary and at least one other section. The urgency is structural and data-backed — never emotional or rhetorical.

---

## Constraints

- Do not invent statistics. Pull from Knowledge Map, IMAN Drive files, or label as "projected [source]."
- Do not use bullet points in the Summary or Background sections — prose only.
- Named partners > generic descriptions. "Northwestern Memorial Hospital" beats "a major academic medical center" every time.
- State the dollar ask clearly in the Summary. Do not bury it.
- Every focus area section must include at least 3 quantified metrics.
- The Spiritual & Cultural section must reference a specific, current moment — never recycle language from the Crown-IMAN proposal verbatim.
- Target length: 12–18 pages of narrative (excluding appendices).
