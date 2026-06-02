# PII Findings — roehrig_large/23_Projekte_Programme

- Files scanned: 526 (449 .docx, 44 .pdf, 33 .xlsx)
- Files with findings: ~14 (after de-duplicating template false-positives)
- HIGH severity: 0
- MED severity: 1 (named-individual health data)
- LOW severity: 10 (non-canonical project-member names recurring across many files)

## Summary

The Projekte_Programme folder is remarkably clean from a direct-PII standpoint:

- **No IBANs** of any kind (not even the canonical whitelisted ones).
- **No email addresses** at all — even though one might expect contact info in
  project charters, none is present.
- **No phone numbers** (+49 patterns matched 0 hits).
- **No Steuer-Identifikationsnummern, no Sozialversicherungsnummern, no Luhn-valid
  credit-card patterns.**
- **No real public figures** (politicians, OEM-CEOs, etc.) cross-matched in the file
  texts. OEMs (BMW, VW, Daimler, ZF, Bosch, Continental, Stellantis, Ford,
  Hyundai) are mentioned only as customer organizations, not via named personnel.
- **External Prüfbericht-PDFs (Dekra, SGS, TÜV Rheinland, Bureau Veritas, REA Labor)
  contain NO names** — they are structured data tables with synthetic ISO numbers
  and `[Labor-Anschrift]` placeholders, so the lab signatories are blank.
- **Lessons-Learned-Berichte contain NO critical performance evaluations** tied to
  named individuals. A keyword sweep for `versagt`, `Fehlleistung`, `Abmahnung`,
  `Kündigung wegen`, `nicht qualifiziert`, `inkompeten*`, `Mobbing` returned zero
  proximity matches with any of the 587 distinct two-word-name tokens harvested
  from the 13 Lessons-Learned documents.

## Medium-severity findings

| # | File | Category | Excerpt | Notes |
|---|---|---|---|---|
| 1 | 23_Projekte_Programme/Abwesenheit_2023_026_Frank_Werner.xlsx | Art9 — Health data | »Abwesenheitskalender 2023 – Frank Werner-A26 … Krankheitstage: Jan 1, Feb 1, März 3, Apr 2, Mai 2, Jun 3, Jul 3, Aug 3, Sep 3, Okt 2, Nov 2, Dez 0« | Frank Werner is a canonical fictional employee, but the file is a personal-attendance sheet enumerating sick-day counts month-by-month. This is structurally DSGVO Art. 9 special-category data (Gesundheitsdaten) attached to a NAMED individual. The numbers are fictional, but the *structure* — a personal absence file with named employee + sick-day tally — is the kind of artefact a real GDPR sweep would call out, because if any real employee accidentally shares a name with the fictional one, ambiguity could arise. **Recommendation:** keep, but note in the corpus documentation. |

## Low-severity findings — non-canonical recurring person names

The following 8 names recur frequently in Project Charters, Gate-Reviews,
Status-Reports, Lessons-Learned and Testberichte as project leads / lab leads
/ test engineers. None of them are on the canonical Vorstand/Aufsichtsrat/Werk-
leitung/Konzern whitelist, but their roles (Projektleitung, Pruefer, Lab-Lead) are
plausible for fictional middle-management characters. All appear consistently across
multiple documents (suggesting an intentional cast of recurring fictional staff),
not in isolated one-offs.

