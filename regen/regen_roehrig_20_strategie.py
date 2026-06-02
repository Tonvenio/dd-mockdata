"""Brennhagen AG / 20_Strategie_Vorstand (54 thin)."""
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

B = f"{_ROOT}/roehrig_large/20_Strategie_Vorstand"
H = {"name": R["name"], "addr": R["addr"], "hrb": R["hrb"]}


# ─────────────────────────────────────────────────────────────────────────────
# HELPER — Strategie-Deck / Strategiepapier
# ─────────────────────────────────────────────────────────────────────────────
def strategie_deck(fname, jahr, kurztitel, leitmotiv, saeulen, kpi_rows,
                   marktkontext, risiken, beschluss_datum, draft=False):
    write_doc(f"{B}/{fname}", H,
        f"Strategiepapier {jahr} – Brennhagen Elektronik AG",
        subtitle=f"»{kurztitel}« – Konzernstrategie {jahr}; Vorlage Vorstand / Aufsichtsrat",
        confidential=True, draft=draft,
        sections=[
            ("Management Summary",
             f"Das vorliegende Strategiepapier {jahr} beschreibt den strategischen Kompass der "
             f"Brennhagen Elektronik AG (»REA«) und ihrer Konzerngesellschaften unter dem Leitmotiv "
             f"»{leitmotiv}«. Es loest die Vorgaengerfassung des Strategiepapiers ab und wurde durch "
             f"den Vorstand in der Sitzung vom {beschluss_datum} beschlossen sowie dem Aufsichtsrat "
             f"in der darauffolgenden Sitzung vorgelegt. Verantwortlich fuer Erstellung und Pflege ist "
             f"das Vorstandsbuero (Dr. Veronika Steiner) in Abstimmung mit dem Strategieausschuss "
             f"unter CFO Laura Bauer.\n\n"
             f"Der Brennhagen-Konzern positioniert sich als europaeischer Tier-1-Spezialist fuer "
             f"automotive Elektronik mit den Schwerpunkten Batteriemanagement (BMS), ADAS Level 2–3 "
             f"und Software-defined Vehicle. Die Strategie {jahr} setzt einen klaren Wachstumspfad "
             f"mit einem Umsatzziel von 1,0 Mrd. EUR fuer das Jahr 2028 (CAGR 13 %) sowie einer "
             f"strukturellen EBITDA-Marge ueber 14 %. Sie ist mit der Mittelfristplanung (MFP) und "
             f"dem Capital Allocation Framework verzahnt."),
            ("Marktkontext und Ausgangslage", marktkontext),
            ("Strategische Saeulen", ("list", saeulen)),
            ("Finanzielle Eckwerte (Mittelfristplan, Mio. EUR)", kpi_rows),
            ("Strategische Initiativen / Roadmap",
             ("list", [
                 "Initiative 1 – BMS-12 Plattform-Expansion: Skalierung der Produktion in Heilbronn auf 4,5 Mio. Module p.a. bis 2026, neue SOP fuer BMS-12.2 (800 V) Q2/2025.",
                 "Initiative 2 – ADAS-V4D Radar Fusion Generation 2: gemeinsame Entwicklung mit Mercedes-Benz und Stellantis, SOP Q4/2026.",
                 "Initiative 3 – Software-as-a-Service Plattform: »BrennhagenOS« Subscription-Modell fuer OTA-Updates, ARR-Ziel 35 Mio. EUR bis 2028.",
                 "Initiative 4 – Nearshoring Marokko: Pruefung Produktionsstandort Tanger Free Zone (Decision Gate Q4/2024).",
                 "Initiative 5 – China-Lokalisierung: Ausbau Shanghai-Vertrieb, Joint-Venture-Pruefung mit CATL fuer lokale BMS-Fertigung.",
                 "Initiative 6 – ESG / CSRD Compliance: Aufbau Reporting-Infrastruktur fuer Berichtspflicht ab GJ 2024, Heubeck-Aktuarberater integriert.",
             ])),
            ("Risikoportfolio und Gegenmassnahmen", ("list", risiken)),
            ("Governance und Steuerung",
             "Die Strategieumsetzung wird ueber den monatlichen Vorstands-Strategie-Jour-Fixe (jeweils "
             "1. Donnerstag) gesteuert. Quartalsberichterstattung an den Aufsichtsrat erfolgt durch die "
             "CEO. Strategische Initiativen werden im Stage-Gate-Verfahren gefuehrt (G0 bis G4); jede "
             "Initiative hat einen verantwortlichen Vorstand (Single Point of Accountability). "
             "KPI-Reporting laeuft ueber das Group Performance Management System (GPMS) mit Anbindung "
             "an SAP S/4HANA."),
            ("Freigabe / Beschluss",
             signatures("Anna Mueller", "Vorstandsvorsitzende", R["name"],
                        "Laura Bauer", "CFO", R["name"],
                        place="Stuttgart", date_str_=beschluss_datum)),
        ])


# ─────────────────────────────────────────────────────────────────────────────
# HELPER — Vorstandspraesentation Quartal
# ─────────────────────────────────────────────────────────────────────────────
def vorstand_quartal(fname, jahr, quartal, schwerpunkte, kpi_table, beschluesse,
                     sitzungsdatum):
    write_doc(f"{B}/{fname}", H,
        f"Vorstandspraesentation {jahr} / {quartal}",
        subtitle=f"Quartalsbericht Vorstand an Aufsichtsrat – {quartal}/{jahr}",
        confidential=True,
        sections=[
            ("Sitzungsangaben",
             f"Vorstandssitzung am {sitzungsdatum}, 8:30–13:00 Uhr, Vaihinger Strasse 120, "
             f"70567 Stuttgart, Raum »Stuttgart« (8. OG). Vorsitz: CEO Anna Mueller. Anwesend: "
             f"Laura Bauer (CFO), Dr. Thomas Weber (COO), Stefan Hoffmann (CTO) sowie ab "
             f"Q2/2023 Stefan Richter (CMO/BD). Schriftfuehrerin: Dr. Veronika Steiner "
             f"(Vorstandsbuero). Ausgewaehlte Tagesordnungspunkte wurden in Anwesenheit "
             f"des KPMG-Lead-Partners Dr. Maximilian Brand behandelt."),
            ("Wesentliche Themen / Schwerpunkte", ("list", schwerpunkte)),
            ("Finanzkennzahlen Konzern (IFRS, Mio. EUR)", kpi_table),
            ("Operative Lage",
             f"Die operative Lage des Konzerns ist im Berichtsquartal stabil. Die Werke in Heilbronn "
             f"(REG), Katowice (RPL), Brno (RCZ) und Gyoer (RHU) laufen im geplanten Auslastungskorridor "
             f"(82–94 %). Werk Heilbronn meldet einen Anstieg der OEE auf 86 % (Vorquartal 83 %). "
             f"Das RSG-Team in Muenchen liegt bei der ASPICE-Level-3-Zertifizierung im Plan "
             f"(geplantes Audit Q4). Das Asien-Geschaeft (RCN Shanghai) zeigt nach wie vor "
             f"Verzoegerungen bei lokalen Tier-2-Lieferanten infolge der Halbleiter-Allokation."),
            ("Beschluesse / Action Items", ("list", beschluesse)),
            ("Risiken und Compliance",
             "Wesentliche Risiken: (a) Halbleiter-Allokation NXP/Infineon bis Mitte des Folgejahres; "
             "(b) FX-Exposure PLN/CZK/HUF teilweise gehedged (siehe FX-Hedge-Quartalsbericht); "
             "(c) regulatorische Vorgaben UNECE R155/R156 (Cybersecurity) und ISO 21434 in Umsetzung; "
             "(d) CSRD-Vorbereitung GJ 2024. Compliance: Keine wesentlichen Vorfaelle im Quartal."),
            ("Naechste Schritte",
             "Naechste Vorstandssitzung gemaess Jahresplan; Folgevorlage an den Aufsichtsrat erfolgt "
             "fristgerecht. Strategiepapier-Revision wird im Q3 im Strategieausschuss aufgesetzt. "
             "Investorentag {jahr_plus} ist in Vorbereitung (Termin und Format wird durch IR/CFO "
             "kommuniziert).".replace("{jahr_plus}", str(jahr + 1))),
            ("Anhang / Verweise",
             ("list", [
                 "Anhang A: Detaillierte Werks-OEE-Reports (REG, RPL, RCZ, RHU)",
                 "Anhang B: Konzern-Covenant-Compliance-Auszug (siehe REA_Covenant_Compliance_*)",
                 "Anhang C: FX-Hedge-Report (siehe REA_FX_Hedge_*)",
                 "Anhang D: Capital Allocation Framework 2023 (siehe REA_Capital_Allocation_Framework_2023)",
             ])),
        ])


# ─────────────────────────────────────────────────────────────────────────────
# HELPER — Innovation / Technologie-Memo
# ─────────────────────────────────────────────────────────────────────────────
def innovation_memo(fname, thema, sponsor, technik_beschreibung, marktchance,
                    risiken, naechste_schritte, jahr=2024):
    write_doc(f"{B}/{fname}", H,
        f"Innovations-Memo: {thema}",
        subtitle=f"Technologie- und Marktbewertung – Vorstandsvorlage CTO/CMO – {jahr}",
        confidential=True,
        sections=[
            ("Anlass und Auftrag",
             f"Im Rahmen der Technologie-Watch des Konzerns wurde der Themenkomplex »{thema}« "
             f"durch das Innovation Office (Leitung: {sponsor}) bewertet. Das Memo dient als "
             f"Entscheidungsvorlage fuer den Vorstand und beschreibt Technologie, Marktchance, "
             f"Risiken und empfohlene Naechste Schritte. Es wurde gemeinsam mit der RSG-Entwicklung "
             f"in Muenchen (Dr. Klaus Kessler) sowie der Konzernforschung (Werk Heilbronn) "
             f"erarbeitet und mit dem Lead-Customer-Team (BMW, Mercedes-Benz, VW) gegengelesen."),
            ("Technologische Beschreibung", technik_beschreibung),
            ("Marktchance / Volumen", marktchance),
            ("Wettbewerbsumfeld",
             "Relevante Wettbewerber: Continental AG, Robert Bosch GmbH, ZF Friedrichshafen AG, "
             "Aptiv plc, Visteon Corp., Magna International, Lear Corporation, Sensata Technologies "
             "sowie asiatische Spezialisten (Denso, Hyundai Mobis). Im Hinblick auf den "
             "Technologie-Reifegrad (TRL 6–7) sieht das Memo Brennhagen als Fast Follower mit "
             "klarem Differenzierungspotenzial im Bereich Software-Integration."),
            ("Risiken und Annahmen", ("list", risiken)),
            ("Investitions- und Ressourcenbedarf",
             f"Geschaetzter Capex-Bedarf 2025–2027: 18–32 Mio. EUR (Pilot + Pre-Series). "
             f"FTE-Bedarf: 12–22 Engineers (RSG Muenchen / REG Heilbronn). Investitionsabflusse "
             f"sind im Capital Allocation Framework 2023 abgebildet und werden im Q-Update an den "
             f"Aufsichtsrat berichtet. Foerdermoeglichkeiten (IPCEI, KDT-JU, BMWK) werden gepruef."),
            ("Empfehlung und naechste Schritte", ("list", naechste_schritte)),
            ("Freigabe",
             signatures(sponsor, "Sponsor / Innovation Office", R["name"],
                        "Anna Mueller", "CEO", R["name"],
                        place="Stuttgart", date_str_=f"14. Maerz {jahr}")),
        ])


# ─────────────────────────────────────────────────────────────────────────────
# HELPER — Wettbewerbsanalyse
# ─────────────────────────────────────────────────────────────────────────────
def wettbewerbsanalyse(fname, wettbewerber, hq, umsatz_b, ebit_marge, segmente,
                       staerken, schwaechen, bedrohung_fuer_rea):
    write_doc(f"{B}/{fname}", H,
        f"Wettbewerbsanalyse: {wettbewerber}",
        subtitle=f"Vertraulicher Analyse-Report – Strategie / Business Development – 2023",
        confidential=True,
        sections=[
            ("Executive Summary",
             f"Die vorliegende Wettbewerbsanalyse beleuchtet das Unternehmen {wettbewerber} (Sitz: {hq}) "
             f"als Tier-1- / Tier-2-Wettbewerber der Brennhagen Elektronik AG in den Segmenten "
             f"{segmente}. Sie wurde durch die Strategieabteilung in Abstimmung mit Roland Berger "
             f"(extern) erstellt und dient als Grundlage fuer die strategische Positionierung des "
             f"Konzerns sowie als Input fuer die OEM-Account-Strategie der Vertriebsorganisation. "
             f"Konzernumsatz {wettbewerber} GJ 2022: ca. {umsatz_b} Mrd. EUR; ausgewiesene "
             f"EBIT-Marge: ca. {ebit_marge} %."),
            ("Unternehmensprofil",
             f"{wettbewerber} ist ein etablierter Marktteilnehmer mit globaler Aufstellung (Hauptsitz "
             f"{hq}) und Aktivitaeten in mehr als 25 Laendern. Das Unternehmen bedient die "
             f"Premium-OEMs in Europa und Nordamerika und investiert ueberdurchschnittlich in "
             f"Forschung und Entwicklung (FuE-Quote 5–8 % vom Umsatz). Strategischer Fokus liegt "
             f"auf den Wachstumsfeldern Elektrifizierung, ADAS, Konnektivitaet und Software-defined "
             f"Vehicle."),
            ("Geschaeftsfelder und Produkte",
             f"Die Geschaeftsfelder umfassen unter anderem: {segmente}. Insbesondere im Bereich "
             f"Batteriemanagement und ADAS-Sensorik bestehen direkte Ueberschneidungen mit dem "
             f"Brennhagen-Portfolio (BMS-12, ADAS-V4D). Im Bereich Infotainment (ICP-3) bestehen "
             f"weiterhin teilweise Ueberschneidungen mit dem Software-Stack des Wettbewerbers."),
            ("Staerken / Wettbewerbsvorteile", ("list", staerken)),
            ("Schwaechen / Verwundbarkeiten", ("list", schwaechen)),
            ("Bedrohungspotenzial fuer REA", bedrohung_fuer_rea),
            ("Empfohlene Massnahmen",
             ("list", [
                 "Account-spezifische Differenzierungsstrategie schaerfen (Vertriebs-Playbook BMW/Mercedes/VW).",
                 "Verstaerkung der RSG-Softwarekompetenz (ASPICE Level 3, ISO 21434).",
                 "Pruefung gezielter Co-Investitionen mit Lead-Customers in BMS-12.2 (800 V).",
                 "Monitoring der Akquisitionsaktivitaeten des Wettbewerbers ueber Goldman Sachs.",
                 "Patent-Watch durch Konzern-IP-Office (Werk Heilbronn) intensivieren.",
             ])),
            ("Quellen und Stichtag",
             "Quellen: Geschaeftsberichte des Wettbewerbers (2020–2022), S&P Capital IQ, Bloomberg, "
             "Roland Berger Marktstudie 2023, eigene OEM-Befragungen (BMW, Mercedes-Benz, VW). "
             "Stichtag: 30. September 2023."),
        ])


