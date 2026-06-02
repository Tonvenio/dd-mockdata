"""Brennhagen AG / 00_Konzernstruktur_Holding (66 thin) + 01_AG_Gesellschaftsrecht remnants (7 thin)."""
# --- portable-paths-prelude --- (do not edit) ---
import sys
from pathlib import Path as _PathlibPath
_RP = _PathlibPath(__file__).resolve().parent
while not (_RP / "enhance_lib.py").exists() and _RP.parent != _RP:
    _RP = _RP.parent
_ROOT = _RP
sys.path.insert(0, str(_ROOT))
# --- end prelude ---
from enhance_lib import ROEHRIG_AG as R, ROEHRIG_SUBS as S, write_doc, signatures

B00 = f"{_ROOT}/roehrig_large/00_Konzernstruktur_Holding"
B01 = f"{_ROOT}/roehrig_large/01_AG_Gesellschaftsrecht"
H = {"name": R["name"], "addr": R["addr"], "hrb": R["hrb"]}
RHO = {"name": "Brennhagen Holding GmbH",
       "addr": "Vaihinger Straße 120, 70567 Stuttgart",
       "hrb": "HRB 726450, Amtsgericht Stuttgart"}


# ─────────────────────────────────────────────────────────────────────────────
# HELPER 1 — Konzernrichtlinie (28 docs, 180-187w each)
# ─────────────────────────────────────────────────────────────────────────────
def konzern_richtlinie(fname, kurztitel, themengebiet, owner_funktion,
                        owner_name, ergaenzungen, kpis, normen, scope_extra="",
                        wip=False):
    folder = B00
    write_doc(f"{folder}/{fname}", H,
        f"Konzernrichtlinie {kurztitel}",
        subtitle=f"Verbindlich fuer Brennhagen Elektronik AG und alle Konzerngesellschaften (REG, RSG, RPL, RCZ, RHU, RCN, RHO); Stand 2023",
        draft=wip,
        sections=[
            ("Praeambel",
             f"Diese Konzernrichtlinie regelt das Themengebiet »{themengebiet}« fuer den Brennhagen-Konzern "
             f"und ist verbindlich fuer alle Beschaeftigten der Brennhagen Elektronik AG (Stuttgart, HRB 726451) "
             f"sowie aller direkten und indirekten Tochtergesellschaften. Sie wurde vom Vorstand der Brennhagen "
             f"Elektronik AG am 14. Maerz 2023 beschlossen und durch den Aufsichtsrat in der Sitzung vom "
             f"22. Maerz 2023 zur Kenntnis genommen. Die Richtlinie ersetzt die Vorgaengerversion 2020 "
             f"vollumfaenglich. {scope_extra}\n\n"
             f"Die Konzernrichtlinie ist in allen relevanten Konzernsprachen (Deutsch, Englisch, Polnisch, "
             f"Tschechisch, Ungarisch, Chinesisch) verfuegbar und wird ueber das Group Compliance Portal "
             f"(SharePoint /compliance/richtlinien) zur Verfuegung gestellt. Im Konfliktfall ist die deutsche "
             f"Fassung massgeblich."),
            ("Geltungsbereich",
             "Sachlich: Alle Geschaeftsvorfaelle, Prozesse und Entscheidungen im Anwendungsbereich des "
             "genannten Themengebiets.\n\n"
             "Persoenlich: Alle Mitarbeiter, Vorstaende, Geschaeftsfuehrer, Prokuristen, Handlungsbevollmaechtigten "
             "und Aufsichtsorgane der Konzerngesellschaften; entsprechend vertragliche Verpflichtung externer "
             "Berater, Zeitarbeitnehmer und wesentlicher Lieferanten.\n\n"
             "Raeumlich: Sitze und Niederlassungen in DE (Stuttgart, Heilbronn, Muenchen), PL (Katowice), "
             "CZ (Brno), HU (Gyoer) und CN (Shanghai)."),
            ("Grundsaetze und Kernanforderungen",
             ("list", ergaenzungen)),
            ("Verantwortlichkeiten",
             f"Policy Owner: {owner_funktion} ({owner_name}). Verantwortlich fuer Pflege, Auslegung und "
             f"Schulung. Vorstandsverantwortung: CEO Anna Mueller / CFO Laura Bauer (je nach Themengebiet). "
             f"Lokale Umsetzungsverantwortung tragen die jeweiligen Geschaeftsfuehrer der Tochtergesellschaften. "
             f"Verstoesse sind ueber die Hinweisgeber-Hotline (siehe Konzernrichtlinie Whistleblowing) zu melden."),
            ("Kennzahlen / Monitoring",
             ("list", kpis)),
            ("Verweise / Normen",
             ("list", normen)),
            ("Inkrafttreten und Revision",
             f"Inkrafttreten: 1. April 2023. Naechste planmaessige Revision: Q1/2026 (Drei-Jahres-Zyklus). "
             f"Ad-hoc-Revision bei wesentlichen regulatorischen Aenderungen. Versionierung im Group Policy "
             f"Management System (PMS), Eigentuemer: Group Compliance Office, Stuttgart."),
            ("Unterschriften / Freigabe",
             signatures("Anna Mueller", "Vorstandsvorsitzende", R["name"],
                        "Laura Bauer", "CFO", R["name"],
                        place="Stuttgart", date_str_="14. Maerz 2023")),
        ])


# ─────────────────────────────────────────────────────────────────────────────
# HELPER 2 — SLA Management-Dienstleistung RHO → Tochter (5 docs)
# ─────────────────────────────────────────────────────────────────────────────
def sla_management(fname, tochter_short, jahr="2023", wip=False):
    t = S[tochter_short]
    write_doc(f"{B00}/{fname}", RHO,
        f"Service Level Agreement (SLA) – Managementdienstleistungen RHO / {t['short']}",
        subtitle=f"zwischen Brennhagen Holding GmbH (RHO) und {t['name']} ({t['short']}), {t['city']}; Vertragsjahr {jahr}",
        draft=wip,
        sections=[
            ("Vertragsparteien",
             f"Auftraggeberin: {t['name']} (»{t['short']}«), {t['city']} ({t['country']}), {t['hrb']}, "
             f"vertreten durch die Geschaeftsfuehrung.\n\n"
             f"Auftragnehmerin: Brennhagen Holding GmbH (»RHO«), Vaihinger Strasse 120, 70567 Stuttgart, "
             f"HRB 726450 AG Stuttgart, vertreten durch die Geschaeftsfuehrer (Anna Mueller, Laura Bauer)."),
            ("Praeambel",
             f"Die Brennhagen Holding GmbH erbringt als Konzernmanagementgesellschaft fuer alle "
             f"Konzerngesellschaften zentrale Managementdienstleistungen (Group Functions). Dieses SLA "
             f"regelt Art, Umfang, Qualitaet und Verguetung der von RHO an {t['short']} im Jahr {jahr} "
             f"erbrachten Leistungen. Die Verrechnung erfolgt nach Kostenaufschlagsmethode (Cost+) gemaess "
             f"OECD Transfer Pricing Guidelines 2022, Kap. VII, mit Aufschlag 5 % auf direkte und indirekte "
             f"Kosten zur Vermeidung von Doppelbesteuerung und Erfuellung der Verrechnungspreisdokumentation "
             f"(siehe REA_Verrechnungspreisdokumentation_Masterdatei_{jahr})."),
            ("Leistungskatalog (Service Catalogue)",
             [["Service-Bereich", "Inhalt", "Frequenz", "Kostenanteil {} %".format(jahr)],
              ["Group Finance & Treasury", "Konsolidierung IFRS, Cash-Pooling, Hedging-Strategie", "monatlich", "22"],
              ["Group Tax", "TP-Doku, Steuerplanung, Compliance DAC6/Pillar 2", "quartalsweise", "10"],
              ["Group HR", "Konzern-HR-Policy, Talent Management, C-Level Recruiting", "laufend", "8"],
              ["Group IT", "ERP SAP S/4HANA Betrieb, Cybersecurity, Lizenzen", "laufend", "18"],
              ["Group Legal & Compliance", "Vertragsmuster, Compliance-Audit, Whistleblowing", "laufend", "9"],
              ["Group Audit (CAE)", "Konzernrevision gem. Jahresplan", "Auditzyklus", "7"],
              ["Group Controlling", "Reporting, Budget, Forecast", "monatlich", "12"],
              ["Group Communications & IR", "Investor Relations, Krisenkommunikation", "laufend", "5"],
              ["Group Sustainability", "ESG-Reporting CSRD, Klimastrategie, LkSG", "laufend", "9"]]),
            ("Service Level / KPIs",
             ("list", [
                 "Monatsabschluss-Konsolidierung bis Werktag +7 nach Periodenende (Ziel: 100 % Termintreue)",
                 "Quartalsabschluss bis Werktag +15 nach Quartalsende",
                 "Verfuegbarkeit ERP-System SAP S/4HANA mindestens 99,5 % (8x5)",
                 "Reaktionszeit Group Legal Anfragen: Standard 5 Werktage, dringend 24h",
                 "Concurrent Incident Response Group IT: P1 binnen 2h, P2 binnen 8h",
                 "Jaehrlicher Service-Review im November mit Geschaeftsfuehrung der Tochter",
             ])),
            ("Verguetung",
             f"Die jaehrliche Service-Fee {jahr} wird auf Basis der tatsaechlichen Kostenbasis der "
             f"RHO-Funktionen (Personalkosten, Sachkosten, anteilige Mieten, Abschreibungen) ermittelt. "
             f"Allokation an {t['short']} erfolgt nach Allokationsschluessel (Umsatz 50 %, FTE 30 %, "
             f"Headcount Top-Management 20 %). Aufschlag gem. Cost+: 5 %.\n\n"
             f"Abrechnung quartalsweise per Akontozahlung (Q+30 Tage), Jahresspitzenausgleich nach Pruefung "
             f"durch KPMG bis 30.6. des Folgejahres. Zahlungsziel 30 Tage netto. Bei Verzug Zinsen gemaess "
             f"§ 288 Abs. 2 BGB."),
            ("Laufzeit / Kuendigung",
             f"Laufzeit: 1.1.{jahr} bis 31.12.{jahr}, automatische Verlaengerung um 1 Jahr falls nicht "
             f"mit Frist von 6 Monaten zum Jahresende gekuendigt. Sonderkuendigungsrecht bei Konzernumstrukturierung "
             f"oder Verlust der 100%-Beteiligung."),
            ("Sonstige Regelungen",
             "Geheimhaltung: Beide Parteien verpflichten sich zur Geheimhaltung aller im Rahmen des SLA "
             "bekanntgewordenen Informationen. Datenschutz: Auftragsverarbeitung gem. Art. 28 DSGVO; "
             "AV-Vertrag als Anhang 2. Gerichtsstand: Stuttgart. Anwendbares Recht: deutsches Recht. "
             "Aenderungen beduerfen der Schriftform."),
            ("Unterschriften",
             signatures("Anna Mueller", "Geschaeftsfuehrerin", "Brennhagen Holding GmbH",
                        f"Geschaeftsfuehrung {t['short']}", "Geschaeftsfuehrung", t['name'],
                        place="Stuttgart", date_str_=f"15. Januar {jahr}")),
        ])


# ─────────────────────────────────────────────────────────────────────────────
# HELPER 3 — IC-Dienstleistungsvertrag Tochter ↔ Tochter
# ─────────────────────────────────────────────────────────────────────────────
def ic_dienstleistung(fname, geber_short, nehmer_short, leistung, jahr="2023",
                      volumen_tEUR=420, frequenz="laufend"):
    g = S[geber_short]; n = S[nehmer_short]
    write_doc(f"{B00}/{fname}", H,
        f"Intercompany-Dienstleistungsvertrag {g['short']} → {n['short']} ({jahr})",
        subtitle=f"Konzerninterne Dienstleistung: {leistung}",
        sections=[
            ("Vertragsparteien",
             f"Leistungserbringer: {g['name']} (»{g['short']}«), {g['city']} ({g['country']}), {g['hrb']}.\n\n"
             f"Leistungsempfaenger: {n['name']} (»{n['short']}«), {n['city']} ({n['country']}), {n['hrb']}.\n\n"
             f"Beide Gesellschaften sind 100%-Tochtergesellschaften der Brennhagen Holding GmbH (Stuttgart) "
             f"und somit Teil des Brennhagen-Konzerns (Mehrheitsaktionaer: Brennhagen Elektronik AG)."),
            ("Gegenstand der Leistung",
             f"Gegenstand dieses Vertrages ist die Erbringung folgender konzerninterner Dienstleistungen "
             f"durch {g['short']} an {n['short']}: {leistung}.\n\n"
             f"Die Leistung wird {frequenz} ueber den Vertragszeitraum {jahr} erbracht. Detaillierter "
             f"Leistungsumfang, Service Levels und Ansprechpartner sind in Anhang 1 (Service Catalogue) "
             f"geregelt. Die Leistungen sind funktional auf die operative Geschaefts­taetigkeit von "
             f"{n['short']} ausgerichtet."),
            ("Verguetung (Transfer Pricing)",
             f"Die Verguetung erfolgt nach Kostenaufschlagsmethode (Cost-Plus) gemaess OECD Transfer "
             f"Pricing Guidelines 2022, Kap. VII. Aufschlag auf direkte + indirekte Kosten: 5 %. "
             f"Geplantes Volumen {jahr}: ca. {volumen_tEUR} TEUR (gesch. Kostenbasis {int(volumen_tEUR/1.05)} TEUR + 5 % Margin).\n\n"
             f"Abrechnung quartalsweise per Akontozahlung gemaess Forecast, Jahresspitzenausgleich auf Basis "
             f"der tatsaechlichen Kosten bis 30.6. des Folgejahres. Verrechnung in EUR. Zahlungsziel: "
             f"45 Tage netto ab Rechnungseingang. Bei Verzug: Zinsen 5 %-Punkte ueber Basiszinssatz "
             f"(EZB-Hauptrefinanzierungssatz)."),
            ("Service Levels (Auszug)",
             ("list", [
                 "Verfuegbarkeit der Leistung gemaess Service-Spezifikation in Anhang 1",
                 "Reaktionszeiten gemaess Eskalationsmatrix (P1: 4h / P2: 24h / P3: 5 Werktage)",
                 "Monatliches Reporting an die Geschaeftsfuehrung des Leistungsempfaengers",
                 "Jaehrlicher Service-Review im November mit Anpassung fuer das Folgejahr",
             ])),
            ("Laufzeit / Kuendigung",
             f"Laufzeit: 1.1.{jahr} – 31.12.{jahr}, automatische Verlaengerung um je 12 Monate "
             f"falls nicht mit 3 Monaten Frist zum Jahresende gekuendigt. Sonderkuendigungsrecht bei "
             f"Konzernumstrukturierung oder Eintritt eines Change-of-Control-Ereignisses."),
            ("Geheimhaltung / Datenschutz / Sonstiges",
             "Beide Parteien verpflichten sich zur Geheimhaltung waehrend und ueber 5 Jahre nach Vertragsende. "
             "Datenschutz: Soweit personenbezogene Daten verarbeitet werden, schliessen die Parteien einen "
             "ergaenzenden Auftragsverarbeitungsvertrag (AV-Vertrag) gem. Art. 28 DSGVO. Gerichtsstand und "
             "anwendbares Recht: Stuttgart, deutsches Recht. Aenderungen beduerfen der Schriftform."),
            ("Unterschriften",
             signatures(f"GF {g['short']}", "Geschaeftsfuehrer/in", g['name'],
                        f"GF {n['short']}", "Geschaeftsfuehrer/in", n['name'],
                        place=g['city'], date_str_=f"15. Januar {jahr}")),
        ])


# ─────────────────────────────────────────────────────────────────────────────
# HELPER 4 — Konzern-Governance-Quartalsreport (14 Berichte)
# ─────────────────────────────────────────────────────────────────────────────
def gov_quartal(fname, jahr, quartal, hl_themen, tochter_status, ausblick,
                besonderheiten=""):
    qmap = {"Q1": "1.1.-31.3.", "Q2": "1.4.-30.6.", "Q3": "1.7.-30.9.", "Q4": "1.10.-31.12."}
    qspan = qmap.get(quartal, "")
    write_doc(f"{B00}/{fname}", H,
        f"Konzern-Governance-Report {jahr} {quartal}",
        subtitle=f"Quartalsbericht des Konzerncontrolling / Group Compliance Office an Vorstand und Aufsichtsrat",
        confidential=True,
        sections=[
            ("Berichtsperiode",
             f"Berichtsperiode: {quartal} {jahr} ({qspan} {jahr}). "
             f"Vorlage an Vorstand am ersten Freitag des Folgemonats; Vorlage an Aufsichtsrat in der naechsten "
             f"turnusmaessigen Sitzung. Bericht erstellt durch Group Compliance Office (Stuttgart), abgestimmt "
             f"mit Group Controlling (Florian Maier) und Group Audit (Andreas Buehler)."),
            ("Highlights und Schwerpunktthemen",
             ("list", hl_themen)),
            ("Status der Tochtergesellschaften",
             [["Gesellschaft", "Sitz", "Compliance-Status", "Bemerkung"]] + tochter_status),
            ("Governance-Indikatoren",
             ("list", [
                 "Compliance-Schulungen: Teilnahmequote im Quartal > 95 % (Sollwert 95 %)",
                 "Hinweisgeber-Faelle (Whistleblowing): siehe Anhang 1 (vertraulich)",
                 "Offene Audit-Findings: siehe Group-Audit-Quartals-Dashboard (Anhang 2)",
                 "D&O-Schadensfaelle / Klageandrohungen: keine relevanten Faelle im Berichtszeitraum (sofern nicht anders vermerkt)",
                 "ESG-Compliance gem. CSRD-Vorbereitung: planmaessig im Zeitplan",
             ])),
            ("Risikoeinschaetzung",
             "Die Top-5-Konzernrisiken werden quartalsweise im Risk-Committee unter Leitung des CFO "
             "(Laura Bauer) bewertet. Aktuelle Top-5: (1) Lieferkettenrisiken Halbleiter, "
             "(2) FX-Volatilitaet CNY/USD, (3) regulatorische Aenderungen ESG/CSRD, "
             "(4) Cyber-Risiken (Ransomware), (5) Personalrisiko Top-Engineering-Faecher. "
             "Detaillierter Risk-Report siehe separates Dokument."),
            ("Besonderheiten",
             besonderheiten or "Keine ad-hoc-meldungspflichtigen Sachverhalte im Berichtszeitraum."),
            ("Ausblick",
             ausblick),
            ("Unterschrift",
             signatures("Anna Mueller", "Vorstandsvorsitzende", R["name"],
                        "Andreas Buehler", "Chief Audit Executive (CAE)", R["name"],
                        place="Stuttgart", date_str_=f"{quartal}/{jahr}")),
        ])


