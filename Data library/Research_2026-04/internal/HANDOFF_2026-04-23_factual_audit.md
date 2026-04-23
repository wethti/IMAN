# Handoff — Factual Audit + Correction Pass (2026-04-23)

**For:** the next Claude Code agent (fresh session, possibly on a different machine)
**From:** prior session — context was about to be lost
**User:** dpo120000@gmail.com (consultant)

---

## Read this first

The user's last message in the prior session: they want a correction pass applied to the IMAN 2040 research package. An independent factual audit has already been run — findings are below. Your job is **not** to re-audit. Your job is to apply the corrections once the user tells you which scope (Option A / B / C, see bottom of this file).

The user's prior-session frustration (paraphrased): *"I asked you to double- and triple-check every number. You shipped a deck and narrative with factual errors. People's lives are at stake."* Trust is burned. Be surgical. Confirm scope before editing anything.

From the user's auto-memory (`MEMORY.md`):
- **Project:** IMAN Knowledge Map — closing the 30-yr LE gap in Englewood/Chicago Lawn, Chicago
- **Collaboration preference:** "Double-check every number, frame for investors and non-technical clients"

---

## The task at a glance

Apply fact-based corrections to the IMAN 2040 research package. 11 artifacts are affected; the **appendix (`05_appendix_evidence_tables.md`) and handoff memo (`06_handoff_memo.md`) are correct and should be treated as ground truth**. Errors all live in the narrative/pitch layer that sits on top of them.

---

## State of play

- ✅ Independent factual audit **completed** (findings table below, reproduced from the background agent output)
- ✅ Parallel review by the prior Claude also done (same findings + the numeric-drift table)
- ✅ Consolidated fix plan in 3 scope tiers (A / B / C) presented to user
- ⏳ **User decision pending** on Option A vs B vs C before any artifact is touched
- ❌ No corrections applied yet

---

## The findings — ship/no-ship by artifact

| Artifact | Verdict |
|---|---|
| `deliverable/05_appendix_evidence_tables.md` | **Ship as-is.** Substantively correct; meets epidemiologist-due-diligence bar. |
| `deliverable/06_handoff_memo.md` | **Ship as-is** (internal). Correctly flags its own limits. |
| `internal/U1_data_provenance_memo.md` | **Ship as-is** (internal, consultant-only). Honestly flags that no datasets were actually downloaded. |
| `deliverable/04_peer_and_positive_deviant_atlas.md` | **Ship after minor citation tightening** on Little Village + Chicago Lawn. |
| `deliverable/C1_client_narrative_brief.md` | **3 surgical fixes** needed (Victor geography, Victor effect size, READI framing; title/gap reconciliation). |
| `deliverable/01_executive_brief.md` | **Minor fixes** — split "10.6–15 yr gap" into two comparisons; align LE projection with C1 (3–5 yr, not 3–7). |
| `deliverable/03_measurement_plan.md` | **Minor** — restore the 16th peer community in the enumeration (currently lists 15). |
| `deliverable/02_investor_onepager.md` | **Do not ship until corrected.** Multiple misattributions + overstated figures. |
| `deliverable/C3_leave_behind_card.html` | **Do not ship until corrected.** LOSARTAN fabrication, Streeterville citation wrong, Deng misattribution. |
| `tmp-pitch/build_pitch.py` → `deliverable/C2_pitch_deck.pptx` | **Do not ship until corrected.** Same issues as C3, plus slide 08 unsourced decomposition, slide 11 unsourced +2.0 yr Dudley Street. |

---

## Tier 1 — factual errors (must fix before ship)

