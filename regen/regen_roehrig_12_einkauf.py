"""Brennhagen AG / 12_Einkauf_Lieferanten - regen thin docs (round 2)."""
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
import re
from pathlib import Path

sys.path.insert(0, f"{_ROOT}")
from enhance_lib import ROEHRIG_AG as R, ROEHRIG_SUBS as S, write_doc, signatures

BASE = Path(f"{_ROOT}/roehrig_large/12_Einkauf_Lieferanten")
H = {"name": R["name"], "addr": R["addr"], "hrb": R["hrb"]}

# ---- supplier master ---------------------------------------------------------
SUP = {
    "INF": {
        "full": "Infineon Technologies AG",
        "addr": "Am Campeon 1-15, 85579 Neubiberg",
        "kategorie": "Mikrocontroller / Power-Halbleiter / AURIX TC3xx / TLE-Treiber",
        "kam": "Herr Dr. Markus Boettcher (Key Account Manager Automotive Tier-1)",
        "qmb": "Frau Dr. Stefanie Lenz",
        "umsatz_eur_mio": 78,
        "anteil_buchung": "33 %",
        "kritikalitaet": "A (single-source AURIX TC397 fuer ECU-900 und ADAS-V4D)",
        "id": "REA-L-INF",
    },
    "NXP": {
        "full": "NXP Semiconductors Germany GmbH",
        "addr": "Troplowitzstrasse 20, 22529 Hamburg",
        "kategorie": "CAN-/LIN-/Ethernet-Transceiver, S32-MCU-Familie, MIFARE-Security",
        "kam": "Frau Petra Sommer (Senior Account Manager EMEA Automotive)",
        "qmb": "Herr Olaf Brandt",
        "umsatz_eur_mio": 62,
        "anteil_buchung": "26 %",
        "kritikalitaet": "A (kritisch fuer ICP-3 Gateway-Funktion, dual-source mit STM)",
        "id": "REA-L-NXP",
    },
    "STM": {
        "full": "STMicroelectronics GmbH",
        "addr": "Bahnhofstrasse 18, 85609 Aschheim-Dornach",
        "kategorie": "STM32-MCU, MEMS-Sensoren (Druck/Inertial), SiC-Power-MOSFETs",
        "kam": "Sig. Luca Marini (EMEA Automotive Account Director)",
        "qmb": "Frau Isabella Conti",
        "umsatz_eur_mio": 48,
        "anteil_buchung": "20 %",
        "kritikalitaet": "B (zweitquelle MCU; einzige Quelle MEMS-Drucksensor BMS-12)",
        "id": "REA-L-STM",
    },
    "BOS": {
        "full": "Robert Bosch GmbH - Bosch Sensortec",
        "addr": "Gerhard-Kindler-Strasse 9, 72770 Reutlingen",
        "kategorie": "Drucksensoren BMP-Serie, Beschleunigungssensoren, MEMS-Gyros",
        "kam": "Herr Dr. Hans-Juergen Schaefer (Director Sensor Sales OEM)",
        "qmb": "Frau Dr. Karin Maier",
        "umsatz_eur_mio": 18,
        "anteil_buchung": "8 %",
        "kritikalitaet": "B (single-source BMP-390 fuer BMS-12 HV-Pack-Drucksensorik)",
        "id": "REA-L-BOS",
    },
    "TEX": {
        "full": "Texas Instruments Deutschland GmbH",
        "addr": "Haggertystrasse 1, 85356 Freising",
        "kategorie": "Analog/Digital-ICs, SerDes (FPD-Link), DC/DC-Wandler",
        "kam": "Herr Frank Donovan (Strategic Account Manager DACH)",
        "qmb": "Frau Dr. Heike Wagner",
        "umsatz_eur_mio": 38,
        "anteil_buchung": "16 %",
        "kritikalitaet": "B (Power-Stage und Sensor-Front-End ADAS-V4D)",
        "id": "REA-L-TEX",
    },
}

# Indirect / C-parts / passive / MRO suppliers (key by short)
RAHMEN_SUP = {
    "BUE": {
        "full": "Buerklin Elektronik GmbH",
        "addr": "Schillerstrasse 41, 85737 Ismaning",
        "kategorie": "Passive Elektronikbauteile (Widerstaende, Kondensatoren, Induktivitaeten)",
        "volumen_eur_mio": 4.2,
        "kam": "Herr Tobias Wagner",
        "warengruppe": "Passive Bauelemente",
        "kritikalitaet": "C (Verteildistribution, dual-source mit Wuerth Industrie / Yageo)",
    },
    "LAP": {
        "full": "Lapp Gruppe (U.I. Lapp GmbH)",
        "addr": "Schulze-Delitzsch-Strasse 25, 70565 Stuttgart",
        "kategorie": "Kabel und Leitungen, Anschluss- und Verbindungstechnik (OELFLEX-Serie)",
        "volumen_eur_mio": 3.1,
        "kam": "Frau Sabine Knopf",
        "warengruppe": "Kabelkonfektion / Steuerleitungen",
        "kritikalitaet": "C (umfangreiche Zweitquelle Helukabel)",
    },
    "RSC": {
        "full": "RS Components GmbH",
        "addr": "Hessenring 13b, 64546 Moerfelden-Walldorf",
        "kategorie": "MRO-Materialien, C-Teile, Laborbedarf, Mess- und Pruefmittel",
        "volumen_eur_mio": 2.4,
        "kam": "Herr Andreas Klein",
        "warengruppe": "MRO / indirekter Bedarf",
        "kritikalitaet": "C",
    },
    "GRA": {
        "full": "Grainger Deutschland GmbH",
        "addr": "Friedrichstrasse 191, 10117 Berlin",
        "kategorie": "Werkzeuge, Betriebsmittel, persoenliche Schutzausruestung, SMD-Hilfsstoffe",
        "volumen_eur_mio": 1.8,
        "kam": "Frau Maren Hoffmann",
        "warengruppe": "Werkzeuge / PSA / Betriebsmittel",
        "kritikalitaet": "C",
    },
    "TEC": {
        "full": "TE Connectivity Germany GmbH",
        "addr": "Ampere strasse 12-14, 64625 Bensheim",
        "kategorie": "Steckverbinder (MATEnet, AMP-Familie), Crimp-Kontakte, Bordnetz",
        "volumen_eur_mio": 11.6,
        "kam": "Herr Dr. Bernd Hofmann",
        "warengruppe": "Steckverbinder / Interconnect",
        "kritikalitaet": "B (kritische Bordnetz-Steckverbinder ECU-900, LightCtrl-7)",
    },
    "WUE": {
        "full": "Wuerth Industrie Service GmbH & Co. KG",
        "addr": "Drillberg, 97980 Bad Mergentheim",
        "kategorie": "Verbindungselemente / C-Teile (Schrauben, Muttern, Kleinteile, Kanban-Belieferung)",
        "volumen_eur_mio": 5.7,
        "kam": "Frau Andrea Schmitt",
        "warengruppe": "C-Teile / Verbindungselemente (CPS-Kanban)",
        "kritikalitaet": "C (vollintegrierte Kanban-Belieferung Werk Heilbronn / Katowice)",
    },
}

PRODUKT_LONG = {
    "ICP-3": "InfoConnect Pro (Infotainment-Modul ICP-3, ARM Cortex-A78, 3 Displays)",
    "BMS-12": "BatteryMS-12 (Batteriemanagementsystem fuer 800-V-Plattformen, ASIL-D)",
    "ADAS-V4D": "ADAS-V4D (Level-2/3 Radar-Fusion-Steuergeraet, Nvidia Orin SoC)",
    "ECU-900": "ECU-900 (Powertrain-Steuergeraet Gen3, Infineon AURIX TC39x)",
    "LightCtrl-7": "LightCtrl-7 (Matrix-LED Steuermodul, 1024 Pixel, GMSL2)",
}

# ---- helpers ----------------------------------------------------------------
def sig(name_a, role_a, comp_a, name_b, role_b, comp_b, date_str="14. Maerz 2023"):
    return signatures(name_a, role_a, comp_a, name_b, role_b, comp_b,
                      place="Stuttgart", date_str_=date_str)


def addr_block(sup_key):
    s = SUP[sup_key]
    return (
        f"Lieferant:\n{s['full']}\n{s['addr']}\n"
        f"Lieferanten-Nr. Brennhagen: {s['id']}\n"
        f"Kategorie / Warengruppe: {s['kategorie']}\n"
        f"Ansprechpartner Lieferant: {s['kam']}\n"
        f"Qualitaetsverantwortlich Lieferant: {s['qmb']}\n\n"
        f"Auftraggeberin:\n{R['name']}, {R['addr']}\n"
        f"Strategischer Einkauf Halbleiter: Tobias Lange (Lead Buyer)\n"
        f"Head of Direct Materials: Sabine Hartmann\n"
        f"Supplier Quality: Andreas Kaufmann (Head of Supplier Quality, Personalunion Werk-Q REG)\n"
        f"Risk Manager: Christine Berger (Supplier Risk)\n"
        f"Vorstandsverantwortung: Dr. Robert Walther (CPO, Operations) - Berichtslinie an COO Dr. Thomas Weber"
    )


# ---- 1. Lieferantenaudit (VDA 6.3) -----------------------------------------
def lieferanten_audit(fname, sup_key, jahr, quartal):
    s = SUP[sup_key]
    auditnr = f"VDA63-{jahr}-{sup_key}-{quartal}"
    datum = {"Q1": f"7.-9. Februar {jahr}",
             "Q2": f"14.-16. Mai {jahr}",
             "Q3": f"22.-24. August {jahr}",
             "Q4": f"6.-8. November {jahr}"}[quartal]
    score = {"Q1": 86, "Q2": 88, "Q3": 91, "Q4": 89}[quartal]
    stufe = "A" if score >= 90 else ("AB" if score >= 80 else "B")
    write_doc(BASE / fname, H,
        f"Lieferantenaudit VDA 6.3 - {s['full']} - {quartal} {jahr}",
        subtitle=f"Audit-Nr. {auditnr} - Process Audit Serienlieferung",
        confidential=True,
        sections=[
            ("Audit-Stammdaten", addr_block(sup_key)),
            ("Audit-Eckdaten",
             [["Feld", "Wert"],
              ["Audit-Nummer", auditnr],
              ["Auditierte Organisation", s['full']],
              ["Auditort", s['addr']],
              ["Audit-Zeitraum", datum],
              ["Audit-Norm", "VDA 6.3 (3. Ausgabe, Juli 2016) - Process Audit Serie"],
              ["Audit-Typ", "Geplantes Wiederholungsaudit (Tier-1 Lieferant Auto-Elektronik)"],
              ["Lead-Auditor (Brennhagen)", "Andreas Kaufmann (Head of Supplier Quality, VDA 6.3 zertifiziert)"],
              ["Co-Auditor", "Christine Berger (Supplier Risk Manager)"],
              ["Audit-Sprache", "Deutsch / Englisch"],
              ["Audit-Score", f"{score} von 100 Punkten - Einstufung Stufe {stufe}"]]),
            ("Bewertete Prozessgruppen (VDA 6.3 P2-P7)",
             [["Prozess", "Pmax", "Punkte", "EG (Erfuellungsgrad)"],
              ["P2 - Projektmanagement", "100", str(score-2), f"{score-2}%"],
              ["P3 - Planung Produktentwicklung", "100", str(score-1), f"{score-1}%"],
              ["P4 - Realisierung Produktentwicklung", "100", str(score), f"{score}%"],
              ["P5 - Lieferantenmanagement", "100", str(score-3), f"{score-3}%"],
              ["P6 - Prozessanalyse Produktion", "100", str(score+1), f"{score+1}%"],
              ["P7 - Kundenbetreuung / Reklamation", "100", str(score-2), f"{score-2}%"]]),
            ("Wesentliche Feststellungen",
             ("list", [
                 f"Auditierter Standort fuer Lieferungen an Brennhagen: {s['addr']} "
                 f"(Fertigung Wafer/Backend) sowie Hub Logistikzentrum Deutschland.",
                 f"Kritikalitaetsstufe in der Brennhagen-Lieferantenbewertung: {s['kritikalitaet']}.",
                 f"Warengruppen-Volumen p.a. (Konzernebene 2023, Ist): rd. {s['umsatz_eur_mio']} Mio. EUR "
                 f"({s['anteil_buchung']} der Halbleiter-Direktbeschaffung).",
                 "Keine kritischen K.O.-Fragen ausgeloest; keine Major Non-Conformities.",
                 "Minor Findings: 2 Beobachtungen zur PPAP-Dokumentationstiefe (PSW-Revisionshistorie unvollstaendig), "
                 "1 Hinweis zur Frequenz der internen Capability-Studien (Cpk-Trend monatlich statt quartalsweise).",
                 "Lieferant verfuegt ueber gueltige IATF 16949 Zertifizierung (rezertifiziert in 2023), "
                 "ISO 14001 sowie ISO 27001; Pruefurkunden liegen vor.",
                 "BCM-Plan (Business Continuity) wurde vorgelegt; Alternativ-Fab-Out fuer A-Teile dokumentiert."
             ])),
            ("Massnahmen und Wiedervorlage",
             [["Massnahme", "Verantwortlich", "Termin"],
              ["Nachreichung PPAP-Revisionsnachweise (PSW Level 3) fuer drei A-Teile",
               f"{s['qmb']} (Lieferant)", f"30 Tage nach Auditbericht"],
              ["Einfuehrung monatlicher Cpk-Trend-Report im Lieferanten-Portal SupplyOn",
               f"{s['qmb']} (Lieferant) / Andreas Kaufmann (Brennhagen)", "60 Tage"],
              ["Wiedervorlage / Follow-up Desk-Audit (remote)", "Christine Berger (Brennhagen)", "90 Tage"]]),
            ("Audit-Ergebnis / Freigabe",
             f"Der auditierte Standort wird in Stufe {stufe} eingestuft und behaelt den Status "
             f"»freigegebener Serienlieferant« mit Auflagen wie oben aufgelistet. Naechstes Regelaudit: "
             f"4. Quartal des Folgejahres. Bei Eintritt einer Lieferengpass-Eskalation oder einer 8D-Eskalationsstufe >= 2 "
             f"erfolgt ein anlassbezogenes Sonderaudit ausserhalb des Regelplans."),
            ("Verteiler",
             ("list", [
                 "Dr. Robert Walther (CPO, Vorstand Operations)",
                 "Sabine Hartmann (Head of Direct Materials)",
                 "Tobias Lange (Strategischer Einkauf Halbleiter)",
                 "Andreas Kaufmann (Head of Supplier Quality)",
                 "Christine Berger (Supplier Risk Manager)",
                 f"Lieferant: {s['kam']}, {s['qmb']}"
             ])),
            ("Unterschriften",
             sig("Andreas Kaufmann", "Head of Supplier Quality / Lead-Auditor", R['name'],
                 s['qmb'].split('(')[0].strip(), "Qualitaetsleitung", s['full'],
                 date_str=f"Stuttgart / Audit-Ort, {datum.split('-')[1] if '-' in datum else datum}")),
        ])


