# PII Scan Brief — dd-mockdata

You are one of ~14 parallel agents performing a **DSGVO / GDPR sweep** of the
mock-data repository. The dataset is entirely fictional but plausibly written —
your job is to find anything that could be (or look like) **real personal data of
real individuals**, accidentally introduced.

## Canonical fictional whitelist (DO NOT flag these — they are by design)

### Halbreiter Maschinenbau GmbH (mueller_small)
- Company: HRB 47312 AG Köln, Industriestraße 12, 50829 Köln
- USt-IdNr.: DE 198 765 432; Steuernummer 215/5765/9876
- IBAN: DE89 3007 0010 0123 4567 89; BIC DEUTDEDB; Deutsche Bank
- People: Klaus Müller (CEO, geb. 12.02.1963), Sandra Becker (CFO, geb. 07.09.1977),
  Andrea Hoffmann (HR), Stefan Braun (Einkauf), Michael Weber (F&E),
  Markus Fischer, Jan Müller, Lisa Schulz, Thomas Schneider, Julia Krause,
  Petra Zimmermann, Sabine Koch, Wolfgang Brettschneider (BR-Vorsitz), Klaus Bauer,
  Anette Klein, Andreas Goebel, Markus Helmer, Felix Engelhardt
- Top customers: ThyssenKrupp Steel Europe AG, Bosch Rexroth AG, Hella, Viessmann, Dürr
- Top suppliers: Schunk, Igus, Siemens, Trumpf, Festo

### Sentavia Precision GmbH (biotech_medium)
- Company: HRB 218934 AG München, Freimannstraße 45, 80939 München
- USt-IdNr.: DE 287 432 109; Steuernummer 143/201/89231
- IBAN: DE42 7002 0270 0012 3456 00; BIC HYVEDEMMXXX; UniCredit/HypoVereinsbank
- People: Dr. Katharina Berger (CEO), Dr. Marcus Vogt (CTO), Thomas Müller (CFO),
  Dr. Annika Schmidt (CMO), Dipl.-Ing. Stefan Hoffmann (QRA),
  Andrea Schneider (Head of Ops, Prokura), Björn Hoffmann (Head of Finance, Prokura),
  Dr. Markus Lehmann (DSB)
- Investors: Sofinnova Partners, Lakestar, HTGF
- Notified Body: TÜV SÜD (0123)

### Brennhagen Elektronik AG (roehrig_large)
- Company: HRB 726451 AG Stuttgart, Vaihinger Straße 120, 70567 Stuttgart
- USt-IdNr.: DE 312 487 901; WKN RHGRP1; ISIN DE000RHGRP12
- Vorstand: Anna Müller (CEO), Laura Bauer (CFO), Dr. Thomas Weber (COO),
  Stefan Hoffmann (CTO bis 30.6.2024), Dr. Petra Hollmann (CTO ab 1.7.2024),
  Dr. Yuki Tanaka (CRO Asia), Stefan Richter (CMO/BD)
- Aufsichtsrat: Dr. Klaus Steinbrück (Vorsitz), Prof. Dr. Gerhard Voss,
  Dr. Ingrid Schöllkopf, Marlies Dürr (AN-Vertretung), Thomas Reinhardt MdB
- Konzern: Markus Pflanzer (Treasurer), Dr. Heike Berger (Tax),
  Florian Maier (Controller), Andreas Bühler (CAE)
- Werkleitungen: Andreas Maier (REG), Dr. Klaus Kessler (RSG), Marek Wojciechowski (RPL),
  Petr Novák (RCZ), László Kovács (RHU), Zhang Hao (RCN)
- WP: KPMG (Dr. Maximilian Brand); Anwalt: Hengeler Mueller
- OEMs: BMW, VW, Mercedes-Benz, Stellantis, Ford, Continental, ZF, Bosch, Hyundai

The full canonical fact list is in `enhance_lib.py`.

## What to FLAG

### Category A — direct PII patterns (regex scan)
- **IBANs** outside the canonical 3 (above). Run a check-digit (mod-97) test;
  IBANs that pass mod-97 but aren't on the whitelist are suspicious.
- **Emails** referencing real personal addresses (gmail.com, yahoo, t-online,
  freenet, web.de, gmx, hotmail) attached to anyone resembling a real person.
- **German Steuer-Identifikationsnummer** (11 digits, distinct from USt-IdNr)
  per Person — should not exist in mock data at all.
- **Sozialversicherungsnummer** (12-character format with letters) — must not exist.
- **Credit card numbers** — 13-19 digit patterns passing Luhn check — must not exist.
- **Real phone numbers** (random-looking, not matching the canonical company numbers
  +49 221 47832-* / +49 89 32178-* / corporate switchboards).
