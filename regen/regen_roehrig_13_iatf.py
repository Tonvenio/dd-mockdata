"""
Re-generation script for roehrig_large/13_IATF_Qualitaet
Agent #11 — IATF 16949 / VDA 6.3 Qualitaetsmanagement.

Overwrites all thin .docx files in that folder with richer content
(>= 200 words each). Idempotent: rerunning yields identical output.
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
from __future__ import annotations

import re
import sys
import time
from pathlib import Path

sys.path.insert(0, f"{_ROOT}")
from enhance_lib import ROEHRIG_AG as R, write_doc, signatures

BASE = Path(f"{_ROOT}/roehrig_large/13_IATF_Qualitaet")
H = {"name": R["name"], "addr": R["addr"], "hrb": R["hrb"]}

# --------------------------------------------------------------------------
# Lookups
# --------------------------------------------------------------------------

OEM = {
    "BMW":  ("BMW Group",           "BMW AG, Petuelring 130, 80809 Muenchen",      "X5 G05, iX i20"),
    "VW":   ("Volkswagen AG",       "Volkswagen AG, Berliner Ring 2, 38440 Wolfsburg", "ID.7, ID.4, MEB+"),
    "MBZ":  ("Mercedes-Benz Group AG", "Mercedesstrasse 120, 70372 Stuttgart",      "EQS V297, S-Klasse W223"),
    "MB":   ("Mercedes-Benz Group AG", "Mercedesstrasse 120, 70372 Stuttgart",      "EQS V297, S-Klasse W223"),
    "STE":  ("Stellantis N.V.",     "Stellantis N.V., Singaporestraat 92-100, 1175 RA Lijnden", "Peugeot e-3008, DS9"),
    "CON":  ("Continental AG",      "Vahrenwalder Strasse 9, 30165 Hannover",      "Tier-1 Plattform CRX-2"),
    "FORD": ("Ford-Werke GmbH",     "Henry-Ford-Strasse 1, 50735 Koeln",           "Ford Explorer EV"),
    "ZF":   ("ZF Friedrichshafen AG", "Loewentaler Strasse 20, 88046 Friedrichshafen", "ProAI Domain Controller"),
    "BOSCH": ("Robert Bosch GmbH",  "Robert-Bosch-Platz 1, 70839 Gerlingen",       "Cross-Domain ECU"),
    "HYU":  ("Hyundai Motor Co.",   "12, Heolleung-ro, Seocho-gu, Seoul",          "Ioniq 5, Ioniq 6"),
    "CATL": ("CATL",                "No. 2 Xingang Road, Ningde, Fujian",          "Kirin Battery Pack"),
}

PROD = {
    "ICP-3":    ("InfoConnect Pro 3", "Infotainment-Headunit", "16 GB LPDDR5, NXP i.MX8QM, 12.3'' Display"),
    "BMS-12":   ("BatteryMS-12",      "Batteriemanagementsystem 800 V EV", "12-Kanal Cell-Monitoring, ASIL D, ISO 26262"),
    "ADAS-V4D": ("Radar Fusion ECU V4D", "Level-2/3 ADAS Steuergeraet", "TI TDA4VM SoC, 4 Radar-Eingaenge, FuSi ASIL B"),
    "ECU-900":  ("Powertrain-ECU Gen3",  "Antriebsstrang-Steuergeraet",  "Infineon AURIX TC399, ASIL D, 4 MB Flash"),
    "LightCtrl-7": ("Matrix-LED Steuermodul", "adaptive Matrix-LED-Ansteuerung", "84 Pixel, CAN-FD, ASIL B"),
}

SITE = {
    "REG": ("Brennhagen Elektronik GmbH",  "Heilbronn (DE)", "Andreas Maier",       "Sabine Brand"),
    "RSG": ("Brennhagen Software GmbH",    "Muenchen (DE)",  "Dr. Klaus Kessler",   "Lars Wittmann"),
    "RPL": ("Brennhagen Polska Sp. z o.o.", "Katowice (PL)",  "Marek Wojciechowski", "Anna Kowalska"),
    "RCZ": ("Brennhagen CZ s.r.o.",        "Brno (CZ)",      "Petr Novak",          "Eva Cerna"),
    "RHU": ("Brennhagen Hungary Kft.",     "Gyoer (HU)",     "Laszlo Kovacs",       "Andrea Szabo"),
    "RCN": ("Brennhagen (Shanghai) Co. Ltd.", "Shanghai (CN)", "Zhang Hao",         "Liang Wei"),
}

QHEAD = "Sabine Brand, Leiterin Qualitaetsmanagement Konzern (REA)"
QHEAD_LOCAL = {
    "REG": "Sabine Brand (Q-Leitung Werk Heilbronn)",
    "RSG": "Dr. Markus Hauser (Q-Leitung RSG Muenchen)",
    "RPL": "Tomasz Lewandowski (Q-Leitung RPL Katowice)",
    "RCZ": "Eva Cerna (Q-Leitung RCZ Brno)",
    "RHU": "Zsofia Nemeth (Q-Leitung RHU Gyoer)",
}

# --------------------------------------------------------------------------
# Helpers for body blocks
# --------------------------------------------------------------------------

def _oem(code: str):
    return OEM.get(code, OEM.get(code.upper(), ("Unbekannter OEM", "—", "—")))

def _prod(code: str):
    return PROD.get(code, ("Produkt " + code, "Steuergeraet", "—"))


def eightd(case: str, oem: str, prod: str) -> dict:
    """Return the full sections list for an 8D-Report."""
    oem_name, oem_addr, oem_modell = _oem(oem)
    prod_name, prod_desc, prod_spec = _prod(prod)
    return [
        ("1. Dokumentenkopf / Stammdaten",
         [["Feld", "Wert"],
          ["8D-Nummer (intern)", f"8D-2023-{case}"],
          ["OEM-Kundenreferenz", f"Q-Cl/{oem}/2023/{case}"],
          ["Kunde", oem_name],
          ["Kundenwerk / Modell", oem_modell],
          ["Lieferantennummer (REA)", "DE-126451-RHO"],
          ["Betroffenes Produkt", f"{prod_name} ({prod})"],
          ["Sachnummer (RAE)", f"RAE-{prod}-A02"],
          ["Reklamierte Charge / Los", f"L{case}-W34-2023, 1.250 Stueck"],
          ["Beanstandungsdatum", "2023-09-18"],
          ["Containment-Start", "2023-09-19 00:30 MESZ"],
          ["Team-Leiter (Champion)", "Sabine Brand, Q-Konzern"],
          ["Reklamierte Menge / Ist-ppm", "8 Stueck / 6,4 ppm (Ziel < 25 ppm)"]]),
        ("D1 — Team",
         "Interdisziplinaeres 8D-Team wurde am 2023-09-19 etabliert. Mitglieder: Sabine Brand (Champion, "
         "Q-Konzern); Dr. Thomas Weber (Sponsor, COO); Andreas Maier (Werkleiter REG Heilbronn); Sandra "
         "Heinz (Prozessingenieurin SMT); Dr. Klaus Kessler (RSG, Software-Lead falls relevant); Holger "
         "Reinmann (Lieferantenqualitaet); Carolin Voss (Reliability Engineering). Stellvertretende "
         "Ansprechpartner sind benannt. OEM-Eskalationsstufe gemaess CSL-Matrix: CSL-1 (Stand 19.09.2023). "
         "Eskalation an Vorstand erfolgt bei Ueberschreitung der 10-Tage-Frist gem. Konzern-QM-Handbuch "
         "Abschnitt 8.3.4."),
        ("D2 — Problembeschreibung",
         f"Der Kunde {oem_name} meldet aus der laufenden Produktion (Werk {oem_modell.split(',')[0].strip()}) "
         f"Funktionsausfaelle am Modul {prod_name}. Symptom: spontaner Reset des Steuergeraetes nach 8-12 "
         "Minuten Betrieb bei Umgebungstemperaturen > 65 °C, reproduzierbar im Klimaschrank. Es wurde "
         "ein Pareto-Muster festgestellt: 7 von 8 Faellen betreffen Geraete aus Charge L-W34-2023, "
         "gefertigt zwischen 23.08. und 25.08.2023 auf SMT-Linie 4 (Heilbronn). Kundeneinfluss: Stopp "
         "der Auslieferung an OEM-Endmontage, geschaetzter Schaden 280 kEUR. 5W2H-Analyse beigefuegt "
         "als Anhang A. Keine sicherheitsrelevanten Auswirkungen (kein Eingriff in Fahrfunktionen, "
         "Modul ist nicht sicherheitsbezogen / QM-Level)."),
        ("D3 — Sofortmassnahmen (Containment)",
         ("clauses", [
             ("D3.1 — Sperrung Lagerbestand",
              ["Sperrung Lagerbestand REG Heilbronn (412 Stueck), CZ-Hub Brno (180 Stueck), Kundenwerk "
               "(86 Stueck Walk-the-line am 19.09.2023, 14:00 MESZ).",
               "100% Visual + Roentgen-Inspektion aller verdaechtigen Module der Charge."]),
             ("D3.2 — Ersatzlieferung",
              ["Express-Sonderfertigung 600 Stueck aus Reserve-Bauteilen (Linie 2), Auslieferung per "
               "Direkt-LKW am 21.09.2023 06:00, Tracking-Nr. DHL-EXPR-29871."]),
             ("D3.3 — CSL-1-Anmeldung",
              ["Anmeldung zu Controlled Shipping Level 1 ueber separates Q-Gate (Cage 4, Halle B) "
               "wirksam ab 20.09.2023 06:00. Pruefer: Q-Gate-Team REG (5 FTE, 3-Schicht)."])
         ])),
        ("D4 — Ursachenanalyse (Root Cause)",
         "Die Ursachenanalyse erfolgte mit Ishikawa-Diagramm (Mensch/Maschine/Material/Methode/Mitwelt/Messung). "
         "Per 5-Why-Analyse wurde als technische Wurzelursache identifiziert: kalte Loetstelle am Spannungsregler "
         "U7 (TI TPS65919), verursacht durch zu niedriges Reflow-Peak-Temperatur-Profil auf SMT-Linie 4 "
         "(gemessen 232 °C statt 245 °C ±5 °C) zwischen 23.08. und 25.08.2023. Ursache der Profilabweichung: "
         "Verschmutzung des PT100-Sensors in Zone 7 fuehrte zu falscher Ist-Temperatur-Meldung. Systemische "
         "Wurzelursache: vorgesehene woechentliche Sensorkalibrierung war im Sommerurlaub (KW33-34) entfallen, "
         "kein Backup-Wartungsplan im Schichtkalender hinterlegt. Eine 2nd-Why-Loop zur QM-Methode ergab, "
         "dass die TPM-Checkliste keine harte Verriegelung der Linie bei ueberfaelliger Sensorkalibrierung "
         "vorsieht."),
        ("D5 — Geplante Abstellmassnahmen",
         [["Nr.", "Massnahme", "Verantw.", "Frist", "Wirksamkeit"],
          ["A1", "Reinigung und Neukalibrierung PT100 Zone 7 Linie 4", "Sandra Heinz", "2023-09-20", "Sofort"],
          ["A2", "Re-Profilierung Reflow Linie 4, KIC-Profil + Pruefkoerper-Aufzeichnung", "Holger Mertens", "2023-09-22", "Validiert"],
          ["A3", "Roll-out PT100-Kalibrierungsintervall 5 Werktage statt 7", "Werksleitung REG", "2023-09-30", "Wirksam"],
          ["A4", "Hardware-Verriegelung: Linie stoppt bei Sensor-Drift > 3 °C ueber 30 min", "Engineering", "2023-10-31", "Wirksam"],
          ["A5", "Aenderung Schichtkalender: TPM-Backup-Plan fuer Ferien/Krankheit", "Andreas Maier", "2023-10-15", "Eingefuehrt"]]),
        ("D6 — Eingefuehrte Abstellmassnahmen / Wirksamkeitspruefung",
         "Massnahmen A1 und A2 wurden am 2023-09-22 (06:00 MESZ) live geschaltet. Wirksamkeitspruefung "
         "ueber 30-Tage-Beobachtungsfenster: 0 weitere Beanstandungen aus Folgechargen (Stand 20.10.2023, "
         "5.880 Module gefertigt, 0 ppm Beanstandung). Cpk Loetstellenpruefung U7 hat sich von 1,12 (vorher) "
         "auf 1,67 (nachher) verbessert. AOI-False-Call-Rate stabil bei 0,4 %. Massnahmen A3-A5 wurden "
         "fristgerecht abgeschlossen und im OneQMS dokumentiert (Workflow-ID WI-23-1187). Pruefung der "
         "Wirksamkeit erfolgte gemeinsam mit OEM-SQE am 28.09.2023 vor Ort, Protokoll Anhang B."),
        ("D7 — Massnahmen zur Vermeidung der Wiederholung",
         "Lessons Learned wurden in die Konzern-Wissensdatenbank uebernommen (Eintrag LL-2023-077). "
         "PFMEA Sachnummer-Familie wurde aktualisiert (RPN 240 -> 80). Eintrag in Concern-Database des "
         "OEM (Q-Track ID 8821). Erweiterung der TPM-Checkliste um den Punkt Sensor-Kalibrierung als "
         "Pflichtfeld mit elektronischer Quittierung in MES (Hydra). Erweiterung Auditcheckliste interner "
         "Q-Audits Punkt 7.3 (TPM-Wirksamkeit). Schulung aller 4 Schichten Linie 4 am 02.10.2023 "
         "durchgefuehrt (Schulungsnachweis LL-2023-077-TRN). CSL-1 wurde am 25.10.2023 nach 6 Wochen "
         "stoerungsfreier Lieferung mit Zustimmung des OEM aufgehoben."),
        ("D8 — Anerkennung des Teams / Abschluss",
         "Das 8D-Team wurde am 30.10.2023 durch den COO Dr. Thomas Weber im Rahmen einer Werksbegehung "
         "REG Heilbronn fuer den schnellen und faktenbasierten Loesungsprozess gewuerdigt. Abschluss-Review "
         "mit OEM-SQE erfolgte am 02.11.2023, OEM-Approval fuer Closure am 06.11.2023 erhalten "
         f"(Referenz Q-Cl/{oem}/2023/{case}-CLOSED). Reklamation in SAP als geschlossen gebucht. "
         "Lessons Learned veroeffentlicht im internen Q-Bulletin 11/2023."),
        ("Unterschriften",
         signatures("Sabine Brand", "Leiterin QM Konzern (Champion)", "Brennhagen Elektronik AG",
                    "Dr. Thomas Weber", "COO (Sponsor)", "Brennhagen Elektronik AG",
                    place="Heilbronn", date_str_="6. November 2023")),
    ]


def ppap(oem: str, prod: str, year: str, level: str = "Level 3") -> list:
    oem_name, oem_addr, oem_modell = _oem(oem)
    prod_name, prod_desc, prod_spec = _prod(prod)
    return [
        ("1. Deckblatt PPAP",
         [["Feld", "Wert"],
          ["Lieferant", "Brennhagen Elektronik AG / Werk REG Heilbronn"],
          ["Lieferantennummer", "DE-126451-RHO"],
          ["Kunde", oem_name],
          ["Kundennummer / Programm", oem_modell],
          ["Sachnummer Kunde", f"{oem}-9214-{prod}-A"],
          ["Sachnummer REA", f"RAE-{prod}-A02"],
          ["Aenderungsstand", "A02"],
          ["PPAP-Level", level],
          ["Vorlagegrund", "Erstmuster Serienproduktion"],
          ["Erstmusterdatum", f"{year}-09-15"],
          ["Genehmigungsanforderung bis", f"{year}-10-31"]]),
        ("2. PPAP-Dokumentenstatus (gemaess AIAG PPAP 4th Ed.)",
         [["#", "Element", "Status"],
          ["1", "Design Records (Zeichnung A02, 3D-CAD STEP)", "vorhanden"],
          ["2", "Engineering Change Documents", "ECN-2023-019 freigegeben"],
          ["3", "Customer Engineering Approval", "ausstehend (Genehmigung mit PPAP)"],
          ["4", "DFMEA", "Rev 04, freigegeben 12.09.2023"],
          ["5", "Process Flow Diagram", "PFD-{prod}-Rev03"],
          ["6", "PFMEA", f"Rev 06 vom 18.09.{year}, RPN max 105"],
          ["7", "Control Plan", f"CP-{prod}-Rev05"],
          ["8", "MSA / Gage R&R", "GRR < 10 %, akzeptiert"],
          ["9", "Dimensionsmessungen", "30 Teile, alle innerhalb Toleranz"],
          ["10", "Material- / Performance Tests", "PV-Bericht TR-23-114, alle bestanden"],
          ["11", "Initial Process Studies (Cpk)", "Cpk min 1,67"],
          ["12", "Qualified Laboratory Doc", "ISO 17025 KBA-P-19-001"],
          ["13", "AAR (Appearance Approval)", "n. a. (kein Sichtteil)"],
          ["14", "Sample Production Parts", "5 Stueck inkl. Pruefzeugnis"],
          ["15", "Master Sample", "im Mastermusterschrank Heilbronn"],
          ["16", "Checking Aids", "Pruefadapter PAd-{prod}-001"],
          ["17", "Customer-Specific Requirements", f"erfuellt gem. {oem}-CSR Rev 2023"],
          ["18", "Part Submission Warrant (PSW)", "siehe Abschnitt 3"]]),
        ("3. Part Submission Warrant (PSW)",
         f"Hiermit bestaetigt die Brennhagen Elektronik AG, dass die Erstmuster der Sachnummer "
         f"RAE-{prod}-A02 ({prod_name}, {prod_desc}) vollumfaenglich den vereinbarten "
         f"Kundenanforderungen der {oem_name} entsprechen. Die Erstmuster wurden unter "
         f"Serienbedingungen im Werk REG Heilbronn am {year}-09-15 in einer "
         "Stichprobengroesse von 300 Stueck (Achtstundenproduktion auf Serienanlagen) "
         "gefertigt. Es wurden 30 Teile vermessen, 5 Teile als physische Muster "
         "beigelegt. Spezifikation: " + prod_spec + ". Die Genehmigung zur Serienlieferung wird hiermit beantragt."),
        ("4. Massergebnisse (Auszug)",
         [["Merkmal", "Sollwert", "Toleranz", "Istwert", "Cpk", "Status"],
          ["Gewicht Modul", "412 g", "± 8 g", "411,3 g", "1,87", "io"],
          ["Stromaufnahme Idle", "120 mA", "± 15 mA", "118 mA", "1,72", "io"],
          ["BCI-Festigkeit nach ISO 11452-4", ">= 100 V/m", "—", "120 V/m", "—", "io"],
          ["ESD-Air Discharge", ">= 15 kV", "—", "+/- 25 kV", "—", "io"],
          ["Temperaturbereich Betrieb", "-40 .. +85 °C", "—", "-40 .. +95 °C", "—", "io"],
          ["EOL-Funktionspruefung", "100 %", "—", "100 %", "—", "io"]]),
        ("5. Freigaben und Verteiler",
         "Vorlage des kompletten PPAP-Pakets erfolgt via Kunden-Supplier-Portal (z. B. SupplyOn fuer "
         "VW, Continental Supplier Web, BMW Group Partner Portal). Interne Freigaben: Sabine Brand "
         "(Q-Leitung Konzern), Dr. Heike Renz (Entwicklungsleitung), Andreas Maier (Werkleitung "
         "REG). Bei Genehmigung erfolgt Hochsetzung der Sachnummer in SAP-MM auf Serienstatus, "
         "Freigabe der EDI-Liefermenge gemaess Lieferabruf des OEM."),
        ("6. Unterschriften",
         signatures("Sabine Brand", "Leiterin QM Konzern", "Brennhagen Elektronik AG",
                    "Andreas Maier", "Werkleiter REG Heilbronn", "Brennhagen Elektronik GmbH",
                    place="Heilbronn", date_str_=f"15. September {year}")),
    ]


def msa(nr: str) -> list:
    return [
        ("1. Studienkopf",
         [["Feld", "Wert"],
          ["Studien-Nr.", f"MSA-2023-{nr}"],
          ["Pruefmittel", "Koordinatenmessmaschine Zeiss CONTURA G2 (Inv. KMG-014)"],
          ["Messmerkmal", "Bohrungs-Durchmesser Steckergehaeuse"],
          ["Sollwert / Toleranz", "8,000 mm +/- 0,050 mm"],
          ["Pruefverfahren", "Type-1 Studie (Cg/Cgk) + Gage R&R nach AIAG MSA 4th Ed."],
          ["Anzahl Teile", "10"],
          ["Anzahl Bediener", "3 (Schicht A/B/C)"],
          ["Anzahl Wiederholungen", "3"],
          ["Datum Durchfuehrung", "2023-09-14"],
          ["Verantwortlich", "Carolin Voss, Reliability Engineering REG"]]),
        ("2. Type-1 Studie (Cg / Cgk)",
         [["Kennzahl", "Wert", "Ziel", "Status"],
          ["Mittelwert Normal", "8,002 mm", "8,000 mm", "io"],
          ["Standardabweichung sg", "0,0021 mm", "—", "—"],
          ["Cg (= 0,2 x T / 6 sg)", "1,59", ">= 1,33", "io"],
          ["Cgk", "1,42", ">= 1,33", "io"],
          ["Bias", "+0,002 mm", "|Bias| < 0,1 x T", "io"]]),
        ("3. Gage R&R (ANOVA-Methode)",
         [["Komponente", "Standardabweichung", "% Contribution", "% Study Variation"],
          ["Wiederholpraezision (EV)", "0,0024 mm", "4,8 %", "21,9 %"],
          ["Vergleichspraezision (AV)", "0,0011 mm", "1,1 %", "10,3 %"],
          ["Gage R&R total", "0,0026 mm", "5,9 %", "24,3 %"],
          ["Teil-zu-Teil (PV)", "0,0102 mm", "94,1 %", "97,0 %"],
          ["Total Variation TV", "0,0105 mm", "100 %", "100 %"]]),
        ("4. Bewertung und Freigabe",
         "Das Pruefmittel ist gemaess AIAG-MSA-Richtlinie freigegeben (% Gage R&R 5,9 %, < 10 % "
         "akzeptiert ohne Auflagen). Die Anzahl unterscheidbarer Klassen (ndc) betraegt 7, "
         "geforderter Mindestwert ndc >= 5 ist erfuellt. Die Wiederholbarkeit dominiert ueber die "
         "Vergleichbarkeit, was auf eine geringe Bediener-Streuung hinweist (Plausibilitaet "
         "gegeben, da KMG vollautomatisches Messprogramm CMM-PRG-008 ausfuehrt). Pruefmittel wird "
         "in Q-DAS qs-STAT mit dem Status 'freigegeben' versehen. Naechste Wiederholungsstudie "
         "in 12 Monaten oder bei Werkzeug-/Programmaenderung."),
        ("5. Verteiler / Unterschriften",
         signatures("Carolin Voss", "Reliability Engineering", "Brennhagen Elektronik GmbH",
                    "Sabine Brand", "Leitung QM Konzern", "Brennhagen Elektronik AG",
                    place="Heilbronn", date_str_="14. September 2023")),
    ]


def capa(nr: str) -> list:
    return [
        ("1. Kopfdaten CAPA",
         [["Feld", "Wert"],
          ["CAPA-Nummer", f"CAPA-2023-{nr}"],
          ["Quelle (Auslöser)", "Internes Audit IATF 16949 / Findings KW36"],
          ["Eroeffnet am", "2023-09-12"],
          ["Eroeffnet durch", "Andreas Buehler (Chief Audit Executive)"],
          ["Verantwortlich (Owner)", "Sabine Brand, Q-Konzern"],
          ["Betroffener Prozess", "Lieferantenbewertung / Wareneingang"],
          ["Kategorie", "Corrective Action (CA) + Preventive Action (PA)"],
          ["Faelligkeit", "2023-12-15"],
          ["Status", "in Bearbeitung (Fortschritt 60 %)"]]),
        ("2. Beschreibung der Abweichung",
         "Im Rahmen des internen IATF-16949-Audits 2023 wurde eine Major Non-Conformity zu "
         "Klausel 8.4.2.4 festgestellt: die Lieferanten-Re-Bewertung (annual re-evaluation) wurde "
         "fuer 14 von 47 produktiven Lieferanten nicht innerhalb der vorgegebenen 12-Monats-Frist "
         "durchgefuehrt. Auditor: Dr. Christian Welt, DEKRA. Frist zur Schliessung 90 Tage."),
        ("3. Sofort- und Korrekturmassnahmen",
         [["Nr.", "Massnahme", "Verantwortlich", "Frist", "Status"],
          ["C1", "Nachholung aller offenen Re-Bewertungen (14 Stueck)", "Holger Reinmann", "2023-10-31", "abgeschlossen"],
          ["C2", "Eskalations-Workflow im SRM-Tool (SAP Ariba) aktivieren", "IT-Q (Florian Maier)", "2023-11-15", "in Test"],
          ["C3", "Pflichtfeld 'Naechste Re-Bewertung' im SRM", "IT-Q", "2023-11-30", "in Umsetzung"],
          ["P1", "Quartalsweiser Bestand-Soll-Abgleich im Q-Cockpit Tableau", "Sabine Brand", "2024-01-31", "geplant"],
          ["P2", "Anpassung Verfahrensanweisung QV-08.4-04", "Sandra Weber", "2023-12-15", "in Pruefung"]]),
        ("4. Wirksamkeitspruefung",
         "Die Wirksamkeitspruefung erfolgt im 1. Quartal 2024 durch erneute Stichprobenpruefung "
         "(10 zufaellig gezogene Lieferanten) sowie ueber das Quartals-KPI 'Anteil ueberfaellige "
         "Re-Bewertungen' (Zielwert 0 %). CAPA-Closure erfolgt nach positiver Wirksamkeitspruefung "
         "und Freigabe durch CAE."),
        ("5. Unterschriften",
         signatures("Sabine Brand", "Leiterin QM Konzern (Owner)", "Brennhagen Elektronik AG",
                    "Andreas Buehler", "Chief Audit Executive", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_="12. September 2023")),
    ]


def aa(site: str, kind: str) -> list:
    """Arbeitsanweisung (AA)."""
    site_name, site_loc, wl, q_loc = SITE[site]
    titles = {
        "Eingangswarenprufung": "Wareneingangspruefung (AA-WE-01)",
        "Endpruefung_EOL":      "Endpruefung End-of-Line (AA-EOL-01)",
        "Fehlerbehandlung_Ausschuss": "Fehlerbehandlung und Ausschussabwicklung (AA-AUS-01)",
        "Funktionstest":        "Funktionstest Steuergeraete (AA-FCT-01)",
        "ICT_Test":             "In-Circuit-Test (AA-ICT-01)",
        "Loetprozess_Reflow":   "Reflow-Loetprozess SMT (AA-RFL-01)",
        "Rueckverfolgbarkeit":  "Rueckverfolgbarkeit und Chargenmarkierung (AA-RV-01)",
        "SMT_Bestueckung":      "SMT-Bestueckung (AA-SMT-01)",
        "Verpackung_Versand":   "Verpackung und Versand (AA-VP-01)",
        "Wartung_Anlagen":      "Wartung und TPM Produktionsanlagen (AA-TPM-01)",
    }
    title = titles.get(kind, f"Arbeitsanweisung {kind}")
    return [
        ("1. Geltungsbereich / Zweck",
         f"Diese Arbeitsanweisung regelt den Prozess »{title}« fuer das Werk {site_name} "
         f"({site_loc}). Sie ist verbindlich fuer alle Mitarbeitenden in den betroffenen "
         "Schichten (3-Schicht-Betrieb) sowie fuer Praktikanten, Leiharbeitnehmer und "
         "Mitarbeitende externer Dienstleister, die in diesem Prozessbereich taetig sind. "
         "Die AA ergaenzt das uebergeordnete Konzern-QM-Handbuch nach IATF 16949 (REA-QMH-IATF, "
         "Rev. 2023) sowie die OEM-spezifischen CSR (Customer Specific Requirements) von BMW, "
         "VW, Mercedes-Benz und Stellantis."),
        ("2. Verantwortlichkeiten",
         [["Rolle", "Verantwortlich fuer"],
          ["Werkleitung " + site, wl + ", Gesamtverantwortung Prozess"],
          ["Schichtleitung", "Operative Durchfuehrung, Schichtuebergabe-Protokoll"],
          ["Q-Beauftragter Linie", q_loc + " bzw. Stellvertretung"],
          ["Prozessingenieur SMT/EOL", "Aenderungsmanagement, Cpk/Cmk-Monitoring"],
          ["Instandhaltung", "Wartungsfenster, TPM-Checkliste, Werkzeugfreigabe"],
          ["Sicherheitsbeauftragter", "Arbeitsschutz, ESD, PSA"],
          ["Auditor (intern/extern)", "Stichprobenpruefung im Rahmen interner / OEM-Audits"]]),
        ("3. Prozessablauf",
         ("clauses", [
             ("3.1 — Vorbereitung",
              ["Werkzeug- und Geraetepruefung gemaess Pruefmittelueberwachung (Kalibrieretikett "
               "gueltig, Sichtpruefung).",
               "Pruefmittel-Status in MES (Hydra) durch Login mit personifizierter ID quittieren.",
               "Bereitstellung Setup-Materialien, Material-Chargennummern erfassen."]),
             ("3.2 — Durchfuehrung",
              ["Ausfuehrung gemaess Pruefplan / Pruefspezifikation (PS-" + kind[:3].upper() + "-01).",
               "Live-Datenerfassung in MES; SPC-Karten (X-quer/R) bei kontinuierlichen Merkmalen.",
               "Bei Out-of-Control-Signal: Reaktionsplan gemaess Control Plan abarbeiten und "
               "Sperrung der Charge bis zur Freigabe durch Q."]),
             ("3.3 — Nachbereitung",
              ["Dokumentation aller Pruefergebnisse mit Pruefer-ID, Charge, Pruefmittel.",
               "Schichtuebergabeprotokoll (HÜP) Vollstaendigkeit pruefen; Abweichungen "
               "an Schichtfolgenden eskalieren.",
               "Wartungsmeldungen via TPM-App (Tag-out, Lock-out beachten)."])
         ])),
        ("4. Qualitaetsmerkmale und Reaktionsplan",
         [["Merkmal", "Pruefmittel", "Toleranz", "Cpk-Ziel", "Reaktionsplan"],
          ["Loetstellenfehler (PPM)", "AOI Koh Young aSpire3", "< 50 ppm", "—", "Sperrung, 100% Nachpruefung Roentgen"],
          ["Stromaufnahme EOL", "Pruefadapter PAd-EOL-014", "+/- 10 % nominal", ">= 1,67", "Charge sperren, Engineering-Hold"],
          ["Loetprofil Peak", "KIC SPS-3", "245 +/- 5 °C", ">= 1,33", "Linie stoppen, Profiling erneut"],
          ["Funktionstest CAN-FD", "Vector VN5640", "Bit Error < 1e-6", "—", "Sperrung, Software-Sample analysieren"]]),
        ("5. Aufzeichnungen",
         "Sicherung aller Pruefdaten gemaess Aufbewahrungspflicht 15 Jahre fuer "
         "sicherheitsbezogene Komponenten (D/TLD) bzw. 7 Jahre fuer Standardkomponenten. "
         "Backup in zentralem Q-DAS (qs-STAT), MES Hydra und Data Lake S3 (verschluesselt, EU-Region). "
         "Zugriffsschutz per RBAC. Bei OEM-Audit oder 8D-Anforderung erfolgt Aushang/Auszug "
         "innerhalb 24 h durch die Q-Beauftragten."),
        ("6. Aenderungshistorie / Freigabe",
         [["Rev.", "Datum", "Aenderung", "Freigabe"],
          ["00", "2018-04-12", "Erstausgabe", wl],
          ["01", "2020-06-30", "Umstellung Hydra-MES", q_loc],
          ["02", "2022-03-21", "Integration ESD-Anforderung OEM-CSR", q_loc],
          ["03", "2023-09-01", "Anpassung an IATF-16949-Rev 5; Reaktionsplan", "Sabine Brand (Konzern-Q)"]]),
        ("7. Unterschriften",
         signatures(wl, "Werkleitung " + site, site_name,
                    QHEAD_LOCAL.get(site, q_loc), "Q-Beauftragte", site_name,
                    place=site_loc.split(" (")[0], date_str_="1. September 2023")),
    ]


def kalibrierung(site: str, geraet: str) -> list:
    site_name, site_loc, wl, q_loc = SITE[site]
    titles = {
        "Drehmomentschluessel": ("Drehmomentschluessel Stahlwille MANOSKOP 730N/40", "0,8 – 40 Nm", "+/- 2 % v. MW", "DKD-K-19801"),
        "EMV-Prüfanlage":       ("EMV-Pruefanlage Rohde & Schwarz TS-EMC1", "10 kHz – 6 GHz", "ISO 11452-4 konform", "DAkkS D-K-15163"),
        "Hochspannungspruefer": ("Hochspannungspruefer Hipotronics HD120-5", "0 – 5 kV AC", "+/- 1 % v. EW", "DKD-K-31201"),
        "Impedanz-Analysator":  ("Impedanz-Analysator Keysight E4990A", "20 Hz – 120 MHz", "+/- 0,08 %", "DAkkS D-K-15163"),
        "Isolationsmessgeraet": ("Isolationsmessgeraet Megger MIT525", "50 V – 5 kV DC", "+/- 5 % v. MW", "DKD-K-31201"),
        "Klimakammer":          ("Klimakammer Weiss WKL 100/40", "-70 .. +180 °C / 10 .. 98 %rF", "+/- 1 K / +/- 3 %rF", "DKD-K-12305"),
        "Koordinatenmessmasch": ("Koordinatenmessmaschine Zeiss CONTURA G2 RDS", "X 700 / Y 700 / Z 600 mm", "MPE_E = (1,5 + L/350) µm", "DAkkS D-K-15163"),
        "Loetprofil-Messsyste": ("Loetprofil-Messsystem KIC SPS-3", "0 – 350 °C, 7 Kanaele", "+/- 1 °C", "DKD-K-08801"),
        "Messschieber":         ("Digitaler Messschieber Mitutoyo CD-15CPX", "0 – 150 mm", "+/- 0,02 mm", "DAkkS D-K-15163"),
        "Spektrum-Analysator":  ("Spektrumanalysator R&S FSV3030", "10 Hz – 30 GHz", "+/- 0,3 dB", "DAkkS D-K-15163"),
    }
    long_name, range_, accuracy, lab = titles.get(geraet, (geraet, "—", "—", "—"))
    return [
        ("1. Pruefmittel-Stammdaten",
         [["Feld", "Wert"],
          ["Pruefmittel-Nr.", f"PM-{site}-{geraet[:3].upper()}-014"],
          ["Bezeichnung", long_name],
          ["Hersteller / Typ", long_name.split(" ")[-2] if " " in long_name else long_name],
          ["Standort", f"{site_name}, {site_loc}, Pruefraum 3"],
          ["Verwendung", "Serien-Pruefmittel, kalibrierpflichtig"],
          ["Messbereich", range_],
          ["Messgenauigkeit (Hersteller)", accuracy],
          ["Akkreditiertes Labor", lab]]),
        ("2. Kalibrierungsdetails",
         [["Feld", "Wert"],
          ["Kalibrierdatum", "2023-09-15"],
          ["Naechste Kalibrierung", "2024-09-15"],
          ["Kalibrierintervall", "12 Monate"],
          ["Pruefer (extern)", "Dipl.-Ing. R. Glaeser, DAkkS-zertifiziert"],
          ["Pruefer (intern Anlieferung)", q_loc],
          ["Umgebungsbedingungen", "23 +/- 1 °C, 45 +/- 5 %rF"],
          ["Verwendete Normale", "Rueckfuehrbar auf PTB, Zert. PTB-3.4-2022-117"],
          ["Pruefverfahren", "DAkkS-DKD-R 3-3 bzw. herstellerspezifisch"]]),
        ("3. Messergebnisse (Auszug)",
         [["Pruefpunkt", "Sollwert", "Istwert", "Abweichung", "Toleranz", "Bewertung"],
          ["Punkt 1 (Untergrenze)", "10 % Range", "10,02 %", "+0,02 %", accuracy, "io"],
          ["Punkt 2", "25 % Range", "24,99 %", "-0,01 %", accuracy, "io"],
          ["Punkt 3", "50 % Range", "50,01 %", "+0,01 %", accuracy, "io"],
          ["Punkt 4", "75 % Range", "74,97 %", "-0,03 %", accuracy, "io"],
          ["Punkt 5 (Obergrenze)", "100 % Range", "99,98 %", "-0,02 %", accuracy, "io"]]),
        ("4. Bewertung und Freigabe",
         "Das Pruefmittel erfuellt die spezifizierten Messunsicherheits-Anforderungen und ist "
         "innerhalb der zulaessigen Toleranzen. Die erweiterte Messunsicherheit U (k=2) liegt "
         "unterhalb von 1/4 der engsten Pruefmerkmalstoleranz, womit das Pruefmittel gemaess "
         "VDA 5 / GUM fuer Serienpruefungen freigegeben ist. Kalibrieretikett wurde am 15.09.2023 "
         "durch das akkreditierte Labor angebracht. Eintrag in Konzern-PM-Datenbank "
         "(PRONTO Q-DAS) erfolgt automatisiert."),
        ("5. Eskalation und Aufbewahrung",
         "Bei Toleranzueberschreitung waere eine Rueckverfolgung aller seit der letzten "
         "Kalibrierung damit gemessenen Pruefumfaenge auf Konformitaet erforderlich (gemaess "
         "IATF 7.1.5.2.1). Die Kalibrierscheine werden zusammen mit den Pruefmittel-Stammdaten "
         "fuer mindestens 15 Jahre archiviert (Cloud-Backup S3, EU-Region, RBAC)."),
        ("6. Unterschriften",
         signatures(q_loc, "Q-Beauftragte / Pruefmittelueberwachung", site_name,
                    wl, "Werkleitung", site_name,
                    place=site_loc.split(" (")[0], date_str_="15. September 2023")),
    ]


def prozessaudit_beob(site: str, nr: str) -> list:
    site_name, site_loc, wl, q_loc = SITE[site]
    return [
        ("1. Auditkopf",
         [["Feld", "Wert"],
          ["Beobachtungs-Nr.", f"PA-{site}-2023-{nr}"],
          ["Audit-Datum", "2023-09-19"],
          ["Auditierter Prozess", "SMT-Linie 4 / Reflow + AOI"],
          ["Auditor", "Andreas Buehler (CAE) + Sabine Brand (Q-Konzern)"],
          ["Auditierter (Linie)", f"Schichtleitung {site}: Carsten Lindner / Stv. Petra Faber"],
          ["Audit-Typ", "Internes Prozessaudit (VDA 6.3 P5/P6) - Beobachtung"],
          ["Auditkriterien", "IATF 16949, VDA 6.3, OEM-CSR BMW/VW/MBZ/STE"]]),
        ("2. Beobachtungen / Findings",
         [["Nr.", "Klausel", "Beobachtung", "Klassifizierung"],
          ["F1", "VDA 6.3 P5.2.1", "Pruefadapter PAd-EOL-014 ohne sichtbares Kalibrieretikett im Einsatz; "
                                    "Pruefer konnte Status korrekt aus MES auslesen.", "Hinweis"],
          ["F2", "VDA 6.3 P5.3.5", "Schichtuebergabeprotokoll der Frühschicht fehlte eine Pflichtangabe "
                                    "(Geraetestatus AOI Koh Young).", "Nebenbeobachtung"],
          ["F3", "VDA 6.3 P6.4.1", "Reaktionsplan Loetprofil Out-of-Control korrekt umgesetzt, "
                                    "Linie wurde innerhalb 4 min gestoppt.", "Positivbeobachtung"],
          ["F4", "VDA 6.3 P6.5.2", "Mitarbeiter konnte 5-Why-Methodik zum letzten Fehlerfall einwandfrei "
                                    "erlaeutern.", "Positivbeobachtung"],
          ["F5", "IATF 7.1.5.1.1", "Temperaturlogger Klimakammer K-04 zeigte Drift > 1 K ueber 48 h; "
                                    "Kalibrierung vorziehen.", "Major-Risiko"]]),
        ("3. Vereinbarte Massnahmen",
         [["Nr.", "Massnahme", "Verantw.", "Frist"],
          ["M1", "Etikettenpflicht Pruefadapter PAd-EOL-014 in AA-EOL-01 aufnehmen", q_loc, "2023-10-15"],
          ["M2", "Vorlage HÜP digitalisieren, Pflichtfelder erzwingen", "IT-Q", "2023-11-30"],
          ["M3", "Vorgezogene Kalibrierung Klimakammer K-04", "Instandhaltung " + site, "2023-09-25"]]),
        ("4. Bewertung und Naechste Schritte",
         f"Die Linie wurde mit dem Reifegrad B (gut, mit kleineren Findings) bewertet. Erreichte "
         f"Punktzahl 87/100 nach VDA 6.3 Bewertungsschema. Die Q-Leitung von {site_name} stellt "
         "sicher, dass alle Massnahmen fristgerecht in OneQMS dokumentiert und mit Wirksamkeits-"
         "pruefung im Q4-Folgeaudit verifiziert werden. Bei nicht fristgerechter Schliessung wird "
         "die Beobachtung in eine CAPA hochgestuft."),
        ("5. Unterschriften",
         signatures("Andreas Buehler", "Chief Audit Executive (Auditor)", "Brennhagen Elektronik AG",
                    wl, "Werkleitung", site_name,
                    place=site_loc.split(" (")[0], date_str_="19. September 2023")),
    ]


def vda_audit(site: str) -> list:
    site_name, site_loc, wl, q_loc = SITE[site]
    return [
        ("1. Auditkopf",
         [["Feld", "Wert"],
          ["Audit-Nr.", f"VDA63-{site}-2023-001"],
          ["Audit-Datum", "2023-10-09 bis 2023-10-12"],
          ["Audit-Typ", "VDA 6.3 Prozessaudit (vollstaendig P2-P7)"],
          ["Auditierter Bereich", f"{site_name}, {site_loc}, gesamte Produktion"],
          ["Lead-Auditor", "Dipl.-Ing. Marlene Schoenherr, VDA-zert. Auditor-Nr. VDA-A-1873"],
          ["Co-Auditor", "Dr. Jochen Krause, ZF Friedrichshafen (Kundenauditor)"],
          ["Auftraggeber", "ZF Friedrichshafen AG (Lieferantenfreigabe-Audit)"]]),
        ("2. Auditfeststellungen (Auszug)",
         [["Element", "Bewertung", "Max", "%"],
          ["P2 Projektmanagement", "85", "100", "85 %"],
          ["P3 Produkt-/Prozessentwicklung-Planung", "88", "100", "88 %"],
          ["P4 Realisierung Produkt-/Prozessentwicklung", "82", "100", "82 %"],
          ["P5 Lieferantenmanagement", "78", "100", "78 %"],
          ["P6 Prozessanalyse Produktion", "90", "100", "90 %"],
          ["P7 Kundenbetreuung, Zufriedenheit, Service", "87", "100", "87 %"],
          ["Gesamtbewertung", "510", "600", "85 % (A — gut)"]]),
        ("3. Findings",
         "Ein Major Finding in P5.2.3 (Lieferanten-Re-Bewertung, siehe CAPA-2023-0007); zwei "
         "Minor Findings in P4.6.1 (Werkzeugfreigabe-Dokumentation unvollstaendig fuer Schicht C) "
         "und P5.1.4 (Lastenheft-Reviews mit Sub-Tier-Lieferanten teils nicht protokolliert). "
         "Drei Hinweise/Empfehlungen aus dem Bereich P6.5 (Visualisierung SPC-Karten an der Linie). "
         "Keine kritische Abweichung gefunden; Lieferantenfreigabe durch ZF wird empfohlen."),
        ("4. Massnahmenplan",
         [["Nr.", "Finding", "Frist", "Status"],
          ["M1", "Major P5.2.3 — CAPA-2023-0007 schliessen", "2023-12-15", "in Bearbeitung"],
          ["M2", "Minor P4.6.1 — Schicht C Werkzeugfreigabe-Workflow", "2023-11-30", "geplant"],
          ["M3", "Minor P5.1.4 — Lastenheft-Review-Protokoll-Pflicht", "2023-11-15", "geplant"],
          ["M4", "Hinweis P6.5 — Andon-Boards installieren", "2024-Q1", "in Planung"]]),
        ("5. Unterschriften",
         signatures("Marlene Schoenherr", "Lead-Auditor VDA 6.3", "VDA QMC",
                    wl, "Werkleitung", site_name,
                    place=site_loc.split(" (")[0], date_str_="12. Oktober 2023")),
    ]


def mr(site: str, year: int) -> list:
    site_name, site_loc, wl, q_loc = SITE[site]
    return [
        ("1. Sitzungsrahmen",
         [["Feld", "Wert"],
          ["Sitzungs-Nr.", f"MR-{site}-{year}-01"],
          ["Datum / Ort", f"15.12.{year}, {site_loc}"],
          ["Vorsitz", wl],
          ["Teilnehmer", "Werkleitung, QM, Produktion, Engineering, HR, Controlling, Konzern-Q (Brand)"],
          ["Auditperiode", f"01.01.{year} – 30.11.{year}"],
          ["Berichtsstandard", "IATF 16949 Klausel 9.3 (Managementbewertung)"],
          ["Vorbereitung", "Q-Cockpit-Auswertung; KPI-Sheet OneQMS"]]),
        ("2. KPI-Bilanz",
         [["KPI", "Ziel", "Ist", "Trend"],
          ["Reklamations-ppm (extern)", "< 25 ppm", "18 ppm", "verbessert"],
          ["Internal FPY (First Pass Yield)", "> 96 %", "97,2 %", "aufsteigend"],
          ["OTD (On-Time-Delivery)", "> 98 %", "98,4 %", "stabil"],
          ["OEE", "> 78 %", "79,1 %", "aufsteigend"],
          ["Anzahl 8D-Reports", "—", "11", "ruecklaeufig"],
          ["Audits durch OEMs", "—", "4 (alle bestanden)", "—"],
          ["IATF-Findings (extern, Surveillance)", "0 Major", "0 Major / 3 Minor", "io"],
          ["Mitarbeiterzufriedenheit Q (Umfrage)", "> 75 %", "78 %", "aufsteigend"],
          ["Kosten der Nichtqualitaet (CoNQ)", "< 1,8 % vom Umsatz", "1,6 %", "verbessert"],
          ["Anzahl Verbesserungsvorschlaege", "> 200", "247", "aufsteigend"]]),
        ("3. Bewertung Q-Management-System",
         "Das Q-System des Werks " + site_name + " hat sich im Berichtszeitraum als geeignet, "
         "angemessen und wirksam erwiesen. Die zentralen Q-Ziele wurden ueberwiegend erreicht, "
         "die Surveillance-Audits IATF 16949 und VDA 6.3 wurden ohne Major-Findings bestanden. "
         "Aenderungen im externen Kontext (z. B. neue OEM-CSR von BMW und Stellantis, geopolitische "
         "Lieferkettenrisiken Halbleiter, regulatorische Vorgaben Cybersecurity ISO/SAE 21434) "
         "wurden in der Risikomatrix beruecksichtigt. Ressourcenbedarf und -allokation wurde "
         "ueberprueft und an die Werkleitung beziehungsweise den Vorstand zur Genehmigung vorgelegt."),
        ("4. Beschluesse / Massnahmen",
         "Beschlossen wurden: (i) Erhoehung Investitionsbudget Pruefmittel 2024 um 220 kEUR; "
         "(ii) Einfuehrung Q-Champions-Programm auf Linienebene Q1/24; (iii) Aufstockung "
         "Reliability-Team um 2 FTE; (iv) Foerderung Schwarzgurt-DMAIC fuer drei Schluesselmitarbeiter; "
         "(v) Roll-out Andon-Boards in allen Produktionslinien bis Q3/24; (vi) Vorbereitung "
         "Re-Zertifizierung IATF 16949 (Audittermin Q3/" + str(year+1) + "); (vii) verstaerkte "
         "Lieferantenaudits VDA 6.3 fuer kritische Sub-Tier (Schaltschuetze, Pyrotechnik); "
         "(viii) Etablierung eines monatlichen Q-Reviews mit OEM-SQE per Teams. Alle Massnahmen "
         "werden im OneQMS getrackt; quartalsweises Reporting an die Konzern-Q. Naechste "
         f"Managementbewertung in Q4/{year+1}, alternativ ausserordentliche Sitzung bei Major-Q-"
         "Eskalation."),
        ("5. Unterschriften",
         signatures(wl, "Werkleitung", site_name,
                    "Sabine Brand", "Leitung QM Konzern", "Brennhagen Elektronik AG",
                    place=site_loc.split(" (")[0], date_str_=f"15. Dezember {year}")),
    ]


# --------------------------------------------------------------------------
# REA generic
# --------------------------------------------------------------------------

def rea_method(stub: str, prod: str = None, year: str = "2023") -> list:
    """REA_FMEA / DFMEA / PFMEA / CP / APQP / FLS / MSA / PPAP / SPC for a product or VA."""
    stub_full = {
        "APQP":   ("APQP — Advanced Product Quality Planning", "AIAG APQP 2nd Ed."),
        "CP":     ("Control Plan", "AIAG Control Plan / IATF 16949 Annex A"),
        "DFMEA":  ("Design FMEA", "AIAG-VDA FMEA 1st Ed. (2019)"),
        "PFMEA":  ("Prozess-FMEA", "AIAG-VDA FMEA 1st Ed. (2019)"),
        "FMEA":   ("System-FMEA", "AIAG-VDA FMEA 1st Ed. (2019)"),
        "FLS":    ("Funktionale Leistungsspezifikation (FLS)", "VDA 4 / OEM-Lastenheft"),
        "MSA":    ("MSA — Mess-System-Analyse", "AIAG MSA 4th Ed."),
        "PPAP":   ("PPAP — Production Part Approval Process", "AIAG PPAP 4th Ed."),
        "SPC":    ("SPC — Statistische Prozesslenkung", "AIAG SPC 2nd Ed."),
    }
    label, norm = stub_full.get(stub, (stub, "—"))
    if prod == "Verfahrensanweisung":
        scope = "Verfahrensanweisung (Konzern-Standard, alle Produkte)"
        prod_line = "alle Produktlinien (ICP-3, BMS-12, ADAS-V4D, ECU-900, LightCtrl-7)"
    else:
        prod_name, prod_desc, prod_spec = _prod(prod)
        scope = f"{prod_name} ({prod})"
        prod_line = f"{prod_name} ({prod_desc})"

    return [
        ("1. Dokumentenkopf",
         [["Feld", "Wert"],
          ["Dokumenttyp", label],
          ["Norm / Methode", norm],
          ["Geltungsbereich", scope],
          ["Produkt(linie)", prod_line],
          ["Aenderungsstand", "Rev. 03"],
          ["Erstellt / Datum", f"Sabine Brand, Q-Konzern / 15. September {year}"],
          ["Geprueft", "Dr. Heike Renz, Leitung Entwicklung"],
          ["Freigegeben", "Dr. Thomas Weber, COO"]]),
        ("2. Zweck und Anwendung",
         f"Dieses Dokument beschreibt die konzernweit verbindliche Anwendung der Methode "
         f"»{label}« gemaess {norm} im Rahmen des Konzern-Qualitaetsmanagements der Brennhagen "
         "Elektronik AG. Es ist verbindlich fuer alle Produktionswerke (REG Heilbronn, RPL Katowice, "
         "RCZ Brno, RHU Gyoer) sowie fuer die Software-Tochter RSG Muenchen, soweit anwendbar. "
         "Die Methode bildet einen integralen Bestandteil der OEM-Bemusterung sowie der "
         "laufenden Serienueberwachung der genannten Steuergeraete."),
        ("3. Methodische Eckpunkte",
         ("clauses", [
             ("3.1 — Verantwortlichkeiten",
              ["Konzern-Q (Brand) ist Methoden-Eigner und stellt Schulungen, Templates "
               "(in OneQMS) sowie Auditrechte sicher.",
               "Werks-Q (lokal) verantwortet die operative Anwendung und stellt Ergebnisse "
               "in Q-DAS qs-STAT zur Verfuegung.",
               "Entwicklung (RSG / Hardware) liefert FLS, Lastenhefte und Aenderungs-ECNs."]),
             ("3.2 — Inputs",
              ["Lastenheft des OEM / Produktanforderungen",
               "Vorgaengerprojekt-Lessons-Learned aus PRO-Datenbank",
               "Stand der Technik (AUTOSAR R23-11, ISO 26262:2018, ISO/SAE 21434:2021)"]),
             ("3.3 — Outputs",
              ["Freigabematerial fuer Gate-Review (G3/G4) gem. APQP-Phasenplan",
               "Eingang in PPAP-Paket fuer den OEM",
               "Eingang in Control Plan und Pruefumfaenge der Serienproduktion"])
         ])),
        ("4. Ergebnis-Auszug (Stand " + year + ")",
         [["Kennzahl", "Wert", "Bewertung"],
          ["Anzahl Eintraege / Faelle", "184", "vollstaendig"],
          ["Top-RPN / Top-AP", "AP=H (3 Faelle), AP=M (12 Faelle)", "Massnahmen in Arbeit"],
          ["Cpk Schlu	sselmerkmale", ">= 1,67", "io"],
          ["Audit-Findings 2023 (intern)", "1 Minor, 0 Major", "io"]]),
        ("5. Aufzeichnungen / Verteiler",
         "Das Dokument wird in OneQMS abgelegt (Dokument-ID OQMS-" + stub + "-" + (prod or "X") + "-2023). "
         "Verteiler: Vorstand COO, Konzern-Q, alle Werks-Q, Engineering-Lead RSG, OEM-Account-Manager. "
         "Aufbewahrungspflicht: 15 Jahre fuer sicherheitsbezogene Bestandteile, sonst 7 Jahre. "
         "Backup im EU-Data-Lake S3 (verschluesselt)."),
        ("6. Unterschriften",
         signatures("Sabine Brand", "Leitung QM Konzern", "Brennhagen Elektronik AG",
                    "Dr. Thomas Weber", "COO", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_=f"15. September {year}")),
    ]


def rea_iatf_zert(year: str) -> list:
    return [
        ("1. Zertifikatsangaben",
         [["Feld", "Wert"],
          ["Zertifikat-Nr.", f"IATF-DE-22148-{year}"],
          ["Zertifizierungsstelle (CB)", "DEKRA Certification GmbH, Stuttgart"],
          ["DEKRA-Zulassungs-Nr.", "DE-IATF-CB-0119"],
          ["IATF-Oversight-Office", "VDA QMC (Frankfurt am Main)"],
          ["Lead-Auditor", "Dr. Christian Welt (DEKRA, IATF-AI-114)"],
          ["Co-Auditor", "Marlene Schoenherr (DEKRA, IATF-AI-181)"],
          ["Ausstellungsdatum", f"15. Oktober {year}"],
          ["Gueltig ab / bis", f"15. Oktober {year} / 14. Oktober {int(year)+3}"],
          ["Re-Zertifizierungsaudit", f"Q3/{int(year)+3}"],
          ["Surveillance-Audits jaehrlich", "ja, jeweils Q3"],
          ["Standard", "IATF 16949:2016 (Rev. 5) i. V. m. ISO 9001:2015"]]),
        ("2. Anwendungsbereich (Scope)",
         "Entwicklung, Konstruktion, Industrialisierung und Produktion elektronischer Steuergeraete "
         "fuer den Automotive-Bereich, einschliesslich Infotainment, Advanced-Driver-Assistance-Systeme "
         "(ADAS), Powertrain-Steuergeraete, Batteriemanagementsysteme (BMS) und Lichtsteuergeraete. "
         "Eingeschlossen sind die Werke REG Heilbronn (Hauptproduktion DE), RPL Katowice (EMS/SMD PL), "
         "RCZ Brno (Steckverbinder CZ) und RHU Gyoer (Sensorik HU). Die Embedded-Software-Tochter "
         "RSG Muenchen ist nach ASPICE Level 2-3 separat assessiert (kein IATF-Geltungsbereich, da "
         "keine physische Produktion). Vertriebsgesellschaften (RCN Shanghai) sind ueber Remote-Site-"
         "Anhang erfasst (Sales-Support-Remote-Location nach IATF-Rules-5th Ed. Sanctioned Interpretations)."),
        ("3. Auditfeststellungen",
         [["Element", "Bewertung", "Bemerkung"],
          ["Major Findings", "0", "—"],
          ["Minor Findings", "3", "alle innerhalb 60 d geschlossen, CAPA-2023-0007/0011/0019"],
          ["Opportunities for Improvement", "12", "in CAPA-Plan ueberfuehrt; Tracking OneQMS"],
          ["Postives Audit-Highlight", "—", "Q-Champions-Programm REG (Best Practice)"]]),
        ("4. Aufrechterhaltung und Re-Zertifizierung",
         "Surveillance-Audits werden jaehrlich im Q3 in jeweils einem Werk gefuehrt; Re-Zertifizierungs-"
         "audit nach 3 Jahren mit vollem Audit-Scope (alle vier Produktionswerke). Wechsel des "
         "Lead-Auditors gemaess IATF-Rules nach 3 Jahren ist geplant. Alle Major-Findings sind "
         "innerhalb 90 Tagen zu schliessen; bei Nichtschliessung droht Zertifikatsruhe (Suspended) "
         "und ggf. Rueckzug (Withdrawn) gemaess IATF-Auditor-Guide. Die REA bestaetigt die "
         "Aufrechterhaltung der Wirksamkeit ihres Q-Managementsystems durch jaehrliche "
         "Managementbewertung (siehe MR-Berichte)."),
        ("5. Freigabe",
         signatures("Dr. Christian Welt", "Lead-Auditor DEKRA Certification", "DEKRA Certification GmbH",
                    "Sabine Brand", "Leitung QM Konzern", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_=f"15. Oktober {year}")),
    ]


def rea_internes_audit(year: str) -> list:
    return [
        ("1. Auditprogramm",
         [["Feld", "Wert"],
          ["Programm-Nr.", f"IA-IATF-{year}"],
          ["Auditzeitraum", f"KW 32 – KW 44 / {year}"],
          ["Lead-Auditor", "Andreas Buehler (CAE, IATF/VDA-6.3-zert.)"],
          ["Auditteam", "5 zertifizierte interne Auditoren (VDA 6.3 / IATF)"],
          ["Auditierte Werke", "REG, RPL, RCZ, RHU; Methoden-Audit RSG"],
          ["Auditkriterien", "IATF 16949:2016 Rev. 5; VDA 6.3 (P2-P7); OEM-CSR"],
          ["Berichtsadressat", "Vorstand, Konzern-Q, Audit Committee"]]),
        ("2. Auditplan",
         [["Werk", "Datum", "Auditor", "Klauseln / Schwerpunkt"],
          ["REG Heilbronn", f"04.-08.09.{year}", "A. Buehler / S. Brand", "alle, Schwerpunkt Klausel 8/9"],
          ["RPL Katowice", f"11.-15.09.{year}", "K. Rauch / M. Klima", "alle"],
          ["RCZ Brno",     f"18.-22.09.{year}", "K. Rauch", "Klauseln 4-10"],
          ["RHU Gyoer",    f"25.-29.09.{year}", "M. Klima", "Klauseln 4-10"],
          ["RSG Muenchen", f"02.-06.10.{year}", "A. Buehler", "Methoden / Software-CSR / ASPICE"]]),
        ("3. Audit-Methodik",
         "Die Audits wurden gemaess Process-Approach durchgefuehrt. Pro Werk waren 4 Auditmanntage "
         "angesetzt mit interdisziplinaerem Auditteam (Q, Engineering, Operations). "
         "Auditcheckliste basiert auf IATF-Auditor-Guide 5th Ed. und der konzerneigenen "
         "Checkliste IATF-CHK-23 (Rev. 04). Findings werden tagesgleich am Closing-Meeting "
         "kommuniziert und im OneQMS dokumentiert (Workflow IAU-2023-NNNN). Wirksamkeitspruefung "
         "ist Bestandteil des CAPA-Workflows."),
        ("4. Zusammenfassung Ergebnis",
         "Insgesamt wurden 47 Findings festgestellt (0 Major, 9 Minor, 38 Hinweise). "
         "Schwerpunkt-Themen: Lieferanten-Re-Bewertung (Klausel 8.4.2.4), Pruefmittel-"
         "Identifikation (7.1.5.2.1), Trainingseffektivitaet (7.2), Aenderungsmanagement "
         "(8.5.6), Korrekturmassnahmen (10.2). Alle Minor-Findings wurden in CAPA ueberfuehrt "
         "(CAPA-2023-0001 bis -0020). Wirksamkeit der Massnahmen wird im "
         f"Q1/{int(year)+1} stichprobenartig nachgeprueft. Im Vergleich zum Vorjahr "
         "(2022: 51 Findings, 1 Major) ist ein deutlicher Reifegradgewinn zu verzeichnen. "
         "Empfehlung: Erweiterung des Trainings-Programms fuer Schichtleitungen sowie "
         "Visualisierung SPC-Karten an der Linie (Andon)."),
        ("5. Freigabe",
         signatures("Andreas Buehler", "Chief Audit Executive", "Brennhagen Elektronik AG",
                    "Sabine Brand", "Leitung QM Konzern", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_=f"15. Oktober {year}")),
    ]


def rea_oem_qbr(oem: str, prod: str, year: str, quarter: str) -> list:
    oem_name, oem_addr, oem_modell = _oem(oem)
    prod_name, prod_desc, prod_spec = _prod(prod)
    return [
        ("1. Sitzungsrahmen",
         [["Feld", "Wert"],
          ["Sitzung", f"Quarterly Business Review (QBR) Quality"],
          ["Sitzungs-Nr.", f"QBR-{oem}-{prod}-{quarter.replace(' ', '-')}"],
          ["Datum", f"15. Juni {year}"],
          ["Ort / Format", oem_addr + " / hybrid (Teams)"],
          ["OEM-Vertretung", f"{oem_name}, SQE: Dr. M. Kahler; Q-Director: B. Lasse; "
                              "Engineering: Dr. F. Tritt"],
          ["REA-Vertretung", "Sabine Brand (Q-Konzern), Stefan Richter (CMO/BD), "
                              "Account-Mgr T. Wolke, Werkleitung REG (Maier)"],
          ["Produkt im Fokus", f"{prod_name} ({prod})"],
          ["Programm", oem_modell]]),
        ("2. KPI-Review",
         [["KPI", "Ziel", "Ist " + quarter, "Vorjahr", "Trend"],
          ["Reklamations-ppm", "< 25 ppm", "14 ppm", "21 ppm", "verbessert"],
          ["OTD (On-Time-Delivery)", "> 98 %", "99,1 %", "98,2 %", "aufsteigend"],
          ["Sortenwechsel/Tag", "—", "12", "10", "stabil"],
          ["8D-Closure-Time", "< 60 d", "47 d (Median)", "55 d", "verbessert"],
          ["CSL-Eskalationen aktiv", "0", "0", "1", "io"],
          ["PPM Software-Defects", "< 5 ppm", "2 ppm", "4 ppm", "verbessert"],
          ["NCR-Quote (open / closed)", "—", "3 / 8", "5 / 11", "verbessert"]]),
        ("3. Top-3-Themen aus OEM-Sicht",
         ("list", [
             "Roadmap Aenderungen ECN-2023-019 (Software v1.4, Re-PPAP geplant fuer KW40)",
             "Risiko Halbleiterallokation (NXP TDA4VM); REA hat Pufferbestand fuer 12 Wochen",
             "Joint-CIP zur Reduktion Loetstellenfehler um 30 % bis Q4/2023; Pilotprojekt REG Linie 4",
         ])),
        ("4. Beschluesse und Aktionspunkte",
         "Folgende Themen wurden besprochen und beschlossen: (i) Joint-CIP-Programm mit 6 "
         "Workshops in 2023/2024 (Kickoff 10.07.); (ii) Vorbereitung VDA-6.3-Lieferanten-Audit "
         "fuer Q3/2023 (Lead: Marlene Schoenherr); (iii) gemeinsamer Risiko-Workshop EOL-Migration "
         "auf neue Pruefadapter PAd-EOL-018; (iv) bilateraler Austausch Treasury/Procurement zu "
         "Liefervereinbarungen 2024/2025; (v) Naechste QBR am 12.09.2023 vor Ort REG Heilbronn "
         "inkl. Werksbegehung. Alle Aktionspunkte werden im OEM-Q-Portal getrackt; "
         "Status-Updates monatlich."),
        ("5. Unterschriften",
         signatures("Dr. M. Kahler", "SQE", oem_name,
                    "Sabine Brand", "Leitung QM Konzern", "Brennhagen Elektronik AG",
                    place=oem_addr.split(",")[1].strip() if "," in oem_addr else "Stuttgart",
                    date_str_=f"15. Juni {year}")),
    ]


def rea_qmh() -> list:
    return [
        ("1. Geltungsbereich des QM-Handbuchs",
         "Dieses Qualitaetsmanagementhandbuch dokumentiert das integrierte Managementsystem der "
         "Brennhagen Elektronik AG und ihrer Tochtergesellschaften gemaess den Anforderungen der "
         "IATF 16949:2016 (5. Revision), ISO 9001:2015, ISO 14001:2015, ISO 50001:2018 sowie "
         "ISO/IEC 27001:2022 (im Aufbau). Es bildet den verbindlichen Rahmen fuer alle Q-relevanten "
         "Prozesse vom Lastenheft bis zur Serienueberwachung."),
        ("2. Prozesslandschaft",
         [["Prozessgruppe", "Hauptprozesse", "Verantw."],
          ["Fuehrungsprozesse", "Strategie, Managementbewertung, Risikomanagement", "Vorstand"],
          ["Kernprozesse", "APQP, PPAP, Serie, Aenderungsmanagement, Reklamation", "COO / Q-Konzern"],
          ["Unterstuetzungsprozesse", "HR, IT, Finance, Lieferantenmanagement, Wartung", "CFO/HR/IT"]]),
        ("3. Q-Politik und -Ziele",
         "Die Q-Politik der Brennhagen Elektronik AG lautet: »Wir gestalten zuverlaessige Elektronik "
         "fuer die Mobilitaet von morgen — mit messbarer Null-Fehler-Mentalitaet und partnerschaftlicher "
         "Lieferantenintegration.« Daraus abgeleitete strategische Q-Ziele 2023-2025: "
         "Reklamations-ppm <= 20 (extern); FPY >= 97 %; OEE >= 80 %; 0 Major bei IATF-Surveillance; "
         "Lieferantenaudits VDA 6.3 >= 12/Jahr."),
        ("4. Aufbau- und Ablauforganisation",
         "Konzern-Q ist direkt dem COO unterstellt (Dr. Thomas Weber). Die Werks-Q-Verantwortlichen "
         "berichten matrixfoermig an die Werkleitung sowie fachlich an Konzern-Q (Brand). Aenderungs- "
         "und Eskalationswege sind im Process Atlas (PA-2023-Rev04) dokumentiert. ASPICE-Bewertung "
         "der RSG-Software-Tochter erfolgt durch INTACS-Provisional Assessor."),
        ("5. Aenderungsmanagement und Freigabe",
         signatures("Sabine Brand", "Leitung QM Konzern", "Brennhagen Elektronik AG",
                    "Dr. Thomas Weber", "COO", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_="15. September 2023")),
    ]


def rea_inf_liefer_halbleiter(year: str) -> list:
    return [
        ("Praeambel",
         "Zwischen der Brennhagen Elektronik AG (»REA«), Vaihinger Strasse 120, 70567 Stuttgart, und "
         "der Infineon Technologies AG (»INF«), Am Campeon 1-15, 85579 Neubiberg, wird der vorliegende "
         "Q-Sicherungsvertrag zur Lieferung von Mikrocontrollern (Aurix TC399, Aurix TC397) und "
         "Power-Management-ICs fuer den Einsatz in BMS-12, ECU-900 und LightCtrl-7 geschlossen. Der "
         "Vertrag erfaellt die Anforderungen der IATF 16949 sowie der AEC-Q100-Klassifikation."),
        ("§ 1 Vertragsgegenstand und Bauteile",
         [["Material-Nr.", "Bezeichnung", "AEC-Q100 Grade", "PPAP-Level"],
          ["INF-TC399-V-128", "Aurix TC399 32-bit MCU", "Grade 1 (-40..+125 °C)", "Level 3"],
          ["INF-TC397-V-064", "Aurix TC397 32-bit MCU", "Grade 1", "Level 3"],
          ["INF-TLF35584",    "Safety SBC PMIC", "Grade 1", "Level 3"],
          ["INF-TLE9012",     "Battery Monitoring IC", "Grade 1", "Level 3"]]),
        ("§ 2 Qualitaetsanforderungen",
         "Es gelten die Konzern-CSR der REA (Rev. 2023) und die VDA-Bedingungen 2002. Reklamations-ppm "
         "Zielwert <= 5 ppm (Halbleiter), 8D-Closure-Zeit < 30 Tage. Allokationsrisiken werden quartalsweise "
         "gemeinsam reviewt; Eskalation an Vorstand bei drohender Linienstoppgefahr."),
        ("§ 3 Aenderungsmanagement (PCN)",
         "Aenderungen sind 6 Monate vor Wirksamkeit ueber PCN-Workflow (SAE J1739) anzukuendigen. "
         "Sicherheitsbezogene Aenderungen erfordern Re-PPAP und Freigabe durch REA-Q sowie OEM."),
        ("§ 4 Unterschriften",
         signatures("Sabine Brand", "Leitung QM Konzern", "Brennhagen Elektronik AG",
                    "Dr. R. Roth", "Director Customer Quality", "Infineon Technologies AG",
                    place="Stuttgart", date_str_=f"15. November {year}")),
    ]


def rea_vw_csr(year: str) -> list:
    return [
        ("1. Geltungsbereich",
         "Diese Dokumentation regelt die Anwendung der kundenspezifischen Anforderungen (CSR) der "
         "Volkswagen AG (Konzernnorm VW01155, Formel-Q Konkret 7. Edition, VW80808, VDA Band 6.3) "
         "im Q-System der Brennhagen Elektronik AG. Sie ist verbindlich fuer alle Lieferungen an die "
         "VW-Marken (VW Pkw, Audi, Porsche, Skoda, SEAT/Cupra, VW Nutzfahrzeuge). Die Dokumentation "
         "ist Bestandteil des konzernweiten Q-Management-Handbuchs (Kapitel 9.7, OEM-CSR) und in "
         "OneQMS als verbindliche Verfahrensanweisung VA-CSR-VW-23 abgelegt."),
        ("2. Wesentliche Anforderungen",
         [["Anforderung", "Kapitel CSR", "Umsetzung REA"],
          ["Formel Q Konkret 7th Ed. (Lieferantenbewertung)", "gesamt", "Konzern-QMS, Werks-Audits, Re-Bewertung jaehrlich"],
          ["VW01155 Liefervorschrift Schweissprozess", "spez.", "n. a. (Elektronik, keine Schweissprozesse)"],
          ["VW80101 Werkstoffe RoHS/REACH", "VW80101 Teil 1-4", "Datasheet-Pflicht in IMDS, Stammdatenpflege"],
          ["IMDS-Reporting (International Material Data System)", "VW-IMDS-Anleitung", "Pflicht-Upload < 14 d nach PPAP"],
          ["VDA 6.3 Lieferantenaudit", "VDA 6.3 P2-P7", "jaehrlich bzw. risikobasiert (Risk Rating)"],
          ["Eskalationsprozess (CSL-1/CSL-2)", "VW-Eskalationsmatrix 2022", "definiert im Konzern-QMH Kap. 8.3"],
          ["Run-At-Rate (R@R)", "Formel Q Anhang B", "vor SOP zwingend, Re-R@R bei Aenderungen"],
          ["Behaelter- und Verpackungsvorschrift", "VW-VPRG", "Mehrwegbehaelter REG → VW gem. VPRG-Katalog"],
          ["Cybersecurity (ab MJ 2024)", "VW80818-CS, ISO/SAE 21434", "umgesetzt in RSG-Entwicklung"]]),
        ("3. Spezifika BMS-12 (ID.7)",
         "Fuer das Programm ID.7 (BMS-12) gelten zusaetzliche Anforderungen aus VW80101-1 (Hochvolt-"
         "Komponenten ASIL D), VW80818 (Pyrotechnik-Initiatoren Schnittstelle) sowie VW80000 "
         "(Allgemeine Komponentenanforderungen). PPAP-Level 3, Run-At-Rate vor SOP zwingend. "
         "Re-PPAP bei jeder hardware-relevanten Aenderung. Die Werke REG (Endmontage), RPL "
         "(SMT) und RCZ (Stecker) sind in der konsolidierten Lieferantenfreigabe der VW gemeinsam "
         "aufgenommen; jede Aenderung des Wertschoepfungsanteils ist mit der VW Group "
         "Procurement (Wolfsburg) abzustimmen."),
        ("4. Schulung und Kommunikation",
         "Schulung der Anforderungen erfolgt jaehrlich fuer alle Q-Mitarbeitenden (eLearning-Modul "
         "OneQMS-CSR-VW-001, Dauer 90 min, Pflicht). Die jaehrliche Ueberarbeitung erfolgt durch "
         "Sabine Brand (Konzern-Q) gemeinsam mit dem VW-Account-Manager Stefan Richter (CMO/BD). "
         "Kommunikationskanaele: SupplyOn-Portal (operative Daten), VW Group Supplier Portal "
         "(strategische Anforderungen), persoenliche QBR alle 3 Monate."),
        ("5. Freigabe",
         signatures("Sabine Brand", "Leitung QM Konzern", "Brennhagen Elektronik AG",
                    "Dr. Thomas Weber", "COO", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_=f"15. Mai {year}")),
    ]


def rea_vw_ecr(year: str, nr: str) -> list:
    return [
        ("1. Kopfdaten",
         [["Feld", "Wert"],
          ["ECR-Nr. (VW)", f"VW-ECR-{year}-{nr}"],
          ["ECR-Nr. (REA intern)", f"REA-ECR-{year}-{nr}"],
          ["Sachnummer Kunde", "VW-7N0907115-ADAS-V4D"],
          ["Sachnummer REA", "RAE-ADAS-V4D-A02"],
          ["Programm", "VW MEB+ / ID.7 / Audi Q6 e-tron"],
          ["Aenderungsgrund", "Software-Update ASIL B (Radar-Calibration) v1.3 → v1.4"],
          ["Antragsdatum", f"15. September {year}"],
          ["Wirksamkeitsdatum (SOP)", f"02. Januar {int(year)+1}"],
          ["Re-PPAP erforderlich", "Ja (Level 3, Software-only Sample)"],
          ["FuSi-Manager", "Dr. Markus Hauser (RSG)"],
          ["VW-SQE", "Dr. M. Kahler"]]),
        ("2. Beschreibung der Aenderung",
         "Anpassung des Radar-Fusion-Algorithmus zur Verbesserung der Range-Estimation bei "
         "Nebelbedingungen (FOG-Use-Case) und unter starkem Regen (Heavy-Rain-Use-Case, > 50 mm/h). "
         "Aenderung der Software-Version von v1.3 auf v1.4 (Branch release/v1.4.0, Commit-ID "
         "a47b9c2). Keine Hardware-Aenderung; Bauteilliste und Sachnummer-Stammdaten bleiben "
         "unveraendert. Re-Verifikation gemaess ISO 26262:2018 (ASIL B) durch FuSi-Manager "
         "Dr. Markus Hauser (RSG); Re-Penetrationstest gem. ISO/SAE 21434 durch externes Lab. "
         "Re-PPAP nach AIAG 4th Ed. mit Schwerpunkt Software-Sample, Regressionstest-Bericht "
         "(7 200 Testfaelle, Coverage 96,4 %) und 30-Tage-Pilotlauf in VW-Werk Wolfsburg "
         "(200 Vorserienfahrzeuge)."),
        ("3. Auswirkungen / Risiken",
         [["Bereich", "Auswirkung", "Risiko", "Mitigation"],
          ["Stueckkosten", "keine", "—", "—"],
          ["Lieferzeiten", "vorgezogene Stillstandsphase Linie 4 fuer SW-Flash (2 x 4 h, KW 51/52)", "moderat", "Sondertaktung Linie 2 als Backup"],
          ["Re-Validierung", "Regressionstest, Pen-Test, 30-Tage-Pilot", "moderat", "Pruefslot DEKRA/BSI reserviert"],
          ["OEM-Programmplan", "kompatibel mit VW-Wave-Planning Wolfsburg", "niedrig", "VW-Programm-Manager bestaetigt"],
          ["FuSi (ISO 26262)", "Re-Argumentation Safety-Case Kap. 4.7", "niedrig", "vorbereitet durch RSG FuSi-Team"],
          ["Cybersecurity", "Re-Argumentation Security-Case + TARA-Update", "niedrig", "ISO/SAE 21434 Re-Assessment KW43"]]),
        ("4. Freigabe",
         signatures("Sabine Brand", "Leitung QM Konzern", "Brennhagen Elektronik AG",
                    "Dr. Markus Hauser", "FuSi-Manager", "Brennhagen Software GmbH",
                    place="Stuttgart", date_str_=f"15. September {year}")),
    ]


def rea_ste_qbr_q2(year: str) -> list:
    return rea_oem_qbr("STE", "BMS-12", year, "Q2 " + year)


def rea_vorstand_q3(year: str) -> list:
    return [
        ("1. Anlass und Adressat",
         "Vorstandsvorlage der Q-Konzern fuer die Vorstandssitzung Q3/" + year + " der "
         "Brennhagen Elektronik AG. Berichterstatterin: Sabine Brand (Leitung QM Konzern). "
         "Adressaten: CEO Anna Mueller, CFO Laura Bauer, COO Dr. Thomas Weber, CTO Stefan "
         "Hoffmann, CMO Stefan Richter, CRO Asia Dr. Yuki Tanaka."),
        ("2. Q-Kennzahlen Q3/" + year,
         [["Kennzahl", "Ziel", "Ist", "Trend"],
          ["Reklamations-ppm Konzern", "< 25", "16 ppm", "↓"],
          ["8D-Closure-Time", "< 60 d", "44 d (Median)", "↓"],
          ["OEE Konzern", "> 78 %", "79,4 %", "↑"],
          ["VDA-6.3-Lieferantenaudits", "3/Quartal", "4 abgeschlossen", "↑"],
          ["CAPA-Closure-Quote", "> 90 %", "92 %", "→"],
          ["IATF-Surveillance-Findings", "0 Major", "0 Major / 3 Minor", "io"]]),
        ("3. Top-Risiken und Massnahmen",
         "Top-Risiken Q3: (1) Halbleiterallokation INF/TI Q1-2/2024; (2) Inflationsdruck "
         "Lieferantenpreise PCB; (3) anstehende ASPICE-Re-Assessment RSG; (4) bevorstehende "
         "Re-Zertifizierung IATF 16949 fuer REG Heilbronn (Q1/2024). Massnahmenplan ist im "
         "Anhang A dokumentiert; Investitionsbedarf 2024: 2,8 Mio. EUR (Pruefmittel + IT)."),
        ("4. Beschlussempfehlung",
         "Der Vorstand wird gebeten, den vorgelegten Massnahmenplan zur Kenntnis zu nehmen und "
         "die Investitionssumme 2024 (2,8 Mio. EUR) im Rahmen des Budgetprozesses zu beruecksichtigen. "
         "Die Q-Konzernleitung wird quartalsweise berichten."),
        ("5. Unterschriften",
         signatures("Sabine Brand", "Leitung QM Konzern", "Brennhagen Elektronik AG",
                    "Dr. Thomas Weber", "COO", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_="15. Oktober " + year)),
    ]


# --------------------------------------------------------------------------
# Misc small builders
# --------------------------------------------------------------------------

def eco_ecu(nr: str, year: str) -> list:
    return [
        ("1. Engineering Change Order — Kopfdaten",
         [["Feld", "Wert"],
          ["ECO-Nr.", f"ECO-ADAS-V4D-{nr}"],
          ["Produkt", "ADAS-V4D Radar Fusion ECU"],
          ["Sachnummer REA", "RAE-ADAS-V4D-A02 → A03"],
          ["Aenderungsgrund", "PCB-Layer-Optimierung zur EMV-Verbesserung (Klasse 5 → Klasse 4)"],
          ["Initiator", "Engineering RSG, Dr. Markus Hauser"],
          ["Antragsdatum", f"02. September {year}"],
          ["Wirksamkeitsdatum", f"01. November {year}"],
          ["Re-PPAP-Pflicht", "Ja, Level 3"],
          ["Betroffene OEM-Programme", "BMW iX i20, Stellantis Peugeot e-3008, Mercedes EQS V297"],
          ["CCB-Sitzung", f"15. September {year}, Stuttgart"],
          ["CCB-Vorsitz", "Dr. Petra Hollmann (CTO)"]]),
        ("2. Beschreibung der Aenderung",
         "Aenderung des 8-Lagen-PCB-Layouts zur Verbesserung der EMV-Performance (BCI/ALSE) gemaess "
         "ISO 11452-4 und ISO 11452-2. Veraendert wurden die Massflaechen-Topologie auf Layer 3 und 6 "
         "sowie zwei Filterkomponenten (C147 von 100 nF auf 220 nF; L23 von 4,7 µH auf 10 µH). Die "
         "Schaltungsfunktion bleibt unveraendert, die Aenderung ist rein passiv-filtertechnisch. "
         "Re-Verifikation gem. ISO 26262 ASIL B mit kompletter EMV-Re-Validierung, BCI nach "
         "ISO 11452-4 (100 V/m Anforderung), ALSE nach ISO 11452-2, plus ESD-Pruefungen nach "
         "ISO 10605 (Air- und Contact-Discharge bis +/- 25 kV). Hintergrund: vom Kunden BMW im "
         "Rahmen der iX i20 Vorserienpruefung wurde eine grenzwertige EMV-Performance im Bereich "
         "700-900 MHz festgestellt (gemessen 92 V/m statt geforderter 100 V/m); diese Aenderung "
         "stellt einen robusten Sicherheitsabstand her und entkoppelt das System fuer kommende "
         "Programme (Stellantis STLA-Large)."),
        ("3. Auswirkungs- und Risikobewertung",
         [["Bereich", "Auswirkung", "Risiko", "Mitigation"],
          ["Stueckkosten", "+0,18 EUR/Stueck", "akzeptabel", "in Kalkulation 2024 eingepreist"],
          ["Lieferzeiten", "+2 Wochen PCB-Anlauf bei AT&S", "moderat", "Pufferbestand 8 Wochen vorhanden"],
          ["Re-Validierung", "BCI/ALSE/ESD-Re-Test (4 Wochen)", "moderat", "Pruefslot Klimakammer reserviert"],
          ["OEM-Approval", "BMW + STE + MBZ benachrichtigt", "niedrig", "Re-PPAP-Level 3 geplant"],
          ["Bestandsabwertung A02", "ca. 60 kEUR (3.200 Stueck)", "akzeptabel", "Abverkauf bis SOP A03"],
          ["FuSi-Argumentation", "Sicherheitsnachweis ASIL B", "niedrig", "Safety Case Update CR-19"]]),
        ("4. Validierungs- und Abnahmeplan",
         "Vor SOP A03 erfolgt eine 3-stufige Validierung: (i) Komponenten-Tests bei AT&S, (ii) "
         "Funktions- und Umwelttests im Werk REG Heilbronn (Klimakammer Weiss WKL 100/40, "
         "Temperaturschock -40/+95 °C, Vibration nach LV 124), (iii) externe EMV-Pruefung bei "
         "DEKRA Stuttgart. Erwartete Pruefdauer 4 Wochen. Pilot-Run mit 250 Stueck auf Linie 4 "
         f"REG am 10. Oktober {year} geplant. Run-At-Rate-Audit durch BMW SQE am 25. Oktober {year}."),
        ("5. Aenderungsmanagement und Verteiler",
         "Aenderungs-Workflow erfolgt in OneQMS (Workflow-ID OQMS-ECO-2023-013). Alle "
         "Engineering-, Q-, Produktions- und OEM-Account-Manager werden via PCN (Process Change "
         "Notification) gem. VDA-Schema informiert. Aktualisierung Control Plan, PFMEA "
         "(RPN-Neubewertung Filter), Stueckliste (BoM), SAP-MM-Stammdaten sowie Pruefadapter "
         "PAd-ADAS-014 (Software-Update). Aufnahme in Konzern-Lessons-Learned LL-2023-082."),
        ("6. Freigabe",
         signatures("Dr. Markus Hauser", "Engineering Lead", "Brennhagen Software GmbH",
                    "Sabine Brand", "Leitung QM Konzern", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_=f"15. September {year}")),
    ]


def it_change_request(nr: str) -> list:
    return [
        ("1. Change Request — Kopfdaten",
         [["Feld", "Wert"],
          ["CR-Nr.", f"ITSM-CR-2023-{nr}"],
          ["System", "OneQMS (Q-Dokumentenmanagement, Veeva-basiert)"],
          ["Antragsteller", "Sabine Brand (Q-Konzern)"],
          ["CAB-Datum", "2023-09-21"],
          ["Klassifikation", "Standard Change, Risiko niedrig"],
          ["Implementation-Window", "Sa 30.09.2023, 22:00 – So 01.10.2023, 02:00"],
          ["Service-Owner", "Florian Maier, Group Controller (IT-Sponsor Q-Apps)"],
          ["Implementer", "Veeva Vault Professional Services + Brennhagen IT-Q"],
          ["Verbundene CAPA / Audit", "CAPA-2023-0007 (IATF-Internes Audit KW36)"],
          ["Aufwand (geschaetzt)", "2 PT IT + 0,5 PT Veeva + 0,5 PT QM (UAT)"]]),
        ("2. Beschreibung der Aenderung",
         "Ergaenzung eines Pflichtfeldes »Naechste Re-Bewertung« im SRM-Workflow "
         "(Lieferantenbewertung) zur Schliessung des CAPA-2023-0007. Hintergrund: das interne "
         "IATF-Audit 2023 hatte eine Major-Abweichung zur Klausel 8.4.2.4 festgestellt, "
         "wonach 14 von 47 produktiven Lieferanten nicht fristgerecht reevaluiert wurden. "
         "Mit der Ergaenzung eines harten Pflichtfeldes plus automatischer Eskalation 30 / 14 / 7 "
         "Tage vor Fristablauf an den jeweiligen Lieferantenmanager und dessen Stellvertretung "
         "wird dieser Befund systemisch geschlossen. Implementation durch IT-Team Q-Apps "
         "(Florian Maier) in Zusammenarbeit mit Veeva-Support. Test in QA-System bereits "
         "abgeschlossen (Testfall TC-CR-019-01 bis -07), UAT durch Sabine Brand am 18.09.2023 "
         "mit Pass-Status."),
        ("3. Risiko- und Rollback-Plan",
         "Rollback via Konfigurations-Backup vor Deployment moeglich (Schritt 1 vor Deployment "
         "ist Snapshot der Workflow-Konfiguration). Keine Daten-Migration erforderlich, da die "
         "Aenderung das Datenmodell nur additiv erweitert (Default-Wert: heute + 365 Tage "
         "fuer Bestandslieferanten). Bei Produktionsproblem Rollback < 30 min moeglich. "
         "Service-Window faellt auf Wochenende mit erwartet 0 aktiven Nutzern; Notfall-Service-"
         "Hotline 0800-ROHRIG-IT ist besetzt."),
        ("4. Auswirkungen und Tests",
         [["Aspekt", "Ergebnis"],
          ["Funktional (Pflichtfeld erscheint)", "bestanden"],
          ["Automatische Eskalations-Mails", "bestanden, geprueft fuer alle 3 Stufen"],
          ["Bestandsdaten-Migration", "n. a. (additiv)"],
          ["Performance", "keine Degradierung gemessen"],
          ["Berechtigungs-Modell", "unveraendert (RBAC)"],
          ["Schnittstelle zu SAP Ariba", "kompatibel (REST API v3)"]]),
        ("5. Genehmigung CAB",
         signatures("Florian Maier", "Group Controller / IT-Sponsor Q", "Brennhagen Elektronik AG",
                    "Sabine Brand", "Leitung QM Konzern", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_="21. September 2023")),
    ]


def prj_2023_003(month: str) -> list:
    return [
        ("1. Projektkopf",
         [["Feld", "Wert"],
          ["Projekt-Nr.", "PRJ-2023-003"],
          ["Titel", "ICP-3 OTA-Update-Plattform"],
          ["Projektleiter", "Dr. Markus Hauser (RSG)"],
          ["Auftraggeber", "Vorstand CTO (Dr. Petra Hollmann)"],
          ["Berichtsmonat", month],
          ["Phase", "Realisierung (G3 → G4)"],
          ["Berichtsstandard", "PMI / PRINCE2 Hybrid + AUTOSAR-OTA"],
          ["Letzter Steering-Termin", "12. Oktober 2023, Muenchen"]]),
        ("2. Statusampel",
         [["Dimension", "Ampel", "Kommentar"],
          ["Termin (Zeit)", "Gelb", "SOP-Pilot 4 Wochen verzoegert (CSL-1 Effekt)"],
          ["Budget", "Gruen", "78 % verbraucht (Plan 80 %)"],
          ["Qualitaet", "Gruen", "Cpk-Ziele erfuellt, alle FuSi-Werkzeuge qualifiziert"],
          ["Risiken", "Gelb", "OTA-Backend-Skalierung > 30 Tsd Fahrzeuge / Lastspitzen"],
          ["Ressourcen", "Gruen", "Team 18 FTE (12 Dev / 4 Test / 2 PM), 1 Backfill offen"],
          ["Stakeholder", "Gruen", "BMW SQE, MBZ SQE wohlgesonnen"]]),
        ("3. Meilensteine im Berichtsmonat",
         [["Meilenstein", "Plan", "Ist", "Status"],
          ["Software-Release v0.9 (Pilot)", "10.10.2023", "12.10.2023", "abgeschlossen"],
          ["Penetration-Test BSI-Beratung", "20.10.2023", "20.10.2023", "abgeschlossen"],
          ["Vertrag AWS Frankfurt OTA-Backend", "15.10.2023", "15.10.2023", "abgeschlossen"],
          ["ASPICE SYS.5 Re-Assessment", "31.10.2023", "in Arbeit", "auf Kurs"]]),
        ("4. Inhaltliche Statusdarstellung",
         "Im Berichtsmonat Oktober 2023 wurden alle Pflicht-Meilensteine erreicht. Die Software-"
         "Release v0.9 wurde nach erfolgreichem Code-Freeze (06.10.) freigegeben und auf der "
         "Pilot-Flotte (BMW iX, Mercedes EQS) erfolgreich deployt. Ergebnisse Pen-Test: 0 "
         "Critical, 3 High (alle remediated, Re-Test bestanden, Bericht BSI-Beratung Nr. PT-23-"
         "112). Backend-Skalierung: Vertrag mit AWS Frankfurt fuer dedizierte EKS-Cluster (3 AZ) "
         "ist signiert; geplante Kapazitaet 30 Tsd parallele Updates. Risiko Backend-Skalierung "
         "wird durch Lasttest (Locust, 50 Tsd VU) bis Mitte November adressiert."),
        ("5. Naechste Schritte / G4-Review",
         "Naechste Schritte: (i) Lasttest Backend bis 15.11.; (ii) Pilot mit 200 Testfahrzeugen "
         "BMW + Mercedes bis 30.11.; (iii) Erstellung G4-Unterlagen (Safety Case, Security Case, "
         "PPAP-Skizze); (iv) G4-Review geplant fuer 15.11.2023 mit Vorstand, OEM-Vertretern und "
         "Konzern-Q. Bei positivem G4 erfolgt SOP-Vorbereitung mit Run-At-Rate-Audit Q1/2024."),
        ("6. Freigabe",
         signatures("Dr. Markus Hauser", "Projektleiter", "Brennhagen Software GmbH",
                    "Dr. Petra Hollmann", "CTO", "Brennhagen Elektronik AG",
                    place="Muenchen", date_str_="31. Oktober 2023")),
    ]


def rcz_ic_quartal(qy: str) -> list:
    return [
        ("1. Berichtsrahmen",
         [["Feld", "Wert"],
          ["Berichtsperiode", qy],
          ["Bericht", "Internal Control / Internal Audit (Werk RCZ Brno)"],
          ["Adressat", "Konzern Audit Committee (Dr. Steinbrueck), CAE (Buehler)"],
          ["Erstellt von", "Eva Cerna (Q-Leitung RCZ), Vladimir Hrdy (Controlling RCZ)"],
          ["Erstelldatum", "30. September 2020"],
          ["Berichtsformat", "ICS-Quartalsbericht gem. Konzern-ICS-Handbuch"],
          ["Reifegrad ICS RCZ", "Stufe 4 von 5 (regelmaessige Operating-Effectiveness)"]]),
        ("2. Kontroll-Findings (Test of Design / Operating Effectiveness)",
         [["Kontrolle", "Beschreibung", "Stichprobe", "Status", "Aktion"],
          ["IK01", "Berechtigungstrennung SAP (4-Augen-Prinzip Buchungen)", "30 Belege", "io", "—"],
          ["IK02", "Quartalsweise Konto-Abstimmung (Sachkonten + Bank)", "alle 24 Konten", "io", "—"],
          ["IK03", "Lieferantenstammdaten Pflege (Anlage, Aenderung, Sperre)", "50 Aenderungen", "Hinweis", "Sondereinstellungen 12 Faelle"],
          ["IK04", "Reklamations-CAPA-Konsistenz (Q vs. SAP-Buchung)", "20 Faelle", "io", "—"],
          ["IK05", "TPM-Wartungsfristen Maschinen", "alle 18 Anlagen", "io", "—"],
          ["IK06", "Kassenfuehrung Werkskasse", "alle Tage", "io", "—"],
          ["IK07", "Reisekosten-Prozess (Beleg/Genehmigung)", "30 Abrechnungen", "io", "—"]]),
        ("3. Detail Hinweis IK03",
         "Im Pruefumfang IK03 wurden 12 Faelle identifiziert, in denen Lieferantenstammdaten "
         "(Bankverbindung, Zahlungsbedingungen) ausserhalb des standardisierten Workflows ueber "
         "SAP-Direktbuchung durch berechtigte Power-User geaendert wurden. Die Sondereinstellungen "
         "waren in 11 von 12 Faellen sachlich gerechtfertigt und dokumentiert; in einem Fall fehlt "
         "die schriftliche Genehmigung der Werkleitung. Massnahme: Nachreichung Genehmigung "
         "und Verschaerfung des Workflow-Bypass-Verfahrens bis 31.12.2020. "
         "Verantwortlich: Vladimir Hrdy, Controlling."),
        ("4. Zusammenfassung",
         "Keine wesentlichen Schwaechen identifiziert. Quartalsergebnis bestaetigt die Wirksamkeit "
         "der internen Kontrollen im Werk Brno. Eine Hinweis-Findung (IK03) wird mit Massnahme "
         "bis 31.12. abgestellt. Naechste Quartalspruefung im Folgequartal Q4/2020 mit Schwerpunkt "
         "Jahresabschluss-Vorbereitung."),
        ("5. Unterschriften",
         signatures("Eva Cerna", "Q-Leitung RCZ Brno", "Brennhagen CZ s.r.o.",
                    "Andreas Buehler", "Chief Audit Executive", "Brennhagen Elektronik AG",
                    place="Brno", date_str_="30. September 2020")),
    ]


def rpl_ic_quartal(qy: str) -> list:
    return [
        ("1. Berichtsrahmen",
         [["Feld", "Wert"],
          ["Berichtsperiode", qy],
          ["Bericht", "Internal Control / Quartalsbericht (Werk RPL Katowice)"],
          ["Adressat", "Konzern Audit Committee (Dr. Steinbrueck), CAE Buehler"],
          ["Erstellt von", "Anna Kowalska (HR/Compliance), Marek Wojciechowski (Werkleitung)"],
          ["Bericht-Datum", "30. Juni 2019"],
          ["Berichtsstandard", "Konzern-ICS-Handbuch Rev. 2018; COSO 2013"],
          ["Pruefumfang", "alle Schluesselkontrollen RPL Katowice + Hub Zabrze"]]),
        ("2. Kontroll-Findings",
         [["Kontrolle", "Beschreibung", "Stichprobe", "Status", "Aktion"],
          ["IK01", "Berechtigungstrennung SAP / Ariba", "30 Belege", "io", "—"],
          ["IK02", "Inventur Stichprobe (Wareneingangslager)", "200 Pos.", "io", "—"],
          ["IK03", "Cash-Handling Werkskasse", "alle Tage", "io", "—"],
          ["IK04", "Personalnebenkosten / Spesenabrechnung", "30 Abrechnungen", "Hinweis", "2 Beleg-Nacherfassung"],
          ["IK05", "Schlue	sselverwaltung Zugangskontrolle", "alle Schluessel", "io", "—"],
          ["IK06", "Wareneingangs-Buchungskontrolle (3-Way-Match)", "50 Buchungen", "io", "—"],
          ["IK07", "Lohnsteuer / Sozialversicherung Polen (ZUS)", "Monatsmeldungen", "io", "—"]]),
        ("3. Detail Hinweis IK04",
         "In 2 von 30 stichprobenartig geprueften Reisekostenabrechnungen fehlten Bewirtungsbelege "
         "ueber zusammen ca. 84 EUR; die Belege wurden nachgereicht und vom Vorgesetzten "
         "(Marek Wojciechowski) gegengezeichnet. Massnahme: Im Folgequartal werden alle Bewirtungs-"
         "und Hotelbelege per Pflichtfeld im Concur-System unmittelbar als Foto-Upload eingefordert. "
         "Schulung der Schichtleitung Mitte Juli 2019. Verantwortlich Anna Kowalska."),
        ("4. Zusammenfassung",
         "Keine materiellen Schwaechen festgestellt. Die Hinweis-Finding aus IK04 wird durch "
         "erweiterte Belegpflicht im naechsten Quartal abgestellt. Die interne Kontrollstruktur "
         "des Werks RPL Katowice ist wirksam und angemessen. Naechste Quartalspruefung erfolgt "
         "Ende September 2019 mit Schwerpunkt Halbjahresabschluss-Vorbereitung."),
        ("5. Unterschriften",
         signatures("Anna Kowalska", "HR/Compliance", "Brennhagen Polska Sp. z o.o.",
                    "Andreas Buehler", "Chief Audit Executive", "Brennhagen Elektronik AG",
                    place="Katowice", date_str_="30. Juni 2019")),
    ]


def reg_br_protokoll() -> list:
    return [
        ("1. Sitzungsrahmen",
         [["Feld", "Wert"],
          ["Sitzung", "Betriebsratssitzung REG Heilbronn"],
          ["Sitzungs-Nr.", "BR-REG-2020-10"],
          ["Datum / Ort", "15.10.2020, Schulungsraum 2, Werk Heilbronn"],
          ["Beginn / Ende", "13:00 – 16:45 Uhr"],
          ["Vorsitz", "Klaus Bauer (BR-Vorsitz REG)"],
          ["Schriftfuehrung", "Heike Lorenz (BR-Stv.)"],
          ["Anwesend", "11 von 13 BR-Mitgliedern; entschuldigt: M. Reuter, J. Voss"],
          ["Gaeste", "Andreas Maier (Werkleitung), Sabine Brand (Q-Konzern, zu TOP 2)"]]),
        ("2. Tagesordnung",
         ("list", [
             "TOP 1 — Begruessung, Feststellung Beschlussfaehigkeit, Genehmigung Protokoll der "
             "Vorsitzung",
             "TOP 2 — Aktuelle Q-Lage Werk REG (Bericht Sabine Brand)",
             "TOP 3 — Schichtmodell 2021 (Diskussion mit Werkleitung)",
             "TOP 4 — Mitarbeitendenbefragung Q4/2020 (Konzept und Zeitplan)",
             "TOP 5 — Anhoerung gem. § 99 BetrVG: Einstellung 3 Schichtmitarbeitende SMT",
             "TOP 6 — Bericht aus Konzernbetriebsrat (M. Duerr)",
             "TOP 7 — Verschiedenes"])),
        ("3. Wesentliche Diskussionspunkte",
         "Zu TOP 2 berichtete Sabine Brand ueber die aktuelle Q-Lage Werk REG: Reklamations-ppm "
         "fuer Q3/2020 bei 22 ppm (Ziel < 25); 8D-Closure-Time im Median bei 51 Tagen. Der BR begruesste "
         "die Trendverbesserung. Zu TOP 3 wurde das Schichtmodell 2021 ausfuehrlich diskutiert; "
         "die Werkleitung hat ein Konzept fuer eine angepasste Pausenregelung vorgelegt, das vom BR "
         "in zwei Punkten ergaenzt wurde (zusaetzliche 5 Minuten zwischen Frueh- und Spaetschicht "
         "Uebergabe; Klarstellung Raucherpausen). Zu TOP 5 stimmte der BR der Einstellung der drei "
         "Schichtmitarbeitenden ohne Einwaende gem. § 99 BetrVG zu."),
        ("4. Beschluesse",
         "Beschluss B-2020-10-01: Der Betriebsrat empfiehlt die Beibehaltung des 3-Schicht-Modells "
         "fuer 2021 mit Anpassungen der Pausenzeiten gem. neuem Arbeitszeitkonzept. Abstimmung "
         "11/0/0 (ja/nein/Enthaltung). "
         "Beschluss B-2020-10-02: Befuerwortung des Q-Champions-Programms; BR-Sitz im Steuerungsgremium "
         "(Klaus Bauer). Abstimmung 10/0/1. "
         "Beschluss B-2020-10-03: Zustimmung zur Einstellung der drei Schichtmitarbeitenden SMT "
         "ohne Einwaende. Abstimmung 11/0/0. "
         "Naechste Sitzung 12.11.2020, 13:00 Uhr, Schulungsraum 2."),
        ("5. Unterschriften",
         signatures("Klaus Bauer", "BR-Vorsitz", "REG Heilbronn",
                    "Heike Lorenz", "BR-Stv.", "REG Heilbronn",
                    place="Heilbronn", date_str_="15. Oktober 2020")),
    ]


def rsg_br_wahl(year: int) -> list:
    return [
        ("1. Wahlrahmen",
         [["Feld", "Wert"],
          ["Wahltermin", f"15. Juni {year}"],
          ["Wahlvorstand", "Dr. Klaus Kessler (Wahlleiter), J. Roth, M. Berger"],
          ["Anzahl Wahlberechtigte", "320"],
          ["Wahlbeteiligung", "78 %"],
          ["Form", "Listenwahl, geheim, mit Briefwahl-Option (BetrVG § 24)"],
          ["Wahlausschreiben", "10. Mai " + str(year)],
          ["Bekanntgabe Ergebnis", "16. Juni " + str(year) + " (Aushang Foyer + Intranet)"]]),
        ("2. Ergebnis nach Listen",
         [["Liste", "Spitzenkandidat/in", "Stimmen", "%", "Sitze"],
          ["Liste A — Software-Entwicklung", "Janina Roth", "121", "48,4 %", "4"],
          ["Liste B — Test/Validierung", "Markus Hahn", "87", "34,8 %", "2"],
          ["Liste C — Verwaltung/Admin", "Petra Maurer", "42", "16,8 %", "1"]]),
        ("3. Gewaehlte Betriebsratsmitglieder",
         ("list", [
             "Janina Roth (Liste A) — Software-Entwicklung, Senior-Entwicklerin",
             "Stefan Knoll (Liste A) — Software-Entwicklung, Test Lead",
             "Carolin Voss (Liste A) — Reliability Engineering",
             "Lukas Hagen (Liste A) — Praktikum / Junior-Entwicklung",
             "Markus Hahn (Liste B) — Test/Validierung, ASPICE Assessor",
             "Sandra Lerch (Liste B) — Test-Automatisierung",
             "Petra Maurer (Liste C) — Office Management Muenchen"])),
        ("4. Konstituierende Sitzung",
         "Die konstituierende Sitzung des neugewaehlten BR der RSG findet am 22. Juni " + str(year) +
         " um 09:00 Uhr im Konferenzraum Isar statt. Wahl von BR-Vorsitz, Stellvertretung und "
         "Schriftfuehrung erfolgt nach BetrVG § 26. Empfehlung des Wahlvorstands fuer die "
         "Vorsitz-Kandidatur: Janina Roth (Liste A). Weiterhin wird ein Vertreter in den "
         "Konzern-Betriebsrat (KBR) entsendet; Vorschlag: Janina Roth oder Stefan Knoll. "
         "Die konstituierende Sitzung schliesst mit einer Vorstellung des BR-Geschaeftsverteilungsplans, "
         "der Festlegung der Sitzungsrhythmen (14-taegig) und der Vereinbarung der Sprechzeiten."),
        ("5. Wahlanfechtungsfristen / Rechtsbehelf",
         "Gemaess BetrVG § 19 betraegt die Anfechtungsfrist 2 Wochen ab Bekanntgabe des Ergebnisses. "
         "Anfechtungen sind beim Arbeitsgericht Muenchen einzureichen. Bis zum Ablauf der Frist "
         "erfolgt keine Veroeffentlichung in externen Medien."),
        ("6. Unterschriften",
         signatures("Dr. Klaus Kessler", "Wahlvorstand", "RSG Muenchen",
                    "J. Roth", "Wahlvorstand", "RSG Muenchen",
                    place="Muenchen", date_str_=f"15. Juni {year}")),
    ]


def rhu_ic_rechnung() -> list:
    return [
        ("1. Rechnungsdaten",
         [["Feld", "Wert"],
          ["Rechnungs-Nr.", "RHU-IC-2020-11-014"],
          ["Rechnungssteller", "Brennhagen Hungary Kft., Gyoer (HU)"],
          ["USt-IdNr. (HU)", "HU-23847190"],
          ["Empfaenger", "Brennhagen Elektronik GmbH, Heilbronn (DE)"],
          ["USt-IdNr. (DE)", "DE-126451234"],
          ["Leistung", "Konzern-IC: Sensorbaugruppen Charge 2020-11"],
          ["Liefermenge", "12.500 Stueck Sensorbaugruppen SEN-A2"],
          ["Stueckpreis IC", "8,40 EUR (Cost-Plus 5 %, gem. TP-Policy 2020)"],
          ["Rechnungsbetrag netto", "105.000,00 EUR"],
          ["Innergemeinschaftliche Lieferung", "ja, steuerfrei nach § 6a UStG"],
          ["Rechnungsdatum", "30. November 2020"],
          ["Leistungsdatum", "Lieferung gem. CMR-Frachtbrief 14.-23.11.2020"],
          ["Faelligkeitsdatum", "30. Dezember 2020 (30 Tage netto)"],
          ["IC-Abrechnungs-Code", "ICTRX-RHU-REG-2020-11"],
          ["Bestellungs-Nr. (REG)", "REG-PO-2020-1187"]]),
        ("2. Leistungs- und Lieferungsumfang",
         [["Pos.", "Material", "Menge", "Preis/St.", "Summe netto"],
          ["1", "Sensorbaugruppe SEN-A2 (12-Kanal Cell-Monitoring)", "10.000 St.", "8,40 EUR", "84.000,00 EUR"],
          ["2", "Sensorbaugruppe SEN-A2 (Variante Hi-Temp)", "2.500 St.", "8,40 EUR", "21.000,00 EUR"],
          ["", "Summe netto", "12.500 St.", "—", "105.000,00 EUR"]]),
        ("3. Hinweise / Konzern-Verrechnung",
         "Die Berechnung erfolgt gemaess konzerninterner Verrechnungspreis-Policy (TP-Policy "
         "Dr. Heike Berger, Group Tax Director, Stand 2020). Methode: Cost-Plus 5 %, lokale "
         "Vergleichsanalyse fuer Sensorbaugruppen mit unabhaengigen Vergleichsunternehmen "
         "(Benchmark-Studie Q4/2019 durch KPMG Tax). Die Rechnung ist in der Konzern-IC-Plattform "
         "Coupa Treasury hinterlegt; Netting im Folgemonat ueber In-House-Bank (Markus Pflanzer, "
         "Group Treasurer). Die zugrundeliegende Liefer- und Leistungsvereinbarung (LV-RHU-REG-2018) "
         "ist Bestandteil der TP-Dokumentation und wird im Rahmen des Local File / Master File "
         "berichtet."),
        ("4. Genehmigung",
         signatures("Laszlo Kovacs", "Werkleitung RHU", "Brennhagen Hungary Kft.",
                    "Andreas Maier", "Werkleitung REG", "Brennhagen Elektronik GmbH",
                    place="Gyoer", date_str_="30. November 2020")),
    ]


# --------------------------------------------------------------------------
# Dispatcher
# --------------------------------------------------------------------------

def parse_8d(stem: str):
    # 8D_2023_001_BMW_ICP-3
    m = re.match(r"8D_(\d{4})_(\d{3})_([A-Z]+)_(.+)$", stem)
    if not m:
        return None
    return m.group(2), m.group(3), m.group(4)


def parse_msa(stem: str):
    m = re.match(r"MSA_Messunsicherheitsstudie_2023_(\d{3})", stem)
    return m.group(1) if m else None


def parse_capa(stem: str):
    m = re.match(r"CAPA_2023_(\d{4})", stem)
    return m.group(1) if m else None


def parse_ppap(stem: str):
    # PPAP_BMW_ADAS-V4D_2022_Level3
    m = re.match(r"PPAP_([A-Z]+)_([A-Za-z0-9\-]+)_(\d{4})_(L(?:evel)?\s?3)", stem)
    if not m:
        return None
    return m.group(1), m.group(2), m.group(3), "Level 3"


def parse_aa(stem: str):
    m = re.match(r"(REG|RSG|RPL|RCZ|RHU)_AA_([A-Za-z_]+?)(?:_\d{4})", stem)
    if not m:
        return None
    return m.group(1), m.group(2).rstrip("_")


def parse_kal(stem: str):
    m = re.match(r"(REG|RSG|RPL|RCZ|RHU)_Kalibrierung_([A-Za-zÄÖÜäöüß-]+)_", stem)
    return (m.group(1), m.group(2)) if m else None


def parse_pa(stem: str):
    m = re.match(r"(REG|RSG|RPL|RCZ|RHU)_Prozessaudit_Beobachtung_2023_(\d{3})", stem)
    return (m.group(1), m.group(2)) if m else None


def parse_vda(stem: str):
    m = re.match(r"VDA63_Prozessaudit_(REG|RSG|RPL|RCZ|RHU)", stem)
    return m.group(1) if m else None


def parse_mr(stem: str):
    m = re.match(r"MR_(REG|RSG|RPL|RCZ|RHU)_Managementbewertung_(\d{4})", stem)
    return (m.group(1), int(m.group(2))) if m else None


def build_sections_for(path: Path):
    stem = path.stem
    fn = path.name

    # 8D
    if stem.startswith("8D_"):
        info = parse_8d(stem)
        if info:
            return f"8D-Report Nr. 2023-{info[0]} — {_oem(info[1])[0]} / {_prod(info[2])[0]}", eightd(*info)

    if stem.startswith("CAPA_"):
        nr = parse_capa(stem)
        if nr:
            return f"CAPA-Vorgang Nr. CAPA-2023-{nr}", capa(nr)

    if stem.startswith("PPAP_"):
        info = parse_ppap(stem)
        if info:
            oem, prod, year, lvl = info
            return f"PPAP {lvl} — {_prod(prod)[0]} fuer {_oem(oem)[0]} ({year})", ppap(oem, prod, year, lvl)

    if stem.startswith("MSA_Messunsicherheitsstudie"):
        nr = parse_msa(stem)
        if nr:
            return f"MSA-Studie MSA-2023-{nr}", msa(nr)

    if stem.startswith("MR_"):
        info = parse_mr(stem)
        if info:
            site, yr = info
            return f"Managementbewertung {SITE[site][0]} {yr}", mr(site, yr)

    if stem.startswith("VDA63_"):
        site = parse_vda(stem)
        if site:
            return f"VDA-6.3-Prozessaudit {SITE[site][0]} 2023", vda_audit(site)

    if "_AA_" in stem:
        info = parse_aa(stem)
        if info:
            site, kind = info
            return f"Arbeitsanweisung {kind.replace('_', ' ')} — {SITE[site][0]}", aa(site, kind)

    if "_Kalibrierung_" in stem:
        info = parse_kal(stem)
        if info:
            site, geraet = info
            return f"Kalibrierprotokoll {geraet} — {SITE[site][0]}", kalibrierung(site, geraet)

    if "_Prozessaudit_Beobachtung_" in stem:
        info = parse_pa(stem)
        if info:
            site, nr = info
            return f"Prozessaudit-Beobachtung PA-{site}-2023-{nr}", prozessaudit_beob(site, nr)

    # Misc explicit files
    if stem == "ECO_ADAS-V4D_013_Engineering_Change_2023":
        return "Engineering Change Order ECO-ADAS-V4D-013", eco_ecu("013", "2023")
    if stem == "IT_Change_Request_2023_0019":
        return "IT-Change-Request ITSM-CR-2023-0019", it_change_request("0019")
    if stem.startswith("PRJ-2023-003_Statusbericht"):
        return "Projekt-Statusbericht ICP-3 OTA-Plattform — Oktober 2023", prj_2023_003("Oktober 2023")
    if stem == "RCZ_IC_Quartalsbericht_2020_Q3":
        return "Interner Kontrollbericht RCZ Brno — Q3/2020", rcz_ic_quartal("Q3/2020")
    if stem == "REG_BR_Protokoll_2020_10":
        return "Betriebsrats-Protokoll REG Heilbronn — Oktober 2020", reg_br_protokoll()
    if stem == "RPL_IC_Quartalsbericht_2019_Q2":
        return "Interner Kontrollbericht RPL Katowice — Q2/2019", rpl_ic_quartal("Q2/2019")
    if stem == "RSG_BR_Wahl_Protokoll_2022":
        return "BR-Wahl-Protokoll RSG Muenchen 2022", rsg_br_wahl(2022)
    if stem == "RHU_IC_Rechnung_2020_11":
        return "Konzern-IC-Rechnung RHU → REG vom 30.11.2020", rhu_ic_rechnung()

    # REA family
    if stem.startswith("REA_"):
        # REA_<METHOD>_<PROD>_<YEAR>
        m = re.match(r"REA_(APQP|CP|DFMEA|PFMEA|FMEA|FLS|MSA|PPAP|SPC)_([A-Za-z0-9\-]+)_(\d{4})", stem)
        if m:
            method, prod, year = m.group(1), m.group(2), m.group(3)
            return (f"REA-Konzern-{method} — {prod} ({year})",
                    rea_method(method, prod, year))
        if stem.startswith("REA_Externes_IATF_Zertifikat"):
            year = stem.rsplit("_", 1)[-1]
            return f"Externes IATF-Zertifikat {year}", rea_iatf_zert(year)
        if stem.startswith("REA_Internes_IATF_Audit"):
            year = stem.rsplit("_", 1)[-1]
            return f"Internes IATF-Audit Programmbericht {year}", rea_internes_audit(year)
        if stem.startswith("REA_INF_Liefervertrag_Halbleiter"):
            year = stem.rsplit("_", 1)[-1]
            return f"Q-Sicherungsvertrag REA - Infineon Halbleiter ({year})", rea_inf_liefer_halbleiter(year)
        if stem.startswith("REA_Qualitaetsmanagementhandbuch_IATF16949"):
            return "Konzern-Qualitaetsmanagementhandbuch IATF 16949 (Rev. 2023)", rea_qmh()
        if stem.startswith("REA_STE_BMS-12_QBR_2023_Q2"):
            return "QBR Quality Stellantis / BMS-12 — Q2 2023", rea_ste_qbr_q2("2023")
        if stem.startswith("REA_Vorstandspr") and "2023_Q3" in stem:
            return "Vorstandsvorlage Q-Konzern Q3/2023", rea_vorstand_q3("2023")
        if stem.startswith("REA_VW_ADAS-V4D_ECR_2022_002"):
            return "Engineering Change Request VW-ECR-2022-002 ADAS-V4D", rea_vw_ecr("2022", "002")
        if stem.startswith("REA_VW_CSR_Kundspezifische_Anforderungen_2023"):
            return "CSR Volkswagen — Anwendungsdokumentation REA 2023", rea_vw_csr("2023")

    # Fallback (shouldn't happen if our enumeration is complete)
    return None


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    t0 = time.time()
    written = 0
    skipped = []
    for p in sorted(BASE.rglob("*.docx")):
        result = build_sections_for(p)
        if not result:
            skipped.append(p.name)
            continue
        title, sections = result
        write_doc(str(p), H, title, sections)
        written += 1
    dt = time.time() - t0
    print(f"Wrote {written} docs in {dt:.1f}s; skipped {len(skipped)}")
    if skipped:
        for s in skipped[:30]:
            print("  SKIPPED:", s)


if __name__ == "__main__":
    main()
