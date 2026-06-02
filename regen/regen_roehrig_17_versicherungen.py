"""Regenerate thin docs in roehrig_large/17_Versicherungen."""
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

BASE = Path(f"{_ROOT}/roehrig_large/17_Versicherungen")
H = {"name": R["name"], "addr": R["addr"], "hrb": R["hrb"]}

# ───────────────────────────── PARAMETERIZED HELPERS ─────────────────────────

def police(fname, sparte, versicherer, polnr, vs, sb, geltungsbereich,
           praemie, laufzeit, jahr=2023, besonderheiten=None):
    """Generate a Versicherungspolice document."""
    title = f"Versicherungspolice {sparte} — {jahr}"
    subtitle = f"Konzern-Master-Police Brennhagen Elektronik AG — Vermittler Marsh GmbH"
    sections = [
        ("1. Vertragsparteien", [
            ["Rolle", "Partei", "Anschrift"],
            ["Versicherungsnehmer", R["name"], R["addr"]],
            ["Mitversicherte Tochter", "Brennhagen Holding GmbH und alle 100%-Toechter (REG, RSG, RPL, RCZ, RHU, RCN)", "konsolidierter Versicherungsschutz"],
            ["Versicherer (Leader)", versicherer, "—"],
            ["Versicherungsmakler", "Marsh GmbH, Duesseldorf", "Lead: Frau Stefanie Kornmann, Senior Vice President Industrial"],
            ["Versicherungsbeauftragter Konzern", "Stefan Hoffmann, CTO (bis 30.6.2024)", "danach Dr. Petra Hollmann"],
            ["Operational Lead Risk Engineering", "Markus Hellbach", "Risk Engineer Konzern"],
        ]),
        ("2. Vertragsgegenstand und Versicherungsumfang", (
            f"Die vorliegende Police regelt den Versicherungsschutz fuer die Sparte »{sparte}« als "
            f"Konzern-Master-Police gemaess dem Konzernversicherungsprogramm der Brennhagen Elektronik AG. "
            f"Der Versicherungsschutz umfasst saemtliche Konzerngesellschaften, deren Geschaeftsbetrieb "
            f"sowie die hiermit verbundenen Risiken in dem unter Ziffer 3 beschriebenen geografischen "
            f"Geltungsbereich.\n\nDie Police ersetzt vollumfaenglich die vorhergehende Vorjahres-Police "
            f"und wurde im Rahmen des jaehrlichen Renewal-Prozesses durch Marsh GmbH neu verhandelt. "
            f"Der hier dokumentierte Wording-Stand entspricht dem mit dem Konzernvorstand am 12.12.{jahr-1} "
            f"abgestimmten Endstand und wurde nach Eingang der Praemienzahlung durch die Treasury "
            f"(Markus Pflanzer) wirksam zum 1.1.{jahr}."
        )),
        ("3. Eckdaten der Versicherung", [
            ["Parameter", "Wert"],
            ["Sparte", sparte],
            ["Versicherer (Risk Carrier)", versicherer],
            ["Polizzen-Nr.", polnr],
            ["Versicherungssumme (VS)", vs],
            ["Selbstbehalt (SB) je Schadenfall", sb],
            ["Geltungsbereich", geltungsbereich],
            ["Jahrespraemie netto", praemie],
            ["Versicherungsperiode", laufzeit],
            ["Praemienzahlweise", "jaehrlich vorab, faellig 15.1."],
            ["Rueckwaertsdeckung", "Nein, Claims-made bzw. Schadenereignisprinzip je nach Sparte"],
            ["Subsidiaritaet", "Nachrangig zu lokalen Pflichtversicherungen der Auslandstoechter"],
        ]),
        ("4. Mitversicherte Risiken und Klauseln", ("list", [
            "Vorsorgeversicherung fuer neu hinzukommende Konzerngesellschaften (Meldepflicht binnen 30 Tagen)",
            "Mitversicherung leitender Angestellter / Organe in deren Eigenschaft als Versicherungsnehmervertreter",
            "Welt-Deckung mit Ausnahme der OFAC-Sanktionslaender (Iran, Nordkorea, Syrien, Kuba, Krim/Russland teilweise)",
            "Innovation Clause: automatische Mitversicherung neuer Produkte/Werke fuer 90 Tage ohne Anzeige",
            "Difference-in-Conditions (DIC) und Difference-in-Limits (DIL) gegenueber lokalen Pflichtdeckungen",
            "Cyber-Sublimit: 5 Mio. EUR pro Schadenereignis, Aggregate 10 Mio. EUR (sofern nicht Cyber-Hauptpolice)",
            "Sanktionsklausel gemaess LMA 3100 (Marktstandard)",
            "Kriegs- und Terrorausschluss mit Rueckausnahme »Terror-Sublimit« iHv 25 Mio. EUR",
        ])),
        ("5. Selbstbehalts- und Schadenregulierung", (
            f"Selbstbehalt je Schadenereignis: {sb}. Schadenregulierung ueber den Konzern-Versicherungsbeauftragten "
            f"in Abstimmung mit Marsh Claims Solutions, Frankfurt. Schadenmeldungen sind binnen 5 Werktagen "
            f"nach Bekanntwerden des schadenstiftenden Ereignisses an den Konzern-Risk-Manager und parallel "
            f"an Marsh zu erstatten. Die Erstellung der Schadensmeldung erfolgt im standardisierten "
            f"Marsh-Schadenmeldeformular; bei Grossschaeden ab 500 TEUR ist zusaetzlich der Vorstand zu "
            f"informieren (Eskalationspfad gemaess Konzern-Risikomanagement-Richtlinie KRR-2022-08)."
        )),
        ("6. Praemie, Anpassungsmechanismus und Bonus-Malus", (
            f"Die Jahrespraemie betraegt {praemie} (netto, zzgl. 19% Versicherungsteuer). Eine Praemienanpassung "
            f"erfolgt jaehrlich auf Basis (i) der konsolidierten Konzern-Umsatzerlose des Vorjahres, (ii) der "
            f"Schadenquote (Loss Ratio) der letzten 5 Versicherungsperioden und (iii) der Risk-Engineering-"
            f"Bewertung durch Marsh Risk Consulting.\n\nBei einer Loss Ratio unter 30% wird ein Bonus von "
            f"5% der Folgejahrespraemie gewaehrt (Profit Sharing). Ueberschreitet die Loss Ratio 75%, ist "
            f"der Versicherer zur ausserordentlichen Praemienanpassung berechtigt."
        )),
        ("7. Besondere Bedingungen", besonderheiten or (
            f"Es gelten die Allgemeinen Bedingungen des Versicherers fuer die Sparte {sparte} in der zum "
            f"Vertragsbeginn aktuellsten Marsh-Wording-Fassung sowie die individuell vereinbarten Klauseln "
            f"des Anhangs A. Vertragssprache ist Deutsch; uebersetzte Fassungen dienen nur der "
            f"Information. Gerichtsstand ist Stuttgart; anwendbares Recht ist deutsches Recht unter "
            f"Ausschluss des UN-Kaufrechts und kollisionsrechtlicher Verweisungen."
        )),
        ("8. Unterzeichnung", signatures(
            "Stefanie Kornmann", "Senior Vice President", "Marsh GmbH (Vermittler)",
            "Stefan Hoffmann", "CTO / Versicherungsbeauftragter", R["name"],
            place="Stuttgart", date_str_=f"15. Dezember {jahr-1}"
        )),
    ]
    write_doc(BASE / fname, H, title, sections, subtitle=subtitle, confidential=True)


