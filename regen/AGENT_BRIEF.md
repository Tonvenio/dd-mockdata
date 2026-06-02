# Parallel Re-generation Agent Brief — roehrig_large

You are one of ~15 parallel agents enriching `roehrig_large/`.
Other agents are working on other folders concurrently. **Do not touch any folder
except the one you are assigned.**

## Repo & helper

```python
import sys
sys.path.insert(0, "."
from enhance_lib import ROEHRIG_AG as R, ROEHRIG_SUBS as S, write_doc, signatures

H = {"name": R["name"], "addr": R["addr"], "hrb": R["hrb"]}
```

`write_doc(path, header, title, sections, subtitle=None, confidential=False, draft=False)`
overwrites a .docx atomically. `sections` is a list of `(heading, body)` tuples where body
is one of:

- `str` — paragraph text (split on blank line)
- `list[list[str]]` — table (first row is header)
- `("list", [...])` — bullet list
- `("clauses", [("§ 1 Heading", ["para1", "para2"]), ...])` — numbered § clauses

`signatures(left_name, left_role, left_company, right_name, right_role, right_company,
            place="Stuttgart", date_str_="—")` returns a signature block string.

## CANONICAL FACTS — Brennhagen Elektronik AG

Use these consistently. Do not invent contradictory names/dates/figures.

**Company:**
- Name: Brennhagen Elektronik AG (publicly listed Prime Standard, Frankfurter Wertpapierbörse)
- Address: Vaihinger Straße 120, 70567 Stuttgart
- HRB 726451, Amtsgericht Stuttgart
- WKN RHGRP1, ISIN DE000RHGRP12
- Grundkapital: 62.500.000 EUR (62,5 Mio. Stückaktien)
- IPO: 14. Oktober 2022, Emissionskurs 24,50 EUR/Aktie, Erlös 612 Mio. EUR

**Vorstand (until 30.6.2024):**
- Anna Müller — CEO / Vorsitzende
- Laura Bauer — CFO
- Dr. Thomas Weber — COO
- Stefan Hoffmann — CTO (verlässt zum 30.6.2024)

**Vorstand-Neubestellungen 2024:**
- Dr. Petra Hollmann — CTO ab 1.7.2024 (von Continental)
- Dr. Yuki Tanaka — CRO Asia (Vorstand International) ab 1.4.2024 (von Denso)
- Stefan Richter — CMO/BD ab 1.4.2023 (von Siemens)

**Aufsichtsrat (5 Mitglieder, Amtsperiode seit 14.6.2022 bis HV 2026):**
- Dr. Klaus Steinbrück — Vorsitz (ehem. CEO ZF Friedrichshafen)
- Prof. Dr.-Ing. Gerhard Voss — stellv. Vorsitz, Prüfungsausschuss-Vorsitz (TU München)
- Dr. Ingrid Schöllkopf — stellv. Prüfungsausschuss (ehem. KPMG-Partnerin)
- Marlies Dürr — Arbeitnehmervertreterin / Konzernbetriebsrats-Vorsitzende (IG Metall)
- Thomas Reinhardt (MdB) — ehem. Bundestagsabgeordneter, Public Affairs

**Konzern-Schlüsselpersonen:**
- Group Treasurer: Markus Pflanzer
- Group Tax Director: Dr. Heike Berger
- Group Controller: Florian Maier
- Chief Audit Executive (CAE): Andreas Bühler
- Stv. Konzernbetriebsrats-Vorsitz: Klaus Bauer (Werk Heilbronn)

**Beratungs- und Bankenpartner:**
- Wirtschaftsprüfung: KPMG AG WPG (Lead Partner Dr. Maximilian Brand)
- Anwaltskanzlei: Hengeler Mueller (Frankfurt)
- M&A-Berater: Goldman Sachs (Frankfurt), Roland Berger
- Notarin: Dr. Karin Sonneborn, Stuttgart
- Kernbanken (5): Deutsche Bank AG (Konsortialführer), Commerzbank AG, UniCredit Bank AG
  (HVB), BNP Paribas, HSBC Continental Europe
- Joint Bookrunners IPO 2022: Deutsche Bank, Berenberg, Commerzbank
- Aktuarberater Pensionen: Heubeck AG (Köln)
- Versicherer D&O: Allianz Global Corporate & Specialty SE (50 Mio. EUR VS)

