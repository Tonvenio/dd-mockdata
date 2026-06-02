"""Müller / 04_Vertraege_Kunden – 34 thin docs."""
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

BASE = f"{_ROOT}/mueller_small/04_Vertraege_Kunden"
H = {"name": M["name"], "addr": M["addr"], "hrb": M["hrb"]}

# Canonical customer data
KUNDEN = {
    "TKSE":     dict(name="ThyssenKrupp Steel Europe AG",      addr="Kaiser-Wilhelm-Strasse 100, 47166 Duisburg",   kn="K-001"),
    "BOSCH":    dict(name="Bosch Rexroth AG",                  addr="Zum Eisengiesser 1, 97816 Lohr am Main",        kn="K-002"),
    "HELLA":    dict(name="Hella GmbH & Co. KGaA",             addr="Rixbecker Strasse 75, 59552 Lippstadt",         kn="K-003"),
    "VIES":     dict(name="Viessmann Climate Solutions SE",    addr="Viessmannstrasse 1, 35108 Allendorf (Eder)",    kn="K-004"),
    "DUERR":    dict(name="Dürr AG",                            addr="Carl-Benz-Strasse 34, 74321 Bietigheim-Bissingen", kn="K-005"),
    "HAVER":    dict(name="Haver & Boecker OHG",               addr="Carl-Haver-Platz 3, 59302 Oelde",               kn="K-006"),
    "NIEH":     dict(name="Maschinenfabrik Niehoff GmbH & Co. KG", addr="Walzwerkstrasse 20, 91126 Schwabach",       kn="K-007"),
    "HEYL":     dict(name="Gebr. Heyl GmbH & Co. KG",          addr="Max-Planck-Strasse 12, 31135 Hildesheim",       kn="K-008"),
}


# Auftragsbestaetigungen ------------------------------------------------------
def auftragsbestaetigung(fname, kunde_key, ab_nr, datum, projekt_titel, lieferadresse,
                          positionen, summe_netto, liefertermin, zahlungskondition="14 Tage netto"):
    K = KUNDEN[kunde_key]
    write_doc(
        f"{BASE}/{fname}.docx", H,
        f"Auftragsbestaetigung Nr. {ab_nr}",
        subtitle=f"Bestellung des Kunden {K['name']} vom {datum}",
        sections=[
            ("Kundendaten",
             f"{K['name']}\n"
             f"{K['addr']}\n"
             f"Kundennummer: {K['kn']}\n"
             f"Bestellung Nr. (Ihrer Referenz): siehe Anlage 1\n"
             f"Auftragsbestaetigung Nr.: {ab_nr}\n"
             f"Datum: {datum}\n"
             f"Lieferadresse: {lieferadresse}"),
            ("Sehr geehrte Damen und Herren,",
             f"wir bestaetigen Ihren Auftrag »{projekt_titel}« in der nachfolgend gelisteten Form. "
             f"Sofern in den nachfolgenden Bestimmungen oder unseren beigefuegten Allgemeinen "
             f"Verkaufs- und Lieferbedingungen (AVB Stand 1.1.2024) nichts Abweichendes geregelt ist, "
             f"gilt der zugrundeliegende Rahmenvertrag zwischen unseren Haeusern."),
            ("Auftragspositionen",
             [["Pos", "Material-Nr.", "Beschreibung", "Menge", "Einheit", "Einzelpreis EUR", "Gesamt EUR"]] + positionen +
             [["", "", "Zwischensumme netto", "", "", "", f"{summe_netto}"],
              ["", "", "Umsatzsteuer 19 %", "", "", "", f"{round(summe_netto*0.19, 2):,}".replace(',','.')+",00"],
              ["", "", "GESAMT brutto", "", "", "", f"{round(summe_netto*1.19, 2):,}".replace(',','.')+",00"]]),
            ("Liefer- und Zahlungsbedingungen",
             f"Liefertermin/-tranchen: {liefertermin}.\n\n"
             f"Lieferbedingung: DAP gemaess INCOTERMS 2020 (frei verbaut, Risiko geht mit Inbetriebnahme "
             f"auf den Kunden ueber).\n\n"
             f"Zahlungsbedingungen: {zahlungskondition}. Vorauszahlung 30 % bei Auftragserteilung; "
             f"40 % bei mechanischer Endabnahme im Werk Koeln (Pre-FAT); 25 % bei Inbetriebnahme "
             f"vor Ort; 5 % nach Ablauf der Gewaehrleistung bzw. gegen Buergschaft.\n\n"
             f"Eigentumsvorbehalt: erweiterter und verlaengerter Eigentumsvorbehalt gemaess Ziff. 8 "
             f"unserer AVB; Sicherungsuebereignung der Forderungen zugunsten der Halbreiter Maschinenbau GmbH."),
            ("Gewaehrleistung und Service",
             "Gewaehrleistung: 24 Monate ab Inbetriebnahme bzw. spaetestens 30 Monate ab Lieferdatum "
             "(was zuerst eintritt). Ein Wartungsangebot ueber 12 Monate (jaehrliche praeventive Wartung, "
             "Reaktionszeit 12 Std., Ersatzteilverfuegbarkeit) liegt der Auftragsbestaetigung als Anlage 2 bei "
             "(separater Auftrag erforderlich)."),
            ("Ansprechpartner",
             "Kommerzielle Abwicklung: Markus Fischer (KAM Industrie) / Jan Mueller (KAM Automotive), "
             "Telefon +49 221 47832-44 / -45, kam-industrie@halbreiter-maschinenbau.de.\n\n"
             "Technische Abwicklung: Michael Weber (Senior Konstrukteur F&E), m.weber@halbreiter-maschinenbau.de."),
            ("Anlagen",
             "Anlage 1: Kundenbestellung\n\n"
             "Anlage 2: Wartungsangebot 12 Monate\n\n"
             "Anlage 3: AVB Halbreiter Maschinenbau GmbH (Stand 1.1.2024)"),
            ("Unterschrift",
             signatures("Markus Fischer / Jan Mueller", "Key Account Manager", M["name"],
                        "", "Auftragsbestaetigung digitales Pendant", "i. A.",
                        place="Koeln", date_str_=datum)),
        ],
    )


