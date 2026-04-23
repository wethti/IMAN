# Deliverable Package — IMAN 2040 Evidence Base

This folder is the client- and investor-facing output of the 2026-04-21 overnight research run. Everything here is written for humans who will not read the appendices.

## What's in the package

Two layers: the original research deliverables (numbered) and the client-facing narrative set (lettered). Everything rests on the same evidence base. The C-series translates it for meetings, leave-behinds, and pitches.

### Narrative / client-facing set (use in live meetings)

| # | File | Audience | Time to read | Format |
|---|---|---|---|---|
| C1 | `C1_client_narrative_brief.md` | Client partner / IMAN CEO | ~10 min | Story-driven brief (SCQA arc) |
| C2 | `C2_pitch_deck.pptx` | Funders, boards, public audiences | 18 slides · ~25 min presented | PowerPoint — editable, 16:9 widescreen, native charts and icons |
| C3 | `C3_leave_behind_card.html` | Anyone you met with | 90 seconds | Print-to-letter one-pager |

### Research deliverables (the evidence underneath)

| # | File | Audience | Time to read |
|---|---|---|---|
| 1 | `01_executive_brief.md` | Consulting client — partner / CEO | 5 min |
| 2 | `02_investor_onepager.md` | Funder / philanthropist / social-impact investor | 2 min |
| 3 | `03_measurement_plan.md` | Client analytics lead | 15 min |
| 4 | `04_peer_and_positive_deviant_atlas.md` | Strategy team | 15 min |
| 5 | `05_appendix_evidence_tables.md` | Researchers / due-diligence | reference |
| 6 | `06_handoff_memo.md` | IMAN analytics lead (internal) | 5 min — what shipped, what didn't, what to do next |

### Consultant-only (not for external distribution)

| # | File | Audience | Time to read |
|---|---|---|---|
| U1 | `../internal/U1_data_provenance_memo.md` | Project owner (consultant) | ~20 min — how the data was pulled, by which tool, where saved, which initiatives can and cannot be evaluated with what we have |

## Reading order by use case

- **Before a board meeting**: `C1_client_narrative_brief.md` → then flip to the data tables in `05_appendix_evidence_tables.md` that you need.
- **Funder pitch**: present `C2_pitch_deck.pptx`; leave behind `C3_leave_behind_card.html` (print one copy per attendee).
- **Handing to the IMAN analytics team**: `03_measurement_plan.md` + `06_handoff_memo.md`.
- **Due diligence from a funder's epidemiologist**: `05_appendix_evidence_tables.md` + `../verification/claims_log.csv`.
- **Consultant's own reference** (what we actually have, what we don't, what to do next): `../internal/U1_data_provenance_memo.md`.

## Provenance

Every numeric claim is keyed to `../verification/claims_log.csv`, which merges the per-stream verification logs. If a claim in any file above is unsourced, it's a bug — open it and check the verification log. For a narrative account of how the data was pulled, with which tool, and where it sits, see `../internal/U1_data_provenance_memo.md`.

## Version

Compiled 2026-04-21 from the parallel outputs of Streams A–F. Next update: after the first synthetic-control run on peer data (target Q3 2026).
