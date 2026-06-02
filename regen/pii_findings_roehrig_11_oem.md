# PII Findings — 11_Vertrieb_OEM (roehrig_large)

- Files scanned: 373 (368 .docx + 4 .xlsx + 1 .pdf)
- Files with findings: 5
- HIGH severity: 0
- MED severity: 0
- LOW severity: 5
- PDFs skipped: 0 (pdfplumber available)

## High-severity findings

_None._

## Medium-severity findings

_None._

## Low-severity / observational findings

Five fictional-looking named contact persons at real OEM corporate entities are
recorded with role/title only (no personal email, no private phone, no address).
Per the brief, this is below the MED threshold (which requires real first+last
name combos tied to OEM email domains or personal phone). Listed for transparency:

| File | Category | Excerpt |
|---|---|---|
| REA_BMW_ADAS-V4D_Nomination_Letter_2022.docx | OEM_NamedContact | BMW, »Dr. Markus Heinz« (Head of Purchasing Electronics) — no email/phone given |
| REA_VW_ADAS-V4D_Nomination_Letter_2022.docx  | OEM_NamedContact | VW, »Frau Petra Lindemann« — no email/phone given |
| REA_MBZ_Jahrespreisverhandlung_2022.docx     | OEM_NamedContact | Mercedes-Benz Group AG, »Dr. Joachim Lessing« (Director Procurement E/E Systems) — no email/phone given |
| REA_CON_Jahrespreisverhandlung_2022.docx     | OEM_NamedContact | Continental AG, »Dr. Henning Brueggemann« (Strategic Purchasing Lead Tier-2) + »Dr. Eva Brenner« (Strategic Sourcing) — no email/phone given |
| REA_MBZ_Jahrespreisverhandlung_2022.docx     | OEM_NamedContact | »Dr. Eva Brenner« also reused as Mercedes stand-in — internally inconsistent across both Continental + Mercedes negotiation docs, which supports the fictional nature of the name. |

These five names are not publicly known executives at the respective OEMs (based
on the assistant's knowledge as of 2026-01). They appear to be fully fabricated
by the mock-data generator. Recommend a quick human cross-check against current
LinkedIn / press releases for each name before publication, just to rule out an
accidental collision with a real person.

## Scanned categories — none triggered

- IBAN (mod-97 valid, non-whitelist): 0 — no IBANs are written into OEM docs
- Public-domain personal email (gmail / yahoo / web.de / gmx / t-online / hotmail / outlook / icloud / aol / freenet): 0
- OEM-domain personal email (bmw.de, volkswagen.de, mercedes-benz.com, stellantis.com, ford.de, continental.com, zf.com, bosch.com, hyundai.com with `first.last@`): 0
- German Steuer-Identifikationsnummer (11-digit, in »Steuer-Id« context): 0
- Sozialversicherungsnummer: 0
- Credit-card numbers passing Luhn: 0
- German mobile phone (+49 15* / +49 16* / +49 17*) or 01x mobile: 0
- DSGVO Art. 9 special-category keywords tied to a named individual
  (Schwerbehinderung, Krankschreibung, Schwangerschaft, Konfession,
  Kirchenmitgliedschaft, Strafregister, Vorstrafe, Homosexualität,
  Transgender, Gewerkschaftsmitgliedschaft etc.): 0
- Birth dates / »geb. …«, »X Jahre alt« tied to a named individual: 0
- Signature blocks containing personal contact info: 0

## Notes / anomalies

1. **Very clean folder.** The OEM-Vertrieb folder is essentially address-only
   for real OEM HQs (BMW Petuelring 130 Munich, etc. — all public corporate
   addresses) and uses generic role placeholders (»n. n. Programm-Manager«,
   »Ansprechpartner Einkauf«). No bank data, no contact data, no Art. 9 data.

2. **»Sabine Brand (Q-Leitung REG Heilbronn, Tel. +49 7131 / 1234-810)«**
   appears in `REA_BMW_Audit_Einladung_2022_ENTWURF.docx`. This is an
   internal Brennhagen (REG Heilbronn site) phone number — `+49 7131` is the
   Heilbronn area code, and `1234` is an obvious dummy block-number. The
   subscriber-number `1234-810` is clearly placeholder syntax. Not flagged.

3. **First-pass false positives suppressed.** Initial naive scan flagged
   171 files for keyword »Diagnose«, but in 100% of cases this referred to
   OBD / UDS automotive diagnostic functions (»DTC-Erweiterung«, »Diagnose-
   Routine«), not human health. Keyword list was tightened to require
   clinically/HR-specific terms (»Schwerbehinderung«, »Krankschreibung«,
   »Schwangerschaft«, »Konfession« etc.), which produced 0 hits.

4. **pdfplumber + openpyxl available** — all 373 files (368 .docx, 4 .xlsx,
   1 .pdf) were fully text-extracted, including tables, headers, footers,
   and spreadsheet cells.

5. **No image embeds were inspected.** If real photos / signatures could be
   embedded as `doc.inline_shapes`, a follow-up image-content scan is
   recommended. (Out of scope for this text-only PII pass.)