# Build 8 Auftragsbestaetigungen
ABs = [
    ("KD_AB010_Auftragsbestätigung_ThyssenKrupp_Steel_E_2023", "TKSE",
     "AB-2023-014", "8. Juni 2023",
     "Pressenlinie PL-500 fuer Werk Duisburg-Hamborn, Halle A41",
     "ThyssenKrupp Steel Europe AG, Werk Hamborn, Hamborner Strasse 89, 47166 Duisburg",
     [["1", "PL500-HW-001", "Hydraulische Stanzpresse PL-500, 800 t", "1", "St.", "2.450.000,00", "2.450.000,00"],
      ["2", "PL500-CTRL-001", "Steuerungssystem SINUMERIK ONE / SPS-Programmierung", "1", "St.", "412.000,00", "412.000,00"],
      ["3", "PL500-INST-001", "Montage / Inbetriebnahme / Endabnahme", "1", "psch.", "298.000,00", "298.000,00"],
      ["4", "PL500-TRAIN-001", "Schulung 5 Tage 8 MA (Bedienung + Wartung)", "1", "psch.", "42.000,00", "42.000,00"],
      ["5", "PL500-WART-001", "Wartungsvertrag 24 Monate (Option, separat zu beauftragen)", "1", "psch.", "118.000,00", "118.000,00"]],
     3320000, "Lieferung Q1/2024, Inbetriebnahme 30. April 2024", "30 Tage netto"),
    ("KD_AB011_Auftragsbestätigung_Bosch_Rexroth_AG_2023", "BOSCH",
     "AB-2023-018", "12. September 2023",
     "Foerderbandanlage FB-200 Linie 4 fuer Werk Lohr am Main",
     "Bosch Rexroth AG, Werk Lohr, Zum Eisengiesser 1, 97816 Lohr am Main",
     [["1", "FB200-MOD-A", "Foerderband-Modul FB-200 Bauart A, 28 m Laenge", "1", "St.", "412.000,00", "412.000,00"],
      ["2", "FB200-MOD-K", "Kurvenmodul 90 Grad, R 1,8 m", "2", "St.", "82.000,00", "164.000,00"],
      ["3", "FB200-CTRL", "Steuerung SPS Siemens S7-1500", "1", "St.", "98.000,00", "98.000,00"],
      ["4", "FB200-INST", "Montage / Anschluss / IBN", "1", "psch.", "78.000,00", "78.000,00"]],
     752000, "Lieferung 14. Dezember 2023, IBN 22. Januar 2024", "14 Tage netto"),
    ("KD_AB012_Auftragsbestätigung_Hella_GmbH_und_Co._KGa_2024", "HELLA",
     "AB-2024-003", "18. Januar 2024",
     "Laserschneidanlage LS-800 5-Achs-Modul fuer Werk Lippstadt",
     "Hella GmbH & Co. KGaA, Werk Lippstadt, Rixbecker Strasse 75, 59552 Lippstadt",
     [["1", "LS800-5AX", "Laserschneidanlage LS-800 5-Achs-Modul (8 kW Faserlaser)", "1", "St.", "1.380.000,00", "1.380.000,00"],
      ["2", "LS800-ABS", "Absauganlage / Filteranlage", "1", "St.", "182.000,00", "182.000,00"],
      ["3", "LS800-CTRL", "Bedienerterminal HMI 22 Zoll inkl. CAM-Software", "1", "St.", "92.000,00", "92.000,00"],
      ["4", "LS800-INST", "Montage / Inbetriebnahme / Endabnahme + 3 Tage Schulung", "1", "psch.", "146.000,00", "146.000,00"]],
     1800000, "Lieferung 30. Juni 2024, IBN 15. Juli 2024", "30 Tage netto"),
    ("KD_AB013_Auftragsbestätigung_Viessmann_Climate_So_2024", "VIES",
     "AB-2024-005", "14. Februar 2024",
     "Montageroboter MR-150 fuer Linie Heiztechnik Allendorf",
     "Viessmann Climate Solutions SE, Viessmannstrasse 1, 35108 Allendorf (Eder)",
     [["1", "MR150-ZELL", "Robotik-Zelle MR-150 (2 Kollaborationsroboter Universal Robots UR10e)", "1", "St.", "385.000,00", "385.000,00"],
      ["2", "MR150-CTRL", "Steuerung Beckhoff TwinCAT 3 + Visualisierung", "1", "St.", "62.000,00", "62.000,00"],
      ["3", "MR150-GRIFF", "Greifersystem Schunk PGN-plus-P 200", "2", "St.", "8.400,00", "16.800,00"],
      ["4", "MR150-INST", "Montage / IBN / Validierung Heiztechniklinie", "1", "psch.", "78.000,00", "78.000,00"]],
     541800, "Lieferung 30. Juni 2024, IBN 22. Juli 2024", "30 Tage netto"),
    ("KD_AB014_Auftragsbestätigung_Dürr_AG_2024", "DUERR",
     "AB-2024-008", "12. Maerz 2024",
     "Pressenlinie PL-500 fuer Werk Queretaro, Mexiko (Export)",
     "Dürr AG, c/o Dürr de México, Av. Acceso Industria 25, El Marqués, 76246 Queretaro, Mexiko",
     [["1", "PL500-HW-002", "Hydraulische Stanzpresse PL-500 800 t (Export-Konfiguration)", "1", "St.", "2.580.000,00", "2.580.000,00"],
      ["2", "PL500-CTRL-002", "Steuerung mit 110V/60Hz, NEMA-konform", "1", "St.", "442.000,00", "442.000,00"],
      ["3", "PL500-VERPACK", "Seetransport-Verpackung / Kraftpaket / Konservierung 6 Monate", "1", "psch.", "182.000,00", "182.000,00"],
      ["4", "PL500-INST-MX", "Inbetriebnahme vor Ort 4 Wochen, 2 Techniker", "1", "psch.", "298.000,00", "298.000,00"]],
     3502000, "Lieferung Q4/2024, IBN Q1/2025", "Akkreditiv (L/C)"),
    ("KD_AB015_Auftragsbestätigung_Haver_und_Boecker_OHG_2024", "HAVER",
     "AB-2024-011", "8. April 2024",
     "Foerderbandanlage FB-200 Linie Saatgut Oelde",
     "Haver & Boecker OHG, Carl-Haver-Platz 3, 59302 Oelde",
     [["1", "FB200-MOD-A", "Foerderband-Modul FB-200 Bauart A, 18 m", "1", "St.", "342.000,00", "342.000,00"],
      ["2", "FB200-CTRL", "Steuerung mit ATEX-Zertifizierung Zone 22", "1", "St.", "118.000,00", "118.000,00"],
      ["3", "FB200-INST", "Montage / IBN / ATEX-Inbetriebnahmedokumentation", "1", "psch.", "82.000,00", "82.000,00"]],
     542000, "Lieferung 14. Juni 2024, IBN 8. Juli 2024", "14 Tage netto"),
    ("KD_AB016_Auftragsbestätigung_Gebr._Heyl_GmbH_und_Co_2023", "HEYL",
     "AB-2023-022", "15. November 2023",
     "Sonderkomponenten Pressen-Werkzeugsystem fuer Trinkwasserstrasse",
     "Gebr. Heyl GmbH & Co. KG, Max-Planck-Strasse 12, 31135 Hildesheim",
     [["1", "PWS-HEYL-01", "Werkzeugsystem Sondertraeger 4-fach (Edelstahl 1.4571)", "1", "St.", "182.000,00", "182.000,00"],
      ["2", "PWS-HEYL-02", "Hydraulikaggregat Druck 220 bar", "1", "St.", "48.000,00", "48.000,00"],
      ["3", "PWS-HEYL-03", "Steuerung Beckhoff CX2030", "1", "St.", "22.000,00", "22.000,00"],
      ["4", "PWS-HEYL-04", "Inbetriebnahme + Trinkwasser-Qualifizierung", "1", "psch.", "18.000,00", "18.000,00"]],
     270000, "Lieferung 18. Januar 2024, IBN 5. Februar 2024", "14 Tage netto"),
    ("KD_AB017_Auftragsbestätigung_Maschinenfabrik_Nieh_2023", "NIEH",
     "AB-2023-026", "8. Dezember 2023",
     "Robotik-Integration MR-150 fuer Kabelwickelanlage",
     "Maschinenfabrik Niehoff GmbH & Co. KG, Walzwerkstrasse 20, 91126 Schwabach",
     [["1", "MR150-ZELL-N", "Robotik-Zelle MR-150 fuer Kabelwickelanlage", "1", "St.", "298.000,00", "298.000,00"],
      ["2", "MR150-CUST", "Anpassung Greifer fuer Kupferleitungen 6-50 mm²", "1", "psch.", "42.000,00", "42.000,00"],
      ["3", "MR150-INST", "Integration in Niehoff-Steuerung, IBN, FAT", "1", "psch.", "62.000,00", "62.000,00"]],
     402000, "Lieferung 30. April 2024, IBN 22. Mai 2024", "30 Tage netto"),
]
for params in ABs:
    auftragsbestaetigung(*params)


