"""Brennhagen AG / 02_Konsolidierte_Finanzen – 68 docs."""
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

BASE = f"{_ROOT}/roehrig_large/02_Konsolidierte_Finanzen"
H = {"name": R["name"], "addr": R["addr"], "hrb": R["hrb"]}


# ── 6 Bankkorrespondenzen ──────────────────────────────────────────────────
def bankkorr(fname, bank, kontaktperson, bank_addr, jahr, kreditrahmen,
             utilization, themen):
    write_doc(f"{BASE}/{fname}", H,
        f"Bankkorrespondenz {bank} – Jahresgespraech {jahr}",
        subtitle=f"Beziehungsbericht der Treasury-Funktion, Stand {jahr}",
        sections=[
            ("Korrespondenzpartner",
             f"Bank: {bank}\n{bank_addr}\n\nSenior Relationship Manager: {kontaktperson}\n\n"
             f"Brennhagen-Verantwortliche: Laura Bauer (CFO), Markus Pflanzer (Group Treasurer)"),
            ("Bankenbeziehung im Ueberblick",
             f"Die {bank.split()[0]}-Beziehung der Brennhagen Elektronik AG besteht seit 2014 als Teil der "
             f"Kernbankenstruktur (5 Hausbanken: Deutsche Bank, Commerzbank, UniCredit, BNP Paribas, HSBC). "
             f"Im Berichtsjahr {jahr} wurde der bestehende Kreditrahmen von {kreditrahmen} Mio. EUR mit "
             f"Auslastung {utilization} % gefuehrt. Die Bank ist zudem Konsortialteilnehmerin im "
             f"Konsortialkreditvertrag 2022 (siehe REA_Konsortialkredit_Rahmenvertrag_2022).\n\n"
             f"Die Bank uebernimmt operativ: Kontokorrentlinie, Avalrahmen fuer Exportbuergschaften, "
             f"FX-Hedging in CNY/CZK/HUF/PLN, Trade-Finance fuer Auftraege > 5 Mio. EUR."),
            ("Themen des Jahresgespraechs " + jahr,
             ("list", themen)),
            ("Vereinbarte Konditionen / Updates",
             f"Konditionen werden jaehrlich im Februar/Maerz aktualisiert. Aktuelle Margen ueber EURIBOR "
             f"6M: +95 bp (Konsortialkredit), +75 bp (bilaterale Linien). Avalprovision unveraendert "
             f"0,8 % p. a. auf in Anspruch genommene Avale. Reporting-Standards gemaess Konsortialkreditvertrag "
             f"(Quarterly Compliance Certificate + Annual Report binnen 120 Tagen)."),
            ("Naechste Schritte",
             f"Naechstes Jahresgespraech: Februar/Maerz {int(jahr)+1}. Halbjaehrliches Strategie-Update durch "
             f"den Group Treasurer im H1. Aktuelle Themen-Pipeline: Pruefung Schuldscheindarlehen "
             f"(150 Mio. EUR) Q2/{int(jahr)+1}, Refinanzierung Konsortialkredit zum Ablauftermin 2027."),
            ("Unterschrift",
             signatures("Laura Bauer", "CFO", R["name"],
                        kontaktperson, "Senior Relationship Manager", bank,
                        place="Stuttgart", date_str_=f"15. Februar {jahr}")),
        ])


bankkorr("REA_Deutsche_Bank_A_Bankkorrespondenz_2022.docx",
         "Deutsche Bank AG", "Dr. Friedrich Stuetzel", "Taunusanlage 12, 60325 Frankfurt am Main", "2022",
         500, 42, [
    "Auftaktgespraech IPO-Begleitung (Joint Bookrunner Mandat ab Mai 2022)",
    "Aufstockung Avalrahmen von 80 auf 120 Mio. EUR fuer Exportauftraege Mexiko / China",
    "Erweiterung des Konsortialkredits um Tranche B (Working-Capital 100 Mio. EUR)",
    "FX-Strategie 2022: Hedging-Quote 80 % der erwarteten EUR-Exposures",
    "Cash-Pooling-Strukturoptimierung mit Tochtergesellschaften REG / RSG / RPL",
    "ESG-linked Loan Pruefung (Sustainability-linked Margin Adjustment +/- 5 bp)",
])
bankkorr("REA_Deutsche_Bank_A_Bankkorrespondenz_2023.docx",
         "Deutsche Bank AG", "Dr. Friedrich Stuetzel", "Taunusanlage 12, 60325 Frankfurt am Main", "2023",
         500, 38, [
    "Rueckblick IPO 14.10.2022 – erfolgreiche Plazierung (Emissionserloes 612 Mio. EUR)",
    "Verlagerung von 180 Mio. EUR Verschuldung in Tilgung Konsortialkredit Tranche A",
    "Pruefung Schuldscheindarlehen 2024 (Volumen 150-200 Mio. EUR, Laufzeit 5/7/10 Jahre)",
    "FX-Strategie 2023: anhaltende EUR/CNY-Volatilitaet, Hedging-Quote auf 90 % erhoeht",
    "ESG-Reporting fuer Sustainability-linked Loan Bedingungen erfuellt (Scope 1+2 -15 %)",
    "Erweiterung Avalrahmen auf 150 Mio. EUR fuer Asien-Geschaeft (Werk Shanghai)",
])
bankkorr("REA_Commerzbank_AG_Bankkorrespondenz_2022.docx",
         "Commerzbank AG", "Stefanie Erbach", "Kaiserplatz, 60311 Frankfurt am Main", "2022",
         200, 35, [
    "Konsortialkredit-Beteiligung Tranche A (40 Mio. EUR)",
    "Joint Bookrunner Mandat IPO Q4/2022",
    "Mittelstandsfinanzierung Werk Heilbronn Erweiterung (22 Mio. EUR bilateral)",
    "Cash-Management Konzern (Sweep-Konten EUR / CHF / PLN)",
    "Trade-Finance Bosch / VW-Auftrag (Exportbuergschaften)",
])
bankkorr("REA_Commerzbank_AG_Bankkorrespondenz_2023_2024-03-01.docx",
         "Commerzbank AG", "Stefanie Erbach", "Kaiserplatz, 60311 Frankfurt am Main", "2023",
         200, 28, [
    "Erweiterung des Avalrahmens fuer Werkserweiterungen Heilbronn (Linie 4 BMS-12)",
    "Aufbau gruener Investitionsrahmen (KfW-Tilgungszuschuss Energieeffizienz 18 %)",
    "Hedging EUR/CZK / EUR/HUF / EUR/PLN ueber Commerzbank-Plattform",
    "Cash-Pooling-Erweiterung um Tochter RCN Shanghai (CNY-Konto, CSCRS-Reporting)",
    "Schuldscheindarlehen-Mandat-Anfrage in 2024 unterstuetzt durch Commerzbank Joint Lead",
])
bankkorr("REA_UniCredit_Bank__Bankkorrespondenz_2022.docx",
         "UniCredit Bank AG (HypoVereinsbank)", "Marcus Reinhold",
         "Arabellastrasse 12, 81925 Muenchen", "2022",
         180, 30, [
    "Konsortialkredit-Beteiligung Tranche B (35 Mio. EUR)",
    "Italien-Geschaeft (Stellantis Mirafiori) – Trade-Finance via Mailand-Filiale",
    "Hedging-Plattform EUR/USD (Mexiko-Exporte) und EUR/PLN (Werk Katowice)",
    "Equity-Beteiligungspruefung an Brennhagen Polska – nicht weiterverfolgt",
    "ESG-Beratung CSRD-Vorbereitung (in Kooperation mit UniCredit Sustainable Finance)",
])
bankkorr("REA_UniCredit_Bank__Bankkorrespondenz_2023_v2.docx",
         "UniCredit Bank AG (HypoVereinsbank)", "Marcus Reinhold",
         "Arabellastrasse 12, 81925 Muenchen", "2023",
         180, 26, [
    "Tilgung Konsortialkredit Tranche B um 25 Mio. EUR aus IPO-Erloesen",
    "Hedging-Volumen EUR/USD (Mexiko / Stellantis-Auftrag) deutlich erhoeht auf 18 Mio. USD p. a.",
    "Italien-Pipeline: Stellantis Cassino + Termoli Auftraege Q4/2023 erfolgreich abgeschlossen",
    "Beratung zur Pruefung Schuldscheindarlehen 2024 (UniCredit Mit-Konsortium)",
    "Aufstockung des Cash-Pools um Brennhagen Hungary Kft. (Mandat ab 1.1.2024)",
])
bankkorr("REA_BNP_Paribas_Bankkorrespondenz_2022.docx",
         "BNP Paribas S.A., Niederlassung Frankfurt", "Veronique Lefebvre",
         "Senckenberganlage 19, 60325 Frankfurt am Main", "2022",
         150, 22, [
    "FX-Hedging EUR/CNY (Werk Shanghai) – Kernpartner mit dezidiertem Asien-Desk",
    "China-Trade-Finance fuer OEM-Auftraege (Mercedes-Benz Beijing, Stellantis Wuhan)",
    "Eroeffnung CNY-Konto in Shanghai (CFETS-Anbindung), Settlement T+1",
    "Cross-Border Cash Management China <-> EU im Rahmen SAFE-Regulierung",
    "Beratung Renminbi-Anleihe (Dim Sum Bond) als Alternativfinanzierung – nicht weiterverfolgt",
])
bankkorr("REA_BNP_Paribas_Bankkorrespondenz_2023.docx",
         "BNP Paribas S.A., Niederlassung Frankfurt", "Veronique Lefebvre",
         "Senckenberganlage 19, 60325 Frankfurt am Main", "2023",
         150, 25, [
    "FX-Hedging EUR/CNY erweitert (Hedging-Quote auf 90 % erhoeht angesichts CNY-Volatilitaet)",
    "China-Werk Shanghai Aufbauphase: Lokalfinanzierung in CNY (RCN-eigenstaendig, 120 Mio. CNY)",
    "ESG-Linked-Loan Pruefung gemeinsam mit BNP Paribas Sustainable Finance",
    "Aufbau Trade-Finance Wuhu (Stellantis JV) – ab Q3/2023 produktiv",
    "Eskalation Devisenkontrolle SAFE bei CNY-Repatrierung (geloest via lokalen Counsel)",
])
bankkorr("REA_HSBC_Deutschlan_Bankkorrespondenz_2022.docx",
         "HSBC Continental Europe S.A., Niederlassung Duesseldorf", "Alexander Lenton",
         "Hansaallee 3, 40549 Duesseldorf", "2022",
         100, 18, [
    "Asien-Schwerpunkt (China, Suedkorea, Japan) – Werk Shanghai Lokalfinanzierung",
    "Trade-Finance Korea (Hyundai-Auftrag BMS-12 Pilot) ueber HSBC Seoul",
    "Cross-Border Settlement CNY / JPY / KRW ueber HSBC-Plattform",
    "Beratung China-Subvention SAFE-Regulierung",
    "Working-Capital-Linie 25 Mio. EUR (vollstaendig unbeansprucht; strategische Reserve)",
])
bankkorr("REA_HSBC_Deutschlan_Bankkorrespondenz_2023.docx",
         "HSBC Continental Europe S.A., Niederlassung Duesseldorf", "Alexander Lenton",
         "Hansaallee 3, 40549 Duesseldorf", "2023",
         100, 20, [
    "Aufbau Trade-Finance Hyundai BMS-12 Programm (KRW-Settlement, Volumen 22 Mio. KRW p. a.)",
    "Pruefung Aufbau Lokalfinanzierung Shanghai (CNY 80 Mio. – wurde an BNP vergeben)",
    "Beratung CFE (Cross-Border Foreign Exchange) Optimierung China <-> EU",
    "Hedging EUR/KRW erweitert (Hyundai-Exposure)",
    "Sustainability-Reporting im HSBC ESG-Framework auf Konzernebene verlinkt",
])


