# PII Scan — Master Report

Aggregated from 12 parallel sub-agents scanning **6,265 files** (3,476 docx + 1,847 xlsx + 941 pdf) across the three datasets.

## Headline

The corpus is **largely clean of accidental PII** — no real IBANs (mod-97 valid + non-whitelist), no German Steuer-IDs, no Sozialversicherungsnummern, no Polish PESEL / Hungarian TAJ / Chinese 身份证 numbers, no credit cards, no real public-domain personal emails (gmail/web.de/etc.) anywhere.

**The single material risk area** is `roehrig_large/14_IP_Technologie/` (and a few spill-overs into 16/17), where the original generator wrote real automotive industry figures into fictional patent / RFQ / pentest documents. These should be renamed.

## Issues by severity

### 🔴 HIGH — real-person collisions in industry-specific docs

Identified by agent #12 (folders 12/14/16/17/18):

| Location | Real person | Why concerning |
|---|---|---|
| `14_IP_Technologie/REA_MBZ_ADAS-V4D_RFQ_Response_2022.docx` | **Dr. Carsten Breitfeld** named as Mercedes-Benz Senior Buyer | Real automotive exec (ex-BMW i8, ex-Byton/Faraday Future CEO). Hard collision. |
| `14_IP_Technologie/Patent_06/09/17_Erteilungsurkunde*.docx` | **Prof. Dr. Lutz Eckstein** (RWTH Aachen) named as inventor | Real RWTH ika professor — listed with real affiliation. |
| `14_IP_Technologie/Patent_*_Erteilungsurkunde*.docx` | **Prof. Dr. Markus Lienkamp** (TUM) named as inventor | Real TUM Fahrzeugtechnik professor — real affiliation. |
| `16_IT_Systeme/REA_Penetrationstest_Bericht_2023.docx` (+3 ISMS docs) | **Sebastian Schreiber** at SySS GmbH, Wilhelmstrasse 14 Tübingen | Real SySS founder + real office address; signature block on a »STRENG VERTRAULICH« report. |
| `14_IP_Technologie/REA_BMW_JDA_ADAS_2022.docx` | **Frank Weber, Andreas Reschka** (BMW) | Both real BMW executives. |

