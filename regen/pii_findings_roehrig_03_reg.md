# PII Findings — roehrig_large / 03_Tochter_DE_REG_Heilbronn

- Files scanned: **259** (147 .docx, 100 .xlsx, 12 .pdf)
- Files with extraction errors: 0
- Files skipped: 0
- Files with image-embeds (`doc.inline_shapes`): 0
- HIGH severity: **0**
- MED severity: **0** (after manual triage — all auto-flagged MED were false positives)
- LOW severity: **2** (after triage; remaining are noise)

## High-severity findings

*None.*

The folder contains 5 Arbeitsverträge (Geschäftsführer, Produktionsleiter, Q-Manager,
Finanzcontroller, HR-Manager). All five were inspected in full text. None of them
contain:

- IBANs of the employee
- Private home addresses ("wohnhaft …" sections do not exist; the contracts use
  only the work address Industriestrasse 47, 74076 Heilbronn or Heilbronner Strasse 88,
  74072 Heilbronn — both fictional REG site addresses, both 74xxx Heilbronn = canonical)
- Birthdays / Geburtsdatum
- Steuer-Identifikationsnummer
- Sozialversicherungsnummer
- Personal phone / private email

Salary figures are present but in role-keyed, plausible ranges
(GF 12.916 EUR, PL 9.450 EUR, QM 9.120 EUR, FC 7.850 EUR, HR 7.200 EUR / month) —
these are by design and tied to fictional name+role, not real-PII risk.

Named contract counterparties (all fictional, all consistent with the
project name-graph):
- AV 01 GF: **Andreas Maier** (canonical Werkleiter REG)
- AV 02 Produktionsleiter: **Dipl.-Ing. Markus Henkel**
- AV 03 Q-Leitung: **Sabine Brand** (canonical Q-Leitung REG)
- AV 04 Finanzcontroller: **Stefan Richter** (this name is also REA CMO/BD canonical — a
  duplication of a canonical AG-Vorstand name with a REG-Werk role; potentially confusing
  but not a PII risk because the name is fictional. Worth a note to enhance_lib maintainers.)
- AV 05 HR-Manager: **Petra Holzwarth**

## Medium-severity findings

*None after triage.*

Auto-flagged-then-cleared:

| Auto-flag | File(s) | Why dismissed |
|---|---|---|
| `SpecialCategory_health: "Diagnose"` (5 hits) | PRJ-2023-001 EOL-Testbericht, Control Plans BMS-12 / ECU-900 | Pure automotive context: »CAN-Bus-Diagnose«, »UDS-Diagnose«, »Funktionsdiagnose« — technical electronic diagnostics, not health. |

## Low-severity findings

| Category | Count | Resolution |
|---|---|---|
| `IBAN_invalid_checksum: DE48 6209 1800 0123 4567 89` | 31 IC-Rechnungen | Volksbank Heilbronn BLZ 62091800 + placeholder Kontonummer `0123456789`. Real BLZ, fake account, fake checksum — designed mock. |
| `IBAN_invalid_checksum: DE55 6002 0290 0987 6543 21` | 12 IC-Rechnungen (REG→RSG) | HypoVereinsbank Muenchen BLZ 60020290 + placeholder Kontonummer `0987654321`. Real BLZ, fake account, fake checksum — designed mock. |
| `OtherCityAddr: 80335 Muenchen` | 32 occurrences in REG→RSG IC-Rechnungen | RSG sister company address »Bayerstrasse 33, 80335 Muenchen« — fictional sibling subsidiary in the Brennhagen group, by design. |
| `OtherCityAddr: 16949 Anhang` / `16949 und` | 9 hits in Control Plans / Arbeitsvertrag QM | False positive — »IATF 16949« automotive QM standard, not an address. |
| `OtherCityAddr: 12345 Steuer-` | 4 hits in WP Management Letters | False positive — placeholder PLZ in tax-ID example text. |

## Non-canonical names found (all plausibly fictional, no real-person match)

These do not appear on the canonical whitelist but consistently appear in
fictional roles at fictional addresses. Logged for the canonical-list maintainer:

| Name | Doc / Role |
|---|---|
| Dipl.-Ing. **Markus Henkel** | REG_Arbeitsvertrag_02 Produktionsleiter |
| **Petra Holzwarth** | REG_Arbeitsvertrag_05 HR-Manager |
| Dr. **Bernd Voelker** | REG_Mietvertrag — GF Industriegrundbesitz Heilbronn GmbH & Co. KG (fictional Vermieterin), Wilhelmstrasse 21, 74072 Heilbronn |
| **Christine Meinhardt** | REG_Versicherungsnachweis — Group Risk Management REA |
| Dr. **Rainer Kunze** | REG_Compliance_Report — Konzern-Compliance-Officer REA Stuttgart |
| Dr. **Lena Engelhardt** | REG_Compliance_Report — Local Compliance Officer REG |
| **Felix Schwarzbauer** | REG_WP_Management_Letter — KPMG Manager (alongside canonical Dr. Maximilian Brand) |
| **Hans-Juergen Klemm** | Mentioned in REG_Arbeitsvertrag_05 — Betriebsrats-Vorsitz Heilbronn (note: enhance_lib gives »Klaus Bauer« as BR-Vorsitz REG, see RCZ regen file — inconsistency with this folder) |
| **Birgit Voelkner** | Mentioned in REG_Arbeitsvertrag_05 — Leiterin Konzern-HR Stuttgart |

None of these surnames map to a recognizable real public figure on a name-check.

## Notes / anomalies

1. **Canonical-list inconsistency (NOT a PII risk, but worth a note):**
   the brief lists »Stefan Richter« as REA CMO/BD on the AG board, yet
   `REG_Arbeitsvertrag_04` puts a »Stefan Richter« in a Werk-Finanzcontroller role
   in Heilbronn. Either two unrelated fictional people share a name, or
   the AG CMO is moonlighting as a plant controller. Suggest renaming the
   contract counterparty in AV_04 for clarity (the filename already encodes
   `_rev_SRichter`).

2. **Canonical-list inconsistency BR-Vorsitz REG:**
   AV_05 names »Hans-Juergen Klemm« as BR-Vorsitz Heilbronn; `regen_roehrig_06_rcz_brno.py`
   names »Klaus Bauer« as BR-Vorsitz REG-Werk. Pick one for the canonical list.

3. **Both mock IBANs use REAL Bankleitzahlen** (Volksbank Heilbronn 62091800,
   HVB Muenchen 60020290). The Kontonummern are sequential placeholders
   (`0123456789` / `0987654321`) and the mod-97 checksums deliberately fail.
   This is not a DSGVO problem (no real account is exposed), but auditors
   may flag the use of real BLZ — acceptable since BLZs are public registry data.

4. **No emails of any kind** were found in any docx/xlsx/pdf in this folder.
   No phone numbers in personal form (only corporate switchboards inside
   address blocks of the form `+49 7131 …` Heilbronn, fictional extensions).

5. **No image embeds, no signatures, no scanned documents.** All docx files
   have `inline_shapes == 0`. PDF files (12 IC-Rechnungen 2023) were
   extracted via pdfplumber without text-from-image fallback needed.

6. **No special category data (DSGVO Art. 9) tied to a named individual.**
   The only Art. 9 keyword matches were technical (»Diagnose« = diagnostics).

7. **No real public figures, no real medical patients, no real coordinates.**
