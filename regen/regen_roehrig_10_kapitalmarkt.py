"""
regen_roehrig_10_kapitalmarkt.py
Enrich thin .docx files in roehrig_large/10_Kapitalmarkt_IR/.
Capital markets / Investor Relations docs for Brennhagen Elektronik AG.
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
from enhance_lib import ROEHRIG_AG as R, ROEHRIG_SUBS as S, write_doc, signatures

BASE = Path(f"{_ROOT}/roehrig_large/10_Kapitalmarkt_IR")

H = {"name": R["name"], "addr": R["addr"], "hrb": R["hrb"]}
H_REG = {"name": S["REG"]["name"], "addr": "Carl-Benz-Straße 14, 74076 Heilbronn", "hrb": S["REG"]["hrb"]}
H_RCZ = {"name": S["RCZ"]["name"], "addr": "Tovární 25, 61700 Brno", "hrb": S["RCZ"]["hrb"]}
H_RPL = {"name": S["RPL"]["name"], "addr": "ul. Roździeńskiego 188, 40-203 Katowice", "hrb": S["RPL"]["hrb"]}
H_KPMG = {"name": "KPMG AG Wirtschaftsprüfungsgesellschaft",
          "addr": "Theodor-Heuss-Straße 5, 70174 Stuttgart",
          "hrb": "HRB 14336, Amtsgericht Berlin"}

ISIN = "DE000RHGRP12"
WKN = "RHGRP1"

# ── Capital-markets common header (ISIN / WKN) ──
H_CM = {"name": R["name"],
        "addr": R["addr"] + "  |  ISIN " + ISIN + "  |  WKN " + WKN,
        "hrb": R["hrb"] + "  |  Prime Standard, Frankfurter Wertpapierbörse"}


# ── Parameterised builders ─────────────────────────────────────────────────

def _pct(s):
    return float(str(s).replace(",", "."))


def _fmt_thousands(n):
    return f"{int(n):,}".replace(",", ".")


def _eur2(n):
    """Format a float as German-style number with 2 decimals: 1.234.567,89"""
    s = f"{n:,.2f}"  # 1,234,567.89
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def beteiligungsmeldung(no, datum, melder, melder_sitz, anteil_alt, anteil_neu,
                        schwelle, instrument, kommentar):
    """§ 33 WpHG Beteiligungsmeldung (Stimmrechtsmitteilung)."""
    aktien = round(_pct(anteil_neu) * 625000)
    sections = [
        ("1. Angaben zum Emittenten", (
            f"Emittent: {R['name']}\n\n"
            f"Sitz: 70567 Stuttgart, Vaihinger Straße 120\n\n"
            f"WKN: {WKN}\nISIN: {ISIN}\n\n"
            f"Grundkapital: 62.500.000 EUR, eingeteilt in 62.500.000 auf den Namen lautende Stueckaktien.\n\n"
            "Segment: Regulierter Markt (Prime Standard) der Frankfurter Wertpapierbörse, "
            "Notierungsaufnahme seit 14. Oktober 2022.")),
        ("2. Mitteilungspflichtige Person / Aktionaer",
            [["Position", "Angabe"],
             ["Name / Firma",        melder],
             ["Sitz",                melder_sitz],
             ["Art der Person",      "Juristische Person / Kapitalanlagegesellschaft"],
             ["Mitteilungspflicht",  "§ 33 Abs. 1 WpHG (Stimmrechte) i.V.m. § 34 WpHG (Zurechnung)"],
             ["Tochter / verb. Unternehmen", "Vgl. Konzernanhang der mitteilenden Person"]]),
        ("3. Anlass und Datum der Schwellenberuehrung", (
            f"Anlass der Mitteilung: Erwerb / Veraeusserung von Aktien mit Stimmrechten an dem Emittenten {R['name']}.\n\n"
            f"Datum der Schwellenberuehrung: {datum}\n\n"
            f"{kommentar}")),
        ("4. Stimmrechtsanteil – Beruehrte Schwelle", (
            f"Beruehrte Schwelle gemaess § 33 WpHG: {schwelle}.\n\n"
            f"Stimmrechtsanteil vor Schwellenberuehrung: {anteil_alt} % der Stimmrechte.\n\n"
            f"Stimmrechtsanteil nach Schwellenberuehrung: {anteil_neu} % der Stimmrechte "
            f"(entspricht rund {_fmt_thousands(aktien)} Stueckaktien).")),
        ("5. Aufschluesselung der Stimmrechte",
            [["Kategorie", "Anteil (%)", "Anzahl Stimmrechte"],
             ["Direkt gehaltene Stimmrechte (§ 33 WpHG)", anteil_neu, _fmt_thousands(aktien)],
             ["Instrumente (§ 38 WpHG)",                  "0,00",     "0"],
             ["Zugerechnete Stimmrechte (§ 34 WpHG)",     "0,00",     "0"],
             ["Summe",                                    anteil_neu, _fmt_thousands(aktien)]]),
        ("6. Instrumente i.S.d. § 38 WpHG", (
            f"Es bestehen aktuell keine sonstigen Finanzinstrumente im Sinne der §§ 38 ff. WpHG. "
            f"Eingesetztes Instrument zur Erlangung der Stimmrechte: {instrument}.")),
        ("7. Kette der Tochterunternehmen / Zurechnung", (
            "Die mitteilungspflichtige Person erlangt die Stimmrechte nicht ueber eine Kette "
            "kontrollierter Unternehmen i.S.d. § 34 WpHG. Eine Zurechnung an Mutterunternehmen "
            "erfolgt – sofern einschlaegig – ueber die in der Konzernrechnungslegung der "
            "mitteilenden Person aufgefuehrten verbundenen Unternehmen.")),
        ("8. Veroeffentlichungs- und Mitteilungsweg", (
            f"Die Mitteilung wurde an die Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) "
            f"sowie an den Emittenten Brennhagen Elektronik AG (Frau Dr. Annika Felder, Leiterin Investor "
            f"Relations) uebermittelt und unverzueglich gemaess § 40 WpHG i.V.m. § 26 Abs. 1 WpHG "
            f"ueber das EQS Cockpit (DGAP) sowie das Unternehmensregister veroeffentlicht.\n\n"
            "Empfangsbestaetigung BaFin: laufende Vorgangsnummer wird auf Anforderung mitgeteilt.")),
        ("9. Ansprechpartner Emittent", (
            "Investor Relations\n"
            "Frau Dr. Annika Felder (Leiterin IR)\n"
            "ir@brennhagen-elektronik.de\n"
            "Telefon: +49 711 4567-9100\n\n"
            f"Stuttgart, {datum}\n\n"
            "Brennhagen Elektronik AG – Der Vorstand")),
    ]
    return f"Beteiligungsmeldung Nr. {no} – Stimmrechtsmitteilung gemaess § 33 WpHG", sections


def directors_dealing(no, datum, person, rolle, art, anzahl, preis):
    volumen = anzahl * preis
    sections = [
        ("1. Angaben zum Emittenten", (
            f"Emittent: {R['name']}\n"
            f"Sitz: 70567 Stuttgart, Vaihinger Straße 120\n"
            f"LEI: 5299006RHGRP1Stuttgart00\n"
            f"WKN: {WKN}  /  ISIN: {ISIN}\n"
            f"Boersensegment: Regulierter Markt, Prime Standard, FWB Frankfurt.")),
        ("2. Angaben zur meldepflichtigen Person", (
            f"Name: {person}\n\n"
            f"Funktion: {rolle}\n\n"
            "Status: Person mit Fuehrungsaufgaben gemaess Art. 3 Abs. 1 Nr. 25 i.V.m. Art. 19 "
            "Marktmissbrauchsverordnung (MAR, VO (EU) 596/2014).\n\n"
            "In enger Beziehung stehende Personen i.S.d. Art. 3 Abs. 1 Nr. 26 MAR: keine "
            "betroffenen Eigengeschaefte zum Berichtsstichtag.")),
        ("3. Angaben zum Geschaeft",
            [["Position", "Angabe"],
             ["Art des Geschaefts",      art],
             ["Datum des Geschaefts",    datum],
             ["Ort des Geschaefts",      "XETRA, Frankfurter Wertpapierbörse"],
             ["Finanzinstrument",        f"Stueckaktien Brennhagen Elektronik AG, ISIN {ISIN}"],
             ["Anzahl Stueck",           _fmt_thousands(anzahl)],
             ["Kurs in EUR",             f"{preis:.2f}".replace(".", ",")],
             ["Volumen in EUR",          _eur2(volumen)],
             ["Waehrung",                "EUR"],
             ["Aggregiert (gewichteter Durchschnitt)", "Ja"]]),
        ("4. Rechtsgrundlage und Sperrfrist", (
            "Die Meldung erfolgt gemaess Art. 19 Abs. 1 MAR (Eigengeschaefte von Fuehrungskraeften) "
            "binnen drei Geschaeftstagen. Es lag zum Zeitpunkt des Geschaefts keine Closed-Period "
            "i.S.d. Art. 19 Abs. 11 MAR vor; insbesondere wurde die 30-Tage-Sperrfrist vor "
            "Veroeffentlichung des Quartals- bzw. Jahresfinanzberichts eingehalten.\n\n"
            "Eine vorherige Freigabe wurde gemaess Insider-Compliance-Richtlinie der "
            "Brennhagen Elektronik AG (Stand 01.10.2022) durch das Compliance-Office "
            "(Andreas Buehler, CAE) erteilt.")),
        ("5. Aggregation der Geschaefte",
            f"Aggregierter Gesamtumfang aller in einem Geschaeftstag durch die meldepflichtige Person "
            f"in dem oben genannten Finanzinstrument durchgefuehrten Geschaefte: {_fmt_thousands(anzahl)} Stueck "
            f"zu einem volumengewichteten Durchschnittskurs von {preis:.2f} EUR. "
            f"Brutto-Transaktionsvolumen: {_eur2(volumen)} EUR."),
        ("6. Veroeffentlichung und Compliance", (
            "Diese Mitteilung wird unverzueglich nach Art. 19 Abs. 3 MAR an die BaFin uebermittelt "
            "und ueber das EQS Cockpit (DGAP) sowie die Investor-Relations-Webseite der "
            "Brennhagen Elektronik AG (www.brennhagen-elektronik.de/ir) veroeffentlicht.\n\n"
            "Die Eintragung in das Insiderverzeichnis gemaess Art. 18 MAR ist erfolgt; das "
            "Verzeichnis wird durch die Compliance-Abteilung gepflegt.")),
        ("7. Ansprechpartner / IR-Office", (
            "Investor Relations: Frau Dr. Annika Felder, ir@brennhagen-elektronik.de, +49 711 4567-9100\n"
            "Compliance: Andreas Buehler (CAE), compliance@brennhagen-elektronik.de\n\n"
            f"Stuttgart, {datum}")),
    ]
    return f"Directors' Dealing Meldung Nr. {no} – Eigengeschaeft einer Fuehrungskraft (Art. 19 MAR)", sections


def wphg_meldung(no, datum, melder, melder_sitz, schwelle_alt, schwelle_neu):
    sections = [
        ("1. Mitteilungspflicht nach §§ 33, 38 WpHG", (
            f"Hiermit teilt {melder} ({melder_sitz}) gemaess §§ 33 ff. Wertpapierhandelsgesetz (WpHG) "
            f"i.V.m. Art. 5 Abs. 1 Buchst. a) der Durchfuehrungsverordnung (EU) 2015/761 mit, dass "
            f"durch eine am {datum} erfolgte Transaktion eine meldepflichtige Schwelle der Stimmrechte "
            f"an der {R['name']} (ISIN {ISIN}) ueber- bzw. unterschritten wurde.")),
        ("2. Schwellenangabe und Stimmrechtsanteil",
            [["Position", "Vor Transaktion", "Nach Transaktion"],
             ["Schwelle (§ 33 WpHG)",   schwelle_alt, schwelle_neu],
             ["Stimmrechtsanteil (%)",  schwelle_alt, schwelle_neu],
             ["Stimmrechte (Stueck)",   _fmt_thousands(_pct(schwelle_alt)*625000), _fmt_thousands(_pct(schwelle_neu)*625000)],
             ["Instrumente (§ 38 WpHG)","0,00 %",     "0,00 %"]]),
        ("3. Art der Stimmrechtsausuebung", (
            "Die Stimmrechte werden unmittelbar gemaess § 33 WpHG gehalten. Eine Zurechnung nach "
            "§ 34 WpHG erfolgt – soweit einschlaegig – ueber Tochterunternehmen im Sinne der "
            "konsolidierten Konzernrechnungslegung der mitteilungspflichtigen Person.\n\n"
            "Es bestehen keine Stimmrechtsvereinbarungen (Acting-in-concert i.S.d. § 34 Abs. 2 WpHG) "
            "mit Dritten in Bezug auf die Aktien des Emittenten.")),
        ("4. Finanzinstrumente i.S.d. § 38 WpHG", (
            "Es werden derzeit keine Finanzinstrumente nach § 38 WpHG mit Bezug auf Aktien der "
            "Brennhagen Elektronik AG gehalten (insbesondere keine Optionen, Wandelschuldverschreibungen, "
            "Cash-settled Equity Swaps oder Contracts for Difference).")),
        ("5. Veroeffentlichung", (
            f"Die Mitteilung wurde am {datum} um 17:30 MEZ an die BaFin und den Emittenten "
            f"uebermittelt. Veroeffentlichung erfolgt unverzueglich nach § 40 WpHG ueber das EQS Cockpit "
            f"(DGAP) sowie das Unternehmensregister. Der Emittent leitet diese Mitteilung gleichzeitig "
            f"den europaeischen Medien zur EU-weiten Verbreitung zu.")),
        ("6. Ansprechpartner", (
            "Brennhagen Elektronik AG – Investor Relations\n"
            "Frau Dr. Annika Felder, Leiterin IR\n"
            "Vaihinger Straße 120, 70567 Stuttgart\n"
            "ir@brennhagen-elektronik.de / +49 711 4567-9100\n\n"
            f"Stuttgart, {datum}")),
    ]
    return f"WpHG-Stimmrechtsmitteilung Nr. {no} (§§ 33, 38 WpHG)", sections


def short_selling(no, datum, melder, melder_sitz, anteil_alt, anteil_neu):
    sections = [
        ("1. Rechtsgrundlage", (
            f"Diese Mitteilung erfolgt gemaess Verordnung (EU) Nr. 236/2012 (Leerverkaufs-VO) "
            f"i.V.m. § 2 Abs. 1 Nr. 30 WpHG. Mitgeteilt wird das Halten / die Veraenderung einer "
            f"signifikanten Netto-Leerverkaufsposition in Aktien der {R['name']} (ISIN {ISIN}).")),
        ("2. Angaben zur meldenden Person",
            [["Position",  "Angabe"],
             ["Firma",     melder],
             ["Sitz",      melder_sitz],
             ["Rechtsform","Investmentgesellschaft / Asset Manager"],
             ["LEI",       "529900XXXXXXXXXXX001"]]),
        ("3. Angaben zur Netto-Leerverkaufsposition",
            [["Position", "Vor", "Nach"],
             ["Datum der Position",                f"vorherige Meldung {melder.split()[0]}", datum],
             ["Anteil am ausgegebenen Aktienkapital (%)", anteil_alt, anteil_neu],
             ["Anzahl Aktien (entspricht)",        _fmt_thousands(_pct(anteil_alt)*625000), _fmt_thousands(_pct(anteil_neu)*625000)],
             ["Schwelle gemaess EU-VO",            "0,50 %",  "0,50 %"]]),
        ("4. Berechnung", (
            "Die Netto-Leerverkaufsposition wurde gemaess Art. 3 der VO (EU) 236/2012 in der "
            "konsolidierten Form berechnet (Bruttoposition minus gehaltene Long-Position bzw. "
            "wirtschaftlich aequivalente Instrumente). Beruecksichtigt wurden alle Cash-Aktien, "
            "Total Return Swaps, Index-Komponenten sowie Optionsdelta.")),
        ("5. Veroeffentlichung und Notifizierung", (
            "Die Mitteilung wurde am angegebenen Datum vor 15:30 Uhr MEZ an die BaFin uebermittelt; "
            "die Veroeffentlichung im BaFin Netto-Leerverkaufs-Register erfolgte am Folgetag um 22:00 Uhr. "
            "Eine Information an den Emittenten erfolgt nachrichtlich.")),
        ("6. Ansprechpartner Emittent", (
            f"Brennhagen Elektronik AG, Investor Relations, Frau Dr. Annika Felder. "
            f"Diese Mitteilung wurde am {datum} im IR-Dossier des Emittenten dokumentiert.")),
    ]
    return f"Netto-Leerverkaufsposition – Meldung Nr. {no} (VO (EU) 236/2012)", sections


# ── Specific (non-capital-markets) docs in this folder ─────────────────────

def qbr_continental():
    title = "Quarterly Business Review Q1/2023 – BMS-12 Programm – Continental AG"
    sections = [
        ("1. Programm-Eckdaten", [
            ["Position", "Angabe"],
            ["Produkt", "BMS-12 (BatteryMS-12, Batteriemanagementsystem EV)"],
            ["Kunde / Tier-1", "Continental AG, Division Smart Mobility, Regensburg"],
            ["End-OEM", "Volkswagen AG (Plattform MEB+, Modell ID.7)"],
            ["Volumen 2023", "ca. 480.000 Stueck (+18 % YoY)"],
            ["Umsatz Q1/2023", "62,4 Mio. EUR"],
            ["DB1 / Marge", "21,8 %"],
        ]),
        ("2. Operative KPIs Q1/2023", [
            ["KPI", "Ziel", "Ist", "Status"],
            ["OTD (On-Time-Delivery)", "≥ 98,5 %", "97,4 %", "gelb"],
            ["PPM-Niveau Feldausfall",  "≤ 12",     "9",      "gruen"],
            ["IATF 16949-Audits",       "0 major",  "0 major","gruen"],
            ["RMA-Quote",               "< 0,3 %",  "0,21 %", "gruen"],
            ["FOR (First Out Right)",   "≥ 96 %",   "95,2 %", "gelb"],
        ]),
        ("3. Top-3 Themen", ("list", [
            "Lieferengpass MOSFET (Infineon) – Sonderlogistik bis KW 18, "
            "Sicherheitsbestand auf 12 Tage erhoeht, gemeinsamer Allocation-Call mit Continental wöchentlich.",
            "Software-Release 12.4.0 (FOTA-Updatefaehigkeit) – Validierung "
            "beim OEM gestartet, Freigabe geplant fuer KW 24/2023.",
            "Capacity Ramp-up Werk RPL Katowice – +25 % Linienkapazitaet bis "
            "Q3/2023, CAPEX 2,8 Mio. EUR genehmigt."
        ])),
        ("4. Forecast 2023", (
            "Auf Basis der aktuellen Take-rates und der bestaetigten Forecasts der "
            "Continental AG (rollierender 12-Monats-Forecast vom 14.03.2023) erwartet "
            "die Brennhagen Elektronik AG fuer das BMS-12-Programm einen Jahresumsatz von "
            "rund 268 Mio. EUR (Vorjahr: 228 Mio. EUR) bei einer DB1-Marge zwischen "
            "20,5 % und 22,0 %. Risiken bestehen vor allem hinsichtlich der Halbleiter-"
            "Verfuegbarkeit (Power-Devices) und einer moeglichen Verschiebung des "
            "Modell-Anlaufs des ID.7-Long-Range.")),
        ("5. Naechste Schritte", ("list", [
            "QBR Q2/2023 am 12. Juli 2023 in Regensburg (Continental-HQ).",
            "Joint Cost-Down Workshop (Target: -3,5 % auf BoM, Effekt ab Q4/2023).",
            "Lieferfreigabe SOP+ fuer Sicherheitsrelais-Variante (DR-12B).",
            "Eskalations-Review bei wiederholtem OTD < 97 %.",
        ])),
        ("6. Teilnehmer", (
            "Brennhagen Elektronik AG: Dr. Thomas Weber (COO), Stefan Richter (CMO/BD), "
            "Markus Pflanzer (Treasurer), Florian Maier (Controlling), Andreas Maier (Werkleiter REG).\n\n"
            "Continental AG: Dr. Stefan Vogt (Head of EE-Architectures), Dr. Eva Linder (Procurement), "
            "Markus Renner (Quality), Lara Pfeiffer (Program Management).\n\n"
            "Datum: 18. April 2023, Online (MS Teams).")),
    ]
    return title, sections, True  # confidential


def kpmg_management_letter_rpl():
    title = "Management Letter 2021 – Brennhagen Polska Sp. z o.o. (Pruefer-Empfehlungen)"
    sections = [
        ("Adressat und Pruefungsumfang", (
            "An den Vorstand der Brennhagen Elektronik AG, z.Hd. Frau Laura Bauer (CFO), "
            "sowie an die Geschaeftsfuehrung der Brennhagen Polska Sp. z o.o. (Werkleiter "
            "Marek Wojciechowski, HR-Leitung Anna Kowalska).\n\n"
            "Im Rahmen der gesetzlichen Abschlusspruefung 2021 der Brennhagen Polska "
            "Sp. z o.o. (KRS 0000543210) gemaess polnischem Bilanzrecht (Ustawa o "
            "rachunkowości) und IFRS-Reporting Package fuer Konsolidierungszwecke "
            "der Brennhagen Elektronik AG haben wir folgende Feststellungen getroffen, "
            "die wir Ihnen mit diesem Management Letter mitteilen.")),
        ("Feststellung 1 – Bestandsbewertung Rohmaterialien", (
            "Das eingesetzte Verfahren der Materialbewertung (gleitender Durchschnitt) "
            "ist grundsaetzlich angemessen. Wir empfehlen jedoch, das automatisierte "
            "Reichweitenkennzeichen (Slow-Moving > 270 Tage) im SAP S/4HANA-System "
            "konsequent monatlich auszuwerten. Im Stichprobenumfang von 50 Materialien "
            "fanden wir 7 Positionen mit Reichweite > 365 Tage ohne Wertberichtigungs-Markierung "
            "(Buchwert TEUR 218). Eine Anpassung wurde nachgebucht.")),
        ("Feststellung 2 – Funktionstrennung Beschaffung / Wareneingang", (
            "In der Werkbeschaffung (Indirektmaterial) ist die Berechtigung zur "
            "Stammdatenpflege Lieferant nicht ausreichend von der Auftragsfreigabe "
            "getrennt. Wir empfehlen eine Anpassung der SAP-Rollenkonzeption (FI-MM) "
            "im Zuge des naechsten S/4HANA-Releases. Risikoklasse: mittel.")),
        ("Feststellung 3 – Dokumentation Verrechnungspreise", (
            "Die polnische Local-File-Dokumentation 2021 (Transfer-Pricing) wurde "
            "uns vorgelegt; die Benchmarkstudie fuer Lohnveredelungs-Cost-Plus-Saetze "
            "stammt aus 2018 und sollte aktualisiert werden. Wir empfehlen eine "
            "Neufassung durch externe Berater (z.B. KPMG Polska, KPMG Stuttgart) bis 30.06.2022.")),
        ("Feststellung 4 – IT-General-Controls", (
            "Patch-Management des SAP-Anwendungsservers in Katowice erfolgt nicht "
            "synchron mit dem Central-IT-Calendar in Stuttgart. Wir empfehlen "
            "Integration in das Group-IT-Patch-Window monatlich, mit dokumentierter "
            "Freigabe durch den lokalen IT-Verantwortlichen.")),
        ("Feststellung 5 – Pensionsverpflichtungen", (
            "Die zur Bewertung der Jubilaeumsverpflichtungen verwendete Sterbetafel "
            "(Polnische ZUS-Tafel 2019) sollte auf den jeweils aktuellen Stand "
            "(2021) aktualisiert werden; Effekt auf das Konsolidierungs-Reporting "
            "geringfuegig (< TEUR 40).")),
        ("Zusammenfassende Beurteilung", (
            "Das interne Kontrollsystem (IKS) der Brennhagen Polska Sp. z o.o. erscheint "
            "in seiner Gesamtheit angemessen; die obigen Empfehlungen fuehren zu "
            "keiner Einschraenkung des Bestaetigungsvermerks. Die Geschaeftsfuehrung "
            "hat die Umsetzung bis zum naechsten Pruefungstermin (Mai 2022) zugesagt.")),
        ("Berliner / Stuttgarter Kontakt", (
            "KPMG AG WPG, Lead-Partner Dr. Maximilian Brand (Stuttgart), "
            "Senior-Manager Anja Petersen, +49 711 9060-12345, "
            "abrand@kpmg.com / apetersen@kpmg.com. Die Diskussion mit dem "
            "Pruefungsausschuss der Brennhagen Elektronik AG (Vorsitz: Prof. Dr.-Ing. "
            "Gerhard Voss) ist fuer den 21.04.2022 terminiert.")),
    ]
    return title, sections, True


def bmw_eskalation():
    title = "Eskalationsschreiben – Lieferengpaesse ICP-3 / ADAS-V4D – Geschaeftsjahr 2022"
    sections = [
        ("Adressat / Bezug", (
            "Empfaenger: BMW Group, Global Procurement Indirect Electronics, "
            "z.Hd. Herrn Dr. Stefan Vogt (Senior Vice President Purchasing E/E), "
            "Knorrstraße 147, 80788 Muenchen.\n\n"
            "Bezug: Rahmenliefervertrag RHV-BMW-2019-04 vom 12.06.2019 sowie "
            "Auftragsabrufe AB-BMW-2022-Q3 und AB-BMW-2022-Q4 ueber Bauteile "
            "ICP-3 (InfoConnect Pro) und ADAS-V4D (Radar Fusion Steuergeraet).")),
        ("Sachverhalt", (
            "Sehr geehrter Herr Dr. Vogt, sehr geehrte Damen und Herren,\n\n"
            "wie bereits mehrfach kommuniziert (zuletzt Konferenzschaltung vom "
            "14. Oktober 2022) sehen wir uns aufgrund der anhaltenden Marktstoerungen "
            "in der Halbleiter-Lieferkette (insbesondere NXP TJA1145T-CAN-Transceiver "
            "und Infineon Aurix TC397 Microcontroller) gezwungen, das urspruenglich "
            "vereinbarte Volumen fuer KW 42–52/2022 in Hoehe von 184.000 Stueck "
            "ICP-3 und 96.000 Stueck ADAS-V4D auf voraussichtlich 152.000 Stueck "
            "ICP-3 und 78.000 Stueck ADAS-V4D anzupassen.")),
        ("Massnahmen Brennhagen", ("list", [
            "Allocation-Verhandlungen mit NXP und Infineon auf Vorstandsebene (Anna Mueller, CEO);",
            "Aktivierung Zweitquelle Renesas RH850/F1KM-D1 fuer Mikrocontroller (Re-Qualifizierung im Werk Heilbronn bis KW 49);",
            "Erhoehung Sicherheitsbestand auf 14 Tage Reichweite (zuvor 7 Tage);",
            "Wechsel auf Luft-Logistik (Air Freight) fuer kritische Subkomponenten – Mehrkosten ca. 380 TEUR/Monat;",
            "Tageweise Kapazitaetsberichte an BMW Global Procurement (Wojciechowski, Werkleiter RPL);",
        ])),
        ("Vertragliche Einordnung", (
            "Wir verweisen auf § 8 Abs. 4 des Rahmenliefervertrages (Hoehere Gewalt / "
            "Force Majeure). Die aktuellen Versorgungsstoerungen erfuellen die dort "
            "vereinbarten Voraussetzungen (oeffentlich dokumentierte Halbleiterkrise, "
            "Allocation-Schreiben der Vorlieferanten, weltweite Industriebetroffenheit). "
            "Wir bitten um eine entsprechende Anpassung der Lieferpflichten ohne "
            "Geltendmachung von Vertragsstrafen bzw. Pönalen.")),
        ("Vorschlag fuer das weitere Vorgehen", (
            "Wir schlagen ein Eskalations-Meeting auf Vorstandsebene Anna Mueller / "
            "Joachim Post (BMW Member of the Board, Procurement) am 03. November 2022 "
            "in Muenchen vor. Bis dahin koordinieren operativ Herr Dr. Thomas Weber "
            "(COO Brennhagen) und Frau Lara Pfeiffer (BMW Program Management).\n\n"
            "Mit der Bitte um Verstaendnis und einer kurzfristigen Rueckmeldung "
            "verbleiben wir mit freundlichen Gruessen.")),
        ("Unterschriften", signatures(
            "Anna Mueller", "Vorstandsvorsitzende (CEO)", "Brennhagen Elektronik AG",
            "Dr. Thomas Weber", "Vorstand (COO)", "Brennhagen Elektronik AG",
            place="Stuttgart", date_str_="19. Oktober 2022")),
    ]
    return title, sections, True


def konzernrichtlinie_einkauf():
    title = "Konzernrichtlinie KR-EK-001 – Beschaffung / Global Sourcing (Gueltig ab 01.01.2023)"
    sections = [
        ("§ 1 Geltungsbereich und Ziel", (
            "Diese Konzernrichtlinie gilt verbindlich fuer alle Beschaffungsvorgaenge im "
            "Brennhagen-Konzern. Erfasst sind die Brennhagen Elektronik AG sowie alle direkten und "
            "indirekten Tochtergesellschaften (REG Heilbronn, RSG Muenchen, RPL Katowice, "
            "RCZ Brno, RHU Gyor, RCN Shanghai, RHO Holding). Ziel ist die Sicherstellung "
            "eines einheitlichen, rechtskonformen und wirtschaftlich vorteilhaften Bezugs "
            "von direkten und indirekten Materialien sowie Dienstleistungen.")),
        ("§ 2 Begriffe und Verantwortlichkeiten", (
            "Direktmaterial: Komponenten, die in die hergestellten Produkte eingehen "
            "(Halbleiter, PCB, Steckverbinder, Sensoren, mechanische Teile).\n\n"
            "Indirektmaterial: Verbrauchs- und Hilfsmittel, IT-Beschaffung, Dienstleistungen, "
            "Anlagen unterhalb Investitionsschwelle.\n\n"
            "Investitionen (CAPEX) > 250 TEUR sind separat ueber die CAPEX-Richtlinie "
            "(KR-FIN-004) zu beantragen.\n\n"
            "Verantwortlich fuer den Konzerneinkauf ist der Group Head of Procurement "
            "(Dr. Thomas Weber, COO) sowie die lokalen Werkleitungen.")),
        ("§ 3 Beschaffungsprinzipien", ("list", [
            "Vier-Augen-Prinzip ab Bestellwert 5.000 EUR;",
            "Ausschreibungspflicht (mind. 3 Angebote) ab 25.000 EUR Bestellwert;",
            "Trennung Bedarfsstellung / Bestellung / Wareneingang (Funktionstrennung);",
            "Lieferantenqualifizierung gemaess IATF 16949 und VDA 6.3 fuer Direktmaterial;",
            "ESG-Mindestanforderungen (UN Global Compact, EU CSDDD, LkSG) fuer alle Lieferanten;",
            "Bevorzugung von Dual- / Multi-Sourcing fuer kritische Halbleiter;",
            "Praeferenz fuer EU-Lieferanten bei sicherheitsrelevanten Bauteilen (Resilience).",
        ])),
        ("§ 4 Genehmigungsmatrix", [
            ["Bestellwert (EUR)", "Genehmigungsstufe", "Pflichtdokumentation"],
            ["bis 5.000",          "Fachbereich / Kostenstellenleitung", "Bestellanforderung, 1 Angebot"],
            ["5.001 – 25.000",     "Einkaufsleitung Werk",                "BANF, 2 Angebote"],
            ["25.001 – 100.000",   "Werkleitung + Group Procurement",     "BANF, 3 Angebote, TCO-Vergleich"],
            ["100.001 – 500.000",  "COO + Treasurer (M. Pflanzer)",       "Sourcing Decision Memo"],
            ["> 500.000",          "Vorstand (kollegial)",                "Vorstandsvorlage"],
        ]),
        ("§ 5 Lieferantenmanagement", (
            "Saemtliche Direktmaterial-Lieferanten sind im SAP-Lieferantenstamm zu "
            "fuehren und werden jaehrlich nach Qualitaet (PPM-Wert), Liefertreue (OTD), "
            "Preis (TCO), Innovation und ESG bewertet (Score 1-5). Lieferanten mit "
            "Score < 2,5 ueber zwei aufeinanderfolgende Bewertungen werden in den "
            "Eskalations- bzw. Phase-out-Prozess ueberfuehrt.")),
        ("§ 6 Compliance, Sanktionen und ESG", (
            "Bei jeder Lieferanten-Neuanlage erfolgt ein Sanctions-Screening (EU/OFAC). "
            "Lieferanten mit Sitz in sanktionierten Laendern sind grundsaetzlich "
            "ausgeschlossen. Die Erfuellung der Sorgfaltspflichten gemaess Lieferketten-"
            "sorgfaltspflichtengesetz (LkSG) wird ueber einen Code-of-Conduct sowie "
            "risikobasierte Audits sichergestellt. Verstoesse sind unverzueglich an "
            "den Chief Audit Executive Andreas Buehler (compliance@brennhagen-elektronik.de) zu melden.")),
        ("§ 7 Inkrafttreten und Aenderungen", (
            "Diese Richtlinie tritt am 01.01.2023 in Kraft und ersetzt die Fassung KR-EK-001 "
            "vom 01.07.2020. Aenderungen werden vom Vorstand beschlossen und ueber das "
            "Konzern-Intranet (Compliance-Portal) bekannt gegeben.\n\n"
            "Stuttgart, 15. Dezember 2022 – Der Vorstand")),
    ]
    return title, sections, False


def patent_antwort():
    title = "Patentanmeldung DE10 2013 1234 567.8 – Antwort des Anmelders auf Pruefbescheid"
    sections = [
        ("Aktenzeichen / Bezug", (
            "Deutsches Patent- und Markenamt (DPMA), Zweibrueckenstraße 12, 80331 Muenchen.\n\n"
            "Aktenzeichen: DE10 2013 1234 567.8\n"
            "Anmelderin: Brennhagen Elektronik AG, Vaihinger Straße 120, 70567 Stuttgart\n"
            "Vertreter: Patentanwaltskanzlei Boehmert & Boehmert PartmbB, Pettenkoferstraße 22, 80336 Muenchen\n"
            "Bezug: Pruefbescheid des DPMA vom 28. Februar 2023 (Pruefer: Dipl.-Phys. Hartmut Renner).")),
        ("Antrag", (
            "Namens und im Auftrag der Anmelderin Brennhagen Elektronik AG beantragen wir, "
            "die Anmeldung in der mit Schriftsatz vom 11. April 2023 vorgelegten geaenderten "
            "Anspruchsfassung (Hauptantrag) zu pruefen und das Patent zu erteilen. Hilfsweise "
            "wird die Pruefung in den geaenderten Anspruchssaetzen 1 bis 3 (Hilfsantraege I-III) beantragt.")),
        ("Aenderungen gegenueber der urspruenglichen Anmeldung", ("list", [
            "Patentanspruch 1 wurde dahingehend praezisiert, dass das radarbasierte "
            "Sensorfusionsmodul ein hardwarebeschleunigtes neuronales Inferenz-Modul "
            "(NPU) mit einer Rechenleistung von mindestens 5 TOPS umfasst.",
            "Patentanspruch 5 wurde gestrichen und in den (gemaess Hilfsantrag I) "
            "in den abhaengigen Patentanspruch 6 integriert.",
            "Beschreibung Seite 12, Zeile 7-21 wurde redaktionell angepasst (Korrektur "
            "der Bezugszeichen).",
            "Figur 3 wurde durch eine erweiterte Darstellung mit Hardware-Architektur ersetzt.",
        ])),
        ("Erwiderung auf die Beanstandungen des Pruefers", (
            "Zur Erfindungsmaennigkeit (§ 4 PatG) im Hinblick auf D1 (US 2018/0345678 A1, "
            'Continental AG, "Sensor fusion module for advanced driver assistance systems") '
            "fuehren wir aus, dass das streitgegenstaendliche Merkmal der NPU-gestuetzten "
            "Echtzeitfusion mit ASIL-D-Konformitaet in D1 weder offenbart noch nahegelegt ist. "
            "D1 lehrt lediglich eine softwarebasierte Fusion auf einem Cortex-A53-Mehrkernprozessor "
            "ohne dedizierte NPU. Eine Kombination mit D2 (DE 10 2019 654 321 A1, NXP) waere "
            "fuer den Fachmann nicht nahegelegt, da D2 keinen Hinweis auf eine "
            "funktionssichere ASIL-D-Implementierung enthaelt.")),
        ("Schlussantrag und Erklaerungen", (
            "Wir bitten um zeitnahe Beruecksichtigung dieses Schriftsatzes und um Mitteilung, "
            "falls weitere Beanstandungen bestehen. Auf Wunsch des Pruefers stehen wir fuer "
            "eine telefonische Pruefer-Anhoerung zur Verfuegung (Ansprechpartner: Patentanwalt "
            "Dr.-Ing. Sebastian Roeder, +49 89 599-09-0).\n\n"
            "Im Auftrag der Brennhagen Elektronik AG\n"
            "Dipl.-Phys. Dr.-Ing. Sebastian Roeder, Patentanwalt\n"
            "Muenchen, 11. April 2023")),
    ]
    return title, sections, False


def rcz_ic_rechnung():
    title = "Intercompany-Rechnung IC-RCZ-2022-12 – Brennhagen CZ s.r.o. → Brennhagen Elektronik GmbH"
    sections = [
        ("Rechnungsdaten",
            [["Position", "Angabe"],
             ["Rechnungsnummer",      "IC-RCZ-2022-12"],
             ["Rechnungsdatum",       "31. Dezember 2022"],
             ["Leistungszeitraum",    "01.12.2022 – 31.12.2022"],
             ["Leistungserbringer",   "Brennhagen CZ s.r.o., Tovární 25, 61700 Brno, CZ, IČO 28418762"],
             ["Leistungsempfaenger",  "Brennhagen Elektronik GmbH, Carl-Benz-Straße 14, 74076 Heilbronn, DE"],
             ["USt-IdNr. RCZ",        "CZ28418762"],
             ["USt-IdNr. REG",        "DE 287 901 234"],
             ["Reverse-Charge",       "Ja (§ 13b UStG / Art. 196 MwStSystRL)"]]),
        ("Leistungsbeschreibung – Lohnveredelung Dezember 2022", [
            ["Pos.", "Produkt / Leistung", "Menge", "Einzelpreis EUR", "Betrag EUR"],
            ["1", "Steckverbinder STV-440 (Lohnveredelung)", "84.500 Stck", "2,180", "184.210,00"],
            ["2", "Steckverbinder STV-680 (Lohnveredelung)", "42.300 Stck", "2,920", "123.516,00"],
            ["3", "EMS-Bestueckung BMS-12-Subboard",         "12.800 Stck", "11,40",  "145.920,00"],
            ["4", "Cost-Plus-Aufschlag 5,5 % (TP)",          "—",           "—",      "24.926,93"],
            ["Summe netto", "", "", "", "478.572,93"],
        ]),
        ("Transferpreis-Methode", (
            "Die Verrechnung erfolgt nach Cost-Plus-Methode mit einem fremdueblichen "
            "Aufschlag von 5,5 % auf die in der Brennhagen CZ s.r.o. angefallenen voll "
            "absorbierten Kosten (Material, Fertigungsloehne, Werks-Gemeinkosten, allgemeine "
            "Verwaltungskosten). Der Aufschlag basiert auf der Benchmark-Studie der "
            "KPMG AG WPG aus 2021 (Kontraktfertigung Elektronik, Median 4,8 %, Bandbreite "
            "3,9 %–6,2 %). Die Local-File-Dokumentation 2022 weist die Methode aus.")),
        ("Zahlung und Bankverbindung", (
            "Zahlung 30 Tage netto ueber das Konzern-Cash-Pool-Konto. Der "
            "Konzern-Treasurer Markus Pflanzer (Brennhagen Holding GmbH) verrechnet "
            "ueber die Cash-Pool-Position; physischer Zahlungsausgleich quartalsweise.\n\n"
            "Begleitend wurde diese Rechnung in der konsolidierten IC-Matching-Liste "
            "Dezember 2022 (Berater: Florian Maier, Group Controller) erfasst.")),
        ("Unterschriften",
            signatures("Petr Novák", "Geschaeftsfuehrer", "Brennhagen CZ s.r.o.",
                       "Andreas Maier", "Werkleiter", "Brennhagen Elektronik GmbH",
                       place="Brno / Heilbronn", date_str_="31. Dezember 2022")),
    ]
    return title, sections, False


def reg_to_rsg_ic():
    title = "Intercompany-Rechnung IC-REG-2022-03 – Brennhagen Elektronik GmbH → Brennhagen Software GmbH"
    sections = [
        ("Rechnungsdaten",
            [["Position", "Angabe"],
             ["Rechnungsnummer",     "IC-REG-2022-03"],
             ["Rechnungsdatum",      "31. Maerz 2022"],
             ["Leistungszeitraum",   "01.03.2022 – 31.03.2022"],
             ["Leistungserbringer",  "Brennhagen Elektronik GmbH (REG), Heilbronn"],
             ["Leistungsempfaenger", "Brennhagen Software GmbH (RSG), Lyonel-Feininger-Straße 28, 80807 Muenchen"],
             ["USt-IdNr. REG",       "DE 287 901 234"],
             ["USt-IdNr. RSG",       "DE 287 901 567"]]),
        ("Leistungsbeschreibung – Test- und Validierungsdienste Maerz 2022", [
            ["Pos.", "Leistung", "Menge", "Stundensatz EUR", "Betrag EUR"],
            ["1", "EMV-Pruefstand REG (BMS-12 Validierung)",     "120 Std.", "165",   "19.800,00"],
            ["2", "Klimakammer-Test (Burn-in, -40 / +85 °C)",     " 80 Std.", "140",   "11.200,00"],
            ["3", "Funktionsmusterbau ICP-3-Engineering-Sample", " 24 Stck.","285",    "6.840,00"],
            ["4", "Cost-Plus-Aufschlag 6,0 % (TP)",               "—",       "—",     "2.270,40"],
            ["Summe netto",                                       "",        "",      "40.110,40"],
        ]),
        ("Verrechnungspreismethode", (
            "Die Verrechnung erfolgt nach Cost-Plus-Methode (TNMM-Bestaetigung). Der "
            "Aufschlagssatz von 6,0 % entspricht dem Median der Benchmark fuer "
            "Pruef-/Validierungs-Dienstleistungen zwischen verbundenen Unternehmen "
            "(KPMG-Benchmark 2021, Bandbreite 4,5 %–7,2 %, Median 5,9 %).")),
        ("Zahlung und Verbuchung", (
            "Faelligkeit 30 Tage nach Rechnungsdatum (Zahlungsziel: 30.04.2022), "
            "Saldierung ueber den Brennhagen-Cash-Pool (Master-Konto Brennhagen Holding GmbH "
            "bei der Deutschen Bank AG, IBAN DE89 6007 0024 0726 4510 00). Der physische "
            "Zahlungsausgleich erfolgt im Rahmen der quartalsweisen Cash-Pool-Saldierung "
            "durch den Group Treasurer Markus Pflanzer.\n\n"
            "Buchungsvorgang im SAP S/4HANA (Mandant 100, Buchungskreis REG): Belegart RV, "
            "Konto 60040 (IC-Erloese Test/Validierung), Gegenkonto 67050 RSG (IC-Aufwand). "
            "Konsolidierungs-Mapping fuer das Konzern-Reporting: Eliminierung gegen "
            "RSG-Belegart KR, dokumentiert in der monatlichen IC-Matching-Liste durch "
            "Florian Maier (Group Controller).")),
        ("Hinweise zur Compliance", (
            "Diese Leistungsverrechnung wurde durch den Group-Tax-Director Dr. Heike "
            "Berger im Rahmen der konzernweiten Transferpreis-Compliance freigegeben "
            "(Freigabe-Memo TP-2022-007). Die Local-File-Dokumentation 2022 fuer beide "
            "Gesellschaften referenziert diesen Vertragstyp explizit (Lohnveredelung und "
            "konzerninterne Dienstleistungen). Eine Master-File-Aktualisierung erfolgt "
            "jaehrlich zentral durch die KPMG AG WPG (Stuttgart) bis zum 31.12. des Folgejahres.")),
        ("Unterschriften",
            signatures("Andreas Maier", "Werkleiter", "Brennhagen Elektronik GmbH",
                       "Dr. Klaus Kessler", "Werkleiter", "Brennhagen Software GmbH",
                       place="Heilbronn / Muenchen", date_str_="31. Maerz 2022")),
    ]
    return title, sections, False


def ppap_mbz():
    title = "PPAP Level 3 – ADAS-V4D (Radar Fusion Steuergeraet) – Mercedes-Benz Group AG"
    sections = [
        ("Programm-Eckdaten",
            [["Position", "Angabe"],
             ["Produkt",                   "ADAS-V4D Radar Fusion Steuergeraet (Sachnr. 110-220-V4D-001)"],
             ["Kunde",                     "Mercedes-Benz Group AG, Mercedesstraße 120, 70372 Stuttgart"],
             ["Programmcode Mercedes",     "MMA Plattform / E-Klasse W214"],
             ["PPAP-Level",                "Level 3 (vollstaendige Dokumentation)"],
             ["Einreichung",               "15. Dezember 2022"],
             ["Werk Lieferant",            "Brennhagen Elektronik GmbH, Heilbronn (DE)"],
             ["Werk Sublieferant SMD",     "Brennhagen Polska Sp. z o.o., Katowice (PL)"],
             ["Lead Quality Engineer REA", "Sabine Brand (Q-Leitung REG)"]]),
        ("PPAP-Element-Checkliste",
            [["Nr.", "PPAP-Element", "Eingereicht", "Status"],
             ["1",  "Konstruktionsunterlagen / Design Records",              "Ja", "Freigegeben"],
             ["2",  "Engineering Change Documents (ECN)",                    "Ja", "Freigegeben"],
             ["3",  "Kundenspezifische Freigabe Engineering",                "Ja", "Freigegeben"],
             ["4",  "DFMEA (Design FMEA, ASIL-D-relevant)",                  "Ja", "Freigegeben"],
             ["5",  "Process Flow Diagrams",                                  "Ja", "Freigegeben"],
             ["6",  "PFMEA (Prozess-FMEA)",                                   "Ja", "Freigegeben"],
             ["7",  "Control Plan (Pre-Launch und Production)",               "Ja", "Freigegeben"],
             ["8",  "MSA (Measurement System Analysis)",                      "Ja", "Freigegeben"],
             ["9",  "Initial Process Studies (Cpk > 1,67 fuer CTQ-Merkmale)", "Ja", "Freigegeben"],
             ["10", "Laboratory Test Results (ISO/IEC 17025)",                "Ja", "Freigegeben"],
             ["11", "Qualified Laboratory Documentation (TUEV SUED)",         "Ja", "Freigegeben"],
             ["12", "Appearance Approval Report (n/a)",                       "n/a","—"],
             ["13", "Sample Production Parts (5 Mustermodule)",               "Ja", "Freigegeben"],
             ["14", "Master Sample (versiegelt)",                             "Ja", "Beim Kunden hinterlegt"],
             ["15", "Checking Aids / Pruefmittel-Liste",                      "Ja", "Freigegeben"],
             ["16", "Customer-specific Requirements (MB-Spezial-A 0001 ff.)", "Ja", "Freigegeben"],
             ["17", "Part Submission Warrant (PSW)",                          "Ja", "Unterzeichnet (Bauer/Brand/Weber)"],
             ["18", "Bulk Material Requirements Checklist (n/a)",             "n/a","—"]]),
        ("Capability- und Audit-Status", (
            "Initial-Process-Studie (4-Wochen-Vorlauf an SMD-Linie Katowice, Linie 7): "
            "Cpk_Loetstellen-Festigkeit = 1,82; Cpk_Stromverbrauch (Idle) = 1,94; "
            "Cpk_Antennen-Reflexion (S11) = 1,71.\n\n"
            "Run-at-Rate-Audit am 28.11.2022 erfolgreich bestanden (Auditor Mercedes: "
            "Markus Renner, MB-Quality). Vereinbarte Stueckzahlrate: 2.400 Stck/Tag "
            "(2-Schicht-Betrieb). VDA 6.3-Score: 89 % (Stufe A).")),
        ("PSW – Part Submission Warrant", (
            "Hiermit bestaetigen wir, dass alle Teile, die im Rahmen dieser Vorlage "
            "eingereicht werden, der zu erwartenden Spezifikation entsprechen und unter "
            "Bedingungen der Serienproduktion hergestellt wurden. Die Anforderungen des "
            "Kunden Mercedes-Benz wurden vollumfaenglich erfuellt.\n\n"
            "Eingereicht von: Sabine Brand (Q-Leitung REG), gegengezeichnet durch "
            "Dr. Thomas Weber (COO). Freigabevermerk Mercedes-Benz erwartet bis 20.01.2023.")),
    ]
    return title, sections, False


def prj_status_adas():
    title = "PRJ-2021-002 – ADAS-V4D Kalibrierungsplattform – Projektstatus Maerz 2023"
    sections = [
        ("Projektsteckbrief", [
            ["Position", "Angabe"],
            ["Projektnummer", "PRJ-2021-002"],
            ["Projektname",   "ADAS-V4D Kalibrierungsplattform – Werk Heilbronn"],
            ["Projektleitung","Lars Wittmann (RSG Muenchen), Dr. Thomas Weber (Sponsor)"],
            ["Start",         "12. September 2021"],
            ["Geplantes Ende","31. Mai 2023"],
            ["Status",        "AMBER (verschoben um 6 Wochen, Risiko Software-Stack)"],
            ["Budget",        "1.840 TEUR (gesamt) / 1.620 TEUR (Ist Maerz 2023)"],
        ]),
        ("Fortschritt seit letztem Status (Februar 2023)", ("list", [
            "Hardware-Endausbau (Roboter-Zelle KUKA KR Cybertech) abgeschlossen, IBN am 22.02.2023;",
            "Kalibriersoftware v2.4.0 in Validierungstest; Bug auf NPU-DMA-Engine (Aurix TC397) gefunden, Ticket #4321 offen;",
            "Mercedes-Auditbegehung am 09.03.2023 (Auditor: Jens Beerlage) erfolgreich, kein Major;",
            "Schulung der 6 Linienmitarbeiter REG (Heilbronn) abgeschlossen (Schulungstrainer: Frau Schmidt, R&D);",
            "Lieferanten-Audit Renesas (Ersatz-MCU) bestanden mit Score B (gut);",
        ])),
        ("Risiken / Top-3", ("list", [
            "R1: Software-Bug DMA-Engine – Workaround dokumentiert, Mitigation: Hotfix-Release v2.4.1 bis KW 15;",
            "R2: Halbleiter-Allocation Infineon Aurix – Sicherheitsbestand 20 Wochen aufgebaut;",
            "R3: Personalwechsel Lead-Tester (Frau Brand wechselt in Q2) – Knowledge-Transfer geplant KW 13/14.",
        ])),
        ("Forecast / Budget", [
            ["Position", "Plan TEUR", "Ist TEUR", "Forecast TEUR"],
            ["Hardware",                "780", "812", "812"],
            ["Software-Entwicklung",    "620", "598", "640"],
            ["Externe Dienstleister",   "240", "150", "210"],
            ["Sonstiges / Reserve",     "200", " 60", "120"],
            ["Summe",                  "1.840","1.620","1.782"],
        ]),
        ("Naechste Meilensteine", (
            "M5 Software-Freigabe v2.4.1 – 12.04.2023\n"
            "M6 Pilot-Run Mercedes-Vorserie (50 Module) – 28.04.2023\n"
            "M7 PPAP-Einreichung Update – 15.05.2023\n"
            "M8 Project Closure / Lessons Learned – 31.05.2023\n\n"
            "Erstellt von: Lars Wittmann (Projektleiter RSG), freigegeben durch "
            "Dr. Thomas Weber (COO), Heilbronn, 24.03.2023.")),
    ]
    return title, sections, True


# ── Build registry ─────────────────────────────────────────────────────────

JOBS = []

# Beteiligungsmeldungen (5)
BET = [
    ("002", "18. Mai 2022",       "BlackRock Inc.",                              "55 East 52nd Street, New York, NY 10055, USA",
     "2,95", "3,12", "3 % (§ 33 Abs. 1 WpHG)", "Erwerb von Stueckaktien ueber Boerse",
     "Erstmalige Ueberschreitung der 3-%-Schwelle im Rahmen normaler Portfolioallokation."),
    ("004", "07. Juni 2022",      "The Vanguard Group, Inc.",                    "100 Vanguard Blvd, Malvern, PA 19355, USA",
     "2,85", "3,07", "3 % (§ 33 Abs. 1 WpHG)", "Erwerb von Stueckaktien ueber Boerse",
     "Ueberschreitung der 3-%-Schwelle durch Index-Track-Investmentfonds."),
    ("010", "22. November 2022",  "DWS Investment GmbH",                         "Mainzer Landstraße 11-17, 60329 Frankfurt am Main, DE",
     "4,82", "5,01", "5 % (§ 33 Abs. 1 WpHG)", "Erwerb ueber Aktienemission (Kapitalerhoehung Mai 2022)",
     "Ueberschreitung der 5-%-Schwelle nach Zuteilung aus der Kapitalerhoehung 2022."),
    ("011", "14. Februar 2023",   "Allianz Global Investors GmbH",               "Bockenheimer Landstr. 42-44, 60323 Frankfurt am Main, DE",
     "2,97", "3,18", "3 % (§ 33 Abs. 1 WpHG)", "Erwerb von Stueckaktien ueber Boerse",
     "Aufstockung im Rahmen der Strategie ESG-EU-Industrials."),
    ("017", "12. Juli 2023",      "Norges Bank (Government Pension Fund Global)","Bankplassen 2, 0151 Oslo, Norwegen",
     "4,98", "5,12", "5 % (§ 33 Abs. 1 WpHG)", "Erwerb ueber Boerse XETRA",
     "Ueberschreitung der 5-%-Schwelle durch Norwegian SWF im Rahmen der Index-Replikation."),
]
for args in BET:
    no = args[0]
    t, s = beteiligungsmeldung(*args)
    JOBS.append((f"REA_Beteiligungsmeldung_2022_002.docx" if no == "002" else
                 f"REA_Beteiligungsmeldung_2022_004.docx" if no == "004" else
                 f"REA_Beteiligungsmeldung_2022_010.docx" if no == "010" else
                 f"REA_Beteiligungsmeldung_2023_011.docx" if no == "011" else
                 f"REA_Beteiligungsmeldung_2023_017.docx",
                 H_CM, t, s, False))

# Directors' Dealings (5)
DD = [
    ("006", "06. Juli 2022",      "Anna Mueller",         "Vorstandsvorsitzende (CEO)",          "Kauf von Stueckaktien",          5000, 26.40),
    ("012", "11. November 2022",  "Laura Bauer",          "Vorstand Finanzen (CFO)",             "Kauf von Stueckaktien",          2500, 22.85),
    ("016", "08. Dezember 2022",  "Dr. Klaus Steinbrueck","Aufsichtsratsvorsitz",                "Kauf von Stueckaktien",          1500, 23.10),
    ("018", "20. Dezember 2022",  "Dr. Thomas Weber",     "Vorstand Operations (COO)",           "Kauf von Stueckaktien",          1200, 23.95),
    ("007", "03. Maerz 2023",     "Stefan Richter",       "Vorstand CMO/BD",                     "Kauf von Stueckaktien (Erstdotierung)", 4200, 27.60),
]
for args in DD:
    no = args[0]
    t, s = directors_dealing(*args)
    fn = (f"REA_Directors_Dealing_2022_006.docx" if no == "006" else
          f"REA_Directors_Dealing_2022_012.docx" if no == "012" else
          f"REA_Directors_Dealing_2022_016.docx" if no == "016" else
          f"REA_Directors_Dealing_2022_018.docx" if no == "018" else
          f"REA_Directors_Dealing_2023_007.docx")
    JOBS.append((fn, H_CM, t, s, True))

# WpHG-Meldungen (4)
WPHG = [
    ("008", "14. September 2022", "Capital Research and Management Company", "333 South Hope Street, Los Angeles, CA, USA", "4,87", "5,02"),
    ("014", "12. Dezember 2022",  "Fidelity Management & Research Company",  "245 Summer Street, Boston, MA, USA",          "2,94", "3,11"),
    ("009", "21. Maerz 2023",     "Union Investment Privatfonds GmbH",       "Weißfrauenstr. 7, 60311 Frankfurt am Main",   "2,98", "3,21"),
    ("013", "18. Mai 2023",       "Deka Investment GmbH",                    "Mainzer Landstr. 16, 60325 Frankfurt am Main","9,87","10,12"),
]
for args in WPHG:
    no = args[0]
    t, s = wphg_meldung(*args)
    fn = (f"REA_WpHG_Meldung_2022_008.docx" if no == "008" else
          f"REA_WpHG_Meldung_2022_014.docx" if no == "014" else
          f"REA_WpHG_Meldung_2023_009.docx" if no == "009" else
          f"REA_WpHG_Meldung_2023_013.docx")
    JOBS.append((fn, H_CM, t, s, False))

# Short Selling Meldungen (6)
SS = [
    ("020", "07. Januar 2022",  "Marshall Wace LLP",            "George House, 131 Sloane Street, London SW1X 9AT, UK",   "0,48", "0,52"),
    ("001", "12. Januar 2023",  "AQR Capital Management LLC",   "Two Greenwich Plaza, Greenwich, CT 06830, USA",          "0,49", "0,61"),
    ("003", "20. Februar 2023", "Citadel Advisors LLC",         "131 South Dearborn Street, Chicago, IL 60603, USA",      "0,52", "0,68"),
    ("005", "14. Maerz 2023",   "BlackRock Investment Management(UK) Ltd","12 Throgmorton Avenue, London EC2N 2DL, UK",  "0,54", "0,42"),
    ("015", "22. Juli 2023",    "GLG Partners LP",              "1 Curzon Street, London W1J 5HB, UK",                    "0,51", "0,73"),
    ("019", "05. September 2023","WorldQuant LLC",              "1700 East Putnam Avenue, Old Greenwich, CT 06870, USA",  "0,49", "0,55"),
]
for args in SS:
    no = args[0]
    t, s = short_selling(*args)
    fn = (f"REA_Short_Selling_Meldung_2022_020.docx" if no == "020" else
          f"REA_Short_Selling_Meldung_2023_001.docx" if no == "001" else
          f"REA_Short_Selling_Meldung_2023_003.docx" if no == "003" else
          f"REA_Short_Selling_Meldung_2023_005.docx" if no == "005" else
          f"REA_Short_Selling_Meldung_2023_015.docx" if no == "015" else
          f"REA_Short_Selling_Meldung_2023_019.docx")
    JOBS.append((fn, H_CM, t, s, False))

# Misplaced / non-IR docs (9)
t, s, c = qbr_continental()
JOBS.append(("REA_CON_BMS-12_QBR_2023_Q1.docx", H, t, s, c))

t, s, c = kpmg_management_letter_rpl()
JOBS.append(("RPL_WP_Management_Letter_2021.docx", H_KPMG, t, s, c))

t, s, c = bmw_eskalation()
JOBS.append(("REA_BMW_Eskalationsbrief_Lieferengpass_2022.docx", H, t, s, c))

t, s, c = konzernrichtlinie_einkauf()
JOBS.append(("Konzernrichtlinie_Einkauf_2023.docx", H, t, s, c))

t, s, c = patent_antwort()
JOBS.append(("Patent_03_Antwort_Anmelder_2023.docx", H, t, s, c))

t, s, c = rcz_ic_rechnung()
JOBS.append(("RCZ_IC_Rechnung_2022_12.docx", H_RCZ, t, s, c))

t, s, c = reg_to_rsg_ic()
JOBS.append(("REG_to_RSG_IC_2022_03.docx", H_REG, t, s, c))

t, s, c = ppap_mbz()
JOBS.append(("PPAP_MBZ_ADAS-V4D_2022_Level3.docx", H, t, s, c))

t, s, c = prj_status_adas()
JOBS.append(("PRJ-2021-002_Status_2023_03_ADAS-V4D_Kalibr.docx", H, t, s, c))


def main():
    written = 0
    for fname, header, title, sections, confidential in JOBS:
        path = BASE / fname
        write_doc(path, header, title, sections, confidential=confidential)
        written += 1
    print(f"Wrote {written} docs.")


if __name__ == "__main__":
    main()