# Rechnungen ------------------------------------------------------------------
def rechnung(fname, kunde_key, re_nr, datum, projekt, ab_ref, netto, ust_freistellung=False,
             leistung_zeit="lt. Lieferschein", iban=M["iban"]):
    K = KUNDEN[kunde_key]
    write_doc(
        f"{BASE}/{fname}.docx", H,
        f"Rechnung Nr. {re_nr}",
        subtitle=f"Leistungs-/Lieferdatum: {leistung_zeit}",
        sections=[
            ("Rechnungsempfaenger",
             f"{K['name']}\n{K['addr']}\nKundennummer: {K['kn']}\n"
             f"Bezug: Auftragsbestaetigung {ab_ref}; Projekt »{projekt}«"),
            ("Rechnungspositionen",
             [["Pos", "Beschreibung", "Menge", "Einheit", "Einzelpreis EUR", "Gesamt EUR"],
              ["1", projekt, "1", "psch.", f"{netto:,}".replace(',','.')+",00",
               f"{netto:,}".replace(',','.')+",00"]] +
             ([["", "Zwischensumme netto", "", "", "", f"{netto:,}".replace(',','.')+",00"],
               ["", "Innergemeinschaftliche / Drittlands-Lieferung (steuerfrei)", "", "", "", "0,00"],
               ["", "GESAMT", "", "", "", f"{netto:,}".replace(',','.')+",00"]] if ust_freistellung else
              [["", "Zwischensumme netto", "", "", "", f"{netto:,}".replace(',','.')+",00"],
               ["", "Umsatzsteuer 19 %", "", "", "", f"{round(netto*0.19):,}".replace(',','.')+",00"],
               ["", "GESAMT brutto", "", "", "", f"{round(netto*1.19):,}".replace(',','.')+",00"]])),
            ("Zahlungsbedingungen",
             "Zahlbar binnen 14 Tagen netto auf das nachstehende Konto unter Angabe der Rechnungsnummer.\n\n"
             f"Bankverbindung: {M['bank']}\nIBAN: {iban}\nBIC: DEUTDEDB\n\n"
             "USt-IdNr. Halbreiter Maschinenbau GmbH: DE 198 765 432\n"
             "Steuernummer: 215/5765/9876, Finanzamt Koeln-Nord\n\n"
             + ("Steuerbefreite innergemeinschaftliche Lieferung / Ausfuhrlieferung gemaess § 4 Nr. 1 UStG. "
                "Hinweis: Steuerschuldnerschaft des Leistungsempfaengers." if ust_freistellung else "")),
            ("Hinweise",
             "Die Rechnung wird elektronisch im X-Rechnungs-Format (XRechnung 2.3.2) ueber das Buyer-Portal "
             "des Kunden uebermittelt; ein Original-Beleg in Papier ist ggf. auf Anforderung erhaeltlich.\n\n"
             "Diese Rechnung wurde maschinell erstellt und ist auch ohne Unterschrift gueltig."),
        ],
    )


# Rechnungen-Liste
REs = [
    ("KD_RE001_Rechnung_ThyssenKrupp_Steel",   "TKSE",  "2023-RE-0421", "12. November 2023",
     "Vorauszahlung 30 % Pressenlinie PL-500 (AB-2023-014)", "AB-2023-014", 996000),
    ("KD_RE002_Rechnung_Bosch_Rexroth_AG",     "BOSCH", "2024-RE-0042", "8. Januar 2024",
     "Endabrechnung Foerderbandanlage FB-200 Linie 4", "AB-2023-018", 752000),
    ("KD_RE003_Rechnung_Hella_GmbH_und_Co._K", "HELLA", "2024-RE-0114", "22. Februar 2024",
     "Anzahlung 30 % Laserschneidanlage LS-800 5-Achs", "AB-2024-003", 540000),
    ("KD_RE004_Rechnung_Viessmann_Climate_",   "VIES",  "2024-RE-0128", "28. Februar 2024",
     "Anzahlung 30 % Montageroboter MR-150 Heiztechnik", "AB-2024-005", 162540),
    ("KD_RE005_Rechnung_Dürr_AG",              "DUERR", "2024-RE-0188", "18. Maerz 2024",
     "Anzahlung 30 % Pressenlinie PL-500 Mexiko", "AB-2024-008", 1050600, True),
    ("KD_RE006_Rechnung_ThyssenKrupp_Steel",   "TKSE",  "2024-RE-0214", "8. April 2024",
     "Zwischenrechnung 40 % Pressenlinie PL-500 (Pre-FAT)", "AB-2023-014", 1328000),
    ("KD_RE007_Rechnung_Bosch_Rexroth_AG",     "BOSCH", "2024-RE-0250", "22. April 2024",
     "Zusatzleistung Engineering-Aenderung FB-200 Linie 4", "AB-2023-018", 48000),
    ("KD_RE008_Rechnung_Haver_und_Boecker_OH", "HAVER", "2024-RE-0312", "22. Juni 2024",
     "Endabrechnung Foerderbandanlage FB-200 ATEX", "AB-2024-011", 542000),
    ("KD_RE009_Rechnung_Gebr._Heyl_GmbH_und_", "HEYL",  "2024-RE-0098", "8. Februar 2024",
     "Endabrechnung Werkzeugsystem Trinkwasserstrasse", "AB-2023-022", 270000),
    ("KD_RE010_Rechnung_Maschinenfabrik_Ni",   "NIEH",  "2024-RE-0282", "30. Mai 2024",
     "Endabrechnung Robotik-Zelle MR-150 Kabelwickelanlage", "AB-2023-026", 402000),
]
for params in REs:
    rechnung(*params)


