"""Brennhagen AG – Highest-Priority Governance Docs (Vorstand, Aufsichtsrat, HV, HRB).

Covers a representative subset of 01_AG_Gesellschaftsrecht:
- 5 Aufsichtsrats-Dienstverträge
- 12 AR-Sitzungsprotokolle (2021-2023 Q1-Q4)
- 3 HV-Protokolle (2021, 2022, 2023)
- 4 HRB-Auszüge (2021-2024)
- 4 Vorstand-Bestellungsbeschlüsse
- 3 Directors-Dealings 2023
- 1 FRAND-Erklärung SEP 2023
- 1 Interne Revision HR 2023
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
from enhance_lib import ROEHRIG_AG as R, write_doc, signatures

BASE = f"{_ROOT}/roehrig_large/01_AG_Gesellschaftsrecht"
H = {"name": R["name"], "addr": R["addr"], "hrb": R["hrb"]}


# ── Aufsichtsrats-Dienstverträge (5) ────────────────────────────────────────
def ar_vertrag(fname, name, ausschuesse, expertise, jahresverguetung, bestelldatum):
    write_doc(f"{BASE}/{fname}", H,
        f"Dienstvertrag Aufsichtsrat – {name}",
        subtitle=f"Bestellung gemaess Hauptversammlungsbeschluss vom {bestelldatum}",
        sections=[
            ("Vertragsparteien",
             f"Brennhagen Elektronik AG, Vaihinger Strasse 120, 70567 Stuttgart, HRB 726451 AG Stuttgart, "
             f"vertreten durch den Vorstand (»Gesellschaft«), und {name} (»Aufsichtsratsmitglied«). "
             f"Die Bestellung erfolgt fuer die Amtsperiode bis zum Ende der ordentlichen Hauptversammlung, "
             f"die ueber die Entlastung fuer das Geschaeftsjahr 2025 beschliesst (Standard 4-Jahres-Periode "
             f"gemaess § 9 Abs. 2 der Satzung; max. 5 Jahre gemaess AktG)."),
            ("Vertragsregelungen",
             ("clauses", [
                 ("§ 1 Aufgaben", [
                     "Das Aufsichtsratsmitglied uebt sein Mandat hauptamtlich/ehrenamtlich nach Massgabe des "
                     "AktG, der Satzung der Brennhagen Elektronik AG und der Geschaeftsordnung des Aufsichtsrats aus.",
                     f"Mitarbeit in den Ausschuessen: {ausschuesse}.",
                     f"Eingebrachte Expertise: {expertise}.",
                 ]),
                 ("§ 2 Vergutung", [
                     f"Die Vergutung betraegt insgesamt {jahresverguetung} EUR brutto p. a. (fix), "
                     "auszahlbar in jeweils gleichen vierteljaehrlichen Tranchen, jeweils zum Quartalsende.",
                     "Zusaetzlich Sitzungsgeld: 1.500 EUR pro Plenarsitzung, 1.000 EUR pro Ausschuss-Sitzung. "
                     "Vorsitzende Ausschuss erhalten 1,5fache Vergutung; AR-Vorsitz erhaelt 3-fache Grund"
                     "vergutung; stellv. AR-Vorsitz 1,5fache.",
                     "Reisekostenerstattung nach den Grundsaetzen der Vorstandsreisekostenordnung "
                     "(Bahn 1. Klasse, Hotel 4-Sterne, Flug ab 4 Std. Reisedauer).",
                 ]),
                 ("§ 3 D&O / Haftung", [
                     "Die Gesellschaft unterhaelt eine D&O-Versicherung gemaess § 116 i. V. m. § 93 AktG "
                     "(Versicherer Allianz Global Corporate & Specialty SE, Versicherungssumme 50 Mio. EUR). "
                     "Das Aufsichtsratsmitglied ist als versicherte Person eingeschlossen.",
                     "Pflicht zur Sorgfalt eines ordentlichen und gewissenhaften Aufsichtsrats; "
                     "Verschwiegenheit gemaess § 116 i. V. m. § 93 Abs. 1 S. 3 AktG.",
                 ]),
                 ("§ 4 Compliance / Insider", [
                     "Beachtung der Marktmissbrauchsverordnung (MAR) sowie der Insider-Richtlinie der Gesellschaft. "
                     "Meldung von Eigengeschaeften (Directors' Dealings) gemaess Art. 19 MAR an BaFin und Gesellschaft.",
                     "Schwarz-Periode (Closed Periods) 30 Tage vor Veroeffentlichung Quartals-/Jahresberichte.",
                 ]),
                 ("§ 5 Vertragsdauer / Beendigung", [
                     "Vertragsdauer kongruent zur Amtsperiode des Aufsichtsratsmitglieds. Verlaengerung nur durch "
                     "Wiederwahl in der Hauptversammlung.",
                     "Eine ordentliche Kuendigung ist ausgeschlossen. Amtsniederlegung jederzeit moeglich, "
                     "spaetestens drei Monate zum Quartalsende; ausserordentliche Beendigung gemaess AktG.",
                 ]),
             ])),
            ("Unterschriften",
             signatures("Anna Mueller", "Vorstandsvorsitzende (CEO) i. V. Gesellschaft", R["name"],
                        name, "Aufsichtsratsmitglied", "i. e. S.",
                        place="Stuttgart", date_str_=bestelldatum)),
        ])


ar_vertrag("REA_AR_Dienstvertrag_Prof._Dr._Gerhard_Voss.docx", "Prof. Dr.-Ing. Gerhard Voss",
    "Pruefungsausschuss (Vorsitz); Innovations- und Technologieausschuss",
    "Technologie-Expertise Automotive Elektronik; ehem. Vorstandsmitglied Continental AG (Powertrain); "
    "Professor TU Muenchen (Embedded Systems)",
    "175.000", "14. Juni 2022")
ar_vertrag("REA_AR_Dienstvertrag_Dr._Klaus_Steinbrück.docx", "Dr. Klaus Steinbrueck",
    "Vorsitz Aufsichtsrat; Personalausschuss (Vorsitz); Praesidialausschuss",
    "Ehem. CEO ZF Friedrichshafen AG; Ehem. Vorstandsmitglied Mahle GmbH; Industrie-Erfahrung Tier-1-Lieferant",
    "320.000", "14. Juni 2022")
ar_vertrag("REA_AR_Dienstvertrag_Dr._Ingrid_Schöllkopf.docx", "Dr. Ingrid Schoellkopf",
    "Pruefungsausschuss (stellv. Vorsitz); Compliance- und Risikoausschuss",
    "Wirtschaftspruefung (Diplom-Kauffrau, Steuerberaterin); ehem. Partner bei KPMG; Ueberbruecker "
    "fuer Sanierungen / komplexe Reorganisation",
    "115.000", "14. Juni 2022")
ar_vertrag("REA_AR_Dienstvertrag_Marlies_Dürr.docx", "Marlies Duerr",
    "Personalausschuss; Innovations- und Technologieausschuss",
    "Arbeitnehmervertreterin (Vorsitzende Konzernbetriebsrat); IG Metall; Schwerpunkt Personal- und "
    "Sozialpolitik, Transformation, Mitbestimmung",
    "95.000", "14. Juni 2022")
ar_vertrag("REA_AR_Dienstvertrag_Thomas_Reinhardt_MdB.docx", "Thomas Reinhardt (MdB)",
    "Compliance- und Risikoausschuss; Praesidialausschuss",
    "Politische Expertise (Mitglied des Deutschen Bundestages 2017-2021, Wirtschaftsausschuss); "
    "ehem. Geschaeftsfuehrer mittelstaendisches Industrieunternehmen; Schwerpunkt Public Affairs",
    "115.000", "14. Juni 2022")


# ── AR-Sitzungsprotokolle (12 Q1-Q4 für 2021/2022/2023) ──────────────────────
def ar_protokoll(fname, datum, quartal, jahr, ar_themen, vorstands_bericht, beschluesse):
    write_doc(f"{BASE}/{fname}", H,
        f"Sitzungsprotokoll Aufsichtsrat – {quartal} {jahr}",
        subtitle=f"Sitzung am {datum} – Vaihinger Strasse 120, 70567 Stuttgart",
        sections=[
            ("Teilnehmende",
             "Aufsichtsrat: Dr. Klaus Steinbrueck (Vorsitzender), Prof. Dr.-Ing. Gerhard Voss (stellv. Vorsitz, "
             "Pruefungsausschuss-Vorsitz), Dr. Ingrid Schoellkopf, Marlies Duerr (Arbeitnehmervertreterin), "
             "Thomas Reinhardt (MdB).\n\n"
             "Geladen Vorstand: Anna Mueller (CEO), Laura Bauer (CFO), Dr. Thomas Weber (COO), "
             "Stefan Hoffmann (CTO).\n\n"
             "Wirtschaftspruefung (sofern relevant): KPMG AG WPG, Dr. Maximilian Brand (Partner)."),
            ("Tagesordnung", ("list", ar_themen)),
            ("Bericht des Vorstands", vorstands_bericht),
            ("Beschluesse / Aktionspunkte", beschluesse),
            ("Schluss", f"Die Sitzung wurde um 18:30 Uhr geschlossen. Naechste Sitzung gemaess Sitzungsplan."),
            ("Unterschriften",
             signatures("Dr. Klaus Steinbrueck", "Aufsichtsratsvorsitzender", R["name"],
                        "Anna Mueller", "Vorstandsvorsitzende", R["name"],
                        place="Stuttgart", date_str_=datum)),
        ])


def std_themen(zusatz=None):
    base = [
        "TOP 1 Genehmigung Protokoll Vorquartal",
        "TOP 2 Bericht Vorstand zum Geschaeftsverlauf",
        "TOP 3 Berichterstattung Pruefungsausschuss / Compliance",
        "TOP 4 Wesentliche M&A- und Investitionsvorhaben",
        "TOP 5 Personalentwicklung Vorstand / 1. Fuehrungsebene",
        "TOP 6 Strategische Themen und Beschluesse",
        "TOP 7 Bericht aus den Ausschuessen",
        "TOP 8 Verschiedenes",
    ]
    if zusatz: base.insert(6, zusatz)
    return base


ar_protokoll("REA_AR_Sitzungsprotokoll_2021_Q1.docx", "18. Februar 2021", "Q1", "2021",
    std_themen("TOP 6.1 Neukundenaufnahme BMW Group – Auftrag InfoConnect Pro (ICP-3)"),
    "CEO Anna Mueller berichtet ueber den herausfordernden Geschaeftsstart 2021: Lieferketten-Engpaesse bei "
    "Halbleitern (TSMC / NXP) belasten alle Tochterwerke. Auftragslage Automotive: stabil, Bedarf an "
    "ADAS-Modulen und Infotainment-Loesungen waechst. CFO Laura Bauer praesentiert Quartalsergebnisse "
    "(Konzern): Umsatz 142 Mio. EUR (Plan 138 Mio.), EBITDA 17,8 Mio. EUR (Plan 16,5 Mio.). "
    "Auftragsbestand 1,8 Mrd. EUR.",
    "Aufsichtsrat genehmigt einstimmig die Aufnahme der Vertragsverhandlungen mit BMW Group fuer "
    "InfoConnect Pro Linie 3 (ICP-3) mit erwartetem Volumen 850 Mio. EUR ueber 5 Jahre. Ferner einstimmige "
    "Zustimmung zum Investitionsvorhaben Werkserweiterung Heilbronn (Linie 3, 22 Mio. EUR; ROI 4,1 Jahre). "
    "Beauftragung an Vorstand: Ausschreibung halbjaehrliche Lieferantenpruefung kritischer Halbleiter ab Q2/2021.")

ar_protokoll("REA_AR_Sitzungsprotokoll_2021_Q2.docx", "12. Mai 2021", "Q2", "2021",
    std_themen("TOP 6.1 BMW-ICP-3 Vertragsabschluss; TOP 6.2 Werk Katowice (Polen) – Erweiterung um 1.500 m² SMD"),
    "Vorstand berichtet ueber den erfolgreichen Vertragsabschluss BMW ICP-3 (Volumen 850 Mio. EUR, "
    "Laufzeit 5+2 Jahre, RFQ-Score 1,8 von max. 5,0). Werk Katowice meldet Bedarf an Produktionserweiterung "
    "auf Grundlage des erwarteten Mehrvolumens. Lieferketten-Situation Halbleiter: Lieferzeit STM und NXP "
    "von 18 Wochen auf 32 Wochen verschoben; Risikobewertung wird vorgelegt.",
    "Aufsichtsrat genehmigt die Werkserweiterung Katowice um 1.500 m² SMD-Linie (Investitionsvolumen "
    "18,5 Mio. EUR, gefoerdert durch polnische Sonderwirtschaftszone). Beauftragung Vorstand: Aufbau "
    "Zweitquelle Halbleiter-Lieferanten (Renesas, Infineon) bis Q4/2021. Beschluss-Nr. AR-2021-Q2-04.")

ar_protokoll("REA_AR_Sitzungsprotokoll_2021_Q3.docx", "18. August 2021", "Q3", "2021",
    std_themen(),
    "CFO berichtet Halbjahreszahlen: Umsatz 290 Mio. EUR (+8,4 % YoY), EBITDA 36,5 Mio. EUR (Marge 12,6 %). "
    "Operative Performance robust trotz Lieferketten-Belastungen. CMO/CTO praesentieren technologische "
    "Roadmap: BMS-12 Batteriemanagement (BEV) als strategischer Wachstumspfad ab 2023; Roadmap erfordert "
    "F&E-Investitionsanstieg um 12 Mio. EUR ab 2022.",
    "Aufsichtsrat befuerwortet die Roadmap BMS-12 und genehmigt das ausserordentliche F&E-Budget "
    "+12 Mio. EUR fuer 2022 (Auftragslage VW BMS, Hyundai BMS in Verhandlung). Vorstand wird ermaechtigt, "
    "weitere Joint-Innovation-Partnerschaften mit Fraunhofer ISC und Bosch zu pruefen.")

ar_protokoll("REA_AR_Sitzungsprotokoll_2021_Q4.docx", "8. Dezember 2021", "Q4", "2021",
    std_themen("TOP 6.1 Budget 2022 / Mehrjahresplanung 2022-2024"),
    "CFO praesentiert Budget 2022 / Mehrjahresplanung 2022-2024: Umsatzwachstum von 595 (2021) auf "
    "740 Mio. EUR (2024), CAGR 7,5 %; EBITDA-Marge stabil 12-13 %. F&E-Anteil steigt von 5,2 % auf "
    "6,5 %. CAPEX 2022 geplant 48 Mio. EUR (Halbleiter-Pruefstaende, BMS-Linie Heilbronn, ADAS-Test"
    "infrastruktur Muenchen).",
    "Aufsichtsrat genehmigt das Budget 2022 sowie die Mehrjahresplanung 2022-2024 in der vorgelegten Fassung. "
    "Dividendenvorschlag 2021 (Beschluss zur HV 2022): 1,40 EUR/Aktie (Vorjahr 1,20 EUR; entspricht "
    "Ausschuettungsquote 35 %). Vorstand wird beauftragt, Q1/2022 eine Lieferanten-Risk-Map "
    "Halbleiter vorzulegen.")

ar_protokoll("REA_AR_Sitzungsprotokoll_2022_Q1.docx", "22. Februar 2022", "Q1", "2022",
    std_themen("TOP 6.1 Ukraine-Krieg: Lieferketten- und Sanktionsfolgen"),
    "CEO informiert ueber Auswirkungen des Russland-Ukraine-Krieges: keine direkten Lieferantenbeziehungen "
    "Russland/Belarus; indirekte Lieferketten (Cobalt, Magnesium, Neon-Gas fuer Lithografie) bedingt belastet. "
    "Sanktionspruefungen verstaerkt. Werk Polen Katowice meldet keine Stoerung; Mitarbeitende solidarisch "
    "mit Ukraine, freiwillige Hilfe organisiert.",
    "Aufsichtsrat nimmt den Sanktionsbericht zur Kenntnis. Beauftragt Vorstand: monatlicher Update an "
    "Pruefungsausschuss zu Lieferkette und Sanktions-Compliance. Genehmigung 'Solidaritaetsfonds Ukraine' "
    "in Hoehe von 500 TEUR (humanitaere Hilfe). Beschluss-Nr. AR-2022-Q1-08.")

ar_protokoll("REA_AR_Sitzungsprotokoll_2022_Q2.docx", "18. Mai 2022", "Q2", "2022",
    std_themen("TOP 6.1 IPO Status; TOP 6.2 KPMG Audit-Vorbereitung"),
    "CFO berichtet ueber Q1: Umsatz 158 Mio. EUR (+11 %), EBITDA 19,8 Mio. EUR. IPO-Prozess (geplantes "
    "Listing Prime Standard Q4/2022) verlaeuft planmaessig: Banken-Beauty-Contest abgeschlossen, "
    "Deutsche Bank + Berenberg + Commerzbank ausgewaehlt als Joint Bookrunners; Bewertungs-Range "
    "1,8-2,3 Mrd. EUR Marktkapitalisierung. KPMG bestaetigt Audit-Vorbereitung im Plan.",
    "Aufsichtsrat genehmigt einstimmig den IPO-Plan, das Pricing-Konzept und die Beauftragung der "
    "Joint Bookrunner. Prospekt-Genehmigung BaFin: erwartet Q3/2022. Listing-Termin: 14. Oktober 2022 "
    "geplant. Vorstand wird ermaechtigt, alle erforderlichen Investorengespraeche zu fuehren.")

ar_protokoll("REA_AR_Sitzungsprotokoll_2022_Q3.docx", "22. September 2022", "Q3", "2022",
    std_themen("TOP 6.1 Finale IPO-Vorbereitung; TOP 6.2 Compliance-Audit Hauptzollamt"),
    "Halbjahres-Performance positiv: Umsatz 305 Mio. EUR (+11 % YoY), EBITDA 39,5 Mio. EUR (Marge 13,0 %). "
    "IPO-Roadshow startet 26. September 2022; Treffen mit ueber 80 institutionellen Investoren (DACH/UK/US) "
    "geplant. Compliance-Audit Hauptzollamt (AEO) ohne Beanstandung abgeschlossen.",
    "Aufsichtsrat bestaetigt den finalen IPO-Plan inkl. Bookbuilding-Range 22,00-26,00 EUR/Aktie "
    "(Marktkapitalisierung 1,90-2,25 Mrd. EUR). Volumen 25 % Streubesitz (15 Mio. neue Aktien + 10 Mio. "
    "Sekundaer-Anteile). Verwendung Emissionserloes: F&E-Investitionen, Internationalisierung China-Werk, "
    "Schuldenrueckfuehrung.")

ar_protokoll("REA_AR_Sitzungsprotokoll_2022_Q4.docx", "14. Dezember 2022", "Q4", "2022",
    std_themen("TOP 6.1 IPO Rueckblick; TOP 6.2 Budget 2023 / Mehrjahresplanung 2023-2025"),
    "IPO am 14. Oktober 2022 erfolgreich abgeschlossen: Emissionskurs 24,50 EUR (Mittelfeld der Range), "
    "Erstnotierung +8 %, aktuelle Marktkapitalisierung 2,15 Mrd. EUR. Erloes 612 Mio. EUR; davon Schulden"
    "rueckfuehrung 180 Mio. EUR; F&E-/CAPEX-Programm 280 Mio. EUR; Investitionsreserve 152 Mio. EUR. "
    "Budget 2023 sieht Umsatz 650 Mio. EUR vor (+9 %), EBITDA-Marge 13,5 %.",
    "Aufsichtsrat genehmigt das Budget 2023 und die Mehrjahresplanung 2023-2025. Genehmigt zudem "
    "Investitionspakete (a) Werk Heilbronn BMS-12 Produktionslinie 28 Mio. EUR; (b) Werk Shanghai "
    "Ausbau 18 Mio. EUR; (c) ADAS-Testzentrum Muenchen 12 Mio. EUR.")

ar_protokoll("REA_AR_Sitzungsprotokoll_2023_Q1.docx", "14. Februar 2023", "Q1", "2023",
    std_themen("TOP 6.1 First-Time Reporting Prime Standard"),
    "Erster Quartalsbericht im Prime Standard verlief erfolgreich (Investoren-Telefonkonferenz mit "
    "ueber 120 Teilnehmern). Geschaeftsverlauf Q4/2022 (testiert): Umsatz Q4 161 Mio. EUR (+9 %), "
    "Gesamtjahr 2022 600 Mio. EUR (+11 %). Auftragsbestand 31.12.2022: 2,1 Mrd. EUR.",
    "Aufsichtsrat genehmigt den Jahresabschluss 2022 (testiert KPMG, uneingeschraenkt) und den "
    "Lagebericht. Vorschlag zur HV: Dividende 1,80 EUR/Aktie (+29 % YoY); Auschuettungsquote 36 %. "
    "Wahl KPMG fuer 2023 wird zur HV vorgeschlagen.")

ar_protokoll("REA_AR_Sitzungsprotokoll_2023_Q2.docx", "11. Mai 2023", "Q2", "2023",
    std_themen("TOP 6.1 Strategie 2026 'NEXT'; TOP 6.2 Pruefungsausschuss Bericht"),
    "Vorstand praesentiert ueberarbeitete Strategie 2026 'NEXT' mit drei Saeulen: (1) BEV / Battery Mgmt; "
    "(2) ADAS Level 2-3 Premiumprodukte; (3) Energie-Software-as-a-Service (neue Saeule, recurring revenue). "
    "Q1-Ergebnisse: Umsatz 162 Mio. EUR (+11 %), EBITDA 22 Mio. EUR. Auftragsbestand stabil bei 2,1 Mrd. EUR.",
    "Aufsichtsrat befuerwortet Strategie 2026 'NEXT'. Genehmigt Ausgliederung der Software-Aktivitaeten in "
    "neue Tochter (Brennhagen Software GmbH wird gestaerkt; ggfs. spaetere Einheit fuer Carve-Out). Beauftragt "
    "Vorstand mit detaillierter Umsetzungsroadmap bis Q3/2023.")

ar_protokoll("REA_AR_Sitzungsprotokoll_2023_Q3.docx", "14. September 2023", "Q3", "2023",
    std_themen("TOP 6.1 H1-Ergebnisse; TOP 6.2 Auftrag VW BMS-12 Update"),
    "Halbjahres-Performance 2023: Umsatz 322 Mio. EUR (+13 %), EBITDA 41 Mio. EUR (Marge 12,7 %). "
    "Auftrag VW BMS-12 fuer ID.7 (Volumen 280 Mio. EUR / Laufzeit 7 Jahre) Vertragsverhandlungen final - "
    "Closing erwartet 30. September 2023. CAPEX-Status 2023: 38 Mio. EUR (78 % geplant)Investitionsfortschritt "
    "Werk Heilbronn BMS-Linie 65 %.",
    "Aufsichtsrat genehmigt einstimmig den Abschluss des VW BMS-12 Vertrages (Beschluss-Nr. AR-2023-Q3-12); "
    "informiert sich detailliert ueber den IBN-Plan; befuerwortet Investitions-Aufstockung Werk Heilbronn "
    "um 4 Mio. EUR fuer zusaetzliche Kapazitaeten BMS-12.")

ar_protokoll("REA_AR_Sitzungsprotokoll_2023_Q4_FINAL.docx", "8. Dezember 2023", "Q4", "2023",
    std_themen("TOP 6.1 Budget 2024 / Mehrjahresplanung 2024-2026; TOP 6.2 Personalauswahl Vorstand"),
    "CFO praesentiert Budget 2024 (Umsatz 700 Mio. EUR +14 %, EBITDA 95 Mio. EUR Marge 13,6 %) und "
    "Mehrjahresplanung 2024-2026 (CAGR 11 %, EBITDA-Marge 14 % bis 2026). CEO informiert ueber Wechsel "
    "im Vorstand: Stefan Hoffmann (CTO) wechselt zum 30. Juni 2024 zu einem Wettbewerber; Nachfolger:in "
    "wird gesucht (Suche extern, Headhunter Egon Zehnder).",
    "Aufsichtsrat genehmigt Budget 2024 und Mehrjahresplanung 2024-2026. Bezueglich CTO-Nachfolge wird "
    "der Praesidialausschuss (Vorsitz Steinbrueck) mit der Auswahl beauftragt; Zielsetzung Besetzung bis "
    "30. April 2024. Genehmigt die ESOP-Anpassung 2024 (zusaetzliche Vesting-Tranche fuer Vorstand).")


# ── HV-Protokolle (3) ──────────────────────────────────────────────────────
def hv_protokoll(fname, datum, gj, dividende_eur, entlastung_pct, beschluesse_zusatz=""):
    write_doc(f"{BASE}/{fname}", H,
        f"Hauptversammlungs-Protokoll – {datum}",
        subtitle=f"Ordentliche Hauptversammlung ueber das Geschaeftsjahr {gj}",
        sections=[
            ("Eroeffnung und Versammlungsleitung",
             f"Die ordentliche Hauptversammlung der Brennhagen Elektronik AG fand am {datum} um 10:00 Uhr in der "
             f"Liederhalle Stuttgart, Berliner Platz 1, 70174 Stuttgart, statt. Versammlungsleiter: "
             f"Aufsichtsratsvorsitzender Dr. Klaus Steinbrueck. Notarin: Dr. Karin Sonneborn, Stuttgart "
             f"(UR-Nr. NS-HV-{gj}/1). Praesenz: {84 + int(gj)*0.1:.1f} % des stimmberechtigten Grundkapitals."),
            ("Tagesordnung",
             ("list", [
                 f"TOP 1 Vorlage des Jahres- und Konzernabschlusses {gj}, des Lageberichts und des Berichts "
                 "des Aufsichtsrats",
                 "TOP 2 Beschluss ueber die Verwendung des Bilanzgewinns",
                 "TOP 3 Beschluss ueber die Entlastung der Mitglieder des Vorstands",
                 "TOP 4 Beschluss ueber die Entlastung der Mitglieder des Aufsichtsrats",
                 "TOP 5 Wahl des Abschlusspruefers fuer das folgende Geschaeftsjahr (KPMG AG WPG)",
                 "TOP 6 Beschluesse zu Aktionsthemen (Ermaechtigung Eigene Aktien, Genehmigtes Kapital)",
                 "TOP 7 Wahlen zum Aufsichtsrat (sofern relevant)",
             ])),
            ("Bericht des Vorstands",
             f"CEO Anna Mueller berichtet ueber das Geschaeftsjahr {gj}. Wesentliche Eckpunkte: "
             f"Konsolidierter Umsatz {580 if gj=='2020' else 595 if gj=='2021' else 600 if gj=='2022' else 612}.0 Mio. EUR; "
             f"EBITDA-Marge zwischen 12,4 % und 13,2 %. Strategie 'NEXT' (Battery Mgmt, ADAS, Software-as-a-Service) "
             "im Plan. Auftragsbestand auf Rekordhoehe (>2,0 Mrd. EUR). Mitarbeitende: 4.180. "
             "Q&A: 14 Aktionaersfragen, vorwiegend zu Halbleiter-Lieferkette und ESG-Strategie."),
            ("Bericht des Aufsichtsrats",
             "AR-Vorsitzender Dr. Steinbrueck legt den Bericht des Aufsichtsrats vor: 4 ordentliche Sitzungen, "
             "ein Pruefungsausschuss-Bericht (10 Sitzungen), Personalausschuss (4 Sitzungen), Praesidial"
             "ausschuss (2 Sitzungen). Aufsichtsrat hat alle wesentlichen Geschaefte vorab geprueft und "
             "begleitet. Vergutungsbericht gemaess § 162 AktG wurde vorgelegt."),
            ("Wesentliche Beschluesse",
             ("clauses", [
                 ("TOP 1 Vorlage", [
                     f"Jahres- und Konzernabschluss {gj} wurden uneingeschraenkt testiert von KPMG AG WPG "
                     "(Bericht im Geschaeftsbericht abgedruckt). Die Hauptversammlung nimmt die Vorlagen zur "
                     "Kenntnis.",
                 ]),
                 ("TOP 2 Verwendung Bilanzgewinn", [
                     f"Beschluss: Dividende von {dividende_eur} EUR je Stueckaktie. Ausschuettungsbetrag "
                     f"insgesamt {int(float(dividende_eur)*62.5):,} Mio. EUR (62,5 Mio. Stueckaktien). "
                     f"Auszahlung am 4. Bankarbeitstag nach Beschluss."
                 ]),
                 ("TOP 3 Entlastung Vorstand", [
                     f"Entlastung der Vorstandsmitglieder fuer {gj} wird mit {entlastung_pct} % der "
                     "abgegebenen Stimmen erteilt.",
                 ]),
                 ("TOP 4 Entlastung Aufsichtsrat", [
                     f"Entlastung der Aufsichtsratsmitglieder fuer {gj} mit ueber 98 % der Stimmen erteilt.",
                 ]),
                 ("TOP 5 Wahl Abschlusspruefer", [
                     f"KPMG AG WPG wird zum Abschlusspruefer fuer das Geschaeftsjahr {int(gj)+1} bestellt "
                     "(Beschluss mit 99,4 % der Stimmen).",
                 ]),
                 ("TOP 6 Sonstige Beschluesse", [beschluesse_zusatz or
                     "Ermaechtigung zum Erwerb eigener Aktien gemaess § 71 Abs. 1 Nr. 8 AktG (bis 10 % "
                     "des Grundkapitals, Laufzeit 5 Jahre).",
                 ]),
             ])),
            ("Schluss",
             f"Die Hauptversammlung wird um 14:45 Uhr geschlossen. Saemtliche Beschluesse werden notariell "
             f"beurkundet. Eine Anfechtungsklage wurde nicht angekuendigt. "),
            ("Unterschriften",
             signatures("Dr. Klaus Steinbrueck", "Versammlungsleiter / AR-Vorsitz", R["name"],
                        "Dr. Karin Sonneborn", "Notarin", "i. e. S.",
                        place="Stuttgart", date_str_=datum)),
        ])


hv_protokoll("REA_HV_Protokoll_2021.docx", "20. Mai 2021", "2020", "1.20", 98.4)
hv_protokoll("REA_HV_Protokoll_2022.docx", "14. Juni 2022", "2021", "1.40", 98.7,
    "Ergaenzend: Wahl Aufsichtsrat (5 Mitglieder); Vorbereitung Boersengang Prime Standard.")
hv_protokoll("REA_HV_Protokoll_2023.docx", "8. Juni 2023", "2022", "1.80", 99.1,
    "Ergaenzend: Genehmigung Vergutungssystem Vorstand 2023-2027 (Say-on-Pay); Anpassung Satzung an Anforderungen "
    "Prime Standard nach IPO 2022.")


# ── HRB-Auszüge (4) ─────────────────────────────────────────────────────────
def hrb_auszug(fname, jahr, eintragungen, grundkapital_jahr):
    write_doc(f"{BASE}/{fname}", H,
        f"Handelsregisterauszug HRB 726451 – Stand {jahr}",
        subtitle="Auszug aus dem Handelsregister beim Amtsgericht Stuttgart",
        sections=[
            ("Firma und Sitz",
             "Firma: Brennhagen Elektronik AG (vormals Brennhagen Elektronik GmbH bis Formwechsel 2020).\n"
             "Sitz: Stuttgart.\n"
             "Geschaeftsanschrift: Vaihinger Strasse 120, 70567 Stuttgart.\n"
             "Geschaeftszweck: Entwicklung, Herstellung und Vertrieb elektronischer Bauteile und Systeme "
             "fuer die Automobilindustrie."),
            ("Grundkapital / Stamm",
             f"Grundkapital (Stand {jahr}): {grundkapital_jahr} EUR. Aktien: 62,5 Mio. Stueck-Inhaber-Aktien "
             "ohne Nennwert (rechnerischer Anteil je Aktie 1,00 EUR). Boersennotiert seit 14.10.2022 im "
             "Prime Standard der Frankfurter Wertpapierboerse (WKN RHGRP1, ISIN DE000RHGRP12)."),
            ("Vorstand",
             "- Anna Mueller (Vorsitzende / CEO), Stuttgart\n"
             "- Laura Bauer (CFO), Stuttgart\n"
             "- Dr. Thomas Weber (COO), Heilbronn\n"
             "- Stefan Hoffmann (CTO), Muenchen [bis 30.6.2024 in Funktion]\n\n"
             "Vertretungsregelung: Jedes Vorstandsmitglied vertritt die Gesellschaft gemeinschaftlich mit "
             "einem weiteren Vorstandsmitglied oder mit einem Prokuristen."),
            ("Aufsichtsrat",
             "- Dr. Klaus Steinbrueck (Vorsitzender, seit 2022)\n"
             "- Prof. Dr.-Ing. Gerhard Voss (stellv. Vorsitz, Pruefungsausschuss-Vorsitz, seit 2022)\n"
             "- Dr. Ingrid Schoellkopf (seit 2022)\n"
             "- Marlies Duerr (Arbeitnehmervertreterin, seit 2022)\n"
             "- Thomas Reinhardt (MdB, seit 2022)"),
            ("Eintragungen / Veraenderungen Berichtsjahr",
             "\n\n".join(eintragungen) if isinstance(eintragungen, list) else eintragungen),
            ("Bekanntmachungen",
             "Pflichtbekanntmachungen erfolgen im Bundesanzeiger sowie auf der Website der Gesellschaft "
             "(www.brennhagen-elektronik.de/investor-relations). Aufsichtsbehoerde: BaFin (Bundesanstalt fuer "
             "Finanzdienstleistungsaufsicht), Bonn / Frankfurt."),
        ])


hrb_auszug("REA_HRB_Auszug_2021.docx", "2021", [
    "10.2.2021: Wechsel der Rechtsform von Brennhagen Elektronik GmbH auf Brennhagen Elektronik AG (Formwechselbeschluss "
    "vom 12.10.2020, Eintragung mit Wirkung 1.1.2021).",
    "10.2.2021: Bestellung der vier Vorstandsmitglieder (Mueller, Bauer, Weber, Hoffmann).",
    "10.2.2021: Bestellung erster Aufsichtsrat (Steinbrueck, Voss, Schoellkopf, Duerr, Reinhardt).",
    "22.6.2021: Genehmigtes Kapital I/2021 ueber 6.250.000 EUR (10 % Grundkapital) bis 21.6.2026.",
], "62.500.000")
hrb_auszug("REA_HRB_Auszug_2022.docx", "2022", [
    "14.10.2022: Boersengang im Prime Standard der Frankfurter Wertpapierboerse (WKN RHGRP1, ISIN DE000RHGRP12).",
    "14.10.2022: Kapitalerhoehung aus Genehmigtem Kapital um 15.000.000 EUR (Ausgabe 15 Mio. Neuer Stueckaktien).",
    "14.6.2022: Neubestellung der fuenf Aufsichtsratsmitglieder (Steinbrueck, Voss, Schoellkopf, Duerr, "
    "Reinhardt) fuer die Amtsperiode bis HV 2026.",
], "62.500.000")
hrb_auszug("REA_HRB_Auszug_2023.docx", "2023", [
    "8.6.2023: Genehmigtes Kapital II/2023 ueber 3.125.000 EUR (5 % Grundkapital) bis 7.6.2028.",
    "8.6.2023: Ermaechtigung zum Erwerb eigener Aktien (5 % des Grundkapitals, Laufzeit 5 Jahre).",
    "31.12.2023: Stand 0,8 % Eigene Aktien (Rueckkauf laufend, Verwendung Aktienoptionsprogramme).",
], "62.500.000")
hrb_auszug("REA_HRB_Auszug_2024.docx", "2024", [
    "14.2.2024: Veroeffentlichung Jahresfinanzbericht 2023 (testiert KPMG, uneingeschraenkt).",
    "20.6.2024: Anstehende HV: Wiederbestellung KPMG; Anpassung Vergutungssystem.",
    "Ausstehende Veraenderungen: CTO-Wechsel zum 30.6.2024 (Nachfolger:in zur Bekanntgabe).",
], "62.500.000")


# ── Vorstand-Bestellungsbeschlüsse (4) ─────────────────────────────────────
def vorst_bestellung(fname, name, funktion, hintergrund, jahresfix, ltp_pct):
    write_doc(f"{BASE}/{fname}", H,
        f"Vorstandsbestellung – {name} – {funktion}",
        subtitle="Beschluss des Aufsichtsrats gemaess § 84 AktG",
        sections=[
            ("Beschlussfassung",
             f"Der Aufsichtsrat der Brennhagen Elektronik AG hat in seiner Sitzung am unter Beschluss-Nr. "
             f"AR-{name.split()[-1][:3].upper()} mit allen abgegebenen Stimmen beschlossen, {name} "
             f"als Mitglied des Vorstandes zu bestellen."),
            ("Funktion und Hintergrund",
             f"Funktion: {funktion}.\n\n"
             f"Hintergrund: {hintergrund}"),
            ("Vertragseckpunkte",
             ("clauses", [
                 ("§ 1 Bestellungszeitraum", [
                     "Die Bestellung erfolgt fuer eine erste Amtsperiode von 4 Jahren (entsprechend der "
                     "Regel-Bestellungsdauer; max. 5 Jahre gemaess § 84 AktG).",
                 ]),
                 ("§ 2 Vergutung", [
                     f"Jahresbruttofixgehalt: {jahresfix} EUR (zwoelf Monatsraten).",
                     f"Short-Term-Incentive (STI): bis zu {ltp_pct} % vom Fixgehalt bei Zielerreichung; "
                     "Bemessungsgrundlage: konsolidiertes EBIT und individuelle Ziele.",
                     "Long-Term-Incentive (LTI): Performance Share Plan ueber 4 Jahre (Vesting), Ziel TSR / "
                     "EBIT-CAGR; Maximalwert 200 % vom Zielwert. LTI-Zielwert pro Tranche: 100 % vom Fixgehalt.",
                     "Dienstwagen, D&O-Versicherung, betriebliche Altersversorgung 14 % vom Fixgehalt p. a.",
                 ]),
                 ("§ 3 Nachvertragliches Wettbewerbsverbot", [
                     "12 Monate; Karenzentschaedigung 50 % der zuletzt bezogenen Festvergutung.",
                 ]),
                 ("§ 4 Anwendbares Recht", [
                     "Es gilt deutsches Recht. Streitigkeiten werden durch das Landgericht Stuttgart entschieden.",
                 ]),
             ])),
            ("Unterschriften",
             signatures("Dr. Klaus Steinbrueck", "Vorsitz Aufsichtsrat", R["name"],
                        name, "Vorstandsmitglied", "i. e. S.",
                        place="Stuttgart", date_str_="—")),
        ])


vorst_bestellung("REA_Vorstand_Bestellung_Dr._Petra_Hollmann.docx", "Dr. Petra Hollmann",
    "Chief Technology Officer (CTO)",
    "Promotion Elektrotechnik (RWTH Aachen, 2008); 14 Jahre Continental AG (Senior Director ADAS Engineering); "
    "Wechsel zu Brennhagen Elektronik AG zum 1. Juli 2024 als Nachfolgerin von Stefan Hoffmann (CTO bis 30.6.2024). "
    "Spezialisierung: ADAS / autonomes Fahren, Sensorfusion, Edge-KI.",
    "385.000", "60")
vorst_bestellung("REA_Vorstand_Bestellung_Dr._Yuki_Tanaka.docx", "Dr. Yuki Tanaka",
    "Chief Regional Officer Asia / Vorstand International",
    "Promotion Wirtschaftswissenschaften (Hitotsubashi University, Tokio); 18 Jahre bei Denso Corp. (zuletzt "
    "Senior Vice President APAC). Bestellung mit Wirkung 1. April 2024 zur Erweiterung des Asien-Geschaefts "
    "(Werk Shanghai und Asien-Vertrieb).",
    "320.000", "55")
vorst_bestellung("REA_Vorstand_Bestellung_Klaus-Peter_Zimmermann.docx", "Klaus-Peter Zimmermann",
    "Chief Operations Officer (COO) [Mandat als Stellvertretung beendete vorzeitig]",
    "Maschinenbauingenieur TU Stuttgart; 22 Jahre bei Robert Bosch GmbH (zuletzt Werkleiter Hildesheim). "
    "Bestellung mit Wirkung 1. Januar 2018 als COO der Brennhagen Elektronik GmbH (damals noch GmbH). "
    "Mandat zum 31. Dezember 2022 einvernehmlich beendet; Nachfolger Dr. Thomas Weber.",
    "298.000", "55")
vorst_bestellung("REA_Vorstand_Bestellung_Stefan_Richter.docx", "Stefan Richter",
    "Chief Marketing & Business Development Officer (Vorstandsmitglied / verantwortlich Akquise)",
    "Diplom-Wirtschaftsingenieur TU Muenchen; 16 Jahre bei Siemens AG (zuletzt SVP Automotive Business Unit); "
    "Bestellung zum 1. April 2023, mit Fokus auf Akquise neuer OEM-Programme und Vertriebsentwicklung "
    "Tier-1.",
    "310.000", "55")


# ── Directors' Dealings 2023 (3) ───────────────────────────────────────────
def dd_meldung(fname, name, funktion, transaktion, anzahl, preis, datum, art="Kauf"):
    write_doc(f"{BASE}/{fname}", H,
        f"Directors' Dealing Meldung – {name} – {transaktion}",
        subtitle=f"Meldung gemaess Art. 19 MAR / SSCR Reportingpflicht",
        sections=[
            ("Meldepflichtige Person",
             f"{name}, Funktion: {funktion} der Brennhagen Elektronik AG."),
            ("Transaktionsdetails",
             [["Detail", "Wert"],
              ["Art der Transaktion", art],
              ["Wertpapier", "Brennhagen Elektronik AG Stueckaktien (ISIN DE000RHGRP12)"],
              ["Anzahl Stueckaktien", str(anzahl)],
              ["Preis je Aktie (EUR)", str(preis)],
              ["Gesamtvolumen (EUR)", f"{anzahl*preis:,.2f}".replace(',','.')],
              ["Datum der Transaktion", datum],
              ["Ort der Transaktion", "Frankfurter Wertpapierboerse / Xetra"]]),
            ("Erklaerung",
             "Die Transaktion erfolgte ausserhalb der Schwarzphase (Closed Periods) und unter Beachtung "
             "der gesetzlichen Vorgaben gemaess Art. 19 MAR. Die Meldung wurde fristgerecht binnen "
             "3 Bankarbeitstagen an die BaFin sowie an die Brennhagen Elektronik AG (Compliance Officer) "
             "uebermittelt. Veroeffentlichung im Bundesanzeiger sowie auf der Investor-Relations-Webseite "
             "erfolgt unverzueglich. Schwellenwert von 20.000 EUR p. a. wurde ueberschritten."),
            ("Bestaetigung",
             "Eigenerklaerung: Es bestand zum Zeitpunkt der Transaktion keine Insider-Kenntnis ueber nicht "
             "oeffentlich bekannte kursrelevante Informationen. Eigene Geschaeft erfolgte ausschliesslich "
             "auf Basis oeffentlich verfuegbarer Informationen."),
            ("Unterschrift",
             signatures(name, funktion, R["name"],
                        "Compliance Officer Brennhagen AG", "Empfangsbestaetigung", R["name"],
                        place="Stuttgart", date_str_=datum)),
        ])


dd_meldung("REA_Directors_Dealings_Dr._Petra_Hollmann_2023.docx", "Dr. Petra Hollmann",
    "Vorstandsmitglied (CTO, Antritt 1.7.2024)", "Erstkauf Brennhagen Aktien als Antrittsinvestition",
    2000, 22.40, "14. Mai 2023")
dd_meldung("REA_Directors_Dealings_Dr._Yuki_Tanaka_2023.docx", "Dr. Yuki Tanaka",
    "Vorstandsmitglied (CRO Asia, Antritt 1.4.2024)", "Pre-Antrittskauf Aktien",
    1500, 23.10, "18. Oktober 2023")
dd_meldung("REA_Directors_Dealings_Stefan_Richter_2023.docx", "Stefan Richter",
    "Vorstandsmitglied (CMO / BD)", "Performance-Share-Plan Vesting Tranche 2023",
    4500, 0.00, "8. April 2023", art="Vesting (kein Kaufpreis, Aktiengewaehr aus LTI)")


# ── Weitere wichtige Docs ─────────────────────────────────────────────────
write_doc(f"{BASE}/REA_FRAND_Erklaerung_SEP_2023.docx", H,
    "FRAND-Erklaerung – Standardessenzielle Patente 2023",
    subtitle="Erklaerung zur Lizenzbereitschaft nach FRAND-Grundsaetzen (Fair, Reasonable, Non-Discriminatory)",
    sections=[
        ("Hintergrund",
         "Die Brennhagen Elektronik AG haelt eine Reihe von Patenten, die im Rahmen der Standardisierungs"
         "verfahren (insbesondere ISO 11898 CAN-FD, AUTOSAR Adaptive Platform, IEEE 802.3bw 100BASE-T1, "
         "DoIP Diagnose-over-IP, ISO 26262 Funktionale Sicherheit) als »standardessenziell« (SEP, "
         "Standard-Essential Patent) deklariert sind."),
        ("Erklaerung",
         "Die Brennhagen Elektronik AG erklaert hiermit gemaess Art. 102 AEUV und der einschlaegigen "
         "Rechtsprechung des EuGH (Huawei/ZTE-Entscheidung), dass sie ihre standardessenziellen Patente "
         "zu fairen, angemessenen und nicht diskriminierenden (FRAND) Bedingungen lizensiert. "
         "Diese Erklaerung ergeht im Rahmen der Verpflichtungen gegenueber den Standardisierungs-Organisationen "
         "(SDO) ISO, IEEE und ETSI."),
        ("SEP-Portfolio",
         [["Standard", "Patente / Schutzrechte (Stueck)", "Jurisdiktion", "Lizenzfeld"],
          ["ISO 11898 CAN-FD", "12", "EP, US, CN, JP", "Steuergeraete OEM"],
          ["AUTOSAR Adaptive Platform", "4", "EP, US", "Software-Plattform"],
          ["IEEE 802.3bw 100BASE-T1", "6", "EP, US, CN", "Automotive Ethernet"],
          ["DoIP Diagnose-over-IP", "3", "EP, US", "Diagnose / OBD"],
          ["ISO 26262 Funktionale Sicherheit", "5", "EP, US, JP", "Safety-Architekturen"],
          ["SUMME", "30", "", ""]]),
        ("Lizenzkonditionen",
         "Lizenzkonditionen werden im Einzelfall fair und transparent verhandelt. Lizenzanalogie / "
         "Royalty-Stack-Vergleich erfolgt auf Basis von Industriestandards. Beispielroyalty CAN-FD: "
         "0,12-0,18 EUR pro Geraet (gemaess Vergleich mit Bosch / NXP). FRAND-Beratung durch Hengeler Mueller "
         "(Patentlizenzierung) sowie unabhaengiger Patentanwaltskanzlei Maiwald."),
        ("Streitfaelle",
         "Aktuell keine laufenden FRAND-Streitfaelle. Eine Pruefung der eigenen Lizenzpraxis durch externe "
         "Berater (Hengeler Mueller, Berlin) erfolgt jaehrlich; letzte Pruefung 14. November 2023, ohne "
         "Beanstandungen."),
        ("Unterschriften",
         signatures("Stefan Hoffmann", "CTO", R["name"],
                    "Laura Bauer", "CFO", R["name"],
                    place="Stuttgart", date_str_="14. Dezember 2023")),
    ])


write_doc(f"{BASE}/REA_Interne_Revision_HR_2023.docx", H,
    "Interne-Revision-Bericht HR-Prozesse 2023",
    subtitle="Pruefbericht der Internal Audit Funktion (Lead: Andreas Buehler, Chief Audit Executive)",
    sections=[
        ("Pruefungsauftrag",
         "Pruefung der HR-Prozesse der Brennhagen Elektronik AG (Konzernperspektive sowie Stichprobenpruefung "
         "in den Werken Heilbronn (REG) und Muenchen (RSG)). Pruefzeitraum 1. Januar bis 31. Dezember 2023. "
         "Pruefungsmandat ausgesprochen durch den Pruefungsausschuss am 14. Februar 2023; Berichts-Empfaenger "
         "Vorstand und Pruefungsausschuss."),
        ("Pruefumfang",
         ("list", [
             "Rekrutierungsprozesse (Stellenausschreibung, Auswahl, Anstellung)",
             "Vergutungs- und Tantieme-Prozesse (Festgehalt, STI, LTI)",
             "Mitbestimmungsprozesse (Betriebsrat / Konzernbetriebsrat)",
             "Datenschutz HR-Daten (Sage HR, SuccessFactors)",
             "Reisekosten- und Bewirtungsabrechnungen (Stichprobe 5 %)",
             "Mitarbeiteraustritte (Aufhebungsvertraege, Outplacement)",
             "Diversity / Equal-Pay-Reporting",
         ])),
        ("Wesentliche Pruefungs-Findings",
         [["#", "Finding", "Schwere", "Empfehlung"],
          ["1", "Stichprobenmaessige Inkonsistenz bei Tantieme-Berechnung (3 Faelle, Werk Heilbronn)", "Mittel", "Re-Calibrierung Berechnungstool Q1/2024"],
          ["2", "AVV-Vertraege mit Recruiting-Dienstleister Hays nicht vollstaendig (1 Standort)", "Mittel", "Vervollstaendigung binnen 30 Tagen"],
          ["3", "Reisekostenabrechnung: 4 Faelle (von 80) mit fehlenden Belegen", "Niedrig", "Schulung erweitert; pauschale Rueckforderung 1.840 EUR"],
          ["4", "Equal-Pay-Reporting fehlt formal (LkSG-Anforderung)", "Mittel", "Erstellung Q2/2024"],
          ["5", "Mitarbeiter-Onboarding-Checkliste nicht in allen Tochterwerken einheitlich", "Niedrig", "Konzernweite Standardisierung 2024"]]),
        ("Empfohlene Massnahmen",
         "(a) Aktualisierung der HR-Verfahrensanweisungen (zentral); (b) Schulung HR-Sachbearbeitende "
         "(Q2/2024); (c) Einfuehrung eines konzernweiten HR-Dashboards (Power BI) mit KPI-Monitoring; "
         "(d) Equal-Pay-Audit durch externen Anbieter (Mercer) als Vorbereitung CSRD-Reporting."),
        ("Status der Behebung",
         "Alle Findings sind dem Vorstand zur Behebung uebertragen. Statusbericht zum 30. Juni 2024 wird "
         "an Pruefungsausschuss vorgelegt. Wiederholungspruefung Q4/2024 vorgesehen."),
        ("Unterschriften",
         signatures("Andreas Buehler", "Chief Audit Executive (CAE)", R["name"],
                    "Prof. Dr.-Ing. Gerhard Voss", "Vorsitz Pruefungsausschuss", R["name"],
                    place="Stuttgart", date_str_="22. Januar 2024")),
    ])


print("OK regen_roehrig_governance.py – ~30 high-priority governance docs written")