**Tochtergesellschaften (alle 100% Tochter via RHO):**
| Short | Name | Sitz | MA | Funktion |
|---|---|---|---:|---|
| REG | Brennhagen Elektronik GmbH | Heilbronn (DE) | 820 | Hauptwerk Produktion |
| RSG | Brennhagen Software GmbH | München (DE) | 340 | Embedded Software / ADAS |
| RPL | Brennhagen Polska Sp. z o.o. | Katowice (PL) | 960 | EMS / SMD |
| RCZ | Brennhagen CZ s.r.o. | Brno (CZ) | 680 | Steckverbinder |
| RHU | Brennhagen Hungary Kft. | Győr (HU) | 540 | Sensorik |
| RCN | Brennhagen (Shanghai) Co. Ltd. | Shanghai (CN) | 320 | Asien-Vertrieb |
| RHO | Brennhagen Holding GmbH | Stuttgart (DE) | 45 | Holding/Mgmt |

**Lokale Werkleitungen:**
- REG (Heilbronn): Werkleiter Andreas Maier; Q-Leitung Sabine Brand
- RSG (München): Werkleiter Dr. Klaus Kessler; Lead Developer Lars Wittmann
- RPL (Katowice): Werkleiter Marek Wojciechowski; HR Anna Kowalska
- RCZ (Brno): Werkleiter Petr Novák; Q-Leitung Eva Černá
- RHU (Győr): Werkleiter László Kovács; HR Andrea Szabó
- RCN (Shanghai): Country Manager Zhang Hao; Finance Liang Wei

**Produkte:**
- **ICP-3** — InfoConnect Pro (Infotainment-Modul) — Hauptkunden BMW, Mercedes
- **BMS-12** — BatteryMS-12 (Batteriemanagementsystem EV) — Hauptkunde VW (ID.7), Hyundai
- **ADAS-V4D** — Radar Fusion Steuergerät (Level-2/3 ADAS) — Mercedes, Stellantis
- **ECU-900** — Powertrain-ECU Gen3 — VW (MEB+/MQB-Evo), Stellantis
- **LightCtrl-7** — Matrix-LED Steuermodul — Audi, BMW

**OEM-Kunden:** BMW Group, Volkswagen AG, Mercedes-Benz Group AG, Stellantis N.V.,
Ford-Werke GmbH, Continental AG, ZF Friedrichshafen AG, Robert Bosch GmbH, Hyundai
Motor Company (KR), CATL (CN, BMS-OEM).

**Financials (Konzern, IFRS, Mio. EUR):**
| | 2020 | 2021 | 2022 | 2023 |
|---|---:|---:|---:|---:|
| Umsatz | 542 | 580 | 600 | 612 |
| EBITDA | 64 | 70 | 73 | 74,3 |
| EBIT | 38 | 42 | 47 | 48,9 |
| FTE | 3.620 | 3.820 | 4.020 | 4.180 |
| Dividende EUR/Aktie | 1,20 | 1,40 | 1,80 | 2,10 (geplant) |

**Finanzierung:**
- Konsortialkredit 2022: 250 Mio. EUR senior facility, Laufzeit 14.3.2022 – 14.3.2027
- Tranche A 150 Mio. Termloan, Tranche B 100 Mio. RCF
- Konsortium: DB (80) / CB (40) / UC (50) / BNP (40) / HSBC (40)
- Financial Covenants: Net Debt/EBITDA ≤ 3,0x; ICR ≥ 4,0x; EQ-Quote ≥ 30 %
- Sustainability-linked margin adjustment ±5 bp (Scope 1+2, Frauenanteil, Erneuerbare)

**Zertifizierungen:**
- IATF 16949 (alle Produktionswerke)
- ISO 9001:2015, ISO 14001:2015, ISO 50001:2018 (Energie), ISO 27001:2022 (in Vorbereitung)
- ASPICE Level 2-3 (RSG München)
- VDA 6.3 (Lieferanten-Audits)

## QUOTING RULES — critical to avoid Python syntax errors

In Python source strings, **NEVER** use German typographic quote pairs
`„`…`"` (U+201E / U+201D) — they often collide with ASCII string delimiters.

