"""Mueller / mueller_small/ – polish 98 remaining thin docs to >= 250 words each.

Idempotent: overwrites .docx files in mueller_small/.
Heavily parameterized via small builder helpers + dict-driven tables.
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
from enhance_lib import MUELLER as M, write_doc, signatures

BASE = f"{_ROOT}/mueller_small"
H = {"name": M["name"], "addr": M["addr"], "hrb": M["hrb"]}

# ── Common boilerplate ─────────────────────────────────────────────────────────
BANK_BLOCK = (
    f"Bankverbindung: {M['bank']}\n"
    f"IBAN: {M['iban']}\nBIC: DEUTDEDB"
)
USTID_BLOCK = (
    f"USt-IdNr. Halbreiter Maschinenbau GmbH: {M['ust']}\n"
    "Steuernummer: 215/5765/9876, Finanzamt Koeln-Nord"
)
KONTAKT = "Halbreiter Maschinenbau GmbH, Industriestrasse 12, 50829 Koeln, Tel. +49 221 47832-0, info@halbreiter-maschinenbau.de"

# Generic helpers
def tbl(headers, rows):
    return [list(headers)] + [list(r) for r in rows]


def money(n):
    return f"{n:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# ════════════════════════════════════════════════════════════════════════════════
# 1. INDEX
# ════════════════════════════════════════════════════════════════════════════════

def gen_index():
    sections = [
        ("Zweck dieses Datenraum-Index",
         "Dieses Dokument fasst den Aufbau, die Gliederung und die Struktur des Due-Diligence-Datenraums der "
         "Halbreiter Maschinenbau GmbH zusammen. Der Datenraum wird im Rahmen einer Vendor Due Diligence durch die "
         "Geschaeftsfuehrung der Halbreiter Maschinenbau GmbH bereitgestellt und richtet sich an potentielle Investoren, "
         "Wirtschaftspruefer (BDO AG WPG) sowie die beratenden Rechtsanwaelte (Heuking Kuehn Lueer Wojtek). Der "
         "Bearbeitungsstand entspricht dem Stichtag 31. Dezember 2023; Aktualisierungen werden durch Sandra Becker (CFO) "
         "freigegeben und in der Versionshistorie am Ende dieses Dokumentes dokumentiert."),
        ("Unternehmensdaten im Ueberblick",
         tbl(["Merkmal", "Wert"],
             [["Firma",              M["name"]],
              ["Sitz",                M["addr"]],
              ["Registergericht",     M["hrb"]],
              ["USt-IdNr.",           M["ust"]],
              ["Geschaeftsfuehrung",  f"{M['ceo']} (CEO), {M['cfo']} (CFO)"],
              ["Geschaeftszweck",     M["geschaeftszweck"]],
              ["Umsatz 2023",         "48,63 Mio. EUR"],
              ["EBITDA 2023",         "5,98 Mio. EUR"],
              ["Mitarbeiter (FTE)",   "247"],
              ["Wirtschaftspruefer",  M["wp"]],
              ["Rechtsberater",       M["anwalt"]],
              ["Hausbank",            M["bank"]]])),
        ("Gliederung des Datenraums",
         tbl(["Ordner", "Inhalt", "Status"],
             [["00", "Index, Inhaltsverzeichnis, Datenraumregeln",                 "freigegeben"],
              ["01", "Gesellschaftsrechtliche Dokumente / Satzung / Gesellschafter","freigegeben"],
              ["02", "Finanzen, Jahresabschluesse, Buchhaltung, Bilanzanhang",     "freigegeben"],
              ["03", "Personal / HR (anonymisierte Personalakten, Tarif, BV)",     "freigegeben"],
              ["04", "Vertraege mit Kunden (Rahmenvertraege, AB, Rechnungen)",     "freigegeben"],
              ["05", "Vertraege mit Lieferanten (Bestellungen, Eingangsrechnungen)", "freigegeben"],
              ["06", "Immobilien (Eigentum, Miete, Grundrisse, Versicherungen)",   "freigegeben"],
              ["07", "IP / Lizenzen / Patente / Software-Subscriptions",           "freigegeben"],
              ["08", "Versicherungen (Police-Spiegel, Schadensmeldungen)",         "freigegeben"],
              ["09", "Compliance / Audits / Zertifikate / Datenschutz",            "freigegeben"],
              ["10", "IT-Infrastruktur und Informationssicherheit",                "freigegeben"],
              ["11", "Strategie, Planung, Beirats- und Geschaeftsfuehrerprotokolle","freigegeben"]])),
        ("Verbindlichkeit und Vertraulichkeit",
         "Saemtliche Dokumente unterliegen einer Vertraulichkeitsvereinbarung (NDA) zwischen den Parteien. Der Datenraum "
         "wird ueber den Anbieter Datasite/Drooms gehostet; Logins werden personenbezogen vergeben. Eine Vervielfaeltigung "
         "oder Weitergabe an Dritte ist ohne ausdrueckliche Zustimmung der Halbreiter Maschinenbau GmbH unzulaessig. "
         "Anfragen sind ueber den Q&A-Tracker des Datenraums zu stellen und werden binnen 48 Stunden durch die "
         "Geschaeftsfuehrung oder den jeweils zustaendigen Bereichsleiter beantwortet."),
        ("Ansprechpartner Datenraum",
         f"Datenraummanagement: Sandra Becker (CFO) – s.becker@halbreiter-maschinenbau.de\n"
         "Vertraulichkeit / Legal: Heuking Kuehn Lueer Wojtek, Frau RAin Dr. Beatrice Klein\n"
         "Tax / Wirtschaftspruefung: BDO AG WPG, Herr Dipl.-Kfm. Joachim Steger"),
        ("Versionshistorie",
         tbl(["Version", "Datum", "Bearbeitung", "Aenderung"],
             [["1.0", "15.01.2024", "Sandra Becker", "Initiale Befuellung"],
              ["1.1", "08.02.2024", "Sandra Becker", "Ordner 02/04 aktualisiert"],
              ["1.2", "12.03.2024", "Sandra Becker", "Q&A-Anhang, Compliance-Dokumente"]])),
    ]
    write_doc(f"{BASE}/00_INDEX_Due_Diligence_Uebersicht.docx", H,
              "Unternehmensuebersicht Due Diligence – Index",
              sections, confidential=True)


# ════════════════════════════════════════════════════════════════════════════════
# 2. FINANZEN
# ════════════════════════════════════════════════════════════════════════════════

def gen_fin_abschlusspruefung():
    sections = [
        ("Auftrag und Pruefungsgegenstand",
         "Die BDO AG Wirtschaftspruefungsgesellschaft (Niederlassung Koeln, verantwortlicher Partner WP/StB "
         "Joachim Steger) wurde durch Beschluss der Gesellschafterversammlung vom 26. Mai 2022 mit der Pruefung des "
         "Jahresabschlusses zum 31. Dezember 2022 sowie des zugehoerigen Lageberichts der Halbreiter Maschinenbau GmbH "
         "beauftragt. Die Pruefung wurde unter Beachtung der vom IDW festgestellten deutschen Grundsaetze "
         "ordnungsmaessiger Abschlusspruefung sowie ergaenzend der International Standards on Auditing (ISA) "
         "durchgefuehrt. Der vollstaendige Bericht hat einen Umfang von 184 Seiten; nachstehend wiedergegeben "
         "ist ein Auszug fuer Zwecke der Due Diligence."),
        ("Pruefungsergebnis (uneingeschraenkter Bestaetigungsvermerk)",
         "Nach unserer Beurteilung aufgrund der bei der Pruefung gewonnenen Erkenntnisse entspricht der Jahresabschluss "
         "den deutschen, fuer Kapitalgesellschaften geltenden handelsrechtlichen Vorschriften und vermittelt unter "
         "Beachtung der Grundsaetze ordnungsmaessiger Buchfuehrung ein den tatsaechlichen Verhaeltnissen entsprechendes "
         "Bild der Vermoegens-, Finanz- und Ertragslage der Halbreiter Maschinenbau GmbH zum 31. Dezember 2022. Der "
         "Lagebericht steht in Einklang mit dem Jahresabschluss, entspricht den gesetzlichen Vorschriften und "
         "vermittelt insgesamt ein zutreffendes Bild von der Lage der Gesellschaft."),
        ("Kennzahlen 2022 (Auszug)",
         tbl(["Kennzahl", "2022", "2021", "Veraenderung"],
             [["Umsatzerloese",        "44.180 TEUR", "39.620 TEUR", "+11,5 %"],
              ["Materialaufwand",      "21.084 TEUR", "19.276 TEUR", "+9,4 %"],
              ["Personalaufwand",      "15.870 TEUR", "14.940 TEUR", "+6,2 %"],
              ["EBITDA",                "5.230 TEUR",  "4.012 TEUR", "+30,4 %"],
              ["EBIT",                  "3.380 TEUR",  "2.420 TEUR", "+39,7 %"],
              ["Jahresueberschuss",     "2.187 TEUR",  "1.578 TEUR", "+38,6 %"],
              ["Eigenkapitalquote",     "38,4 %",      "36,1 %",     "+2,3 PP"],
              ["Bilanzsumme",          "31.840 TEUR", "29.220 TEUR", "+9,0 %"]])),
        ("Key Audit Matters (Auszug)",
         ("list",
          ["Bewertung der Pensionsrueckstellungen (Heubeck-Richttafeln 2018 G, Rechnungszins 1,80 %).",
           "Forderungsbewertung im langlaufenden Anlagenbau (Percentage-of-Completion).",
           "Werthaltigkeit aktivierter Entwicklungskosten (TEUR 1.420).",
           "Vorratsbewertung und Identifikation langsam drehender Bestaende.",
           "Konzentrationsrisiko bei den Top-5-Kunden (kumuliert 58 % Umsatzanteil)."])),
        ("Erklaerung des Wirtschaftspruefers",
         "Koeln, den 12. April 2023. WP/StB Joachim Steger, BDO AG Wirtschaftspruefungsgesellschaft. "
         "Der Bericht in Langfassung liegt in Ordner 02_Finanzen vor."),
    ]
    write_doc(f"{BASE}/02_Finanzen/FIN_Abschlussprüfungsbericht_WP_2022.docx", H,
              "Abschlusspruefungsbericht 2022 – Auszug", sections, confidential=True)


def gen_fin_rueckstellungen():
    sections = [
        ("Vorbemerkung",
         "Diese Uebersicht stellt die zum 31. Dezember 2023 nach HGB bilanzierten Rueckstellungen der "
         "Halbreiter Maschinenbau GmbH dar. Sie ist Bestandteil des Bilanzanhangs und der Vendor-Due-Diligence-Akten. "
         "Die Bewertung erfolgte nach handelsrechtlichen Vorschriften, insbesondere § 253 HGB; die Pensionsrueckstellung "
         "ist nach der projizierten Anwartschaftsbarwertmethode (PUC, IAS 19 analog) ermittelt worden."),
        ("Rueckstellungsspiegel zum 31.12.2023",
         tbl(["Position", "Stand 01.01.2023", "Verbrauch", "Aufloesung", "Zufuehrung", "Stand 31.12.2023"],
             [["Pensionsrueckstellungen",     "3.420 TEUR", "180 TEUR",   "—",        "260 TEUR", "3.500 TEUR"],
              ["Gewaehrleistung",             "1.260 TEUR", "640 TEUR",   "120 TEUR", "880 TEUR", "1.380 TEUR"],
              ["Urlaubs- und Gleitzeitkonten",  "780 TEUR", "780 TEUR",   "—",        "820 TEUR",   "820 TEUR"],
              ["Tantieme/Boni Geschaeftsleitung","440 TEUR", "440 TEUR",  "—",        "510 TEUR",   "510 TEUR"],
              ["Drohverluste Auftraege",        "210 TEUR", "—",          "60 TEUR",  "180 TEUR",   "330 TEUR"],
              ["Prozesskosten (Restbestand)",   "120 TEUR", "85 TEUR",   "—",         "40 TEUR",    "75 TEUR"],
              ["Sonstige (Archiv, Pruefung)",   "240 TEUR", "210 TEUR",  "10 TEUR",   "260 TEUR",  "280 TEUR"],
              ["Gesamt",                       "6.470 TEUR","2.335 TEUR","190 TEUR", "2.950 TEUR","6.895 TEUR"]])),
        ("Erlaeuterungen zu den wesentlichen Positionen",
         "Pensionsrueckstellungen: betreffen 22 Versorgungsberechtigte (Aktive und Rentner). Rechnungszins 1,80 % "
         "(Vorjahr 1,75 %), Gehaltstrend 2,5 %, Rententrend 1,5 %, Heubeck-Richttafeln 2018 G. Versicherungsmathematische "
         "Bewertung durch Heubeck AG, Koeln.\n\n"
         "Gewaehrleistung: pauschal 1,2 % auf gewaehrleistungspflichtige Umsatzerloese der letzten 24 Monate; "
         "Einzelrueckstellungen fuer bekannte Beanstandungen bei der Pressenlinie PL-500 (Charge Q3/2022) und "
         "Foerderbandanlage FB-200.\n\n"
         "Drohverluste: betrifft einen festpreisgebundenen Auftrag der Maschinenfabrik Niehoff (Kalkulationsrisiko "
         "Stahlbau) mit erwartetem Negativergebnis von 0,3 Mio. EUR (Stichtag 30.11.2023).\n\n"
         "Prozesskosten: Restbestand aus Vergleichsverhandlung mit ehem. Lieferant Hagedorn GmbH (Rechtsanwaelte "
         "Heuking Kuehn); voraussichtliche Erledigung in Q2/2024."),
        ("Pruefungsvermerk",
         "Die Rueckstellungsuebersicht wurde am 19. Februar 2024 durch Sandra Becker (CFO) freigegeben und im "
         "Rahmen der laufenden Pruefung 2023 durch BDO AG WPG eingesehen."),
    ]
    write_doc(f"{BASE}/02_Finanzen/FIN_Rückstellungsübersicht_2023.docx", H,
              "Rueckstellungsuebersicht – Stand 31. Dezember 2023", sections, confidential=True)


# ════════════════════════════════════════════════════════════════════════════════
# 3. HR
# ════════════════════════════════════════════════════════════════════════════════

def gen_hr_at_struktur():
    sections = [
        ("Geltungsbereich und Zweck",
         "Diese AT-Gehaltsstruktur regelt die Verguetung der auszertariflichen (AT) Angestellten der "
         "Halbreiter Maschinenbau GmbH. Sie gilt fuer alle Beschaeftigten oberhalb der hoechsten Tarifgruppe E13 des "
         "Tarifvertrages Metall- und Elektroindustrie NRW. Stichtag der Tabellenwerte ist der 1. April 2024. "
         "Die Struktur wurde von der Geschaeftsfuehrung am 12. Maerz 2024 beschlossen und mit dem Betriebsrat am "
         "20. Maerz 2024 in einer Regelungsabrede abgestimmt."),
        ("Verguetungsbaender 2024",
         tbl(["Band", "Funktionsbeispiele", "Jahres-Grundgehalt EUR", "Bonus-Ziel %", "Dienstwagen"],
             [["AT-1", "Junior Spezialist, Projektingenieur 1-3 J. BE",
               "62.000 - 78.000",  "8 %",   "—"],
              ["AT-2", "Senior-Ingenieur, Teamleiter, Bereichskoordinator",
               "78.000 - 96.000", "12 %",   "optional"],
              ["AT-3", "Abteilungsleiter, Werkleiter Stellv., Senior-Manager",
               "96.000 - 118.000","18 %",   "ja"],
              ["AT-4", "Bereichsleiter, Direktor, Generalbevollmaechtigte",
               "118.000 - 148.000","22 %",  "ja"],
              ["AT-5", "Geschaeftsfuehrung (gesondert geregelt im Anstellungsvertrag)",
               "—",                "—",     "ja"]])),
        ("Verguetungskomponenten",
         ("list",
          ["Grundgehalt: 12 gleiche Monatsraten, zahlbar zum letzten Werktag des Monats.",
           "Variable Verguetung: ergebnisabhaengig, gemessen an EBITDA-Quote und persoenlichen Zielen (60/40-Gewichtung).",
           "Urlaubs- und Weihnachtsgeld: in den AT-Baendern in das Grundgehalt eingerechnet (1/12).",
           "Betriebliche Altersversorgung: Direktversicherung bei Allianz, Arbeitgeberzuschuss 200 EUR/Monat ab AT-2.",
           "Mobilitaet: Dienstwagenrichtlinie ab Band AT-3 (Audi A4/BMW 3er-Klasse, BEV bevorzugt).",
           "Weiterbildung: Budget 2.500 EUR/Jahr (AT-1/2), 4.000 EUR/Jahr (ab AT-3)."])),
        ("Gehaltsanpassungen",
         "Tabellenwerte werden jaehrlich zum 1. April angepasst (Orientierung am Tarifabschluss IG Metall NRW). "
         "Ausserplanmaessige Anpassungen erfolgen ausschliesslich durch Beschluss der Geschaeftsfuehrung; Antragsweg "
         "ueber den jeweiligen Bereichsleiter via HR-System (Personio). Die individuelle Einordnung in die Baender "
         "ergibt sich aus der Stellenbeschreibung und der Funktionsbewertung (Mercer IPE)."),
        ("Datenschutz und Vertraulichkeit",
         "Diese Tabelle ist als »intern – streng vertraulich« klassifiziert. Eine Weitergabe an Dritte oder an "
         "Mitarbeiter ausserhalb der Geschaeftsfuehrung und der Personalabteilung ist nicht zulaessig."),
    ]
    write_doc(f"{BASE}/03_Personal_HR/HR_Gehaltsstruktur_AT_Mitarbeiter_2024.docx", H,
              "AT-Gehaltsstruktur 2024 – Halbreiter Maschinenbau GmbH", sections, confidential=True)


# ════════════════════════════════════════════════════════════════════════════════
# 4. KUNDEN — Rechnungen + Rahmenvertrag + SLA + Kundenzufriedenheit
# ════════════════════════════════════════════════════════════════════════════════

KUNDEN = {
    "TKS":  dict(name="ThyssenKrupp Steel Europe AG", addr="Kaiser-Wilhelm-Strasse 100, 47166 Duisburg",  kdnr="K-001"),
    "BOSR": dict(name="Bosch Rexroth AG",             addr="Zum Eisengiesser 1, 97816 Lohr am Main",       kdnr="K-002"),
    "HELLA":dict(name="Hella GmbH & Co. KGaA",        addr="Rixbecker Strasse 75, 59552 Lippstadt",        kdnr="K-003"),
    "VIES": dict(name="Viessmann Climate Solutions SE",addr="Viessmannstrasse 1, 35108 Allendorf (Eder)",  kdnr="K-004"),
    "DUERR":dict(name="Duerr AG",                     addr="Carl-Benz-Strasse 34, 74321 Bietigheim-Bissingen", kdnr=""),
    "HAVB": dict(name="Haver & Boecker OHG",          addr="Carl-Haver-Platz 3, 59302 Oelde",              kdnr="K-014"),
    "HEYL": dict(name="Gebr. Heyl GmbH & Co. KG",     addr="Max-Planck-Strasse 23, 31135 Hildesheim",      kdnr="K-018"),
    "NIEH": dict(name="Maschinenfabrik Niehoff GmbH & Co. KG", addr="Walter-Niehoff-Strasse 2, 91126 Schwabach", kdnr="K-021"),
}
KUNDEN["DUERR"]["kdnr"] = "K-005"


def rechnung(fname, title, kkey, leistung, datum, positionen, summe_netto, bezug=""):
    K = KUNDEN[kkey]
    bezug_line = f"\nBezug: {bezug}" if bezug else ""
    netto = summe_netto
    ust   = round(netto * 0.19, 2)
    brutto= round(netto + ust, 2)

    pos_table = (
        [["Pos", "Beschreibung", "Menge", "Einheit", "Einzelpreis EUR", "Gesamt EUR"]] +
        positionen +
        [["", "Zwischensumme netto", "", "", "", money(netto)],
         ["", "Umsatzsteuer 19 %",    "", "", "", money(ust)],
         ["", "GESAMT brutto",         "", "", "", money(brutto)]]
    )

    sections = [
        ("Rechnungsempfaenger",
         f"{K['name']}\n{K['addr']}\nKundennummer: {K['kdnr']}{bezug_line}"),
        ("Leistungs- bzw. Lieferzeitraum",
         f"Leistungs-/Lieferdatum: {leistung}.\nFakturadatum (Rechnungsstellung): {datum}.\n"
         "Fakturierende Stelle: Halbreiter Maschinenbau GmbH, Buchhaltung Debitoren, Industriestrasse 12, 50829 Koeln."),
        ("Rechnungspositionen", pos_table),
        ("Zahlungsbedingungen",
         "Zahlbar binnen 14 Tagen netto auf das nachstehende Konto unter Angabe der Rechnungsnummer. "
         "Bei Zahlung innerhalb von 8 Tagen wird kein Skonto gewaehrt. Verzugszinsen 9 Prozentpunkte ueber "
         "Basiszinssatz gemaess § 288 Abs. 2 BGB.\n\n" + BANK_BLOCK),
        ("Steuerliche Angaben", USTID_BLOCK),
        ("Hinweise",
         "Die Rechnung wird elektronisch im X-Rechnungs-Format (XRechnung 2.3.2) ueber das Buyer-Portal des "
         "Kunden uebermittelt; ein Original-Beleg in Papier ist auf Anforderung erhaeltlich. Reklamationen sind "
         "binnen 14 Tagen schriftlich anzuzeigen. Eigentumsvorbehalt: gelieferte Ware bleibt bis zur vollstaendigen "
         "Bezahlung Eigentum der Halbreiter Maschinenbau GmbH (verlaengerter Eigentumsvorbehalt gemaess EKBs)."),
        ("Kontakt Buchhaltung und Archivierung",
         "Fragen zur Rechnung: Tatjana Weber, Telefon +49 221 47832-31, t.weber@halbreiter-maschinenbau.de. "
         "Diese Rechnung wurde maschinell erstellt und ist auch ohne Unterschrift gueltig. "
         "Aufbewahrungsfrist: 10 Jahre gemaess § 147 AO. Die elektronische Originaldatei wird revisionssicher im DMS "
         "(M-Files) abgelegt; der zugehoerige XRechnungs-XML-Stream wird ueber das Buyer-Portal des Kunden "
         "uebermittelt und durch eine qualifizierte elektronische Signatur des MMB-Signaturdienstleisters "
         "(D-TRUST GmbH) gegen Manipulation geschuetzt. Bei Zahlungsverzug erfolgen Mahnungen automatisiert "
         "(1. Mahnung: 14 Tage nach Faelligkeit, kostenfrei; 2. Mahnung: 14 Tage spaeter mit Mahngebuehr 5,00 EUR; "
         "3. Mahnung mit anschliessender Uebergabe an den Forderungs-Service der BFS Finance GmbH)."),
    ]
    write_doc(f"{BASE}/04_Vertraege_Kunden/{fname}.docx", H, title,
              subtitle=f"Fakturadatum: {datum}", sections=sections)


def gen_rechnungen():
    rechnung("KD_RE001_Rechnung_ThyssenKrupp_Steel", "Rechnung Nr. 2023-RE-0421", "TKS",
             "lt. Lieferschein (AB-2023-014)", "08. November 2023",
             [["1", "Vorauszahlung 30 % Pressenlinie PL-500 (AB-2023-014)", "1", "psch.", "996.000,00", "996.000,00"]],
             996000.00, bezug="Auftragsbestaetigung AB-2023-014; Projekt »Vorauszahlung 30 % Pressenlinie PL-500«")
    rechnung("KD_RE002_Rechnung_Bosch_Rexroth_AG",   "Rechnung Nr. 2024-RE-0042", "BOSR",
             "lt. Lieferschein LS-2024-0124", "12. Februar 2024",
             [["1", "Foerderbandanlage FB-200, Konfiguration BR-Standard",  "2", "St.", "84.500,00", "169.000,00"],
              ["2", "Montage und Inbetriebnahme vor Ort",                   "1", "psch.","18.400,00", "18.400,00"],
              ["3", "Verpackung und Anlieferung DAP Lohr",                  "1", "psch.", "2.800,00",  "2.800,00"]],
             190200.00, bezug="Bestellung BR-2023-09-1820; Werk Lohr")
    rechnung("KD_RE003_Rechnung_Hella_GmbH_und_Co._K","Rechnung Nr. 2024-RE-0114","HELLA",
             "lt. Lieferschein (Teillieferung Robotik)", "06. Maerz 2024",
             [["1", "Montageroboter MR-150 inkl. Greifer-Set", "3", "St.", "62.400,00", "187.200,00"],
              ["2", "Programmierung und Sicherheitsabnahme",   "1", "psch.","12.800,00", "12.800,00"]],
             200000.00, bezug="Rahmenabruf Hella 2024-Q1, AB-2024-021")
    rechnung("KD_RE004_Rechnung_Viessmann_Climate_", "Rechnung Nr. 2024-RE-0128", "VIES",
             "lt. Lieferschein (Laser LS-800)", "14. Maerz 2024",
             [["1", "Laserschneidanlage LS-800, 5-Achs-CNC",        "1", "St.", "412.000,00", "412.000,00"],
              ["2", "Filterpaket Hochleistung Premium",             "1", "St.",   "8.400,00",   "8.400,00"],
              ["3", "Schulung Bediener (2 Tage, vor Ort Allendorf)","2", "TG",   "1.450,00",   "2.900,00"]],
             423300.00, bezug="Auftragsbestaetigung AB-2024-008")
    rechnung("KD_RE005_Rechnung_Dürr_AG",          "Rechnung Nr. 2024-RE-0188", "DUERR",
             "lt. Lieferschein (Teillieferung Endbearbeitung)", "29. Maerz 2024",
             [["1", "Montagezelle MR-150 + FB-200 (kombiniert)", "1", "St.", "238.000,00", "238.000,00"],
              ["2", "Engineering Sondererweiterung",             "1", "psch.","42.000,00",  "42.000,00"]],
             280000.00, bezug="Bestellung Duerr DPO-2024-0119; Werk Bietigheim")
    rechnung("KD_RE006_Rechnung_ThyssenKrupp_Steel","Rechnung Nr. 2024-RE-0214", "TKS",
             "lt. Lieferschein (Restzahlung PL-500)", "12. April 2024",
             [["1", "Restzahlung 70 % Pressenlinie PL-500 (AB-2023-014)", "1", "psch.", "2.324.000,00", "2.324.000,00"]],
             2324000.00, bezug="Schlussrechnung zu AB-2023-014")
    rechnung("KD_RE007_Rechnung_Bosch_Rexroth_AG",  "Rechnung Nr. 2024-RE-0250", "BOSR",
             "lt. Lieferschein FB-200 Charge 2", "26. April 2024",
             [["1", "Foerderbandanlage FB-200, Konfiguration BR-XL", "1", "St.", "112.000,00", "112.000,00"],
              ["2", "Sonderzubehoer: Schwenkmodul, Auswerfer-Kit",   "1", "psch.","18.800,00",  "18.800,00"]],
             130800.00, bezug="Abruf Rahmenvertrag BR-2023-09-1820")
    rechnung("KD_RE008_Rechnung_Haver_und_Boecker_OH","Rechnung Nr. 2024-RE-0312","HAVB",
             "lt. Lieferschein (Sondermaschine)", "21. Mai 2024",
             [["1", "Sondermontagestation auf Basis MR-150", "1", "St.", "118.500,00", "118.500,00"],
              ["2", "Engineering und Kundenspezifik",        "1", "psch.","24.600,00",  "24.600,00"]],
             143100.00, bezug="AB-2024-031 Werk Oelde")
    rechnung("KD_RE009_Rechnung_Gebr._Heyl_GmbH_und_","Rechnung Nr. 2024-RE-0098","HEYL",
             "lt. Lieferschein (FB-200 Standard)", "29. Februar 2024",
             [["1", "Foerderbandanlage FB-200, Standardkonfiguration", "1", "St.", "78.400,00", "78.400,00"],
              ["2", "Montage vor Ort Hildesheim",                       "1", "psch.","11.200,00", "11.200,00"]],
             89600.00, bezug="Bestellung Heyl HL-2024-018")
    rechnung("KD_RE010_Rechnung_Maschinenfabrik_Ni","Rechnung Nr. 2024-RE-0282", "NIEH",
             "lt. Lieferschein (Stanzpresse Sonderausfuehrung)", "10. Mai 2024",
             [["1", "Pressenlinie PL-500 Sonderausfuehrung", "1", "St.", "1.124.000,00", "1.124.000,00"],
              ["2", "Anschluss- und Sicherheitseinrichtung", "1", "psch.","48.000,00",     "48.000,00"]],
             1172000.00, bezug="AB-2024-014 Werk Schwabach")


def gen_kd_rahmenvertrag_tks():
    sections = [
        ("Vertragsparteien",
         f"{M['name']}, {M['addr']} ('Lieferant') und ThyssenKrupp Steel Europe AG, Kaiser-Wilhelm-Strasse 100, "
         "47166 Duisburg, eingetragen im Handelsregister des AG Duisburg HRB 9326 ('Besteller')."),
        ("Praeambel",
         "Der Lieferant ist auf Entwicklung und Herstellung von Sondermaschinen, insbesondere Pressenlinien, "
         "spezialisiert. Der Besteller setzt diese Maschinen in seinen Stahlwerken zur Weiterverarbeitung von "
         "Walzprodukten ein. Die Parteien schliessen diesen Rahmenvertrag zur Vereinheitlichung der Liefer- und "
         "Vertragsbedingungen fuer die kommenden Abrufe."),
        ("Vertragsinhalt",
         ("clauses",
          [("§ 1 Vertragsgegenstand",
            ["Gegenstand sind die Lieferung von Pressenlinien der Baureihe PL-500 sowie zugehoerige Ersatzteile, "
             "Serviceleistungen und Inbetriebnahmen.",
             "Konkrete Liefermengen, Lieferorte und Preisstaffeln werden ueber Einzelabrufe (Bestellungen) festgelegt; "
             "ein Mindestabnahmevolumen ist nicht vereinbart."]),
           ("§ 2 Preise und Zahlung",
            ["Preise nach Preisliste 2023, Stand 1. Februar 2023. Eine jaehrliche Indexierung erfolgt nach VDMA-Preisgleitklausel.",
             "Zahlungsziel 30 Tage netto ab Rechnungserhalt; Skonto 2 % bei Zahlung binnen 14 Tagen.",
             "Bei Anlagen ueber 500 TEUR Auftragswert: Vorauszahlung 30 % bei AB, 60 % bei Versand, 10 % nach erfolgreicher Abnahme."]),
           ("§ 3 Lieferung und Gefahruebergang",
            ["Lieferung DAP Werk Duisburg (INCOTERMS 2020). Gefahruebergang mit Anlieferung am Werkstor des Bestellers."]),
           ("§ 4 Gewaehrleistung",
            ["24 Monate ab erfolgreicher Abnahme. Verlaengerung auf 36 Monate gegen Aufpreis 2,5 % moeglich.",
             "Reaktionszeit bei Stoerungen Klasse A (Anlagenstillstand): 4 Stunden remote / 24 Stunden vor Ort."]),
           ("§ 5 Haftung",
            ["Haftung beschraenkt auf den 2-fachen Auftragswert pro Schadensereignis, kumuliert auf 6 Mio. EUR pro Vertragsjahr; "
             "ausgenommen Vorsatz, grobe Fahrlaessigkeit, Verletzung wesentlicher Vertragspflichten."]),
           ("§ 6 Compliance und Lieferketten",
            ["Die Parteien erkennen gegenseitig die Verhaltenskodexe (Code of Conduct) sowie die "
             "Lieferkettensorgfaltspflicht (LkSG, ab 2024 auch fuer den Lieferanten verbindlich) an."]),
           ("§ 7 Laufzeit und Schlussbestimmungen",
            ["Laufzeit 1.1.2023 - 31.12.2025 mit automatischer Verlaengerung um jeweils 12 Monate, "
             "wenn nicht 6 Monate vor Ablauf gekuendigt wird. Gerichtsstand: Duesseldorf. Schriftform."])])),
        ("Unterschriften",
         signatures(M["ceo"], "Geschaeftsfuehrer", M["name"],
                    "Dr. Bernhard Osburg", "Vorstand Steel", "ThyssenKrupp Steel Europe AG",
                    place="Koeln/Duisburg", date_str_="20. Februar 2023")),
    ]
    write_doc(f"{BASE}/04_Vertraege_Kunden/KD_Rahmenvertrag_ThyssenKrupp_2023.docx", H,
              "Rahmenvertrag ThyssenKrupp Steel Europe AG 2023 (Kurzfassung)", sections,
              confidential=True)


def gen_kd_sla_bosch():
    sections = [
        ("Parteien und Geltungsbereich",
         f"{M['name']} ('Auftragnehmer') und Bosch Rexroth AG, Zum Eisengiesser 1, 97816 Lohr am Main ('Auftraggeber') "
         "vereinbaren das nachfolgende Service-Level-Agreement (SLA) als Anlage 3 zum Rahmenvertrag BR-2023-09-1820. "
         "Das SLA regelt den After-Sales-Service fuer die durch den Auftragnehmer gelieferten Foerderbandanlagen FB-200 "
         "und Montageroboter MR-150 in den Werken Lohr, Erbach und Schweinfurt."),
        ("Service-Klassen und Reaktionszeiten",
         tbl(["Klasse", "Beschreibung", "Reaktionszeit Remote", "Reaktionszeit vor Ort", "Wiederherstellzeit"],
             [["A", "Anlagenstillstand (line down)",         "30 min",  "4 h",  "24 h"],
              ["B", "Wesentliche Funktionseinschraenkung",   "2 h",     "8 h",  "48 h"],
              ["C", "Geringfuegige Stoerung, Workaround moeglich", "8 h", "Naechster Werktag", "5 AT"],
              ["D", "Wartung, Patches, Updates",              "—",      "geplant", "geplant"]])),
        ("Verfuegbarkeitszusagen",
         "Service-Verfuegbarkeit Hotline: Mo-Fr 06:00-22:00 Uhr, Sa 08:00-16:00 Uhr; ausserhalb dieser Zeiten "
         "Bereitschaftsdienst mit Reaktionszeit gemaess Klasse A. Anlagen-Verfuegbarkeit (Mean Time Between Failures, "
         "MTBF) FB-200: > 8.500 Betriebsstunden; MR-150: > 12.000 Betriebsstunden. "
         "Bei Unterschreitung der zugesagten Wiederherstellzeit greift ein Service-Credit gemaess Anhang B."),
        ("Wartungspakete",
         ("list",
          ["Basispaket: 2 Praeventiv-Wartungen pro Jahr, inkl. Inspektionsprotokoll und Ersatzteilbericht.",
            "Premium-Paket: 4 Praeventiv-Wartungen + Predictive-Monitoring via MMB-IoT-Cloud + 24/7-Hotline.",
            "Ersatzteilbevorratung: Verschleissteile auf Lager Lohr (Werkstattvereinbarung) oder Konsignationslager.",
            "Software-Updates: Patches kostenfrei, Major-Releases gegen Verguetung gemaess Preisliste."])),
        ("Preise und Verguetung",
         "Basispaket pauschal 28.000 EUR/Jahr je Anlage; Premium-Paket 48.000 EUR/Jahr je Anlage. "
         "Einsatzstunden ausserhalb des Wartungspaketes nach Stundensatz 142,00 EUR (Werktag) / 198,00 EUR (Wochenende). "
         "Anfahrtspauschale 320 EUR je Einsatz. Saemtliche Preise zzgl. gesetzlicher Mehrwertsteuer."),
        ("Laufzeit und Kuendigung",
         "Laufzeit 01.01.2023 - 31.12.2025. Kuendigung mit 6 Monaten Frist zum Ende der Vertragslaufzeit. "
         "Ausserordentliche Kuendigung aus wichtigem Grund bleibt unberuehrt."),
        ("Unterschriften",
         signatures(M["ceo"], "Geschaeftsfuehrer", M["name"],
                    "Dr. Marc Wucherer", "Vorstand Industrial Hydraulics", "Bosch Rexroth AG",
                    place="Koeln/Lohr", date_str_="15. Dezember 2022")),
    ]
    write_doc(f"{BASE}/04_Vertraege_Kunden/KD_SLA_After_Sales_Service_Bosch_2023.docx", H,
              "SLA After-Sales-Service Bosch Rexroth AG 2023-2025", sections, confidential=True)


def gen_kd_zufriedenheit():
    sections = [
        ("Auftrag und Methodik",
         "Die jaehrliche Kundenzufriedenheitsumfrage wurde durch die externe Marktforschung KANTAR GmbH (Frankfurt) "
         "im Auftrag der Halbreiter Maschinenbau GmbH zwischen September und November 2023 durchgefuehrt. Befragt wurden "
         "die 32 wichtigsten Kunden (A- und B-Kunden, > 70 % Umsatzanteil). Die Erhebung erfolgte mittels strukturierter "
         "Online-Befragung sowie telefonischer Tiefeninterviews mit Einkaufsleitern und technischen Ansprechpartnern. "
         "Ruecklaufquote: 78 % (25 Antworten verwertbar)."),
        ("Kernergebnisse",
         tbl(["Dimension", "Skala 1-5 (5=Top)", "Vorjahr", "Trend"],
             [["Produktqualitaet",          "4,4", "4,3", "↗"],
              ["Liefertreue (Termintreue)", "4,1", "4,0", "↗"],
              ["Servicequalitaet",          "4,3", "4,2", "↗"],
              ["Preis-Leistungs-Verhaeltnis","3,9", "3,8", "↗"],
              ["Innovationskraft",          "4,2", "4,0", "↗"],
              ["Kommunikation Vertrieb",    "4,5", "4,4", "↗"],
              ["Reaktion bei Reklamationen","4,0", "3,9", "↗"],
              ["Net Promoter Score (NPS)", "+48", "+42", "↗"]])),
        ("Wesentliche Erkenntnisse",
         ("list",
          ["Hohe Zufriedenheit bei Produktqualitaet und Servicekommunikation; Bestaetigung der Premium-Positionierung.",
           "Verbesserungspotenzial bei Reaktionszeit Ersatzteilversand (Wunsch < 24 h).",
           "Wunsch nach erweitertem Self-Service-Portal (Ersatzteil-Konfigurator, Wartungsplaner).",
           "Top-5-Kunden bestaetigen Wiederkaufabsicht (»definitiv ja«) zu 92 %.",
           "Kritik bei Dokumentationsstand (Software-Releases sollen frueher angekuendigt werden)."])),
        ("Massnahmenplan 2024",
         tbl(["Massnahme", "Verantwortlich", "Termin"],
             [["Ersatzteil-Versand 24-h-Garantie A-Kunden", "Vertrieb / Logistik", "Q1 2024"],
              ["Customer-Portal v2 (Wartungsplaner)",        "IT / Service",        "Q3 2024"],
              ["Roadmap-Communication-Plan Software",        "Produktmanagement",   "Q2 2024"],
              ["Re-Audit ISO 9001 mit Fokus Reklamation",   "Qualitaetswesen",      "Q4 2024"]])),
        ("Schlussbemerkung",
         "Die Geschaeftsfuehrung hat die Ergebnisse am 12. Dezember 2023 zur Kenntnis genommen und den Massnahmenplan "
         "2024 freigegeben. Die naechste Erhebung ist fuer Q3/2024 vorgesehen."),
    ]
    write_doc(f"{BASE}/04_Vertraege_Kunden/KD_Kundenzufriedenheitsumfrage_2023.docx", H,
              "Kundenzufriedenheitsumfrage 2023", sections)


# ════════════════════════════════════════════════════════════════════════════════
# 5. LIEFERANTEN – Bestellungen, Eingangsrechnungen, Rahmenvertraege, Audits
# ════════════════════════════════════════════════════════════════════════════════

LIEF = {
    "SCHUNK":  dict(name="Schunk GmbH & Co. KG",                addr="Bahnhofstrasse 106-134, 74348 Lauffen am Neckar",  knr="L-001"),
    "IGUS":    dict(name="Igus GmbH",                            addr="Spicher Strasse 1a, 51147 Koeln",                  knr="L-002"),
    "SIEMENS": dict(name="Siemens AG, Digital Industries",       addr="Werner-von-Siemens-Strasse 50, 91052 Erlangen",    knr="L-003"),
    "TRUMPF":  dict(name="Trumpf SE + Co. KG",                   addr="Johann-Maus-Strasse 2, 71254 Ditzingen",           knr="L-004"),
    "DBSCH":   dict(name="DB Schenker Deutschland AG",           addr="Edmund-Rumpler-Strasse 3, 60549 Frankfurt am Main", knr="L-006"),
    "TRUMPF_FS":dict(name="Trumpf Financial Services GmbH",      addr="Johann-Maus-Strasse 2, 71254 Ditzingen",           knr="L-004-FS"),
}


def bestellung(fname, lkey, bnr, datum, positionen, summe_netto):
    L = LIEF[lkey]
    netto = summe_netto
    ust = round(netto * 0.19, 2)
    brutto = round(netto + ust, 2)
    pos_table = (
        [["Pos", "Material-Nr. Lieferant", "Beschreibung", "Menge", "Einheit", "Einzelpreis EUR", "Gesamt EUR"]] +
        positionen +
        [["", "", "Zwischensumme netto", "", "", "", money(netto)],
         ["", "", "Umsatzsteuer 19 %",    "", "", "", money(ust)],
         ["", "", "GESAMT brutto",         "", "", "", money(brutto)]]
    )
    sections = [
        ("Empfaenger Lieferant", f"{L['name']}\n{L['addr']}\nLieferantennummer: {L['knr']}"),
        ("Bestellpositionen", pos_table),
        ("Liefer- und Zahlungsbedingungen",
         "Lieferung: DAP Werk Koeln (INCOTERMS 2020) gemaess Standard-EKBs der Halbreiter Maschinenbau GmbH. "
         "Zahlungsziel 30 Tage netto bzw. 2 % Skonto bei Zahlung binnen 14 Tagen.\n\n"
         "Lieferadresse: Halbreiter Maschinenbau GmbH, Wareneingang Halle C, Industriestrasse 12, 50829 Koeln, "
         "Tor 3, Anlieferzeiten Mo-Fr 07:00-15:00 Uhr.\n\n"
         "Versandfertigmeldung (ASN) bitte 24 Std. vor Eintreffen per EDI an asn@halbreiter-maschinenbau.de "
         "(EDIFACT DESADV-Format). Der Lieferant verpflichtet sich, Lieferverzoegerungen unverzueglich "
         "anzuzeigen; Konventionalstrafe 0,5 % je angefangener Woche, max. 5 % des Auftragswertes."),
        ("Qualitaet und Compliance",
         "Erstmusterpruefbericht (Erstmuster gemaess VDA Band 2) ist mit der Erstlieferung beizustellen. "
         "Materialzertifikate (3.1 nach EN 10204 fuer Werkstoffe) auf Anforderung. "
         "Es gelten die Allgemeinen Einkaufsbedingungen Halbreiter Maschinenbau GmbH (Stand 1.1.2024). "
         "Lieferketten-Sorgfaltspflicht gemaess LkSG ist anzuerkennen. "
         "REACH-/RoHS-Konformitaet ist mit jeder Lieferung zu bestaetigen."),
        ("Verpackung und Etikettierung",
         "Mehrwegtraeger gemaess Verpackungsrichtlinie MMB-EK-VPK-001 (Rev. 4). Etikettierung nach VDA 4902 mit "
         "GS1-Barcode. Beipackdokumente: Lieferschein, Konformitaetserklaerung, ggf. Sicherheitsdatenblatt."),
        ("Bearbeitung",
         "Sachbearbeiter Einkauf: Stefan Braun, Telefon +49 221 47832-22, s.braun@halbreiter-maschinenbau.de. "
         "Bestellnummer und Kostenstelle (lt. Lieferschein) bei allen Korrespondenzen zwingend angeben. "
         f"Bankverbindung Lieferant gemaess Stammsatz im SAP-System der {M['name']}."),
    ]
    write_doc(f"{BASE}/05_Vertraege_Lieferanten/{fname}.docx", H,
              f"Bestellung Nr. {bnr}", subtitle=f"Bestelldatum: {datum}", sections=sections)


def gen_bestellungen():
    bestellung("LF_B001_Bestellung_Schunk_GmbH_und_C", "SCHUNK", "BE-2024-01-0142", "12. Januar 2024",
               [["1", "PGN-PLUS-P-200", "Kraftspannblock pneumatisch 200 mm",      "8",  "St.",  "1.580,00", "12.640,00"],
                ["2", "PZB-PLUS-160",   "Parallelgreifer 160 mm",                  "12", "St.",  "892,00",  "10.704,00"],
                ["3", "MMS-22-S-PNP",   "Magnetfeldsensor M8x1 PNP",               "48", "St.",   "78,00",   "3.744,00"]],
               27088)
    bestellung("LF_B002_Bestellung_Igus_GmbH", "IGUS", "BE-2024-01-0148", "18. Januar 2024",
               [["1", "E14.4.038.50", "Energiekette 14er, Innenbreite 38 mm, Laenge 1500 mm", "12", "St.", "245,00", "2.940,00"],
                ["2", "TRE.50.50.075","Polymerleitung 50x50 mm",                              "240","m",   "32,40", "7.776,00"],
                ["3", "CFROBOT5",     "Robotik-Hochflexkabel CFRobot5",                       "180","m",   "28,40", "5.112,00"]],
               15828)
    bestellung("LF_B003_Bestellung_Siemens_AG_–_An", "SIEMENS", "BE-2024-02-0184", "8. Februar 2024",
               [["1", "6SL3210-5HE17-0KF0", "SINAMICS S210 Servo 7,0 A",         "6", "St.", "3.420,00", "20.520,00"],
                ["2", "1FK7080-5AF71-1RG0", "Servomotor SIMOTICS 1FK7",          "6", "St.", "2.840,00", "17.040,00"],
                ["3", "6SL3055-0AA00-3AA0", "Optionsbaugruppe CBC10 Kommunikation","6","St.",  "385,00",  "2.310,00"]],
               39870)
    bestellung("LF_B004_Bestellung_Trumpf_SE_plus_Co.", "TRUMPF", "BE-2024-02-0212", "22. Februar 2024",
               [["1", "TRUDISK-8002-FW", "Faserlaser 8 kW Resonator + Strahlfuehrung", "1", "St.", "245.000,00", "245.000,00"],
                ["2", "BC-040-LASKOPF",  "Laserschneidkopf BC-040",                    "1", "St.",  "42.000,00",  "42.000,00"],
                ["3", "FILTER-PREMIUM",  "Filterpaket Hochleistung 4-stufig",          "1", "St.",   "8.400,00",   "8.400,00"]],
               295400)
    bestellung("LF_B005_Bestellung_Schunk_GmbH_und_C", "SCHUNK", "BE-2024-03-0241", "12. Maerz 2024",
               [["1", "VERO-S-NSL-160", "Schnellwechselsystem VERO-S NSL 160", "4", "St.", "2.180,00", "8.720,00"],
                ["2", "RWA-9-180",      "Robotik-Werkzeugadapter RWA 180",     "8", "St.",   "920,00", "7.360,00"]],
               16080)


def eingangsrechnung(fname, lkey, rnr, rdatum, positionen, summe_netto, bestellbezug):
    L = LIEF[lkey]
    netto = summe_netto
    ust = round(netto * 0.19, 2)
    brutto = round(netto + ust, 2)
    pos_table = (
        [["Pos", "Beschreibung", "Menge", "Einheit", "Einzelpreis EUR", "Gesamt EUR"]] +
        positionen +
        [["", "Zwischensumme netto", "", "", "", money(netto)],
         ["", "Umsatzsteuer 19 %",    "", "", "", money(ust)],
         ["", "GESAMT brutto",         "", "", "", money(brutto)]]
    )
    sections = [
        ("Rechnungssteller (Lieferant)",
         f"{L['name']}\n{L['addr']}\nLieferantennummer (intern): {L['knr']}"),
        ("Bezug und Wareneingang",
         f"Bezug: {bestellbezug}.\nWareneingang gebucht durch Wareneingang Halle C, Buchungsdatum "
         "lt. Lieferschein. Pruefung durch Stefan Braun (Einkauf) am Tage des Wareneingangs."),
        ("Rechnungspositionen", pos_table),
        ("Zahlungspruefung",
         "Sachliche und rechnerische Pruefung durch Buchhaltung Kreditoren (Frau Anja Lenz). "
         "Freigabe in SAP MM unter Belegnummer und 4-Augen-Prinzip durch den Bereichsleiter Einkauf "
         "(Holger Brinkmann). Skontofrist 14 Tage; Zahlungslauf Mittwoch und Freitag."),
        ("Kontierung",
         tbl(["Konto", "Bezeichnung", "Anteil"],
             [["3400/3401", "Wareneingang/Bestandsveraenderung", "100 %"],
              ["1576",      "Vorsteuer 19 %",                    f"{money(ust)} EUR"],
              ["1600",      "Verbindlichkeiten LuL",             f"{money(brutto)} EUR"]])),
        ("Steuerliche Angaben Lieferant", "Die Rechnung erfuellt die Anforderungen § 14 UStG. " + USTID_BLOCK),
        ("Hinweise und Archivierung",
         "Die Rechnung wurde elektronisch (ZUGFeRD 2.1 / X-Rechnung) ueber das Lieferantenportal eingereicht; "
         "das Original liegt revisionssicher in der Belegablage Kreditorenbuchhaltung (Archivnummer KRDT-2024). "
         "Aufbewahrungsfrist 10 Jahre gemaess § 147 AO. Reklamationen werden ueber das Wareneingangs-Beanstandungs-"
         "formular (Vordruck MMB-WE-Q-014) abgewickelt; Frist 14 Tage ab Rechnungserhalt. Skontoabzug ist nur bei "
         "fristgerechter Zahlung zulaessig, der Skonto-Tag wird im SAP MM-Beleg automatisch berechnet. "
         "Bankverbindung des Lieferanten ergibt sich aus dem Stammsatz im SAP-System und wurde vor Buchung gegen "
         "Bankverbindungs-Whitelist (Compliance, Frau Anja Lenz) abgeglichen, um Lieferantenbetrug (CEO-Fraud, "
         "Fake-IBAN) zu vermeiden. Bei Abweichungen wird ein 4-Augen-Verifikationsprozess ausgeloest "
         "(telefonische Rueckbestaetigung durch den Kreditorenstamm-Verantwortlichen)."),
    ]
    write_doc(f"{BASE}/05_Vertraege_Lieferanten/{fname}.docx", H,
              f"Eingangsrechnung – {L['name']}", subtitle=f"Rechnungsdatum: {rdatum}",
              sections=sections)


def gen_eingangsrechnungen():
    eingangsrechnung("LF_ER001_Eingangsrechnung_Schunk_GmbH_und_Co._","SCHUNK",
                     "RN-2024-0098", "18. Januar 2024",
                     [["1","Kraftspannblock pneumatisch 200 mm","8","St.","1.580,00","12.640,00"],
                      ["2","Parallelgreifer 160 mm",            "12","St.","892,00", "10.704,00"],
                      ["3","Magnetfeldsensor M8x1 PNP",         "48","St.","78,00",   "3.744,00"]],
                     27088, "Bestellung BE-2024-01-0142")
    eingangsrechnung("LF_ER002_Eingangsrechnung_Igus_GmbH","IGUS",
                     "IG-RE-2024-00214", "24. Januar 2024",
                     [["1","Energiekette 14er, 1500 mm","12","St.","245,00", "2.940,00"],
                      ["2","Polymerleitung 50x50",      "240","m",  "32,40", "7.776,00"],
                      ["3","Robotik-Kabel CFRobot5",    "180","m",  "28,40", "5.112,00"]],
                     15828, "Bestellung BE-2024-01-0148")
    eingangsrechnung("LF_ER003_Eingangsrechnung_Siemens_AG_–_Antri","SIEMENS",
                     "SIE-RG-2024-30142", "14. Februar 2024",
                     [["1","SINAMICS S210 Servo 7,0 A",          "6","St.","3.420,00","20.520,00"],
                      ["2","Servomotor SIMOTICS 1FK7",            "6","St.","2.840,00","17.040,00"],
                      ["3","Optionsbaugruppe CBC10 Kommunikation","6","St.",  "385,00", "2.310,00"]],
                     39870, "Bestellung BE-2024-02-0184")
    eingangsrechnung("LF_ER004_Eingangsrechnung_Trumpf_SE_plus_Co._KG","TRUMPF",
                     "TR-2024-04812", "28. Februar 2024",
                     [["1","Faserlaser 8 kW Resonator + Strahlfuehrung","1","St.","245.000,00","245.000,00"],
                      ["2","Laserschneidkopf BC-040",                  "1","St.", "42.000,00", "42.000,00"],
                      ["3","Filterpaket Hochleistung 4-stufig",        "1","St.",  "8.400,00",  "8.400,00"]],
                     295400, "Bestellung BE-2024-02-0212")
    eingangsrechnung("LF_ER005_Eingangsrechnung_Schunk_GmbH_und_Co._","SCHUNK",
                     "RN-2024-0142", "18. Maerz 2024",
                     [["1","Schnellwechselsystem VERO-S NSL 160","4","St.","2.180,00","8.720,00"],
                      ["2","Robotik-Werkzeugadapter RWA 180",    "8","St.",  "920,00","7.360,00"]],
                     16080, "Bestellung BE-2024-03-0241")
    eingangsrechnung("LF_ER006_Eingangsrechnung_Siemens_AG_–_Antri","SIEMENS",
                     "SIE-RG-2024-30821", "12. April 2024",
                     [["1","SINAMICS S210 Servo 5,0 A","4","St.","2.840,00","11.360,00"],
                      ["2","SIMATIC S7-1500 CPU 1517-3 PN/DP", "2","St.","4.620,00", "9.240,00"]],
                     20600, "Bestellung BE-2024-04-0316")
    eingangsrechnung("LF_ER007_Eingangsrechnung_Igus_GmbH","IGUS",
                     "IG-RE-2024-00489", "06. Mai 2024",
                     [["1","Energiekette 20er, Innenbreite 60 mm, 2000 mm","8","St.","312,00","2.496,00"],
                      ["2","Servoleitung CF11.UL.D",                       "320","m","24,80","7.936,00"]],
                     10432, "Bestellung BE-2024-04-0408")
    eingangsrechnung("LF_ER008_Eingangsrechnung_Trumpf_SE_plus_Co._KG","TRUMPF",
                     "TR-2024-05821", "14. Mai 2024",
                     [["1","Service-Pauschale Inbetriebnahme TruDisk", "1","psch.","18.500,00","18.500,00"],
                      ["2","Verbrauchsmaterial Optikpaket",            "1","Set",  "4.200,00", "4.200,00"]],
                     22700, "Bestellung BE-2024-05-0492")


def gen_lf_audit_schunk():
    sections = [
        ("Audit-Eckdaten",
         tbl(["Merkmal", "Wert"],
             [["Lieferant",       "Schunk GmbH & Co. KG"],
              ["Standort",        "Lauffen am Neckar (Hauptwerk)"],
              ["Audit-Datum",     "12.-13. September 2023"],
              ["Audit-Team",      "Sandra Becker (Lead), Holger Brinkmann (Einkauf), Petra Krueger (Q)"],
              ["Audit-Typ",       "Lieferantenaudit nach VDA 6.3 (Prozessaudit)"],
              ["Audit-Anlass",    "Jaehrliche Routine, A-Lieferant"],
              ["Gesamtergebnis",  "92 % – Status A (Hoechstbewertung)"]])),
        ("Befundzusammenfassung",
         ("list",
          ["Managementsystem: ISO 9001:2015, IATF 16949 vorhanden und gepflegt (Konformitaet 95 %).",
           "Entwicklungsprozess: Stage-Gate-Modell, FMEA und PPAP nachweisbar (90 %).",
           "Lieferantenmanagement Schunks: durchgaengiger Audit-Zyklus belegt (94 %).",
           "Produktionsprozess: hohe Maschinenverfuegbarkeit, Stichproben im Toleranzbereich (93 %).",
           "Kundenbetreuung und Reklamationsmanagement: 8D-Prozesse etabliert (90 %)."])),
        ("Abweichungen und Massnahmen",
         tbl(["Nr.", "Befund", "Klasse", "Massnahme", "Termin"],
             [["1", "Kalibrierscheine fehlten bei 2 Messmitteln (Lager 3.1)", "B",
               "Nachpflege im DMS bis 30.09.2023", "30.09.2023"],
              ["2", "Mitarbeiterschulung Werkstoff-Substitution noch nicht abgeschlossen", "C",
               "Bis Q4/2023 vollstaendig nachholen", "31.12.2023"],
              ["3", "Rueckverfolgbarkeit bei Kleinteilen nicht eindeutig dokumentiert", "C",
               "QM-Prozess erweitern (Chargennummer auf Lieferschein)", "31.03.2024"]])),
        ("Bewertung und Schlussfolgerung",
         "Schunk wird weiterhin als A-Lieferant gefuehrt. Der naechste Audit-Termin ist fuer das 4. Quartal 2024 "
         "vorgesehen. Die Massnahmen 1 und 2 werden im internen Lieferanten-Tracking-System (SAP SRM) "
         "ueberwacht; Massnahme 3 wird im Rahmen eines kurzen Telefon-Re-Audits Q1/2024 verifiziert."),
        ("Freigabe",
         signatures("Sandra Becker", "CFO / Lead Auditor", M["name"],
                    "Stefan Braun", "Einkaufsleiter", M["name"],
                    place="Lauffen am Neckar", date_str_="13. September 2023")),
    ]
    write_doc(f"{BASE}/05_Vertraege_Lieferanten/LF_Lieferantenaudit_Schunk_2023.docx", H,
              "Lieferantenaudit – Schunk GmbH & Co. KG (2023)", sections)


def gen_lf_bewertung():
    sections = [
        ("Zweck und Methodik",
         "Die jaehrliche Lieferantenbewertung 2023 dient der systematischen Beurteilung der A- und B-Lieferanten "
         "der Halbreiter Maschinenbau GmbH gemaess der Verfahrensanweisung VA-EK-005. Die Bewertung erfolgt anhand "
         "von vier Kriterien (Qualitaet 40 %, Liefertreue 30 %, Preis/Konditionen 20 %, Service/Kommunikation 10 %). "
         "Die Erhebung wurde im Dezember 2023 durch die Einkaufsabteilung in Zusammenarbeit mit Qualitaetssicherung "
         "und Wareneingang vorgenommen."),
        ("Bewertungsuebersicht (Top-Lieferanten)",
         tbl(["Lieferant", "Kategorie", "Qual.", "Liefertreue", "Preis", "Service", "Gesamt", "Status"],
             [["Schunk GmbH & Co. KG",    "A", "97 %", "94 %", "85 %", "92 %", "92 %", "A"],
              ["Siemens AG Antriebstechnik","A", "94 %", "91 %", "82 %", "89 %", "90 %", "A"],
              ["Trumpf SE + Co. KG",       "A", "93 %", "88 %", "78 %", "90 %", "88 %", "A"],
              ["Festo SE & Co. KG",        "A", "92 %", "90 %", "84 %", "88 %", "89 %", "A"],
              ["Igus GmbH",                "B", "90 %", "92 %", "88 %", "85 %", "90 %", "A"],
              ["DB Schenker Deutschland",   "B", "86 %", "84 %", "82 %", "86 %", "85 %", "B"],
              ["SAP SE",                   "B", "88 %", "92 %", "70 %", "84 %", "84 %", "B"]])),
        ("Massnahmen",
         ("list",
          ["A-Lieferanten erhalten Status-Bestaetigung und Einladung zum Lieferantentag 2024 (12. April 2024 Koeln).",
           "B-Lieferanten mit Gesamtbewertung < 85 % werden im Q1/2024 zu Quartalsgespraechen eingeladen.",
           "Es wurden keine C-Lieferanten identifiziert, die ein Auslistungsverfahren erforderlich machen.",
           "Die Kategorie Service wird ab 2024 staerker an Reaktionszeit-KPIs (Hotline, Ersatzteilversand) gekoppelt."])),
        ("Freigabe und Verteiler",
         "Freigabe durch Stefan Braun (Einkaufsleiter) und Sandra Becker (CFO) am 22. Januar 2024. "
         "Verteiler: Geschaeftsfuehrung, Bereichsleiter Einkauf, Bereichsleiter Qualitaet, Bereichsleiter Produktion."),
    ]
    write_doc(f"{BASE}/05_Vertraege_Lieferanten/LF_Lieferantenbewertung_2023.docx", H,
              "Lieferantenbewertung 2023", sections)


def gen_lf_rahmenvertrag_einkauf():
    sections = [
        ("Praeambel",
         "Dieser Sammel-Rahmenvertrag bietet einheitliche Geschaeftsbedingungen fuer Nicht-A-Lieferanten der "
         "Halbreiter Maschinenbau GmbH ohne individuellen Rahmenvertrag. Er fasst die Mindeststandards der "
         "Allgemeinen Einkaufsbedingungen (EKBs Stand 1.1.2024) sowie der internen Lieferantenrichtlinie "
         "(VA-EK-001 Rev. 6) zu einem unterschriftsfaehigen Dokument zusammen."),
        ("Eckwerte",
         ("clauses",
          [("§ 1 Vertragsgegenstand",
            ["Gegenstand ist die regelmaessige Belieferung der MMB mit Standardteilen, Verbrauchsmaterialien, "
             "Werkzeugen und Dienstleistungen unterhalb der individuell vertraglich geregelten Schwelle.",
             "Konkrete Liefermengen werden ueber Einzelbestellungen abgerufen."]),
           ("§ 2 Preise und Zahlung",
            ["Es gelten die zwischen den Parteien jaehrlich bestaetigten Preislisten. Preisanpassungen sind nur mit "
             "60 Tagen Vorlaufzeit zulaessig.",
             "Zahlungsziel 30 Tage netto, 2 % Skonto binnen 14 Tagen."]),
           ("§ 3 Lieferung",
            ["Lieferung DAP Werk Koeln (INCOTERMS 2020). Der Lieferant tragt Verpackungs- und Transportkosten, "
             "sofern nicht abweichend in der Bestellung vereinbart.",
             "Ein verlaengerter Eigentumsvorbehalt zugunsten des Lieferanten wird ausdruecklich ausgeschlossen, "
             "soweit gesetzlich zulaessig."]),
           ("§ 4 Qualitaet",
            ["Lieferungen muessen DIN-/ISO-/CE-konform sein. Materialzertifikate (3.1 EN 10204) auf Anforderung. "
             "Erstmuster bei sicherheitsrelevanten Komponenten verpflichtend."]),
           ("§ 5 Gewaehrleistung und Haftung",
            ["Gewaehrleistung 24 Monate ab Lieferung. Bei Mangelhaftigkeit hat MMB das Recht auf Nachlieferung, "
             "Ersatzlieferung oder Minderung; weitergehende Ansprueche bleiben unberuehrt.",
             "Produkthaftpflichtversicherung des Lieferanten mit Mindestdeckung 2 Mio. EUR ist nachzuweisen."]),
           ("§ 6 Compliance",
            ["Anerkennung des MMB-Lieferanten-Verhaltenskodex (Stand 2024) und der LkSG-Sorgfaltspflichten."]),
           ("§ 7 Laufzeit",
            ["Laufzeit ein Jahr, Verlaengerung automatisch um jeweils 12 Monate ohne Kuendigung mit 3 Monaten Frist."])])),
        ("Anlagen", "EKBs Stand 1.1.2024; Code of Conduct fuer Lieferanten (Rev. 3); Preisliste 2024."),
        ("Unterschrift", "Diese Sammelvereinbarung wird mit dem jeweiligen Lieferanten gegengezeichnet. "
                           "Eine zentrale Kopie wird im SAP SRM unter der Vertragsnummer 2024-EK-SAMMEL hinterlegt."),
    ]
    write_doc(f"{BASE}/05_Vertraege_Lieferanten/LF_Rahmenvertrag_Einkauf_Allgemein_2023.docx", H,
              "Allgemeiner Einkaufsrahmenvertrag 2023 – Sammelvereinbarung Nicht-A-Lieferanten", sections)


def gen_lf_leasing_trumpf():
    sections = [
        ("Parteien",
         f"{M['name']} ('Leasingnehmer') und Trumpf Financial Services GmbH, Johann-Maus-Strasse 2, "
         "71254 Ditzingen ('Leasinggeber')."),
        ("Vertragsgegenstand",
         ("clauses",
          [("§ 1 Leasingobjekt",
            ["Faserlaser TruDisk 8001 (Seriennummer 2023-FL-887) inkl. Steuerung, Optikpaket und Filteranlage.",
             "Anschaffungswert: 312.000 EUR netto."]),
           ("§ 2 Leasingrate und Laufzeit",
            ["Monatliche Leasingrate: 6.420 EUR netto, zahlbar zum Monatsanfang.",
             "Laufzeit 60 Monate ab 1. April 2023, unkuendbar.",
             "Restwert am Laufzeitende: 31.200 EUR (10 % des AW); Option zur Verlaengerung oder Andienung."]),
           ("§ 3 Wartung und Instandhaltung",
            ["Wartung gemaess Wartungsplan Trumpf (2 Termine/Jahr) durch Trumpf Service GmbH (separater Vertrag).",
             "Reparaturen ausserhalb Wartung gehen zu Lasten des Leasingnehmers; Versicherungspflicht (Allgefahren)."]),
           ("§ 4 Versicherung",
            ["MMB schliesst eine Maschinenversicherung mit Mindestdeckung in Hoehe des Restwertes ab. "
             "Versicherer: Allianz Versicherungs-AG; Police-Nr. MV-2023-77812."]),
           ("§ 5 Eigentum und Nutzung",
            ["Das Leasingobjekt verbleibt im Eigentum des Leasinggebers. Eine Untervermietung oder "
             "Sicherungsuebereignung an Dritte ist ohne schriftliche Zustimmung untersagt."]),
           ("§ 6 Beendigung",
            ["Bei vorzeitiger Kuendigung durch den Leasingnehmer wird eine Vorfaelligkeitsentschaedigung in Hoehe "
             "der diskontierten Restleasingraten faellig (Diskontsatz 5 % p.a.)."])])),
        ("Unterschrift",
         signatures(M["cfo"], "CFO", M["name"],
                    "Klaus Heberlein", "Geschaeftsfuehrer", "Trumpf Financial Services GmbH",
                    place="Koeln/Ditzingen", date_str_="28. Maerz 2023")),
    ]
    write_doc(f"{BASE}/05_Vertraege_Lieferanten/LF_Rahmenvertrag_Leasing_Trumpf.docx", H,
              "Rahmenvereinbarung Maschinen-Leasing – Trumpf Financial Services GmbH (2023)",
              sections, confidential=True)


def gen_lf_logistik_dbsch():
    sections = [
        ("Parteien",
         f"{M['name']} ('Auftraggeber') und DB Schenker Deutschland AG, Edmund-Rumpler-Strasse 3, "
         "60549 Frankfurt am Main ('Spediteur') schliessen den nachfolgenden Rahmenvertrag ueber Speditions- und "
         "Logistikleistungen ab. Vertragslaufzeit 1.1.2023 - 31.12.2026."),
        ("Leistungsumfang",
         ("list",
          ["Strassentransporte FTL/LTL inkl. EU-weiter Sammelverkehre.",
           "Luft- und Seefracht (Export Asien, USA) inkl. Zollabwicklung als indirekter Vertreter (AEO-F).",
           "Verpackung und Containerstauung auf Anforderung; Schwergutverladungen ueber Partnerunternehmen.",
           "Bereitstellung Sendungsverfolgung (Track & Trace) ueber Connect 4 Land/Sea/Air."])),
        ("Preise und Konditionen",
         tbl(["Leistung", "Preisbasis", "Zahlungsziel", "Indexierung"],
             [["Strassentransport DE/EU",   "Preisliste Anlage 1",       "30 Tage netto", "DIESELfloater monatlich"],
              ["Luftfracht",                 "Preisliste Anlage 2",       "30 Tage netto", "FSC/SSC IATA-Standards"],
              ["Seefracht",                  "Preisliste Anlage 3",       "30 Tage netto", "BAF / CAF quartalsweise"],
              ["Lagerung Aussenlager",      "Pauschal je Palettenmonat", "30 Tage netto", "Jahresanpassung VPI"]])),
        ("Haftung und Versicherung",
         "Es gelten die ADSp 2017 in der jeweils gueltigen Fassung sowie subsidiaer die §§ 425 ff. HGB. "
         "Spediteurhaftung beschraenkt auf 8,33 SZR/kg (CMR). Eine Transportversicherung kann individuell "
         "beauftragt werden (FOR-Bedingungen). Der Spediteur weist eine Verkehrshaftungsversicherung mit "
         "Deckung 5 Mio. EUR je Schadensfall nach."),
        ("KPI",
         tbl(["KPI", "Zielwert"],
             [["Termintreue (OTIF)",            "97 %"],
              ["Reklamationsquote Sendungen", "< 1,5 %"],
              ["Reaktion auf Schaeden",        "< 24 h"],
              ["CO2-Reporting",                "quartalsweise (GLEC-Framework)"]])),
        ("Unterschrift",
         signatures(M["ceo"], "Geschaeftsfuehrer", M["name"],
                    "Dr. Thorsten Meincke", "Mitglied des Vorstands", "DB Schenker Deutschland AG",
                    place="Koeln/Frankfurt", date_str_="14. Dezember 2022")),
    ]
    write_doc(f"{BASE}/05_Vertraege_Lieferanten/LF_Rahmenvertrag_Logistik_DB_Schenker.docx", H,
              "Rahmenvertrag Logistik 2023-2026 – DB Schenker Deutschland AG", sections)


# ════════════════════════════════════════════════════════════════════════════════
# 6. IMMOBILIEN
# ════════════════════════════════════════════════════════════════════════════════

def gen_anlagenakte_fz4891():
    sections = [
        ("Stammdaten der Anlage",
         tbl(["Merkmal", "Wert"],
             [["Anlagennummer (intern)", "FZ-4891"],
              ["Bezeichnung",            "Faserlaser TruDisk 8001"],
              ["Hersteller",             "Trumpf SE + Co. KG, Ditzingen"],
              ["Seriennummer",           "2023-FL-887"],
              ["Baujahr",                "2023"],
              ["Inbetriebnahme",         "15. April 2023"],
              ["Standort",               "Halle B, Achse 4, Industriestrasse 12, 50829 Koeln"],
              ["Strom-Anschluss",        "400 V / 63 A CEE, Sicherung 80 A"],
              ["Anschaffungswert",       "312.000 EUR (netto, Leasingobjekt)"],
              ["Eigentumsverhaeltnis",   "Leasing Trumpf Financial Services GmbH (siehe Ordner 05)"]])),
        ("Technische Spezifikation",
         ("list",
          ["Laserleistung: 8.000 W cw, Wellenlaenge 1.030 nm.",
           "Bearbeitungsbereich: 3.000 x 1.500 mm, Z-Achse 100 mm.",
           "Schneidkopf: BC-040 mit Crash-Schutz und Linsenwechselsystem.",
           "Filtersystem: 4-stufige Absaugung 5.500 m3/h.",
           "Kuehlung: Kompaktkuehler 15 kW, Glykol-Wasser-Mischung."])),
        ("Wartung und Pruefung",
         tbl(["Aufgabe", "Frequenz", "Letzte Pruefung", "Naechste Pruefung", "Verantwortlich"],
             [["Sichtpruefung Strahlfuehrung", "monatlich",   "08.04.2024", "08.05.2024", "Bediener"],
              ["Filterwechsel (HEPA)",         "quartalsweise","04.04.2024", "04.07.2024", "Instandhaltung"],
              ["UVV-Pruefung elektrisch",      "jaehrlich",   "12.03.2024", "12.03.2025", "Externe Fachfirma"],
              ["Trumpf-Service-Wartung",       "halbjaehrlich","20.02.2024","20.08.2024", "Trumpf Service"]])),
        ("Sicherheits- und Schulungsanforderungen",
         "Bediener muessen das Schulungsmodul »Laserklasse 4« (Dauer 8 h) sowie die Einweisung am Geraet (Trumpf-Werk) "
         "absolviert haben. Schulungsnachweise sind in der Personalakte hinterlegt. Schutzkleidung (Laserschutzbrille "
         "OD 7+ bei 1.064 nm) ist bereitzustellen. Notaus, Tuerueberwachung und Strahlungsabschirmung werden monatlich "
         "auf Funktion geprueft. Sicherheitsdatenblatt fuer Schneidgase (Stickstoff, Sauerstoff) liegt im Ordner 09 vor."),
        ("Hinweise", "Bei Veraeusserung oder Verlagerung der Anlage ist die Leasinggesellschaft (Trumpf FS) zu informieren. "
                       "Anlagenakte wird jaehrlich durch Instandhaltung (Markus Junker) gepflegt."),
    ]
    write_doc(f"{BASE}/06_Immobilien/Anlagenakte_Maschine_FZ4891.docx", H,
              "Anlagenakte Maschine FZ-4891 – Faserlaser TruDisk 8001", sections)


def gen_imm_002_aussenlager():
    sections = [
        ("Parteien",
         f"Vermieter: PV Industrieliegenschaften Koeln GmbH, Niehler Strasse 88, 50735 Koeln, vertreten durch GF Herrn Peter Voigt.\n"
         f"Mieter: {M['name']}, {M['addr']}, vertreten durch GF {M['ceo']}."),
        ("Mietobjekt",
         "Industriehalle mit 2.150 m2 Hallenflaeche zzgl. 320 m2 Buero- und Sozialflaechen, Hofflaeche 1.450 m2, "
         "Lkw-Anbindung mit 2 Toren (4,5 x 4,5 m), Stromanschluss 250 A, Sprinkleranlage VdS-CEA 4001. "
         "Lage: Niehler Strasse 88, 50735 Koeln, ca. 4 km Entfernung zum Hauptstandort Industriestrasse 12."),
        ("Vertragsinhalt",
         ("clauses",
          [("§ 1 Mietzweck",
            ["Lagerung von Halbfabrikaten, Verpackungsmaterialien und Versandgut der Halbreiter Maschinenbau GmbH. "
             "Eine produktive Bearbeitung von Werkstuecken ist nicht zulaessig (Baurecht / Genehmigung GE-Industriegebiet)."]),
           ("§ 2 Mietzins",
            ["Grundmiete 7,80 EUR/m2 fuer Halle, 11,20 EUR/m2 fuer Buero, 2,40 EUR/m2 fuer Hofflaeche; gesamt rund "
             "22.460 EUR netto monatlich. Zzgl. Nebenkostenvorauszahlung 3.200 EUR/Monat (Grundsteuer, Versicherung, "
             "Wartung Sprinkler/Lueftung). Indexklausel: Anpassung an VPI ab dem 3. Mietjahr."]),
           ("§ 3 Mietdauer",
            ["Festlaufzeit 5 Jahre, beginnend 01.06.2022, endend 31.05.2027. Verlaengerungsoption fuer 2 x 3 Jahre, "
             "Ausuebung mit 9 Monaten Frist."]),
           ("§ 4 Schoenheitsreparaturen",
            ["Vermieter traegt Dach, Fach und Fassade; Mieter traegt Schoenheitsreparaturen Innenraeume."]),
           ("§ 5 Untervermietung",
            ["Eine Untervermietung an konzernfremde Dritte bedarf der schriftlichen Zustimmung des Vermieters."]),
           ("§ 6 Versicherung und Haftung",
            ["Mieter haelt eine Betriebshaftpflicht mit 5 Mio. EUR Deckung; Vermieter haelt Gebaeudeversicherung."])])),
        ("Unterschriften",
         signatures(M["ceo"], "Geschaeftsfuehrer", M["name"],
                    "Peter Voigt", "Geschaeftsfuehrer", "PV Industrieliegenschaften Koeln GmbH",
                    place="Koeln", date_str_="18. Mai 2022")),
    ]
    write_doc(f"{BASE}/06_Immobilien/IMM_002_Mietvertrag_Außenlager_Niehler_.docx", H,
              "Mietvertrag Aussenlager Niehler Strasse 88", sections, confidential=True)


def gen_imm_bauantrag():
    sections = [
        ("Antragstellerin und Vorhaben",
         f"Antragstellerin: {M['name']}, {M['addr']}; vertreten durch GF {M['ceo']}. "
         "Vorhaben: Erweiterung der Produktionshalle B um 1.280 m2 Nutzflaeche (Hallenanbau Sued) zur Aufnahme "
         "der neuen Laserschneidanlage LS-800 sowie der zugehoerigen Vor- und Nachbearbeitungsfertigung."),
        ("Eckdaten zum Bauvorhaben",
         tbl(["Merkmal", "Wert"],
             [["Adresse",                     "Industriestrasse 12, 50829 Koeln (Gemarkung Ossendorf, Flur 8, Flurst. 1294/3)"],
              ["Art des Vorhabens",          "Anbau Halle B Sued (Neubau, ein Vollgeschoss)"],
              ["Bruttogrundflaeche",         "1.420 m2"],
              ["Nutzflaeche",                "1.280 m2"],
              ["Firsthoehe",                 "10,80 m (Maximalhoehe 12,00 m gemaess B-Plan)"],
              ["Bauklasse / Brandschutz",    "Gebaeudeklasse 3, Industriebau-Richtlinie M-IndBauRL 2014"],
              ["Tragwerk",                    "Stahlbau, Sandwich-Fassade (PUR-Kern)"],
              ["Dach",                        "Stahl-Trapez mit Solar-Vorruestung 350 kWp"],
              ["Geplante Bauzeit",           "08/2024 - 05/2025"],
              ["Baukosten (KG 300+400 DIN 276)","ca. 4,2 Mio. EUR netto"]])),
        ("Planungsbeteiligte und Genehmigungen",
         "Architekt: Schmidt Architekten BDA, Koeln (Bauleitung). Tragwerksplaner: IB Hartmann, Aachen. "
         "Brandschutzgutachter: Halfkann + Kirchner, Erkelenz. Bodengutachten: Geo-Consult Rheinland (Vorbericht 12.2023). "
         "Stellplatznachweis: 18 zusaetzliche Pkw-Stellplaetze auf Flurstueck 1294/4 (eigene Liegenschaft). "
         "Versickerung Niederschlagswasser ueber neue Mulden-Rigolen-Anlage gemaess DWA-A 138."),
        ("Eingereichte Unterlagen",
         ("list",
          ["Bauantragsformular (Stadt Koeln, Bauaufsicht)",
           "Lageplan M 1:500, Grundrisse und Schnitte M 1:100",
           "Baubeschreibung gemaess § 70 BauO NRW",
           "Brandschutzkonzept (gutachterliche Stellungnahme)",
           "Statische Berechnung (vorab) und Bewehrungsplaene",
           "Standsicherheitsnachweis Sandwichfassade",
           "Energieausweis Vorabbewertung (KfW-55-Standard angestrebt)"])),
        ("Bearbeitungsstand",
         "Antrag eingereicht bei der Stadt Koeln, Bauaufsichtsamt, am 26. Februar 2024. Aktenzeichen 63.31-2024-184. "
         "Vorpruefung positiv, Eingangsbestaetigung 1. Maerz 2024. Mit der Erteilung der Baugenehmigung wird im "
         "Mai/Juni 2024 gerechnet."),
    ]
    write_doc(f"{BASE}/06_Immobilien/IMM_Bauantrag_Hallenanbau_2024.docx", H,
              "Bauantrag Hallenanbau 2024 – Erweiterung Halle B um 1.280 m²", sections)


def gen_imm_grundriss_prod_a():
    sections = [
        ("Beschreibung",
         "Diese Plandokumentation enthaelt den schematischen Grundriss der Produktionshalle A am Hauptstandort "
         "Industriestrasse 12, 50829 Koeln. Halle A ist die aelteste Halle des Werks (Erstellt 1978, "
         "Generalsanierung 2015-2016) und beherbergt im Wesentlichen die mechanische Bearbeitung "
         "(Fraesen, Drehen) sowie die Vormontage der Pressenlinien PL-500."),
        ("Eckdaten",
         tbl(["Merkmal", "Wert"],
             [["Hallenflaeche brutto",        "3.840 m2"],
              ["Hallenhoehe nutzbar",         "9,20 m bis Kranbahn"],
              ["Krananlagen",                 "2 Brueckenkrane 16 t, 1 Halbportalkran 5 t"],
              ["Tore",                        "3 Sektionaltore (4,5 x 4,5 m), 1 Schiebetor 6,0 x 4,5 m"],
              ["Stromanschluss",              "630 A, redundante Trafostation Sued"],
              ["Druckluft",                   "Ringleitung 8 bar, Kompressorraum Halle C"],
              ["Brandschutz",                 "Sprinkleranlage VdS-CEA, Brandabschnitte BA-A1 bis BA-A4"],
              ["Belegungsflaeche Maschinen", "ca. 65 % (CNC-Fraesen, Drehen, Bohrwerke)"]])),
        ("Bereiche",
         ("list",
          ["Bereich A1 (Nord): Wareneingang Halbzeuge, Materiallager Rohstahl.",
           "Bereich A2 (Ost): Zerspanung CNC (Fraesen DMG Mori, Drehen Mazak).",
           "Bereich A3 (Sued): Vormontage PL-500-Modulgruppen.",
           "Bereich A4 (West): Werkstoffpruefung, Messraum (Zeiss-Koordinatenmessmaschine).",
           "Bereich A5 (Mitte): Logistik, Lkw-Verkehr, Stellplaetze Stapler."])),
        ("Notwendige Auflagen",
         "Die Halle unterliegt dem Bauschein 1978/0421 (Stadt Koeln) sowie den Auflagen der Industriebau-Richtlinie. "
         "Letzte Brandschutzbegehung 14.11.2023, naechste 11/2024. Pruefung Krananlagen jaehrlich durch TUEV Rheinland."),
        ("Hinweise zur Plandarstellung",
         "Der vollstaendige CAD-Plan (AutoCAD .dwg und PDF, M 1:200) liegt in der CAD-Ablage CAD/Werk/Halle_A/2024/. "
         "Verantwortlich fuer die Pflege: Markus Junker (Instandhaltung) in Abstimmung mit dem Architekturbuero "
         "Schmidt Architekten BDA."),
    ]
    write_doc(f"{BASE}/06_Immobilien/IMM_Grundriss_Produktionshalle_A.docx", H,
              "Grundriss Produktionshalle A – Industriestrasse 12, 50829 Koeln", sections)


def gen_imm_grundriss_verwaltung():
    sections = [
        ("Beschreibung",
         "Das Verwaltungsgebaeude beherbergt die kaufmaennischen Funktionen der Halbreiter Maschinenbau GmbH "
         "einschliesslich Geschaeftsfuehrung, Personal, Buchhaltung, Vertrieb, Einkauf, Konstruktion und IT. "
         "Es wurde 2008 errichtet und 2019 energetisch saniert (KfW-Effizienzhaus 70)."),
        ("Eckdaten",
         tbl(["Merkmal", "Wert"],
             [["Geschosse",                "4 Vollgeschosse + UG (Archiv, Technik)"],
              ["Bruttogeschossflaeche",    "3.120 m2"],
              ["Nutzflaeche",              "2.640 m2"],
              ["Stellplaetze",              "84 Stellplaetze (12 mit Ladesaeule)"],
              ["Heizung / Kuehlung",        "Waermepumpe + GLT, Spitzenlast Gas-Brennwert"],
              ["Glasfaser-Anschluss",       "2 x 1 Gbit/s (NetCologne / Telekom redundant)"],
              ["Brandmeldeanlage",          "VdS Klasse C, aufgeschaltet auf Feuerwehr Koeln-Ossendorf"]])),
        ("Raumaufteilung",
         tbl(["Geschoss", "Funktion", "Personen"],
             [["UG",   "Archiv, IT-Serverraum, Technikraeume", "0 (unbemannt)"],
              ["EG",   "Empfang, Besprechung 1-3, Showroom",   "—"],
              ["1.OG", "Vertrieb (32), Einkauf (12), Marketing (4)", "48"],
              ["2.OG", "Buchhaltung (14), Controlling (5), HR (8), Compliance (3)", "30"],
              ["3.OG", "Geschaeftsfuehrung, Konstruktion, IT", "42"]])),
        ("Sicherheits- und Zutrittsregelungen",
         "Zutrittskontrolle ueber Salto-/Bosch-System mit personalisierten Karten; Besucher erhalten "
         "tagesgueltige Karten am Empfang. Videoueberwachung in oeffentlichen Bereichen gemaess DSGVO. "
         "Hausmeisterdienst durch die Firma Gegenbauer Services GmbH (Vertrag siehe Ordner 06)."),
        ("Plandokumente und CAD-Ablage",
         "Die vollstaendigen CAD-Plaene (AutoCAD .dwg, M 1:100 je Geschoss) liegen unter "
         "CAD/Werk/Verwaltung/2024/. Verantwortlich fuer die Pflege: Holger Brinkmann (Bauwesen / Facility). "
         "Eine Synchronisation mit dem CAFM-System (PIT-FM 7) erfolgt automatisch ueber den naechtlichen Import-Job."),
        ("Energetik und Nachhaltigkeit",
         "Energiestandard nach KfW-Effizienzhaus 70 (Sanierung 2019). Heizung ueber Sole-Wasser-Waermepumpe "
         "(Vaillant geoTHERM, 28 kW) plus Spitzenlast-Gasbrennwertkessel. Kuehlung im Bereich Serverraum redundant "
         "(2x 18 kW Splitanlage). Photovoltaik auf Flachdach (44 kWp, Einspeisung) seit 09/2020. "
         "Endenergiebedarf (Energieausweis 2023): 78 kWh/m²a (Strom + Waerme). "
         "Eine Pruefung auf weitere Daemmungsmassnahmen ist fuer Q4/2024 vorgesehen."),
        ("Wartung und Pruefintervalle",
         tbl(["Anlage", "Pruefintervall", "Verantwortlich"],
             [["Brandmeldeanlage (VdS C)", "vierteljaehrlich", "Bosch Sicherheitssysteme"],
              ["Aufzugsanlage (1 Aufzug)",  "monatlich",         "Schindler Deutschland AG"],
              ["Klima-/Lueftungstechnik",   "halbjaehrlich",     "Carrier Klimatechnik"],
              ["Waermepumpe / GLT",         "jaehrlich",          "Vaillant Service"],
              ["Brandschutztueren / RWA",   "jaehrlich",          "Hoermann Service GmbH"]])),
    ]
    write_doc(f"{BASE}/06_Immobilien/IMM_Grundriss_Verwaltungsgebäude.docx", H,
              "Grundriss Verwaltungsgebaeude – Industriestrasse 12, 50829 Koeln", sections)


def gen_imm_kundenparkplatz():
    sections = [
        ("Parteien",
         f"Vermieterin: Stadt Koeln, Liegenschaftsamt, vertreten durch das Amt fuer Liegenschaften und "
         "Wirtschaftsfoerderung, Willy-Brandt-Platz 2, 50679 Koeln.\n"
         f"Mieterin: {M['name']}, {M['addr']}."),
        ("Mietobjekt",
         "Pkw-Stellplaetze auf staedtischem Grund, Flurstueck 1297/5 Gemarkung Ossendorf, ca. 35 m "
         "noerdlich des Hauptzufahrtstores der Mieterin. Insgesamt 24 markierte Stellplaetze (3 davon barrierefrei), "
         "asphaltierte Befestigung, Beleuchtung 4 LED-Mastleuchten. Die Stellplaetze werden den Besuchern, "
         "Lieferanten und Kunden der Mieterin zugaenglich gemacht."),
        ("Vertragsinhalt",
         ("clauses",
          [("§ 1 Mietzins",
            ["Monatlicher Mietzins 1.080 EUR netto (24 x 45 EUR), zahlbar bis zum 3. Werktag des Monats. "
             "Indexklausel: Anpassung an VPI alle 24 Monate."]),
           ("§ 2 Mietdauer",
            ["Festlaufzeit 36 Monate, beginnend 01.07.2022, endend 30.06.2025. Stillschweigende Verlaengerung um "
             "jeweils 12 Monate, sofern nicht 6 Monate vor Ablauf gekuendigt wird."]),
           ("§ 3 Verkehrssicherungspflicht",
            ["Winterdienst, Beleuchtung und Markierung werden durch den Vermieter erbracht. "
             "Beschaedigungen an Bordsteinen oder Fahrbahnbelag sind unverzueglich anzuzeigen."]),
           ("§ 4 Nutzungsumfang",
            ["Nutzung ausschliesslich fuer Besucher und Kunden der Mieterin. Lagerung, Aufstellen von "
             "Containern oder Werbeflaechen ist unzulaessig."]),
           ("§ 5 Versicherung",
            ["Schaeden an den Fahrzeugen Dritter werden durch Mieter oder Eigentuemer reguliert. "
             "Mieter unterhaelt eine Betriebshaftpflicht mit 5 Mio. EUR Deckung."])])),
        ("Sonderregelungen",
         "Die Stadt Koeln behaelt sich vor, im Falle staedtebaulicher Massnahmen das Mietverhaeltnis mit einer Frist "
         "von 12 Monaten zum Ablauf eines Mietjahres zu kuendigen; in diesem Fall wird die Stadt sich bemuehen, "
         "alternative Stellplaetze im Umkreis von 500 m anzubieten."),
        ("Unterschriften",
         signatures(M["ceo"], "Geschaeftsfuehrer", M["name"],
                    "Manfred Krause", "Liegenschaftsamt, Sachgebietsleiter", "Stadt Koeln",
                    place="Koeln", date_str_="22. Juni 2022")),
    ]
    write_doc(f"{BASE}/06_Immobilien/IMM_Mietvertrag_Kundenparkplatz_2022.docx", H,
              "Mietvertrag Kundenparkplatz 2022 – Vermieter Stadt Koeln (Liegenschaftsamt)", sections)


def gen_imm_versicherungskataster():
    sections = [
        ("Zweck",
         "Dieses Versicherungskataster dokumentiert die Versicherungssituation aller wesentlichen Immobilien "
         "und Liegenschaften der Halbreiter Maschinenbau GmbH (eigene und gemietete Objekte). Es wird jaehrlich "
         "von Sandra Becker (CFO) in Abstimmung mit dem Versicherungsmakler Funk Gruppe GmbH (Hamburg) gepflegt."),
        ("Uebersicht der versicherten Objekte",
         tbl(["Objekt", "Eigentum/Miete", "Versicherer", "Police-Nr.", "Deckungssumme", "Stand"],
             [["Hauptwerk Industriestrasse 12, Koeln",  "Eigentum", "Allianz Versicherungs-AG",     "GB-2023-22431", "32,5 Mio. EUR (NW)", "01.01.2024"],
              ["Aussenlager Niehler Strasse 88, Koeln", "Miete",    "Vermieter (PV Industrieliegen)","-",            "Gebaeude vermieter; Inhalt MMB 2,8 Mio. EUR", "01.01.2024"],
              ["Verwaltungsgebaeude (gleiche Adresse)",  "Eigentum", "Allianz Versicherungs-AG",     "GB-2023-22431", "Anteil 6,2 Mio. EUR (NW)", "01.01.2024"],
              ["Kundenparkplatz Stadt Koeln",            "Miete",    "—",                            "—",            "Stadt Koeln traegt",  "01.01.2024"]])),
        ("Deckungsbausteine",
         ("list",
          ["Gebaeudeversicherung: Feuer, Leitungswasser, Sturm/Hagel (gleitender Neuwert).",
           "Inhaltsversicherung: Maschinen, Vorraete, Bueroausstattung (Allgefahrendeckung).",
           "Betriebsunterbrechung (BU): Haftzeit 24 Monate, Selbstbehalt 50 TEUR/Schadenereignis.",
           "Elementardeckung: Hochwasser, Erdbeben, Rueckstau (begrenzt 5 Mio. EUR).",
           "Maschinenversicherung: ausgewaehlte Anlagen (Pressen, Laser), Listung in Anlage 2."])),
        ("Maklerbetreuung und Schadensbearbeitung",
         "Versicherungsmakler: Funk Gruppe GmbH, Niederlassung Koeln (Ansprechpartner Frau Annette Witt). "
         "Schadensmeldungen erfolgen ueber das Maklerportal innerhalb von 48 Stunden nach Schadensereignis. "
         "Im Berichtsjahr 2023 wurde ein Wasserschaden (Verwaltungsgebaeude) gemeldet; Regulierung Q4/2023, "
         "Schadenshoehe 18.420 EUR netto (siehe Ordner 08)."),
        ("Hinweise",
         "Police-Spiegel als Anlage 1 (Excel). Naechste Pruefung der Deckungswerte und Selbstbehalte: Q4/2024."),
    ]
    write_doc(f"{BASE}/06_Immobilien/IMM_Versicherungskataster_Immobilien_2024.docx", H,
              "Versicherungskataster Immobilien 2024", sections)


# ════════════════════════════════════════════════════════════════════════════════
# 7. IP / Lizenzen
# ════════════════════════════════════════════════════════════════════════════════

def lizenz(fname, title, lizenzgeber, lizenzgeber_addr, produkt, lizenztyp, anzahl,
           preis_jaehrlich, laufzeit, anwender_kreis, support):
    sections = [
        ("Lizenznehmer",
         f"{M['name']}, {M['addr']}, vertreten durch {M['ceo']}. "
         f"USt-IdNr.: {M['ust']}. Hausbank: {M['bank']}."),
        ("Lizenzgeber", f"{lizenzgeber}, {lizenzgeber_addr}."),
        ("Lizenzgegenstand und Umfang",
         tbl(["Merkmal", "Wert"],
             [["Produkt",                produkt],
              ["Lizenztyp",              lizenztyp],
              ["Anzahl Lizenzen / User", anzahl],
              ["Anwenderkreis",           anwender_kreis],
              ["Stand der Lizenzdaten",  "31.12.2023"]])),
        ("Konditionen",
         f"Jaehrliche Lizenz-/Subskriptionsgebuehr: {preis_jaehrlich}. Zahlung jaehrlich im Voraus, "
         "Rechnungsstellung zum 1. Januar. Preisanpassung gemaess Vertrag max. einmal jaehrlich, "
         "Vorlauffrist 90 Tage."),
        ("Laufzeit und Kuendigung",
         f"Laufzeit: {laufzeit}. Ordentliche Kuendigung mit 3 Monaten Frist zum Vertragsende. "
         "Ausserordentliche Kuendigung bleibt unberuehrt."),
        ("Support und Wartung",
         support + "\n\nSLA-Reaktionszeiten: kritisch < 4 h, hoch < 8 h, normal < 24 h. "
         "Software-Updates und Security-Patches sind im Vertragspreis enthalten."),
        ("Nutzungsbeschraenkungen",
         "Die Lizenz ist auf Konzernunternehmen der Halbreiter Maschinenbau GmbH beschraenkt. Eine Weitergabe oder "
         "Unterlizensierung an konzernfremde Dritte ist ausgeschlossen. Auditrecht des Lizenzgebers mit "
         "Vorankuendigung 30 Tage, max. einmal pro Vertragsjahr."),
        ("Datenschutz und Compliance",
         "Soweit personenbezogene Daten verarbeitet werden, gilt der DSGVO-Auftragsverarbeitungsvertrag (AVV) "
         "in der jeweils gueltigen Fassung; technisch-organisatorische Massnahmen siehe Anlage TOM. "
         "Der Lizenzgeber verfuegt ueber ISO/IEC 27001-Zertifizierung."),
        ("Interner Verantwortlicher", "IT-Leitung: Holger Brinkmann; Lizenzmanagement: Anja Lenz (Compliance)."),
    ]
    write_doc(f"{BASE}/07_IP_Lizenzen/{fname}.docx", H, title, sections)


def gen_lizenzen():
    lizenz("IP_004_Lizenz_SAP_S-4HANA_On-Prem",
           "Lizenz SAP S/4HANA On-Premise (Standard Maintenance Subscription)",
           "SAP SE", "Dietmar-Hopp-Allee 16, 69190 Walldorf",
           "SAP S/4HANA Enterprise Edition, On-Premise (Module FI, CO, MM, SD, PP, QM)",
           "Named-User-Lizenz + Engine-Lizenzen (HANA Runtime)",
           "118 Professional User, 64 Functional User, 14 Productivity User",
           "284.000 EUR p.a. Wartung (Enterprise Support, 22 % der Lizenz)",
           "unbefristete Lizenz, Wartung jaehrlich verlaengernd",
           "Verwaltung, Buchhaltung, Einkauf, Vertrieb, Produktion",
           "Enterprise Support (24/7) mit Reaktionszeiten gemaess SAP-SLA.")
    lizenz("IP_005_Lizenz_Salesforce_Sales_Clo",
           "Lizenz Salesforce Sales Cloud Enterprise (Lizenzvertrag SF-MMB-2023)",
           "salesforce.com Germany GmbH", "Erika-Mann-Strasse 31, 80636 Muenchen",
           "Salesforce Sales Cloud Enterprise Edition + Service Cloud Enterprise",
           "Cloud-Subscription (Named-User)",
           "32 Sales User + 18 Service User",
           "84.600 EUR p.a. (3-Jahres-Vertrag, Volumenrabatt 12 %)",
           "01.04.2023 - 31.03.2026 (3 Jahre)",
           "Vertrieb (DACH + International), After-Sales-Service",
           "Premier Success Plan (Reaktionszeit 1 h fuer Sev1).")
    lizenz("IP_006_Lizenz_SINUMERIK_ONE_CNC-So",
           "Lizenz SINUMERIK ONE CNC-Steuerung (Siemens)",
           "Siemens AG, Digital Industries", "Werner-von-Siemens-Strasse 50, 91052 Erlangen",
           "SINUMERIK ONE CNC-Steuerung inkl. SINUMERIK Edge und MindSphere-Konnektor",
           "Maschinenbezogene Runtime-Lizenz + Optionspaket Advanced Surface",
           "12 Maschinen-Runtime-Lizenzen (CNC PL-500 und LS-800)",
           "62.400 EUR p.a. Wartung",
           "unbefristet (Runtime), Wartung verlaengernd jeweils 12 Monate",
           "Produktion, CNC-Fertigung",
           "Siemens Industry Online Support, Hotline 24/7.")
    lizenz("IP_007_Lizenz_AutoCAD_Mechanical_2",
           "Lizenz AutoCAD Mechanical 2024 (Autodesk Subscription)",
           "Autodesk GmbH", "Neumarkter Strasse 46, 81673 Muenchen",
           "AutoCAD Mechanical 2024 inkl. Toolset, Inventor LT (Mechanical Cloud Service)",
           "Cloud-Subscription, Named-User-Single-Use",
           "28 Lizenzen (Konstruktion, Engineering, Service)",
           "38.640 EUR p.a. (1.380 EUR pro User/Jahr)",
           "01.05.2023 - 30.04.2026 (3 Jahre)",
           "Konstruktion, Engineering Special Machines, Service",
           "Standard Support (Mo-Fr 09:00-17:00 Uhr) und Online-Wissensdatenbank.")
    lizenz("IP_008_Lizenz_SOLIDWORKS_Premium_",
           "Lizenz SOLIDWORKS Premium / Halbreiter Maschinenbau GmbH",
           "Dassault Systèmes Deutschland GmbH", "Meitnerstrasse 8, 70563 Stuttgart",
           "SOLIDWORKS Premium 2024 + Simulation Professional + PDM Standard",
           "Stand-alone-Lizenz (Network/Floating-Lizenz)",
           "18 Floating-Lizenzen + 4 Simulation + PDM 18-User",
           "62.800 EUR p.a. Wartung (Subscription Service)",
           "unbefristet (Stand-alone), Subscription jaehrlich",
           "Konstruktion (Sondermaschinen, FEM-Simulation)",
           "Dassault Customer Portal, Reaktionszeit gemaess Support Level 2.")


def gen_ip_gebrauchsmuster():
    sections = [
        ("Stammdaten",
         tbl(["Merkmal", "Wert"],
             [["Schutzrecht",            "Gebrauchsmuster"],
              ["Aktenzeichen",           "DE 20 2021 105 482.4"],
              ["Anmelder/Inhaber",       M["name"]],
              ["Erfinder",                "Dipl.-Ing. Hartmut Lauer; Dr.-Ing. Sabine Hoff"],
              ["Anmeldetag",              "08.10.2021"],
              ["Eintragungstag",          "14.01.2022 (DPMA)"],
              ["Schutzdauer",             "max. 10 Jahre, jaehrliche Aufrechterhaltungsgebuehr"],
              ["Patentanwalt",            "Boehmert & Boehmert PartG mbB, Berlin"]])),
        ("Bezeichnung",
         "Hydraulisches Schnellwechselsystem fuer Pressenwerkzeuge mit selbstzentrierender Klemmgeometrie zur "
         "Reduktion der Ruestzeit von Stanzpressen der Baureihe PL-500."),
        ("Schutzanspruch (Kurzdarstellung)",
         "Anspruch 1: Schnellwechselsystem mit hydraulischer Klemmvorrichtung zur Aufnahme von Pressenwerkzeugen, "
         "dadurch gekennzeichnet, dass die Klemmkraefte ueber selbstzentrierende konische Aufnahmeflaechen geleitet "
         "und ueber eine integrierte Druck-Sensorik im Bereich von 220 bis 280 bar geregelt werden, sodass eine "
         "Werkzeugfixierung in unter 90 Sekunden erreichbar ist.\n\n"
         "Ansprueche 2 - 8 betreffen vorteilhafte Ausgestaltungen (Sensorik, Hydraulikkreislauf, modulare Bauweise)."),
        ("Wirtschaftliche Bedeutung",
         "Die Erfindung reduziert Werkzeugwechselzeiten an Pressenlinien der Halbreiter Maschinenbau GmbH von "
         "durchschnittlich 12 Minuten auf unter 2 Minuten. Sie wird seit 2022 in der PL-500-Serie eingesetzt und "
         "ist ein wesentliches Differenzierungsmerkmal gegenueber Mitbewerbern wie Schuler oder Fagor."),
        ("Status und Gebuehren",
         tbl(["Jahr", "Aufrechterhaltungsgebuehr DPMA", "Zahlung", "Status"],
             [["3. Jahr (2024)", "260 EUR", "geleistet 12.01.2024", "aufrechterhalten"],
              ["4. Jahr (2025)", "260 EUR", "geplant 01/2025",      "vorgesehen"]])),
        ("Empfehlung",
         "Der Patentanwalt empfiehlt eine Pruefung der Erweiterung in Europa (EP) sowie ggf. USA/China zur Q3/2024. "
         "Geschaeftsfuehrung wird sich mit der Empfehlung im Rahmen der naechsten IP-Strategieklausur befassen."),
    ]
    write_doc(f"{BASE}/07_IP_Lizenzen/IP_Gebrauchsmuster_DE202021.docx", H,
              "Gebrauchsmuster DE 20 2021 105 482.4 – Hydraulisches Schnellwechselsystem", sections)


def gen_ip_marke():
    sections = [
        ("Markenuebersicht",
         tbl(["Merkmal", "Wert"],
             [["Markeninhaber",         M["name"]],
              ["Markenform",            "Wort-/Bildmarke (MMB-Logo)"],
              ["Register-Nr. DPMA",     "30 2017 209 187"],
              ["Eintragungstag",        "22.05.2017"],
              ["Letzte Verlaengerung",  "22.05.2027 (10 Jahre)"],
              ["Anwalt",                 "Boehmert & Boehmert PartG mbB, Berlin"]])),
        ("Geschuetzte Nizza-Klassen",
         tbl(["Klasse", "Beschreibung (Auszug)"],
             [["7",  "Maschinen, Maschinenwerkzeuge, motorische Geraete (Pressen, Foerderbaender, Laser)"],
              ["9",  "Mess-, Kontroll- und Lehrgeraete; Software fuer Maschinensteuerung"],
              ["37", "Installation, Wartung und Reparatur von Maschinen"],
              ["42", "Wissenschaftliche und technologische Dienstleistungen; Engineering"]])),
        ("Internationale Ausdehnungen",
         ("list",
          ["IR-Marke (Madrid Protocol): Anmeldung 14.06.2018, geschuetzt in EUIPO, CH, TR, US, CN.",
           "EU-Marke (EUIPO): 017 821 432, eingetragen 03.10.2018.",
           "US-Marke (USPTO): 5 901 234, eingetragen 06.05.2019."])),
        ("Kosten und Verwaltung",
         "Jaehrliche Verwaltungskosten der Markenfamilie: rund 6.800 EUR (Anwaltsgebuehren + Renewal-Gebuehren). "
         "Naechste Verlaengerung in groesserem Umfang: 2027 (DPMA), 2028 (EUIPO/IR). "
         "Markenueberwachung erfolgt durch Compagnia Markenschutz GmbH (Quartalsberichte zu Kollisionen)."),
        ("Lizenzierung",
         "Die Marke wird konzernintern verwendet. Externe Lizenzen werden derzeit nicht vergeben. Eine eventuelle "
         "Lizenzierung an Joint-Venture-Partner waere durch die Geschaeftsfuehrung gesondert zu genehmigen."),
        ("Streitigkeiten",
         "Es bestehen keine offenen Loeschungs- oder Widerspruchsverfahren. Im Jahr 2023 wurden zwei Kollisionen "
         "(EUIPO) gemeldet und einvernehmlich beigelegt (Koexistenzvereinbarungen). Eine bilaterale "
         "Koexistenzvereinbarung wurde mit einem belgischen Maschinenbauer (»Muller Industries SA«) "
         "abgeschlossen; der Geltungsbereich der jeweils geschuetzten Marken wurde nach Branchen und Regionen "
         "klar abgegrenzt."),
        ("Strategie und Roadmap",
         "Die Markenstrategie der Halbreiter Maschinenbau GmbH zielt auf eine konsequente Premium-Positionierung der "
         "Marke »MMB« im Bereich Sondermaschinenbau. Geplante Schritte 2024/2025: Anmeldung der Marke in Brasilien "
         "(INPI) und Indien (Trade Marks Registry) im Zuge der Internationalisierungs-Roadmap (siehe Ordner 11). "
         "Pruefung einer Submarken-Strategie fuer die Produktlinien PL/FB/LS/MR. Eine Markenwertbewertung gemaess "
         "ISO 10668 wurde durch Brand Finance Deutschland zum Bewertungsstichtag 31.12.2023 mit 4,8 Mio. EUR "
         "(Markenwert) durchgefuehrt; der vollstaendige Bewertungsbericht liegt der Finanzabteilung vor."),
    ]
    write_doc(f"{BASE}/07_IP_Lizenzen/IP_Marke_MMB_Logo_DPMA.docx", H,
              "Markenrechte MMB – Eintragung Deutsches Patent- und Markenamt (DPMA)", sections)


def gen_ip_tech_transfer():
    sections = [
        ("Parteien",
         f"{M['name']}, {M['addr']} ('Lizenznehmer / Industriepartner') und "
         "Rheinisch-Westfaelische Technische Hochschule Aachen (RWTH Aachen), Lehrstuhl fuer "
         "Produktionssystematik und Umformtechnik (PtU), vertreten durch Univ.-Prof. Dr.-Ing. Sebastian Bross "
         "('Forschungspartner / Lizenzgeber'). Templergraben 55, 52062 Aachen."),
        ("Praeambel",
         "Die RWTH hat im Rahmen eines BMBF-gefoerderten Vorhabens (FKZ 02P19A132) ein KI-Modell zur adaptiven "
         "Prozesssteuerung von Stanzpressen entwickelt (»Adaptive Process Control AI v1.4«). Halbreiter Maschinenbau "
         "ist Industriepartner des Projektes und beabsichtigt, die Forschungsergebnisse in eigenen Produkten "
         "(PL-500 Serie 2024+) kommerziell zu verwerten."),
        ("Vertragsinhalt",
         ("clauses",
          [("§ 1 Vertragsgegenstand",
            ["Gegenstand ist die Einraeumung eines nicht-exklusiven, weltweiten, kommerziellen Nutzungsrechtes an "
             "der Software »Adaptive Process Control AI v1.4« sowie der zugehoerigen Dokumentation und Algorithmen."]),
           ("§ 2 Verguetung",
            ["Einmalzahlung 240.000 EUR netto bei Vertragsabschluss.",
             "Stuecklizenzgebuehr 1.200 EUR netto je auslieferter Pressenlinie PL-500 ab Werk Koeln.",
             "Jaehrliche Mindestlizenzgebuehr 60.000 EUR ab Vertragsjahr 2."]),
           ("§ 3 Schutzrechte",
            ["Erfinderbenennungen bleiben unberuehrt. Weiterentwicklungen durch den Lizenznehmer fallen in dessen "
             "Eigentum; Verbesserungen am Kernalgorithmus werden RWTH lizenzfrei rueckangeboten (»Grant-Back«)."]),
           ("§ 4 Vertraulichkeit",
            ["NDA-Anlage 1 ist Bestandteil; Schutzpflicht 5 Jahre nach Vertragsende."]),
           ("§ 5 Laufzeit",
            ["Laufzeit 5 Jahre ab 1.7.2023, Verlaengerung optional um je 3 Jahre."])])),
        ("Foerdermittel-Bezug",
         "Das Vorhaben wurde durch das BMBF im Rahmen der Foerderlinie »KI in der Produktion« unterstuetzt. "
         "Die Verpflichtung zur Berichterstattung gegenueber dem Projekttraeger Karlsruhe (PtKa) wird von RWTH "
         "wahrgenommen. Halbreiter Maschinenbau steuert anonymisierte Performance-Daten bei."),
        ("Unterschriften",
         signatures(M["ceo"], "Geschaeftsfuehrer", M["name"],
                    "Univ.-Prof. Dr.-Ing. Sebastian Bross", "Lehrstuhlinhaber", "RWTH Aachen, Lehrstuhl PtU",
                    place="Koeln/Aachen", date_str_="28. Juni 2023")),
    ]
    write_doc(f"{BASE}/07_IP_Lizenzen/IP_Technologie_Transfer_RWTH.docx", H,
              "Technologietransfervertrag – RWTH Aachen, Lehrstuhl PtU – KI-gestuetzte Adaptive Process Control",
              sections, confidential=True)


def gen_tech_dokumentation_pl500():
    sections = [
        ("Dokumentstatus",
         tbl(["Merkmal", "Wert"],
             [["Produkt",            "Pressenlinie PL-500 (hydraulische Stanzpresse)"],
              ["Revision",            "3"],
              ["Stand",              "31.03.2024"],
              ["Verantwortlich",     "Dr.-Ing. Sabine Hoff (Konstruktion)"],
              ["Freigegeben durch",  f"{M['ceo']} (Geschaeftsfuehrung)"]])),
        ("Inhaltsuebersicht",
         ("list",
          ["Kapitel 1 – Aufbau und Funktion der Anlage",
           "Kapitel 2 – Steuerung (SINUMERIK ONE) und Schnittstellen",
           "Kapitel 3 – Werkzeug- und Schnellwechselsystem (Patent DE 20 2021 105 482.4)",
           "Kapitel 4 – Hydraulische Komponenten und Versorgung",
           "Kapitel 5 – Sicherheitseinrichtungen, CE-Konformitaet",
           "Kapitel 6 – Inbetriebnahme und Wartungsplan",
           "Kapitel 7 – Stoerungsdiagnose und Fehlercodes",
           "Kapitel 8 – Ersatzteilkatalog (Anhang A)"])),
        ("Technische Eckdaten PL-500 Rev. 3",
         tbl(["Merkmal", "Wert"],
             [["Presskraft",           "5.000 kN"],
              ["Tischflaeche",         "2.500 x 1.200 mm"],
              ["Hub",                   "max. 350 mm"],
              ["Hubzahl",              "bis 60 Hub/min"],
              ["Antrieb",              "Servo-hydraulisch, redundant"],
              ["Steuerung",            "Siemens SINUMERIK ONE, optional KI-Modul Adaptive Process Control"],
              ["Stellflaeche",          "ca. 18,5 m2"],
              ["Anschlussleistung",    "75 kW"]])),
        ("Aenderungen zur Vorrevision",
         "Rev. 3 enthaelt insbesondere: (1) Integration KI-Modul »Adaptive Process Control« (Lizenz RWTH Aachen), "
         "(2) Update SINUMERIK ONE Firmware V5.3, (3) erweiterter Schnellwechseladapter (Kapitel 3.2), "
         "(4) angepasstes EG-Konformitaetsmodul (Maschinenrichtlinie 2006/42/EG, EN ISO 13849-1 PL d)."),
        ("Verteiler und Ablage",
         "Diese Dokumentation wird im PDM-System (SOLIDWORKS PDM) abgelegt. Originalfreigabe in Papier liegt im "
         "Archiv der Konstruktion. Auslieferung an Kunden erfolgt elektronisch (PDF/A-3) gemeinsam mit der "
         "Maschine; Aktualisierungen werden durch Markus Junker an die Service-Stuetzpunkte verteilt."),
    ]
    write_doc(f"{BASE}/07_IP_Lizenzen/Technische_Dokumentation_PL500_Rev3.docx", H,
              "Technische Dokumentation Pressenlinie PL-500, Rev. 3", sections)


def gen_wartungshandbuch_fb200():
    sections = [
        ("Dokumentstatus und Geltungsbereich",
         "Dieses Wartungshandbuch gilt fuer die Foerderbandanlage FB-200 (modulares Transportsystem, Standardkonfiguration). "
         "Das Handbuch ist mit der Anlage ausgeliefert und richtet sich an den Betreiber sowie an autorisierte "
         "Wartungstechniker. Stand: 02/2024, Rev. 2."),
        ("Sicherheitshinweise",
         ("list",
          ["Vor Beginn der Wartung Hauptschalter aus / abschliessen (LOTO-Verfahren).",
           "Persoenliche Schutzausruestung (PSA): Sicherheitsschuhe, Handschuhe Schnittschutz 5, Schutzbrille.",
           "Schwerlastteile (Antriebsstation, Spannrolle) ueber Hebezug oder zu zweit transportieren.",
           "Schutzhauben und Lichtschranken nach Wartung wieder vollstaendig anbringen und auf Funktion pruefen."])),
        ("Wartungsintervalle",
         tbl(["Aufgabe", "Intervall", "Dauer ca.", "Werkzeug / Material"],
             [["Sichtpruefung Foerderband (Risse, Verschleiss)", "woechentlich", "10 min", "Taschenlampe"],
              ["Spannung Foerdergurt einstellen",                "monatlich",    "30 min", "Drehmomentschluessel 30 Nm"],
              ["Schmierung Antriebslager",                       "vierteljaehrlich", "20 min", "Schmierfett LGHP 2"],
              ["Pruefung Motor und Frequenzumrichter",            "halbjaehrlich", "60 min", "Multimeter, Diagnose-PC"],
              ["Gurt-Reinigung und Splitt-Entfernung",            "monatlich",    "45 min", "Druckluft, Buersten"],
              ["Austausch Antriebslager",                         "alle 5 Jahre", "4 h",   "Lager SKF 6308-2RS"]])),
        ("Diagnose und Fehlercodes",
         "Die Anlage meldet Stoerungen ueber den HMI-Bediener-PC (Touch-Panel) und LED-Statusanzeige am Schaltschrank. "
         "Eine ausfuehrliche Liste der Fehlercodes (F-001 bis F-148) findet sich in Anhang C. "
         "Bei Stoerungen Klasse A (Sicherheitsabschaltung) ist die Anlage stehenzulassen und der MMB-Service "
         "unverzueglich zu informieren (+49 221 47832-99)."),
        ("Ersatzteilbestellung",
         "Ersatzteile sind ueber das MMB-Service-Portal oder per E-Mail an spareparts@halbreiter-maschinenbau.de "
         "bestellbar. Bei Angabe von Anlagenseriennummer und Position aus dem Ersatzteilkatalog (Anhang A) "
         "erfolgt die Lieferung in der Regel innerhalb von 48 h."),
        ("Aktualisierung",
         "Naechste Revision geplant: 09/2024 (Anpassung an Software FB-200-FW Rev. 1.4)."),
    ]
    write_doc(f"{BASE}/07_IP_Lizenzen/Wartungshandbuch_FB200.docx", H,
              "Wartungshandbuch Foerderbandanlage FB-200", sections)


# ════════════════════════════════════════════════════════════════════════════════
# 8. Versicherungen
# ════════════════════════════════════════════════════════════════════════════════

def gen_vs_wasserschaden():
    sections = [
        ("Schadenseckdaten",
         tbl(["Merkmal", "Wert"],
             [["Schadensnummer (Versicherer)", "AGCS-2023-09-2178"],
              ["Versicherer",                   "Allianz Versicherungs-AG"],
              ["Police-Nr.",                    "GB-2023-22431"],
              ["Schadenstag",                   "11.09.2023, ca. 22:40 Uhr"],
              ["Schadensort",                   "Verwaltungsgebaeude, 2. OG, Bereich Buchhaltung"],
              ["Schadensursache",               "Bruch einer Anschlussleitung Heizungssystem (Stockwerksverteilung)"],
              ["Versicherter Schaden",         "Wasserschaden Gebaeude und Inhalt"],
              ["Schadenshoehe (gemeldet)",     "ca. 18.420 EUR netto"]])),
        ("Schadensverlauf",
         "Am 11.09.2023 gegen 22:40 Uhr loeste der Wassermelder im 2. OG des Verwaltungsgebaeudes Alarm aus (Brand- und "
         "Wassermeldeanlage Bosch). Die unverzueglich verstaendigte Werkfeuerwehr und ein Mitarbeiter des Hausmeister-"
         "Dienstleisters (Gegenbauer Services GmbH) erreichten den Standort innerhalb von 25 Minuten und stellten den "
         "Hauptwasserzulauf ab. Eine defekte Loetstelle in der Etagen-Anschlussleitung war Ausloeser des Ereignisses. "
         "Betroffen sind drei Bueros der Buchhaltung (Boden, untere Wandflaechen, Aktenschrank) sowie der angrenzende "
         "Flur. Die EDV-Ausstattung wurde nicht beschaedigt."),
        ("Sofortmassnahmen",
         ("list",
          ["Abschaltung Wasserversorgung Etage 2 und Trocknung (Aufstellung Bautrockner durch Belfor) ab 12.09.2023.",
           "Sicherung beschaedigter Akten in Trocknungskammer Belfor (Schadensminderung).",
           "Provisorische Versetzung der drei betroffenen Buchhaltungsmitarbeiter in das Besprechungsruraum 2.4.",
           "Sofortmeldung an Versicherer (Funk Gruppe als Makler) am 12.09.2023 - 08:15 Uhr."])),
        ("Schadenshoehe (Aufstellung)",
         tbl(["Position", "Betrag netto EUR"],
             [["Trocknung und Mietkosten Bautrockner (Belfor)",            "6.840"],
              ["Maler- und Bodenarbeiten (Trocknungs- und Renovierungsarbeiten)", "7.920"],
              ["Reinigung und Aktenrettung (Belfor)",                       "1.480"],
              ["Mobiliar (1 Schrank Totalschaden, 2 Schreibtische gereinigt)","2.180"],
              ["Gesamt",                                                   "18.420"]])),
        ("Bearbeitungsstand und Regulierung",
         "Schadensbesichtigung durch den Allianz-Sachverstaendigen am 14.09.2023. Regulierung in Hoehe von "
         "16.420 EUR (Selbstbehalt 2.000 EUR) per Ueberweisung am 06.11.2023 eingegangen. Abschluss des Falles "
         "am 14.11.2023. Lessons-Learned wurden in das Versicherungskataster (Ordner 06) aufgenommen."),
    ]
    write_doc(f"{BASE}/08_Versicherungen/VS_Schadensmeldung_2023_Wasserschaden.docx", H,
              "Schadensmeldung 2023 – Wasserschaden Verwaltungsgebaeude", sections)


# ════════════════════════════════════════════════════════════════════════════════
# 9. COMPLIANCE
# ════════════════════════════════════════════════════════════════════════════════

def ce_konformitaet(fname, title, produkt, baureihe, technische_daten, normen, sn_examples):
    sections = [
        ("Hersteller", f"{M['name']}, {M['addr']}, {M['hrb']}, USt-IdNr. {M['ust']}."),
        ("Bezeichnung des Produkts",
         tbl(["Merkmal", "Wert"],
             [["Produkt",           produkt],
              ["Baureihe",          baureihe],
              ["Erstellungsdatum",  "12. Januar 2024"],
              ["Bevollmaechtigter fuer technische Unterlagen", f"Dr.-Ing. Sabine Hoff, {M['name']}"]])),
        ("Technische Daten", technische_daten),
        ("Wir erklaeren in alleiniger Verantwortung",
         f"dass das oben bezeichnete Produkt mit den nachstehenden EU-Richtlinien sowie den harmonisierten "
         f"Normen uebereinstimmt:\n\n{normen}"),
        ("Konformitaetsbewertungsverfahren",
         "Konformitaetsbewertungsverfahren nach Modul A (interne Fertigungskontrolle) gemaess Maschinenrichtlinie "
         "2006/42/EG, Anhang VIII. Eine baumusterpruefung durch eine Benannte Stelle ist nicht erforderlich, "
         "da das Produkt nicht im Anhang IV der Maschinenrichtlinie aufgefuehrt ist. "
         "Die technischen Unterlagen liegen am Standort der Halbreiter Maschinenbau GmbH zur Einsichtnahme durch "
         "die Marktueberwachungsbehoerden gemaess Artikel 8 vor."),
        ("Bisher hergestellte Seriennummern (Auszug)", sn_examples),
        ("Unterschrift",
         signatures(M["ceo"], "Geschaeftsfuehrer", M["name"],
                    "Dr.-Ing. Sabine Hoff", "Leitung Konstruktion", M["name"],
                    place="Koeln", date_str_="12. Januar 2024")),
        ("Hinweise",
         "Diese Konformitaetserklaerung verliert ihre Gueltigkeit, wenn das Produkt ohne Zustimmung der "
         "Halbreiter Maschinenbau GmbH umgebaut oder veraendert wird. Sie ist gemeinsam mit der Betriebsanleitung "
         "auszuhaendigen und 10 Jahre nach Inverkehrbringen aufzubewahren."),
    ]
    write_doc(f"{BASE}/09_Compliance/{fname}.docx", H, title, sections)


def gen_ce_konformitaet():
    ce_konformitaet("CE_Konformitaetserklaerung_LS800",
                    "EG-Konformitaetserklaerung Laserschneidanlage LS-800",
                    "Laserschneidanlage LS-800 (5-Achs-CNC, Faserlaser)",
                    "LS-800",
                    "Laserleistung 8.000 W cw / 1.030 nm; Bearbeitungsbereich 3.000 x 1.500 mm; Anschlussleistung 32 kW; "
                    "Steuerung Siemens SINUMERIK ONE; Sicherheitsbauteile mit Schutzart IP54.",
                    "- Maschinenrichtlinie 2006/42/EG (Anhang II Teil A)\n"
                    "- EMV-Richtlinie 2014/30/EU\n"
                    "- Niederspannungsrichtlinie 2014/35/EU\n"
                    "- EN ISO 12100:2010 (Sicherheit von Maschinen, Risikobeurteilung)\n"
                    "- EN ISO 11553-1:2020 (Laserbearbeitungsmaschinen, Sicherheit)\n"
                    "- EN ISO 13849-1:2015 PL d (sicherheitsbezogene Steuerungen)\n"
                    "- EN 60204-1:2018 (Elektrische Ausruestung von Maschinen)",
                    ("list",
                     ["LS800-SN2023001 (ausgeliefert 12/2023 an Viessmann)",
                      "LS800-SN2024001 (ausgeliefert 03/2024)",
                      "LS800-SN2024002 (in Endmontage Q2/2024)"]))
    ce_konformitaet("CE_Konformitaetserklaerung_PL500",
                    "EG-Konformitaetserklaerung Pressenlinie PL-500",
                    "Pressenlinie PL-500 (hydraulische Stanzpresse)",
                    "PL-500 (Rev. 3, ab Baujahr 2024)",
                    "Presskraft 5.000 kN; Tischflaeche 2.500 x 1.200 mm; Hub 350 mm; Hubzahl bis 60/min; "
                    "Antrieb servo-hydraulisch; Steuerung Siemens SINUMERIK ONE; "
                    "optionales KI-Modul Adaptive Process Control (Lizenz RWTH Aachen).",
                    "- Maschinenrichtlinie 2006/42/EG (Anhang II Teil A)\n"
                    "- EMV-Richtlinie 2014/30/EU\n"
                    "- Niederspannungsrichtlinie 2014/35/EU\n"
                    "- DGRL 2014/68/EU (fuer Hydraulik-Druckbehaelter, Kategorie II, Modul D)\n"
                    "- EN ISO 12100:2010 (Sicherheit von Maschinen, Risikobeurteilung)\n"
                    "- EN 692:2005+A1:2009 (mechanische Pressen)\n"
                    "- EN ISO 13849-1:2015 PL d (sicherheitsbezogene Steuerungen)\n"
                    "- EN 60204-1:2018 (Elektrische Ausruestung von Maschinen)",
                    ("list",
                     ["PL500-SN2023001 (ausgeliefert 11/2023 an ThyssenKrupp Steel)",
                      "PL500-SN2023002 (Endmontage 12/2023, Auslieferung 02/2024)",
                      "PL500-SN2024001 (in Auftrag, Lieferung Q3/2024 Maschinenfabrik Niehoff)"]))


# Generic short COMP doc helper
def comp_short(fname, title, intro, abschnitte):
    """abschnitte: list of (heading, body)"""
    footer = ("Dokumentstatus und Pflege",
              "Klassifizierung: »intern – vertraulich«. Dieses Dokument ist Bestandteil des "
              "Compliance-Management-Systems (CMS) der Halbreiter Maschinenbau GmbH gemaess der Verfahrensanweisung "
              "VA-COMP-001 (Rev. 4). Verantwortlich fuer die Pflege ist Anja Lenz (Compliance-Stelle) in Abstimmung "
              "mit Sandra Becker (CFO). Eine Aktualisierung erfolgt mindestens jaehrlich sowie anlassbezogen bei "
              "wesentlichen Aenderungen der Rechtslage, der Organisation oder der Geschaeftsprozesse. "
              "Verteiler: Geschaeftsfuehrung, Bereichsleiter Compliance, Bereichsleiter QM, Betriebsrat. "
              "Archivierung erfolgt revisionssicher im DMS (M-Files) gemaess Aufbewahrungsfristenkatalog der "
              "Halbreiter Maschinenbau GmbH (Standardfrist 10 Jahre, soweit nicht laenger gesetzlich vorgeschrieben). "
              "Bei Fragen zu Inhalt oder Anwendbarkeit dieses Dokumentes wenden Sie sich an "
              "compliance@halbreiter-maschinenbau.de oder an die zustaendige Bereichsleitung.")
    sections = [("Zweck und Geltungsbereich", intro)] + list(abschnitte) + [footer]
    write_doc(f"{BASE}/09_Compliance/{fname}.docx", H, title, sections)


def gen_comp_shorts():
    comp_short("COMP_Abfallentsorgungsnachweis_2023",
               "Abfallentsorgungsnachweis 2023",
               "Dieser Nachweis dokumentiert die ordnungsgemaesse Entsorgung der bei der Halbreiter Maschinenbau GmbH "
               "in 2023 angefallenen gefaehrlichen und nicht gefaehrlichen Abfaelle gemaess KrWG, "
               "Nachweisverordnung (NachwV) und Abfallverzeichnis-Verordnung (AVV).",
               [("Abfallschluessel und Mengen",
                 tbl(["AVV-Schluessel", "Bezeichnung", "Menge (t)", "Entsorger"],
                     [["12 01 01", "Eisenmetallspaene", "184,2", "TSR Recycling GmbH"],
                      ["12 01 03", "NE-Metallspaene",   "  12,4", "TSR Recycling GmbH"],
                      ["12 01 09*","Bearbeitungsemulsionen (gefaehrl.)", "8,6", "Avista Oil AG"],
                      ["12 01 12*","verbrauchte Schleifmittel",          "1,2", "Remondis SE & Co. KG"],
                      ["15 01 02", "Verpackung Kunststoff",              "4,8", "Remondis SE & Co. KG"],
                      ["15 01 03", "Verpackung Holz (Paletten)",        "11,2", "Remondis SE & Co. KG"],
                      ["20 03 01", "gemischte Siedlungsabfaelle",        "5,4", "AWB Koeln"]])),
                ("Begleitscheine und Aufbewahrung",
                 "Saemtliche Begleit- und Uebernahmescheine (eANV-Verfahren) werden im Modul ZEDAL gefuehrt und "
                 "fuer 3 Jahre archiviert (gefaehrliche Abfaelle) bzw. 6 Jahre bei Nachweispflicht. Verantwortlich: "
                 "Betriebsbeauftragter fuer Abfall Markus Junker (Bestellung 04/2018)."),
                ("Erklaerung",
                 "Wir bestaetigen, dass die Entsorgung saemtlicher Abfaelle ueber zertifizierte Entsorgungsfachbetriebe "
                 "(EfbV) erfolgt ist und keine Auffaelligkeiten gemeldet wurden. "
                 "Freigabe: Markus Junker, 22. Januar 2024."),
                ("Anlagen",
                 ("list",
                  ["Liste eANV-Begleitscheine 2023 (Anlage 1)",
                   "Zertifikate der Entsorgungsfachbetriebe (Anlage 2)",
                   "Bestellung Abfallbeauftragter (Anlage 3)"]))])

    comp_short("COMP_Antikorruptions_Training_2023_Protokoll",
               "Protokoll Antikorruptionsschulung 2023",
               "Im Berichtsjahr 2023 wurde fuer alle gefaehrdeten Funktionen der Halbreiter Maschinenbau GmbH "
               "(Einkauf, Vertrieb, Geschaeftsfuehrung, Service) eine Pflichtschulung zur Antikorruption durchgefuehrt. "
               "Grundlage ist die Richtlinie »Antikorruption und Zuwendungen« (COMP_004, Rev. 2) sowie der UK Bribery Act / "
               "deutsche §§ 299 ff. StGB.",
               [("Schulungsumfang",
                 ("list",
                  ["Webbasiertes Training (eLearning, 90 min) ueber Plattform Lawpilots.",
                   "Praesenz-Workshop fuer Einkaufsleitung und Vertriebsleitung (4 h) am 18.05.2023.",
                   "Wissens-Check (15 Fragen, Mindestbestehen 80 %)."])),
                ("Teilnahmestatistik",
                 tbl(["Funktion", "Pflichtige", "Absolviert", "Quote"],
                     [["Einkauf",          "18", "18", "100 %"],
                      ["Vertrieb DACH/Int","26", "26", "100 %"],
                      ["Service / Field",  "32", "31",  "97 %"],
                      ["Geschaeftsfuehrung","2",  "2", "100 %"],
                      ["Compliance/Recht",  "3",  "3", "100 %"],
                      ["Gesamt",           "81", "80",  "99 %"]])),
                ("Massnahmen bei Nichtabsolvierung",
                 "Ein Service-Mitarbeiter (laenger erkrankt) wird das Training nach Genesung in Q1/2024 nachholen. "
                 "Personalabteilung verfolgt offene Faelle. Wiederholungsfrequenz: alle 24 Monate, ggf. bei "
                 "Funktionswechsel sofort."),
                ("Freigabe",
                 "Schulungsdurchfuehrung dokumentiert durch HR-Leitung (Frau Petra Hartmann). Geschaeftsfuehrungs-"
                 "freigabe durch Sandra Becker (CFO) am 10.12.2023.")])

    comp_short("COMP_Arbeitsschutz_Gefaehrdungsbeurteilung_2023",
               "Gefaehrdungsbeurteilung Arbeitsschutz 2023",
               "Die Gefaehrdungsbeurteilung gemaess § 5 ArbSchG und Betriebssicherheitsverordnung (BetrSichV) wurde "
               "in 2023 systematisch fuer alle Arbeitsbereiche der Halbreiter Maschinenbau GmbH aktualisiert. "
               "Sie umfasst die Identifikation von Gefaehrdungen, die Bewertung der Risiken und die Festlegung "
               "von Schutzmassnahmen.",
               [("Methodik",
                 "Die Beurteilung erfolgt nach Nohl-Methode (Schadensschwere x Eintrittswahrscheinlichkeit) mit "
                 "einer 7-stufigen Skala. Begehungen wurden vom Sicherheitsingenieur (Markus Junker), der "
                 "Sicherheitsfachkraft (extern: TUEV Rheinland, Herr Mehrens) und Betriebsraetin Frau Tatjana "
                 "Weber gemeinsam durchgefuehrt."),
                ("Hauptergebnisse",
                 tbl(["Bereich", "Top-Risiken", "Massnahmenstatus"],
                     [["CNC-Zerspanung Halle A",   "Spaenefluc, Larm > 85 dB(A)", "PSA + Schallschutzkapsel offen"],
                      ["Laserschneiden Halle B",   "Laserstrahlung Klasse 4",     "Schutzgehaeuse vorhanden, OK"],
                      ["Pressen Halle B",          "Quetschgefahr Werkzeugwechsel","Zweihandbedienung OK"],
                      ["Wareneingang / Logistik",  "Gabelstapler-Personenverkehr","Wegekonzept aktualisiert"],
                      ["Bueros",                    "Bildschirmarbeit, Ergonomie",  "Sitzpositionsschulung 04/2024"]])),
                ("Massnahmenplan",
                 ("list",
                  ["Schallschutzkapsel an 2 CNC-Fraesmaschinen nachruesten (Q2/2024).",
                   "Hilfsmittel zum Werkzeugwechsel an PL-500 standardisieren (Q3/2024).",
                   "Schulung Bildschirmarbeit/Ergonomie fuer Buero-Beschaeftigte (04/2024)."])),
                ("Freigabe und Wiederholung",
                 "Die Geschaeftsfuehrung hat die GBU am 18.12.2023 freigegeben. Eine vollstaendige Wiederholung "
                 "ist alle 24 Monate vorgesehen; anlassbezogene Aktualisierungen werden fortlaufend dokumentiert. "
                 "Pflege im Modul »Quentic Safety«.")])

    comp_short("COMP_Aufsichtsbehörden_Kommunikation_2023",  # umlaut intentional
               "Kommunikation mit Aufsichtsbehoerden 2023",
               "Diese Uebersicht dokumentiert alle wesentlichen Kontakte und Korrespondenzen zwischen der "
               "Halbreiter Maschinenbau GmbH und externen Aufsichtsbehoerden im Berichtsjahr 2023 (DSGVO, Umwelt, "
               "Arbeitsschutz, Zoll, Marktueberwachung).",
               [("Uebersicht der Kontakte",
                 tbl(["Behoerde", "Anlass", "Datum", "Ergebnis"],
                     [["LDI NRW",                    "Routine-Anfrage Datenschutz (CRM)", "14.03.2023", "Beantwortet, keine Beanstandung"],
                      ["BG Holz und Metall",         "Betriebsbegehung",                   "22.05.2023", "2 Hinweise, Massnahmen Q3 erledigt"],
                      ["BAFA",                       "Ausfuhrgenehmigung CN, ECCN 2B999",  "12.07.2023", "Genehmigung erteilt"],
                      ["StU Koeln (Umwelt)",         "Pruefung Indirekteinleiter",         "08.09.2023", "Ohne Beanstandung"],
                      ["Hauptzollamt Koeln",         "Routine-Pruefung AEO-Status",        "14.11.2023", "AEO-F bestaetigt"],
                      ["Gewerbeaufsicht",            "Anhoerung Hallenanbau (Bauantrag)",  "26.02.2024", "Stellungnahme positiv"]])),
                ("Bearbeitungsprozess",
                 "Anfragen werden zentral durch die Compliance-Stelle (Frau Anja Lenz) entgegengenommen, "
                 "dokumentiert und an die zustaendigen Bereichsleiter weitergeleitet. Antworten werden vor "
                 "Versand durch Sandra Becker (CFO) gegengezeichnet."),
                ("Kennzahlen 2023",
                 ("list",
                  ["6 Vorgaenge insgesamt (Vorjahr: 4).",
                   "Durchschnittliche Reaktionszeit: 3,2 Werktage.",
                   "Keine Sanktionen, keine offenen Mahnungen.",
                   "1 Folgeauflage (BG): vollstaendig erledigt."])),
                ("Schlussfolgerung",
                 "Die Compliance-Stelle bewertet das Niveau der behoerdlichen Interaktion als unauffaellig. "
                 "Eine Eskalation oder behoerdliche Massnahme war im Berichtsjahr nicht erforderlich.")])

    comp_short("COMP_Betriebsbegehungsprotokoll_BG_",
               "Betriebsbegehungsprotokoll BG Holz und Metall 2023",
               "Am 22. Mai 2023 fand am Standort Koeln eine Betriebsbegehung durch die Berufsgenossenschaft "
               "Holz und Metall (Aufsichtsperson Frau Dr. Bettina Werner) statt. Inhalt war die Pruefung "
               "der Arbeitsschutzorganisation gemaess DGUV Vorschrift 2 und DGUV Vorschrift 1.",
               [("Teilnehmer",
                 ("list",
                  ["BGHM: Dr. Bettina Werner (Aufsichtsperson Bezirk Koeln-West)",
                   "MMB: Klaus Mueller (CEO), Markus Junker (SiFa), Petra Hartmann (HR)",
                   "Betriebsrat: Tatjana Weber"])),
                ("Begangenheiten",
                 ("list",
                  ["Werkstattbereiche Halle A (CNC-Zerspanung)",
                   "Halle B (Lasern, Pressen, Vormontage)",
                   "Wareneingang / Stapler-Verkehr",
                   "Aussenbereiche / Fluchtwege",
                   "Sozialraeume und Sanitaereinrichtungen"])),
                ("Befunde",
                 tbl(["Nr.", "Befund", "Klasse", "Massnahme", "Termin"],
                     [["1", "Markierung Stapler-Fahrwege Halle C teilweise verblasst", "B",
                       "Bodenmarkierung erneuern", "Q3/2023"],
                      ["2", "Schulungsnachweise Hubarbeitsbuehne unvollstaendig (2 MA)", "B",
                       "Nachschulung und Eintrag in Personalakte", "Q3/2023"],
                      ["3", "Erste-Hilfe-Aushang Halle B veraltet (Notrufnummern)", "C",
                       "Aushang aktualisieren", "06/2023"]])),
                ("Statusbericht",
                 "Alle Befunde wurden bis September 2023 abgearbeitet. Die BGHM wurde am 14.11.2023 schriftlich "
                 "informiert; keine Nachpruefung gefordert. Eine Begehung BG ist turnusgemaess in 2026 vorgesehen.")])

    comp_short("COMP_CO2-Bilanz_2023_Corporate_Car",
               "CO2-Bilanz 2023 (Corporate Carbon Footprint)",
               "Die CO2-Bilanz (Corporate Carbon Footprint, CCF) der Halbreiter Maschinenbau GmbH wurde fuer das "
               "Geschaeftsjahr 2023 erstmals nach GHG-Protocol Corporate Standard und ISO 14064-1 ermittelt. "
               "Berichtsgrenzen: operativ kontrollierter Ansatz, Standort Koeln (inkl. Aussenlager Niehler Strasse).",
               [("Scope-Ergebnisse",
                 tbl(["Scope", "Quelle", "Emission t CO2eq"],
                     [["1", "Erdgas (Heizung, Prozesse)",                   "186"],
                      ["1", "Dieselverbrauch Stapler/Fuhrpark Werk",         " 24"],
                      ["1", "Kuehlmittelverluste (R134a/R32)",               "  4"],
                      ["2", "Strom (Marktbezug, Standardmix)",              "412"],
                      ["2", "Strom (Marktbezug, Greenpower-Anteil 35 %)",   "-144 (gutgeschrieben)"],
                      ["3", "Geschaeftsreisen, Vorprodukte (Hot-Spots)",   "1.580 (geschaetzt)"],
                      ["Gesamt Scope 1+2 (location-based)",                  "626"]])),
                ("Methodik",
                 "Datenerhebung durch Sandra Becker (CFO) und Markus Junker (Energiebeauftragter). "
                 "Emissionsfaktoren GEMIS 5.0 / Defra 2023. Externe Plausibilisierung durch EnviCon GmbH (Koeln) "
                 "im Q1/2024. Scope 3 wird in 2024 vertieft erhoben (PCF je Produkt)."),
                ("Reduktionsmassnahmen 2024",
                 ("list",
                  ["PV-Anlage Halle B Sued (350 kWp, Inbetriebnahme Q4/2024).",
                   "Wechsel auf zertifizierten Oekostrom (Standortzertifikat) zum 01.01.2025 geplant.",
                   "Umstellung Stapler-Fuhrpark auf Lithium-Ionen (4 von 8 in 2024).",
                   "Dienstwagen-Richtlinie: Neuzugaenge ab 04/2024 nur noch BEV/PHEV (CO2 < 50 g/km)."]))])

    comp_short("COMP_Datenschutzerklärung_Website",
               "Datenschutzerklaerung Website halbreiter-maschinenbau.de",
               "Diese Datenschutzerklaerung informiert ueber die Verarbeitung personenbezogener Daten auf der "
               "Unternehmens-Website www.halbreiter-maschinenbau.de gemaess Art. 13 DSGVO. Verantwortlicher ist die "
               f"{M['name']}, {M['addr']}.",
               [("Verarbeitungsuebersicht",
                 tbl(["Zweck", "Datenkategorien", "Rechtsgrundlage", "Speicherdauer"],
                     [["Server-Logs (Sicherheit)", "IP, User-Agent, Zeitstempel",   "Art. 6 Abs. 1 lit. f", "30 Tage"],
                      ["Kontaktformular",          "Name, E-Mail, Nachricht",        "Art. 6 Abs. 1 lit. b", "6 Monate"],
                      ["Newsletter (Double-Opt-In)","E-Mail, Anrede",                "Art. 6 Abs. 1 lit. a", "bis Abmeldung"],
                      ["Karriereportal",           "Bewerbungsdaten (Lebenslauf, Zeugnisse)", "Art. 6 Abs. 1 lit. b", "6 Monate nach Absage"],
                      ["Webanalyse (Matomo, anonymisierte IP)", "Klicks, Verweildauer", "Art. 6 Abs. 1 lit. f", "6 Monate"]])),
                ("Empfaenger und Auftragsverarbeiter",
                 ("list",
                  ["Hosting: Hetzner Online GmbH (Falkenstein), AVV vorhanden.",
                   "E-Mail-Versand Newsletter: Cleverreach GmbH & Co. KG (Rastede), AVV vorhanden.",
                   "Bewerbermanagement: Personio SE & Co. KG (Muenchen), AVV vorhanden."])),
                ("Betroffenenrechte",
                 "Betroffene haben das Recht auf Auskunft (Art. 15), Berichtigung (Art. 16), Loeschung (Art. 17), "
                 "Einschraenkung der Verarbeitung (Art. 18), Datenuebertragbarkeit (Art. 20) und Widerspruch (Art. 21). "
                 "Anfragen sind per E-Mail an datenschutz@halbreiter-maschinenbau.de zu richten. "
                 "Beschwerderecht bei LDI NRW. Datenschutzbeauftragter: Herr RA Dr. Joerg Hilpert (extern, "
                 "Hilpert & Partner mbB, Koeln)."),
                ("Stand", "Stand 12.02.2024, jaehrliche Pruefung Q1.")])

    comp_short("COMP_Datenschutzfolgeabschaetzung_CRM",
               "Datenschutz-Folgenabschaetzung (DSFA) CRM-System 2024",
               "Die DSFA gemaess Art. 35 DSGVO wurde fuer den Einsatz des CRM-Systems Salesforce Sales Cloud + "
               "Service Cloud bei der Halbreiter Maschinenbau GmbH erstellt, da personenbezogene Daten von "
               "Ansprechpartnern, Interessenten und Servicekontakten in betraechtlichem Umfang verarbeitet werden.",
               [("Verarbeitungsuebersicht",
                 tbl(["Phase", "Datenkategorien"],
                     [["Lead-/Kontaktdaten",   "Name, Position, Telefon, E-Mail, Unternehmen"],
                      ["Vertriebsaktivitaeten","Notizen, Angebote, E-Mail-Korrespondenz"],
                      ["Servicefaelle",        "Reklamationsbeschreibung, ggf. Foto-/Anlagedaten"],
                      ["Marketingautomation",   "Open Rates, Klicks (anonymisierbar)"]])),
                ("Risikobewertung",
                 ("list",
                  ["Hauptrisiken: unbefugter Zugriff durch externe Angreifer; Berechtigungs-Sprawl intern.",
                   "Drittlandtransfer: Salesforce hat EU-Datenresidenz (Frankfurt) gewaehlt; SCC 2021 verfuegbar.",
                   "Profilbildung Marketing wird nur fuer Newsletter-Empfaenger mit Einwilligung vorgenommen.",
                   "Risikoniveau gesamt: »mittel« nach Restrisikobewertung."])),
                ("Schutzmassnahmen",
                 ("list",
                  ["MFA-Pflicht fuer alle User (Salesforce + IdP Azure AD).",
                   "Rollen- und Berechtigungskonzept (Need-to-know), jaehrliche Rezertifizierung.",
                   "Audit-Log-Auswertung quartalsweise; Anomalie-Erkennung via Salesforce Shield.",
                   "Loeschkonzept: Inaktive Leads > 24 Monate werden anonymisiert."])),
                ("Freigabe",
                 "DSFA wurde am 18.02.2024 durch den DSB (Dr. Joerg Hilpert) abschliessend bewertet und durch "
                 "die Geschaeftsfuehrung freigegeben. Re-Assessment alle 12 Monate bzw. anlassbezogen.")])

    comp_short("COMP_Einheitliche_Europäische_Eigen",
               "Einheitliche Europaeische Eigenerklaerung (ESPD) – Vergabe Stadt Koeln 2024",
               "Diese ESPD wurde im Rahmen des oberschwelligen Vergabeverfahrens »Lieferung und Inbetriebnahme einer "
               "Foerderbandanlage fuer den Wertstoffhof der Stadt Koeln« (Vergabe-Nr. 67.3-2024-S-018) abgegeben. "
               "Sie erfuellt die Anforderungen gemaess Art. 59 RL 2014/24/EU und § 50 VgV.",
               [("Angaben zum Wirtschaftsteilnehmer",
                 tbl(["Merkmal", "Wert"],
                     [["Firma",     M["name"]],
                      ["Anschrift", M["addr"]],
                      ["Register",  M["hrb"]],
                      ["USt-IdNr.", M["ust"]],
                      ["Vertretungsberechtigter", f"{M['ceo']} (Geschaeftsfuehrer)"],
                      ["Mitarbeiter (FTE)", "247"],
                      ["Jahresumsatz 2023", "48,63 Mio. EUR"]])),
                ("Erklaerungen zu Ausschlussgruenden",
                 ("list",
                  ["Keine rechtskraeftige Verurteilung wegen Bestechung, Geldwaesche, Steuerhinterziehung o.ae.",
                   "Keine offenen Sozialversicherungs- oder Steuerschulden.",
                   "Keine Insolvenz oder Liquidation; kein Antrag anhaengig.",
                   "Tariftreueerklaerung NRW abgegeben (Mindestlohn, Verguetungstarif IGM NRW)."])),
                ("Eignungsangaben",
                 ("list",
                  ["Referenzobjekte (3 in den letzten 3 Jahren) liegen vor, siehe Anlage 1.",
                   "Beruflichefachkundige Leitung: Dr.-Ing. Sabine Hoff.",
                   "Versicherung Betriebshaftpflicht 10 Mio. EUR (Allianz)."])),
                ("Unterschrift",
                 signatures(M["ceo"], "Geschaeftsfuehrer", M["name"],
                            "Stefan Braun", "Bevollmaechtigter Vertrieb", M["name"],
                            place="Koeln", date_str_="26. Februar 2024"))])

    comp_short("COMP_Energiemanagementsystem_DIN_EN_ISO_50001",
               "Energiemanagementsystem DIN EN ISO 50001 – Statusbericht",
               "Statusbericht zum Energiemanagementsystem (EnMS) gemaess DIN EN ISO 50001:2018 fuer das "
               "Berichtsjahr 2023. Das EnMS wurde 2020 eingefuehrt und im November 2023 durch DEKRA Certification "
               "GmbH erfolgreich re-zertifiziert (Zertifikat gueltig bis 11/2026).",
               [("Energiekennzahlen 2023",
                 tbl(["Kennzahl", "2023", "2022", "Veraenderung"],
                     [["Stromverbrauch (MWh)",        "1.180", "1.226", "-3,8 %"],
                      ["Erdgasverbrauch (MWh)",         "742",   "812",  "-8,6 %"],
                      ["Energiekosten (TEUR)",          "318",   "362", "-12,2 %"],
                      ["Energieintensitaet (kWh/EUR Umsatz)", "0,040", "0,046", "-13,0 %"]])),
                ("Massnahmen 2023",
                 ("list",
                  ["LED-Umruestung Halle A (Phase 2): -42 MWh/a.",
                   "Druckluft-Leckage-Programm: -28 MWh/a.",
                   "Optimierung Heizungssteuerung Verwaltungsgebaeude: -55 MWh/a.",
                   "Sensitive Aufklaerung Mitarbeiter ('Energie-Botschafter'-Programm).",
                   "Erstellung Spitzenlastmanagement-Konzept fuer 2024 (gemeinsam mit RWE)."])),
                ("Naechste Schritte 2024",
                 ("list",
                  ["Inbetriebnahme PV-Anlage Halle B Sued (350 kWp, Q4/2024).",
                   "Wechsel auf zertifizierten Oekostrom zum 01.01.2025.",
                   "Internes ISO 50001-Audit Q3/2024 (Auditor: Markus Junker)."])),
                ("Freigabe",
                 "Statusbericht freigegeben durch Sandra Becker (CFO) am 22. Februar 2024. Verteiler: GF, Bereichsleiter, "
                 "Betriebsrat. Naechste Aktualisierung: Q1/2025.")])

    comp_short("COMP_Exportkontrollbericht_2023",
               "Exportkontrollbericht 2023",
               "Dieser Bericht fasst die Tatigkeiten der Halbreiter Maschinenbau GmbH im Bereich Exportkontrolle "
               "fuer das Berichtsjahr 2023 zusammen. Grundlage sind insbesondere die AWG/AWV, die EU-Dual-Use-VO "
               "2021/821 sowie die EU-Sanktionen gegen Russland und Belarus.",
               [("Exportstatistik 2023",
                 tbl(["Bestimmungsland", "Anzahl Ausfuhren", "Davon genehmigungspflichtig", "Umsatzanteil"],
                     [["EU",                  "184", "0",  "62 %"],
                      ["UK, CH",                "42", "0",   "8 %"],
                      ["USA, KANADA",           "28", "0",   "6 %"],
                      ["Asien (CN, JP, KR)",   "36", "12", "16 %"],
                      ["Mittlerer Osten",        "8", "3",   "4 %"],
                      ["Sonstige",              "12", "1",   "4 %"]])),
                ("Genehmigungen",
                 ("list",
                  ["BAFA-Einzelgenehmigung CN: 12 Vorgaenge (PL-500 + Software), ECCN 2B999 / 2D993.",
                   "BAFA Sammelgenehmigung Saudi-Arabien: 3 Vorgaenge (FB-200), Pruefung Endverwendungserklaerung.",
                   "Antrag Indien: 1 Vorgang in Bearbeitung (Bescheidung erwartet Q1/2024)."])),
                ("Sanktionspruefung",
                 "Saemtliche Geschaeftspartner werden ueber das Compliance-Tool »MK Denial«-Pruefung gegen die "
                 "EU-Sanktionslisten (CFSP), die US-OFAC SDN-Liste und die UK-Konsolidierte Liste abgeglichen. "
                 "2023 wurden 4 potentielle Treffer manuell geklaert; 1 Geschaeftsanbahnung in Belarus wurde "
                 "abgebrochen (Sanktionsbetroffenheit)."),
                ("Schulung und Audit",
                 "Exportkontrollbeauftragter Holger Brinkmann; Stellvertretung Anja Lenz. Jaehrliches "
                 "BAFA-AEO-Refresher-Training durchgefuehrt. Naechstes internes Audit Q2/2024.")])

    comp_short("COMP_FuE_Antrag_Foerderung_BMWi",
               "Foerderantrag BMWi – Pressenmaschinen 4.0 Edge-KI",
               "Antrag auf Foerderung im Rahmen der ZIM-Foerderlinie »Innovation und Mittelstand« des BMWK (vormals BMWi) "
               "fuer das FuE-Projekt »Pressenmaschinen 4.0 – Edge-KI fuer adaptive Prozesssteuerung«.",
               [("Eckdaten Antrag",
                 tbl(["Merkmal", "Wert"],
                     [["Antragsteller",       M["name"]],
                      ["Foerderlinie",        "ZIM (Zentrales Innovationsprogramm Mittelstand)"],
                      ["Projektpartner",      "RWTH Aachen (Lehrstuhl PtU); ifak Magdeburg"],
                      ["Projektlaufzeit",      "01.07.2024 – 30.06.2027 (36 Monate)"],
                      ["Antragsdatum",         "14.02.2024"],
                      ["Aktenzeichen",         "ZIM-KK1418042KS4"]])),
                ("Projektzusammenfassung",
                 "Ziel des Vorhabens ist die Entwicklung einer Edge-KI-Loesung zur adaptiven Prozesssteuerung von "
                 "hydraulischen Pressen unter Beruecksichtigung von Werkzeug- und Werkstoffvarianzen. "
                 "Im Ergebnis sollen Ausschussraten um > 30 % reduziert und Energieverbrauch um > 10 % gesenkt werden."),
                ("Aufwand und Foerderbedarf",
                 tbl(["Position", "Betrag (TEUR)", "Foerderquote"],
                     [["Personal MMB",       "1.420", "45 %"],
                      ["Sachmittel MMB",       "320",  "45 %"],
                      ["Vergaben RWTH (UA)",   "480", "100 %"],
                      ["Vergaben ifak (UA)",   "320", "100 %"],
                      ["Gesamtvolumen",       "2.540", "—"]])),
                ("Bewilligungsperspektive",
                 "Projekttraeger AiF/PtKa; Voraussetzung positive Bewertung durch externen Gutachter. "
                 "Erste Rueckmeldung erwartet bis 06/2024.")])

    comp_short("COMP_FuE_Bericht_2023",
               "Forschungs- und Entwicklungsbericht 2023",
               "Dieser Bericht fasst die wesentlichen FuE-Aktivitaeten der Halbreiter Maschinenbau GmbH im "
               "Geschaeftsjahr 2023 zusammen. FuE-Quote (FuE-Ausgaben / Umsatz): 6,4 % (Vorjahr 5,9 %).",
               [("Kennzahlen",
                 tbl(["Merkmal", "2023", "2022"],
                     [["FuE-Ausgaben (TEUR)",         "3.110", "2.620"],
                      ["FuE-Personal (FTE)",          "  21",   "  18"],
                      ["Schutzrechtsanmeldungen",     "   2",   "   1"],
                      ["Aktive Schutzrechte",          "  14",   "  13"],
                      ["KFW/BAFA-Foerderung erhalten","  342",   "  280"]])),
                ("Schwerpunkte 2023",
                 ("list",
                  ["PL-500 Rev. 3: Integration KI-Modul »Adaptive Process Control« (mit RWTH Aachen).",
                   "FB-200: Modular-Erweiterung Schwenkmodul, Markteinfuehrung Q1/2024.",
                   "MR-150: Vorbereitung Kollaborationsroboter-Konfiguration mit Onrobot-Greifer (TS 2025).",
                   "Neue Pruefumgebung: Aufbau Software-in-the-Loop (SIL) Stand fuer Maschinenfirmware."])),
                ("Geplante Schritte 2024",
                 ("list",
                  ["Foerderantrag »Pressenmaschinen 4.0« (ZIM, mit RWTH und ifak).",
                   "Anmeldung eines Patentes »Adaptive Pressenwerkzeug-Erkennung« (Boehmert & Boehmert).",
                   "Aufbau MMB-IoT-Cloud-Pilot fuer Predictive Maintenance bei A-Kunden."])),
                ("Freigabe",
                 "Bericht freigegeben durch Dr.-Ing. Sabine Hoff (Leitung Konstruktion) und Klaus Mueller (CEO) "
                 "am 12. Februar 2024.")])

    comp_short("COMP_Internes_Audit_ISO_9001_2023",
               "Internes Audit ISO 9001:2015 – Programm 2023",
               "Das jaehrliche interne Audit-Programm 2023 zur Aufrechterhaltung der Zertifizierung nach "
               "DIN EN ISO 9001:2015 wurde planmaessig durchgefuehrt. Lead Auditor: Petra Krueger "
               "(Qualitaetsmanagementbeauftragte). Auditierungszeitraum: Februar-November 2023.",
               [("Auditbereiche und Befunde",
                 tbl(["Bereich", "Auditdatum", "Befunde A/B/C", "Status"],
                     [["Geschaeftsleitung / KVP",       "14.02.2023", "0 / 0 / 2", "abgeschlossen"],
                      ["Vertrieb / Auftragsbearbeitung","12.04.2023", "0 / 1 / 3", "abgeschlossen"],
                      ["Einkauf / Lieferantenmgmt.",    "07.05.2023", "0 / 1 / 2", "abgeschlossen"],
                      ["Produktion Halle A/B",          "18.06.2023", "0 / 0 / 4", "abgeschlossen"],
                      ["Qualitaetssicherung",          "22.09.2023", "0 / 0 / 1", "abgeschlossen"],
                      ["Service / After-Sales",         "14.11.2023", "0 / 1 / 2", "abgeschlossen"]])),
                ("Schwerpunkte / KVP",
                 ("list",
                  ["Reklamationsbearbeitung: durchschnittliche Loesungszeit 7,2 Tage (Ziel <= 5 Tage).",
                   "Lieferantenmanagement: Lieferantenstatus systematischer dokumentieren (Massnahme 2024).",
                   "Schulungsplaene: Aktualitaet im HR-System fuer Service-MA verbessern."])),
                ("Re-Zertifizierung",
                 "Externes Re-Zertifizierungsaudit durch DEKRA Certification: 8.-10.11.2023. Zertifikat gueltig "
                 "bis 11/2026. Hauptbefunde: keine Major-Findings; 4 Minor und 6 Hinweise wurden bis 31.12.2023 "
                 "abgeschlossen.")])

    comp_short("COMP_Lieferantenbewertung_Matrix_2023",
               "Lieferanten-Risikomatrix 2023 (Compliance-Schwerpunkt)",
               "Diese Risikomatrix bewertet die Lieferanten der Halbreiter Maschinenbau GmbH unter Compliance-Aspekten "
               "gemaess Lieferkettensorgfaltspflichtengesetz (LkSG) sowie der internen Code-of-Conduct-Anforderungen. "
               "Sie ergaenzt die operative Lieferantenbewertung (siehe Ordner 05).",
               [("Risikokategorien",
                 tbl(["Risikokategorie", "Gewicht", "Beschreibung"],
                     [["Menschenrechte",      "30 %", "Zwangsarbeit, Kinderarbeit, Vereinigungsfreiheit"],
                      ["Umwelt",              "25 %", "Konventionen Minamata, Basel; Emissionen, Wasser"],
                      ["Antikorruption",      "20 %", "Bestechung, Interessenkonflikte"],
                      ["Geografie",            "15 %", "Laenderrisiko BAFA-Lange / Heritage-Risk-Index"],
                      ["Branchenrisiko",       "10 %", "Branchenspezifisches Konfliktmineralien-Risiko"]])),
                ("Risikoeinstufung Hauptlieferanten",
                 tbl(["Lieferant", "Land", "Risikoscore (0-100)", "Status"],
                     [["Schunk GmbH & Co. KG",          "DE",  "8",  "niedrig"],
                      ["Igus GmbH",                      "DE", "10",  "niedrig"],
                      ["Siemens AG",                     "DE",  "9",  "niedrig"],
                      ["Trumpf SE + Co. KG",             "DE",  "9",  "niedrig"],
                      ["SAP SE",                          "DE",  "8",  "niedrig"],
                      ["DB Schenker Deutschland AG",     "DE", "12",  "niedrig"]])),
                ("Massnahmen",
                 ("list",
                  ["Self-Assessment Questionnaire (SAQ) jaehrlich an alle A-Lieferanten.",
                   "Vor-Ort-Audits stichprobenartig bei B-Lieferanten mit Score > 30 (in 2024: 4 Audits geplant).",
                   "Eskalationsverfahren bei Verstoessen gemaess LkSG (Beschwerdekanal Compliance-Hotline)."])),
                ("Bericht und Pflege",
                 "Verantwortlich: Anja Lenz (Compliance). Pflege quartalsweise; Bericht an Geschaeftsfuehrung "
                 "halbjaehrlich.")])

    comp_short("COMP_Maßnahmenplan_ISO_9001_Audit_2",
               "Massnahmenplan ISO 9001:2015 – Audit 2023",
               "Massnahmenplan zur Bearbeitung der im externen Re-Zertifizierungsaudit ISO 9001:2015 (DEKRA, "
               "8.-10.11.2023) festgestellten Hinweise und Minor-Findings. Stand: 31.12.2023.",
               [("Massnahmenuebersicht",
                 tbl(["Nr.", "Befund / Hinweis", "Klasse", "Massnahme", "Verantwortlich", "Termin", "Status"],
                     [["1", "Lieferantenstatus nicht konsistent im SAP SRM dokumentiert", "Minor",
                       "Stammdatenbereinigung A/B/C-Klassifizierung", "S. Braun", "31.12.2023", "erledigt"],
                      ["2", "Reklamations-Loesungszeit > 5 Tage (Service)", "Minor",
                       "8D-Prozess straffen, Reaktionszeit definieren", "P. Krueger", "31.03.2024", "in Arbeit"],
                      ["3", "Schulungsmatrix Service-Techniker veraltet", "Minor",
                       "Aktualisierung in Personio", "P. Hartmann", "31.12.2023", "erledigt"],
                      ["4", "Pruefmittelueberwachung Halle A unvollst.",   "Minor",
                       "Kalibrierscheine im DMS pflegen", "M. Junker", "31.12.2023", "erledigt"]])),
                ("Naechste Schritte",
                 "Nachverfolgung im Modul »IMS QM Direct« ueber das Tracking-Board QM-2023-AUD. "
                 "Bestaetigung der erledigten Massnahmen durch QMB Petra Krueger. Ueberpruefung im Rahmen des "
                 "internen Audits 2024."),
                ("Freigabe",
                 "Massnahmenplan freigegeben durch Petra Krueger (QMB) und Sandra Becker (CFO) am 18.12.2023.")])

    comp_short("COMP_Nachhaltigkeitsbericht_2023",
               "Nachhaltigkeitsbericht 2023",
               "Der Nachhaltigkeitsbericht 2023 der Halbreiter Maschinenbau GmbH ist als verkuerzter Bericht in "
               "Anlehnung an die GRI-Standards 2021 und an die CSRD-Vorbereitung erstellt. Die Halbreiter Maschinenbau "
               "GmbH erstellt diesen Bericht freiwillig (CSRD-Pflicht ab Geschaeftsjahr 2025).",
               [("ESG-Kennzahlen",
                 tbl(["Bereich", "Kennzahl", "2023", "2022"],
                     [["Umwelt",  "Energieverbrauch (MWh)",          "1.922", "2.038"],
                      ["Umwelt",  "Scope-1+2 CO2 (t CO2eq)",            "626",   "692"],
                      ["Umwelt",  "Wasserverbrauch (m3)",             "4.840", "5.120"],
                      ["Umwelt",  "Abfall gefaehrlich (t)",            "  9,8", " 11,2"],
                      ["Soziales","Mitarbeiter (FTE)",                  "247",   "236"],
                      ["Soziales","Frauenanteil Gesamt",               "24 %",  "23 %"],
                      ["Soziales","Frauenanteil Fuehrung",             "18 %",  "16 %"],
                      ["Soziales","Unfallquote (LTIFR)",                "4,2",   "5,1"],
                      ["Governance","Compliance-Schulungsquote",     "99 %",  "97 %"],
                      ["Governance","Lieferanten mit CoC-Anerkennung","96 %",  "92 %"]])),
                ("Strategische Hebel 2024",
                 ("list",
                  ["PV-Anlage Halle B Sued (350 kWp).",
                   "Wechsel auf zertifizierten Oekostrom 01.01.2025.",
                   "Diversity-Programm »Frauen in Technik« in Kooperation mit RWTH/FH Koeln.",
                   "Lieferketten-Sorgfaltspflicht: Roll-out SAQ und Risikomatrix."])),
                ("Bestaetigung",
                 "Der Bericht wurde durch Sandra Becker (CFO) am 14. Maerz 2024 freigegeben und vom externen "
                 "Berater EnviCon GmbH (Koeln) auf Plausibilitaet durchgesehen.")])

    comp_short("COMP_Notfallplan_Produktionsausfall",
               "Notfallplan Produktionsausfall",
               "Dieser Notfallplan beschreibt die Massnahmen zur Wiederherstellung des Produktionsbetriebs der "
               "Halbreiter Maschinenbau GmbH bei wesentlichen Stoerungen (Stromausfall, Cyber-Vorfall, "
               "Kritikalitaetsausfall einer Schluesselmaschine, Brand, Pandemie).",
               [("Szenarien und Sofortmassnahmen",
                 tbl(["Szenario", "Sofortmassnahme", "Zust. Funktion"],
                     [["Stromausfall > 4 h",              "USV/NotStrom Server; manuelle Stilllegung Maschinen",
                       "Facility / Produktion"],
                      ["Brand (Halle A/B)",                "Werkfeuerwehr / Feuerwehr Koeln; Evakuierung",
                       "SiGeKo / SiFa"],
                      ["Ausfall PL-500 Hauptlinie",        "Verlagerung in Halle C, Lastausgleich Schichtbetrieb",
                       "Produktionsleitung"],
                      ["Cyber-Vorfall ERP/SAP",            "Schaltschrank IT-Trennung; Krisenstab; SOC-Aktivierung",
                       "IT / Geschaeftsleitung"],
                      ["Pandemie/Hochinzidenz",            "Hygienekonzept; Schichttrennung; Homeoffice Bueros",
                       "HR / GF"]])),
                ("Krisenstab und Eskalation",
                 "Krisenstab: CEO (Vorsitz), CFO, Produktionsleitung, IT-Leitung, HR-Leitung. "
                 "Tagung 24/7-Erreichbarkeit ueber Telefonkette. Krisenstabsraum: Verwaltungsgebaeude 3. OG, R. 3.05. "
                 "Erstreaktion innerhalb 60 Minuten nach Eintritt."),
                ("Wiederanlauf-Zeitziele",
                 ("list",
                  ["IT-Kernsysteme (SAP, AD): RTO < 24 h, RPO < 4 h (siehe IT-Notfallhandbuch).",
                   "Pressenlinie PL-500: Wiederanlauf < 72 h (Ersatzteilbevorratung).",
                   "Foerderbandanlagen: Wiederanlauf < 24 h.",
                   "Verwaltung: Wiederanlauf < 48 h (Notarbeitsplaetze konfiguriert)."])),
                ("Tests",
                 "Mindestens 1 Krisenuebung jaehrlich (Tabletop-Exercise). Letzte Uebung: 14.10.2023, "
                 "Szenario »Cyber-Ransomware«. Lessons-Learned in Massnahmenliste IT/BCM-2023.")])

    comp_short("COMP_Qualitätsprüfbericht_Q4_2023",
               "Qualitaetspruefbericht Q4/2023",
               "Quartalsbericht der Qualitaetssicherung der Halbreiter Maschinenbau GmbH zum 4. Quartal 2023. "
               "Erstellt durch Petra Krueger (Qualitaetsmanagementbeauftragte), freigegeben durch GF.",
               [("Kennzahlen Q4/2023",
                 tbl(["Kennzahl", "Q4/2023", "Q3/2023", "Trend"],
                     [["Reklamationsquote (auf Lieferungen)", "1,2 %", "1,4 %", "↘"],
                      ["8D-Reports erstellt",                  "9",     "11",    "↘"],
                      ["FPY (First Pass Yield) Endmontage",   "94,8 %","93,6 %", "↗"],
                      ["Pruefumfangsabweichung (>1,5σ)",       "0,9 %", "1,1 %", "↘"],
                      ["Lieferantenreklamationen",             "6",     "9",     "↘"]])),
                ("Hauptbefunde",
                 ("list",
                  ["Wiederholungsproblem »Hydraulikleck PL-500 Q3-Charge«: Massnahme Lieferantenwechsel Dichtungsring "
                   "(neuer Lieferant Trelleborg) erfolgreich.",
                   "Servicereklamationen Bosch: deutliche Reduktion durch Premium-SLA und proaktive Wartung.",
                   "Schulungsbedarf bei Endmontage Halle B identifiziert (Loetstellen-Inspektion)."])),
                ("Massnahmen Q1/2024",
                 ("list",
                  ["Implementierung erweitertes SPC-Reporting (PowerBI-Dashboard).",
                   "Schulung »Sichtpruefung Loetstellen« fuer 12 Endmontage-MA.",
                   "Lieferantenaudit Trelleborg (vor Ort) Q1/2024."]))])

    comp_short("COMP_REACH_Verordnung_Dokumentation",
               "REACH-Verordnung – Compliance-Dokumentation 2024",
               "Diese Dokumentation belegt die Einhaltung der REACH-Verordnung (EG) Nr. 1907/2006 durch die "
               "Halbreiter Maschinenbau GmbH. Die Gesellschaft ist nachgeschalteter Anwender (Downstream User) und "
               "Produkthersteller; eine Registrierungspflicht besteht aufgrund Tonnage und Produktart nicht.",
               [("Erfasste Stoffgruppen",
                 tbl(["Stoffgruppe", "Verwendung", "Lieferant", "Beobachtung"],
                     [["Kuehlschmierstoffe", "CNC-Zerspanung",        "Castrol GmbH",    "REACH-konform, SDB v3"],
                      ["Hydraulikoele",      "Pressen / Foerderband", "Shell Deutschland","REACH-konform"],
                      ["Schmierfette",       "Lager, Antriebe",       "SKF / Klueber",   "REACH-konform"],
                      ["Klebstoffe",          "Sondermontage",        "Henkel Loctite",  "REACH-konform"],
                      ["Reinigungsmittel",    "Werkstatt",             "diverse",         "Plausibilitaetspr. quart."]])),
                ("SVHC-Pruefung",
                 "Eine jaehrliche Pruefung der Kandidatenliste fuer besonders besorgniserregende Stoffe (SVHC) "
                 "wird durch Petra Krueger (QMB) durchgefuehrt. Stand 31.01.2024: 240 SVHC auf der Kandidatenliste; "
                 "im MMB-Produktportfolio sind keine SVHC > 0,1 % w/w enthalten (Stand der Stoffinformationen "
                 "Lieferanten)."),
                ("Lieferantenkommunikation",
                 "Lieferanten muessen bei Aenderungen der Stoffzusammensetzung Sicherheitsdatenblaetter (SDB nach "
                 "Anhang II der REACH-VO) zeitnah uebermitteln. Eingangserfassung im DMS, Pruefung durch QMB "
                 "binnen 5 Werktagen."),
                ("Schnittstelle CLP / ECHA",
                 "Kennzeichnung von Gefahrstoffen am Standort gemaess CLP-VO; Stoffkataster im SAP EHS-Modul.")])

    comp_short("COMP_Revisionsplan_2024",
               "Revisions- und Auditplan 2024 (Internal Audit)",
               "Jaehrlicher Revisionsplan der Halbreiter Maschinenbau GmbH (Internal Audit). Die Funktion »Internal "
               "Audit« wird von Anja Lenz (Compliance) wahrgenommen und an Sandra Becker (CFO) sowie die "
               "Geschaeftsfuehrung berichtet.",
               [("Auditplan 2024",
                 tbl(["Nr.", "Audit-Gegenstand", "Quartal", "Auditor"],
                     [["1", "Wareneingang / Wertfluss",                       "Q1", "A. Lenz + ext. Berater"],
                      ["2", "Abrechnung A-Kunden / Forderungsmanagement",     "Q1", "A. Lenz"],
                      ["3", "Lieferantenmanagement / Vendor-File-Risiko",      "Q2", "A. Lenz + S. Braun"],
                      ["4", "IT-Berechtigungen / SAP-Rollen",                 "Q2", "A. Lenz + H. Brinkmann (IT)"],
                      ["5", "Reisekostenabrechnung GF + Vertrieb",            "Q3", "A. Lenz"],
                      ["6", "Exportkontrolle / Sanktionen",                    "Q3", "A. Lenz + ext. BAFA-Berater"],
                      ["7", "Tankvertraege / Fuhrpark",                        "Q4", "A. Lenz"],
                      ["8", "Compliance Communication / Hinweisgebersystem", "Q4", "A. Lenz"]])),
                ("Ressourcen und Berichtsrhythmus",
                 "Audits werden gemaess IDW PS 983 (analog) durchgefuehrt. Berichte gehen an GF/Aufsicht binnen 30 Tagen "
                 "nach Audit-Abschluss; Massnahmen werden im Modul »Internal Audit Tracker« nachverfolgt."),
                ("Themen 2025 (Vorausplanung)",
                 ("list",
                  ["Erstes Pre-Audit zur CSRD-Berichterstattung.",
                   "DSGVO-Audit (Routine alle 2 Jahre).",
                   "ISO 27001-Vorbereitung (ITSec-Reifegrad)."])),
                ("Freigabe",
                 "Plan freigegeben durch Klaus Mueller (CEO) und Sandra Becker (CFO) am 22.01.2024.")])

    comp_short("COMP_Risikoregister_2024",
               "Risikoregister 2024 (Top-10-Risiken)",
               "Das Risikoregister erfasst die wesentlichen Unternehmensrisiken der Halbreiter Maschinenbau GmbH. "
               "Es wird quartalsweise durch das Risk Committee (CEO, CFO, COO/Produktion, IT, Compliance) "
               "ueberpruefst und an den Beirat berichtet.",
               [("Top-10-Risiken",
                 tbl(["Nr.", "Risiko", "Eintritt", "Auswirkung (EUR)", "Steuerung"],
                     [["1",  "Konjunkturrisiko Maschinenbau",          "mittel",   "> 5 Mio.", "Diversifikation Branchen"],
                      ["2",  "Kundenkonzentration (Top-5 = 58 %)",     "mittel",   "> 8 Mio.", "Neukundenakquise Sued/Ost"],
                      ["3",  "Stahlpreisrisiko / Materialinflation",  "hoch",     "> 1,5 Mio.","Preisindexierung Vertrag"],
                      ["4",  "Cyber-Vorfall (ERP/Produktion)",         "mittel",   "> 2 Mio.", "ISMS, BCM, Versicherung"],
                      ["5",  "Stoerung Pressenlinie PL-500",            "niedrig", "> 1 Mio.", "Praeventive Wartung"],
                      ["6",  "Fachkraeftemangel CNC / Konstrukt.",     "hoch",     "> 0,5 Mio.","Ausbildungsoffensive"],
                      ["7",  "Wechselkursrisiko EUR/USD (Trumpf-FX)",  "mittel",   "> 0,3 Mio.","Hedging"],
                      ["8",  "Compliance-Risiko Exportkontrolle CN",   "mittel",  "Reputation",  "Schulungen, BAFA"],
                      ["9",  "Klimaregulierung (CBAM, ETS-Indirekt)",  "mittel",  "> 0,4 Mio.", "ESG-Strategie"],
                      ["10", "Pruefungsrisiko (Patente Mitbewerber)",  "niedrig", "Reputation", "IP-Pflege, FTO-Studien"]])),
                ("Top-Risiko-Massnahmen",
                 ("list",
                  ["Reduktion Konzentrationsrisiko: Aufbau Sales-Pipeline neue Branchen (Lebensmittel-, Pharma-Maschinen).",
                   "Verstaerkte Materialhedging-Vereinbarungen mit Stahllieferanten (Q1/2024).",
                   "Implementierung erweitertes Monitoring SOC (24/7) ueber externen Dienstleister bis 06/2024."])),
                ("Pflege",
                 "Verantwortlich Sandra Becker; Beirat erhaelt quartalsweise Bericht.")])

    comp_short("COMP_UVV_Prüfprotokoll_Elektro_2023",
               "UVV-Pruefprotokoll Elektrische Anlagen 2023",
               "Jaehrliche Pruefung der elektrischen Anlagen und ortsveraenderlichen Betriebsmittel gemaess "
               "DGUV Vorschrift 3 (UVV »Elektrische Anlagen und Betriebsmittel«) und DIN VDE 0701/0702. "
               "Durchgefuehrt durch die Firma Bruni Elektroanlagen GmbH, Koeln (Sachverstaendiger Herr Volker Schmid).",
               [("Pruefumfang",
                 tbl(["Anlage / Bereich", "Anzahl Pruefpunkte", "Bestanden", "Beanstandung"],
                     [["Schaltanlagen Halle A (Trafo-Station Nord)", "184", "184", "0"],
                      ["Schaltanlagen Halle B + C",                  "212", "210", "2"],
                      ["Verwaltungsgebaeude (alle Etagen)",            "98",  "98", "0"],
                      ["Ortsveraenderliche Betriebsmittel (BGV A3)", "742", "722","20"]])),
                ("Festgestellte Beanstandungen",
                 ("list",
                  ["Halle B: zwei Kabeltrommeln mit beschaedigter Isolierung (sofort ausgetauscht).",
                   "Ortsveraenderliche Betriebsmittel: 20 Geraete (Kabeltrommeln, Verlaengerungen) ausgetauscht.",
                   "Schaltanlagen: keine Beanstandungen, naechste Pruefung 11/2024."])),
                ("Schluss",
                 "Nach Abschluss der Massnahmen wurden alle Anlagen und Betriebsmittel als »ohne Beanstandung« "
                 "freigegeben. Pruefplaketten angebracht; Dokumentation im Modul »Eplan PPE« hinterlegt. "
                 "Verantwortlich: Markus Junker (Instandhaltung)."),
                ("Pruefintervall",
                 "Schaltanlagen: 4 Jahre; ortsveraenderliche Betriebsmittel: 12 Monate (Werkstatt/Produktion), "
                 "24 Monate (Buero). Naechste Pruefung im Plan: 11/2024.")])

    comp_short("COMP_Whistleblower_Richtlinie",
               "Hinweisgeber-Richtlinie (HinSchG)",
               "Diese Richtlinie regelt das interne Meldewesen der Halbreiter Maschinenbau GmbH gemaess dem "
               "Hinweisgeberschutzgesetz (HinSchG, in Kraft seit 02.07.2023) sowie der EU-Whistleblower-Richtlinie "
               "(EU 2019/1937). Sie gilt fuer alle Beschaeftigten, Leiharbeitnehmer, Bewerber und ehemalige "
               "Beschaeftigte.",
               [("Geschuetzter Personenkreis und Meldegegenstaende",
                 ("list",
                  ["Geschuetzt: Beschaeftigte, Bewerber, Praktikanten, Leihbeschaeftigte, ehem. Beschaeftigte, Lieferantenmitarbeiter.",
                   "Meldegegenstaende: Verstoesse gegen Strafrecht, Bussgeldrecht, Datenschutz, Arbeitsschutz, Umweltrecht, "
                   "Geldwaesche, Korruption sowie Verstoesse gegen interne Richtlinien."])),
                ("Meldekanal",
                 "Interner Meldekanal: Die Halbreiter Maschinenbau GmbH nutzt das externe webbasierte Hinweisgebersystem "
                 "»EQS Integrity Line«. Meldungen sind anonym moeglich; Identifikation des Hinweisgebers ist "
                 "freiwillig. URL: https://halbreiter-maschinenbau.integrityline.com.\n\n"
                 "Externer Meldekanal: Externe Meldestelle des Bundes (BfJ); Beschaeftigte koennen unabhaengig vom internen Kanal "
                 "die externe Meldestelle waehlen."),
                ("Bearbeitung und Schutz",
                 ("list",
                  ["Bearbeitung durch Compliance-Office (Anja Lenz, primaer; Stellvertretung extern: RA Dr. Hilpert).",
                   "Bestaetigung des Eingangs binnen 7 Tagen; Rueckmeldung zum Bearbeitungsstand spaetestens nach 3 Monaten.",
                   "Schutz vor Repressalien gemaess §§ 36-37 HinSchG; Beweislastumkehr.",
                   "Dokumentation gemaess § 11 HinSchG; Aufbewahrung 3 Jahre."])),
                ("Schulung und Aushang",
                 "Information aller Beschaeftigten ueber Aushang (Schwarzes Brett, Intranet) und im Rahmen der "
                 "jaehrlichen Compliance-Schulungen. Verantwortlich: Compliance / HR.")])


def gen_pruefprotokoll(fname, title, produkt, sn, datum):
    sections = [
        ("Pruefgegenstand und Identifikation",
         tbl(["Merkmal", "Wert"],
             [["Produkt",          produkt],
              ["Seriennummer",     sn],
              ["Pruefdatum",       datum],
              ["Pruefort",         "Halbreiter Maschinenbau GmbH, Endmontage Halle B"],
              ["Pruefer",          "Petra Krueger (QMB) + Stefan Braun (Endabnahme)"],
              ["Anwesende Kunden", "Vertreter Kundenseite (Werksabnahme/SAT)"]])),
        ("Pruefumfang",
         ("list",
          ["Maschinenfunktion: Hauptantrieb, Steuerung, Sicherheitsabschaltung.",
           "Geometrische Pruefung (Toleranzen ISO 8062 CT8) Stichproben.",
           "Sicherheitseinrichtungen: Lichtgitter, Zweihandbedienung, Notaus.",
           "EMV-Test mit Pruefadapter (Hausnorm MMB-EMV-01).",
           "Lasertest / Laserleistung gemaess EN ISO 11553-1 (nur LS-800).",
           "Funktionspruefung Software (Steuerung SINUMERIK ONE, FW V5.3)."])),
        ("Messergebnisse (Auszug)",
         tbl(["Pruefpunkt", "Soll", "Ist", "Toleranz", "Status"],
             [["Presskraft-Aufbauzeit", "< 0,8 s",  "0,72 s",  "± 0,1 s", "i.O."],
              ["Hub-Wiederholgenauigkeit", "± 0,05 mm","0,03 mm","± 0,05 mm", "i.O."],
              ["Schutzhaubenueberwachung", "PL d",     "PL d",    "—",         "i.O."],
              ["Hydraulikdruck",             "260 bar",  "262 bar", "± 5 bar",   "i.O."],
              ["Anschlussleistung Spitze", "< 75 kW",   "71 kW",   "—",         "i.O."]])),
        ("Sicherheitsabnahme",
         "Saemtliche sicherheitsrelevanten Komponenten wurden geprueft und entsprechen den Anforderungen der "
         "EG-Konformitaetserklaerung (Maschinenrichtlinie 2006/42/EG). Risikobeurteilung gemaess EN ISO 12100:2010 "
         "in der Anlagenakte."),
        ("Befunde und Massnahmen",
         "Keine wesentlichen Befunde. Restpunkte (Soft-Releasenotes V5.3.1 nachreichen) werden gemaess "
         "FAT/SAT-Vereinbarung beim Endkunden bei Inbetriebnahme aktualisiert."),
        ("Freigabe und Versandfreigabe",
         signatures("Petra Krueger", "QMB", M["name"],
                    "Stefan Braun", "Endabnahme", M["name"],
                    place="Koeln", date_str_=datum)),
    ]
    write_doc(f"{BASE}/09_Compliance/{fname}.docx", H, title, sections)


def gen_pruefprotokolle():
    gen_pruefprotokoll("Prüfprotokoll_LS800_SN2023001",
                      "Pruefprotokoll Laserschneidanlage LS-800, SN 2023001",
                      "Laserschneidanlage LS-800 (5-Achs-CNC, Faserlaser)", "LS800-SN2023001", "14. Dezember 2023")
    gen_pruefprotokoll("Prüfprotokoll_PL500_SN2023001",
                      "Pruefprotokoll Pressenlinie PL-500, SN 2023001",
                      "Pressenlinie PL-500 (hydraulische Stanzpresse)", "PL500-SN2023001", "26. Oktober 2023")
    gen_pruefprotokoll("Prüfprotokoll_PL500_SN2023002",
                      "Pruefprotokoll Pressenlinie PL-500, SN 2023002",
                      "Pressenlinie PL-500 (hydraulische Stanzpresse)", "PL500-SN2023002", "18. Januar 2024")


def gen_sdb_kuehlschmierstoff():
    sections = [
        ("Identifikation des Stoffes / Gemisches",
         "Produktbezeichnung: Castrol Hyspin AWS 46 (Hydraulikoel-Universaloel).\n"
         "Verwendung: Hydraulikoel fuer industrielle Maschinen (Pressen, Foerderbaender).\n"
         "Lieferant: Castrol Industrial / BP Europa SE, Wittener Strasse 45, 44789 Bochum.\n"
         "Notrufnummer: +49 30 30686790 (Giftnotruf Berlin, 24/7)."),
        ("Moegliche Gefahren",
         ("list",
          ["Einstufung gemaess CLP-VO: nicht als gefaehrlich eingestuft.",
           "Hinweise: kann bei wiederholtem laengeren Hautkontakt zu Reizungen fuehren.",
           "Aerosole/Daempfe vermeiden; bei hoher Erhitzung Brand- und Gesundheitsrisiken."])),
        ("Erste-Hilfe-Massnahmen",
         tbl(["Expositionsweg", "Massnahme"],
             [["Hautkontakt",        "Mit Seife und Wasser reinigen, kontaminierte Kleidung wechseln."],
              ["Augenkontakt",       "Mit reichlich Wasser spuelen, ggf. Augenarzt aufsuchen."],
              ["Verschlucken",       "Nicht zum Erbrechen bringen, sofort Arzt konsultieren."],
              ["Einatmen (Aerosole)","An die frische Luft bringen, Atemwege freihalten."]])),
        ("Brandbekaempfung und Lagerung",
         "Geeignete Loeschmittel: Schaum, Loeschpulver, CO2. Wasserstrahl ungeeignet. Lagerung in geschlossenen "
         "Originalgebinden, geschuetzt vor Hitze und Zuendquellen, in trockenen Raeumen, Lagerklasse 10 (TRGS 510). "
         "Trennlagerung von Oxidationsmitteln."),
        ("Physikalische und chemische Eigenschaften",
         tbl(["Merkmal", "Wert"],
             [["Aggregatzustand bei 20°C", "Fluessig"],
              ["Farbe",                   "Hellgelb"],
              ["Geruch",                   "Schwach mineraloelartig"],
              ["Dichte (15°C)",            "0,876 g/cm3"],
              ["Flammpunkt",               "215 °C (COC)"],
              ["Viskositaet (40°C)",       "46 mm2/s"],
              ["Wassergefaehrdungsklasse", "WGK 2 (wassergefaehrdend)"]])),
        ("Entsorgung und Hinweise",
         "Entsorgung gemaess Abfallschluessel 13 02 05* (Mineraloele) ueber Entsorger Avista Oil AG. "
         "Verpackungen vollstaendig entleert dem Recycling zufuehren. "
         "SDB-Stand: 02/2024, Version 4; gepflegt durch Markus Junker (BBA). "
         "Anwendungsspezifische Risikobeurteilung siehe Gefaehrdungsbeurteilung COMP_Arbeitsschutz."),
    ]
    write_doc(f"{BASE}/09_Compliance/Sicherheitsdatenblatt_Kuehlschmierstoff.docx", H,
              "Sicherheitsdatenblatt – Kuehlschmierstoff Castrol Hyspin AWS 46", sections)


# ════════════════════════════════════════════════════════════════════════════════
# 10. IT-Infrastruktur
# ════════════════════════════════════════════════════════════════════════════════

def it_doc(fname, title, intro, abschnitte):
    sections = [("Zweck und Geltungsbereich", intro)] + list(abschnitte) + [
        ("Verantwortlichkeit, Pflege und Schnittstellen",
         "IT-Leitung: Holger Brinkmann (h.brinkmann@halbreiter-maschinenbau.de). Stellvertretung: Andreas Klein "
         "(Infrastruktur). Pflege dieses Dokumentes erfolgt mindestens jaehrlich oder anlassbezogen bei wesentlichen "
         "Aenderungen der IT-Landschaft, der regulatorischen Anforderungen oder der Geschaeftsprozesse. "
         "Freigabe durch die Geschaeftsfuehrung (Klaus Mueller, CEO). Schnittstellen bestehen zum ISMS-Rahmenwerk "
         "(Richtlinie COMP_007), zum Notfallplan Produktionsausfall (Ordner 09) sowie zum Risikomanagement "
         "(Risikoregister Ordner 09). Verteiler: Geschaeftsfuehrung, Bereichsleiter IT, Bereichsleiter Compliance, "
         "Betriebsrat, Datenschutzbeauftragter. Archivierung im DMS (M-Files) gemaess Aufbewahrungsfristenkatalog "
         "der Halbreiter Maschinenbau GmbH. Rueckfragen zu Inhalt oder Anwendung an it-support@halbreiter-maschinenbau.de."),
    ]
    write_doc(f"{BASE}/10_IT_Infrastruktur/{fname}.docx", H, title, sections)


def gen_it_docs():
    it_doc("IT_Backup-Restore-Konzept",
           "Backup- und Restore-Konzept",
           "Dieses Konzept beschreibt die Sicherung der IT-Systeme der Halbreiter Maschinenbau GmbH. Geltung fuer "
           "Server-Systeme, Datenbanken, Filer und Benutzerendgeraete (M365). Es ergaenzt das IT-Notfallhandbuch "
           "und das ISMS-Rahmenwerk.",
           [("Strategie",
             ("list",
              ["3-2-1-Strategie: 3 Kopien, 2 Speichermedien, 1 Off-Site.",
               "Differentielle Sicherung taeglich, vollstaendige Sicherung woechentlich.",
               "Aufbewahrung: 30 Tage Tagessicherung, 12 Monate Monatssicherung, 7 Jahre Jahressicherung (steuerrelevant)."])),
            ("Systeme und SLAs",
             tbl(["System", "Backup-Typ", "Frequenz", "RTO", "RPO"],
                 [["SAP ECC/S4HANA",   "Online HANA SystemReplication + Veeam", "kontinuierlich", "4 h",  "15 min"],
                  ["Active Directory", "Veeam VM-Backup",                       "4x taeglich",     "2 h",  "6 h"],
                  ["File Server",      "Veeam / Tape (LTO-8)",                  "taeglich",        "8 h", "24 h"],
                  ["Salesforce (Cloud)","OwnBackup",                             "taeglich",        "8 h", "24 h"],
                  ["Microsoft 365",    "Veeam Cloud Connect M365",              "taeglich",        "8 h", "24 h"]])),
            ("Tests",
             "Wiederherstellungstests werden quartalsweise stichprobenartig durchgefuehrt (Restore zu Testumgebung). "
             "Letzter Test 09.02.2024 erfolgreich (SAP HANA + AD). Naechster Test Q2/2024 (File-Server)."),
            ("Off-Site und Geo-Redundanz",
             "Off-Site-Replikation in Rechenzentrum Frankfurt (Equinix FR8) via dediziertes 1 Gbit/s. "
             "Tape-Saetze (Quartalsende) ausgelagert beim Dienstleister Iron Mountain.")])

    it_doc("IT_Cloud_Strategie_2024_2026",
           "Cloud-Strategie 2024-2026",
           "Die Cloud-Strategie der Halbreiter Maschinenbau GmbH definiert das Zielbild und den Migrationspfad fuer "
           "die Cloud-Nutzung in den Jahren 2024 bis 2026. Sie wurde durch die Geschaeftsfuehrung am 14. Januar 2024 "
           "verabschiedet.",
           [("Zielbild (»Cloud Smart«)",
             ("list",
              ["»Cloud Smart« anstelle »Cloud First«: pro Anwendung wird situativ entschieden.",
               "Multi-Cloud bevorzugt: Azure (M365 + IaaS DACH), Salesforce (CRM/Service), SAP (S/4-Hyperscaler ab 2026 evaluierend).",
               "On-Premise bleibt fuer Produktions-OT, Engineering-Daten (PDM) und sensible IP.",
               "Verschluesselung: Kundenschluessel (BYOK) wo verfuegbar."])),
            ("Migrationsroadmap",
             tbl(["Phase", "Zeitraum", "Massnahme"],
                 [["1. Foundation",    "Q1-Q2/2024", "Azure Landing Zone, Conditional Access, Defender for Cloud"],
                  ["2. Produktivitaet", "Q2-Q3/2024", "Vollmigration M365 E5 (inkl. Defender, Purview)"],
                  ["3. Branch & DR",   "Q3-Q4/2024", "Azure VPN, DR-Lite fuer SAP via ASR"],
                  ["4. SAP Roadmap",   "2025-2026",  "Rise with SAP Optionspruefung mit BDO"],
                  ["5. Datenarchitektur","2026",     "Data Fabric Pilot (Synapse / Fabric)"]])),
            ("Governance",
             ("list",
              ["Cloud Center of Excellence (CCoE) ab Q2/2024 (Holger Brinkmann + 2 Architekten).",
               "Policies: Naming, Tagging, Cost Mgmt, FinOps-Reporting monatlich.",
               "Sicherheitskontrollen: ISO/IEC 27017 + 27018 als Referenz.",
               "Datenklassifikation: Microsoft Purview (4 Klassen) verbindlich."])),
            ("Budget",
             "Investitionsplanung 2024: 280 TEUR (CapEx) + 420 TEUR (OpEx). Konsolidierte Cost-Optimierung in 2025 "
             "(Ziel: -10 % Run-Kosten Identity/M365).")])

    it_doc("IT_Disaster_Recovery_Plan_2024",
           "Disaster-Recovery-Plan 2024",
           "Der DRP beschreibt die Wiederherstellung der kritischen IT-Systeme der Halbreiter Maschinenbau GmbH nach "
           "einem katastrophalen Ausfall (Brand, Cyber-Vorfall, Total-Hardware-Ausfall). Er stuetzt sich auf das "
           "IT-Notfallhandbuch (BCM) und das Backup-Restore-Konzept.",
           [("Szenarien und Wiederanlauf",
             tbl(["Szenario", "RTO Ziel", "RPO Ziel", "Massnahme"],
                 [["Hardware-Ausfall Server",       "4 h",  "15 min", "Failover Veeam Replikation"],
                  ["Brand RZ Hauptstandort",        "24 h",  "1 h",   "Failover RZ Frankfurt (Equinix FR8)"],
                  ["Cyber-Vorfall (Ransomware)",   "48 h",  "24 h",  "Restore aus Air-Gap-Backup + Forensik"],
                  ["Verlust Salesforce-Daten",     "8 h",  "24 h",  "OwnBackup Restore"],
                  ["Verlust SAP HANA",              "4 h",  "15 min", "HANA System Replication Failover"]])),
            ("Krisenstab und Eskalation",
             "Krisenstab IT: Holger Brinkmann (IT-Leitung, Vorsitz), Andreas Klein (Infrastruktur), "
             "Dr. Marius Pohl (Anwendungen / SAP), Jens Decker (Security/SOC). Erste Reaktion innerhalb "
             "30 Minuten. Eskalation an Geschaeftsfuehrung binnen 1 Stunde."),
            ("Externe Dienstleister",
             ("list",
              ["RZ-Betrieb sekundaer: Equinix FR8 (Frankfurt), Datacenter-Vertrag.",
               "SOC / Incident Response: SECUINFRA GmbH (Berlin), 24/7-Dienstleistung.",
               "Forensik / IRP: HiSolutions AG (Berlin)."])),
            ("Tests",
             "Mindestens 1 vollstaendiger Failover-Test pro Jahr. Letzter Test 14.10.2023 (Szenario Ransomware), "
             "Ergebnis erfolgreich mit RTO 41 h. Lessons-Learned: Verbesserung Restore-Sequenz SAP, "
             "Anschaffung Hardware-Air-Gap Bank.")])

    it_doc("IT_ISMS-Richtlinie_Passwortmanage",
           "ISMS-Richtlinie Passwortmanagement",
           "Diese Richtlinie regelt den Umgang mit Passwoertern fuer interne IT-Systeme der Halbreiter Maschinenbau "
           "GmbH gemaess der ISMS-Rahmenrichtlinie (COMP_007). Sie orientiert sich an ISO/IEC 27001:2022 "
           "Annex A.9.4 und an BSI-Grundschutzbaustein ORP.4.",
           [("Anforderungen an Passwoerter",
             ("list",
              ["Mindestlaenge 12 Zeichen, mindestens 3 von 4 Zeichenklassen (Klein-/Grossbuchstaben, Zahlen, Sonderzeichen).",
               "Keine Trivialpassworte (Listen NIST CommonPassword aktiv).",
               "Passwort-Historie 6 Eintraege; kein Recycling.",
               "Wechsel: bei privilegierten Konten alle 90 Tage; bei Standard-Konten anlassbezogen.",
               "Passwort-Manager (Keeper Security Enterprise) Pflicht fuer admin-Konten."])),
            ("Multi-Faktor-Authentifizierung",
             "MFA verpflichtend fuer alle Cloud-Anwendungen (Azure AD Conditional Access), externe Zugriffe (VPN), "
             "privilegierte Konten (PIM/PAM). Faktoren: Microsoft Authenticator App oder FIDO2-Token (YubiKey)."),
            ("Service-Konten",
             ("list",
              ["Mindestlaenge 24 Zeichen, kein Wechsel zwingend, aber jaehrliche Pruefung.",
               "Hinterlegung im Privileged Access Vault (CyberArk).",
               "Verwendung nur ueber Vault-gesteuerten Workflow; Audit-Logging aktiv."])),
            ("Schulung und Kontrolle",
             "Pflichtmodul »Passwort- und Identitaetssicherheit« im Lawpilots-eLearning, jaehrlich verpflichtend. "
             "Stichproben durch Internal Audit (Anja Lenz) quartalsweise. Verstoesse werden im IT-Ticketsystem "
             "(ServiceNow) als Security-Event aufgenommen.")])

    it_doc("IT_IT-Notfallhandbuch",
           "IT-Notfallhandbuch (BCM)",
           "Das IT-Notfallhandbuch konsolidiert die Vorgehensweisen bei Sicherheitsvorfaellen und Ausfaellen der "
           "IT-Systeme der Halbreiter Maschinenbau GmbH gemaess BSI-Standard 200-4 (Business Continuity Management). "
           "Es ergaenzt den Notfallplan Produktionsausfall (Ordner 09) sowie den DRP (10_IT).",
           [("Vorfallklassen",
             tbl(["Klasse", "Beschreibung", "Reaktionszeit"],
                 [["1 – kritisch", "Komplettausfall ERP oder Werkstattnetz", "< 30 min"],
                  ["2 – hoch",     "Ausfall Einzelanwendung mit hoher Wirkung", "< 2 h"],
                  ["3 – mittel",   "Funktionseinschraenkung",                "< 8 h"],
                  ["4 – niedrig",  "Routine-Fehler ohne Geschaeftsstoerung","SLA Std."]])),
            ("Rollen und Verantwortung",
             ("list",
              ["IT-Leitung (Holger Brinkmann): Krisenstab-Vorsitz IT.",
               "SOC / Security (Jens Decker, Stv. extern SECUINFRA): Erstanalyse, Forensik-Triage.",
               "Anwendungsteam (Dr. Marius Pohl): SAP-/Salesforce-Spezifika.",
               "Infrastruktur (Andreas Klein): Netz/Hardware/Backup.",
               "HR (Petra Hartmann): Kommunikation an Mitarbeiter."])),
            ("Standardprozesse",
             ("list",
              ["Detection: SOC-Alert, Helpdesk-Eskalation, Anomalie-Erkennung.",
               "Containment: Netzsegmentierung, betroffene Accounts disablen.",
               "Eradication: Forensische Untersuchung, Patchen, Wiederaufsetzen.",
               "Recovery: Restore aus Backup, Validierung, Wiederinbetriebnahme.",
               "Post-Incident-Review: schriftliches Lessons-Learned binnen 14 Tagen."])),
            ("Uebungen",
             "Tabletop-Uebung mindestens jaehrlich (zuletzt 14.10.2023). Naechste Uebung: 06/2024 "
             "Szenario »Insider-Threat / Daten-Exfiltration«.")])

    it_doc("IT_IT-Sicherheitskonzept_2024",
           "IT-Sicherheitskonzept 2024",
           "Das IT-Sicherheitskonzept beschreibt das Schutzniveau, die Massnahmen und die Verantwortlichkeiten "
           "fuer die Informationssicherheit der Halbreiter Maschinenbau GmbH. Es ist Teil des ISMS-Rahmenwerkes und "
           "orientiert sich an ISO/IEC 27001:2022 sowie an den BSI-Grundschutz-Bausteinen.",
           [("Schutzbedarf",
             tbl(["Kategorie", "Vertraulichkeit", "Integritaet", "Verfuegbarkeit"],
                 [["SAP ERP / Finance",      "hoch",     "sehr hoch", "hoch"],
                  ["CAD / PDM Engineering",  "sehr hoch","hoch",      "hoch"],
                  ["Werkstattnetz (OT)",     "mittel",   "sehr hoch", "sehr hoch"],
                  ["E-Mail / M365",          "hoch",     "hoch",      "mittel"],
                  ["Salesforce (Kundendaten)","hoch",     "hoch",      "mittel"]])),
            ("Kontrollen",
             ("list",
              ["Identity: Azure AD, Conditional Access, MFA Pflicht.",
               "Endpoint: Microsoft Defender for Endpoint + EDR (Defender XDR).",
               "Netz: Segmentierung IT/OT (Firewall Fortinet), DMZ fuer Remote Service.",
               "Daten: BitLocker, Purview-Klassifizierung, DLP-Policies.",
               "Logging: Sentinel SIEM mit 1-Jahres-Retention, Anbindung an SECUINFRA-SOC."])),
            ("Awareness und Schulung",
             "Verpflichtende eLearning-Module (Phishing, Passwort, Datenschutz). Jaehrliche Phishing-Tests "
             "(zuletzt 03/2024: Klickquote 6,8 %, Ziel < 5 %). Spezialschulungen Engineering (CAD-IP-Schutz) "
             "halbjaehrlich."),
            ("Roadmap 2024",
             ("list",
              ["ISO 27001-Zertifizierung Vorpruefung Q4/2024 (Audit-Partner DEKRA).",
               "Erweiterung SOC-Service auf 24/7 ab Q2/2024 (SECUINFRA).",
               "Rollout PAM (CyberArk Privilege Cloud) Q3/2024.",
               "Network Access Control (NAC) Q4/2024."]))])

    it_doc("IT_Netzwerkdokumentation_2024",
           "Netzwerkdokumentation 2024",
           "Die Netzwerkdokumentation beschreibt die IT- und OT-Netzwerkarchitektur der Halbreiter Maschinenbau GmbH "
           "am Standort Industriestrasse 12, Koeln. Sie wird zusaetzlich detailliert im Network-Management-System "
           "(Auvik) gefuehrt; das vorliegende Dokument fasst die Zielarchitektur zusammen.",
           [("Standorte und WAN",
             ("list",
              ["Hauptstandort Industriestrasse 12, Koeln: 2x Glasfaser 1 Gbit/s (NetCologne + Telekom Business).",
               "Aussenlager Niehler Strasse 88: 1x Glasfaser 200 Mbit/s + LTE-Backup.",
               "Cloud-Anbindung: 2x ExpressRoute 1 Gbit/s zu Azure (Equinix FR8 / FR6)."])),
            ("Segmentierung (VLAN/Subnets)",
             tbl(["VLAN", "Zweck", "Subnet", "Firewall-Zone"],
                 [["10 ", "Server (DC, SAP, AD)",      "10.10.10.0/24",  "TRUST"],
                  ["20 ", "Clients Buero",             "10.10.20.0/22",  "TRUST"],
                  ["30 ", "OT Halle A (CNC, Pressen)","10.10.30.0/24",  "OT-A"],
                  ["31 ", "OT Halle B (Laser, FB)",   "10.10.31.0/24",  "OT-B"],
                  ["40 ", "WLAN Gaeste",               "10.10.40.0/23",  "GUEST"],
                  ["50 ", "VPN-User Remote",          "10.10.50.0/24",  "VPN"],
                  ["99 ", "DMZ (Web, Service)",       "10.10.99.0/24",  "DMZ"]])),
            ("Komponenten",
             ("list",
              ["Firewalls: Fortinet 600F (HA-Cluster), 2x; Fortinet 100F fuer Aussenlager.",
               "Switching: Cisco Catalyst 9300 Core (Stack), Catalyst 9200 Access.",
               "WLAN: Cisco Catalyst 9100 (28 APs Wi-Fi 6).",
               "DNS/DHCP: Infoblox vNIOS."])),
            ("Pflege",
             "Topologie-Aktualisierung jaehrlich; Auvik-Discovery automatisch. Letzte Aktualisierung 22.01.2024.")])

    it_doc("IT_Penetrationstest-Bericht_2023",
           "Penetrationstest-Bericht 2023",
           "Ergebnisse des externen Penetrationstests bei der Halbreiter Maschinenbau GmbH, durchgefuehrt durch "
           "HiSolutions AG (Berlin) im Zeitraum 02.-13. Oktober 2023. Auftragsumfang: Black-Box-Test externer "
           "Perimeter sowie Grey-Box-Test wichtiger Web- und SAP-Schnittstellen. Methode: OWASP, OSSTMM, BSI.",
           [("Scope",
             ("list",
              ["Externer Perimeter (10 oeffentliche IPs, 4 Web-Anwendungen).",
               "Salesforce-Integrationen (REST API).",
               "SAP Fiori Launchpad (extern erreichbar).",
               "VPN-Gateway (Fortinet FortiClient + SSL-VPN).",
               "WLAN-Sicherheit am Standort Koeln (vor Ort)."])),
            ("Befundsverteilung",
             tbl(["Kategorie", "Anzahl", "Beispiele"],
                 [["Critical",       "0", "—"],
                  ["High",           "2", "veraltete TLS-Cipher; Default-Credentials Drucker"],
                  ["Medium",         "5", "Information Disclosure, fehlende CSP-Header"],
                  ["Low",            "7", "veraltete Bibliotheken, schwache Cookie-Flags"],
                  ["Informational", "12", "Best-Practice-Empfehlungen"]])),
            ("Massnahmenstatus",
             "Alle High-Findings binnen 14 Tagen behoben. Medium-Findings bis Ende Q4/2023 abgeschlossen. "
             "Low/Informational werden im Backlog des IT-Sicherheitsteams gepflegt und in den naechsten "
             "Patch-Zyklen abgearbeitet."),
            ("Empfehlungen",
             ("list",
              ["Einfuehrung eines kontinuierlichen Schwachstellenscans (Tenable Nessus, geplant Q1/2024).",
               "Aufbau Bug-Bounty-Programm fuer ausgewaehlte Anwendungen ab 2025.",
               "Erweiterung der Penetrationstests auf OT-Bereich (Werkstattnetz) in 2024."])),
            ("Bewertung",
             "Gesamtbewertung des Pentests: »angemessen mit Verbesserungspotenzial«; keine kritischen Befunde, "
             "rasche Reaktionszeit auf High-Findings. Re-Test fuer Q3/2024 beauftragt.")])

    it_doc("IT_Software-Inventar_2024",
           "Software-Inventar 2024",
           "Das Software-Inventar dokumentiert die zentral verwalteten Software-Lizenzen, Subscriptions und Open-Source-"
           "Komponenten der Halbreiter Maschinenbau GmbH. Pflege erfolgt automatisiert (Microsoft Intune, Cherwell) "
           "ergaenzt durch manuelle Pflege der Spezialanwendungen.",
           [("Hauptanwendungen",
             tbl(["Anwendung", "Hersteller", "Lizenztyp", "Anzahl"],
                 [["SAP S/4HANA (Module FI, CO, MM, SD, PP, QM)", "SAP SE",            "Named-User + Engines", "196 User"],
                  ["Salesforce Sales + Service Cloud",            "salesforce.com",     "Subscription",         " 50 User"],
                  ["SINUMERIK ONE",                              "Siemens AG",         "Runtime + Wartung",    " 12 Lizenzen"],
                  ["AutoCAD Mechanical 2024",                    "Autodesk",           "Subscription",         " 28 User"],
                  ["SOLIDWORKS Premium 2024",                    "Dassault Systèmes",  "Stand-alone",          " 18 Floating"],
                  ["Microsoft 365 E5",                            "Microsoft",          "Subscription",         "240 User"],
                  ["Veeam Backup & Replication",                 "Veeam",              "Subscription",         "  1 Lizenz (Site)"],
                  ["Defender XDR + Sentinel",                    "Microsoft",          "Subscription",         "240 User"]])),
            ("Compliance",
             ("list",
              ["Jaehrliche Lizenzpruefung (Software Asset Management) durch Anja Lenz.",
               "Audit-Spiegel SAP intern (Engine-Nutzung); Re-Audit alle 24 Monate.",
               "Open-Source-Komponenten: SBOM-Pflege fuer eigene Embedded-Software (PL-500, FB-200)."])),
            ("Roadmap",
             ("list",
              ["Migration AutoCAD Mechanical 2024 -> 2025 Q2/2024.",
               "Pilot M365 Copilot Q3/2024 (40 Pilotanwender).",
               "Evaluierung Power Platform fuer Service-App Q4/2024."])),
            ("Datenhaltung",
             "Software-Inventar wird in Cherwell Asset Mgmt gefuehrt. Schnittstelle zu SAP CO (Kostenstellen).")])


# ════════════════════════════════════════════════════════════════════════════════
# 11. STRATEGIE
# ════════════════════════════════════════════════════════════════════════════════

def gen_strat_beirat():
    sections = [
        ("Sitzungsdaten",
         tbl(["Merkmal", "Wert"],
             [["Sitzung",            "Q1/2024 (Sitzung Nr. 2024-01)"],
              ["Ort",                 "Halbreiter Maschinenbau GmbH, Verwaltungsgebaeude, R. 3.05"],
              ["Datum",               "14. Maerz 2024"],
              ["Beginn / Ende",       "09:30 / 13:45 Uhr"],
              ["Vorsitz Beirat",      "Dr. Hans-Joachim Lemke (ext. Beirat)"],
              ["Protokoll",            "Anja Lenz"]])),
        ("Anwesende",
         ("list",
          ["Beirat: Dr. Hans-Joachim Lemke (Vorsitz), Prof. Dr. Carla Brandt (Hochschule Niederrhein), Dipl.-Kfm. Heinz Roettgen (ehem. Schuler AG)",
           "Geschaeftsfuehrung: Klaus Mueller (CEO), Sandra Becker (CFO)",
           "Gaeste: Dr.-Ing. Sabine Hoff (Konstruktion, TOP 4), Stefan Braun (Einkauf, TOP 5)"])),
        ("Tagesordnung",
         ("list",
          ["TOP 1 – Begruessung und Annahme des Protokolls Q4/2023",
           "TOP 2 – Bericht der Geschaeftsfuehrung (Lage, KPIs Q1/2024)",
           "TOP 3 – Strategischer Lagebericht 2024-2026",
           "TOP 4 – Innovationsroadmap (PL-500 Rev. 4, KI-Edge)",
           "TOP 5 – Materialinflation / Hedging-Strategie",
           "TOP 6 – Sonstiges"])),
        ("Wesentliche Beschluesse",
         ("list",
          ["Annahme des Protokolls Q4/2023 (einstimmig).",
           "Zur Kenntnisnahme: Lagebericht Q1/2024; Umsatzplan 2024 i.H.v. 52,5 Mio. EUR bestaetigt.",
           "Empfehlung an die GF: Vorbereitung CSRD-Berichterstattung mit Zieltermin 2025 weiterfuehren.",
           "Empfehlung: Vertiefung der Hedging-Vereinbarungen mit Stahllieferanten (Q2/2024).",
           "Naechste Sitzung: 13. Juni 2024."])),
        ("Vorlagen",
         tbl(["Nr.", "Vorlage", "Erstellt von"],
             [["V-2024-01", "Lagebericht Q1/2024 (KPIs, Auftragseingang, Liquiditaet)", "Sandra Becker"],
              ["V-2024-02", "Strategielageplan 2024-2026 (SWOT, Wettbewerb)",            "Klaus Mueller"],
              ["V-2024-03", "Innovationsroadmap PL-500 Rev. 4 / KI-Edge",                "Sabine Hoff"],
              ["V-2024-04", "Hedging-Konzept Stahl",                                     "Stefan Braun"]])),
        ("Unterschrift",
         signatures("Dr. Hans-Joachim Lemke", "Vorsitz Beirat", "Beirat MMB",
                    "Klaus Mueller", "Geschaeftsfuehrer", M["name"],
                    place="Koeln", date_str_="14. Maerz 2024")),
    ]
    write_doc(f"{BASE}/11_Strategie_Planung/STRAT_Beiratssitzung_Protokoll_2024.docx", H,
              "Protokoll Beiratssitzung Q1/2024", sections, confidential=True)


def gen_strat_digital():
    sections = [
        ("Zweck und Geltungsbereich",
         "Der Digitalisierungsbericht Q2/2024 fasst den Stand der Digitalisierungsinitiative »MMB Digital 2026« "
         "der Halbreiter Maschinenbau GmbH zusammen und dokumentiert die im Quartal abgeschlossenen sowie geplanten "
         "Massnahmen."),
        ("Programmstruktur",
         tbl(["Cluster", "Initiative", "Status", "Ziel"],
             [["1. Verwaltung",      "M365 E5 Vollmigration", "abgeschlossen",       "Produktivitaet, Sicherheit"],
              ["1. Verwaltung",      "Einfuehrung Personio (HR)", "abgeschlossen",   "Self-Service Mitarbeiter"],
              ["2. Engineering",     "PDM-Konsolidierung SOLIDWORKS","in Arbeit",    "CAD-Single-Source"],
              ["2. Engineering",     "Digital Twin Pilot PL-500","Pilot Q3/2024",   "Service / Predictive"],
              ["3. Produktion",      "OT/IT-Segmentierung",     "abgeschlossen",     "OT-Sicherheit"],
              ["3. Produktion",      "MES-Modul Halle B",        "in Arbeit",        "Transparenz"],
              ["4. Service",         "Customer-Portal v2",       "Beta Q3/2024",     "Self-Service Kunden"],
              ["4. Service",         "Predictive Maintenance Pilot","gestartet",   "Reduktion Stoerungen"]])),
        ("Kennzahlen Q2/2024",
         ("list",
          ["Digitalisierungs-Investitionen YTD: 0,68 Mio. EUR (Plan 1,2 Mio. EUR im Jahr).",
           "Anteil Self-Service Service-Tickets ueber Portal: 32 % (Vorjahr 18 %).",
           "Mean Time To Resolution Service-Tickets: 7,2 Tage (-1,8 Tage vs. Vorjahr).",
           "Aktive Pilotkunden Predictive Maintenance: 6 (Ziel 2024: 10)."])),
        ("Risiken / Abhaengigkeiten",
         ("list",
          ["Verzoegerungen MES-Modul Halle B aufgrund Lieferanten-Engpass (PSI Software AG).",
           "Personalengpass im Engineering bremst PDM-Konsolidierung.",
           "Cybersicherheitsrisiken durch ausgeweitete Cloud-Schnittstellen; Kontrolle ueber SOC."])),
        ("Naechste Schritte",
         ("list",
          ["Go-Live MES Modul Halle B verschoben auf Q4/2024.",
           "Digital Twin Pilot PL-500 mit RWTH Aachen Q3/2024.",
           "Customer-Portal v2 General-Release Q4/2024."])),
        ("Freigabe",
         "Bericht freigegeben durch Klaus Mueller (CEO) und Holger Brinkmann (IT) am 15. Juli 2024."),
    ]
    write_doc(f"{BASE}/11_Strategie_Planung/STRAT_Digitalisierungsbericht_Q2_2024.docx", H,
              "Digitalisierungsbericht Q2/2024", sections)


def gen_strat_energie():
    sections = [
        ("Zweck",
         "Diese Analyse fasst den Energieverbrauch der Halbreiter Maschinenbau GmbH im Berichtsjahr 2023 zusammen und "
         "ordnet ihn in die Mehrjahresentwicklung ein. Sie dient als Grundlage fuer Investitionsentscheidungen "
         "im Rahmen des Energiemanagementsystems (DIN EN ISO 50001) und der Klimastrategie."),
        ("Mehrjahresvergleich",
         tbl(["Energieart", "2021", "2022", "2023", "Veraenderung 23/22"],
             [["Strom (MWh)",                   "1.348", "1.226", "1.180", "-3,8 %"],
              ["Erdgas (MWh)",                  "  912",   "812",   "742", "-8,6 %"],
              ["Diesel Werkfuhrpark (l)",       "12.420","11.840","10.620", "-10,3 %"],
              ["Wasser (m3)",                   "5.640", "5.120", "4.840", "-5,5 %"],
              ["Energiekosten gesamt (TEUR)",   "354",   "362",   "318",  "-12,2 %"]])),
        ("Massnahmen mit Wirkung",
         ("list",
          ["LED-Umruestung Halle A (Phase 2), Einsparung 42 MWh/a.",
           "Druckluft-Leckage-Programm, Einsparung 28 MWh/a.",
           "Optimierung Heizungssteuerung Verwaltungsgebaeude, 55 MWh/a.",
           "Erhoehung Effizienz Wasserkreislauf Kuehlung, -8 % Wasser."])),
        ("Verbrauchsprofile",
         tbl(["Bereich", "Stromanteil 2023"],
             [["CNC-Zerspanung Halle A",   "32 %"],
              ["Laserschneiden / Pressen Halle B","41 %"],
              ["Druckluft (Kompressorstation)",  "9 %"],
              ["Beleuchtung",                     "6 %"],
              ["Verwaltungsgebaeude",            "8 %"],
              ["Sonstige (Lager, Aussen)",        "4 %"]])),
        ("Ausblick 2024",
         ("list",
          ["Inbetriebnahme PV-Anlage Halle B Sued (350 kWp) – Eigenverbrauch erwartet 280 MWh/a.",
           "Wechsel auf zertifizierten Oekostrom (Naturstrom AG) zum 01.01.2025.",
           "Pilot Spitzenlastmanagement gemeinsam mit RWE Trading (Demand Response).",
           "Erweiterung der Energie-Submeter um 6 weitere Messpunkte (CNC-Linien)."])),
        ("Freigabe",
         "Analyse freigegeben durch Sandra Becker (CFO) und Markus Junker (Energiemanagement) am "
         "22.02.2024. Verteiler: GF, Beirat, Betriebsrat."),
    ]
    write_doc(f"{BASE}/11_Strategie_Planung/STRAT_Energieverbrauchsanalyse_2023.docx", H,
              "Energieverbrauchsanalyse 2023", sections)


def gen_strat_intl():
    sections = [
        ("Strategischer Hintergrund",
         "Die Roadmap Internationalisierung 2025-2027 beschreibt die geplante geografische Ausweitung der "
         "Vertriebs- und Servicestrukturen der Halbreiter Maschinenbau GmbH. Der bisherige Auslandsanteil von rund "
         "32 % am Umsatz soll bis 2027 auf 42 % erhoeht werden. Schwerpunkte: Europa (Sued, CEE), Asien (CN, IN), USA."),
        ("Phasenplan",
         tbl(["Phase", "Zeitraum", "Massnahme"],
             [["1", "Q1-Q4 2025", "Aufbau Vertretungsbuero CZ (Brno) mit 2 Sales/Service-FTE"],
              ["2", "Q2-Q4 2025", "Service-Stuetzpunkt Italien (Mailand) via Distributor M-Tec srl"],
              ["3", "Q1-Q2 2026", "Vertriebsbuero China (Shanghai) ueber Joint-Venture mit lokalem Partner"],
              ["4", "Q3 2026",   "Erschliessung indischer Markt (Pune) ueber Distributor Schunk India"],
              ["5", "Q1-Q3 2027", "USA Vertriebskooperation (Joint Sales) mit US-Servicepartner"]])),
        ("Zielkennzahlen",
         tbl(["Kennzahl", "2024 (Ist Plan)", "2025e", "2026e", "2027e"],
             [["Umsatz Gesamt",            "52,5",  "57,0",  "62,0",  "68,0", ],
              ["davon Auslandsanteil",      "33 %",  "36 %",  "39 %",  "42 %"],
              ["Auslaendische Mitarbeiter", "8",     "14",    "22",    "30"],
              ["Anzahl Distributoren",       "5",     "8",     "12",    "15"]])),
        ("Risiken und Mitigation",
         ("list",
          ["Politische / regulatorische Risiken CN / IN: enge Begleitung durch Compliance + BAFA.",
           "Fachkraefte-Engpass: gezielte Recruiting-Kampagne ab Q4/2024.",
           "Waehrungsrisiko: Erweiterung des Hedging-Programms in Abstimmung mit Deutsche Bank.",
           "Rechtsrisiko Auslandsgesellschaften: lokale Anwaelte und Joint-Venture-Strukturen pruefen."])),
        ("Naechste Schritte",
         ("list",
          ["Q3/2024: Investmentvorlage »CZ-Buero Brno« an Beirat.",
           "Q4/2024: Auswahl Joint-Venture-Partner China (Shortlist 3).",
           "Q1/2025: Erste Stellenausschreibungen Vertretungsbuero CZ."])),
        ("Freigabe",
         "Beirat hat die Roadmap am 14.03.2024 zur Kenntnis genommen und befuerwortet. "
         "Detailplanung erfolgt durch Klaus Mueller (CEO) gemeinsam mit Sandra Becker (CFO)."),
    ]
    write_doc(f"{BASE}/11_Strategie_Planung/STRAT_Roadmap_Internationalisierung_2025.docx", H,
              "Roadmap Internationalisierung 2025-2027", sections, confidential=True)


def gen_strat_swot():
    sections = [
        ("Zweck",
         "Die SWOT-Analyse 2024 dient als Grundlage fuer die strategische Planung der Halbreiter Maschinenbau GmbH "
         "und fliesst in die Beiratssitzung Q1/2024 sowie in die Roadmap Internationalisierung 2025-2027 ein. "
         "Aktualisierung erfolgt jaehrlich oder bei wesentlichen Veraenderungen des Marktumfeldes."),
        ("Strengths (Staerken)",
         ("list",
          ["Hohe Produktqualitaet (Kundenzufriedenheit 4,4/5; siehe Ordner 04).",
           "Patentierte Werkzeugschnellwechsel-Technologie PL-500 (Differenzierung im Wettbewerb).",
           "Stabile Top-5-Kundenbasis mit langfristigen Rahmenvertraegen (58 % Umsatz).",
           "Engagiertes Engineering-Team und Netzwerk zur RWTH Aachen (Lehrstuhl PtU).",
           "Solide Eigenkapitalquote 38,4 %; gute Bonitaet bei Hausbank Deutsche Bank."])),
        ("Weaknesses (Schwaechen)",
         ("list",
          ["Kundenkonzentration Top-5 (58 %) erhoeht Abhaengigkeit.",
           "Auslandsanteil mit 32 % unter Branchendurchschnitt.",
           "Verteilte Engineering-Datenhaltung (PDM-Konsolidierung erst in Arbeit).",
           "Fachkraeftesituation CNC-Zerspaner / Mechatroniker angespannt.",
           "Begrenzte digitale Service-Angebote (Customer-Portal v1)."])),
        ("Opportunities (Chancen)",
         ("list",
          ["Wachstumsmaerkte Asien (Industrie 4.0) und CEE (Reshoring).",
           "KI-/Edge-Loesungen (mit RWTH) als Premium-Differenzierung.",
           "Service-Geschaeft (Predictive Maintenance) ausbauen.",
           "Foerderprogramme BMWK/ZIM fuer KI-Pressen.",
           "Energie-Effizienz / Eigenstrom-PV als Kosten- und Marketingvorteil."])),
        ("Threats (Risiken)",
         ("list",
          ["Konjunkturschwaeche im Maschinenbau, Auftragseingang volatil.",
           "Stahl- und Energiepreis-Volatilitaet.",
           "Asiatische Wettbewerber mit aggressiver Preispolitik (insb. CN-Hersteller).",
           "Regulatorische Anforderungen (CSRD, CBAM, LkSG) erhoehen Bueroaufwand.",
           "Cyber-Risiken durch erweiterte Cloud- und OT-Schnittstellen."])),
        ("Strategische Schlussfolgerungen",
         ("list",
          ["Reduktion Kundenkonzentration durch Neukundenakquise (Pharma-, Lebensmittel-Branchen).",
           "Auslandsanteil bis 2027 auf 42 % steigern (siehe Roadmap Internationalisierung).",
           "PDM-Konsolidierung beschleunigen; Digital Twin Pilot PL-500 erfolgreich abschliessen.",
           "Energie- und Nachhaltigkeitsprofil staerken (PV, Oekostrom, CSRD-Reporting)."])),
    ]
    write_doc(f"{BASE}/11_Strategie_Planung/STRAT_SWOT-Analyse_2024.docx", H,
              "SWOT-Analyse 2024", sections)


def gen_strat_wettbewerb():
    sections = [
        ("Zweck und Methodik",
         "Diese Wettbewerbsanalyse beleuchtet die Marktposition der Halbreiter Maschinenbau GmbH im Segment "
         "»Pressen- und Sondermaschinenbau«. Datengrundlage: Branchenstudien VDMA 2023, Geschaeftsberichte der "
         "Wettbewerber, Kundeninterviews (Q4/2023), Messeauftritte EMO 2023 / Blechexpo 2023."),
        ("Hauptwettbewerber",
         tbl(["Wettbewerber", "Sitz", "Umsatz 2023 (Mio. EUR)", "Hauptprodukt", "Positionierung"],
             [["Schuler AG",                "Goeppingen",  ">1.200", "Pressen (Servo, Hydraulik)", "Marktfuehrer DE"],
              ["Halbreiter Maschinenbau GmbH","Koeln",        "48,6",   "PL-500, FB-200",              "Premium Nischen"],
              ["Fagor Arrasate",           "Spanien",      "Ca. 280", "Pressen",                    "Wettbewerber Sued-EU"],
              ["AIDA Engineering",          "Japan",       "Ca. 750","Servo-Pressen",               "Asien-stark"],
              ["Komatsu Industries",       "Japan",       "Ca. 600", "Pressen",                     "Asien"],
              ["Stamag GmbH",              "Aachen",       "Ca. 35",  "Sondermaschinen",             "DE-Wettbewerber"]])),
        ("Differenzierungsmerkmale MMB",
         ("list",
          ["Patentiertes Schnellwechselsystem (Werkzeugwechsel < 2 min).",
           "KI-Modul »Adaptive Process Control« (Lizenz RWTH Aachen).",
           "Hohe Kundenorientierung und Customizing-Faehigkeit fuer Sondermaschinen.",
           "Service- und Wartungsnetz im DACH-Raum mit Reaktionszeit < 24 h."])),
        ("Trends im Marktumfeld",
         ("list",
          ["Verschiebung zu Servo-Pressen (Energieeffizienz, Steuerbarkeit).",
           "Predictive Maintenance / Digital Twin als Kundenanforderung.",
           "Nachhaltigkeits-/CO2-Bilanzen als Beschaffungskriterium (insbesondere OEM).",
           "Asiatische Hersteller draengen mit aggressiver Preisstrategie nach Europa.",
           "Reshoring-Trend in CEE verstaerkt Investitionsneigung in 2025-2026."])),
        ("Strategische Empfehlungen",
         ("list",
          ["Verstaerkter Fokus auf KI- und Digital-Twin-Loesungen als Wettbewerbsvorteil.",
           "Aufbau Service-Stuetzpunkt CEE (siehe Roadmap Internationalisierung).",
           "Kommunikation Patentschutz und FuE-Quote staerker im Marketing nutzen.",
           "Selektive Preisanpassungen, jedoch Premium-Positionierung erhalten."])),
        ("Freigabe",
         "Analyse durchgefuehrt durch Klaus Mueller (CEO) gemeinsam mit Stefan Braun (Vertrieb). "
         "Stand: 06. Maerz 2024."),
    ]
    write_doc(f"{BASE}/11_Strategie_Planung/STRAT_Wettbewerbsanalyse_2024.docx", H,
              "Wettbewerbsanalyse 2024 – Pressen- und Sondermaschinenbau", sections)


# ════════════════════════════════════════════════════════════════════════════════
# Orchestration
# ════════════════════════════════════════════════════════════════════════════════

def main():
    print("Generating polished docs ...")
    # 00 Index
    gen_index()
    # 02 Finanzen
    gen_fin_abschlusspruefung()
    gen_fin_rueckstellungen()
    # 03 HR
    gen_hr_at_struktur()
    # 04 Kunden
    gen_rechnungen()
    gen_kd_rahmenvertrag_tks()
    gen_kd_sla_bosch()
    gen_kd_zufriedenheit()
    # 05 Lieferanten
    gen_bestellungen()
    gen_eingangsrechnungen()
    gen_lf_audit_schunk()
    gen_lf_bewertung()
    gen_lf_rahmenvertrag_einkauf()
    gen_lf_leasing_trumpf()
    gen_lf_logistik_dbsch()
    # 06 Immobilien
    gen_anlagenakte_fz4891()
    gen_imm_002_aussenlager()
    gen_imm_bauantrag()
    gen_imm_grundriss_prod_a()
    gen_imm_grundriss_verwaltung()
    gen_imm_kundenparkplatz()
    gen_imm_versicherungskataster()
    # 07 IP
    gen_lizenzen()
    gen_ip_gebrauchsmuster()
    gen_ip_marke()
    gen_ip_tech_transfer()
    gen_tech_dokumentation_pl500()
    gen_wartungshandbuch_fb200()
    # 08 Versicherungen
    gen_vs_wasserschaden()
    # 09 Compliance
    gen_ce_konformitaet()
    gen_comp_shorts()
    gen_pruefprotokolle()
    gen_sdb_kuehlschmierstoff()
    # 10 IT
    gen_it_docs()
    # 11 Strategie
    gen_strat_beirat()
    gen_strat_digital()
    gen_strat_energie()
    gen_strat_intl()
    gen_strat_swot()
    gen_strat_wettbewerb()
    print("Done.")


if __name__ == "__main__":
    main()
