"""Brennhagen AG / 23_Projekte_Programme – Charters, Gates, Lessons, Testberichte,
Lastenheft, Pflichtenheft + 6 misplaced docs. ~180 docs.

Idempotent: overwrites only files that exist at expected paths.
"""
# --- portable-paths-prelude --- (do not edit) ---
import sys
from pathlib import Path as _PathlibPath
_RP = _PathlibPath(__file__).resolve().parent
while not (_RP / "enhance_lib.py").exists() and _RP.parent != _RP:
    _RP = _RP.parent
_ROOT = _RP
sys.path.insert(0, str(_ROOT))
# --- end prelude ---
import sys
from pathlib import Path
sys.path.insert(0, f"{_ROOT}")
from enhance_lib import ROEHRIG_AG as R, write_doc, signatures

BASE = Path(f"{_ROOT}/roehrig_large/23_Projekte_Programme")
H = {"name": R["name"], "addr": R["addr"], "hrb": R["hrb"]}


# ── Master Project Catalog ────────────────────────────────────────────────
# (prj_id, kurztitel, produkt, oem_kunde, leader, sponsor, budget_mio, start, ende,
#  zielbeschr, scope, risiken_top3)
PROJEKTE = [
    ("PRJ-2021-001", "ECU-900 Gen3 Entwicklung", "ECU-900",
     "VW (MEB+/MQB-Evo), Stellantis",
     "Dipl.-Ing. Andreas Schultheiss (REG)", "Dr. Thomas Weber (COO)",
     18.5, "Q1 2021", "Q4 2023",
     "Vollstaendige Entwicklung der dritten Generation der Powertrain-ECU mit "
     "32-bit Aurix TC397, AUTOSAR 4.3 R20-11 Stack, ISO 26262 ASIL-D und "
     "Cybersecurity nach ISO/SAE 21434. Zielkosten 78,50 EUR/Stueck bei "
     "Stueckzahlen 1,2 Mio. p.a.",
     ["Hardware-Design 8-lagiger PCB", "Bootloader + OTA",
      "Diagnose ueber UDS/DoIP", "Funktionssicherheits-Konzept",
      "EMV-/Klimavalidierung gem. LV124", "PPAP fuer VW + Stellantis"],
     ["Aurix-Liefersituation (Infineon Allocation) Q3/2022",
      "AUTOSAR-Stack-Lizenzkosten Vector ueber Plan",
      "ASIL-D Sicherheitsnachweis Konvergenz-Risiko"]),

    ("PRJ-2021-002", "ADAS-V4D Kalibrierungsplattform", "ADAS-V4D",
     "Mercedes-Benz",
     "Dr. Stefan Brodbeck (RSG)", "Stefan Hoffmann (CTO bis 6/2024)",
     12.2, "Q2 2021", "Q3 2023",
     "Aufbau einer durchgaengigen Kalibrierungsplattform fuer Radar-Fusion-"
     "Steuergeraete mit Vector vCDM Backend, MATLAB/Simulink Modellintegration "
     "und HiL-Pruefstand bei RSG Muenchen. Ziel: Reduktion Kalibrieraufwand "
     "von 18 auf 8 Wochen je Variante.",
     ["vCDM Server-Installation", "HiL-Bench dSpace Scalexio",
      "Mess-Plug-In INCA/CANape", "DOE-Skripte (Python)",
      "Trainings-Curriculum Kalibrierungs-Ingenieure"],
     ["Konvergenz HiL-Echtfahrt Lateralregler",
      "Lizenzdauer vCDM-Cluster",
      "Personalknappheit Cal-Engineering bei RSG"]),

    ("PRJ-2022-001", "BatteryMS-12 EV Plattform", "BMS-12",
     "Volkswagen (ID.7), Hyundai",
     "Dr. Petra Hollmann (REG, ab 7/2024 CTO)", "Dr. Thomas Weber (COO)",
     34.0, "Q1 2022", "Q1 2024",
     "Neuentwicklung des Batteriemanagementsystems der zwoelften Generation "
     "fuer 800-V-EV-Plattform mit Cell-Supervisor-Aufbau, aktivem Balancing, "
     "Hochvolt-Isolationsmonitoring und CCS-Schnellladekommunikation (ISO 15118-20). "
     "Zielsicherheit ASIL-D, Funktionsverfuegbarkeit 99,9 %.",
     ["CSC Hard- und Software", "BMU mit Aurix TC397XX",
      "ISO 15118-20 Plug & Charge", "Thermomanagement-Schnittstelle",
      "Cyber-Security HSM", "End-of-Line-Test-Setup REG Heilbronn"],
     ["Halbleitermangel CSC-ASICs bis Q2/2023",
      "VW PPAP-Zeitfenster gefaehrdet (SOP ID.7 verschoben)",
      "Hochvolt-Pruefstand Engpass Heilbronn"]),

    ("PRJ-2022-002", "InfoConnect Pro 4.0", "ICP-3",
     "BMW, Mercedes",
     "Lars Wittmann (RSG)", "Stefan Hoffmann (CTO)",
     22.7, "Q2 2022", "Q4 2024",
     "Major-Release des Infotainment-Moduls ICP-3 auf Linux-Kernel 6.1 LTS, "
     "Android Automotive OS 14, integrierter 5G/Wi-Fi-7-Stack und OTA-Update "
     "(SOTA/FOTA). UX-Refresh nach BMW-Style-Guide 2023. Ziel: Reduktion "
     "Bootzeit 18 → 6 s, App-Cold-Start < 800 ms.",
     ["Yocto Build-Pipeline", "Android Automotive Integration",
      "5G-Modem-Stack", "OTA-Backend (AWS)",
      "Sprach-Assistenz IVI", "App-Framework Drittentwickler"],
     ["BMW Style-Guide Spaet-Frozen",
      "Qualcomm SA8295 Liefersituation",
      "AOSP-Lizenzauflagen GMS Restriktion"]),

    ("PRJ-2022-003", "ECU-900 AUTOSAR Refactoring", "ECU-900",
     "VW (Plattformuebergreifend)",
     "Marco Frey (RSG)", "Dr. Thomas Weber (COO)",
     6.8, "Q3 2022", "Q2 2024",
     "Migration des bestehenden ECU-900-Software-Stacks von AUTOSAR 4.2 auf "
     "4.3 R20-11 mit Modernisierung des RTE-Generators, Einfuehrung Adaptive "
     "Platform fuer ausgewaehlte Apps und ASPICE-Level-3-Konformitaet. "
     "Reduzierte Build-Zeit < 12 min, Coverage > 90 % MC/DC.",
     ["Vector MICROSAR Update", "DaVinci Configurator",
      "Adaptive AUTOSAR Pilot", "Test-Coverage-Werkzeug VectorCAST",
      "Migration Legacy-BSW-Module"],
     ["Vector-Lizenzkosten ueber Budget",
      "RTE-Performance-Regression im Echtbetrieb",
      "Personalbindung Senior-Embedded-Engineers"]),

    ("PRJ-2023-001", "ADAS-V4D Radar Fusion", "ADAS-V4D",
     "Mercedes-Benz, Stellantis",
     "Dr. Stefan Brodbeck (RSG)", "Dr. Petra Hollmann (CTO ab 7/2024)",
     28.4, "Q1 2023", "Q4 2025",
     "Entwicklung eines Level-2+/Level-3-faehigen Radar-Fusion-Steuergeraets "
     "mit 4x Frontradar 77 GHz, 5x Eckradare, Kamera-Fusion und HD-Map-"
     "Integration. Ziel: Highway-Pilot bis 130 km/h, Stau-Pilot bis 60 km/h, "
     "Verfuegbarkeit > 98 % im freigegebenen ODD.",
     ["Sensor-Fusion-Algorithmus", "ODD-Definition",
      "HD-Map Provider Mercedes/HERE", "Sicherheits-Architektur ISO 21448 (SOTIF)",
      "Validierungs-Strecke / EuroNCAP-Konformitaet"],
     ["SOTIF-Nachweis nicht abschliessend definiert",
      "HD-Map Lizenz/Daten-Hoheit",
      "Konflikt Stellantis vs. Mercedes Requirements"]),

    ("PRJ-2023-002", "BatteryMS-12 China Adaptation", "BMS-12",
     "CATL, Hyundai (China)",
     "Zhang Hao (RCN, Country Mgr)", "Dr. Yuki Tanaka (CRO Asia)",
     9.6, "Q1 2023", "Q2 2024",
     "Lokalisierung der BMS-12-Plattform fuer chinesischen Markt: GB/T 18488-"
     "Konformitaet, MIIT-Zulassung, CATL-CSC-Schnittstelle, lokale "
     "Lieferantenbasis und Anbindung an chinesische Lade-Backends (GBT, NEV).",
     ["GB-T-Adaptation Software", "MIIT-Zulassungsverfahren",
      "Lokal-Lieferant fuer CSC-PCB",
      "Mandarin-UI fuer Diagnose-Tools",
      "Anbindung State-Grid-OCPI"],
     ["MIIT-Zertifizierungsdauer (>9 Mon.)",
      "Datentransfer-Restriktion (CSL-DSL-PIPL)",
      "Wechselkurs CNY-EUR Margin-Erosion"]),

    ("PRJ-2023-003", "ICP-3 OTA Update Platform", "ICP-3",
     "BMW, Mercedes",
     "Lars Wittmann (RSG)", "Dr. Petra Hollmann (CTO ab 7/2024)",
     11.3, "Q1 2023", "Q3 2024",
     "Aufbau einer skalierbaren OTA-Update-Plattform fuer Bestands- und "
     "Neufahrzeuge mit ICP-3-Modul (Linux + AOSP). Differential Updates "
     "(< 50 MB), Rollback in < 2 min, Update-Verteilung an > 1 Mio. Fahrzeuge "
     "binnen 30 Tagen. ISO/SAE 21434 + UN R155/156-Konformitaet.",
     ["AWS-Backend mit S3/CloudFront",
      "Delta-Patch-Engine (bsdiff/HDiffPatch)",
      "Signatur HSM (Thales Luna)",
      "Rollback-Mechanismus A/B-Partition",
      "Telemetrie/Monitoring (Grafana, Prometheus)"],
     ["UN R156 Type Approval Verzug",
      "AWS-Kostenexplosion bei Peak-Rollout",
      "Kryptographische Schluesselrotation"]),

    ("PRJ-2023-004", "Cost Reduction Program CZ", "Steckverbinder (RCZ)",
     "intern",
     "Petr Novak (Werkleiter RCZ)", "Dr. Thomas Weber (COO)",
     2.4, "Q2 2023", "Q4 2024",
     "Strukturiertes Kostenoptimierungs-Programm am Standort Brno: "
     "Material-Reduktion (Wertanalyse), Prozessverdichtung Stanzlinie, "
     "Energie-Einsparung 12 %, Reduktion Ausschussquote von 1,8 % auf < 0,9 %. "
     "Ziel-Einsparung 4,2 Mio. EUR p.a. ab 2025.",
     ["Wertanalyse VAVE-Workshops",
      "Stanzwerkzeug-Modernisierung",
      "Energie-Audit ISO 50001",
      "SMED-Programm Stanzlinie 3",
      "Schulungs-Curriculum Operator"],
     ["Werkleitung Wechselrisiko",
      "CAPEX-Freigabe Stanzwerkzeug (1,4 Mio. EUR)",
      "Energiepreis-Volatilitaet CZ"]),

    ("PRJ-2023-005", "Heilbronn Plant Expansion", "BMS-12 + Linie 4",
     "intern (Werks-Erweiterung REG)",
     "Andreas Maier (Werkleiter REG)", "Dr. Thomas Weber (COO)",
     38.0, "Q2 2023", "Q1 2025",
     "Errichtung einer vierten Produktionslinie BMS-12 im Werk Heilbronn "
     "(Hallenneubau 4.200 qm, Aufstockung 24 Arbeitsplaetze, Hochvolt-"
     "Pruefstand Phase 2, Energie-Eigenversorgung 1,8 MWp PV). Genehmigung "
     "Stadt Heilbronn 03/2023, Inbetriebnahme Q1 2025.",
     ["Baugenehmigung 06/2023",
      "Auftragsvergabe Hochbau (Goldbeck)",
      "Maschinenanschaffung (ASM, Heller, Krause)",
      "PV-Anlage 1,8 MWp inkl. Speicher",
      "Personalrecruiting +24 Mitarbeitende"],
     ["Lieferzeit Bestueckungsautomaten (ASM > 50 Wochen)",
      "Baukosteneskalation +12 % vs. Plan",
      "Genehmigungsverfahren Hochvolt-Pruefraum"]),

    ("PRJ-2024-001", "ECU-1000 Concept Study", "ECU-1000 (Nachfolger ECU-900)",
     "VW, Stellantis (Konzeptphase)",
     "Marco Frey (RSG)", "Dr. Petra Hollmann (CTO)",
     3.2, "Q1 2024", "Q4 2024",
     "Konzeptphase fuer die naechste ECU-Generation (ECU-1000) mit 64-bit "
     "Multi-Core-SoC, Adaptive-AUTOSAR-zentriertem Stack, OTA-First-Architektur "
     "und Zone-Controller-Faehigkeit fuer SDV. Liefer-Ergebnis: Konzept-Spec, "
     "Roadmap, Business-Case fuer Gate-G1.",
     ["Markt-/Technologie-Scouting",
      "Architektur-Vorentwurf",
      "Halbleiter-Marktanalyse (NXP S32G3, Renesas RH850/X4)",
      "Business-Case Tool (3 OEM-Szenarien)",
      "Patent-Recherche Adaptive Platform"],
     ["OEM-Anforderungen noch ungeklaert",
      "Halbleiter-Roadmap-Unsicherheit",
      "Personalverfuegbarkeit Architekten"]),

    ("PRJ-2024-002", "DSGVO Compliance Remediation", "DSGVO/IT-Compliance",
     "intern (Konzernweit)",
     "Dr. Anna Brand (Konzern-DSB)", "Anna Mueller (CEO)",
     1.8, "Q2 2024", "Q1 2025",
     "Umsetzung der Empfehlungen aus dem KPMG-Audit 2023 zur DSGVO-"
     "Konformitaet: Aktualisierung VVT, ROPA-Tool-Einfuehrung, AVV-"
     "Standardvertraege, Loeschkonzepte HR-System, DSFA Marketing-CRM, "
     "Schulungs-Rollout 4.180 MA.",
     ["VVT-Tool OneTrust Einfuehrung",
      "AVV-Workflow Onboarding",
      "Loeschkonzept SAP HR",
      "DSFA HubSpot/Salesforce",
      "E-Learning DSGVO 2024"],
     ["Lizenz-Kosten OneTrust ueber Plan",
      "Akzeptanz in Werken (CZ, HU, PL)",
      "Datenuebermittlung China (PIPL/Schrems II)"]),

    ("PRJ-2024-003", "SAP S/4HANA Rollout Polen", "ERP / SAP",
     "intern (RPL Katowice)",
     "Marek Wojciechowski (Werkleiter RPL)", "Laura Bauer (CFO)",
     7.4, "Q1 2024", "Q4 2025",
     "Greenfield-Migration des polnischen Werkes RPL von SAP ECC 6.0 auf "
     "S/4HANA 2023 mit lokalisierten Modulen (FI/CO/PP/MM/SD/QM), Fiori-"
     "Frontend, Anbindung an Konzern-EDW (SAP DataSphere) und Compliance "
     "polnisches KSeF/JPK.",
     ["Implementation Partner: T-Systems Polska",
      "Datenmigration Materialstamm 220.000 Positionen",
      "Customizing FI fuer PL-GAAP/MSSF",
      "KSeF-Anbindung E-Invoicing",
      "User-Trainings 960 MA"],
     ["KSeF-Frist 02/2026 nicht haltbar",
      "Datenqualitaet Altsystem (10 % Bereinigung)",
      "Change-Management lokale Akzeptanz"]),

    ("PRJ-2024-004", "LkSG Supply Chain Audit", "Lieferketten-Compliance",
     "intern (Konzern, alle Werke)",
     "Dr. Klaudia Hoffmann (Compliance)", "Stefan Richter (CMO/BD)",
     2.1, "Q1 2024", "Q4 2024",
     "Erstmalige Umsetzung des Lieferkettensorgfaltspflichtengesetz (LkSG) "
     "fuer Brennhagen-Konzern: Risikoanalyse 1.420 Direktlieferanten, "
     "Praeventionsmassnahmen, Beschwerdemechanismus, jaehrlicher BAFA-Bericht "
     "und Integration in SAP Ariba.",
     ["Lieferanten-Risikoanalyse (IntegrityNext)",
      "Beschwerdemechanismus (Whistleblowing-Tool EQS)",
      "BAFA-Bericht 04/2025",
      "Tier-2-Eskalations-Pfad (Konfliktmineralien)",
      "Schulungen Einkauf 86 MA"],
     ["Tier-2/3-Transparenz Halbleiter-Lieferkette",
      "China-Lieferanten DSGVO/PIPL-Konflikt",
      "BAFA-Berichtsformat erst spaet final"]),

    ("PRJ-2024-005", "Cybersecurity TISAX Level 3", "Cybersecurity",
     "intern (Konzern, Maingate fuer VDA-Audit)",
     "Andreas Buehler (CAE)", "Dr. Petra Hollmann (CTO)",
     3.6, "Q1 2024", "Q2 2025",
     "Erlangung der TISAX-Pruefung Level 3 (Assessment AL 3) fuer Standorte "
     "Stuttgart, Heilbronn, Muenchen, Brno: ISMS nach ISO 27001:2022, "
     "Schutzklasse hoch (Prototypenschutz, Datenschutz), Audit durch "
     "akkreditiertes Pruefhaus DEKRA.",
     ["ISMS-Aufbau ISO 27001:2022",
      "Asset-Management CMDB ServiceNow",
      "Penetration-Tests (Schwarz/Grey-Box)",
      "Awareness-Kampagne 4.180 MA",
      "DEKRA-Audit Q1/2025"],
     ["Personalengpass IT-Security (2 offene Stellen)",
      "Legacy-Systeme (RCZ Brno) erst migrieren",
      "Audit-Aufwand RSG Muenchen ASPICE Konflikt"]),
]