# Angebote --------------------------------------------------------------------
def angebot(fname, kunde_key, angebot_nr, datum, projekt, positionen, summe_netto, gueltig_bis):
    K = KUNDEN[kunde_key]
    write_doc(
        f"{BASE}/{fname}.docx", H,
        f"Angebot Nr. {angebot_nr}",
        subtitle=f"Gueltig bis: {gueltig_bis}",
        sections=[
            ("Adressat",
             f"{K['name']}\n{K['addr']}\nz. Hd. Einkauf"),
            ("Sehr geehrte Damen und Herren,",
             f"vielen Dank fuer Ihre Anfrage zum Thema »{projekt}«. Gemaess Ihrer Spezifikation und "
             f"unserem Besprechungsprotokoll vom {datum} unterbreiten wir Ihnen das folgende, "
             f"unverbindliche Angebot. Wir freuen uns auf einen weiteren Austausch und stehen fuer "
             f"einen technischen Termin gerne kurzfristig zur Verfuegung."),
            ("Positionen",
             [["Pos", "Beschreibung", "Menge", "Einheit", "Einzelpreis EUR", "Gesamt EUR"]] + positionen +
             [["", "Zwischensumme netto", "", "", "", f"{summe_netto:,}".replace(',','.')+",00"],
              ["", "Umsatzsteuer 19 %", "", "", "", f"{round(summe_netto*0.19):,}".replace(',','.')+",00"],
              ["", "GESAMT brutto", "", "", "", f"{round(summe_netto*1.19):,}".replace(',','.')+",00"]]),
            ("Kommerzielle Konditionen",
             "Liefer- und Zahlungsbedingungen, Eigentumsvorbehalt, Gewaehrleistung und Service-Level "
             "richten sich nach unseren AVB Stand 1.1.2024 (Anlage) sowie nach dem zugrundeliegenden "
             "Rahmenvertrag.\n\n"
             "Zahlungsbedingung empfohlen: 30 % bei Auftragserteilung, 40 % bei Pre-FAT, 25 % bei IBN, "
             "5 % nach Gewaehrleistungsablauf (oder Buergschaft).\n\n"
             "Liefertermin: ca. 22-28 Wochen nach Auftragserteilung und technischer Klaerung.\n\n"
             "Optionale Module sind separat ausgewiesen und auf Wunsch beauftragbar."),
            ("Schluss",
             "Fuer Rueckfragen stehen wir unter +49 221 47832-44 (Vertrieb) bzw. -22 (Konstruktion / "
             "Michael Weber) gerne zur Verfuegung.\n\nMit freundlichen Gruessen, "
             "Halbreiter Maschinenbau GmbH"),
        ],
    )


angebot("KD_A001_Angebot_Hella_GmbH_und_Co._KGa", "HELLA", "A-2024-003-DRAFT", "10. Januar 2024",
        "Laserschneidanlage LS-800 5-Achs-Modul fuer Werk Lippstadt",
        [["1", "Laserschneidanlage LS-800 5-Achs-Modul (8 kW Faserlaser)", "1", "St.", "1.380.000,00", "1.380.000,00"],
         ["2", "Absauganlage / Filteranlage", "1", "St.", "182.000,00", "182.000,00"],
         ["3", "Bedienerterminal HMI 22 Zoll inkl. CAM-Software", "1", "St.", "92.000,00", "92.000,00"],
         ["4", "Montage / Inbetriebnahme / Endabnahme + 3 Tage Schulung", "1", "psch.", "146.000,00", "146.000,00"],
         ["Opt.", "MES-Schnittstelle OPC-UA + REST-API", "1", "psch.", "62.000,00", "62.000,00"]],
        1862000, "30. April 2024")
angebot("KD_A002_Angebot_Viessmann_Climate_So", "VIES", "A-2024-005", "8. Februar 2024",
        "Montageroboter MR-150 fuer Linie Heiztechnik Allendorf",
        [["1", "Robotik-Zelle MR-150 (2 Kollaborationsroboter UR10e)", "1", "St.", "385.000,00", "385.000,00"],
         ["2", "Steuerung Beckhoff TwinCAT 3 + Visualisierung", "1", "St.", "62.000,00", "62.000,00"],
         ["3", "Greifersystem Schunk PGN-plus-P 200", "2", "St.", "8.400,00", "16.800,00"],
         ["4", "Montage / IBN / Validierung Heiztechniklinie", "1", "psch.", "78.000,00", "78.000,00"],
         ["Opt.", "Zusatzroboter UR10e (Nr. 3)", "1", "St.", "62.000,00", "62.000,00"]],
        603800, "30. April 2024")
angebot("KD_A003_Angebot_Dürr_AG", "DUERR", "A-2024-008-EXP", "20. Februar 2024",
        "Pressenlinie PL-500 fuer Werk Queretaro, Mexiko (Export)",
        [["1", "Hydraulische Stanzpresse PL-500 800 t (Export-Konfiguration NEMA)", "1", "St.", "2.580.000,00", "2.580.000,00"],
         ["2", "Steuerung mit 110V/60Hz NEMA-konform", "1", "St.", "442.000,00", "442.000,00"],
         ["3", "Seetransport-Verpackung / Konservierung 6 Monate", "1", "psch.", "182.000,00", "182.000,00"],
         ["4", "Inbetriebnahme vor Ort 4 Wochen, 2 Techniker (incl. Anreise)", "1", "psch.", "298.000,00", "298.000,00"],
         ["Opt.", "Predictive-Maintenance-Modul + 24 Mo. Servicepaket", "1", "psch.", "182.000,00", "182.000,00"]],
        3684000, "30. April 2024")