# ── 8 Covenant Compliance Certificates ───────────────────────────────────────
def covenant(fname, quartal, jahr, ebitda, net_debt, leverage, icr, equity_ratio,
             covenant_status="EINGEHALTEN", anmerkung=""):
    write_doc(f"{BASE}/{fname}", H,
        f"Covenant Compliance Certificate – {quartal} {jahr}",
        subtitle=f"Konsortialkredit-Reporting; Quartals-Compliance fuer das KW {quartal}",
        sections=[
            ("Adressat / Rechtsgrundlage",
             f"An die Konsortialfuehrerin Deutsche Bank AG sowie an die uebrigen Konsortialteilnehmer "
             f"(Commerzbank AG, UniCredit Bank AG, BNP Paribas S.A., HSBC Continental Europe S.A.). "
             f"Vorlage gemaess § 11 Abs. 3 des Konsortialkredit-Rahmenvertrages vom 14. Maerz 2022 "
             f"(Faciliy-Volumen: 250 Mio. EUR / Laufzeit bis 14.3.2027)."),
            ("Berichtszeitraum",
             f"Quartalsabschluss: {quartal} {jahr}. Konsolidierte Kennzahlen (IFRS, ungeprueft "
             f"falls Q1/Q2/Q3; geprueft Q4):"),
            ("Finanzkennzahlen",
             [["Kennzahl", "Wert", "Covenant", "Status"],
              ["Konsolidiertes EBITDA (LTM, Mio. EUR)", f"{ebitda:.1f}", ">= 50,0", "ok"],
              ["Nettoverschuldung (Mio. EUR)", f"{net_debt:.1f}", "n/a", "Info"],
              ["Leverage Net Debt / EBITDA (LTM)", f"{leverage:.2f}", "<= 3,0", "ok" if leverage <= 3.0 else "BREACH"],
              ["Interest Coverage Ratio (ICR)", f"{icr:.1f}", ">= 4,0", "ok" if icr >= 4.0 else "BREACH"],
              ["Eigenkapitalquote (%)", f"{equity_ratio:.1f}", ">= 30,0", "ok" if equity_ratio >= 30.0 else "BREACH"],
              ]),
            ("Erklaerung des CFO",
             f"Hiermit bestaetigt die Geschaeftsfuehrung der Brennhagen Elektronik AG, dass zum "
             f"{quartal}-Stichtag {jahr} samtliche im Konsortialkredit-Rahmenvertrag definierten "
             f"Financial Covenants {covenant_status} wurden. Die Berechnung erfolgt auf Basis der "
             f"in den IFRS-Konzernzahlen ausgewiesenen Werte sowie der Definitionen in Anhang 3 "
             f"des Konsortialkreditvertrages. {anmerkung}"),
            ("Berichtspflichten und Anlagen",
             "Beigefuegt: (1) Konsolidierte GuV und Bilanz Quartalsabschluss (Auszug); (2) "
             "Berechnungsschema fuer LTM-EBITDA inkl. Bereinigungen; (3) Bestaetigung des Wirtschafts"
             "pruefers (KPMG AG WPG) fuer den Jahresabschluss (nur Q4-Reporting); (4) Bestaetigung "
             "Group Treasurer Markus Pflanzer ueber Cash-Equivalents und Verschuldungsstand."),
            ("Unterschriften",
             signatures("Laura Bauer", "CFO", R["name"],
                        "Markus Pflanzer", "Group Treasurer", R["name"],
                        place="Stuttgart", date_str_=f"30 Tage nach {quartal}-Ende {jahr}")),
        ])


covenant("REA_Covenant_Compliance_2022_Q1.docx", "Q1", "2022", 67.2, 198.5, 0.74, 18.3, 38.4)
covenant("REA_Covenant_Compliance_2022_Q2_FINAL.docx", "Q2", "2022", 68.4, 215.2, 0.81, 17.9, 37.8)
covenant("REA_Covenant_Compliance_2022_Q3.docx", "Q3", "2022", 70.1, 224.8, 0.85, 17.4, 36.5,
    anmerkung="Q3 mit zusaetzlichen IPO-Vorbereitungskosten 4,2 Mio. EUR belastet (im LTM-EBITDA als One-Time-Item bereinigt gemaess Anhang 3 § 5).")
covenant("REA_Covenant_Compliance_2022_Q4.docx", "Q4", "2022", 73.8, 78.4, 0.27, 24.2, 48.6,
    anmerkung="Q4 zeigt deutliche Entschuldung infolge IPO (Erloes 612 Mio. EUR per 14.10.2022; Tilgung Tranche A 180 Mio. EUR sowie Tranche B 35 Mio. EUR).")
covenant("REA_Covenant_Compliance_2023_Q1.docx", "Q1", "2023", 75.6, 82.1, 0.29, 23.8, 50.2)
covenant("REA_Covenant_Compliance_2023_Q2.docx", "Q2", "2023", 77.4, 88.5, 0.31, 22.4, 51.8)
covenant("REA_Covenant_Compliance_2023_Q3.docx", "Q3", "2023", 78.9, 91.2, 0.32, 21.9, 52.4)
covenant("REA_Covenant_Compliance_2023_Q4.docx", "Q4", "2023", 74.3, 84.6, 0.32, 22.8, 53.1,
    anmerkung="Vollstaendiger Jahresabschluss 2023 testiert KPMG AG WPG am 12. Februar 2024 ohne Beanstandung.")


# ── 28 FX-Hedge Reports (4 Waehrungen x 7 Quartale = 28) ────────────────────
def fx_hedge(fname, waehrung, quartal, jahr, exposure_mio, hedge_quote_pct,
             forward_rate, spot_rate, mtm_eur, kommentar):
    cur_pair = f"EUR/{waehrung}"
    write_doc(f"{BASE}/{fname}", H,
        f"FX-Hedging Bericht {cur_pair} – {quartal} {jahr}",
        subtitle="Treasury-Quartalsbericht zur Devisensicherung",
        sections=[
            ("Berichtszweck",
             f"Quartalsbericht zur Absicherung der EUR/{waehrung}-Risiken der Brennhagen-Gruppe. Berichts-"
             f"empfaenger: CFO Laura Bauer, Pruefungsausschuss-Vorsitz Prof. Voss, Group Treasurer "
             f"Markus Pflanzer. Vorlagepflicht gemaess Treasury-Richtlinie 2022 sowie IFRS 7 / IFRS 9 "
             f"Disclosure-Anforderungen."),
            ("Exposure-Uebersicht",
             f"Im Berichtsquartal lag das EUR/{waehrung}-Exposure aus operativem Geschaeft sowie aus "
             f"Intercompany-Positionen bei rund {exposure_mio:.1f} Mio. EUR-Aequivalent. Wesentliche "
             f"Treiber: " + ({
                 "CNY": "Werk Brennhagen (Shanghai) Co. Ltd. (Lieferungen + Lokalkosten), Liefervertraege Mercedes-Benz China und Stellantis Wuhan.",
                 "CZK": "Werk Brennhagen CZ s.r.o. (Brno) – Steckverbinder-Produktion; Materialkosten und Lohnkosten in CZK.",
                 "HUF": "Werk Brennhagen Hungary Kft. (Gyoer) – Sensorik-Produktion; Loehne und Energiekosten HUF.",
                 "PLN": "Werk Brennhagen Polska Sp. z o.o. (Katowice) – EMS / SMD; Loehne und Investitionsaufwand PLN.",
             }[waehrung])),
            ("Hedge-Position",
             [["Position", "Wert"],
              ["Hedging-Quote", f"{hedge_quote_pct} %"],
              ["Eingesetzte Instrumente", "Devisenterminkontrakte (Forwards), z. T. Cross-Currency Swaps"],
              ["Counterparties", "Deutsche Bank AG, " + ({"CNY":"BNP Paribas","CZK":"UniCredit","HUF":"UniCredit","PLN":"Commerzbank"}[waehrung])],
              ["Durchschnittlicher Forward-Kurs", f"{forward_rate:.4f}"],
              ["Spot-Kurs zum Quartalsende", f"{spot_rate:.4f}"],
              ["Mark-to-Market (Mio. EUR)", f"{mtm_eur:+.1f}"],
              ["Tenorprofil (Anteile)", "0-3M 40 %; 3-6M 30 %; 6-12M 25 %; > 12M 5 %"]]),
            ("Kommentar",
             kommentar),
            ("Hedge Accounting (IFRS 9)",
             "Saemtliche Sicherungsbeziehungen werden als Cashflow-Hedges designiert und im Rahmen "
             "der Hedge-Accounting-Methodik gemaess IFRS 9 bilanziert. Effektivitaet wird prospektiv "
             "und retrospektiv getestet (qualitative Dokumentation Hedge Documentation File je Hedge). "
             "Ineffective Portion wird im Finanzergebnis erfasst; effektive Portion im Other Comprehensive Income (OCI)."),
            ("Naechste Schritte",
             f"Anpassung Hedge-Quote im Folgequartal gemaess rollierendem 12M-Forecast. Quartalsweise "
             f"Treasury-Review-Sitzung mit Group Treasurer und CFO am 20. Tag nach Quartalsende."),
            ("Unterschriften",
             signatures("Markus Pflanzer", "Group Treasurer", R["name"],
                        "Laura Bauer", "CFO", R["name"],
                        place="Stuttgart", date_str_=f"15. Tag nach {quartal} {jahr}")),
        ])