def _findings(prj_id, kurztitel, sponsor):
    # default sign block
    return signatures(sponsor.split("(")[0].strip(), "Projekt-Sponsor", R["name"],
                      "Projektleitung", "PL " + kurztitel, R["name"],
                      place="Stuttgart", date_str_="—")


# ── CHARTER ────────────────────────────────────────────────────────────────
def charter(prj_id, kurztitel, produkt, oem, leiter, sponsor, budget, start, ende,
            ziel, scope, risiken):
    # Filename: PRJ-2021-001_Charter_ECU-900_Gen3_Entwicklung.docx
    # Look up actual filename in directory.
    matches = list(BASE.glob(f"{prj_id}_Charter_*.docx"))
    if not matches:
        return None
    path = matches[0]
    write_doc(str(path), H,
        f"Projekt-Charter {prj_id} – {kurztitel}",
        subtitle=f"Projekt-Charter / Project Initiation Document (Version 1.0)",
        sections=[
            ("1. Projektidentifikation",
             [["Feld", "Inhalt"],
              ["Projekt-ID", prj_id],
              ["Projekt-Titel", kurztitel],
              ["Produkt-/Programm-Bezug", produkt],
              ["Hauptkunde / OEM", oem],
              ["Projektleitung", leiter],
              ["Projekt-Sponsor (Lenkungsausschuss-Vorsitz)", sponsor],
              ["Genehmigtes Budget (CAPEX + OPEX)", f"{budget:.1f} Mio. EUR"],
              ["Projektstart", start],
              ["Geplantes Projektende", ende]]),
            ("2. Hintergrund und strategische Einordnung",
             f"Das Projekt {prj_id} »{kurztitel}« ist Bestandteil der Konzern-Roadmap "
             f"2023–2027 der Brennhagen Elektronik AG und unterstuetzt die strategischen "
             f"Stossrichtungen »Electrification«, »Software-Defined Vehicle« und "
             f"»Operational Excellence«. Das Vorhaben wurde im Strategischen "
             f"Investitionsplan des Vorstands (Vorlage TOP 4 der Vorstandssitzung) "
             f"als »kritisch fuer die Wettbewerbsfaehigkeit« eingestuft und vom "
             f"Aufsichtsrats-Pruefungsausschuss zur Kenntnis genommen.\n\n"
             f"Hauptkunde bzw. interner Auftraggeber ist {oem}. Der Business-Case "
             f"baut auf einer Stueckzahlplanung und einem Zielkostenpfad auf, der mit "
             f"der Group-Controlling-Funktion (Florian Maier) abgestimmt wurde."),
            ("3. Projektziele (SMART)",
             ziel),
            ("4. Scope und Liefergegenstaende (in-Scope)",
             ("list", scope)),
            ("5. Out-of-Scope-Abgrenzung",
             "Nicht Bestandteil dieses Projektes sind: a) Anpassungen an angrenzenden "
             "Plattform-Komponenten ausserhalb der definierten Schnittstellen; b) Serien-"
             "begleitende A-Musterabnahmen Folgegenerationen; c) Vermarktung und Pre-Sales-"
             "Aktivitaeten; d) Lokalisierungen ueber die im Lastenheft fixierten "
             "Maerkte hinaus. Diese Themen werden ggf. in Folgeprojekten oder im "
             "Linienbetrieb adressiert."),
            ("6. Stakeholder-Matrix",
             [["Stakeholder", "Rolle", "Einflussgrad"],
              ["Vorstand REA", "Auftraggeber / Eskalation", "Hoch"],
              ["Lenkungsausschuss", "Quartalsentscheidungen", "Hoch"],
              [oem, "Externer Kunde / Spezifikation", "Hoch"],
              ["Konzern-Controlling", "Budget-Tracking", "Mittel"],
              ["Group Quality / VDA 6.3", "Q-Freigaben", "Mittel"],
              ["Konzernbetriebsrat", "Personalmassnahmen", "Mittel"],
              ["Group IT / SAP", "Systemintegration", "Niedrig–Mittel"]]),
            ("7. Top-Risiken bei Projektstart",
             ("list", risiken + [
                "Wechselkurs-Risiko EUR/USD bzw. EUR/CNY > 5 % im Projektzeitraum",
                "Personal-/Schluesselrollen-Risiko (Senior Engineers)",
                "Regulatorisches Risiko (Type Approval, Zertifizierungen)"])),
            ("8. Meilensteinplan (Gates)",
             [["Gate", "Inhalt", "Termin (geplant)"],
              ["G0", "Projekt-Initiierung / Charter freigegeben", start],
              ["G1", "Konzept-Freigabe (Konzept-Spec, Business-Case v2)", "+3 Monate"],
              ["G2", "Systemdesign-Freigabe (Architektur, Pflichtenheft)", "+9 Monate"],
              ["G3", "Detailentwicklung abgeschlossen (Codefreeze, B-Muster)", "Mitte Laufzeit"],
              ["G4", "Validierung abgeschlossen (PPAP/PV bestanden)", "Ende - 3 Monate"],
              ["G5", "Serienanlauf / SOP", "Projektende"],
              ["G6", "Hochlauf-Review (Lessons-Learned 1)", "+6 Monate nach SOP"],
              ["G7", "Lifecycle-Uebergabe an Linie", "+12 Monate nach SOP"]]),
            ("9. Budget-Struktur",
             f"Das Projektbudget von {budget:.1f} Mio. EUR teilt sich auf in rund "
             f"60 % Personalkosten (interne FTE und externe Beratungs-/Engineering-"
             f"Dienstleister), 25 % Hardware-/Pruefstand-/Werkzeug-Investitionen "
             f"(CAPEX, aktivierungspflichtig nach IAS 38), 10 % Software-Lizenzen "
             f"(Vector, dSpace, MathWorks, Synopsys) und 5 % Reise- und Schulungskosten. "
             f"Aktivierungspflicht wird durch Group Controlling im Quartalsrhythmus "
             f"geprueft. Reporting an Lenkungsausschuss monatlich, an Vorstand quartalsweise."),
            ("10. Freigaben und Unterschriften",
             _findings(prj_id, kurztitel, sponsor)),
        ])
    return path