| Name | Frequency | Role(s) | Risk |
|---|---|---|---|
| Stefan Brodbeck | 155 mentions | RSG Projektleitung (ADAS-V4D etc.) | LOW — plausibly fictional, no real-figure match |
| Karl-Heinz Wiegand | 136 mentions | Pruefer / Lab-Lead (recurring across ~all internal Testberichte) | LOW — Dr.-titled internal QA lead, plausibly fictional |
| Lars Wittmann | 130 mentions | RSG Projektleitung (InfoConnect, OTA) | LOW — common German name, no public-figure match |
| Sabine Brand | 122 mentions | REG-Q Pruefer-Team | LOW — plausibly fictional |
| Andreas Schultheiss | 85 mentions | REG Projektleitung (ECU-900 Gen3) | LOW — Schultheiss is a known German surname (brewery) but no public-figure collision |
| Marco Frey | 73 mentions | Projektleitung (AUTOSAR Refactoring) | LOW — there IS a real Prof. Marco Frey at Zeppelin Univ. Friedrichshafen (management academic); however no role overlap with electronics-engineering, so collision risk is low. Worth keeping on watch-list. |
| Klaudia Hoffmann | 46 mentions | Projektleitung (DSGVO Compliance Remediation) | LOW — unusual spelling, plausibly fictional |
| Anna Brand | 45 mentions | Projektleitung (LkSG Supply Chain Audit) | LOW — plausibly fictional |

### Sparsely-mentioned names (≤2 hits — potential review)

| Name | Hits | Notes |
|---|---|---|
| Eva Cerna | 2 | Plausibly fictional; Czech-origin name fits RCZ-Werk-context |
| Martin Lauer | 2 | A real Martin Lauer (1937–2019) was an Olympic 110-m-hurdles champion and Schlager singer. Collision risk if the doc context positions him in sports/music — but inspected contexts show only project-engineering roles, so LOW. |
| Stefan Goeb | 2 | Plausibly fictional |

## Notes / anomalies

1. **Templated content dominates.** The folder consists almost entirely of templated
   reports (status reports, gate reviews, test reports). Many documents repeat the
   exact same boilerplate — e.g., "OEM-spezifische Diagnose-Spezifikation (UDS-Layer)
   eingefroren" appears in dozens of status reports verbatim. This explains the
   144 false-positive `diagnose` keyword hits: every match is technical UDS/DoIP/OBD
   vehicle diagnostics, never medical diagnosis.
2. **Zero contact info.** Despite 526 files about projects, *no* email address,
   phone number, or IBAN appears anywhere. This is unusual for realistic corporate
   project docs and is a strong indicator that the author deliberately scrubbed all
   direct-contact PII.
3. **External Prüfbericht-PDFs are stripped.** PDFs from Dekra Stuttgart, SGS Hamburg,
   TÜV Rheinland Köln, Bureau Veritas, REA Labor Stuttgart all use
   `[Labor-Anschrift]` placeholders and contain no signatory names — well-engineered
   for plausibility without exposing real-lab personnel names.
4. **Lessons-Learned content is non-defamatory.** The 13 Lessons-Learned docs are
   structurally critical (they discuss what went wrong on projects), but the
   critique is consistently directed at processes, suppliers, decisions, and
   organisational topics — never at named individuals. No "X hat versagt" /
   "Y wurde abgemahnt" patterns were detected.
5. **Frank Werner absence sheet is the only file in the folder that materially
   diverges from the rest.** It is an HR-style personal-attendance file rather
   than a project artefact, suggesting it may have been mis-foldered (would more
   naturally live in `30_Personal_HR/` or similar). Mock-data corpus owners may
   want to relocate it for thematic coherence and so that PII reviewers see HR
   docs grouped together.
6. **Inline images.** None of the scanned .docx files reported `inline_shapes > 0`
   on extraction — no embedded photos / signatures / scanned IDs to worry about.
7. **PLZ + Ort patterns.** 353 instances of "5-digit + city" patterns were
   detected, but every one of them is either `70567 Stuttgart` (canonical Brennhagen
   HQ) or a known Werk-location (e.g., `74076 Heilbronn`, `38440 Wolfsburg`,
   `38114 Braunschweig` — all OEM-context locations). No private-residence-style
   addresses (street + PLZ + small-village name) were detected.

## Confidence

Scanner coverage was high (all 526 files extracted successfully; 0 extraction
errors). All `.docx`, `.xlsx`, and `.pdf` files were text-parsed. Image-content
OCR was not performed but no inline shapes exist in the .docx files. PDF text
extraction used pypdf and recovered structured tables cleanly.
