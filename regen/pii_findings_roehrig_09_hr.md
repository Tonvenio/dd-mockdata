# PII Findings — roehrig_large/09_Personal_HR

- **Files scanned:** 496 (261 .docx, 234 .xlsx, 1 .pdf)
- **Files with raw regex hits:** 135
- **HIGH severity (real PII risk):** 0
- **MED severity (worth a human review):** 0 after de-noising
- **LOW severity (boilerplate term hits, not personal data):** 135
- **Read errors:** 0

## Analyst summary

Despite the high-risk profile of this folder (Arbeitsverträge, Gehaltsänderungen,
Personalakten, ESOP/LTI), the scan did **not** surface any direct PII patterns:

| Pattern | Result |
|---|---|
| IBAN (mod-97 valid, not in canonical whitelist) | **0 hits** anywhere in the folder (including in DOCX headers / footers) |
| German Steuer-Identifikationsnummer (11-stellig) | **0 hits** — no field labelled »Steuer-ID«, »TIN«, »IdNr« with digits |
| Sozialversicherungsnummer (12-char SVNR pattern) | **0 hits** — label »SV-Nr/Sozialversicherungsnummer« never appears with a number; only the boilerplate clause "…Eintritt in die gesetzliche Rentenversicherung erreicht…" matched the loose regex |
| Credit-card numbers (Luhn-valid) | 0 |
| Public/personal email domains (gmail, gmx, web.de, etc.) | 0 |
| Non-canonical corporate email domains | 0 |
| Real-birthday-of-named-person (dd.mm.yyyy, 1940-2005) | **0 hits** in any document |
| Real public figure names (Merkel, Scholz, Musk, real OEM-CEOs …) | 0 |
| ESOP/VSOP/LTI lists with names + grant detail | **0** — the LTI plan describes groups generically ("Gruppe A — Vorstand REA (4 Personen)"); no per-person grant table |
| Vergütungsbericht § 162 AktG | Policy `REA_HR_Policy_Vorstandsverguetung_2023.docx` references only canonical persons (Anna Müller, Laura Bauer, Marlies Dürr, Prof. Renate Meyer) |

## Why 135 files were flagged in the raw scan (all false positives)

### 116× `SpecialCat_health` → boilerplate Arbeitsvertrag § 5

Every Arbeitsvertrag (`AV_*.docx`) contains the standard clause:

> § 5 Urlaub und Krankheit
> (1) Jahresurlaub: 30 Arbeitstage.
> (2) Im Krankheitsfall ist der Arbeitgeber ab dem ersten Tag zu informieren …

This triggers on the word `Krankheit`. None of these documents contain an
actual diagnosis, medication, mental-health condition, Schwerbehinderung,
pregnancy status, or any other Art. 9 DSGVO special-category data tied to
an identified person. A second-pass scan for `Diagnose|Depression|Burnout|HIV|
Krebs|Tumor|Schwerbehinderung|Suizid|psychisch erkrankt|chronische Erkrankung`
returned **zero hits** across all 496 files.

### 19× `SpecialCat_union` → »IG Metall« in BV preambles

Mentions of `IG Metall` appear in Betriebsvereinbarungen / Wahlprotokollen as
the bargaining counterparty (e.g. `REA_BV_Vergütungssystem_IGM_Tarif_2022.docx`,
`REG_BR_Wahl_Protokoll_2022.docx`). The canonical brief explicitly whitelists
»Marlies Dürr, IG Metall« and treats organisational mention of a union in a BV
as non-PII. No file ties an individual rank-and-file employee to union
membership.

## Notes / anomalies

- Salary letters (`Gehaltsaenderung_2023_*.docx`) carry only `Personalnummer P-NNN`
  — no bank details, no Steuer-IDs, no SV-Nr.
- The `REA_Gehaltsstruktur_2023.xlsx` Vergütungsbänder sheet contains generic
  level bands (E1/M5/P4/etc.), not individual salaries linked to names.
- The Long-Term Incentive Plan 2022 document references only canonical
  Aufsichtsratsvorsitzender Dr. Klaus Steinbrück and CEO Anna Müller; the PSU
  allocation table is aggregated by group ("Vorstand REA — 4 Personen"), not
  per-person.
- The "Vorstandsvergütung" policy mentions Bjoern Franke in a HR-Lenkungskreis
  role — this name is **not** on the canonical whitelist in PII_BRIEF.md but
  fits the established fictional-employee naming convention (German given +
  surname). Flagging as **informational** only — recommend confirming Bjoern
  Franke is intended-fictional in `enhance_lib.py`.

## Raw regex hits (kept for traceability — all benign on review)

<details>
<summary>116× SpecialCat_health (boilerplate § 5 Arbeitsvertrag — click to expand)</summary>

All hits are `Krankheit` in the standard Arbeitsvertrag clause; no real
health data. File list (truncated):

- AV_001_Anna_Müller_Vorstandsvorsitzende.docx … AV_116_*.docx
- Pattern identical in every Anstellungsvertrag.

</details>

<details>
<summary>19× SpecialCat_union (»IG Metall« in BVs)</summary>

Boilerplate Betriebsvereinbarung / Wahlprotokoll mentions; not tied to
individual employees beyond the canonical Marlies Dürr.

- REA_BV_Betriebliche_Altersversorgung_2022_v2.docx
- REA_BV_Betriebliches_Eingliederungsmanagement_2022.docx
- REA_BV_Datenschutz_IT_Systeme_2022.docx
- REA_BV_Essenszuschuss_Kantine_2022_ENTWURF.docx
- REA_BV_Gesundheitsfoerderung_2022.docx
- REA_BV_Homeoffice_Mobiles_Arbeiten_2022.docx
- REA_BV_Jubilaeumsregelung_2022.docx
- REA_BV_Kurzarbeit_2022.docx
- REA_BV_Leistungsbeurteilung_und_Prämien_2022.docx
- REA_BV_Mobilitätszuschuss_ÖPNV_2022.docx
- REA_BV_Qualifizierung_Weiterbildung_2022.docx
- REA_BV_Urlaub_Urlaubsgeld_2022.docx
- REA_BV_Vergütungssystem_IGM_Tarif_2022.docx
- REA_BV_Vertrauensarbeitszeit_Führungskräfte_2022.docx
- REA_BV_Zuschlagsregelung_Schichtarbeit_2022.docx
- REA_Organigramm_Konzern_2024.docx
- REG_BR_Wahl_Protokoll_2022.docx
- REG_BV_Homeoffice_Telearbeit_2022.docx
- RHO_BR_Wahl_Protokoll_2022.docx

</details>

## Verdict

The 09_Personal_HR folder is **clean** of real-world PII against all
high-risk patterns checked. The mock-data generator appears to have
deliberately omitted IBAN/Steuer-ID/SVNR fields from personnel records, and
restricted per-person compensation detail to aggregated bands. No real public
figures, no real birthdays, no special-category data tied to a named
individual. The only follow-up item is to confirm »Bjoern Franke« is an
intended canonical fictional employee.
