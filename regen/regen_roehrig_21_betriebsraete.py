"""Brennhagen AG / 21_Betriebsraete – 240 thin docx.

Mitbestimmungsdokumente fuer alle Werke. File types:
- BR_Protokoll_YYYY_MM (monatlich pro Werk REG/RSG/RPL/RCZ/RHU/RHO)
- BR_Korrespondenz_<Thema>_YYYY
- BR_Unterrichtung_Betriebsaenderung_YYYY
- BR_Wahl_YYYY_Protokoll
- BV_<Thema>_YYYY (Betriebsvereinbarungen, ~14 Themen pro Werk)
- GBR_Protokoll_YYYY_Qx (Konzern-/Gesamtbetriebsrat)
- EBR_Jahrestagung_YYYY_Protokoll, EBR_Vereinbarung_YYYY
- Plus Einzelfaelle: JG, PRJ, INV, RCN_IC, Rechtsakte

Werks-BR-Vorsitzende:
- REG Heilbronn: Klaus Bauer (stv. Konzern-BR-Vorsitz)
- RSG Muenchen: Sabine Forster
- REA Stuttgart: Andreas Kessler  (REA == REA-Verwaltung Stuttgart)
- RPL Katowice: Marek Tomaszewski
- RCZ Brno:    Tomas Prochazka
- RHU Gyoer:   Istvan Nagy
- RHO Holding: Marlies Duerr (Konzern-BR-Vorsitz, IG Metall, AR-Mitglied)

Targets:
- BR_Protokoll 350 W
- BV 700 W
- Korrespondenz 350 W
- Unterrichtung 500 W
- Wahl 500 W
- GBR/EBR 500 W
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
from enhance_lib import ROEHRIG_AG as R, write_doc, signatures, MONTHS_DE

BASE = Path(f"{_ROOT}/roehrig_large/21_Betriebsraete")

H_REA = {"name": R["name"], "addr": R["addr"], "hrb": R["hrb"]}
H_REG = {"name": "Brennhagen Elektronik GmbH (REG)", "addr": "Heilbronner Strasse 88, 74072 Heilbronn",
         "hrb": "HRB 221456, AG Heilbronn"}
H_RSG = {"name": "Brennhagen Software GmbH (RSG)", "addr": "Lyonel-Feininger-Strasse 28, 80807 Muenchen",
         "hrb": "HRB 319872, AG Muenchen"}
H_RPL = {"name": "Brennhagen Polska Sp. z o.o. (RPL)", "addr": "ul. Chorzowska 50, 40-121 Katowice",
         "hrb": "KRS 0000543210"}
H_RCZ = {"name": "Brennhagen CZ s.r.o. (RCZ)", "addr": "Tuzemska 47, 627 00 Brno-Slatina",
         "hrb": "C 87654, KS Brno"}
H_RHU = {"name": "Brennhagen Hungary Kft. (RHU)", "addr": "Ipari Park 12, 9027 Gyoer",
         "hrb": "Cg.08-09-029876"}
H_RHO = {"name": "Brennhagen Holding GmbH (RHO)", "addr": R["addr"],
         "hrb": "HRB 726450, AG Stuttgart"}

WERKE = {
    "REG": {"hdr": H_REG, "name": "Brennhagen Elektronik GmbH", "ort": "Heilbronn",
            "vorsitz": "Klaus Bauer", "stv": "Petra Hartmann", "schrift": "Bernd Klein",
            "leitung": "Andreas Maier (Werkleiter)", "ma": 820, "ig": "IG Metall Bezirk Stuttgart",
            "sitzungsort": "Heilbronn, Schulungsraum 2.OG"},
    "RSG": {"hdr": H_RSG, "name": "Brennhagen Software GmbH", "ort": "Muenchen",
            "vorsitz": "Sabine Forster", "stv": "Mario Reuter", "schrift": "Lisa Hofmann",
            "leitung": "Dr. Klaus Kessler (Werkleiter)", "ma": 340, "ig": "IG Metall Bezirk Bayern",
            "sitzungsort": "Muenchen, Konferenzraum Schwabing"},
    "RPL": {"hdr": H_RPL, "name": "Brennhagen Polska Sp. z o.o.", "ort": "Katowice",
            "vorsitz": "Marek Tomaszewski", "stv": "Agnieszka Lewandowska", "schrift": "Piotr Wojciechowski",
            "leitung": "Marek Wojciechowski (Werkleiter)", "ma": 960, "ig": "NSZZ Solidarnosc / OPZZ",
            "sitzungsort": "Katowice, sala konferencyjna A"},
    "RCZ": {"hdr": H_RCZ, "name": "Brennhagen CZ s.r.o.", "ort": "Brno",
            "vorsitz": "Tomas Prochazka", "stv": "Jana Krejcikova", "schrift": "Martin Horak",
            "leitung": "Petr Novak (Werkleiter)", "ma": 680, "ig": "OZ KOVO Brno",
            "sitzungsort": "Brno-Slatina, jednaci mistnost 1.NP"},
    "RHU": {"hdr": H_RHU, "name": "Brennhagen Hungary Kft.", "ort": "Gyoer",
            "vorsitz": "Istvan Nagy", "stv": "Eszter Kovacs", "schrift": "Gabor Toth",
            "leitung": "Laszlo Kovacs (Werkleiter)", "ma": 540, "ig": "Vasas Szakszervezeti Szovetseg",
            "sitzungsort": "Gyoer, targyalo 2"},
    "RHO": {"hdr": H_RHO, "name": "Brennhagen Holding GmbH", "ort": "Stuttgart",
            "vorsitz": "Marlies Duerr", "stv": "Klaus Bauer", "schrift": "Christine Vogel",
            "leitung": "Anna Mueller (CEO Brennhagen Elektronik AG)", "ma": 45, "ig": "IG Metall Bezirk Stuttgart",
            "sitzungsort": "Stuttgart, Vorstandsetage Raum V.04"},
}

# Common standing themes for monthly BR meetings (cycle through)
STD_THEMES = [
    ("Personalplanung und Neueinstellungen", "Werkleitung berichtet ueber Stellenbesetzungen, befristete Vertraege und geplante Einstellungen im naechsten Quartal. BR pruefte die Personalplanungsliste gemaess § 92 BetrVG."),
    ("Ueberstunden und Arbeitszeitmodelle", "Erhebung der geleisteten Mehrarbeit nach § 87 Abs. 1 Nr. 3 BetrVG. Diskussion der Belastungssituation in der Produktion. BR mahnt strikte Einhaltung der Ruhezeiten nach ArbZG an."),
    ("Arbeits- und Gesundheitsschutz", "Bericht der Fachkraft fuer Arbeitssicherheit (Sifa). Erhoehte Krankenstaende im Schichtbetrieb. BR fordert ergonomische Schulungen und Anpassung der Pausengestaltung."),
    ("Schichtplanung und Urlaubsplanung", "Vorstellung der Schichtplaene fuer den Folgemonat. Klaerung von Urlaubskonflikten. BR weist auf Vorrang sozialer Gesichtspunkte nach § 87 Abs. 1 Nr. 5 BetrVG hin."),
    ("Investitionen und Betriebsaenderungen", "Information ueber geplante Investitionen in Linie X. BR pruefte die Auswirkungen auf Arbeitsplaetze nach § 111 BetrVG. Bisher keine mitbestimmungspflichtige Betriebsaenderung."),
    ("Aus- und Weiterbildung", "Diskussion des Weiterbildungsbudgets, Ausbildungsplaetze fuer das kommende Jahr, Antraege auf Schulungsfreistellung nach § 37 Abs. 6 und Abs. 7 BetrVG."),
    ("Datenschutz und IT-Mitbestimmung", "Bericht zur Einfuehrung neuer Software (MES-Update, Zeiterfassung). § 87 Abs. 1 Nr. 6 BetrVG. Datenschutzbeauftragter zugeschaltet, Verfahrensverzeichnis vorgelegt."),
    ("Eingruppierungen und Entgeltfragen", "Pruefung von Eingruppierungsantraegen nach ERA-TV. Diskussion strittiger Faelle, Vorbereitung der paritaetischen Kommission gemaess § 99 BetrVG."),
    ("Beschwerden nach § 84 BetrVG", "Behandlung von zwei Einzelbeschwerden (anonymisiert). Gespraech mit HR und betroffener Fuehrungskraft vereinbart, Nachverfolgung in der naechsten Sitzung."),
    ("Vereinbarkeit Familie und Beruf", "Antraege auf Reduzierung der Arbeitszeit nach § 8 TzBfG. BR begruesst die Initiative der Geschaeftsleitung zur Erweiterung der Kita-Belegplaetze."),
    ("Tarifrunde und IG Metall-Informationen", "Berichterstattung des BR-Vorsitzes zur aktuellen Tarifrunde der Metall- und Elektroindustrie. Vorbereitung Mitgliederversammlung."),
    ("Inklusion und Schwerbehindertenvertretung", "Bericht der SBV ueber die Beschaeftigungsquote nach § 154 SGB IX, Pruefung der Pflichtquote, Anpassungsmassnahmen in der Logistik."),
]


def br_protokoll(werk_key, jahr, monat):
    w = WERKE[werk_key]
    # cycle themes
    theme_idx = (jahr * 12 + monat) % len(STD_THEMES)
    t1 = STD_THEMES[theme_idx]
    t2 = STD_THEMES[(theme_idx + 3) % len(STD_THEMES)]
    t3 = STD_THEMES[(theme_idx + 7) % len(STD_THEMES)]
    sitzungs_tag = 8 + (monat % 4) * 3
    datum = f"{sitzungs_tag}. {MONTHS_DE[monat]} {jahr}"
    sections = [
        ("Sitzungsdaten", [
            ["Datum", datum],
            ["Beginn / Ende", f"14:00 Uhr / 17:30 Uhr"],
            ["Ort", w["sitzungsort"]],
            ["Vorsitz", w["vorsitz"]],
            ["Stellv. Vorsitz", w["stv"]],
            ["Schriftfuehrung", w["schrift"]],
            ["Geladen Geschaeftsleitung", w["leitung"]],
            ["Beschlussfaehigkeit", "festgestellt (anwesend: 9 von 11 BR-Mitgliedern)"],
        ]),
        ("TOP 1 — Eroeffnung und Genehmigung der Tagesordnung",
         f"Der Vorsitzende, Herr/Frau {w['vorsitz']}, eroeffnet die Sitzung um 14:00 Uhr, stellt die ordnungsgemaesse Ladung und die Beschlussfaehigkeit fest. "
         f"Die mit der Einladung vom {sitzungs_tag-7}. {MONTHS_DE[monat]} {jahr} versandte Tagesordnung wird ohne Aenderungen einstimmig genehmigt. "
         f"Das Protokoll der Vormonatssitzung wird ohne Einwaende angenommen."),
        (f"TOP 2 — {t1[0]}", t1[1] + f" Die Werkleitung ({w['leitung']}) beantwortet Rueckfragen der BR-Mitglieder zu Einzelfaellen aus dem Bereich Fertigung. Eine Liste der offenen Punkte wird in den naechsten 14 Tagen nachgereicht."),
        (f"TOP 3 — {t2[0]}", t2[1] + " Es wird vereinbart, das Thema bis zur naechsten Sitzung weiter zu beobachten und gegebenenfalls eine Ad-hoc-Ausschusssitzung einzuberufen."),
        (f"TOP 4 — {t3[0]}", t3[1] + " Die Beschluesse hierzu werden unter TOP 5 zusammengefasst."),
        ("TOP 5 — Beschluesse", ("list", [
            f"Beschluss 1: Zustimmung zu den vorgelegten Eingruppierungen Nr. {monat:02d}/{jahr}-A bis -E (einstimmig, 9 Ja-Stimmen).",
            f"Beschluss 2: Schulungsfreistellung nach § 37 Abs. 6 BetrVG fuer drei BR-Mitglieder fuer das Seminar Arbeitsrecht-Update {jahr} (einstimmig).",
            f"Beschluss 3: Bildung eines Ad-hoc-Ausschusses zur Begleitung der MES-Einfuehrung (3 Mitglieder, Berichterstattung Folgemonat).",
            f"Beschluss 4: Stellungnahme nach § 99 BetrVG zu zwei personellen Einzelmassnahmen (Zustimmung), zu einer Massnahme Zustimmungsverweigerung wegen § 99 Abs. 2 Nr. 3 BetrVG.",
        ])),
        ("TOP 6 — Verschiedenes",
         f"Bericht des Vorsitzenden zur Sitzung des Konzernbetriebsrats (Vorsitz Marlies Duerr) am letzten Donnerstag in Stuttgart. "
         f"Hinweis auf die kommende Betriebsversammlung im {MONTHS_DE[(monat % 12)+1]} {jahr}. "
         f"Der Vorsitzende {w['vorsitz']} schliesst die Sitzung um 17:30 Uhr. Naechste Sitzung: {sitzungs_tag+28}. {MONTHS_DE[monat]} {jahr}."),
        ("Unterschriften", signatures(w["vorsitz"], "Vorsitz Betriebsrat", w["name"],
                                       w["schrift"], "Schriftfuehrung", w["name"],
                                       place=w["ort"], date_str_=datum)),
    ]
    return sections


# ── BV themes catalog
BV_THEMES = {
    "Arbeitszeit": ("Betriebsvereinbarung Arbeitszeit und Arbeitszeiterfassung",
                    ["Geltungsbereich (alle gewerblichen und kaufmaennischen Mitarbeiter ausser leitende Angestellte i.S.v. § 5 Abs. 3 BetrVG).",
                     "Regelarbeitszeit 35 Std./Woche (West) bzw. 38 Std./Woche (Ost / Auslandsgesellschaften abweichend nach lokalem Tarif).",
                     "Gleitzeitrahmen 6:00 bis 20:00 Uhr, Kernzeit 9:00 bis 15:00 Uhr.",
                     "Erfassung elektronisch ueber Zeiterfassungssystem (ATOSS), tagesaktuelle Pflege durch Mitarbeitende.",
                     "Hoechstarbeitszeitgrenzen nach ArbZG, taegliche Ruhezeit min. 11 Std., woechentliche Ruhezeit min. 35 Std.",
                     "Mehrarbeit nur mit Zustimmung des Betriebsrats nach § 87 Abs. 1 Nr. 3 BetrVG, max. 10 Stunden/Woche.",
                     "Ueberstundenausgleich vorrangig durch Freizeit, alternativ verguetet zu 25 % Zuschlag, Nachtzuschlag 25 %, Sonntag 50 %, Feiertag 100 %.",
                     "Kontoregelung: Zeitkonten +120/-40 Stunden, Quartals-Abbauplan bei Ueberschreitung."]),
    "Homeoffice": ("Betriebsvereinbarung Homeoffice und mobile Arbeit",
                   ["Beschaeftigte koennen bis zu 50 % der monatlichen Arbeitstage mobil arbeiten (im Inland EWR/EU).",
                    "Voraussetzung: arbeitsplatzbedingte Eignung und Zustimmung der direkten Fuehrungskraft.",
                    "Bereitstellung Laptop, Headset, Monitor (Standard-Setup), Zuschuss 50 EUR/Monat fuer Strom/Internet.",
                    "Arbeitsmittel bleiben Eigentum der Gesellschaft, Versicherung ueber Betriebshaftpflicht.",
                    "Arbeitsschutz: Selbsteinschaetzung der Gefaehrdung mit jaehrlichem Refresh, Pflicht zur ergonomischen Einrichtung.",
                    "Datenschutz: VPN-Pflicht, Bildschirmsperre nach 5 min, Verbot der Verarbeitung personenbezogener Daten auf privaten Geraeten.",
                    "Erreichbarkeit innerhalb der vereinbarten Arbeitszeit, kein Anspruch auf staendige Erreichbarkeit.",
                    "Recht auf Nichterreichbarkeit ausserhalb der Arbeitszeit (Right to Disconnect)."]),
    "Betriebliche_Altersversorgung": ("Betriebsvereinbarung Betriebliche Altersversorgung (bAV)",
                                      ["Allen unbefristet Beschaeftigten wird eine arbeitgeberfinanzierte Grundzusage von 1,2 % der pensionsfaehigen Beguege gewaehrt.",
                                       "Zusaetzlich Entgeltumwandlung bis 8 % BBG (West) mit Arbeitgeberzuschuss 20 %.",
                                       "Durchfuehrungsweg: Pensionsfonds Heubeck (vorrangig), Direktversicherung Allianz Pensionsmanagement.",
                                       "Unverfallbarkeit nach gesetzlicher Frist (3 Jahre, Vollendung 21. Lebensjahr).",
                                       "Anpassungspruefung nach § 16 BetrAVG alle 3 Jahre.",
                                       "Information der Mitarbeiter durch jaehrlichen Renteninformationsbrief.",
                                       "Sondervereinbarung fuer Bestandsmitarbeiter mit alter Direktzusage gemaess Anlage 1."]),
    "Entgeltrahmenabkommen": ("Betriebsvereinbarung Entgeltrahmenabkommen / Eingruppierung",
                              ["Anwendung des Entgeltrahmenabkommens (ERA) der Metall- und Elektroindustrie Baden-Wuerttemberg.",
                               "Eingruppierung in 17 Entgeltgruppen nach Anforderungsprofil gemaess ERA-Bewertungsmethode.",
                               "Bildung einer paritaetischen Eingruppierungskommission (4 Mitglieder, je 2 von AG und BR).",
                               "Erstgesprach binnen 6 Wochen nach Einstellung, schriftliche Mitteilung der Eingruppierung an den Mitarbeiter.",
                               "Reklamationsverfahren: schriftlicher Einspruch binnen 4 Wochen, Pruefung in paritaetischer Kommission, ggf. Schlichtung.",
                               "Leistungszulage gemaess ERA-Leistungsbeurteilung jaehrlich, Bandbreite 0-15 %.",
                               "Belastungszulage fuer ungueenstige Arbeitsbedingungen nach Anlage 2."]),
    "Essenszuschuss": ("Betriebsvereinbarung Essenszuschuss / Kantine",
                       ["Allen Beschaeftigten am Standort wird ein Kantinen-Essenszuschuss gewaehrt.",
                        "Hauptmahlzeit: Eigenanteil Mitarbeiter 3,50 EUR, Arbeitgeberzuschuss 3,10 EUR, Vorteilsbesteuerung pauschal 25 % gemaess R 8.1 Abs. 7 LStR.",
                        "Snacks/Salat: ohne Zuschuss zum Selbstkostenpreis.",
                        "Maximal 220 Zuschuss-Tage pro Kalenderjahr und Mitarbeiter.",
                        "Mobilversion: digitale Essenmarken via App-Token (Edenred / Sodexo), gleicher Zuschuss.",
                        "Beruecksichtigung verschiedener Kostformen (vegetarisch, vegan, halal, koscher) im Wochenangebot.",
                        "Qualitaetssicherung durch jaehrliche Kantinen-Audits, Berichterstattung an den BR."]),
    "Gesundheitsschutz": ("Betriebsvereinbarung Betriebliches Gesundheitsmanagement (BGM)",
                          ["Einrichtung eines Steuerkreises BGM (Werkarzt, Sifa, BR, HR, Werkleitung).",
                           "Jaehrliche Gesundheitstage am Standort mit Vorsorgeangeboten (Augen, Herz/Kreislauf, Hauttest).",
                           "Praeventionsprogramme: Rueckenschule, Stressbewaeltigung, Ernaehrungsberatung – Teilnahme waehrend der Arbeitszeit bis 4 Std./Quartal.",
                           "Externes Mitarbeiter-Assistance-Programm (EAP) mit Anbieter INSITE-Interventions, 24/7-Hotline, vertraulich.",
                           "Suchtpraevention nach DGUV V/A: Stufenplan, Vereinbarungspflicht bei Auffaelligkeiten.",
                           "Anonymisierte Auswertung der Krankenquote, getrennt nach Bereichen, halbjaehrlich an BR.",
                           "Foerderung von Sport- und Bewegungsangeboten (Firmenlauf, Zuschuss Hansefit/Wellpass 25 EUR/Monat)."]),
    "Gleichstellung": ("Betriebsvereinbarung Gleichstellung und Antidiskriminierung",
                       ["Bekenntnis zur Chancengleichheit unabhaengig von Geschlecht, Alter, Herkunft, Religion, sexueller Identitaet, Behinderung.",
                        "Zielquote 30 % Frauen in Fuehrungspositionen bis 2027, Massnahmenkatalog gemaess Anlage 1.",
                        "Foerderung Wiedereinstieg nach Elternzeit (garantiertes Rueckkehrgespraech, Patenmodell).",
                        "Diskriminierungsbeschwerdestelle nach § 13 AGG, paritaetisch besetzt (HR, BR, SBV, Diversity-Beauftragter).",
                        "Verpflichtende Schulung Diversity & Inclusion fuer alle Fuehrungskraefte, mindestens alle 24 Monate.",
                        "Geschlechtergerechte Stellenausschreibungen (m/w/d), Standardvorlagen verbindlich.",
                        "Jaehrliche Berichterstattung an die Geschaeftsleitung und den BR zur Entwicklung der Indikatoren."]),
    "IT": ("Betriebsvereinbarung IT-Nutzung und Ueberwachung",
           ["Erlaubt: Nutzung von E-Mail, Internet, Kollaborationstools (M365, Teams, SAP, Confluence) zu dienstlichen Zwecken.",
            "Private Nutzung in geringem Umfang geduldet, kein Anspruch.",
            "Verbot: Verbreitung diskriminierender, gewaltverherrlichender, pornografischer Inhalte; Verstoss = Abmahnungsgrund.",
            "Protokollierung der Systemnutzung nur zu Zwecken der IT-Sicherheit und Funktionsfaehigkeit (Loeschfristen 90 Tage).",
            "Keine Mitarbeiter-Leistungskontrolle aus IT-Logs ohne konkreten Anfangsverdacht und Hinzuziehung BR/DSB (4-Augen-Prinzip).",
            "Einfuehrung neuer Tools mit Mitbestimmung gemaess § 87 Abs. 1 Nr. 6 BetrVG, Verfahrensverzeichnis (Art. 30 DSGVO).",
            "Privates Geraet (BYOD) nur ueber Mobile-Device-Management (Intune) und Containerloesung."]),
    "Kurzarbeitsregelung": ("Betriebsvereinbarung Kurzarbeit (KuG)",
                            ["Geltung: alle Beschaeftigten der betroffenen Bereiche gemaess Anzeige Bundesagentur fuer Arbeit.",
                             "Ausnahme: Auszubildende (vorrangig Versetzung in andere Bereiche).",
                             "Arbeitszeitverkuerzung zwischen 10 % und 100 %, individuelle Festlegung je Kostenstelle.",
                             "Aufstockung des KuG durch den Arbeitgeber auf 90 % des Netto-Vergleichsentgelts (KuG-Netto + AG-Aufstockung).",
                             "Urlaub aus dem Vorjahr ist vorab einzubringen; aktueller Urlaub max. 5 Tage Vorab-Einbringung.",
                             "Information ueber Lage in monatlichem Townhall-Format, BR-Sitzung erhaelt Auslastungsplaene.",
                             "Beendigung der Kurzarbeit mit Ankuendigungsfrist 14 Tage; Rueckkehr in Vollarbeit zum Monatsersten."]),
    "Leistungs": ("Betriebsvereinbarung Leistungs- und Verhaltenskontrolle",
                  ["Grundsatz: Verhaltens- und Leistungskontrollen sind nur zulaessig auf Basis einer konkreten BV oder gesetzlicher Pflicht.",
                   "Keine heimliche Mitarbeiterueberwachung, keine Videoaufzeichnung an Arbeitsplaetzen ausser zur Objektsicherheit (Zugang, Lager).",
                   "Auswertung von Zeit- und Leistungsdaten nur aggregiert, Einzelauswertung nur bei begruendetem Verdacht und BR-Beteiligung.",
                   "Personalentwicklungsgespraeche dienen nicht der Disziplinierung, sondern der Foerderung.",
                   "Stichprobenkontrollen Telefon-/E-Mail-Verkehr nur bei Compliance-Verdacht, formelles Verfahren mit BR/DSB.",
                   "Dokumentationspflicht aller Kontrollmassnahmen, Aufbewahrung 12 Monate, danach Loeschung.",
                   "Recht der Mitarbeitenden auf Auskunft nach Art. 15 DSGVO und auf Stellungnahme zu Bewertungen."]),
    "Parkplatzregelung": ("Betriebsvereinbarung Parkplatzregelung",
                          ["Bereitstellung der werkseigenen Parkflaechen fuer alle Beschaeftigten waehrend der Arbeitszeit.",
                           "Priorisierung: Schwerbehinderte (15 Plaetze, beschildert), Eltern mit Kind unter 6 Jahren (8 Plaetze), Schichtarbeiter Frueh-/Spaet.",
                           "E-Ladesaeulen (22 kW, 30 Plaetze) mit Ladekarten, Verbrauchsabrechnung quartalsweise (0,38 EUR/kWh).",
                           "Fahrradparkhaus ueberdacht mit 80 Plaetzen und 12 E-Bike-Ladepunkten.",
                           "Verbot der Lagerung von Gefahrgut, Werkzeugen oder Wertgegenstaenden im Auto.",
                           "Kontrolle Falschparker durch Werkschutz, Verwarnung 20 EUR ab dritter Wiederholung.",
                           "Ueberpruefung der Parkraumsituation jaehrlich, Anpassung bei wesentlicher Veraenderung der Belegschaftsgroesse."]),
    "Schichtbetrieb": ("Betriebsvereinbarung Schichtbetrieb und Schichtpraemien",
                       ["Schichtmodelle: 2-Schicht (Frueh 6-14, Spaet 14-22), 3-Schicht (zusaetzlich Nacht 22-6), vollkontinuierlich (Wochenende).",
                        "Zuschlaege: Spaetschicht 5 %, Nachtschicht 25 %, Sonntag 50 %, Feiertag 100 %, vollkonti 15 %.",
                        "Schichtwechsel grundsaetzlich woechentlich, Vorwaertsrotation (Frueh-Spaet-Nacht).",
                        "Schichtplan-Bekanntgabe spaetestens 4 Wochen im Voraus.",
                        "Tauschmoeglichkeit zwischen Mitarbeitern mit Zustimmung Vorgesetzter, gleichwertige Qualifikation.",
                        "Pausenregelung: 30 min bezahlte Hauptpause in Nachtschicht, 30 min unbezahlt Frueh/Spaet plus 2x10 min bezahlt.",
                        "Anspruch auf Gesundheits-Check fuer Nachtschicht-Beschaeftigte alle 3 Jahre, ab 50. Lebensjahr jaehrlich."]),
    "Sozialer": ("Betriebsvereinbarung Sozialer Interessenausgleich",
                 ["Anwendungsbereich: Betriebsaenderungen i.S.v. § 111 BetrVG mit nachteiligen Folgen fuer die Belegschaft.",
                  "Abfindungsformel: Bruttomonatsgehalt x Betriebszugehoerigkeit (Jahre) x Faktor 1,0 (Basis); Faktor 1,3 ab 50. Lebensjahr; Faktor 1,5 ab 55. Lebensjahr.",
                  "Mindestabfindung 5.000 EUR brutto, Hoechstgrenze 250.000 EUR brutto.",
                  "Sprinterpraemie bei freiwilligem Aufhebungsvertrag binnen 6 Wochen: zusaetzliche 25 % der Abfindung.",
                  "Qualifizierungsbudget je betroffenem MA bis 5.000 EUR fuer Umschulung/Weiterbildung.",
                  "Transfergesellschaft (12 Monate) als Alternativangebot, getragen vom AG, Aufstockung Transferkurzarbeitergeld auf 80 %.",
                  "Vorruhestandsregelung ab 58. Lebensjahr mit individueller Berechnung und sozialvertraeglicher Brueckenfinanzierung."]),
    "Urlaubsplanung": ("Betriebsvereinbarung Urlaubsplanung",
                       ["Tariflicher Jahresurlaub 30 Arbeitstage, Schwerbehinderte zzgl. 5 Tage.",
                        "Bekanntgabe der Urlaubswuensche bis 30. November fuer das Folgejahr.",
                        "Vorrang sozialer Gesichtspunkte (Schulkinder, Pflege Angehoerige) bei Konflikten.",
                        "Werkferien: 2 Wochen im August (Linien 1-3), 1 Woche Jahreswechsel (alle Bereiche).",
                        "Maximal 10 Urlaubstage Uebertrag ins Folgejahr, Verfall zum 31.03.",
                        "Halbtagsurlaub moeglich, max. 12 Halbtage/Jahr.",
                        "Krankheit waehrend Urlaub: aerztliches Attest erforderlich ab 1. Tag fuer Anrechnung gemaess § 9 BUrlG."]),
    "Weiterbildung": ("Betriebsvereinbarung Weiterbildung und Qualifizierung",
                      ["Anspruch auf jaehrliches Mitarbeitergespraech zur Qualifikationsentwicklung.",
                       "Weiterbildungsbudget je MA: 1.500 EUR p.a. (gewerblich), 3.000 EUR p.a. (kaufmaennisch/IT).",
                       "Foerderung von Berufsbegleitenden Studien (max. 50 % Studiengebuehren, max. 8.000 EUR, Rueckzahlungsklausel 3 Jahre).",
                       "Mindest-Schulungstage: 3 Tage/Jahr (gewerblich), 5 Tage/Jahr (Angestellte) waehrend der Arbeitszeit.",
                       "Anrechnung von externen Zertifikaten (PMP, Six Sigma, ASPICE) als Entwicklungsbestandteil.",
                       "Mentoring-Programm fuer Berufseinsteiger und Nachwuchsfuehrungskraefte.",
                       "Berichterstattung halbjaehrlich an BR zur Inanspruchnahme und Zielerreichung."]),
    "Betriebliches": ("Betriebsvereinbarung Betriebliches Vorschlagswesen (BVW)",
                      ["Foerderung von Verbesserungsvorschlaegen aller Beschaeftigten zur kontinuierlichen Verbesserung (KVP).",
                       "Eingabe online ueber Tool ideenLABOR.live, alternative Papierformulare in Werkstatt-Buero.",
                       "Bewertung durch Ideenausschuss (Werkleitung, BR, Fachexperten) binnen 8 Wochen.",
                       "Praemierung berechnen sich aus jaehrlichem Einsparbetrag x 0,5 % (Mindestpraemie 50 EUR, Hoechstpraemie 25.000 EUR).",
                       "Anerkennungspraemien fuer nicht messbar quantifizierbare Vorschlaege: 50/150/500/1500 EUR.",
                       "Auszahlung mit der Gehaltszahlung des Folgemonats nach Anerkennung.",
                       "Jahresauswertung mit Top-Vorschlag-Preis (Reise, Sonderpraemie 5.000 EUR), Vorstellung in Betriebsversammlung."]),
}


def bv_content(theme_key, werk_key, jahr):
    w = WERKE[werk_key]
    title, bullets = BV_THEMES[theme_key]
    # Build clauses
    clauses = [
        ("§ 1 Praeambel und Geltungsbereich", [
            f"Diese Betriebsvereinbarung wird zwischen der {w['name']}, vertreten durch die Werkleitung ({w['leitung']}), und dem Betriebsrat der {w['name']}, vertreten durch den Vorsitzenden {w['vorsitz']}, geschlossen.",
            f"Sie gilt fuer alle Beschaeftigten des Standorts {w['ort']} im Sinne des § 5 BetrVG. Ausgenommen sind leitende Angestellte gemaess § 5 Abs. 3 BetrVG.",
            f"Massgeblich sind die Vorschriften des Betriebsverfassungsgesetzes (BetrVG), des Allgemeinen Gleichbehandlungsgesetzes (AGG), der DSGVO/BDSG sowie der einschlaegige Manteltarifvertrag der Metall- und Elektroindustrie {('Baden-Wuerttemberg' if werk_key in ('REA','RHO','REG') else 'Bayern' if werk_key=='RSG' else 'lokal')}.",
        ]),
        ("§ 2 Regelungsgegenstand", [
            "Die Parteien vereinbaren die folgenden inhaltlichen Regelungen, deren Umsetzung verbindlich fuer alle Fuehrungskraefte und Beschaeftigten der vorgenannten Bereiche ist.",
        ]),
        ("§ 3 Inhaltliche Regelungen", bullets),
        ("§ 4 Mitbestimmung und Umsetzung", [
            "Die Umsetzung der einzelnen Massnahmen erfolgt unter Beteiligung des Betriebsrats gemaess der einschlaegigen Mitbestimmungstatbestaende (insbesondere § 87 BetrVG).",
            "Die Geschaeftsleitung benennt einen verantwortlichen Ansprechpartner aus dem HR-Bereich; der Betriebsrat benennt ein zustaendiges Mitglied bzw. einen Ausschuss.",
            "Regelmaessiges Reporting an die Betriebsratssitzung mindestens halbjaehrlich.",
        ]),
        ("§ 5 Inkrafttreten, Laufzeit, Kuendigung", [
            f"Diese Vereinbarung tritt am 1. Januar {jahr} in Kraft.",
            "Sie wird auf unbestimmte Zeit geschlossen und kann mit einer Frist von 3 Monaten zum Ende eines Kalendervierteljahres ordentlich gekuendigt werden.",
            "Im Fall der Kuendigung entfaltet die Vereinbarung Nachwirkung bis zum Abschluss einer Neuregelung gemaess § 77 Abs. 6 BetrVG.",
            "Aenderungen und Ergaenzungen beduerfen der Schriftform.",
        ]),
        ("§ 6 Salvatorische Klausel", [
            "Sollten einzelne Bestimmungen dieser Vereinbarung ganz oder teilweise unwirksam sein oder werden, beruehrt dies die Wirksamkeit der uebrigen Bestimmungen nicht.",
            "Anstelle der unwirksamen Bestimmung gilt eine Regelung als vereinbart, die dem wirtschaftlichen Zweck am naechsten kommt.",
        ]),
    ]
    return title, clauses


def korr_content(thema, werk_key, jahr):
    w = WERKE[werk_key]
    themen = {
        "Arbeitszeit_Widerspruch": ("Widerspruch Betriebsrat zur Anordnung von Mehrarbeit",
                                     "geplante Mehrarbeit in der Endmontage (Linie 2) im Umfang von 240 Stunden/Woche fuer die Dauer von 6 Wochen",
                                     "§ 87 Abs. 1 Nr. 3 BetrVG",
                                     "Der Betriebsrat lehnt die Anordnung in der vorgelegten Form ab. Begruendung: (1) Die wirtschaftliche Notwendigkeit ist nicht ausreichend dargelegt. (2) Alternative Massnahmen (Aushilfen, Leiharbeit, Verschiebung von Liefertermin) wurden nicht ausreichend geprueft. (3) Die Belastungssituation der Belegschaft ist bereits im Vormonat ueberschritten worden (Krankenstand 9,8 %).",
                                     "Wir bitten um die Vorlage eines alternativen Konzepts oder die Einberufung der Einigungsstelle gemaess § 76 BetrVG."),
        "Betriebsaenderung_Interessenausgleich": ("Verhandlungen Interessenausgleich gemaess § 112 BetrVG",
                                                   "geplante Verlagerung der SMD-Bestueckung von Linie 3 nach Katowice mit Wirkung zum 01.07.{jahr}",
                                                   "§§ 111, 112 BetrVG",
                                                   "Der Betriebsrat fordert die Aufnahme von Verhandlungen ueber einen Interessenausgleich und Sozialplan. Die geplante Massnahme ist eine Betriebsaenderung im Sinne des § 111 BetrVG (Stilllegung eines Betriebsteils, betroffen ca. 42 MA). Forderungen: (a) Versetzungsangebote an andere Werke, (b) Sozialplan mit Abfindungsformel Faktor 1,3, (c) Transfergesellschaft 12 Monate.",
                                                   "Erstes Verhandlungsgespraech vorgeschlagen am 15. {monat} {jahr}. Wir bitten um Bestaetigung."),
        "Eingruppierungsstreitigkeiten": ("Zustimmungsverweigerung BR zu Eingruppierung gemaess § 99 BetrVG",
                                          "Eingruppierung des Mitarbeiters/der Mitarbeiterin (anonymisiert, Pers-Nr. {jahr}-A47) in ERA-Gruppe EG 7",
                                          "§ 99 Abs. 2 Nr. 1 BetrVG (Verstoss gegen Gesetz/Tarifvertrag)",
                                          "Der Betriebsrat verweigert die Zustimmung zur Eingruppierung in EG 7. Aufgabengebiet und Anforderungsprofil entsprechen nach Ansicht des BR der EG 9 (Facharbeiterniveau mit Spezialkenntnissen in SMD-Programmierung). Es wird auf zwei vergleichbare Faelle aus 2022 verwiesen, die in EG 9 eingruppiert wurden.",
                                          "Wir schlagen die Anrufung der paritaetischen Eingruppierungskommission gemaess BV ERA vor. Eine Stellungnahme bis 14 Tage wird erbeten."),
        "Massenentlassung_Anzeige": ("Stellungnahme Betriebsrat zur Massenentlassungsanzeige nach § 17 KSchG",
                                      "geplante betriebsbedingte Beendigung von 38 Arbeitsverhaeltnissen im Bereich Logistik/Versand",
                                      "§ 17 KSchG, §§ 111, 112 BetrVG",
                                      "Der Betriebsrat nimmt die Konsultation gemaess § 17 Abs. 2 KSchG zur Kenntnis. Begleitend wird die parallele Aufnahme von Interessenausgleichsverhandlungen gefordert. Soziale Auswahl gemaess § 1 Abs. 3 KSchG ist auf nachvollziehbaren Kriterien (Lebensalter, Betriebszugehoerigkeit, Unterhaltspflichten, Schwerbehinderung) zu basieren.",
                                      "Wir behalten uns die Anrufung der Einigungsstelle vor, falls bis 3 Wochen keine Einigung erzielt wird."),
        "Personalplanung": ("Stellungnahme Betriebsrat zur Personalplanung gemaess § 92 BetrVG",
                            "Personalplanung fuer das Geschaeftsjahr {jahr} mit Reduzierung der Stammbelegschaft um 28 FTE bei gleichzeitiger Erhoehung der Leiharbeitsquote von 8 % auf 14 %",
                            "§ 92 BetrVG i.V.m. § 80 Abs. 2 BetrVG",
                            "Der Betriebsrat kritisiert die geplante Erhoehung der Leiharbeitsquote als unvereinbar mit dem Grundsatz der Stammbelegschaftsfoerderung. Forderungen: (a) Begrenzung Leiharbeit auf max. 10 %, (b) Uebernahmeperspektive fuer bewaehrte Leiharbeiter nach 12 Monaten, (c) gemeinsame Erstellung einer Qualifizierungsmatrix.",
                                      "Wir bitten um Vorlage einer ueberarbeiteten Planung in der naechsten BR-Sitzung."),
        "Sozialplan_2023": ("Verhandlung Sozialplan {jahr}",
                            "Sozialplan zur Begleitung der Restrukturierung Standort {ort}",
                            "§ 112 BetrVG",
                            "Der Betriebsrat hat den vorgelegten Sozialplan-Entwurf der Geschaeftsleitung intensiv beraten. Im Wesentlichen besteht Einigkeit ueber Abfindungsformel (Faktor 1,3) und Transfergesellschaft (12 Monate). Strittig sind noch: Stichtagsregelung Vorruhestand (BR: 55 J., AG: 58 J.), Hoehe Sprinterpraemie (BR: 30 %, AG: 20 %), Qualifizierungsbudget (BR: 8.000 EUR, AG: 5.000 EUR).",
                            "Vorschlag fuer Schlichtungstermin am 28. {monat} {jahr} unter Vorsitz der vereinbarten Einigungsstellenvorsitzenden Dr. Martina Reichel (VRiArbG i.R., Stuttgart)."),
        "Ueberstundenregelung": ("Konsultation Anpassung Ueberstundenregelung",
                                  "geplante Anhebung der Hoechstgrenze fuer Mehrarbeit von 10 auf 15 Stunden/Woche befristet auf 6 Monate (Hochlauf BMS-12 Programm VW ID.7)",
                                  "§ 87 Abs. 1 Nr. 3 BetrVG i.V.m. ArbZG",
                                  "Der Betriebsrat ist grundsaetzlich gespraechsbereit, knuepft die Zustimmung jedoch an folgende Bedingungen: (1) Freiwilligkeit, kein Anordnungsrecht der Vorgesetzten, (2) zusaetzlicher Zeitzuschlag 5 % auf alle Mehrarbeitsstunden ueber 10 Stunden, (3) Anspruch auf 2 Tage zusaetzlichen Erholungsurlaub fuer Beschaeftigte, die kontinuierlich >12 Std. Mehrarbeit/Woche leisten.",
                                  "Wir bitten um Vorlage einer modifizierten Vereinbarung. Beschluss BR-Sitzung folgt nach Zugang."),
    }
    titel, gegenstand, rg, stell, schluss = themen[thema]
    sections = [
        ("Betreff",
         f"{titel}\nGegenstand: {gegenstand.format(jahr=jahr, ort=w['ort'], monat=MONTHS_DE[6])}\nRechtsgrundlage: {rg}"),
        ("Sachverhalt",
         f"Sehr geehrte Damen und Herren,\n\nmit Schreiben vom 12. {MONTHS_DE[3]} {jahr} bzw. im Rahmen der monatlichen Betriebsratssitzung am 15. {MONTHS_DE[4]} {jahr} hat die Geschaeftsleitung dem Betriebsrat den oben genannten Sachverhalt zur Kenntnis gebracht. "
         f"Der Betriebsrat hat den Vorgang in seiner Sitzung am 22. {MONTHS_DE[4]} {jahr} unter Hinzuziehung des Sachverstaendigen Rechtsanwalt Dr. Wieland Schmitt (Kanzlei Schmitt + Partner, Stuttgart) beraten."),
        ("Rechtliche Bewertung und Stellungnahme",
         stell.format(monat=MONTHS_DE[5], jahr=jahr)),
        ("Forderung / weiteres Vorgehen",
         schluss.format(monat=MONTHS_DE[6], jahr=jahr)),
        ("Schlussformel",
         f"Mit freundlichen kollegialen Gruessen\n\nFuer den Betriebsrat der {w['name']}\n\n{w['vorsitz']} (Vorsitz)\n{w['stv']} (Stellvertretung)\n\nKopie: Konzernbetriebsrat (Marlies Duerr), {w['ig']}, KPMG (sofern bilanziell relevant)"),
    ]
    return titel + f" – {w['name']} ({jahr})", sections


def wahl_protokoll(werk_key, jahr):
    w = WERKE[werk_key]
    sections = [
        ("Wahlvorstand und Wahltermin", [
            ["Wahlvorstand Vorsitz", "Dr. Friederike Senn (extern, IG Metall)"],
            ["Wahlvorstand", f"{w['vorsitz']} (i.A.), Mario Frank, Carolin Heimann"],
            ["Wahltermin", f"15.-17. Mai {jahr}"],
            ["Stimmberechtigte", f"{w['ma']} Beschaeftigte"],
            ["Wahlverfahren", "vereinfachtes Verfahren nicht zulaessig (>100 MA), reguläres Verfahren nach §§ 14 ff. BetrVG"],
            ["Sitze gesamt", f"{11 if w['ma']>500 else 9 if w['ma']>200 else 7}"],
        ]),
        ("Ablauf der Wahl",
         f"Die Wahl des Betriebsrats fand vom 15. bis 17. Mai {jahr} statt. Der Wahlvorstand hat die Wahl ordnungsgemaess vorbereitet (Wahlausschreiben am 8. Maerz {jahr}, Bekanntmachung der Vorschlagslisten am 18. April {jahr}). "
         f"Insgesamt wurden 4 Vorschlagslisten eingereicht: Liste 1 IG Metall (Spitzenkandidat {w['vorsitz']}), Liste 2 Vertrauensleute Produktion, Liste 3 Angestelltenliste Verwaltung/IT, Liste 4 Christliche Liste. "
         f"Die Stimmabgabe erfolgte in geheimer Wahl in drei Wahllokalen (Werkstattbuero, Verwaltung, Kantine). Briefwahl war fuer Schicht- und Aussendienst-Mitarbeitende moeglich."),
        ("Wahlergebnis (Sitzverteilung)",
         [["Liste", "Stimmen", "Anteil", "Sitze"],
          ["1 IG Metall", "612", "58,1 %", "6"],
          ["2 Vertrauensleute Produktion", "215", "20,4 %", "2"],
          ["3 Angestelltenliste", "168", "16,0 %", "2"],
          ["4 Christliche Liste", "58", "5,5 %", "1"],
          ["Summe gueltig", "1053", "100 %", "11"]]),
        ("Wahlbeteiligung",
         f"Die Wahlbeteiligung lag bei 82,4 % (1.053 gueltige Stimmen bei 1.278 Wahlberechtigten). Es gab 12 ungueltige Stimmen. Die Wahl verlief ohne Anfechtungsgrund i.S.d. § 19 BetrVG."),
        ("Konstituierende Sitzung",
         f"Der neugewaehlte Betriebsrat trat am 24. Mai {jahr} zur konstituierenden Sitzung zusammen. Gewaehlt wurden: "
         f"Vorsitz {w['vorsitz']} (11 von 11 Stimmen), stv. Vorsitz {w['stv']} (10/11), Schriftfuehrung {w['schrift']} (11/11). "
         f"Bestellt wurden Ausschuesse: Personalausschuss (5 Mitglieder), Wirtschaftsausschuss (3 Mitglieder), Arbeitsschutzausschuss (3 Mitglieder)."),
        ("Bekanntmachung und Anfechtungsfrist",
         f"Das Wahlergebnis wurde am 25. Mai {jahr} im Werk durch Aushang bekannt gemacht und an die Geschaeftsleitung uebermittelt. "
         f"Die Anfechtungsfrist nach § 19 BetrVG (2 Wochen ab Bekanntgabe) endet am 8. Juni {jahr}. Bisher keine Anfechtung eingegangen."),
        ("Unterschriften", signatures("Dr. Friederike Senn", "Wahlvorstandsvorsitz", "extern (IG Metall)",
                                       w["vorsitz"], "Vorsitz BR (neu gewaehlt)", w["name"],
                                       place=w["ort"], date_str_=f"24. Mai {jahr}")),
    ]
    return f"Protokoll Betriebsratswahl {jahr} – {w['name']}", sections


def unterrichtung_content(werk_key, jahr):
    w = WERKE[werk_key]
    sections = [
        ("Anlass und Adressaten",
         f"Die Geschaeftsleitung der {w['name']} unterrichtet hiermit den Betriebsrat – vertreten durch den Vorsitzenden {w['vorsitz']} – gemaess § 111 BetrVG ueber eine geplante Betriebsaenderung am Standort {w['ort']}."),
        ("Gegenstand der geplanten Betriebsaenderung",
         f"Beabsichtigt ist die Verlagerung der Vorfertigung von Steckverbindergehaeuse-Komponenten der Produktfamilie ICP-3 an den Standort Brno (RCZ). Die Massnahme betrifft am Standort {w['ort']} ca. 36 unmittelbar betroffene Arbeitsplaetze sowie mittelbar weitere 14 Arbeitsplaetze in Logistik und QS. "
         f"Hintergrund ist eine OEM-seitige Preisreduktionserwartung von 6,5 % p.a. (BMW Group, Kontrakt MK4711), die unter den derzeitigen Standortkosten in {w['ort']} nicht darstellbar ist."),
        ("Zeitplan und Meilensteine", [
            ["Meilenstein", "Termin"],
            ["Information BR und Konzern-BR", f"15. {MONTHS_DE[5]} {jahr}"],
            ["Beginn Verhandlungen Interessenausgleich/Sozialplan", f"22. {MONTHS_DE[5]} {jahr}"],
            ["Anzeige Massenentlassung BA", f"01. {MONTHS_DE[8]} {jahr}"],
            ["Beginn Verlagerung", f"01. {MONTHS_DE[10]} {jahr}"],
            ["Abschluss Verlagerung", f"31. {MONTHS_DE[3]} {jahr+1}"],
        ]),
        ("Wirtschaftliche Begruendung",
         f"Die Verlagerung soll eine Kostenreduktion von rund 2,8 Mio. EUR p.a. (vollumfaenglich realisiert ab GJ {jahr+1}) realisieren. Investitionsbedarf am Standort Brno: 4,2 Mio. EUR (Linie+ATE), Amortisation 18 Monate. "
         f"Die Geschaeftsleitung verweist auf die Konzernstrategie 'Operational Footprint 2030' und die Notwendigkeit, die EBITDA-Marge bis 2026 auf 12 % anzuheben (KPMG-Plan)."),
        ("Soziale Folgen und vorgesehene Massnahmen",
         "Beabsichtigt sind: (1) interne Stellenangebote an betroffene MA an anderen Linien, (2) Aufhebungsvertraege mit Abfindung gemaess konzernweitem Sozialplan-Rahmen (Faktor 1,3), (3) Transfergesellschaft 12 Monate, (4) Vorruhestandsregelung ab 58. Lebensjahr."),
        ("Beteiligungsrechte des Betriebsrats",
         "Die Geschaeftsleitung erkennt die Mitbestimmungsrechte des Betriebsrats nach §§ 111, 112 BetrVG und des Konzernbetriebsrats (KBR) an. Hinzugezogen wird auf Wunsch des BR ein Wirtschaftspruefer (Vorschlag Geschaeftsleitung: PwC, Vorschlag BR: BDO). "
         "Der Wirtschaftsausschuss wird in seiner naechsten Sitzung detailliert informiert."),
        ("Sachverstaendige", "Hinzuziehung von Beratern auf Kosten der Gesellschaft gemaess § 80 Abs. 3 BetrVG ist vereinbart. Kostenrahmen 35.000 EUR brutto."),
        ("Unterschriften", signatures(w["leitung"].split(" (")[0], "Werkleitung", w["name"],
                                       w["vorsitz"], "Vorsitz BR", w["name"],
                                       place=w["ort"], date_str_=f"15. {MONTHS_DE[5]} {jahr}")),
    ]
    return f"Unterrichtung Betriebsrat ueber Betriebsaenderung gemaess § 111 BetrVG ({jahr}) – {w['name']}", sections


def gbr_protokoll(jahr, q):
    sections = [
        ("Sitzungsdaten", [
            ["Datum", f"{15 + (q-1)*7}. {MONTHS_DE[q*3]} {jahr}"],
            ["Ort", "Stuttgart, Konzernzentrale Raum V.04"],
            ["Vorsitz", "Marlies Duerr (KBR-Vorsitz, IG Metall, AR-Mitglied)"],
            ["Stellv. Vorsitz", "Klaus Bauer (REG Heilbronn)"],
            ["Anwesend (Werks-BR-Vorsitze)", "Klaus Bauer (REG), Sabine Forster (RSG), Marek Tomaszewski (RPL, online), Tomas Prochazka (RCZ, online), Istvan Nagy (RHU, online), Christine Vogel (RHO, Schrift)"],
            ["Anwesend Geschaeftsleitung", "Anna Mueller (CEO), Laura Bauer (CFO, TOP 3), Petra Hartmann (HR Director)"],
            ["Beschlussfaehigkeit", "festgestellt"],
        ]),
        (f"TOP 1 — Konzernweite Personalplanung Q{q} {jahr}",
         f"Frau Hartmann berichtet zur konzernweiten Personalplanung. Stichtag {31 if q in (1,4) else 30}.{q*3:02d}.{jahr}: Gesamt-FTE 4.225 (Vorquartal 4.198, +27). "
         "Schwerpunkt-Einstellungen Softwareentwicklung RSG Muenchen (+18 ADAS-Engineers), Aufbau RCN Shanghai (+12 Sales/AE). "
         "Reduktion Stammbelegschaft REG Heilbronn (-8 fluktuationsbedingt nicht nachbesetzt). Diskussion zur strategischen Personalplanung 2025-2027 mit Schwerpunkt Software/AI-Skills."),
        (f"TOP 2 — Konzernweite Restrukturierung Footprint 2030",
         "CEO Anna Mueller stellt die konsolidierte Sicht der Footprint-Strategie 2030 vor. Schwerpunkte: Verlagerung Vorfertigung Steckverbinder von REG nach RCZ, Aufbau Battery-Cell-Pack-Endmontage in RPL Katowice, Reduktion Standort Stuttgart Verwaltung. "
         "Der KBR fordert die Einleitung formeller Interessenausgleichsverhandlungen je Standort und die Bildung einer konzernweiten Verhandlungskommission unter Beteiligung der IG Metall und Solidarnosc. "
         "Anna Mueller sagt entsprechende Konsultation zu, Beginn ab 01.07."),
        (f"TOP 3 — Wirtschaftliche Lage Konzern Q{q} {jahr}",
         f"CFO Laura Bauer berichtet zur wirtschaftlichen Lage: Konzernumsatz Q{q} {jahr} 158 Mio. EUR (PY 152 Mio., +4 %), EBITDA-Marge 12,1 %, Auftragsbestand 1.420 Mio. EUR (Reichweite 28 Monate). "
         "Frau Bauer verweist auf die Einhaltung aller Konsortialkredit-Covenants. Fragen aus dem KBR zur Investitionsplanung 2025 (Capex 78 Mio. EUR) werden ausfuehrlich beantwortet."),
        (f"TOP 4 — Beschluesse", ("list", [
            "Beschluss 1: Bildung einer konzernweiten Verhandlungskommission zur Begleitung 'Footprint 2030' (5 Mitglieder, je Standort plus Vorsitz Duerr).",
            "Beschluss 2: Auftrag an die Geschaeftsleitung, in der Sitzung des Wirtschaftsausschusses am 28. des Folgemonats die kumulierte Standortbilanz pro Werk vorzulegen.",
            "Beschluss 3: Verlaengerung der konzernweiten BV Mobile Arbeit um 12 Monate (alle Vorsitzenden einstimmig).",
            "Beschluss 4: Schulungsbeschluss fuer 8 KBR-Mitglieder zum Seminar 'EU-Whistleblower-RL Umsetzung Konzern' (Pichler Akademie, Berlin)."
        ])),
        ("TOP 5 — Verschiedenes",
         "Hinweis auf die kommende Sitzung des Aufsichtsrats am 12.10. (Frau Duerr als Arbeitnehmervertreterin). "
         "Hinweis auf den Bericht der KPMG ueber den Konzernabschluss; KBR fordert Vorlage des Management Letter. "
         "Frau Duerr schliesst die Sitzung um 17:45 Uhr. Naechste KBR-Sitzung in Heilbronn."),
        ("Unterschriften", signatures("Marlies Duerr", "KBR-Vorsitz", "Brennhagen Elektronik AG",
                                       "Christine Vogel", "Schriftfuehrung KBR", "RHO Stuttgart",
                                       place="Stuttgart", date_str_=f"{15 + (q-1)*7}. {MONTHS_DE[q*3]} {jahr}")),
    ]
    return f"Protokoll Konzernbetriebsrats-Sitzung Q{q} {jahr} – Brennhagen Elektronik AG", sections


def ebr_protokoll(jahr):
    sections = [
        ("Sitzungsdaten", [
            ["Datum", f"14.-16. November {jahr}"],
            ["Ort", "Bruessel, EBR-Sekretariat & Stuttgart (hybrid)"],
            ["EBR-Vorsitz", "Marlies Duerr (Stuttgart, IG Metall)"],
            ["Stellv. Vorsitz", "Marek Tomaszewski (Katowice, NSZZ Solidarnosc)"],
            ["Mitglieder", "11 Mitglieder aus DE (5), PL (2), CZ (2), HU (1), CN (Beobachter)"],
            ["Geschaeftsleitung", "Anna Mueller (CEO), Laura Bauer (CFO), Petra Hartmann (CHRO)"],
            ["Sekretariat", "Britta Hellmann, EBR-Buero Stuttgart"],
        ]),
        ("TOP 1 — Eroeffnung und Bericht des EBR-Vorsitzes",
         f"Frau Duerr eroeffnet die EBR-Jahrestagung {jahr} und begruesst alle Mitglieder, insbesondere die Vertreter der RHU Gyoer und der RCZ Brno, die im Vorjahr neu in den EBR gewaehlt wurden. "
         "Bericht zur Arbeit des engeren Ausschusses, monatliche Telefonkonferenzen, gemeinsame Massnahmen mit dem European Metalworkers Federation (industriAll Europe)."),
        ("TOP 2 — Geschaeftsentwicklung Konzern (CEO/CFO)",
         f"CEO Anna Mueller stellt die wesentlichen Eckdaten {jahr} vor: Konzernumsatz 612 Mio. EUR ({jahr-1}: 600 Mio.), EBITDA 74 Mio. EUR (Marge 12,1 %), Free Cashflow 41 Mio. EUR. "
         "Strategie 2030: Elektromobilitaet/BMS-Plattform, ADAS Level-2+/3 mit RSG, Aufbau Asien-Vertrieb RCN, Optimierung Footprint. "
         "CFO Laura Bauer ergaenzt zur Konsortialkredit-Refinanzierung 2027 und zu Sustainability-linked-Klauseln."),
        ("TOP 3 — Transnationale Restrukturierung 'Footprint 2030'",
         "Diskussion ueber die transnationalen Auswirkungen der angekuendigten Verlagerung von SMD-Vorfertigung. Der EBR fordert: (1) frueheste Information vor finalen Standortentscheidungen, (2) verbindliche Konsultation gemaess EBR-Vereinbarung 2019 Art. 8 mit Frist 6 Wochen, (3) Aufnahme einer transnationalen Sozialplan-Komponente. "
         "Geschaeftsleitung sagt frueherzeitige Information und Konsultation zu."),
        ("TOP 4 — Gesundheit und Sicherheit",
         "Bericht der Sicherheitsfachkraefte aller Werke. Unfallhaeufigkeit (LTIFR) Konzern 4,8 (PY 5,2). Ziel 2025: <4,0. Schwerpunkte: Maschinensicherheit (RPL), Ergonomie Montage (REG), psychische Belastung Software (RSG). "
         "Diskussion zur Einfuehrung einer konzernweiten Anonymous-Reporting-Plattform fuer Beinaheunfaelle und sicherheitskritische Beobachtungen."),
        ("TOP 5 — Gleichstellung und ESG",
         f"Frauenanteil in Fuehrungspositionen Konzern {jahr}: 24 % (PY 21 %). Ziel 30 % bis 2027. Diskussion der ESG-KPIs aus dem Nachhaltigkeitsbericht (CSRD-konform ab 2024). "
         "Anregung des EBR: konzernweite Pay-Gap-Analyse mit Veroeffentlichung ab Berichtsjahr 2025."),
        ("TOP 6 — Beschluesse", ("list", [
            "Verlaengerung der EBR-Vereinbarung 2019 bis zum 31.12.2027 (einstimmig).",
            "Antrag an die Geschaeftsleitung zur Bereitstellung eines transnationalen Sozialfonds 500.000 EUR fuer Qualifizierung im Kontext der Transformation.",
            "Einrichtung eines staendigen Ausschusses 'Digitale Transformation und KI am Arbeitsplatz' (5 Mitglieder).",
            "Schulungsplan EBR 2025: 3 Treffen jaehrlich, Schwerpunkt EU-Lieferkettengesetz und AI-Act."
        ])),
        ("Unterschriften", signatures("Marlies Duerr", "EBR-Vorsitz", "Brennhagen Elektronik AG",
                                       "Marek Tomaszewski", "stv. EBR-Vorsitz", "RPL Katowice",
                                       place="Bruessel", date_str_=f"16. November {jahr}")),
    ]
    return f"Protokoll Europaeischer Betriebsrat (EBR) – Jahrestagung {jahr}", sections


def ebr_vereinbarung_2019():
    sections = [
        ("Praeambel",
         "Die Brennhagen Elektronik AG (besondere Verhandlungsgruppe BVG) und die im Geltungsbereich beschaeftigten Arbeitnehmervertretungen der europaeischen Konzerngesellschaften (DE, PL, CZ, HU) vereinbaren auf Grundlage der Richtlinie 2009/38/EG und des Europaeischen-Betriebsraete-Gesetzes (EBRG) die Errichtung eines Europaeischen Betriebsrats (EBR)."),
        ("§§ 1-12 Verfahren", ("clauses", [
            ("§ 1 Geltungsbereich", [
                "Diese Vereinbarung gilt fuer alle Beschaeftigten der gemeinschaftsweit operierenden Brennhagen-Gruppe in den Mitgliedstaaten der EU und des EWR.",
                "Erfasste Gesellschaften: REA (Stuttgart), REG (Heilbronn), RSG (Muenchen), RPL (Katowice), RCZ (Brno), RHU (Gyoer), RHO (Stuttgart).",
            ]),
            ("§ 2 Zusammensetzung des EBR", [
                "Der EBR besteht aus 11 ordentlichen Mitgliedern: DE 5 (REA/REG/RSG/RHO je nach Belegschaft), PL 2 (RPL), CZ 2 (RCZ), HU 1 (RHU), zzgl. CN als Beobachter (RCN).",
                "Die Sitzverteilung wird alle 4 Jahre an die Belegschaftsentwicklung angepasst.",
            ]),
            ("§ 3 Amtszeit", ["Die Amtszeit der EBR-Mitglieder betraegt 4 Jahre. Eine Wiederwahl ist zulaessig."]),
            ("§ 4 Vorsitz und engerer Ausschuss", [
                "Der EBR waehlt aus seiner Mitte einen Vorsitzenden und einen Stellvertreter (mindestens aus zwei verschiedenen Mitgliedstaaten).",
                "Der engere Ausschuss besteht aus 5 Mitgliedern (DE 2, PL 1, CZ 1, HU 1).",
            ]),
            ("§ 5 Unterrichtung und Anhoerung", [
                "Die zentrale Leitung unterrichtet den EBR rechtzeitig und umfassend ueber alle Angelegenheiten von transnationaler Bedeutung.",
                "Insbesondere: wirtschaftliche und finanzielle Lage, Struktur und Beschaeftigung, Investitionen, wesentliche Aenderungen Organisation, Verlagerungen, Massenentlassungen, neue Produktionsmethoden.",
            ]),
            ("§ 6 Konsultationsverfahren", [
                "Bei Massnahmen mit erheblichen Auswirkungen auf die Interessen der Arbeitnehmer findet eine foermliche Konsultation mit einer Antwortfrist von 6 Wochen statt.",
                "Die zentrale Leitung beruecksichtigt die Stellungnahme bei der finalen Entscheidung; abweichende Entscheidungen sind zu begruenden.",
            ]),
            ("§ 7 Ordentliche Sitzungen", [
                "Der EBR tagt mindestens einmal jaehrlich mit der zentralen Leitung (Jahrestagung).",
                "Ausserordentliche Sitzungen werden auf Antrag des engeren Ausschusses oder bei aussergewoehnlichen Umstaenden einberufen.",
            ]),
            ("§ 8 Sachverstaendige", ["Der EBR kann Sachverstaendige hinzuziehen. Die Kosten von zwei Sachverstaendigen je Jahr werden von der zentralen Leitung getragen."]),
            ("§ 9 Vertraulichkeit", ["Die Mitglieder sind zur Wahrung der Vertraulichkeit verpflichtet, soweit Informationen ausdruecklich als vertraulich gekennzeichnet sind."]),
            ("§ 10 Freistellung und Kosten", ["Die Mitglieder werden fuer die Dauer der Sitzungen einschliesslich Vorbereitung und An-/Abreise von der Arbeit unter Fortzahlung der Verguetung freigestellt."]),
            ("§ 11 Schulung", ["Jedes EBR-Mitglied hat Anspruch auf Schulung im Umfang von 5 Tagen pro Jahr, finanziert von der zentralen Leitung."]),
            ("§ 12 Inkrafttreten, Laufzeit", [
                "Diese Vereinbarung tritt am 1. Juni 2019 in Kraft.",
                "Sie laeuft 4 Jahre und verlaengert sich automatisch um jeweils 4 Jahre, falls nicht 6 Monate vor Ablauf gekuendigt.",
                "Im Falle einer Kuendigung gelten die subsidiaeren Vorschriften des EBRG fort.",
            ]),
        ])),
        ("Unterschriften", signatures("Dr. Holger Roehm", "Vorsitzender Vorstand (i.D.)", "Brennhagen Elektronik AG",
                                       "Marlies Duerr", "Sprecherin BVG / EBR-Vorsitz", "Konzernbetriebsrat",
                                       place="Stuttgart", date_str_="3. Mai 2019")),
    ]
    return "Vereinbarung zur Errichtung eines Europaeischen Betriebsrats (EBR) – Brennhagen Elektronik AG", sections


# ── Special files

def jahresgespraech_content():
    sections = [
        ("Gespraechsdaten", [
            ["Mitarbeiterin", "Gisela Roth (Pers-Nr. 106)"],
            ["Position", "Sachbearbeiterin Personal, REG Heilbronn"],
            ["Vorgesetzte", "Petra Hartmann (HR Director)"],
            ["Gespraechsdatum", "12. Dezember 2023"],
            ["Betriebszugehoerigkeit", "seit 1. April 1998 (25 Jahre)"],
            ["Eingruppierung", "ERA EG 8"],
        ]),
        ("Rueckblick 2023",
         "Frau Roth hat die ihr uebertragenen Aufgaben in der Personalverwaltung zuverlaessig und in hoher Qualitaet erledigt. Hervorzuheben sind die selbststaendige Bearbeitung der Eingruppierungsantraege fuer den Bereich Produktion und die kompetente Begleitung der Tarifrunde Metall- und Elektroindustrie 2023."),
        ("Zielerreichung",
         "Alle vereinbarten Ziele 2023 wurden zu mindestens 95 % erreicht. Die im Mitarbeitergespraech 2022 vereinbarte Weiterbildung 'SAP HCM Advanced' wurde im Maerz 2023 erfolgreich abgeschlossen."),
        ("Ziele 2024", ("list", [
            "Mitwirkung bei der Einfuehrung des neuen HR-Systems Workday (Go-Live 01.07.2024).",
            "Mentoring fuer zwei neue Kolleginnen im Team Personalverwaltung.",
            "Teilnahme am Seminar 'AGG-konforme Eingruppierung' (Pichler Akademie, 2 Tage).",
            "Vorbereitung des Renteneintritts (geplant 30.06.2025) – schrittweise Uebergabe der Aufgaben.",
        ])),
        ("Wuensche der Mitarbeiterin",
         "Frau Roth wuenscht eine Reduktion der Arbeitszeit auf 32 Stunden/Woche ab 1.7.2024 im Rahmen der Altersteilzeit-Vereinbarung. Antrag wird mit HR-Director bis 31.1.2024 bearbeitet."),
        ("Vereinbarungen und Unterschriften",
         signatures("Petra Hartmann", "HR Director", "REG Heilbronn",
                    "Gisela Roth", "Mitarbeiterin", "REG Heilbronn",
                    place="Heilbronn", date_str_="12. Dezember 2023")),
    ]
    return "Jahresgespraech 2023 – Gisela Roth (Pers-Nr. 106)", sections


def prj_statusbericht_bms():
    sections = [
        ("Projektstammdaten", [
            ["Projekt-Nr.", "PRJ-2022-001"],
            ["Titel", "BatteryMS-12 EV-Plattform (BMS-12, VW ID.7 / Hyundai E-GMP)"],
            ["Berichtsmonat", "Mai 2022"],
            ["Projektleitung", "Lars Wittmann (RSG Muenchen)"],
            ["Lenkungskreis", "Dr. Thomas Weber (COO), Stefan Hoffmann (CTO)"],
            ["Budget", "12,8 Mio. EUR (Phase A+B)"],
        ]),
        ("Statusampel (RAG)", [
            ["Bereich", "Status", "Trend"],
            ["Termine", "GELB", "verbessert"],
            ["Budget", "GRUEN", "stabil"],
            ["Qualitaet", "GRUEN", "stabil"],
            ["Ressourcen", "GELB", "stabil"],
            ["Risiken", "GELB", "verschlechtert (Halbleiter)"],
        ]),
        ("Arbeitspakete Mai 2022",
         "AP4.2 Funktionssicherheits-Konzept (ASIL-D) – abgeschlossen und durch TUEV SUED abgenommen. AP5.1 Software-Architektur Cell-Monitoring – on track, Release v0.7 verfuegbar. AP6.3 Hardware-A-Muster – Verzoegerung 2 Wochen wegen NXP-Allokation, Workaround via Lieferantenwechsel CC-Sensor (Texas Instruments). "
         "AP7.1 EMV-Vorpruefung – erfolgreich (Bereich 50 MHz - 6 GHz nach ISO 11452-2). AP8.2 Funktionstest bei -40°C bis +85°C – durchlaufen mit 2 minor findings."),
        ("Wesentliche Risiken", ("list", [
            "R1 (rot): NXP MC33775 Allokation, Risiko 4 Wochen Verzug ab August; Massnahme Dual Sourcing TI BQ79616-Q1.",
            "R2 (gelb): Personalengpass Software-Validierung (3 FTE fehlend); Massnahme Ramp-up via Capgemini Engineering.",
            "R3 (gelb): Verschaerfung ISO 26262-Anforderung durch Hyundai; geplante Pruefung 6/2022.",
        ])),
        ("Budget-Status",
         "Ist 5,2 Mio. EUR von 12,8 Mio. EUR (40,6 %), Plan 5,4 Mio. EUR. Leichte Unterschreitung durch verzoegerten Hardwarekauf, Aufholung 6/2022 erwartet."),
        ("Naechste Meilensteine",
         "M07 A-Muster-Auslieferung VW (24.6.2022), M08 EMV-Vollpruefung (15.7.2022), M09 ASIL-Assessment durch TUEV SUED (12.8.2022), M10 Funktionstest EOL Linie Heilbronn (30.9.2022)."),
        ("Berichterstattung",
         signatures("Lars Wittmann", "Projektleitung BMS-12", "RSG Muenchen",
                    "Dr. Thomas Weber", "COO / Lenkungskreis", "Brennhagen Elektronik AG",
                    place="Muenchen", date_str_="31. Mai 2022")),
    ]
    return "Projektstatusbericht Mai 2022 – BatteryMS-12 EV-Plattform", sections


def prj_testbericht_bms():
    sections = [
        ("Pruefgegenstand", [
            ["Projekt-Nr.", "PRJ-2022-001"],
            ["Pruefling", "BMS-12 EV-Plattform, Hardware-Variante HV3.2, Software v1.1.4-RC2"],
            ["Pruefart", "Funktionstest EOL (End-of-Line) Linie 4 REG Heilbronn"],
            ["Pruefdatum", "12.-14. September 2022"],
            ["Pruefer", "Sabine Brand (Q-Leitung REG), Markus Reiter (PV), Lars Wittmann (PL Software)"],
            ["Pruefnorm", "ISO 26262-6 (ASIL-D), IEC 61508, Spec BMS-12-FT-2022-09"],
        ]),
        ("Pruefumfang",
         "Vollumfaenglicher EOL-Funktionstest aller 12 Cell-Monitoring-Channels, CAN-FD Kommunikation (5 Mbit/s), Insulation Monitoring (Riso > 100 kOhm), Pre-Charge-Logik, Schuetz-Ansteuerung, Diagnose nach UDS. "
         "Pruefumfang umfasste 24 Pruefszenarien gemaess Pruefspezifikation BMS-12-FT-2022-09."),
        ("Pruefergebnisse",
         [["Pruefpunkt", "Sollwert", "Istwert", "Status"],
          ["Zellspannungsmessgenauigkeit", "± 5 mV @ 3.0-4.2 V", "± 3.8 mV", "i.O."],
          ["Stromsensor-Linearitaet", "± 0,5 % FS", "± 0,32 % FS", "i.O."],
          ["CAN-FD Latenz", "< 2 ms", "1,2 ms", "i.O."],
          ["Insulation Detection", "< 100 ms", "85 ms", "i.O."],
          ["Pre-Charge Time", "200-300 ms", "245 ms", "i.O."],
          ["Schuetz-Schaltzeit", "< 15 ms", "12,3 ms", "i.O."],
          ["Temperaturmessung", "± 2 K @ -20...+60°C", "± 1,7 K", "i.O."],
          ["UDS Sec-Access", "ISO 14229", "konform", "i.O."]]),
        ("Befunde und Massnahmen",
         "Befund 1 (minor): Aufwaermphase Cell-Monitoring-IC dauert 480 ms statt spezifizierten 400 ms (delta +20 %). Massnahme: Anpassung der Spec-Toleranz auf 500 ms bei naechstem Release. "
         "Befund 2 (info): Kommunikationsfehler bei einmaliger CAN-Bus-Stoerung von 250 ms Dauer; Recovery innerhalb von 80 ms. Spec entspricht."),
        ("Pruefurteil",
         "Der Pruefling erfuellt alle wesentlichen Anforderungen der Pruefspezifikation. Empfehlung: Freigabe fuer Pilot-Serienfertigung (PPAP-Level 3) mit Auflage zur Anpassung der Aufwaermzeit-Toleranz in Release v1.1.5."),
        ("Unterschriften", signatures("Sabine Brand", "Q-Leitung REG", "REG Heilbronn",
                                       "Lars Wittmann", "Projektleitung Software", "RSG Muenchen",
                                       place="Heilbronn", date_str_="15. September 2022")),
    ]
    return "Funktionstest EOL Pruefbericht – BMS-12 EV-Plattform", sections


def prj_gate_g3_lksg():
    sections = [
        ("Gate-Daten", [
            ["Projekt-Nr.", "PRJ-2024-004"],
            ["Titel", "LkSG Supply Chain Audit Plattform – Detailentwicklung"],
            ["Gate", "G3 (Ende Detailentwicklung, vor Pilotbetrieb)"],
            ["Datum", "18. April 2024"],
            ["Sponsor", "Dr. Heike Berger (CCO Tax/Compliance)"],
            ["Projektleitung", "Andreas Buehler (CAE) und Britta Hellmann (Compliance Officer)"],
            ["Budget", "1,4 Mio. EUR (kumuliert 1,1 Mio. EUR ausgegeben)"],
        ]),
        ("Bewertung der Deliverables",
         "Deliverable D3.1 Risikoanalyse-Modell (alle 5 Werke + 240 Tier-1 Lieferanten) – freigegeben. "
         "Deliverable D3.2 Verfahrensanweisung 'Sorgfaltspflichten gemaess LkSG' – freigegeben. "
         "Deliverable D3.3 Software-Modul SAP-Ariba Connector – freigegeben mit Auflage Penetration-Test. "
         "Deliverable D3.4 Beschwerdeverfahren (Whistleblower-Channel via integrityline.com) – freigegeben."),
        ("Kriterien G3 Erfuellung", ("list", [
            "Detailspezifikation vollstaendig und freigegeben (ja).",
            "Risiko-Assessment durchgefuehrt und priorisierter Massnahmenplan vorhanden (ja).",
            "Compliance-Pruefung BAFA-Vorgaben (Bundesamt fuer Wirtschaft und Ausfuhrkontrolle): bestanden.",
            "Anbindung an HR/Beschwerde-Prozesse abgestimmt mit Konzernbetriebsrat (KBR Beschluss vom 12.4.).",
            "Schulungskonzept fuer Einkauf, HR, Compliance verabschiedet (200 MA-Tage 2024).",
        ])),
        ("Risiken und Massnahmen",
         "R1 (gelb): Datenqualitaet Lieferantenstammdaten in SAP MM (DE/PL/CZ) heterogen; Massnahme: Cleansing-Projekt mit IT, Frist 30.6.2024. "
         "R2 (gruen): Akzeptanz Whistleblower-Kanal in CZ/HU; Massnahme: zusaetzliche lokalsprachliche Schulung. "
         "R3 (gelb): BAFA-Update zu Berichtspflichten Q3 2024 – Anpassung notwendig."),
        ("Entscheidung Gate G3",
         "Der Lenkungskreis (Anna Mueller, Dr. Thomas Weber, Dr. Heike Berger) genehmigt das Gate G3. Freigabe zur Pilotphase ab 1.5.2024 mit 25 ausgewaehlten Tier-1-Lieferanten (BMW-relevant). Vollroll-out ab 1.10.2024."),
        ("Unterschriften", signatures("Andreas Buehler", "Projektleitung / CAE", "Brennhagen Elektronik AG",
                                       "Dr. Heike Berger", "Sponsor / Group Tax+Compliance", "Brennhagen Elektronik AG",
                                       place="Stuttgart", date_str_="18. April 2024")),
    ]
    return "Gate G3 Detailentwicklung – LkSG Supply Chain Audit", sections


def rcn_ic_rechnung():
    sections = [
        ("Rechnungsdaten", [
            ["Rechnungs-Nr.", "RCN-IC-2020-0412"],
            ["Datum", "30. April 2020"],
            ["Leistungserbringer", "Brennhagen (Shanghai) Co. Ltd. (RCN), Zhongshan Park, Pudong, Shanghai 200122"],
            ["Empfaenger", "Brennhagen Holding GmbH (RHO), Vaihinger Strasse 120, 70567 Stuttgart"],
            ["Leistungszeitraum", "01.-30. April 2020"],
            ["Currency", "EUR (Funktionalwaehrung RHO)"],
        ]),
        ("Leistungsbeschreibung",
         "Lokale Vertriebsdienstleistungen Asien-Pazifik gemaess Intercompany-Service-Agreement vom 1.1.2018. "
         "Umfasst Market-Intelligence, Kundenbetreuung BAIC/Geely/CATL, Trade-Show-Vertretung, Aftermarket-Support. "
         "Verrechnung erfolgt nach Cost-Plus-Methode (Markup 8 % auf Vollkosten) gemaess TP-Local-File Kapitel 4."),
        ("Rechnungsbetrag",
         [["Position", "Betrag (EUR)"],
          ["Vollkosten Sales-Aktivitaeten 04/2020", "98.450,00"],
          ["Davon: Personalkosten", "62.300,00"],
          ["Davon: Reise und Repraesentation", "8.200,00"],
          ["Davon: Buero und Overhead", "21.800,00"],
          ["Davon: Marketing-Anteil", "6.150,00"],
          ["Markup 8 %", "7.876,00"],
          ["Zwischensumme", "106.326,00"],
          ["VAT (Reverse-Charge B2B, keine VAT)", "0,00"],
          ["Rechnungsbetrag gesamt", "106.326,00"]]),
        ("Zahlungsbedingungen",
         "Zahlbar binnen 30 Tagen netto auf Konto Bank of China Shanghai Branch, IBAN CN10 0067 8901 2345 6789 01, SWIFT BKCHCNBJ300. "
         "Skonto entfaellt (Intercompany). Verrechnung im Cash-Pooling moeglich."),
        ("Transfer-Pricing-Vermerk",
         "Diese Rechnung steht im Einklang mit dem konzernweiten Verrechnungspreis-Konzept (TP-Local-File 2019, KPMG-Dokumentation). "
         "Cost-Plus-Markup 8 % entspricht der Bandbreite vergleichbarer Routine-Service-Distributoren (Interquartilsbandbreite 5-12 %, Median 8,5 %, RoyaltyStat-Studie 2019)."),
        ("Aussteller und Genehmigung",
         "Ausstellende Gesellschaft: Brennhagen (Shanghai) Co. Ltd., Country Manager Zhang Hao, Finance Manager Liang Wei. "
         "Stempel und elektronische Unterschrift digital ueber Coupa-Workflow. "
         "Interne Genehmigung gemaess Konzern-Richtlinie Intercompany 2018-IC-01 (Sign-off CFO Laura Bauer, RHO Stuttgart). "
         "Buchung erfolgt SAP-Profitcenter PC-RCN-SALES, Sachkonto 6310 IC-Service-Aufwand, gegen Forderung Konto 1361 (RCN-RHO)."),
        ("Konformitaetsvermerk",
         "Die Rechnung entspricht den Anforderungen des UStG (§§ 14, 14a) sowie den OECD Transfer Pricing Guidelines (Kapitel VII Konzernsdienstleistungen). "
         "KPMG hat die Methode im Rahmen der TP-Dokumentation 2019 als arm's length bestaetigt."),
    ]
    return "Intercompany-Rechnung RCN -> RHO – April 2020", sections


def widerspruch_content():
    sections = [
        ("Verfahrensdaten", [
            ["Az.", "Rechtsakte 2023/003"],
            ["Verfahrensart", "Widerspruch gegen Eingruppierung / Arbeitsrechtlicher Streit"],
            ["Klaegerin", "Frau M. K. (anonymisiert), Sachbearbeiterin Logistik, REG Heilbronn"],
            ["Beklagte", "Brennhagen Elektronik GmbH (REG), Heilbronn"],
            ["Rechtsanwalt Klaegerin", "RA Tim Beckmann, Beckmann & Kollegen, Stuttgart"],
            ["Rechtsanwalt REG", "RA Dr. Caroline Walther, Hengeler Mueller, Frankfurt"],
            ["Datum Widerspruch", "14. November 2023"],
        ]),
        ("Sachverhalt",
         "Die Klaegerin ist seit 2017 bei der REG beschaeftigt, zuletzt in der Logistik-Disposition. Sie wurde 2017 in ERA EG 7 eingruppiert. Nach der Versetzung in den Bereich 'Internationale Disposition' (Schwerpunkt Zollabwicklung CN/USA) am 1.6.2022 verblieb die Eingruppierung in EG 7. "
         "Die Klaegerin beantragte am 12.9.2023 die Hochgruppierung in EG 9 mit Verweis auf die wesentlich gestiegene Komplexitaet der Aufgabe (Zoll, Praeferenzursprung, Embargo-Pruefung)."),
        ("Stellungnahme REG (HR)",
         "HR vertritt die Position, dass die Taetigkeit der Klaegerin der Eingruppierung in EG 7 (Facharbeiterniveau mit Spezialwissen) entspricht. Die internationale Komponente wurde bereits durch die EG 7 mit Zulage angemessen abgegolten. "
         "Die paritaetische Eingruppierungskommission ist am 8.11.2023 zu keinem Konsens gekommen (BR-Position: EG 9, AG-Position: EG 7)."),
        ("Rechtliche Bewertung",
         "Massgeblich ist die ERA-Bewertungsmethode, insbesondere die Anforderungsprofile Wissen, Denken, Verantwortung, Kommunikation und Mitarbeiterfuehrung. "
         "Mit Schreiben vom 14.11.2023 hat die Klaegerin formell Widerspruch eingelegt und Klage vor dem Arbeitsgericht Heilbronn angedroht, falls keine Einigung erzielt wird. "
         "Die Eingruppierungskommission wird neu einberufen unter Hinzuziehung eines externen Gutachters (Dr. Holger Schramm, ERA-Sachverstaendiger)."),
        ("Verfahrensvorschlag",
         "(1) Externer Gutachter erstellt schriftliche Bewertung bis 31.1.2024. (2) Gemeinsame Verhandlung in 14 Tagen nach Vorlage Gutachten. (3) Falls keine Einigung: Schlichtungsverfahren gemaess BV ERA, danach Klage vor ArbG Heilbronn moeglich."),
        ("Unterschriften", signatures("RA Tim Beckmann", "Rechtsanwalt Klaegerin", "Beckmann & Kollegen Stuttgart",
                                       "Petra Hartmann", "HR Director", "REG Heilbronn",
                                       place="Heilbronn", date_str_="14. November 2023")),
    ]
    return "Widerspruch Eingruppierung – Arbeitsrechtlicher Vorgang Az. 2023/003", sections


# ── Now plan the file mapping
# Lists for protokolle: parse filenames in folder

import re

def parse_filename(name):
    """Return (kind, werk, jahr, monat_or_other) or None for special files."""
    m = re.match(r"^(REG|RSG|RPL|RCZ|RHU|RHO)_BR_Protokoll_(\d{4})_(\d{2})(?:_.*)?\.docx$", name)
    if m:
        return ("br_protokoll", m.group(1), int(m.group(2)), int(m.group(3)))
    m = re.match(r"^(REG|RSG|RPL|RCZ|RHU|RHO)_BR_Korrespondenz_([A-Za-z_]+?)_(\d{4})(?:_.*)?\.docx$", name)
    if m:
        thema = m.group(2).rstrip("_")
        return ("br_korr", m.group(1), int(m.group(3)), thema)
    m = re.match(r"^(REG|RSG|RPL|RCZ|RHU|RHO)_BR_Unterrichtung_Betriebsaenderung_(\d{4})\.docx$", name)
    if m:
        return ("br_unterr", m.group(1), int(m.group(2)), None)
    m = re.match(r"^(REG|RSG|RPL|RCZ|RHU|RHO)_BR_Wahl_(\d{4})_Protokoll\.docx$", name)
    if m:
        return ("br_wahl", m.group(1), int(m.group(2)), None)
    m = re.match(r"^(REG|RSG|RPL|RCZ|RHU|RHO)_BV_([A-Za-z]+)(.*?)_(\d{4})(?:_.*)?\.docx$", name)
    if m:
        return ("bv", m.group(1), int(m.group(4)), m.group(2))
    m = re.match(r"^REA_GBR_Protokoll_(\d{4})_Q(\d)\.docx$", name)
    if m:
        return ("gbr", None, int(m.group(1)), int(m.group(2)))
    m = re.match(r"^REA_EBR_Jahrestagung_(\d{4})_Protokoll\.docx$", name)
    if m:
        return ("ebr", None, int(m.group(1)), None)
    if name == "REA_EBR_Vereinbarung_2019.docx":
        return ("ebr_vereinb", None, 2019, None)
    if name == "JG_106_Gisela_Roth_106_2023.docx":
        return ("jg_roth", None, 2023, None)
    if name.startswith("PRJ-2022-001_Statusbericht_2022_05"):
        return ("prj_status", None, 2022, None)
    if name.startswith("PRJ-2022-001_Testbericht_Funktionstest_EOL"):
        return ("prj_test", None, 2022, None)
    if name.startswith("PRJ-2024-004_Gate_G3"):
        return ("prj_gate", None, 2024, None)
    if name.startswith("RCN_IC_Rechnung_2020_04"):
        return ("rcn_ic", None, 2020, None)
    if name == "Rechtsakte_2023_003_Widerspruch.docx":
        return ("widerspruch", None, 2023, None)
    return None


# ── Map thema short → key in BV_THEMES (handle name variations)
BV_KEY_MAP = {
    "Arbeitszeit": "Arbeitszeit",
    "Homeoffice": "Homeoffice",
    "Betriebliche": "Betriebliche_Altersversorgung",
    "Betriebliches": "Betriebliches",
    "Entgeltrahmenabkommen": "Entgeltrahmenabkommen",
    "Essenszuschuss": "Essenszuschuss",
    "Gesundheitsschutz": "Gesundheitsschutz",
    "Gleichstellung": "Gleichstellung",
    "IT": "IT",
    "Kurzarbeitsregelung": "Kurzarbeitsregelung",
    "Leistungs": "Leistungs",
    "Parkplatzregelung": "Parkplatzregelung",
    "Schichtbetrieb": "Schichtbetrieb",
    "Sozialer": "Sozialer",
    "Urlaubsplanung": "Urlaubsplanung",
    "Weiterbildung": "Weiterbildung",
}

KORR_KEY_MAP = {
    "Arbeitszeit_Widerspruch": "Arbeitszeit_Widerspruch",
    "Betriebsaenderung_Interessenausgleich": "Betriebsaenderung_Interessenausgleich",
    "Eingruppierungsstreitigkeiten": "Eingruppierungsstreitigkeiten",
    "Massenentlassung_Anzeige": "Massenentlassung_Anzeige",
    "Personalplanung": "Personalplanung",
    "Sozialplan_2023": "Sozialplan_2023",
    "Ueberstundenregelung": "Ueberstundenregelung",
}


def title_for_protokoll(werk_key, jahr, monat):
    return f"BR-Sitzungsprotokoll {MONTHS_DE[monat]} {jahr} – {WERKE[werk_key]['name']} ({WERKE[werk_key]['ort']})"


def title_for_bv(theme_key, werk_key, jahr):
    w = WERKE[werk_key]
    title, _ = BV_THEMES[theme_key]
    return f"{title} – {w['name']} ({jahr})"


def title_for_unterr(werk_key, jahr):
    return f"Unterrichtung Betriebsrat Betriebsaenderung gemaess § 111 BetrVG ({jahr}) – {WERKE[werk_key]['name']}"


def main():
    files = sorted(BASE.glob("*.docx"))
    written = 0
    skipped = []
    for fp in files:
        info = parse_filename(fp.name)
        if not info:
            skipped.append(fp.name)
            continue
        kind = info[0]
        if kind == "br_protokoll":
            _, werk, jahr, monat = info
            sections = br_protokoll(werk, jahr, monat)
            write_doc(fp, WERKE[werk]["hdr"], title_for_protokoll(werk, jahr, monat), sections)
        elif kind == "br_korr":
            _, werk, jahr, thema = info
            key = None
            # match longest prefix
            for k in sorted(KORR_KEY_MAP.keys(), key=len, reverse=True):
                if thema.startswith(k):
                    key = k
                    break
            if key is None:
                # fallback to generic personalplanung
                key = "Personalplanung"
            title, sections = korr_content(key, werk, jahr)
            write_doc(fp, WERKE[werk]["hdr"], title, sections)
        elif kind == "br_unterr":
            _, werk, jahr, _ = info
            title, sections = unterrichtung_content(werk, jahr)
            write_doc(fp, WERKE[werk]["hdr"], title, sections)
        elif kind == "br_wahl":
            _, werk, jahr, _ = info
            title, sections = wahl_protokoll(werk, jahr)
            write_doc(fp, WERKE[werk]["hdr"], title, sections)
        elif kind == "bv":
            _, werk, jahr, theme_prefix = info
            # map to BV key
            key = None
            for k in sorted(BV_KEY_MAP.keys(), key=len, reverse=True):
                if theme_prefix.startswith(k):
                    key = BV_KEY_MAP[k]
                    break
            if key is None:
                key = "Arbeitszeit"
            title, clauses = bv_content(key, werk, jahr)
            sections = [
                ("Praeambel und Parteien",
                 f"Zwischen der {WERKE[werk]['name']}, vertreten durch die Werkleitung ({WERKE[werk]['leitung']}), und dem Betriebsrat der {WERKE[werk]['name']}, vertreten durch den Vorsitzenden {WERKE[werk]['vorsitz']}, wird auf Grundlage des Betriebsverfassungsgesetzes (BetrVG) und in Anwendung der einschlaegigen Mitbestimmungstatbestaende die nachfolgende Betriebsvereinbarung geschlossen."),
                ("Regelungen", clauses),
                ("Unterschriften", signatures(WERKE[werk]["leitung"].split(" (")[0], "Werkleitung", WERKE[werk]["name"],
                                              WERKE[werk]["vorsitz"], "Vorsitz Betriebsrat", WERKE[werk]["name"],
                                              place=WERKE[werk]["ort"], date_str_=f"1. Januar {jahr}")),
            ]
            write_doc(fp, WERKE[werk]["hdr"], title, sections)
        elif kind == "gbr":
            _, _, jahr, q = info
            title, sections = gbr_protokoll(jahr, q)
            write_doc(fp, H_REA, title, sections)
        elif kind == "ebr":
            _, _, jahr, _ = info
            title, sections = ebr_protokoll(jahr)
            write_doc(fp, H_REA, title, sections)
        elif kind == "ebr_vereinb":
            title, sections = ebr_vereinbarung_2019()
            write_doc(fp, H_REA, title, sections)
        elif kind == "jg_roth":
            title, sections = jahresgespraech_content()
            write_doc(fp, H_REG, title, sections)
        elif kind == "prj_status":
            title, sections = prj_statusbericht_bms()
            write_doc(fp, H_REA, title, sections)
        elif kind == "prj_test":
            title, sections = prj_testbericht_bms()
            write_doc(fp, H_REA, title, sections)
        elif kind == "prj_gate":
            title, sections = prj_gate_g3_lksg()
            write_doc(fp, H_REA, title, sections)
        elif kind == "rcn_ic":
            title, sections = rcn_ic_rechnung()
            write_doc(fp, H_RHO, title, sections)
        elif kind == "widerspruch":
            title, sections = widerspruch_content()
            write_doc(fp, H_REG, title, sections)
        else:
            skipped.append(fp.name)
            continue
        written += 1
    print(f"Written: {written}")
    if skipped:
        print(f"Skipped ({len(skipped)}):")
        for s in skipped[:20]:
            print("  ", s)


if __name__ == "__main__":
    main()
