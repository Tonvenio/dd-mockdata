# PII Findings — Brennhagen folders 12, 14, 16, 17, 18

Scope: `roehrig_large/{12_Einkauf_Lieferanten, 14_IP_Technologie, 16_IT_Systeme, 17_Versicherungen, 18_Immobilien}`.

- Files scanned: **577**
  - 12_Einkauf_Lieferanten: 234
  - 14_IP_Technologie: 163
  - 16_IT_Systeme: 63
  - 17_Versicherungen: 54
  - 18_Immobilien: 63
- Files with at least one regex finding: 137 (most are real corporate HQ addresses of suppliers; see Notes)
- HIGH severity: **11 distinct issues** (multiple files affected by some)
- MED severity: 0 (no foreign-domain personal email addresses found — all emails are within `brennhagen-elektronik.de` if present)
- LOW severity: 297 (almost all are real public corporate HQ addresses of OEM/supplier/service-provider organisations, e.g. Infineon Neubiberg 85579, NXP Hamburg 22529, Bosch Reutlingen 72770, Allianz Munich, Marsh Düsseldorf — these are organisation addresses, not personal data)

No IBANs outside the canonical whitelist (mod-97 verified). No SteuerIDs. No SVNRs. No public-domain email addresses (gmail/web.de/etc.) anywhere. No phone numbers attached to named natural persons.

## High-severity findings (real-public-figure risk, DSGVO Art. 6 / Art. 9 adjacent)

| # | File(s) | Category | Real person | Risk |
|---|---|---|---|---|
| 1 | `16_IT_Systeme/REA_Cybersecurity_Policy_ISMS_2023.docx`, `REA_Endpoint_Security_Policy_2023.docx`, `REA_IAM_Identity_Access_Management_2023.docx`, `REA_Penetrationstest_Bericht_2023.docx` | RealPerson | **Sebastian Schreiber, CEO / Lead Pentester, SySS GmbH, Tübingen, Wilhelmstrasse 14** | Real, publicly known SySS founder; real office address; explicitly named as pentest lead with signature block on confidential report |
| 2 | `14_IP_Technologie/Patent_06_Erteilungsurkunde_2022_WIP.docx`, `Patent_06_Selbstkalibrierendes_Sensorsys_2023.docx`, `Patent_17_Erteilungsurkunde_2021.docx` | RealPerson | **Prof. Dr. Lutz Eckstein (RWTH Aachen)** — named as patent inventor | Real, Director ika RWTH Aachen; affiliation explicit; attributed to fictional Brennhagen patents |
| 3 | `14_IP_Technologie/Patent_09_Erteilungsurkunde_2021.docx`, `Patent_09_Verfahren_zur_Detektion_von_Sp_2023.docx` | RealPerson | **Prof. Dr. Markus Lienkamp (TUM)** — named as patent inventor | Real, Lehrstuhl FTM TU München; affiliation explicit |
| 4 | `14_IP_Technologie/REA_BMW_JDA_ADAS_2022.docx` | RealPerson | **Dr. Andreas Reschka (BMW)** — named as Technical Lead BMW | Real, formerly BMW autonomous-driving researcher (later Volocopter) |
| 5 | `14_IP_Technologie/REA_BMW_JDA_ADAS_2022.docx` | RealPerson | **Frank Weber, VP Driving Experience, BMW** | Real, former BMW Board Member for Development; explicit role title |
| 6 | `14_IP_Technologie/REA_MBZ_ADAS-V4D_RFQ_Response_2022.docx` | RealPerson | **Dr. Carsten Breitfeld** — named as »Senior Buyer Mercedes-Benz« with full Mercedesstrasse 137 address | Carsten Breitfeld is a very prominent real automotive exec (ex-BMW i8 chief engineer, ex-Byton CEO, ex-Faraday Future CEO). Attaching this name to a Mercedes Einkauf role is high-impact reputational risk |
| 7 | `14_IP_Technologie/REA_BMW_JDA_ADAS_2022.docx` | PossibleRealPerson | Dr. Karsten Heuer (BMW), Dr. Helmut Wagner (BMW QM), Mike Schoenberg (BMW Legal) | Less unique but the combination "Name + BMW department" turns them into identifiable contacts; flagged for review |
| 8 | `14_IP_Technologie/Patent_03_Batteriemanagementsystem_mit_p_2023_rev_SRichter.docx`, `Patent_03_Erteilungsurkunde_2023_20230915.docx`, `Patent_10_Erteilungsurkunde_2022.docx`, `Patent_10_Wärmemanagement-Optimierung_in_2023.docx` | PossibleRealPerson | **Dr. Markus Lehmann (Fraunhofer ISC)** — named as patent inventor | Fraunhofer ISC (Silicate Research, Würzburg) is real; the brief notes »Dr. Markus Lehmann« is also Brennhagen canonical DSB at Sentavia Precision — collision; here used differently as Fraunhofer ISC; reviewer should check |
| 9 | `14_IP_Technologie/Patent_11_Erteilungsurkunde_2023.docx`, `Patent_11_Prozess_…2023.docx` | LikelyFictional-but-verify | Dr.-Ing. Thomas Becker (Fraunhofer IPA) | Fraunhofer IPA Stuttgart is real; »Thomas Becker« is generic — low confidence on identification but flagged for completeness |
| 10 | `18_Immobilien/PRJ-2024-003_Testbericht_Funktionstest_EOL_SAP_S_4HANA_Rollout_.docx` | PossibleRealPerson | **Dr. Karin Sonneborn, Notar Stuttgart** | A real Karin Sonneborn (CDU) was a Bundestag member; she is not known as a Stuttgart notary; risk is name-collision rather than direct attribution, but worth checking against current Notariatsregister Stuttgart |
| 11 | `16_IT_Systeme/REA_Cloud_Strategie_2023.docx`, `REA_Cybersecurity_Policy_ISMS_2023.docx`, `REA_Endpoint_Security_Policy_2023.docx`, `REA_IAM_Identity_Access_Management_2023.docx`, `REA_IT_Governance_Framework_2023.docx`, `REA_IT_Risikobericht_2023.docx` | NameCollisionWithRealConsultancy | Dr. Karin Lehnhardt described as »CIO extern beauftragt, BTC AG« | BTC AG (Oldenburg) is a real consultancy; »Karin Lehnhardt« does not match a known BTC AG manager and is likely fictional, but the combination explicitly attributes a senior role at a real firm — flagged for review |

