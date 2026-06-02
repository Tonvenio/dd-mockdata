# PII Findings — biotech_medium

- Files scanned: 935
- Files with findings: 15
- HIGH severity: 6
- MED severity: 10
- LOW severity: 0
- PDFs unreadable / empty: 0
- DOCX with inline images: 0

## High-severity findings

| File | Category | Excerpt |
|---|---|---|
| 09_IP_Patente/IP_001_Patentportfolio_Uebersicht.xlsx | HealthDataNamedPerson(patient) | DE/EP Angemeldet EP Dr. Lena Fischer Anhängig bis 2042 BTP-P-009 Verfahren zur patientenspezifischen Normierung von Messdaten 2022 DE/EP Ang |
| 04_Vertrieb_Distributoren/TRAINING_CHR_Cardevio P_Schulungszertifikat_v2.pdf | HealthDataNamedPerson(diagnose) | ommen hat. Die Schulung umfasste Inbetriebnahme, Bedienung, Reinigung und Fehlerdiagnose. Teilnehmer Name Funktion Unterschrift Dr. med. Mül |
| 04_Vertrieb_Distributoren/TRAINING_CHR_Ostevo Nav_Schulungszertifikat.pdf | HealthDataNamedPerson(diagnose) | ommen hat. Die Schulung umfasste Inbetriebnahme, Bedienung, Reinigung und Fehlerdiagnose. Teilnehmer Name Funktion Unterschrift Dr. med. Mül |
| 04_Vertrieb_Distributoren/TRAINING_UKE_Cardevio P_Schulungszertifikat.pdf | HealthDataNamedPerson(diagnose) | ommen hat. Die Schulung umfasste Inbetriebnahme, Bedienung, Reinigung und Fehlerdiagnose. Teilnehmer Name Funktion Unterschrift Dr. med. Sch |
| 04_Vertrieb_Distributoren/TRAINING_UKE_Ostevo Nav_Schulungszertifikat.pdf | HealthDataNamedPerson(diagnose) | ommen hat. Die Schulung umfasste Inbetriebnahme, Bedienung, Reinigung und Fehlerdiagnose. Teilnehmer Name Funktion Unterschrift Dr. med. Mül |
| 15_FuE_Innovation/RD_107_Kooperationsvertrag Fraun.pdf | HealthDataNamedPerson(operation) | / HRB 218934 Kooperationsvertrag Fraunhofer IPA F&E; Übersicht F&E-Dokument;: Kooperationsvertrag Fraunhofer IPA F&E; Datum: 20. August 2023 |

## Medium-severity findings

| File | Category | Excerpt |
|---|---|---|
| 13_Compliance_Recht/COMP_01_Anti-Korruptions-Richtlin.docx | NonCanonicalPhone | +49 800 555 33 22 |
| 13_Compliance_Recht/COMP_02_HWG-Compliance – Medizinp.docx | NonCanonicalPhone | +49 800 555 33 22 |
| 13_Compliance_Recht/COMP_03_MBO-Ä und Antikorruptions.docx | NonCanonicalPhone | +49 800 555 33 22 |
| 13_Compliance_Recht/COMP_04_Code of Conduct.docx | NonCanonicalPhone | +49 800 555 33 22 |
| 13_Compliance_Recht/COMP_04_Code of Conduct.docx | Art9_Religion(religion) | eies Arbeitsumfeld (keine Diskriminierung aufgrund Geschlecht, Alter, Herkunft, Religion, sexueller Orientierung, Behinderung). Wir sind Ste |
| 13_Compliance_Recht/COMP_05_Interessenkonflikt-Richtl.docx | NonCanonicalPhone | +49 800 555 33 22 |
| 13_Compliance_Recht/COMP_06_Sanktionslisten-Screening.docx | NonCanonicalPhone | +49 800 555 33 22 |
| 13_Compliance_Recht/COMP_07_Datenschutzrichtlinie _DS.docx | NonCanonicalPhone | +49 800 555 33 22 |
| 13_Compliance_Recht/COMP_08_Social Media Policy.docx | NonCanonicalPhone | +49 800 555 33 22 |
| 13_Compliance_Recht/COMP_HinSchG_Hinweisgebersystem_Richtlinie.docx | NonCanonicalPhone | +49 800 555 33 22 |

## DOCX files containing inline images


## Notes / anomalies

- 0 PDFs were unreadable or empty. All 625 PDFs scanned successfully via pdfplumber.
- All 6 HIGH findings on manual review are FALSE POSITIVES from substring matches:
  - `IP_001_Patentportfolio_Uebersicht.xlsx`: keyword "patient" matched
    "patientenspezifischen Normierung" — a patent title, no patient PII. The names
    "Dr. Lena Fischer" / "Dr. Marcus Vogt" are listed as patent inventors (Vogt is
    canonical CTO; Fischer appears to be a non-canonical fictional inventor — borderline,
    flagged for review but no health-data linkage).
  - 4x `TRAINING_..._Schulungszertifikat.pdf`: "diagnose" matched "Fehlerdiagnose"
    (troubleshooting). The certificates list only generic "Dr. med. Müller" /
    "Dr. med. Schmidt" without first names or patient data.
  - `RD_107_Kooperationsvertrag Fraun.pdf`: "operation" matched "Kooperationsvertrag".
- All 9 MED phone hits are the same fictional whistleblower hotline `+49 800 555 33 22`
  appearing across compliance docs — clearly a placeholder, not a real number.
- The Religion MED hit in `COMP_04_Code of Conduct.docx` is a generic
  anti-discrimination clause (no named person), not a Cat-B violation.
- No real-public-figure names, no public-email addresses, no off-whitelist IBANs,
  no Steuer-IDs, no Sozialversicherungsnummern, no credit-card numbers,
  no inline images/signatures in any of the 161 .docx files,
  no named clinical study subjects, no patient identifiers detected.
- Verdict: the BioTech mock-data folder appears CLEAN of real PII.
  Optional cleanup: confirm "Dr. Lena Fischer" inventor name is intentional fiction
  (recommend adding to canonical whitelist) and confirm the 800-number placeholder
  is the intended hotline.