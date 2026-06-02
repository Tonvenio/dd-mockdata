"""Müller / 05_Vertraege_Lieferanten – 30 thin docs."""
# --- portable-paths-prelude --- (do not edit) ---
import sys
from pathlib import Path as _PathlibPath
_RP = _PathlibPath(__file__).resolve().parent
while not (_RP / "enhance_lib.py").exists() and _RP.parent != _RP:
    _RP = _RP.parent
_ROOT = _RP
sys.path.insert(0, str(_ROOT))
# --- end prelude ---
from enhance_lib import MUELLER as M, write_doc, signatures

BASE = f"{_ROOT}/mueller_small/05_Vertraege_Lieferanten"
H = {"name": M["name"], "addr": M["addr"], "hrb": M["hrb"]}

LIEF = {
    "SCHUNK":  dict(name="Schunk GmbH & Co. KG",            addr="Bahnhofstrasse 106-134, 74348 Lauffen am Neckar"),
    "IGUS":    dict(name="Igus GmbH",                       addr="Spicher Strasse 1a, 51147 Koeln"),
    "SIEMENS": dict(name="Siemens AG, Digital Industries",  addr="Werner-von-Siemens-Strasse 50, 91052 Erlangen"),
    "TRUMPF":  dict(name="Trumpf SE + Co. KG",              addr="Johann-Maus-Strasse 2, 71254 Ditzingen"),
    "FESTO":   dict(name="Festo SE & Co. KG",               addr="Ruiter Strasse 82, 73734 Esslingen am Neckar"),
    "DBSCHEN": dict(name="DB Schenker Deutschland AG",      addr="Edmund-Rumpler-Strasse 3, 60549 Frankfurt am Main"),
    "SAP":     dict(name="SAP SE",                          addr="Dietmar-Hopp-Allee 16, 69190 Walldorf"),
    "TRUMPF_SVC": dict(name="Trumpf Service GmbH (Tochter Trumpf SE)", addr="Johann-Maus-Strasse 2, 71254 Ditzingen"),
    "SCHIND":  dict(name="Schindler Deutschland AG",        addr="Adlerstrasse 7, 65479 Raunheim"),
    "BRUNI":   dict(name="Bruni Elektroanlagen GmbH",       addr="Rather Strasse 49a, 50739 Koeln"),
    "SIEM_SVC": dict(name="Siemens Industry Services GmbH", addr="Otto-Hahn-Ring 6, 81739 Muenchen"),
}


# Bestellungen
def bestellung(fname, lkey, bnr, datum, positionen, summe_netto):
    L = LIEF[lkey]
    write_doc(
        f"{BASE}/{fname}.docx", H,
        f"Bestellung Nr. {bnr}",
        subtitle=f"Bestelldatum: {datum}",
        sections=[
            ("Empfaenger Lieferant",
             f"{L['name']}\n{L['addr']}"),
            ("Bestellpositionen",
             [["Pos", "Material-Nr. Lieferant", "Beschreibung", "Menge", "Einheit", "Einzelpreis EUR", "Gesamt EUR"]] + positionen +
             [["", "", "Zwischensumme netto", "", "", "", f"{summe_netto:,}".replace(',','.')+",00"],
              ["", "", "Umsatzsteuer 19 %", "", "", "", f"{round(summe_netto*0.19):,}".replace(',','.')+",00"],
              ["", "", "GESAMT brutto", "", "", "", f"{round(summe_netto*1.19):,}".replace(',','.')+",00"]]),
            ("Liefer- und Zahlungsbedingungen",
             "Lieferung: DAP Werk Koeln (INCOTERMS 2020) gemaess Standard-EKBs der Halbreiter Maschinenbau GmbH. "
             "Zahlungsziel: 30 Tage netto bzw. 2 % Skonto bei Zahlung binnen 14 Tagen.\n\n"
             "Lieferadresse: Halbreiter Maschinenbau GmbH, Wareneingang Halle C, Industriestrasse 12, 50829 Koeln, "
             "Tor 3, Anlieferzeiten Mo-Fr 07:00-15:00 Uhr.\n\n"
             "Versandfertigmeldung (ASN) bitte 24 Std. vor Eintreffen per EDI an asn@halbreiter-maschinenbau.de "
             "(EDIFACT DESADV-Format)."),
            ("Qualitaet und Compliance",
             "Erstmusterpruefbericht (Erstmuster gemaess VDA Band 2) ist mit der Erstlieferung beizustellen. "
             "Materialzertifikate (3.1 nach EN 10204 fuer Werkstoffe) auf Anforderung. "
             "Es gelten die Allgemeinen Einkaufsbedingungen Halbreiter Maschinenbau GmbH (Stand 1.1.2024). "
             "Lieferketten-Sorgfaltspflicht gemaess LkSG ist anzuerkennen."),
            ("Bearbeitung",
             "Sachbearbeiter Einkauf: Stefan Braun, Telefon +49 221 47832-22, "
             "s.braun@halbreiter-maschinenbau.de. Kostenstelle: lt. Lieferschein."),
        ],
    )