# ─────────────────────────────────────────────────────────────────────────────
# HELPER — Markt-/Szenario-Analyse
# ─────────────────────────────────────────────────────────────────────────────
def szenario_analyse(fname, titel, untertitel, kontext, szenarien, datenrows,
                     implikationen):
    write_doc(f"{B}/{fname}", H, titel,
        subtitle=untertitel,
        confidential=True,
        sections=[
            ("Anlass und Methodik",
             f"{kontext}\n\nMethodisch wird ein Szenario-Ansatz mit drei Pfaden gewaehlt "
             f"(Base / Upside / Downside) auf Basis der Quellen S&P Global Mobility, IHS Markit, "
             f"VDA Bilanzpressekonferenz 2023, McKinsey Automotive Outlook 2023 sowie eigener "
             f"Auswertungen der OEM-Forecasts. Die Aggregation erfolgt durch das Strategieteam "
             f"(Strategy & Corporate Development) unter Begleitung von Roland Berger."),
            ("Marktdaten / Volumina", datenrows),
            ("Szenario-Beschreibung", ("list", szenarien)),
            ("Implikationen fuer Brennhagen", implikationen),
            ("Empfohlene strategische Antworten",
             ("list", [
                 "Capex-Planung an Base-Case ausrichten, Trigger fuer Upside-Anpassung definieren.",
                 "Lieferanten-Diversifizierung (Halbleiter) konsequent fortsetzen (siehe Memo Lieferantendiversifizierung).",
                 "OEM-Forecast-Hygiene mit BMW, Mercedes-Benz, VW, Stellantis quartalsweise abgleichen.",
                 "China-Strategie (RCN Shanghai) angepasst an lokales BEV-Wachstumstempo.",
                 "Stressszenario in MFP einarbeiten und an Aufsichtsrat Pruefungsausschuss reporten.",
             ])),
            ("Versionierung",
             "Version 1.0 / Stand 15. September 2023. Naechste Revision: 31. Maerz 2024. "
             "Verteiler: Vorstand, Strategieausschuss, Aufsichtsrat (Pruefungsausschuss)."),
        ])


# ─────────────────────────────────────────────────────────────────────────────
# HELPER — Investorentag Q&A-Protokoll
# ─────────────────────────────────────────────────────────────────────────────
def investorentag(fname, jahr, ort, kernthemen, qa_pairs, datum):
    write_doc(f"{B}/{fname}", H,
        f"Investorentag {jahr} – Q&A-Protokoll",
        subtitle=f"Capital Markets Day {jahr}, {ort}; Vertraulich – Investor-Relations",
        confidential=True,
        sections=[
            ("Veranstaltungsdaten",
             f"Datum: {datum}. Ort: {ort}. Teilnehmer Brennhagen Elektronik AG: CEO Anna Mueller, "
             f"CFO Laura Bauer, COO Dr. Thomas Weber, CTO Stefan Hoffmann. Moderation: Head of "
             f"Investor Relations (Dr. Susanne Lehmann). Teilnehmer-Investoren: rund 65 "
             f"institutionelle Investoren (Sell-Side + Buy-Side), darunter Deka, DWS, Union, "
             f"Allianz GI, BlackRock, Fidelity, Capital Group, UBS, Berenberg, Goldman Sachs. "
             f"Format: Hybrid (Praesenz + Webcast)."),
            ("Kernthemen / Agenda", ("list", kernthemen)),
            ("Frage- und Antwortrunde",
             ("list", qa_pairs)),
            ("Markt- und Analystenresonanz",
             f"Die Resonanz der Sell-Side war ueberwiegend positiv. Analysten von Berenberg "
             f"(»Buy / TP 31,00 EUR«), Deutsche Bank (»Buy / TP 30,00«), Commerzbank (»Hold / "
             f"TP 26,50«) und Hauck Aufhaeuser (»Buy / TP 32,00«) heben das BMS-12-Wachstum "
             f"und die Software-Defined-Vehicle-Strategie positiv hervor. Kritisch gesehen werden "
             f"die FX-Exposure und das China-Geschaeft. Konsens-TP nach Investorentag: 29,50 EUR."),
            ("Disclosure und naechste Schritte",
             "Alle Aussagen wurden in Uebereinstimmung mit den Regelungen der MAR 596/2014 "
             "(Marktmissbrauchsverordnung) sowie der ad-hoc-Publizitaetspflichten der Brennhagen "
             "Elektronik AG getroffen. Die Praesentation wird am Folgetag auf der IR-Website "
             "publiziert. Etwaige Folgegespraeche mit Analysten / Investoren laufen ueber die "
             "IR-Abteilung. Naechster IR-Termin: Quartalsbericht (Halbjahresfinanzbericht)."),
            ("Freigabe",
             signatures("Anna Mueller", "CEO", R["name"],
                        "Laura Bauer", "CFO", R["name"],
                        place=ort, date_str_=datum)),
        ])


# ─────────────────────────────────────────────────────────────────────────────
# HELPER — Strategie-Memo (kurz, fokussiert)
# ─────────────────────────────────────────────────────────────────────────────
def strategie_memo(fname, titel, anlass, kerninhalt, optionen, empfehlung,
                   verfasser="Stefan Richter, CMO/BD", datum="14. Maerz 2024",
                   draft=False):
    write_doc(f"{B}/{fname}", H,
        f"Strategie-Memo: {titel}",
        subtitle=f"Vorstandsvorlage / Strategie & Business Development – {datum}",
        confidential=True, draft=draft,
        sections=[
            ("Anlass",
             anlass + "\n\nDas Memo wurde durch " + verfasser +
             " auf Anforderung des Vorstandes (CEO Anna Mueller) erstellt und mit dem CFO "
             "(Laura Bauer) sowie dem COO (Dr. Thomas Weber) abgestimmt. Es dient als Grundlage "
             "fuer den Beschluss in der naechsten regulaeren Vorstandssitzung sowie "
             "ggf. als Vorlage an den Aufsichtsrat / Pruefungsausschuss."),
            ("Sachverhalt / Kerninhalt", kerninhalt),
            ("Handlungsoptionen", ("list", optionen)),
            ("Bewertung und Empfehlung", empfehlung),
            ("Auswirkungen auf Konzernsteuerung",
             "Die Umsetzung des empfohlenen Pfades beeinflusst die Konzernsteuerung in den "
             "Dimensionen Capex (Capital Allocation Framework), Personal (HR-Roadmap), "
             "Technologie (FuE-Roadmap CTO) sowie Compliance (Group Compliance Office). "
             "Die Konsequenzen werden in der Mittelfristplanung (MFP) ab dem naechsten Zyklus "
             "abgebildet und an den Aufsichtsrat (Pruefungsausschuss) berichtet."),
            ("Naechste Schritte",
             ("list", [
                 "Beschlussvorlage Vorstand: naechste regulaere Sitzung.",
                 "Information Aufsichtsrats-Vorsitz (Dr. Klaus Steinbrueck) durch CEO.",
                 "Aufnahme in Strategie-Roadmap (Strategy Office).",
                 "Kommunikationspaket Investor-Relations vorbereiten (falls ad-hoc-relevant).",
             ])),
            ("Verfasser / Freigabe",
             signatures(verfasser.split(",")[0], verfasser.split(",", 1)[1].strip() if "," in verfasser else "Verfasser", R["name"],
                        "Anna Mueller", "CEO", R["name"],
                        place="Stuttgart", date_str_=datum)),
        ])


# ─────────────────────────────────────────────────────────────────────────────
# HELPER — Generic Management-/Strategie-Dokument
# ─────────────────────────────────────────────────────────────────────────────
def generic_strategie(fname, titel, untertitel, abschnitte, datum="2023"):
    write_doc(f"{B}/{fname}", H, titel, subtitle=untertitel, confidential=True,
              sections=abschnitte + [
                  ("Versionierung und Verteiler",
                   f"Version 1.0 / Stand {datum}. Verteiler: Vorstand der Brennhagen Elektronik AG, "
                   f"Aufsichtsrats-Vorsitz (Dr. Klaus Steinbrueck), Pruefungsausschuss-Vorsitz "
                   f"(Prof. Dr.-Ing. Gerhard Voss), Group Compliance Office, Schriftfuehrerin "
                   f"Dr. Veronika Steiner."),
              ])


# ═════════════════════════════════════════════════════════════════════════════
# DOC INSTANCES
# ═════════════════════════════════════════════════════════════════════════════

# ── Strategiepapiere 2021–2023 (Strategiepapier_2021 ist ueber 200w → skip;
#    2022 + 2023 sind je 194w → noch knapp thin) ────────────────────────────
strategie_deck(
    "REA_Strategiepapier_2022.docx", 2022, "Precision Growth 2022 – Phase II",
    "Vor-IPO-Wachstum mit Fokus auf BMS und ADAS",
    saeulen=[
        "Saeule I – Operative Exzellenz: OEE-Steigerung in allen Werken auf >85 % bis Ende 2023.",
        "Saeule II – BEV-Fokus: BMS-12-Hochlauf in Heilbronn, Skalierung auf 3,0 Mio. Module/Jahr.",
        "Saeule III – ADAS-Software: Aufbau ASPICE-Level-3-Kompetenz in RSG Muenchen.",
        "Saeule IV – Internationalisierung: Vorbereitung Vorstandsressort Asien (CRO Asia).",
        "Saeule V – Kapitalmarkt: IPO-Vorbereitung Q3/2022, Roadshow mit Deutsche Bank / Berenberg / Commerzbank.",
    ],
    kpi_rows=[
        ["KPI", "2021 Ist", "2022 Plan", "2022 Erwartung", "2025 Ziel"],
        ["Umsatz Konzern", "580", "595", "600", "780"],
        ["EBITDA", "70", "72", "73", "118"],
        ["EBITDA-Marge %", "12,1", "12,1", "12,2", "15,1"],
        ["FTE", "3.820", "3.970", "4.020", "4.500"],
        ["Capex", "38", "55", "52", "62"],
    ],
    marktkontext=(
        "Das Marktumfeld 2022 ist gepraegt durch anhaltende Halbleiter-Allokation (NXP, Infineon, STMicroelectronics), "
        "geopolitische Risiken (Ukraine-Krieg) sowie eine beschleunigte Elektrifizierung der OEM-Plattformen "
        "(VW MEB+, Mercedes-Benz MMA, BMW Neue Klasse, Stellantis STLA). Brennhagen profitiert vom BEV-Hochlauf, "
        "ist aber gegen die Halbleiter-Knappheit nur teilweise abgesichert (Dual-Sourcing-Quote 38 %)."
    ),
    risiken=[
        "Risiko HL1 – Halbleiter-Allokation NXP S32G: Gegenmassnahme Dual-Sourcing mit Infineon AURIX TC4xx (Roadmap Q4/2023).",
        "Risiko OEM1 – VW MEB+-Verzoegerung (Cariad-Software): potenzielle Volumen-Verschiebung 2024/25.",
        "Risiko FX – PLN/CZK/HUF: Hedging via Deutsche Bank / Commerzbank Treasury-Konsortium (siehe FX-Hedge-Berichte).",
        "Risiko REG – Personal Heilbronn: Skill-Gap Embedded-Software, Gegensteuerung ueber Talentprogramm.",
    ],
    beschluss_datum="9. Dezember 2021",
)

strategie_deck(
    "REA_Strategiepapier_2023.docx", 2023, "NEXT 2026 – Post-IPO-Wachstum",
    "Skalierung mit drei Saeulen: BEV/BMS, ADAS L2-3, Software-as-a-Service",
    saeulen=[
        "Saeule I – BEV/BMS: BMS-12-Plattform-Expansion (800 V), neue Generation BMS-12.2 SOP Q2/2025.",
        "Saeule II – ADAS L2-3: Radar Fusion ADAS-V4D, Lead-Customers Mercedes-Benz und Stellantis.",
        "Saeule III – Software-as-a-Service: »BrennhagenOS« – OTA-Update-Plattform mit ARR-Geschaeftsmodell.",
        "Saeule IV – Internationalisierung: Vorstand CRO Asia (Dr. Yuki Tanaka) ab 1.4.2024.",
        "Saeule V – ESG / CSRD: Reporting-Infrastruktur Berichtspflicht GJ 2024 (BTP-Gruppe + RHO).",
    ],
    kpi_rows=[
        ["KPI", "2022 Ist", "2023 Erwartung", "2025 Plan", "2028 Ziel"],
        ["Umsatz Konzern", "600", "612", "820", "1.000"],
        ["EBITDA", "73", "74,3", "128", "150"],
        ["EBITDA-Marge %", "12,2", "12,1", "15,6", "15,0"],
        ["FTE", "4.020", "4.180", "4.700", "5.000"],
        ["Capex", "52", "62", "72", "80"],
        ["Dividende EUR/Aktie", "1,80", "2,10", "2,80", "3,50"],
    ],
    marktkontext=(
        "Nach erfolgreichem IPO (14. Oktober 2022, Emissionskurs 24,50 EUR/Aktie, Erloes 612 Mio. EUR) "
        "ist Brennhagen Elektronik AG nun Prime-Standard-Wert. Der BEV-Markt waechst in Europa mit CAGR 18-22 % bis 2028, "
        "ADAS Level 2-3 mit CAGR 12 %. China-Markt zeigt Konsolidierungstendenzen mit starker lokaler Konkurrenz "
        "(BYD, Huawei, NIO). Halbleiter-Verfuegbarkeit normalisiert sich, bleibt aber spezifisch (NXP, Renesas) eng."
    ),
    risiken=[
        "Risiko M1 – BEV-Nachfrage-Eindellung (Foerdermittel-Wegfall DE): Stress-Szenario Downside -8 % Umsatz.",
        "Risiko M2 – China-Exposure / Decoupling: RCN-Strategy-Review Q4/2024, Pruefung lokaler Partner.",
        "Risiko OEM1 – Stellantis Werks-Schliessungen (FR/IT): mittelbare Volumen-Risiken ADAS-V4D / ECU-900.",
        "Risiko T1 – Cybersecurity UNECE R155: Verspaetete Type-Approval bei nicht-konformen Zulieferern.",
        "Risiko F1 – Zinsumfeld / Refinanzierung Konsortialkredit 2027: fruehzeitige Markt-Sondierung 2025.",
    ],
    beschluss_datum="12. Dezember 2022",
)