def schadensmeldung(fname, snr, sparte, datum, werk, schadenort, ursache, schaden_kurz,
                    schaden_eur, status="In Bearbeitung", versicherer="HDI Global SE"):
    """Generate a Schadensmeldung document."""
    title = f"Schadensmeldung {snr} — {sparte}"
    subtitle = f"Schadenmeldung an Versicherer ueber Marsh GmbH"
    sections = [
        ("1. Meldungs-Stammdaten", [
            ["Parameter", "Wert"],
            ["Schadennummer (intern)", snr],
            ["Schadennummer (Versicherer)", f"VS-{snr}-{versicherer.split()[0][:3].upper()}"],
            ["Sparte", sparte],
            ["Versicherer (Leader)", versicherer],
            ["Vermittler", "Marsh GmbH, Duesseldorf"],
            ["Schadendatum", datum],
            ["Meldedatum bei Marsh", datum],
            ["Versicherungsnehmer", R["name"]],
            ["Betroffene Gesellschaft / Werk", werk],
            ["Schadenort", schadenort],
            ["Vorlaeufiger Status", status],
        ]),
        ("2. Sachverhalt und Schadenshergang", (
            f"Am {datum} ereignete sich im {werk} ({schadenort}) folgender Schaden: {schaden_kurz}\n\n"
            f"Der Vorfall wurde durch den lokalen EHS-Verantwortlichen unverzueglich an den Konzern-Risk-Manager "
            f"(Stefan Hoffmann bzw. ab 1.7.2024 Dr. Petra Hollmann) sowie an den Operational Lead Risk Engineering "
            f"Markus Hellbach gemeldet. Die Schadenstelle wurde binnen 2 Stunden gesichert; eine fotografische "
            f"Dokumentation gemaess Konzern-Schadenprotokoll-Standard SOP-RISK-04 wurde erstellt und in der "
            f"Marsh ClientView-Schadenakte hinterlegt."
        )),
        ("3. Ursachenanalyse (vorlaeufig)", (
            f"Vorlaeufige Ursachenfeststellung: {ursache}\n\nEine abschliessende Root-Cause-Analyse wird im "
            f"Rahmen eines 5Why-/Ishikawa-Workshops mit dem Werkleiter, der Q-Leitung und ggf. einem externen "
            f"Sachverstaendigen des Versicherers durchgefuehrt. Bei Verdacht auf Vorsatz, grobe Fahrlaessigkeit "
            f"oder strafrechtliche Relevanz wird zusaetzlich der Chief Audit Executive Andreas Buehler "
            f"sowie die Rechtsabteilung in Stuttgart eingebunden."
        )),
        ("4. Schadenshoehe und finanzielle Auswirkung", [
            ["Position", "Betrag (EUR)"],
            ["Vorlaeufig geschaetzte Schadenshoehe (brutto)", schaden_eur],
            ["Selbstbehalt gemaess Police", "siehe Police-Stammdaten"],
            ["Erwartete Entschaedigung (netto)", "wird nach Sachverstaendigengutachten festgestellt"],
            ["Folgekosten / Betriebsunterbrechung", "separate BU-Meldung folgt falls einschlaegig"],
            ["Reservierte Rueckstellung (HGB / IFRS)", "wird im naechsten Quartalsabschluss gebildet"],
        ]),
        ("5. Sofortmassnahmen und Schadenminderung", ("list", [
            "Sicherung der Schadenstelle und Abgrenzung des betroffenen Bereichs",
            "Information an betroffene Mitarbeiter, ggf. Erste-Hilfe-Leistung und D-Arzt-Vorstellung",
            "Foto- und Videodokumentation gemaess SOP-RISK-04",
            "Asservierung beschaedigter Bauteile fuer Sachverstaendigenpruefung",
            "Information der lokalen Behoerden (Gewerbeaufsicht, ggf. Polizei) bei meldepflichtigen Ereignissen",
            "Aktivierung des Konzern-Krisen-Kommunikationspfads bei Schaeden > 1 Mio. EUR",
            "Schadenmeldung an Marsh ClientView binnen 5 Werktagen (eingehalten)",
            "Einleitung von Schadenminderungsmassnahmen gemaess Pflicht des Versicherungsnehmers",
        ])),
        ("6. Naechste Schritte und Eskalation", (
            f"Naechste Schritte: (i) Beauftragung eines externen Sachverstaendigen durch {versicherer} "
            f"in Abstimmung mit Marsh; (ii) Erstellung des abschliessenden Schadenberichts binnen 30 Tagen; "
            f"(iii) Verhandlung der Regulierungssumme mit dem Versicherer; (iv) ggf. Regressforderungen "
            f"gegen Dritte (Lieferanten, Subunternehmer) durch die Rechtsabteilung pruefen lassen.\n\n"
            f"Die Schadenakte verbleibt bis zur abschliessenden Regulierung im Status »{status}« und wird "
            f"im monatlichen Schadenstatistik-Update an Marsh sowie quartalsweise im Risk-Committee "
            f"(Vorsitz: CFO Laura Bauer) berichtet."
        )),
        ("7. Verteiler", ("list", [
            "Konzern-Risk-Manager (Stefan Hoffmann / ab 1.7.2024 Dr. Petra Hollmann)",
            "Operational Lead Risk Engineering (Markus Hellbach)",
            "Marsh GmbH — Frau Stefanie Kornmann (SVP Industrial)",
            f"Versicherer {versicherer} — Schaden-Sachbearbeitung",
            "Betroffene Werkleitung",
            "Konzern-Controlling (Florian Maier) — Rueckstellungsbildung",
            "Chief Audit Executive (Andreas Buehler) ab Schadenshoehe > 500 TEUR",
        ])),
    ]
    write_doc(BASE / fname, H, title, sections, subtitle=subtitle, confidential=True)


def renewal_status(fname, jahr, sparte, ergebnis):
    """Generic renewal/QBR/status doc."""
    title = f"Renewal-Bericht {sparte} — Versicherungsperiode {jahr}"
    sections = [
        ("1. Zielsetzung des Renewals", (
            f"Das Renewal {jahr} fuer die Konzern-Master-Police »{sparte}« wurde durch Marsh GmbH "
            f"unter Federfuehrung von Frau Stefanie Kornmann (SVP Industrial) in Abstimmung mit dem "
            f"Konzern-Versicherungsbeauftragten gefuehrt. Ziel war eine moeglichst stabile "
            f"Praemienentwicklung bei gleichzeitiger Wording-Verbesserung in den Bereichen Cyber-Sublimit, "
            f"Lieferketten-Unterbrechung und ESG-Klausel."
        )),
        ("2. Marktumfeld", (
            f"Der Industrieversicherungsmarkt zeigt fuer {jahr} eine ueberwiegend stabile Marktphase "
            f"mit leichten Praemienreduzierungen in den Sparten Sach und Maschinenbruch, jedoch weiterhin "
            f"deutliche Praemienerhoehungen in den Sparten Cyber und D&O. Die Schadenquote des "
            f"Brennhagen-Konzerns liegt mit 38% im 5-Jahres-Durchschnitt unterhalb der Marktquote der "
            f"vergleichbaren Automotive-Tier-1-Zulieferer (47%)."
        )),
        ("3. Verhandlungsergebnis", ergebnis),
        ("4. Empfehlung", (
            f"Marsh empfiehlt die Verlaengerung der Master-Police {sparte} zu den verhandelten Konditionen. "
            f"Die Police wurde durch den Vorstand am 12.12.{jahr-1} formell genehmigt und durch den "
            f"Konzern-Versicherungsbeauftragten gegengezeichnet. Die naechste turnusgemaesse Renewal-"
            f"Verhandlung findet im Q4-{jahr} statt."
        )),
    ]
    write_doc(BASE / fname, H, title, sections, subtitle=f"Marsh GmbH — Renewal {jahr}", confidential=True)


def generic_doc(fname, title, intro, body_paras, signers=None):
    """Generic fallback for non-standard misfiled docs."""
    sections = [
        ("1. Einleitung und Hintergrund", intro),
        ("2. Sachverhalt", body_paras[0] if body_paras else ""),
        ("3. Bewertung und Massnahmen", body_paras[1] if len(body_paras) > 1 else ""),
        ("4. Naechste Schritte", body_paras[2] if len(body_paras) > 2 else ""),
    ]
    if signers:
        sections.append(("5. Unterschriften", signers))
    write_doc(BASE / fname, H, title, sections, confidential=False)


# ───────────────────────────── POLICEN ───────────────────────────────────────

police(
    "REA_Police_D_O_Versicherung_2023.docx",
    sparte="Directors & Officers Liability (D&O)",
    versicherer="Allianz Global Corporate & Specialty SE (AGCS), Muenchen",
    polnr="AGCS-DO-REA-2023-0001",
    vs="50.000.000 EUR pro Versicherungsfall und Jahresaggregat",
    sb="10% des Schadens, mindestens 25.000 EUR",
    geltungsbereich="weltweit (inkl. USA/Kanada-Ueberdeckung mit Side-A-DIC-Layer)",
    praemie="245.000 EUR p.a.",
    laufzeit="1.1.2023 – 31.12.2023 (mit 12 Monate Nachmeldefrist)",
    besonderheiten=(
        "Mitversicherte Personen: alle aktuellen, ehemaligen und kuenftigen Mitglieder von Vorstand und "
        "Aufsichtsrat der Brennhagen Elektronik AG sowie aller mitversicherten Konzerngesellschaften. "
        "Inklusive Outside Directorship Coverage fuer Vorstandsmandate in Branchenverbaenden. "
        "Side-A-Layer 25 Mio. EUR fuer nicht entschaedigte Anspruchsfaelle.\n\nDie Police wurde im "
        "Rahmen des IPO 2022 angepasst und enthaelt eine Public-Offering-of-Securities-Insurance-"
        "Klausel (POSI) mit eigener Versicherungssumme iHv 25 Mio. EUR fuer Prospekthaftungsanspruechen."
    ),
)