bestellung("LF_B001_Bestellung_Schunk_GmbH_und_C", "SCHUNK", "BE-2024-01-0142", "12. Januar 2024",
           [["1", "PGN-PLUS-P-200", "Kraftspannblock pneumatisch 200 mm",      "8",  "St.",  "1.580,00", "12.640,00"],
            ["2", "PZB-PLUS-160",   "Parallelgreifer 160 mm",                  "12", "St.",  "892,00",  "10.704,00"],
            ["3", "MMS-22-S-PNP",   "Magnetfeldsensor M8x1 PNP",               "48", "St.",   "78,00",   "3.744,00"]],
           27088)
bestellung("LF_B002_Bestellung_Igus_GmbH",         "IGUS",   "BE-2024-01-0148", "18. Januar 2024",
           [["1", "E14.4.038.50", "Energiekette 14er, Innenbreite 38 mm, Laenge 1500 mm", "12", "St.", "245,00", "2.940,00"],
            ["2", "TRE.50.50.075","Polymerleitung 50x50 mm", "240", "m", "32,40", "7.776,00"],
            ["3", "CFROBOT5",     "Robotik-Hochflexkabel CFRobot5", "180", "m", "28,40", "5.112,00"]],
           15828)
bestellung("LF_B003_Bestellung_Siemens_AG_–_An",  "SIEMENS","BE-2024-02-0184", "8. Februar 2024",
           [["1", "6SL3210-5HE17-0KF0", "SINAMICS S210 Servo 7,0 A", "6", "St.", "3.420,00", "20.520,00"],
            ["2", "1FK7080-5AF71-1RG0", "Servomotor SIMOTICS 1FK7", "6", "St.", "2.840,00", "17.040,00"],
            ["3", "6SL3055-0AA00-3AA0", "Optionsbaugruppe CBC10 Kommunikation", "6", "St.", "385,00", "2.310,00"]],
           39870)
bestellung("LF_B004_Bestellung_Trumpf_SE_plus_Co.","TRUMPF", "BE-2024-02-0212", "22. Februar 2024",
           [["1", "TRUDISK-8002-FW", "Faserlaser 8 kW Resonator + Strahlfuehrung", "1", "St.", "245.000,00", "245.000,00"],
            ["2", "BC-040-LASKOPF",  "Laserschneidkopf BC-040",                    "1", "St.",  "42.000,00",  "42.000,00"],
            ["3", "FILTER-PREMIUM",  "Filterpaket Hochleistung 4-stufig",          "1", "St.",   "8.400,00",   "8.400,00"]],
           295400)
bestellung("LF_B005_Bestellung_Schunk_GmbH_und_C", "SCHUNK", "BE-2024-03-0241", "12. Maerz 2024",
           [["1", "VERO-S-NSL-160", "Schnellwechselsystem VERO-S NSL 160", "4", "St.", "2.180,00", "8.720,00"],
            ["2", "RWA-9-180", "Robotik-Werkzeugadapter RWA 180", "8", "St.", "920,00", "7.360,00"],
            ["3", "KSP-LH-160", "Kraftspannblock Hochkraft 160", "2", "St.", "3.180,00", "6.360,00"]],
           22440)


# Eingangsrechnungen
def er(fname, lkey, re_nr, datum, posbez, netto, bestellref):
    L = LIEF[lkey]
    write_doc(
        f"{BASE}/{fname}.docx", H,
        f"Eingangsrechnung – {L['name']}",
        subtitle=f"Rechnungsnr. Lieferant: {re_nr}, Datum: {datum}",
        sections=[
            ("Lieferantendaten",
             f"{L['name']}\n{L['addr']}\nUSt-IdNr.: hinterlegt in Lieferantenstammdatensatz / SAP Konto-Nr. 7000xxxx"),
            ("Rechnungspositionen",
             [["Pos", "Beschreibung", "Menge", "Einheit", "Einzelpreis EUR", "Gesamt EUR"],
              ["1", posbez, "1", "psch.", f"{netto:,}".replace(',','.')+",00", f"{netto:,}".replace(',','.')+",00"],
              ["", "Zwischensumme netto", "", "", "", f"{netto:,}".replace(',','.')+",00"],
              ["", "Umsatzsteuer 19 %", "", "", "", f"{round(netto*0.19):,}".replace(',','.')+",00"],
              ["", "GESAMT brutto", "", "", "", f"{round(netto*1.19):,}".replace(',','.')+",00"]]),
            ("Buchung und Pruefung",
             f"Bezug: Bestellung Nr. {bestellref}. Wareneingangsbuchung in SAP MM erfolgte am Tag der "
             f"Anlieferung; sachliche Pruefung durch Stefan Braun (Einkauf), rechnerische Pruefung durch "
             f"Petra Zimmermann (Buchhaltung).\n\n"
             f"Zahlungsbedingung gemaess Rahmenvereinbarung: 30 Tage netto bzw. 2 % Skonto bei Zahlung "
             f"binnen 14 Tagen. Die Zahlung erfolgt automatisch ueber den Zahllauf SAP F110 am 25. des "
             f"Folgemonats.\n\n"
             f"Steuerschluessel V1 (Inland 19 % Vorsteuer); Buchung auf Sachkonto entsprechend Materialgruppe."),
        ],
    )