# Strategiepapier 2021 ist bereits dick genug (skip) — aber sicher ueberschreiben um konsistent zu sein
strategie_deck(
    "REA_Strategiepapier_2021.docx", 2021, "Precision Growth 2021–2025 – Phase I",
    "Vorbereitung des Boersengangs (IPO) und Aufbau Skalen-Plattform",
    saeulen=[
        "Saeule I – Operative Exzellenz (OEE / IATF 16949 in allen Werken).",
        "Saeule II – BMS-12-Plattform: Hochlauf in Heilbronn, Lead-Kunde VW (ID.7).",
        "Saeule III – ADAS-V4D Vorentwicklung mit Mercedes-Benz.",
        "Saeule IV – IPO-Vorbereitung mit Goldman Sachs / Hengeler Mueller / KPMG.",
        "Saeule V – Konzern-Governance gemaess DCGK und Prime-Standard-Anforderungen.",
    ],
    kpi_rows=[
        ["KPI", "2019 Ist", "2020 Ist", "2021 Plan", "2025 Ziel"],
        ["Umsatz", "510", "542", "580", "780"],
        ["EBITDA", "61", "64", "70", "118"],
        ["FTE", "3.510", "3.620", "3.820", "4.500"],
    ],
    marktkontext=(
        "Das Jahr 2021 ist gepraegt durch COVID-Nachwirkungen, Halbleiter-Krise und einen "
        "beschleunigten Wandel der OEMs in Richtung Elektrifizierung. Brennhagen positioniert sich "
        "fuer den Boersengang als europaeischer Tier-1-Spezialist mit BMS-, ADAS- und Infotainment-"
        "Schwerpunkt."
    ),
    risiken=[
        "Risiko Halbleiter (NXP, Infineon, STMicro) – Allokation und Preissteigerungen.",
        "Risiko COVID Werks-Schliessungen – Kontingenz-Plan in allen Werken aktiv.",
        "Risiko IPO-Window 2022 – Marktvolatilitaet, Backup-Szenario »Private Placement«.",
    ],
    beschluss_datum="10. Dezember 2020",
)

# ── Vorstandspraesentationen Quartal 2022 + 2023 ──────────────────────────────
for (jahr, q, datum) in [
    (2022, "Q1", "10. Maerz 2022"),
    (2022, "Q2", "16. Juni 2022"),
    (2022, "Q3", "15. September 2022"),
    (2022, "Q4", "8. Dezember 2022"),
    (2023, "Q1", "9. Maerz 2023"),
    (2023, "Q2", "15. Juni 2023"),
    (2023, "Q4", "7. Dezember 2023"),
]:
    fname = f"REA_Vorstandspräsentation_{jahr}_{q}.docx"
    schwerpunkte = [
        f"OEM-Pipeline Update {q}/{jahr} (BMW, Mercedes-Benz, VW, Stellantis, Hyundai)",
        f"BMS-12 Hochlauf Heilbronn – Status SOP / OEE / Stueckzahlen",
        f"ADAS-V4D-Programm – Engineering-Sample-Lieferungen / ASPICE-Status RSG",
        f"FX- und Treasury-Lage – siehe FX-Hedge-Bericht {q}/{jahr}",
        f"Investor-Relations Update – Analystenkonsens, Aktienkursentwicklung, Aktionaersstruktur",
        f"HR / Vorstandsthemen – Nachbesetzungen, Talentprogramme",
    ]
    kpi_table = [
        ["KPI", f"{q}/{jahr} Ist", f"{q}/{jahr} Plan", "Vorjahr", "FY Forecast"],
        ["Umsatz", "152", "150", "145", "612"],
        ["EBITDA", "18,4", "18,0", "17,1", "74,3"],
        ["EBITDA-Marge %", "12,1", "12,0", "11,8", "12,1"],
        ["Net Debt", "182", "190", "210", "175"],
        ["Capex", "14,2", "16,5", "12,8", "62"],
    ]
    beschluesse = [
        f"V-{jahr}-{q}-001: Freigabe Investitionsantrag Werk Heilbronn (Capex 4,8 Mio. EUR).",
        f"V-{jahr}-{q}-002: Beauftragung KPMG mit Pruefungsschwerpunkten {jahr}.",
        f"V-{jahr}-{q}-003: Genehmigung Dienstreise-Plan COO Asien (Sept./Okt.).",
        f"V-{jahr}-{q}-004: Vorlage CSRD-Roadmap an Pruefungsausschuss bis Ende Folgequartal.",
    ]
    vorstand_quartal(fname, jahr, q, schwerpunkte, kpi_table, beschluesse, datum)


# ── Innovations-Memos (11 docs) ───────────────────────────────────────────────
innovations = [
    ("REA_Innovation_48V_Bordnetz_Modul_2024.docx", "48V-Bordnetz-Modul (Mild-Hybrid)",
     "Dr. Klaus Kessler (RSG Muenchen)",
     "Das 48V-Bordnetz-Modul vereinfacht den Aufbau von Mild-Hybrid-Architekturen (MHEV) und ermoeglicht "
     "Energie-Rueckgewinnung bis 12 kW. Schluesselkomponenten sind DC/DC-Konverter (48V/12V, 3 kW), "
     "Riemen-Startergenerator (BSG)-Ansteuerung und integriertes Batteriemanagement fuer "
     "Lithium-Ionen-48V-Pack. Brennhagen kann auf BMS-12-Bausteine und ECU-900-Plattform aufbauen.",
     "TAM 2025–2028: 3,5–4,2 Mrd. EUR; SAM Europa: ca. 1,2 Mrd. EUR. Lead-Customer-Kandidaten: "
     "Ford-Werke (Kuga MHEV-Refresh), Stellantis (1,5 Hybrid), Hyundai. Preispunkt 35–48 EUR / Modul.",
     ["Wettbewerber Continental und Bosch mit etabliertem 48V-Portfolio – Differenzierung notwendig.",
      "Risiko BEV-Substitution: Mild-Hybrid wird mittelfristig durch Voll-BEV ersetzt (Window 2025–2030).",
      "Skill-Gap BSG-Ansteuerung – Aufbau in RSG Muenchen erforderlich."],
     ["Pilot-Projekt mit Stellantis Q3/2024 starten (Engineering Sample).",
      "Patent-Recherche durch IP-Office Heilbronn beauftragen.",
      "Capex-Antrag fuer SMT-Linie Heilbronn (3,2 Mio. EUR) vorbereiten."]),

    ("REA_Innovation_AI_Driven_ADAS_2024.docx", "KI-getriebenes ADAS (Domain Controller)",
     "Lars Wittmann (Lead Developer RSG)",
     "AI-driven ADAS nutzt Deep-Learning-Beschleuniger (NVIDIA Drive Thor, Qualcomm Ride Flex) "
     "fuer Sensor-Fusion (Radar, LiDAR, Kamera) auf einem Domain Controller (DC). Brennhagen kombiniert "
     "ADAS-V4D-Hardware mit Software-Stack auf ROS2 / AUTOSAR Adaptive Basis.",
     "TAM 2026–2030: 18–24 Mrd. EUR fuer ADAS-Domain-Controller; SAM Europa Premium-OEMs: 6 Mrd. EUR. "
     "Lead-Customer-Pipeline: Mercedes-Benz (MMA-Plattform), BMW Neue Klasse.",
     ["Wettbewerber Mobileye (EyeQ6), NVIDIA-Mobileye-Tesla-Stack, Qualcomm Snapdragon Ride.",
      "Risiko Halbleiter-Lieferzeiten (NVIDIA Drive Thor) – Allocation-Gespraeche notwendig.",
      "Regulatorisches Risiko EU AI Act – Konformitaetsbewertung erforderlich."],
     ["Joint-Development-Vereinbarung mit NVIDIA pruefen.",
      "ASPICE-Level-3-Audit RSG abschliessen (Q4/2024).",
      "Foerderantrag IPCEI-CIS einreichen."]),

    ("REA_Innovation_Automotive_WIFI7_Module_2024.docx", "Automotive Wi-Fi 7 Modul",
     "Dr. Klaus Kessler (RSG Muenchen)",
     "Automotive Wi-Fi 7 (IEEE 802.11be) ermoeglicht Multi-Gigabit-Konnektivitaet im Fahrzeug "
     "(In-Car-Streaming, V2X-Daten, OTA-Massendownload). Brennhagen plant ein integriertes Modul mit "
     "Qualcomm FastConnect 7800-Chipsatz, AEC-Q100 Grade 3 Qualifizierung.",
     "TAM 2026–2030: 0,8–1,5 Mrd. EUR; Wachstum getrieben durch SDV-Architekturen und "
     "Streaming-Use-Cases (rear-seat entertainment).",
     ["Konkurrenz durch LG Innotek, Continental, Marquardt, Murata.",
      "Risiko Spektrum-Allocation (6 GHz Band) – regulatorische Klaerung in DE/EU teils offen.",
      "Risiko Chipsatz-Verfuegbarkeit Qualcomm – Single-Source."],
     ["Sample-Lieferung an BMW (MGU2) Q2/2025.",
      "Kooperation mit Qualcomm-Automotive-Team vertiefen.",
      "ICP-3-Plattform-Variante »ICP-3 Connect« definieren."]),

    ("REA_Innovation_Digital_Twin_Fertigung_2024_20230915.docx", "Digital Twin Fertigung",
     "Dr. Thomas Weber (COO)",
     "Digital Twin der Produktionslinien in Heilbronn und Katowice basierend auf Siemens MindSphere "
     "und SAP DMC. Ziel: Echtzeit-OEE-Monitoring, Predictive Maintenance, Energieverbrauchs-Optimierung "
     "(ISO 50001).",
     "Quantifizierter Nutzen: OEE +3 ppt (entspricht ca. 7 Mio. EUR Marge p.a.); Energieverbrauch "
     "-12 % (Beitrag ESG / Scope 2).",
     ["Risiko OT/IT-Konvergenz – Cybersecurity, Segmentierung mit SOC erforderlich.",
      "Risiko Akzeptanz Werkleitung – Change-Management notwendig.",
      "Risiko Datenqualitaet aus Altanlagen – Retrofit-Sensorik teils notwendig."],
     ["Pilot in Heilbronn Linie 4 Q1/2024.",
      "Roll-out Katowice Q3/2024.",
      "Integration in Group Performance Management System (GPMS)."]),

    ("REA_Innovation_LiDAR_Integration_2024.docx", "LiDAR-Integration ADAS-V4D",
     "Lars Wittmann (Lead Developer RSG)",
     "Integration eines Solid-State-LiDAR (Innoviz, Luminar, Valeo SCALA 3) in das ADAS-V4D-System. "
     "Sensor-Fusion auf ECU-Level mit Radar + Kamera. Ziel: Hands-Free L3 Autobahn ab 130 km/h.",
     "TAM Premium-Segment 2027–2030: 4,5–6,2 Mrd. EUR. Lead-Customer: Mercedes-Benz (Drive Pilot 2).",
     ["Hohe Kosten LiDAR-Sensor (350–600 EUR/Stueck) – Kosten-Roadmap kritisch.",
      "Wettbewerb durch Mobileye Chauffeur und Tesla FSD-Stack.",
      "Regulatorische Anforderungen UNECE R157 (ALKS)."],
     ["Sourcing-Strategie LiDAR-Sensor (Dual-Source Valeo / Luminar).",
      "Sample-Programm Mercedes-Benz Q3/2025.",
      "Patentanmeldung Fusion-Algorithmus durch RSG."]),

    ("REA_Innovation_OTA_Update_Platform_v3_2024.docx", "OTA-Update-Plattform v3 (»BrennhagenOS«)",
     "Dr. Klaus Kessler (RSG Muenchen)",
     "Over-the-Air-Update-Plattform fuer ECU-900, ICP-3 und ADAS-V4D. Architektur: Edge-Caching, "
     "delta-Updates (UPDATE-3.0), kryptographische Signaturen (UNECE R156 konform). Backend: AWS "
     "EU (Frankfurt) mit Failover ins Konzern-RZ Stuttgart.",
     "Geschaeftsmodell: Subscription / Pay-per-Update; ARR-Ziel 2028: 35 Mio. EUR. Cross-Sell ueber "
     "alle OEM-Plattformen.",
     ["Cybersecurity-Risiken UNECE R155 – TARA und Penetration-Tests verpflichtend.",
      "OEM-Akzeptanz unterschiedlich – manche OEMs wollen eigene Update-Backbones.",
      "Hyperscaler-Abhaengigkeit AWS – Cloud-Exit-Strategie definieren."]
     ,
     ["Pilot mit Stellantis (ECU-900) Q1/2025.",
      "Integration in ICP-3 mit BMW Q3/2025.",
      "Geschaeftsmodell-Validierung mit IR / CFO fuer Capital Markets Day 2025."]),

    ("REA_Innovation_Software_Defined_Vehicle_OS_2024.docx", "Software-Defined Vehicle OS",
     "Lars Wittmann (Lead Developer RSG)",
     "BrennhagenOS als HAL-/Middleware-Schicht zwischen AUTOSAR Adaptive und Anwendungs-Layer. "
     "Unterstuetzung von Zone Controllern, ECU-Konsolidierung 80+ → 8–12 ECUs. Containerisierung "
     "(OCI), DDS-Kommunikation, OTA-Integration.",
     "TAM 2028–2032: 12–18 Mrd. EUR; Lead-Markt Europa und China. SDV-Strategie eng verzahnt mit "
     "Software-as-a-Service-Saeule.",
     ["Wettbewerb Vector cVDL, ETAS RTA-VRTE, Elektrobit EB tresos, Bosch SDV-Stack.",
      "Akzeptanz OEM-Plattform-Strategien (VW Cariad, Mercedes MB.OS, Stellantis STLA).",
      "Skill-Gap Microservice-Architektur – Recruitment RSG 60 FTE."],
     ["Strategische Partnerschaft mit Elektrobit pruefen.",
      "Joint-Development VW Cariad sondieren.",
      "Capex-Antrag RSG fuer Test-/Validation-Labor (4,5 Mio. EUR)."]),

    ("REA_Innovation_Solid_State_Battery_BMS_2024.docx", "BMS fuer Solid-State-Batterien",
     "Sabine Brand (Q-Leitung REG)",
     "Anpassung der BMS-12-Plattform an Solid-State-Batterien (SSB) der Generation 2027+ (Lead-Kunden "
     "VW PowerCo, Mercedes-Factorial, Hyundai). SSB erfordern hoehere Spannungen (>900 V), niedrigere "
     "Innenwiderstaende und neue Thermomanagement-Strategien.",
     "TAM 2028–2032: 8–14 Mrd. EUR. Brennhagen in fruehzeitiger Co-Engineering-Phase mit VW PowerCo "
     "(Salzgitter) sowie Hyundai (Ulsan).",
     ["Technologie-Risiko SSB-Reife – Verzoegerungen 2027 → 2029 wahrscheinlich.",
      "Wettbewerb chinesische Anbieter (CATL, BYD) mit eigener BMS-Integration.",
      "FuE-Investitionsbedarf hoch (>22 Mio. EUR ueber 4 Jahre)."],
     ["Joint-Engineering-Vereinbarung VW PowerCo unterzeichnen (Q3/2024).",
      "Patentstrategie SSB-BMS definieren.",
      "Foerderantrag IPCEI-Batterie pruefen."]),

    ("REA_Innovation_V2X_Kommunikationsmodul_2024.docx", "V2X-Kommunikationsmodul",
     "Dr. Klaus Kessler (RSG Muenchen)",
     "Vehicle-to-Everything (V2X) Modul mit C-V2X (3GPP Release 17) und ITS-G5 Dual-Mode. "
     "Anwendungsszenarien: Cooperative Adaptive Cruise Control, Intersection Movement Assist, "
     "Hazard Warning. AEC-Q100 Grade 2 Qualifizierung.",
     "TAM 2027–2031: 2,2–3,8 Mrd. EUR. EU C-ITS-Mandat foerdert Marktdurchbruch ab 2026/27.",
     ["Regulatorische Unsicherheit C-V2X vs. ITS-G5 (EU-Pruefung).",
      "Konkurrenz Continental, Bosch, LG Innotek.",
      "Chipsatz-Single-Source Qualcomm 9150 – Alternative Autotalks pruefen."],
     ["Field-Trial mit ASFINAG (AT) und BASt (DE) Q2/2025.",
      "Sample-Lieferung VW Q4/2025.",
      "Patentanmeldung Multi-Channel-Sicherheit."]),

    ("REA_Innovation_Zonal_ECU_Architektur_2024.docx", "Zonal ECU Architektur",
     "Lars Wittmann (Lead Developer RSG)",
     "Zonal-ECU-Architektur konsolidiert Fahrzeug-Funktionen in 4–6 Zonen-Controllern statt 80+ "
     "dezidierten ECUs. Hauptvorteile: 30–45 % Kabelbaumreduktion, einfachere SDV-Integration, "
     "geringeres Gewicht. Brennhagen kombiniert ECU-900-Plattform mit BrennhagenOS.",
     "TAM 2027–2031: 5,5–8,2 Mrd. EUR. Lead-Plattformen: BMW Neue Klasse, Mercedes MMA, Stellantis STLA.",
     ["Konkurrenz durch ZF (zFAS), Continental, Bosch, Aptiv (Smart Vehicle Architecture).",
      "Skill-Gap Zonen-Controller-Validierung – RSG-Recruitment in Muenchen.",
      "Standardisierungs-Risiko AUTOSAR Adaptive vs. proprietaere OEM-Stacks."],
     ["Sample-Lieferung BMW Neue Klasse Q2/2026.",
      "Co-Development Mercedes-Benz MMA pruefen.",
      "Capex-Antrag Heilbronn fuer Zonen-Controller-Linie (8,2 Mio. EUR)."]),
]
for tup in innovations:
    innovation_memo(*tup)