police(
    "REA_Police_Produkthaftpflicht_2023.docx",
    sparte="Erweiterte Produkthaftpflicht (Industriehaftpflicht)",
    versicherer="Allianz Global Corporate & Specialty SE (AGCS), Muenchen",
    polnr="AGCS-PH-REA-2023-0002",
    vs="100.000.000 EUR pauschal weltweit",
    sb="50.000 EUR je Schadenereignis",
    geltungsbereich="weltweit (inkl. USA / Kanada via DIC-Layer)",
    praemie="1.180.000 EUR p.a.",
    laufzeit="1.1.2023 – 31.12.2023",
    besonderheiten=(
        "Mitversichert sind insbesondere: Rueckrufkosten (Sublimit 20 Mio. EUR), Aus- und Einbaukosten, "
        "Bearbeitungsschaeden, Produktschutz-/Recall-Beratungskosten der Crisis Communications "
        "Hotline, sowie erweiterte Mangelfolgeschaeden gemaess Marsh-Wording 2023. Mitversicherung "
        "saemtlicher OEM-Lieferungen einschliesslich der Produkte ICP-3, BMS-12, ADAS-V4D, ECU-900 "
        "und LightCtrl-7. Lieferantenregress vorbehalten."
    ),
)

police(
    "REA_Police_Betriebsunterbrechung_2023.docx",
    sparte="Betriebsunterbrechungsversicherung (BU)",
    versicherer="HDI Global SE, Hannover",
    polnr="HDI-BU-REA-2023-0003",
    vs="350.000.000 EUR (12-Monats-Karenz, Haftzeit 24 Monate)",
    sb="5 Werktage Karenz je Unterbrechungsfall",
    geltungsbereich="EU-Werke (REG Heilbronn, RSG Muenchen, RPL Katowice, RCZ Brno, RHU Gyoer) plus weltweite Lieferketten-Erweiterung (CBI-Sublimit 50 Mio. EUR)",
    praemie="780.000 EUR p.a.",
    laufzeit="1.1.2023 – 31.12.2023",
    besonderheiten=(
        "Contingent Business Interruption (CBI) bis 50 Mio. EUR fuer namentlich benannte Lieferanten "
        "(Bosch, Infineon, STMicroelectronics, TSMC). Versicherte Deckungsbeitrag wird jaehrlich auf "
        "Basis der IFRS-Konzernzahlen aktualisiert; Stand 2023 beruht auf Umsatz 612 Mio. EUR und "
        "Deckungsbeitragsquote 28%. Mitversicherung von Mehrkosten zur Schadenminderung (Sublimit 25 Mio. EUR)."
    ),
)

police(
    "REA_Police_Transportversicherung_2023.docx",
    sparte="Transportversicherung (Warentransport)",
    versicherer="Allianz Global Corporate & Specialty SE (AGCS), Muenchen",
    polnr="AGCS-TR-REA-2023-0004",
    vs="25.000.000 EUR pro Sendung",
    sb="10.000 EUR je Schadenfall",
    geltungsbereich="weltweit, Inco-Terms FCA/DAP/DDP gemaess Lieferbedingungen",
    praemie="185.000 EUR p.a.",
    laufzeit="1.1.2023 – 31.12.2023",
    besonderheiten=(
        "Generalpolice fuer alle See-, Luft- und Strassen-Transporte des Konzerns. Mitversichert sind "
        "interne Werkstransporte zwischen REG, RPL, RCZ, RHU sowie OEM-JIT-Lieferungen. "
        "Allgefahrendeckung gemaess ICC(A); Sublimit fuer Lagerungen ausserhalb des Werks 5 Mio. EUR. "
        "Mitversichert: Container-Demurrage-Kosten bei Schadenereignissen sowie havariegrosse-Beitraege."
    ),
)

police(
    "REA_Police_Cyber_Versicherung_2023.docx",
    sparte="Cyber-Versicherung (Cyber Risk / Data Breach)",
    versicherer="Munich Re Beazley Syndicate (via Marsh)",
    polnr="MRB-CY-REA-2023-0005",
    vs="25.000.000 EUR pro Schadenereignis und Jahresaggregat",
    sb="250.000 EUR je Schadenfall",
    geltungsbereich="weltweit, inkl. Cloud-Anbieter (SAP, Microsoft Azure, AWS) im erweiterten Vendor-Coverage",
    praemie="420.000 EUR p.a.",
    laufzeit="1.1.2023 – 31.12.2023",
    besonderheiten=(
        "Eingeschlossene Deckungsbausteine: Eigenschadenkomponenten (Forensik, Wiederherstellung, "
        "Cyber-Erpressung mit Sublimit 5 Mio. EUR), Drittschadenkomponenten (Haftpflicht aus "
        "Datenschutzverletzungen, behoerdliche Strafen DSGVO soweit versicherbar), "
        "Betriebsunterbrechung durch Cyber-Vorfall (Sublimit 10 Mio. EUR, 8 Stunden Karenz), "
        "Reputationsschadenmanagement, Incident-Response-Hotline 24/7 (Beazley Breach Response).\n\n"
        "Voraussetzung der Deckung: MFA fuer alle privilegierten Konten, segmentierte Backups, "
        "EDR-Loesung auf allen Endpunkten. Brennhagen nutzt CrowdStrike Falcon (RSG Muenchen ist "
        "Pilot-Site fuer XDR-Rollout 2023)."
    ),
)

# ───────────────────────────── SCHADENSMELDUNGEN ─────────────────────────────

