# PII Findings — Brennhagen Töchter CZ/HU/CN (06, 07, 08)

- Files scanned: 693
- Files with findings: 38
- HIGH severity: 0
- MED severity: 0
- LOW severity: 71
- Read errors: 0

## Per-folder severity counts

| Folder | HIGH | MED | LOW |
|---|---|---|---|
| 06_Tochter_CZ_Brno | 0 | 0 | 1 |
| 07_Tochter_HU_Gyoer | 0 | 0 | 3 |
| 08_Tochter_CN_Shanghai | 0 | 0 | 67 |

## High-severity findings

_None._

## Medium-severity findings

_None._

## Low-severity findings (sampled)

### ExternalEmail (71 occurrences)

| File | Category | Excerpt |
|---|---|---|
| 06_Tochter_CZ_Brno/RCZ_Versicherungsnachweis_2023.docx | ExternalEmail | marsh.frankfurt@marsh.com |
| 07_Tochter_HU_Gyoer/RHU_WP_Management_Letter_2021.docx | ExternalEmail | tamas.hegedus@kpmg.hu |
| 08_Tochter_CN_Shanghai/RCN_IC_Rechnung_2020_01.docx | ExternalEmail | liang.wei@rohrig.cn |
| 08_Tochter_CN_Shanghai/RCN_IC_Rechnung_2020_01.docx | ExternalEmail | tax@rohrig.de |
| 08_Tochter_CN_Shanghai/RCN_Versicherungsnachweis_2023.docx | ExternalEmail | h.schroeder@rohrig.de |

_… 66 additional similar items omitted._

## Notes / anomalies

- No read errors. All 693 files parsed cleanly (.docx / .xlsx / .pdf).

### False-positives screened out during scan (documented for audit)

- **»CN Citizen ID« hits on `91310000789123456X`** — this is the Brennhagen RCN
  subsidiary's **USCC (Unified Social Credit Code)**, i.e. a corporate
  registration number, not a personal 身份证. Province-code prefix »9« and
  the literal »USCC« label in context confirm corporate identity. Filtered.
- **»CZ rodné číslo« hit on `243210987`** in `07_Tochter_HU_Gyoer/RPL_IC_Rechnung_2020_01.docx`
  — this is actually a **Polish REGON** (company registry number, sister entity
  RPL Wroclaw), in the surrounding context »KRS 0000543210, NIP PL 6342876541,
  REGON 243210987«. The file lives in the HU folder but documents an
  intercompany invoice from RPL — note also the cross-folder filing
  anomaly below.
- **»SensitiveCat_health« hits on `Behandlung`** in CZ intercompany invoices
  refer to the VAT treatment (»DPH-Behandlung / Reverse Charge«), not health
  data. Filtered via DPH/MWSt/Reverse-Charge context filter.

### Employment contracts — explicit »no personal IDs« design

All employment contracts in CZ/HU/CN deliberately reference personal
identifiers as held off-document, which is the **correct** GDPR-aware design:

- CZ contracts: »Rodne cislo: auf Anfrage / on file (HR-Akte vertraulich)«
- HU contracts: »(Adoazonosito jel und Sozialversicherungsnummer im
  Personalakt hinterlegt)«
- CN contracts: »Hukou-Registrierung und Ausweis-Nr. liegen der Gesellschaft vor«

No CZ rodné číslo, HU TAJ, or CN 身份证 values were ever materialised in any
of the 693 scanned files.

### IBAN check

**No IBANs at all** were found in any of the 693 files for these three
subsidiaries — neither whitelisted nor suspicious. Bank-detail blocks in
intercompany invoices reference »Konto-Nr. / SWIFT auf Anfrage« patterns
rather than full IBANs.

### Domain inconsistency (informational, not PII)

The canonical Brennhagen email domain per `enhance_lib.py` is
`brennhagen-elektronik.de`. The CN folder uses `rohrig.cn` and `rohrig.de`
(e.g. `liang.wei@rohrig.cn`, `tax@rohrig.de`, `h.schroeder@rohrig.de`).
These belong to the fictional Brennhagen group, not third-party persons, so this
is **not a PII finding** — but it is a **consistency anomaly** worth
flagging to the data-generation pipeline.

### Cross-folder filing anomaly (informational)

`07_Tochter_HU_Gyoer/` contains multiple files prefixed `RPL_…` (e.g.
`RPL_IC_Rechnung_2020_01.docx`) that document the Polish subsidiary's
intercompany invoicing, not Hungarian. Not a PII issue, but it explains
the apparent »CZ rodné číslo« hit (which was actually a Polish REGON).

### External email addresses (LOW)

Only five unique external email patterns appear across all 693 files:

- `marsh.frankfurt@marsh.com` — Marsh insurance broker (functional inbox, fine)
- `tamas.hegedus@kpmg.hu` — KPMG Hungary auditor (named contact at the audit
  firm; consistent with the canonical »WP: KPMG« fact)
- `liang.wei@rohrig.cn` — canonical fictional CN employee, expected
- `tax@rohrig.de`, `h.schroeder@rohrig.de` — internal Brennhagen functional/named
  addresses (domain inconsistency noted above)

None of these resolve to public free-email providers (gmail, gmx, etc.),
none reference identifiable real persons outside the canonical fictional set,
and the KPMG contact is a plausible auditor-firm functional contact.