# ── GATE REVIEW ─────────────────────────────────────────────────────────────
GATE_INFO = {
    "G1": ("Konzept", "Konzept-Spec, Business-Case v2, Top-Level-Architektur",
           ["Konzept-Spec v1.0 abgenommen", "Business-Case > 18 % IRR bestaetigt",
            "Risiko-Register (initial) freigegeben", "Konzept-Architektur Review-Workshop"]),
    "G2": ("Systemdesign", "System-Architektur, Pflichtenheft Version 1.0",
           ["Pflichtenheft abgenommen", "Architektur-Review Vector / dSpace",
            "FMEA D-FMEA + System-FMEA Stand 80 %",
            "Lieferanten-Vorvereinbarungen (RFI/RFQ)"]),
    "G3": ("Detailentwicklung", "Code-Freeze, B-Muster, Vor-Validierung",
           ["B-Muster lieferbar (intern)", "Code-Coverage > 80 % MC/DC",
            "Erste EMV-Vorpruefungen erfolgreich",
            "Bemusterungs-Plan fuer Kunden abgestimmt"]),
    "G4": ("Validierung", "PPAP, Production Validation, Type Approval",
           ["PV-Plan vollstaendig abgearbeitet", "PPAP Level 3 beim Kunden eingereicht",
            "Cyber-Security UN R155 / TISAX-Konformitaet",
            "EOL-Pruefstand abgenommen"]),
    "G5": ("Serienanlauf / SOP", "Serienproduktion startet, OEE > 75 %",
           ["SOP-Termin bestaetigt", "OEE > 75 % nach 3 Wochen",
            "Ausschuss < 0,5 %", "Reklamationsquote < 50 ppm"]),
    "G6": ("Hochlauf-Review", "Lessons-Learned 1, Stabilitaetsanalyse",
           ["KPI-Stabilitaet ueber 6 Mon.", "Lessons-Learned 1 dokumentiert"]),
    "G7": ("Lifecycle-Uebergabe", "Uebergabe an Produkt-Linien-Mgmt",
           ["Linien-Verantwortung dokumentiert"]),
}