| # | Error | Where | Fix |
|---|---|---|---|
| 1 | **"Streeterville 90.0 (CDPH 2023)"** is wrong. CDPH 2023 highest-LE CA is **The Loop at 87.3**. The 90.0 traces to NYU City Health Dashboard USALEEP 2010-2015 — different dataset, different geography, different vintage. | C1 §I, C3 number band, 01 opening, 02 headline, `build_pitch.py` slide 01 | Drop to "The Loop 87.3 (CDPH 2023) · Englewood 67.7 · 19.6-year gap" **OR** keep 90.0 and cite "NYU City Health Dashboard, USALEEP 2010-2015." Not CDPH 2023. |
| 2 | **"LOSARTAN"** attributed to Victor 2018 — fabricated | C3 evidence strip | Remove. Intervention was pharmacist-led multi-class titration. |
| 3 | **"a nearby Black community"** for Victor | C1 §II | Change to **"Los Angeles"** (Victor 2018 was 52 barbershops in LA County) |
| 4 | **"27 mm Hg" as treatment effect** — that's within-arm. Between-group ATE is **21.6 mm Hg** (95% CI −28.4 to −14.7) | C1 §II, C3 evidence strip | Use "21.6 mm Hg between-group" or secondary-outcome form "63.6% vs 11.7% reached BP control (secondary)" |
| 5 | **Deng/Mozaffarian HA 2025 cited for Fresh Market / Fresh-food access** — Deng is **medically tailored meals** for dual-eligible Medicare-Medicaid pts, not fresh food | 02 scorecard row, C3 evidence row | Re-cite Philadelphia Healthy Corner Store Initiative (Cassady/Jetter 2013; Dannefer AJPH 2012) |
| 6 | **"VanderWeele, JAMA 2017 — 4-14 additional years LE"** — fabricated combination. VanderWeele 2016 JAMA Intern Med = 33% mortality HR. "4–14 yrs" is Buettner/Blue Zones | 02 §"4 replicable features" item 2 | Pick one: "VanderWeele 2016 JAMA Intern Med: 33% lower all-cause mortality (HR 0.67) with weekly religious attendance" OR "Blue Zones (Buettner / Pes & Poulain): 4–14 yrs LE associated with faith, diet, purpose" — **never combined** |
| 7 | **Dudley Street +2.0 yr LE** — DSNI has no peer-reviewed LE effect. Unsourced. | `build_pitch.py` slide 11 | Remove. Replace with Branas PNAS 2018 greening cluster-RCT (29% reduction in gun assaults; 42% reduction in depression) |
| 8 | **READI "cut serious violence in half"** — primary composite outcome was **null**. −65% full sample is p≈0.13 FDR. Only **−79% outreach subgroup** is statistically significant | C1 §II, C3 evidence row, 02 scorecard, `build_pitch.py` slide 13 | Exactly: *"79% reduction in shooting/homicide arrests in pre-specified outreach-referred subgroup (Bhatt et al., QJE 2024; statistically significant after adjustment). Primary composite violence outcome did not reach significance."* |

## Tier 2 — numeric drift (appendix ground truth vs narratives)

| Claim | Appendix | C1/02/C3/deck | Recommendation |
|---|---|---|---|
| Medicaid LE gain | 0.7 yr (A-HC3-01) | 1.1 yr | **0.7** everywhere |
| Barbershop BP LE gain | 0.6 yr (A-HC4-01) | 0.8 yr | **0.6** everywhere; label as modeled from 21.6 mm Hg ATE |
| READI / CVI LE gain | 1.2 yr (appendix table 1 row 31) | 0.7 yr | **Reconcile:** the 1.2 uses −65% full sample (not sig. after FDR). Honest derived figure using only the significant −79% subgroup is ~0.7–0.9 yr. Prefer 0.9 everywhere with footnote. |
| Fresh Market LE gain | 0.8 yr (FA1) | 0.5 yr | **0.4–0.8 range** with uncertainty noted; cite Drake 2026 null on produce-Rx honestly |
| Green infra / PM2.5 | 0.3 yr (MT1) | 0.4 yr | **0.3** everywhere |
| Green ReEntry housing+workforce | 1.3 yr (HO3 0.5 + IM3 0.8) | 2.0 yr | **1.3** with component breakdown |

## Tier 3 — internal inconsistencies

- **C1 title "30-year gap" vs §0 "11 fewer years"** — no Chicago pair produces 30. Recommend retitle to **"Why a 20-year life-expectancy gap exists"** (Englewood 67.7 vs Loop 87.3 = 19.6, CDPH 2023) and align §0 accordingly.
- **LE gain projection: C1 "3–5 yr" vs 01 exec brief "3–7 yr"** — align on **3–5 yr**.
- **16 peer communities** — `03_measurement_plan.md` enumerates 15. Reconcile with `peer_neighborhoods/01_client_canonical_list.md`.
- **"10.6–15 year gap" in 01** — two distinct comparisons (Black-vs-White 10.6; Black-vs-Asian/PI 15.0), not a range. Split into two sentences.
- **Little Village distance: C1 "3 miles" vs 02 "10 miles"** — actual ~5-7 miles. Standardize.
- **`build_pitch.py` slide 08 decomposition** (14.1→10.8→9.4→8.1→5.0) — no cited source; likely team's own regression. Either cite as "research-team analysis of CDC USALEEP + ACS covariates; methodology in appendix" **and** add the methodology to 05_appendix OR remove specific coefficients.
- **`build_pitch.py` slide 02 Chicago Lawn "73.9"** — appendix + handoff memo flag this as bounded inference (UNVERIFIED). Widen to "~72–75 (bounded estimate; CDPH 2023 does not separately publish Chicago Lawn CA 66)" or drop.