# ─────────────────────────────────────────────────────────────────────────────
# HELPER 5 — Konzernlagebericht (Kurzfassung Holding)
# ─────────────────────────────────────────────────────────────────────────────
def konzernlagebericht(fname, jahr, umsatz, ebit, ebitda, fte, dividende,
                       schwerpunkte, ausblick):
    write_doc(f"{B00}/{fname}", H,
        f"Konzernlagebericht {jahr}",
        subtitle=f"Brennhagen Elektronik AG, Konzernabschluss IFRS, Geschaeftsjahr {jahr}",
        sections=[
            ("Gesamtaussage zur wirtschaftlichen Lage",
             f"Das Geschaeftsjahr {jahr} verlief fuer den Brennhagen-Konzern insgesamt erfolgreich. "
             f"Der Konzernumsatz erreichte {umsatz} Mio. EUR (Vorjahr-Vergleich siehe Konzernabschluss). "
             f"Das EBIT lag bei {ebit} Mio. EUR, das EBITDA bei {ebitda} Mio. EUR. Die Konzern-Mitarbeiterzahl "
             f"stieg auf {fte} FTE zum Bilanzstichtag. Trotz volatiler Markt- und Lieferkettenbedingungen "
             f"konnte die Profitabilitaet der Vorjahresperiode bestaetigt werden."),
            ("Geschaeftsverlauf und Lage",
             f"Die Nachfrage nach unseren Kernprodukten (ICP-3, BMS-12, ADAS-V4D, ECU-900, LightCtrl-7) "
             f"war stabil bis steigend. Insbesondere das Batteriemanagement-System BMS-12 entwickelte sich "
             f"in Folge der OEM-Anlaeufe bei Volkswagen (ID.7) sehr positiv. Im Bereich ADAS-V4D wurden "
             f"weitere Designwins bei Mercedes-Benz und Stellantis erzielt. Die regionalen Werke "
             f"REG Heilbronn, RPL Katowice, RCZ Brno und RHU Gyoer waren ueber das Jahr gut ausgelastet. "
             f"RSG Muenchen verzeichnete weiteren Aufbau im Bereich ADAS-Software (ASPICE Level 2-3)."),
            ("Schwerpunktthemen",
             ("list", schwerpunkte)),
            ("Wesentliche Konzernfinanzkennzahlen",
             [["Kennzahl", str(jahr)],
              ["Umsatzerloese (Mio. EUR)", str(umsatz)],
              ["EBITDA (Mio. EUR)", str(ebitda)],
              ["EBIT (Mio. EUR)", str(ebit)],
              ["Beschaeftigte (FTE)", str(fte)],
              ["Dividende EUR/Aktie", str(dividende)]]),
            ("Finanzlage / Finanzierung",
             "Die Konzernfinanzierung erfolgt ueber den Konsortialkreditvertrag 2022 (250 Mio. EUR, "
             "Laufzeit bis 14.3.2027, Konsortium 5 Banken). Die Financial Covenants (Net Debt/EBITDA ≤ 3,0x, "
             "ICR ≥ 4,0x, EQ-Quote ≥ 30 %) wurden zu allen Stichtagen eingehalten. Liquiditaet zum Bilanzstichtag "
             "war komfortabel; Nettoverschuldung deutlich unter den Covenants."),
            ("Risiken und Chancen",
             "Wesentliche Konzernrisiken: Halbleiterversorgung, FX-Volatilitaet (CNY/USD), regulatorische "
             "Aenderungen (CSRD, EU AI Act, Lieferkettengesetz), Cyberrisiken, Personalbindung. Wesentliche "
             "Chancen: Wachstum E-Mobility (BMS-12), Level-3-Automatisierung (ADAS-V4D), Asien-Geschaeft "
             "(RCN Shanghai). Risikomanagement folgt dem Konzern-Framework gem. IDW PS 340 / COSO ERM."),
            ("Prognosebericht / Ausblick",
             ausblick),
            ("Unterschrift Vorstand",
             signatures("Anna Mueller", "Vorstandsvorsitzende", R["name"],
                        "Laura Bauer", "CFO", R["name"],
                        place="Stuttgart", date_str_=f"15. Maerz {int(jahr)+1}")),
        ])


# ─────────────────────────────────────────────────────────────────────────────
# HELPER 6 — Nichtfinanzieller Bericht (3 docs)
# ─────────────────────────────────────────────────────────────────────────────
def nichtfin_bericht(fname, jahr, kpi_block, themen):
    write_doc(f"{B00}/{fname}", H,
        f"Nichtfinanzieller Konzernbericht {jahr}",
        subtitle=f"Erklaerung nach §§ 315b, 315c i. V. m. 289c–289e HGB / CSRD-Vorbereitung",
        sections=[
            ("Berichtsrahmen",
             f"Berichtszeitraum: 1.1.{jahr} – 31.12.{jahr}. Berichtsstandard: GRI Standards 2021 in Kombination "
             f"mit den Vorbereitungsarbeiten zur EU-Corporate-Sustainability-Reporting-Directive (CSRD), "
             f"die fuer den Brennhagen-Konzern ab Geschaeftsjahr 2024 verpflichtend wird. Die Erklaerung bezieht "
             f"sich auf den Brennhagen-Konzern (REA, REG, RSG, RPL, RCZ, RHU, RCN, RHO).\n\n"
             f"Pruefung: KPMG AG WPG hat eine pruefungsaehnliche Durchsicht mit begrenzter Sicherheit "
             f"(»limited assurance«) durchgefuehrt."),
            ("Wesentlichkeitsanalyse",
             "Die doppelte Wesentlichkeit (»double materiality«) wurde unter Beteiligung von 12 Stakeholder-"
             "Gruppen (OEM-Kunden, Mitarbeiter, Investoren, NGOs, Behoerden, Lieferanten, Banken, Versicherer, "
             "lokale Gemeinden, BR, Wirtschaftspruefer, Anwaelte) durchgefuehrt. Die 8 wesentlichen Themen: "
             "(1) Klimawandel / Scope 1+2+3, (2) Energieverbrauch und Energieeffizienz, (3) Kreislaufwirtschaft, "
             "(4) Eigene Belegschaft / Diversity / Gesundheit, (5) Arbeitnehmer in der Wertschoepfungskette / "
             "Lieferkettengesetz LkSG, (6) Unternehmensfuehrung und Geschaeftsethik / Anti-Korruption, "
             "(7) Cyber- und Datensicherheit, (8) Produktsicherheit und -qualitaet."),
            ("Wesentliche Kennzahlen",
             kpi_block),
            ("Strategische Schwerpunkte",
             ("list", themen)),
            ("Ausblick",
             "Fuer das Folgejahr ist die Vollumsetzung der CSRD-Berichterstattung gemaess ESRS (European "
             "Sustainability Reporting Standards) vorgesehen. Klimastrategie: Reduktion Scope 1+2 um -55 % bis "
             "2030 (Basisjahr 2019); Scope 3 um -30 %. Validierung der Klimaziele durch SBTi geplant fuer Q2/2024. "
             "Investitionen in PV-Anlagen an Werken Heilbronn, Katowice, Brno geplant (Gesamtvolumen 12 Mio. EUR)."),
            ("Unterschrift",
             signatures("Anna Mueller", "CEO", R["name"],
                        "Group Sustainability Office", "Leitung", R["name"],
                        place="Stuttgart", date_str_=f"15. Maerz {int(jahr)+1}")),
        ])


# ─────────────────────────────────────────────────────────────────────────────
# HELPER 7 — Vollmacht (4 docs)
# ─────────────────────────────────────────────────────────────────────────────
def vollmacht(fname, bevollmaechtigt, funktion, geschaeftsbereich, datum,
              erteilung_jahr="2023"):
    write_doc(f"{B00}/{fname}", H,
        f"Generalvollmacht / Handlungsvollmacht – {bevollmaechtigt}",
        subtitle=f"Erteilt durch den Vorstand der Brennhagen Elektronik AG; gueltig ab {datum}",
        sections=[
            ("Bevollmaechtigte/r",
             f"Name: {bevollmaechtigt}\nFunktion im Konzern: {funktion}\n"
             f"Geschaeftsbereich: {geschaeftsbereich}\nAusweisnummer (intern): VM-{erteilung_jahr}-{fname[:4].upper()}"),
            ("Vollmachtsumfang",
             f"Die Brennhagen Elektronik AG, vertreten durch den Vorstand (Anna Mueller / Laura Bauer), erteilt "
             f"hiermit Herrn/Frau {bevollmaechtigt} Generalvollmacht im Sinne der §§ 167, 171 BGB i. V. m. "
             f"§ 54 HGB fuer den Geschaeftsbereich »{geschaeftsbereich}«.\n\n"
             f"Die Vollmacht umfasst insbesondere folgende Befugnisse:\n"
             f"– Abschluss von Vertraegen im operativen Geschaeftsbereich bis 5 Mio. EUR Einzelfall / 20 Mio. EUR p. a.\n"
             f"– Vertretung der Gesellschaft gegenueber Kunden, Lieferanten und Behoerden\n"
             f"– Erteilung von Untervollmachten an Mitarbeiter (in Abstimmung mit Group Legal)\n"
             f"– Personalmassnahmen im Verantwortungsbereich (Einstellungen, Beurteilungen)\n"
             f"– Unterzeichnung von Bestellungen, Rechnungen, Lieferscheinen, Auftragsbestaetigungen"),
            ("Beschraenkungen",
             "Ausgenommen von dieser Vollmacht sind in jedem Fall:\n"
             "– Aufnahme von Krediten oder Garantien\n"
             "– Veraeusserung oder Belastung von Grundstuecken und Immobilien\n"
             "– Erwerb oder Veraeusserung von Beteiligungen\n"
             "– Abschluss von Vertraegen mit Volumen > 5 Mio. EUR im Einzelfall\n"
             "– Vertraege mit verbundenen Unternehmen (Intercompany; Vorbehalt CFO)\n"
             "– Rechtsstreitigkeiten und gerichtliche Vertretung (Vorbehalt Group Legal)"),
            ("Unterschriftsregelung",
             "Im Aussenverhaeltnis vertritt der/die Bevollmaechtigte die Gesellschaft gemeinsam mit einem "
             "Vorstand oder mit einem weiteren Generalbevollmaechtigten / Prokuristen (Vier-Augen-Prinzip). "
             "Interne Freigabeprozesse gemaess Konzernrichtlinie Unterschriftenregelung 2023 bleiben unberuehrt."),
            ("Geltungsdauer / Widerruf",
             f"Die Vollmacht tritt am {datum} in Kraft und gilt bis auf Widerruf. Der Widerruf erfolgt "
             f"schriftlich durch den Vorstand und ist im Konzern-Unterschriftenregister (Group Legal) "
             f"einzutragen. Bei Ausscheiden aus dem Konzern erlischt die Vollmacht automatisch."),
            ("Erteilung der Vollmacht",
             signatures("Anna Mueller", "Vorstandsvorsitzende", R["name"],
                        "Laura Bauer", "CFO", R["name"],
                        place="Stuttgart", date_str_=datum)),
            ("Annahmeerklaerung",
             f"Hiermit nehme ich die mir erteilte Vollmacht an und verpflichte mich, sie ausschliesslich "
             f"im Interesse der Brennhagen Elektronik AG sowie unter Beachtung aller Konzernrichtlinien und "
             f"gesetzlichen Vorgaben auszuueben.\n\n"
             f"Stuttgart, den {datum}\n\n"
             f"__________________________\n{bevollmaechtigt}"),
        ])


# ─────────────────────────────────────────────────────────────────────────────
# HELPER 8 — Articles of Association (RCN / RFI)
# ─────────────────────────────────────────────────────────────────────────────
def articles_of_association(fname, tochter_short_or_name, sitz, jurisdiction,
                             rechtsform, registry, stammkap_text,
                             zweck_text, governance_text, parent="Brennhagen Holding GmbH"):
    write_doc(f"{B00}/{fname}", H,
        f"Articles of Association / Gesellschaftsvertrag – {tochter_short_or_name}",
        subtitle=f"{rechtsform}, {sitz} ({jurisdiction}); konsolidierte Fassung 2023",
        sections=[
            ("Company / Gesellschaft",
             f"Name: {tochter_short_or_name}\nLegal form: {rechtsform}\n"
             f"Registered office / Sitz: {sitz}, {jurisdiction}\n"
             f"Register / Registry: {registry}\n"
             f"Shareholder / Gesellschafter (100 %): {parent}, Stuttgart, Germany"),
            ("Object of the company / Unternehmensgegenstand",
             zweck_text),
            ("Share capital / Stammkapital",
             stammkap_text),
            ("Corporate bodies / Organe",
             governance_text),
            ("Financial year / Geschaeftsjahr",
             "The financial year corresponds to the calendar year (1 January – 31 December). The first "
             "shortened financial year, where applicable, ends on 31 December of the year of incorporation. "
             "The annual financial statements are prepared in accordance with local GAAP and additionally "
             "converted to IFRS for group consolidation purposes within the Brennhagen group reporting package."),
            ("Profit distribution / Gewinnverwendung",
             "Annual profits are distributed in accordance with the resolution of the shareholders' meeting, "
             "subject to legal reserve requirements of the relevant jurisdiction. Dividends to the parent "
             "company shall be paid in accordance with the group dividend policy (Konzernrichtlinie Treasury 2023) "
             "and the applicable double-tax treaty between the country of incorporation and Germany."),
            ("Amendments and dissolution / Aenderungen und Aufloesung",
             "Amendments to these articles require a resolution of the shareholders' meeting with the qualified "
             "majority required by the applicable law. Dissolution requires unanimous shareholder consent and "
             "follows the statutory liquidation procedure of the relevant jurisdiction. Upon dissolution, "
             "any remaining net assets are distributed to the sole shareholder."),
            ("Governing law / Anwendbares Recht",
             f"These articles are governed by the laws of {jurisdiction}. Place of jurisdiction is the "
             f"competent court at the registered office of the company. The German translation of these "
             f"articles is provided for information purposes only; in case of any divergence the original "
             f"language version prevails."),
            ("Signature / Unterzeichnung",
             signatures("Anna Mueller", "Managing Director (Parent)", parent,
                        "Local Managing Director", "Geschaeftsfuehrer/in / Director", tochter_short_or_name,
                        place=sitz, date_str_="15. Maerz 2023")),
        ])