# ---- 2. Allokationsvereinbarung Halbleitermangel 2021 -----------------------
def allokationsvereinbarung(fname, sup_key, jahr=2021):
    s = SUP[sup_key]
    write_doc(BASE / fname, H,
        f"Allokationsvereinbarung Halbleitermangel {jahr} - {s['full']}",
        subtitle="Sondervereinbarung zur Sicherstellung der Serienversorgung waehrend der globalen Halbleiterkrise",
        confidential=True,
        sections=[
            ("Vertragsparteien", addr_block(sup_key)),
            ("Praeambel",
             f"Die globale Halbleiterkrise hat im Jahr {jahr} zu erheblichen Lieferengpaessen gefuehrt. "
             f"Die Parteien beabsichtigen, mit dieser Sondervereinbarung die Versorgung der Brennhagen-Serienprogramme "
             f"(ICP-3, ECU-900, ADAS-V4D, BMS-12, LightCtrl-7) waehrend des Allokations-Zeitraums sicherzustellen "
             f"und gegenseitige Eskalationspflichten zu definieren. Diese Vereinbarung ergaenzt den bestehenden "
             f"Rahmenliefervertrag und den Long-Term Agreement (LTA), bleibt im Konflikt jedoch vorrangig."),
            ("§ Vereinbarungen",
             ("clauses", [
                 ("§ 1 Allokationsmenge und Verbindlichkeit",
                  [f"{s['full']} sichert {R['name']} eine garantierte Mindest-Allokation in Hoehe von "
                   f"100 % des im Forecast (12-Monats-Rolling) hinterlegten Volumens zu. "
                   f"Basis: Forecast-Stand 30.6.{jahr}, ueberprueft monatlich im Allocation-Call.",
                   f"Im Falle Knappheit gelten die nachstehenden Prioritaetsklassen: Klasse A "
                   f"(Serienprogramme mit aktiver OEM-SOP-Bindung) wird vor Klasse B (Ersatzteilbedarf) "
                   f"und Klasse C (Sample- und Entwicklungsbedarf) bedient.",
                   f"Bei Unterlieferung > 5 % der zugesicherten Menge greift die Eskalationspflicht "
                   f"binnen 48 Stunden gegenueber CPO Dr. Robert Walther."]),
                 ("§ 2 Preisstellung waehrend der Allokation",
                  [f"Die LTA-Preisstellung bleibt grundsaetzlich erhalten. Eine Allocation-Surcharge "
                   f"von max. 8 % auf die Standardkonditionen ist fuer maximal sechs Monate zulaessig "
                   f"und kann nur nach schriftlicher Zustimmung von Dr. Robert Walther (CPO) angewandt werden.",
                   f"Spot-Mengen ausserhalb der Allokation werden ausschliesslich zu Spotmarktpreis +5 % Handling abgerechnet."]),
                 ("§ 3 Transparenz und Reporting",
                  [f"Wochen-Update jeden Donnerstag 16:00 Uhr (Allocation Steering Call), Teilnehmer: "
                   f"Tobias Lange (Brennhagen Lead Buyer), {s['kam']}.",
                   f"Datenformat: standardisierte Allokationsmatrix (Excel, Vorlage Brennhagen RSK-AM-001) ",
                   f"mit Aufschluesselung nach Brennhagen-Werk (REG Heilbronn, RPL Katowice, RCZ Brno, RHU Gyoer)."]),
                 ("§ 4 Laufzeit und Beendigung",
                  [f"Diese Vereinbarung gilt rueckwirkend ab 1.7.{jahr} und endet automatisch, "
                   f"wenn das Branchen-Allokationsverhaeltnis (Quelle: SIA / WSTS) ueber drei Monate "
                   f"in Folge < 1,1 liegt, spaetestens jedoch zum 31.12.{jahr+2}.",
                   f"Eine vorzeitige Beendigung bedarf der Schriftform und der Zustimmung beider CPOs."]),
             ])),
            ("Unterschriften",
             sig("Dr. Robert Walther", "Vorstand / CPO Operations", R['name'],
                 s['kam'].split('(')[0].strip(), "Key Account Manager Automotive", s['full'],
                 date_str=f"Stuttgart / Muenchen, 21. September {jahr}")),
        ])


# ---- 3. Langfristvertrag LTA -------------------------------------------------
def lta(fname, sup_key, jahr=2023):
    s = SUP[sup_key]
    write_doc(BASE / fname, H,
        f"Long-Term Agreement (LTA) - {s['full']} - {jahr}-{jahr+3}",
        subtitle=f"Langfristlieferzusage und Preisbindung fuer Halbleiterkomponenten",
        confidential=True,
        sections=[
            ("Vertragsparteien", addr_block(sup_key)),
            ("1. Rahmenbedingungen",
             f"Die Parteien vereinbaren mit diesem Long-Term Agreement (»LTA«) eine Mehrjahres-Lieferbeziehung "
             f"fuer die in Anhang 1 aufgefuehrten Halbleiterkomponenten der Warengruppe »{s['kategorie']}«. "
             f"Vertragslaufzeit: 1. Januar {jahr} bis 31. Dezember {jahr+3} (36 Monate) mit Verlaengerungsoption "
             f"um jeweils 12 Monate bei beidseitiger Erklaerung spaetestens 9 Monate vor Vertragsende."),
            ("2. Volumen und Verbindlichkeit",
             [["Jahr", "Min-Volumen (Stueck, kumuliert ueber Komponenten)", "Wertvolumen (Mio. EUR, indikativ)"],
              [str(jahr), "4.200.000", f"{s['umsatz_eur_mio']}"],
              [str(jahr+1), "4.600.000", f"{int(s['umsatz_eur_mio']*1.08)}"],
              [str(jahr+2), "5.000.000", f"{int(s['umsatz_eur_mio']*1.15)}"],
              [str(jahr+3), "5.300.000", f"{int(s['umsatz_eur_mio']*1.20)}"]]),
            ("3. Preisanpassungsmechanik",
             "Die Stueckpreise gemaess Anhang 2 gelten als Festpreise. Eine Preisanpassung ist einmal "
             "jaehrlich (Jahrespreisverhandlung Q4) zulaessig und wird auf Basis der Indizes Destatis GP "
             "Reihe 24 (Industrie-Erzeugerpreise Elektronik), WSTS Halbleitermarkt-Index sowie der "
             "tatsaechlichen Wafer-Capex-Auslastung des Lieferanten verhandelt. Pass-through-Reglung fuer "
             "Energie- und Logistikkosten gemaess gesondertem Anhang 3."),
            ("4. Versorgungssicherheit und BCM",
             ("list", [
                 "Lieferant verpflichtet sich zur Vorhaltung eines Sicherheitsbestands von 6 Wochen "
                 "Forward-Bedarf am Distributionszentrum (Bonded Stock).",
                 "Aufbau eines zweiten Wafer-Fab-Outs fuer alle A-Teile bis spaetestens 30.6.{jahr_plus2}.".replace("{jahr_plus2}", str(jahr+2)),
                 "Quartalsweiser BCM-Report an Christine Berger (Supplier Risk Manager Brennhagen).",
                 f"Eskalationsweg bei Lieferengpass: {s['kam']} -> Tobias Lange (Brennhagen Lead Buyer) -> "
                 "Sabine Hartmann (Head of Direct Materials) -> Dr. Robert Walther (CPO).",
             ])),
            ("5. Qualitaet und Pflichten",
             "Es gelten die zwischen den Parteien geschlossene Qualitaetssicherungsvereinbarung (QSV) "
             "in der jeweils gueltigen Fassung, IATF 16949, VDA 6.3 Auditregime sowie die Bestimmungen "
             "des Brennhagen Code of Conduct (Stand 2023). Reklamationen werden im 8D-Verfahren bearbeitet; "
             "Ziel-Reaktionszeit auf D3 < 24 h, D8-Abschluss < 30 Kalendertage."),
            ("6. LkSG / Nachhaltigkeit",
             "Lieferant bestaetigt die Einhaltung der Sorgfaltspflichten gemaess deutschem Lieferkettengesetz "
             "(LkSG) sowie die jaehrliche Lieferanten-Selbstauskunft (SAQ ueber EcoVadis, Mindest-Score 65). "
             "Verpflichtung zur stufenweisen Umstellung auf erneuerbare Energie (Scope 1+2): "
             "30 % bis 2025, 100 % bis 2030, kohaerent mit Brennhagen Carbon-Neutrality-Roadmap 2030."),
            ("7. Vertraulichkeit, Haftung, Schlussbestimmungen",
             "NDA gemaess Standard-NDA Brennhagen in der Fassung vom 15.3.2022. Haftung gemaess Brennhagen-AEB "
             "Stand 1.1.2023 in Verbindung mit DIN 9000-Reihe. Gerichtsstand: Stuttgart, deutsches Recht "
             "unter Ausschluss UN-Kaufrecht (CISG). Sprachfassungen Deutsch und Englisch; im Konfliktfall "
             "geht die deutsche Fassung vor."),
            ("Unterschriften",
             sig("Dr. Robert Walther", "Vorstand / CPO Operations", R['name'],
                 s['kam'].split('(')[0].strip(), "Key Account Manager Automotive", s['full'],
                 date_str=f"Stuttgart, 18. Dezember {jahr-1}")),
        ])