er("LF_ER001_Eingangsrechnung_Schunk_GmbH_und_Co._", "SCHUNK", "SCH-2024-001142", "20. Januar 2024",
   "Greifer und Sensorik gemaess Bestellung", 27088, "BE-2024-01-0142")
er("LF_ER002_Eingangsrechnung_Igus_GmbH",            "IGUS",   "IGU-2024-008412", "26. Januar 2024",
   "Energiekette / Flexkabel", 15828, "BE-2024-01-0148")
er("LF_ER003_Eingangsrechnung_Siemens_AG_–_Antri",   "SIEMENS","SIE-2024-002841", "18. Februar 2024",
   "SINAMICS S210 / SIMOTICS Servoantriebe", 39870, "BE-2024-02-0184")
er("LF_ER004_Eingangsrechnung_Trumpf_SE_plus_Co._KG","TRUMPF", "TRU-2024-014812", "10. Maerz 2024",
   "Faserlaser-Resonator und Schneidkopf BC-040", 295400, "BE-2024-02-0212")
er("LF_ER005_Eingangsrechnung_Schunk_GmbH_und_Co._", "SCHUNK", "SCH-2024-002012", "22. Maerz 2024",
   "Schnellwechselsystem VERO-S", 22440, "BE-2024-03-0241")
er("LF_ER006_Eingangsrechnung_Siemens_AG_–_Antri",   "SIEMENS","SIE-2024-008412", "14. April 2024",
   "Wartungspauschale Q1 SINUMERIK + Updates", 18200, "Pauschalvertrag SLA001")
er("LF_ER007_Eingangsrechnung_Igus_GmbH",            "IGUS",   "IGU-2024-014212", "22. April 2024",
   "Energiekette / Werkzeugschlauchpaket", 9420, "BE-2024-04-0312")
er("LF_ER008_Eingangsrechnung_Trumpf_SE_plus_Co._KG","TRUMPF", "TRU-2024-026841", "12. Mai 2024",
   "Vor-Ort-Service Faserlaser 2 Tage", 6840, "Pauschalvertrag SLA003")