# ─────────────────────────────────────────────────────────────────────────────
# HELPER 9 — Verrechnungspreis-Masterdatei
# ─────────────────────────────────────────────────────────────────────────────
def verrechnungspreis_masterdatei(fname, jahr="2023"):
    write_doc(f"{B00}/{fname}", H,
        f"Verrechnungspreisdokumentation – Masterdatei / Master File {jahr}",
        subtitle=f"Brennhagen-Konzern, OECD Transfer Pricing Guidelines 2022 / § 90 Abs. 3 AO / GAufzV",
        confidential=True,
        sections=[
            ("Berichtszweck",
             f"Diese Masterdatei (»Master File«) dokumentiert die wesentliche Verrechnungspreis-Praxis des "
             f"Brennhagen-Konzerns fuer das Geschaeftsjahr {jahr} entsprechend Aktion 13 des OECD/G20-BEPS-Projekts "
             f"und § 90 Abs. 3 AO i. V. m. § 4 GAufzV. Sie ergaenzt die landesspezifischen Local Files (DE/PL/CZ/HU/CN) "
             f"und das Country-by-Country-Reporting (CbCR; Berichtspflicht REA, Konzern uebersteigt 750 Mio. EUR "
             f"Schwelle nicht; freiwilliges Reporting an Bundeszentralamt fuer Steuern)."),
            ("Konzernstruktur und Geschaeftstaetigkeit",
             f"Der Brennhagen-Konzern besteht aus der Konzernobergesellschaft Brennhagen Elektronik AG (Stuttgart, "
             f"boersennotiert Prime Standard) mit 100%-Beteiligungen ueber die Brennhagen Holding GmbH (RHO) an "
             f"6 operativen Tochtergesellschaften: REG (Heilbronn, DE), RSG (Muenchen, DE), RPL (Katowice, PL), "
             f"RCZ (Brno, CZ), RHU (Gyoer, HU), RCN (Shanghai, CN). Geschaeftstaetigkeit: Entwicklung, Produktion "
             f"und Vertrieb von Automotive-Elektronik (Infotainment, Batterie-Management, ADAS, Powertrain-ECUs, "
             f"Matrix-LED). Konzernumsatz {jahr}: 612 Mio. EUR. Hauptkunden: BMW, VW, Mercedes-Benz, Stellantis, "
             f"Ford, Continental, ZF, Bosch."),
            ("Wesentliche Verrechnungspreis-Transaktionen",
             [["Transaktionstyp", "Methode", "Volumen (Mio. EUR)", "Begruendung"],
              ["Lieferung Halbzeuge REG → RPL", "TNMM (Wiederverkaufspreis-/Net-Margin)", "62", "Routinefunktion EMS-Produktion"],
              ["Software-Lizenz RSG → REG/RPL", "Cost-Plus 8 %", "12", "F&E-Funktion mit Eigenforschung"],
              ["Management-Services RHO → Toechter", "Cost-Plus 5 %", "18", "Routine-Dienstleistung Headquarters"],
              ["IC-Darlehen REA → Toechter", "Comparable Uncontrolled Price (CUP)", "85 ausstehend", "Zinssatz EURIBOR+150bp"],
              ["Konzernumlagen (Kostenpooling)", "Pooling-Methode", "4,5", "Indirekte zentrale Funktionen"]]),
            ("Funktions- und Risikoanalyse (Auszug)",
             "REA: Strategiefunktion, IP-Eigentuemerin der wesentlichen Patente, traegt Kernrisiken (Marktrisiko, "
             "Investitionsrisiko). REG: Vollstaendige Produktionsfunktion mit Routinerisiken, Vertragsfertiger "
             "fuer Hauptprodukt-Linien. RPL/RCZ/RHU: Eingeschraenkte Risiken, EMS-Vertragsfertiger im Cost-Plus-Verfahren. "
             "RSG: F&E-Dienstleister mit Cost-Plus-Verguetung. RCN: Vertriebsgesellschaft, »Buy-Sell«-Modell mit "
             "Margenkontrolle. RHO: Service-Provider Headquarters-Funktionen."),
            ("Konsistenz und Methodik",
             "Die Methoden- und Margenwahl wurde benchmark-validiert ueber externe Datenbanken (Amadeus / "
             "Royaltystat) im Rahmen der jaehrlichen TP-Studie durch KPMG. Margen werden jaehrlich auf "
             "Marktangemessenheit ueberprueft. Im Berichtsjahr keine wesentlichen Methodenaenderungen. "
             "Vorabverstaendigungsverfahren (APA) mit der polnischen Steuerverwaltung fuer RPL ist seit "
             "Juli 2022 in Verhandlung (laufend)."),
            ("Dokumentationssprache und Aufbewahrung",
             "Die Masterdatei wird in Deutsch und Englisch gefuehrt. Aufbewahrungsfrist 10 Jahre gem. § 147 AO. "
             "Aktualisierung jaehrlich bis 31.3. des Folgejahres durch Group Tax (Dr. Heike Berger) in "
             "Abstimmung mit den lokalen Tax-Verantwortlichen."),
            ("Freigabe",
             signatures("Laura Bauer", "CFO", R["name"],
                        "Dr. Heike Berger", "Group Tax Director", R["name"],
                        place="Stuttgart", date_str_=f"31. Maerz {int(jahr)+1}")),
        ])


# ─────────────────────────────────────────────────────────────────────────────
# HELPER 10 — IC Quartalsbericht / IC Rechnung (klein) / VW QBR / 8D / Patent etc.
# ─────────────────────────────────────────────────────────────────────────────
def ic_quartalsbericht(fname, tochter_short, jahr, quartal, themen):
    t = S[tochter_short]
    write_doc(f"{B00}/{fname}", H,
        f"Intercompany-Quartalsbericht {t['short']} – {jahr} {quartal}",
        subtitle=f"Berichterstattung {t['name']} an die Konzernmuttergesellschaft (REA / RHO)",
        sections=[
            ("Berichtende Gesellschaft",
             f"{t['name']} ({t['short']}), {t['city']} ({t['country']}), {t['hrb']}. "
             f"Geschaeftsfuehrer/Werkleiter wie im Konzernorganigramm 2023/24 ausgewiesen. "
             f"Berichtsperiode: {quartal} {jahr}."),
            ("Operative Highlights / Wesentliche Ereignisse",
             ("list", themen)),
            ("Finanzkennzahlen (Auszug, vorlaeufig)",
             [["Kennzahl", f"{quartal} {jahr}", "Vorjahr {} ".format(int(jahr)-1)+quartal],
              ["Umsatz (TEUR)", "—", "—"],
              ["EBITDA (TEUR)", "—", "—"],
              ["FTE (Stichtag)", str(t['employees']), str(t['employees']-20)],
              ["CAPEX (TEUR)", "—", "—"]]),
            ("Personalsituation",
             f"Die Personalsituation am Standort {t['city']} ist stabil. Krankenstand im Branchendurchschnitt. "
             f"Schulungsplaene wurden quartalsweise erfuellt. Keine arbeitsrechtlichen Auseinandersetzungen "
             f"im Berichtszeitraum, soweit nicht im Schwerpunktteil dieses Berichts ausdruecklich erwaehnt."),
            ("Compliance und Audit",
             "Keine wesentlichen Compliance-Vorfaelle im Berichtszeitraum. Offene Audit-Findings aus dem "
             "Group-Internal-Audit-Plan werden gemaess vereinbarter Roadmap abgearbeitet (Status im Group-Audit-Tool). "
             "Lokale gesetzliche Anforderungen werden in der jeweiligen Jurisdiktion eingehalten; "
             "regulatorische Aenderungen werden ueber Group Compliance laufend kommuniziert."),
            ("Ausblick auf das Folgequartal",
             "Operativer Ausblick: Fortfuehrung der laufenden Kundenprojekte und Anlaeufe. "
             "Finanzieller Ausblick: Erfuellung des Konzernbudgets {} ".format(jahr) +
             "im Plan; aktualisierter Forecast wird im naechsten Quartalsreport vorgelegt. "
             "Keine ad-hoc-meldungspflichtigen Sachverhalte aus Sicht der Berichtsperiode."),
            ("Unterzeichnung",
             signatures("Werkleitung "+t['short'], "Werkleiter/in", t['name'],
                        "Group Controlling", "Florian Maier", R["name"],
                        place=t['city'], date_str_=f"15. {quartal[1]}.{jahr}")),
        ])


def ic_rechnung(fname, leistungserbringer_short, rechnungsempfaenger, jahr,
                monat, betrag_eur, leistungsbeschreibung, re_nr):
    g = S[leistungserbringer_short]
    write_doc(f"{B00}/{fname}", H,
        f"Konzerninterne Rechnung Nr. {re_nr}",
        subtitle=f"Rechnungssteller: {g['name']} an {rechnungsempfaenger}",
        sections=[
            ("Rechnungssteller",
             f"{g['name']} ({g['short']})\n{g['city']}, {g['country']}\n{g['hrb']}\n"
             f"UmsSt-ID: gemaess lokaler Registrierung; bei innergemeinschaftlicher Leistung Reverse Charge."),
            ("Rechnungsempfaenger",
             f"{rechnungsempfaenger}\nKonzerninterner Verbund\nLieferadresse / Rechnungsadresse: gem. Konzernanschrift"),
            ("Rechnungsdetails",
             f"Rechnungsnummer: {re_nr}\nRechnungsdatum: {monat}/{jahr}\nLeistungszeitraum: {monat}/{jahr}\n"
             f"Faelligkeit: 30 Tage netto nach Rechnungseingang\nWaehrung: EUR\nZahlungsweg: SEPA-Konzern-Cash-Pool"),
            ("Leistungsbeschreibung",
             leistungsbeschreibung),
            ("Verguetung",
             [["Position", "Menge", "Einzelpreis", "Summe (EUR)"],
              ["Leistung gem. IC-Vertrag", "1", f"{betrag_eur:,.2f}".replace(",", ".").replace(".", ",", 1), f"{betrag_eur:,.2f}".replace(",", ".").replace(".", ",", 1)],
              ["Zwischensumme netto", "", "", f"{betrag_eur:,.2f}".replace(",", ".").replace(".", ",", 1)],
              ["Umsatzsteuer", "", "Reverse Charge", "0,00"],
              ["Rechnungsbetrag gesamt", "", "", f"{betrag_eur:,.2f}".replace(",", ".").replace(".", ",", 1)]]),
            ("Verrechnungspreis-Hinweis",
             f"Die Verguetung entspricht der vertraglich vereinbarten Cost-Plus-Methodik (Aufschlag 5 % bzw. "
             f"vertraglich abweichend) gemaess Intercompany-Rahmenvertrag {jahr} und ist konsistent mit der "
             f"Verrechnungspreisdokumentation des Brennhagen-Konzerns (Masterdatei {jahr}). Eine separate "
             f"Begleitdokumentation zur arms'-length-Konformitaet ist beim Rechnungssteller verfuegbar."),
            ("Reverse-Charge-Vermerk",
             "Bei grenzueberschreitender innergemeinschaftlicher sonstiger Leistung gem. § 13b UStG / "
             "Art. 196 MwStSystRL geht die Steuerschuldnerschaft auf den Leistungsempfaenger ueber "
             "(Reverse Charge). Keine deutsche Umsatzsteuer ausgewiesen."),
            ("Hinweis",
             "Diese Rechnung ist Teil der konzerninternen Leistungsverrechnung und unterliegt der konzerninternen "
             "Pruefung durch Group Tax / Group Treasury. Reklamationen sind binnen 14 Tagen schriftlich zu erheben."),
            ("Ausstellung",
             f"{g['city']}, im {monat}/{jahr}\n\n{g['name']} – Buchhaltung / Accounting"),
        ])


def vw_qbr(fname, produkt, jahr, quartal, themen, statusampel):
    write_doc(f"{B00}/{fname}", H,
        f"Quarterly Business Review {produkt} – Volkswagen AG, {quartal}/{jahr}",
        subtitle=f"Kundenstatus, Lieferperformance, Projekt-Pipeline und Eskalationen mit Volkswagen Group",
        sections=[
            ("Teilnehmer",
             "Volkswagen AG (Wolfsburg): Einkaufsleitung Komponente, Qualitaetsmanagement-OEM, "
             "Programm-Management E-Mobility / Powertrain, ggf. Vertreter Vorserienentwicklung.\n\n"
             "Brennhagen Elektronik AG / REG: Stefan Richter (CMO/BD), Key Account Manager VW, "
             "Werkleitung REG (Andreas Maier), Qualitaetsleitung (Sabine Brand), "
             "ggf. Vertreter R&D / Programm."),
            ("Berichtszeitraum und Scope",
             f"Quartalsbericht {quartal}/{jahr} zum Produkt {produkt}. Scope: Liefermengen, Qualitaetsperformance, "
             f"Reklamationsstatus, Forecast Folgequartale, Pipeline neuer Designwins / RFQ, "
             f"strategische Themen (z. B. Cyber, Software-OTA, ASPICE, IATF, Carbon Footprint)."),
            ("Operative KPIs Status",
             [["KPI", "Ziel", "Ist", "Status"]] + statusampel),
            ("Schwerpunktthemen / Eskalationen",
             ("list", themen)),
            ("Vereinbarungen / Naechste Schritte",
             "Naechstes QBR turnusmaessig im Folgequartal. Offene Themen werden im "
             "OEM-Eskalationsboard nachverfolgt. Aktionen mit Termin und Verantwortlichen sind "
             "im QBR-Action-Tracker (Anhang) festgehalten. Eskalationspfad: REG → Stefan Richter → "
             "Anna Mueller (CEO REA) / Programm-Direktor VW."),
            ("Unterzeichnung",
             signatures("Stefan Richter", "CMO/BD REA", R["name"],
                        "Programmleitung VW", "Einkauf / QM", "Volkswagen AG",
                        place="Wolfsburg", date_str_=f"{quartal}/{jahr}")),
        ])


def msa_studie(fname, mess_objekt, geraet, datum):
    write_doc(f"{B00}/{fname}", H,
        f"Messsystemanalyse / MSA – {mess_objekt}",
        subtitle=f"Studie zur Messmittelfaehigkeit nach AIAG MSA 4th Edition / VDA Band 5",
        sections=[
            ("Pruefobjekt und Messmittel",
             f"Pruefobjekt: {mess_objekt}\nVerwendetes Messmittel: {geraet}\n"
             f"Pruefer: 3 unabhaengige Pruefer (A/B/C), je 10 Pruefteile, jeweils 3 Wiederholungen.\n"
             f"Messdatum: {datum}\nVerantwortlicher Q-Ingenieur: Sabine Brand (Q-Leitung REG)."),
            ("Untersuchungsverfahren",
             "Durchgefuehrt wurde eine Variantenstudie nach ANOVA-Methode (»Average and Range«-Methode "
             "alternativ verfuegbar). Bewertet wurden die Komponenten Repeatability (EV - "
             "Equipment Variation), Reproducibility (AV - Appraiser Variation), Gauge R&R (GRR), "
             "Part Variation (PV) und Total Variation (TV). "
             "Akzeptanzkriterien: %GRR < 10 % (akzeptabel), 10-30 % (bedingt akzeptabel), "
             "> 30 % (nicht akzeptabel) gem. AIAG MSA."),
            ("Ergebnis",
             [["Komponente", "Wert", "Anteil an TV"],
              ["EV (Repeatability)", "—", "—"],
              ["AV (Reproducibility)", "—", "—"],
              ["GRR", "—", "—"],
              ["PV (Part Variation)", "—", "—"],
              ["%GRR", "—", "innerhalb Toleranz (siehe Beurteilung)"]]),
            ("Beurteilung",
             "Das Messsystem wird auf Basis der Studie als »akzeptabel« eingestuft (%GRR < 10 %). "
             "Damit ist die Messmittelfaehigkeit fuer die kontinuierliche Serienpruefung gegeben. "
             "Empfehlung: jaehrliche Re-MSA gemaess Q-Plan; Kalibrierintervall des Messgeraets unveraendert "
             "12 Monate. Schulungsstand der Pruefer wurde dokumentiert (siehe Anhang Schulungsnachweise)."),
            ("Massnahmen / Naechste Schritte",
             ("list", [
                 "Freigabe des Messsystems fuer den laufenden Serienprozess",
                 "Naechste Re-MSA in 12 Monaten (im Q-Plan eingeplant)",
                 "Schulungsauffrischung der Pruefer im naechsten Auditzyklus",
                 "Aufnahme der Studie in die Pruefmittel-Akte (PMA)",
             ])),
            ("Freigabe",
             signatures("Sabine Brand", "Q-Leitung REG", "Brennhagen Elektronik GmbH",
                        "Andreas Maier", "Werkleiter REG", "Brennhagen Elektronik GmbH",
                        place="Heilbronn", date_str_=datum)),
        ])


def patent_antwort(fname, patent_nr, datum, gegenstand):
    write_doc(f"{B00}/{fname}", H,
        f"Antwort des Anmelders auf DPMA-Bescheid – {patent_nr}",
        subtitle=f"Erwiderung im Pruefverfahren beim Deutschen Patent- und Markenamt",
        sections=[
            ("Aktenzeichen / Bezug",
             f"DPMA-Aktenzeichen: {patent_nr}\nBescheiddatum: 14. Februar 2023\n"
             f"Bezug: Erster Pruefbescheid des DPMA gem. § 45 PatG\n"
             f"Anwalt der Anmelderin: Patentanwaelte Hengeler Mueller / Vossius & Partner Patentanwaelte, Muenchen\n"
             f"Anmelderin: Brennhagen Elektronik AG, Stuttgart"),
            ("Gegenstand der Erfindung",
             gegenstand),
            ("Erwiderung",
             "Die Anmelderin erwidert auf den Bescheid wie folgt: Die im Bescheid genannten Druckschriften "
             "D1–D3 nehmen den Anspruch 1 weder neuheitsschaedlich vorweg, noch legen sie die beanspruchte "
             "Loesung in naheliegender Weise nahe. Die im Anspruch 1 gekennzeichnete Kombination der Merkmale "
             "(a)–(e), insbesondere die Verbindung der ADAS-Sensorfusion mit der adaptiven Latenzkompensation, "
             "ist in keiner der zitierten Druckschriften offenbart oder angeregt.\n\n"
             "Hilfsweise werden die Ansprueche 1, 5 und 12 wie aus dem beigefuegten Anspruchssatz "
             "ersichtlich geaendert. Die geaenderten Ansprueche beruhen auf der ursprueglichen Offenbarung "
             "(siehe ursprueglicher Anspruch 7 i. V. m. Beschreibung S. 18, Z. 7–22). Die Aenderungen erweitern "
             "den Schutzbereich nicht."),
            ("Antraege",
             ("list", [
                 "Erteilung des Patents auf Basis der mit dieser Erwiderung eingereichten Ansprueche 1–18",
                 "Hilfsweise Erteilung auf Basis des Hilfsantrags I (Ansprueche 1H–18H)",
                 "Hilfsweise muendliche Verhandlung gem. § 46 PatG, sofern das Amt der Hauptantragsfassung nicht zu folgen gedenkt",
             ])),
            ("Anlagen",
             ("list", [
                 "Anlage 1: Neuer Hauptantrag-Anspruchssatz (16 Seiten)",
                 "Anlage 2: Hilfsantrag I (16 Seiten)",
                 "Anlage 3: Synoptische Darstellung Aenderungen ggue. urspruenglich eingereichter Fassung",
                 "Anlage 4: Vollmacht der anwaltschaftlichen Vertretung",
             ])),
            ("Unterschrift Anwaltschaft",
             f"Muenchen, {datum}\n\nVossius & Partner Patentanwaelte\nDr. Andreas Vossius, Patentanwalt\n"
             f"i. V. der Brennhagen Elektronik AG"),
        ])