# Vertraege (KD_001 … KD_007) -------------------------------------------------
def vertrag(fname, kunde_key, vertragsnr, datum, projekt, volumen_eur, vertrags_typ="Rahmenvertrag",
            laufzeit="bis 31. Dezember 2026", incoterm="DAP gemaess INCOTERMS 2020", lex="deutsches Recht; Gerichtsstand Koeln"):
    K = KUNDEN[kunde_key]
    write_doc(
        f"{BASE}/{fname}.docx", H,
        f"{vertrags_typ} – {K['name']} – »{projekt}«",
        subtitle=f"Vertragsnr. {vertragsnr}, Stand {datum}",
        sections=[
            ("Vertragsparteien",
             f"1. Halbreiter Maschinenbau GmbH, Industriestrasse 12, 50829 Koeln, HRB 47312, AG Koeln, "
             f"vertreten durch Klaus Mueller (CEO) und Sandra Becker (CFO) – nachfolgend »MMB« –, sowie\n\n"
             f"2. {K['name']}, {K['addr']} – nachfolgend »Kunde« –"),
            ("Praeambel",
             f"MMB ist Spezialist fuer Sondermaschinenbau und Anlagenbau in der metallverarbeitenden Industrie. "
             f"Der Kunde betreibt Werke und Anlagen, fuer die er hochpraezise Maschinenkomponenten und Systeme "
             f"in wiederkehrender Lieferform benoetigt. Im Rahmen des Projektes »{projekt}« mit einem "
             f"erwarteten Gesamtvolumen von rund {volumen_eur:,} EUR".replace(',','.') +
             f" ueber die Vertragslaufzeit schliessen die Parteien diesen Rahmenvertrag, um Bestellungen "
             f"effizient unter einheitlichen Konditionen abwickeln zu koennen."),
            ("Vertragsregelungen",
             ("clauses", [
                 ("§ 1 Gegenstand", [
                     f"Gegenstand ist die Lieferung und Montage der vom Kunden im Rahmen des Projektes "
                     f"»{projekt}« beauftragten Maschinen, Anlagen und zugehoeriger Dienstleistungen.",
                     "Einzelauftraege erfolgen ueber gesonderte Bestellungen / Auftragsbestaetigungen "
                     "auf Basis dieses Rahmenvertrags. Bei Widerspruch geht die Auftragsbestaetigung im "
                     "Einzelfall vor, im Uebrigen dieser Rahmenvertrag.",
                 ]),
                 ("§ 2 Liefermenge / Vorlauf", [
                     "Der Kunde uebermittelt rollierend einen 12-Monats-Forecast (taeglicher Abgleich "
                     "ueber EDI/ANSI X.12 oder OPC-UA-Schnittstelle), aufgeteilt in: Fixzone (0-3 Monate), "
                     "Tradezone (4-6 Monate) und Forecastzone (7-12 Monate).",
                     "MMB verpflichtet sich, fixe Mengen rechtzeitig zu liefern; Aenderungen in der Tradezone "
                     "werden auf Basis Aufwandsausgleich angepasst.",
                 ]),
                 ("§ 3 Preise", [
                     "Preise sind in der Preisliste Anlage 2 festgelegt. Preisanpassungen erfolgen "
                     "jaehrlich entlang der Materialkostenindex-Klausel (Stahl-/Aluminium-Index gemaess "
                     "Statistisches Bundesamt) sowie der Personalkosten-Klausel (M+E NRW-Tarifabschluss).",
                     "Materialklausel: > +/- 5 % Aenderung Vormonats-Index loest Anpassung in laufender Bestellung aus.",
                 ]),
                 ("§ 4 Lieferung / Eigentumsvorbehalt", [
                     f"Lieferung erfolgt {incoterm}. Gefahruebergang mit Eintreffen am Werkstor des Kunden.",
                     "Eigentumsvorbehalt: erweiterter und verlaengerter Eigentumsvorbehalt gemaess Ziff. 8 "
                     "AVB MMB. Forderungen aus der Weiterveraeusserung werden im Voraus an MMB abgetreten.",
                 ]),
                 ("§ 5 Zahlungsbedingungen", [
                     "Zahlung erfolgt 30 Tage netto nach Rechnungseingang. Bei Lieferung > 500 TEUR "
                     "Einzelauftragswert: Anzahlung 30 % bei Auftragserteilung, 40 % bei Pre-FAT, "
                     "25 % bei IBN, 5 % nach Gewaehrleistung oder Buergschaft.",
                 ]),
                 ("§ 6 Gewaehrleistung / Haftung", [
                     "Gewaehrleistung 24 Monate ab IBN, spaetestens 30 Monate ab Lieferung. Haftung MMB "
                     "begrenzt auf 100 % des Vertragswertes pro Schadensereignis und 200 % insgesamt; "
                     "ausgenommen Vorsatz und grobe Fahrlaessigkeit sowie Personenschaeden.",
                     "Produkthaftung gemaess ProdHaftG bleibt unberuehrt.",
                 ]),
                 ("§ 7 Service-Level / Wartung", [
                     "Vertragsbestandteil ist – soweit gesondert beauftragt – ein 24-Monats-Wartungsvertrag "
                     "(jaehrliche Pruefung, Telefon-Reaktion 4 Std., vor-Ort-Reaktion 24 Std., Ersatzteile "
                     "lagernd 12 Monate).",
                 ]),
                 ("§ 8 Vertraulichkeit", [
                     "Saemtliche Informationen, die im Zusammenhang mit der Geschaeftsbeziehung ausgetauscht "
                     "werden, sind vertraulich und duerfen nicht ohne Zustimmung der jeweils anderen Partei "
                     "Dritten zugaenglich gemacht werden. Eine separate NDA (Anlage 3) gilt fuer Detailangaben.",
                 ]),
                 ("§ 9 Compliance / ESG / Lieferkette", [
                     "Die Parteien verpflichten sich auf die Einhaltung der einschlaegigen Gesetze, "
                     "insbesondere LkSG (Lieferkettensorgfaltspflichtengesetz), Anti-Korruption, "
                     "Exportkontrolle und Sanktionsrecht.",
                     "MMB legt jaehrlich eine Lieferkettensorgfalts-Erklaerung (Anlage 4) vor.",
                 ]),
                 ("§ 10 Anwendbares Recht / Streitbeilegung", [
                     f"Es gilt {lex}. Streitigkeiten werden zunaechst durch Mediation (Pro-bono-Mediator "
                     "der Industrie- und Handelskammer Koeln) geklaert; gelingt dies nicht binnen 60 Tagen, "
                     "entscheidet das ordentliche Gericht.",
                 ]),
                 ("§ 11 Laufzeit / Kuendigung", [
                     f"Dieser Vertrag laeuft vom {datum} {laufzeit}. Eine Verlaengerung um 12 Monate "
                     "erfolgt automatisch, soweit nicht 6 Monate vor Ablauf gekuendigt wird.",
                     "Ausserordentliche Kuendigung aus wichtigem Grund bleibt unberuehrt.",
                 ]),
             ])),
            ("Anlagen",
             "Anlage 1: Technische Spezifikation\n\nAnlage 2: Preisliste 2024\n\n"
             "Anlage 3: Vertraulichkeitsvereinbarung (NDA)\n\nAnlage 4: LkSG-Sorgfaltserklaerung MMB"),
            ("Unterschriften",
             signatures("Klaus Mueller / Sandra Becker", "Geschaeftsfuehrung", M["name"],
                        "Einkaufsleitung", "Bevollmaechtigte", K["name"],
                        place="Koeln / " + K["addr"].split(",")[-1].strip(), date_str_=datum)),
        ],
    )


vertrag("KD_001_Vertrag_ThyssenKrupp_Steel_E", "TKSE", "RV-2023-TKSE-001", "14. Juni 2023",
        "Lieferung Pressenlinien PL-500 fuer Werke Duisburg / Bochum", 12_500_000)