def gate(prj_id, kurztitel, leiter, sponsor, gate_id, datum_str):
    matches = list(BASE.glob(f"{prj_id}_Gate_{gate_id}_*.docx"))
    if not matches:
        return None
    path = matches[0]
    g_name, g_inhalt, kriterien = GATE_INFO[gate_id]
    write_doc(str(path), H,
        f"Gate-Review {gate_id} – {g_name}",
        subtitle=f"{prj_id} – {kurztitel} | Lenkungsausschuss-Vorlage",
        sections=[
            ("1. Gate-Identifikation",
             [["Feld", "Inhalt"],
              ["Projekt-ID", prj_id],
              ["Projekt-Titel", kurztitel],
              ["Gate", f"{gate_id} – {g_name}"],
              ["Gate-Inhalt (Phase Exit)", g_inhalt],
              ["Sitzungstermin", datum_str],
              ["Sitzungsort", "Brennhagen Elektronik AG, Stuttgart (hybrid via Teams)"],
              ["Vorsitz", sponsor],
              ["Projektleitung", leiter]]),
            ("2. Status-Ampel",
             [["Dimension", "Status", "Kommentar"],
              ["Termin", "GELB", "Termintreue zu Soll-Datum innerhalb +/- 2 Wochen"],
              ["Budget", "GRUEN", "Plan-Ist-Abweichung < 5 %"],
              ["Qualitaet", "GRUEN", "Keine kritischen Mangel gemeldet"],
              ["Scope", "GRUEN", "Keine Scope-Aenderungen nach Charter"],
              ["Risiken", "GELB", "Drei Top-Risiken aktiv – Massnahmen definiert"]]),
            ("3. Erfuellung der Eintrittskriterien",
             ("list", [k + " – ERFUELLT" for k in kriterien])),
            ("4. Praesentierte Liefergegenstaende",
             "Im Rahmen der Gate-Sitzung wurden folgende Artefakte vom "
             "Projektteam praesentiert und vom Lenkungsausschuss inhaltlich "
             "abgenommen: Status-Bericht der vergangenen Phase, Risiko-Register "
             "mit Massnahmen-Status, Budget-Forecast inkl. EAC-Berechnung, "
             "technische Praesentation (Architektur-/Validierungs-Ergebnisse), "
             "Update der Stakeholder-Matrix sowie Update des Meilensteinplans "
             "fuer die naechste Phase. Alle Dokumente sind im Projekt-Wiki "
             f"unter /projekte/{prj_id}/gates/{gate_id}/ versioniert abgelegt."),
            ("5. Beratung und Diskussion",
             "Der Lenkungsausschuss diskutierte insbesondere die offenen Top-"
             "Risiken und die Auswirkungen auf die nachfolgende Phase. Group-"
             "Controlling (vertreten durch Florian Maier) bestaetigte die "
             "Budget-Aktualitaet und wies auf die Aktivierungspruefung gem. "
             "IAS 38 hin. Group Quality (vertreten durch Sabine Brand, REG) "
             "bestaetigte die Konformitaet mit IATF 16949 und VDA 6.3. "
             "Konzernbetriebsrat (Marlies Duerr) nahm die Personalplanung der "
             "Folgephase zur Kenntnis und meldete keine Einwaende an."),
            ("6. Beschluesse",
             ("list", [
                f"Gate {gate_id} wird FREIGEGEBEN (Phase Exit bestaetigt).",
                f"Naechste Phase darf gestartet werden; Budget der Folgephase "
                f"wird auf Basis aktualisierter EAC freigegeben.",
                "Top-Risiken sind in der Risiko-Sitzung monatlich zu reviewen.",
                "Status-Reporting an Lenkungsausschuss erfolgt weiterhin monatlich.",
                f"Folge-Gate ist gemaess Meilensteinplan terminiert.",
             ])),
            ("7. Aktionsliste (Folgemassnahmen)",
             [["Nr.", "Aktion", "Verantwortlich", "Termin"],
              ["1", "Aktualisierung Risiko-Register und Verteilung an SC", leiter, "+2 Wochen"],
              ["2", "Detailbudget Folgephase im SAP CO buchen", "Florian Maier", "+3 Wochen"],
              ["3", "Aktualisierung Pflichtenheft auf Stand Gate-Beschluss", leiter, "+4 Wochen"],
              ["4", "Stakeholder-Update an OEM-Kontakt", leiter, "+1 Woche"],
              ["5", "Eintrag in Projekt-Tracker / IFS Project & Portfolio", "PMO", "+1 Woche"]]),
            ("8. Unterschriften",
             signatures(sponsor.split("(")[0].strip(), "Vorsitz Lenkungsausschuss", R["name"],
                        leiter, "Projektleitung", R["name"],
                        place="Stuttgart", date_str_=datum_str)),
        ])
    return path


# ── LESSONS LEARNED ────────────────────────────────────────────────────────
def lessons(prj_id, kurztitel, produkt, leiter, sponsor, budget, ende_jahr):
    matches = list(BASE.glob(f"{prj_id}_Lessons_Learned_*.docx"))
    if not matches:
        return None
    path = matches[0]
    write_doc(str(path), H,
        f"Lessons-Learned-Bericht {prj_id} – {kurztitel}",
        subtitle=f"Post-Mortem-Workshop, Stand {ende_jahr}",
        sections=[
            ("1. Projektzusammenfassung",
             [["Feld", "Inhalt"],
              ["Projekt-ID", prj_id],
              ["Projekt-Titel", kurztitel],
              ["Produktbezug", produkt],
              ["Projektleitung", leiter],
              ["Projekt-Sponsor", sponsor],
              ["Genehmigtes Budget", f"{budget:.1f} Mio. EUR"],
              ["Ist-Kosten zum Abschluss", f"{budget*1.04:.1f} Mio. EUR (+4 %)"],
              ["Projektabschluss", str(ende_jahr)]]),
            ("2. Zielereichung",
             f"Die im Charter definierten Projektziele wurden im Wesentlichen "
             f"erreicht. Der vereinbarte Funktionsumfang konnte mit kleinen "
             f"Abweichungen (Carry-Over-Items im Umfang von ca. 3 % der "
             f"User-Stories) ausgeliefert werden. Der Termin SOP wurde um 6 "
             f"Wochen ueberschritten, hauptsaechlich verursacht durch externe "
             f"Lieferengpaesse bei Halbleitern (Aurix-Allocation Q3/2022 bzw. "
             f"Qualcomm SA8295). Das Projekt wurde mit einer Budget-Ueberschreitung "
             f"von rund 4 % (kalkuliert auf Genehmigtes Budget) abgeschlossen, "
             f"was innerhalb der vom Vorstand definierten 5-%-Toleranz liegt."),
            ("3. Was hat gut funktioniert (Best Practices)",
             ("list", [
                "Klar definierter Charter zu Projektbeginn (Charter v1.0 freigegeben vor Kick-Off)",
                "Wochentliche Risiko-Reviews ab Projektphase G2",
                "Frueher Einbezug des Konzernbetriebsrates bei Personalplanung",
                "Stabile Personenausstattung im Kernteam (Fluktuation < 5 %)",
                "Aktive Lieferanten-Steuerung im Stoerungsfall (Eskalation auf C-Level)",
                "Tools-Konvergenz auf Vector, dSpace, JIRA, Confluence ohne Insellösungen",
                "Lessons-Learned-Workshops nach jedem Gate ab G3",
             ])),
            ("4. Was sollten wir besser machen (Verbesserungspotenzial)",
             ("list", [
                "Frueheres Eskalations-Protokoll bei Lieferanten-Risiken (Halbleiter-Allocation)",
                "Zentrale Engineering-Capacity-Planung (RSG-Engineers waren Bottleneck)",
                "Konsequentere Anwendung der ASPICE-Level-3-Templates (RSG)",
                "Kunden-spezifische OEM-Anforderungen frueher kanalisieren (Joint-Workshops Q1)",
                "Schaerfere Trennung Linien- vs. Projektaufgaben fuer Schluesselpersonen",
                "Standardisiertes EAC-/ETC-Reporting auf monatlicher Basis ab G2",
                "Vorab-Investition in Test-Automation (CI/CD) zahlt sich aus",
             ])),
            ("5. Konkrete Massnahmen fuer Folgeprojekte",
             [["Nr.", "Massnahme", "Verantwortlich (Linie)", "Umsetzungstermin"],
              ["1", "Konzern-PMO-Template Charter v2.0 einfuehren", "PMO", "Q2/Folgejahr"],
              ["2", "Halbleiter-Strategic-Sourcing-Programm aufsetzen", "Group Purchasing", "Q2/Folgejahr"],
              ["3", "Capacity-Planning-Tool Engineering RSG einfuehren", "RSG Werkleitung", "Q3/Folgejahr"],
              ["4", "ASPICE-Compliance-Audit als interner Quartals-Check", "Group Quality", "ab Q1/Folgejahr"],
              ["5", "Joint-OEM-Workshops nach Charter als Pflicht", "Vertrieb / PMO", "ab Q1/Folgejahr"]]),
            ("6. Risiko-Realisierungen",
             "Von den im Charter dokumentierten Top-Risiken haben sich zwei (Halbleiter-"
             "Liefersituation und OEM-Spec-Spaetaenderungen) materialisiert und "
             "wesentliche Auswirkungen auf den Termin und das Budget gehabt. Die "
             "uebrigen Risiken konnten durch fruehzeitige Massnahmen entweder vermieden "
             "(z. B. Personal-Bindungsprogramm) oder in der Auswirkung minimiert werden. "
             "Eine konsolidierte Risiko-Datenbank wird im PMO gepflegt und steht fuer "
             "Folgeprojekte als Erfahrungsbasis zur Verfuegung."),
            ("7. Empfehlungen an den Vorstand / Aufsichtsrat",
             "Der Lenkungsausschuss empfiehlt dem Vorstand, die im Punkt 5 genannten "
             "Massnahmen als verbindliche Konzernrichtlinien zu verankern. Insbesondere "
             "das Strategic-Sourcing-Programm fuer kritische Halbleiter ist als "
             "strategisch zwingend einzustufen. Eine Vorlage an den Pruefungsausschuss "
             "des Aufsichtsrats ist im Rahmen des naechsten Quartals-Reportings "
             "vorgesehen."),
            ("8. Workshop-Teilnehmer und Unterschriften",
             signatures(sponsor.split("(")[0].strip(), "Projekt-Sponsor", R["name"],
                        leiter, "Projektleitung", R["name"],
                        place="Stuttgart", date_str_=f"15. Dezember {ende_jahr}")),
        ])
    return path