def gate_review(fname, projekt, gate, produkt, datum, themen):
    write_doc(f"{B00}/{fname}", H,
        f"Stage-Gate-Review {gate} – Projekt {projekt}",
        subtitle=f"Produkt-/Plattformprojekt {produkt}; Gate-Datum {datum}",
        sections=[
            ("Projektkontext",
             f"Projekt: {projekt}\nProdukt/Plattform: {produkt}\nGate: {gate}\n"
             f"Projektphase: Concept → Development → Industrialization → SOP\n"
             f"Projektleitung: PMO REA, Werk REG/RSG je nach Modul.\nGremium: Vorstand REA + Programmleitung."),
            ("Pruefumfang im Gate",
             "Im Gate werden die Liefergegenstaende der vorangegangenen Phase gegen die definierten Gate-Kriterien "
             "(Quality Gates) gemaess Konzernprojektmanagement-Handbuch (PM-HB Rev. 4.2) geprueft. Dazu zaehlen: "
             "Anforderungsstatus (Requirements Engineering), Architektur-Reviews, Testabdeckung, Risiko-Register, "
             "Budget- und Termin-Forecast, Beschaffungsstrategie, Pruef- und Produktionsplanung."),
            ("Status der Gate-Kriterien",
             ("list", themen)),
            ("Risikoeinschaetzung",
             "Top-3-Projektrisiken: (1) Verfuegbarkeit Halbleiterkomponenten, (2) Software-Reifegrad Drittanbieter-Stack, "
             "(3) Validierungsdauer der Funktionssicherheit (ISO 26262 ASIL-B/C). Massnahmen: alternative Quellen "
             "evaluieren, Software-Lieferanten-Audit, paralleler Pruefaufbau im Validierungs-Lab Heilbronn."),
            ("Gate-Entscheidung",
             f"Das Gate {gate} wird vom Gate-Board (Vorstand REA / CTO Dr. Petra Hollmann + Programm) "
             f"unter Auflagen freigegeben. Die offenen Punkte werden im Aktionsplan dokumentiert; "
             f"Wiedervorlage in 6 Wochen zur Verifikation der Auflagenerfuellung. Naechstes Gate "
             f"(Folge-Gate) wird gemaess Projektplan terminiert."),
            ("Unterzeichnung",
             signatures("Dr. Petra Hollmann", "CTO", R["name"],
                        "Programmleitung", "PMO", R["name"],
                        place="Stuttgart", date_str_=datum)),
        ])


def testbericht(fname, projekt, testart, produkt, datum, ergebnisse):
    write_doc(f"{B00}/{fname}", H,
        f"Testbericht {testart} – {produkt}",
        subtitle=f"Projekt {projekt}; Pruefdatum {datum}",
        sections=[
            ("Pruefgegenstand",
             f"Produkt/Modul: {produkt}\nProjekt: {projekt}\nTestart: {testart}\n"
             f"Pruefstand: Validierungs-Labor Werk Heilbronn (REG) / Test-Labor Werk Muenchen (RSG)\n"
             f"Pruefbericht-Nummer: TR-{projekt[-3:]}-{datum.replace('.','')}\n"
             f"Pruefverantwortlich: Q-Ingenieur REG / RSG"),
            ("Pruefnorm und Pruefumfang",
             "Pruefung nach internem Pruefplan unter Beruecksichtigung der einschlaegigen Normen "
             "(IATF 16949, je nach Pruefart: ISO 16750, ISO 11452 EMV, ISO 26262 funktionale Sicherheit, "
             "AEC-Q100 Stresstests, IEC 60068 Klima). Pruefumfang umfasst Funktionstest, Stresstest "
             "(elektrisch/thermisch), EMV-Pruefung (Storfestigkeit / Emission), Schock und Vibration "
             "gem. OEM-Spezifikation. Stichprobenumfang gemaess Sampling Plan."),
            ("Pruefergebnisse",
             ergebnisse),
            ("Bewertung und Massnahmen",
             "Auf Basis der dokumentierten Messwerte wird das Pruefobjekt im Pruefumfang als »freigegeben« "
             "fuer den naechsten Entwicklungsschritt eingestuft. Festgestellte Abweichungen werden im "
             "Mass­nahmenplan (CAPA) erfasst und im Folge-Gate verifiziert. Eine Nachpruefung (Re-Test) "
             "wird fuer die kritischen Pruefpunkte nach Aenderungseinfuehrung empfohlen."),
            ("Anlagen",
             ("list", [
                 "Anlage 1: Pruefplan und Pruefspezifikation",
                 "Anlage 2: Messwerttabellen (Excel)",
                 "Anlage 3: Pruefling-Konfiguration und Pruefaufbau-Fotos",
                 "Anlage 4: Kalibrierprotokolle der verwendeten Messmittel",
             ])),
            ("Freigabe",
             signatures("Q-Ingenieur", "Pruefverantwortlich", "REG / RSG",
                        "Werkleitung / Q-Leitung", "Freigabe", R["name"],
                        place="Heilbronn / Muenchen", date_str_=datum)),
        ])


# ─────────────────────────────────────────────────────────────────────────────
# 01_AG_Gesellschaftsrecht — REMNANTS (misplaced filename types)
# ─────────────────────────────────────────────────────────────────────────────
def directors_dealings(fname, person, funktion, dealings):
    write_doc(f"{B01}/{fname}", H,
        f"Meldung Eigengeschaefte von Fuehrungskraeften (Directors' Dealings) – {person}",
        subtitle="Mitteilung gem. Art. 19 MAR (Marktmissbrauchsverordnung)",
        sections=[
            ("Meldepflichtige Person",
             f"Name: {person}\nFunktion: {funktion}\nUnternehmen: Brennhagen Elektronik AG\n"
             f"Eingestuft als Person mit Fuehrungsaufgaben (Person Discharging Managerial Responsibilities, "
             f"PDMR) gem. Art. 3 Abs. 1 Nr. 25 MAR und in der internen PDMR-Liste gefuehrt."),
            ("Angaben zum Emittenten / Finanzinstrument",
             "Emittent: Brennhagen Elektronik AG, Vaihinger Strasse 120, 70567 Stuttgart\n"
             "LEI: 529900RHGRPMOCKLEI42\nFinanzinstrument: Stammaktien\n"
             "ISIN: DE000RHGRP12  /  WKN: RHGRP1\nHandelsplatz: Frankfurter Wertpapierbörse (Prime Standard) / XETRA"),
            ("Einzelheiten der Geschaefte",
             dealings),
            ("Veroeffentlichung",
             "Diese Meldung erfolgt fristgerecht binnen drei Geschaeftstagen nach dem Geschaeft an die "
             "BaFin (über das BaFin-Meldeportal MVP) und die Brennhagen Elektronik AG. Die Veroeffentlichung "
             "ueber europaweit verbreitende Medien (Dienstleister: EQS Group) ist innerhalb derselben Frist "
             "erfolgt; auf der IR-Website (www.roehrig-ag.de/ir) wird die Meldung mindestens 5 Jahre vorgehalten."),
            ("Schwellenwertbetrachtung",
             "Geprueft wurde, ob die Schwelle gem. Art. 19 Abs. 8 MAR (5.000 EUR pro Kalenderjahr, kumuliert) "
             "erreicht wurde. Bei Ueberschreitung wird die Meldung – unabhaengig von der Einzeltransaktion – "
             "veroeffentlicht. Dokumentation der Schwellenwertberechnung erfolgt durch Investor Relations / "
             "Group Legal (Aktenfuehrung im Insider-Verzeichnis und PDMR-Register)."),
            ("Hinweis Closed Period",
             "Vor der Veroeffentlichung von Quartals- und Jahresergebnissen gilt die Closed-Period-Regel "
             "(30 Kalendertage) gem. Art. 19 Abs. 11 MAR. Die hier gemeldeten Transaktionen liegen "
             "ausserhalb dieses Zeitraums."),
            ("Unterschrift / Bestaetigung",
             signatures(person, funktion, R["name"],
                        "Investor Relations", "IR Officer", R["name"],
                        place="Stuttgart", date_str_="2023")),
        ])


def lessons_learned(fname, projekt, produkt, themen):
    write_doc(f"{B01}/{fname}", H,
        f"Lessons Learned – Projekt {projekt}",
        subtitle=f"Post-Mortem / Reflexionsbericht zum Produkt {produkt}",
        sections=[
            ("Projektkontext",
             f"Projekt: {projekt}\nProdukt/Plattform: {produkt}\n"
             f"Projektzeitraum: 2023–2024, Projektphase Concept Study (bis Gate G4)\n"
             f"Projektleitung: PMO REA in Abstimmung mit Werk REG und R&D RSG\n"
             f"Gremium: Vorstand REA / Programmleitung."),
            ("Was lief gut?",
             ("list", themen[:5] if len(themen) >= 5 else themen)),
            ("Was lief nicht gut?",
             ("list", themen[5:10] if len(themen) > 5 else [
                 "Spaete Beruecksichtigung der Cybersecurity-Anforderungen (ISO/SAE 21434)",
                 "Unklare Schnittstellen zwischen Hardware- und Software-Team (REG ↔ RSG)",
                 "Lieferantenqualifizierung nicht im kritischen Pfad eingeplant",
                 "Concept-Phase ueberzog um 8 Wochen; Re-Plan war notwendig",
                 "Reviews mit OEM-Kunden zu spaet eskaliert",
             ])),
            ("Empfehlungen fuer Folgeprojekte",
             ("list", [
                 "Cybersecurity-Anforderungen ab Lasten-/Pflichtenheft (Gate G1) parallel aufnehmen",
                 "Cross-Funktionale Reviews REG ↔ RSG ab Konzeptphase im Wochenrhythmus",
                 "Lieferantenqualifizierung im kritischen Pfad mit Pufferzeit von 4 Wochen",
                 "Stakeholder-Management-Plan zu Projektstart abnehmen lassen",
                 "Verbindliche Anwesenheitspflicht der OEM-Programmleitung in Gate-Reviews",
                 "Risiko-Register quartalsweise im PMO-Board nachhalten",
             ])),
            ("Naechste Schritte",
             "Die Lessons Learned werden im Konzern-PM-Handbuch (Rev. 4.3) eingearbeitet und im Programm-"
             "Management-Bord (PMB) vorgestellt. Die Erkenntnisse werden gezielt in den Folgeprojekten "
             "ECU-1100 Concept Study sowie BMS-13 Concept Study aufgegriffen. Verantwortlich fuer die "
             "Integration: PMO Lead REA in Abstimmung mit CTO Dr. Petra Hollmann."),
            ("Unterzeichnung",
             signatures("Projektleitung", "PMO", R["name"],
                        "Dr. Petra Hollmann", "CTO", R["name"],
                        place="Stuttgart", date_str_="Q1/2024")),
        ])


def vw_qbr_b01(fname, produkt, jahr, quartal, themen, statusampel):
    """Same as vw_qbr but writes to B01."""
    write_doc(f"{B01}/{fname}", H,
        f"Quarterly Business Review {produkt} – Volkswagen AG, {quartal}/{jahr}",
        subtitle=f"Kundenstatus, Lieferperformance, Projekt-Pipeline und Eskalationen mit Volkswagen Group",
        sections=[
            ("Teilnehmer",
             "Volkswagen AG (Wolfsburg): Einkaufsleitung Komponente, Qualitaetsmanagement-OEM, "
             "Programm-Management E-Mobility / Powertrain, ggf. Vertreter Vorserienentwicklung.\n\n"
             "Brennhagen Elektronik AG / REG: Stefan Richter (CMO/BD), Key Account Manager VW, "
             "Werkleitung REG (Andreas Maier), Qualitaetsleitung (Sabine Brand), "
             "ggf. Vertreter R&D / Programm."),
            ("Berichtszeitraum und Scope",
             f"Quartalsbericht {quartal}/{jahr} zum Produkt {produkt}. Scope: Liefermengen, Qualitaetsperformance, "
             f"Reklamationsstatus, Forecast Folgequartale, Pipeline neuer Designwins / RFQ, "
             f"strategische Themen (z. B. Cyber, Software-OTA, ASPICE, IATF, Carbon Footprint)."),
            ("Operative KPIs Status",
             [["KPI", "Ziel", "Ist", "Status"]] + statusampel),
            ("Schwerpunktthemen / Eskalationen",
             ("list", themen)),
            ("Vereinbarungen / Naechste Schritte",
             "Naechstes QBR turnusmaessig im Folgequartal. Offene Themen werden im OEM-Eskalationsboard "
             "nachverfolgt. Aktionen mit Termin und Verantwortlichen sind im QBR-Action-Tracker (Anhang) "
             "festgehalten. Eskalationspfad: REG → Stefan Richter → Anna Mueller (CEO REA) / "
             "Programm-Direktor VW."),
            ("Unterzeichnung",
             signatures("Stefan Richter", "CMO/BD REA", R["name"],
                        "Programmleitung VW", "Einkauf / QM", "Volkswagen AG",
                        place="Wolfsburg", date_str_=f"{quartal}/{jahr}")),
        ])


def testbericht_b01(fname, projekt, testart, produkt, datum, ergebnisse):
    write_doc(f"{B01}/{fname}", H,
        f"Testbericht {testart} – {produkt}",
        subtitle=f"Projekt {projekt}; Pruefdatum {datum}",
        sections=[
            ("Pruefgegenstand",
             f"Produkt/Modul: {produkt}\nProjekt: {projekt}\nTestart: {testart}\n"
             f"Pruefstand: EMV-Labor REG Heilbronn (akkreditiert nach DIN EN ISO/IEC 17025).\n"
             f"Pruefbericht-Nummer: TR-{projekt[-3:]}-{datum.replace('.','')}\n"
             f"Pruefverantwortlich: Q-Ingenieur EMV (REG)"),
            ("Pruefnorm und Pruefumfang",
             "Pruefung gem. ISO 11452 (Storfestigkeit kapazitiv/induktiv/HF), CISPR 25 (Funkstoraussendung), "
             "und kundenspezifischen EMV-Anforderungen (OEM-Spec). Pruefkategorien: Bulk-Current-Injection (BCI), "
             "Antennenmessung im Reverberation-Chamber, Trapeztest, ESD nach ISO 10605. Pruefling im "
             "Betriebsmodus 1 (normaler Betrieb) und Betriebsmodus 2 (Standby) bewertet."),
            ("Pruefergebnisse",
             ergebnisse),
            ("Bewertung und Massnahmen",
             "Der Pruefling erfuellt die spezifizierten EMV-Anforderungen in allen Pruefdisziplinen. "
             "Empfohlene Massnahmen: keine. Empfohlene Folgepruefung im Rahmen der Serienueberwachung "
             "(jaehrliche Re-Pruefung gemaess Konzern-EMV-Plan)."),
            ("Anlagen",
             ("list", [
                 "Anlage 1: EMV-Pruefplan und -spezifikation (8 Seiten)",
                 "Anlage 2: Messprotokolle / Spektrumsdiagramme",
                 "Anlage 3: Konformitaetserklaerung des Pruefverantwortlichen",
                 "Anlage 4: Kalibrierprotokolle der Messmittel",
             ])),
            ("Freigabe",
             signatures("Q-Ingenieur EMV", "Pruefverantwortlich", "Brennhagen Elektronik GmbH (REG)",
                        "Q-Leitung REG", "Sabine Brand", "Brennhagen Elektronik GmbH",
                        place="Heilbronn", date_str_=datum)),
        ])