# ---- 4. Entwicklungsprogramm -------------------------------------------------
def entwicklungsprogramm(fname, sup_key, jahr=2023):
    s = SUP[sup_key]
    write_doc(BASE / fname, H,
        f"Lieferantenentwicklungsprogramm {jahr} - {s['full']}",
        subtitle="Supplier Development Plan / SDP - Brennhagen Konzern-Einkauf",
        confidential=True,
        sections=[
            ("Programmrahmen", addr_block(sup_key)),
            ("Zielsetzung",
             f"Auf Basis der Lieferantenbewertung {jahr-1} sowie der VDA 6.3-Auditergebnisse {jahr-1}-{jahr} "
             f"definiert dieses Lieferantenentwicklungsprogramm konkrete Massnahmen, um den Lieferanten "
             f"{s['full']} (Brennhagen-Lieferanten-Nr. {s['id']}) als strategischen Partner der Kategorie "
             f"»{s['kategorie']}« weiterzuentwickeln. Programmzeitraum: Kalenderjahr {jahr}, "
             f"Status-Reviews Q1, Q2, Q3, Abschlussreview Dezember {jahr}."),
            ("Massnahmenplan",
             [["Nr.", "Massnahme", "Verantwortlich (Brennhagen)", "Verantwortlich (Lieferant)", "Termin"],
              ["1", "Einfuehrung Cpk-Trend-Monitoring monatlich (SupplyOn-Portal)",
               "Andreas Kaufmann (Head SQE)", s['qmb'], "31.3."+str(jahr)],
              ["2", "BCM-Plan-Update mit Second-Source-Fab-Out fuer alle A-Teile",
               "Christine Berger (Risk Mgr)", s['kam'], "30.6."+str(jahr)],
              ["3", "Reduktion 8D-Reaktionszeit D3 auf < 24 h (von 36 h)",
               "Andreas Kaufmann", s['qmb'], "30.6."+str(jahr)],
              ["4", "ECO-Anbindung: digitale CAR (Corrective Action Request) ueber SupplyOn",
               "Tobias Lange (Lead Buyer)", s['kam'], "30.9."+str(jahr)],
              ["5", "EcoVadis-Score-Steigerung auf >= 72 (Stand 2022: 64)",
               "Christine Berger", s['qmb'], "31.12."+str(jahr)],
              ["6", "Pilot Direkt-Cross-Docking REG Heilbronn (Reduktion Bestand -25 %)",
               "Sabine Hartmann (Head Direct)", s['kam'], "31.12."+str(jahr)]]),
            ("KPI-Zielwerte",
             [["KPI", "Stand "+str(jahr-1), "Ziel "+str(jahr)],
              ["Liefertreue (OTD)", "94,2 %", ">= 98,0 %"],
              ["Liefermengentreue (OQD)", "96,8 %", ">= 99,0 %"],
              ["Reklamationsquote (PPM)", "82", "<= 40"],
              ["8D-Reaktionszeit D3 (h)", "36", "< 24"],
              ["VDA 6.3 Audit-Score", "86", ">= 90"],
              ["EcoVadis-Score", "64", ">= 72"]]),
            ("Governance",
             ("list", [
                 "Monatlicher SDP-Steering-Call (jeweils 1. Mittwoch im Monat, 09:30 Uhr).",
                 "Quartalsweises Executive Review mit Dr. Robert Walther (CPO) und Geschaeftsleitung Lieferant.",
                 "Eskalationspfad bei Off-Track: Tobias Lange -> Sabine Hartmann -> Dr. Robert Walther.",
                 "Programmabschluss-Review: 15.12."+str(jahr)+", gemeinsamer Sign-off durch CPO und Lieferant.",
             ])),
            ("Sign-off",
             sig("Sabine Hartmann", "Head of Direct Materials", R['name'],
                 s['kam'].split('(')[0].strip(), "Key Account Manager Automotive", s['full'],
                 date_str=f"Stuttgart, 16. Januar {jahr}")),
        ])


# ---- 5. REACH / RoHS Konformitaetserklaerung ---------------------------------
def reach_rohs(fname, sup_key, jahr=2023):
    s = SUP[sup_key]
    write_doc(BASE / fname, H,
        f"REACH- und RoHS-Konformitaetserklaerung - {s['full']} - {jahr}",
        subtitle=f"Erklaerung gemaess VO (EG) Nr. 1907/2006 (REACH) und Richtlinie 2011/65/EU (RoHS 3)",
        sections=[
            ("Erklaerende",
             f"{s['full']}\n{s['addr']}\nLieferanten-Nr. Brennhagen: {s['id']}\n"
             f"Verantwortliche Person Lieferant: {s['qmb']}\n"
             f"Gegenstand der Erklaerung: alle an {R['name']} gelieferten Komponenten der Warengruppe "
             f"»{s['kategorie']}«, Bezugsjahr {jahr}."),
            ("REACH-Erklaerung",
             f"Hiermit bestaetigt {s['full']} verbindlich, dass alle an Brennhagen gelieferten Komponenten "
             f"die Anforderungen der Verordnung (EG) Nr. 1907/2006 (REACH) in der derzeit gueltigen Fassung "
             f"erfuellen. Die Kandidatenliste der besonders besorgniserregenden Stoffe (SVHC) wurde mit Stand "
             f"per 1.7.{jahr} (235 Eintraege) abgeglichen. SVHC-Stoffe oberhalb der Schwellenwerte 0,1 Gew.-% "
             f"sind nicht in den gelieferten Artikeln enthalten bzw. werden im SCIP-Eintrag (ECHA) gefuehrt "
             f"und Brennhagen vorab schriftlich angezeigt."),
            ("RoHS-Erklaerung",
             f"Saemtliche an Brennhagen gelieferten Komponenten sind konform zur Richtlinie 2011/65/EU (RoHS) "
             f"einschliesslich Erweiterung 2015/863 (RoHS 3 - vier Phthalate). Die Grenzwerte "
             f"fuer Blei (0,1 %), Quecksilber (0,1 %), Cadmium (0,01 %), Chrom VI (0,1 %), PBB (0,1 %), "
             f"PBDE (0,1 %), DEHP (0,1 %), BBP (0,1 %), DBP (0,1 %), DIBP (0,1 %) werden eingehalten. "
             f"Etwaige Ausnahmen gemaess Anhang III/IV der Richtlinie sind in der Datenblatt-Sammlung "
             f"(IPC-1752A Class D Brennhagen-Format) im Detail aufgefuehrt."),
            ("Weitere stoffliche Konformitaeten",
             ("list", [
                 "Konfliktmineralien: Konformitaetsbestaetigung gemaess EU-VO 2017/821 und RMI/RBA "
                 "Conflict Minerals Reporting Template (CMRT 6.31), eingereicht 15.5."+str(jahr)+".",
                 "POP-Verordnung (EU) 2019/1021: keine Persistent Organic Pollutants oberhalb Grenzwert.",
                 "China RoHS 2 (GB/T 26572): erweiterte Kennzeichnung erfolgt fuer Lieferungen an "
                 "RCN Shanghai.",
                 "California Proposition 65: Warnhinweise bei Bedarf, eigene Auflistung Anhang B.",
                 "Halogen-frei (IEC 61249-2-21): bestaetigt fuer alle Gehaeuse und Vergussmaterialien.",
             ])),
            ("Aenderungsmanagement",
             "Bei Aenderungen an Material- oder Prozesszusammensetzung wird Brennhagen (Andreas Kaufmann, "
             "Head of Supplier Quality) mindestens 90 Kalendertage vor Implementierung schriftlich "
             "informiert. Die Anzeige- und Genehmigungspflicht (PCN/PDN-Prozess) ist Bestandteil der "
             "Qualitaetssicherungsvereinbarung (QSV)."),
            ("Gueltigkeit",
             f"Diese Erklaerung gilt fuer das Kalenderjahr {jahr} und wird bis spaetestens 31.1.{jahr+1} "
             f"jaehrlich erneuert. Bei wesentlichen regulatorischen Aenderungen erfolgt ad-hoc-Update."),
            ("Unterschrift Lieferant",
             sig(s['qmb'].split('(')[0].strip(), "Qualitaetsverantwortliche / REACH-Beauftragte", s['full'],
                 "Andreas Kaufmann", "Head of Supplier Quality", R['name'],
                 date_str=f"Werk Lieferant / Stuttgart, 24. Januar {jahr}")),
        ])


# ---- 6. Rahmenvertrag indirekte / passive Lieferanten ------------------------
def rahmenvertrag_indirekt(fname, sup_key, jahr=2022):
    s = RAHMEN_SUP[sup_key]
    write_doc(BASE / fname, H,
        f"Rahmenliefervertrag - {s['full']} - {s['warengruppe']}",
        subtitle=f"Konzernweiter Rahmenvertrag {jahr}-{jahr+2}",
        confidential=False,
        sections=[
            ("Vertragsparteien",
             f"Auftraggeberin:\n{R['name']}, {R['addr']}, vertreten durch Dr. Robert Walther (Vorstand / CPO Operations) "
             f"und Frank Wendel (Head of Indirect / MRO).\n\n"
             f"Lieferant:\n{s['full']}, {s['addr']}, vertreten durch {s['kam']} (Key Account Manager).\n\n"
             f"Warengruppe: {s['kategorie']}\n"
             f"Geschaetztes Jahresvolumen Konzern (Mio. EUR): {s['volumen_eur_mio']}\n"
             f"Kritikalitaetsstufe Brennhagen: {s['kritikalitaet']}\n"
             f"Geltungsbereich: alle Brennhagen-Konzerngesellschaften (REG Heilbronn, RSG Muenchen, "
             f"RPL Katowice, RCZ Brno, RHU Gyoer; RCN Shanghai nur fuer Re-Export-Faelle)."),
            ("Vertragsklauseln",
             ("clauses", [
                 ("§ 1 Vertragsgegenstand und Geltung",
                  [f"Der Lieferant liefert Brennhagen die in Anlage 1 katalogisierten Artikel der Warengruppe "
                   f"»{s['warengruppe']}«. Einzelbestellungen erfolgen ueber das Brennhagen-eProcurement-System "
                   f"(SAP Ariba / Coupa) auf Basis dieses Rahmenvertrages.",
                   f"Dieser Vertrag ist nicht-exklusiv. Brennhagen behaelt sich Dual-/Multi-Sourcing vor. "
                   f"Mindestabnahmemengen werden nicht zugesichert; Plan-Volumina dienen Forecast-Zwecken.",
                   f"Vertragslaufzeit: 1.1.{jahr} - 31.12.{jahr+2} mit Verlaengerungsoption um jeweils 12 Monate "
                   f"bei beidseitiger Erklaerung 6 Monate vor Vertragsende."]),
                 ("§ 2 Konditionen und Preise",
                  ["Preisstellung gemaess Preisliste Anhang 2 (DDP Werk Heilbronn, Incoterms 2020).",
                   "Preisbindung 12 Monate; jaehrliche Preisverhandlung im Q4 (Jahrespreisverhandlung).",
                   "Zahlungsziel: 60 Tage netto ab Rechnungseingang; 2 % Skonto bei Zahlung binnen 14 Tagen.",
                   "Mengenrabattstaffel gemaess Anhang 2; Bonus-Regelung 1,0 % bei Erreichen Konzernvolumen >= 110 %."]),
                 ("§ 3 Logistik und Lieferung",
                  [f"Standard-Lieferzeiten: Lagerware 48 h, Sonderbeschaffung 10 Arbeitstage.",
                   f"Lieferort: SAP-Werks-Adressen REG/RPL/RCZ/RHU; Konsignations-/Kanban-Modell fuer C-Teile "
                   f"(insbesondere CPS-Kanban WUE und MRO-Schrank RSC).",
                   f"Versandkostenpauschale: frei Haus ab Bestellwert 250 EUR; darunter 9,50 EUR Pauschale.",
                   f"OTD-Ziel: >= 98 %; Reporting monatlich an Frank Wendel (Brennhagen)."]),
                 ("§ 4 Qualitaet und Reklamation",
                  ["RoHS-/REACH-Konformitaet ist Liefervoraussetzung; jaehrliche Konformitaetserklaerung.",
                   "Reklamationen werden ueber das Brennhagen Q-Portal (SupplyOn) abgewickelt.",
                   "8D-Pflicht ab Stufe 2-Reklamation (kunden- oder serienkritische Faelle)."]),
                 ("§ 5 LkSG, Nachhaltigkeit, Schlussbestimmungen",
                  [f"Lieferant verpflichtet sich zur Einhaltung des Brennhagen Code of Conduct (Stand {jahr}) "
                   f"sowie der Sorgfaltspflichten gemaess deutschem LkSG. Jaehrliche SAQ ueber EcoVadis.",
                   f"Es gelten die AEB Brennhagen Stand 1.1.{jahr}. Gerichtsstand Stuttgart, deutsches Recht "
                   f"unter Ausschluss UN-Kaufrecht."]),
             ])),
            ("Unterschriften",
             sig("Frank Wendel", "Head of Indirect / MRO", R['name'],
                 s['kam'].split('(')[0].strip(), "Key Account Manager", s['full'],
                 date_str=f"Stuttgart, 11. November {jahr-1}")),
        ])


