# `regen/` — Enrichment & PII patches

This folder is a **session log + a set of idempotent enrichment patches**
applied to the seed corpus in May 2026. It is kept in-tree (rather than
folded back into the original generators) for transparency: anyone curious
about how the corpus reached its current form can read the briefs / progress
notes here and re-run any patch.

## What's in here

| File | Purpose |
|---|---|
| `PROGRESS.md` | Session log — what was generated when, by which agent, how the parallel runs were dispatched. |
| `AGENT_BRIEF.md` | Brief given to the parallel generation agents (canonical facts, helper API, quoting rules, type-dependent word-count targets). |
| `PII_BRIEF.md` | Brief given to the parallel PII-scan agents (categories A-D, regex patterns, whitelists). |
| `PII_REPORT.md` | Master PII audit report with remediation log. |
| `fix_real_persons.py` | Surgical idempotent replacement of real-person / real-entity references with fictional equivalents (the PII remediation pass). |
| `regen_mueller_*.py` (8 scripts) | Per-folder enrichment of the Müller dataset. |
| `regen_biotech_all.py` | Enrichment of the BioTech dataset. |
| `regen_roehrig_*.py` (17 scripts) | Per-folder enrichment of the Brennhagen dataset (one script per top-level folder or group). |
| `pii_findings_*.md` | Per-agent PII findings (raw output from the 12-agent scan). |
| `_oss_fix_paths.py`, `_oss_restructure.py` | One-shot housekeeping scripts for the open-source release (path portability, folder renames, junk cleanup). |

## Reproducing the patches

All patch scripts are idempotent — re-running them overwrites the target
docx/xlsx files with deterministic output and is safe.

```bash
# Apply every patch in lexical order:
for f in regen/regen_*.py; do python3 "$f"; done
python3 regen/fix_real_persons.py
```

## How the patches came about

The original generators (`generate_mueller.py`, `generate_biotech.py`,
`generate_roehrig.py`) produce a seed corpus of ~3,475 docx files but at very
low per-document word count (median ~60 words). The patches in this folder
re-write each docx with realistic, type-appropriate German legal/business
content (median ~290 words; range 130–1,500 depending on type). They were
dispatched as parallel sub-agents — see `AGENT_BRIEF.md` for the brief each
agent received and `PROGRESS.md` for the dispatch log.

A follow-up PII sweep (12 parallel agents, `PII_BRIEF.md`) verified the
enriched corpus, identified ~16 real-person collisions introduced during
enrichment, and produced a remediation script (`fix_real_persons.py`) that
fixed every collision deterministically.