# Rahmenvertraege (LF_001 … 004) + LF_Rahmenvertrag_Festo_SE
def rahmenvertrag(fname, lkey, vol_eur_p_a, kategorie, schwerpunkt, laufzeit="36 Monate"):
    L = LIEF[lkey]
    write_doc(
        f"{BASE}/{fname}.docx", H,
        f"Rahmen-Liefervertrag – {L['name']}",
        subtitle=f"Kategorie: {kategorie}; Schwerpunkt: {schwerpunkt}; Laufzeit: {laufzeit}",
        sections=[
            ("Vertragsparteien",
             f"Auftraggeberin: Halbreiter Maschinenbau GmbH, HRB 47312 AG Koeln.\n\n"
             f"Lieferantin: {L['name']}, {L['addr']}."),
            ("Praeambel",
             f"Die Halbreiter Maschinenbau GmbH bezieht ueber einen Jahreshorizont rund {vol_eur_p_a:,}".replace(',','.') +
             f" EUR an {kategorie}. Mit diesem Rahmenvertrag werden die kaufmaennischen, technischen und "
             f"qualitativen Bedingungen fuer Einzelbestellungen einheitlich festgelegt. "
             f"Schwerpunkt: {schwerpunkt}."),
            ("Vertragsregelungen",
             ("clauses", [
                 ("§ 1 Vertragsgegenstand", [
                     "Gegenstand sind sukzessive Einzelbestellungen, die unter diesem Rahmenvertrag "
                     "abgerufen werden. Die in den jeweiligen Bestellungen genannten Positionen sind "
                     "verbindlich.",
                     "Eine bestimmte Mindestabnahme ist nicht zugesichert; sofern eine sog. "
                     "»Take-or-Pay«-Verpflichtung gewuenscht ist, wird dies in Anhang 2 separat geregelt.",
                 ]),
                 ("§ 2 Preise und Konditionen", [
                     "Preise gemaess Preisliste Anhang 1; Preisanpassung jaehrlich (Stahl-/Aluminium-Index, "
                     "Lohnentwicklung gemaess M+E NRW). Bei > +/- 5 % Index-Sprung Sondervorlauf.",
                     "Skonto: 2 % bei Zahlung binnen 14 Tagen; 30 Tage netto. Mengenrabattstaffel siehe "
                     "Anhang 1.",
                 ]),
                 ("§ 3 Forecast / EDI / SCM-Anbindung", [
                     "Halbreiter Maschinenbau GmbH stellt rollierend einen 6-Monats-Forecast bereit. "
                     "Bestelluebermittlung erfolgt ueber EDIFACT (ORDERS, DESADV, INVOIC) oder OPC-UA. "
                     "Eine VMI-Vereinbarung (Vendor-Managed-Inventory) wird im Bedarfsfall separat geschlossen.",
                 ]),
                 ("§ 4 Qualitaet / Erstmuster / Audit", [
                     "Erstmusterpruefberichte gemaess VDA Band 2; Q-Audits im 24-Monats-Rhythmus. "
                     "Bei Reklamationsquote > 0,5 % automatische Reaktivierung der erweiterten Eingangskontrolle.",
                 ]),
                 ("§ 5 Lieferung / Logistik", [
                     "DAP Werk Koeln (INCOTERMS 2020); Anlieferung Tor 3 Halle C; ASN 24 Std. vorab.",
                 ]),
                 ("§ 6 Gewaehrleistung / Haftung", [
                     "Gewaehrleistung 36 Monate ab Wareneingang. Haftung begrenzt auf 200 % des "
                     "Vertragswertes pro Schadensereignis; ausgenommen Vorsatz, grobe Fahrlaessigkeit, "
                     "Personenschaeden und Produkthaftung.",
                 ]),
                 ("§ 7 Compliance / Lieferkette", [
                     "Anerkennung Code of Conduct (Anhang 3) und LkSG-Erklaerung. Sub-Tier-Bekanntgabe "
                     "auf Anforderung. Bei Verdacht auf Sanktionsverstoss sofortige Information.",
                 ]),
                 ("§ 8 Vertraulichkeit", [
                     "Saemtliche Daten und Konstruktionszeichnungen sind vertraulich; eine separate NDA "
                     "(Anhang 4) gilt.",
                 ]),
                 ("§ 9 Laufzeit / Kuendigung", [
                     f"{laufzeit}, danach Verlaengerung um 12 Monate (Kuendigung 6 Monate vorab). "
                     "Ausserordentliche Kuendigung bei wesentlichen Vertragsverstoessen.",
                 ]),
                 ("§ 10 Schlussbestimmungen", [
                     "Es gilt deutsches Recht; Gerichtsstand Koeln.",
                 ]),
             ])),
            ("Anhaenge",
             "1: Preisliste / Konditionen\n2: Take-or-Pay (sofern relevant)\n3: Code of Conduct MMB\n4: NDA"),
            ("Unterschriften",
             signatures("Sandra Becker", "CFO", M["name"],
                        "Verkaufsleitung", "i. e. S.", L["name"],
                        place="Koeln / " + L["addr"].split(",")[-1].strip(), date_str_="—")),
        ],
    )


rahmenvertrag("LF_001_Rahmenvertrag_Schunk_GmbH_und_Co._KG", "SCHUNK", 1_400_000,
              "Greifsysteme, Spanntechnik und Sensorik", "Vorzugslieferant Greifer & Sensorik")
rahmenvertrag("LF_002_Rahmenvertrag_Igus_GmbH", "IGUS", 380_000,
              "Energiezufuehrungssysteme und Polymerlager", "Wartungsfreie Polymer-Komponenten")
rahmenvertrag("LF_003_Rahmenvertrag_Siemens_AG_–_Antrieb", "SIEMENS", 2_300_000,
              "Antriebs- und Steuerungstechnik (SINUMERIK / SIMATIC / SINAMICS)",
              "Strategischer Lieferant – Tier A")
rahmenvertrag("LF_004_Rahmenvertrag_Trumpf_SE_plus_Co._KG", "TRUMPF", 1_900_000,
              "Faserlaser-Resonatoren, Schneidkoepfe, Wartung", "Schluessellieferant Laser")
rahmenvertrag("LF_Rahmenvertrag_Festo_SE", "FESTO", 420_000,
              "Pneumatik- und Automatisierungstechnik", "Pneumatik-Standardisierung")