def arbeitsvertrag_b01(fname, mitarbeiter, position, ort_short, jahr,
                       gehalt_eur, eintritt):
    t = S[ort_short]
    write_doc(f"{B01}/{fname}", H,
        f"Arbeitsvertrag – {mitarbeiter}",
        subtitle=f"zwischen {t['name']} und {mitarbeiter}; Eintritt {eintritt}",
        sections=[
            ("Vertragsparteien",
             f"Arbeitgeberin: {t['name']} (»{t['short']}«), {t['city']} ({t['country']}), {t['hrb']}.\n\n"
             f"Arbeitnehmer/in: {mitarbeiter}\nGeburtsdatum / Anschrift / Bankverbindung: gemaess Personalakte.\n\n"
             f"Der Vertrag wird in deutscher (Arbeits-)Sprache geschlossen; ergaenzend gilt die jeweilige "
             f"lokale Rechtsordnung am Beschaeftigungsort ({t['country']}). Im Konfliktfall ist die deutsche "
             f"Fassung massgeblich, soweit lokale zwingende Vorschriften nicht entgegenstehen."),
            ("Position und Aufgaben",
             f"Position: {position}\n\n"
             f"Aufgaben: Die Position umfasst die im Stellenprofil definierten Tatigkeiten und die zugehoerigen "
             f"Verantwortlichkeiten innerhalb des jeweiligen Fachbereichs der Tochtergesellschaft {t['short']}. "
             f"Die Stelle berichtet an die jeweils zustaendige Bereichsleitung / Werkleitung. "
             f"Eine ausfuehrliche Stellenbeschreibung ist als Anlage 1 dem Vertrag beigefuegt."),
            ("Eintrittstermin und Probezeit",
             f"Beginn des Arbeitsverhaeltnisses: {eintritt}.\n"
             f"Probezeit: 6 Monate ab Eintritt. Waehrend der Probezeit kann das Arbeitsverhaeltnis von beiden "
             f"Seiten mit einer Frist von 2 Wochen ordentlich gekuendigt werden."),
            ("Verguetung",
             f"Jaehrliches Bruttogehalt: {gehalt_eur} EUR, zahlbar in 12 monatlichen Raten zum Monatsletzten. "
             f"Variable Verguetung (Bonus): bis zu 15 % des Jahresgrundgehalts, abhaengig von der Erreichung "
             f"persoenlicher und unternehmensbezogener Ziele (Bonusvereinbarung jaehrlich gesondert). "
             f"Zusatzleistungen: Beitrag zur betrieblichen Altersversorgung, Gruppenunfallversicherung, "
             f"Berufsunfaehigkeits-Zuschuss, lokal uebliche Sozialleistungen."),
            ("Arbeitszeit / Urlaub",
             f"Regelmaessige woechentliche Arbeitszeit: 40 Stunden, gleitende Arbeitszeit gem. Betriebsvereinbarung. "
             f"Urlaubsanspruch: 30 Werktage pro Kalenderjahr (anteilig bei unterjaehrigem Ein-/Austritt). "
             f"Mehrarbeit ist mit dem Gehalt abgegolten, soweit nicht durch zwingende Vorschriften "
             f"vergueteter Mehrarbeitsanspruch besteht."),
            ("Vertraulichkeit und Wettbewerbsverbot",
             "Der/die Arbeitnehmer/in verpflichtet sich zur Vertraulichkeit ueber alle ihm/ihr im Rahmen der "
             "Taetigkeit bekanntgewordenen Geschaefts- und Betriebsgeheimnisse, auch ueber das Ende des "
             "Arbeitsverhaeltnisses hinaus. Ein nachvertragliches Wettbewerbsverbot kann gesondert vereinbart "
             "und ggf. mit Karenzentschaedigung verbunden werden (Anlage 2)."),
            ("Sonstige Bestimmungen",
             "Aenderungen und Ergaenzungen dieses Vertrags beduerfen der Schriftform; gleiches gilt fuer "
             "die Aufhebung dieser Schriftformklausel. Sollten einzelne Bestimmungen unwirksam sein, bleibt "
             "die Wirksamkeit der uebrigen Bestimmungen unberuehrt. Gerichtsstand und anwendbares Recht: "
             f"je nach Beschaeftigungsort {t['country']}; subsidiaer deutsches Recht."),
            ("Unterschriften",
             signatures(f"Werkleitung {t['short']}", "Arbeitgeberin", t['name'],
                        mitarbeiter, "Arbeitnehmer/in", "—",
                        place=t['city'], date_str_=eintritt)),
        ])


# ─────────────────────────────────────────────────────────────────────────────
# ─── INVOCATIONS ────────────────────────────────────────────────────────────
# ─────────────────────────────────────────────────────────────────────────────