# ---- 7. RFQ ------------------------------------------------------------------
def rfq(fname, warengruppe_lang, warengruppe_kurz, jahr=2024):
    write_doc(BASE / fname, H,
        f"Anfrage (RFQ) - {warengruppe_lang} {jahr}",
        subtitle=f"Request for Quotation - Strategischer Einkauf Brennhagen Elektronik AG",
        confidential=True,
        sections=[
            ("Anfragestellung",
             f"Auftraggeberin:\n{R['name']}, {R['addr']}\n"
             f"Anfrage-Nr.: REA-RFQ-{jahr}-{warengruppe_kurz}\n"
             f"Anfrage-Datum: 18. Januar {jahr}\n"
             f"Rueckmeldefrist (verbindliches Angebot): 28. Februar {jahr}, 17:00 Uhr MEZ\n\n"
             f"Verantwortlich Einkauf: Tobias Lange (Strategischer Einkauf Halbleiter) bzw. "
             f"Sabine Hartmann (Head of Direct Materials)\n"
             f"In Kopie: Dr. Robert Walther (CPO), Christine Berger (Supplier Risk), "
             f"Andreas Kaufmann (Head of Supplier Quality)"),
            ("Beschaffungsumfang",
             f"Brennhagen fragt fuer die Programmzeitraeume {jahr} bis {jahr+3} ein verbindliches Angebot zur "
             f"Belieferung der Warengruppe »{warengruppe_lang}« an. Belieferungsziele: Werke REG Heilbronn, "
             f"RPL Katowice, RCZ Brno und RHU Gyoer. Die detaillierte Stueckliste (BOM) inklusive Plan-Volumina, "
             f"Spezifikationen, Pruefanforderungen und Verpackungsvorgaben liegt als Anlage 1 zu dieser Anfrage bei "
             f"(zugaenglich nur ueber das Brennhagen-eRFQ-Portal SupplyOn nach NDA-Unterzeichnung)."),
            ("Plan-Volumen indikativ",
             [["Jahr", "Volumen kumuliert (Stueck/Jahr)", "Wertvolumen (Mio. EUR, indikativ)"],
              [str(jahr), "rd. 1,8 Mio.", "rd. 4,2"],
              [str(jahr+1), "rd. 2,2 Mio.", "rd. 5,1"],
              [str(jahr+2), "rd. 2,5 Mio.", "rd. 5,8"],
              [str(jahr+3), "rd. 2,6 Mio.", "rd. 6,0"]]),
            ("Anforderungen an das Angebot",
             ("list", [
                 "Verbindliche Stueckpreise EXW und DDP Werk Heilbronn (Incoterms 2020).",
                 "Preisstaffelung nach Abrufmenge, Festpreis-Zusage 24 Monate.",
                 "Liefertreue-Zusage (OTD) >= 98 %, OQD >= 99 %.",
                 "Aussagefaehiger BCM-Plan (mind. zweiter Fertigungsstandort fuer A-Teile).",
                 "Vollumfaengliche PPAP Level 3 fuer alle Erstmuster bis 30.9.{jahr}.".replace("{jahr}", str(jahr)),
                 "Sustainability: EcoVadis-Score >= 65, LkSG-Selbstauskunft beigefuegt.",
                 "Zertifikate: IATF 16949, ISO 14001, ISO 27001 oder TISAX (sofern softwarenah).",
                 "Konzeptvorschlag Konsignations-/Kanban-Belieferung sofern wirtschaftlich.",
             ])),
            ("Bewertungsmatrix (Punkte 100)",
             [["Kriterium", "Gewichtung"],
              ["Preis (TCO)", "40 %"],
              ["Lieferfaehigkeit / BCM", "20 %"],
              ["Qualitaet (Audit-Historie, PPM)", "15 %"],
              ["Innovation / Roadmap-Fit", "10 %"],
              ["Nachhaltigkeit (EcoVadis, Scope 1+2)", "10 %"],
              ["Vertrags- und Compliance-Reife", "5 %"]]),
            ("Verfahrenshinweise",
             "Die Anfrage richtet sich an die im Anhang 3 aufgefuehrten 6 vor-qualifizierten Lieferanten. "
             "Zwischenfragen sind ausschliesslich ueber das Q&A-Modul im eRFQ-Portal bis 14.2."+str(jahr)+" zu stellen. "
             "Nach Auswertung erfolgt eine Shortlist auf 2-3 Lieferanten und eine Verhandlungsrunde "
             "im April "+str(jahr)+"; Award-Entscheidung durch Einkaufsausschuss (CPO + CFO + COO) im Mai "+str(jahr)+"."),
            ("Unterschrift",
             sig("Tobias Lange", "Strategischer Einkauf", R['name'],
                 "Sabine Hartmann", "Head of Direct Materials", R['name'],
                 date_str=f"Stuttgart, 18. Januar {jahr}")),
        ])


# ---- 8. SPEC - Komponentenspezifikation -------------------------------------
def komponenten_spec(fname, produkt_key, sup_key, jahr=2023):
    s = SUP[sup_key]
    prod_lang = PRODUKT_LONG.get(produkt_key, produkt_key)
    # Component depends on supplier
    if sup_key == "INF":
        bauteil = "Mikrocontroller AURIX TC397 (32-bit, multi-core, ASIL-D)"
        partnr = "SAK-TC397XX-256F300S BD"
    elif sup_key == "NXP":
        bauteil = "CAN-FD Transceiver TJA1463 / S32G274A Gateway-Prozessor"
        partnr = "TJA1463ATKZ / S32G274AHA1VPB1"
    elif sup_key == "STM":
        bauteil = "STM32H7-Mikrocontroller (Cortex-M7, 480 MHz)"
        partnr = "STM32H753ZIT6"
    else:
        bauteil = "Komponente (siehe Datenblatt)"
        partnr = "n/a"
    write_doc(BASE / fname, H,
        f"Komponentenspezifikation - {prod_lang} - Lieferant {s['full']}",
        subtitle=f"Produkt-/Lieferant-spezifische Bauteilspezifikation - Spec-Nr. SPEC-{produkt_key}-{sup_key}-{jahr}",
        sections=[
            ("1. Produktidentifikation",
             f"Brennhagen-Produkt: {prod_lang}\n"
             f"Lieferant: {s['full']} ({s['addr']})\n"
             f"Bauteil-Beschreibung: {bauteil}\n"
             f"Lieferanten-Teilenummer: {partnr}\n"
             f"Brennhagen-Materialnr.: REA-{produkt_key}-{sup_key}-001\n"
             f"Stand: Revision 3.1, Freigabe 15. Mai {jahr} (Spec-Owner: Dr. Stefan Hoffmann, CTO; "
             f"Mit-Owner Hardware: Lars Wittmann, Lead Developer RSG Muenchen)"),
            ("2. Funktion und Einbauort",
             f"Das Bauteil wird im Modul {produkt_key} ({prod_lang}) zentral fuer die "
             f"Steuerungs-/Sensorik-/Schnittstellenfunktion eingesetzt. Stueckzahl pro Modul: 1 "
             f"({produkt_key}-Mainboard, Position U101). Einbauort: PCB-Layer 6, BGA-Footprint, "
             f"Pitch 0,8 mm. Thermische Anforderungen: max. T_J 150 degC bei T_amb 105 degC."),
            ("3. Elektrische und mechanische Spezifikation",
             [["Parameter", "Spezifikation", "Pruefverfahren"],
              ["Versorgungsspannung V_DD", "3,3 V +/- 5 %", "AEC-Q100 Class 2"],
              ["Stromaufnahme I_DD (typ.)", "240 mA bei 300 MHz", "Datenblatt Lieferant"],
              ["Betriebstemperatur", "-40 degC bis +125 degC (Grade 1)", "Burn-in 24 h @ 125 degC"],
              ["Gehaeuse", "LFBGA-292 (16x16 mm)", "JEDEC MS-034"],
              ["Lagerung Floor-Life", "MSL 3 (168 h nach Oeffnen)", "JEDEC J-STD-020"],
              ["Funktionssicherheit", "ISO 26262 ASIL-D-ready (Safety Manual v2.1)", "ISO 26262 Part 5/9"],
              ["EMV", "ISO 11452-4 / IEC 62132-3", "EMV-Labor REG Heilbronn"]]),
            ("4. Qualitaet und Pruefumfang",
             ("list", [
                 "PPAP Level 3 (full submission) bei Erstmuster und nach jeder PCN.",
                 "100 %-Endtest beim Lieferanten (Boundary-Scan, Funktionspattern).",
                 "AOI (Automated Optical Inspection) im SMD-Prozess REG/RPL.",
                 "ICT/Flying-Probe-Test im Brennhagen-Werk; FAI vor Serienfreigabe.",
                 "Rueckverfolgbarkeit: Lot-Nr.-basierte Traceability bis Wafer-Lot des Lieferanten.",
                 "Cpk-Anforderung kritische Parameter >= 1,67; CmK >= 2,0 bei Initial-Capability-Studie.",
             ])),
            ("5. Logistik und Verpackung",
             "Standardverpackung: Tape & Reel (4.000 Stueck/Reel), MSL-3-Trockenbeutel mit Indikatorkarte. "
             "Etikettierung gemaess VDA 4994 (DataMatrix-Code, GTIN). Versand DDP REG Heilbronn (Incoterms 2020), "
             "ESD-konforme Tray-Verpackung fuer Mustermengen. Sicherheitsbestand: 6 Wochen Forward-Bedarf "
             "im Bonded Warehouse Lieferant. Konsignationslager fuer Serie geplant ab Q4 "+str(jahr+1)+"."),
            ("6. Aenderungsmanagement",
             "Aenderungen am Bauteil (Material, Prozess, Wafer-Fab, Backend-Site, Re-Naming) erfordern "
             "PCN (Product Change Notification) mit 6 Monaten Vorlaufzeit. Genehmigungspflicht durch "
             "Andreas Kaufmann (Head of Supplier Quality) und Dr. Stefan Hoffmann (CTO; ab 1.7.2024 "
             "Dr. Petra Hollmann). Bei Wafer-Fab-Wechsel: voller Re-Qualifikationslauf gemaess AEC-Q100, "
             "begleitende EMV-Re-Verifikation in REG Heilbronn."),
            ("7. Freigabe / Sign-off",
             sig("Dr. Stefan Hoffmann", "CTO (Hardware-Verantwortung)", R['name'],
                 s['qmb'].split('(')[0].strip(), "Qualitaetsleitung Lieferant", s['full'],
                 date_str=f"Stuttgart, 15. Mai {jahr}")),
        ])