vertrag("KD_002_Vertrag_Bosch_Rexroth_AG", "BOSCH", "RV-2023-BOSCH-001", "22. Juni 2023",
        "Foerderbandanlagen FB-200 fuer Werk Lohr (Linien 4-6)", 4_200_000)
vertrag("KD_003_Vertrag_Hella_GmbH_und_Co._KGa", "HELLA", "RV-2024-HELLA-001", "30. Januar 2024",
        "Laserschneidanlagen LS-800 fuer Werk Lippstadt", 6_800_000)
vertrag("KD_004_Vertrag_Viessmann_Climate_So", "VIES", "RV-2024-VIES-001", "22. Februar 2024",
        "Montageroboter MR-150 fuer Heiztechnik Allendorf (Linien 1-4)", 2_400_000)
vertrag("KD_005_Vertrag_Dürr_AG", "DUERR", "RV-2024-DUERR-001", "18. Maerz 2024",
        "Pressenlinien PL-500 fuer das Werk Queretaro, Mexiko", 8_900_000,
        incoterm="DAP Queretaro gemaess INCOTERMS 2020",
        lex="deutsches Recht; Schiedsgericht DIS, Sitz Koeln")
vertrag("KD_006_Vertrag_ThyssenKrupp_Steel_E", "TKSE", "RV-2024-TKSE-002", "12. April 2024",
        "Wartungs- und Servicevertrag Pressenlinien PL-300 und PL-500", 1_600_000,
        vertrags_typ="Service- und Wartungsvertrag")
vertrag("KD_007_Vertrag_Bosch_Rexroth_AG", "BOSCH", "RV-2024-BOSCH-002", "14. Mai 2024",
        "Modernisierung Steuerung Bestandsanlagen FB-200 (Retrofit Linien 1-3)",
        1_950_000, vertrags_typ="Modernisierungs- / Retrofit-Vertrag")


# Sonstige Dokumente ---------------------------------------------------------
write_doc(
    f"{BASE}/KD_Rahmenvertrag_ThyssenKrupp_2023.docx", H,
    "Rahmenvertrag ThyssenKrupp Steel Europe AG 2023 (Kurzfassung)",
    subtitle="Auszug zur Datenraum-Vorlage; Volldokument siehe KD_001",
    sections=[
        ("Vertragspartner", "Halbreiter Maschinenbau GmbH und ThyssenKrupp Steel Europe AG (TKSE)."),
        ("Volumen / Laufzeit",
         "Vertragsvolumen ueber 3 Jahre rund 12,5 Mio. EUR (Schluesselkunde). Laufzeit 14.06.2023 "
         "bis 31.12.2026, Verlaengerungsoption +12 Monate, sofern nicht 6 Monate vor Ablauf gekuendigt."),
        ("Wesentliche Punkte",
         ("list", [
             "Liefergegenstand: Pressenlinien PL-500 und Sonderkonfigurationen fuer Werke Duisburg-Hamborn, Bochum.",
             "Preisanpassung jaehrlich nach Materialindex (Stahl), Tarif M+E NRW.",
             "Zahlungsbedingung: 30 % Anzahlung / 40 % Pre-FAT / 25 % IBN / 5 % Gewaehrleistungseinbehalt oder Buergschaft.",
             "Liefer-Incoterm: DAP gemaess INCOTERMS 2020.",
             "Gewaehrleistung: 24 Monate ab IBN.",
             "Eskalationsstufen: KAM Markus Fischer -> GF MMB -> GF TKSE.",
         ])),
        ("Hinweis",
         "Diese Kurzfassung dient lediglich der Schnellinformation. Massgeblich ist die vollstaendige "
         "Vertragsfassung mit Anlagen (KD_001_Vertrag_ThyssenKrupp_Steel_E.docx)."),
    ],
)


write_doc(
    f"{BASE}/KD_SLA_After_Sales_Service_Bosch_2023.docx", H,
    "SLA After-Sales-Service Bosch Rexroth AG 2023-2025",
    subtitle="Service-Level-Agreement, gueltig ab 1. Juli 2023",
    sections=[
        ("Geltungsbereich",
         "Dieses SLA gilt fuer den After-Sales-Service der durch die Halbreiter Maschinenbau GmbH gelieferten "
         "Foerderbandanlagen FB-200 in den Werken Lohr am Main, Erbach und Witten der Bosch Rexroth AG."),
        ("Reaktions- und Reparaturzeiten",
         [
             ["Prioritaet", "Definition", "Reaktion telefonisch", "Reaktion vor Ort", "Wiederherstellung"],
             ["P1 Anlagenstillstand", "Linie steht > 30 Min.", "30 Min.", "8 Std.", "24 Std."],
             ["P2 Funktionseinschraenkung", "Reduzierte Leistung", "2 Std.", "24 Std.", "5 Werktage"],
             ["P3 Standardanforderung", "Vorbeugende Wartung", "1 Werktag", "5 Werktage", "10 Werktage"],
         ]),
        ("Verfuegbarkeit",
         "Servicebereitschaft 24/7 ueber die Servicehotline +49 221 47832-72; Eskalationsstufen "
         "Servicetechniker -> Servicekoordinator -> Servicemanager Stefan Bauer -> COO."),
        ("Ersatzteile",
         "Verfuegbarkeit von Verschleissteilen ab Lager Koeln in 90 % der Faelle innerhalb von 24 Stunden. "
         "Halbreiter Maschinenbau GmbH garantiert eine Ersatzteilversorgung fuer mindestens 12 Jahre nach "
         "Auslieferung."),
        ("KPI und Reporting",
         "Monatlicher SLA-Bericht (Erfuellungsgrad, Eskalationen, Pre/Post-Mortem). Quartals-Review-Meeting "
         "mit dem Kunden. Vertragsstrafe bei nicht eingehaltener Reaktionszeit P1: 2.000 EUR pro Stunde "
         "Verspaetung."),
        ("Vergutung",
         "Service-Pauschale 320.000 EUR p. a. (3 Werke / 12 Anlagen). Materialien und Arbeitszeit fuer "
         "Ausserplan-Einsaetze nach Aufwand zu Stundensaetzen (Tech-Stundensatz 145 EUR, Senior 180 EUR, "
         "Reisezeit 50 %)."),
    ],
)