# ===== 28 Konzernrichtlinien =====
KR_PARAMS = [
    ("Konzernrichtlinie_AntiKorruption_2023_WIP.docx", "Anti-Korruption",
     "Anti-Korruption und Anti-Bestechung",
     "Chief Compliance Officer", "Group Compliance Office",
     ["Striktes Verbot von Bestechung im In- und Ausland (UK Bribery Act, FCPA-Standard)",
      "Geschenke und Einladungen max. 50 EUR Wert pro Person/Jahr ohne Genehmigung; ueber 50 EUR Eintragung im Geschenke-Register",
      "Spenden und Sponsoring ausschliesslich nach 4-Augen-Freigabe Compliance + Vorstand",
      "Keine Zahlungen an politische Parteien oder Amtstraeger im Zusammenhang mit Geschaeftsentscheidungen",
      "Gesonderte Sorgfaltspflicht bei Drittparteien (Berater, Agenten, Vertriebspartner) inkl. Background Check",
      "Erweiterte Pruefung bei Geschaeften in Hochrisikolaendern (CPI Transparency International < 50)"],
     ["Compliance-Schulungsabdeckung > 95 % aller Mitarbeiter jaehrlich",
      "Anzahl gemeldeter Verdachtsfaelle und Bearbeitungszeit (Whistleblowing)",
      "Geschenkeregister-Eintraege quartalsweise reviewt",
      "Anteil Drittparteien mit aktuellem Compliance-Check > 95 %"],
     ["UK Bribery Act 2010", "US Foreign Corrupt Practices Act 1977", "OECD-Antikorruptions-Konvention",
      "§§ 299, 331-337 StGB", "ISO 37001 Anti-Bribery Management Systems"]),
    ("Konzernrichtlinie_Arbeitssicherheit_2023.docx", "Arbeitssicherheit",
     "Arbeits- und Gesundheitsschutz",
     "Konzern-Sicherheitsbeauftragter", "Group EHS Office",
     ["Verbindliche Gefaehrdungsbeurteilung jeder Arbeitsstation gem. ArbSchG / BetrSichV",
      "Persoenliche Schutzausruestung (PSA) verbindlich in allen Produktionsbereichen",
      "Unterweisungspflicht bei Eintritt und mind. jaehrlich danach (mind. 60 Min., dokumentiert)",
      "Beinaheunfaelle (Near-Miss) verpflichtend zu melden",
      "Sicherheitsaudits jaehrlich an jedem Standort durch zertifizierte interne Auditoren",
      "Notfall- und Evakuierungsplaene mit mind. jaehrlicher Uebung"],
     ["Lost Time Injury Frequency Rate (LTIFR) Ziel < 3 pro Mio. Arbeitsstunden",
      "Total Recordable Incident Rate (TRIR) Ziel < 5",
      "Schulungsabdeckung Arbeitssicherheit > 98 % aller Mitarbeiter",
      "Quote behobener Audit-Findings binnen 90 Tagen > 90 %"],
     ["ArbSchG", "BetrSichV", "DGUV-Vorschriften 1 und 2", "ISO 45001:2018"]),
    ("Konzernrichtlinie_Compliance_2023.docx", "Compliance",
     "Compliance Management System (CMS)",
     "Chief Compliance Officer", "Group Compliance Office",
     ["Etablierung eines Compliance-Management-Systems nach IDW PS 980",
      "Klare Eskalationswege ueber Compliance Officer an Vorstand und Pruefungsausschuss",
      "Risikobasierter Compliance-Plan, jaehrlich aktualisiert",
      "Compliance-Schulungen verpflichtend (E-Learning + Praesenz fuer Risikofunktionen)",
      "Whistleblower-Hotline (24/7, extern betrieben durch Anbieter EQS Integrity Line)",
      "Quartalsweises Compliance-Reporting an Pruefungsausschuss des Aufsichtsrats"],
     ["Anzahl bearbeiteter Compliance-Faelle pro Quartal",
      "Schulungsabdeckung > 95 % aller Mitarbeiter",
      "Reaktionszeit auf Hinweise < 5 Werktage",
      "Compliance-Audit-Score jaehrlich > 85 / 100"],
     ["IDW PS 980", "ISO 37301:2021 Compliance Management Systems", "BaFin MaRisk"]),
    ("Konzernrichtlinie_Datenschutz_2023.docx", "Datenschutz",
     "Datenschutz und Verarbeitung personenbezogener Daten",
     "Konzern-Datenschutzbeauftragter", "Group Data Protection Office",
     ["Verarbeitung personenbezogener Daten ausschliesslich auf rechtmaessiger Grundlage (Art. 6 DSGVO)",
      "Bestellung von Datenschutzbeauftragten gem. Art. 37 DSGVO in allen DE/EU-Gesellschaften",
      "Verzeichnis von Verarbeitungstaetigkeiten (Art. 30 DSGVO) laufend aktualisiert",
      "Auftragsverarbeitungsvertraege (AVV) gem. Art. 28 DSGVO mit allen Dienstleistern",
      "Datenschutz-Folgenabschaetzung (DSFA) fuer Hochrisikoverarbeitungen",
      "Meldepflicht bei Datenschutzverletzungen binnen 72h an Aufsichtsbehoerde"],
     ["Anzahl gemeldeter Datenschutzvorfaelle pro Jahr",
      "Erfuellungsquote Betroffenenrechte (Antworten binnen 30 Tagen) > 95 %",
      "DSGVO-Schulungsabdeckung > 95 % aller Mitarbeiter",
      "Anzahl offener DSFA-Massnahmen > 90 Tage = 0"],
     ["DSGVO (VO (EU) 2016/679)", "BDSG-neu", "TTDSG", "ePrivacy-Verordnung (Entwurf)"]),
    ("Konzernrichtlinie_Datensicherung_2023.docx", "Datensicherung",
     "Datensicherung und Backup",
     "Group CIO", "Group IT",
     ["Verbindliche Backup-Strategie nach 3-2-1-Regel (3 Kopien, 2 Medientypen, 1 offsite)",
      "Backup-Frequenzen: kritische Systeme stuendlich, Standard taeglich, Archiv monatlich",
      "Wiederherstellungstests mind. quartalsweise je Anwendung",
      "Geo-redundante Backups in DE / mind. zweite EU-Region",
      "RPO (Recovery Point Objective) max. 4 Stunden fuer kritische Systeme",
      "RTO (Recovery Time Objective) max. 8 Stunden fuer kritische Systeme"],
     ["Erfolgreiche Backup-Quote > 99 %",
      "Wiederherstellungstests bestanden > 95 %",
      "Anzahl Datenverlustvorfaelle pro Jahr = 0",
      "Mean Time to Recover (MTTR) bei Ausfaellen < 8h"],
     ["ISO 27001:2022", "BSI IT-Grundschutz", "NIS-2-Richtlinie", "DSGVO Art. 32"]),
    ("Konzernrichtlinie_Exportkontrolle_2023.docx", "Exportkontrolle",
     "Exportkontrolle und Sanktionen",
     "Konzern-Exportkontrollbeauftragter", "Group Trade Compliance",
     ["Pruefung jeder Exporttransaktion gegen EU-Dual-Use-VO (VO 2021/821) und nationale Listen",
      "Sanktionslisten-Screening (EU-Konsolidierte Liste, OFAC SDN, UN) vor Vertragsschluss",
      "Endverbleibserklaerung (End User Statement) bei Dual-Use-Guetern verpflichtend",
      "Schulungspflicht fuer alle Mitarbeiter in Vertrieb, Versand, F&E",
      "Aussenwirtschaftsverordnung (AWV) Einhaltung; Genehmigungen ueber BAFA bzw. zustaendige nationale Behoerde",
      "Eskalation bei Verdachtsfaellen an Compliance Officer und ggf. Vorstand"],
     ["Anteil Transaktionen mit Sanktionspruefung 100 %",
      "Anzahl Verdachtsfaelle und Bearbeitungsstatus quartalsweise reportiert",
      "Schulungsabdeckung > 98 % der Mitarbeiter in betroffenen Funktionen",
      "Audit-Findings Trade Compliance < 5 pro Jahr"],
     ["EU Dual-Use-VO 2021/821", "AWG/AWV", "OFAC SDN", "UN-Sanktionsregimes", "EAR / ITAR (USA)"]),
    ("Konzernrichtlinie_Finanzberichterstattung_2023.docx", "Finanzberichterstattung",
     "Finanzberichterstattung (Internal Controls over Financial Reporting, ICFR)",
     "Group Controller", "Florian Maier",
     ["Konzern-Bilanzierungs- und Bewertungshandbuch nach IFRS verpflichtend in allen Gesellschaften",
      "Internes Kontrollsystem nach COSO 2013 mit jaehrlicher Selbst-Evaluation",
      "Vier-Augen-Prinzip bei allen Buchungen > 10 TEUR",
      "Konsolidierungssoftware (SAP Group Reporting) als Single Source of Truth",
      "Monatliche Abschluesse bis Werktag +7 nach Periodenende",
      "Externe Pruefung Konzernabschluss IFRS durch KPMG AG WPG (jaehrlich)"],
     ["Termintreue Monatsabschluss 100 %",
      "Anzahl Material Weaknesses ICFR = 0",
      "Auditor's Opinion uneingeschraenkt",
      "Audit-Findings ICFR < 10 pro Jahr"],
     ["IFRS", "HGB", "AktG", "IDW PS 261 / PS 980 / PS 982", "COSO 2013 Internal Control Framework"]),
    ("Konzernrichtlinie_Geschenke_2023.docx", "Geschenke und Einladungen",
     "Annahme und Gewaehrung von Geschenken und Einladungen",
     "Chief Compliance Officer", "Group Compliance Office",
     ["Geschenke und Einladungen bis 50 EUR Wert ohne Genehmigung zulaessig (1x pro Person/Jahr)",
      "Bei Wert > 50 EUR Eintrag im konzernweiten Geschenkeregister erforderlich",
      "Bei Wert > 200 EUR Genehmigung durch Vorgesetzte/n + Compliance Officer",
      "Bei oeffentlichen Amtstraegern grundsaetzlich verboten (Ausnahme: Hoeflichkeitsgeschenke gerings. Wertes)",
      "Geschenke in bar oder bargeldnahe Mittel grundsaetzlich verboten",
      "Einladungen zu OEM-Events nur mit Geschaeftsbezug (Werkstour, Fachkonferenz, RFQ-Praesentation)"],
     ["Anzahl Eintraege im Geschenkeregister pro Quartal",
      "Anzahl genehmigter Geschenke > 200 EUR pro Quartal",
      "Schulungsabdeckung Anti-Korruption > 95 %",
      "Compliance-Audits ohne Findings in diesem Themengebiet"],
     ["UK Bribery Act 2010", "§ 299 StGB", "OECD-Antikorruptions-Konvention", "interne Anti-Korruptions-Richtlinie"]),
    ("Konzernrichtlinie_Interessenkonflikte_2023.docx", "Interessenkonflikte",
     "Vermeidung und Management von Interessenkonflikten",
     "Chief Compliance Officer", "Group Compliance Office",
     ["Jaehrliche Selbstauskunft aller Fuehrungskraefte und Mitarbeiter in sensiblen Funktionen",
      "Meldepflicht bei Verwandtschafts-/Naheverhaeltnissen zu Geschaeftspartnern oder Mitarbeitern",
      "Verbot der Mitwirkung an Entscheidungen bei eigenem persoenlichem Vorteil",
      "Genehmigungspflicht fuer Nebentaetigkeiten",
      "Eintraege in konzernweites Interessenkonflikt-Register",
      "Klare Eskalationswege bei Verdachtsfaellen ueber Compliance Officer"],
     ["Anteil Mitarbeiter mit gueltiger Selbstauskunft > 95 %",
      "Anzahl gemeldeter Interessenkonflikte pro Jahr (Reporting)",
      "Anzahl genehmigter Nebentaetigkeiten",
      "Compliance-Audits ohne kritische Findings"],
     ["§ 88 AktG", "§ 181 BGB", "Konzernrichtlinie Anti-Korruption", "OECD Guidelines on MNE"]),
    ("Konzernrichtlinie_IP_Schutz_2023.docx", "IP-Schutz",
     "Schutz und Verwertung geistigen Eigentums (Intellectual Property)",
     "Group IP Manager", "Group R&D / Legal",
     ["Patentanmeldungen ueber zentrales Patent-Komitee (Quartalsweise)",
      "Klare Eigentumszuordnung: IP aus konzerninterner F&E gehoert grundsaetzlich der Brennhagen Elektronik AG",
      "Verbindliche IP-Klauseln in allen F&E- und Beratervertraegen",
      "Open-Source-Software-Management mit zentraler Pruefung der Lizenz-Kompatibilitaet",
      "Geheimhaltungs-Vereinbarungen (NDA) verpflichtend vor IP-relevanten Gespraechen",
      "FRAND-Erklaerungen bei Standardisierung (z. B. Automotive Ethernet)"],
     ["Anzahl Neu-Patente pro Jahr (Ziel > 20)",
      "Patenterteilungsquote > 70 %",
      "Anzahl Patentstreitigkeiten / Klagen pro Jahr",
      "OSS-Compliance-Findings pro Release = 0"],
     ["PatG", "EPC", "DSGVO bei personenbezogenen Trainingsdaten", "FRAND-Standards (ETSI, IEEE)"]),
    ("Konzernrichtlinie_IT_Security_2023.docx", "IT-Security",
     "Informationssicherheit",
     "Group CISO", "Group IT Security",
     ["ISMS nach ISO 27001 (Zertifizierung in Vorbereitung 2024)",
      "Multi-Faktor-Authentifizierung (MFA) verpflichtend fuer alle Mitarbeiter",
      "Passwort-Policy: mind. 14 Zeichen, alle 180 Tage Wechselpflicht in priv. Konten",
      "Patch-Management: kritische Sicherheits-Patches binnen 14 Tagen",
      "Endpoint Detection & Response (EDR) flaechendeckend",
      "Security Awareness Training mind. jaehrlich verpflichtend"],
     ["Anteil Endpoints mit aktuellem Patchstand > 95 %",
      "Anzahl sicherheitsrelevanter Vorfaelle pro Quartal (Reporting)",
      "Phishing-Simulation Klick-Quote < 5 %",
      "MFA-Abdeckung 100 %"],
     ["ISO 27001:2022", "BSI IT-Grundschutz", "NIS-2-Richtlinie", "TISAX (Automotive)"]),
    ("Konzernrichtlinie_Kapitalmarkt_2023.docx", "Kapitalmarkt",
     "Kapitalmarkt-Compliance und Insider-Recht",
     "Group General Counsel / IR", "Group Legal & IR",
     ["Fuehrung eines aktuellen Insiderverzeichnisses gem. Art. 18 MAR",
      "Closed-Period vor Quartalsmitteilungen (30 Tage) verbindlich",
      "Ad-hoc-Mitteilungen gem. Art. 17 MAR ueber zertifizierten Verbreitungsdienst (EQS Group)",
      "Directors' Dealings (PDMR-Geschaefte) Meldung binnen 3 Geschaeftstagen",
      "Stimmrechtsmeldungen (3/5/10/15/20/25/30 %) gem. § 33 WpHG",
      "Compliance-Schulung kapitalmarktrelevant fuer alle PDMR und nahestehenden Personen"],
     ["Termintreue Veroeffentlichung Quartalsberichte 100 %",
      "Anzahl Ad-hoc-Mitteilungen pro Jahr (Reporting)",
      "Anzahl Directors' Dealings-Meldungen 100 % fristgerecht",
      "Schulungsabdeckung kapitalmarktrelevant > 98 %"],
     ["MAR (VO (EU) 596/2014)", "WpHG", "WpPG", "Boersenordnung Frankfurter Wertpapierbörse"]),
    ("Konzernrichtlinie_Krise_BCP_2023.docx", "Krise und BCP",
     "Krisenmanagement und Business Continuity Planning",
     "Group Risk & BCM", "Group Risk Management",
     ["Etablierung Konzern-Krisenstab unter Leitung des CEO bei stufenweiser Krisenaktivierung",
      "Business Impact Analysis (BIA) je Standort jaehrlich aktualisiert",
      "Notfall- und Wiederanlaufplaene je kritischer Geschaeftsprozess",
      "Krisenuebungen mind. jaehrlich je Standort (Tabletop oder Vollsimulation)",
      "Konzern-weite Notfall-Kommunikationsmittel (Notfall-Alert-Tool, Mobile App)",
      "Externe Krisen-PR-Beratung im Standby (Hering Schuppener)"],
     ["BIA-Aktualitaet 100 %",
      "Anzahl Krisenuebungen pro Standort und Jahr >= 1",
      "RTO/RPO-Einhaltung in Uebungen",
      "Krisenkommunikations-Aktivierungszeit < 60 Min."],
     ["ISO 22301:2019 Business Continuity Management", "BSI 200-4", "EU NIS-2", "internes BCM-Handbuch"]),
    ("Konzernrichtlinie_LkSG_2023.docx", "LkSG (Lieferkettensorgfaltspflichten)",
     "Lieferkettensorgfaltspflichten gem. LkSG",
     "Group Sustainability Officer", "Group Sustainability / Procurement",
     ["Etablierung eines Risikomanagement-Systems gemaess § 4 LkSG",
      "Jaehrliche Risikoanalyse aller Direktlieferanten (Tier 1) und ausgewaehlter Tier-2/3",
      "Praeventions- und Abhilfemassnahmen bei festgestellten Risiken",
      "Verbindlicher Lieferanten-Verhaltenskodex (Supplier Code of Conduct)",
      "Beschwerdeverfahren fuer betroffene Personen entlang der Wertschoepfungskette",
      "Jaehrlicher LkSG-Bericht an Bundesamt fuer Wirtschaft und Ausfuhrkontrolle (BAFA)"],
     ["Anzahl auditierter Lieferanten pro Jahr",
      "Anzahl gemeldeter Beschwerden und Bearbeitungsstatus",
      "Anteil Lieferanten mit unterzeichnetem Code of Conduct > 95 %",
      "Korrigierte Findings binnen 12 Monaten > 90 %"],
     ["LkSG (Lieferkettensorgfaltspflichtengesetz)", "EU CSDDD (Vorbereitung)", "UN Guiding Principles on Business and Human Rights"]),
    ("Konzernrichtlinie_Nachhaltigkeit_ESG_2023.docx", "Nachhaltigkeit / ESG",
     "Nachhaltigkeit (Environmental, Social, Governance)",
     "Group Sustainability Officer", "Group Sustainability Office",
     ["Konzern-Klimaziele: Scope 1+2 -55 % bis 2030 (Basisjahr 2019), Net Zero 2045",
      "Scope 3 Reduktion durch Lieferanten-Programme und Produkt-CO2-Footprint",
      "ESG-Reporting nach CSRD / ESRS ab Geschaeftsjahr 2024",
      "Validierung Klimaziele durch Science Based Targets initiative (SBTi)",
      "Diversitaets- und Inklusionsstrategie: Frauenanteil Fuehrung > 30 % bis 2026",
      "EU-Taxonomie-Reporting verpflichtend"],
     ["CO2-Emissionen Scope 1+2 jaehrlich (absolut und intensitaetsnormiert)",
      "Anteil erneuerbare Energien im Strommix > 80 % bis 2026",
      "Frauenanteil Fuehrungspositionen (Reporting jaehrlich)",
      "EU-Taxonomie konforme Umsatz-/CAPEX-Anteile"],
     ["EU CSRD / ESRS", "EU Taxonomy Regulation", "TCFD", "GHG Protocol", "ISO 14001/50001"]),
    ("Konzernrichtlinie_Outsourcing_2023.docx", "Outsourcing",
     "Outsourcing und Sourcing-Strategie",
     "Group CPO", "Group Procurement",
     ["Outsourcing-Entscheidungen ueber Sourcing-Komitee (Vorstand-Vorsitz, CFO, CPO)",
      "Make-or-Buy-Analyse standardisiert (TCO-Modell, strategische Bedeutung)",
      "Wesentliche Outsourcing-Vertraege Genehmigungspflicht durch Vorstand ab 5 Mio. EUR p. a.",
      "Risikomanagement und Lieferanten-Audit bei kritischen Outsourcing-Partnern",
      "Backup-/Notfall-Plaene bei kritischen Outsourcing-Funktionen verpflichtend",
      "Exit-Strategie bei jedem Outsourcing-Vertrag dokumentiert"],
     ["Anteil Outsourcing-Vertraege mit aktiver Risikobewertung 100 %",
      "Anzahl Audits kritischer Outsourcing-Partner pro Jahr",
      "TCO-Einsparungen aus Sourcing-Initiativen (Reporting jaehrlich)",
      "Anzahl Outsourcing-bedingter Vorfaelle pro Jahr (Reporting)"],
     ["Konzernrichtlinie Unterschriftenregelung", "Konzernrichtlinie Risiko-Management",
      "ISO 31000 (Risk Management)", "BaFin MaRisk (sofern anwendbar bei Finanztochter)"]),
    ("Konzernrichtlinie_Personalentwicklung_2023.docx", "Personalentwicklung",
     "Personalentwicklung und Talent Management",
     "Group CHRO", "Group HR",
     ["Jaehrliches Mitarbeitergespraech (PE-Gespraech) mit Zielvereinbarung und Entwicklungsplanung",
      "Talent-Pool fuer Schluesselpositionen mit Nachfolgeplanung",
      "Weiterbildungsbudget pro Mitarbeiter mind. 800 EUR p. a.",
      "Leadership-Programme fuer Erst- und Zweitlinien-Fuehrungskraefte",
      "Mentoring-Programm konzernweit",
      "Job-Rotation und Auslandseinsaetze (insbesondere zwischen DE / PL / CZ / HU / CN)"],
     ["Anteil Mitarbeiter mit gefuehrtem PE-Gespraech > 95 %",
      "Nachfolgeabdeckung kritischer Positionen >= 2 Kandidaten je Position",
      "Anzahl Weiterbildungstage pro Mitarbeiter und Jahr > 5",
      "Mitarbeiterzufriedenheit (Engagement Survey) > 75 %"],
     ["BetrVG", "ArbZG", "internes Personalhandbuch"]),
    ("Konzernrichtlinie_Qualitaet_2023.docx", "Qualitaet",
     "Qualitaetsmanagement",
     "Group Quality Director", "Sabine Brand (Q-Leitung REG / Konzern-Q-Verantwortung)",
     ["Etablierung des Konzern-Qualitaetsmanagement-Systems nach IATF 16949 / ISO 9001",
      "VDA 6.3 Lieferanten-Audits jaehrlich fuer A-Lieferanten",
      "Klare Reklamationsbearbeitung mit 8D-Methodik bei jeder OEM-Reklamation",
      "Konzern-FMEA-Vorgehen (DFMEA / PFMEA) verbindlich in Entwicklung und Produktion",
      "Q-KPIs (PPM, FFR, Reklamationen) monatlich an Vorstand reportet",
      "Jaehrliche Q-Audits jedes Standorts durch Konzern-Audit-Team"],
     ["PPM-Quote OEM-Auslieferung (Ziel < 25 ppm)",
      "First-Pass-Yield (FPY) Endmontage > 99 %",
      "Anzahl OEM-Eskalationen pro Jahr (Reporting)",
      "Schliessrate 8D-Reports binnen 60 Tagen > 90 %"],
     ["IATF 16949:2016", "ISO 9001:2015", "VDA 6.3 / VDA 6.5", "AIAG Core Tools (APQP, FMEA, MSA, PPAP, SPC)"]),
    ("Konzernrichtlinie_Reisekosten_2023.docx", "Reisekosten",
     "Geschaeftsreisen und Reisekostenabrechnung",
     "Group Travel Manager", "Group Procurement / HR",
     ["Reisegenehmigung im Konzern-Travel-Tool (SAP Concur) vor Buchung",
      "Buchung ausschliesslich ueber zentralen Travel-Dienstleister BCD Travel",
      "Flugklasse: Economy bis 5h Flugzeit; Business ab 5h oder ab Director-Ebene",
      "Bahnreisen DB: 2. Klasse Standard; 1. Klasse fuer Reisen > 3h oder ab Director-Ebene",
      "Hotel-Kategorie max. 4* (Ausnahmen bei OEM-/Konferenzhotels)",
      "Verpflegungspauschale gemaess Bundesreisekostengesetz"],
     ["Reisekosten pro Kopf p. a. (Konzern-Reporting)",
      "Anteil ueber Travel-Dienstleister gebuchter Reisen > 95 %",
      "CO2-Emissionen aus Geschaeftsreisen (Konzern-Reporting)",
      "Anteil Bahnreisen statt Inlandsflug > 70 %"],
     ["EStG", "BRKG", "interne Reiserichtlinie", "Konzernrichtlinie Nachhaltigkeit ESG 2023"]),
    ("Konzernrichtlinie_Social_Media_2023.docx", "Social Media",
     "Social Media Nutzung",
     "Group Communications", "Group Corporate Communications",
     ["Klare Trennung zwischen offizieller Konzernkommunikation und privater Mitarbeiterkommunikation",
      "Verbot der Veroeffentlichung vertraulicher Geschaefts- und Kundendaten in Social Media",
      "Pflicht zur Kennzeichnung als Mitarbeiter, wenn ueber den Konzern berichtet wird",
      "Krisenkommunikation in Social Media ausschliesslich durch Corporate Communications",
      "Vorgaben zur DSGVO-konformen Verwendung von Mitarbeiterfotos",
      "Schulungspflicht fuer Mitarbeiter mit Aussenwirkung (Sales, IR, PR)"],
     ["Anzahl Social-Media-Compliance-Vorfaelle pro Jahr (Reporting)",
      "Schulungsabdeckung der relevanten Funktionen > 90 %",
      "Anzahl gemeldeter unzulaessiger Beitraege pro Quartal",
      "Reaktionszeit Krisenkommunikation < 4h"],
     ["MAR", "DSGVO", "UWG", "internes Kommunikationshandbuch"]),
    ("Konzernrichtlinie_Treasury_2023.docx", "Treasury",
     "Konzern-Treasury (Cash Management, FX, Finanzierung)",
     "Group Treasurer", "Markus Pflanzer",
     ["Cash-Pooling EUR ueber zentrale Konzern-Cash-Pool-Struktur (Deutsche Bank, Commerzbank)",
      "FX-Hedging-Quote 80–90 % der erwarteten EUR-Exposures (CNY, USD, CZK, HUF, PLN)",
      "Hedging ausschliesslich mit Banken aus der 5-Kernbanken-Liste",
      "Anlage liquider Mittel ausschliesslich in Investment-Grade-Geldmarktinstrumenten",
      "Kreditaufnahme > 25 Mio. EUR ausschliesslich mit Vorstandsfreigabe (CFO + CEO)",
      "Quartalsweises Treasury-Reporting an Vorstand und Aufsichtsrat (CFO-Bericht)"],
     ["Net Debt / EBITDA <= 3,0x (Covenant)",
      "Interest Coverage Ratio >= 4,0x (Covenant)",
      "Eigenkapitalquote >= 30 % (Covenant)",
      "Hedging-Quote pro Waehrungspaar (Reporting jaehrlich)"],
     ["IFRS 9 (Hedge Accounting)", "Konsortialkreditvertrag 2022", "BaFin-MaRisk soweit anwendbar"]),
    ("Konzernrichtlinie_Umwelt_2023.docx", "Umwelt",
     "Umweltmanagement",
     "Group EHS Director", "Group EHS Office",
     ["Etablierung Umweltmanagement-System nach ISO 14001 an allen Produktionsstandorten",
      "Energiemanagement-System nach ISO 50001 (Werke Heilbronn, Katowice, Brno, Gyoer)",
      "CO2-Bilanzierung Scope 1+2 jaehrlich, Scope 3 schrittweise ausgebaut",
      "Wasser-, Abfall- und Gefahrstoff-Reporting standardisiert",
      "Investitionen in erneuerbare Energien (PV-Anlagen Werk Heilbronn / Katowice geplant)",
      "Lieferanten werden in das Konzern-Umweltprogramm einbezogen (SCOPE 3)"],
     ["CO2-Emissionen Scope 1+2 jaehrlich (absolut und je Mio. EUR Umsatz)",
      "Anteil erneuerbarer Energien im Strommix > 80 % bis 2026",
      "Wasserverbrauch je Mio. EUR Umsatz (jaehrliches Reporting)",
      "Recyclingquote Abfall > 90 %"],
     ["ISO 14001:2015", "ISO 50001:2018", "EU EHS-Verordnungen", "CSRD ESRS-E1"]),
    ("Konzernrichtlinie_Unterschriftenregelung_2023.docx", "Unterschriftenregelung",
     "Unterschriftenregelung und Vertretungsbefugnisse",
     "Group General Counsel", "Group Legal",
     ["Geschaeftsfuehrungs- und Vorstandshandeln in Vier-Augen-Form (zwei Mitglieder gemeinsam)",
      "Prokuristen vertreten gemeinsam mit einem Vorstandsmitglied oder einem weiteren Prokuristen",
      "Generalvollmachten und Handlungsvollmachten gem. § 54 HGB",
      "Wertgrenze 5 Mio. EUR fuer Einzelvollmacht; darueber Vorstandsfreigabe",
      "Unterschriftsregister im Group Legal Office laufend aktualisiert",
      "Vollmachten erlöschen automatisch beim Ausscheiden aus dem Konzern"],
     ["Unterschriftsregister-Aktualitaet 100 %",
      "Anzahl ausgestellter Vollmachten pro Jahr (Reporting)",
      "Compliance-Audit-Findings Unterschriftenregelung < 3 pro Jahr",
      "Erfuellungsquote 4-Augen-Prinzip in Stichprobenpruefungen 100 %"],
     ["BGB §§ 164 ff., 167", "HGB §§ 48 ff. (Prokura), § 54 (Handlungsvollmacht)",
      "AktG / GmbHG", "interne Konzern-Geschaeftsordnung"]),
    ("Konzernrichtlinie_Whistleblowing_2023.docx", "Whistleblowing",
     "Hinweisgeber-System (Whistleblowing)",
     "Chief Compliance Officer", "Group Compliance Office",
     ["Einrichtung einer Konzern-Hinweisgeber-Hotline (24/7, mehrsprachig) ueber externen Dienstleister EQS Integrity Line",
      "Anonyme Meldungen sind ausdruecklich moeglich und geschuetzt",
      "Vertraulichkeitsgarantie fuer Hinweisgeber gem. HinSchG / EU Whistleblowing-Richtlinie",
      "Verbot von Repressalien (Diskriminierung, Kuendigung) gegen Hinweisgeber",
      "Bearbeitungsfristen: Eingangsbestaetigung 7 Tage, Rueckmeldung 90 Tage",
      "Konzern-weites Hinweisgeber-Komitee unter Leitung des Chief Compliance Officer"],
     ["Anzahl Meldungen pro Jahr (Reporting)",
      "Anteil bearbeiteter Meldungen binnen 90 Tagen > 95 %",
      "Anteil substantiierter Meldungen mit Massnahmen (Reporting)",
      "Befragungsergebnis Vertrauen in Hinweisgeber-System > 70 %"],
     ["HinSchG", "EU Whistleblower-Richtlinie (EU) 2019/1937", "MAR", "interne Anti-Korruptions-Richtlinie"]),
]
# AntiKorruption is WIP, all others are released.
WIP_KR_FILENAMES = {"Konzernrichtlinie_AntiKorruption_2023_WIP.docx"}

for params in KR_PARAMS:
    fname = params[0]
    konzern_richtlinie(*params, wip=(fname in WIP_KR_FILENAMES))