# ── Wettbewerbsanalysen (9 docs) ──────────────────────────────────────────────
wettbewerber = [
    ("REA_Wettbewerbsanalyse_Aptiv_plc_2023.docx", "Aptiv plc", "Dublin / Schaffhausen",
     "17,5", "9,2", "Signal & Power Solutions, Advanced Safety & User Experience",
     ["Globale Skalierung mit >190.000 MA, breites OEM-Portfolio.",
      "Starke Position im US-Markt (Detroit Big Three).",
      "SVA (Smart Vehicle Architecture) als SDV-Plattform reif.",
      "Software-Geschaeft Wind River (Cloud-Native, Linux)."],
     ["Komplexes Konglomerat – integrationsbedingte Reibungsverluste.",
      "Europa-Premium-OEMs (BMW, Mercedes-Benz) weniger stark vertreten.",
      "Niedrige Bruttomarge im Connector-Geschaeft (Power Solutions)."],
     "Aptiv ist im SDV-Bereich wesentlicher Wettbewerber von BrennhagenOS – Differenzierungsstrategie "
     "ueber tieferes ECU-/BMS-Hardware-Know-how und ASPICE-Level-3-Software-Reife. Bedrohungsgrad: hoch."),

    ("REA_Wettbewerbsanalyse_Continental_AG_2023.docx", "Continental AG", "Hannover",
     "39,4", "5,1", "Automotive (ADAS, Display, Connectivity), Tires, ContiTech",
     ["Marktfuehrer Europa fuer ADAS-Systeme (Radar/Kamera).",
      "Direkter Zugang zu allen deutschen OEMs (BMW, Mercedes, VW, Audi, Porsche).",
      "Hohe Patentdichte ADAS / Fahrwerkselektronik.",
      "Spin-off Vitesco als reiner E-Antriebs-Player."],
     ["Profitabilitaet im Automotive-Segment niedrig (Restrukturierung 2023–2025).",
      "Komplexitaetsprobleme nach Vitesco-Trennung.",
      "Software-/SDV-Strategie nicht klar konturiert."],
     "Continental ist der dominante Wettbewerber im europaeischen ADAS-Markt und Hauptkonkurrent "
     "fuer ADAS-V4D. Bedrohungsgrad: sehr hoch. Differenzierung ueber Lean-Organisation, schnellere "
     "Time-to-Market und ASPICE-Level-3."),

    ("REA_Wettbewerbsanalyse_Lear_Corporation_2023.docx", "Lear Corporation", "Southfield, MI (USA)",
     "20,9", "5,4", "Seating, E-Systems (Connectors, Wiring, BEV-Komponenten)",
     ["Starke Connector-Position (#2 weltweit nach Aptiv).",
      "Aufstrebende E-Systems-Division mit BEV-Fokus.",
      "Strategische Akquisitionen IGB Automotive, M&N Plastics, Kongsberg PowerTech."],
     ["Geringer Marktanteil ADAS / Domain-Controller.",
      "Europa-Praesenz weniger stark als US/MX.",
      "Margenpotenzial bei Seating begrenzt."],
     "Lear ist im Connector- und E-Systems-Bereich relevanter Wettbewerber, weniger im ADAS-Premium-Segment. "
     "Bedrohungsgrad: mittel. Beobachtung im Hinblick auf BMS-Strategie."),

    ("REA_Wettbewerbsanalyse_Magna_International_2023.docx", "Magna International", "Aurora, Ontario (CA)",
     "37,8", "4,8", "Body Exteriors & Structures, Power & Vision, Seating Systems, Complete Vehicles",
     ["Breite Wertschoepfungskette inklusive Komplettfahrzeug-Montage (Magna Steyr).",
      "Marktfuehrer Mirror/Camera-Module (Magna Mirrors).",
      "Strategische Partnerschaften mit BMW (Spartanburg), Toyota (Onnaing)."],
     ["Niedrige Software-Anteil – kaum SDV-Strategie sichtbar.",
      "Profitabilitaet auf Konzernebene gedrueckt (Body Exteriors).",
      "Begrenzte BMS-Kompetenz."],
     "Magna konkurriert peripher in ADAS-Sensorik (Magna Electronics). Bedrohungsgrad: mittel. "
     "Beobachtung in Camera-/Mirror-Modulen, geringe Ueberschneidung mit BMS-12."),

    ("REA_Wettbewerbsanalyse_Robert_Bosch_GmbH_2023.docx", "Robert Bosch GmbH", "Gerlingen (Stuttgart)",
     "88,2", "7,5", "Mobility Solutions (Powertrain, Chassis, Body Electronics, Connected Mobility)",
     ["Globaler Marktfuehrer Automotive Tier-1 – breites Produktportfolio.",
      "Hohe FuE-Quote (>8 % vom Umsatz).",
      "Starke Position bei Diesel-Einspritzung, Bremssystemen, ESP, ADAS-Radar.",
      "Massive Investitionen in BEV (PowerCo Lieferant), SiC-Halbleiter (Reutlingen)."],
     ["Hohe Komplexitaet, Restrukturierung Powertrain Solutions noetig.",
      "Reaktionszeit / Time-to-Market vergleichsweise lang.",
      "Software-Kompetenz im SDV-Segment im Aufbau."],
     "Bosch ist der wichtigste Wettbewerber in nahezu allen Brennhagen-Segmenten. Bedrohungsgrad: sehr hoch. "
     "Differenzierung ueber Spezialisierung (BMS-12, ADAS-V4D, BrennhagenOS) und schnellere Innovationszyklen."),

    ("REA_Wettbewerbsanalyse_Sensata_Technologies_2023.docx", "Sensata Technologies", "Attleboro, MA (USA)",
     "4,0", "12,1", "Sensors (Pressure, Temperature, Position), Controls (Electrical Protection)",
     ["Hohe Spezialisierung in MEMS-Sensorik.",
      "Marktposition in Reifenluftdrucksensoren (TPMS) und Drucksensoren.",
      "BEV-spezifische Sensoren (Battery, HV-Power)."],
     ["Limitierte Software-Kompetenz.",
      "Hohe Abhaengigkeit von US-OEMs.",
      "Sensor-only Geschaeftsmodell – kein System-Tier-1."],
     "Sensata konkurriert in Teilbereichen der BMS-Sensorik (HV-Stromsensor). Bedrohungsgrad: niedrig–mittel. "
     "Mehr Lieferant als Wettbewerber."),

    ("REA_Wettbewerbsanalyse_Visteon_Corp_2023.docx", "Visteon Corp.", "Van Buren Township, MI (USA)",
     "3,8", "8,8", "Cockpit Electronics (Displays, Clusters, Infotainment, ADAS)",
     ["Spezialist fuer Displays / Cluster-Module.",
      "Starkes Wachstum bei Software-Defined-Cockpit (SmartCore-Plattform).",
      "Hohe Margen (Cockpit Electronics Pure-Play)."],
     ["Hohe Konzentration auf US-OEMs (Ford, GM, Stellantis).",
      "Begrenzte ADAS-Sensorik-Kompetenz.",
      "Wenig BMS-Praesenz."],
     "Visteon konkurriert mit ICP-3 im Infotainment-/Cluster-Bereich. Bedrohungsgrad: mittel. "
     "Differenzierung ueber Software-Tiefe und OEM-Lokalisierung Europa."),

    ("REA_Wettbewerbsanalyse_ZF_Friedrichshafen_AG_2023.docx", "ZF Friedrichshafen AG", "Friedrichshafen",
     "43,8", "3,9", "Passive Safety, Vehicle Motion Control, Electrified Powertrain, ADAS, Industrial Tech",
     ["Marktfuehrer Lenkung / Bremsen / Fahrwerk-Elektronik.",
      "Hohe FuE-Investitionen in zFAS (zentraler Fahrcomputer).",
      "Akquisitionen WABCO, TRW – breites Portfolio."],
     ["Hohe Verschuldung nach WABCO-Akquisition.",
      "Restrukturierungsdruck Powertrain (Diesel).",
      "Software-/SDV-Position im Aufbau."],
     "ZF ist im ADAS-Domain-Controller (zFAS) direkter Wettbewerber. Bedrohungsgrad: hoch. AR-Vorsitz "
     "Dr. Steinbrueck war frueher CEO ZF Friedrichshafen – Conflict-of-Interest-Prozesse beachten."),

    ("REA_Wettbewerbsanalyse_Tier1_2023.docx", "Tier-1-Wettbewerbslandschaft Konsolidiert",
     "global (Top 20 Tier-1)",
     "ca. 400 (Aggregat)", "5,8 (gewichteter Schnitt)",
     "Konsolidierte Analyse Top-20-Wettbewerber: Bosch, ZF, Continental, Aptiv, Magna, Lear, Forvia, "
     "DENSO, Marelli, Aisin, Mando, Sumitomo, Yazaki, BorgWarner, Schaeffler, Veoneer, Hella (Forvia), "
     "Visteon, Vitesco, Valeo",
     ["Hohe FuE-Budgets der Top-5 (>3 Mrd. EUR p.a.).",
      "Diversifiziertes Portfolio (Hardware + Software).",
      "Globale Skalierung mit Werken auf allen Kontinenten."],
     ["Komplexitaet und Reaktionsgeschwindigkeit teils begrenzt.",
      "Profitabilitaet im Mittel unter Premium-Spezialisten.",
      "Restrukturierung Diesel-/ICE-Lastigkeit (CAF-Index)."],
     "Die Top-20-Tier-1 dominieren rund 75 % des globalen Marktvolumens. Brennhagen positioniert sich als "
     "Premium-Spezialist mit klarem Fokus auf BMS, ADAS und SDV. Bedrohungsgrad in Summe hoch, aber "
     "Spezialisierungs-Strategie schuetzt vor direktem Kostenwettbewerb."),
]
for tup in wettbewerber:
    wettbewerbsanalyse(*tup)


# ── Markt-/Szenario-Analysen ──────────────────────────────────────────────────
szenario_analyse(
    "REA_ADAS_Markt_2024.docx",
    "ADAS-Marktanalyse 2024 (Europa / China)",
    "Strategie-/Marktanalyse – ADAS Level 2-3 – Vorstandsvorlage CTO/CMO 2024",
    "Die ADAS-Markt-Volumen entwickeln sich auf Europa-Ebene mit ca. 12 % CAGR (2023–2030). "
    "In China steigt das ADAS-Volumen schneller (ca. 18 % CAGR) aufgrund regulatorischer "
    "Anreize und neuer OEM-Plattformen (Huawei HarmonyOS Cockpit, NIO Banyan). Brennhagen "
    "fokussiert das Premium-Segment Europa (Mercedes-Benz, BMW, Audi) sowie ausgewaehlte "
    "Mass-Market-Plattformen (Stellantis STLA, Ford). Das Memo dient als Grundlage fuer die "
    "ADAS-V4D-Plattform-Roadmap.",
    szenarien=[
        "Base: ADAS L2 weiter Hauptvolumen, ADAS L3 in Premium ab 2026; ADAS-V4D-Umsatz 2026: 180 Mio. EUR.",
        "Upside: schneller L3-Rollout BMW/Mercedes; ADAS-V4D-Umsatz 2026: 235 Mio. EUR.",
        "Downside: Regulatory Lag (UNECE R157), L3-Verschiebung; ADAS-V4D-Umsatz 2026: 140 Mio. EUR.",
    ],
    datenrows=[
        ["Region", "2023 Volumen Mio. Stk.", "2026 Base", "2028 Base", "CAGR %"],
        ["Europa", "21", "33", "42", "12,1"],
        ["China", "32", "58", "78", "18,4"],
        ["Nordamerika", "18", "26", "32", "10,1"],
        ["Rest of World", "8", "12", "16", "9,2"],
    ],
    implikationen=(
        "Brennhagen sollte den Lead-Customer-Approach Mercedes-Benz und BMW intensiveren und die "
        "Patent-Roadmap im Bereich Sensor-Fusion ausbauen. Die ADAS-V4D-Plattform wird in zwei "
        "Generationen entwickelt (V4D Gen-1 SOP 2024, Gen-2 SOP 2026). Die China-Adressierung "
        "erfolgt selektiv ueber RCN Shanghai und potenzielle Tier-1-Partner (Joyson, Huawei DRIVE)."
    ),
)