# ---- 9. Zollabfertigung ------------------------------------------------------
def zollabfertigung(fname, monat_nr, jahr=2023):
    monat = ["", "Januar","Februar","Maerz","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember"][monat_nr]
    nachweis_nr = f"REA-ZOLL-{jahr}-{monat_nr:02d}"
    write_doc(BASE / fname, H,
        f"Zollabfertigungsnachweis - Import - {monat} {jahr}",
        subtitle=f"Sammelnachweis ATLAS-Einfuhranmeldungen, Hauptzollamt Stuttgart - Nr. {nachweis_nr}",
        sections=[
            ("Abfertigungsdaten",
             f"Anmelder: {R['name']}, {R['addr']}\n"
             f"EORI-Nummer: DE5891234567890\n"
             f"Bewilligungsnummer Zugelassener Wirtschaftsbeteiligter (AEO-C/AEOF): DE/AEOF/123456/0322\n"
             f"Hauptzollamt: Stuttgart, Dienstort Heilbronn (fuer Werk REG)\n"
             f"Zollvertretung: indirekt durch Kuehne+Nagel (Deutschland) GmbH, Niederlassung Heilbronn\n"
             f"Verantwortlich Brennhagen: Frank Wendel (Head of Indirect / Trade Compliance), "
             f"Sabine Hartmann (Head of Direct Materials), Christine Berger (Risk)"),
            ("Sammelnachweis Einfuhren " + monat + " " + str(jahr),
             [["MRN (Movement Reference Number)", "Versender / Land", "Warenbeschreibung", "Statistischer Wert (EUR)", "Zollanmeldungsdatum"],
              [f"{jahr}DE12345{monat_nr:02d}01001", "Infineon Technologies AG / DE",
               "Mikrocontroller AURIX (Pos. 8542 3110)", "284.500", f"04.{monat_nr:02d}.{jahr}"],
              [f"{jahr}DE12345{monat_nr:02d}01017", "NXP Semiconductors / NL",
               "CAN-FD Transceiver (Pos. 8542 3990)", "186.230", f"08.{monat_nr:02d}.{jahr}"],
              [f"{jahr}DE12345{monat_nr:02d}01029", "STMicroelectronics / IT",
               "STM32-MCU (Pos. 8542 3190)", "142.800", f"11.{monat_nr:02d}.{jahr}"],
              [f"{jahr}DE12345{monat_nr:02d}01044", "Texas Instruments / US",
               "Analog/DCDC-Wandler (Pos. 8542 3300)", "98.450", f"15.{monat_nr:02d}.{jahr}"],
              [f"{jahr}DE12345{monat_nr:02d}01062", "Murata / JP",
               "Passive Komponenten (Pos. 8532 2200)", "62.150", f"19.{monat_nr:02d}.{jahr}"],
              [f"{jahr}DE12345{monat_nr:02d}01088", "TE Connectivity / CN",
               "Steckverbinder (Pos. 8536 6990)", "54.720", f"22.{monat_nr:02d}.{jahr}"],
              [f"{jahr}DE12345{monat_nr:02d}01101", "Bosch Sensortec / DE (Re-Import)",
               "Drucksensoren MEMS (Pos. 9026 8020)", "37.860", f"26.{monat_nr:02d}.{jahr}"]]),
            ("Steuerliche Behandlung",
             "Einfuhrumsatzsteuer (EUSt) gemaess § 1 Abs. 1 Nr. 4 UStG: aufgeschoben (Vor-Anschreibungs-Verfahren). "
             "Verrechnung mit Vorsteueranspruch in der UStVA des Folgemonats. "
             "Zollabgaben: keine, da ueberwiegend Pos. 8542 (Halbleiter) zollfrei (ITA/WTO-Befreiung). "
             "Praeferenzpraeferenzen: PEM-Konvention angewendet fuer Importe aus IT/NL; Ursprungsnachweis EUR.1 "
             "bzw. Erklaerung auf der Rechnung fuer KMU-Lieferanten."),
            ("Compliance-Check",
             ("list", [
                 "Sanktionslisten-Pruefung (EU-, US- und UN-Listen) ueber MIC Customs Solutions: keine Treffer.",
                 "Dual-Use-Pruefung (EG VO 2021/821): keine genehmigungspflichtigen Gueter im Berichtsmonat.",
                 "Lieferanten-Stammdaten in SAP GTS sind auf Stand "+monat+" "+str(jahr)+" gepflegt.",
                 "AEO-Status: gueltig bis 31.3.2026 (Re-Audit Hauptzollamt 2025 geplant).",
                 "Stichproben durch Christine Berger (3 MRN, ohne Beanstandung).",
             ])),
            ("Aufbewahrung",
             "Anmeldungs- und Begleitdokumente werden gemaess § 147 AO 10 Jahre revisionssicher archiviert "
             "(Brennhagen-DMS d.velop documents, Stamm-Mandant REA). Originalbelege (Frachtbriefe, Handelsrechnungen) "
             "werden parallel im Logistikordner Werk REG abgelegt."),
            ("Unterschrift",
             sig("Frank Wendel", "Head of Indirect / Trade Compliance", R['name'],
                 "Christine Berger", "Risk / Trade-Compliance Officer", R['name'],
                 date_str=f"Stuttgart, Anfang {['','Februar','Maerz','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember','Januar'][monat_nr]} {jahr + (1 if monat_nr==12 else 0)}")),
        ])


# ---- 10. Misc one-offs -------------------------------------------------------
def gate_review_g1(fname):
    write_doc(BASE / fname, H,
        "Gate Review - G1 Konzept - ICP-3 OTA Update Platform",
        subtitle="Projekt PRJ-2023-003 / Stage-Gate G1 (Konzept-Gate) - ICP-3 OTA-Plattform",
        sections=[
            ("Projektkennung",
             "Projekt-Nr.: PRJ-2023-003\n"
             "Projektname: ICP-3 OTA (Over-the-Air) Update Platform\n"
             "Projektart: Plattform-Erweiterung Infotainment (Software + Backend)\n"
             "Stage-Gate: G1 - Konzept (Concept Gate)\n"
             "Reviewdatum: 4. Mai 2023, 09:00-12:00 Uhr (Vor-Ort REG Heilbronn + Teams)\n"
             "Projektleitung: Lars Wittmann (Lead Developer RSG Muenchen), Sponsor: Dr. Stefan Hoffmann (CTO)\n"
             "Begleitung Einkauf: Tobias Lange (fuer ggf. Halbleiter-/Cloud-Service-Beschaffung)"),
            ("Gate-Teilnehmer",
             ("list", [
                 "Sponsor: Dr. Stefan Hoffmann (CTO)",
                 "PMO: Florian Maier (Group Controller, Projektportfolio-Sicht)",
                 "RSG Muenchen: Dr. Klaus Kessler (Werkleiter), Lars Wittmann (Lead Dev)",
                 "REG Heilbronn: Andreas Maier (Werkleiter), Sabine Brand (Q-Leitung)",
                 "Einkauf: Tobias Lange (Strategischer Einkauf Halbleiter), Sabine Hartmann (Head Direct)",
                 "Compliance / Cybersecurity: CISO-Referat (delegiert)",
                 "OEM-Vertretung: Stefan Richter (CMO/BD, mit BMW-/MBZ-Hut)",
             ])),
            ("Bewertung G1 (Konzept) - Pruefkriterien",
             [["Kriterium", "Bewertung", "Kommentar"],
              ["Business-Case (NPV 7 Jahre)", "GO", "+18,5 Mio. EUR, Pay-back 26 Monate"],
              ["Technische Machbarkeit (Architekturkonzept)", "GO", "Cloud-Backend AWS Frankfurt; Delta-OTA via DM/AB-Partitionsmodell"],
              ["Cybersecurity (ISO/SAE 21434)", "GO mit Auflage", "TARA-Workshop in G2 nachholen"],
              ["Regulatorik (UNECE R155/R156)", "GO", "Compliance-Roadmap dokumentiert"],
              ["Ressourcen-Verfuegbarkeit", "GO", "RSG 8 FTE bestaetigt; Werkstudent-Pool"],
              ["Lieferanten-Strategie Cloud", "PARK", "Cloud-Service-Beschaffung in G2 finalisieren"]]),
            ("Gate-Entscheidung",
             "Der Sponsoren-Kreis erteilt G1-Freigabe (GO mit Auflagen). Das Projekt geht in Phase 2 "
             "(Konzept-Vertiefung und Architekturspezifikation) ueber. Naechstes Gate (G2 - Definition) "
             "ist fuer den 5. Oktober 2023 terminiert. Budget G1->G2: 480.000 EUR (Engineering RSG + "
             "externe Cybersecurity-Beratung)."),
            ("Auflagen / Action Items",
             [["Nr.", "Auflage", "Verantwortlich", "Termin"],
              ["A1", "TARA-Workshop nach ISO/SAE 21434 mit externem TUV-Auditor", "Lars Wittmann", "30.6.2023"],
              ["A2", "Cloud-Service-Anbieter-Shortlist (AWS / Azure / GCP) inkl. DSGVO-Schufa", "Tobias Lange", "31.7.2023"],
              ["A3", "Detaillierter Resource-Plan G2-G3 (FTE-Heatmap)", "Lars Wittmann / Dr. Kessler", "15.7.2023"],
              ["A4", "Erste Bedrohungsmodellierung (STRIDE) fuer OTA-Backend", "RSG Muenchen", "31.8.2023"]]),
            ("Unterschrift",
             sig("Dr. Stefan Hoffmann", "CTO (Sponsor)", R['name'],
                 "Lars Wittmann", "Projektleitung / Lead Developer", "Brennhagen Software GmbH (RSG)",
                 date_str="Muenchen / Heilbronn, 4. Mai 2023")),
        ])


def rcn_steuerbescheid_2020(fname):
    write_doc(BASE / fname, {"name": "Brennhagen (Shanghai) Co. Ltd. / RCN",
                              "addr": "Bldg. 12, No. 1518 Lianhang Road, Minhang District, Shanghai 201112, P.R. China",
                              "hrb": "Einheitlicher Sozialkredit-Code: 91310115MA1FL42Q38"},
        "Steuerbescheid / Tax Assessment 2020 - Brennhagen (Shanghai) Co. Ltd.",
        subtitle="Koerperschaftsteuer-Bescheid VR China, Steuerjahr 2020",
        sections=[
            ("Bescheidkopf",
             "Steuerbehoerde: State Taxation Administration, Shanghai Municipal Office, "
             "Local Inspectorate Minhang District\n"
             "Bescheid-Nr.: SH-MH-CIT-2020-0084771\n"
             "Bescheid-Datum: 28. April 2021\n"
             "Steuerpflichtige: Brennhagen (Shanghai) Co. Ltd. (RCN)\n"
             "Steuerart: Corporate Income Tax (CIT) - VR China\n"
             "Steuerjahr: 1.1.2020 - 31.12.2020\n"
             "Vertretung in CN: Zhang Hao (Country Manager), Liang Wei (Finance Manager)\n"
             "Externe Begleitung: KPMG China (Shanghai Office), Berichtsadressat KPMG Frankfurt "
             "(Lead Partner Brennhagen: Dr. Maximilian Brand)"),
            ("Bemessungsgrundlage",
             [["Position", "Betrag (CNY)", "Betrag (EUR Aequivalent, Kurs 31.12.2020)"],
              ["Umsatzerloese (CIT-Basis)", "182.450.000", "22.806.250"],
              ["Operative Aufwendungen", "-164.200.000", "-20.525.000"],
              ["Zwischensumme Operativ", "18.250.000", "2.281.250"],
              ["F&E-Superabzug (175 %, gemaess Cai Shui 2018-99)", "-3.250.000", "-406.250"],
              ["Sonstige Erloese (Zinsen)", "+420.000", "+52.500"],
              ["Steuerpflichtiges Einkommen (CIT-Basis)", "15.420.000", "1.927.500"]]),
            ("Steuerberechnung",
             "Steuersatz Regelfall CIT VR China: 25 %.\n"
             "Anwendbare Beguenstigung: keine HNTE-Zertifizierung in 2020 (Antrag erst 2021 gestellt). "
             "Berechnete Koerperschaftsteuer: 3.855.000 CNY (entspricht ca. 481.875 EUR).\n"
             "Bereits geleistete Vorauszahlungen (vierteljaehrlich): 3.700.000 CNY.\n"
             "Nachzahlungsbetrag: 155.000 CNY (ca. 19.375 EUR), faellig zum 30. Mai 2021.\n"
             "Saeumniszinsen: keine."),
            ("Hinweise und Auflagen",
             ("list", [
                 "Transfer-Pricing-Dokumentation Local File 2020 fristgerecht eingereicht (30.6.2021).",
                 "Master File / Country-by-Country-Report werden ueber Konzernmutter REA via "
                 "BZSt Deutschland gepflegt; Mitteilungspflicht in CN per Formular A108 erfuellt.",
                 "VAT-Sonderpruefung 2020 ohne Beanstandung abgeschlossen (Bescheid Nr. SH-MH-VAT-2020-1142).",
                 "Hinweis: ab Steuerjahr 2021 voraussichtlich HNTE-Status (Hightech-Statusermaessigung 15 %) - "
                 "Auswirkungen werden separat im Jahresabschluss Folgejahr erlaeutert.",
             ])),
            ("Rechtsbehelfsbelehrung",
             "Gegen diesen Bescheid kann binnen 60 Tagen ab Zustellung Einspruch beim "
             "Shanghai Municipal Tax Administrative Reconsideration Office eingelegt werden. "
             "Ein Einspruch ist nicht beabsichtigt (Abstimmung Steuerteam RCN/Konzern Dr. Heike Berger, "
             "Group Tax Director, 12. Mai 2021)."),
            ("Verteiler intern",
             ("list", [
                 "Liang Wei (Finance Manager RCN) - Ablage Local Books",
                 "Zhang Hao (Country Manager RCN)",
                 "Dr. Heike Berger (Group Tax Director, Konzern)",
                 "Markus Pflanzer (Group Treasurer) - Liquiditaetssteuerung",
                 "Laura Bauer (CFO) - quartalsbezogen im Tax-Review",
                 "KPMG China (Bestaetigungs-Memo)",
             ])),
        ])