# Service-Level-Agreements (Wartungsvertraege)
def sla(fname, lkey, fokus, jahresvol_eur, sla_text_extra=""):
    L = LIEF[lkey]
    write_doc(
        f"{BASE}/{fname}.docx", H,
        f"Service-Level-Agreement – {L['name']}",
        subtitle=f"Wartung / Service: {fokus}",
        sections=[
            ("Vertragsparteien",
             f"Auftraggeberin: Halbreiter Maschinenbau GmbH.\n\nDienstleisterin: {L['name']}, {L['addr']}."),
            ("Leistungsbeschreibung",
             f"Der Dienstleister erbringt die nachfolgenden Leistungen im Bereich »{fokus}«. "
             f"Die Vergutung erfolgt als jaehrliche Pauschale in Hoehe von {jahresvol_eur:,}".replace(',','.') +
             f" EUR (netto) zzgl. USt., zahlbar quartalsweise zu Beginn des Quartals."),
            ("Service-Level",
             [
                 ["Prioritaet", "Definition", "Reaktion telefonisch", "Reaktion vor Ort", "Wiederherstellung"],
                 ["P1 Stillstand", "Anlage steht", "1 Std.", "8 Std.", "24 Std."],
                 ["P2 Funktionseinschraenkung", "reduzierte Leistung", "4 Std.", "24 Std.", "5 WT"],
                 ["P3 Geplante Wartung / KVP", "Standard", "1 WT", "5 WT", "10 WT"],
             ]),
            ("Inhalt",
             "Inkludiert sind: praeventive Wartungen gemaess Wartungsplan (mind. 1x p. a.); Software- und "
             "Firmware-Updates; telefonische Hotline (Mo-Fr 07:00-19:00 Uhr); Online-Diagnose via "
             "Remote-Zugang (VPN, Reverse-Proxy); Verwendung von Originalersatzteilen; Dokumentation der "
             "Eingriffe im Anlagenstammdatensatz und im SAP-Anlagenstamm.\n\n"
             "Nicht inkludiert: Aenderungsservice und Umbauten; Schaeden infolge nicht autorisierter Eingriffe; "
             "Verbrauchsmaterialien (z. B. Filter, Schmieroele). " + sla_text_extra),
            ("Berichtswesen",
             "Quartalsweiser Service-Report mit Aufstellung der durchgefuehrten Einsaetze, Verbrauch von "
             "Verschleissteilen, Erfuellungsgrad der Service-Level (SLA-Score). Jaehrliches Review-Meeting "
             "im Februar. Eskalationsstufen: Service-Koordinator -> Servicemanager Stefan Bauer (MMB) -> "
             "Geschaeftsleitung."),
            ("Laufzeit / Kuendigung",
             "Laufzeit 24 Monate, Verlaengerung um jeweils 12 Monate (Kuendigung 6 Monate vorab). "
             "Ausserordentliche Kuendigung bei wiederholtem Versagen der SLA-Erfuellung (3 P1-Verstoesse "
             "binnen 12 Monaten)."),
        ],
    )


sla("LF_SLA001_Wartung_Siemens_Industry_Ser",   "SIEM_SVC", "SINUMERIK ONE / TIA Portal Lizenzwartung + Hotline", 78_000)
sla("LF_SLA002_Wartung_SAP_SE_Maintenance",     "SAP",      "SAP S/4HANA Standard-Wartung und Cloud-Services",     320_000,
    "Eine separate Service-Beschreibung gemaess SAP CSPS / Cloud Service Schedule liegt bei.")
sla("LF_SLA003_Wartung_Trumpf_Service_GmbH",    "TRUMPF_SVC","Faserlaser-Wartung (TRUMPF TruLaser & TruDisk)",      118_000)
sla("LF_SLA004_Wartung_Schindler_Deutschlan",   "SCHIND",    "Aufzugswartung (3 Aufzuege Verwaltung / Halle)",       18_000)
sla("LF_SLA005_Wartung_Bruni_Elektroanlagen",   "BRUNI",     "Elektroinstallation / NSHV-Wartung Werk Koeln",        24_000)


# Weitere Lieferantendokumente -------------------------------------------------
write_doc(
    f"{BASE}/LF_Zollpräferenznachweis_2023.docx", H,
    "Praeferenznachweis 2023 – Lieferantenerklaerung gemaess UCC / VO (EU) 2015/2447",
    subtitle="Erklaerung des Praeferenzursprungs der Vorerzeugnisse",
    sections=[
        ("Erklaerender",
         "Halbreiter Maschinenbau GmbH, Industriestrasse 12, 50829 Koeln; Reg-EORI Nr.: DEAEO112543200."),
        ("Erklaerung",
         "Wir bestaetigen, dass die nachstehend aufgefuehrten Erzeugnisse die Praeferenzursprungs-Regeln "
         "erfuellen und Ursprungserzeugnisse Europaeische Union (EU) im Sinne der Praeferenzabkommen sind, "
         "die zwischen der EU und folgenden Laendern bestehen: Schweiz, Norwegen, Vereinigtes Koenigreich, "
         "Mexiko, Kanada, Suedkorea, Japan, Singapur sowie EFTA-Staaten."),
        ("Erfasste Erzeugnisse",
         [
             ["Materialklasse", "HS-Code", "Erfasste Position", "Geltung"],
             ["Pressenlinien PL-500 und Module", "8462 39 10", "Lieferungen 2023", "Praeferenz EU-Mexiko / EU-UK"],
             ["Foerderbaender FB-200 und Module", "8428 33 00", "Lieferungen 2023", "Praeferenz EU-CH / EU-NO"],
             ["Laserschneidanlagen LS-800", "8456 12 00", "Lieferungen 2023", "Praeferenz EU-JP / EU-KR"],
             ["Robotik-Zellen MR-150", "8479 50 00", "Lieferungen 2023", "Praeferenz EU-UK / EU-SG"],
         ]),
        ("Gueltigkeit / Aufbewahrung",
         "Diese Lieferantenerklaerung gilt fuer alle Lieferungen mit Versanddatum im Kalenderjahr 2023. "
         "Sie kann auf Anforderung der Kunden in elektronischer Form (PDF mit qualifizierter Signatur) zur "
         "Verfuegung gestellt werden. Die Aufbewahrungsfrist gemaess UCC betraegt 3 Jahre."),
        ("Erklaerung",
         "Ich verpflichte mich, eventuelle Aenderungen der Eigenschaften der genannten Waren unverzueglich "
         "den Kunden anzuzeigen. Vorsaetzliche oder fahrlaessige Falscherklaerungen koennen zu Strafverfolgung "
         "fuehren."),
        ("Unterschrift",
         signatures("Stefan Braun", "Leiter Strategischer Einkauf", M["name"],
                    "Sandra Becker", "Geschaeftsfuehrerin / CFO", M["name"],
                    place="Koeln", date_str_="15. Januar 2024")),
    ],
)