szenario_analyse(
    "REA_EV_Marktanalyse_2023.docx",
    "EV-Marktanalyse 2023 – BEV-Hochlauf Europa und China",
    "Strategiepapier – BEV-Wachstumspfad – Vorlage CMO/CFO 2023",
    "Die globale BEV-Penetration steigt 2023 auf ca. 18 % (vs. 13 % 2022). Europa fuehrt mit "
    "26 % Plug-in-Anteil (BEV+PHEV), China mit 33 % NEV-Anteil. Foerderlandschaft in DE und FR "
    "wandelt sich (Kaufpraemie-Stopp DE 12/2023). Brennhagen adressiert den Markt ueber BMS-12 "
    "(Lead VW ID.7, Hyundai) und ECU-900 (Powertrain).",
    szenarien=[
        "Base: Europaeischer BEV-Anteil 2028 = 42 %; BMS-12-Volumen 2028 = 5,8 Mio. Module.",
        "Upside: BEV-Anteil 2028 = 52 % (regulatorischer Push CO2-Flottenziele); BMS-12 = 7,2 Mio.",
        "Downside: Eindellung durch Subventionsabbau / Energiepreise; BEV-Anteil 2028 = 32 %; BMS-12 = 4,1 Mio.",
    ],
    datenrows=[
        ["Region", "BEV-Anteil 2023", "BEV-Anteil 2028 Base", "Volumen 2028 Mio. Fahrz.", "CAGR %"],
        ["Europa", "15 %", "42 %", "8,4", "22"],
        ["China", "24 %", "55 %", "16,2", "20"],
        ["Nordamerika", "8 %", "28 %", "5,1", "26"],
        ["Rest of World", "3 %", "12 %", "3,2", "30"],
    ],
    implikationen=(
        "Die BMS-12-Plattform-Expansion in Heilbronn ist kritisch. Capex-Antrag fuer Linie 5/6 "
        "(SMT + Final-Assembly) wird vorbereitet (12,8 Mio. EUR). Lieferanten-Diversifizierung "
        "(NXP / Infineon / Renesas) verstaerken. China-Strategie ueber RCN Shanghai (CATL-Partnerschaft) "
        "vertiefen."
    ),
)

szenario_analyse(
    "REA_Marktanalyse_China_Automobil_2023_intern.docx",
    "Marktanalyse China-Automobilmarkt 2023",
    "Vertraulich – RCN Shanghai / Strategie Asien – Vorlage CRO Asia (Dr. Tanaka)",
    "Der chinesische Automobilmarkt 2023 ist gepraegt durch Konsolidierung (BYD, Geely, Chery), "
    "schnelle BEV-Penetration (33 % NEV-Anteil) und massive lokale Software-Investitionen "
    "(Huawei, Xiaomi, NIO Banyan, Li Auto). Auslaendische OEMs (VW, BMW, Mercedes-Benz) verlieren "
    "Marktanteile im Premium-NEV-Segment. RCN Shanghai (320 MA) fokussiert auf Vertrieb an lokale "
    "Plattformen und VW China.",
    szenarien=[
        "Base: RCN-Umsatz 2026 = 95 Mio. EUR (CAGR 18 %); Lokalisierungspfad mit CATL.",
        "Upside: Joint Venture mit CATL fuer lokale BMS-Fertigung (Volumen +40 %).",
        "Downside: Geopolitisches Decoupling, Exportkontrollen, Markt-Exit DE-OEMs.",
    ],
    datenrows=[
        ["Segment", "2022 Volumen Mio.", "2023 Schaetzung", "2026 Base Mio.", "Wachstum %"],
        ["NEV gesamt", "6,9", "9,5", "16,2", "70 %"],
        ["ICE", "16,1", "14,2", "11,5", "-19 %"],
        ["Premium NEV", "1,2", "1,8", "3,5", "94 %"],
    ],
    implikationen=(
        "Die China-Strategie erfordert Entscheidungen: (a) Vertiefung Lokalisierung (Capex-Bedarf), "
        "(b) Joint-Venture-Pruefung mit CATL, (c) Decoupling-Stress-Szenario (Rueckzug auf Hong-Kong-Hub). "
        "Vorstand CRO Asia (Dr. Tanaka) wird ab 1.4.2024 zustaendig. Strategy-Review Q4/2024 geplant."
    ),
)


# ── Investorentag Q&A-Protokolle (3 docs) ─────────────────────────────────────
investorentag(
    "REA_Investorentag_2021_QA_Protokoll.docx", 2021, "Frankfurt am Main (Vor-IPO)",
    kernthemen=[
        "Strategie Precision Growth 2021–2025 (CEO Anna Mueller)",
        "Operative Lage / OEE-Status (COO Dr. Thomas Weber)",
        "Finanzplanung 2021–2025 und IPO-Vorbereitung (CFO Laura Bauer)",
        "Technologie-Roadmap BMS / ADAS / Infotainment (CTO Stefan Hoffmann)",
        "ESG-Vorbereitung CSRD und SBTi (CFO)",
    ],
    qa_pairs=[
        "Q1 (Berenberg): Wie hoch ist die Sensitivitaet auf Halbleiterpreise? A: CFO – Materialkosten-Exposure ca. 12 %, Pass-Through-Mechanismus mit OEMs in 70 % der Vertraege.",
        "Q2 (Deutsche Bank): IPO-Window 2022 – Backup-Szenarien? A: CEO – Vorbereitung mit Goldman Sachs, Backup Private Placement / weiteres Bankenkonsortium.",
        "Q3 (BlackRock): EBITDA-Marge 2025 = 15 % – treiber? A: COO – OEE +5 ppt, Materialeffizienz, BMS-12 hoehere Marge als Legacy-ICP.",
        "Q4 (Allianz GI): Kapitalstruktur nach IPO? A: CFO – Net Debt 150–180 Mio., Konsortialkredit 250 Mio. ab 2022.",
        "Q5 (DWS): China-Strategie? A: CEO – RCN als Vertriebshub, Co-Engineering mit lokalen OEMs, Pruefung BMS-JV.",
        "Q6 (Union Investment): Dividendenpolitik post-IPO? A: CFO – Payout 35–40 % vom Konzernergebnis.",
        "Q7 (UBS): Lieferanten-Diversifizierung Halbleiter? A: CTO – Dual-Sourcing-Quote 38 %, Ziel 70 % bis 2024.",
    ],
    datum="22. September 2021",
)

investorentag(
    "REA_Investorentag_2022_QA_Protokoll.docx", 2022, "Frankfurt am Main (Post-IPO)",
    kernthemen=[
        "Erstes Halbjahr Post-IPO – Performance Review",
        "BMS-12 Hochlauf Heilbronn (Lead-Kunde VW ID.7)",
        "ADAS-V4D Engineering-Sample-Lieferungen Mercedes-Benz",
        "Akquisitionen / M&A-Pipeline (Goldman Sachs Mandat)",
        "Capital Markets Day 2023 – Outlook",
    ],
    qa_pairs=[
        "Q1 (Berenberg): IPO-Verwendung Erloes 612 Mio.? A: CFO – ca. 280 Mio. Capex, 180 Mio. Schuldenabbau, 100 Mio. M&A-Reserve, 50 Mio. R&D-Akzeleration.",
        "Q2 (Goldman Sachs): M&A-Pipeline aktiv? A: CEO – Sondierungen in Software / ADAS-Sensorik (Pre-NDA-Phase mit 4 Targets).",
        "Q3 (Fidelity): EBITDA-Guidance 2022? A: CFO – 73 Mio. EBITDA bestaetigt, Upside aus BMS-12-Volumen.",
        "Q4 (DWS): UNECE R155 / R156 Compliance? A: CTO – ISO 21434 in Umsetzung, TARA fuer ICP-3 und ADAS-V4D bis Q1/2024.",
        "Q5 (Capital Group): Aktionaersstruktur post-IPO? A: IR – Brennhagen-Familie 38 %, Streubesitz 58 %, Treasury 4 %.",
        "Q6 (Commerzbank): Margenpfad 2025 – Trigger? A: COO – OEE Hochlauf, Mix-Shift BMS-12, FX-Stabilisierung.",
        "Q7 (Hauck Aufhaeuser): ESG-Reporting Roadmap? A: CFO – CSRD Berichtspflicht GJ 2024, Heubeck als Aktuar bestellt.",
    ],
    datum="15. September 2022",
)

investorentag(
    "REA_Investorentag_2023_QA_Protokoll_20230915.docx", 2023, "Frankfurt am Main",
    kernthemen=[
        "NEXT 2026 – Strategiepapier 2023 Vorstellung",
        "Drei Saeulen: BEV/BMS, ADAS L2-3, Software-as-a-Service",
        "Mittelfristplanung 2024–2028 (Umsatz 1,0 Mrd. EUR Ziel)",
        "ESG / CSRD-Roadmap fuer Berichtspflicht GJ 2024",
        "Vorstandsergaenzung CRO Asia (Dr. Tanaka) ab 1.4.2024",
    ],
    qa_pairs=[
        "Q1 (Berenberg): Software-as-a-Service ARR-Pfad bis 2028? A: CEO/CTO – ARR-Ziel 35 Mio. EUR, Cross-Sell ECU-900 + ICP-3 + ADAS-V4D.",
        "Q2 (Deutsche Bank): Stress-Szenario BEV-Foerderungs-Wegfall? A: CFO – Downside Umsatz 2026 -8 %, Capex-Steuerung mit Trigger-Mechanismus.",
        "Q3 (BlackRock): CTO-Nachfolge (Hoffmann verlaesst 30.6.2024)? A: CEO – Dr. Petra Hollmann (Continental) ab 1.7.2024.",
        "Q4 (Allianz GI): Capital Allocation Framework? A: CFO – Capex / Dividende / M&A klar priorisiert, siehe REA_Capital_Allocation_Framework_2023.",
        "Q5 (DWS): China-Geopolitik / Decoupling-Risiko? A: CRO Asia (Tanaka, ab 1.4.2024) – RCN-Strategy-Review Q4/2024 mit lokalem Partnerschaftsmodell.",
        "Q6 (Union Investment): Refinanzierung Konsortialkredit 2027? A: Treasurer (Pflanzer) – Markt-Sondierung 2025, Sustainability-linked Loan Erweiterung geplant.",
        "Q7 (UBS): Dividende 2024 – Wachstum? A: CFO – Anhebung auf 2,10 EUR/Aktie vorgeschlagen (vorbehaltlich AR/HV-Beschluss).",
    ],
    datum="15. September 2023",
)


# ── Strategie-Memos (8 docs) ─────────────────────────────────────────────────
strategie_memo(
    "REA_Memo_Acquisition_Target_Analyse_2024_WIP.docx",
    "Acquisition Target Analyse 2024",
    "Im Rahmen der NEXT-2026-Strategie hat das Strategy & Corporate Development Office "
    "in Abstimmung mit Goldman Sachs (Frankfurt) eine Long-List potenzieller Akquisitionsziele "
    "im Bereich ADAS-Sensorik und Embedded Software erstellt. Das Memo enthaelt die ersten "
    "Bewertungen und dient als Grundlage fuer Pre-NDA-Sondierungen.",
    "Long-List 12 Targets, davon Short-List 4: (1) ADAS-Software-Spezialist im Raum Stuttgart "
    "(<200 MA, ~30 Mio. EUR Umsatz, EBITDA-Marge ~14 %), (2) Radar-Sensorik-Anbieter (CZ, ~140 MA), "
    "(3) BMS-Software-Boutique (CN, JV-Modell), (4) AUTOSAR-Adaptive-Plattform-Anbieter (NL, "
    "~80 MA). Bewertungsspannen: EV/EBITDA 8–14x.",
    optionen=[
        "Option A: Akquisition Target #1 (ADAS-Software DE) als Bolt-on (50–80 Mio. EUR EV).",
        "Option B: Minority-Investment plus Co-Engineering Target #3 (CN BMS-Software).",
        "Option C: Buy-and-Build mit Target #1 als Plattform plus 2 Tuck-ins (mittelfristig).",
        "Option D: Status quo (organisches Wachstum); Capex statt M&A.",
    ],
    empfehlung=(
        "Empfehlung: Option A (Bolt-on Target #1) priorisieren. Begruendung: hohe strategische "
        "Passung, geringes Integrationsrisiko (gleiche Region, kulturelle Naehe), klarer "
        "Margen-Beitrag in 24 Monaten. Pre-NDA-Phase mit Goldman Sachs starten. Beschlussvorlage "
        "an Aufsichtsrat (Pruefungsausschuss) in der naechsten Sitzung."
    ),
    verfasser="Stefan Richter, CMO/BD",
    datum="28. Februar 2024",
    draft=True,
)

strategie_memo(
    "REA_Memo_Cybersecurity_UNECE_155_156.docx",
    "Cybersecurity Roadmap UNECE R155 / R156",
    "Mit Wirkung zum 1. Juli 2024 sind UNECE R155 (Cybersecurity) und R156 (Software-Updates) "
    "verpflichtend fuer alle Typ-Zulassungen in EU-Mitgliedsstaaten. Brennhagen muss als Tier-1-Zulieferer "
    "die Konformitaet fuer alle aktiven Plattformen (ICP-3, BMS-12, ADAS-V4D, ECU-900) sicherstellen. "
    "Das Memo dokumentiert den Roadmap-Stand und identifiziert Handlungsbedarf.",
    "Status Q1/2024: ISO 21434 (Cybersecurity Engineering) in Umsetzung; TARA (Threat Analysis "
    "and Risk Assessment) fuer ICP-3 und ADAS-V4D in finaler Pruefung; CSMS (Cybersecurity Management "
    "System) durch externe Auditfirma (TUEV Sued) begleitet. OTA-Plattform (BrennhagenOS) ist R156-konform "
    "konzipiert. Kritische Luecke: Lieferantenpool – nur 64 % der Tier-2-Lieferanten haben CSMS.",
    optionen=[
        "Option A: Beschleunigung Lieferanten-Audit-Programm (zusaetzlich 1,2 Mio. EUR Budget 2024).",
        "Option B: Lieferanten-Konsolidierung auf zertifizierte Tier-2 (Risiko: Single-Source).",
        "Option C: Inhouse-Substitution durch RSG fuer kritische Komponenten.",
        "Option D: Verzoegerung Typ-Zulassung neuer Plattformen.",
    ],
    empfehlung=(
        "Empfehlung: Kombination Option A + Option B. Beschleunigtes Audit-Programm (1,2 Mio. EUR "
        "Budget freigeben), gleichzeitig Konsolidierung auf zertifizierte Tier-2-Pool. Beschluss "
        "Vorstand: Freigabe Budget und Mandat an Group Compliance Office (in Abstimmung mit CTO)."
    ),
    verfasser="Stefan Hoffmann, CTO",
    datum="14. Maerz 2024",
)