✅ Use German guillemets `»…«` inside prose. They are safe.
✅ Use ASCII `"…"` only as Python string-literal delimiters.
✅ Use single quotes `'…'` sparingly inside double-quoted strings.
✅ Use `ae`/`oe`/`ue`/`ss` if you want to avoid umlauts entirely (most existing
   scripts use this convention to dodge encoding issues).

## Word-count targets (type-dependent)

| Document type | Target words |
|---|---|
| Verträge / Liefer-/Service-/Beratungs-Verträge | 800–1500 |
| Sitzungsprotokolle / Quartalsberichte / Audit-Berichte | 400–800 |
| 8D-Reports / FMEA / Prüfberichte | 300–600 |
| Erklärungen / Konformitätsbescheinigungen / kurze Briefe | 200–400 |
| Personalakten / Arbeitsverträge | 500–900 |
| Patentschriften / Bescheide / IP-Dokumente | 300–600 |
| Betriebsrats-Protokolle | 300–500 |
| Projektakten (Charter/Gate-Review/Lessons-Learned) | 300–600 |

**Minimum acceptable: 200 words.** Below = fail.

## DELIVERABLE

1. Write `regen/regen_roehrig_<folder>.py` containing
   a self-contained idempotent script that overwrites each thin .docx in your folder.
2. Run the script: `python3 regen/regen_roehrig_<folder>.py`
3. Re-count thin docs (use the snippet below). Aim for **0 remaining thin**.
4. Report back (terse, ≤ 200 words): docs written, final thin count, anomalies.

```python
# Verification snippet — run after your script:
from docx import Document
from pathlib import Path
base = Path("roehrig_large/<YOUR_FOLDER>")
total = thin = 0
for p in base.rglob("*.docx"):
    d = Document(p); t = " ".join(par.text for par in d.paragraphs)
    for tbl in d.tables:
        for r in tbl.rows:
            for c in r.cells: t += " " + c.text
    w = len(t.split()); total += 1
    if w < 200: thin += 1
print(f"{total} total, {thin} still thin")
```

## DOC TYPE DETECTION HINTS

Detect doc type from the filename prefix. Common patterns in `roehrig_large/`:

| Prefix | Type | Example |
|---|---|---|
| `REA_AR_Sitzungsprotokoll_*` | Aufsichtsrat-Protokoll | 400-800w |
| `REA_HV_Protokoll_*` | Hauptversammlungs-Protokoll | 600-1000w |
| `REA_Vorstand_Bestellung_*` | Vorstandsbestellungsvertrag | 500-800w |
| `REA_FX_Hedge_*` | Treasury-Quartalsbericht FX | 400-600w |
| `REA_Covenant_Compliance_*` | Konsortialkredit Quartals-Reporting | 400-500w |
| `REA_IFRS_Bilanzierungsrichtlinie_*` | IFRS Accounting Policy | 500-900w |
| `TP_LocalFile_*` | Transfer Pricing Local File | 500-800w |
| `BR_*_Protokoll_*` | Betriebsrats-Protokoll | 300-500w |
| `8D_*` | 8D-Report (D1-D8) | 400-600w |
| `PRJ-*_Charter_*` | Projekt-Charter | 400-700w |
| `PRJ-*_Gate_*` | Stage-Gate-Review | 400-600w |
| `PRJ-*_Lessons_Learned_*` | Post-Mortem | 300-600w |
| `PRJ-*_Testbericht_*` | Funktions-/EMV-/Pruef-Bericht | 300-600w |
| `*_Arbeitsvertrag_*` | Arbeitsvertrag | 500-900w |
| `*_OEE_*`, `*_MonatsPL_*` | Werks-KPI/Reporting (xlsx-Companion) | 200-400w |
| `*_Rahmenliefervertrag_*` | OEM-Liefervertrag | 800-1200w |
| `*_Auftragsbestätigung_*` | OEM-AB | 300-500w |
| `*_8D_*` | 8D | 400-600w |
| `*_PPAP_*` | Production Part Approval Process | 300-500w |
| `Patent_*` | Patentdokument / Bescheid | 300-500w |

If files seem misplaced (e.g., `RPL_Arbeitsvertrag_*` in `02_Finanzen`) — that is
intentional realism (the original generator sprinkles ~5% "wrong folder" docs). Treat
the file by its filename type, not its containing folder.