SCHADEN = [
    # 2020
    ("Schadensmeldung_2020_0004.docx", "SM-2020-0004", "Maschinenbruch", "15.03.2020",
     "REG Heilbronn", "Werk Heilbronn, Halle 3, SMD-Linie 2",
     "Lagerschaden an Pick&Place-Maschine SIPLACE TX2 — Spindelausfall durch Schmiermittelausfall",
     "Bruch des Y-Achsen-Spindellagers; betroffene Linie 4 Tage stillgelegt",
     "180.000 EUR (Reparatur + Mehrkosten)", "Reguliert 06/2020", "HDI Global SE"),
    ("Schadensmeldung_2020_0008.docx", "SM-2020-0008", "Sach (Feuer)", "22.04.2020",
     "RPL Katowice", "Werk Katowice, Lagerhalle B",
     "Schwelbrand in Lithium-Batterie-Lager — vermutlich thermal runaway eines defekten Testmusters",
     "Schwelbrand und Ruschaden auf ca. 120 m2 Lagerflaeche; keine Personenschaeden",
     "85.000 EUR (Bereinigung + entwerteter Bestand)", "Reguliert 09/2020", "HDI Global SE"),
    ("Schadensmeldung_2020_0012.docx", "SM-2020-0012", "Transport", "08.06.2020",
     "Lieferung REG → BMW Werk Leipzig", "BAB A4 Hoehe Erfurt-West",
     "Transportschaden ECU-900 Container — Auffahrunfall des LKW, Sendung teilweise zerstoert",
     "12 Paletten ECU-900 unbrauchbar, Bauteilebezeichnung beschaedigt",
     "240.000 EUR (Warenwert + Eilersatzproduktion)", "Reguliert 10/2020", "AGCS"),
    ("Schadensmeldung_2020_0016.docx", "SM-2020-0016", "Betriebsunterbrechung", "12.08.2020",
     "RCZ Brno", "Werk Brno, Spritzgussabteilung",
     "Stromausfall bei lokalem Versorger CEZ — Spritzgussproduktion 26 Stunden unterbrochen",
     "Sekundaerer BU-Schaden: 12 OEM-Lieferungen verspaetet; Sonderfracht erforderlich",
     "92.000 EUR (DB-Ausfall + Sonderfrachten)", "Reguliert 12/2020", "HDI Global SE"),
    ("Schadensmeldung_2020_0020.docx", "SM-2020-0020", "Haftpflicht (Produkt)", "05.09.2020",
     "BMW Werk Dingolfing — Einbau ICP-3", "Werk Dingolfing, Endmontage",
     "Reklamation fehlerhafter ICP-3-Module — Bluetooth-Antennenkontakt korrodiert (Galvanik-Charge)",
     "Reklamation 4.800 Module; Aus- und Einbaukosten beim OEM",
     "320.000 EUR (Tauschkosten + Logistik)", "Reguliert 02/2021", "AGCS"),
    ("Schadensmeldung_2020_0024.docx", "SM-2020-0024", "KFZ-Flotte", "18.10.2020",
     "Konzern-Fuhrpark", "B27 Stuttgart-Vaihingen",
     "Totalschaden Dienstwagen Audi A6 (CTO Hoffmann) — Wildunfall, kein Personenschaden",
     "Fahrzeug Totalschaden, Ablieferung an Verwertungsbetrieb",
     "48.000 EUR (Wiederbeschaffungswert)", "Reguliert 11/2020", "Allianz"),
    ("Schadensmeldung_2020_0028.docx", "SM-2020-0028", "Vertrauensschaden", "07.12.2020",
     "REG Heilbronn", "Werk Heilbronn, Einkauf",
     "Verdacht auf Spesenmanipulation Einkaeufer (Whistleblower-Hinweis) — interne Untersuchung CAE",
     "Vermutlich 35.000 EUR fingierte Reisekosten ueber 18 Monate; Arbeitsrechtsverfahren laeuft",
     "35.000 EUR Schaden + 22.000 EUR Untersuchungskosten", "Anhaengig — Strafanzeige eingereicht", "AGCS"),

    # 2021
    ("Schadensmeldung_2021_0001.docx", "SM-2021-0001", "Sach (Wasser)", "11.01.2021",
     "RHU Gyoer", "Werk Gyoer, Reinraum-Stufe 2",
     "Wassereinbruch durch defektes Klimageraet — Reinraum-Boden und 2 Pruefplaetze beschaedigt",
     "Reinraum 5 Tage gesperrt, Re-Qualifizierung erforderlich",
     "165.000 EUR (Reparatur + Requalifizierung)", "Reguliert 05/2021", "HDI Global SE"),
    ("Schadensmeldung_2021_0005_2024-03-01.docx", "SM-2021-0005", "Produkthaftpflicht", "23.02.2021",
     "Stellantis Werk Mirafiori (IT) — Einbau ADAS-V4D",
     "Werk Mirafiori, Endmontage",
     "Software-Bug ADAS-V4D Firmware 2.3 — Falschpositiv-Detektionen bei Bauarbeiten-Markierungen",
     "OTA-Rueckruf 18.500 Fahrzeuge; gemeinsame Rueckrufaktion mit Stellantis (Update auf FW 2.3.1)",
     "1.450.000 EUR (Engineering + Rueckruf-Logistik)", "Reguliert 11/2023 nach Rechtsstreit", "AGCS"),
    ("Schadensmeldung_2021_0009.docx", "SM-2021-0009", "Cyber", "17.03.2021",
     "RSG Muenchen", "Office-Network RSG",
     "Phishing-Angriff auf Lead-Developer Lars Wittmann — Credential-Theft, keine Datenexfiltration nachgewiesen",
     "Sofortige Reset aller betroffenen Konten; CrowdStrike-Forensik 5 Tage",
     "78.000 EUR (Forensik + Awareness-Schulung)", "Reguliert 06/2021", "Munich Re Beazley"),
    ("Schadensmeldung_2021_0013.docx", "SM-2021-0013", "Maschinenbruch", "02.04.2021",
     "RCZ Brno", "Werk Brno, Spritzgusslinie 1",
     "Heisskanal-Defekt Spritzgussmaschine Engel 200t — Werkzeugaufnahme rissig",
     "3-Tage-Stillstand, Werkzeug-Reparatur durch externe Firma; Linie 2 als Notfallproduktion",
     "210.000 EUR (Werkzeug + BU-Anteil)", "Reguliert 08/2021", "HDI Global SE"),
    ("Schadensmeldung_2021_0017.docx", "SM-2021-0017", "Transport", "29.05.2021",
     "Lieferung RPL → Volkswagen Werk Zwickau", "Hafen Hamburg-Altenwerder",
     "Containerverlust bei Umschlag — Container ueber Bord gegangen, Bergung erfolglos",
     "Containerinhalt BMS-12 Steuergeraete: 1.200 Stueck",
     "385.000 EUR (Warenwert)", "Reguliert 10/2021", "AGCS"),
    ("Schadensmeldung_2021_0021.docx", "SM-2021-0021", "Haftpflicht (Betriebshaftpflicht)", "14.07.2021",
     "REG Heilbronn", "Werk Heilbronn, Werksgelaende",
     "Fremdfirmenmitarbeiter durch herabfallende Palette verletzt — Sturz vom Gabelstapler",
     "Berufsunfaehigkeit fuer 6 Wochen; BG-Verfahren laeuft",
     "65.000 EUR (Schmerzensgeld + BG-Regress)", "Reguliert 03/2022", "AGCS"),
    ("Schadensmeldung_2021_0025.docx", "SM-2021-0025", "Reisekrankenversicherung", "21.08.2021",
     "Reise CEO Anna Mueller — Detroit (USA)", "Henry Ford Hospital, Detroit",
     "Akute Magen-Darm-Erkrankung waehrend Ford-Werksbesuch — stationaere Behandlung 3 Tage",
     "Ambulante und stationaere Behandlung, Krankenruecktransport per Linienflug",
     "18.500 EUR (Behandlung + Ruecktransport)", "Reguliert 10/2021", "DKV"),
    ("Schadensmeldung_2021_0029.docx", "SM-2021-0029", "Rechtsschutz (Sondersparten)", "03.11.2021",
     "REA Konzern", "AG Stuttgart, Wettbewerbskammer",
     "Wettbewerbsklage eines ehemaligen Lieferanten wegen angeblicher Markterhebungsspionage — abgewiesen",
     "Gerichtsverfahren ueber 2 Instanzen, Klage rechtskraeftig abgewiesen",
     "95.000 EUR (Anwalts- + Gerichtskosten)", "Reguliert 05/2023", "Roland Rechtsschutz"),

    # 2022
    ("Schadensmeldung_2022_0002.docx", "SM-2022-0002", "Sach (Sturm)", "19.02.2022",
     "REG Heilbronn", "Werk Heilbronn, Daecher Halle 1+2",
     "Sturm »Zeynep« — Daecher beschaedigt, Dichtungsabriss",
     "Wassereintritt in Halle 1, 3 Maschinen Schaeden durch Feuchtigkeit",
     "420.000 EUR (Dachreparatur + Maschinen-Folgeschaeden)", "Reguliert 09/2022", "HDI Global SE"),
    ("Schadensmeldung_2022_0006.docx", "SM-2022-0006", "Cyber (Ransomware-Versuch)", "08.03.2022",
     "RPL Katowice", "Werk Katowice, OT-Netzwerk",
     "Ransomware-Versuch ueber kompromittiertes USB-Geraet — Angriff durch EDR (CrowdStrike) gestoppt",
     "Forensik bestaetigt: kein lateral movement; isolierter Endpunkt rebuildet",
     "65.000 EUR (Forensik + Hardware-Rebuild)", "Reguliert 06/2022", "Munich Re Beazley"),
    ("Schadensmeldung_2022_0010.docx", "SM-2022-0010", "Maschinenbruch", "25.04.2022",
     "RPL Katowice", "Werk Katowice, AOI-Pruefplatz",
     "Hauptkamera AOI-Anlage Koh Young Defekt — Pixel-Burnout durch Versorgungsspannungsspitze",
     "AOI-Linie 4 Tage stillgelegt, manueller Backup-Pruefprozess aktiviert",
     "110.000 EUR (Ersatzkamera + Kalibrierung)", "Reguliert 08/2022", "HDI Global SE"),
    ("Schadensmeldung_2022_0014_2024-03-01.docx", "SM-2022-0014", "Produkthaftpflicht (Feldproblem)", "11.06.2022",
     "VW ID.7 Vorserie — BMS-12", "Werk Zwickau, Vorserienmontage",
     "Vorserien-BMS-12 mit fehlerhafter Zellbalancierungs-FW — Risiko Tiefentladung",
     "Vorserienflotte 230 Fahrzeuge; FW-Update durch VW im Vorserienprozess",
     "680.000 EUR (Engineering + OTA-Update + Logistik)", "Reguliert 02/2024 nach Verhandlung", "AGCS"),
    ("Schadensmeldung_2022_0018.docx", "SM-2022-0018", "KFZ-Flotte", "30.07.2022",
     "Konzern-Fuhrpark", "BAB A8 Stuttgart-Ost",
     "Auffahrunfall Dienstwagen Mercedes E-Klasse — Verschulden Gegner, Regress an Allianz",
     "Kollege leicht verletzt, Fahrzeug reparaturfaehig",
     "14.500 EUR (Reparatur, Regress laeuft)", "Reguliert 09/2022", "Allianz"),
    ("Schadensmeldung_2022_0022.docx", "SM-2022-0022", "Vertrauensschaden (Phishing-CEO-Fraud)", "14.09.2022",
     "REA Konzern Treasury", "Stuttgart Hauptsitz, Treasury",
     "CEO-Fraud-Versuch via gefaelschter E-Mail »Anna Mueller« — Ueberweisungsauftrag 480 TEUR — durch Treasury (Pflanzer) erkannt",
     "Kein finanzieller Schaden, aber forensische Aufarbeitung und Awareness-Update",
     "28.000 EUR (Forensik + Awareness-Programm)", "Reguliert 12/2022", "AGCS"),
    ("Schadensmeldung_2022_0026.docx", "SM-2022-0026", "BU (Lieferantenausfall)", "22.10.2022",
     "REG Heilbronn — Zulieferer Infineon Werk Dresden", "Heilbronn, Wareneingang",
     "CBI-Schaden — Lieferengpass Infineon-Halbleiter durch Brand in Wafer-Fab",
     "Produktion ECU-900 4 Tage reduziert; Sonderfrachten und Allokationsverhandlungen",
     "520.000 EUR (DB-Anteil + Sonderfrachten)", "Reguliert 04/2023", "HDI Global SE"),

    # 2023
    ("Schadensmeldung_2023_0003.docx", "SM-2023-0003", "Sach (Feuer)", "27.01.2023",
     "RCZ Brno", "Werk Brno, Galvanik-Bereich",
     "Kleinbrand in Galvanik-Filter — Verpuffung im Aktivkohlefilter, kein Personenschaden",
     "Brandbereich 25 m2; Filteranlage Totalschaden; Galvanik 6 Tage stillgelegt",
     "240.000 EUR (Anlagenreparatur + BU)", "Reguliert 07/2023", "HDI Global SE"),
    ("Schadensmeldung_2023_0007_v2.docx", "SM-2023-0007", "Cyber (DDoS)", "12.02.2023",
     "REA Konzern Web/Investor Relations", "Hosting-Provider extern",
     "DDoS-Angriff auf Investor-Relations-Webseite — 6 Stunden Nichtverfuegbarkeit, ad-hoc Mitteilung verzoegert",
     "Cloudflare-Mitigation aktiviert; ad-hoc Mitteilung mit 4h Verzoegerung publiziert",
     "42.000 EUR (Forensik + Hosting-Hardening)", "Reguliert 05/2023", "Munich Re Beazley"),
    ("Schadensmeldung_2023_0011.docx", "SM-2023-0011", "Maschinenbruch", "08.03.2023",
     "RHU Gyoer", "Werk Gyoer, Sensor-Pruefstand",
     "Hochfrequenz-Pruefstand R&S CMW500 Defekt — Endstufenmodul defekt, Reparatur durch Hersteller",
     "Pruefstand 9 Tage offline, Mietgeraet R&S CMW500 als Backup",
     "85.000 EUR (Reparatur + Mietgeraet)", "Reguliert 06/2023", "HDI Global SE"),
    ("Schadensmeldung_2023_0015.docx", "SM-2023-0015", "Transport", "19.04.2023",
     "Lieferung RCZ → Mercedes Werk Sindelfingen", "Tschechische Grenze, Rozvadov",
     "Diebstahl bei LKW-Pause — Container teilweise aufgebrochen, ADAS-V4D-Module entwendet",
     "320 ADAS-V4D-Module gestohlen, Versicherer eingeschaltet, Polizei-Bericht erstattet",
     "210.000 EUR (Warenwert)", "Reguliert 08/2023", "AGCS"),
    ("Schadensmeldung_2023_0019.docx", "SM-2023-0019", "Haftpflicht (Umwelthaftung)", "25.05.2023",
     "RPL Katowice", "Werk Katowice, Galvanik-Abwasserneutralisation",
     "Geringfuegige Ueberschreitung Kupfer-Grenzwert in Abwasser — Selbstanzeige beim WIOS Katowice",
     "Bussgeld 18.000 PLN; Sanierungsauflage; Nachruestung Filteranlage erforderlich",
     "120.000 EUR (Bussgeld + Sanierung + Nachruestung)", "Reguliert 11/2023", "AGCS"),
    ("Schadensmeldung_2023_0023.docx", "SM-2023-0023", "D&O (Anspruchsabwehr)", "14.07.2023",
     "REA Vorstand", "OLG Stuttgart, Aktionaersklage",
     "Aktionaersklage wegen vermeintlich verspaeteter Ad-hoc-Mitteilung (BMS-12 Reklamation) — abgewiesen 1. Instanz",
     "Anwaltliche Vertretung Hengeler Mueller; Klage in 1. Instanz abgewiesen, Berufung anhaengig",
     "240.000 EUR (Anwaltskosten 1. Instanz)", "In Bearbeitung — Berufung anhaengig", "AGCS"),
    ("Schadensmeldung_2023_0027.docx", "SM-2023-0027", "Cyber (Datenschutzvorfall)", "21.09.2023",
     "RSG Muenchen", "RSG, HR-Datenbank",
     "Unbefugter Zugriff Praktikant auf HR-Datenbank — versehentliche Berechtigungserteilung, kein Datenabfluss extern",
     "Meldung an LDI BW; interne arbeitsrechtliche Massnahmen; Awareness-Schulung HR",
     "55.000 EUR (Forensik + LDI-Verfahren + Schulung)", "Reguliert 12/2023", "Munich Re Beazley"),
]