strategie_memo(
    "REA_Memo_Digital_Manufacturing_Heilbronn.docx",
    "Digital Manufacturing Heilbronn – Strategischer Pfad",
    "Werk Heilbronn (REG) ist das Hauptproduktionsstandort fuer BMS-12 und ICP-3. "
    "Die Digital-Manufacturing-Initiative verbindet Digital Twin, MES-Konsolidierung "
    "(SAP DMC), Predictive Maintenance und Energie-Optimierung. Strategischer Hebel: "
    "OEE +5 ppt, Energiekosten -12 %.",
    "Status Q1/2024: Pilot Linie 4 (BMS-12-SMT) abgeschlossen, OEE +3,2 ppt nachgewiesen. "
    "Roll-out auf Linien 1–3 ab Q2/2024 geplant. Investitionsvolumen 8,5 Mio. EUR ueber 24 Monate. "
    "Integration in Group Performance Management System (GPMS) ab Q3/2024.",
    optionen=[
        "Option A: Vollausbau Heilbronn 2024–2025 (Capex 8,5 Mio. EUR).",
        "Option B: Phased-Approach (Capex 4,2 Mio. EUR 2024, Rest 2025/26).",
        "Option C: Roll-out auch Katowice/Brno (Skaleneffekte, Capex 14 Mio. EUR Gesamt).",
        "Option D: Verschiebung um 12 Monate (Capex-Schutz).",
    ],
    empfehlung=(
        "Empfehlung: Option C (Roll-out alle EU-Werke). Skaleneffekte durch konsolidierte "
        "Software-Plattform und einheitliche KPI-Reporting. Beschluss Vorstand: Capex-Antrag "
        "14 Mio. EUR (gestaffelt 2024/25) freigeben. Begleitung durch COO."
    ),
    verfasser="Dr. Thomas Weber, COO",
    datum="14. Februar 2024",
)

strategie_memo(
    "REA_Memo_EV_Wachstumsstrategie_2023.docx",
    "EV-Wachstumsstrategie 2023–2028",
    "Der BEV-Hochlauf bei den OEM-Plattformen VW MEB+, Mercedes-Benz MMA, BMW Neue Klasse, "
    "Stellantis STLA und Hyundai E-GMP eroeffnet fuer Brennhagen signifikante Wachstumschancen. "
    "Das Memo skizziert den Wachstumspfad fuer BMS-12, ECU-900 und ergaenzende Module.",
    "BMS-12-Plattform-Hochlauf: 2024 = 2,2 Mio. Module, 2026 = 4,2 Mio., 2028 = 5,8 Mio. "
    "Capex-Bedarf Heilbronn: 12,8 Mio. EUR fuer Linien 5/6. Lead-Customer-Pipeline: VW ID.7, "
    "ID.Buzz, Hyundai Ioniq 6/7, Mercedes-Benz EQS-Lift (BMS-12.2 800V). ECU-900-Hochlauf: "
    "Volumen 2024 = 1,8 Mio., 2028 = 3,5 Mio.",
    optionen=[
        "Option A: Aggressiver Capex-Pfad (15 Mio. EUR Heilbronn + 4,8 Katowice 2024–2025).",
        "Option B: Konservativer Pfad mit Trigger-Mechanismus an OEM-Forecasts.",
        "Option C: JV-Pruefung mit OEM (VW PowerCo) fuer Solid-State-BMS.",
        "Option D: Inorganic Boost via M&A (Target ADAS-/BMS-Software-Spezialist).",
    ],
    empfehlung=(
        "Empfehlung: Option A + Option C. Aggressiver Capex-Pfad fuer kurzfristigen Hochlauf, "
        "parallel JV-Sondierung mit VW PowerCo fuer 2027+ Solid-State-BMS. Beschluss Vorstand: "
        "Capex-Antrag und JV-Mandat freigeben."
    ),
    verfasser="Stefan Richter, CMO/BD",
    datum="14. September 2023",
)

strategie_memo(
    "REA_Memo_ISO21434_Zertifizierung_Roadmap.docx",
    "ISO 21434 Zertifizierung Roadmap",
    "ISO 21434:2021 (Road Vehicles – Cybersecurity Engineering) ist die Grundlage fuer "
    "UNECE R155-Konformitaet. Brennhagen fuehrt das Engineering-Verfahren konzernweit ein. "
    "Das Memo beschreibt Status, Meilensteine und Ressourcenbedarf.",
    "Status Q1/2024: Engineering-Prozesse in RSG (Muenchen) auf Level 2 (Pre-Audit); "
    "TARA fuer ICP-3 und ADAS-V4D abgeschlossen; BMS-12 in Bearbeitung. CSMS-Audit durch "
    "TUEV Sued geplant Q3/2024. Schulungsprogramm fuer 480 Engineers laeuft (E-Learning + "
    "Praesenz). Investitionsbedarf 2024: 2,1 Mio. EUR.",
    optionen=[
        "Option A: Vollausrollung 2024 (alle Plattformen, alle Werke).",
        "Option B: Plattform-priorisiert (zuerst BMS-12, dann ADAS-V4D, danach ICP-3).",
        "Option C: Auslagerung Audit-Vorbereitung an externes Beratungshaus.",
    ],
    empfehlung=(
        "Empfehlung: Option B (priorisierte Ausrollung). Begruendung: Volumen-Drittel-Logik – "
        "BMS-12 wegen OEM-Pflicht 7/2024 priorisieren. Externe Begleitung TUEV Sued + EY beibehalten. "
        "Beschluss Vorstand: Roadmap bestaetigen, Budget 2024 freigeben."
    ),
    verfasser="Stefan Hoffmann, CTO",
    datum="14. Februar 2024",
)

strategie_memo(
    "REA_Memo_Lieferantendiversifizierung_Halbleiter.docx",
    "Lieferantendiversifizierung Halbleiter",
    "Die Halbleiter-Allokation 2021–2023 hat strukturelle Risiken im Konzern aufgezeigt. "
    "Das Memo beschreibt die Strategie zur Diversifizierung und Dual-Sourcing in den "
    "kritischen Bauteilgruppen (Microcontroller, Power-Management, Sensoren).",
    "Status: Dual-Sourcing-Quote Q1/2024 = 52 % (Ziel 70 % Ende 2024). Kritische Single-Sources: "
    "NXP S32G fuer ECU-900, Renesas RH850 fuer ICP-3, Infineon AURIX TC3xx fuer BMS-12. "
    "Qualifikations-Aufwand fuer Alternative: 14–18 Monate je Bauteil. Investitionsvolumen "
    "Qualifizierung: 3,2 Mio. EUR ueber 2 Jahre.",
    optionen=[
        "Option A: Aggressive Dual-Sourcing-Strategie (Quote 80 % bis Mitte 2025).",
        "Option B: Risikobasierte Priorisierung (kritische Single-Sources zuerst).",
        "Option C: Strategische Vorratsbildung (Buffer-Stock 6 Monate fuer Top-15 Bauteile).",
        "Option D: Kombination B + C (priorisierte Dual-Sources + Buffer).",
    ],
    empfehlung=(
        "Empfehlung: Option D (Kombination). Begruendung: balanceiert Capex-Belastung und Risiko. "
        "Buffer-Stock-Aufbau finanziert durch Konsortialkredit-RCF. Beschluss Vorstand: Mandat an "
        "Group Procurement und Treasury."
    ),
    verfasser="Dr. Thomas Weber, COO",
    datum="14. Maerz 2024",
)

strategie_memo(
    "REA_Memo_Nearshoring_Marokko_2023.docx",
    "Nearshoring Marokko – Decision Gate Vorbereitung",
    "Die Pruefung eines Nearshoring-Standortes in Marokko (Tanger Free Zone) wurde als Antwort "
    "auf die China-Abhaengigkeit und steigende Lohnkosten in EU-Standorten initiiert. Das Memo "
    "fasst die Vor-Pruefung zusammen und bereitet den Decision Gate Q4/2024 vor.",
    "Standortbewertung Tanger Free Zone: gute Infrastruktur (Hafen Tanger-Med), niedrige Lohnkosten "
    "(ca. 35 % von Heilbronn), gute Anbindung an EU-Werke (Faehrverbindung Algeciras). "
    "Investitionsvolumen geschaetzt 45–55 Mio. EUR fuer SMT-Werk mit 2 Linien (initial ~250 MA). "
    "Risiken: politische Stabilitaet, Lieferanten-Oekosystem im Aufbau, Qualifikationsniveau.",
    optionen=[
        "Option A: Greenfield-Werk Tanger (Vollausbau).",
        "Option B: Joint-Venture mit lokalem Partner (Risiko-Sharing).",
        "Option C: Auslagerung an EMS-Dienstleister (Foxconn, Jabil) – kein eigenes Werk.",
        "Option D: Kein Nearshoring – Verstaerkung Katowice/Brno.",
    ],
    empfehlung=(
        "Empfehlung: Option B (Joint-Venture). Begruendung: balanceiert Investition, Risiko und "
        "Marktzugang. Sondierung mit zwei potenziellen Partnern initiieren. Decision Gate Q4/2024."
    ),
    verfasser="Dr. Thomas Weber, COO",
    datum="14. September 2023",
)

strategie_memo(
    "REA_Memo_Software_Defined_Vehicle_2024.docx",
    "Software-Defined Vehicle – Plattformstrategie",
    "Software-Defined Vehicle (SDV) ist der dominante OEM-Trend 2024–2030. Brennhagen positioniert "
    "BrennhagenOS als HAL-/Middleware-Schicht und Service-Plattform. Das Memo skizziert die "
    "Plattformstrategie und Investitionsbedarf.",
    "BrennhagenOS-Vision: Container-faehiges Middleware (OCI), AUTOSAR Adaptive-konform, "
    "DDS-Kommunikation, OTA-Integration (UNECE R156). Backend: AWS EU + Konzern-RZ Stuttgart "
    "(Hybrid Cloud). Geschaeftsmodell: Subscription-/Pay-per-Update. ARR-Ziel 2028: 35 Mio. EUR. "
    "Investitionsbedarf RSG: 22 Mio. EUR ueber 4 Jahre + 60 FTE Recruitment.",
    optionen=[
        "Option A: Eigenentwicklung Vollstack (Capex 22 Mio. EUR, FTE +60).",
        "Option B: Partnerschaft Elektrobit / Vector / ETAS (geringere Capex, weniger Differenzierung).",
        "Option C: Akquisition AUTOSAR-Adaptive-Boutique (M&A 40–60 Mio. EUR).",
        "Option D: Mix-Modell: Eigene Kern-Layer + Partnerschaft fuer Tools.",
    ],
    empfehlung=(
        "Empfehlung: Option D (Mix-Modell). Begruendung: eigene Kern-Differenzierung + Tool-Pragmatismus. "
        "Capex und Recruitment-Antrag in MFP-Zyklus 2024–2028 aufnehmen."
    ),
    verfasser="Stefan Hoffmann, CTO",
    datum="14. Maerz 2024",
)

strategie_memo(
    "REA_Memo_TISAX_Level3_Roadmap.docx",
    "TISAX Level 3 Roadmap",
    "TISAX (Trusted Information Security Assessment Exchange) ist OEM-Anforderung fuer "
    "Informationssicherheit. Brennhagen hat TISAX Level 2 in REG, RSG, RPL, RCZ, RHU. Premium-OEMs "
    "(BMW, Mercedes-Benz, Audi) fordern Level 3 ab 2025. Das Memo beschreibt die Roadmap.",
    "Status Q1/2024: TISAX Level 2 in 5 Werken; Level 3 erfordert zusaetzliche Sicherheits-Audits "
    "(z.B. Hochsicherheits-Areale fuer Prototypen, erweiterte Pen-Tests). Investitionsbedarf "
    "Gesamtkonzern: 1,8 Mio. EUR (Audit + Infrastruktur). Externer Auditor: TUEV Hessen.",
    optionen=[
        "Option A: Vollausrollung Level 3 in allen Werken bis Q3/2025.",
        "Option B: Priorisierung RSG Muenchen (Prototypen-Werk) und Heilbronn (BMS-12 Prototypen).",
        "Option C: Konsolidierung Prototypen-Aktivitaeten in RSG (Single Site Level 3).",
    ],
    empfehlung=(
        "Empfehlung: Option B (priorisierte Ausrollung). RSG und Heilbronn zuerst, Folge-Werke "
        "in 2026. Beschluss Vorstand: Roadmap und Budget genehmigen. Verantwortung Group CISO."
    ),
    verfasser="Stefan Hoffmann, CTO",
    datum="14. Februar 2024",
)


# ── Capital Allocation Framework + STE Lobesbriefe + sonstige ─────────────────
generic_strategie(
    "REA_Capital_Allocation_Framework_2023.docx",
    "Capital Allocation Framework 2023",
    "Konzern-Capital-Allocation-Richtlinie – Vorlage Aufsichtsrat / Pruefungsausschuss",
    [
        ("Zielsetzung und Anwendungsbereich",
         "Das Capital Allocation Framework (CAF) der Brennhagen Elektronik AG definiert verbindliche "
         "Grundsaetze fuer die Allokation des Konzernkapitals auf Capex, M&A, Dividende und "
         "Schuldentilgung. Es gilt fuer alle Investitionsentscheidungen oberhalb von 1,0 Mio. EUR "
         "und ist verbindliche Vorlage in jedem Investitionsantrag. Verantwortlich: CFO Laura Bauer; "
         "operative Steuerung: Group Controlling (Florian Maier)."),
        ("Hierarchie der Mittelverwendung",
         ("list", [
             "Stufe 1 – Maintenance Capex (Erhalt operativer Faehigkeiten, Compliance, Sicherheit). Pflichtinvestitionen.",
             "Stufe 2 – Growth Capex (BMS-12-Hochlauf, ADAS-V4D, BrennhagenOS, neue Werks-Linien).",
             "Stufe 3 – Dividende (Payout-Range 35–45 % vom Konzernergebnis nach Steuern, Stabilitaet ueber Konjunkturzyklen).",
             "Stufe 4 – M&A / strategische Akquisitionen (Bolt-on, Tuck-in, transformativ).",
             "Stufe 5 – Schuldentilgung / Buyback (Optimierung Net-Debt-Profil, ggf. Aktienrueckkaeufe nach AR-Beschluss und HV-Ermaechtigung).",
         ])),
        ("Hurdle Rates und Bewertungskriterien",
         ("list", [
             "WACC Konzern: 8,4 % (Stichtag 30.6.2023), Updates jaehrlich durch Treasury.",
             "Hurdle Rate Maintenance Capex: WACC + 1 ppt.",
             "Hurdle Rate Growth Capex: WACC + 3 ppt.",
             "Hurdle Rate M&A: WACC + 5 ppt (inkl. Synergy-Hurdle).",
             "Payback-Period Growth Capex: <= 5 Jahre, Maintenance <= 7 Jahre.",
             "Mindest-IRR M&A: 15 % (post-Synergie, post-Integration).",
         ])),
        ("Governance und Freigaben",
         ("list", [
             "Investitionen <1 Mio. EUR: Bereichsleiter / Werkleiter.",
             "Investitionen 1–5 Mio. EUR: CFO + zustaendiger Vorstand.",
             "Investitionen 5–25 Mio. EUR: Vorstand komplett.",
             "Investitionen >25 Mio. EUR oder M&A: Aufsichtsrats-Zustimmung (Pruefungsausschuss).",
             "Pflichtberichterstattung quartalsweise an Aufsichtsrat (Pruefungsausschuss).",
         ])),
        ("Reporting und Monitoring",
         "Quartalsweises Reporting der Capex-Pipeline (Pre-Approval, Approved, In Execution, Closed) "
         "an den Pruefungsausschuss. Jaehrliche Capital-Allocation-Pruefung im Strategie-Zyklus. "
         "Post-Investment-Reviews fuer alle Investitionen >5 Mio. EUR nach 24 Monaten. Pruefung "
         "durch Internal Audit (CAE Andreas Buehler)."),
        ("Inkrafttreten",
         signatures("Laura Bauer", "CFO", R["name"],
                    "Anna Mueller", "CEO", R["name"],
                    place="Stuttgart", date_str_="14. Maerz 2023")),
    ],
    datum="14. Maerz 2023",
)