write_doc(
    f"{BASE}/LF_Lieferantenbewertung_2023.docx", H,
    "Lieferantenbewertung 2023",
    subtitle="Jaehrliches Lieferanten-Scoring, ausgewertet 31. Januar 2024",
    sections=[
        ("Methodik",
         "Bewertung der 24 strategischen Lieferanten in vier Dimensionen mit folgenden Gewichtungen: "
         "Qualitaet (35 %), Liefertreue (30 %), Preis-Leistungs-Verhaeltnis (20 %), Service / Kommunikation "
         "(15 %). Bewertung 5-stufig (5 = sehr gut). Ergebnis-Klassifikation: A (≥ 4,5), B (3,5-4,5), C (< 3,5)."),
        ("Top-10-Lieferanten",
         [
             ["Lieferant", "Q", "LT", "P/L", "Service", "Score", "Klasse"],
             ["Schunk GmbH & Co. KG", "4,8", "4,7", "4,2", "4,6", "4,6", "A"],
             ["Trumpf SE + Co. KG", "4,8", "4,6", "3,8", "4,7", "4,5", "A"],
             ["Siemens AG, Digital Industries", "4,7", "4,5", "4,0", "4,5", "4,4", "B"],
             ["Igus GmbH", "4,6", "4,8", "4,5", "4,4", "4,6", "A"],
             ["Festo SE & Co. KG", "4,5", "4,6", "4,4", "4,3", "4,5", "A"],
             ["SAP SE", "4,3", "4,2", "3,4", "4,2", "4,0", "B"],
             ["DB Schenker Deutschland AG", "4,1", "4,3", "4,2", "4,1", "4,2", "B"],
             ["Schindler Deutschland AG", "4,4", "4,5", "4,2", "4,3", "4,3", "B"],
             ["Sensirion AG (Schweiz)", "4,7", "4,3", "4,2", "4,3", "4,4", "B"],
             ["SEW-EURODRIVE GmbH & Co KG", "4,6", "4,5", "4,1", "4,4", "4,4", "B"],
         ]),
        ("Massnahmen 2024",
         "(a) Vereinbarung jaehrlicher Auditierung mit B-Klasse-Lieferanten oberhalb 500 TEUR Jahresvolumen. "
         "(b) Erweiterung der Zweitquellenstrategie fuer kritische Komponenten (Antriebselektronik, Sensorik). "
         "(c) Aufnahme von Nachhaltigkeitskriterien (CO2-Fussabdruck Werk, ESG-Reporting) ab Q3/2024."),
    ],
)


write_doc(
    f"{BASE}/LF_Lieferantenaudit_Schunk_2023.docx", H,
    "Lieferantenaudit – Schunk GmbH & Co. KG (2023)",
    subtitle="Audit gemaess VDA 6.3, durchgefuehrt 11.-12. Juli 2023, Werk Lauffen am Neckar",
    sections=[
        ("Auditteam",
         "Auditleitung Halbreiter Maschinenbau GmbH: Stefan Braun (Einkaufsleitung), begleitet von Klaus Bauer "
         "(Logistikleitung, Wareneingang) und Andreas Goebel (Qualitaetsmanagement). Auditierte Werke: "
         "Lauffen am Neckar (Hauptwerk). Auditierte Prozesse: Beschaffung, Produktion, Pruefung, Logistik."),
        ("Ergebnis",
         "Gesamtbewertung VDA 6.3: 91,4 % (A-Lieferant). Zwei kleinere Nicht-Konformitaeten: "
         "(1) Erstmuster-Doku Position SG-201 nicht in der vorgegebenen Form (gepruefte Korrektur);\n\n"
         "(2) Reklamations-Reaktion in einem Fall ueber Zielzeit. Behebungstermin: 30. September 2023; "
         "fristgerecht abgeschlossen."),
        ("Empfehlungen",
         ("list", [
             "Erweiterung des Stichprobenumfangs bei Wareneingangskontrolle Greifer-Komponenten",
             "Einfuehrung einer monatlichen Q-Reklamations-Rate KPI im Lieferanten-Cockpit (SAP Lieferanten-Stamm)",
             "Pruefung Aufnahme von Schunk in das Programm »Preferred Supplier Engineering Co-Innovation«",
         ])),
        ("Folgemassnahmen / Aktionen",
         "Schunk uebernimmt die Korrekturmassnahmen schriftlich; Re-Audit (verkuerzt) am 15.11.2023 erfolgreich. "
         "Naechstes Vollaudit: 24 Monate Rhythmus, geplant Q3/2025."),
    ],
)


