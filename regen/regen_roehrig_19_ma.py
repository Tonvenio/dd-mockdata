"""Brennhagen Elektronik AG – 19_MA_Transaktionen.

Enriches all 55 thin docs in roehrig_large/19_MA_Transaktionen:
- DD-Berichte / LoI / SPA-Auszuege / NDA / Integration Plans
  for the documented historic acquisitions: Brennhagen Czech (2018), Brennhagen
  Hungary (2019), Shanghai JV Konsolidierung (2021).
- M&A Pipeline 2023/2024 working papers, Bewertungsmodelle, Finanzanalysen,
  Synergieberechnungen, First-Approach-Memos, Management-Meeting-Protokolle,
  Target-Screenings, DD-Working-Papers (Stefan Richter / Goldman Sachs /
  Roland Berger / KPMG / Hengeler Mueller / PwC).
- Plus: Teaser strategischer Prozess 2024, NDA-Register, ECR BMW BMS-12,
  PRJ-2023-005 Status, RCN-Steuerbescheid 2021, REG-Lohnsteuer 2021.
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

BASE = f"{_ROOT}/roehrig_large/19_MA_Transaktionen"
H = {"name": R["name"], "addr": R["addr"], "hrb": R["hrb"]}


# ─────────────────────────────────────────────────────────────────────────────
# Historic acquisitions referenced in filenames (Czech, Hungary, Shanghai JV)
# These are pre-IPO transactions on subsidiary level (acquisition of additional
# stake / consolidation into Brennhagen Holding GmbH).
# ─────────────────────────────────────────────────────────────────────────────

DEALS = {
    "czech": {
        "target_full": "Brennhagen Czech s.r.o. (vormals ElektroBrno s.r.o.)",
        "target_short": "Brennhagen Czech s.r.o.",
        "sitz": "Brno (CZ), Vinarska 460/9, 603 00 Brno-stred",
        "ico": "IC 27485102, KS Brno, oddil C, vlozka 51284",
        "tx_typ": "Share Deal – Erwerb 100 % der Geschaeftsanteile (vormals 49 % JV-Anteil bestehend)",
        "kaufpreis": "EUR 14,2 Mio. (Enterprise Value)",
        "earn_out": "EUR 1,8 Mio. Earn-Out (EBITDA-Hurdle 2019/2020)",
        "signing": "18. September 2018",
        "closing": "12. November 2018 (nach Kartellfreigabe BWB Wien fuer Konzernanteil ueber 5 Mio. CZK)",
        "berater_ma": "Goldman Sachs International (Frankfurt) – Lead Senior Banker Dr. Klaus Bessler",
        "berater_legal": "Hengeler Mueller (Frankfurt) – Lead Partner Dr. Martin Klusmann",
        "berater_finddd": "KPMG Deal Advisory (Frankfurt) – Lead Director Susanne Lehmann",
        "berater_taxdd": "PwC Tax (Prag) – Lead Tax Director Tomas Havel",
        "berater_techdd": "Roland Berger Muenchen – Lead Partner Dr. Stefan Vogel",
        "goodwill": "EUR 6,4 Mio. Goodwill (PPA gemaess IFRS 3)",
        "rationale": "Vollkonsolidierung Steckverbinder-Produktion Brno; Beendigung JV mit lokalem "
                     "Partner Bohemia Connector a.s. (49 % verbleibender Anteil).",
        "tax_strukt": "Tax-Step-Up nicht moeglich (Share Deal); Verschmelzung mit Brennhagen Holding "
                      "geprueft, jedoch verworfen (lokale CIT-Vorteile in CZ).",
        "mitarb": "678 Mitarbeitende (Stand Closing)",
        "umsatz_target": "EUR 71,4 Mio. (FY 2017)",
        "ebitda_target": "EUR 8,9 Mio. (FY 2017; Marge 12,5 %)",
        "year": "2018",
    },
    "hungary": {
        "target_full": "Brennhagen Hungary Kft. (vormals SensorTech Hungaria Kft.)",
        "target_short": "Brennhagen Hungary Kft.",
        "sitz": "Gyoer (HU), Ipari Park ut 14, 9027 Gyoer",
        "ico": "Cg.08-09-027841, Cegbirosag Gyoer",
        "tx_typ": "Asset Deal / Share Deal kombiniert – Erwerb 100 % der Geschaeftsanteile sowie "
                  "ergaenzender Erwerb des Produktionsgrundstuecks (5,4 ha)",
        "kaufpreis": "EUR 22,8 Mio. (Enterprise Value, davon EUR 4,1 Mio. Grundstueck-Kaufpreis)",
        "earn_out": "EUR 2,4 Mio. Earn-Out (Sensorik-Umsatz 2020/2021)",
        "signing": "14. Mai 2019",
        "closing": "30. Juli 2019 (nach Kartellfreigabe GVH Budapest)",
        "berater_ma": "Goldman Sachs International (Frankfurt) – Lead Senior Banker Dr. Klaus Bessler",
        "berater_legal": "Hengeler Mueller (Frankfurt) – Local Counsel: Kinstellar Budapest",
        "berater_finddd": "KPMG Deal Advisory Budapest – Lead Partner Akos Becsey",
        "berater_taxdd": "PwC Tax (Budapest) – Lead Tax Andras Szilagyi",
        "berater_techdd": "Roland Berger Muenchen – Lead Partner Dr. Stefan Vogel; technische DD vor Ort durch "
                          "Brennhagen Engineering Heilbronn",
        "goodwill": "EUR 9,8 Mio. Goodwill (PPA gemaess IFRS 3)",
        "rationale": "Sensorik-Kompetenzaufbau (Inertialsensoren, Drucksensoren); Erweiterung des "
                     "Produktportfolios fuer ADAS-Anwendungen; Nutzung niedriger Lohnkosten-Standort.",
        "tax_strukt": "Asset-Deal-Teil ermoeglicht Step-Up auf Sensorik-Maschinenpark; AfA-Vorteil "
                      "EUR 0,6 Mio. p. a. ueber 10 Jahre.",
        "mitarb": "542 Mitarbeitende (Stand Closing)",
        "umsatz_target": "EUR 38,2 Mio. (FY 2018)",
        "ebitda_target": "EUR 4,7 Mio. (FY 2018; Marge 12,3 %)",
        "year": "2019",
    },
    "shanghai": {
        "target_full": "Brennhagen (Shanghai) Co. Ltd. (Konsolidierung JV-Restanteil 35 % von Yangtze Electronics)",
        "target_short": "Brennhagen (Shanghai) Co. Ltd.",
        "sitz": "Shanghai (CN), 88 Pudong Avenue, Building B, 200120 Shanghai",
        "ico": "Unified Social Credit Code 91310115MA1FL42Q38",
        "tx_typ": "Equity Transfer Agreement (ETA) – Erwerb verbleibender 35 % JV-Anteile zur Vollkonsolidierung",
        "kaufpreis": "EUR 8,4 Mio. (RMB 65 Mio. zum Stichtagskurs 1 EUR = 7,75 RMB)",
        "earn_out": "Keine (Festpreis-Strukturierung)",
        "signing": "8. Maerz 2021",
        "closing": "21. Juni 2021 (nach Anmeldung MOFCOM Shanghai und SAFE-Genehmigung Kapitalruekfluss)",
        "berater_ma": "Goldman Sachs Asia (Hongkong) – Lead Senior Banker Dr. Klaus Bessler",
        "berater_legal": "Hengeler Mueller (Frankfurt) – Local Counsel: King & Wood Mallesons Shanghai",
        "berater_finddd": "KPMG Deal Advisory Shanghai – Lead Partner Frank Liu",
        "berater_taxdd": "PwC Tax (Shanghai) – Lead Tax Director Wendy Chen",
        "berater_techdd": "Roland Berger Shanghai – Lead Partner Denis Depoux",
        "goodwill": "EUR 2,1 Mio. Goodwill",
        "rationale": "Konsolidierung des Asien-Vertriebs unter alleiniger Kontrolle; Schutz vor "
                     "Wettbewerbsverhalten des JV-Partners; Vorbereitung Ausbau Produktion BMS-12 China.",
        "tax_strukt": "Equity Transfer Tax 10 % auf Veraeusserungsgewinn (China-Withholding) durch "
                      "Verkaeufer zu tragen; Steuerklausel im ETA verankert.",
        "mitarb": "298 Mitarbeitende (Stand Closing)",
        "umsatz_target": "EUR 28,4 Mio. (FY 2020)",
        "ebitda_target": "EUR 2,1 Mio. (FY 2020; Marge 7,4 %)",
        "year": "2021",
    },
}


# ── DD-Bericht (Financial / Commercial / Legal / Tech) ─────────────────────
def dd_bericht(fname, deal_key):
    d = DEALS[deal_key]
    write_doc(f"{BASE}/{fname}", H,
        f"Due-Diligence-Bericht (konsolidiert) – {d['target_short']} ({d['year']})",
        subtitle=f"Financial / Commercial / Legal / Tax / Technical DD – Stand: pre-Closing {d['year']}",
        confidential=True,
        sections=[
            ("Transaktionsgegenstand",
             f"Zielgesellschaft: {d['target_full']}.\n"
             f"Sitz: {d['sitz']}.\n"
             f"Registereintrag: {d['ico']}.\n\n"
             f"Transaktionstyp: {d['tx_typ']}.\n"
             f"Kaufpreis-Indikation: {d['kaufpreis']} zzgl. {d['earn_out']}.\n"
             f"Geplanter Signing-Termin: {d['signing']}; Closing: {d['closing']}.\n\n"
             f"Strategische Logik / Deal-Rationale: {d['rationale']}"),
            ("DD-Beraterteam",
             [["Workstream", "Berater", "Lead"],
              ["M&A-Lead / Banker", "Goldman Sachs Frankfurt", "Dr. Klaus Bessler (Senior Banker)"],
              ["Legal DD", d['berater_legal'], "Hengeler Mueller Team"],
              ["Financial DD", d['berater_finddd'], "KPMG Deal Advisory"],
              ["Tax DD", d['berater_taxdd'], "PwC Tax Team"],
              ["Technical / Commercial DD", d['berater_techdd'], "Roland Berger"],
              ["Strategie-DD intern", "Brennhagen BD/M&A", "Stefan Richter (Vorstand BD ab 4/2023)"]]),
            ("Financial Due Diligence (KPMG)",
             "Untersuchungsgegenstand: Quality of Earnings (QoE) FY 2016–2018 (Czech / Hungary) bzw. "
             "FY 2018–2020 (Shanghai), Working Capital, Net Debt-Definition, Cash-Conversion, "
             "Auftragsbestand und Kunden-Konzentration. Adjustments QoE: Bereinigung um Einmal"
             "effekte (Restrukturierung 2017, FX-Sondereffekte, Management-Boni). "
             f"Reported EBITDA der Zielgesellschaft: {d['ebitda_target']}; Bereinigtes EBITDA: "
             f"+EUR 0,8 Mio. (ueber QoE). Umsatz: {d['umsatz_target']}. Working-Capital-Normalisierung: "
             "Inventory-Tage 92, DSO 64, DPO 71. Net-Debt-Stichtag: lokale Bankverbindlichkeiten "
             "EUR 3,8 Mio., Pensionsrueckstellungen EUR 1,2 Mio., Operating Lease EUR 0,9 Mio.\n\n"
             f"Mitarbeitende: {d['mitarb']}. Personalintensive Bereiche: Produktion (78 %), "
             "Entwicklung (12 %), Verwaltung (10 %). Personal-Risiken: Tarifvertrag mit lokaler "
             "Gewerkschaft (CZ/HU); Loehne unter Bundesdurchschnitt."),
            ("Commercial DD (Roland Berger)",
             "Marktposition: Top-5-Anbieter im jeweiligen lokalen Segment; Kundenkonzentration "
             "moderat (Top-3-Kunden = 52 % Umsatz). Wachstumsperspektive: 5,8 % CAGR (Marktstudie "
             "Roland Berger 2018/2019). Synergie-Potenzial mit Brennhagen-Plattform: Cross-Selling "
             "ICP-3/ADAS, Einkaufs-Bundling Halbleiter, Konzern-IT-Migration. Synergien quantifiziert: "
             "Run-Rate EUR 2,1 Mio./Jahr ab Jahr 3 (vor Integrationskosten EUR 3,8 Mio. einmalig). "
             "Wettbewerbsanalyse: Hauptwettbewerber Continental Automotive Hungary, Robert Bosch CZ, "
             "Marquardt CZ. Wettbewerbsvorteil Target: Naehe zu OEM-Werken (Skoda Mlada Boleslav, "
             "Audi Gyoer, VW Bratislava)."),
            ("Legal DD (Hengeler Mueller)",
             "Geprueft: Gesellschaftsrechtliche Verhaeltnisse (vollstaendige Eigentumskette), wesentliche "
             "Vertraege (Top-15 Kunden- und Lieferantenvertraege, Mietvertraege, Lizenzvereinbarungen), "
             "Arbeitsrecht (Tarifvertrag, Sozialplan, individuelle Schluesselpersonenvertraege), "
             "Compliance (Sanktions-Screening, Anti-Korruption, GDPR/AVV), Litigation (3 anhaengige "
             "Verfahren, max. Exposure EUR 0,6 Mio.), IP-Rechte (12 angemeldete Patente, 4 erteilt). "
             "Wesentliche Findings: Change-of-Control-Klauseln in 4 Kundenvertraegen (Audi, Skoda, "
             "Continental, ZF) erfordern Konsent oder Notification. Risikoeinschaetzung: niedrig "
             "bis mittel; Mitigations in SPA verankert (Garantien, Freistellungen, W&I)."),
            ("Tax DD (PwC)",
             f"Geprueft: Koerperschaftsteuer (CIT), Umsatzsteuer (VAT/MwSt), Lohnsteuer, "
             f"Verrechnungspreise (TP). Steuerstrukturierung: {d['tax_strukt']}. "
             "Wesentliche Findings: (a) TP-Dokumentation Local File ueber 2 Jahre nachzubessern; "
             "(b) Vorsteuer-Abzug aus Konzern-Cost-Recharges in 2 Jahren formal mangelhaft "
             "(Risikoexposure EUR 0,4 Mio., in SPA als spezifische Freistellung); (c) keine "
             "wesentlichen Tax Holidays oder Foerdermittel mit Clawback-Risiko."),
            ("Technical / Operational DD",
             "Produktionsanlagen: Maschinenpark Durchschnittsalter 8,4 Jahre; CAPEX-Nachholbedarf "
             "EUR 2,8 Mio. (SMD-Linien-Modernisierung). IATF-16949-Zertifizierung gueltig. ASPICE-"
             "Reife L2 (Czech), L1 (Hungary), nicht relevant (Shanghai). EHS: keine Altlasten-Befunde; "
             "Umweltgutachten (Phase-I-ESA) durch ERM ohne wesentliche Findings. IT: Migration auf "
             "Brennhagen-SAP-S/4HANA-Template binnen 18 Monaten geplant; Migrationsbudget EUR 1,4 Mio."),
            ("Bewertung / Kaufpreis-Bruecke",
             [["Position", "Wert"],
              ["Enterprise Value (EV)", d['kaufpreis']],
              ["./. Net Debt (Stichtag)", "EUR 5,9 Mio."],
              ["+/- Working-Capital-Anpassung (Target NWC)", "EUR 0,3 Mio."],
              ["./. Pensionsrueckstellungen", "EUR 1,2 Mio."],
              ["= Equity Value (vor Earn-Out)", "—"],
              ["+ Earn-Out (max.)", d['earn_out']],
              ["= Total Purchase Consideration (max.)", "—"]]),
            ("Empfehlung",
             "Das DD-Team empfiehlt den Erwerb zu den verhandelten Konditionen. Restrisiken sind "
             "durch (a) W&I-Versicherungspolice (Versicherer AIG, Versicherungssumme EUR 8 Mio., "
             "Selbstbehalt 0,5 % EV), (b) spezifische Verkaeufer-Freistellungen (Tax, Litigation), "
             f"(c) Earn-Out-Struktur und (d) Goodwill-Werthaltigkeits-Tests (jaehrlich gemaess IAS 36) "
             f"abgedeckt. PPA gemaess IFRS 3 ergibt: {d['goodwill']}. Vorstand und Aufsichtsrat "
             "wurden gemaess Bericht in Sitzung vorab informiert; AR-Zustimmung wird im naechsten "
             "Plenum eingeholt."),
            ("Verteiler / Unterschriften",
             signatures("Stefan Richter", "Vorstand BD / M&A (intern Projektleitung)", R["name"],
                        "Dr. Klaus Bessler", "Senior Banker, Goldman Sachs Frankfurt", "Goldman Sachs",
                        place="Frankfurt am Main", date_str_=d['signing'])),
        ])


dd_bericht("DD_Bericht_Erwerb_Brennhagen_Czech_s.r.o._2018.docx", "czech")
dd_bericht("DD_Bericht_Erwerb_Brennhagen_Hungary_Kft._2019.docx", "hungary")
dd_bericht("DD_Bericht_Konsolidierung_Shanghai_JV_→_1_2021.docx", "shanghai")


# ── LoI / Term Sheet ────────────────────────────────────────────────────────
def loi(fname, deal_key):
    d = DEALS[deal_key]
    write_doc(f"{BASE}/{fname}", H,
        f"Letter of Intent / Term Sheet – {d['target_short']}",
        subtitle=f"Indikativ – nicht-bindend (mit Ausnahme der Exklusivitaets- und Vertraulichkeitsklauseln)",
        confidential=True,
        sections=[
            ("Praeambel",
             f"Zwischen der Brennhagen Elektronik AG (»Erwerberin« bzw. »Brennhagen«), Vaihinger Strasse 120, "
             f"70567 Stuttgart, vertreten durch den Vorstand, und den Veraeusserern (Eigentuemer bzw. "
             f"verbleibende JV-Partner) der {d['target_full']} (»Zielgesellschaft«), {d['sitz']}, "
             f"besteht die gemeinsame Absicht, den im nachfolgenden Term Sheet skizzierten Erwerb "
             f"vorzubereiten und – vorbehaltlich der erfolgreichen Due Diligence sowie der Zustimmung "
             f"der jeweiligen Gremien – zum Abschluss zu bringen."),
            ("Eckpunkte des geplanten Erwerbs",
             ("clauses", [
                 ("§ 1 Transaktionsstruktur", [
                     f"Geplante Strukturierung: {d['tx_typ']}.",
                     "Erwerberin ist die Brennhagen Holding GmbH (100%-ige Tochter der Brennhagen Elektronik AG); "
                     "auf Erwerberseite handeln die Vorstaende der Holding sowie der Konzernobergesellschaft.",
                 ]),
                 ("§ 2 Kaufpreis (indikativ)", [
                     f"Indikative Kaufpreis-Bandbreite (Enterprise Value): {d['kaufpreis']}.",
                     f"Zusaetzlicher Earn-Out (max.): {d['earn_out']}, bemessen anhand des EBITDA der "
                     "Zielgesellschaft fuer die ersten zwei vollen Geschaeftsjahre nach Closing.",
                     "Kaufpreismechanik: Locked-Box ab dem Stichtag 31.12. des Vorjahres bzw. alternativ "
                     "Completion Accounts mit Working-Capital- und Net-Debt-Anpassung. Mechanik wird "
                     "im Rahmen der SPA-Verhandlungen final festgelegt.",
                 ]),
                 ("§ 3 Conditions Precedent", [
                     "Erfolgreicher Abschluss der finanziellen, rechtlichen, steuerlichen und technischen "
                     "Due Diligence durch die Erwerberin.",
                     "Zustimmung des Aufsichtsrats der Brennhagen Elektronik AG.",
                     "Kartellrechtliche Freigaben (insbesondere lokale Behoerde der Zielgesellschaft).",
                     "Material-Adverse-Change-Klausel (MAC): keine wesentliche Verschlechterung der "
                     "wirtschaftlichen Verhaeltnisse zwischen Signing und Closing.",
                 ]),
                 ("§ 4 Exklusivitaet", [
                     "Die Veraeusserer verpflichten sich, fuer eine Periode von 90 Tagen ab Unterzeichnung "
                     "dieses LoI keine konkurrierenden Verhandlungen mit Dritten zu fuehren bzw. Angebote "
                     "Dritter zu sondieren. No-Shop-Klausel inkl. Konventionalstrafe von EUR 250.000 "
                     "bei Verstoss.",
                 ]),
                 ("§ 5 Vertraulichkeit", [
                     "Es gelten die Regelungen der gleichzeitig unterzeichneten Non-Disclosure-Agreement "
                     "(NDA) vom Datum des LoI; diese sind ausdruecklicher Bestandteil dieses LoI.",
                 ]),
                 ("§ 6 Kosten", [
                     "Jede Partei traegt ihre eigenen Beratungskosten (M&A-Berater, Anwaelte, Wirtschafts"
                     "pruefer). Im Falle des Scheiterns der Transaktion aus Gruenden ausserhalb der "
                     "Kontrolle der Erwerberin werden die Kosten der DD-Berater (KPMG/PwC/Hengeler/"
                     "Roland Berger) bis EUR 800.000 von der Erwerberin getragen.",
                 ]),
                 ("§ 7 Anwendbares Recht / Gerichtsstand", [
                     "Dieser LoI unterliegt deutschem Recht. Gerichtsstand fuer Streitigkeiten ist "
                     "Frankfurt am Main; Schiedsklausel (ICC, Sitz Frankfurt, deutsche Sprache) optional.",
                 ]),
             ])),
            ("Zeitplan (indikativ)",
             [["Phase", "Termin"],
              ["LoI / NDA Unterzeichnung", "Tag 0"],
              ["DD-Start (Roland Berger Commercial, KPMG Financial)", "Tag 7"],
              ["DD-Abschluss / Findings-Report", "Tag 60"],
              ["SPA-Verhandlung", "Tag 60–80"],
              ["Signing", d['signing']],
              ["Closing (nach Kartellfreigabe)", d['closing']]]),
            ("Berater der Erwerberin",
             f"M&A-Berater: {d['berater_ma']}.\n"
             f"Rechtsberatung: {d['berater_legal']}.\n"
             f"Financial DD: {d['berater_finddd']}.\n"
             f"Tax DD: {d['berater_taxdd']}.\n"
             f"Strategie-/Tech-DD: {d['berater_techdd']}.\n"
             f"Interne Projektleitung: Stefan Richter (Vorstand BD/M&A) – ab 1.4.2023 etabliert; vor "
             f"diesem Datum verantwortet durch die zustaendigen Vorstandsmitglieder ad interim."),
            ("Unterschriften",
             signatures("Anna Mueller", "CEO i. V. Brennhagen Elektronik AG", R["name"],
                        "Veraeusserer / JV-Partner Vertreter:in", "—", d['target_short'],
                        place="Frankfurt am Main", date_str_=d['signing'])),
        ])


loi("LOI_Erwerb_Brennhagen_Czech_s.r.o._2018.docx", "czech")
loi("LOI_Konsolidierung_Shanghai_JV_→_1_2021.docx", "shanghai")


# ── SPA Auszug ──────────────────────────────────────────────────────────────
def spa(fname, deal_key):
    d = DEALS[deal_key]
    write_doc(f"{BASE}/{fname}", H,
        f"Share Purchase Agreement (Auszug) – {d['target_short']}",
        subtitle=f"Auszug zur ablage; Vollversion verwahrt bei Notarin Dr. Karin Sonneborn, Stuttgart",
        confidential=True,
        sections=[
            ("Vertragsparteien",
             f"(1) Brennhagen Holding GmbH, eingetragen im Handelsregister AG Stuttgart unter HRB 726450, "
             f"Vaihinger Strasse 120, 70567 Stuttgart, vertreten durch die Geschaeftsfuehrung (»Erwerberin«);\n\n"
             f"(2) Verkaeufer / JV-Partner gemaess Anlage 1.1 (»Veraeusserer«);\n\n"
             f"(3) {d['target_full']} als Zielgesellschaft mit Sitz in {d['sitz']}, "
             f"Registereintrag {d['ico']} (»Zielgesellschaft«)."),
            ("Vertragliche Regelungen (Auszug)",
             ("clauses", [
                 ("§ 1 Kaufgegenstand", [
                     f"Gegenstand des Kaufvertrags ist die Veraeusserung und Uebertragung der "
                     f"Geschaeftsanteile gemaess {d['tx_typ']}.",
                     f"Stichtag der wirtschaftlichen Wirkung (Effective Date): 1. Januar {d['year']} "
                     "(Locked-Box-Mechanik gemaess § 3).",
                 ]),
                 ("§ 2 Kaufpreis", [
                     f"Der Kaufpreis (Equity Value) betraegt {d['kaufpreis']} (Enterprise Value), "
                     f"vermindert um Net Debt zum Stichtag und angepasst um Working-Capital-Differenz "
                     f"zur Target NWC.",
                     f"Zusaetzlich wird ein Earn-Out in Hoehe von max. {d['earn_out']} vereinbart, "
                     "auszahlbar in zwei Tranchen nach Abnahme der jeweiligen Jahresabschluesse durch "
                     "KPMG AG WPG.",
                     "Sicherungsmechanismen: 10 % des Equity Value (EUR 1,4 Mio. Czech / EUR 2,3 Mio. "
                     "Hungary / EUR 0,8 Mio. Shanghai) werden bei einem Treuhaender (Escrow Agent: "
                     "Deutsche Bank AG, Frankfurt) fuer 24 Monate hinterlegt zur Absicherung von "
                     "Garantieansprueche.",
                 ]),
                 ("§ 3 Locked Box / Kaufpreis-Mechanik", [
                     f"Locked-Box-Stichtag: 31. Dezember {int(d['year'])-1}. Zwischen Stichtag und Closing "
                     "duerfen keine Permitted Leakage Events ueber den vereinbarten Permitted-Leakage-Katalog "
                     "(Anlage 3.1) hinaus erfolgen.",
                     "Verzinsung des Kaufpreises ab Stichtag bis Closing: 4,5 % p. a. (Ticking-Fee).",
                 ]),
                 ("§ 4 Garantien (Reps & Warranties)", [
                     "Verkaeufer-Garantien gemaess Garantie-Katalog (Anlage 4.1): "
                     "Gesellschafts-, Bilanz-, Steuer-, Mitarbeiter-, Umwelt-, IP- und Compliance-Garantien.",
                     "Knowledge-Qualifier: »nach bestem Wissen« der namentlich benannten Knowledge Holder "
                     "(CEO und CFO der Zielgesellschaft).",
                     "Cap: 15 % des Equity Value bei allgemeinen Garantien; 100 % bei Title- und "
                     "Fundamental-Garantien; 5 % De-Minimis pro Einzelschaden; EUR 50.000 Basket.",
                     "Verjaehrungsfrist: 24 Monate (allgemein), 7 Jahre (Tax), 10 Jahre (Title-Garantien).",
                 ]),
                 ("§ 5 Specific Indemnities", [
                     "Spezifische Verkaeufer-Freistellungen gemaess Anlage 5.1 fuer (a) anhaengige "
                     "Litigation-Verfahren, (b) Vorsteuer-Risiko aus Konzern-Cost-Recharge 2017/2018, "
                     "(c) potenzielle Altlasten am Standort gemaess Phase-I-ESA-Report.",
                 ]),
                 ("§ 6 W&I-Versicherung", [
                     "Die Erwerberin schliesst eine Warranty-&-Indemnity-Versicherung (W&I-Police) bei "
                     "AIG Europe SA ab; Versicherungssumme EUR 8 Mio.; Selbstbehalt 0,5 % EV; "
                     "Praemie EUR 96.000 (1,2 % VS).",
                 ]),
                 ("§ 7 Conditions Precedent / MAC", [
                     "Closing-Voraussetzungen: (a) Kartellfreigabe der zustaendigen Behoerde "
                     "(BWB Wien / GVH Budapest / MOFCOM Shanghai); (b) Konsent unter Change-of-Control-"
                     "Klauseln bei vier OEM-Vertraegen (vgl. Anlage 7.1); (c) keine Material Adverse "
                     "Change zwischen Signing und Closing.",
                 ]),
                 ("§ 8 Non-Compete / Non-Solicit", [
                     "Wettbewerbsverbot der Veraeusserer fuer 36 Monate ab Closing, raeumlich Europa "
                     "und Asien, sachlich Automotive-Elektronik. Abwerbeverbot fuer Schluesselpersonen "
                     "fuer 24 Monate.",
                 ]),
                 ("§ 9 Anwendbares Recht / Schiedsklausel", [
                     "Es gilt deutsches Recht (mit Ausnahme von UN-Kaufrecht). Streitigkeiten werden "
                     "durch ein Schiedsgericht (ICC, Sitz Frankfurt am Main, drei Schiedsrichter, "
                     "deutsche Sprache) entschieden.",
                 ]),
             ])),
            ("Anlagen-Verzeichnis (Auszug)",
             [["Anlage", "Inhalt"],
              ["1.1", "Veraeusserer / Verkaeufer-Verzeichnis"],
              ["3.1", "Permitted-Leakage-Katalog"],
              ["4.1", "Garantie-Katalog (Reps & Warranties)"],
              ["5.1", "Specific Indemnities"],
              ["7.1", "Change-of-Control-Konsente OEM"],
              ["8.1", "Wettbewerbsverbots-Personen"],
              ["12.1", "Disclosure Schedules (vollstaendig)"]]),
            ("Unterschriften / Beurkundung",
             "Der Vertrag wurde am " + d['signing'] + " vor Notarin Dr. Karin Sonneborn, "
             "Vaihinger Strasse 18, 70567 Stuttgart, unter UR-Nr. NS-MA-" + d['year'] + "/" +
             ("014" if deal_key=="czech" else "008" if deal_key=="hungary" else "021") +
             " notariell beurkundet (Auszug; Originale verwahrt im Notariat).\n\n" +
             signatures("Anna Mueller", "Vorstandsvorsitzende, RHO i. V.", R["name"],
                        "Veraeusserer-Sprecher", "Verkaeufer / JV-Partner", d['target_short'],
                        place="Stuttgart", date_str_=d['signing'])),
        ])


spa("SPA_Erwerb_Brennhagen_Czech_s.r.o._2018_Auszug.docx", "czech")
spa("SPA_Erwerb_Brennhagen_Hungary_Kft._2019_Auszug.docx", "hungary")
spa("SPA_Konsolidierung_Shanghai_JV_→_1_2021_Auszug.docx", "shanghai")


# ── NDA ────────────────────────────────────────────────────────────────────
def nda(fname, deal_key):
    d = DEALS[deal_key]
    write_doc(f"{BASE}/{fname}", H,
        f"Non-Disclosure Agreement (NDA) – {d['target_short']}",
        subtitle="Vertraulichkeitsvereinbarung im Vorfeld der DD-Phase",
        confidential=True,
        sections=[
            ("Vertragsparteien",
             f"(1) Brennhagen Elektronik AG, Vaihinger Strasse 120, 70567 Stuttgart, vertreten durch den "
             f"Vorstand (»Empfaengerin«); und\n\n"
             f"(2) Veraeusserer / JV-Partner der {d['target_full']}, {d['sitz']} (»Offenlegende Partei«)."),
            ("Praeambel",
             "Die Parteien beabsichtigen, im Rahmen einer moeglichen Transaktion vertrauliche "
             "Informationen auszutauschen (Geschaeftsplan, Kunden- und Lieferantendaten, technische "
             "Spezifikationen, Mitarbeiterdaten, IP-Rechte). Zur Wahrung der berechtigten Geheimhaltungs"
             "interessen werden die nachfolgenden Verpflichtungen vereinbart."),
            ("Wesentliche Regelungen",
             ("clauses", [
                 ("§ 1 Vertrauliche Informationen", [
                     "»Vertrauliche Informationen« umfassen saemtliche schriftlich, muendlich oder "
                     "elektronisch uebermittelten Informationen, soweit als »vertraulich« gekennzeichnet "
                     "oder erkennbar vertraulicher Natur (Finanzdaten, Kundenlisten, Vertraege, "
                     "Mitarbeiterdaten, technisches Know-how, IP-Rechte).",
                     "Ausgenommen sind Informationen, die (a) bereits oeffentlich bekannt sind, "
                     "(b) der Empfaengerin vor Offenlegung rechtmaessig bekannt waren, (c) ohne "
                     "Vertraulichkeitsverpflichtung von Dritten erlangt wurden, (d) unabhaengig "
                     "entwickelt wurden.",
                 ]),
                 ("§ 2 Geheimhaltungspflicht", [
                     "Die Empfaengerin verpflichtet sich, vertrauliche Informationen ausschliesslich "
                     "fuer den Transaktionszweck zu verwenden und nicht an Dritte weiterzugeben, "
                     "ausgenommen an die hinzugezogenen Berater (Goldman Sachs, KPMG, PwC, Hengeler "
                     "Mueller, Roland Berger) unter Verpflichtung auf entsprechende Vertraulichkeit.",
                     "Need-to-know-Prinzip; Dokumentation der Zugriffsberechtigten in einem internen "
                     "Distribution Log (verantwortlich: Stefan Richter, Vorstand BD/M&A).",
                 ]),
                 ("§ 3 Laufzeit", [
                     "Diese NDA gilt fuer eine Laufzeit von 3 Jahren ab Unterzeichnung bzw. "
                     "12 Monate nach Beendigung der Transaktionsgespraeche, je nachdem, welcher "
                     "Zeitpunkt frueher eintritt.",
                 ]),
                 ("§ 4 Rueckgabe / Vernichtung", [
                     "Nach Beendigung der Transaktionsgespraeche oder auf Anforderung sind alle "
                     "vertraulichen Materialien (Papier und elektronisch) zu vernichten bzw. zurueckzugeben; "
                     "Vernichtungsprotokoll auf Anforderung. Ausgenommen ist eine Archivkopie bei den "
                     "Anwaelten der Empfaengerin (Hengeler Mueller) zur Erfuellung gesetzlicher "
                     "Aufbewahrungspflichten.",
                 ]),
                 ("§ 5 Non-Solicit / No-Hire", [
                     "Die Empfaengerin verpflichtet sich, fuer 24 Monate ab Unterzeichnung keine "
                     "Schluesselpersonen der Zielgesellschaft (Top-15 Schluesselpersonen gemaess Anlage 5.1) "
                     "aktiv abzuwerben. Ausgenommen sind allgemeine Stellenausschreibungen.",
                 ]),
                 ("§ 6 Konventionalstrafe", [
                     "Im Fall eines vorsaetzlichen oder grob fahrlaessigen Verstoss gegen die Geheim"
                     "haltungspflicht wird eine Konventionalstrafe in Hoehe von EUR 250.000 pro Verstoss "
                     "faellig, unbeschadet der Geltendmachung weiterer Schadensersatzansprueche.",
                 ]),
                 ("§ 7 Anwendbares Recht / Gerichtsstand", [
                     "Deutsches Recht. Gerichtsstand: Frankfurt am Main. Salvatorische Klausel.",
                 ]),
             ])),
            ("Unterschriften",
             signatures("Stefan Richter (oder ad interim Vorstand)", "Vorstand BD/M&A", R["name"],
                        "Veraeusserer-Sprecher", "—", d['target_short'],
                        place="Frankfurt am Main", date_str_=d['signing'])),
        ])


nda("NDA_Erwerb_Brennhagen_Czech_s.r.o._2018.docx", "czech")
nda("NDA_Erwerb_Brennhagen_Hungary_Kft._2019_2024-03-01.docx", "hungary")
nda("NDA_Konsolidierung_Shanghai_JV_→_1_2021.docx", "shanghai")


# ── Integration Plan / PMI ──────────────────────────────────────────────────
def integration_plan(fname, deal_key):
    d = DEALS[deal_key]
    write_doc(f"{BASE}/{fname}", H,
        f"Post-Merger-Integration (PMI) Plan – {d['target_short']}",
        subtitle=f"Integration in den Brennhagen-Konzern – 18-Monats-Plan (Closing {d['closing']})",
        confidential=True,
        sections=[
            ("Zielsetzung der Integration",
             f"Vollintegration der {d['target_short']} in den Brennhagen-Konzern binnen 18 Monaten nach "
             f"Closing. Strategische Logik: {d['rationale']} Synergie-Ziel: Run-Rate EUR 2,1 Mio./Jahr "
             f"ab Monat 18 (geprueft durch Roland Berger im Rahmen der Commercial DD)."),
            ("PMI-Governance",
             ("list", [
                 "Steering Committee: Anna Mueller (CEO, Vorsitz), Laura Bauer (CFO), Dr. Thomas Weber "
                 "(COO), Stefan Richter (BD/M&A ab 4/2023); Aufsichtsrats-Reporting quartalsweise.",
                 "PMI-Lead (operativ): Stefan Richter; PMO mit 6 FTE (4 intern, 2 extern Roland Berger).",
                 "Workstream-Leiter:innen: Finanzen (Florian Maier), HR (Birgit Schmitt), IT (Markus "
                 "Hofstetter), Operations (Andreas Maier), Vertrieb (Stefan Richter), Compliance "
                 "(Dr. Andrea Bergmann).",
                 "Reporting-Kadenz: woechentliches Workstream-Update; zweiwoechentlicher SteerCo; "
                 "monatlicher Vorstands-Status; quartalsweiser Bericht an AR (Pruefungsausschuss).",
             ])),
            ("Workstream-Plan / Meilensteine",
             [["#", "Workstream", "Meilenstein", "Termin (Monat nach Closing)"],
              ["1", "Day-1-Readiness", "Tag-1-Kommunikation OEM-Kunden / Lieferanten", "M0"],
              ["2", "Finance / Bilanzierung", "Eroeffnungsbilanz IFRS / PPA gemaess IAS 3", "M2"],
              ["3", "Finance / Reporting", "Anbindung lokales ERP an Konzern-SAP-S/4HANA", "M9–M18"],
              ["4", "HR / Compensation", "Harmonisierung Tantieme-Systeme / Konzern-LTI-Rollout", "M6"],
              ["5", "HR / Betriebsrat", "Mitbestimmungs-Verfahren / Konzernbetriebsrats-Anbindung", "M4"],
              ["6", "Operations / IATF", "Audit-Vorbereitung und Re-Zertifizierung IATF 16949", "M12"],
              ["7", "IT / Cybersecurity", "Roll-out Konzern-IT-Sicherheitsstandards / ISO 27001", "M9"],
              ["8", "Sales / Cross-Sell", "Brennhagen-Sales-Force / Cross-Selling ICP-3 / ADAS / BMS-12", "M3–M18"],
              ["9", "Procurement / Bundling", "Einbindung in Konzern-Einkauf / Lieferanten-Bundling", "M6"],
              ["10", "Synergie-Tracker", "Initialer Synergie-Baseline; Tracking ab M3", "M0–M18"],
              ["11", "Compliance", "Roll-out Code of Conduct, Whistleblowing-System, GDPR-Audit", "M3"],
              ["12", "Rebranding / Marke", "Umfirmierung auf »Brennhagen Czech / Hungary / Shanghai«", "M1–M3"]]),
            ("Synergie-Plan (Run-Rate ab M18)",
             [["Synergie-Hebel", "Run-Rate (EUR Mio./Jahr)", "Umsetzung bis"],
              ["Einkaufs-Bundling Halbleiter / Passive", "0,8", "M9"],
              ["IT-Konsolidierung (SAP, Lizenzen)", "0,3", "M12"],
              ["Vertriebs-Cross-Selling Brennhagen-Portfolio", "0,6", "M18"],
              ["Overhead-Reduktion (Konzern-Shared-Services)", "0,4", "M12"],
              ["SUMME", "2,1", "M18"]]),
            ("Integrationskosten (One-Off)",
             [["Position", "Wert (EUR Mio.)"],
              ["IT-Migration SAP-S/4HANA-Template", "1,4"],
              ["Beratungs- und Projektkosten (Roland Berger PMI)", "0,9"],
              ["Sozialplan / Restrukturierung (sofern erforderlich)", "0,6"],
              ["Rebranding / Marketing", "0,2"],
              ["W&I-Versicherungskosten (allocated)", "0,1"],
              ["Sonstige Integrationskosten", "0,6"],
              ["SUMME", "3,8"]]),
            ("Risiken und Mitigation",
             "Hauptrisiken: (a) Mitarbeiter-Fluktuation Schluesselpersonen (Mitigation: Retention-Bonusplan "
             "bis EUR 320.000 ueber 24 Monate, vorab in W&I einkalkuliert); (b) Kunden-Konsent unter "
             "Change-of-Control-Klauseln (Mitigation: vorab eingeholt vor Closing); (c) IT-Migration "
             "Risiko Produktionsstoerung (Mitigation: Cutover-Wochenende, Parallel-Run, Rollback-Plan); "
             "(d) Synergie-Realisierung verzoegert (Mitigation: monatliches Synergie-Tracking durch CFO-Team)."),
            ("Unterschriften",
             signatures("Stefan Richter", "Vorstand BD/M&A – PMI Lead", R["name"],
                        "Anna Mueller", "CEO – PMI SteerCo Vorsitz", R["name"],
                        place="Stuttgart", date_str_=d['closing'])),
        ])


integration_plan("Integration_Plan_Erwerb_Brennhagen_Czech_s.r.o._2018.docx", "czech")
integration_plan("Integration_Plan_Erwerb_Brennhagen_Hungary_Kft._2019.docx", "hungary")
integration_plan("Integration_Plan_Konsolidierung_Shanghai_JV_→_1_2021.docx", "shanghai")


# ─────────────────────────────────────────────────────────────────────────────
# Strategischer Prozess 2023/2024 – M&A Pipeline-Dokumente
# (DD-Working-Papers, Finanzanalysen, Bewertungsmodelle, Synergie, First Approach,
#  Management Meeting, Target Screening). Targets: SensoElectro (Wiesbaden),
#  SilicaTech (Krakau), EmbedSoft (Aachen), BMS-Soft (Aachen, Pipeline-Target).
# ─────────────────────────────────────────────────────────────────────────────

PIPELINE_TARGETS = [
    {"code": "T-001", "name": "BMS-Soft GmbH", "sitz": "Aachen",
     "umsatz": "EUR 14,8 Mio. (FY 2023)", "ebitda": "EUR 2,1 Mio.",
     "thema": "Embedded BMS-Software, Modell-basierte Entwicklung (Matlab/Simulink)",
     "rationale": "Vertikale Integration BMS-12 Software-Stack; Reduktion externer Lizenzen"},
    {"code": "T-002", "name": "SensoFusion GmbH", "sitz": "Karlsruhe",
     "umsatz": "EUR 22,4 Mio. (FY 2023)", "ebitda": "EUR 3,8 Mio.",
     "thema": "Sensorfusion Radar/Lidar fuer Level-3-ADAS",
     "rationale": "Ergaenzung ADAS-V4D-Portfolio mit Lidar-Fusion"},
    {"code": "T-003", "name": "PowerSemi AG", "sitz": "Erlangen",
     "umsatz": "EUR 38,1 Mio. (FY 2023)", "ebitda": "EUR 5,9 Mio.",
     "thema": "SiC/GaN-Leistungselektronik fuer BEV-Inverter",
     "rationale": "Vorwaertsintegration Inverter / Halbleiter-Souveraenitaet"},
    {"code": "T-004", "name": "DriveTech Innovations s.r.o.", "sitz": "Prag (CZ)",
     "umsatz": "EUR 11,2 Mio.", "ebitda": "EUR 1,4 Mio.",
     "thema": "AUTOSAR Adaptive Toolchain; Software-Defined-Vehicle",
     "rationale": "Beschleunigung Software-Stack Adaptive AUTOSAR"},
    {"code": "T-005", "name": "EnergiSoft B.V.", "sitz": "Eindhoven (NL)",
     "umsatz": "EUR 18,7 Mio.", "ebitda": "EUR 2,9 Mio.",
     "thema": "Energy-Management-SaaS / Cloud-basierte Fleet-Analytics",
     "rationale": "Aufbau dritte Saeule »Energie-SaaS« gemaess Strategie NEXT"},
]


def pipeline_target(idx):
    """Stable target selection from pipeline based on doc-index (deterministic)."""
    return PIPELINE_TARGETS[idx % len(PIPELINE_TARGETS)]


# ── DD Working Papers ───────────────────────────────────────────────────────
def dd_working_paper(fname, nr, datum, target, focus, draft=False):
    write_doc(f"{BASE}/{fname}", H,
        f"Due Diligence Arbeitspapier #{nr:03d} – Strategischer Prozess 2023/2024",
        subtitle=f"Workstream-Findings | Target-Code {target['code']} | Bearbeitung: Stefan Richter / Goldman Sachs",
        confidential=True, draft=draft,
        sections=[
            ("Kontext und Bearbeitungsstand",
             f"DD-Arbeitspapier Nr. {nr} im Rahmen des strategischen Prozesses 2023/2024 der Brennhagen "
             f"Elektronik AG. Ziel: Vorpruefung des Pipeline-Targets {target['code']} ({target['name']}, "
             f"{target['sitz']}). Bearbeitungsverantwortung: Stefan Richter (Vorstand BD/M&A); externe "
             f"Unterstuetzung: Goldman Sachs Frankfurt (Lead Banker Dr. Klaus Bessler), Roland Berger "
             f"Muenchen (Lead Partner Dr. Stefan Vogel). Bearbeitungsstand: {datum}."),
            ("Untersuchungsgegenstand (Workstream)",
             f"Fokus dieses Arbeitspapiers: {focus}.\n\n"
             f"Hintergrund: Das Pipeline-Target {target['name']} liefert (FY 2023): Umsatz {target['umsatz']}, "
             f"EBITDA {target['ebitda']}. Strategisches Thema: {target['thema']}. "
             f"Deal-Rationale: {target['rationale']}."),
            ("Findings",
             ("list", [
                 "Datenraum-Zugang am " + datum + " geoeffnet (Intralinks); aktuell 412 Dokumente "
                 "indiziert, davon 218 als »priority« markiert.",
                 "Q&A-Liste mit 47 offenen Fragen an Verkaeufer-Berater (Lazard / KPMG) versandt; "
                 "Antworten erwartet binnen 5 Bankarbeitstagen.",
                 "Stichprobenpruefung Top-10-Kundenvertraege: 3 Vertraege mit Change-of-Control-Klausel "
                 "identifiziert (Audi, Continental, ZF). Konsentfaehigkeit zu pruefen.",
                 "Auswertung historische EBITDA-Bridges: Bereinigung um Einmaleffekte (Restrukturierung "
                 "2022, IPO-Vorbereitungs-Kosten der Verkaeufer-Seite) ergibt EBITDA-Adjustment "
                 "+EUR 0,4 Mio.",
                 "Kommerzielle Plausibilisierung Roland Berger: Marktwachstum 2024–2028 6,8 % CAGR; "
                 "Target oberhalb Marktwachstum positioniert.",
             ])),
            ("Risiko-Einschaetzung (vorlaeufig)",
             [["Risikobereich", "Einschaetzung", "Mitigation"],
              ["Kundenkonzentration (Top-3 = 58 %)", "Mittel", "Spezifische Garantie / Earn-Out-Hurdle"],
              ["IP-/Patent-Risiken (Software-Stack)", "Niedrig–Mittel", "Patent-FtO-Analyse Maiwald"],
              ["Schluesselpersonen-Retention", "Mittel–Hoch", "Retention-Plan vorbereiten"],
              ["Tax-/TP-Risiken", "Niedrig", "PwC Tax DD"],
              ["Cyber-/IT-Risiken", "Mittel", "ISO 27001 Gap-Analyse"]]),
            ("Naechste Schritte",
             "(a) Beantwortung der Q&A-Liste durch Verkaeufer-Berater abwarten; (b) Site-Visit "
             "innerhalb der naechsten 2 Wochen koordinieren (Brennhagen BD/M&A, KPMG, Roland Berger); "
             "(c) Bewertungs-Bandbreite verfeinern nach Erhalt der QoE-Light durch KPMG; "
             "(d) Briefing AR-Pruefungsausschuss vor Term-Sheet-Verhandlung; "
             "(e) Working-Capital-Bridge bis zum naechsten DD-Working-Paper aktualisieren."),
            ("Verteiler",
             "Vertraulich – streng begrenzter Verteiler: Stefan Richter (Vorstand BD/M&A), Laura Bauer "
             "(CFO), Anna Mueller (CEO), Dr. Klaus Bessler (Goldman Sachs), Dr. Stefan Vogel (Roland "
             "Berger), Hengeler Mueller (Projekt-Code »NEXT-" + target['code'] + "«), KPMG-DD-Team. "
             "Verteilerprotokoll im NDA-Register (siehe REA_NDA_Register_2023.xlsx) dokumentiert."),
        ])


_dd_focuses = {
    "001": "Datenraum-Eroeffnung, Q&A-Setup, Top-Kundenvertrags-Review",
    "002": "Working-Capital-Bridge / Net-Debt-Definition / Cash-Conversion",
    "003": "QoE-Light KPMG / EBITDA-Bridge / Pro-Forma-Adjustments",
    "004": "Commercial-Marktanalyse Roland Berger / Wettbewerber-Benchmark",
    "005": "Legal-Findings Hengeler Mueller / Change-of-Control / Litigation",
    "006": "Tax DD PwC / TP-Dokumentation / VAT-Recovery",
    "008": "IP-Portfolio / Patent-FtO / Software-Lizenzen (DRAFT)",
    "009": "HR DD / Schluesselpersonen / Tarifvertrag",
    "010": "Technical DD / ASPICE / IATF / EMV-Pruefberichte",
    "011": "Synergie-Validierung / Cross-Sell-Potenzial OEM",
    "012": "PMI-Vorbereitung / IT-Cutover-Konzept",
    "013": "ESG-DD / CSRD-Readiness / Scope-1/2/3-Carbon-Footprint",
    "014": "Insurance DD / W&I-Marktansprache / D&O-Run-off",
    "015": "Bewertung-Update / DCF / Multiples / Football-Field",
}


_DD_FILES = [
    ("DD_WorkingPaper_2023_001.docx", 1, "14. November 2023", 0, False),
    ("DD_WorkingPaper_2023_002.docx", 2, "21. November 2023", 0, False),
    ("DD_WorkingPaper_2023_003_2024-03-01.docx", 3, "1. Maerz 2024", 0, False),
    ("DD_WorkingPaper_2023_004.docx", 4, "5. Dezember 2023", 1, False),
    ("DD_WorkingPaper_2023_005.docx", 5, "12. Dezember 2023", 0, False),
    ("DD_WorkingPaper_2023_006.docx", 6, "19. Dezember 2023", 2, False),
    ("DD_WorkingPaper_2023_008_DRAFT.docx", 8, "9. Januar 2024", 0, True),
    ("DD_WorkingPaper_2023_009.docx", 9, "16. Januar 2024", 0, False),
    ("DD_WorkingPaper_2023_010.docx", 10, "23. Januar 2024", 1, False),
    ("DD_WorkingPaper_2023_011.docx", 11, "30. Januar 2024", 3, False),
    ("DD_WorkingPaper_2023_012.docx", 12, "6. Februar 2024", 0, False),
    ("DD_WorkingPaper_2023_013.docx", 13, "13. Februar 2024", 4, False),
    ("DD_WorkingPaper_2023_014.docx", 14, "20. Februar 2024", 2, False),
    ("DD_WorkingPaper_2023_015.docx", 15, "27. Februar 2024", 0, False),
]

for fname, nr, datum, t_idx, draft in _DD_FILES:
    dd_working_paper(fname, nr, datum, PIPELINE_TARGETS[t_idx],
                     _dd_focuses.get(f"{nr:03d}", "Allgemeines DD-Findings-Update"),
                     draft=draft)


# ── Generic pipeline doc helper (Finanzanalyse / First Approach / Mgmt Meeting / Target Screening / Bewertungsmodell / Synergieberechnung)
def pipeline_doc(fname, kind, nr, target, datum, status="finalisiert", draft=False, suffix=""):
    title = f"M&A Pipeline – {kind} #{nr:03d}{(' – ' + suffix) if suffix else ''}"
    subtitle = (f"Strategischer Prozess 2023/2024 | Target-Code {target['code']} | "
                f"Bearbeitung: Stefan Richter (Vorstand BD/M&A) | Status: {status}")

    common_intro = (
        f"Vertrauliches M&A-Dokument im Rahmen des strategischen Prozesses 2023/2024 der Brennhagen "
        f"Elektronik AG. Pipeline-Target: {target['code']} (»{target['name']}«, {target['sitz']}). "
        f"Strategisches Thema: {target['thema']}. Deal-Rationale: {target['rationale']}. "
        f"Datum: {datum}. Bearbeitung: Stefan Richter (Vorstand BD/M&A, seit 1.4.2023). "
        f"Externe Berater: Goldman Sachs Frankfurt (Dr. Klaus Bessler), Roland Berger (Dr. Stefan Vogel), "
        f"KPMG Deal Advisory, Hengeler Mueller, PwC."
    )

    if kind == "Finanzanalyse":
        sections = [
            ("Dokument", common_intro),
            ("Finanzielle Eckdaten Target",
             [["Kennzahl", "FY 2021", "FY 2022", "FY 2023"],
              ["Umsatz", "EUR 11,8 Mio.", "EUR 13,4 Mio.", target['umsatz']],
              ["Umsatzwachstum y/y", "—", "+13,6 %", "+11 %"],
              ["EBITDA", "EUR 1,4 Mio.", "EUR 1,8 Mio.", target['ebitda']],
              ["EBITDA-Marge", "11,9 %", "13,4 %", "14,2 %"],
              ["Working Capital (EUR Mio.)", "1,8", "2,2", "2,4"],
              ["Net Debt (EUR Mio.)", "0,9", "1,1", "1,4"],
              ["CAPEX (EUR Mio.)", "0,4", "0,6", "0,7"],
              ["F&E-Quote", "8,4 %", "9,1 %", "9,6 %"],
              ["FTE (Anzahl)", "84", "98", "112"]]),
            ("EBITDA-Bridge / Adjustments (QoE-light)",
             "Bereinigung um Einmaleffekte: (a) Restrukturierung Q2/2022 +EUR 0,18 Mio.; "
             "(b) IPO-Vorbereitungskosten Verkaeufer-Seite +EUR 0,12 Mio. (verbleiben beim Verkaeufer); "
             "(c) Foerdermittel Einmal +EUR 0,08 Mio. (kein Run-Rate); (d) Personalkosten-Normalisierung "
             "Management -EUR 0,06 Mio. Bereinigtes EBITDA FY 2023: +EUR 0,32 Mio. ggue. Reported."),
            ("Cash-Conversion und Bilanz-Struktur",
             "Cash-Conversion (FCF/EBITDA) durchschnittlich 68 % ueber FY 2021–2023; Working-Capital-"
             "Intensitaet (NWC / Umsatz) 16,2 %. Bilanzstruktur: Eigenkapital-Quote 41 %; Net-Debt/EBITDA "
             "0,7x; kurzfristige Verbindlichkeiten 38 %. Pensionsrueckstellungen unter EUR 0,1 Mio."),
            ("Bewertung (vorlaeufig)",
             [["Methode", "Multiple / Annahme", "Equity Value (EUR Mio.)"],
              ["EV/EBITDA 8,5x (FY 2023)", "8,5x EUR 2,1 Mio.", "17,9"],
              ["EV/EBITDA 11,0x (FY 2025e)", "11,0x EUR 3,2 Mio.", "35,2"],
              ["EV/Umsatz 1,4x (FY 2023)", "1,4x EUR 14,8 Mio.", "20,7"],
              ["DCF (WACC 9,4 %, TGR 2,5 %)", "DCF-Modell v15", "22,4"],
              ["Football-Field Median", "—", "21,0–24,0"]]),
            ("Naechste Schritte",
             "Verfeinerung Forecast 2024–2027 mit Management-Plan; Sensitivitaets-Analyse WACC ±100 bp; "
             "Marktvergleich Multiples (Bloomberg / Capital IQ); finale Football-Field zur SteerCo "
             "in der KW " + datum.split()[0] + "."),
        ]

    elif kind == "First Approach":
        sections = [
            ("Dokument", common_intro),
            ("Erstansprache Verkaeufer / Eigentuemer",
             f"Stefan Richter (Vorstand BD/M&A) hat am {datum} ein Erstgespraech mit der Geschaeftsfuehrung "
             f"des Targets {target['name']} gefuehrt. Setting: persoenliches Treffen in den Raeumen von "
             f"Goldman Sachs Frankfurt; Roland Berger als Strategie-Berater anwesend. Verkaeufer-Seite "
             f"vertreten durch Mehrheits-Gesellschafter und Geschaeftsfuehrer."),
            ("Erkenntnisse aus dem Gespraech",
             ("list", [
                 "Gesellschafter grundsaetzlich verkaufsbereit (Wechsel in den Ruhestand des Hauptgesellschafters "
                 "ab Anfang 2025).",
                 "Wertvorstellung Verkaeufer: »oberhalb von 30 Mio. EUR Enterprise Value«; "
                 "Wertvorstellung Erwerber (Brennhagen): EUR 20–24 Mio. EV.",
                 "Geschaeftsfuehrer Operations bleibt verfuegbar fuer Earn-Out-Phase (mind. 24 Monate); "
                 "CTO-Schluesselperson (Eigentuemer-Sohn) wird ggfs. Lock-up-Vereinbarung benoetigen.",
                 "Datenraum-Setup durch Lazard / KPMG bereits vorbereitet; Eroeffnung nach NDA und LoI moeglich.",
                 "Zeitplan-Erwartung Verkaeufer: Signing bis Q2/2024; Closing Q3/2024.",
             ])),
            ("Ergebnis und Empfehlung",
             "Empfehlung an Vorstand: Fortsetzung des Prozesses durch (a) Versand NDA (Hengeler Mueller "
             "Template); (b) anschliessend nicht-bindender LoI mit indikativer Bewertung in der Range "
             "EUR 20–24 Mio. EV; (c) DD-Setup; (d) AR-Information ueber Pre-Termsheet-Brief. Risikoeinschaetzung: "
             "Wertvorstellung-Gap zu schliessen ueber Earn-Out-Struktur und vendor financing."),
            ("Naechste Aktionen",
             [["Aktion", "Verantwortlich", "Termin"],
              ["NDA-Versand", "Hengeler Mueller / S. Richter", "+5 Tage"],
              ["Indikativer LoI / Term Sheet", "Goldman Sachs / S. Richter", "+10 Tage"],
              ["AR-Pruefungsausschuss-Briefing", "S. Richter / Anna Mueller", "+14 Tage"],
              ["DD-Beraterteam-Beauftragung", "S. Richter / Florian Maier", "+21 Tage"]]),
        ]

    elif kind == "Management Meeting":
        sections = [
            ("Dokument", common_intro),
            ("Teilnehmende",
             "Brennhagen-Seite: Stefan Richter (Vorstand BD/M&A, Verhandlungsfuehrung), Laura Bauer (CFO, "
             "Bewertung/Finanzierung), Dr. Klaus Bessler (Goldman Sachs Frankfurt, Lead Banker), "
             "Dr. Stefan Vogel (Roland Berger, Strategie-Berater).\n\n"
             f"Target-Seite ({target['name']}): Geschaeftsfuehrung (CEO, CFO), Lead-Engineer / CTO sowie "
             "Verkaeufer-Berater (Lazard / KPMG)."),
            ("Diskussionspunkte",
             ("list", [
                 "Strategische Logik der Transaktion aus Brennhagen-Sicht (Strategie 2026 »NEXT«, Saeulen "
                 "BMS / ADAS / Software-as-a-Service).",
                 "Integrations-Konzept (PMI-Plan; Standort-Strategie; Fortbestand der Marke fuer "
                 "Transition-Phase).",
                 "Bewertungs-Diskussion: Brennhagen-Range EUR 20–24 Mio.; Verkaeufer-Forderung EUR 30+ Mio.; "
                 "Brueckenbildung ueber Earn-Out (max. EUR 4 Mio. ueber 24 Monate, EBITDA-Hurdle).",
                 "Lock-up der Schluesselperson CTO (12 Monate post-closing) und Retention-Bonus "
                 "(EUR 280.000 pro Person ueber 24 Monate).",
                 "Kunden- und Lieferanten-Kommunikation: gemeinsame OEM-Calls binnen 2 Wochen "
                 "nach Closing-Ankuendigung.",
             ])),
            ("Beschluesse / Aktionspunkte",
             [["#", "Aktion", "Verantwortlich", "Termin"],
              ["1", "Term Sheet 2.0 mit Earn-Out-Struktur ausarbeiten", "Goldman Sachs / S. Richter", "+7 Tage"],
              ["2", "Retention-Bonus-Konzept abstimmen mit HR / Compensation", "L. Bauer / B. Schmitt", "+10 Tage"],
              ["3", "DD-Phase-2 (Site-Visit, Tech-DD vor Ort)", "Roland Berger / Brennhagen Engineering", "+14 Tage"],
              ["4", "AR-Pruefungsausschuss-Update", "S. Richter", "+21 Tage"]]),
            ("Vertraulichkeit",
             "Das Protokoll ist vertraulich. Verteiler beschraenkt auf Vorstand Brennhagen, Aufsichtsrats-"
             "Vorsitz, Goldman Sachs, Roland Berger. Speicherort: Concord Deal Room »NEXT-" + target['code'] + "«."),
        ]

    elif kind == "Target Screening":
        sections = [
            ("Dokument", common_intro),
            ("Screening-Methodik",
             "Im Rahmen des strategischen Prozesses 2023/2024 wurden 47 potenzielle Targets gescreent "
             "(Quellen: Roland-Berger-Marktstudie, Mergermarket, Capital IQ, Eigen-Netzwerk Goldman "
             "Sachs, Empfehlungen Hengeler Mueller). Methodik: 3-stufiges Screening mit Kriterien "
             "(a) Strategische Passung, (b) Bewertungs-/Finanzierbarkeit, (c) Realisierbarkeit "
             "(Verkaeufer-Bereitschaft, Kartell, Konsente)."),
            ("Bewertungs-Matrix Top-5-Targets",
             [["Code", "Target", "Sitz", "Strategie-Fit", "Bewertung-Fit", "Realisierbarkeit", "Score (max. 15)"],
              ["T-001", "BMS-Soft GmbH", "Aachen", "5/5", "4/5", "4/5", "13"],
              ["T-002", "SensoFusion GmbH", "Karlsruhe", "5/5", "3/5", "4/5", "12"],
              ["T-003", "PowerSemi AG", "Erlangen", "4/5", "2/5", "3/5", "9"],
              ["T-004", "DriveTech Innovations s.r.o.", "Prag", "4/5", "4/5", "5/5", "13"],
              ["T-005", "EnergiSoft B.V.", "Eindhoven", "5/5", "3/5", "4/5", "12"]]),
            ("Empfehlung",
             "Priorisierung der Targets in der Reihenfolge: (1) T-001 BMS-Soft GmbH und T-004 DriveTech "
             "(je 13 Punkte); (2) T-002 SensoFusion und T-005 EnergiSoft (je 12 Punkte); (3) T-003 PowerSemi "
             "(9 Punkte; Realisierbarkeit eingeschraenkt aufgrund Mehrheitsaktionaer und Bewertungs"
             "vorstellungen). Fuer dieses Target-Profil " + target['code'] + " (" + target['name'] +
             ") wird die Fortsetzung des Prozesses durch First Approach und LoI empfohlen."),
            ("Naechste Schritte",
             "Fuer die priorisierten Targets: NDA-Versand, First-Approach-Meeting, anschliessend "
             "indikativer LoI mit Bewertungs-Range und Kondition. Status-Update an den Vorstand alle "
             "zwei Wochen; quartalsweise an den Aufsichtsrat (Pruefungs- bzw. Strategieausschuss)."),
        ]

    elif kind == "Bewertungsmodell":
        sections = [
            ("Dokument", common_intro),
            ("Modellstruktur",
             "DCF-Bewertungsmodell (Excel, Version v15) fuer Target " + target['code'] + ". Aufbau: "
             "(1) Historie FY 2021–2023, (2) Forecast FY 2024–2030 (7 Jahre explicit period), "
             "(3) Terminal-Value (Gordon-Growth), (4) WACC-Komponenten, (5) Sensitivitaeten, "
             "(6) Football-Field. Plausibilisierung durch KPMG Deal Advisory."),
            ("Forecast-Annahmen",
             [["Treiber", "FY 2024e", "FY 2025e", "FY 2026e", "FY 2027e", "FY 2028e"],
              ["Umsatzwachstum y/y", "+18 %", "+22 %", "+18 %", "+14 %", "+11 %"],
              ["EBITDA-Marge", "15,1 %", "16,8 %", "17,9 %", "18,4 %", "18,8 %"],
              ["CAPEX/Umsatz", "5,2 %", "4,8 %", "4,3 %", "3,9 %", "3,7 %"],
              ["NWC-Intensitaet", "16,0 %", "15,5 %", "15,0 %", "14,8 %", "14,6 %"]]),
            ("WACC-Herleitung",
             [["Komponente", "Wert"],
              ["Risikofreier Zins (Bund 10Y, Stichtag)", "2,4 %"],
              ["Eigenkapital-Risikopraemie (MRP)", "5,5 %"],
              ["Beta (peer-adjusted, unlevered)", "1,15"],
              ["Beta (re-levered)", "1,28"],
              ["Cost of Equity (CAPM)", "9,5 %"],
              ["Cost of Debt (pre-tax)", "4,8 %"],
              ["Tax Shield (CIT 30 %)", "—"],
              ["Cost of Debt (post-tax)", "3,4 %"],
              ["Capital Structure (Debt/EV)", "20 %"],
              ["WACC", "9,4 %"]]),
            ("Bewertungs-Ergebnis (Football Field)",
             "Die Triangulation der Bewertungsmethoden ergibt eine Bewertungs-Range fuer das Equity Value "
             "von EUR 19,4 Mio. (untere Grenze, EV/EBITDA 8,5x) bis EUR 26,8 Mio. (obere Grenze, DCF "
             "mit Best-Case-Annahmen). Median: EUR 22,4 Mio. Empfohlene Verhandlungsbasis fuer LoI: "
             "EUR 20–24 Mio. EV (inklusive moeglichem Earn-Out von max. EUR 4 Mio.)."),
            ("Sensitivitaets-Analyse",
             [["WACC \\ TGR", "1,5 %", "2,0 %", "2,5 %", "3,0 %"],
              ["8,4 %", "24,1", "25,8", "27,8", "30,2"],
              ["8,9 %", "22,4", "23,9", "25,6", "27,7"],
              ["9,4 %", "20,8", "22,1", "23,6", "25,4"],
              ["9,9 %", "19,4", "20,5", "21,8", "23,4"],
              ["10,4 %", "18,1", "19,1", "20,2", "21,6"]]),
        ]

    elif kind == "Synergieberechnung":
        sections = [
            ("Dokument", common_intro),
            ("Synergie-Hebel (Run-Rate post-Closing)",
             [["#", "Synergie-Hebel", "Run-Rate (EUR Mio./Jahr)", "Realisierung bis"],
              ["1", "Cross-Sell ICP-3 / BMS-12 / ADAS-V4D in Target-Kundenbasis", "1,4", "M18"],
              ["2", "Einkauf: Bundling Halbleiter / Passive bei Konzern-Lieferanten", "0,6", "M9"],
              ["3", "Vertikale Integration: Reduktion externer Software-Lizenzen", "0,4", "M12"],
              ["4", "Overhead: Konzern-Shared-Services (Finance, HR, IT, Legal)", "0,5", "M12"],
              ["5", "F&E: Gemeinsame Plattform-Entwicklung / Asset-Sharing", "0,3", "M18"],
              ["6", "Steuern: Optimierung Transferpreise / Holding-Struktur", "0,2", "M12"],
              ["SUMME Run-Rate", "—", "3,4", "M18"]]),
            ("Realisierungskurve (Quartalsweise nach Closing)",
             [["Quartal post-Closing", "Q1", "Q2", "Q3", "Q4", "Q5", "Q6"],
              ["% Run-Rate erreicht", "10 %", "25 %", "40 %", "55 %", "75 %", "100 %"],
              ["EBITDA-Effekt (EUR Mio.)", "0,3", "0,9", "1,4", "1,9", "2,6", "3,4"]]),
            ("Integrationskosten (One-Off)",
             [["Position", "Wert (EUR Mio.)"],
              ["IT-Migration / SAP-S/4HANA-Anbindung", "1,4"],
              ["PMI-Beratungskosten (Roland Berger)", "0,9"],
              ["Restrukturierung (Sozialplan, Abfindungen, Outplacement)", "0,7"],
              ["Rebranding / Marketing-Transition", "0,2"],
              ["Sonstige (Compliance-Audits, IATF-Migration)", "0,4"],
              ["SUMME", "3,6"]]),
            ("Netto-Synergie-Effekt (NPV ueber 5 Jahre)",
             "Netto-Synergie-Wert (NPV, WACC 9,4 %): EUR 11,8 Mio. ueber 5 Jahre. Dieser Wert wird in "
             "der finalen Bewertungs-Bridge auf den Strategic-Value addiert; aus Verhandlungsperspektive "
             "verbleibt der ueberwiegende Anteil (>70 %) jedoch beim Erwerber (Brennhagen)."),
            ("Risiken Synergie-Realisierung",
             "Hauptrisiken: (a) Cross-Sell-Hebel abhaengig von Kunden-Konsentfaehigkeit (Change-of-Control); "
             "(b) F&E-Synergien benoetigen 18 Monate Plattform-Harmonisierung; (c) Overhead-Reduktion "
             "abhaengig von Sozialplan-Verhandlung mit Konzernbetriebsrat (Marlies Duerr); "
             "(d) Steuer-Optimierung abhaengig von BEPS-2.0-Pillar-2-Regelung."),
        ]

    else:
        sections = [("Dokument", common_intro)]

    write_doc(f"{BASE}/{fname}", H, title, subtitle=subtitle,
              confidential=True, draft=draft, sections=sections)


# Finanzanalyse-Files
pipeline_doc("MA_Finanzanalyse_2023_002.docx", "Finanzanalyse", 2, pipeline_target(0), "21. November 2023")
pipeline_doc("MA_Finanzanalyse_2023_006_FINAL_v2.docx", "Finanzanalyse", 6, pipeline_target(2), "19. Dezember 2023", suffix="FINAL v2")
pipeline_doc("MA_Finanzanalyse_2023_012.docx", "Finanzanalyse", 12, pipeline_target(1), "6. Februar 2024")
pipeline_doc("MA_Finanzanalyse_2023_023.docx", "Finanzanalyse", 23, pipeline_target(3), "5. April 2024")

# Bewertungsmodell
pipeline_doc("MA_Bewertungsmodell_2023_015.docx", "Bewertungsmodell", 15, pipeline_target(0), "27. Februar 2024")

# First Approach
pipeline_doc("MA_First_Approach_2023_003.docx", "First Approach", 3, pipeline_target(0), "28. November 2023")
pipeline_doc("MA_First_Approach_2023_007.docx", "First Approach", 7, pipeline_target(3), "8. Dezember 2023")
pipeline_doc("MA_First_Approach_2023_010.docx", "First Approach", 10, pipeline_target(4), "9. Januar 2024")
pipeline_doc("MA_First_Approach_2023_017.docx", "First Approach", 17, pipeline_target(1), "26. Februar 2024")

# Management Meeting
pipeline_doc("MA_Management_Meeting_2023_004.docx", "Management Meeting", 4, pipeline_target(0), "1. Dezember 2023")
pipeline_doc("MA_Management_Meeting_2023_005.docx", "Management Meeting", 5, pipeline_target(3), "11. Dezember 2023")
pipeline_doc("MA_Management_Meeting_2023_019.docx", "Management Meeting", 19, pipeline_target(1), "5. Maerz 2024")
pipeline_doc("MA_Management_Meeting_2023_022.docx", "Management Meeting", 22, pipeline_target(4), "26. Maerz 2024")

# Synergieberechnung
pipeline_doc("MA_Synergieberechnung_2023_001.docx", "Synergieberechnung", 1, pipeline_target(0), "14. November 2023")
pipeline_doc("MA_Synergieberechnung_2023_011.docx", "Synergieberechnung", 11, pipeline_target(3), "30. Januar 2024")
pipeline_doc("MA_Synergieberechnung_2023_013.docx", "Synergieberechnung", 13, pipeline_target(2), "13. Februar 2024")
pipeline_doc("MA_Synergieberechnung_2023_014.docx", "Synergieberechnung", 14, pipeline_target(4), "20. Februar 2024")
pipeline_doc("MA_Synergieberechnung_2023_016.docx", "Synergieberechnung", 16, pipeline_target(1), "5. Maerz 2024")
pipeline_doc("MA_Synergieberechnung_2023_021.docx", "Synergieberechnung", 21, pipeline_target(0), "22. Maerz 2024")

# Target Screening
pipeline_doc("MA_Target_Screening_2023_008.docx", "Target Screening", 8, pipeline_target(2), "12. Dezember 2023")
pipeline_doc("MA_Target_Screening_2023_009_WIP.docx", "Target Screening", 9, pipeline_target(4), "20. Dezember 2023", status="Work in Progress (WIP)", draft=True)
pipeline_doc("MA_Target_Screening_2023_024.docx", "Target Screening", 24, pipeline_target(1), "10. April 2024")


# ── REA_Teaser_Strategischer_Prozess_2024 ───────────────────────────────────
write_doc(f"{BASE}/REA_Teaser_Strategischer_Prozess_2024_SANITIZED.docx", H,
    "Unternehmens-Teaser – Strategischer Prozess 2024 [SANITIZED]",
    subtitle="Sell-side Teaser-Variante zur Marktansprache potenzieller Investoren / Co-Investoren",
    confidential=True,
    sections=[
        ("Company Overview (Sanitized)",
         "The »Company« is a leading Tier-1 automotive electronics supplier headquartered in Southern "
         "Germany, listed on the Prime Standard segment of the Frankfurt Stock Exchange. The Company "
         "develops, manufactures, and distributes infotainment modules, battery management systems (BMS), "
         "advanced driver assistance system (ADAS) electronic control units, and powertrain electronics "
         "to a blue-chip OEM customer base across the European and Asian automotive industries."),
        ("Investment Highlights",
         ("list", [
             "Prime Standard-listed; market capitalization EUR 2,15 bn (as of latest reporting period).",
             "FY 2023: Revenue EUR 612 m (+2 % YoY); EBITDA EUR 74,3 m (margin 12,1 %).",
             "Blue-chip OEM customer base: BMW Group (28 % revenue), Volkswagen AG (22 %), Mercedes-Benz "
             "Group (18 %), Stellantis N.V. (10 %), Hyundai/CATL (8 %), others (14 %).",
             "Strategic growth platforms: Battery Management Systems (BMS-12, secured order with VW for "
             "ID.7), ADAS Level 2-3 (radar fusion ECU on Mercedes/Stellantis platforms), Energy-Software-"
             "as-a-Service (new strategic pillar from 2024).",
             "Order book at record high (>EUR 2,1 bn at year-end 2023); revenue visibility 3,4 years.",
             "Multi-country production footprint (Germany, Czech Republic, Poland, Hungary, China) with "
             "IATF 16949 / ASPICE / ISO certifications.",
         ])),
        ("Key Financials (sanitized)",
         [["EUR Mio.", "FY 2020", "FY 2021", "FY 2022", "FY 2023"],
          ["Revenue", "542", "580", "600", "612"],
          ["EBITDA", "64", "70", "73", "74,3"],
          ["EBITDA-Margin", "11,8 %", "12,1 %", "12,2 %", "12,1 %"],
          ["EBIT", "38", "42", "47", "48,9"],
          ["FTE (Year-end)", "3.620", "3.820", "4.020", "4.180"]]),
        ("Process Information",
         "This Teaser is being made available on a confidential basis to selected pre-qualified investors. "
         "Any expression of interest should be addressed exclusively to the M&A advisor (Goldman Sachs "
         "International, Frankfurt; Lead Senior Banker Dr. Klaus Bessler). Bid-Procedure-Letter and access "
         "to the Information Memorandum / Virtual Data Room will be provided upon execution of a Non-"
         "Disclosure Agreement (NDA) using the advisor's template. Indicative bid deadline: TBD. "
         "Selected bidders will be invited to a structured DD process (financial / legal / tax / commercial "
         "/ technical) following the timeline communicated in the Process Letter."),
        ("Disclaimer",
         "This document has been sanitized for confidentiality purposes. Identification of the »Company« "
         "may not be readily possible based on this Teaser; however, the contents are accurate as of the "
         "date of issuance. No representation or warranty is made as to the accuracy or completeness of "
         "the information contained herein. Forward-looking statements are subject to risks and uncertainties. "
         "Prepared by: Goldman Sachs International (M&A advisor) in coordination with Stefan Richter "
         "(Vorstand BD/M&A, Brennhagen Elektronik AG)."),
        ("Verteiler / Distribution Log",
         "Distribution is strictly limited and recorded in the central NDA-Register "
         "(REA_NDA_Register_2023.xlsx). Schwellenwert fuer Verteilung: vorhandene unterzeichnete NDA "
         "(Hengeler-Mueller-Template); Distribution List freigegeben durch S. Richter und L. Bauer (CFO). "
         "Distribution erfolgt ueber Concord Deal Room mit Wasserzeichen-Trace."),
    ])


# ── REA_BMW_BMS-12_ECR_2023_003_reviewed ────────────────────────────────────
write_doc(f"{BASE}/REA_BMW_BMS-12_ECR_2023_003_reviewed.docx", H,
    "Engineering Change Request (ECR) #003 – BatteryMS-12 (BMS-12) – BMW Group",
    subtitle="ECR im Rahmen des BMW-Liefer-/Entwicklungsprojekts NEUE KLASSE; Reviewed Edition",
    confidential=True,
    sections=[
        ("ECR Details",
         [["Feld", "Wert"],
          ["ECR-Nummer", "ECR-2023-BMW-BMS12-003"],
          ["Produkt", "BMS-12 Battery Management System (BMW NEUE KLASSE i-Plattform)"],
          ["Sachgrund", "Aenderung Zelltyp (von prismatisch 2170 auf 4680) zwecks Energie-Dichte"],
          ["Initiator (BMW)", "Dr. Stefan Wagner, Senior Engineer Batteriesysteme BMW Group"],
          ["Empfaenger (Brennhagen)", "Dr. Klaus Kessler, RSG Muenchen (Werkleiter); Lars Wittmann (Lead Dev)"],
          ["Status", "Reviewed – Phase 1 Engineering Assessment abgeschlossen"],
          ["Eingang ECR", "14. September 2023"],
          ["Review-Frist Brennhagen", "30 Werktage (ECR-Standard)"],
          ["Quotation-Frist", "60 Werktage nach Engineering Approval"]]),
        ("Aenderungsbeschreibung",
         "BMW Group fordert eine Aenderung des BMS-12 zur Unterstuetzung der naechsten Generation "
         "zylindrischer Lithium-Ionen-Zellen 4680 (anstelle der urspruenglich spezifizierten prismatischen "
         "2170-Zellen). Aenderungsumfang: (a) Anpassung Cell-Voltage-Monitoring (BMS-IC und Wiring); "
         "(b) Update Battery-Pack-Algorithmen (State-of-Charge-Estimator, State-of-Health-Estimator); "
         "(c) Anpassung Sicherheits-Pruefkette (ISO 26262 ASIL D Re-Validation)."),
        ("Engineering Assessment",
         "Phase 1 Engineering Assessment durch RSG Muenchen (Lead: Lars Wittmann, 18 Personen Team) "
         "ergibt: technisch machbar, Aufwand 14.200 Engineering-Stunden (ca. 9 FTE-Monate). Auswirkungen "
         "auf Time-to-Market: SOP-Verzoegerung von Q2/2025 auf Q4/2025 wahrscheinlich. Mehrkosten "
         "fuer Re-Validierung ASIL D (ISO 26262): EUR 0,8 Mio. (Test-Equipment, Pruefstandsbelegung "
         "TUEV Sued / DEKRA). Materialkosten: BMS-IC-Bauteilkosten bleiben unveraendert; PCB-Layout-"
         "Aenderung (Re-Spin) noetig (1 Iteration, EUR 280k NRE)."),
        ("Kommerzielle Auswirkungen",
         [["Position", "Wert"],
          ["NRE-Mehraufwand (Re-Engineering, Re-Validation)", "EUR 1,4 Mio."],
          ["Stueckpreis-Aenderung (PPV)", "Keine (Material bleibt aequivalent)"],
          ["Time-to-Market-Verzoegerung", "ca. 6 Monate (Q4/2025 statt Q2/2025)"],
          ["Volumen-Anpassung", "Keine (5-Jahres-Volumen-Forecast unveraendert)"],
          ["Zahlungsbedingungen NRE", "30 % bei Approval; 40 % bei DV-Test; 30 % bei SOP"]]),
        ("Naechste Schritte",
         "Brennhagen versendet finales Quotation und revidierten Projektplan binnen 30 Werktagen. BMW "
         "Group prueft und gibt formale ECR-Freigabe (Q-Stempel) durch Procurement und Engineering "
         "Sign-off. Anschliessend Vertragsaenderung (Anlage zum Rahmenliefervertrag #BMW-2021-ICP3-BMS12). "
         "Reviewed durch: Dr. Klaus Kessler (Werkleiter RSG), Stefan Richter (Vorstand BD/M&A; Quotation), "
         "Florian Maier (Group Controlling; Margin-Pruefung)."),
        ("Unterschriften / Sign-off",
         signatures("Lars Wittmann", "Lead Developer / RSG Muenchen", R["name"],
                    "Dr. Stefan Wagner", "Senior Engineer Batteriesysteme", "BMW Group",
                    place="Muenchen", date_str_="9. Oktober 2023")),
    ])


# ── PRJ-2023-005_Status_2024_05 ──────────────────────────────────────────
write_doc(f"{BASE}/PRJ-2023-005_Status_2024_05_Heilbronn_Plant.docx", H,
    "Projektstatusbericht Mai 2024 – Heilbronn Plant Expansion (PRJ-2023-005)",
    subtitle="Projektstatus Werkserweiterung Heilbronn / BMS-12-Produktionslinie / Stand 30. Mai 2024",
    confidential=True,
    sections=[
        ("Projektrahmen",
         "Projekt PRJ-2023-005 »Heilbronn Plant Expansion / BMS-12 Linie 3«. Genehmigt durch Aufsichts"
         "rat in Sitzung Q3/2023 (Beschluss-Nr. AR-2023-Q3-12); Investitionsvolumen genehmigt EUR 28 "
         "Mio., spaetere Aufstockung um EUR 4 Mio. fuer zusaetzliche BMS-12-Kapazitaeten. Ziel: "
         "SOP BMS-12 fuer VW ID.7 Q4/2024; Volumen 280 Mio. EUR / Laufzeit 7 Jahre."),
        ("Projektorganisation",
         "Gesamtprojektleitung: Dr. Thomas Weber (COO); Werkleiter Heilbronn: Andreas Maier; "
         "Quality-Lead: Sabine Brand; IT-Lead: Markus Hofstetter; Externer GU-Partner: Bauunternehmen "
         "Heberger GmbH (Schwetzingen). Steering Committee: Vorstand + Werkleiter + GU-Lead; "
         "Sitzungsturnus zweiwoechentlich."),
        ("Statusampel-Uebersicht (Mai 2024)",
         [["Workstream", "Ampel", "% Fortschritt", "Kommentar"],
          ["Bau / Gebaeude (Halle 3 Erweiterung)", "GRUEN", "92 %", "Dach- und Fassadenarbeiten abgeschlossen; Innenausbau Q3/2024"],
          ["Produktions-Equipment (SMD-Linien, ICT, AOI)", "GELB", "78 %", "Lieferverzug Yamaha YSM40 um 8 Wochen; Mitigation: Backup-Maschine geleast"],
          ["IT / SAP-S/4HANA Anbindung Linie 3", "GRUEN", "85 %", "Cutover-Wochenende geplant 18.-20. Oktober 2024"],
          ["Qualifizierung / IATF-Audit", "GELB", "60 %", "Pruefstaende noch nicht alle qualifiziert (PPAP-Vorbereitung)"],
          ["Personal-Recruitment (45 FTE)", "ORANGE", "55 %", "Arbeitsmarkt eng; aktuell 25 Einstellungen, 20 offen"],
          ["Lieferantenfreigaben (PPAP)", "GELB", "62 %", "PPAP-Level-3-Validierung Halbleiter-Lieferant NXP laeuft"]]),
        ("Budget-Status",
         [["Position", "Budget (EUR Mio.)", "Ist (EUR Mio.)", "Forecast EJ (EUR Mio.)", "Abweichung"],
          ["Bau / Gebaeude", "12,4", "11,8", "12,6", "+0,2 (+1,6 %)"],
          ["Produktions-Equipment", "14,8", "10,2", "15,4", "+0,6 (+4,1 %)"],
          ["IT / Software-Lizenzen", "1,8", "1,4", "1,8", "0,0"],
          ["Engineering / Qualifizierung", "1,6", "1,1", "1,8", "+0,2 (+12,5 %)"],
          ["Personal-Onboarding / Training", "0,9", "0,4", "0,9", "0,0"],
          ["Kontingenz (5 %)", "1,5", "0,0", "0,5", "-1,0 (genutzt)"],
          ["SUMME", "33,0", "24,9", "33,0", "0,0"]]),
        ("Risiken und Massnahmen",
         "Hauptrisiken: (a) Personal-Recruitment in einem engen Arbeitsmarkt (Mitigation: Kooperation "
         "mit Agenturen Hays + Adecco; Werbe-Kampagne; Werks-Tag im Juli 2024); (b) Lieferverzug "
         "Yamaha-Bestueckung (Mitigation: Backup-Maschine geleast, Beschleunigungs-Pramiazahlung "
         "vereinbart); (c) IATF-Qualifizierungs-Audit-Termin im November 2024 (Mitigation: externe "
         "Q-Vorbereitung durch ProQM-Consulting); (d) PPAP-Lieferantenfreigaben Halbleiter "
         "(Mitigation: woechentlicher Status-Call mit NXP-Account-Team).") ,
        ("Kommunikation OEM / Kunden",
         "VW Group (Volkswagen Konzern Beschaffung Wolfsburg) wurde im SteerCo-Reporting am 28. Mai 2024 "
         "ueber den aktuellen Projektstatus unterrichtet (SOP Q4/2024 plangemaess). BMW Group, Hyundai "
         "und CATL erhalten quartalsweise Status-Updates im Rahmen der Customer-Reviews. Eine "
         "Werksbesichtigung fuer VW Group ist fuer August 2024 geplant."),
        ("Unterschriften",
         signatures("Andreas Maier", "Werkleiter REG Heilbronn", "Brennhagen Elektronik GmbH",
                    "Dr. Thomas Weber", "COO / Gesamtprojektleitung", R["name"],
                    place="Heilbronn", date_str_="30. Mai 2024")),
    ])


# ── RCN_Steuerbescheid_2021 ────────────────────────────────────────────────
write_doc(f"{BASE}/RCN_Steuerbescheid_2021.docx",
    {"name": "Brennhagen (Shanghai) Co. Ltd. / 罗瑞格 (上海) 电子有限公司",
     "addr": "88 Pudong Avenue, Building B, 200120 Shanghai, China",
     "hrb": "Unified Social Credit Code 91310115MA1FL42Q38"},
    "Tax Assessment / Steuerbescheid 2021 – Brennhagen (Shanghai) Co. Ltd.",
    subtitle="Steuerveranlagung des Steuerjahres 2021 (CIT / VAT / IIT-Compliance) | Behoerde: Shanghai Tax Bureau, Pudong Branch",
    sections=[
        ("Bescheid-Kopfdaten",
         [["Feld", "Wert"],
          ["Behoerde", "State Tax Administration / Shanghai Pudong Tax Bureau"],
          ["Aktenzeichen", "STB-PUDONG-2022-CIT-91310115MA1FL42Q38"],
          ["Steuerpflichtiger", "Brennhagen (Shanghai) Co. Ltd."],
          ["Steuerjahr", "1.1.2021 – 31.12.2021"],
          ["Bescheid-Datum", "14. Juni 2022"],
          ["Bearbeitende Steuerberatung", "Deloitte China (Shanghai); Lead Partner Felix Cheng"],
          ["Berichts-Empfaenger (Konzern)", "Dr. Heike Berger (Group Tax Director), Florian Maier (Group Controller)"]]),
        ("Festsetzung Koerperschaftsteuer (CIT)",
         "Festgesetzte Koerperschaftsteuer (Corporate Income Tax, CIT) fuer 2021: CNY 8.110.000 "
         "(zum Stichtagskurs ca. EUR 1.046.424). Bemessungsgrundlage: Steuerlicher Gewinn vor Steuern "
         "CNY 32.440.000 (ca. EUR 4,18 Mio.); Steuersatz 25 % (Standard-CIT-Satz). "
         "Verrechnungspreis-Anpassungen: keine (TP-Local-File-Pruefung ohne Beanstandung). "
         "Foerderungen / Steuer-Holidays: nicht beansprucht (R&D-Tax-Incentive aufgrund fehlender "
         "lokal qualifizierter F&E-Aktivitaeten nicht anwendbar)."),
        ("Umsatzsteuer (VAT) und Quellensteuer",
         "Festgesetzte VAT (Value Added Tax) 2021: CNY 5.244.000 (Standard-VAT-Satz 13 % auf "
         "Produktverkaeufe in China). Vorsteuer-Abzug: vollstaendig anerkannt. Quellensteuer "
         "(Withholding Tax) auf konzerninterne Dividenden: 10 % (DBA-Schutz Deutschland-China gilt "
         "fuer 5 %-Quellensteuer; jedoch wurde 2021 keine Dividende ausgeschuettet). Lohnsteuer "
         "(Individual Income Tax, IIT): durch Payroll-Provider HRConnect Shanghai abgewickelt, "
         "keine Beanstandung."),
        ("Audit-Ergebnis und Findings",
         "Steuerpruefung durch das Pudong Tax Bureau erfolgte im Maerz/April 2022. Schwerpunkt: "
         "(a) Verrechnungspreise (TP) im Konzernverbund (Brennhagen Holding GmbH, Brennhagen Elektronik AG); "
         "(b) Cross-Border Service Fees (intragroup), insbesondere SAP-Lizenzen und Konzern-Management-"
         "Fee; (c) Vorsteuer-Abzug auf importierte Halbleiter. Findings: keine wesentlichen Beanstandungen; "
         "1 informaler Hinweis zu Sub-Stantiation der Konzern-Management-Fee (zu adressieren in TP-Local "
         "File 2022)."),
        ("Konsequenzen / Massnahmen Konzern",
         "Group Tax Director Dr. Heike Berger nimmt den Bescheid an; keine Einspruchsverfahren "
         "erforderlich. Massnahmen: (a) TP-Local-File 2022 mit erweiterter Begruendung der "
         "Konzern-Management-Fee (Benchmarking, Beneficial-Owner-Test); (b) Dokumentation IT-Service-"
         "Recharges mit detaillierten Stundenaufzeichnungen; (c) abgestimmt mit PwC Tax Shanghai. "
         "Zahlungseingang Steuerschuld vollstaendig binnen Frist."),
        ("Bestaetigungen",
         signatures("Liang Wei", "Finance Manager RCN Shanghai", "Brennhagen (Shanghai) Co. Ltd.",
                    "Dr. Heike Berger", "Group Tax Director", R["name"],
                    place="Shanghai", date_str_="20. Juni 2022")),
    ])


# ── DE_REG_Lohnsteuer_Jahresabschluss_2021 ─────────────────────────────────
write_doc(f"{BASE}/DE_REG_Lohnsteuer_Jahresabschluss_2021.docx",
    {"name": "Brennhagen Elektronik GmbH (Werk Heilbronn)",
     "addr": "Industriestrasse 24, 74076 Heilbronn",
     "hrb": "HRB 221456, AG Heilbronn"},
    "Lohnsteuer-Jahresabschluss 2021 – Werk Heilbronn (REG)",
    subtitle="Regulatorische Meldung gemaess § 41a EStG / Lohnsteuer-Anmeldung Jahresabschluss",
    sections=[
        ("Meldepflichtiger",
         "Brennhagen Elektronik GmbH (REG), Industriestrasse 24, 74076 Heilbronn. Eingetragen im "
         "Handelsregister AG Heilbronn unter HRB 221456. Steuer-Nr. 65091/26415 (Finanzamt Heilbronn). "
         "Steuerverantwortlich gegenueber Finanzamt: Geschaeftsfuehrung REG (Andreas Maier, Werkleiter); "
         "Lohnsteuer-Verantwortung: HR-Leitung REG (Birgit Schmitt) in Abstimmung mit Group Tax Director "
         "Dr. Heike Berger."),
        ("Mitarbeiter-Eckdaten Werk Heilbronn 2021",
         [["Kategorie", "Anzahl", "Lohnsumme (EUR Mio.)"],
          ["Vollzeit-Beschaeftigte", "742", "47,8"],
          ["Teilzeit-Beschaeftigte", "58", "1,9"],
          ["Auszubildende", "20", "0,4"],
          ["Werkstudenten / Praktikanten", "12", "0,2"],
          ["Leiharbeitnehmer (durchschnittlich)", "32", "—"],
          ["SUMME (festes Personal)", "832", "50,3"]]),
        ("Lohnsteuer-Anmeldung",
         [["Steuerart", "Bemessungsgrundlage (EUR Mio.)", "Steuerbetrag (EUR Mio.)"],
          ["Lohnsteuer", "50,3", "9,82"],
          ["Solidaritaetszuschlag (5,5 %)", "—", "0,18"],
          ["Kirchensteuer (ca. 6 %, gewogen)", "—", "0,42"],
          ["Pauschsteuer geringfuegige Beschaeftigung (§ 40a EStG)", "0,21", "0,06"],
          ["SUMME Lohnsteuer-Abfuehrung 2021", "—", "10,48"]]),
        ("Besondere Sachverhalte 2021",
         "(a) Kurzarbeitergeld-Aufstockung (Werks-Sondersituation Halbleiter-Engpass Q3/2021): KuG-"
         "Anwendung fuer 124 Beschaeftigte in 3 Monaten; Aufstockung durch Arbeitgeber-Tarifvertrag "
         "auf 95 % Nettoentgelt; entsprechende Lohnsteuer-Behandlung beachtet (KuG ist steuerfrei, "
         "aber Progressionsvorbehalt; Aufstockungsbetrag voll steuerpflichtig). "
         "(b) Pruefung Lohnsteuer-Aussenpruefung durch FA Heilbronn im April 2022: ohne Beanstandung "
         "abgeschlossen (Pruefbericht vom 14. Mai 2022). "
         "(c) Anpassung Direktversicherung / Pensionsplan: alle Beitraege geprueft, korrekt unter "
         "§ 3 Nr. 63 EStG behandelt. "
         "(d) Geldwerter Vorteil Dienstwagen: 184 Berechtigte; 1 %-Regelung; pauschale Lohnsteuer "
         "0,03 % je Entfernungskilometer."),
        ("Konsequenzen",
         "Alle Lohnsteuer-Abfuehrungen 2021 sind vollstaendig, fristgerecht und korrekt an das "
         "Finanzamt Heilbronn erfolgt. Jahresmeldung gemaess § 41 EStG (Lohnsteuerbescheinigung) "
         "an alle Beschaeftigten bis zum 28. Februar 2022 versandt. Elektronische Uebermittlung "
         "an das Bundeszentralamt fuer Steuern via ELStAM erfolgt; keine Korrekturen erforderlich."),
        ("Unterschriften",
         signatures("Birgit Schmitt", "HR-Leitung REG", "Brennhagen Elektronik GmbH",
                    "Dr. Heike Berger", "Group Tax Director", R["name"],
                    place="Heilbronn", date_str_="28. Februar 2022")),
    ])


print("OK regen_roehrig_19_ma.py – 55 docs written (DD / LoI / SPA / NDA / PMI / Pipeline)")