generic_strategie(
    "REA_STE_Lobesbriefe_Top_Supplier_2022.docx",
    "Lobesbriefe Top-Supplier 2022 – Supplier of the Year Awards",
    "Anerkennungsbriefe an strategische Lieferanten (STE = Supplier of the Year) – Vorstand",
    [
        ("Anlass und Selektion",
         "Im Rahmen des jaehrlichen Supplier-of-the-Year-Programms wuerdigt der Vorstand der "
         "Brennhagen Elektronik AG die strategisch wichtigsten Lieferanten der Konzerngesellschaften. "
         "Bewertet werden Qualitaet, On-Time-Delivery, Innovation, ESG-Performance und "
         "Kooperationsbereitschaft. Auswahl durch Group Procurement (Leitung Markus Pflanzer "
         "in Funktion Treasurer mit Supplier-Sponsorship) und die Werkleitungen."),
        ("Geehrte Lieferanten 2022", ("list", [
            "Lieferant A – NXP Semiconductors Germany GmbH (Hamburg) – Kategorie Halbleiter MCU",
            "Lieferant B – Infineon Technologies AG (Neubiberg) – Kategorie Halbleiter Power/BMS",
            "Lieferant C – TDK-Lambda Germany GmbH (Achern) – Kategorie Power-Komponenten",
            "Lieferant D – TE Connectivity (Bensheim) – Kategorie Steckverbinder",
            "Lieferant E – Bossard AG (Zug, CH) – Kategorie Verbindungstechnik",
            "Lieferant F – Murrelektronik GmbH (Oppenweiler) – Kategorie Schalt-/Steuerungskomponenten",
        ])),
        ("Mustertext Anerkennungsschreiben",
         "Sehr geehrte Damen und Herren,\n\nim Namen des Vorstandes der Brennhagen Elektronik AG "
         "moechten wir Ihnen unsere Anerkennung fuer die hervorragende Zusammenarbeit im "
         "Geschaeftsjahr 2022 aussprechen. Mit einer On-Time-Delivery-Quote von 99,2 % und einer "
         "Reklamationsquote unter 50 ppm haben Sie als Schluessellieferant einen wesentlichen "
         "Beitrag zur Produktionsstabilitaet unserer Konzerngesellschaften (REG Heilbronn, RPL "
         "Katowice, RCZ Brno, RHU Gyoer) geleistet.\n\nWir freuen uns, Sie als Supplier of the Year "
         "2022 in der Kategorie [Kategorie] auszuzeichnen. Diese Auszeichnung wird im Rahmen des "
         "Supplier Days am 12. Maerz 2023 in Stuttgart offiziell verliehen.\n\nMit freundlichen Gruessen\n\n"
         "Dr. Thomas Weber                                Anna Mueller\n"
         "COO                                                              CEO"),
        ("Naechste Schritte",
         ("list", [
             "Supplier Day 2023 am 12. Maerz 2023, Stuttgart (Vaihinger Strasse 120).",
             "Aushaendigung der Awards in feierlichem Rahmen durch CEO und COO.",
             "Pressemitteilung mit Einwilligung der Lieferanten.",
             "Aufnahme in jaehrlichen Supplier-Sustainability-Bericht.",
         ])),
    ],
    datum="2022",
)


# ── Sonstige Misfit-Docs (laut Brief: ~5 % Wrong-Folder-Realismus) ─────────────
generic_strategie(
    "MA_Management_Meeting_2023_020.docx",
    "Management Meeting #20 / 2023",
    "Erweitertes Management-Meeting Konzern – Protokoll",
    [
        ("Sitzungsdaten",
         "Datum: 18. Oktober 2023, 9:00–16:30 Uhr. Ort: Vaihinger Strasse 120, 70567 Stuttgart, "
         "Raum »Bodensee« (4. OG). Teilnehmer: Vorstand komplett (Mueller, Bauer, Weber, Hoffmann, "
         "Richter), erweiterte Management-Runde (Werkleitungen REG, RSG, RPL, RCZ, RHU, Country "
         "Manager RCN, Group Treasurer Pflanzer, Group Controller Maier, CAE Buehler, "
         "Group HR Director). Schriftfuehrerin: Dr. Veronika Steiner."),
        ("Themen",
         ("list", [
             "Strategie NEXT 2026 – Update Q3 (CEO).",
             "Operative Lage Werke – OEE / Personal / Qualitaet (Werkleiter Runde).",
             "Halbjahres-Forecast und Mittelfristplanung 2024–2028 (CFO).",
             "Technologie-Roadmap – BMS-12.2, ADAS-V4D Gen2, BrennhagenOS (CTO).",
             "OEM-Pipeline und Account-Status (CMO/BD).",
             "Compliance / Cybersecurity / CSRD-Vorbereitung (Group Compliance).",
             "M&A-Pipeline (CEO + Goldman Sachs Update).",
         ])),
        ("Wesentliche Beschluesse / Action Items",
         ("list", [
             "AI #2023-20-01: BMS-12.2-Hochlauf-Plan bis Q1/2024 finalisieren (verantwortlich COO).",
             "AI #2023-20-02: CSRD-Datenmodell bis Q4/2023 implementieren (verantwortlich CFO).",
             "AI #2023-20-03: RSG-Recruitment 60 FTE in 2024 starten (verantwortlich CTO / HR).",
             "AI #2023-20-04: Capex-Antrag Linie 5/6 Heilbronn an Aufsichtsrat (verantwortlich CFO).",
         ])),
        ("Naechste Sitzung",
         "Naechstes erweitertes Management-Meeting: 17. Januar 2024, 9:00 Uhr, Stuttgart. "
         "Strategie-Klausur Vorstand + Werkleitungen: 22.–23. Februar 2024, Hotel Schloss Solitude."),
    ],
    datum="18. Oktober 2023",
)

generic_strategie(
    "MR_RSG_Managementbewertung_2022.docx",
    "Managementbewertung RSG 2022 (ISO 9001 / IATF 16949 / ASPICE)",
    "Brennhagen Software GmbH – Jaehrliche Managementbewertung Geschaeftsjahr 2022",
    [
        ("Anlass und Geltungsbereich",
         "Die Managementbewertung (Management Review) erfolgt gemaess ISO 9001:2015 Abschnitt 9.3 "
         "sowie IATF 16949 und beruecksichtigt die ASPICE-spezifischen Aspekte des "
         "RSG-Entwicklungsprozesses (Muenchen). Sie wurde durch Werkleiter Dr. Klaus Kessler "
         "geleitet, unter Beteiligung der Q-Leitung (Markus Schneider, RSG) und der Lead Developer "
         "(Lars Wittmann). Konzernseitig vertreten durch CTO Stefan Hoffmann."),
        ("Eingangsgroessen",
         ("list", [
             "Audit-Ergebnisse 2022 (intern: 1 major, 8 minor; extern TUEV Sued: 0 major, 4 minor).",
             "Kundenfeedback (BMW, Mercedes-Benz, VW) – ueberwiegend positiv, Verbesserungsbedarf Time-to-Market.",
             "Prozess-Leistungskennzahlen (Code-Quality, MTTR, Defect Density).",
             "Status Korrektur- und Vorbeugungsmassnahmen (CAPA).",
             "Massnahmen aus letzter Managementbewertung 2021.",
             "ASPICE-Level-Status (aktuell Level 2, Roadmap Level 3 fuer Q4/2024).",
         ])),
        ("Bewertung und Beschluesse",
         ("list", [
             "Beschluss 2022-MR-01: ASPICE-Level-3-Vorbereitung Budget 480 TEUR genehmigt.",
             "Beschluss 2022-MR-02: Personalaufbau 12 FTE 2023 (Embedded-Software, ASPICE-Spezialisten).",
             "Beschluss 2022-MR-03: Test-Automation-Plattform-Erneuerung 220 TEUR (CI/CD-Tooling).",
             "Beschluss 2022-MR-04: TISAX-Level-3-Vorbereitung starten (RSG als Prototypen-Standort).",
             "Beschluss 2022-MR-05: ISO 21434-Implementierung priorisieren (Cybersecurity).",
         ])),
        ("Ergebnis Managementbewertung",
         "Das Qualitaetsmanagementsystem (QMS) der RSG ist insgesamt wirksam und angemessen. "
         "Wesentliche Verbesserungspotenziale liegen in den Bereichen Time-to-Market, "
         "Test-Automation und Cybersecurity-Reife. Die ASPICE-Level-3-Roadmap ist auf Plan. "
         "Naechste Managementbewertung: Februar 2024."),
        ("Freigabe",
         signatures("Dr. Klaus Kessler", "Werkleiter RSG", "Brennhagen Software GmbH",
                    "Stefan Hoffmann", "CTO", R["name"],
                    place="Muenchen", date_str_="22. Februar 2023")),
    ],
    datum="22. Februar 2023",
)

generic_strategie(
    "REA_INF_Lieferantenaudit_2023_Q3.docx",
    "Lieferantenaudit Q3/2023 – Infineon Technologies AG",
    "INF / VDA 6.3 Lieferanten-Prozess-Audit – Auswertung Konzern-Procurement",
    [
        ("Audit-Daten",
         "Auditiertes Unternehmen: Infineon Technologies AG, Werk Regensburg. Audit-Datum: "
         "12.–14. September 2023. Audit-Standard: VDA 6.3 Prozess-Audit (P5 / P6 / P7). "
         "Audit-Team Brennhagen: Sabine Brand (Lead Auditor, REG Heilbronn), Markus Schneider (RSG), "
         "Hans-Juergen Bohlen (Group Procurement). Auditiert wurden die Linien fuer AURIX TC3xx "
         "und Power-MOSFETs (BMS-12-relevant)."),
        ("Auditbefund",
         ("list", [
             "Bewertung gesamt: 92,3 Punkte (Stufe A). Keine major non-conformities.",
             "P5 Prozess-Stabilitaet: 94 Punkte – sehr gute Cpk-Werte (alle >1,67).",
             "P6 Kundenbetreuung / Liefertreue: 90 Punkte – OTD 98,7 %; 2 minor (Forecast-Quality).",
             "P7 Qualifizierung Personal: 92 Punkte – sehr gutes Trainings-System.",
             "Cybersecurity: ISO 27001 zertifiziert, kein Befund.",
             "ESG: Sustainability-Bericht vorhanden, SBTi-Commitment auf 1,5 Grad-Pfad.",
         ])),
        ("Massnahmen Lieferant",
         ("list", [
             "M-INF-2023-Q3-01: Forecast-Quality (Rolling 12-Months) verbessern – Mitarbeiter-Schulung Q4/2023.",
             "M-INF-2023-Q3-02: Quarterly Business Review (QBR) mit Brennhagen Procurement einfuehren.",
             "M-INF-2023-Q3-03: Detaillierte Allocation-Letter bei Engpaessen.",
         ])),
        ("Konsequenzen fuer Brennhagen",
         "Infineon bleibt strategischer Top-Lieferant in Kategorie A. Pruefung Erweiterung "
         "Single-Source AURIX TC3xx → AURIX TC4xx (Dual-Source mit NXP S32G) im Rahmen der "
         "Lieferanten-Diversifizierungs-Strategie (siehe Memo Lieferantendiversifizierung Halbleiter). "
         "Naechstes Audit Q3/2024."),
        ("Freigabe",
         signatures("Sabine Brand", "Lead Auditor Q-Leitung REG", "Brennhagen Elektronik GmbH",
                    "Markus Pflanzer", "Group Treasurer / Procurement Sponsor", R["name"],
                    place="Regensburg", date_str_="14. September 2023")),
    ],
    datum="14. September 2023",
)

generic_strategie(
    "REA_MBZ_Qualitaetsvereinbarung_2022.docx",
    "Qualitaetssicherungsvereinbarung Mercedes-Benz Group AG / Brennhagen 2022",
    "MBZ – Quality Assurance Agreement (QAA) – Vertraulich",
    [
        ("Vertragsparteien und Geltungsbereich",
         "Diese Qualitaetssicherungsvereinbarung (QSV) wird abgeschlossen zwischen der "
         "Mercedes-Benz Group AG, Mercedesstrasse 120, 70372 Stuttgart (»MBZ«), und der "
         "Brennhagen Elektronik AG, Vaihinger Strasse 120, 70567 Stuttgart (»REA«) bzw. den "
         "konzernverbundenen Lieferanten REG (Heilbronn) und RSG (Muenchen). Sie gilt fuer "
         "alle Lieferungen der Produkte ADAS-V4D, ICP-3, BMS-12 (Mercedes-Benz EQS / MMA) sowie "
         "ECU-900 (Mercedes-Benz NCV Vito-Familie)."),
        ("Qualitaetsanforderungen",
         ("list", [
             "Lieferqualitaet: ppm-Ziel <= 25 ppm rollierender 12-Monats-Schnitt.",
             "OTD (On-Time-Delivery): >= 99,5 %.",
             "Erstmusterpruefung gemaess MBN 10448 / VDA Band 2 (PPAP-aequivalent).",
             "Prozessfaehigkeit: Cpk >= 1,67 fuer kritische Merkmale.",
             "Audit-Recht MBZ jaehrlich (mit 4 Wochen Frist).",
             "TISAX Level 2 / 3 Pflicht in Prototypen-Werken.",
             "Cybersecurity gem. ISO 21434 fuer relevante Steuergeraete.",
         ])),
        ("Reklamation und 8D-Prozess",
         "REA verpflichtet sich zur Bearbeitung von Reklamationen nach VDA-Standard 8D. "
         "Erstantwort 24h, Containment 48h, Root-Cause-Analyse 10 Werktage, finaler 8D-Report "
         "20 Werktage. Eskalationsstufen: Lieferant-QM (Sabine Brand, REG) → Werkleitung → "
         "Group Quality → CTO (Stefan Hoffmann). MBZ-seitige Eskalation: SQM-Kontakt → "
         "Bereichsleitung Qualitaet → Mercedes-Benz Cars."),
        ("Pflichten und Haftung",
         ("list", [
             "Rueckruf-Beteiligung gem. Produkthaftungsgesetz §§ 1 ff. ProdHaftG.",
             "D&O-Versicherungspflicht (Allianz GCS, 50 Mio. EUR Versicherungssumme).",
             "Lieferanten-Selbstaudit jaehrlich, MBZ-Audit nach Bedarf.",
             "Konsignations-/Sicherheitsbestaende gem. separater Logistikvereinbarung.",
             "Geheimhaltung gem. separatem NDA.",
         ])),
        ("Laufzeit und Aenderungen",
         "Laufzeit: 1. Januar 2022 bis 31. Dezember 2027 (5 Jahre). Verlaengerung um jeweils "
         "12 Monate bei beidseitiger Bestaetigung. Aenderungen beduerfen der Schriftform. "
         "Anwendbares Recht: deutsches Recht ohne UN-Kaufrecht. Gerichtsstand: Stuttgart."),
        ("Unterschriften",
         signatures("Stefan Hoffmann", "CTO", R["name"],
                    "[MBZ Procurement Lead]", "Vice President SQM", "Mercedes-Benz Group AG",
                    place="Stuttgart", date_str_="14. Januar 2022")),
    ],
    datum="14. Januar 2022",
)