# ── TESTBERICHTE ───────────────────────────────────────────────────────────
TEST_INFO = {
    "EMV_Test": ("EMV-Pruefbericht (Stoerfestigkeit und Stoeraussendung)",
                 "CISPR 25 Ed. 5, ISO 11452-2/-4, ISO 7637-2/-3",
                 "Pruefraum REA EMV-Labor Stuttgart, Kammer 3 (semi-anechoic 3 m)",
                 ["Stoeraussendung CISPR 25 Klasse 5 bestanden",
                  "BCI ISO 11452-4 (1–400 MHz, 100 mA) bestanden",
                  "ALSE 3 m gem. CISPR 25 (150 kHz–2,5 GHz) bestanden",
                  "Pulse 1/2a/2b/3a/3b ISO 7637-2 bestanden",
                  "Coupling Clamp ISO 7637-3 bestanden"]),
    "Funktionstest_EOL": ("EOL-Funktionstest (End of Line)",
                          "Werks-Spezifikation REG-EOL-V2.4, IATF 16949",
                          "EOL-Pruefstand Werk Heilbronn, Linie 4",
                          ["Power-Up / Boot < 800 ms bestanden",
                           "CAN/CAN-FD/Ethernet-Diagnose UDS bestanden",
                           "I/O-Loopback alle Pins bestanden",
                           "Programmierung Final-FW + Calibration-Dataset",
                           "Pruefprotokoll automatisiert in MES (Hydra) abgelegt"]),
    "Klimatest": ("Klimapruefung (Temperaturwechsel und Feuchte)",
                  "LV124, ISO 16750-4, IEC 60068-2-30 / -2-38",
                  "Pruefraum REA Klimalabor Stuttgart, Kammer K7 (Voetsch VC4060)",
                  ["Temperaturwechsel -40/+85 deg C, 1000 Zyklen bestanden",
                   "Damp Heat IEC 60068-2-30 (25/55 deg C, 95 % rH) bestanden",
                   "Composite Cycle IEC 60068-2-38 (10 Zyklen) bestanden",
                   "Funktionsfaehigkeit nach Pruefung verifiziert (Boot + UDS)"]),
    "Lebensdauertest": ("Beschleunigte Lebensdauer-Pruefung",
                        "ISO 16750-4 Abschnitt 5, HALT/HASS Werks-Spezifikation",
                        "Pruefraum Dekra Stuttgart und REA HALT-Kammer",
                        ["HALT-Profil 96 h kombiniert (Temperatur + Vibration) bestanden",
                         "Mission-Profile-Test 15-Jahre-Aequivalent abgebildet",
                         "Restwertanalyse Loetstellen: keine Auffaelligkeiten",
                         "Beanspruchung der HV-Isolation: > 1500 MOhm"]),
    "Vibration": ("Vibrations- und Schockpruefung",
                  "ISO 16750-3, LV124, MIL-STD-810G Method 514.6",
                  "Pruefraum REA Mechanik-Labor Stuttgart, Shaker Unholtz-Dickie",
                  ["Sinusvibration 10–2000 Hz, 5 g RMS bestanden",
                   "Rauschen (Random) 10–2000 Hz, 27,8 m/s2 RMS bestanden",
                   "Schock 50 g / 6 ms 3-axial bestanden",
                   "Visuelle und elektrische Inspektion nach Pruefung positiv"]),
}


def testbericht(prj_id, kurztitel, produkt, leiter, test_typ, datum_str):
    # find file
    pattern = f"{prj_id}_Testbericht_{test_typ}_*.docx"
    matches = list(BASE.glob(pattern))
    if not matches:
        return None
    path = matches[0]
    titel, norm, ort, ergebnisse = TEST_INFO[test_typ]
    write_doc(str(path), H,
        f"{titel} – {produkt}",
        subtitle=f"{prj_id} – {kurztitel} | Pruefbericht-Nr. {prj_id}-T-{test_typ[:3].upper()}-001",
        sections=[
            ("1. Pruefgegenstand",
             [["Feld", "Inhalt"],
              ["Projekt-ID", prj_id],
              ["Produktbezeichnung", produkt],
              ["Pruefmuster (Bezeichnung)", f"{produkt} – Sample-Nr. SN-2023-{prj_id[-3:]}"],
              ["Pruefmuster-Index / Stand", "B-Muster, Index B.04"],
              ["Pruef-Typ", titel],
              ["Pruefdatum", datum_str],
              ["Pruefer (Lab-Team)", "Dr. Karl-Heinz Wiegand (Lead), Sabine Brand (REG-Q)"],
              ["Projektleitung", leiter]]),
            ("2. Pruefnormen und Spezifikationen",
             f"Die Pruefung erfolgte nach den nachstehenden Normen und werksinternen "
             f"Spezifikationen: {norm}. Zusatzlich wurden die Kunden-spezifischen "
             f"Anforderungen aus dem Lastenheft (LV124-konforme Ergaenzungen) "
             f"beruecksichtigt. Die Pruefumgebung und die Messmittel sind nach ISO/IEC "
             f"17025 akkreditiert; Kalibrierscheine liegen vor und sind im "
             f"Pruefprotokoll referenziert."),
            ("3. Pruefaufbau",
             f"Ort: {ort}.\n\n"
             f"Pruefaufbau: Das Pruefmuster wurde im Betriebszustand 'normal operation' "
             f"in die Pruefkammer eingebaut und ueber den werksinternen Pruefadapter "
             f"versorgt (Bordnetz 12 V/14 V bzw. HV 800 V). Mess-Schnittstellen: "
             f"CAN, CAN-FD, Automotive Ethernet 100BASE-T1, Diagnose UDS via "
             f"Vector CANoe 18 SP3, Stromaufnahme via R&S NGM202 Power Supply.\n\n"
             f"Begleitende Mess-Werkzeuge: Tektronix MSO64 Oszilloskop, ETAS ES910 "
             f"Mess-Hardware, Vector CANape 23 fuer XCP-on-Ethernet. Alle Geraete "
             f"waren in der Kalibrierfrist."),
            ("4. Ergebnis-Zusammenfassung",
             ("list", [e + " – PASS" for e in ergebnisse])),
            ("5. Detail-Messwerte (Auszug)",
             [["Pruefpunkt", "Soll-Wert", "Ist-Wert", "Bewertung"],
              ["Stromaufnahme Ruhe (mA)", "< 1,5", "0,94", "PASS"],
              ["Stromaufnahme Last (A)", "< 4,2", "3,67", "PASS"],
              ["Boot-Time (ms)", "< 800", "612", "PASS"],
              ["CAN-Bus-Last (%)", "< 60", "37", "PASS"],
              ["Diagnose-Antwort UDS (ms)", "< 50", "21", "PASS"],
              ["Temperatur-Innenraum max. (deg C)", "< 95", "84", "PASS"]]),
            ("6. Abweichungen und Bemerkungen",
             "Waehrend der Pruefung sind keine sicherheitsrelevanten Abweichungen "
             "aufgetreten. Einzelne Messpunkte bewegten sich an der oberen Toleranz-"
             "Grenze, blieben jedoch klar innerhalb der Spezifikation. Beobachtete "
             "Auffaelligkeiten wurden im Pruef-Logbuch dokumentiert und an die "
             "Entwicklung zur Optimierung in der naechsten Muster-Stufe (C-Muster) "
             "weitergeleitet."),
            ("7. Gesamtbewertung",
             f"Das Pruefmuster {produkt} (B-Muster, Index B.04) hat die hier "
             f"dokumentierten Pruefungen bestanden. Die Anforderungen des Lastenhefts "
             f"sowie der referenzierten Normen werden erfuellt. Aus Sicht des Pruef-"
             f"Labors bestehen keine Einwaende gegen die Weitergabe an den Validierungs-"
             f"Schritt der naechsten Projektphase."),
            ("8. Unterschriften / Freigabe",
             signatures("Dr. Karl-Heinz Wiegand", "Pruefer / Lab-Lead", R["name"],
                        leiter, "Projektleitung", R["name"],
                        place="Stuttgart", date_str_=datum_str)),
        ])
    return path


# ── LASTENHEFT ────────────────────────────────────────────────────────────
def lastenheft(prj_id, kurztitel, produkt, oem, leiter, sponsor, ziel, scope):
    matches = list(BASE.glob(f"{prj_id}_Lastenheft_*.docx"))
    if not matches:
        return None
    path = matches[0]
    write_doc(str(path), H,
        f"Lastenheft {prj_id} – {kurztitel}",
        subtitle=f"Auftraggeber-Spezifikation, Version 1.0",
        sections=[
            ("1. Vorbemerkung",
             "Das vorliegende Lastenheft beschreibt aus Sicht des Auftraggebers "
             "(internes Produkt-Management bzw. OEM) die funktionalen und nicht-"
             "funktionalen Anforderungen an das im Projekt zu entwickelnde Produkt "
             "bzw. die zu erbringende Leistung. Das Lastenheft ist Grundlage fuer "
             "die Erstellung des Pflichtenhefts durch den Auftragnehmer (REA-"
             "Entwicklungsteam)."),
            ("2. Projekt-/Produkt-Bezug",
             [["Feld", "Inhalt"],
              ["Projekt-ID", prj_id],
              ["Produktbezeichnung", produkt],
              ["Hauptkunde / OEM", oem],
              ["Projektleitung (Auftragnehmer)", leiter],
              ["Auftraggeber (Sponsor)", sponsor]]),
            ("3. Zielsetzung",
             ziel),
            ("4. Anforderungen – Funktional",
             ("list", scope + [
                 "Diagnose ueber UDS (ISO 14229-1)",
                 "OTA-Updatefaehigkeit (sofern Anwendungsbereich)",
                 "Cybersecurity nach ISO/SAE 21434 und UN R155",
                 "Funktionssicherheit nach ISO 26262 (ASIL gemaess Konzept)"])),
            ("5. Anforderungen – Nicht-funktional",
             [["Kategorie", "Anforderung"],
              ["Temperaturbereich", "-40 ... +85 deg C (Betriebsbereich)"],
              ["Lagertemperatur", "-40 ... +105 deg C"],
              ["Schutzart", "IP6K7/IP6K9K (montagelagenabhaengig)"],
              ["EMV", "CISPR 25 Klasse 5, LV124, ISO 11452-2/-4"],
              ["Lebensdauer", "15 Jahre / 250.000 km / 8.000 h"],
              ["Verfuegbarkeit", "> 99 % (Funktion), > 99,9 % (Sicherheitsfunktionen)"],
              ["Cybersecurity", "ISO/SAE 21434 + UN R155/156-Konformitaet"]]),
            ("6. Schnittstellen",
             "Definiert werden alle elektrischen, kommunikativen und mechanischen "
             "Schnittstellen zum Fahrzeug-Bordnetz (12 V / 24 V / HV 400/800 V), "
             "zu Kommunikations-Bussen (CAN, CAN-FD, Automotive Ethernet 100/1000BASE-T1), "
             "zu Sensoren/Aktoren sowie zur OBD- und After-Sales-Diagnose. Die "
             "elektrischen Schnittstellen sind im separaten Pinning-Dokument "
             "(REA-Pin-LH-001 v1.0) detailliert beschrieben."),
            ("7. Liefer- und Akzeptanzkriterien",
             ("list", [
                "A-Muster (Konzept-Validierung) zum Gate G2",
                "B-Muster (Pre-Production) zum Gate G3 inkl. Test-Coverage > 80 %",
                "PPAP Level 3 zum Gate G4 (D/PFMEA, MSA, Cpk > 1,67)",
                "Vollstaendige Dokumentation gem. VDA 6.3 und IATF 16949",
                "Schulungsunterlagen fuer After-Sales und Linien-Mitarbeiter",
             ])),
            ("8. Termin- und Kostenrahmen",
             "Die im Projekt-Charter festgelegten Termine und Budgets gelten "
             "verbindlich. Aenderungen erfolgen ueber das im Charter beschriebene "
             "Change-Management (Change-Control-Board, Vorsitz Group-Controlling)."),
            ("9. Unterschriften (Freigabe Lastenheft)",
             signatures(sponsor.split("(")[0].strip(), "Auftraggeber / Sponsor", R["name"],
                        leiter, "Auftragnehmer / Projektleitung", R["name"],
                        place="Stuttgart", date_str_="—")),
        ])
    return path