write_doc(
    f"{BASE}/LF_Preferred_Supplier_Siemens_2023.docx", H,
    "Preferred-Supplier-Vereinbarung – Siemens AG, Digital Industries (2023)",
    subtitle="Strategische Lieferantenvereinbarung gueltig 1. Juli 2023 bis 30. Juni 2026",
    sections=[
        ("Praeambel",
         "Die Halbreiter Maschinenbau GmbH und die Siemens AG (Digital Industries) bestehen seit ueber zwei "
         "Jahrzehnten in einer engen Lieferanten-Kunden-Partnerschaft im Bereich Antriebstechnik und Steuerungen "
         "(SINUMERIK, SIMATIC, SINAMICS). Mit dieser Preferred-Supplier-Vereinbarung wird der strategische "
         "Charakter dieser Beziehung gefestigt."),
        ("Vereinbarungen",
         ("list", [
             "Siemens stellt einen dedizierten Key Account Engineer (Frau Dr. Sabine Erlmeier) zur Verfuegung.",
             "Vorrangige Beteiligung an Co-Engineering-Projekten (Pressen 4.0, Predictive Maintenance Plattform).",
             "Vorzugsrabatt 6 % auf Listenpreis fuer Standardpositionen; Tageshandling-Pauschalen reduziert.",
             "Forecast-getriebene Sichtbarkeit (12 Monate) ueber Siemens SCM Cloud.",
             "Eskalations-Hotline (Reaktion 2 Std., 24/7).",
             "Gemeinsamer KPI-Bericht quartalsweise.",
         ])),
        ("Co-Innovation-Roadmap",
         "Drei gemeinsame Projekte im Backlog: (1) Predictive Maintenance auf PL-500 (Pilot ThyssenKrupp); "
         "(2) Edge-Computing Plattform fuer FB-200 (Industrial Edge); (3) Cybersecurity-Studie OT-Netzwerk "
         "(Defender for OT). Gesamtbudget der Pilotphasen: 480.000 EUR (Foerderquote BMWi 30 %)."),
        ("Laufzeit",
         "1. Juli 2023 bis 30. Juni 2026. Automatische Verlaengerung um 12 Monate, soweit nicht 6 Monate "
         "vor Ablauf gekuendigt."),
        ("Unterschriften",
         signatures("Stefan Braun", "Leiter Strategischer Einkauf", M["name"],
                    "Dr. Sabine Erlmeier", "Senior Key Account Manager", "Siemens AG",
                    place="Koeln / Erlangen", date_str_="20. Juni 2023")),
    ],
)


write_doc(
    f"{BASE}/LF_Rahmenvertrag_Leasing_Trumpf.docx", H,
    "Rahmenvereinbarung Maschinen-Leasing – Trumpf Financial Services GmbH (2023)",
    subtitle="Operating-Lease ueber Laser- und Stanzmaschinen, Stand 8. Mai 2023",
    sections=[
        ("Parteien",
         "Leasinggeberin: Trumpf Financial Services GmbH, Johann-Maus-Str. 2, 71254 Ditzingen. "
         "Leasingnehmerin: Halbreiter Maschinenbau GmbH."),
        ("Gegenstand",
         "Operating-Lease zur Refinanzierung der Maschinen Trumpf TruLaser 3030 fiber sowie TruDisk 8001 fiber "
         "im Wert von 2,4 Mio. EUR. Die Maschinen verbleiben im Eigentum der Leasinggeberin; Buchung der "
         "Leasingraten als Aufwand (off-balance gemaess HGB-Wahlrecht; IFRS 16: nicht relevant, da HGB-Abschluss)."),
        ("Konditionen",
         "Leasingrate: 38.420 EUR netto monatlich; Laufzeit 60 Monate; Kaufoption am Ende zum Restwert "
         "240.000 EUR. Wartung inklusive (durch Trumpf Service GmbH gemaess separatem SLA LF_SLA003).\n\n"
         "Versicherung: Maschinenbruchversicherung ueber Allianz SE (Standardbedingungen Industrieversicherung)."),
        ("Sonderbestimmungen",
         "Vorzeitige Rueckgabe zulaessig ab Monat 36 unter Zahlung einer Aufloesungsgebuehr in Hoehe von "
         "12 Monatsraten. Verlaengerungsoption um 12 Monate bei reduzierter Rate (-25 %). "
         "Standortverlagerung der Maschinen nur mit schriftlicher Zustimmung der Leasinggeberin."),
        ("Unterschriften",
         signatures("Sandra Becker", "CFO", M["name"],
                    "Markus Helmer", "Senior Account Manager", "Trumpf Financial Services GmbH",
                    place="Koeln / Ditzingen", date_str_="8. Mai 2023")),
    ],
)