---

## Options on the table (user must pick before you edit)

**Option A — Full fix pass across all 11 artifacts.** ~4-6 hours. Every figure survives funder-epidemiologist review. Package loses the "90.0 Streeterville" and "cut violence in half" dramatic numbers; gains defensibility.

**Option B — Critical-errors-only pass** (Tier 1 + the LE-projection / gap / peer-count inconsistencies in Tier 3). ~2 hours. Nothing in the package is demonstrably false; some minor numeric drift between appendix and narratives remains.

**Option C — Start with safe demonstrably-false fixes** (LOSARTAN, "nearby Black community", Dudley +2.0 yr, VanderWeele, Deng attribution, 15→16 peer count); pause before touching story-level numbers (Streeterville framing, READI framing, title/gap reconciliation) so the user can make those editorial calls.

**If the user has already responded with a choice, honor it. If not, ask once, then proceed.**

---

## After edits are applied

1. **Rebuild the deck.** `cd "Data library/Research_2026-04/tmp-pitch"` then `python build_pitch.py` (or equivalent on the new machine — see Environment notes at bottom). Deck overwrites `../deliverable/C2_pitch_deck.pptx`.
2. **Re-verify numeric consistency across artifacts.** Grep the same claim across all 11 files; same number, same source, same phrasing.
3. **Append corrections to `verification/claims_log.csv`** — for every figure you change, update the row (or add a new row) with status `verified` + primary-source URL.
4. **Do not delete `tmp-pitch/`** — it's the build scaffold. Clean-up was deferred in the prior session.

---

## Ground-truth sources (use these; don't hunt)

### Primary sources for the claims in play

| Claim | Primary source | Verified? |
|---|---|---|
| Englewood LE 67.7 (2023) | CDPH 2023 Healthy Chicago Data Brief: Life Expectancy | ✅ |
| Chicago citywide LE 78.7 (2023) | Same | ✅ |
| The Loop LE 87.3 (highest CA) | Same | ✅ |
| Streeterville LE 90.0 | NYU City Health Dashboard, USALEEP 2010-2015 tract-level (NOT CDPH) | ✅ |
| Victor barbershop trial | Victor, Lynch, Gelfand et al., *NEJM* 2018;378:1291-1301. Primary outcome: −21.6 mm Hg between-group SBP at 6 mo (95% CI −28.4 to −14.7). Secondary: 63.6% vs 11.7% BP control. **Los Angeles County, 52 barbershops, N=319 Black men.** | ✅ |
| READI Chicago | Bhatt, Heller, Kapustin, Bertrand, Blattman, *QJE* 2024;139(1):1-56. **Primary composite outcome: null.** Secondary −65% shooting/homicide arrests (p≈0.13 FDR). Subgroup −79% in outreach-referred (sig. after adjustment). BCR 4:1 to 18:1. | ✅ |
| Sommers Medicaid mortality | Sommers, Baicker, Epstein, *NEJM* 2012;367:1025-1034. −6.1% relative / −19.6 per 100k absolute. 3 expansion states vs 4 controls. | ✅ |
| Deng MTM | Deng, Thorndike, Mozaffarian et al., *Health Affairs* 2025. **Medically tailored meals** for dual-eligible Medicare-Medicaid. 47% hospitalization reduction. **Not fresh food / not produce Rx.** | ✅ |
| Branas greening | Branas, South, Kondo et al., *PNAS* 2018;115(12):2946-2951. 29% reduction in gun assaults; 42% reduction in depression. **Did not measure CV mortality.** | ✅ |
| Sampson collective efficacy | Sampson, Raudenbush, Earls, *Science* 1997;277:918-924. 2-SD increase → 40% lower homicide. | ✅ |
| Palloni Hispanic salmon-bias | Palloni & Arias, *Demography* 2004;41(3):385-415. Mexican-origin foreign-born LE overstated by 3–5 yrs due to return-migration. | ✅ |
| Walley naloxone | Walley, Xuan, Hackman et al., *BMJ* 2013;346:f174. **46% is the high-implementation stratum** (>100 enrollees/100k). Overall 27%. | ✅ |
| VanderWeele religious attendance | Li, Stampfer, Williams, VanderWeele, *JAMA Intern Med* 2016. 33% lower all-cause mortality (HR 0.67, 95% CI 0.62–0.71), women >1x/week. **No "4–14 years" figure in this paper.** | ✅ |
| Asa vacant lots | Asa et al., *AJPH* 2026. DiD 2007-2023: −30% agg. assault; −56.6 per sq mi/yr (95% CI −97.9 to −15.2). **Did not measure CV mortality.** | ✅ |
| Macinko Brazil | Macinko et al., *J Epi Comm Health* 2006: **infant mortality** 13-22% reduction. LE effect is Rasella et al. *Lancet* 2014, not Macinko. | ✅ |
| Bailey FQHC mortality | Bailey & Goodman-Bacon, *AER* 2015. ~2% adult mortality reduction sustained over decades. | ✅ |