# FX Hedge data table (Quartal, Waehrung, exposure_mio, hedge_quote, fwd, spot, mtm, kommentar)
FX_DATA = [
    # CNY
    ("CNY","2022 Q1", 18.4, 80, 7.1240, 7.0985, +0.5, "Yuan robust gegenueber Euro infolge Zhang Wei-Krise; Hedging-Quote zur Stabilisierung Werks-Ergebnisses erforderlich."),
    ("CNY","2022 Q2", 19.2, 82, 7.0850, 7.1240, -0.3, "Volatilitaet erhoeht durch Shanghai-Lockdown; Sicherungsstrategie unveraendert."),
    ("CNY","2022 Q4", 21.4, 85, 7.4180, 7.4850, +1.2, "Yuan-Schwaeche zum Jahresende; Hedging-Gewinne im OCI eingebucht."),
    ("CNY","2023 Q1", 22.1, 85, 7.4220, 7.3950, +0.8, "Anhaltende CNY-Volatilitaet; Treasury erwaegt Erhoehung Hedging-Quote auf 90 %."),
    ("CNY","2023 Q2", 23.6, 88, 7.5980, 7.7240, +2.1, "Hedging-Quote auf 88 % erhoeht; Mark-to-Market positiv durch CNY-Schwaeche."),
    ("CNY","2023 Q3", 24.8, 90, 7.6450, 7.6280, +0.4, "Hedging-Quote auf 90 % erhoeht (entspricht Treasury-Beschluss vom 14.8.2023)."),
    ("CNY","2023 Q4", 26.2, 90, 7.7180, 7.7980, +1.8, "Stabile Hedging-Performance; Volumen mit Werk-Shanghai-Ausbau gestiegen."),
    # CZK
    ("CZK","2022 Q1", 12.4, 70, 24.30, 24.42, +0.1, "Tschechische Krone leicht schwacher; geringes Mark-to-Market."),
    ("CZK","2022 Q2", 12.8, 72, 24.65, 24.71, +0.1, "Stabile CZK-Entwicklung; Hedging-Quote unveraendert."),
    ("CZK","2022 Q3", 13.2, 75, 24.42, 24.51, +0.2, "Volatilitaetsanstieg im Sommer; Quote leicht erhoeht."),
    ("CZK","2022 Q4", 13.8, 75, 24.18, 24.10, -0.1, "CZK staerker zum Jahresende; geringer Wechselkurs-Verlust."),
    ("CZK","2023 Q1", 14.1, 78, 23.85, 23.50, -0.5, "CZK-Aufwertung nach CNB-Zinserhoehung; Hedging gegen Aufwertung schwer."),
    ("CZK","2023 Q2", 14.4, 80, 23.65, 23.78, +0.2, "Werk Brno meldet Lohnsteigerungen; Materialkosten in CZK fluktuierend."),
    ("CZK","2023 Q3", 14.8, 80, 24.10, 24.30, +0.3, "CZK-Abwertung zum Ende Q3; Hedging-Gewinne stabilisieren Ergebnis."),
    ("CZK","2023 Q4", 15.2, 82, 24.62, 24.80, +0.4, "Ergebnis Werk Brno mit Hedging stabilisiert auf Plan-Ergebnis."),
    # HUF
    ("HUF","2022 Q1", 10.2, 65, 365.4, 369.2, +0.3, "Forint-Schwaeche nach EZB-/MNB-Spread; Hedging stabilisiert."),
    ("HUF","2022 Q2", 10.4, 68, 385.6, 396.8, +0.9, "Erhebliche HUF-Schwaeche infolge Energie-Importabhaengigkeit Ungarn."),
    ("HUF","2022 Q3", 10.6, 70, 410.2, 412.4, +0.4, "Anhaltend hohe Volatilitaet; Werk Gyoer Loehne und Energiekosten HUF-belastet."),
    ("HUF","2023 Q1", 10.9, 75, 392.5, 379.8, -1.2, "HUF-Aufwertung nach MNB-Stabilisierungspolitik; Hedging-Verlust ausgewiesen."),
    ("HUF","2023 Q2", 11.2, 75, 378.4, 372.2, -0.4, "HUF weiter staerker; Hedging-Quote bei 75 % gehalten."),
    ("HUF","2023 Q3", 11.4, 78, 385.6, 388.4, +0.2, "Volatilitaet bleibt erhoeht; Hedging-Quote leicht erhoeht."),
    ("HUF","2023 Q4", 11.6, 80, 380.8, 382.5, +0.3, "Werk Gyoer Ergebnis durch Hedging stabilisiert."),
    # PLN
    ("PLN","2022 Q1", 22.4, 80, 4.6420, 4.6520, +0.2, "Zloty-Stabilitaet trotz Krieg in der Ukraine (Nachbarland Polen)."),
    ("PLN","2022 Q2", 23.1, 82, 4.6920, 4.7240, +0.4, "Erhoehte Volatilitaet; Werk Katowice belastet von Energiekostensteigerungen."),
    ("PLN","2022 Q3", 23.8, 85, 4.7480, 4.8240, +0.9, "PLN-Schwaeche; Hedging-Gewinne stabilisieren Werks-Performance."),
    ("PLN","2022 Q4", 24.2, 85, 4.7120, 4.6810, -0.4, "Zloty-Aufwertung zum Jahresende infolge NBP-Zinserhoehungen."),
    ("PLN","2023 Q1", 24.6, 85, 4.6850, 4.6750, -0.1, "Stabile PLN-Entwicklung; Werk Katowice mit Lieferengpaessen Halbleiter."),
    ("PLN","2023 Q2", 25.1, 87, 4.5240, 4.4380, -1.1, "Deutliche PLN-Aufwertung; Hedging-Verlust eingebucht."),
    ("PLN","2023 Q3", 25.4, 90, 4.4980, 4.6240, +1.4, "PLN-Schwaeche; Hedging-Gewinne kompensieren Q2-Verlust."),
    ("PLN","2023 Q4", 25.8, 90, 4.6420, 4.3380, -3.4, "Erhebliche PLN-Aufwertung Q4; bedeutender Hedging-Verlust eingebucht."),
]

# Map filenames to data
fx_files = {
    ("CNY","2022 Q1"): "REA_FX_Hedge_EUR_CNY_2022_Q1.docx",
    ("CNY","2022 Q2"): "REA_FX_Hedge_EUR_CNY_2022_Q2.docx",
    ("CNY","2022 Q4"): "REA_FX_Hedge_EUR_CNY_2022_Q4.docx",
    ("CNY","2023 Q1"): "REA_FX_Hedge_EUR_CNY_2023_Q1.docx",
    ("CNY","2023 Q2"): "REA_FX_Hedge_EUR_CNY_2023_Q2.docx",
    ("CNY","2023 Q3"): "REA_FX_Hedge_EUR_CNY_2023_Q3.docx",
    ("CNY","2023 Q4"): "REA_FX_Hedge_EUR_CNY_2023_Q4.docx",
    ("CZK","2022 Q1"): "REA_FX_Hedge_EUR_CZK_2022_Q1.docx",
    ("CZK","2022 Q2"): "REA_FX_Hedge_EUR_CZK_2022_Q2.docx",
    ("CZK","2022 Q3"): "REA_FX_Hedge_EUR_CZK_2022_Q3.docx",
    ("CZK","2022 Q4"): "REA_FX_Hedge_EUR_CZK_2022_Q4.docx",
    ("CZK","2023 Q1"): "REA_FX_Hedge_EUR_CZK_2023_Q1.docx",
    ("CZK","2023 Q2"): "REA_FX_Hedge_EUR_CZK_2023_Q2.docx",
    ("CZK","2023 Q3"): "REA_FX_Hedge_EUR_CZK_2023_Q3.docx",
    ("CZK","2023 Q4"): "REA_FX_Hedge_EUR_CZK_2023_Q4.docx",
    ("HUF","2022 Q1"): "REA_FX_Hedge_EUR_HUF_2022_Q1.docx",
    ("HUF","2022 Q2"): "REA_FX_Hedge_EUR_HUF_2022_Q2.docx",
    ("HUF","2022 Q3"): "REA_FX_Hedge_EUR_HUF_2022_Q3.docx",
    ("HUF","2023 Q1"): "REA_FX_Hedge_EUR_HUF_2023_Q1_WIP.docx",
    ("HUF","2023 Q2"): "REA_FX_Hedge_EUR_HUF_2023_Q2.docx",
    ("HUF","2023 Q3"): "REA_FX_Hedge_EUR_HUF_2023_Q3.docx",
    ("HUF","2023 Q4"): "REA_FX_Hedge_EUR_HUF_2023_Q4.docx",
    ("PLN","2022 Q1"): "REA_FX_Hedge_EUR_PLN_2022_Q1.docx",
    ("PLN","2022 Q2"): "REA_FX_Hedge_EUR_PLN_2022_Q2_reviewed.docx",
    ("PLN","2022 Q3"): "REA_FX_Hedge_EUR_PLN_2022_Q3.docx",
    ("PLN","2022 Q4"): "REA_FX_Hedge_EUR_PLN_2022_Q4.docx",
    ("PLN","2023 Q1"): "REA_FX_Hedge_EUR_PLN_2023_Q1.docx",
    ("PLN","2023 Q2"): "REA_FX_Hedge_EUR_PLN_2023_Q2.docx",
    ("PLN","2023 Q3"): "REA_FX_Hedge_EUR_PLN_2023_Q3.docx",
    ("PLN","2023 Q4"): "REA_FX_Hedge_EUR_PLN_2023_Q4.docx",
}

for cur, qtr, exp, hq, fwd, spot, mtm, comm in FX_DATA:
    quartal, jahr = qtr.split()[1], qtr.split()[0]
    fn = fx_files[(cur, qtr)]
    fx_hedge(fn, cur, quartal, jahr, exp, hq, fwd, spot, mtm, comm)


# ── 7 IFRS Bilanzierungsrichtlinien ─────────────────────────────────────────
def ifrs_richtlinie(fname, standard, titel, scope_text, kern_regelungen, beispiele_btp, schaetzungen):
    write_doc(f"{BASE}/{fname}", H,
        f"IFRS-Bilanzierungsrichtlinie {standard} – {titel}",
        subtitle="Verbindlich fuer alle Konzerngesellschaften der Brennhagen-Gruppe, Stand 2023",
        sections=[
            ("Geltungsbereich",
             f"Diese Bilanzierungsrichtlinie konkretisiert die Anwendung von {standard} ({titel}) "
             f"in der Brennhagen-Gruppe. Sie gilt fuer alle Konzerngesellschaften (REA, REG, RSG, RPL, "
             f"RCZ, RHU, RCN, RHO) und ist Pflicht-Bestandteil der Konzern-Reportingrichtlinie 2023. "
             f"Pruefer: KPMG AG WPG (Audit Lead Dr. Maximilian Brand)."),
            ("Scope und Definitionen", scope_text),
            ("Wesentliche Regelungen",
             ("list", kern_regelungen)),
            ("Anwendung in der Brennhagen-Gruppe (Beispiele)", beispiele_btp),
            ("Wesentliche Ermessenspielraeume und Schaetzungen",
             schaetzungen),
            ("Reporting-Anforderungen",
             "Quartalsweise Berichterstattung im IFRS-Konsolidierungstool (HFM / OneStream). "
             "Ausserplanmaessige Anhaltspunkte (z. B. Impairment-Indikatoren) sind unverzueglich an "
             "die Konzern-Bilanzierung (Group Controller Florian Maier) zu melden. Aenderungen dieser "
             "Richtlinie beduerfen der Zustimmung des CFO."),
            ("Letzte Aktualisierung / Verantwortlich",
             f"Letzte Aktualisierung: 14. November 2023. Verantwortlich: Group Controller "
             f"Florian Maier; Review CFO Laura Bauer; finale Freigabe Pruefungsausschuss "
             f"(Sitzung 14.9.2023)."),
        ])