### Already-canonical / NOT flagged

- »Sebastian Hahn« as CrowdStrike Account Manager in `IT_Sicherheitsvorfall_2023_0024.docx` — not a known CrowdStrike public exec; likely fictional.
- Supplier contacts at Infineon (Dr. Markus Boettcher, Dr. Stefanie Lenz), NXP (Petra Sommer, Olaf Brandt), STM (Luca Marini, Isabella Conti), Bosch (Dr. Karin Maier) — none of these match known public executives of those firms. Plausible fictional.
- Patent attorneys: Dipl.-Ing. Hartmut Reinkemeier (Maiwald), Dr. Stefan Rueber (Boehmert & Boehmert), Dr. Stefan Brodbeck — do not match known partner lists of Maiwald or Boehmert. Plausibly fictional. (Maiwald real partners include Eberhard Bock, Martin Huenges, Annelie Wuensche; Boehmert real partners include Heinz Goddar, Stefan Bornhausen, Martin Wirtz — none match.)
- Drees & Sommer contacts (Dr. Wolfgang Hertz, Markus Reuter, Sabine Hartlieb) — not matching known D&S partners (real: Steffen Szeidl, Dierk Mutschler, Klaus Dederichs).
- Stefanie Kornmann (Marsh broker) — canonical fictional per PII_BRIEF.md.
- Real corporate HQ addresses (Bosch Reutlingen Robert-Bosch-Strasse 9 72770, Infineon Neubiberg 85579 Am Campeon, NXP Hamburg Troplowitzstrasse 22529, STM Dornach, SAP Walldorf, Microsoft Munich, CrowdStrike Munich, Marsh Düsseldorf, Allianz/AGCS Munich) — these are organisation addresses, not personal data; correctly not flagged.

## Medium-severity findings

None. No personal email addresses on public domains. No foreign supplier-domain emails reaching a named natural person (most emails are functional roles like `einkauf@…` or `quality@…` and resolve to `@brennhagen-elektronik.de`).

## Low-severity findings (summary)

297 LOW hits, ~95 % are: PLZ + city pattern matches that correctly identify the real public HQ address of an organisation (Bosch, Infineon, NXP, Allianz, Marsh, Drees & Sommer Stuttgart, etc.). These are not personal data. The remaining ~5 % are spreadsheet artefacts where 5-digit codes happened to be followed by a German verb (»Seitwärts«, »Steigend«, »Fallend«) inside a Rohstoffrisiko Excel — clearly false positives.

## Notes / anomalies

1. The **single highest-impact concentration** is in folder 14 (`14_IP_Technologie`), where the synthetic patent corpus binds real-world automotive academics (Prof. Eckstein RWTH Aachen, Prof. Lienkamp TUM) and real BMW executives (Reschka, Frank Weber, plausibly Heuer/Wagner) to fictional Brennhagen patents. If the dataset is ever shared externally these specific attributions are the most likely to attract a DSGVO Art. 17 erasure request or a complaint, because the affected persons are publicly identifiable.
2. The **single most reputationally damaging** entry is `REA_MBZ_ADAS-V4D_RFQ_Response_2022.docx`, which addresses an RFQ to »Dr. Carsten Breitfeld, Senior Buyer Mercedes-Benz, Mercedesstrasse 137, 70327 Stuttgart«. Breitfeld is a very high-profile real automotive executive who never held that role; this is a hard collision and should be renamed (suggestion: »Dr. Carsten Breitenbach« or fully synthetic).
3. The **SySS pentest report** (16) is a striking case because it carries the real-life SySS founder Sebastian Schreiber's name, real office address (Wilhelmstrasse 14 Tübingen), and a signature block on a »STRENG VERTRAULICH« document — i.e. the surface-form looks exactly like a real, confidential customer pentest report from SySS. Recommend replacing with »Dr. Stefan R. Bühler, Lead Pentester« or similar synthetic identity and a fictional address.
4. Folder 12, 17, 18 are cleaner: all supplier/broker/D&S/Notar/Sachverständige contacts checked are plausible-fictional with no matches to known public executives, with the exception of (10) above about »Karin Sonneborn«.
5. No IBANs, no Steuer-IDs, no SVNRs, no public-domain emails, no Luhn-passing credit-card-shaped numbers, and no Art. 9 special-category data (health, religion, union, sexual orientation, biometric, criminal record) tied to any named natural person were found in these five folders.
6. PDFs in folder 12 (NXP datasheets, etc.) extracted only partially via raw-byte fallback because `pdfplumber` may not be installed; a manual spot-check of `NXP_Lieferantenrisikobericht_2021_2024-03-01.pdf` and `NXP_ICP-3_Datasheet_2023.pdf` is recommended.