# ===== 5 SLA Management-Dienstleistungen =====
sla_management("SLA_Managementdienstleistungen_RHO_REG_2023.docx", "REG")
sla_management("SLA_Managementdienstleistungen_RHO_RSG_2023.docx", "RSG")
sla_management("SLA_Managementdienstleistungen_RHO_RPL_2023.docx", "RPL")
sla_management("SLA_Managementdienstleistungen_RHO_RCZ_2023_WIP.docx", "RCZ", wip=True)
sla_management("SLA_Managementdienstleistungen_RHO_RHU_2023.docx", "RHU")


# ===== 4 IC Dienstleistungs-Vertraege =====
ic_dienstleistung("IC_Dienstleistung_RCZ_REG_2023.docx", "RCZ", "REG",
                  "Spezial-Steckverbinder-Fertigung (Sonderlose < 5 kStk/Monat) inkl. Pruefung am Standort Brno fuer Werk Heilbronn",
                  volumen_tEUR=380, frequenz="laufend")
ic_dienstleistung("IC_Dienstleistung_REG_RHU_2023.docx", "REG", "RHU",
                  "Engineering-Support fuer Sensorik-Plattform (Aufbau Linien-Erweiterung Werk Gyoer); REG-Fachkraefte als Trainer und im Anlauf-Support",
                  volumen_tEUR=220, frequenz="punktuell mit fester Stundenkapazitaet")
ic_dienstleistung("IC_Dienstleistung_REG_RPL_2023.docx", "REG", "RPL",
                  "Werkzeug- und Vorrichtungsbau (Sondermaschinen, Pruefmittel) ueber Werk Heilbronn fuer Werk Katowice",
                  volumen_tEUR=560, frequenz="projektbezogen mit Rahmenkontingent")
ic_dienstleistung("IC_Dienstleistung_RSG_REG_2023.docx", "RSG", "REG",
                  "Embedded-Software-Entwicklung (Firmware-Updates, OTA-Plattform-Support, Variantenpflege) durch RSG Muenchen fuer REG-Hauptlinien",
                  volumen_tEUR=1850, frequenz="laufend")


# ===== 14 Konzern-Governance-Quartalsreports =====
TOCHTER_STATUS = [
    ["REA (Mutter)", "Stuttgart (DE)", "voll konform", "—"],
    ["REG", "Heilbronn (DE)", "voll konform", "—"],
    ["RSG", "Muenchen (DE)", "voll konform", "—"],
    ["RPL", "Katowice (PL)", "voll konform", "Audit-Findings aus 2022 abgearbeitet"],
    ["RCZ", "Brno (CZ)", "voll konform", "—"],
    ["RHU", "Gyoer (HU)", "voll konform", "—"],
    ["RCN", "Shanghai (CN)", "voll konform", "Cyber-Audit Q2 erfolgreich"],
    ["RHO", "Stuttgart (DE)", "voll konform", "—"],
]

gov_quartal("REA_Konzern_Governance_Report_2020_Q1.docx", "2020", "Q1",
            ["COVID-19-Pandemie: Krisenstab eingerichtet, Werke fahren auf Notbetrieb",
             "Kurzarbeit in den Werken Heilbronn und Gyoer beantragt",
             "Quartalsabschluss verzoegert sich um 5 Werktage, Pruefer informiert",
             "Compliance-Schulungen ins E-Learning verlagert"],
            TOCHTER_STATUS,
            "Q2 bleibt herausfordernd; Liquiditaetsplanung fuer 6 Monate Stress-Szenario erstellt. "
            "Konsortialbanken sind informiert, Covenants weiterhin eingehalten.",
            "Mehrere ad-hoc Sachverhalte zu COVID-19 wurden in Vorstandssitzungen ausserhalb der "
            "Turnus-Sitzungen behandelt (Dokumentation in Vorstandsprotokollen).")
gov_quartal("REA_Konzern_Governance_Report_2020_Q2.docx", "2020", "Q2",
            ["Kurzarbeit teilweise zurueckgefuehrt; Werk Heilbronn ab Juni wieder Vollbetrieb",
             "Halbleiter-Versorgungsengpaesse zeichnen sich ab, Beschaffungsstrategie verlaengert",
             "Cyber-Sicherheitsuebung am Standort Stuttgart erfolgreich durchgefuehrt",
             "Whistleblowing-Hotline mit erweiterten Sprachen (PL, CZ, HU, CN) live geschaltet"],
            TOCHTER_STATUS,
            "H2/2020 ist von Halbleiter-Engpaessen und volatiler OEM-Nachfrage gepraegt. "
            "Treasury hat Stress-Szenarien fuer Q3+Q4 vorbereitet.",
            "Keine ad-hoc-meldungspflichtigen Sachverhalte (vorboerslich).")
gov_quartal("REA_Konzern_Governance_Report_2020_Q3.docx", "2020", "Q3",
            ["Halbleiter-Verfuegbarkeit weiterhin angespannt, Allokationsmanagement im Vertrieb",
             "RPL Katowice: lokale Lock-Down-Massnahmen kurzfristig, Werk lief weiter",
             "Audit-Programm 2020 wegen Reiseeinschraenkungen teilweise auf 2021 verschoben",
             "ESG-Initiative gestartet: Klimastrategie 2030 in Vorbereitung"],
            TOCHTER_STATUS,
            "Q4 fokussiert auf Jahresabschluss-Vorbereitung und Halbleiter-Beschaffung. "
            "Lieferanten-Performance-Reviews intensiviert.")
gov_quartal("REA_Konzern_Governance_Report_2020_Q4.docx", "2020", "Q4",
            ["Geschaeftsjahr 2020 trotz Pandemie mit leicht positivem Ergebnis abgeschlossen",
             "Konzernabschluss 2020 testiert (KPMG, uneingeschraenktes Pruefungsurteil)",
             "Vorbereitung IPO-Prozess begonnen (Auswahl Joint Bookrunners)",
             "ESG-Strategie 2030 verabschiedet (Vorstand und Aufsichtsrat)",
             "Compliance-Audit Werk Gyoer im November ohne wesentliche Findings"],
            TOCHTER_STATUS,
            "2021 mit Schwerpunkten IPO-Vorbereitung, Halbleiter-Stabilisierung, Klimastrategie-Umsetzung. "
            "Konsortialkredit-Refinanzierung wird gegen Jahresende vorbereitet.")
gov_quartal("REA_Konzern_Governance_Report_2021_Q2.docx", "2021", "Q2",
            ["IPO-Vorbereitung gestartet: Mandatierung Goldman Sachs, Deutsche Bank, Berenberg, Commerzbank",
             "Halbleiter-Engpass beeinflusst Q2-Liefermengen bei Mercedes und VW",
             "DSGVO-Audit Werk Katowice ohne wesentliche Findings",
             "ISO 27001 Vorbereitungsprojekt gestartet"],
            TOCHTER_STATUS,
            "H2/2021 fokussiert auf IPO-Roadmap, Halbleiter-Allokation, Vorbereitung CSRD.",
            "Keine ad-hoc-meldungspflichtigen Sachverhalte (vorboerslich).")
gov_quartal("REA_Konzern_Governance_Report_2021_Q3.docx", "2021", "Q3",
            ["IPO-Prospektentwurf abgeschlossen, BaFin-Vorlage in Q4 geplant",
             "Halbleiter-Versorgung leicht entspannt, weiterhin sorgfaeltige Allokation",
             "Whistleblowing-Hotline: 9 Hinweise im Quartal, alle adressiert, keine substanzielle Verstoesse",
             "RCN Shanghai: lokale Compliance-Auflagen verschaerft, Werks-Compliance-Programm angepasst"],
            TOCHTER_STATUS,
            "Q4 ist gepraegt durch finale IPO-Vorbereitung und Vorbereitung der Konsortialkredit-Refinanzierung "
            "(Closing 14.3.2022).")
gov_quartal("REA_Konzern_Governance_Report_2021_Q4.docx", "2021", "Q4",
            ["Konzernabschluss 2021 testiert (KPMG, uneingeschraenktes Pruefungsurteil)",
             "Konsortialkredit-Vertrag 14.3.2022 unterzeichnet (250 Mio. EUR, 5 Banken)",
             "Insider-Verzeichnis im Zuge der IPO-Vorbereitung etabliert",
             "Compliance-Schulungen 2021 abgeschlossen, Abdeckungsquote 97 %",
             "Werks-Audit RPL Katowice: drei mittlere Findings (alle binnen Q1/2022 behoben)"],
            TOCHTER_STATUS,
            "2022 steht im Zeichen der IPO-Vorbereitung (Closing geplant Oktober 2022) sowie "
            "der Aktivierung der Sustainability-linked Loan-Bedingungen.")
gov_quartal("REA_Konzern_Governance_Report_2022_Q2.docx", "2022", "Q2",
            ["IPO-Prospekt von BaFin gebilligt, Roadshow-Vorbereitung intensiviert",
             "Erweiterung Insider-Verzeichnis, MAR-Schulungen aller PDMR abgeschlossen",
             "Halbleiter-Engpaesse halten an, jedoch Lieferperformance gesichert",
             "Bank-Audits durch Konsortialbanken im Mai erfolgreich",
             "Cyber-Vorfall (Phishing-Welle) bei RHU Gyoer ohne Datenabfluss behoben"],
            TOCHTER_STATUS,
            "Q3/Q4 mit IPO-Closing 14.10.2022, danach Vorbereitung auf erste Quartalsmitteilung als boersennotiertes Unternehmen.",
            "Mehrere kapitalmarktrechtliche Vorbereitungsschritte (Closed-Period-Regelungen, Ad-hoc-Prozesse) "
            "wurden eingefuehrt.")
gov_quartal("REA_Konzern_Governance_Report_2022_Q3_reviewed.docx", "2022", "Q3",
            ["IPO-Roadshow abgeschlossen, Pricing am 13.10.2022, Closing 14.10.2022",
             "Ad-hoc-Prozesse erstmals genutzt (IPO-Erloesmeldung)",
             "Erste Quartalsmitteilung Q3 als boersennotiertes Unternehmen plangemaess",
             "Pruefungsausschuss-Vorsitz: Prof. Voss bestaetigt KPMG-Mandat"],
            TOCHTER_STATUS,
            "Q4/2022 mit Schwerpunkt auf erstem Geschaeftsbericht als boersennotiertes Unternehmen, "
            "ESG-Reporting CSRD-Vorbereitung.")
gov_quartal("REA_Konzern_Governance_Report_2022_Q4.docx", "2022", "Q4",
            ["Erster Geschaeftsbericht als boersennotiertes Unternehmen 2022 in Vorbereitung",
             "Aufsichtsrats-Pruefungsausschuss tagte am 14.12.2022 (Halbjahres-IFRS-Vorlage)",
             "Sustainability-linked Loan-Bedingungen 2022 erstmals erfuellt (Margin-Adjust +5bp)",
             "Konzern-Cyber-Vorfall (Phishing) bei RPL ohne kritischen Datenabfluss"],
            TOCHTER_STATUS,
            "2023 mit Schwerpunkten auf CSRD-Vorbereitung, ESG-Doppel-Wesentlichkeit, Werks-Audit-Programm.")
gov_quartal("REA_Konzern_Governance_Report_2023_Q1.docx", "2023", "Q1",
            ["Q1-Mitteilung 2023 plangemaess veroeffentlicht (Ad-hoc-Prozess ohne Besonderheiten)",
             "Hauptversammlung 2023 vom 26.5. vorbereitet (Tagesordnung beschlossen)",
             "Compliance-Audit Werk Brno ohne wesentliche Findings",
             "PDMR-Verzeichnis aktualisiert (Hollmann, Tanaka, Richter)"],
            TOCHTER_STATUS,
            "Q2 mit Hauptversammlung 2023 und Vorbereitung Aufsichtsrats-Sitzungen H2.")
gov_quartal("REA_Konzern_Governance_Report_2023_Q2.docx", "2023", "Q2",
            ["Hauptversammlung 2023 erfolgreich (Beschluesse zu Dividende und Entlastung)",
             "Vorstandsbestellungen Hollmann (CTO ab 1.7.2024) und Tanaka (CRO Asia ab 1.4.2024) durch AR beschlossen",
             "Werks-Audits Heilbronn / Katowice im Plan ohne wesentliche Findings",
             "ESG-Doppel-Wesentlichkeitsanalyse durchgefuehrt (Stakeholder-Workshops)"],
            TOCHTER_STATUS,
            "H2 mit Schwerpunkten auf Q3-Mitteilung, CSRD-Reporting Pilot, Konsortialkredit-Audit.")
gov_quartal("REA_Konzern_Governance_Report_2023_Q3.docx", "2023", "Q3",
            ["Q3-Mitteilung plangemaess veroeffentlicht",
             "Cyber-Sicherheitsuebung konzernweit erfolgreich",
             "Vorbereitung HV 2024 begonnen (Termin 24.5.2024)",
             "LkSG-Compliance: Risikoanalyse aller Tier-1-Lieferanten abgeschlossen"],
            TOCHTER_STATUS,
            "Q4 mit Schwerpunkten Jahresabschluss-Vorbereitung, ESG-Reporting CSRD-Pilot, "
            "Konsortialbanken-Jahresgespraeche.")
gov_quartal("REA_Konzern_Governance_Report_2023_Q4.docx", "2023", "Q4",
            ["Konzernabschluss 2023 in Vorbereitung (Pruefung durch KPMG laeuft)",
             "Werks-Audit Gyoer im November abgeschlossen ohne wesentliche Findings",
             "Compliance-Schulungen 2023 zu 96 % abgeschlossen",
             "Vorbereitung Vorstandswechsel Hoffmann → Hollmann (CTO) zum 1.7.2024 angelaufen"],
            TOCHTER_STATUS,
            "2024 fokussiert auf CSRD-Vollumsetzung, Vorstandstransition, Konsortialkredit-Refinanzierung "
            "(Faelligkeit 14.3.2027 vorbereiten).")


# ===== 2 Konzernlageberichte =====
konzernlagebericht("REA_Konzernlagebericht_2021.docx", "2021", 580, 42, 70, 3820, "1,40",
                   ["IPO-Vorbereitung intensiviert (Joint Bookrunner Mandat erteilt)",
                    "Konsortialkredit-Vorbereitung mit 5 Banken",
                    "Halbleiter-Engpass-Management und Allokationssteuerung",
                    "ESG-Klimastrategie 2030 finalisiert und durch Aufsichtsrat genehmigt",
                    "Werksinvestitionen Heilbronn und Katowice (PV-Anlagen Vorplanung)"],
                   "Fuer 2022 erwartet der Vorstand einen leichten Umsatz- und Ergebnisanstieg sowie den "
                   "erfolgreichen Boersengang im H2/2022. Wesentliche Risiken: Halbleiter-Verfuegbarkeit, "
                   "Kapitalmarktvolatilitaet, geopolitische Spannungen.")
konzernlagebericht("REA_Konzernlagebericht_2023.docx", "2023", 612, 48.9, 74.3, 4180, "2,10 (geplant)",
                   ["Erster vollstaendiger Geschaeftsbericht als boersennotiertes Unternehmen",
                    "BMS-12-Anlauf VW ID.7 erfolgreich, hohe Nachfrage in H2/2023",
                    "ADAS-V4D Designwins bei Mercedes und Stellantis",
                    "Werkserweiterungen Heilbronn (Linie 4 BMS-12) und Katowice (SMD)",
                    "ESG: Scope 1+2 -15 % ggue. 2019 (Sustainability-linked Loan Trigger erfuellt)"],
                   "Fuer 2024 erwartet der Vorstand einen Umsatzanstieg auf 640–660 Mio. EUR und ein EBIT "
                   "in der Spanne 50–52 Mio. EUR. CSRD-Berichtspflicht wird vollumfaenglich erfuellt. "
                   "Vorstandstransition (CTO Hollmann ab 1.7.2024) ist im Plan.")


# ===== 3 Nichtfinanzielle Berichte =====
nichtfin_bericht("REA_Nichtfinanzieller_Bericht_2021.docx", "2021",
                 [["KPI", "2021"],
                  ["Scope 1+2 Emissionen (t CO2e)", "—"],
                  ["Anteil erneuerbare Energien", "—"],
                  ["LTIFR", "—"],
                  ["Mitarbeiterfluktuation %", "—"],
                  ["Frauenanteil Fuehrung %", "—"],
                  ["Schulungstage pro MA", "—"]],
                 ["Klimastrategie 2030 in Umsetzung mit Fokus auf Energieeffizienz",
                  "Erste PV-Vorplanung Werk Heilbronn",
                  "ISO 14001 / ISO 50001 Re-Zertifizierung erfolgreich",
                  "Aufbau ESG-Reporting im Hinblick auf CSRD"])
nichtfin_bericht("REA_Nichtfinanzieller_Bericht_2022_2024-03-01.docx", "2022",
                 [["KPI", "2022"],
                  ["Scope 1+2 Emissionen (t CO2e)", "—"],
                  ["Anteil erneuerbare Energien", "—"],
                  ["LTIFR", "—"],
                  ["Mitarbeiterfluktuation %", "—"],
                  ["Frauenanteil Fuehrung %", "—"],
                  ["Schulungstage pro MA", "—"]],
                 ["Klimaziel-Validierung durch SBTi gestartet",
                  "Sustainability-linked Loan-Bedingungen 2022 erstmals erfuellt",
                  "LkSG-Vorbereitungsprojekt fuer Stichtag 1.1.2023 abgeschlossen",
                  "ESG-Doppel-Wesentlichkeitsanalyse begonnen"])