def rsg_br_korrespondenz(fname):
    write_doc(BASE / fname, {"name": "Brennhagen Software GmbH (RSG)",
                              "addr": "Leopoldstrasse 244, 80807 Muenchen",
                              "hrb": "HRB 319872, Amtsgericht Muenchen"},
        "BR-Korrespondenz - Arbeitszeit Widerspruch RSG Muenchen - 2023",
        subtitle="Widerspruch des Betriebsrats gegen einseitige Arbeitszeit-Anordnung",
        sections=[
            ("Anschreiben Betriebsrat an Geschaeftsfuehrung",
             "An die Geschaeftsfuehrung der Brennhagen Software GmbH\nz.Hd. Dr. Klaus Kessler\n"
             "Leopoldstrasse 244, 80807 Muenchen\n\n"
             "Muenchen, den 18. Juli 2023\n\n"
             "Betreff: Widerspruch des Betriebsrats gemaess § 87 Abs. 1 Nr. 2 BetrVG - "
             "einseitige Verlaengerung der Wochenarbeitszeit fuer das Projekt »ADAS-V4D Software-Stack«\n\n"
             "Sehr geehrter Herr Dr. Kessler,\n\n"
             "der Betriebsrat der Brennhagen Software GmbH widerspricht hiermit foermlich der mit "
             "E-Mail vom 11. Juli 2023 (10:42 Uhr) durch die Projektleitung Lars Wittmann angeordneten "
             "Verlaengerung der woechentlichen Arbeitszeit auf bis zu 50 Stunden fuer die Sprint-Phase "
             "vom 1. August bis 30. September 2023 (ADAS-V4D Release-Vorbereitung)."),
            ("Begruendung",
             ("list", [
                 "Die Anordnung stellt eine mitbestimmungspflichtige Massnahme im Sinne § 87 Abs. 1 Nr. 2 BetrVG "
                 "(Lage der Arbeitszeit) sowie Nr. 3 (vorruebergehende Verkuerzung/Verlaengerung) dar.",
                 "Eine Anhoerung oder Zustimmung des Betriebsrats hat vor Anordnung nicht stattgefunden.",
                 "Die geplante Verlaengerung ueberschreitet den im § 3 ArbZG normierten Hoechstrahmen "
                 "(8h/Tag, Verlaengerung auf max. 10h im Ausgleichszeitraum) ueber sechs Wochen hinweg.",
                 "Aktuelle Ueberstundenkonten von 14 Mitarbeitenden im Team weisen bereits Salden "
                 "ueber 80 Stunden auf; die geplante Anordnung wuerde gegen die in der BV »Gleitzeit RSG 2022« "
                 "vereinbarte Obergrenze (100 Std.-Konto) verstossen.",
                 "Eine Gefaehrdungsbeurteilung psychischer Belastung im Sinne § 5 ArbSchG fuer die "
                 "Verlaengerungs-Phase liegt nicht vor.",
             ])),
            ("Forderungen des BR",
             ("list", [
                 "Sofortige Aussetzung der Anordnung mit Wirkung zum 19. Juli 2023.",
                 "Aufnahme von Einigungsgespraechen mit der Geschaeftsfuehrung bis spaetestens 26. Juli 2023.",
                 "Schriftliche Vorlage des Massnahmenplans mit Ressourcen-Alternativen "
                 "(z.B. zeitlich befristete Werkvertraege, Verschiebung Release-Termin).",
                 "Vorlage einer aktuellen Gefaehrdungsbeurteilung psychischer Belastung.",
                 "Falls keine Einigung erfolgt: Anrufung der Einigungsstelle gemaess § 76 BetrVG.",
             ])),
            ("Hinweis auf rechtliche Schritte",
             "Sollte die Anordnung ohne Mitbestimmungsverfahren in Kraft gesetzt werden, wird der "
             "Betriebsrat einen Antrag auf einstweilige Verfuegung beim Arbeitsgericht Muenchen pruefen lassen "
             "(Kanzlei Schwegler Rechtsanwaelte, in Abstimmung). Eine Befassung des Konzernbetriebsrats "
             "(Marlies Duerr, Vorsitz / Aufsichtsrat) ist zur Information vorgesehen."),
            ("Antwort der Geschaeftsfuehrung (Eintragung)",
             "Geschaeftsfuehrer Dr. Kessler bestaetigt mit Schreiben vom 20. Juli 2023 die Aussetzung "
             "der Anordnung und lae dt zu einem Einigungsgespraech am 25. Juli 2023, 14:00 Uhr, in den "
             "Konferenzraum Maxvorstadt ein. Teilnehmer: GF, BR-Vorsitz, Lars Wittmann, HR-Leitung RSG "
             "(Frau Sabine Mohrmann). Ergebnis: protokolliert in BR-Sitzungsprotokoll 2023-08."),
            ("Unterschrift",
             sig("Markus Helbig", "Vorsitzender des Betriebsrats", "Brennhagen Software GmbH (RSG)",
                 "Dr. Klaus Kessler", "Werkleiter / Geschaeftsfuehrer", "Brennhagen Software GmbH (RSG)",
                 date_str="Muenchen, 20. Juli 2023")),
        ])


def memo_carbon_neutrality(fname):
    write_doc(BASE / fname, H,
        "Vorstandsmemo - Carbon Neutrality 2030",
        subtitle="Konzern-Roadmap zur Klimaneutralitaet bis 2030 - Beschlussvorlage Vorstand",
        confidential=True,
        sections=[
            ("Adressat / Verfasser",
             "Adressat: Vorstand der Brennhagen Elektronik AG (Anna Mueller, Laura Bauer, Dr. Thomas Weber, "
             "Stefan Hoffmann), zur Kenntnis: Aufsichtsratspraesidium Dr. Klaus Steinbrueck (Vorsitz).\n"
             "Verfasser: Dr. Robert Walther (CPO Operations, Sponsor Roadmap) in Abstimmung mit "
             "Florian Maier (Group Controller) und Christine Berger (Risk).\n"
             "Datum: 7. Februar 2023\n"
             "Status: Beschlussvorlage Vorstand (Sitzung 15.2.2023, TOP 5)"),
            ("Zielsetzung",
             "Die Brennhagen Elektronik AG beabsichtigt, bis spaetestens 31.12.2030 in den Scopes 1 und 2 "
             "vollstaendige Klimaneutralitaet (Net-Zero) zu erreichen. Scope 3 (Lieferkette) wird "
             "mit dem Zielhorizont 2040 nachgelagert. Die Roadmap stuetzt sich auf die Vorgaben "
             "der SBTi (Science Based Targets initiative, 1,5-Grad-Pfad) und ist Bestandteil der "
             "CSRD-Berichterstattung ab Geschaeftsjahr 2024."),
            ("Ausgangslage 2022 (Bilanz Scope 1+2, Mio. t CO2e)",
             [["Standort", "Scope 1 (direkt)", "Scope 2 (Strom/Waerme)", "Summe Scope 1+2"],
              ["REG Heilbronn", "0,012", "0,041", "0,053"],
              ["RSG Muenchen (Buero)", "0,001", "0,008", "0,009"],
              ["RPL Katowice", "0,018", "0,062", "0,080"],
              ["RCZ Brno", "0,009", "0,033", "0,042"],
              ["RHU Gyoer", "0,007", "0,028", "0,035"],
              ["RCN Shanghai", "0,002", "0,011", "0,013"],
              ["Konzern gesamt", "0,049", "0,183", "0,232"]]),
            ("Massnahmenpaket (Auszug)",
             ("clauses", [
                 ("§ 1 Energiebezug (Scope 2)",
                  ["Sofortige Umstellung deutscher Standorte (REG, RSG, RHO) auf 100 %-Gruenstrom-PPAs "
                   "ab 1.1.2024 (Ausschreibung Q2 2023, Lead Sabine Hartmann).",
                   "Polen (RPL): PPA mit Onshore-Wind PL-Nord, 65 GWh/a, Vertragslaufzeit 10 Jahre, "
                   "Verhandlungsfuehrung mit Tauron Polska Energia und PGE Energia Odnawialna.",
                   "Tschechien (RCZ) und Ungarn (RHU): kombinierter PPA mit CEZ/MVM oder Marktbezug mit "
                   "Herkunftsnachweisen (GoO/G-REX)."]),
                 ("§ 2 Eigenerzeugung",
                  ["PV-Aufdach REG Heilbronn: 4,8 MWp (Dachflaeche Werk 1+2), Investvolumen 4,2 Mio. EUR, "
                   "ROI ca. 8 Jahre. Inbetriebnahme Q3 2024.",
                   "PV RPL Katowice 3,2 MWp; pruefung Batteriespeicher 2 MWh.",
                   "Kraft-Waerme-Kopplung Werk Brno: Pruefung BHKW 1,5 MWel mit Biomethan."]),
                 ("§ 3 Scope 1 - Brennstoffe",
                  ["Umstellung Erdgas-Heizung REG/RPL auf elektrische Waermepumpen + industrielle "
                   "Abwaermenutzung der SMD-Linien (Pilot 2024, Roll-out bis 2028).",
                   "Fuhrpark: Umstellung Aussendienst-Fahrzeuge auf BEV bis 2026 (100 %)."]),
                 ("§ 4 Restemissionen",
                  ["Verbleibende Scope-1+2-Restmenge (Schaetzung 2030: < 10 % von 2022) wird ueber "
                   "hochqualifizierte CO2-Removal-Zertifikate (CDR, Gold Standard / Verra VCS) "
                   "kompensiert. Kein offsetting via fossiler Vermeidungsprojekte."]),
             ])),
            ("Finanzieller Rahmen / Covenants-Bezug",
             "Geschaetztes Capex 2023-2030: 48 Mio. EUR (davon 24 Mio. PV/PPA-Infrastruktur). "
             "Refinanzierung ueber ESG-Tranche bestehende Konsortialfinanzierung (Sustainability-Linked-Loan "
             "mit ±5 bp Margenanpassung gemaess Scope 1+2-KPI). Auswirkung auf Net-Debt/EBITDA-Covenant "
             "im Toleranzbereich (< 0,1 turn). Abstimmung mit Markus Pflanzer (Group Treasurer)."),
            ("Beschlussvorschlag",
             "Der Vorstand beschliesst die Roadmap »Carbon Neutrality 2030« in der vorliegenden Fassung "
             "und beauftragt Dr. Robert Walther (CPO) mit der Umsetzung. Quartalsweises Reporting an "
             "den Aufsichtsrat (Pruefungsausschuss Prof. Dr.-Ing. Voss). Erste Massnahmen werden im "
             "Q1/Q2 2023 angestossen; CSRD-Berichtsreife bis 31.12.2024."),
            ("Unterschrift Vorlage",
             sig("Dr. Robert Walther", "Vorstand / CPO Operations", R['name'],
                 "Florian Maier", "Group Controller", R['name'],
                 date_str="Stuttgart, 7. Februar 2023")),
        ])