ifrs_richtlinie("REA_IFRS_Bilanzierungsrichtlinie_IAS_12_Ertragsteuern_2023.docx",
    "IAS 12", "Ertragsteuern",
    "IAS 12 regelt die Bilanzierung von Ertragsteuern (laufende und latente Steuern) einschliesslich "
    "der Behandlung von steuerlichen Verlustvortraegen, Steueranreizen und der Auswirkungen von "
    "Konsolidierungsmassnahmen. Die Richtlinie konkretisiert die Methodik fuer die Gruppe und die "
    "Schnittstelle zu lokalen Steuerdeklarationen.",
    ["Laufende Steuern werden zu den nominalen Steuersaetzen erfasst (Deutschland 30 %, Polen 19 %, "
     "Tschechien 19 %, Ungarn 9 %, China 25 %).",
     "Latente Steuern werden auf temporaere Differenzen zwischen IFRS-Buchwerten und Steuerbasis "
     "gebildet (Liability-Methode).",
     "Verlustvortraege werden als latente Steuer-Aktiva ausgewiesen, soweit deren Nutzbarkeit "
     "wahrscheinlich ist (substantielle Vorhersagbarkeit; Pruefintervall jaehrlich).",
     "Country-by-Country Reporting gemaess BEPS Action 13 obligatorisch (jaehrliche Erstellung "
     "durch PwC AG WPG fuer Brennhagen-Gruppe als Multinational).",
     "Steuersatz-Aenderungen werden im Periodengewinn (P&L) erfasst, soweit nicht im OCI gehoerig."],
    "Die Brennhagen-Gruppe hat zum 31.12.2023 latente Steueraktiva 14,8 Mio. EUR (u. a. Verlustvortrag "
    "RCN Shanghai aus Anlaufphase, Pensions-Rueckstellungen Deutschland, Rueckstellungs-Differenzen). "
    "Latente Steuerpassiva 22,4 Mio. EUR (u. a. Goodwill aus M&A-Aktivitaeten). Effektive "
    "Konzernsteuerquote 2023: 28,3 % (Plan 29,0 %).",
    "Werthaltigkeit der latenten Steueraktiva (insbesondere RCN Shanghai mit kumuliertem Verlust "
    "12 Mio. EUR aus Aufbauphase 2022-2023) basiert auf Geschaeftsplan mit erwartetem Break-Even 2025 "
    "und Wirtschaftlichkeit ab 2026. Annahme: stabile Steuergesetzgebung China; Risiko: Aenderung "
    "der lokalen Steuerverguenstigungen.")

ifrs_richtlinie("REA_IFRS_Bilanzierungsrichtlinie_IAS_19_Pensionen_2023.docx",
    "IAS 19", "Leistungen an Arbeitnehmer (Pensionsverpflichtungen)",
    "IAS 19 regelt die Bilanzierung von Leistungen an Arbeitnehmer einschliesslich kurzfristiger "
    "Verguetungen, leistungsorientierter (defined benefit) und beitragsorientierter (defined "
    "contribution) Versorgungsplaene sowie sonstiger langfristiger Leistungen. Bei der Brennhagen-Gruppe "
    "ueberwiegen die Pensionsverpflichtungen aus Deutschland (Direktzusagen + Unterstuetzungskasse).",
    ["Defined Benefit Obligations (DBO) werden mittels Projected-Unit-Credit-Methode bewertet; "
     "Bewertungsstichtag jeweils 31.12.; aktuarisches Gutachten durch Heubeck AG (Koeln).",
     "Diskontierungszinssatz: gemaess hochwertigen Unternehmensanleihen (AA-Rating EUR Bond) mit "
     "kongruenter Laufzeit; Stichtag 31.12.2023: 3,40 % (Vorjahr 3,75 %).",
     "Gehaltstrend-Annahmen: 2,5 % p. a. (DE), Inflationstrend 2,0 %, Rententrend 1,75 %.",
     "Aktuarische Gewinne und Verluste werden im OCI (Other Comprehensive Income) erfasst "
     "(IAS 19 Re-Measurement-Komponente).",
     "Plan Assets (Rueckdeckungsversicherungen bei Allianz Lebensversicherung AG und Talanx) "
     "werden zum beizulegenden Zeitwert bewertet."],
    "Die Brennhagen-Gruppe hat zum 31.12.2023 eine DBO von 78,4 Mio. EUR (Vorjahr 82,1 Mio. EUR; "
    "Reduktion durch Zinsanstieg). Plan Assets 32,6 Mio. EUR; Nettoverpflichtung 45,8 Mio. EUR "
    "(Vorjahr 48,2 Mio. EUR). Wesentliche Pensionsplaene: Direktzusagen Vorstand REA (8 Personen, "
    "DBO 14,8 Mio. EUR), Unterstuetzungskasse REG Heilbronn (DBO 42,8 Mio. EUR), Direktzusagen "
    "Fuehrungskraefte RSG Muenchen (DBO 18,4 Mio. EUR). Auslandsplaene CZK/HUF/PLN sind "
    "defined-contribution-Plaene (Beitragspflicht).",
    "Sensitivitaeten: Diskontierungssatz +/- 50 bp aendert DBO um +/- 5,8 Mio. EUR. Lebenserwartung "
    "+/- 1 Jahr aendert DBO um +/- 2,1 Mio. EUR. Gehaltstrend +/- 50 bp aendert DBO um +/- 1,4 Mio. EUR. "
    "Heubeck-Richttafeln 2018 G werden verwendet (Update auf 2024 G in Pruefung).")

ifrs_richtlinie("REA_IFRS_Bilanzierungsrichtlinie_IAS_38_Immaterielle_Werte_2023.docx",
    "IAS 38", "Immaterielle Vermoegenswerte (Patente, Entwicklungskosten, Software)",
    "IAS 38 regelt die Bilanzierung immaterieller Vermoegenswerte einschliesslich der Aktivierung "
    "von Entwicklungskosten und der Nicht-Aktivierung von Forschungskosten. Bei der Brennhagen-Gruppe "
    "von besonderer Bedeutung wegen substantieller F&E-Aktivitaeten in Heilbronn (REG) und Muenchen "
    "(RSG, Software).",
    ["Forschungskosten werden in der Periode des Anfalls aufwandswirksam erfasst.",
     "Entwicklungskosten werden aktiviert, wenn die sechs Kriterien des IAS 38.57 kumulativ erfuellt "
     "sind (Technische Machbarkeit, Absicht zur Fertigstellung, Faehigkeit zur Nutzung/Verkauf, "
     "wirtschaftlicher Nutzen, Verfuegbarkeit der Ressourcen, zuverlaessige Bewertung der Aufwendungen).",
     "Aktivierte Entwicklungskosten werden linear ueber die erwartete Nutzungsdauer (in der Regel "
     "5-7 Jahre) abgeschrieben; Beginn mit Start der Produktion / Marktfreigabe.",
     "Patente werden zu Anschaffungskosten aktiviert; Abschreibung linear ueber die Schutzfrist "
     "(20 Jahre Patent; 10 Jahre Gebrauchsmuster) oder die wirtschaftliche Nutzungsdauer.",
     "Software wird aktiviert; Lizenzkosten und Implementierungsaufwand bis zur Inbetriebnahme; "
     "Abschreibungsdauer 3-7 Jahre."],
    "Aktivierte Entwicklungskosten zum 31.12.2023: 28,4 Mio. EUR (Vorjahr 22,1 Mio. EUR), "
    "im Wesentlichen fuer Projekte ICP-3 (Infotainment 6,2 Mio.), BMS-12 (Battery Mgmt 12,4 Mio.), "
    "ADAS-V4D (Radar Fusion 8,4 Mio.), ECU-900 Gen3 (1,4 Mio.). Goodwill aus Acquisitionen: 38,2 Mio. "
    "EUR (insbesondere aus Erwerb 2018 von SensoElectro GmbH, Wiesbaden, 28,4 Mio. EUR). "
    "Patente und Schutzrechte: 4,8 Mio. EUR (rund 120 aktive Patente).",
    "Werthaltigkeitspruefung (Impairment) jaehrlich gemaess IAS 36 fuer Goodwill und in Entwicklung "
    "befindliche immaterielle Vermoegenswerte. Wesentliche Annahmen: 5-Jahres-Geschaeftsplan, "
    "Diskontierungssatz WACC nach Marktinformation (Brennhagen WACC 2023: 8,4 %), erwartete "
    "Umsatzrenditen je CGU. Goodwill SensoElectro: keine Wertminderung notwendig (Headroom 22 %).")

ifrs_richtlinie("REA_IFRS_Bilanzierungsrichtlinie_IFRS_15_Umsatzerloese_2023.docx",
    "IFRS 15", "Umsatzerloese aus Vertraegen mit Kunden",
    "IFRS 15 etabliert ein 5-Schritte-Modell fuer die Umsatzrealisierung. Fuer Brennhagen als "
    "Automotive-Tier-1 mit langlaufenden Vertraegen ueber OEM-Programme (Volumen meist 3-7 Jahre) "
    "ist die korrekte Identifizierung von Leistungsverpflichtungen und Allokation der Transaktions"
    "preise zentral.",
    ["5-Schritte-Modell: (1) Identifizierung des Vertrags; (2) Identifizierung der Leistungsverpflichtungen; "
     "(3) Bestimmung des Transaktionspreises; (4) Allokation des Transaktionspreises auf die Leistungs"
     "verpflichtungen; (5) Erfassung des Umsatzes bei Erfuellung der Leistungsverpflichtung.",
     "Bei OEM-Auftraegen erfolgt Umsatzrealisierung bei Uebertragung der Verfuegungsmacht (in der Regel "
     "DAP-Lieferung an OEM-Werk; Eigentum geht ueber, Risiko und Nutzen liegen beim Kunden).",
     "Sonderzahlungen (Entwicklungs-/Anlauf-Tools) werden ueber die Laufzeit der Lieferungen verteilt "
     "(Abgrenzung als Vertragsverbindlichkeit, allokiert auf einzelne Einheiten).",
     "Variable Vergutung (Mengenrabatte, Volumen-Boni, Preisanpassungsklauseln) wird ueber die "
     "geschaetzte zu erwartende Hoehe in den Transaktionspreis einbezogen (Expected-Value-Methode).",
     "Garantien werden in Service- und Assurance-Garantien aufgeteilt; Service-Garantien werden als "
     "separate Leistungsverpflichtungen behandelt (Tool-/Wartungsumsatz)."],
    "Wesentliche Vertraege: BMW ICP-3 (Volumen 850 Mio. EUR / 5 Jahre), VW BMS-12 (280 Mio. EUR / 7 J.), "
    "Mercedes ADAS-V4D (380 Mio. EUR / 5 J.), Stellantis ECU-900 (210 Mio. EUR / 4 J.). "
    "Sonderzahlungen Entwicklungs-Tools 2023: 12,8 Mio. EUR (abgegrenzt). Variable Vergutung "
    "(Mengenboni VW, Stellantis) im Plan 2023: 4,2 Mio. EUR Rueckstellung.",
    "Schaetzungen betreffen insbesondere: (a) Erwartete Gesamtmengen ueber Vertragslaufzeit (Basis "
    "OEM-Programm-Forecast +/-15 %); (b) Anteil der Service-Garantien (basierend auf historischen "
    "Schadenquoten 0,6-1,2 %); (c) Variable Vergutung (Probability-Weighted Expected Value). "
    "Aenderungen werden prospektiv beruecksichtigt.")