# ── PFLICHTENHEFT ──────────────────────────────────────────────────────────
def pflichtenheft(prj_id, kurztitel, produkt, oem, leiter, sponsor, ziel, scope):
    matches = list(BASE.glob(f"{prj_id}_Pflichtenheft_*.docx"))
    if not matches:
        return None
    path = matches[0]
    write_doc(str(path), H,
        f"Pflichtenheft {prj_id} – {kurztitel}",
        subtitle=f"Auftragnehmer-Konkretisierung, Version 1.0",
        sections=[
            ("1. Bezug zum Lastenheft",
             f"Das vorliegende Pflichtenheft ist die Antwort des Auftragnehmers "
             f"(REA-Entwicklungsteam) auf das Lastenheft {prj_id}. Es konkretisiert "
             f"die Anforderungen, beschreibt die technische Umsetzung und enthaelt "
             f"die Verbindlichkeitserklaerung gegenueber dem Auftraggeber."),
            ("2. Identifikation",
             [["Feld", "Inhalt"],
              ["Projekt-ID", prj_id],
              ["Produkt", produkt],
              ["Kunde / OEM", oem],
              ["Projektleitung", leiter],
              ["Sponsor / Auftraggeber", sponsor]]),
            ("3. Loesungs-Architektur (Ueberblick)",
             f"Die Loesung baut auf der Plattform-Strategie der Brennhagen "
             f"Elektronik AG fuer {produkt} auf. Die Architektur besteht aus "
             f"einem Hauptsteuergeraet, mehreren Sub-Komponenten sowie der "
             f"Software-Komponente in den Schichten Hardware-Abstraktion, "
             f"Basis-Software (AUTOSAR Classic 4.3 / Adaptive 21-11), "
             f"Applikations-Software und Diagnose. Die elektrische Architektur "
             f"folgt der Plattform-Referenz von Brennhagen, ergaenzt um die "
             f"kundenspezifischen Schnittstellen aus dem Lastenheft."),
            ("4. Konkretisierung der Anforderungen",
             ("list", scope)),
            ("5. Verifikations-Strategie",
             "Die Verifikation der hier konkretisierten Anforderungen erfolgt "
             "auf vier Ebenen: 1) Unit-Test (Coverage > 90 % MC/DC), 2) "
             "Integrationstest (HiL bei RSG Muenchen), 3) System-Test "
             "(Komponenten-Pruefstand und Vehicle-in-the-Loop) und 4) "
             "Validierung im Zielfahrzeug. Ein vollstaendiges Requirements-"
             "Tracing wird in IBM DOORS Next gefuehrt und im RTM dokumentiert."),
            ("6. Annahmen, Voraussetzungen, Risiken",
             "Wesentliche Annahmen sind: 1) Verfuegbarkeit der angefragten "
             "Halbleiter-Bausteine (Infineon Aurix, NXP S32 etc.) gemaess "
             "Allocation-Bestaetigung; 2) Bereitstellung der OEM-spezifischen "
             "Testpattern und Fahrzeug-Schnittstellen; 3) Aktualitaet der OEM-"
             "Spezifikation (eingefrorener Stand zu definiertem Zeitpunkt). "
             "Aenderungen an diesen Annahmen werden als Change-Request behandelt."),
            ("7. Termine, Liefergegenstaende, Akzeptanztests",
             ziel),
            ("8. Verbindlichkeitserklaerung und Unterschriften",
             signatures(leiter, "Projektleitung / Auftragnehmer", R["name"],
                        sponsor.split("(")[0].strip(), "Sponsor / Auftraggeber", R["name"],
                        place="Stuttgart", date_str_="—")),
        ])
    return path