- **Real-looking addresses** (street + PLZ + city) not on the canonical list and not
  matching a recognised OEM/supplier/Partner from the canonical list.

### Category B — DSGVO Art. 9 special categories (keyword scan)
- Health/disease/medication info tied to a NAMED individual
- Religious belief / Kirchenmitgliedschaft for a NAMED individual
- Political opinion for a NAMED individual (beyond "MdB Thomas Reinhardt" canonical fact)
- Sexual orientation, gender identity
- Criminal records / Strafregisterauszug for a NAMED individual
- Trade union membership for a NAMED individual (beyond "Marlies Dürr, IG Metall" canonical)
- Genetic / biometric data
- Patient identifiers in clinical trial docs (study subject IDs are fine; real names are not)

### Category C — outright "real person" risk
- Names of **real public figures** (current/former politicians, celebrities,
  CEOs of real companies who aren't fictional canonical persons)
- References to **real medical patients** in biotech clinical study docs
- Real photos or signatures (image embeds in docx — check `doc.inline_shapes`)
- Real birthdays / ages of identifiable real persons
- Real geo-coordinates pointing to private residences

### Category D — what NOT to flag
- The canonical fictional people, addresses, IBANs, tax IDs listed above
- Real-but-public company names used as customers/suppliers (BMW, VW, Mercedes etc.)
  — these are organizations, not personal data
- Fictional employee names (e.g. AV_017_Sabine_Müller) — even if the surname
  happens to be common, that alone is not a flag
- References to real laws/regulations (DSGVO, AktG, IATF, etc.)

## How to scan

```python
import re
from pathlib import Path
from docx import Document
import openpyxl

# IBAN regex (Germany + adjacent)
IBAN_RE = re.compile(r'\b[A-Z]{2}\d{2}[\s\d]{15,32}\b')
EMAIL_RE = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
PHONE_RE = re.compile(r'\+\d{1,3}[\s-]?\d[\d\s\-/]{6,18}')
PLZ_ADDR_RE = re.compile(r'\b\d{5}\s+[A-ZÄÖÜ][a-zäöüß]+\b')

WHITELIST_IBANS = {
    'DE89 3007 0010 0123 4567 89'.replace(' ', ''),
    'DE42 7002 0270 0012 3456 00'.replace(' ', ''),
    # Brennhagen hat im Konzern mehrere IBANs — KEINE feste Liste; alle DE-IBANs durch
    # mod-97 testen und manuell beurteilen
}
WHITELIST_EMAIL_DOMAINS = {
    'halbreiter-maschinenbau.de', 'sentavia-precision.de', 'brennhagen-elektronik.de',
}
PUBLIC_DOMAINS = {'gmail.com','yahoo.com','t-online.de','freenet.de','web.de',
                  'gmx.de','gmx.net','hotmail.com','outlook.com'}

def iban_mod97(iban: str) -> bool:
    iban = iban.replace(' ', '').upper()
    if not re.match(r'^[A-Z]{2}\d{2}[A-Z0-9]+$', iban): return False
    rearr = iban[4:] + iban[:4]
    num = ''.join(str(ord(c)-55) if c.isalpha() else c for c in rearr)
    return int(num) % 97 == 1

def scan_text(text, fpath):
    findings = []
    for m in IBAN_RE.findall(text):
        ib = m.replace(' ', '')
        if iban_mod97(ib) and ib not in WHITELIST_IBANS:
            findings.append(('HIGH', 'IBAN', m, fpath))
    for m in EMAIL_RE.findall(text):
        domain = m.split('@')[1].lower()
        if domain in PUBLIC_DOMAINS:
            findings.append(('HIGH', 'PublicEmailDomain', m, fpath))
    # phone, address, special categories etc.
    return findings

# scan all .docx in your assigned folder; also try .xlsx and .pdf for completeness
```

For **.pdf** use `pdfplumber` if available, else skip (note in report).
For **.xlsx** use openpyxl; iterate cells.

## Deliverable

Write findings to **`regen/pii_findings_<your_folder_key>.md`**.

Format:
```markdown
# PII Findings — <folder>

- Files scanned: N
- Files with findings: M
- HIGH severity: H
- MED severity: D
- LOW severity: L

## High-severity findings

| File | Category | Excerpt |
|---|---|---|
| folder/foo.docx | RealIBAN | DE12 5004 0000 ... |
| folder/bar.docx | PublicEmail | jdoe@gmail.com |

## Medium-severity findings
...

## Notes / anomalies
```

Then **report back ≤ 200 words** with: total files scanned, count of HIGH/MED findings,
2-3 most concerning examples (file + category + excerpt), and any anomalies.

## Quoting rules — same as elsewhere
- ASCII straight quotes in Python source
- »…« in German prose
- No `„…"` typographic quotes in source code