ifrs_richtlinie("REA_IFRS_Bilanzierungsrichtlinie_IFRS_16_Leasing_2023.docx",
    "IFRS 16", "Leasingverhaeltnisse",
    "IFRS 16 verlangt fuer Leasingnehmer die On-Balance-Bilanzierung saemtlicher Leasingverhaeltnisse "
    "(Right-of-Use-Asset + Lease-Liability). Bei der Brennhagen-Gruppe von wesentlicher Bedeutung wegen "
    "umfangreicher Liegenschafts-Leasings (Werke + Bueros) sowie Fuhrpark-Leasings.",
    ["Recognition Exception fuer kurzfristige Leases (<= 12 Monate) und Geringwertige Vermoegens"
     "werte (<= 5 TEUR Anschaffungswert) – wird Konzernweit angewandt.",
     "Right-of-Use-Asset (RoU) wird zu Anschaffungskosten ergebniswirksam abgeschrieben (linear ueber "
     "Leasingdauer); Lease-Liability wird mittels Effektivzinsmethode getilgt (Zinsaufwand + "
     "Tilgungsanteil).",
     "Diskontierungszinssatz: Incremental Borrowing Rate (IBR) je Konzerngesellschaft und Land "
     "ermittelt; Stand 31.12.2023: REA/REG/RSG 3,8 %, RPL 5,2 %, RCZ 5,4 %, RHU 7,8 %, RCN 4,2 %.",
     "Verlaengerungsoptionen werden in die Leasingdauer einbezogen, soweit Ausuebung wahrscheinlich ist.",
     "Modifikationen (Anpassung Mietzins, Flaechenanpassung, Restrukturierung) loesen Re-Measurement "
     "des Lease-Liability aus; ggfs. Erfassung im Profit/Loss."],
    "Wesentliche Leasings zum 31.12.2023: (a) Hauptsitz REA Stuttgart (Vaihinger Strasse 120) "
    "RoU 22,4 Mio. EUR, Restlaufzeit 12 Jahre; (b) Werk Katowice RPL (RoU 14,8 Mio., 18 J.); "
    "(c) Werk Brno RCZ (RoU 12,1 Mio., 16 J.); (d) Werk Gyoer RHU (RoU 9,6 Mio., 14 J.); "
    "(e) Werk Shanghai RCN (RoU 4,8 Mio., 8 J.); (f) Fuhrpark Konzern (RoU 8,2 Mio., Ø 3 J.). "
    "Gesamt RoU 71,9 Mio. EUR; Lease Liability 68,4 Mio. EUR.",
    "Schaetzungen betreffen: Ausuebung von Verlaengerungsoptionen (z. B. RPL Werk Katowice mit "
    "2 x 5 Jahre Option – Wahrscheinlichkeit 90 % bewertet), IBR-Bestimmung (Bench gegen lokale "
    "Anleihezinsen), Restwert-Garantien (bei Fuhrpark unueblich). Verlaengerungsoptionen werden im "
    "Anhang ausgewiesen.")

ifrs_richtlinie("REA_IFRS_Bilanzierungsrichtlinie_IFRS_3_Unternehmenszusammenschluesse_2023.docx",
    "IFRS 3", "Unternehmenszusammenschluesse",
    "IFRS 3 regelt die bilanzielle Behandlung von Unternehmenszusammenschluessen. Anwendung der "
    "Acquisition-Methode (Erwerbsmethode): Identifizierung des Erwerbers, Bestimmung des Erwerbs"
    "stichtages, Bilanzierung der erworbenen Vermoegenswerte / uebernommenen Schulden zum beizu"
    "legenden Zeitwert und Erfassung des Goodwill als Residualgroesse.",
    ["Acquisition-Methode obligatorisch fuer alle Business-Combinations; Asset-Deals werden separat "
     "behandelt (Asset Purchase Allocation).",
     "Identifizierte Vermoegenswerte (insb. immaterielle: Kundenbeziehungen, Marken, Technologie, "
     "Auftragsbestand) werden zum Fair Value angesetzt; Bewertung durch externe Gutachter "
     "(KPMG Valuation Services oder PwC Deals).",
     "Goodwill = Kaufpreis (inkl. Earn-Outs zum Fair Value) - Fair Value Net Identifiable Assets. "
     "Goodwill wird nicht planmaessig abgeschrieben, sondern jaehrlich impairment-getestet (IAS 36).",
     "Transaktionskosten (Beratung, Legal, M&A) werden im Profit/Loss als Aufwand erfasst (nicht "
     "im Goodwill kapitalisiert).",
     "Earn-Outs werden zum Fair Value erfasst; nachtraegliche Anpassungen ueber Profit/Loss "
     "(Liability Classification) oder im Eigenkapital (Equity Classification)."],
    "Wesentliche Acquisitions der Vergangenheit: (a) 2018 SensoElectro GmbH, Wiesbaden (Sensorik fuer "
    "ADAS); Kaufpreis 52,4 Mio. EUR; Goodwill 28,4 Mio. EUR; (b) 2021 SilicaTech Sp. z o.o., Krakau "
    "(SiC-Halbleiter-Engineering); Asset-Deal Kaufpreis 12,8 Mio. EUR, keine Goodwill-Entstehung; "
    "(c) 2022 EmbedSoft AG, Aachen (Software-Entwicklung Embedded Linux); Kaufpreis 18,4 Mio. EUR "
    "inkl. Earn-Out 3,6 Mio. EUR; Goodwill 8,2 Mio. EUR. Gesamter konsolidierter Goodwill 31.12.2023: "
    "38,2 Mio. EUR.",
    "Werthaltigkeitspruefung (Impairment Test) jaehrlich gemaess IAS 36; Allokation des Goodwills "
    "auf Cash-Generating-Units (CGU): SensoElectro -> CGU ADAS; EmbedSoft -> CGU Software/RSG. "
    "Bewertung mittels Discounted Cash Flow (5-Jahres-Plan + Terminal Value), WACC 8,4 %, "
    "Wachstumsrate Terminal Value 1,5 %. Headroom (Recoverable Amount - Buchwert): ADAS 22 %, "
    "Software 28 %. Keine Wertminderung 2023 noetig.")

ifrs_richtlinie("REA_IFRS_Bilanzierungsrichtlinie_IFRS_9_Finanzinstrumente_2023.docx",
    "IFRS 9", "Finanzinstrumente",
    "IFRS 9 regelt die Klassifizierung und Bewertung von Finanzinstrumenten sowie das Hedge "
    "Accounting (loese IAS 39 ab). Drei Klassifizierungskategorien fuer finanzielle Vermoegens"
    "werte: At Amortised Cost, FVOCI (Fair Value through OCI), FVPL (Fair Value through P/L). "
    "Expected-Credit-Loss-Modell (ECL) fuer Wertberichtigungen (anstelle Incurred-Loss-Model).",
    ["Klassifizierung erfolgt anhand des Geschaeftsmodells und der Cashflow-Eigenschaften (SPPI-Test "
     "= Solely Payments of Principal and Interest).",
     "Operative Forderungen aus L+L sowie Bankguthaben werden i. d. R. zu Amortised Cost bewertet "
     "(Halten zur Vereinnahmung der Cashflows; SPPI erfuellt).",
     "ECL-Bewertung: 3-stufiges Modell (Stage 1: 12-Monats-ECL; Stage 2: Lifetime-ECL ab signifikanter "
     "Verschlechterung der Bonitaet; Stage 3: tatsaechliche Wertminderung).",
     "Vereinfachte Methode (Lifetime-ECL) wird fuer Trade Receivables ohne signifikante "
     "Finanzierungskomponente angewandt.",
     "Hedge Accounting: Cashflow-Hedge fuer FX-Forwards (siehe FX-Hedge-Berichte); Net-Investment "
     "Hedge fuer Tochter-Investments; Fair-Value-Hedge fuer Zinsswaps auf Konsortialkredit-Anteile."],
    "Trade Receivables zum 31.12.2023: 142,5 Mio. EUR; ECL-Wertberichtigung 1,8 Mio. EUR (1,3 %); "
    "in der Sektor-Concentration vergleichsweise niedrig wegen Premium-OEM-Kundenstamm (BMW, "
    "Mercedes, VW, Stellantis – alle Investment-Grade-Rating). Finanzielle Vermoegenswerte FVOCI: "
    "8,4 Mio. EUR (Eigenkapital-Beteiligungen Joint Ventures); FVPL: 4,2 Mio. EUR (Derivate aus "
    "FX-Hedging-Aktivitaeten). Cash and Cash Equivalents 184 Mio. EUR (At Amortised Cost).",
    "ECL-Modell verwendet eine Mischung aus historischen Ausfallquoten und Forward-Looking Macro-"
    "Faktoren (BIP-Wachstum DACH/EU, Automotive-Produktionsindex, Insolvenzquoten Sektor). "
    "Sensitivitaet: Erhoehung der erwarteten Ausfallquote um 50 bp wuerde ECL um 0,7 Mio. EUR erhoehen. "
    "Hedge-Effectiveness wird quartalsweise getestet; keine ineffektiven Hedges 2023 dokumentiert.")