for args in SCHADEN:
    schadensmeldung(*args)


# ───────────────────────────── MISC / MISFILED DOCS ─────────────────────────

# REA_AR_Dienstvertrag_Dipl.-Kfm._Heinrich_Baumeister.docx — AR-Dienstvertrag (misfiled)
generic_doc(
    "REA_AR_Dienstvertrag_Dipl.-Kfm._Heinrich_Baumeister.docx",
    title="Aufsichtsrats-Dienstvertrag — Dipl.-Kfm. Heinrich Baumeister",
    intro=(
        f"Zwischen der {R['name']}, {R['addr']} (nachfolgend »Gesellschaft«), vertreten durch den "
        f"Aufsichtsratsvorsitzenden Dr. Klaus Steinbrueck, einerseits, und Herrn Dipl.-Kfm. Heinrich "
        f"Baumeister, geboren am 4. August 1958, wohnhaft in Bad Homburg vor der Hoehe, andererseits, "
        f"wird mit Wirkung zum 1. Juli 2024 nachfolgender Dienstvertrag geschlossen.\n\n"
        f"Anlass des Vertrags ist die Bestellung von Herrn Baumeister durch Beschluss des Aufsichtsrats "
        f"vom 14. Juni 2024 als externer Berater des Pruefungsausschusses fuer Fragen der "
        f"versicherungsbezogenen Risikobewertung im Rahmen der Konzern-D&O-Police und der "
        f"Versicherungsstrategie."
    ),
    body_paras=[
        (
            "Der Dienstvertrag regelt die beraterische Taetigkeit von Herrn Baumeister als externer "
            "Risikoberater fuer den Pruefungsausschuss in versicherungsbezogenen Fragestellungen. "
            "Herr Baumeister verfuegt ueber langjaehrige Erfahrung als Vorstand der Gerling-Konzern "
            "Allgemeine Versicherungs-AG (1992-2006) sowie als Senior Advisor bei Marsh GmbH "
            "(2006-2019). Seine Expertise ist insbesondere fuer die Begleitung der jaehrlichen "
            "D&O-Renewals, fuer die Ueberwachung der Marsh-Maklerleistung und fuer "
            "Schadenfallbegleitung gefragt."
        ),
        (
            "Verguetung: 75.000 EUR p.a. zuzueglich Umsatzsteuer, faellig in vier vierteljaehrlichen "
            "Raten. Aufwandsersatz nach Belegnachweis. Spesen-Reisen ausserhalb des DACH-Raums "
            "beduerfen der vorherigen Zustimmung des Pruefungsausschuss-Vorsitzenden Prof. Dr.-Ing. "
            "Gerhard Voss.\n\nVerschwiegenheitspflicht gemaess § 116 AktG iVm § 93 AktG. "
            "Versicherungsschutz: Aufnahme in die Konzern-D&O-Police als »Outside Director« mit "
            "Mitversicherung im Side-A-Layer."
        ),
        (
            "Laufzeit: 3 Jahre, beginnend am 1. Juli 2024, endend am 30. Juni 2027. Verlaengerung "
            "moeglich durch beiderseitiges Einvernehmen. Ausserordentliche Kuendigung jederzeit "
            "moeglich aus wichtigem Grund. Gerichtsstand Stuttgart, anwendbares Recht: deutsches "
            "Recht.\n\nDer Vertrag wurde durch den Aufsichtsrat in der Sitzung vom 14. Juni 2024 "
            "einstimmig genehmigt und durch den Konzern-Versicherungsbeauftragten zur Aufnahme "
            "in die D&O-Police gemeldet."
        ),
    ],
    signers=signatures(
        "Dr. Klaus Steinbrueck", "Aufsichtsratsvorsitzender", R["name"],
        "Dipl.-Kfm. Heinrich Baumeister", "Externer Berater", "—",
        place="Stuttgart", date_str_="20. Juni 2024",
    ),
)