write_doc(
    f"{BASE}/KD_Kundenreklamationsstatistik_20.docx", H,
    "Kundenreklamationsstatistik 2023",
    subtitle="Auswertung Qualitaetsmanagement, Stand 31. Januar 2024",
    sections=[
        ("Gesamtbild",
         "Im Geschaeftsjahr 2023 wurden 38 Kundenreklamationen erfasst (Vorjahr 47), entspricht einer "
         "Reklamationsquote von 0,68 % bezogen auf die Anzahl ausgelieferter Auftraege (5.580). Damit liegt "
         "die Quote zum zweiten Mal in Folge unter dem internen Zielwert von 0,80 %."),
        ("Aufschluesselung nach Produkt",
         [
             ["Produkt", "Reklamationen 2023", "Reklamationen 2022", "Trend"],
             ["Pressenlinie PL-500", "12", "8", "↑ (mehr ausgelieferte)"],
             ["Pressenlinie PL-300 (Auslauf)", "6", "16", "↓"],
             ["Foerderbandanlage FB-200", "9", "11", "↓"],
             ["Laserschneidanlage LS-800", "5", "4", "↑"],
             ["Robotik MR-150", "4", "3", "↑"],
             ["Sonderkomponenten / Werkzeuge", "2", "5", "↓"],
             ["", "SUMME", "38", "47", "↓"],
         ]),
        ("Top-3 Ursachen",
         "(1) Steuerungssoftware-Versions-Inkompatibilitaet bei Updates Trumpf-Module (LS-800), "
         "Anteil 18 % der Reklamationen. Massnahme: Versionsregister erweitert, FW-Test im Pre-FAT verstaerkt.\n\n"
         "(2) Sensorik-Drift (FB-200), Anteil 14 %. Massnahme: Verlagerung auf Sensirion AG Schweiz "
         "(Lieferant 2) als Zweitquelle.\n\n"
         "(3) Werkzeugverschleiss schneller als spezifiziert (PL-500 in Hartmaterial-Anwendungen). "
         "Massnahme: Werkzeugempfehlung im Inbetriebnahmeprotokoll konkretisiert."),
        ("8D-Berichte",
         "Im Berichtszeitraum wurden 14 8D-Berichte erstellt; alle dokumentiert in QM-Datenbank "
         "(ATLAS QMS). Eskalierte 8D-Berichte (D8 ueber 30 Tage offen): 2."),
        ("Massnahmen 2024",
         "(a) Erweiterte Eingangskontrolle bei kritischen Steuerungskomponenten; (b) Vertiefung der "
         "Schulung der Vor-Ort-Servicetechniker:innen (intern + Trumpf Academy); (c) Aufnahme einer "
         "monatlichen Reklamationsquoten-KPI in den Geschaeftsfuehrungsbericht."),
    ],
)


write_doc(
    f"{BASE}/KD_Kundenzufriedenheitsumfrage_2023.docx", H,
    "Kundenzufriedenheitsumfrage 2023",
    subtitle="Auswertung der jaehrlichen Befragung, durchgefuehrt Q4/2023",
    sections=[
        ("Methodik",
         "Befragt wurden 47 Kundenkontakte bei 22 Kundenunternehmen (Schluesselkunden + ausgewaehlte "
         "Bestandskunden). Befragungsmethode: Online-Fragebogen (28 Fragen) plus 6 vertiefende "
         "Telefoninterviews. Ruecklaufquote: 81 % (38 vollstaendige Antworten). Durchfuehrung durch das "
         "interne Marktforschungsteam (Lead: Julia Krause)."),
        ("Net Promoter Score (NPS)",
         "NPS 2023: +52 (Vorjahr +47). Industriebenchmark Sondermaschinenbau (BITKOM-/VDMA-Auswertung 2023): "
         "+38. MMB liegt damit signifikant ueber dem Branchendurchschnitt."),
        ("Top-Ergebnisse",
         [
             ["Dimension", "Score (5 = sehr gut)", "Vorjahr", "Tendenz"],
             ["Lieferzuverlaessigkeit", "4,6", "4,4", "↑"],
             ["Produktqualitaet", "4,7", "4,5", "↑"],
             ["Inbetriebnahme-Begleitung", "4,5", "4,4", "↑"],
             ["After-Sales / Service", "4,3", "4,2", "↑"],
             ["Preis-Leistungs-Verhaeltnis", "3,9", "3,8", "↑"],
             ["Innovationskraft", "4,4", "4,1", "↑"],
             ["Kommunikation Key-Account", "4,7", "4,6", "↑"],
             ["Reaktionszeit Reklamationen", "4,1", "3,9", "↑"],
         ]),
        ("Top-Verbesserungspotentiale",
         "(1) Beschleunigung Ersatzteilversorgung in Asien-/Amerikas-Werken (genannt von Dürr und TKSE);\n\n"
         "(2) Erweiterung des Self-Service-Portals (Online-Bestellung Ersatzteile, Wartungshistorie);\n\n"
         "(3) Bessere Transparenz Lieferstatus in der Produktionsphase (»wo steht die Anlage gerade«)."),
        ("Massnahmen 2024",
         "Massnahmen wurden im OKR-Quartalsprogramm Q2/2024 verankert: Aufbau Kunden-Self-Service-Portal "
         "(Salesforce Experience Cloud, Go-Live Q4/2024); Erweiterung Service-Hub Asien (Suzhou, China, "
         "Pilot Q3/2024); Lieferstatus-Tracking in MES-Pilot integriert (Go-Live Q2/2024)."),
    ],
)


write_doc(
    f"{BASE}/KD_Kundenprojektliste_2023_2024.docx", H,
    "Kundenprojektliste 2023-2024",
    subtitle="Auszug aus dem CRM-System (Salesforce Sales Cloud); Stand 15. Februar 2024",
    sections=[
        ("Hinweis",
         "Liste umfasst alle aktiven und in Akquisition befindlichen Projekte mit einem Volumen ≥ 250 TEUR. "
         "Status: NEW (Pipeline), DEAL (Vertrag), DELIV (in Lieferung), POSTDEL (in Service / Gewaehrleistung)."),
        ("Top-Projekte",
         [
             ["Projektnr.", "Kunde", "Produkt", "Volumen (k EUR)", "Status", "Erwartete IBN"],
             ["P-2023-014", "ThyssenKrupp Steel Europe AG", "Pressenlinie PL-500 Duisburg-Hamborn", "3.800", "DELIV", "30. April 2024"],
             ["P-2023-018", "Bosch Rexroth AG", "Foerderband FB-200 Linie 4 Lohr", "752", "POSTDEL", "22. Januar 2024"],
             ["P-2024-003", "Hella GmbH & Co. KGaA", "Laserschneidanlage LS-800 5-Achs", "1.862", "DELIV", "15. Juli 2024"],
             ["P-2024-005", "Viessmann Climate Solutions SE", "Robotik MR-150 Heiztechnik", "542", "DELIV", "22. Juli 2024"],
             ["P-2024-008", "Dürr AG (Werk Queretaro, Mexiko)", "Pressenlinie PL-500 (Export)", "3.684", "DEAL", "Q1/2025"],
             ["P-2024-011", "Haver & Boecker OHG", "Foerderband FB-200 ATEX", "542", "DEAL", "8. Juli 2024"],
             ["P-2024-014", "Stellantis N.V. (Werk Ruesselsheim)", "Pressenlinie PL-500", "4.200", "NEW", "n. v."],
             ["P-2024-015", "VW Bratislava", "Robotik MR-150 (3 Zellen)", "1.620", "NEW", "n. v."],
             ["P-2024-016", "Continental AG", "Foerderband FB-200 (2 Linien)", "1.180", "NEW", "n. v."],
             ["P-2024-018", "Gebr. Heyl GmbH & Co. KG", "Sonderwerkzeugsystem", "270", "POSTDEL", "5. Februar 2024"],
             ["P-2023-026", "Maschinenfabrik Niehoff", "Robotik MR-150 Kabelwickel", "402", "DELIV", "22. Mai 2024"],
         ]),
        ("Pipeline",
         "Pipeline-Wert NEW: 7,00 Mio. EUR (gewichtet mit 35 % Erwartungswert: 2,45 Mio. EUR). "
         "Konversionsrate NEW->DEAL der letzten 4 Quartale: 38 %.\n\n"
         "Auftragseingang DEAL Q4/2023 + Q1/2024: 7,82 Mio. EUR (Vorjahresvergleich +14 %)."),
    ],
)