# ── 6 Transfer Pricing Local Files ─────────────────────────────────────────
def tp_local_file(fname, sub_short, sub_full, city, country, jahr, umsatz_mio, ic_volumen,
                  hauptproduktbezug, lokale_funktion):
    write_doc(f"{BASE}/{fname}", H,
        f"Transfer Pricing Local File {sub_short} – {jahr}",
        subtitle=f"Verrechnungspreisdokumentation gemaess OECD VPL / lokales Steuerrecht",
        sections=[
            ("Berichtsgegenstand",
             f"Local File fuer die {sub_full} (Sitz: {city}, {country}) fuer das Geschaeftsjahr {jahr}. "
             f"Dokumentationspflicht gemaess OECD Verrechnungspreisleitlinien 2022 (VPL) und lokalem "
             f"Steuerrecht. Master File auf Konzernebene wird separat durch die Konzern-Steuerabteilung "
             f"(Group Tax Director Frau Dr. Heike Berger) erstellt und ueber das KPMG-Mandant-Portal "
             f"abgelegt."),
            ("Gesellschaftsprofil",
             f"Funktion und Risikoprofil: {lokale_funktion}\n\n"
             f"Hauptprodukte / Wertschoepfung: {hauptproduktbezug}\n\n"
             f"Umsatz {jahr}: {umsatz_mio} Mio. EUR (davon Intercompany {ic_volumen} Mio. EUR). "
             f"Mitarbeitende: {S[sub_short]['employees']}. Eigentumsverhaeltnis: 100 % Tochter "
             f"der Brennhagen Holding GmbH (RHO Stuttgart)."),
            ("Wesentliche Intercompany-Transaktionen",
             [["Transaktion", "Vertragspartner", "Volumen Mio. EUR", "Verrechnungspreis-Methode"],
              ["Lieferung Halbfertigerzeugnisse / Komponenten", "REG Heilbronn", f"{ic_volumen*0.42:.1f}", "Cost+ (5-7 %)"],
              ["Engineering-/Service-Leistungen", "REA Stuttgart (Holding)", f"{ic_volumen*0.18:.1f}", "Cost+ (8-10 %)"],
              ["Lizenzgebuehren Patente / Software", "REA Stuttgart", f"{ic_volumen*0.12:.1f}", "CUP (3,5-4,2 %)"],
              ["Konzernumlagen (Shared Services)", "RHO Stuttgart", f"{ic_volumen*0.08:.1f}", "Kostenumlage"],
              ["Cash-Pool / Intercompany-Darlehen", "REA Treasury", f"{ic_volumen*0.20:.1f}", "Marktueblicher Zins"]]),
            ("Funktions- und Risikoanalyse",
             "Die Gesellschaft erfuellt die Funktion eines Routine-Producer mit begrenztem Routine-Risiko: "
             "Produktion, Qualitaetspruefung, Logistik. Strategische Funktionen (F&E, Produktentwicklung, "
             "Markt-Strategie) sind bei der Konzernmutter REA Stuttgart angesiedelt. Risiken: Auslastungs"
             "risiko (Produktion), Vorratsrisiko (Material), Wechselkursrisiko (durch Konzern-Treasury "
             "abgesichert). Marketing- und FX-Risiken sind beim Konzernsitz konzentriert."),
            ("Verrechnungspreis-Methodik",
             "Cost+ Methode mit Routine-Margen von 5-7 % auf Vollkosten (Benchmark: TP-Analyse durch "
             "PwC AG WPG 2022, Quartil 25-75 %); CUP fuer Lizenzgebuehren (Marktpreis aus vergleichbaren "
             "Lizenztransaktionen); Konzernumlagen nach BO-Schluessel (Headcount + Umsatz); marktueblicher "
             "Zins fuer Intercompany-Darlehen (EURIBOR + 150-250 bp je nach Bonitaet)."),
            ("Compliance-Status / Pruefungen",
             f"Local File wurde durch lokale Steuerberater geprueft (KPMG {country}) und der lokalen "
             f"Steuerbehoerde auf Anforderung verfuegbar. Letzte Betriebspruefung der lokalen Behoerde: "
             f"{('2022' if country in ['CZ','HU','PL'] else '2021')}. Keine wesentlichen Beanstandungen. "
             f"Country-by-Country-Reporting (CbCR) erfolgt jaehrlich durch Konzernsteuerabteilung "
             f"(Master File-Verantwortlich)."),
            ("Unterschriften",
             signatures("Florian Maier", "Group Controller", R["name"],
                        "Dr. Heike Berger", "Group Tax Director", R["name"],
                        place="Stuttgart", date_str_=f"30. November {jahr}")),
        ])


tp_local_file("TP_LocalFile_REG_2023.docx", "REG", S["REG"]["name"], "Heilbronn", "Deutschland", "2023",
    280, 184, "Hauptwerk Produktion ICP-3, BMS-12, ECU-900; vollintegrierte SMD/Montage/Endabnahme.",
    "Produktion und Endabnahme (volle Wertschoepfung Hardware), mittlerer Strategy-Anteil; "
    "Funktionsprofil: Limited-Risk-Producer mit Stratifizierung.")
tp_local_file("TP_LocalFile_RSG_2023.docx", "RSG", S["RSG"]["name"], "Muenchen", "Deutschland", "2023",
    62, 48, "Embedded Software-Entwicklung fuer ADAS, BMS, OTA-Updates; Lieferung Software-Module an "
    "REG / OEM-Kunden.",
    "Software-Entwicklung mit strategischem Charakter; hoehere Routine-Marge (8-10 %) als reine "
    "Produktion. Bewertung als Routine-Service-Provider mit Spezialisierungs-Komponente.")
tp_local_file("TP_LocalFile_RPL_2023.docx", "RPL", S["RPL"]["name"], "Katowice", "Polen", "2023",
    98, 78, "EMS / SMD-Bestueckung, automatisierte Loetlinien fuer Steuergeraete; Kapazitaet 8 SMT-Linien.",
    "Routine-Producer mit reiner Auftragsfertigung; Material-Stellung durch REG. "
    "Routine-Marge gemaess Benchmark-Studie: 4-6 % auf Conversion Cost.")
tp_local_file("TP_LocalFile_RCZ_2023.docx", "RCZ", S["RCZ"]["name"], "Brno", "Tschechien", "2023",
    72, 58, "Produktion Steckverbinder und Kabelbaeume (Tier-2 Komponenten); Spezialisierung "
    "Automotive-Stecker.",
    "Routine-Producer (Steckverbinder-Produktion); Material in CZK eingekauft, Verkauf via REG "
    "an OEM-Kunden. Routine-Marge 5-7 % auf Vollkosten.")
tp_local_file("TP_LocalFile_RHU_2023.docx", "RHU", S["RHU"]["name"], "Gyoer", "Ungarn", "2023",
    54, 42, "Produktion Sensorik-Komponenten (Drehzahl-, Beschleunigungs-, Drucksensoren) fuer "
    "Powertrain und ADAS; Spezialfertigung Kleinserien.",
    "Routine-Producer mit Spezialisierungs-Komponente (Sensorik); Material teilweise lokal beschafft "
    "(HUF-Exposure), Verkauf via REG. Routine-Marge 5-7 %.")
tp_local_file("TP_LocalFile_RCN_2023.docx", "RCN", S["RCN"]["name"], "Shanghai", "China", "2023",
    42, 32, "Asien-Vertriebsgesellschaft mit Aftermarket-Geschaeft und Service-Support fuer "
    "OEM-Werke China (Mercedes Beijing, Stellantis Wuhan, BMW Brilliance Shenyang).",
    "Limited-Risk-Distributor / Service-Gesellschaft; keine eigene Produktion; Marge 3-4 % auf "
    "Aftermarket-Verkaufspreis (Berlin Method: Resale-minus). Lokale Steuerverguenstigungen "
    "(Foreign-Invested Enterprise FIE) bis 2025.")


# ── Sonstige Docs ──────────────────────────────────────────────────────────
write_doc(f"{BASE}/MA_First_Approach_2023_018.docx", H,
    "M&A First Approach #018 – Pruefung Erwerb spezialisierte BMS-Software-Firma",
    subtitle="Vorlage Strategie- und Vorstandsbericht, Stand 14. November 2023",
    sections=[
        ("Hintergrund / Zielsetzung",
         "Im Rahmen der Strategie 2026 'NEXT' (Saeule Battery Management) wird ein gezielter Aufbau "
         "der Software-Kompetenz angestrebt. Die in Aachen ansaessige BMS-Soft GmbH (Umsatz 12,4 Mio. "
         "EUR / 84 Mitarbeiter / spezialisiert auf BMS-Software fuer Lithium-Ionen / Sodium-Ion-Akkus) "
         "wurde als strategisches Target identifiziert."),
        ("Target-Profil",
         "Firma: BMS-Soft GmbH, Aachen.\nGruendung: 2017 aus RWTH Aachen Spin-off.\n"
         "Umsatz 2022: 11,2 Mio. EUR (+38 % YoY); 2023e: 14,8 Mio.\n"
         "EBITDA-Marge: 22 % (2022) / 26 % (2023e).\n"
         "Mitarbeiter: 84 (davon 62 Engineers, 12 Sales, 10 Admin).\n"
         "Eigentum: 3 Gruender (60 %), VC Earlybird (25 %), Mitarbeiter ESOP (15 %).\n"
         "Top-Kunden: Volkswagen (35 %), Stellantis (22 %), Daimler (18 %), CATL (12 %).\n"
         "Technologie: KI-basierte Cell-State-of-Health-Prediction; SiC-spezifische Charging-Algorithmen."),
        ("Strategischer Fit",
         "Hohe Komplementaritaet zu Brennhagen-Portfolio: BMS-12 Hardware-Modul (REG/RSG) ergaenzt um "
         "spezialisierte BMS-Software (BMS-Soft). Cross-Selling-Potenzial zu BMW + Mercedes (Schluesselkunden "
         "Brennhagen, aktuell nicht abgedeckt von BMS-Soft). Schneller Markteintritt in Sodium-Ion-Segment "
         "(Wachstum erwartet 2025+)."),
        ("Indikative Bewertung",
         "Bewertungsbandbreite (Pre-Money): 80-110 Mio. EUR (entspricht 5,4-7,4x EV/Revenue 2023e). "
         "Strukturierung: 70 % Cash + 30 % Brennhagen-Aktien (Tausch); Earn-Out 25 % nach 24 Monaten "
         "(EBITDA-basiert). Erwarteter Goodwill: 55-65 Mio. EUR."),
        ("Naechste Schritte / Vorschlag",
         "(1) Vertieftes Sondierungsgespraech CEO Anna Mueller mit BMS-Soft-CEO Dr. Florian Lehmann "
         "(geplant 22. November 2023);\n"
         "(2) Genehmigung Beirat ueber Aufnahme formaler Due Diligence (geplant 14. Dezember 2023);\n"
         "(3) NDA + Letter of Intent (LOI) Q1/2024;\n"
         "(4) Closing-Ziel Q3/2024 (vorbehaltlich Kartellfreigabe BKartA / EU-Kommission).\n\n"
         "Externe Berater: Roland Berger (Strategie-DD), KPMG (Financial DD), Hengeler Mueller (Legal)."),
        ("Risikobewertung",
         "Hoehepriorisiertes Risiko: Mitarbeiter-Retention (Software-Spezialisten). Mitigation: "
         "Earn-Out + ESOP Retention-Pool. Mittleres Risiko: Kunden-Concentration (Top-3 Kunden 75 %). "
         "Niedrigeres Risiko: Technologie-Reife (bereits 4 Serienproduktionen)."),
        ("Unterschriften",
         signatures("Stefan Richter", "Vorstand M&A / BD", R["name"],
                    "Laura Bauer", "CFO", R["name"],
                    place="Stuttgart", date_str_="14. November 2023")),
    ])