generic_strategie(
    "CN_RCN_Umweltbericht_2023.docx",
    "Umweltbericht RCN Shanghai 2023",
    "Brennhagen (Shanghai) Co. Ltd. – Annual Environmental Report 2023 (gem. lokalen Vorschriften + Konzern-ESG)",
    [
        ("Berichtsgegenstand",
         "Dieser Umweltbericht erfasst die Umweltkennzahlen der Brennhagen (Shanghai) Co. Ltd. (RCN) "
         "fuer das Geschaeftsjahr 2023. RCN ist die Vertriebsgesellschaft des Brennhagen-Konzerns in China "
         "(Sitz: Pudong, Shanghai; ~320 MA). Es werden Energieverbrauch, Wasser, Abfall und Mobilitaet "
         "berichtet. Der Bericht erfuellt die Anforderungen der chinesischen Umweltbehoerde (MEE) "
         "sowie der Konzern-CSRD-Datensammlung (ab GJ 2024 berichtspflichtig)."),
        ("Kennzahlen 2023",
         [["Kategorie", "Einheit", "2022", "2023", "Veraenderung"],
          ["Stromverbrauch", "MWh", "2.140", "2.080", "-2,8 %"],
          ["Davon erneuerbar", "%", "32 %", "48 %", "+16 ppt"],
          ["Erdgas", "MWh", "85", "70", "-17,6 %"],
          ["Wasser", "m³", "5.420", "5.180", "-4,4 %"],
          ["Abfall gesamt", "t", "82", "78", "-4,9 %"],
          ["Recyclingquote", "%", "78", "84", "+6 ppt"],
          ["CO2-Emissionen Scope 1", "t CO2e", "18", "15", "-16,7 %"],
          ["CO2-Emissionen Scope 2 (Location)", "t CO2e", "1.450", "1.380", "-4,8 %"]],
        ),
        ("Massnahmen 2023",
         ("list", [
             "Stromtarif-Umstellung auf Green Tariff in Pudong (+16 ppt erneuerbar).",
             "LED-Beleuchtung im Bueroflaechen-Retrofit (Ersparnis ca. 120 MWh/Jahr).",
             "Hybrid-Dienstwagenflotte – 12 von 24 PKW elektrifiziert.",
             "Recycling-Programm fuer Verpackungsmaterialien (Karton, Holz).",
             "Mitarbeiter-Schulung Umweltschutz (jaehrlich, 95 % Teilnehmerquote).",
         ])),
        ("Ausblick 2024",
         ("list", [
             "Ziel Strombezug 60 % erneuerbar.",
             "Reduktion Scope-2-Emissionen um -8 %.",
             "Mobilitaetsbudget statt Dienstwagen pruefen.",
             "Integration in Konzern-CSRD-Reporting.",
         ])),
        ("Freigabe",
         signatures("Zhang Hao", "Country Manager", "Brennhagen (Shanghai) Co. Ltd.",
                    "Liang Wei", "Finance Manager / ESG-Lead RCN", "Brennhagen (Shanghai) Co. Ltd.",
                    place="Shanghai", date_str_="14. Februar 2024")),
    ],
    datum="14. Februar 2024",
)

# Misfit-Docs: Projekt-/Test-/IC-Rechnungen aus anderen Bereichen
generic_strategie(
    "PRJ-2024-001_Gate_G1_Konzept_ECU-1000_Concept_Study.docx",
    "Stage-Gate G1: Konzept-Review ECU-1000",
    "Projekt PRJ-2024-001 – Concept Study Powertrain-ECU der naechsten Generation (ECU-1000)",
    [
        ("Projekt-Kontext",
         "Das Projekt PRJ-2024-001 fuehrt die Konzeptstudie fuer die naechste Generation der "
         "Powertrain-ECU (Arbeitstitel »ECU-1000«) durch. Ziel: Nachfolger der ECU-900 ab SOP "
         "Q4/2026, Skalierung auf MEB+/STLA-Plattformen, ASPICE-Level-3-konform. Lead Engineer: "
         "Lars Wittmann (RSG). Sponsor: CTO Stefan Hoffmann."),
        ("Gate-G1-Pruefung",
         ("list", [
             "Anforderungsklaerung mit OEM (VW, Stellantis): erfuellt.",
             "Marktanalyse / Volumenprognose: erfuellt (TAM 1,8 Mrd. EUR 2027–2030).",
             "Technische Machbarkeit Microcontroller-Auswahl (NXP S32G3 / Infineon AURIX TC4xx): erfuellt.",
             "Patentlandkarte und Freedom-to-Operate-Pruefung: laufend (Abschluss Q2/2024).",
             "Capex-Schaetzung (Pilot + Linie): 22 Mio. EUR ueber 30 Monate.",
             "Business-Case IRR: 16,8 % (ueber Hurdle 11,4 %).",
         ])),
        ("Beschluss Gate G1",
         "Das Gate G1 wird unter Auflagen freigegeben. Auflagen: (a) Abschluss Patent-Pruefung "
         "Q2/2024; (b) OEM-LOI von mindestens 2 Lead-Customers (VW + Stellantis) bis Gate G2; "
         "(c) Detail-Capex-Antrag mit Lieferanten-Quotes bis Gate G2 (Q3/2024). Entscheider: "
         "Vorstand komplett (CEO/CFO/COO/CTO)."),
        ("Naechste Schritte (G2-Vorbereitung)",
         ("list", [
             "Detail-Architektur-Spec mit ASPICE Level 3 in RSG.",
             "Lieferanten-Sondierung MCU / Power-Devices.",
             "OEM-Lead-Customer-Workshops VW (Wolfsburg), Stellantis (Trnava).",
             "Gate G2 Termin: 15. November 2024.",
         ])),
        ("Freigabe",
         signatures("Lars Wittmann", "Lead Engineer RSG", "Brennhagen Software GmbH",
                    "Stefan Hoffmann", "CTO / Sponsor", R["name"],
                    place="Muenchen", date_str_="14. Maerz 2024")),
    ],
    datum="14. Maerz 2024",
)

generic_strategie(
    "PRJ-2024-004_Testbericht_Funktionstest_EOL_LkSG_Supply_Chain_Au.docx",
    "Testbericht Funktionstest EOL – Projekt PRJ-2024-004 (LkSG Supply-Chain-Audit-Tool)",
    "Internes Tool – End-of-Line-Pruefstand fuer Lieferanten-Auditdaten (LkSG-Konformitaet)",
    [
        ("Projekt-Kontext",
         "Das Projekt PRJ-2024-004 entwickelt ein End-of-Line-Pruefstand-Tool fuer die LkSG-Pflichten "
         "(Lieferkettensorgfaltspflichtengesetz, gueltig 2023+). Das Tool wird in Heilbronn entwickelt "
         "und konzernweit ausgerollt. Lead: Sabine Brand (Q-Leitung REG). Sponsor: Group Compliance."),
        ("Pruefumfang",
         ("list", [
             "Datenimport von Lieferanten-Selbstauskuenften (>800 Lieferanten Tier-1 + Tier-2).",
             "Risiko-Scoring nach LkSG-Risikokriterien (Land, Branche, Compliance-Historie).",
             "Audit-Trail / Versionierung fuer Behoerden-Anfragen (BAFA).",
             "Schnittstellen zu SAP S/4HANA Sourcing, Group Compliance Portal.",
             "Reporting an Aufsichtsrats-Pruefungsausschuss (quartalsweise).",
         ])),
        ("Testergebnisse",
         ("list", [
             "Funktionstest: 98 von 102 Anforderungen erfuellt (96,1 %).",
             "Performance: <2s Antwortzeit bei 95 % der Anfragen.",
             "Datenmigration aus Altsystem: erfolgreich (820 Lieferanten migriert).",
             "Penetration-Test: keine kritischen Schwachstellen.",
             "Offene Punkte: 4 minor (Reporting-Layout, Benutzerrechte-Granularitaet).",
         ])),
        ("Empfehlung",
         "Empfehlung zur Inbetriebnahme produktiv ab 1. Mai 2024 unter Aufloesung der 4 minor "
         "Befunde bis 15. April 2024. Verantwortlich Group Compliance + IT. Konzernweiter Roll-out "
         "in Tochtergesellschaften ab Q3/2024."),
        ("Freigabe",
         signatures("Sabine Brand", "Q-Leitung REG / Projektleiterin", "Brennhagen Elektronik GmbH",
                    "Andreas Buehler", "CAE / Sponsor Group Compliance", R["name"],
                    place="Heilbronn", date_str_="22. Maerz 2024")),
    ],
    datum="22. Maerz 2024",
)

generic_strategie(
    "RSG_IC_Rechnung_2020_03_20230915.docx",
    "Konzern-interne Rechnung RSG → REA (Maerz 2020) – Beleg-Nacherfassung",
    "Brennhagen Software GmbH (RSG) an Brennhagen Elektronik AG (REA) – Beleg-Wiedererstellung im Rahmen TP-Documentation",
    [
        ("Rechnungsangaben",
         "Rechnungsnummer: RSG-IC-2020-03-014. Rechnungsdatum: 31. Maerz 2020. "
         "Leistungsempfaenger: Brennhagen Elektronik AG, Vaihinger Strasse 120, 70567 Stuttgart. "
         "Leistungserbringer: Brennhagen Software GmbH, Schillerstrasse 18, 80336 Muenchen. "
         "USt-IdNr REA: DE 287 654 321; USt-IdNr RSG: DE 295 432 109."),
        ("Leistungsgegenstand",
         ("list", [
             "Embedded-Software-Entwicklung ICP-3 Release 2.1 (BMW MGU2-Adaptation): 1.840 Engineering-Stunden.",
             "ASPICE-Konformitaets-Dokumentation: 320 Stunden.",
             "Code-Review Premium-OEM-Spec (Mercedes-Benz MBN): 240 Stunden.",
             "Cybersecurity-TARA-Vorbereitung (ISO 21434): 180 Stunden.",
         ])),
        ("Verrechnungspreis und Steuer",
         ("list", [
             "Verrechnungspreissatz Engineering: 138 EUR/Std. (Cost-Plus-Methode, +9 % Margenaufschlag).",
             "Summe Engineering-Stunden: 2.580 × 138 EUR = 356.040 EUR.",
             "Reisekosten und Spesen (durchlaufend): 4.860 EUR.",
             "Zwischensumme netto: 360.900 EUR.",
             "Umsatzsteuer 19 % (innergemeinschaftlich, beide DE): 68.571 EUR.",
             "Rechnungsbetrag brutto: 429.471 EUR.",
             "Faelligkeit: 30. April 2020 (Konzern-Standard-Zahlungsziel 30 Tage).",
         ])),
        ("Hintergrund Nacherfassung",
         "Im Rahmen der TP-Dokumentation 2020 (Local File) wurde festgestellt, dass die "
         "Originalrechnung nicht ordnungsgemaess im SAP-System archiviert wurde. Die vorliegende "
         "Beleg-Wiedererstellung dient der vollstaendigen TP-Dokumentation gemaess § 90 Abs. 3 AO "
         "und der OECD-TP-Guidelines. Sie wurde durch Group Tax Director Dr. Heike Berger "
         "autorisiert und durch die Wirtschaftspruefung KPMG (Lead Partner Dr. Maximilian Brand) "
         "im Rahmen der GJ 2020-Pruefung zur Kenntnis genommen."),
        ("Freigabe",
         signatures("Florian Maier", "Group Controller", R["name"],
                    "Dr. Heike Berger", "Group Tax Director", R["name"],
                    place="Stuttgart", date_str_="15. September 2023")),
    ],
    datum="15. September 2023",
)

generic_strategie(
    "RCZ_to_REG_IC_2023_09_intern.docx",
    "Konzern-interne Rechnung RCZ → REG (September 2023) – Interne Dokumentation",
    "Brennhagen CZ s.r.o. an Brennhagen Elektronik GmbH – Liefer-Beleg konzern-interne Verrechnung",
    [
        ("Rechnungsangaben",
         "Rechnungsnummer: RCZ-IC-2023-09-128. Rechnungsdatum: 30. September 2023. "
         "Leistungsempfaenger: Brennhagen Elektronik GmbH, Wilhelm-Brennhagen-Strasse 1, 74072 Heilbronn. "
         "Leistungserbringer: Brennhagen CZ s.r.o., Vyskocilova 1100, 60200 Brno, Tschechien. "
         "USt-IdNr REG: DE 287 654 322; USt-IdNr RCZ: CZ 28412345."),
        ("Leistungsgegenstand",
         ("list", [
             "Lieferung Steckverbinder Typ STK-740 (BMS-12-relevant): 184.000 Stueck à 1,82 EUR.",
             "Lieferung Steckverbinder Typ STK-820 (ADAS-V4D): 92.000 Stueck à 2,14 EUR.",
             "Lieferung Steckverbinder Typ STK-310 (ICP-3-Anschluss): 320.000 Stueck à 0,68 EUR.",
             "Sondertransporte Express (Halbleiter-Allokation-Reaktion): 14 Lieferungen.",
         ])),
        ("Verrechnungspreis und Steuer",
         ("list", [
             "Berechnungsbasis: Cost-Plus +6,5 % (TP-Methode gem. konzernweiter TP-Policy).",
             "Summe Material: STK-740 = 334.880 EUR + STK-820 = 196.880 EUR + STK-310 = 217.600 EUR = 749.360 EUR.",
             "Sondertransporte: 18.400 EUR.",
             "Zwischensumme netto: 767.760 EUR.",
             "Umsatzsteuer: 0 % (innergemeinschaftliche Lieferung gem. § 4 Nr. 1b UStG / Art. 138 MwStSystRL).",
             "Rechnungsbetrag: 767.760 EUR.",
             "Faelligkeit: 30. November 2023.",
         ])),
        ("Konzern-interne Verwendung",
         "Die vorliegende Dokumentation dient ausschliesslich der konzern-internen Nachvollziehbarkeit "
         "und der TP-Documentation 2023. Sie wurde durch Werkleiter Brno (Petr Novak) und Werkleiter "
         "Heilbronn (Andreas Maier) abgestimmt. Group Tax Director (Dr. Heike Berger) hat das "
         "Verrechnungspreis-Modell genehmigt. Eintragung im SAP S/4HANA Konzern-IC-Modul erfolgt."),
        ("Freigabe",
         signatures("Petr Novak", "Werkleiter RCZ", "Brennhagen CZ s.r.o.",
                    "Andreas Maier", "Werkleiter REG", "Brennhagen Elektronik GmbH",
                    place="Brno / Heilbronn", date_str_="30. September 2023")),
    ],
    datum="30. September 2023",
)


if __name__ == "__main__":
    print("regen_roehrig_20_strategie.py done.")