def bv_arbeitszeit_gleitzeit(fname):
    write_doc(BASE / fname, H,
        "Betriebsvereinbarung Arbeitszeit / Gleitzeit - Konzern 2022",
        subtitle="Konzernbetriebsvereinbarung zwischen Konzernbetriebsrat und Konzernleitung",
        sections=[
            ("Vereinbarende",
             "Konzernleitung: Brennhagen Elektronik AG, vertreten durch den Vorstand "
             "(Anna Mueller / CEO und Dr. Thomas Weber / COO).\n"
             "Konzernbetriebsrat (KBR): vertreten durch Marlies Duerr (Vorsitzende; Aufsichtsraetin), "
             "Klaus Bauer (stv. Vorsitz, Werk Heilbronn).\n"
             "Geltungsbereich: alle deutschen Konzerngesellschaften (REA Holding/RHO, REG Heilbronn, "
             "RSG Muenchen); fuer auslaendische Tochtergesellschaften gilt lokales Recht (subsidiaere "
             "Empfehlung).\n"
             "Inkrafttreten: 1. Mai 2022; unbefristet, mit Kuendigungsfrist 6 Monate zum Quartalsende."),
            ("Praeambel",
             "Die Vertragsparteien sind sich einig, dass moderne Arbeitszeitmodelle zur Vereinbarkeit "
             "von Beruf, Familie und Gesundheit beitragen und gleichzeitig die operative Leistungsfaehigkeit "
             "der Brennhagen-Gruppe sichern. Diese Konzernbetriebsvereinbarung regelt das Gleitzeitmodell "
             "fuer Tarifbeschaeftigte und ATB-Mitarbeitende in der Verwaltung, im indirekten Bereich "
             "sowie in den Software- und Entwicklungsabteilungen. Schichtbeschaeftigte (Werk REG, RPL, RCZ, RHU) "
             "sind durch eigenstaendige Schichtmodelle in werksbezogenen BVs geregelt."),
            ("Gleitzeit-Eckwerte",
             [["Regelung", "Wert"],
              ["Regelarbeitszeit / Woche", "40 Std. (Tarif IG Metall Baden-Wuerttemberg, AT 38 Std.)"],
              ["Kernarbeitszeit", "09:30 - 15:00 Uhr (Mo-Do); Fr 09:30 - 13:30 Uhr"],
              ["Gleitspanne morgens", "06:30 - 09:30 Uhr"],
              ["Gleitspanne abends", "15:00 - 20:00 Uhr (Fr bis 18:00 Uhr)"],
              ["Pausenpflicht", "30 min ab 6 Std., 45 min ab 9 Std."],
              ["Gleitzeitkonto", "-30 / +60 Stunden zulaessig (Monatsdurchschnitt -10/+20)"],
              ["Saldoausgleich (Abbau)", "halbjaehrlich, sonst Vereinbarung mit Vorgesetzter"],
              ["Mobile Work-Quote", "bis 60 % der Wochenarbeitszeit, ortsunabhaengig (DE)"]]),
            ("Erfassung und Datenschutz",
             ("list", [
                 "Erfassung ueber SAP SuccessFactors Time Management; Selbsterfassung mit Vier-Augen-Pruefung "
                 "durch Fuehrungskraft.",
                 "Datenschutz: Zugriff nur fuer Beschaeftigte selbst, Fuehrungskraft, HR und ggf. BR. "
                 "Auswertungen ueber Einzelpersonen sind verboten - Ausnahme: dokumentierte arbeitsrechtliche Anlaesse.",
                 "Aufbewahrung gemaess § 16 ArbZG (2 Jahre) und BDSG.",
                 "Loeschkonzept abgestimmt mit Datenschutzbeauftragtem (Frau Dr. Beate Holler, extern).",
             ])),
            ("Mehrarbeit / Ueberstunden",
             "Mehrarbeit ueber das Gleitzeitkonto hinaus (>60 Std. Saldo) ist nur zulaessig bei "
             "schriftlicher Anordnung der Fuehrungskraft und Information des BR (kein Zustimmungsvorbehalt "
             "unterhalb 80 Std.). Ueberstunden werden 1:1 in Freizeit ausgeglichen; auf Wunsch der "
             "Mitarbeitenden auch in Geld (Tarif-Zuschlag 25 %). Auflagen aus dem Arbeitszeitgesetz "
             "(11 Std. Ruhezeit, Hoechstdauer 10 Std./Tag) sind strikt einzuhalten."),
            ("Mobile Work und Erreichbarkeit",
             "Beschaeftigte koennen bis zu 60 % der Wochenarbeitszeit mobil arbeiten (innerhalb DE). "
             "Ausserhalb der individuellen Arbeitszeit besteht kein Pflicht zur dienstlichen Erreichbarkeit "
             "(»Recht auf Nicht-Erreichbarkeit«). Notfallnummer / Rufbereitschaftsdienste sind "
             "in gesonderten BVs geregelt."),
            ("Schlussbestimmungen",
             "Streitfaelle werden durch eine paritaetisch besetzte Kommission (2 KBR / 2 GL) erstrangig "
             "behandelt. Bei Nichteinigung: Einigungsstelle gemaess § 76 BetrVG. Diese BV ersetzt die "
             "frueheren Einzel-BVs aus 2018 / 2019 (REG / RSG)."),
            ("Unterschriften",
             sig("Marlies Duerr", "Vorsitzende Konzernbetriebsrat", R['name'],
                 "Dr. Thomas Weber", "COO / Vorstand", R['name'],
                 date_str="Stuttgart, 14. April 2022")),
        ])


def governance_report_q1(fname):
    write_doc(BASE / fname, H,
        "Konzern-Governance-Bericht Q1 2022",
        subtitle="Quartals-Compliance- und Governance-Berichterstattung an Vorstand und Pruefungsausschuss",
        confidential=True,
        sections=[
            ("Berichtskopf",
             f"Berichtsperiode: 1. Januar 2022 - 31. Maerz 2022\n"
             f"Berichtsersteller: Andreas Buehler (Chief Audit Executive / Internal Audit)\n"
             f"Adressat: Vorstand der {R['name']}; in Kopie Pruefungsausschuss-Vorsitz "
             f"Prof. Dr.-Ing. Gerhard Voss\n"
             f"Berichtsdatum: 22. April 2022\n"
             f"Klassifizierung: Vertraulich - Aufsichtsrat / Pruefungsausschuss"),
            ("Compliance-Status",
             [["Bereich", "Status", "Kommentar"],
              ["Code of Conduct (Awareness)", "Gruen", "98 % Trainingsquote (Praesenz + E-Learning)"],
              ["Hinweisgebersystem (BKMS)", "Gruen", "11 Meldungen Q1, 9 abschliessend bearbeitet"],
              ["Kartellrecht", "Gruen", "Keine offenen Verdachtsfaelle"],
              ["Sanktionsrecht (RU/BY/IR)", "Gelb", "Erhoehte Pruefintensitaet nach EU-Sanktionspaket 2/3/4"],
              ["Datenschutz (DSGVO)", "Gelb", "2 meldepflichtige Vorfaelle, beide < 72 h gemeldet"],
              ["Insiderrecht (MAR)", "Gruen", "Insiderliste gepflegt, Closed Period 21.3.-31.3. eingehalten"],
              ["LkSG-Vorbereitung", "Gelb", "Implementierung lt. Plan; SAQ-Rollout im April"]]),
            ("Internal-Audit-Aktivitaeten",
             ("list", [
                 "Audit »Beschaffung indirekte Materialien« REG/RSG abgeschlossen - "
                 "3 Empfehlungen (low), Umsetzungsplan vereinbart.",
                 "Audit »Treasury Front-/Mid-/Back-Office-Funktionstrennung« laufend (Abschluss Q2).",
                 "Sonder-Review »IPO-Internal-Controls« (Q4 2022 IPO-Vorbereitung) - Scoping abgeschlossen, "
                 "Beginn Feldarbeit 1.5.2022.",
                 "ITGC-Pruefung SAP S/4HANA Berechtigungen - 4 Findings (medium), Remediation H2 2022.",
             ])),
            ("Wesentliche Risiken (Top-5 Konzern)",
             [["Risiko", "Brutto-Score", "Netto-Score nach Massnahmen"],
              ["Halbleiter-Versorgungsengpaesse", "Hoch", "Mittel (Allokationsvereinbarungen, LTAs)"],
              ["Energiepreisvolatilitaet 2022 (Ukraine-Krise)", "Hoch", "Mittel (Hedging, PPA-Pipeline)"],
              ["FX-Volatilitaet USD/EUR", "Mittel", "Niedrig (Rolling-Hedge Programm)"],
              ["Cyber-Sicherheit OT-Netzwerk REG", "Mittel-Hoch", "Mittel (Segmentierung, Zero-Trust-Pilot)"],
              ["IPO-Readiness Internal Controls", "Mittel", "Niedrig nach Audit-Empfehlungen"]]),
            ("Vorgaenge mit Aufsichtsratsrelevanz",
             ("list", [
                 "Geplante Bestellung einer ESG-/Nachhaltigkeitsbeauftragten (Vorlage Vorstand 15.5.2022).",
                 "Vorbereitung Konsortialkreditvertrag 250 Mio. EUR (Closing 14.3.2022 - bereits erfolgt).",
                 "Update zum Stand IPO-Vorbereitung (Roadshow Q3, Listing Q4).",
                 "Pruefungsausschuss-Sitzung 12.5.2022: TOPs Q1-Reporting, IFRS-Pilotbilanz.",
             ])),
            ("Fazit / Ausblick",
             "Die Governance-Lage zum Stichtag 31.3.2022 ist insgesamt geordnet. Im Zuge der "
             "Ukraine-Krise wurden Sanktions- und Versorgungs-Risiken hochgestuft und mit "
             "zusaetzlichen Kontrollen versehen. Schwerpunkte des Q2 sind die LkSG-Implementierung "
             "sowie der vollstaendige Aufbau IPO-faehiger internal controls."),
            ("Unterschrift",
             sig("Andreas Buehler", "Chief Audit Executive (CAE)", R['name'],
                 "Dr. Heike Berger", "Group Tax Director / Compliance-Koordination", R['name'],
                 date_str="Stuttgart, 22. April 2022")),
        ])