write_doc(
    f"{BASE}/Preisliste_2024_Standardprodukte.docx", H,
    "Preisliste 2024 – Standardprodukte und Optionen",
    subtitle="Gueltig ab 1. April 2024, vorbehaltlich Materialindex-Klausel",
    sections=[
        ("Hinweise",
         "Diese Preisliste gilt fuer Standardkonfigurationen der nachfolgend gelisteten Produktreihen. "
         "Kundenspezifische Sonderkonfigurationen, Service- und Wartungsleistungen sowie Inbetriebnahme-"
         "Aufwendungen werden separat kalkuliert. Alle Preise verstehen sich netto ab Werk Koeln (EXW) "
         "gemaess INCOTERMS 2020 zzgl. gesetzlicher Umsatzsteuer."),
        ("Pressenlinie PL-500",
         [
             ["Konfiguration", "Pressenkraft (t)", "Hublaenge (mm)", "Preis EUR", "Lieferzeit"],
             ["PL-500-500-Std.", "500", "400", "1.890.000,00", "22 Wo."],
             ["PL-500-800-Std.", "800", "500", "2.450.000,00", "26 Wo."],
             ["PL-500-1000-Std.", "1000", "600", "2.890.000,00", "30 Wo."],
             ["PL-500-Servo-Option", "+", "+", "+ 280.000,00", "+ 4 Wo."],
             ["PL-500-Predict-Maint.", "+", "+", "+ 145.000,00", "+ 2 Wo."],
         ]),
        ("Foerderbandanlage FB-200",
         [
             ["Konfiguration", "Laenge", "Geschw.", "Preis EUR", "Lieferzeit"],
             ["FB-200-Mod A (Gerade)", "12 m", "1,5 m/s", "260.000,00", "12 Wo."],
             ["FB-200-Mod A (Gerade)", "28 m", "1,5 m/s", "412.000,00", "16 Wo."],
             ["FB-200-Mod K (Kurve)", "R 1,8 m", "1,5 m/s", "82.000,00", "10 Wo."],
             ["FB-200-ATEX-Option", "+", "+", "+ 118.000,00", "+ 4 Wo."],
         ]),
        ("Laserschneidanlage LS-800",
         [
             ["Konfiguration", "Laserleistung", "Achsen", "Preis EUR", "Lieferzeit"],
             ["LS-800-4kW-3Achs", "4 kW", "3", "740.000,00", "18 Wo."],
             ["LS-800-6kW-3Achs", "6 kW", "3", "980.000,00", "20 Wo."],
             ["LS-800-8kW-3Achs", "8 kW", "3", "1.180.000,00", "22 Wo."],
             ["LS-800-8kW-5Achs", "8 kW", "5", "1.380.000,00", "24 Wo."],
         ]),
        ("Robotik MR-150",
         [
             ["Konfiguration", "Robotertyp", "Anzahl", "Preis EUR", "Lieferzeit"],
             ["MR-150-Single", "UR10e", "1", "248.000,00", "14 Wo."],
             ["MR-150-Dual", "UR10e", "2", "385.000,00", "16 Wo."],
             ["MR-150-Triple", "UR10e", "3", "498.000,00", "18 Wo."],
             ["MR-150-Cobot-MAX", "UR16e", "+", "+ 62.000,00", "+ 2 Wo."],
         ]),
        ("Service- und Wartung",
         "Wartungspakete (Jahrespauschale): Basic (1x p. a.) 28.000 EUR; Premium (2x p. a. + Hotline) "
         "56.000 EUR; Total Care (4x p. a. + 8h-Reaktionszeit + Ersatzteilbevorratung) 118.000 EUR.\n\n"
         "Stundensaetze ausserhalb Wartungsvertrag: Techniker:in 145 EUR, Senior 180 EUR, Reisezeit 50 % "
         "des Stundensatzes."),
    ],
)


write_doc(
    f"{BASE}/KD_Rahmenvertrag_ThyssenKrupp_2023.docx", H,  # already created above; redundant duplicate - we re-write same file
    "Rahmenvertrag ThyssenKrupp Steel Europe AG 2023 (Kurzfassung)",
    subtitle="Auszug zur Datenraum-Vorlage; Volldokument siehe KD_001",
    sections=[
        ("Vertragspartner", "Halbreiter Maschinenbau GmbH und ThyssenKrupp Steel Europe AG (TKSE)."),
        ("Eckpunkte",
         ("list", [
             "Volumen ca. 12,5 Mio. EUR ueber 3 Jahre; Schluesselkunden-Status (Tier A).",
             "Laufzeit 14.06.2023 bis 31.12.2026, +12 Monate Verlaengerungsoption.",
             "Liefergegenstand: PL-500 Standard und Sonderausstattung fuer Werke Duisburg-Hamborn und Bochum.",
             "Preisanpassung jaehrlich (Materialindex Stahl + M+E NRW Tarif).",
             "Zahlung 30/40/25/5 (Anzahlung / Pre-FAT / IBN / Gewaehrl.).",
             "Liefer-Incoterm: DAP gemaess INCOTERMS 2020.",
             "Gewaehrleistung 24 Monate ab IBN.",
             "Eskalation: KAM Markus Fischer -> GF MMB -> Procurement Director TKSE.",
             "Spezialregelung: TKSE-Sonderbedingungen Stahl-Lieferanten-Code TKSE-SCC 2023 wird beigefuegt (Anlage 5).",
         ])),
        ("Anlagen",
         "Anlage 1: Technische Spezifikation\nAnlage 2: Preisliste 2023\nAnlage 3: NDA\nAnlage 4: LkSG-Erklaerung\nAnlage 5: TKSE-SCC 2023"),
    ],
)


print("OK regen_mueller_04.py – ~34 docs written")
