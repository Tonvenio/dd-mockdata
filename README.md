# dd-mockdata

A **synthetic German legal due-diligence corpus** for legal-tech research —
6,265 documents (DOCX + XLSX + PDF) modelled on the contents of a realistic
M&A virtual data room, generated for three fictional companies at three scales.

Dual-licensed: **code MIT** ([LICENSE](LICENSE)), **data CC-BY-4.0** ([LICENSE-DATA](LICENSE-DATA)).

> **For research and educational use.** dd-mockdata exists to support research
> and teaching in legal-tech, NLP and knowledge engineering. Every entity,
> person, contract, financial figure and identifier is **fictional**; it is
> **not** legal or financial advice and must not be used for decisions about
> real people or organisations.

> 📊 **Knowledge-graph companion:** a structured RDF / Neo4j knowledge graph
> built from this corpus lives at
> [**dd-mockdata-knowledge-graph**](https://github.com/Tonvenio/dd-mockdata-knowledge-graph)
> — companies, subsidiaries, people, contracts, patents and financial covenants
> with provenance back to the source documents, plus RAG / IE / contradiction
> evaluation harnesses.

---

## Datasets at a glance

| Path | Profile | Files | Total size |
|---|---|---:|---:|
| [`mueller_small/`](mueller_small/) | **Halbreiter Maschinenbau GmbH** — mittelständischer Sondermaschinenbau, ~250 MA, ~50 Mio. EUR Umsatz, familiengeführt (60/40 Familien-GbR). | 311 | 8.8 MB |
| [`biotech_medium/`](biotech_medium/) | **Sentavia Precision GmbH** — Medizinprodukte-Wachstumsunternehmen (Cardevio Pro / Ostevo Navigator / Veridiq SARS-Flex), ~600 MA, ~90 Mio. EUR, VC-finanziert (Sofinnova, Lakestar). | 950 | 9.9 MB |
| [`roehrig_large/`](roehrig_large/) | **Brennhagen Elektronik AG** — börsennotierte Automotive-Tier-1-Holding (Prime Standard seit 14.10.2022), 6 Tochterwerke in DE/PL/CZ/HU/CN, ~4.200 MA, ~612 Mio. EUR Konzernumsatz. | 5,053 | 135 MB |
| **Total** | | **6,265** | **~155 MB** |

Each dataset is organised in DD-typical Datenraum-Ordnerstruktur
(01_Gesellschaftsrecht, 02_Finanzen, 03_Personal_HR, etc.). The largest
dataset (Brennhagen) has 24 top-level folders covering subsidiary entities,
transfer-pricing local files, IFRS bilanzierungsrichtlinien, IATF 16949
quality docs, capital-markets / IR, M&A history, works-council minutes,
pensions (bAV) and a 449-doc project portfolio.

> All entities, persons, contracts, financials and identifiers are
> **fictional**. Real organisational names (BMW, KPMG, RWTH Aachen, etc.)
> appear as fictional counterparties — no relationship to actual companies
> should be inferred. See [DATASHEET.md](DATASHEET.md) and
> [`regen/PII_REPORT.md`](regen/PII_REPORT.md).

## Quickstart

```bash
git clone https://github.com/Tonvenio/dd-mockdata.git
cd dd-mockdata
pip install -r requirements.txt           # only needed to re-run generators

# read a document
python3 - <<'PY'
from docx import Document
d = Document("roehrig_large/01_AG_Gesellschaftsrecht/REA_HV_Protokoll_2023.docx")
for p in d.paragraphs[:10]:
    print(p.text)
PY
```

To regenerate (re-run any patch script — they are all idempotent):

```bash
python3 regen/regen_mueller_01.py        # rebuilds a folder's worth of docs
python3 regen/fix_real_persons.py        # the PII remediation pass (no-op now)
```

## Why does this exist?

Open German legal-tech corpora are scarce. Most are court decisions
(stylistically narrow), too small, or drawn from real proprietary deals and
therefore unshareable. dd-mockdata is meant to fill the **synthetic
multi-company, multi-scale, multi-document-type** gap for evaluation and
prototyping of:

- Information extraction & NER on long German legal/business prose
- Retrieval-Augmented Generation evaluation (cross-document queries)
- Document classification across realistic doc-type taxonomies
- Cross-document consistency / contradiction detection
- Knowledge-graph construction from a multi-entity holding structure
- Long-context LLM benchmarking on realistic German documents

See [DATASHEET.md](DATASHEET.md) for the full motivation, composition,
collection process, intended uses, and limitations.

## Repository layout

```
dd-mockdata/
├── README.md             you are here
├── LICENSE               code license — MIT
├── LICENSE-DATA          data license — CC-BY-4.0 (the 3 corpora)
├── DATASHEET.md          datasheet-for-datasets (Gebru et al. 2021)
├── CITATION.cff          academic citation
├── requirements.txt
│
├── mueller_small/        DATA — Halbreiter Maschinenbau (311 files)
├── biotech_medium/       DATA — Sentavia Precision (950 files)
├── roehrig_large/        DATA — Brennhagen Elektronik AG (5,053 files)
│
├── enhance_lib.py        Canonical facts (people/companies/products) +
│                         shared write_doc()/signatures() helpers
├── legal_templates.py    Clause / boilerplate library
├── generate_mueller.py   Original generators — produce the seed corpus
├── generate_biotech.py
├── generate_roehrig.py
│
└── regen/                Incremental enrichment + PII patches (May 2026)
    ├── PROGRESS.md       Session log (what was generated when, by which agent)
    ├── AGENT_BRIEF.md    Brief for the parallel generation agents
    ├── PII_BRIEF.md      Brief for the parallel PII-scan agents
    ├── PII_REPORT.md     Master PII audit report
    ├── fix_real_persons.py   Surgical PII remediation patch
    └── regen_*.py        ~30 per-folder regeneration scripts
```

All paths in the Python scripts are resolved from the location of
`enhance_lib.py` (walked upward via a small prelude), so scripts work no
matter where you clone the repo.

## Reproducing the dataset from scratch

```bash
# Wipe and regenerate (warning: overwrites the included data)
rm -rf mueller_small biotech_medium roehrig_large
python3 generate_mueller.py
python3 generate_biotech.py
python3 generate_roehrig.py

# Then apply the May-2026 enrichment patches (each is idempotent):
for f in regen/regen_*.py; do python3 "$f"; done

# Then the PII remediation pass:
python3 regen/fix_real_persons.py
```

Generation is single-threaded and takes a few minutes per dataset. The
enrichment patches were originally run via parallel sub-agents — sequentially
they take ~30 minutes total.

## Citation

If you use this dataset in research, please cite via [CITATION.cff](CITATION.cff)
or with the following BibTeX:

```bibtex
@misc{ohrendorf2026ddmockdata,
  author       = {Ohrendorf, Marc},
  title        = {{dd-mockdata}: A Synthetic German Legal Due-Diligence Corpus},
  year         = {2026},
  version      = {1.0.0},
  publisher    = {GitHub},
  url          = {https://github.com/Tonvenio/dd-mockdata}
}
```

## Contributing

Issues and pull requests welcome. Particularly useful contributions:

- Additional document types (e.g. BAFin-Bescheide, Bundesanzeiger-Veröffentlichungen,
  Schiedsverfahren-Akten, GwG-Meldungen).
- Ground-truth annotations (entity-linking, relation extraction, key-value
  extraction).
- A paired English-language counterpart for cross-lingual research.
- Bug reports if you find real-PII residue that the audit missed.

## Acknowledgments

The May-2026 enrichment + PII-remediation pass was performed using Claude
(Anthropic) as a generative agent. The original generators are pure Python
(no LLM involvement).

---

## Roadmap & related work — should I build a knowledge graph?

> ✅ **Built.** The knowledge graph now exists as a separate, dependent project:
> [**dd-mockdata-knowledge-graph**](https://github.com/Tonvenio/dd-mockdata-knowledge-graph).
> It ships rule-based extractor pipelines, a canonical "gold" graph in
> Turtle + JSON-LD + Neo4j-Cypher, and RAG / IE / contradiction evaluation
> harnesses — exactly the sibling-repo design sketched below. The rationale
> for keeping it separate is preserved here for context.

This question is a common ask for a corpus like this. **Recommendation:
build the knowledge graph as a separate, dependent project** —
not in this repository. Rationale:

**Arguments for keeping the KG separate:**

1. **Different audiences.** This repo's audience is researchers who want
   raw documents. A KG audience overlaps but skews to graph-DB / SPARQL /
   Neo4j / semantic-web folks who expect a different toolchain
   (RDF/Turtle, Cypher, GraphML).
2. **Dependency direction is clean.** A KG repo can `pip install
   dd-mockdata` (or pin a git SHA) and produce its triples; the dataset
   has no dependency on the KG. Mixing them couples release cadences
   awkwardly.
3. **Multiple KGs are useful.** The "right" KG depends on the task. A
   ground-truth KG for IE evaluation, a navigational KG for RAG, a
   compliance / regulatory KG, a financial-relationship KG — these are
   different schemas. Keeping the dataset KG-agnostic invites
   contributions of *several* KGs from different research groups, which
   is more interesting than committing to one.
4. **Repo size & dependencies.** A KG-side project will pull in
   `rdflib`/`pyshacl`/`neo4j`/`networkx`, plus possibly OpenIE / LLM
   pipelines. Keeping those out of the dataset repo keeps it small and
   trivial to clone.
5. **Version lifecycles diverge.** The dataset will need occasional
   touch-ups (more doc types, PII catches, new languages). The KG will
   evolve much more rapidly as schemas / extractors improve. Decoupling
   means a v2 of the KG doesn't require a v2 of the dataset.

**Arguments for a paired-KG release** (i.e. *do* combine):

- A KG is exactly what a researcher needs to evaluate RAG / IE systems —
  no KG = no easy benchmark.
- A single canonical "ground-truth KG" published with the data prevents
  evaluation fragmentation.

**Suggested compromise.** Keep this repo dataset-only. Publish the KG as a
sibling repository — for example **`dd-mockdata-kg`** — that:

- Declares `dd-mockdata >= 1.0` as input (git submodule or download script).
- Ships extractor pipelines (LLM-based, rule-based, hybrid) reproducibly.
- Publishes one canonical "gold KG" in Turtle + JSON-LD + Neo4j-cypher,
  versioned independently.
- Includes evaluation harnesses for RAG / IE / contradiction-detection.

The dataset is a natural fit for KG construction because it already has
strong relational structure: Konzernhierarchie RHO → 6 Töchter; Aufsichts-
rats- und Vorstandsbestellungen mit Datumsachse; Vertragsketten OEM ↔ REA ↔
Tochter ↔ Sub-Tier; FX-Hedges, IFRS-Salden und TP-Verrechnungspreise mit
Cross-Doc-Konsistenz; Patente mit Erfindern und Lizenzgebern; M&A-Targets
mit DD-Workflows; Compliance-Verstöße mit Whistleblower-Verfahren. The
relationships are designed to be cross-document — pulling them into a graph
is one of the highest-value follow-on contributions.

If a contributor wants to build it, here is a starter schema sketch:

```
Entities:    Company, Subsidiary, Person, Role, Position, Contract,
             Patent, Product, Customer, Supplier, Regulator, AuditFirm,
             LawFirm, Bank, InsurancePolicy, RealEstate, Project, Risk,
             ComplianceCase, ESOPGrant, PensionPlan, ICTransaction
Relations:   ownsSubsidiary, employs, holdsPosition, signs, partyTo,
             supplies, customerOf, audits, advises, insures, leases,
             invents, ownsPatent, licensesFrom, licensesTo, holdsStake,
             contributedBy, depositedAt, governedBy, hedgedBy, allocatedTo
Temporal:    appointedOn / resignedOn, validFrom / validUntil, effectiveDate
Provenance:  evidenceDocument (URL or path), evidenceParagraph, confidence
```