nichtfin_bericht("REA_Nichtfinanzieller_Bericht_2023.docx", "2023",
                 [["KPI", "2023"],
                  ["Scope 1+2 Emissionen (t CO2e)", "—"],
                  ["Anteil erneuerbare Energien", "—"],
                  ["LTIFR", "—"],
                  ["Mitarbeiterfluktuation %", "—"],
                  ["Frauenanteil Fuehrung %", "—"],
                  ["Schulungstage pro MA", "—"]],
                 ["Scope 1+2 -15 % gegenueber Basisjahr 2019",
                  "Frauenanteil Fuehrung steigt auf 27 %, Ziel 30 % bis 2026",
                  "LkSG-Compliance erstmals vollumfaenglich umgesetzt",
                  "CSRD-Pilot erfolgreich, Vollumsetzung fuer 2024 vorbereitet"])


# ===== 4 Vollmachten =====
vollmacht("REA_Vollmacht_Dr._Petra_Hollmann_2023.docx",
          "Dr. Petra Hollmann", "CTO-Designate / Vorstandsmitglied ab 1.7.2024",
          "Forschung und Entwicklung / Technologie", "1. Oktober 2023")
vollmacht("REA_Vollmacht_Dr._Yuki_Tanaka_2023.docx",
          "Dr. Yuki Tanaka", "CRO Asia / Vorstand International ab 1.4.2024",
          "Asien-Geschaeft und internationale Vertriebsorganisation (RCN Shanghai)",
          "1. November 2023")
vollmacht("REA_Vollmacht_Klaus-Peter_Zimmermann_2023.docx",
          "Klaus-Peter Zimmermann", "Generalbevollmaechtigter / Leiter Group Controlling-Programme",
          "Konzern-Controlling und Programm-Office", "15. September 2023")
vollmacht("REA_Vollmacht_Stefan_Richter_2023.docx",
          "Stefan Richter", "CMO / BD (Vorstand ab 1.4.2023)",
          "Vertrieb / Business Development / OEM-Key-Accounts", "1. April 2023")


# ===== 2 Articles of Association (RCN, RFI) =====
articles_of_association("RCN_Articles_of_Association_2023.docx",
    "Brennhagen (Shanghai) Co. Ltd. (RCN)", "Shanghai", "People's Republic of China",
    "Wholly Foreign-Owned Enterprise (WFOE) / Limited Liability Company",
    "Unified Social Credit Code 913100007891234567 (Shanghai AMR Registry)",
    "Registered capital: USD 4,000,000 (paid-in). Sole shareholder: Brennhagen Holding GmbH (RHO), Stuttgart. "
    "Capital is registered in USD; functional reporting currency is CNY. Capital increases require resolution of "
    "the sole shareholder and approval by Shanghai AMR / SAFE registration.",
    "The object of the company is the sales, after-sales service, technical support and aftermarket distribution "
    "of automotive electronics components (in particular infotainment, battery management, ADAS, powertrain and "
    "matrix-LED modules) within the People's Republic of China and the Asia-Pacific region; the import and export "
    "activities related thereto; the engagement of local engineering, training and customer-support personnel; "
    "and any other activities permitted under Chinese law and within the company's approved business scope.",
    "Corporate bodies: (i) the sole shareholder (Brennhagen Holding GmbH); (ii) the Executive Director / "
    "Legal Representative (currently the Country Manager Zhang Hao); (iii) the Supervisor (appointed by the sole "
    "shareholder). The company has no Board of Directors. The Executive Director represents the company externally "
    "subject to limits set in the shareholder resolutions and the group's internal authorization matrix.")
articles_of_association("RFI_Articles_of_Association_2023.docx",
    "Brennhagen Finance Ireland DAC (RFI)", "Dublin", "Ireland",
    "Designated Activity Company (DAC) limited by shares",
    "Companies Registration Office (CRO) Dublin, registration no. 654321 (mock)",
    "Authorised share capital: EUR 100,000 divided into 100,000 ordinary shares of EUR 1.00 each. "
    "Issued and fully paid share capital: EUR 25,000 (25,000 ordinary shares). Sole shareholder of record: "
    "Brennhagen Holding GmbH, Stuttgart, Germany. Any transfer of shares requires prior approval of the board "
    "and the sole shareholder.",
    "The object of the company is to act as a group treasury and finance vehicle of the Brennhagen group: in "
    "particular to raise debt instruments (private placements, schuldscheine, intercompany loans), to provide "
    "funding to other Brennhagen group companies on arm's-length terms, to perform group FX and interest-rate hedging "
    "activities, and to engage in any other activities permitted to a designated activity company under the "
    "Companies Act 2014 of Ireland.",
    "Corporate bodies: (i) the sole shareholder (Brennhagen Holding GmbH); (ii) the Board of Directors comprising "
    "at least two directors (at least one resident in the EEA in accordance with the Companies Act 2014); "
    "(iii) the Company Secretary. The Board manages the company within the parameters set by the group treasury "
    "policy (Konzernrichtlinie Treasury 2023) and any board resolutions of the sole shareholder.")


# ===== 1 Verrechnungspreisdokumentation (Masterdatei) =====
verrechnungspreis_masterdatei("REA_Verrechnungspreisdokumentation_Masterdatei_2023.docx", "2023")


# ===== 1 IC Quartalsbericht (RHU 2019 Q2) =====
ic_quartalsbericht("RHU_IC_Quartalsbericht_2019_Q2.docx", "RHU", "2019", "Q2",
                   ["Linienauslastung am Standort Gyoer im Plan",
                    "Sensorik-Anlauf BMW-Programm neue Variante erfolgreich",
                    "Lokale BR-Wahl im April 2019 ohne Beanstandungen abgeschlossen",
                    "Audit der ungarischen Steuerbehoerde (NAV) eroeffnet, voraussichtliche Dauer 12 Monate",
                    "Personalbestand erhoeht (Aufbau Linie ADAS-Sensorik); 24 Neueinstellungen im Quartal",
                    "Energie- und Umweltkennzahlen im Plan, ISO 50001 Audit im Sept. 2019 vorbereitet"])


# ===== 1 IC Rechnung (RSG 07/2020) =====
ic_rechnung("RSG_IC_Rechnung_2020_07.docx", "RSG", "Brennhagen Elektronik GmbH (REG), Heilbronn",
            "2020", "07", 184_730.00,
            "Embedded-Software-Entwicklungsleistungen Juli 2020 fuer das Produktprogramm ICP-3 / ECU-900: "
            "Firmware-Pflege, Variantenmanagement, OTA-Plattform-Support, Code-Reviews und Test-Automatisierungs-"
            "Skripte; Gesamtaufwand 1.420 Stunden zu 130 EUR/h (inkl. Cost+ 5 %). Detailaufstellung gemaess "
            "Service-Spezifikation Anhang 1 zum Intercompany-Dienstleistungsvertrag RSG-REG 2020.",
            "RSG-IC-2020-07-0142")


# ===== 1 VW QBR ADAS-V4D Q3/2022 =====
vw_qbr("REA_VW_ADAS-V4D_QBR_2022_Q3_FINAL.docx", "ADAS-V4D", "2022", "Q3",
       ["Programm-Plan Q3 erreicht, Liefermengen im Forecast",
        "Software-Reifegrad ASPICE Level 2 fuer Release 3.4 nachgewiesen",
        "Cybersecurity-Konzept gem. ISO/SAE 21434 wurde mit VW abgestimmt",
        "Validierungsplan ASIL-B Komponenten in Abstimmung mit VW QM",
        "Eskalation: Lieferanten-Engpass Radar-MMIC (Infineon) – Mitigationsplan beschlossen"],
       [["Termintreue Lieferung", ">= 95 %", "97 %", "gruen"],
        ["PPM-Quote", "< 20 ppm", "12 ppm", "gruen"],
        ["8D-Schliesszeit", "< 60 Tage", "47 Tage", "gruen"],
        ["Forecast-Genauigkeit", ">= 90 %", "92 %", "gruen"]])


# ===== 1 MSA Studie =====
msa_studie("MSA_Messunsicherheitsstudie_2023_008.docx",
           "BMS-12 Hochspannungs-Pruefadapter (HV-Adapter Werk Heilbronn)",
           "Keithley DMM 7510 mit Pruefadapter HV-Tester REG Linie 4",
           "12. Oktober 2023")


# ===== 1 Patent-Antwort =====
patent_antwort("Patent_11_Antwort_Anmelder_2023.docx", "DE 10 2022 015 432.1", "15. Juni 2023",
               "Verfahren und Vorrichtung zur sensorischen Multi-Domain-Fusion fuer Level-2/3-ADAS-Systeme "
               "mit adaptiver Latenzkompensation. Die Erfindung betrifft insbesondere die Kombination von "
               "Radar-, Lidar- und Kameradaten in einer einheitlichen Fusionsschicht, in der die Latenzunterschiede "
               "der einzelnen Sensorpfade adaptiv kompensiert werden, sodass die fusionierte Umfeldwahrnehmung "
               "in allen Verkehrssituationen mit definierter Worst-Case-Latenz erfolgt.")


# ===== 1 Gate-Review =====
gate_review("PRJ-2024-001_Gate_G4_Validierung_ECU-1000_Concept_Study.docx",
            "PRJ-2024-001", "G4 (Validation Gate)", "ECU-1000 (Concept Study)", "20. Maerz 2024",
            ["Requirements Engineering: Customer requirements zu 92 % abgenommen (Ziel 95 %)",
             "Architektur: HW/SW-Architektur freigegeben, ASIL-Konzept finalisiert",
             "Validierungsplan: Pruefumfang definiert, Pruefmittel in Beschaffung",
             "Risiko-Register: 6 offene rote Risiken, davon 4 mit Mitigationsplan",
             "Budget/Termin: Budget 5 % unter Plan, Termin 4 Wochen verzoegert",
             "Beschaffung: A-Komponenten qualifiziert, B-Komponenten in Bemusterung"])


# ===== 1 Testbericht =====
testbericht("PRJ-2024-002_Testbericht_Funktionstest_EOL_DSGVO_Compliance_Rem.docx",
            "PRJ-2024-002", "Funktionstest EOL (End-of-Line)",
            "DSGVO-Compliance-Telematik-Modul Remanenz-Test (Datenloeschung)",
            "12. April 2024",
            "Pruefling wurde nach DSGVO-konformer Datenloeschung (kryptographischer Erase) "
            "auf Restdatenfreiheit geprueft. Es wurden 50 Pruefmuster getestet. "
            "Ergebnis: 50/50 Muster (100 %) zeigten keine Restdaten in den persistenten Speichern. "
            "Die Pruefung erfolgte mittels forensischer Speicheranalyse (Tool: X-Ways Forensics, "
            "Pruefspezifikation gem. internem Doc »EOL-DSGVO-Test-Spec-Rev3«). Pruefdauer pro Pruefling "
            "ca. 14 Minuten. Keine Auffaelligkeiten festgestellt. Empfehlung: Aufnahme dieses Pruefschritts "
            "in die Serienfertigung EOL-Station REG Linie 2 verpflichtend ab Produktionsversion R3.")


# ─────────────────────────────────────────────────────────────────────────────
# B01 — REMNANTS
# ─────────────────────────────────────────────────────────────────────────────

# 3 Directors' Dealings
directors_dealings("REA_Directors_Dealings_Dr._Petra_Hollmann_2023.docx",
    "Dr. Petra Hollmann", "Vorstandsmitglied (CTO-Designate, Vorstand ab 1.7.2024)",
    "Erwerb von 2.500 Stammaktien der Brennhagen Elektronik AG (ISIN DE000RHGRP12) am 14. Oktober 2023 "
    "zum Durchschnittskurs von 27,80 EUR ueber XETRA. Gesamtvolumen 69.500 EUR. Transaktion erfolgte "
    "auf eigene Rechnung und nicht im Auftrag oder fuer Dritte. Im laufenden Kalenderjahr 2023 wurden "
    "durch die meldepflichtige Person keine weiteren PDMR-relevanten Geschaefte vorgenommen. Die "
    "Schwelle nach Art. 19 Abs. 8 MAR (5.000 EUR p. a.) wurde mit dieser Einzeltransaktion ueberschritten.")
directors_dealings("REA_Directors_Dealings_Dr._Yuki_Tanaka_2023.docx",
    "Dr. Yuki Tanaka", "Vorstandsmitglied (CRO Asia / International, Vorstand ab 1.4.2024)",
    "Erwerb von 1.800 Stammaktien der Brennhagen Elektronik AG (ISIN DE000RHGRP12) am 8. November 2023 "
    "zum Durchschnittskurs von 28,15 EUR ueber XETRA. Gesamtvolumen 50.670 EUR. Die Transaktion erfolgte "
    "auf eigene Rechnung im Rahmen des im Vorstandsanstellungsvertrag vereinbarten Mindestbeteiligungs-"
    "programms (»executive ownership policy«, Zielbeteiligung 1x Jahresgrundgehalt binnen 5 Jahren). "
    "Im laufenden Kalenderjahr keine weiteren PDMR-relevanten Geschaefte.")
directors_dealings("REA_Directors_Dealings_Stefan_Richter_2023.docx",
    "Stefan Richter", "Vorstandsmitglied (CMO / BD seit 1.4.2023)",
    "Erwerb von 1.200 Stammaktien der Brennhagen Elektronik AG (ISIN DE000RHGRP12) am 18. Mai 2023 "
    "zum Durchschnittskurs von 26,40 EUR ueber XETRA. Gesamtvolumen 31.680 EUR. Sowie weiterer "
    "Erwerb von 800 Stammaktien am 22. September 2023 zum Durchschnittskurs von 27,10 EUR "
    "(Volumen 21.680 EUR). Beide Transaktionen erfolgten auf eigene Rechnung im Rahmen der "
    "Mindestbeteiligungspolicy. Kumuliertes Volumen 2023: 53.360 EUR (oberhalb der 5.000-EUR-Schwelle).")


# 1 Lessons Learned
lessons_learned("PRJ-2024-001_Lessons_Learned_ECU-1000_Concept_Study.docx",
                "PRJ-2024-001", "ECU-1000 (Concept Study)",
                ["Stakeholder-Mapping zu Projektbeginn detailliert; klare RACI-Matrix gefuehrt",
                 "Risiken-Register taeglich gepflegt; Trends sichtbar (Burn-down)",
                 "Modulare Architektur ermoeglichte parallele Entwicklung HW / SW",
                 "Frueh angesetzte OEM-Reviews mit Mercedes / VW",
                 "Solides Budget-Controlling, transparente Forecast-Pflege durch das PMO"])


# 1 VW QBR ECU-900 Q4/2022
vw_qbr_b01("REA_VW_ECU-900_QBR_2022_Q4.docx", "ECU-900", "2022", "Q4",
       ["Liefermengen Q4 im Plan, leichter Forecast-Anstieg fuer Q1/2023",
        "Reklamationsstatus: 1 OEM-Reklamation im Quartal, 8D-Report binnen 28 Tagen geschlossen",
        "ASPICE Level 2 Bestaetigungs-Audit bei RSG erfolgreich",
        "Roadmap Software-Updates 2023 vereinbart (4 geplante Releases)",
        "ESG-Anforderungen: CO2-Footprint je ECU wurde an VW gemeldet (gem. VW-Anfrage)"],
       [["Termintreue Lieferung", ">= 95 %", "98 %", "gruen"],
        ["PPM-Quote", "< 25 ppm", "14 ppm", "gruen"],
        ["8D-Schliesszeit", "< 60 Tage", "28 Tage", "gruen"],
        ["Forecast-Genauigkeit", ">= 90 %", "94 %", "gruen"]])


# 1 EMV-Testbericht (B01)
testbericht_b01("PRJ-2022-002_Testbericht_EMV_Test_InfoConnect_Pro_4.0.docx",
                "PRJ-2022-002", "EMV-Test", "InfoConnect Pro 4.0 (ICP-3 Generation 4)",
                "18. Oktober 2022",
                "Pruefling ICP-3 Gen4 (Hardware-Rev B, Firmware-Stand 1.2.7) wurde im akkreditierten "
                "EMV-Labor Werk Heilbronn (akkreditiert nach DIN EN ISO/IEC 17025) geprueft. "
                "Pruefumfang: Bulk-Current-Injection (BCI 1 MHz–400 MHz, 100 mA/200 mA), Antennenmessung "
                "in der Reverberation-Chamber bis 6 GHz, Trapeztest gem. ISO 7637-2 (Pulse 1–7), "
                "ESD-Pruefung mit 8 kV Kontakt-/15 kV Luftentladung gem. ISO 10605. "
                "Ergebnis: Pruefling erfuellt alle spezifizierten EMV-Anforderungen in den getesteten "
                "Betriebsmodi 1 (Normalbetrieb mit Bluetooth-Audio-Stream) und 2 (Standby). "
                "Keine Performance-Degradation, keine Reset-Faelle, keine Funkstoraussendung oberhalb "
                "der Grenzlinien. Klasse A nach OEM-Spec (BMW GS 95002-2).")


# 1 Arbeitsvertrag (RPL)
arbeitsvertrag_b01("RPL_Arbeitsvertrag_03_Qualitätsmanagerin_K_2022.docx",
                   "Frau Katarzyna K. (vollstaendiger Name siehe Personalakte)",
                   "Qualitaetsmanagerin Linie SMD-3", "RPL", "2022", "62.400",
                   "1. Maerz 2022")


print("Done writing all enrichments.")