### Internal ground-truth files (trust these when conflicts arise)

- `deliverable/05_appendix_evidence_tables.md` — **the master appendix.** Tables 1–6 are the numeric bible.
- `verification/claims_log.csv` — 234 claims, status-tagged. Note: rows marked `needs_verification` are still suspect; the audit elevated several of those to "primary-source confirmed" (see primary-sources table above).
- `internal/U1_data_provenance_memo.md` — honest account of what was and wasn't done. **Section 1: "We did not actually download any of the 40+ datasets."** Keep this in mind if anyone challenges a number.

---

## Environment notes (for the new machine)

### What you need

- Python 3.10+
- `pip install python-pptx matplotlib pillow markitdown[pptx]`
- For deck-to-PDF verification: LibreOffice (`soffice`) + Poppler (`pdftoppm`) — used by the pptx skill for visual QA
- PowerPoint is **not** required; the prior build used COM automation as a convenience but `python-pptx` builds the deck directly
- Git (if you're cloning)

### How to get the repo onto the new machine

The `Research_2026-04/` directory is currently **untracked** in the git working tree (see `git status`). To transfer:

**Option 1 — push from the old machine, clone on the new:**
```bash
# On OLD machine (Windows, at c:/Users/piggl/Documents/IMAN)
git add "Data library/Research_2026-04/" .claude/ .mcp.json
git commit -m "[auto] Stage Research_2026-04 package for handoff"
git push origin main
# On NEW machine
git clone https://github.com/wethti/IMAN.git
cd IMAN
```
⚠️ Check for secrets before pushing — `.claude/` and `.mcp.json` may contain local tool/MCP config. Review with `git diff --cached` first.

**Option 2 — rsync/scp the folder directly** (safer if `.claude/` has machine-specific paths):
```bash
# From old machine
rsync -a "c:/Users/piggl/Documents/IMAN/" user@new-machine:/path/to/IMAN/
# or use a USB drive / cloud storage for the whole folder
```

### The memory system does not transfer

Auto-memory at `C:\Users\piggl\.claude\projects\c--Users-piggl-Documents-IMAN\memory\` is **local to the old machine.** On the new machine Claude Code will start with empty memory. The memory summaries you need are embedded at the top of this handoff ("Read this first" section).

### Path caveats

All absolute paths in this handoff start with `c:\Users\piggl\Documents\IMAN\`. On a non-Windows new machine, the equivalent is whatever path you cloned into. Use relative paths when possible: everything lives under `Data library/Research_2026-04/`.

---

## What to say to the next Claude Code agent

Copy-paste this prompt after starting Claude Code in the repo root on the new machine:

> I'm resuming work from another machine. Read `Data library/Research_2026-04/internal/HANDOFF_2026-04-23_factual_audit.md` in full — it has the task context, the completed audit findings, the fix plan in three scope tiers, and ground-truth sources. Do not re-audit; the audit is done. Confirm you've read the handoff, tell me which scope option I previously chose (if I've said), and if I haven't, ask me to pick A / B / C before touching any artifact.

If you've already decided between A / B / C, add that to the prompt:

> ...Proceed with **Option [A/B/C]** from that handoff.

---

## TODO state at handoff

1. ✅ Independent audit of C1, C3, 01, 02, 05, U1 against claims_log.csv + appendix tables
2. ✅ Background blog-researcher primary-source verification complete
3. ✅ Cross-checked independent findings against agent findings — overlap is substantial, this handoff is the consolidation
4. ⏳ Present findings table to user; get approval on correction scope — **done in the prior session; response awaited**
5. ⏳ Apply corrections across artifacts per chosen scope
6. ⏳ Rebuild C2 pitch deck from corrected `build_pitch.py` text
7. ⏳ Re-verify numeric consistency across artifacts

---

*Compiled 2026-04-23 from two independent review passes (automated blog-researcher agent + parallel manual review). If anything in this handoff contradicts `05_appendix_evidence_tables.md`, trust the appendix.*