# REA_Directors_Dealings_Klaus-Peter_Zimmermann_2023.docx (misfiled — Directors Dealings)
generic_doc(
    "REA_Directors_Dealings_Klaus-Peter_Zimmermann_2023.docx",
    title="Directors' Dealings-Meldung — Klaus-Peter Zimmermann",
    intro=(
        f"Stimmrechtsmitteilung und Directors-Dealings-Meldung gemaess Art. 19 MAR und § 26 WpHG "
        f"betreffend die {R['name']}, ISIN DE000RHGRP12. Meldende Person: Herr Klaus-Peter "
        f"Zimmermann, Leiter Konzern-Versicherungen (Direct Report an CTO Stefan Hoffmann). Als "
        f"»Person, die Fuehrungsaufgaben wahrnimmt« iSd Art. 3 Abs. 1 Nr. 25 MAR gilt Herr Zimmermann "
        f"aufgrund seiner Befugnis zur Mitzeichnung von Versicherungsvertraegen ueber 1 Mio. EUR "
        f"Praemienvolumen und seines unbeschraenkten Zugangs zu nicht-oeffentlichen Risikoinformationen."
    ),
    body_paras=[
        (
            "Gegenstand der Meldung: Erwerb von 2.500 Stueck Stammaktien Brennhagen Elektronik AG "
            "(ISIN DE000RHGRP12, WKN RHGRP1) zum Durchschnittskurs von 28,40 EUR/Aktie, "
            "Gesamtvolumen 71.000 EUR, Geschaeftstag 14. September 2023, Ausfuehrungsort XETRA. "
            "Geschaeftsart: Kauf. Anlass: privater Vermoegensaufbau, keine Insiderkenntnis."
        ),
        (
            "Der Erwerb erfolgte ausserhalb der Closed Periods gemaess Konzern-Insider-Richtlinie. "
            "Eine Pre-Clearance durch den Compliance-Officer Dr. Sebastian Lohmann liegt vor "
            "(Vorgang COMP-2023-0421). Die Bestaende werden im Konzern-Insiderregister gefuehrt; "
            "die Meldung wurde fristgerecht binnen 3 Geschaeftstagen an die BaFin und die Brennhagen "
            "Elektronik AG uebermittelt und ueber den IR-Verteiler (Investor Relations Lead: "
            "Dr. Annette Reuter) publiziert."
        ),
        (
            "Weitere Schritte: Veroeffentlichung der Stimmrechtsmitteilung ueber den DGAP-Newswire, "
            "Eintragung im konzerninternen Personal-Geschaefte-Register, Update der Excel-Liste "
            "MAR-COMP-2023. Eine Nachmeldung erfolgt nicht, da keine zustimmungspflichtige "
            "Aenderung der Position erfolgt. Die naechste Closed Period beginnt am 1. Februar 2024 "
            "(vor Veroeffentlichung des Jahresabschlusses 2023)."
        ),
    ],
)

# REG_to_RSG_IC_2023_06.docx (misfiled — Intercompany Invoice)
generic_doc(
    "REG_to_RSG_IC_2023_06.docx",
    title="Intercompany-Rechnung REG → RSG — Juni 2023",
    intro=(
        f"Konzerninterne Verrechnung der Versicherungsumlage Juni 2023 fuer die Sparten Sach, "
        f"Maschinenbruch und Betriebsunterbrechung. Rechnungssteller: Brennhagen Elektronik GmbH "
        f"(REG), Heilbronn, als Anteilstraegerin der Master-Police; Rechnungsempfaenger: Brennhagen "
        f"Software GmbH (RSG), Muenchen. Verteilungsschluessel gemaess Konzern-Versicherungsumlage-"
        f"Richtlinie KRR-2022-09 (Headcount, Anlagenwert, Umsatzanteil)."
    ),
    body_paras=[
        (
            "Verrechnungspositionen Juni 2023: (i) Sach-Versicherung HDI, RSG-Anteil 8,2% gemaess "
            "Schluessel = 5.330 EUR; (ii) Maschinenbruch HDI, RSG-Anteil 4,1% = 273 EUR; "
            "(iii) Cyber-Versicherung Beazley, RSG-Anteil 18,5% (erhoehter Anteil wegen "
            "Software-Risikoprofil) = 6.475 EUR; (iv) D&O-Anteil pauschal 3.200 EUR; "
            "(v) sonstige Sparten (Vertrauensschaden, Rechtsschutz) anteilig 1.420 EUR. "
            "Summe netto: 16.698 EUR, zzgl. 19% USt 3.172,62 EUR, brutto 19.870,62 EUR."
        ),
        (
            "Rechtsgrundlage: Konzern-Service-Vertrag zwischen REG und RSG vom 1.1.2022, "
            "§ 4 Verrechnungsleistungen, Pos. 3 »Versicherungsumlage«. Die Verteilung erfolgt "
            "auf Cost-Plus-Basis mit 0% Aufschlag (durchlaufender Posten). Verrechnungspreis-"
            "Dokumentation gemaess OECD-TPG und § 90 Abs. 3 AO im Konzern-TP-Local-File "
            "dokumentiert.\n\nZahlungsziel: 30 Tage netto. Faelligkeit: 30. Juli 2023. "
            "Banknummer REG: Deutsche Bank Heilbronn. Buchung auf Sachkonto 4500 (Versicherungen)."
        ),
        (
            "Die Buchung erfolgt im Konzern-SAP-System (Konzern-Mandant 100) als IC-Transaktion "
            "mit Trading-Partner-Schluessel; Konsolidierungsausgleich erfolgt im Quartalsabschluss "
            "automatisch. Buchungsverantwortliche: bei REG Buchhalterin Frau Walter, bei RSG "
            "Frau Glaser. Pruefung der Umlage durch den Konzern-Controller Florian Maier "
            "im Rahmen des Quartals-Reviews."
        ),
    ],
)

# RHU_to_REG_IC_2023_11.docx (misfiled — IC Invoice)
generic_doc(
    "RHU_to_REG_IC_2023_11.docx",
    title="Intercompany-Rechnung RHU → REG — November 2023",
    intro=(
        f"Konzerninterne Erstattung von Versicherungsleistungen November 2023. Rechnungssteller: "
        f"Brennhagen Hungary Kft. (RHU), Gyoer; Rechnungsempfaenger: Brennhagen Elektronik GmbH (REG), "
        f"Heilbronn. Gegenstand: lokal in Ungarn vorab beglichene Pflicht-KFZ-Versicherungs-"
        f"Praemien sowie lokale Sachversicherungsanteile fuer die ungarische Pflichtdeckung, "
        f"deren wirtschaftliche Tragung gemaess Konzern-Versicherungsumlage-Richtlinie zentral "
        f"ueber REG erfolgt."
    ),
    body_paras=[
        (
            "Verrechnungspositionen November 2023: (i) Pflicht-KFZ-Haftpflichtversicherung "
            "fuer 24 in Ungarn zugelassene Konzern-Fahrzeuge (Allianz Hungary), Monatsanteil "
            "1.920 EUR; (ii) lokaler Sachversicherungsanteil HDI Hungary (Pflichtdeckung mit "
            "DIC zum Marsh-Master), Monatsanteil 2.450 EUR; (iii) gesetzliche Unfall-"
            "versicherung Ungarn (ungarisches Sozialversicherungssystem, NEAK), "
            "Monatsbeitrag arbeitgeberseitig 8.640 EUR. Summe netto: 13.010 EUR."
        ),
        (
            "Die ungarische Lokalversicherung dient ausschliesslich der Erfuellung lokaler "
            "Pflichten und ist subsidiaer zum Konzern-Master-Programm der Marsh. Die zentrale "
            "Tragung der Praemien erfolgt deshalb durch REG als Konzern-Versicherungstraeger. "
            "Verrechnung auf Cost-to-Cost-Basis ohne Aufschlag.\n\nDie Rechnung wird im "
            "SAP-System mit IC-Marker eingebucht und im Quartalsabschluss konsolidiert. "
            "Buchungsverantwortliche RHU: Andrea Szabo (HR/Buchhaltung); REG: Frau Walter. "
            "Pruefung durch Konzern-Controlling (Florian Maier)."
        ),
        (
            "Zahlungsziel: 30 Tage netto. Faelligkeit: 15. Dezember 2023. Bankverbindung RHU: "
            "OTP Bank Gyoer. Eine Stornierung der lokalen Pflichtversicherung zugunsten einer "
            "vollstaendigen Master-Konzeption wurde 2022 von Marsh geprueft; aufgrund "
            "ungarischer Pflichtversicherungsgesetzgebung (KFZ und Pflicht-UV) jedoch nicht "
            "umsetzbar. Die jaehrliche Bewertung erfolgt im Rahmen des Marsh-Renewals."
        ),
    ],
)