write_doc(f"{BASE}/REA_Konsortialkredit_Rahmenvertrag_2022.docx", H,
    "Konsortialkredit-Rahmenvertrag 2022 – Senior Facility 250 Mio. EUR",
    subtitle="Vertrag vom 14. Maerz 2022; Laufzeit bis 14. Maerz 2027",
    sections=[
        ("Vertragsparteien",
         "Kreditnehmerin: Brennhagen Elektronik AG (auch fuer Tochtergesellschaften REG, RSG, RPL, RCZ, "
         "RHU, RCN als Garantiegeber).\n\n"
         "Konsortium (5 Banken):\n"
         "- Deutsche Bank AG (Konsortialfuehrerin, Agent, 80 Mio. EUR / 32 %)\n"
         "- Commerzbank AG (40 Mio. EUR / 16 %)\n"
         "- UniCredit Bank AG (HypoVereinsbank) (50 Mio. EUR / 20 %)\n"
         "- BNP Paribas S.A. (40 Mio. EUR / 16 %)\n"
         "- HSBC Continental Europe S.A. (40 Mio. EUR / 16 %)"),
        ("Vertragsstruktur",
         "Tranche A (Termloan): 150 Mio. EUR, Laufzeit 5 Jahre, Tilgung am Ende (Bullet); "
         "Margin EURIBOR 6M + 110 bp.\n\n"
         "Tranche B (Revolving Credit Facility / RCF): 100 Mio. EUR, revolvierende Linie fuer "
         "Working-Capital, Laufzeit 5 Jahre; Commitment Fee 35 % der Margin auf nicht in Anspruch "
         "genommenen Betrag; Margin EURIBOR 6M + 95 bp."),
        ("Wesentliche Klauseln",
         ("clauses", [
             ("§ 11 Financial Covenants", [
                 "Net Debt / EBITDA (LTM) <= 3,0x",
                 "Interest Coverage Ratio (EBITDA / Interest Expense) >= 4,0x",
                 "Eigenkapitalquote (Konzern) >= 30 %",
                 "Quartalsmaessiges Reporting (binnen 60 Tagen nach Quartalsende) und Jahres-Compliance "
                 "Certificate (binnen 120 Tagen)",
             ]),
             ("§ 13 Sicherheiten / Garantien", [
                 "Patronatserklaerung fuer wesentliche Tochtergesellschaften (REG, RSG, RPL, RCZ).",
                 "Negativerklaerung (kein Lasten-Recht auf Konzern-Assets > 5 Mio. EUR ohne Konsens).",
                 "Cross-Default-Klausel fuer Verschuldung > 10 Mio. EUR.",
             ]),
             ("§ 15 ESG / Sustainability", [
                 "Sustainability-linked Margin Adjustment: +/- 5 bp je nach Erreichung der ESG-KPIs "
                 "(Scope 1+2 Reduktion, Anteil erneuerbare Energie, Frauenanteil Fuehrungspositionen).",
                 "Jaehrliche Berichterstattung gegen ESG-KPIs durch Sustainability Officer.",
             ]),
             ("§ 17 Vorzeitige Tilgung", [
                 "Vorzeitige Tilgung Tranche A jederzeit zulaessig (Make-Whole nicht erforderlich).",
                 "Mandatorische Vorabtilgung bei Change-of-Control (>= 30 % Anteilsuebergang).",
             ]),
         ])),
        ("Anwendbares Recht / Streitbeilegung",
         "Deutsches Recht. LMA Standard-Form (German Law-Variante). Streitigkeiten: Schiedsgericht "
         "DIS (Deutsche Institution fuer Schiedsgerichtsbarkeit) mit Sitz Frankfurt am Main. "
         "Anwaltliche Begleitung: Hengeler Mueller (Brennhagen); Linklaters (Konsortium)."),
        ("Unterschriften",
         signatures("Anna Mueller / Laura Bauer", "Vorstand", R["name"],
                    "Dr. Friedrich Stuetzel", "Senior MD, Konsortialfuehrer", "Deutsche Bank AG",
                    place="Stuttgart / Frankfurt", date_str_="14. Maerz 2022")),
    ])


write_doc(f"{BASE}/REA_Geschaeftsordnung_Aufsichtsrat_2022.docx", H,
    "Geschaeftsordnung des Aufsichtsrats 2022",
    subtitle="Beschlossen durch den Aufsichtsrat am 18. Februar 2022",
    sections=[
        ("Praeambel",
         "Diese Geschaeftsordnung regelt die innere Ordnung des Aufsichtsrats der Brennhagen Elektronik AG "
         "auf Basis der Satzung der Gesellschaft, des Aktiengesetzes (AktG) sowie des Deutschen "
         "Corporate Governance Kodex (DCGK)."),
        ("Konstituierung und Mitgliedschaft",
         ("clauses", [
             ("§ 1 Mitgliederzahl", [
                 "Der Aufsichtsrat besteht aus fuenf Mitgliedern, davon eine Arbeitnehmervertreterin "
                 "gemaess Drittelbeteiligungsgesetz (DrittelbG).",
                 "Die Amtsperiode betraegt 4 Jahre (gestaffelte Wiederwahl moeglich).",
             ]),
             ("§ 2 Vorsitz", [
                 "Der Aufsichtsrat waehlt aus seiner Mitte den/die Vorsitzende/n und den/die stellv. "
                 "Vorsitzende/n. Wahl mit einfacher Mehrheit der abgegebenen Stimmen.",
             ]),
             ("§ 3 Ausschuesse", [
                 "Der Aufsichtsrat bildet folgende Ausschuesse: Pruefungsausschuss (mind. 3 Mitglieder, "
                 "Vorsitz Finanz-/Pruefungsexperte gemaess § 100 Abs. 5 AktG); Praesidialausschuss "
                 "(3 Mitglieder); Personalausschuss (3 Mitglieder); Compliance- und Risikoausschuss "
                 "(3 Mitglieder); Innovations- und Technologieausschuss (3 Mitglieder).",
                 "Ausschuesse berichten dem Plenum mind. einmal pro Sitzungsperiode.",
             ]),
         ])),
        ("Sitzungen",
         ("clauses", [
             ("§ 4 Frequenz", [
                 "Es finden mind. 4 ordentliche Sitzungen pro Geschaeftsjahr statt (jeweils Q1-Q4). "
                 "Zusaetzliche ausserordentliche Sitzungen koennen auf Antrag eines Mitglieds oder des "
                 "Vorstandes einberufen werden.",
             ]),
             ("§ 5 Einberufung", [
                 "Einberufung durch den/die Vorsitzende/n schriftlich oder elektronisch unter Wahrung "
                 "einer Frist von 14 Tagen mit Tagesordnung. Bei besonderer Eilbeduerftigkeit Verkuerzung "
                 "auf 3 Tage zulaessig.",
             ]),
             ("§ 6 Beschlussfaehigkeit", [
                 "Beschlussfaehigkeit bei mind. 3 anwesenden Mitgliedern. Beschluesse werden mit der "
                 "Mehrheit der abgegebenen Stimmen gefasst (bei Stimmengleichheit entscheidet "
                 "Stimmrecht des/der Vorsitzenden).",
             ]),
             ("§ 7 Niederschrift", [
                 "Sitzungen werden protokolliert; Protokolle sind nach Genehmigung durch den/die "
                 "Vorsitzende/n bindend.",
             ]),
         ])),
        ("Vergutung und D&O",
         "Die Vergutung der Aufsichtsratsmitglieder ergibt sich aus den individuellen Dienstvertraegen "
         "(siehe 01_AG_Gesellschaftsrecht) sowie aus § 11 der Satzung. D&O-Versicherungssumme 50 Mio. "
         "EUR (Allianz Global Corporate & Specialty SE)."),
        ("Letzte Aktualisierung", "Beschlussfassung des Aufsichtsrats am 18. Februar 2022."),
    ])


write_doc(f"{BASE}/REA_Konzern_Governance_Report_2021_Q1.docx", H,
    "Konzern-Governance-Report Q1/2021",
    subtitle="Vorlage Aufsichtsrat – Berichtsperiode 1. Januar bis 31. Maerz 2021",
    sections=[
        ("Berichtsgegenstand",
         "Quartalsbericht der Konzern-Governance- und Compliance-Funktion fuer das Q1/2021. Berichts"
         "empfaenger: Aufsichtsrat (Pruefungsausschuss / Compliance- und Risikoausschuss), Vorstand, "
         "Geschaeftsfuehrungen der Tochterwerke."),
        ("Konzernstruktur",
         "Konsolidierte Gesellschaften zum 31.3.2021 (alle 100 % Tochter): "
         "REG Heilbronn (820 MA), RSG Muenchen (340 MA), RPL Katowice (960 MA), RCZ Brno (680 MA), "
         "RHU Gyoer (540 MA), RCN Shanghai (320 MA), RHO Stuttgart (45 MA). "
         "Konzernspitze: Brennhagen Elektronik AG (im Formwechsel seit 10.2.2021, vorher GmbH)."),
        ("Compliance-Status",
         "Wesentliche Compliance-Themen Q1: (a) keine SAR-relevanten Vorfaelle (Suspicious Activity "
         "Reports); (b) 2 Hinweise via SPEAK-UP@Brennhagen (beide unbegruendet); (c) Antikorruptions"
         "schulung Q1 abgeschlossen (96 % der Belegschaft); (d) Sanktionspruefung erweitert um "
         "Ukraine/Russland (in Vorbereitung)."),
        ("Wesentliche Risiken",
         ("list", [
             "Halbleiter-Lieferengpaesse (TSMC/NXP): Risikobewertung HOCH; Mitigation in Aufbau "
             "(Zweitquellen-Strategie).",
             "OEM-Programmrisiken: Risiko mittel; Diversifikation 8 OEM-Kunden gut.",
             "Cybersecurity: Risiko erhoeht (laut BSI-Lagebericht); ISMS-Programm in Umsetzung.",
             "FX-Volatilitaet: Risiko mittel; Hedging-Programm aktiv (siehe FX-Hedge-Berichte).",
         ])),
        ("Personalentwicklung Vorstand",
         "Vorstand komplett besetzt (4 Mitglieder: Mueller, Bauer, Weber, Hoffmann). Erster Aufsichtsrat "
         "im Anschluss an Formwechsel im Februar 2021 bestellt (5 Mitglieder)."),
        ("Anstehend Q2/2021",
         "BMW ICP-3 Vertragsverhandlungen (Volumen 850 Mio. EUR; Abschluss erwartet Mai 2021); Werks"
         "erweiterung Katowice (Beschlussfassung Aufsichtsrat geplant); Aufbau Compliance- und Risiko"
         "ausschuss in der konstituierenden Sitzung."),
    ])