write_doc(
    f"{BASE}/LF_Rahmenvertrag_Logistik_DB_Schenker.docx", H,
    "Rahmenvertrag Logistik 2023-2026 – DB Schenker Deutschland AG",
    subtitle="Gueltig ab 1. April 2023",
    sections=[
        ("Parteien", "Halbreiter Maschinenbau GmbH und DB Schenker Deutschland AG."),
        ("Leistungsumfang",
         "(1) Inlandtransporte (Stueckgut / Teilladung / Komplettladung) DE / EU; "
         "(2) See- und Lufttransporte fuer Exportauftraege (insb. Mexiko, Mercosur, MENA, ASEAN); "
         "(3) Zollabwicklung Ausfuhr / Einfuhr (Bevollmaechtigter Zollvertreter); "
         "(4) Projektlogistik fuer Schwertransporte (Pressenlinien PL-500 > 80 t)."),
        ("Konditionen",
         "Tarife gemaess Anhang 1 (Strecke / Gewichts-/Volumenklassen); Sondertarife fuer "
         "Schwertransporte. Skonto 2 % bei 14 Tagen; 30 Tage netto. Servicegrad: 95 % On-Time-Delivery; "
         "Vertragsstrafe 250 EUR pro Stunde Verspaetung bei P1-Sendungen.\n\nVersicherung: Verkehrshaftungs"
         "versicherung gemaess HGB / CMR. Wertgutbescheinigung fuer Sondertransporte > 500.000 EUR."),
        ("Zoll und Compliance",
         "DB Schenker uebernimmt die Zollanmeldung als Bevollmaechtigte; AEO-C Bewilligung Halbreiter Maschinenbau "
         "GmbH wird mitgenutzt. Sanktionspruefung saemtlicher Sendungen vor Verzollung; Dual-Use-Position "
         "wird im Rahmen der Exportkontrolle gepruft (vgl. COMP_Exportkontrollbericht_2023)."),
        ("Laufzeit / Kuendigung",
         "1.4.2023 bis 31.3.2026, Verlaengerung +12 Monate, Kuendigung 6 Monate vorab. "
         "Ausserordentliche Kuendigung bei wiederholten Performance-Verstoessen."),
    ],
)


write_doc(
    f"{BASE}/LF_Rahmenvertrag_Einkauf_Allgemein_2023.docx", H,
    "Allgemeiner Einkaufsrahmenvertrag 2023 – Sammelvereinbarung Nicht-A-Lieferanten",
    subtitle="Sammelvereinbarung fuer indirekte Bedarfe (MRO, Buero, Reinigung, Werkzeuge)",
    sections=[
        ("Geltung",
         "Diese Vereinbarung kommt fuer alle nicht in spezifischen Rahmenvertraegen geregelten Bedarfe zur "
         "Anwendung (MRO, indirekte Bedarfe, Werkzeuge, Bueromaterial, Reinigungsmittel, etc.) und gilt "
         "fuer Bestellungen ueber das interne Beschaffungsportal (ARIBA-Spend). Eine Lieferantenfreigabe "
         "erfolgt nur fuer als zugelassen markierte Lieferanten."),
        ("Standardkonditionen",
         "Zahlungsziel 30 Tage netto / 2 % Skonto 14 Tage; Lieferung DAP Werk Koeln; "
         "Aufnahmebescheinigung (»Conformity of Delivery«) am Wareneingang; Pflicht zur ASN; Beachtung der "
         "Allgemeinen Einkaufsbedingungen MMB (Stand 1.1.2024)."),
        ("Compliance",
         "Lieferant verpflichtet sich auf Einhaltung des LkSG, der Antikorruptionsrichtlinie sowie der "
         "GDPR. Geschenke und Zuwendungen oberhalb 50 EUR sind unzulaessig. Sub-Tier-Bekanntgabe auf "
         "Anforderung. Sanktionspruefung erfolgt zentralisiert ueber das Tool »ComplyCube«."),
        ("Eskalation und Streitbeilegung",
         "Bei Performance-Maengeln: Stufe 1 Sachbearbeiter -> Stufe 2 Stefan Braun -> Stufe 3 GF MMB. "
         "Streitbeilegung in Koeln nach deutschem Recht."),
        ("Laufzeit",
         "Vertrag laeuft unbefristet; Anpassungen veroeffentlicht MMB ueber das Lieferantenportal."),
    ],
)


print("OK regen_mueller_05.py – 30 docs written")