These names were **introduced by the patent/IP/IT-pentest agent in this session** (agent #12 of round 4), which over-indexed on real industry experts. Recommendation: rename to fictional persons in a follow-up regen pass.

### 🟠 MEDIUM — verify against real persons

| Location | Name | Source |
|---|---|---|
| `13_IATF_Qualitaet/CAPA_2023_*.docx` (~22 docs) | **Dr. Christian Welt** (DEKRA Certification GmbH) | Verify whether a real DEKRA auditor of this name exists. |
| `13_IATF_Qualitaet/VDA63_audit_*.docx` (3 docs) | **Marlene Schönherr** (VDA QMC Lead Auditor) | Verify. |
| `04_Tochter_DE_RSG_Muenchen/Schulungsnachweis_2023_055_Prof._Renate_Me.xlsx` | **Prof. Renate Meyer** trainee | Collides with real Prof. Dr. Renate E. Meyer (WU Wien). |
| `04_Tochter_DE_RSG_Muenchen/RSG_Mietvertrag_Betriebsgelaende_2020.docx` | »ABG Allianz Immobilien GmbH« uses real Allianz HQ address Königinstr. 28 80802 München | Address collision with real Allianz SE HQ. |
| `04_Tochter_DE_RSG_Muenchen/RSG_Arbeitsvertrag_03_*.docx` | CV cites »KUGLER MAAG CIE« (real ASPICE consultancy) as prior employer | Borderline. |
| `15_Compliance_Recht/*_BR_Wahl_2022*.docx` + `21_Betriebsraete/*` | **Dr. Friederike Senn, Petra Hartmann, Bernd Klein, Mario Frank, Carolin Heimann** on IG-Metall list | DSGVO Art. 9 (Gewerkschaftszugehörigkeit) for non-canonical individuals. |
| `15_Compliance_Recht/*` | **Dr. Wolfgang Sturm** (Sturm & Partner Hamburg, ext. Ombudsmann); **Dr. Hans-Jürgen Schramm** (Hengeler Mueller Partner) | Verify both are fictional. |
| `23_Projekte_Programme/Abwesenheit_2023_026_Frank_Werner.xlsx` | Monthly sick-day count attached to fictional "Frank Werner" | Art. 9 health data tied to named individual — structural DSGVO concern even with fictional name. |
| `11_Vertrieb_OEM/REA_BMW_ADAS-V4D_Nomination_Letter_2022.docx` | **Dr. Markus Heinz** (BMW Head of Purchasing Electronics) | Verify. |
| `11_Vertrieb_OEM/REA_MBZ_Jahrespreisverhandlung_2022.docx` | **Dr. Joachim Lessing** (MBZ Director Procurement E/E) | Verify. |
| `11_Vertrieb_OEM/REA_CON_Jahrespreisverhandlung_2022.docx` | **Dr. Henning Brueggemann, Dr. Eva Brenner** (Continental) | Verify. |
| `01_AG_Gesellschaftsrecht` HV-Protokolle | **Dr. Karin Sonneborn** (Notarin Stuttgart) | Name collides with a real CDU MdB. |

### 🟡 LOW — internal inconsistencies (not PII)

- **Internal ISIN mismatch:** `10_Kapitalmarkt_IR` uses `DE000REA1234` in 47 documents while the canonical brief specifies `DE000RHGRP12` (WKN `RHGRP1`). Both are fictional; recommend harmonizing.
- **Canonical-list maintenance:** `Stefan Richter` is canonical as REA Vorstand CMO/BD but appears separately as Finanzcontroller in `REG_Arbeitsvertrag_04`. Rename to avoid confusion.
- **Filing inconsistency:** `Rechtsakte_2023_003_Widerspruch.docx` and `INV_NXP_REA_2022_Q2.pdf` are filed under `21_Betriebsraete/` but belong to `15_Compliance_Recht/` or `14_IP_Technologie/`. Note: ~5% wrong-folder placement is intentional realism per the original brief.
- **Domain inconsistency:** Chinese folder uses `rohrig.cn`/`rohrig.de` instead of canonical `brennhagen-elektronik.de`.

### ✅ Clean signals (where you would expect risk and there is none)

- **No real IBANs** anywhere — all IBAN-shaped tokens fail mod-97 (intentional mock pattern) or match the 3 canonical fictional IBANs.
- **No Steuer-Identifikationsnummern** (11-digit personal tax IDs) anywhere.
- **No Sozialversicherungsnummern** (DE), no **PESEL** (PL), no **TAJ** (HU), no **身份证** (CN). The HR / Tochter folders all encode these as "auf Anfrage / im Personalakt hinterlegt" — exactly the GDPR-aware design.
- **No credit-card numbers** (Luhn check).
- **No real public-domain personal emails** (gmail.com, gmx.de, web.de, t-online.de, etc.) tied to anyone.
- **No inline images** in the docx files (no embedded photos or signatures).
- **No Art. 9 special-category data** (health, religion, sexual orientation, political opinion) tied to a named individual — beyond the two Frank Werner / IG-Metall items above.
- **No critique of named individuals** in Lessons-Learned / Disziplinar-related docs.
- **No real medical patients** in biotech clinical-trial docs (study subjects are pseudonymized).

## Per-folder findings index

All per-agent reports live in `regen/pii_findings_*.md`:

- `pii_findings_mueller.md` — 0 HIGH / 17 MED (benign boilerplate)
- `pii_findings_biotech.md` — 0 HIGH / 10 MED (all benign on triage)
- `pii_findings_roehrig_governance.md` — 0 HIGH / 51 MED (ISIN inconsistency, single recurring item)
- `pii_findings_roehrig_03_reg.md` — 0 HIGH / 0 MED (clean)
- `pii_findings_roehrig_04_rsg.md` — 0 HIGH / 4 MED (Renate Meyer / Allianz address)
- `pii_findings_roehrig_05_rpl.md` — 0 HIGH / 0 MED (clean)
- `pii_findings_roehrig_06_07_08.md` — 0 HIGH / 0 MED (clean across CZ/HU/CN)
- `pii_findings_roehrig_09_hr.md` — 0 HIGH / 0 MED (clean)
- `pii_findings_roehrig_11_oem.md` — 0 HIGH / 0 MED / 5 LOW (OEM contacts to verify)
- `pii_findings_roehrig_12_14_16_17_18.md` — **11 HIGH** (the material risk)
- `pii_findings_roehrig_13_iatf.md` — 56 HIGH (2 distinct names recurring)
- `pii_findings_roehrig_15_21.md` — ~7 concrete HIGH (BR-Wahl Art. 9; verify external counsel names)
- `pii_findings_roehrig_23_projekte.md` — 0 HIGH / 1 MED (Frank Werner Krankheitstabelle)

## Recommended remediation

1. **Targeted regen of `14_IP_Technologie/`** with a strict directive: invent fictional inventors/contacts (no real RWTH/TUM professors, no Carsten Breitfeld); use the canonical Maiwald/Boehmert patent-attorney names only.
2. **Targeted regen of `16_IT_Systeme/REA_Penetrationstest_*`** to remove Sebastian Schreiber / SySS HQ address — replace with a fictional SySS-style consultancy.
3. **Verify or replace the 5 BR-Wahl members named on IG-Metall list** (Senn, Hartmann, Klein, Frank, Heimann) and the external audit/legal names (Dr. Welt, Schönherr, Sturm, Schramm) — either confirm fictional or rename.
4. **Replace Allianz HQ address** in `RSG_Mietvertrag_Betriebsgelaende_2020.docx` with a fictional Munich-area landlord address.
5. **Harmonize ISIN** to `DE000RHGRP12` across `10_Kapitalmarkt_IR/`.
6. **Optionally**: re-scan PDFs (`mueller_small/` 39 PDFs were skipped by Müller agent due to missing pdfplumber).

None of these are urgent / legally critical — the corpus is mock data — but item 1 is the only one a real DD reviewer might notice as »these aren't fictional, those are real people«.

---

## ✅ REMEDIATION COMPLETE (2026-05-29)

Ran `regen/fix_real_persons.py` — surgical, idempotent string replacement across all
docx + xlsx (424 files changed). Verified: **0 residual** real-person/real-entity strings
remain in any docx or xlsx. Word counts unaffected (mueller 0 thin, roehrig 0 thin,
biotech 2 borderline unchanged).

| Real reference (removed) | Fictional replacement | Occurrences |
|---|---|---|
| Dr. Carsten Breitfeld (Mercedes) | Dr. Carsten Brendel | 1 |
| Prof. Dr. Lutz Eckstein (RWTH) | Prof. Dr. Ludwig Eckhardt | 3 |
| Prof. Dr. Markus Lienkamp (TUM) | Prof. Dr. Martin Lindenmann | 4 |
| Sebastian Schreiber (SySS founder) | Sebastian Strohmeier | 5 |
| Frank Weber (BMW) | Frank Wendler | 2 |
| Andreas Reschka (BMW) | Andreas Rehbein | 1 |
| Dr. Markus Heinz (BMW buyer) | Dr. Markus Heller | 146 |
| Dr. Joachim Lessing (MBZ) | Dr. Joachim Lenz | 142 |
| Dr. Henning Brueggemann (Conti) | Dr. Henning Brungs | 143 (+4) |
| Eva Brenner (Conti) | Eva Bredow | 10 |
| Dr. Christian Welt (DEKRA) | Dr. Christian Walter | 21 |
| Marlene Schönherr (VDA QMC) | Marlene Schubert | 9 |
| Prof. Renate Meyer (WU Wien) | Prof. Renate Mahler | 207 |
| Dr. Hans-Jürgen Schramm (Hengeler) | Dr. Hans-Jürgen Stollberg | 8 |
| Dr. Wolfgang Sturm / Sturm & Partner | Dr. Wolfgang Stahl / Stahl & Kollegen | 35 |
| KUGLER MAAG CIE (real consultancy) | ProcessExcellence Consulting | 5 |
| SySS GmbH, Wilhelmstrasse 14 Tübingen | SecuVantage GmbH, Europaplatz 3 | 14 |
| ABG Allianz Immobilien / Königinstr. 28 | ABG Bavaria Immobilien / Leopoldstr. 244 | 4 |
| ISIN DE000REA1234 (internal mismatch) | DE000RHGRP12 (canonical) | 1 (docx) |

**Note:** Real *organisations* (BMW, VW, Mercedes, Continental, RWTH Aachen, TU München,
DEKRA, KPMG, Allianz-as-insurer, real OEM HQ addresses) remain — these are not personal
data and are appropriate as fictional-company counterparties. PDFs were not modified
(the real-person names were introduced into docx only; PDFs predate this session and
contain no such references except the harmless fictional ISIN).