# RCZ_Kalibrierung_EMV-Prüfanlage_2023.docx (misfiled — calibration report)
generic_doc(
    "RCZ_Kalibrierung_EMV-Prüfanlage_2023.docx",
    title="Kalibrierungsnachweis EMV-Pruefanlage RCZ Brno 2023",
    intro=(
        f"Kalibrierungsnachweis fuer die EMV-Pruefanlage im Werk Brno (Brennhagen CZ s.r.o.), "
        f"erforderlich als Bestandteil der Risk-Engineering-Auflage der HDI Global SE im Rahmen "
        f"der Sach- und Maschinenbruchversicherung (Marsh-Wording 2023, Ziffer 4.2 »Pruefmittel "
        f"sicherheitsrelevanter Produktionsanlagen«). Der Nachweis dient gleichzeitig als "
        f"Konformitaetsnachweis gemaess IATF 16949 § 7.1.5 (Resourcen fuer Ueberwachung und Messung)."
    ),
    body_paras=[
        (
            "Pruefanlage: EMV-Halbanechoische Kammer der Marke ETS-Lindgren, Baujahr 2018, "
            "Inventarnummer RCZ-EMV-001, eingesetzt fuer EMV-Konformitaetspruefungen aller in "
            "Brno gefertigten Steckverbinder-Baugruppen. Kalibrierdatum: 14. November 2023. "
            "Kalibrierdienstleister: Rohde & Schwarz Praha s.r.o. (akkreditiert nach ISO/IEC "
            "17025). Kalibrierschein-Nr.: RS-CZ-2023-08714. Naechste Kalibrierung faellig: "
            "14. November 2024."
        ),
        (
            "Pruefergebnisse: alle Messparameter (Feldstaerke, Frequenzbereich 9 kHz bis 6 GHz, "
            "Antennen-Faktoren, Daempfungsglieder) innerhalb Toleranzgrenzen. Messunsicherheit "
            "konform zu CISPR 16-1-4. Kalibrierergebnis: »ohne Beanstandung, Anlage uneingeschraenkt "
            "freigegeben fuer Produkt-Konformitaetspruefungen«. Anlage als »kritisches Pruefmittel« "
            "gemaess Konzern-Q-Anweisung Q-RCZ-014 klassifiziert."
        ),
        (
            "Versicherungsrelevanz: Die Kalibrierung ist Voraussetzung fuer die Mitversicherung "
            "der Anlage in der Maschinenbruchpolice (HDI). Eine Kopie des Kalibrierscheins wird "
            "an Marsh ClientView Bei den Police-Dokumenten zur Anlage RCZ-EMV-001 hochgeladen. "
            "Die Risk-Engineering-Folgepruefung durch Marsh Risk Consulting ist fuer Q2/2024 "
            "vorgesehen (Begleitung durch Markus Hellbach)."
        ),
    ],
    signers=signatures(
        "Petr Novak", "Werkleiter RCZ", "Brennhagen CZ s.r.o.",
        "Eva Cerna", "Q-Leitung RCZ", "Brennhagen CZ s.r.o.",
        place="Brno", date_str_="20. November 2023",
    ),
)

# FTO_ADAS-V4D_BMW_2023.docx (misfiled — Freedom To Operate / IP-Statement)
generic_doc(
    "FTO_ADAS-V4D_BMW_2023.docx",
    title="Freedom-to-Operate-Stellungnahme ADAS-V4D fuer BMW-Lieferung 2023",
    intro=(
        f"Freedom-to-Operate-(FTO)-Stellungnahme fuer das Radar-Fusion-Steuergeraet ADAS-V4D, "
        f"das von der {R['name']} an die BMW Group geliefert wird. Die Stellungnahme dient als "
        f"Anlage zum BMW-Rahmenliefervertrag und ist insbesondere fuer die Mitversicherung in "
        f"der Konzern-Produkthaftpflichtpolice der AGCS sowie der Cyber-Police (sicherheits-"
        f"kritische OTA-Funktionalitaet) relevant."
    ),
    body_paras=[
        (
            "Pruefumfang der FTO: Die Patentabteilung der Brennhagen Elektronik AG (Leitung: "
            "Dipl.-Ing. Patentanwalt Dr. Markus Reuter, Boehmert & Boehmert) hat in Zusammenarbeit "
            "mit der externen Kanzlei Hoffmann Eitle (Muenchen) eine umfassende Patentrecherche "
            "in den Datenbanken DEPATISnet, EPO Espacenet und USPTO durchgefuehrt. Geprueft wurden "
            "die patentrechtlich relevanten Funktionsbloecke des ADAS-V4D: Radar-Fusion-Algorithmik, "
            "Sensor-Pre-Processing, Kommunikationsstack (AUTOSAR-Adaptive), OTA-Update-Mechanismus."
        ),
        (
            "Ergebnis: Es wurden 12 potenziell relevante Patente identifiziert (u.a. Bosch, "
            "Continental, Mobileye, Aptiv). Fuer 4 Patente besteht eine Lizenzvereinbarung (LVK), "
            "fuer 6 Patente wurde nach Pruefung keine Verletzung festgestellt (no infringement "
            "opinion durch Hoffmann Eitle), fuer 2 Patente (Aptiv US 11 234 567 B2 und "
            "Mobileye EP 3 456 789 B1) wurde eine Design-around-Implementierung in Firmware-"
            "Version 2.4 vorgenommen."
        ),
        (
            "Versicherungsrelevanz: Die FTO-Stellungnahme reduziert das Risiko fuer Patent-"
            "verletzungsklagen, die unter die Produkthaftpflichtpolice (AGCS) sowie die "
            "D&O-Police fallen koennten. Die Stellungnahme ist Bestandteil der Schadenpraevention "
            "und wird im Rahmen des jaehrlichen Risk-Engineering-Reviews durch Marsh erwaehnt. "
            "Eine Kopie wurde an BMW Patentabteilung (Dr. Klaus Reuter, BMW Group Patents) "
            "uebermittelt und ist Bestandteil der BMW-Lieferantenakte."
        ),
    ],
)

# INF_Lieferantenrisikobericht_2021.pdf — leave (PDF, not docx); but we have a .docx variant? -- skip if PDF
# REA_CON_ECU-900_QBR_2023_Q2.docx (misfiled — Quarterly Business Review)
generic_doc(
    "REA_CON_ECU-900_QBR_2023_Q2.docx",
    title="ECU-900 Quarterly Business Review Q2/2023 — Versicherungs-Aspekte",
    intro=(
        f"Vierteljaehrlicher QBR-Bericht fuer das Produkt ECU-900 (Powertrain-ECU Gen3, "
        f"Hauptkunde Volkswagen AG und Stellantis N.V.) mit Fokus auf versicherungs- und "
        f"risikorelevante Themen des Quartals Q2/2023. Erstellt durch Produktmanagement "
        f"ECU-900 in Abstimmung mit dem Konzern-Versicherungsbeauftragten und Marsh "
        f"Risk Consulting."
    ),
    body_paras=[
        (
            "Geschaeftsentwicklung Q2/2023: Stueckzahlausstoss ECU-900 192.000 Einheiten "
            "(+8% gg. Q1/2023); Umsatz 38,4 Mio. EUR; durchschnittliche FPY (First Pass Yield) "
            "98,4%. Lieferquote OEM-A (VW): 99,1%; OEM-B (Stellantis): 98,7%. Reklamations-PPM "
            "Q2: 12 ppm (Vorquartal 18 ppm). Keine sicherheitskritischen Felderausfaelle. "
            "Geringe Anzahl Reklamationen (8 Stueck) wurden im 8D-Prozess bearbeitet."
        ),
        (
            "Versicherungsrelevante Vorfaelle: Ein produkthaftpflichtrelevanter Vorfall im "
            "Quartal (Schadensmeldung SM-2023-0008, Lager-Korrosion bei einer Charge), "
            "Schadenshoehe ca. 95 TEUR, in Bearbeitung mit AGCS. Massnahme: Korrosions-"
            "schutzprozess der Lagerlogistik bei Spediteur DSV ueberarbeitet. Risk-Engineering-"
            "Empfehlung von Marsh (Markus Hellbach) wurde umgesetzt. Eine Anpassung der "
            "Produkthaftpflicht-Praemie ist nicht erforderlich (innerhalb Loss-Ratio-Bandbreite)."
        ),
        (
            "Risiken und Massnahmen H2/2023: (i) Markthochlauf VW MEB+ erwartet — Risikobewertung "
            "fuer CBI (Contingent Business Interruption) wird aktualisiert; (ii) neue Kundenanforderung "
            "Stellantis fuer Cyber-Resilience-Nachweis gemaess UNECE WP.29 — Anpassung der "
            "Cyber-Police im Renewal 2024 vorgesehen; (iii) FTO-Update geplant fuer Q3/2023 "
            "wegen neuer Patente in Konkurrenzanalyse.\n\nFolge-QBR: 25. Oktober 2023."
        ),
    ],
)

