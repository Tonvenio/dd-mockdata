# Datasheet — dd-mockdata v1.0

A Datasheet-for-Datasets style description (after Gebru et al., 2021).

## Motivation

**For what purpose was the dataset created?**
To provide the German legal-tech research community with a large, openly
licensed, realistic synthetic corpus of M&A / due-diligence documents that can
be used for information extraction, retrieval-augmented generation, document
classification, knowledge-graph construction, and benchmarking long-context
language models on real-world-style German legal/business prose.

Most existing German legal corpora are either (a) too small, (b) court-decision
heavy and stylistically narrow, or (c) drawn from real proprietary deals and
therefore unshareable. dd-mockdata addresses the gap with a fully fictional
multi-company corpus at three realistic scales.

**Who funded the dataset?** Self-funded; no external sponsorship.

## Composition

**What do the instances represent?** Individual German-language documents
typically found in an M&A or due-diligence virtual data room: contracts,
corporate-governance protocols, board resolutions, financial reports, HR
records, intercompany agreements, regulatory filings, IP filings, patent
documents, quality-assurance reports (IATF 16949 / VDA 6.3), works-council
minutes, supplier audits, project gates / lessons-learned, IFRS accounting
policies, transfer-pricing documentation, capital-markets disclosures,
insurance policies, real-estate leases.

**How many instances?** 6,265 files in total:

| Dataset | Profile | Files | DOCX | XLSX | PDF |
|---|---|---:|---:|---:|---:|
| `mueller_small/` | Mittelständischer Sondermaschinenbau, ~250 MA, ~50 Mio. EUR Umsatz, familiengeführt | 311 | 211 | 50 | 39 |
| `biotech_medium/` | Wachstums-Medizinproduktehersteller (Cardevio/Ostevo/Veridiq), ~600 MA, ~90 Mio. EUR, VC-finanziert (Sofinnova/Lakestar) | 950 | 161 | 149 | 625 |
| `roehrig_large/` | Börsennotierte Automotive-Tier-1-Holding (Prime Standard) mit 6 Tochterwerken DE/PL/CZ/HU/CN, ~4.200 MA, ~612 Mio. EUR | 5,053 | 3,104 | 1,648 | 277 |
| **Total** | | **6,265** | **3,476** | **1,847** | **941** |

**Topical coverage** (per dataset, see `<dataset>/00_*` and subfolder names):
governance, finance, HR, customer contracts, supplier contracts, real estate,
IP/licensing, insurance, compliance, IT infrastructure, strategy & planning;
plus for the larger sets: subsidiary entities, transfer pricing, IFRS,
capital-markets / IR, M&A history, IATF quality management, works councils,
pensions (bAV), project portfolio.

**Median per-document length** (DOCX): ~290 words; range 130–1,500. The
distribution reflects the realistic mix of contracts (long), reports (medium)
and certificates / invoices (short).

**Does the dataset contain all possible instances or a sample?** It is a
generated sample tuned to be representative of a real DD virtual data room
for the three company profiles.

## Collection process

**How was the data acquired?** The corpus was procedurally generated using the
Python scripts included in this repository:

- `generate_mueller.py`, `generate_biotech.py`, `generate_roehrig.py` —
  original generators that produce the seed corpus per company.
- `enhance_lib.py` — shared facts and a `write_doc()` helper used across all
  generators and patches.
- `regen/regen_*.py` — incremental enrichment patches that lift document
  length and realism (a generative pass added in 2026-05).
- `regen/fix_real_persons.py` — a PII remediation patch (see below).

**Time frame.** Initial generation 2026-05-19; enrichment + PII sweep
2026-05-26 to 2026-05-29. All in-document dates referenced are fictional
(typically 2018–2024 spread across the corpus).

## Pre-processing / cleaning / labelling

**PII audit.** A 14-agent parallel sweep (`regen/PII_REPORT.md`) verified
the corpus contains no real IBANs (mod-97 valid + non-whitelist), no German
Steuer-Identifikationsnummern, no Sozialversicherungsnummern, no Polish PESEL,
no Hungarian TAJ, no Chinese national-ID numbers, no Luhn-valid credit card
numbers, no public-domain personal email addresses, and no embedded photos
or signatures. Sixteen real-person collisions (industry figures, academics,
auditors) introduced during enrichment were rewritten to fictional equivalents
via `regen/fix_real_persons.py`.

**What the corpus does contain.** Real *organisational* names appear as
fictional counterparties / service providers (BMW, VW, Mercedes, KPMG,
Hengeler Mueller, RWTH Aachen, TU München, Allianz as insurer, etc.). No
business relationship, statement of fact, or endorsement should be inferred.

## Uses

**Intended use cases.** Legal-tech research, including:

- Long-document Information Extraction (NER, relation extraction, key-value
  extraction from contracts)
- Retrieval-Augmented Generation (RAG) evaluation on cross-document German
  legal queries — e.g. "Liste alle Aufsichtsratsmitglieder und ihre
  Vergütung 2023"
- Document classification (24+ document types across 24 dataset folders)
- Cross-document consistency / contradiction detection
- Knowledge-graph construction from a multi-entity holding corpus
- Benchmarking long-context LLMs on realistic German business prose
- Generative-pipeline evaluation (the included generators are themselves a
  template / parameterized-prose research artefact)

**Tasks the dataset is NOT suitable for.** Training a language model on real
German legal style — the corpus is generated, so it carries the stylistic
fingerprints of `python-docx` paragraph construction and the LLM prompts
used in the enrichment pass. It is best used as an evaluation set or as a
controlled environment for prototyping pipelines.

**Distribution.** GitHub repository, dual-licensed: code MIT, data CC-BY-4.0.

## Maintenance

**Who maintains the dataset?** Marc Ohrendorf (initial release).
Contributions welcome via pull request.

**How to report errors or PII concerns?** Open an issue on GitHub.

**Will the dataset be updated?** Future revisions may add a paired
knowledge-graph / ground-truth annotation layer; further document types
(BAFin-Bescheide, Bundesanzeiger-Veröffentlichungen, Schiedsverfahren-Akten);
or English-language counterparts for cross-lingual research.