def konzernlagebericht_2022(fname):
    write_doc(BASE / fname, H,
        "Zusammengefasster Konzernlagebericht 2022 - Brennhagen Elektronik AG",
        subtitle="Berichterstattung gemaess §§ 315, 315a HGB i.V.m. DRS 20 - Geschaeftsjahr 2022",
        sections=[
            ("Berichtsumfang",
             "Der zusammengefasste Konzernlagebericht der Brennhagen Elektronik AG fasst den "
             "Konzernlagebericht und den Lagebericht der Muttergesellschaft fuer das Geschaeftsjahr "
             "vom 1. Januar 2022 bis 31. Dezember 2022 zusammen. Er wurde vom Vorstand am "
             "15. Maerz 2023 aufgestellt und vom Aufsichtsrat in der Bilanzsitzung am 30. Maerz 2023 "
             "geprueft und gebilligt. Der Abschlusspruefer (KPMG AG WPG, Lead-Partner Dr. Maximilian Brand) "
             "hat einen uneingeschraenkten Bestaetigungsvermerk erteilt."),
            ("1. Wirtschaftsbericht",
             "Die Brennhagen Elektronik AG konnte im Geschaeftsjahr 2022 ihren Umsatz auf 600 Mio. EUR "
             "(Vorjahr 580 Mio. EUR) steigern. Das EBITDA stieg auf 73 Mio. EUR (Vorjahr 70 Mio. EUR), "
             "die EBITDA-Marge lag bei 12,2 % (Vj. 12,1 %). Wesentliche Treiber: Hochlauf BMS-12 fuer "
             "VW ID.7 (SOP planmaessig fuer Q1 2024 vorbereitet), Erholung der OEM-Volumina nach "
             "Halbleiterkrise (insbes. ECU-900) sowie Erloesbeitraege aus der Markteinfuehrung des "
             "neuen Werks RPL Katowice. Belastend wirkten die hohen Energie- und Inputfaktorkosten "
             "(Halbleiter, Logistik). Der IPO am 14. Oktober 2022 brachte einen Bruttoemissionserloes "
             "von 612 Mio. EUR (Emissionskurs 24,50 EUR) und staerkt das Eigenkapital nachhaltig."),
            ("2. Finanz- und Vermoegenslage",
             [["Kennzahl (Mio. EUR)", "2020", "2021", "2022"],
              ["Umsatz", "542", "580", "600"],
              ["EBITDA", "64", "70", "73"],
              ["EBIT", "38", "42", "47"],
              ["Periodenergebnis", "21", "25", "29"],
              ["Eigenkapital (zum Stichtag)", "190", "215", "820"],
              ["EK-Quote", "32 %", "34 %", "61 %"],
              ["Net Debt / EBITDA", "1,8x", "1,7x", "0,4x"],
              ["FTE (Konzern, Stichtag)", "3.620", "3.820", "4.020"]]),
            ("3. Nichtfinanzielle Erklaerung",
             ("list", [
                 "Erstmalige freiwillige Berichterstattung gemaess GRI-Standards (Core) - Bruecke zu CSRD ab 2024.",
                 "Scope-1+2-Emissionen: 0,232 Mio. t CO2e (Konzern). Roadmap Carbon Neutrality 2030 beschlossen.",
                 "Frauenanteil Gesamtbelegschaft: 28 %; in Fuehrungspositionen 22 %.",
                 "Unfallrate (LTIF): 3,4 (Vorjahr 4,1) - Verbesserung durch Werkssicherheitsoffensive.",
                 "LkSG-Vorbereitung abgeschlossen, Inkrafttreten 1.1.2023.",
             ])),
            ("4. Prognosebericht",
             "Fuer das Geschaeftsjahr 2023 erwartet der Vorstand einen Konzernumsatz im Korridor "
             "605-625 Mio. EUR sowie ein EBITDA zwischen 73 und 78 Mio. EUR. Wesentliche Annahmen: "
             "weitere Erholung Halbleiterbeschaffung, planmaessige SOP BMS-12 fuer VW ID.7 Q1 2024, "
             "Stabilisierung der Energiepreise auf erhoehtem Niveau. Risiken: geopolitische Eskalation, "
             "OEM-Volumenrueckgaenge BEV-Plattformen, Inflations- und Lohnentwicklung."),
            ("5. Chancen- und Risikobericht",
             "Wesentliche Risiken werden im konzernweiten ERM-System (Risk Owner pro Risiko, "
             "quartalsweises Reporting an Vorstand und Pruefungsausschuss) gesteuert. Top-Risiken 2022: "
             "Halbleiterversorgung (mittel, mit weiteren Long-Term Agreements adressiert), "
             "Energiepreis (mittel, Hedging und PPA-Programm), Cyber-Sicherheit OT-Netzwerk REG "
             "(mittel, Massnahmen mit Roll-out 2023-2024). Wesentliche Chancen: BEV-Hochlauf, "
             "ADAS-Level-3-Programme bei MBZ, Skalierung Software-Anteil (RSG, ASPICE L3)."),
            ("6. Vergueterungsbericht / Erklaerung Unternehmensfuehrung",
             "Vergueterung Vorstand und Aufsichtsrat erfolgt gemaess Vergueterungssystem 2022 "
             "(zustimmender HV-Beschluss 14.6.2022). Erklaerung zur Unternehmensfuehrung sowie "
             "Entsprechenserklaerung DCGK in der Fassung 2022 separat veroeffentlicht."),
            ("Unterschrift Vorstand",
             sig("Anna Mueller", "CEO / Vorsitzende des Vorstands", R['name'],
                 "Laura Bauer", "CFO", R['name'],
                 date_str="Stuttgart, 15. Maerz 2023")),
        ])


# ---- DRIVER ------------------------------------------------------------------
RFQ_MAP = {
    "REA_RFQ_Halbleiter_MCU_2024.docx": ("Halbleiter Mikrocontroller (MCU) - Programmportfolio Brennhagen", "MCU"),
    "REA_RFQ_Halbleiter_Power_2024.docx": ("Halbleiter Power (Power-MOSFET / SiC / GaN)", "PWR"),
    "REA_RFQ_Kabel_Steckverbinder_2024.docx": ("Kabel und Steckverbinder (Bordnetz und Interconnect)", "INT"),
    "REA_RFQ_Leiterplatten_HDI_2024.docx": ("Leiterplatten HDI (8-12 Lagen, Microvia, HF-Material)", "PCB"),
    "REA_RFQ_Passive_Komponenten_2023.docx": ("Passive Komponenten (Widerstaende, Kondensatoren, Induktivitaeten)", "PAS"),
    "REA_RFQ_Gehaeuse_Kunststoff_2024.docx": ("Kunststoffgehaeuse / Spritzguss (PA66, PBT, technische Thermoplaste)", "GEH"),
}

RAHMEN_FILES = {
    "REA_BUE_Rahmenvertrag_2022.docx": "BUE",
    "REA_LAP_Rahmenvertrag_2022.docx": "LAP",
    "REA_RSC_Rahmenvertrag_2022.docx": "RSC",
    "REA_GRA_Rahmenvertrag_2022.docx": "GRA",
    "REA_TEC_Rahmenvertrag_2022.docx": "TEC",
    "REA_WUE_Rahmenvertrag_2022_rev_SRichter.docx": "WUE",
}

ZOLL_FILES = {
    "REA_Zollabfertigung_2023_03.docx": 3,
    "REA_Zollabfertigung_2023_06.docx": 6,
    "REA_Zollabfertigung_2023_09.docx": 9,
    "REA_Zollabfertigung_2023_12.docx": 12,
}


def main():
    written = 0
    # Audits (4 suppliers x 4 quarters with some variants)
    audit_files = [
        ("REA_INF_Lieferantenaudit_2023_Q1_ALT.docx", "INF", "Q1"),
        ("REA_INF_Lieferantenaudit_2023_Q2.docx", "INF", "Q2"),
        ("REA_INF_Lieferantenaudit_2023_Q4.docx", "INF", "Q4"),
        ("REA_NXP_Lieferantenaudit_2023_Q1_v2.docx", "NXP", "Q1"),
        ("REA_NXP_Lieferantenaudit_2023_Q2.docx", "NXP", "Q2"),
        ("REA_NXP_Lieferantenaudit_2023_Q3.docx", "NXP", "Q3"),
        ("REA_NXP_Lieferantenaudit_2023_Q4_2024-03-01.docx", "NXP", "Q4"),
        ("REA_STM_Lieferantenaudit_2023_Q1.docx", "STM", "Q1"),
        ("REA_STM_Lieferantenaudit_2023_Q2.docx", "STM", "Q2"),
        ("REA_STM_Lieferantenaudit_2023_Q3.docx", "STM", "Q3"),
        ("REA_STM_Lieferantenaudit_2023_Q4.docx", "STM", "Q4"),
        ("REA_BOS_Lieferantenaudit_2023_Q1.docx", "BOS", "Q1"),
        ("REA_BOS_Lieferantenaudit_2023_Q2.docx", "BOS", "Q2"),
        ("REA_BOS_Lieferantenaudit_2023_Q3.docx", "BOS", "Q3"),
        ("REA_BOS_Lieferantenaudit_2023_Q4.docx", "BOS", "Q4"),
    ]
    for fname, sup, q in audit_files:
        lieferanten_audit(fname, sup, 2023, q); written += 1

    # Allokation 2021
    for sup in ("INF", "NXP", "STM", "BOS"):
        allokationsvereinbarung(f"REA_{sup}_Allokationsvereinbarung_2021.docx", sup, 2021); written += 1

    # LTA 2023
    for sup in ("INF", "NXP", "STM"):
        lta(f"REA_{sup}_Langfristvertrag_LTA_2023.docx", sup, 2023); written += 1

    # Entwicklungsprogramm 2023
    entwicklungsprogramm("REA_INF_Entwicklungsprogramm_2023_WIP.docx", "INF", 2023); written += 1
    entwicklungsprogramm("REA_NXP_Entwicklungsprogramm_2023.docx", "NXP", 2023); written += 1
    entwicklungsprogramm("REA_STM_Entwicklungsprogramm_2023.docx", "STM", 2023); written += 1
    entwicklungsprogramm("REA_BOS_Entwicklungsprogramm_2023.docx", "BOS", 2023); written += 1

    # REACH RoHS
    reach_rohs("REA_INF_REACH_RoHS_Konformitaet_2023.docx", "INF"); written += 1
    reach_rohs("REA_NXP_REACH_RoHS_Konformitaet_2023.docx", "NXP"); written += 1
    reach_rohs("REA_STM_REACH_RoHS_Konformitaet_2023_FINAL_v2.docx", "STM"); written += 1
    reach_rohs("REA_BOS_REACH_RoHS_Konformitaet_2023.docx", "BOS"); written += 1

    # Indirect Rahmenvertraege
    for fname, key in RAHMEN_FILES.items():
        rahmenvertrag_indirekt(fname, key, 2022); written += 1

    # RFQs
    for fname, (lang, kurz) in RFQ_MAP.items():
        jahr = 2023 if "2023" in fname else 2024
        rfq(fname, lang, kurz, jahr); written += 1

    # SPECs
    spec_files = [
        ("SPEC_ADAS-V4D_INF_Komponentenspez_2023.docx", "ADAS-V4D", "INF"),
        ("SPEC_ADAS-V4D_NXP_Komponentenspez_2023.docx", "ADAS-V4D", "NXP"),
        ("SPEC_ADAS-V4D_STM_Komponentenspez_2023.docx", "ADAS-V4D", "STM"),
        ("SPEC_BMS-12_INF_Komponentenspez_2023.docx", "BMS-12", "INF"),
        ("SPEC_BMS-12_NXP_Komponentenspez_2023.docx", "BMS-12", "NXP"),
        ("SPEC_BMS-12_STM_Komponentenspez_2023.docx", "BMS-12", "STM"),
        ("SPEC_ECU-900_INF_Komponentenspez_2023.docx", "ECU-900", "INF"),
        ("SPEC_ECU-900_NXP_Komponentenspez_2023.docx", "ECU-900", "NXP"),
        ("SPEC_ECU-900_STM_Komponentenspez_2023.docx", "ECU-900", "STM"),
        ("SPEC_ICP-3_INF_Komponentenspez_2023.docx", "ICP-3", "INF"),
        ("SPEC_ICP-3_NXP_Komponentenspez_2023.docx", "ICP-3", "NXP"),
        ("SPEC_ICP-3_STM_Komponentenspez_2023.docx", "ICP-3", "STM"),
    ]
    for fname, prod, sup in spec_files:
        komponenten_spec(fname, prod, sup, 2023); written += 1

    # Zoll
    for fname, m in ZOLL_FILES.items():
        zollabfertigung(fname, m, 2023); written += 1

    # One-offs
    gate_review_g1("PRJ-2023-003_Gate_G1_Konzept_ICP-3_OTA_Update_Platform.docx"); written += 1
    rcn_steuerbescheid_2020("RCN_Steuerbescheid_2020.docx"); written += 1
    rsg_br_korrespondenz("RSG_BR_Korrespondenz_Arbeitszeit_Widerspruch_2023.docx"); written += 1
    memo_carbon_neutrality("REA_Memo_Carbon_Neutrality_2030.docx"); written += 1
    bv_arbeitszeit_gleitzeit("REA_BV_Arbeitszeit_Gleitzeit_2022.docx"); written += 1
    governance_report_q1("REA_Konzern_Governance_Report_2022_Q1.docx"); written += 1
    konzernlagebericht_2022("REA_Konzernlagebericht_2022.docx"); written += 1

    print(f"WROTE {written} docs")


if __name__ == "__main__":
    main()