# RPL_Legal_Compliance_Report_2021.docx (misfiled — Legal Compliance Report)
generic_doc(
    "RPL_Legal_Compliance_Report_2021.docx",
    title="Legal Compliance Report RPL Katowice 2021 — Versicherungs-Compliance",
    intro=(
        f"Jaehrlicher Legal-Compliance-Bericht fuer die Brennhagen Polska Sp. z o.o. (RPL), "
        f"Geschaeftsjahr 2021, mit Schwerpunkt auf den versicherungsrechtlichen "
        f"Pflichten in Polen und der Integration in das Konzern-Versicherungsprogramm "
        f"der Marsh GmbH. Erstellt durch die lokale Rechtsabteilung RPL (Mecenas Anna "
        f"Kowalewska, Kowalewska & Partners) in Abstimmung mit Hengeler Mueller "
        f"(Frankfurt) und der Konzern-Versicherungsabteilung."
    ),
    body_paras=[
        (
            "Versicherungspflichten in Polen 2021: (i) Pflichthaftpflichtversicherung "
            "Werksbetrieb (OC ogolna) erfuellt durch lokale Police bei PZU SA mit DIC zum "
            "Marsh-Master; (ii) Pflicht-Sozialversicherung ZUS erfuellt; (iii) "
            "Berufsgenossenschaft (Wypadkowe) erfuellt mit erhoehter Beitragsklasse "
            "aufgrund Galvanik-Tatigkeit; (iv) Kfz-Pflichtversicherung OC + AC fuer 12 "
            "lokale Fahrzeuge bei Allianz Polen, integriert in Marsh-Master ueber "
            "Network-Police."
        ),
        (
            "Vorfaelle 2021: Ein Pflichtverletzungsvorwurf der Wojewodzki Inspektorat Ochrony "
            "Srodowiska (WIOS) wegen Grenzwertueberschreitung Galvanik-Abwasser (siehe "
            "Schadensmeldung SM-2023-0019 — Folge-Vorfall) wurde abschliessend in 2021 "
            "behoben (Bussgeld 12.000 PLN, Filteranlage gewartet). Lokale Compliance-Stelle "
            "(Marek Wojciechowski, Werkleiter) hat alle Auflagen erfuellt; Versicherungsschutz "
            "durch Konzern-Umwelthaftpflichtpolice (AGCS) bestaetigt."
        ),
        (
            "Ausblick 2022: (i) lokale Pflichtversicherungs-Renewals zum 1.1.2022 mit "
            "Marsh-Koordination; (ii) Anpassung der RPL-spezifischen DIC-Klauseln aufgrund "
            "neuer polnischer KSC-Cyber-Sicherheitsgesetzgebung; (iii) Integration der "
            "neuen SMD-Linie 4 in die Maschinenbruchpolice (Inventarmeldung an HDI bis "
            "30.4.2022); (iv) Update des lokalen Datenschutzkonzepts (RODO) als Teil der "
            "Cyber-Police-Underwriting-Voraussetzung. Verantwortlich: Anna Kowalska (HR), "
            "Marek Wojciechowski (Werkleitung)."
        ),
    ],
)

# PRJ-2024-001_Statusbericht_2024_03_ECU-1000_Concept_Study.docx
generic_doc(
    "PRJ-2024-001_Statusbericht_2024_03_ECU-1000_Concept_Study.docx",
    title="Projekt-Statusbericht PRJ-2024-001 — ECU-1000 Concept Study (Maerz 2024)",
    intro=(
        f"Projekt-Statusbericht fuer das Konzeptprojekt PRJ-2024-001 (ECU-1000 — naechste "
        f"Powertrain-ECU-Generation, Nachfolgegeneration ECU-900). Berichtszeitraum: "
        f"Maerz 2024. Projektleitung: Dipl.-Ing. Wolfgang Hertel (RSG Muenchen). "
        f"Berichts-Adressat: Steering Committee unter Vorsitz CTO Stefan Hoffmann (bis "
        f"30.6.2024) bzw. ab Q3/2024 Dr. Petra Hollmann. Versicherungsrelevante Aspekte "
        f"werden hier mit Blick auf die kuenftige Mitversicherung in der Konzern-"
        f"Produkthaftpflichtpolice dargestellt."
    ),
    body_paras=[
        (
            "Projektfortschritt Maerz 2024: Konzeptphase abgeschlossen zu 65%, Lasten-"
            "heft-Review mit Lead-OEM Volkswagen abgeschlossen, ASIL-D-Konzept (ISO 26262) "
            "in Erarbeitung. Patent-Screening durch Boehmert & Boehmert laeuft "
            "(FTO-Stellungnahme erwartet bis Q3/2024). Cyber-Security-Konzept gemaess "
            "ISO/SAE 21434 in Vorbereitung als Voraussetzung fuer kuenftige Mitversicherung "
            "in der Konzern-Cyber-Police (Munich Re Beazley)."
        ),
        (
            "Versicherungsrelevante Risiken in der Konzeptphase: (i) IP-Risiko Patentverletzung "
            "— wird durch FTO bewertet und ueber AGCS-Produkthaftpflichtpolice abgedeckt; "
            "(ii) Cyber-Risiken durch erweiterten OTA-Update-Mechanismus — Aufnahme in "
            "Cyber-Police-Renewal 2025 vorgesehen; (iii) Lieferketten-Risiken (Halbleiter-"
            "Sourcing TSMC und STMicroelectronics) — CBI-Klausel der BU-Police wird im "
            "Renewal entsprechend angepasst. Eskalation an Risk-Manager fortlaufend."
        ),
        (
            "Naechste Meilensteine Q2/2024: (i) Konzept-Review-Meeting mit Marsh "
            "Risk Consulting fuer Versicherbarkeitsbewertung; (ii) Abstimmung mit AGCS "
            "ueber Underwriting-Anforderungen fuer das neue Produkt; (iii) PPAP-Vorbereitung "
            "fuer OEM-Reviews. Budget Q1/2024 zu 92% planmaessig ausgeschoepft; "
            "Gesamtbudget Konzeptphase 4,2 Mio. EUR (Stand: 3,86 Mio. EUR committed). "
            "Eskalationsstufe: gelb (keine kritischen Abweichungen)."
        ),
    ],
)

# PRJ-2024-003_Status_2025_03_SAP_S_4HANA_Rol.docx
generic_doc(
    "PRJ-2024-003_Status_2025_03_SAP_S_4HANA_Rol.docx",
    title="Projekt-Statusbericht PRJ-2024-003 — SAP S/4HANA Rollout (Maerz 2025)",
    intro=(
        f"Statusbericht fuer das Konzern-IT-Projekt PRJ-2024-003 »SAP S/4HANA Rollout« "
        f"(Migrationsprojekt vom Legacy SAP ECC 6.0 auf S/4HANA 2023). Berichtszeitraum: "
        f"Maerz 2025. Projektleitung: Andreas Kremer (CIO RSG Muenchen) und Daniela Foerster "
        f"(SAP Lead Konzern). Adressat: Steering Committee unter Vorsitz CFO Laura Bauer. "
        f"Versicherungsbezug: Cyber-Police-Anforderungen, Risk-Engineering und "
        f"Betriebsunterbrechungs-Risiko waehrend Cutover."
    ),
    body_paras=[
        (
            "Projektfortschritt Maerz 2025: Phase Realize 2 abgeschlossen zu 78%, Datenmigrations-"
            "Probelaeufe mit Erfolg durchgefuehrt (3 Iterationen). Werke Heilbronn (REG), "
            "Muenchen (RSG) und Brno (RCZ) sind im Cutover-Plan fuer 1. Mai 2025 (Big-Bang-Ansatz "
            "fuer DE und CZ). Werke RPL (Katowice) und RHU (Gyoer) folgen im 2. Welle 1. Oktober "
            "2025. Cybersicherheits-Audit durch externe KPMG-Pruefer (Lead: Dr. Maximilian Brand) "
            "im Februar 2025 abgeschlossen — keine kritischen Befunde."
        ),
        (
            "Versicherungsrelevante Massnahmen: (i) Pre-Notification an Munich Re Beazley "
            "ueber den Cutover gemaess Cyber-Police Ziffer 4.7 (Major-Change-Notification) — "
            "erfolgt am 14. Maerz 2025; (ii) Erhoehung des Cyber-Sublimits »Betriebsunterbrechung"
            " durch Cyber-Vorfall« waehrend der Cutover-Phase im April-Mai 2025 von 10 Mio. EUR "
            "auf 25 Mio. EUR temporaer (Sondervereinbarung mit Beazley, Praemienzuschlag 18.000 "
            "EUR); (iii) BU-Police HDI: Pre-Notification ueber den Big-Bang-Cutover und "
            "Implementierung erweiterter Notfall-Backup-Verfahren (Hot-Standby ECC fuer 30 "
            "Tage nach Go-live)."
        ),
        (
            "Risiken und Eskalationen: (i) Schnittstelle zu Banking-System (Konzern-Treasury) "
            "noch nicht vollstaendig validiert — Test geplant 12. April 2025; (ii) Daten-"
            "qualitaetsprobleme in den Stammdaten der Materialnummern bei RPL — Bereinigung "
            "im Maerz/April abgeschlossen; (iii) Ausbildungsbedarf 240 Key-User — laeuft "
            "planmaessig. Eskalationsstufe: gelb. Budget 9,8 Mio. EUR (Stand 7,4 Mio. EUR "
            "committed). Risikomanager Markus Hellbach hat regelmaessige Status-Calls mit "
            "Marsh Risk Consulting zur Versicherbarkeit etabliert."
        ),
    ],
)

print("Done — regen_roehrig_17_versicherungen complete")