write_doc(f"{BASE}/REA_MBZ_Audit_Einladung_2021.docx", H,
    "Audit-Einladung Mercedes-Benz AG (MBZ) – VDA 6.3 Lieferantenaudit 2021",
    subtitle="Audit Geplant 14.-16. September 2021 in Heilbronn",
    sections=[
        ("Auditeinladende",
         "Mercedes-Benz AG, Procurement / Supplier Quality Management, Mercedesstrasse 120, "
         "70372 Stuttgart. Audit-Leiter: Herr Dipl.-Ing. Klaus-Peter Behrens (Senior Supplier Quality "
         "Manager); begleitet von Frau Anette Weidner (TPQA Trim & Powertrain Quality)."),
        ("Auditierte Standort",
         "Brennhagen Elektronik GmbH (REG), Werk Heilbronn. Audit-Umfang: Prozesse fuer die ECU-900 "
         "Lieferung an Mercedes-Benz Werk Untertuerkheim (Powertrain); Volumen 2021 ca. 1,2 Mio. "
         "ECU-Einheiten p. a."),
        ("Audit-Plan / Inhalte",
         ("list", [
             "Tag 1 (14.9.): Eroeffnungsgespraech, Walk-through Produktion, Q-Prozesse Eingangsk.",
             "Tag 2 (15.9.): Prozessaudit Bestueckung SMT, Loetprozesse, Endpruefung; Pruefung "
             "Reklamationsmanagement (8D-Prozess); IATF 16949 / VDA 6.3-Konformitaet.",
             "Tag 3 (16.9.): Pruefung Lieferanten-Audit-Programm (Tier-2-Lieferanten); Krisen-Management "
             "und Liefersicherheit; Abschlussbesprechung mit Maßnahmenplan.",
         ])),
        ("Vorbereitung Brennhagen (REG Heilbronn)",
         "Audit-Vorbereitungsteam: Dr. Thomas Weber (COO; Schirmherr), Andreas Maier (Werksleiter "
         "REG), Sabine Brand (Qualitaetsleiterin REG), Christian Probst (SQM-Manager). Vorlauf-"
         "Pakete an MBZ uebermittelt 14 Tage vorher (FMEA-Updates, 8D-Berichte letzte 12 Monate, "
         "Tier-2-Lieferantenliste mit Q-Bewertung)."),
        ("Erwartetes Ergebnis",
         "Anvisierte Bewertung: A (90+ Punkte); Konkretisierung Top-Verbesserungspotenziale "
         "(Maßnahmenplan binnen 30 Tagen nach Audit). Rezertifizierungstermin VDA 6.3: 24 Monate."),
        ("Naechste Schritte",
         "Final-Confirmation gegenueber MBZ bis 6.9.2021; Tagungsraum REG fuer 3 Tage reserviert. "
         "Hotel-Buchung MBZ-Team: Park Inn Heilbronn (3 Naechte; bestaetigt)."),
    ])


write_doc(f"{BASE}/REA_VW_Liefervertrag_ECU-900_2023.docx", H,
    "Volkswagen AG – Liefervertrag ECU-900 Gen3 (2023)",
    subtitle="Rahmen-Liefervertrag fuer Powertrain-Steuergeraete (ECU)",
    sections=[
        ("Vertragsparteien",
         "Auftraggeber: Volkswagen AG, Berliner Ring 2, 38440 Wolfsburg, vertreten durch das Einkaufs"
         "ressort Elektronik (Bevollmaechtigte: Frau Stefanie Krug, Senior Buyer Electronics).\n\n"
         "Auftragnehmerin: Brennhagen Elektronik AG (mit Lieferungen durch REG Heilbronn)."),
        ("Vertragsgegenstand",
         "Lieferung von Powertrain-Steuergeraeten (ECU-900 Gen3) fuer die VW-Plattformen MEB+ "
         "(Modular Electric Toolkit Erweitert) und MQB-Evo (Modular Quer Baukasten Evolution). "
         "Volumen-Forecast: 1,8 Mio. ECU-Einheiten p. a. ueber 5 Jahre."),
        ("Konditionen",
         ("clauses", [
             ("§ 1 Volumen / Forecast", [
                 "Volumen-Forecast: 1,4 Mio. (2024); 1,6 Mio. (2025); 1,8 Mio. (2026-2028).",
                 "Vorlaufzeit 16 Wochen; rollierender 12-Monats-Forecast (Fix-Zone 8 Wochen; "
                 "Tradezone 9-24 Wochen).",
             ]),
             ("§ 2 Preise", [
                 "Stueckpreis 84,50 EUR (Standardausfuehrung); Volumenrabatte ueber 1,5 Mio. -2 %, "
                 "ueber 1,8 Mio. -3,5 %.",
                 "Preisindex-Klausel: Halbleiter-Komponenten (NXP/STM/Infineon) >+10 % Preisanstieg "
                 "loest Preisanpassung aus (max. 4 % p. a.).",
             ]),
             ("§ 3 Lieferbedingungen", [
                 "Incoterm 2020: DAP-Wolfsburg (frei verbaut Werk Wolfsburg);",
                 "Zahlungsbedingung: 60 Tage netto;",
                 "Liefergrad-KPI: >= 99,5 % On-Time-Delivery (Vertragsstrafe 5 EUR/Std. Verspaetung "
                 "ab P1-Linienstillstand).",
             ]),
             ("§ 4 Qualitaet", [
                 "Reklamationsquote (ppm) <= 25 ppm; bei Ueberschreitung Eskalationsstufen-Prozess.",
                 "8D-Bericht binnen 7 Werktagen bei P1-Faellen.",
                 "Re-Audit bei systematischen Q-Maengeln binnen 14 Tagen.",
             ]),
             ("§ 5 Gewaehrleistung / Haftung", [
                 "Gewaehrleistungszeit 24 Monate ab Verbau; max. 36 Monate ab Lieferung;",
                 "Haftungshoechstgrenze 100 % des Vertragsvolumens p. a. (ausgenommen Vorsatz / "
                 "Personenschaeden / Produkthaftung).",
             ]),
             ("§ 6 Vertraulichkeit / IP", [
                 "Strenge Geheimhaltung VW-spezifischer Konstruktions- und Software-Daten; "
                 "Schutz IP Brennhagen bleibt unberuehrt; Cross-Licensing nur fuer Reverse-Engineering "
                 "Erweiterungen.",
             ]),
             ("§ 7 Laufzeit / Kuendigung", [
                 "Laufzeit 5 Jahre ab 1. Januar 2024 (bis 31.12.2028); Verlaengerung um 2 Jahre auf Antrag.",
                 "Ordentliche Kuendigung mit 12 Monaten Vorlauf zum Ende des Geschaeftsjahres.",
             ]),
         ])),
        ("Anlagen",
         "Anlage 1: Technische Spezifikation ECU-900 Gen3.\nAnlage 2: Preisliste mit Volumenstaffel.\n"
         "Anlage 3: Forecast-Procedure und EDI-Schnittstelle.\nAnlage 4: VDA-6.3-Audit-Anforderungen."),
        ("Unterschriften",
         signatures("Stefan Richter", "Vorstand M&A/BD", R["name"],
                    "Stefanie Krug", "Senior Buyer Electronics", "Volkswagen AG",
                    place="Stuttgart / Wolfsburg", date_str_="22. November 2023")),
    ])


write_doc(f"{BASE}/RCN_Arbeitsvertrag_04_Finanzcontroller_Sha_2022_ENTWURF.docx", H,
    "Arbeitsvertrag (Entwurf) – Finanzcontroller RCN Shanghai 2022",
    subtitle="Lokaler Arbeitsvertrag fuer Brennhagen (Shanghai) Co., Ltd.",
    sections=[
        ("Vertragsparteien",
         "Arbeitgeberin: Brennhagen (Shanghai) Co., Ltd. (RCN), Unit 1208, China Insurance Building, "
         "166 East Lujiazui Road, Pudong New Area, Shanghai 200120, China.\n\n"
         "Arbeitnehmer: Herr Liang Wei, geboren 14.06.1985, wohnhaft Shanghai. (Hinweis: dies "
         "ist die deutsche Fassung; der bindende Vertragstext ist die chinesische Sprachfassung "
         "gemaess chinesischem Arbeitsrecht §10 Arbeitsvertragsgesetz).\n\nStatus: ENTWURF zur "
         "Genehmigung HR-Konzern / Group Tax."),
        ("Vertragsregelungen",
         ("clauses", [
             ("§ 1 Arbeitsverhaeltnis", [
                 "Beginn 1. April 2022; befristet 3 Jahre (Probezeit erste 6 Monate);",
                 "Bei erfolgreicher Probezeit Umwandlung in unbefristetes Verhaeltnis (gemaess "
                 "chinesischem Arbeitsrecht / Labor Contract Law of PRC, Art. 14).",
             ]),
             ("§ 2 Position und Aufgaben", [
                 "Position: Finance Controller (Senior); Berichtsweg an Country Manager Mr. Zhang Hao;",
                 "Aufgaben: Monatsabschluss IFRS-Reporting; Local Tax + VAT-Compliance; "
                 "Transfer-Pricing-Dokumentation (in Zusammenarbeit mit Group Tax Stuttgart); "
                 "FX-Hedging Vorbereitung (Schnittstelle Group Treasury).",
             ]),
             ("§ 3 Verguetung", [
                 "Grundgehalt RMB 480.000 p. a. (entspricht ca. 62.000 EUR; Stand Maerz 2022); "
                 "13. Monatsgehalt (Chinese New Year Bonus);",
                 "Variable Verguetung bis 25 % bei Zielerreichung (KPIs: termingerechte "
                 "Konsolidierung, TP-Compliance, lokale Pruefungsbestaetigung).",
                 "Pflichtbeitraege Sozialversicherung (Pension, Medical, Unemployment) gemaess "
                 "Shanghai-Tarif sowie Housing Fund (Wohnungsfonds 12 %).",
             ]),
             ("§ 4 Arbeitszeit / Urlaub", [
                 "Standard-Arbeitszeit Mo-Fr 9:00-18:00 Uhr; 40h/Woche (gemaess chinesischem Arbeitsrecht).",
                 "Urlaub: 15 Werktage p. a. (gemaess lokal); zusaetzliche 5 Tage 'Brennhagen-Urlaub'.",
             ]),
             ("§ 5 Verschwiegenheit / Wettbewerb", [
                 "Strikte Verschwiegenheit waehrend und 24 Monate nach Beendigung; nachvertragliches "
                 "Wettbewerbsverbot (Schutzfristen gemaess chinesischem Recht max. 2 Jahre, "
                 "Karenzentschaedigung 30 %).",
             ]),
             ("§ 6 Anwendbares Recht / Streitbeilegung", [
                 "Chinesisches Arbeitsrecht (Labor Contract Law of PRC); Streitbeilegung durch das "
                 "Shanghai Arbeitsschlichtungskomitee (Labor Arbitration Committee); bei Nichteinigung "
                 "Volksgericht Shanghai.",
             ]),
         ])),
        ("Anlagen / Hinweis",
         "Vertrag wird in chinesischer und englischer Sprachfassung erstellt; bindend ist die "
         "chinesische Fassung. Pflichtmeldung lokaler Sozialversicherung binnen 30 Tagen ab Vertrags"
         "beginn. Visum und Arbeitserlaubnis (sofern erforderlich) durch HR Shanghai zu organisieren."),
        ("Unterschriften",
         signatures("Mr. Zhang Hao", "Country Manager RCN", "Brennhagen (Shanghai) Co., Ltd.",
                    "Liang Wei", "Finance Controller", "i. e. S.",
                    place="Shanghai", date_str_="22. Maerz 2022")),
    ])


print("OK regen_roehrig_02_finanzen.py – ~68 docs written")
