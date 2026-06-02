# PII Findings — roehrig_large / 04_Tochter_DE_RSG_Muenchen

- Files scanned: 244 (244 of 244 readable — no parse errors)
- File types: ~206 .docx + ~38 .xlsx
- Files with findings: 6 (HIGH 0 / MED 4 unique items / LOW 4)
- HIGH severity: 0
- MED severity: 4 (unique items; same-surname coincidence + real-name collision + real-firm reference + real-address reference)
- LOW severity: 4

## Scan methodology

Automated regex sweep (IBAN mod-97, email public-domains, Steuer-ID, SVNR, phone, address, GitHub/LinkedIn, DSGVO Art. 9 keywords with word-boundary `\b…\b`) over all .docx / .xlsx in the folder, plus manual review of the 11 high-risk documents (5 Arbeitsverträge, 3 WP Management Letter, Compliance Report, Mietvertrag, Versicherungsnachweis).

No IBANs passing mod-97 found (the single repeated IBAN `DE89 7015 0000 0123 4567 89` deliberately fails mod-97 — properly fictional). No public-domain emails, no Steuer-IDs, no Sozialversicherungsnummern, no Luhn-valid card numbers, no real phone numbers, no GitHub / LinkedIn handles, no health / religion / political / trade-union / criminal-record content tied to named individuals.

## HIGH-severity findings

_None._

## MED-severity findings

| File | Category | Excerpt / Note |
|---|---|---|
| `Schulungsnachweis_2023_055_Prof._Renate_Me.xlsx` | RealPersonCollision | Trainee listed as »Prof. Renate Meyer«. The combination Prof. + Renate Meyer collides with a real, well-known academic (Prof. Dr. Renate E. Meyer, WU Wien, organisation studies). Recommend renaming to e.g. »Prof. Renate Mertens« to break the collision. |
| `RSG_Arbeitsvertrag_03_Qualitätsmanagerin_M_2022.docx` | RealCompanyAsEmployer | Dr. Sabrina Halbig (Qualitätsmanagerin / ASPICE-Lead Assessor) listed as »zuvor KUGLER MAAG CIE, dann BMW Group«. KUGLER MAAG CIE is a real, well-known German ASPICE / Automotive-SPICE consultancy. Attribution of an individual's CV to a real consultancy is acceptable as canonical employer reference for BMW — but for KUGLER MAAG (a small specialist firm with named partners) this looks closer to a real CV. Consider replacing with a clearly fictional consultancy. |
| `RSG_Arbeitsvertrag_05_HR-Manager_München_2022.docx` | SameSurnameAnomaly | HR-Manager »Petra Kessler« contracts with GF »Dr. Klaus Kessler« — identical surname creates a nepotism-appearance anomaly in the mock data. Not real PII, but unrealistic for a real Arbeitsvertrag (governance / conflict-of-interest issue). Recommend giving the HR-Manager a different surname. |
| `RSG_Mietvertrag_Betriebsgelaende_2020.docx` | RealAddressForFictionalEntity | Landlord »ABG Allianz Immobilien GmbH, Königinstrasse 28, 80802 Muenchen, HRB 142587«. Königinstr. 28, 80802 München is the actual Allianz SE corporate-headquarters address. Allianz Real Estate / Allianz Immobilien GmbH does exist (different HRB). The fictional »ABG Allianz Immobilien GmbH« + real Allianz HQ address is borderline — recommend either drop »Allianz« from the landlord name or change the street. |

## LOW-severity findings

| File(s) | Category | Note |
|---|---|---|
| `RSG_WP_Management_Letter_2021/2022/2023.docx` | RealOfficeAddress | KPMG AG WPG »Ganghoferstrasse 29, 80339 Muenchen« — real KPMG München office address. Institutional, not personal, but real. Acceptable per Brief Category D. |
| `RSG_Steuerbescheid_*.docx` (4 files) | RealOfficeAddress | »Deroystrasse 18, 80335 Muenchen« — real Finanzamt München address. Institutional, not personal. Acceptable. |
| `RSG_WP_Management_Letter_2021/2022/2023.docx` | NamedKPMGAuditor | »Anke Riethmaier, Senior Manager Vor-Ort« — not on canonical KPMG whitelist (only Dr. Maximilian Brand is canonical). Common-enough name, no other identifiers; treat as fictional sub-staff. |
| `RSG_Arbeitsvertrag_01_*.docx` | SelfContractAnomaly | Geschäftsführer-Anstellungsvertrag is signed by »Dr. Klaus Kessler« on both sides (Arbeitgeberin und Mitarbeiter) — would normally require Aufsichtsrat / Gesellschafter-Vertretung signature. Not PII, but document-integrity issue. |

## DSGVO Art. 9 special categories

Initial automated scan returned 37 hits across files for biometric / DNA keywords. **All 37 are false positives** caused by substring matching (e.g. "Geno**m**" matched inside »ausge**nom**men« — German for »excluded«; "DNA" matched inside Czech word »je**dna**tel« — managing director). After re-running with `\b…\b` word boundaries: **0 special-category findings**.

No mention of health / illness, religion, party affiliation, sexual orientation, criminal record, genetic, biometric data tied to any named individual. The Compliance Report references »Langzeitkranke und Elternzeit-Faelle« only as anonymous aggregate, and the Mobbing-Vorwurf entry is described anonymized (»Teamlead R&D«, no name).

## Identifier inventory (informational, all properly fictional)

- HRB 319872 (Brennhagen Software GmbH, AG München) — fictional, consistent across all docs.
- HRB 142587 (ABG Allianz Immobilien GmbH) — fictional.
- IBAN `DE89 7015 0000 0123 4567 89` — appears in 68 IC-invoice / monthly-PL docs; fails mod-97 → properly fictional.
- HRB 726451 (Brennhagen Elektronik AG Stuttgart) — canonical.
- Policen-Nr. (DO-REA-2022-001, CY-REA-2023-001, etc.) — fictional internal IDs.

## Notes / anomalies

1. **Pure surname coincidence Klaus Kessler / Petra Kessler** in the Arbeitsvertrag 05 — looks like a generation-error (the regenerator probably re-used »Kessler« when sampling HR-Manager name). Not a privacy issue, but unrealistic.
2. **Self-signed Geschäftsführer-Anstellungsvertrag** (Arbeitsvertrag 01): both signature blocks bear »Dr. Klaus Kessler«. Document-realism issue, not PII.
3. **Real-but-institutional addresses** (KPMG Ganghoferstr. 29; Finanzamt Deroystr. 18) appear and are acceptable per the brief.
4. **Königinstr. 28** (Allianz HQ) used as landlord address with a fictional name partly resembling Allianz — recommend mitigation.
5. **Prof. Renate Meyer** in the training record collides with a real academic; recommend a name change.
6. **No GitHub / LinkedIn handles** found anywhere in the developer-heavy Arbeitsverträge, contrary to the brief's heightened concern for this subsidiary. Looks intentional (handles deliberately omitted in the mock data).
7. **No ASPICE-Assessor name reuse**: Dr. Sabrina Halbig (RSG) and the (unnamed) intacs Principal Assessor references are fictional/generic. The only real-firm exposure on the ASPICE side is the »KUGLER MAAG CIE« employer reference.
8. **Phone numbers**: none found at all in this folder (no `+49 …` strings caught by the phone regex). Consistent with mock data that uses no contact details.