# ── MISPLACED DOCS (treated by filename type) ─────────────────────────────
def misplaced_files():
    # 1. REG_IC_Quartalsbericht_2019_Q4.docx — intercompany quarterly
    p = BASE / "REG_IC_Quartalsbericht_2019_Q4.docx"
    if p.exists():
        write_doc(str(p), H,
            "Intercompany-Quartalsbericht REG 2019 Q4",
            subtitle="Brennhagen Elektronik GmbH (REG) – Berichterstattung an Konzern-Controlling",
            sections=[
                ("1. Berichterstatter",
                 [["Feld", "Inhalt"],
                  ["Gesellschaft", "Brennhagen Elektronik GmbH (REG), Heilbronn"],
                  ["Berichtszeitraum", "01.10.2019 – 31.12.2019"],
                  ["Erstellt durch", "Sandra Wertheim (Werks-Controlling REG)"],
                  ["Empfaenger", "Konzern-Controlling, Florian Maier (Stuttgart)"],
                  ["Erstellungsdatum", "20. Januar 2020"]]),
                ("2. Umsatz und Profitabilitaet",
                 "Im vierten Quartal 2019 erzielte REG einen Umsatz von 142,3 Mio. EUR "
                 "(Vorjahr Q4/2018: 134,8 Mio. EUR; +5,6 %). Das EBIT betrug 11,7 Mio. EUR "
                 "(8,2 % EBIT-Marge), im Vorjahresquartal 10,9 Mio. EUR (8,1 %). Das "
                 "Jahresergebnis 2019 wird mit ca. 540 Mio. EUR Umsatz und 42 Mio. EUR EBIT "
                 "abschliessen, was im Rahmen des Budgets 2019 liegt."),
                ("3. Wesentliche Ereignisse Q4/2019",
                 ("list", [
                    "Anlauf der ECU-900-Gen2-Plattform fuer VW MEB (SOP 11/2019)",
                    "Erweiterung der BMS-Linie 2 abgeschlossen (CAPEX 4,1 Mio. EUR)",
                    "IATF 16949-Re-Zertifizierung erfolgreich (DEKRA, 17.10.2019)",
                    "Personalaufbau 32 FTE (Engineering 18, Produktion 14)",
                    "Lieferanten-Audit Continental als Tier-2 erfolgreich"])),
                ("4. Intercompany-Salden (Stichtag 31.12.2019)",
                 [["Konto / Partner", "Saldo (TEUR)", "Bemerkung"],
                  ["RHO – Management-Fee (Aufwand)", "1.840", "Quartal Q4"],
                  ["RSG – Lizenz-/Engineering (Aufwand)", "2.210", "Software-Bezug"],
                  ["RCZ – Steckverbinder (Aufwand)", "3.420", "Materialbezug"],
                  ["RPL – EMS-/SMD-Dienstleistung (Aufwand)", "8.940", "Materialbezug"],
                  ["RCN – Vertrieb (Erloes)", "1.180", "Provision China"]]),
                ("5. Forecast Q1/2020 und Risiken",
                 "Fuer Q1/2020 wird ein Umsatz von 138–142 Mio. EUR erwartet. Wesentliche "
                 "Risiken: Coronavirus-Lieferketten-Stoerung China (im Beobachtungs-Status), "
                 "Halbleiter-Liefersituation Aurix (Allocation), Currency-Effekte USD/CNY."),
                ("6. Unterschrift",
                 signatures("Sandra Wertheim", "Werks-Controlling REG", R["name"],
                            "Florian Maier", "Group Controller", R["name"],
                            place="Heilbronn", date_str_="20. Januar 2020")),
            ])

    # 2. REA_CON_ICP-3_QBR_2022_Q2.docx — Quarterly Business Review Continental ICP-3
    p = BASE / "REA_CON_ICP-3_QBR_2022_Q2.docx"
    if p.exists():
        write_doc(str(p), H,
            "Quarterly Business Review – Continental AG / ICP-3 (Q2 2022)",
            subtitle="Kundenmanagement-Bericht, Stand 31. Juni 2022",
            sections=[
                ("1. Kunde und Programm",
                 [["Feld", "Inhalt"],
                  ["Kunde", "Continental AG, Regensburg / Frankfurt"],
                  ["Produktbezug", "ICP-3 InfoConnect Pro (Infotainment-Modul)"],
                  ["Programm-Verantwortlich (Kunde)", "Dr. Martin Lauer (Continental)"],
                  ["Account Manager REA", "Stefan Richter (CMO/BD)"],
                  ["Berichtszeitraum", "01.04.2022 – 30.06.2022"]]),
                ("2. Volumen und Erloes",
                 "Im Berichtsquartal wurden 38.420 Einheiten ICP-3 an Continental fuer "
                 "die Endabnehmer BMW und Mercedes geliefert (Q1/2022: 36.110). Daraus "
                 "ergibt sich ein Quartals-Umsatz von 17,8 Mio. EUR (Q1: 16,7 Mio. EUR). "
                 "Die Year-to-Date-Erloese liegen 4,2 % ueber Plan."),
                ("3. Qualitaets-Performance",
                 [["KPI", "Q2/2022", "Ziel", "Bewertung"],
                  ["Reklamationsquote (ppm)", "32", "< 50", "GRUEN"],
                  ["8D-Reports offen", "3", "< 5", "GRUEN"],
                  ["Liefertreue On-Time", "97,8 %", "> 95 %", "GRUEN"],
                  ["Audit-Score VDA 6.3 (intern)", "92 / 100", "> 85", "GRUEN"]]),
                ("4. Top-Themen im Quartal",
                 ("list", [
                    "Software-Release ICP-3 v3.4 ausgerollt (OTA-Update fuer Bestand)",
                    "Joint Engineering 5G-Modemintegration (Qualcomm SA8295) gestartet",
                    "Lieferanten-Audit REG Heilbronn Q-Score 92/100 (Continental Quality)",
                    "Eskalation: Bauteilengpass Filter-IC behoben (Allocation +20 %)"])),
                ("5. Forecast H2/2022 und Vorausschau 2023",
                 "Continental plant die Verlaengerung des Rahmenliefervertrags bis Ende "
                 "2025 mit Anpassung der Volumina (Erwartung 320.000 Einheiten 2023). "
                 "Der naechste QBR ist fuer Mitte Oktober 2022 angesetzt."),
                ("6. Unterschriften",
                 signatures("Stefan Richter", "CMO/BD", R["name"],
                            "Dr. Martin Lauer", "Programm-Manager", "Continental AG",
                            place="Stuttgart", date_str_="15. Juli 2022")),
            ])

    # 3. REG_IC_Rechnung_2020_08.docx — IC-Rechnung
    p = BASE / "REG_IC_Rechnung_2020_08.docx"
    if p.exists():
        write_doc(str(p), H,
            "Intercompany-Rechnung REG → RHO August 2020",
            subtitle="Rechnungs-Nr. REG-IC-2020-008 | Leistungsperiode 08/2020",
            sections=[
                ("1. Rechnungs-Identifikation",
                 [["Feld", "Inhalt"],
                  ["Rechnungs-Nr.", "REG-IC-2020-008"],
                  ["Rechnungsdatum", "31. August 2020"],
                  ["Leistungszeitraum", "01.08.2020 – 31.08.2020"],
                  ["Leistungserbringer (RE-Steller)", "Brennhagen Elektronik GmbH (REG), Heilbronn"],
                  ["Rechnungs-Empfaenger", "Brennhagen Holding GmbH (RHO), Stuttgart"],
                  ["Faelligkeit (30 Tage netto)", "30. September 2020"]]),
                ("2. Leistungs-Positionen",
                 [["Position", "Beschreibung", "Menge", "EP (EUR)", "Summe (EUR)"],
                  ["1", "Auftragsfertigung BMS-12 Charge 2020-08-A", "12.420 St.", "84,50", "1.049.490,00"],
                  ["2", "Vorserien-Bemusterung ECU-900 Gen3 (B-Muster)", "120 St.", "320,00", "38.400,00"],
                  ["3", "EOL-Pruefung Linie 3 (Mehrarbeit)", "180 h", "85,00", "15.300,00"],
                  ["4", "Engineering-Support Customer-Audit BMW", "42 h", "120,00", "5.040,00"]]),
                ("3. Rechnungs-Summen",
                 [["Posten", "Betrag (EUR)"],
                  ["Netto-Rechnungssumme", "1.108.230,00"],
                  ["Umsatzsteuer 19 %", "210.563,70"],
                  ["Brutto-Rechnungssumme", "1.318.793,70"]]),
                ("4. Verrechnungspreis-Politik",
                 "Die Leistungserbringung erfolgt zu marktueblichen Verrechnungspreisen "
                 "(Cost-Plus 8 % auf direkte Engineering-Leistungen; Materialbezug "
                 "marktueblich, Aufschlag 5 % auf Vollkosten). Die Transferpreis-"
                 "Dokumentation ist im Local File RHO/REG 2020 (siehe TP_LocalFile_REG_2020) "
                 "abgelegt. Steuer-/Gesellschafts-Rechtliche Wirkung gemaess BMF-Schreiben "
                 "vom 14.07.2021."),
                ("5. Bankverbindung REG",
                 "Empfaengerbank: Commerzbank AG Heilbronn, IBAN DE12 6204 0000 0123 4567 89, "
                 "BIC COBADEFFXXX. Verwendungszweck bitte mit Rechnungs-Nr. angeben."),
                ("6. Unterschrift",
                 signatures("Andreas Maier", "Werkleiter REG", R["name"],
                            "Florian Maier", "Group Controller", R["name"],
                            place="Heilbronn", date_str_="31. August 2020")),
            ])

    # 4. REA_VW_ICP-3_ECR_2023_003.docx — Engineering Change Request
    p = BASE / "REA_VW_ICP-3_ECR_2023_003.docx"
    if p.exists():
        write_doc(str(p), H,
            "Engineering Change Request – ICP-3 / VW Programm (ECR 2023-003)",
            subtitle="Aenderungsantrag, Stand 14. Maerz 2023",
            sections=[
                ("1. ECR-Identifikation",
                 [["Feld", "Inhalt"],
                  ["ECR-Nr.", "VW-ICP-3-ECR-2023-003"],
                  ["Kunde", "Volkswagen AG, Wolfsburg"],
                  ["Produktbezug", "ICP-3 InfoConnect Pro (Infotainment-Modul)"],
                  ["Antragsteller (Kunde)", "Stefan Goeb (VW Konzern-Einkauf, K-GIT-E)"],
                  ["Bearbeiter REA", "Lars Wittmann (RSG)"],
                  ["Antragsdatum", "14.03.2023"]]),
                ("2. Beschreibung der Aenderung",
                 "Volkswagen beantragt die Integration einer zusaetzlichen "
                 "Sprach-Schnittstelle (China-Mandarin) in das ICP-3-Modul fuer "
                 "die Markt-Variante 'VW China JV'. Die Aenderung betrifft die "
                 "Sprach-Datenbank (TTS/STT-Engine), die UI-Layer (Right-to-Left "
                 "nicht erforderlich) sowie die kanonischen Sprach-Befehle des "
                 "Voice-Assistants."),
                ("3. Auswirkungen",
                 [["Dimension", "Auswirkung"],
                  ["Hardware", "Keine (gleiche Hardware-Bestueckung)"],
                  ["Software", "Erweiterung HMI-Layer, +1 Sprach-Pack (ca. 380 MB)"],
                  ["Speicher", "+420 MB Flash (innerhalb Reserve)"],
                  ["Test", "Re-Test HMI, Voice, Localization (geschaetzt 6 Wochen)"],
                  ["Termin", "Verzug +4 Wochen ab Vereinbarung"],
                  ["Kosten (einmalig)", "284.000 EUR (Engineering + Test)"],
                  ["Stueckkosten-Effekt", "Keine Aenderung"]]),
                ("4. Empfehlung",
                 "REA empfiehlt die Annahme des ECR unter Voraussetzung der schriftlichen "
                 "Bestellung der einmaligen Engineering-Kosten und einer entsprechenden "
                 "Anpassung des Liefertermins. Die Aenderung ist mit Group Quality "
                 "(Sabine Brand, REG) und Group Legal abgestimmt."),
                ("5. Freigaben",
                 signatures("Lars Wittmann", "Bearbeiter RSG", R["name"],
                            "Stefan Goeb", "Konzern-Einkauf K-GIT-E", "Volkswagen AG",
                            place="Stuttgart", date_str_="20. Maerz 2023")),
            ])

    # 5. RCZ_Prozessaudit_Beobachtung_2023_007_WIP.docx
    p = BASE / "RCZ_Prozessaudit_Beobachtung_2023_007_WIP.docx"
    if p.exists():
        write_doc(str(p), H,
            "Prozess-Audit-Beobachtung Nr. 2023-007 – RCZ Brno",
            subtitle="Auditprotokoll-Auszug (WORKING DRAFT), Stand 18.07.2023",
            draft=True,
            sections=[
                ("1. Audit-Identifikation",
                 [["Feld", "Inhalt"],
                  ["Audit-Nr.", "RCZ-PA-2023-007"],
                  ["Audit-Typ", "Internes Prozess-Audit nach VDA 6.3"],
                  ["Audit-Datum", "18. Juli 2023"],
                  ["Auditor (Lead)", "Eva Cerna (Q-Leitung RCZ)"],
                  ["Co-Auditor", "Andreas Buehler (CAE, Konzern Stuttgart)"],
                  ["Auditierter Bereich", "Stanzlinie 3 (Steckverbinder ECU-900)"]]),
                ("2. Beobachtung",
                 "Beim Audit wurde festgestellt, dass die Werkzeug-Wechsel-Dokumentation "
                 "an Stanzlinie 3 nicht in allen Faellen vollstaendig ausgefuellt war. "
                 "In 3 von 12 stichprobenartig geprueften Werkzeug-Wechsel-Protokollen "
                 "fehlten Eintragungen zu Mass-Kontrolle (CTQ-Mass C3, Spaltmass 0,12 mm) "
                 "vor Freigabe der Produktion. Die fehlenden Mass-Kontrollen wurden "
                 "nachtraeglich aus dem MES-System rekonstruiert; in keinem Fall war "
                 "die Spezifikation tatsaechlich verletzt."),
                ("3. Bewertung",
                 "Die Beobachtung wird als nicht-konformitaet (Minor) gemaess VDA 6.3 "
                 "P5.4 eingestuft. Korrekturmassnahme erforderlich, kein Audit-Stopp. "
                 "Die Sicherheit des Endprodukts ist nicht gefaehrdet, da die "
                 "geforderten Massnahmen (Mass-Kontrolle) zwar nicht im Original-"
                 "Protokoll, aber im MES-System nachvollziehbar dokumentiert sind. "
                 "Die Audit-Vorgehensweise entspricht der internen Audit-Richtlinie "
                 "RHO-Q-AUD-001 v3.2 vom 12.01.2023 sowie den Vorgaben des VDA 6.3 "
                 "Auditfragenkatalog 2023."),
                ("3a. Wirkungsanalyse",
                 "Eine Stichprobenpruefung der zwischen Mai und Juli 2023 aus der "
                 "Stanzlinie 3 ausgelieferten Charge-Nummern hat ergeben, dass keine "
                 "Spezifikations-Abweichungen am Endprodukt aufgetreten sind. Die "
                 "Reklamationsquote (ppm) lag im Berichtszeitraum stabil bei 28 ppm "
                 "(Ziel < 50 ppm). Der internen Risiko-Bewertung zufolge ist die "
                 "Wahrscheinlichkeit eines Auslieferungs-Risikos als gering, die "
                 "Wirkung als mittel und der Gesamt-Risiko-Score als niedrig "
                 "einzustufen."),
                ("4. Korrekturmassnahme (vereinbart)",
                 ("list", [
                    "Werkzeug-Wechsel-Protokoll als Pflicht-Schritt im MES (Hydra) verankern",
                    "Schichtleiter-Schulung (alle 14 Schichtleiter) bis 31.08.2023",
                    "Re-Audit der Stanzlinie 3 in 6 Monaten (Februar 2024)",
                    "Quartals-Stichprobenpruefung Q4/2023 durch RCZ-Q"])),
                ("5. Unterschriften (WIP – nicht final)",
                 signatures("Eva Cerna", "Q-Leitung RCZ / Lead-Auditor", R["name"],
                            "Petr Novak", "Werkleiter RCZ", R["name"],
                            place="Brno", date_str_="18.07.2023")),
            ])

    # 6. SLA_Managementdienstleistungen_RHO_RCN_2023.docx
    p = BASE / "SLA_Managementdienstleistungen_RHO_RCN_2023.docx"
    if p.exists():
        write_doc(str(p), H,
            "Service Level Agreement – Managementdienstleistungen RHO ↔ RCN",
            subtitle="Verrechnungspreis-Vertrag RHO / RCN Shanghai, Jahr 2023",
            sections=[
                ("1. Vertragsparteien",
                 [["Partei", "Sitz", "Rolle"],
                  ["Brennhagen Holding GmbH (RHO)", "Stuttgart, DE", "Leistungserbringer"],
                  ["Brennhagen (Shanghai) Co. Ltd. (RCN)", "Shanghai, CN", "Leistungsempfaenger"]]),
                ("2. Vertragsgegenstand",
                 "RHO erbringt fuer RCN folgende konzerninterne Managementdienstleistungen: "
                 "a) Strategische Steuerung und Reporting; b) Konzern-Treasury (Cash-Pooling, "
                 "FX-Hedging); c) Konzern-Controlling und Konsolidierung (IFRS); d) Konzern-"
                 "Compliance und Recht (LkSG, DSGVO/PIPL); e) IT-Infrastruktur (Konzernnetz, "
                 "SAP-Plattform); f) Konzern-Personalwesen (Talent-Management, Vergueltung "
                 "Expatriates); g) Konzern-Einkauf (strategische Lieferanten)."),
                ("3. Verguetungs-Modell",
                 "Die Verguetung erfolgt nach OECD-Verrechnungspreis-Richtlinien (Kapitel VII) "
                 "auf Basis Cost-Plus-Methode mit Aufschlag 5 % auf Vollkosten. Die jaehrliche "
                 "Schluessel-Aufteilung erfolgt nach 'Allocation Key' (50 % Umsatz / 30 % FTE / "
                 "20 % EBIT). Fuer 2023 betraegt das budgetierte Volumen 480 TEUR (Vorjahr "
                 "420 TEUR)."),
                ("4. Service Level (KPI)",
                 [["Service", "SLA", "Reporting"],
                  ["Monats-Reporting", "Versand bis Werktag 8 nach Monatsende", "monatlich"],
                  ["Quartals-Konsolidierung", "Versand bis Werktag 15 nach Q-Ende", "quartalsweise"],
                  ["IT-Helpdesk", "Reaktion < 4 h Bueroaktivitaet", "monatlich KPI"],
                  ["Treasury Cash-Forecast", "wochentlich Mittwoch 12:00 CET", "wochentlich"],
                  ["Compliance-Anfragen", "Beantwortung < 5 Werktage", "auf Anfrage"]]),
                ("5. Laufzeit",
                 "Der Vertrag laeuft vom 01.01.2023 bis 31.12.2023 und verlaengert sich "
                 "automatisch um jeweils ein Jahr, sofern nicht 3 Monate vor Ablauf "
                 "schriftlich gekuendigt. Aenderungen erfolgen ueber Vertragszusatz, "
                 "der von beiden Geschaeftsfuehrungen zu unterzeichnen ist."),
                ("6. TP-Dokumentation",
                 "Diese Vereinbarung ist Bestandteil des Transfer-Pricing-Local-Files RHO "
                 "Stuttgart und RCN Shanghai (Stand 2023). Die Cost-Allokation wird durch "
                 "die Group-Tax-Direktion (Dr. Heike Berger) jaehrlich gepruepft und durch "
                 "den Konzern-Abschlusspruefer (KPMG) im Rahmen der Jahresabschlusspruefung "
                 "validiert."),
                ("7. Unterschriften",
                 signatures("Anna Mueller", "Geschaeftsfuehrung RHO", "Brennhagen Holding GmbH",
                            "Zhang Hao", "Country Manager RCN", "Brennhagen (Shanghai) Co. Ltd.",
                            place="Stuttgart / Shanghai", date_str_="15. Januar 2023")),
            ])


# ── DRIVER ─────────────────────────────────────────────────────────────────
GATE_DATES = {
    "G1": "+3 Mon. nach Charter",
    "G2": "+9 Mon. nach Charter",
    "G3": "Mitte Laufzeit",
    "G4": "Ende - 3 Mon.",
}


def main():
    n_charter = n_gate = n_lessons = n_test = n_lh = n_ph = 0

    for prj in PROJEKTE:
        (pid, kt, prod, oem, leiter, sponsor, budget, start, ende, ziel, scope, risiken) = prj
        if charter(pid, kt, prod, oem, leiter, sponsor, budget, start, ende, ziel, scope, risiken):
            n_charter += 1
        for gid in ("G1", "G2", "G3", "G4"):
            # Compute synthetic date
            year = int(pid.split("-")[1])
            offset = {"G1": "15.04.", "G2": "15.10.", "G3": "15.05.", "G4": "15.11."}[gid]
            yroff = {"G1": 0, "G2": 0, "G3": 1, "G4": 1}[gid]
            datum = f"{offset}{year + yroff}"
            if gate(pid, kt, leiter, sponsor, gid, datum):
                n_gate += 1
        # Lessons
        end_y = int(pid.split("-")[1]) + 2
        if lessons(pid, kt, prod, leiter, sponsor, budget, end_y):
            n_lessons += 1
        # Testberichte
        for tt in ("EMV_Test", "Funktionstest_EOL", "Klimatest", "Lebensdauertest", "Vibration"):
            year = int(pid.split("-")[1]) + 1
            datum = {"EMV_Test": f"05.{year}",
                     "Funktionstest_EOL": f"08.{year}",
                     "Klimatest": f"06.{year}",
                     "Lebensdauertest": f"09.{year}",
                     "Vibration": f"07.{year}"}[tt]
            datum = f"15.{datum.replace(str(year)+'.', '').zfill(2)}.{year}" if False else f"15.{datum}"
            # simpler format:
            month = {"EMV_Test": "05", "Funktionstest_EOL": "08", "Klimatest": "06",
                     "Lebensdauertest": "09", "Vibration": "07"}[tt]
            datum = f"15.{month}.{year}"
            if testbericht(pid, kt, prod, leiter, tt, datum):
                n_test += 1
        # Lastenheft + Pflichtenheft
        ziel_text = f"{ziel} Ziel-Termin SOP: {ende}."
        if lastenheft(pid, kt, prod, oem, leiter, sponsor, ziel_text, scope):
            n_lh += 1
        if pflichtenheft(pid, kt, prod, oem, leiter, sponsor, ziel_text, scope):
            n_ph += 1

    misplaced_files()
    print(f"Charters: {n_charter}, Gates: {n_gate}, Lessons: {n_lessons}, "
          f"Tests: {n_test}, Lastenh: {n_lh}, Pflichtenh: {n_ph}")


if __name__ == "__main__":
    main()
