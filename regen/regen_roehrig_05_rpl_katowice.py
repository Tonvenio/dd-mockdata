"""Brennhagen AG / 05_Tochter_PL_Katowice (RPL = Brennhagen Polska Sp. z o.o.) – 98 thin docs.

Polish jurisdiction. Werkleiter Marek Wojciechowski, HR Anna Kowalska.
Mock data with Polish-specific elements (KRS, ZUS, NIP, PLN).
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
from enhance_lib import ROEHRIG_AG as R, ROEHRIG_SUBS as S, write_doc, signatures

BASE = f"{_ROOT}/roehrig_large/05_Tochter_PL_Katowice"

# Local Polish entity header – use RPL identity, not REA holding
RPL = S["RPL"]
RPL_ADDR = "ul. Roozdzienskiego 188, 40-203 Katowice, Polen"
RPL_KRS = "KRS 0000543210, Sad Rejonowy Katowice-Wschod"
RPL_NIP = "PL 634-287-91-04"
RPL_REGON = "367281904"

H_RPL = {"name": RPL["name"], "addr": RPL_ADDR, "hrb": RPL_KRS}
H_REA = {"name": R["name"], "addr": R["addr"], "hrb": R["hrb"]}


# ─────────────────────────────────────────────────────────────────────────────
# 1) Arbeitsvertraege Polska (4 + 1 leftover AV_065)
# ─────────────────────────────────────────────────────────────────────────────

def av_polska(fname, ord_nr, position_de, position_pl, name, gehalt_eur,
              urlaub, bonus_pct, befristung="unbefristet", abt="Werksleitung"):
    sections = [
        ("Vertragsparteien",
         f"Zwischen\n\n{RPL['name']}, {RPL_ADDR}, eingetragen im Krajowy Rejestr Sadowy "
         f"({RPL_KRS}), NIP {RPL_NIP}, REGON {RPL_REGON}, vertreten durch den Geschaeftsfuehrer "
         f"Marek Wojciechowski (Werkleiter / Dyrektor Zakladu)\n\n"
         f"– nachfolgend »Arbeitgeber« bzw. »Pracodawca« –\n\n"
         f"und\n\n{name}, wohnhaft in Katowice / Powiat Katowicki, Polen\n\n"
         f"– nachfolgend »Arbeitnehmer/in« bzw. »Pracownik« –\n\n"
         f"wird folgender Arbeitsvertrag (umowa o prace) nach polnischem Arbeitsrecht "
         f"(Kodeks pracy, Dz.U. 1974 Nr. 24, Pos. 141) geschlossen."),
        ("§ 1 Taetigkeit / Stanowisko",
         f"(1) Der/Die Arbeitnehmer/in wird als {position_de} (poln. {position_pl}) "
         f"in der Abteilung {abt} der {RPL['name']}, Werk Katowice, angestellt.\n\n"
         f"(2) Dienstort: Katowice, Polen (ul. Roozdzienskiego 188). Aenderungen des "
         f"Dienstortes innerhalb der Wojewodschaft Slaskie bleiben dem Arbeitgeber vorbehalten.\n\n"
         f"(3) Disziplinarisch und fachlich berichtet der/die Arbeitnehmer/in an den Werkleiter "
         f"Marek Wojciechowski. Funktional bestehen Berichtspflichten gegenueber den fachlich "
         f"zustaendigen Konzernfunktionen (HR / Finance / Operations) der Brennhagen Elektronik AG "
         f"in Stuttgart."),
        ("§ 2 Vertragsbeginn und Vertragsdauer",
         f"(1) Das Arbeitsverhaeltnis beginnt am 1. Januar 2022 und wird {befristung} geschlossen.\n\n"
         f"(2) Die Probezeit (okres probny) betraegt 3 Monate gemaess Art. 25 (2) Kodeks pracy. "
         f"Waehrend der Probezeit gilt eine Kuendigungsfrist von 2 Wochen.\n\n"
         f"(3) Nach der Probezeit gelten die gesetzlichen Kuendigungsfristen nach Art. 36 Kodeks "
         f"pracy (1, 3 oder 3 Monate, je nach Beschaeftigungsdauer)."),
        ("§ 3 Verguetung / Wynagrodzenie",
         f"(1) Das monatliche Bruttogehalt (wynagrodzenie miesieczne brutto) betraegt "
         f"EUR {gehalt_eur:,} (entsprechend ca. PLN {gehalt_eur*4.55:,.0f} zum Referenzkurs der "
         f"Narodowy Bank Polski (NBP), Stand Vertragsschluss). Die Auszahlung erfolgt monatlich "
         f"nachtraeglich bis zum 10. Tag des Folgemonats auf das vom/von der Arbeitnehmer/in "
         f"benannte Konto in Polen.\n\n"
         f"(2) Zusaetzlich erhaelt der/die Arbeitnehmer/in eine jaehrliche variable Verguetung "
         f"(premia roczna) von bis zu {bonus_pct} % des Bruttojahresgehalts bei voller Zielerreichung. "
         f"Zielvereinbarung erfolgt jaehrlich bis 31.03. (Werks-OEE >= 78 %, Ausschussquote <= 0,8 %, "
         f"Liefertreue >= 96 %, Konzern-EBIT-Beitrag).\n\n"
         f"(3) Sozialversicherungsbeitraege werden gemaess polnischem Sozialversicherungsrecht "
         f"abgefuehrt: ZUS-Beitraege (Zaklad Ubezpieczen Spolecznych) Renten- (19,52 %), Kranken- "
         f"(2,45 %), Unfall- (1,67 %) und Arbeitslosenversicherung sowie Krankenkassenbeitrag NFZ "
         f"(9 %). Lohnsteuer (PIT) nach polnischem Tarif.\n\n"
         f"(4) Der/Die Arbeitnehmer/in nimmt am Konzern-Aktienprogramm der Brennhagen Elektronik AG "
         f"(LTI 2022) ab Position-Level L4 teil; Details regelt der LTI-Anhang.")
        ,
        ("§ 4 Arbeitszeit / Czas pracy",
         f"(1) Die regulaere woechentliche Arbeitszeit betraegt 40 Stunden, verteilt auf Montag "
         f"bis Freitag (8 h taeglich) gemaess Art. 129 Kodeks pracy. Beginn 07:00 Uhr, Ende 15:30 "
         f"Uhr (inkl. 30 min Pause). Im Schichtbetrieb gelten die Werks-Schichtplaene.\n\n"
         f"(2) Mehrarbeit (praca w godzinach nadliczbowych) ist im Rahmen der gesetzlichen Grenzen "
         f"(150 h/Jahr) zulaessig und wird gemaess Art. 151{chr(0x00B9)} Kodeks pracy mit Zuschlaegen "
         f"verguetet bzw. durch Freizeit ausgeglichen.\n\n"
         f"(3) Reisezeiten zu Konzerngesellschaften (Stuttgart, Heilbronn, Brno, Gyor) gelten "
         f"als Arbeitszeit im gesetzlichen Rahmen."),
        ("§ 5 Urlaub / Urlop",
         f"(1) Der Jahresurlaub (urlop wypoczynkowy) betraegt {urlaub} Arbeitstage gemaess "
         f"Art. 154 Kodeks pracy (gesetzlich 26 Tage bei >= 10 Jahren Berufserfahrung).\n\n"
         f"(2) Urlaubsplanung erfolgt im Urlaubsplan (plan urlopow) bis 31.01. des Kalenderjahres "
         f"in Abstimmung mit dem Werkleiter und dem Betriebsrat (Rada Pracownikow).\n\n"
         f"(3) Sonderurlaub fuer familiaere Ereignisse (Heirat, Geburt, Sterbefall) gemaess "
         f"Verordnung des Arbeitsministeriums vom 15.05.1996."),
        ("§ 6 Geheimhaltung / Tajemnica przedsiebiorstwa",
         f"(1) Der/Die Arbeitnehmer/in verpflichtet sich, alle Betriebs- und Geschaeftsgeheimnisse "
         f"der {RPL['name']} und des Brennhagen-Konzerns (insb. Konstruktionsunterlagen, Prozessparameter "
         f"SMD-Linien, Kunden- und Lieferantenkonditionen, Preiskalkulationen, OEM-Spezifikationen "
         f"BMW/VW/Mercedes/Stellantis) sowohl waehrend als auch nach Beendigung des Arbeitsverhaeltnisses "
         f"streng vertraulich zu behandeln.\n\n"
         f"(2) Die Pflicht zur Geheimhaltung richtet sich nach Ustawa o zwalczaniu nieuczciwej "
         f"konkurencji vom 16.04.1993 (Gesetz gegen unlauteren Wettbewerb, Art. 11) sowie nach "
         f"den ergaenzenden Konzern-Compliance-Richtlinien (Code of Conduct Brennhagen Elektronik AG)."),
        ("§ 7 Nachvertragliches Wettbewerbsverbot / Zakaz konkurencji po ustaniu",
         f"(1) Nach Beendigung des Arbeitsverhaeltnisses gilt ein Wettbewerbsverbot von 12 Monaten "
         f"im Bereich Automotive Electronics / EMS / SMD-Fertigung. Geographischer Geltungsbereich: "
         f"Polen, Tschechien, Slowakei, Ungarn, Deutschland.\n\n"
         f"(2) Als Karenzentschaedigung (odszkodowanie) erhaelt der/die Arbeitnehmer/in gemaess "
         f"Art. 101{chr(0x00B2)} Kodeks pracy 25 % des zuletzt bezogenen Gehaltes ueber die Dauer "
         f"des Verbots, zahlbar monatlich.\n\n"
         f"(3) Eine schriftliche Vereinbarung nach Art. 101{chr(0x00B2)} § 1 Kodeks pracy liegt "
         f"diesem Vertrag als Anhang A bei."),
        ("§ 8 Compliance / Datenschutz",
         f"(1) Der/Die Arbeitnehmer/in haelt die Konzern-Compliance-Richtlinien ein (Code of "
         f"Conduct, Antikorruptionsrichtlinie, IATF 16949 Q-Anforderungen, Exportkontrolle).\n\n"
         f"(2) Die Verarbeitung personenbezogener Daten richtet sich nach DSGVO/RODO (Rozporzadzenie "
         f"Ogolne o Ochronie Danych Osobowych) sowie nach dem polnischen Datenschutzgesetz vom "
         f"10.05.2018 (Dz.U. 2018 Pos. 1000)."),
        ("§ 9 Anwendbares Recht und Gerichtsstand",
         f"(1) Auf diesen Vertrag findet polnisches Recht Anwendung.\n\n"
         f"(2) Ausschliesslicher Gerichtsstand fuer alle Streitigkeiten aus diesem Vertrag ist "
         f"das Sad Rejonowy Katowice-Zachod / Wydzial Pracy.\n\n"
         f"(3) Sollte eine Bestimmung dieses Vertrages unwirksam sein, beruehrt dies die Gueltigkeit "
         f"der uebrigen Bestimmungen nicht. Aenderungen beduerfen der Schriftform."),
        ("Unterschriften / Podpisy",
         signatures("Marek Wojciechowski", "Werkleiter / Dyrektor Zakladu", RPL["name"],
                    name, position_de, "Arbeitnehmer/in",
                    place="Katowice", date_str_="15. Dezember 2021")),
    ]
    write_doc(f"{BASE}/{fname}", H_RPL,
              f"Anstellungsvertrag / Umowa o prace – {position_de}",
              subtitle=f"Vertragsnummer RPL-AV-{ord_nr}-2022 / {position_pl}",
              sections=sections, draft=False)


av_polska("RPL_Arbeitsvertrag_01_Geschäftsführer_in_R_2022.docx", "01",
          "Geschaeftsfuehrer (Dyrektor Zakladu)", "Dyrektor Generalny",
          "Marek Wojciechowski", 9000, 30, 35, abt="Werksleitung")
av_polska("RPL_Arbeitsvertrag_02_Produktionsleiter_in_2022_20230915.docx", "02",
          "Produktionsleiter/in", "Kierownik Produkcji",
          "Krzysztof Nowak", 5400, 26, 22, abt="Produktion EMS/SMD")
av_polska("RPL_Arbeitsvertrag_04_Finanzcontroller_Kat_2022.docx", "04",
          "Finanzcontroller/in Katowice", "Kontroler Finansowy",
          "Magdalena Lewandowska", 4200, 26, 18, abt="Finanzen/Controlling")
av_polska("RPL_Arbeitsvertrag_05_HR-Manager_Katowice_2022.docx", "05",
          "HR-Manager/in Katowice", "Kierownik HR / Dyrektor Personalny",
          "Anna Kowalska", 4500, 26, 18, abt="Personalwesen / HR")


# AV_065 – leftover Konzern-AV in PL folder (filename realism)
write_doc(f"{BASE}/AV_065_Stefan_Hoffmann_65_VP_Engineering.docx", H_REA,
          "Aenderungsvereinbarung zum Anstellungsvertrag – Stefan Hoffmann (VP Engineering)",
          subtitle="Vertragsnummer AV-065-2018 (Aenderung Nr. 3 v. 12. Maerz 2024)",
          sections=[
              ("Vertragsparteien",
               f"Zwischen der {R['name']}, {R['addr']}, eingetragen im Handelsregister "
               f"{R['hrb']}, vertreten durch die Vorstandsvorsitzende Anna Mueller (CEO) "
               f"und die Chief Financial Officer Laura Bauer (CFO),\n\n"
               f"– nachfolgend »Gesellschaft« –\n\n"
               f"und Herrn Stefan Hoffmann, wohnhaft Stuttgart,\n\n"
               f"– nachfolgend »Arbeitnehmer« –\n\n"
               f"wird zur Bereinigung von Doppelablage in der Datenraum-Struktur (Folder 05 RPL) "
               f"festgestellt: Dieses Dokument betrifft die deutsche Holding-Ebene, nicht die "
               f"polnische Tochter, und wird in der dataroom-Indexrevision in den korrekten "
               f"Personalakten-Ordner verschoben."),
              ("Hintergrund",
               "Herr Stefan Hoffmann war bis 30. Juni 2024 Chief Technology Officer (CTO) der "
               "Brennhagen Elektronik AG (Vorstandsbestellung gemaess REA-Vorstand-Bestellungsvertrag "
               "v. 01.07.2018). Mit Wirkung zum 1. Juli 2024 wechselt Herr Hoffmann auf eigenen "
               "Wunsch in die operative Funktion Vice President Engineering (VP Engineering) der "
               "Brennhagen Elektronik AG mit fachlicher Verantwortung fuer die Plattform-Roadmap "
               "ICP-3 / BMS-12 / ADAS-V4D ueber die Werke Heilbronn, Muenchen, Katowice, Brno, "
               "Gyor und Shanghai hinweg."),
              ("§ 1 Neue Funktion und Berichtsweg",
               "(1) Herr Hoffmann uebernimmt mit Wirkung zum 1. Juli 2024 die Funktion »Vice "
               "President Engineering« mit direkter Berichtspflicht an die neue CTO Dr. Petra "
               "Hollmann.\n\n"
               "(2) Die Verantwortlichkeit umfasst Architektur- und Plattformentscheidungen fuer "
               "Embedded Systems der Konzernprodukte, Schnittstelle zu RSG Muenchen (Lead "
               "Developer Lars Wittmann) sowie technische Eskalationsinstanz fuer die EMS-Werke."),
              ("§ 2 Verguetung",
               "(1) Das Bruttojahresgehalt betraegt ab 1. Juli 2024 EUR 320.000 zzgl. "
               "Tantieme bis zu 60 % bei voller Zielerreichung.\n\n"
               "(2) Bestehende LTI-Tranchen 2022 und 2023 laufen vereinbarungsgemaess weiter; "
               "Neuzuteilungen erfolgen ab Tarif Level L1 (VP)."),
              ("§ 3 Sonstige Bedingungen",
               "(1) Im Uebrigen bleibt der Anstellungsvertrag v. 01.07.2018 nebst Aenderungen 1 "
               "(2020) und 2 (2022) unveraendert.\n\n"
               "(2) Wettbewerbsverbot, Geheimhaltung und Compliance-Pflichten gelten fort.\n\n"
               "(3) Diese Aenderung tritt mit Unterzeichnung in Kraft."),
              ("Unterschriften",
               signatures("Anna Mueller", "CEO", R["name"],
                          "Stefan Hoffmann", "VP Engineering (ab 1.7.2024)", R["name"],
                          place="Stuttgart", date_str_="12. Maerz 2024")),
          ])


# ─────────────────────────────────────────────────────────────────────────────
# 2) RPL_IC_Quartalsbericht_* (7 docs, 2019-Q1..2020-Q4) – PL→DE intercompany
# ─────────────────────────────────────────────────────────────────────────────

QUARTAL_DATA = {
    ("2019", "Q1"): (21.8, 1.92, 18.4, 940, 78.2, 0.91, 96.4, "ENTWURF"),
    ("2019", "Q3"): (24.1, 2.21, 19.6, 945, 79.0, 0.84, 96.8, ""),
    ("2019", "Q4"): (25.6, 2.40, 20.8, 950, 79.4, 0.82, 97.0, ""),
    ("2020", "Q1"): (22.4, 1.78, 17.9, 935, 76.1, 0.95, 95.2, ""),  # COVID
    ("2020", "Q2"): (18.9, 1.21, 14.2, 920, 71.4, 1.18, 92.8, ""),  # COVID deep
    ("2020", "Q3"): (23.7, 2.05, 19.1, 940, 77.8, 0.88, 96.1, ""),
    ("2020", "Q4"): (26.2, 2.48, 21.3, 952, 79.6, 0.81, 97.2, ""),
}


def ic_quartal(fname, jahr, quartal, ums_mio, ebit_mio, ic_invoice_mio, mas,
               oee, ausschuss, liefertreue, status):
    is_draft = (status == "ENTWURF")
    sections = [
        ("Zusammenfassung / Executive Summary",
         f"Die Brennhagen Polska Sp. z o.o. (RPL), Werk Katowice, berichtet fuer das "
         f"{quartal} {jahr} an die Konzernmuttergesellschaft Brennhagen Elektronik AG (REA), "
         f"Stuttgart, sowie die Zwischenholding Brennhagen Holding GmbH (RHO). Der vorliegende "
         f"Bericht dokumentiert die intercompany-relevanten Geschaeftsvorfaelle zwischen "
         f"RPL und REG (Brennhagen Elektronik GmbH, Heilbronn) sowie den Konzernumlagen.\n\n"
         f"Im Berichtszeitraum wurden Umsatzerloese in Hoehe von {ums_mio:.1f} Mio. EUR "
         f"(davon {ic_invoice_mio:.1f} Mio. EUR Intercompany-Lieferungen an REG) und ein "
         f"EBIT von {ebit_mio:.2f} Mio. EUR erzielt. Headcount: {mas} Mitarbeiter (FTE)."),
        ("Verrechnung mit REG Heilbronn",
         f"Die Intercompany-Verrechnung zwischen RPL und REG erfolgt nach der konzernweiten "
         f"Verrechnungspreisrichtlinie (TP-Richtlinie 2018, ueberarbeitet 2022) auf Basis "
         f"der Transactional Net Margin Method (TNMM) mit einer Ziel-Routinemarge von 4,5 % "
         f"auf vollkostenbezogene Herstellungskosten (Cost-Plus). Quartalsergebnis: "
         f"Routinemarge ca. {(ebit_mio/ums_mio*100):.1f} %.\n\n"
         f"Die intercompany-Lieferungen umfassten im Berichtsquartal hauptsaechlich die "
         f"Produktfamilien ICP-3 (Infotainment-Module), ECU-900 (Powertrain-ECU) sowie "
         f"Vorbaugruppen fuer ADAS-V4D. Bezahlung in EUR, Zahlungsziel 60 Tage netto. "
         f"Forderungen gegenueber REG zum Quartalsende: ca. {ic_invoice_mio*0.62:.1f} Mio. EUR."),
        ("Operative Kennzahlen / Operational KPI",
         [
             ["KPI", "Ist", "Ziel", "Bemerkung"],
             ["OEE Gesamtwerk (8 SMD-Linien)", f"{oee:.1f} %", ">= 78,0 %",
              "Bestperformance Linie 5/6"],
             ["Ausschussquote (PPM)", f"{ausschuss:.2f} %", "<= 0,80 %",
              "Top-Defekte: Solder-Bridge, Tombstone"],
             ["Liefertreue OTIF", f"{liefertreue:.1f} %", ">= 96,0 %",
              "Verzoegerungen v. a. RM-Komponenten (Chip-Shortage)"],
             ["Headcount FTE", f"{mas}", "950 (Plan)", "Plan +/- 1 %"],
             ["Krankheitsstand", "3,8 %", "<= 4,0 %", "Saisonale Effekte Q1/Q4"],
             ["Energie kWh / Produkt", "1,84", "<= 1,90", "ISO 50001 Massnahmen wirksam"],
         ]),
        ("Sozialversicherung / ZUS-Beitraege",
         f"Quartalsbeitraege ZUS (Zaklad Ubezpieczen Spolecznych): ca. PLN 18,6 Mio. "
         f"(Arbeitgeberanteil) und PLN 4,2 Mio. (Arbeitnehmeranteil, abgefuehrt). NFZ-Beitraege "
         f"PLN 3,1 Mio. PIT-Lohnsteuer PLN 2,8 Mio. Saemtliche Meldungen ZUS DRA / DPA fristgerecht "
         f"abgegeben. Keine Korrekturmeldungen erforderlich."),
        ("Personalentwicklung",
         f"Anzahl Mitarbeiter (Stichtag Quartalsende): {mas} FTE. Veraenderungen im Berichtsquartal: "
         f"Einstellungen +14 (Schwerpunkt SMD-Operator/in, Q-Inspektor/in), Abgaenge -8 (davon "
         f"3 Renteneintritte, 5 Eigenkuendigungen). Fluktuationsrate ann. 8,2 %. Schulungen: "
         f"4.180 Schulungsstunden (IATF 16949, ESD, 5S, Lean Production)."),
        ("Risiken / Ausblick",
         f"Wesentliche Risiken im Berichtszeitraum: (i) anhaltende Lieferengpaesse bei "
         f"Halbleitern (insb. NXP, Infineon), (ii) EUR/PLN-Volatilitaet (Hedging-Quote "
         f"82 %), (iii) Strompreisentwicklung Polen / Tauron. Mitigation: Dual-Sourcing-"
         f"Strategie Komponenten, FX-Hedging ueber Konzern-Treasury (M. Pflanzer), "
         f"PPA-Vertrag Tauron Polska Energia (verlaengert bis 2024).\n\n"
         f"Status Bericht: {status if status else 'final freigegeben'}."),
        ("Freigabe",
         signatures("Magdalena Lewandowska", "Finanzcontrollerin RPL", RPL["name"],
                    "Marek Wojciechowski", "Werkleiter RPL", RPL["name"],
                    place="Katowice", date_str_=f"15. {['', 'Januar','April','Juli','Oktober'][int(quartal[1])]+'/' if False else ''}"
                    + ['', 'April', 'Juli', 'Oktober', 'Januar'][int(quartal[1])]
                    + f" {jahr if int(quartal[1])<4 else int(jahr)+1}")),
    ]
    write_doc(f"{BASE}/{fname}", H_RPL,
              f"Intercompany-Quartalsbericht {quartal} {jahr} – {RPL['name']}",
              subtitle=f"Bericht an Konzernmutter Brennhagen Elektronik AG, Stuttgart",
              sections=sections, draft=is_draft)


for (yr, q), data in QUARTAL_DATA.items():
    ums, ebit, ic, mas, oee, ausschuss, lt, status = data
    if yr == "2019" and q == "Q1":
        fname = "RPL_IC_Quartalsbericht_2019_Q1_ENTWURF.docx"
    elif yr == "2020" and q == "Q2":
        fname = "RPL_IC_Quartalsbericht_2020_Q2_v2.docx"
    else:
        fname = f"RPL_IC_Quartalsbericht_{yr}_{q}.docx"
    ic_quartal(fname, yr, q, ums, ebit, ic, mas, oee, ausschuss, lt, status)


# ─────────────────────────────────────────────────────────────────────────────
# 3) RPL_IC_Rechnung_* (32 docs) – RPL → REG monthly intercompany invoices
# ─────────────────────────────────────────────────────────────────────────────

MONTHS_DE = ["", "Januar", "Februar", "Maerz", "April", "Mai", "Juni",
             "Juli", "August", "September", "Oktober", "November", "Dezember"]


def ic_rechnung(fname, jahr, monat, betrag_eur, wip=False, status="final"):
    monat_int = int(monat)
    rgnr = f"RPL-IC-{jahr}-{monat:02d}"
    products = [
        ("ICP-3 Sub-Assy LRR-71", 18400, 14.50, "BG-ICP3-S-002"),
        ("ECU-900 PCBA bestueckt", 12200, 22.80, "BG-ECU900-PCBA-A"),
        ("ADAS-V4D Front-End Modul", 4800, 78.20, "BG-ADASV4D-FE-01"),
        ("LightCtrl-7 PCBA", 9600, 18.40, "BG-LC7-PCBA-02"),
        ("Werkzeug-/Pruefkostenumlage", 1, 4200, "WZG-Q-2023"),
    ]
    rows = [["Pos", "Artikel-Nr.", "Beschreibung", "Menge", "EP (EUR)", "Betrag (EUR)"]]
    summe = 0.0
    for i, (desc, qty, ep, art) in enumerate(products[:4], 1):
        amt = qty * ep
        summe += amt
        rows.append([str(i), art, desc, f"{qty:,}".replace(",", "."),
                     f"{ep:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                     f"{amt:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")])
    # Adjust to target
    adj = betrag_eur - summe
    rows.append(["5", "WZG-Q-PROZESS", "Werkzeug- und Pruefmittelumlage (anteilig)",
                 "1", f"{adj:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                 f"{adj:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")])
    rows.append(["", "", "Nettobetrag", "", "", f"{betrag_eur:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")])

    sections = [
        ("Rechnungsstellerin / Wystawca faktury",
         f"{RPL['name']}\n{RPL_ADDR}\nKRS {RPL_KRS}\nNIP {RPL_NIP}, REGON {RPL_REGON}\n"
         f"Bankverbindung: PKO Bank Polski S.A., IBAN PL27 1020 2313 0000 3102 0512 9876, BIC BPKOPLPW\n"
         f"Vertretungsberechtigt: Marek Wojciechowski (Dyrektor Zakladu)"),
        ("Rechnungsempfaengerin / Odbiorca",
         f"Brennhagen Elektronik GmbH (REG)\nGottlieb-Daimler-Strasse 24, 74172 Neckarsulm-Heilbronn\n"
         f"HRB 221456, Amtsgericht Heilbronn\nUSt-IdNr. DE 287 645 109\n"
         f"Ansprechpartner: Finance-Team REG (sap-id 412)"),
        ("Rechnungsangaben",
         f"Rechnungsnummer: {rgnr}\nRechnungsdatum: 28. {MONTHS_DE[monat_int]} {jahr}\n"
         f"Leistungszeitraum: 1.–{['','31','28','31','30','31','30','31','31','30','31','30','31'][monat_int]}. "
         f"{MONTHS_DE[monat_int]} {jahr}\nWaehrung: EUR (gemaess IC-Rahmenvertrag REA-IC-2018)\n"
         f"Zahlungsziel: 60 Tage netto, Faelligkeit ca. {MONTHS_DE[(monat_int%12)+1]} {jahr if monat_int<11 else int(jahr)+1}\n"
         f"Bestellbezug: REG-PO-{jahr}-{monat:02d} (Rahmen-Liefervereinbarung)\n"
         f"Verrechnungsbasis: Transferpreisrichtlinie 2018 (TNMM, Cost-Plus 4,5 %)"),
        ("Leistungsbeschreibung / Specification of services",
         rows),
        ("Umsatzsteuerliche Behandlung",
         f"Innergemeinschaftliche Lieferung (B2B) gemaess Art. 138 MwStSystRL. Steuerfreie "
         f"Lieferung in einen anderen EU-Mitgliedstaat (Deutschland). USt-IdNr. Lieferant: "
         f"PL 634-287-91-04; USt-IdNr. Empfaenger: DE 287 645 109. Reverse-Charge-Verfahren. "
         f"Belegnachweis (Versandpapiere CMR Nr. CMR-{rgnr}) und Buchnachweis liegen vor. "
         f"Meldung INTRASTAT erfolgt monatlich an GUS (Glowny Urzad Statystyczny).\n\n"
         f"Status: {status}. "
         + ("Dieser Beleg ist als WIP (Entwurf) gekennzeichnet und beduerftiger formaler Freigabe "
            "durch das Finanzcontrolling RPL (M. Lewandowska)." if wip else
            "Freigegeben durch Finanzcontrolling RPL (M. Lewandowska, " +
            f"{['',2,1,1,2,2,3,3,3,4,4,4,4][monat_int]}. " +
            f"{MONTHS_DE[(monat_int%12)+1] if monat_int<12 else 'Januar'} {jahr if monat_int<11 else int(jahr)+1}).")),
        ("Hinweise",
         f"Rechnung erstellt auf Basis Rahmenliefervertrag REA-IC-RPL-REG-2018. Streitigkeiten "
         f"werden gemaess Schiedsklausel (DIS Frankfurt) beigelegt. Eine Kopie geht an Group "
         f"Treasury (M. Pflanzer) und Group Tax (Dr. H. Berger). Buchung erfolgt in SAP S/4HANA "
         f"unter Belegart RV / Buchungskreis PL10."),
    ]
    write_doc(f"{BASE}/{fname}", H_RPL,
              f"IC-Rechnung Nr. {rgnr} – Lieferungen {MONTHS_DE[monat_int]} {jahr}",
              subtitle=f"Brennhagen Polska Sp. z o.o. → Brennhagen Elektronik GmbH",
              sections=sections, draft=wip)


# Generate the IC_Rechnung files (these are "received invoices" in the RPL folder)
IC_RECH = [
    ("RPL_IC_Rechnung_2020_02.docx", 2020, 2, 1_184_000, False, "final"),
    ("RPL_IC_Rechnung_2020_03.docx", 2020, 3, 1_096_500, False, "final"),
    ("RPL_IC_Rechnung_2020_04.docx", 2020, 4, 842_300, False, "final"),
    ("RPL_IC_Rechnung_2020_05.docx", 2020, 5, 798_200, False, "final"),
    ("RPL_IC_Rechnung_2020_06.docx", 2020, 6, 921_100, False, "final"),
    ("RPL_IC_Rechnung_2020_07.docx", 2020, 7, 1_038_400, False, "final"),
    ("RPL_IC_Rechnung_2020_09.docx", 2020, 9, 1_142_700, False, "final"),
    ("RPL_IC_Rechnung_2020_10.docx", 2020, 10, 1_198_300, False, "final"),
    ("RPL_IC_Rechnung_2020_11.docx", 2020, 11, 1_224_900, False, "final"),
    ("RPL_IC_Rechnung_2020_12.docx", 2020, 12, 1_287_500, False, "final"),
    ("RPL_IC_Rechnung_2021_01.docx", 2021, 1, 1_312_800, False, "final"),
    ("RPL_IC_Rechnung_2021_02.docx", 2021, 2, 1_268_400, False, "final"),
    ("RPL_IC_Rechnung_2021_03.docx", 2021, 3, 1_354_200, False, "final"),
    ("RPL_IC_Rechnung_2021_04.docx", 2021, 4, 1_298_700, False, "final"),
    ("RPL_IC_Rechnung_2021_05_FINAL.docx", 2021, 5, 1_341_900, False, "final/freigegeben"),
    ("RPL_IC_Rechnung_2021_07.docx", 2021, 7, 1_378_500, False, "final"),
    ("RPL_IC_Rechnung_2021_08.docx", 2021, 8, 1_402_300, False, "final"),
    ("RPL_IC_Rechnung_2021_09.docx", 2021, 9, 1_419_600, False, "final"),
    ("RPL_IC_Rechnung_2021_10.docx", 2021, 10, 1_438_100, False, "final"),
    ("RPL_IC_Rechnung_2021_11.docx", 2021, 11, 1_462_800, False, "final"),
    ("RPL_IC_Rechnung_2021_12.docx", 2021, 12, 1_494_500, False, "final"),
    ("RPL_IC_Rechnung_2022_01.docx", 2022, 1, 1_512_400, False, "final"),
    ("RPL_IC_Rechnung_2022_02.docx", 2022, 2, 1_487_900, False, "final"),
    ("RPL_IC_Rechnung_2022_03.docx", 2022, 3, 1_528_300, False, "final"),
    ("RPL_IC_Rechnung_2022_04.docx", 2022, 4, 1_541_600, False, "final"),
    ("RPL_IC_Rechnung_2022_05.docx", 2022, 5, 1_563_400, False, "final"),
    ("RPL_IC_Rechnung_2022_06.docx", 2022, 6, 1_578_900, False, "final"),
    ("RPL_IC_Rechnung_2022_08.docx", 2022, 8, 1_592_700, False, "final"),
    ("RPL_IC_Rechnung_2022_09_WIP.docx", 2022, 9, 1_608_400, True, "WIP / Entwurf"),
    ("RPL_IC_Rechnung_2022_10.docx", 2022, 10, 1_624_300, False, "final"),
    ("RPL_IC_Rechnung_2022_11.docx", 2022, 11, 1_647_800, False, "final"),
    ("RPL_IC_Rechnung_2022_12.docx", 2022, 12, 1_672_500, False, "final"),
]
for rec in IC_RECH:
    ic_rechnung(*rec)


# ─────────────────────────────────────────────────────────────────────────────
# 4) RPL_to_REG_IC_* (36 monthly companion docs)
# ─────────────────────────────────────────────────────────────────────────────

def rpl_to_reg(fname, jahr, monat, betrag_eur, status="final"):
    monat_int = int(monat)
    rgnr = f"RPL-REG-IC-{jahr}-{monat:02d}"
    sections = [
        ("Lieferanten- und Empfaengerangaben",
         f"Lieferantin (Wystawca): {RPL['name']}, {RPL_ADDR}, KRS {RPL_KRS}, NIP {RPL_NIP}, "
         f"REGON {RPL_REGON}. Vertretungsberechtigt: Marek Wojciechowski.\n\n"
         f"Empfaengerin (Odbiorca): Brennhagen Elektronik GmbH (REG), Gottlieb-Daimler-Strasse 24, "
         f"74172 Neckarsulm-Heilbronn, HRB 221456 Amtsgericht Heilbronn, USt-IdNr. DE 287 645 109. "
         f"Ansprechpartner: Werkleiter Andreas Maier, Q-Leitung Sabine Brand."),
        ("Rechnungsdaten / Dane faktury",
         f"Rechnungsnummer: {rgnr}\nRechnungsdatum: 30. {MONTHS_DE[monat_int]} {jahr}\n"
         f"Leistungsmonat: {MONTHS_DE[monat_int]} {jahr}\n"
         f"Waehrung: EUR (Konzernkonvention IC, Rahmenvertrag IC-2018)\n"
         f"Faelligkeit: 60 Tage netto\nBestellbezug: REG-PO-MOY-{jahr}-{monat:02d}\n"
         f"Verrechnungsbasis: TP-Richtlinie 2018, TNMM Cost-Plus 4,5 %\n"
         f"Gesamtbetrag (netto): EUR {betrag_eur:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")),
        ("Leistungsuebersicht / Wykaz dostaw",
         [
             ["Pos", "Produktfamilie", "Menge (Stk.)", "Netto (EUR)"],
             ["1", "ICP-3 Sub-Assemblies (BMW i7-Plattform)", "21.400",
              f"{betrag_eur*0.38:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")],
             ["2", "ECU-900 PCBAs bestueckt", "14.800",
              f"{betrag_eur*0.31:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")],
             ["3", "ADAS-V4D Front-End / Side-Radar Module", "5.600",
              f"{betrag_eur*0.21:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")],
             ["4", "Sonstige (LightCtrl-7, Pruefumlage)", "—",
              f"{betrag_eur*0.10:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")],
             ["", "Summe", "", f"{betrag_eur:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")],
         ]),
        ("Umsatzsteuer / VAT-Behandlung",
         f"Innergemeinschaftliche Lieferung gemaess Art. 138 MwStSystRL i. V. m. § 6a "
         f"polnisches MwSt-Gesetz (Ustawa o VAT). Steuerbefreit. Reverse-Charge auf Seiten "
         f"REG. USt-IdNr. Lieferant PL 634-287-91-04, USt-IdNr. Empfaenger DE 287 645 109. "
         f"Versandnachweis: CMR-{rgnr}-CMR (Transport Spedycja Slaska Sp. z o.o.). "
         f"INTRASTAT-Meldung erfolgt monatlich an GUS Polen / DESTATIS Deutschland."),
        ("Hinweise / Status",
         f"Status: {status}. Buchung in SAP S/4HANA Buchungskreis PL10 (RPL) / DE20 (REG). "
         f"Spiegelbuchung in Konzernkonsolidierung (SAP Group Reporting) wird ueber das "
         f"IC-Matching-Verfahren automatisch abgeglichen; Abstimmungsdifferenz <= 0,2 % wird "
         f"als zulaessig im Konzernabschluss IFRS akzeptiert.\n\nGenehmigt durch Werkleitung "
         f"RPL (M. Wojciechowski) und Finanzcontrolling RPL (M. Lewandowska)."),
    ]
    is_draft = "ENTWURF" in status.upper() or "ENTWURF" in fname
    write_doc(f"{BASE}/{fname}", H_RPL,
              f"IC-Rechnung {MONTHS_DE[monat_int]} {jahr}: {RPL['name']} an Brennhagen Elektronik GmbH",
              subtitle=f"Rechnungs-Nr. {rgnr} – Konzern-Verrechnung (TP-Richtlinie 2018)",
              sections=sections, draft=is_draft)


IC_TO_REG = [
    ("RPL_to_REG_IC_2021_01.docx", 2021, 1, 1_312_800, "final"),
    ("RPL_to_REG_IC_2021_02.docx", 2021, 2, 1_268_400, "final"),
    ("RPL_to_REG_IC_2021_03_ENTWURF.docx", 2021, 3, 1_354_200, "ENTWURF"),
    ("RPL_to_REG_IC_2021_04.docx", 2021, 4, 1_298_700, "final"),
    ("RPL_to_REG_IC_2021_05.docx", 2021, 5, 1_341_900, "final"),
    ("RPL_to_REG_IC_2021_06.docx", 2021, 6, 1_368_400, "final"),
    ("RPL_to_REG_IC_2021_07.docx", 2021, 7, 1_378_500, "final"),
    ("RPL_to_REG_IC_2021_08.docx", 2021, 8, 1_402_300, "final"),
    ("RPL_to_REG_IC_2021_09.docx", 2021, 9, 1_419_600, "final"),
    ("RPL_to_REG_IC_2021_10.docx", 2021, 10, 1_438_100, "final"),
    ("RPL_to_REG_IC_2021_11.docx", 2021, 11, 1_462_800, "final"),
    ("RPL_to_REG_IC_2021_12.docx", 2021, 12, 1_494_500, "final"),
    ("RPL_to_REG_IC_2022_01.docx", 2022, 1, 1_512_400, "final"),
    ("RPL_to_REG_IC_2022_02.docx", 2022, 2, 1_487_900, "final"),
    ("RPL_to_REG_IC_2022_03.docx", 2022, 3, 1_528_300, "final"),
    ("RPL_to_REG_IC_2022_04_ENTWURF.docx", 2022, 4, 1_541_600, "ENTWURF"),
    ("RPL_to_REG_IC_2022_05_20230915.docx", 2022, 5, 1_563_400, "final/Korrektur 15.09.2023"),
    ("RPL_to_REG_IC_2022_06.docx", 2022, 6, 1_578_900, "final"),
    ("RPL_to_REG_IC_2022_07.docx", 2022, 7, 1_584_200, "final"),
    ("RPL_to_REG_IC_2022_08.docx", 2022, 8, 1_592_700, "final"),
    ("RPL_to_REG_IC_2022_09.docx", 2022, 9, 1_608_400, "final"),
    ("RPL_to_REG_IC_2022_10.docx", 2022, 10, 1_624_300, "final"),
    ("RPL_to_REG_IC_2022_11.docx", 2022, 11, 1_647_800, "final"),
    ("RPL_to_REG_IC_2022_12.docx", 2022, 12, 1_672_500, "final"),
    ("RPL_to_REG_IC_2023_01.docx", 2023, 1, 1_698_400, "final"),
    ("RPL_to_REG_IC_2023_02.docx", 2023, 2, 1_672_300, "final"),
    ("RPL_to_REG_IC_2023_03.docx", 2023, 3, 1_724_500, "final"),
    ("RPL_to_REG_IC_2023_04.docx", 2023, 4, 1_741_200, "final"),
    ("RPL_to_REG_IC_2023_05.docx", 2023, 5, 1_756_800, "final"),
    ("RPL_to_REG_IC_2023_06.docx", 2023, 6, 1_768_400, "final"),
    ("RPL_to_REG_IC_2023_07.docx", 2023, 7, 1_782_700, "final"),
    ("RPL_to_REG_IC_2023_08.docx", 2023, 8, 1_798_300, "final"),
    ("RPL_to_REG_IC_2023_09.docx", 2023, 9, 1_814_900, "final"),
    ("RPL_to_REG_IC_2023_10_ENTWURF.docx", 2023, 10, 1_832_400, "ENTWURF"),
    ("RPL_to_REG_IC_2023_11.docx", 2023, 11, 1_851_600, "final"),
    ("RPL_to_REG_IC_2023_12.docx", 2023, 12, 1_874_200, "final"),
]
for rec in IC_TO_REG:
    rpl_to_reg(*rec)


# ─────────────────────────────────────────────────────────────────────────────
# 5) RPL_Steuerbescheid_* (4 docs)
# ─────────────────────────────────────────────────────────────────────────────

def steuerbescheid(fname, jahr, kst_pln, kst_eur, gewinn_pln, gewinn_eur,
                   bemerkung="", intern=False):
    confidential = intern or jahr in ("2020", "2022", "2023")
    sections = [
        ("Bescheidkopf / Naglowek decyzji",
         f"Urzad Skarbowy w Katowicach (Finanzamt Katowice)\n"
         f"ul. Zarska 5, 40-022 Katowice\n\n"
         f"Adressat: {RPL['name']}, {RPL_ADDR}, KRS {RPL_KRS}, NIP {RPL_NIP}.\n\n"
         f"Bescheid-Nr.: USK/CIT/{jahr}/RPL-67234\n"
         f"Steuerart: Koerperschaftsteuer (CIT – Podatek dochodowy od osob prawnych)\n"
         f"Steuerjahr: 1. Januar {jahr} – 31. Dezember {jahr}\n"
         f"Veranlagungszeitraum: 12 Monate\n"
         f"Bescheiddatum: 18. November {int(jahr)+1}"),
        ("Festsetzungsgrundlagen",
         [
             ["Position", "PLN", "EUR (NBP-Mittelkurs)"],
             ["Steuerlicher Gewinn vor Steuern (CIT-8)",
              f"{gewinn_pln:,.0f}".replace(",", "."), f"{gewinn_eur:,.0f}".replace(",", ".")],
             ["Steuersatz (CIT regulaer)", "19,0 %", "19,0 %"],
             ["Festgesetzte CIT-Belastung",
              f"{kst_pln:,.0f}".replace(",", "."), f"{kst_eur:,.0f}".replace(",", ".")],
             ["Vorauszahlungen (zaliczki) geleistet",
              f"{int(kst_pln*0.92):,.0f}".replace(",", "."),
              f"{int(kst_eur*0.92):,.0f}".replace(",", ".")],
             ["Nachzahlung / Erstattung",
              f"{int(kst_pln*0.08):,.0f}".replace(",", "."),
              f"{int(kst_eur*0.08):,.0f}".replace(",", ".")],
         ]),
        ("Begruendung der Festsetzung",
         f"Die Festsetzung beruht auf der durch den Steuerpflichtigen am 31. Maerz {int(jahr)+1} "
         f"eingereichten Steuererklaerung CIT-8 nebst Anlagen CIT-8/O (sonstige Ertraege), "
         f"CIT-D (Spenden) sowie CIT-IB (Investitionsabzug Sonderwirtschaftszone Katowice). "
         f"Der ausgewiesene steuerliche Gewinn von PLN {gewinn_pln:,.0f}".replace(",", ".")
         + " wurde nach Pruefung der Konzern-Verrechnungspreise (Local File RPL " + str(jahr) + " " +
         "gemaess Ustawa o cenach transferowych) anerkannt. Die Konzernverrechnungen mit REG "
         "(Heilbronn) und RHO (Stuttgart) wurden geprueft; die TNMM-Routinemarge von 4,5 % "
         "auf Vollkosten gilt als fremdueblich. Keine TP-Adjustments erforderlich.\n\n"
         f"Anrechenbare auslaendische Quellensteuern: keine. Investitionsabzug Sonderwirtschaftszone "
         f"Katowice (Katowicka SSE) ausgenutzt mit PLN 412.000 (Mindern der Bemessungsgrundlage). "
         f"{bemerkung}"),
        ("Hinweise zur Bezahlung / Rechtsbehelf",
         f"Die Nachzahlung ist binnen 14 Tagen ab Zustellung auf das Konto des Urzad Skarbowy "
         f"in Katowice (Nationale Steuerverwaltung KAS, IBAN PL13 1010 1212 3127 8800 0000 0001) "
         f"zu leisten. Bei Versaeumnis werden Verzugszinsen gemaess Art. 56 Ordynacja podatkowa "
         f"(Steuerordnung) berechnet (8 % p. a. Stand {jahr}).\n\n"
         f"Gegen diesen Bescheid kann innerhalb von 14 Tagen ab Zustellung Einspruch (odwolanie) "
         f"beim Dyrektor Izby Administracji Skarbowej Katowice eingelegt werden. Der Einspruch ist "
         f"ueber den Urzad Skarbowy w Katowicach einzureichen."),
        ("Bearbeitung",
         f"Bearbeitung der Steuererklaerung und Pruefung der Verrechnungspreise erfolgte unter "
         f"Mitwirkung von Deloitte Polska Sp. z o.o. (Warschau), Lead-Partner Adam Kowalczyk, "
         f"im Auftrag der RPL-Finanzleitung (M. Lewandowska) und in Abstimmung mit dem Group "
         f"Tax Director der REA (Dr. Heike Berger, Stuttgart). KPMG AG WPG (Konzern-WP, "
         f"Lead Partner Dr. Maximilian Brand) hat die steuerliche Position fuer Zwecke des "
         f"Konzern-Jahresabschlusses {jahr} (IFRS / IAS 12) bestaetigt."),
        ("Unterschrift",
         "Decyzja wydana w imieniu Naczelnika Urzedu Skarbowego w Katowicach.\n\n"
         "_______________________________\n"
         "mgr Joanna Brzezinska\nKierownik Dzialu Podatkow Dochodowych od Osob Prawnych\n"
         "Urzad Skarbowy w Katowicach"),
    ]
    write_doc(f"{BASE}/{fname}", H_RPL,
              f"Steuerbescheid / Decyzja podatkowa CIT {jahr} – {RPL['name']}",
              subtitle=f"Bescheid Nr. USK/CIT/{jahr}/RPL-67234 (Urzad Skarbowy Katowice)",
              sections=sections, confidential=confidential)


steuerbescheid("RPL_Steuerbescheid_2020_intern.docx", "2020",
               kst_pln=6_120_000, kst_eur=1_345_000,
               gewinn_pln=32_210_000, gewinn_eur=7_080_000,
               bemerkung="Hinweis: 2020 COVID-bedingt reduziertes Ergebnis. Verlustruecktrag aus Folgejahr nicht moeglich (PL).",
               intern=True)
steuerbescheid("RPL_Steuerbescheid_2021.docx", "2021",
               kst_pln=8_485_000, kst_eur=1_863_000,
               gewinn_pln=44_660_000, gewinn_eur=9_820_000)
steuerbescheid("RPL_Steuerbescheid_2022.docx", "2022",
               kst_pln=9_320_000, kst_eur=1_988_000,
               gewinn_pln=49_050_000, gewinn_eur=10_460_000)
steuerbescheid("RPL_Steuerbescheid_KSt_2023.docx", "2023",
               kst_pln=10_140_000, kst_eur=2_172_000,
               gewinn_pln=53_370_000, gewinn_eur=11_430_000,
               bemerkung="Investitionszulage Katowicka SSE: PLN 612.000.")


# ─────────────────────────────────────────────────────────────────────────────
# 6) RPL_ControlPlan_* (4 docs)
# ─────────────────────────────────────────────────────────────────────────────

def control_plan(fname, produkt, produktcode, kunde, linien, takt_s, wip=False):
    sections = [
        ("Lenkungsplan-Identifikation",
         f"Produkt: {produkt} ({produktcode})\nHauptkunden: {kunde}\nProduktionsstandort: "
         f"{RPL['name']}, Werk Katowice (8 SMD-Linien)\nFertigungslinien fuer dieses Produkt: {linien}\n"
         f"Taktzeit Ziel: {takt_s} s/Stk.\n"
         f"Lenkungsplan-Nr.: RPL-CP-{produktcode}-2023.04\nGueltig ab: 1. April 2023\n"
         f"Ueberarbeitung Nr.: 04 (jaehrliche Re-Validierung gemaess IATF 16949 §8.5.1.1)\n"
         f"Erstellt durch: Q-Manager RPL (Krzysztof Nowak / Anna Sokolowska)\n"
         f"Freigegeben durch: Werkleiter Marek Wojciechowski / OEM-Kundenvertretung\n"
         f"Anwendung: Produktionslenkung / Serienfertigung (Production Control)"),
        ("Geltungsbereich",
         f"Dieser Lenkungsplan gilt fuer die Fertigung des Produktes {produkt} ({produktcode}) "
         f"auf den Linien {linien} im Werk Katowice. Er beschreibt die Prozessschritte, Prozess- "
         f"und Produktmerkmale, Mess- und Pruefverfahren sowie Reaktionsplaene gemaess "
         f"IATF 16949:2016, AIAG-VDA FMEA-Handbuch (2019) sowie der jeweiligen Kunden-CSR "
         f"(Customer Specific Requirements: BMW GS95015, VW Konzernnormen, Mercedes MBN). "
         f"Bezugsdokumente: PFMEA Rev. 07, Prozessflussdiagramm Rev. 05, Werkerstandards "
         f"AS-RPL-{produktcode}, Pruefmittelfaehigkeitsanalysen MSA Rev. 03."),
        ("Prozess- und Pruefmatrix",
         [
             ["Schritt", "Prozess", "Merkmal", "Spezifikation", "Methode/Mittel",
              "Stichprobe", "Reaktionsplan"],
             ["10", "Solder Paste Print",
              "Pastenvolumen 100 +/- 12 %", "SPI 5DX (Koh Young KY8030)",
              "100 % SPI", "1 Linie/h", "Linie Stopp + Reinigung Stencil"],
             ["20", "SMD-Bestueckung Top",
              "Bauteil-Positionierung +/- 50 µm", "Pick-and-Place ASM Siplace SX2",
              "1x/Schicht Erstmusterpruefung", "n=5 / Schicht",
              "Linie Stopp / Nozzle-Pruefung"],
             ["30", "Reflow-Loeten",
              "Temperaturprofil 245 +/- 5 °C Peak",
              "Reflow-Ofen Heller 1936 MK7 (12 Zonen, N2)", "Profilmessung 2x/Schicht KIC2000",
              "n=1 PCB/Schicht", "Stop / Profilanpassung / Eskalation Q-Leitung"],
             ["40", "AOI (Optisch)",
              "Loetstellen, Polaritaet, Bauteil-Praesenz", "Koh Young Zenith Alpha 3D-AOI",
              "100 %", "100 %", "Pseudo-Faults < 0,5 % / sonst Stopp"],
             ["50", "ICT / Flying Probe",
              "Funktionstest Leiterzuege, Bauteilwerte +/- 5 %",
              "Teradyne / SPEA 4060", "100 %", "100 %", "Fail-Bin / Nacharbeit / Quarantaene"],
             ["60", "Funktionstest EOL",
              "Performance- und Software-Test gemaess Kundenspez.",
              "Pruefstand PRF-" + produktcode + "-01 (kundenfreigegeben)", "100 %",
              "100 %", "Fail-Bin / 8D-Eroeffnung > 100 ppm"],
             ["70", "Endverpackung / ESD",
              "ESD-konform, Label nach Kundenspez. (KANBAN/Galia)",
              "Manuelle Sichtpruefung + Scan", "Stichprobe", "n=10 / Schicht",
              "Rework / Quarantaene-Bestand"],
         ]),
        ("Kunden- und Normspezifika",
         f"Anwendbare Kundenforderungen / Normen:\n"
         f"- IATF 16949:2016 (Quality Management Automotive)\n"
         f"- ISO 9001:2015 / ISO 14001:2015 / ISO 50001:2018\n"
         f"- IPC-A-610 Klasse 3 (Verbindungstechnik)\n"
         f"- AIAG-VDA FMEA Handbuch 1. Ausgabe (2019)\n"
         f"- VDA 6.3 Prozessaudit (mind. P-Niveau A)\n"
         f"- Kundenspezifika {kunde} (CSR-Matrix in QM-Tool e1NS hinterlegt)\n\n"
         f"Pruefmittelfaehigkeit (MSA): Cg/Cgk >= 1,33; Gage R&R <= 10 %. Pruefmittel werden "
         f"kalibriert nach Kalibrierplan RPL-KAL-2023, Intervall 12 Monate, durch DAkkS-akkreditierte "
         f"Labore (z. B. Testo Industrial Services Polska)."),
        ("Reaktionsplaene und Eskalation",
         f"Bei OOS-Werten (out of specification) ist die Linie sofort zu stoppen. Die Schichtleitung "
         f"eskaliert binnen 15 Minuten an Q-Leitung und Produktionsleitung. Quarantaene aller "
         f"betroffenen Bestaende. Bei Lieferungen an Kunde innerhalb 24 h: 8D-Eroeffnung "
         f"(D1 in 24 h, D3 in 48 h, D8 in 21 Tagen). Bei sicherheits- oder typgenehmigungsrelevanten "
         f"Merkmalen sofortige Information CTO (Dr. Petra Hollmann) und CRO Asia / Konzern-Q "
         f"(Sabine Brand REG)."),
        ("Freigabe / Approval",
         f"Dieser Lenkungsplan ist freigegeben und gueltig.\n\n"
         + signatures("Krzysztof Nowak", "Produktionsleiter RPL", RPL["name"],
                      "Anna Sokolowska", "Q-Leitung RPL", RPL["name"],
                      place="Katowice",
                      date_str_="1. April 2023" if not wip else "12. Maerz 2024 (Entwurf)")),
    ]
    write_doc(f"{BASE}/{fname}", H_RPL,
              f"Lenkungsplan (Control Plan) – {produkt} – {RPL['name']}",
              subtitle=f"IATF 16949 §8.5.1.1 / AIAG-VDA / Linien {linien}",
              sections=sections, draft=wip)


control_plan("RPL_ControlPlan_ADAS-V4D_2023.docx",
             "Radar Fusion Steuergeraet (Level-2/3 ADAS)", "ADAS-V4D",
             "Mercedes-Benz Group AG, Stellantis N.V.", "Linie 6 + 7", 32, wip=False)
control_plan("RPL_ControlPlan_BMS-12_2023.docx",
             "BatteryMS-12 (Batteriemanagementsystem EV)", "BMS-12",
             "Volkswagen AG (ID.7), Hyundai Motor Company", "Linie 3 + 4", 28, wip=False)
control_plan("RPL_ControlPlan_ECU-900_2023.docx",
             "Powertrain-ECU Gen3", "ECU-900",
             "Volkswagen AG (MEB+/MQB-Evo), Stellantis N.V.", "Linie 2 + 5", 24, wip=False)
control_plan("RPL_ControlPlan_ICP-3_2023_WIP.docx",
             "InfoConnect Pro (Infotainment-Modul)", "ICP-3",
             "BMW Group, Mercedes-Benz Group AG", "Linie 1 + 8", 36, wip=True)


# ─────────────────────────────────────────────────────────────────────────────
# 7) RPL_Compliance_Report_2023.docx
# ─────────────────────────────────────────────────────────────────────────────

write_doc(f"{BASE}/RPL_Compliance_Report_2023.docx", H_RPL,
          f"Compliance-Jahresbericht 2023 – {RPL['name']}",
          subtitle="Berichtszeitraum 1. Januar 2023 – 31. Dezember 2023",
          sections=[
              ("Vorbemerkung",
               "Dieser Compliance-Jahresbericht 2023 dokumentiert die Umsetzung der konzernweit "
               "geltenden Compliance-Standards (Code of Conduct Brennhagen Elektronik AG, "
               "Antikorruptionsrichtlinie, Exportkontrolle, Whistleblowing-Richtlinie) durch die "
               "Brennhagen Polska Sp. z o.o. und ist Teil des Konzern-Compliance-Reportings an den "
               "Pruefungsausschuss des Aufsichtsrats der Brennhagen Elektronik AG (Vorsitz Prof. "
               "Dr.-Ing. Gerhard Voss)."),
              ("Compliance-Organisation",
               f"Local Compliance Officer (LCO) RPL: Magdalena Lewandowska (Doppelfunktion mit "
               f"Finance Controlling). Berichtsweg: an Group Compliance Officer Dr. Andreas "
               f"Bühler (Chief Audit Executive, Stuttgart). Lokales Compliance-Komitee tagt "
               f"quartalsweise (Werkleiter, HR, Finance, Q-Leitung, Betriebsratsvorsitz). "
               f"Sitzungen 2023: 14.02., 18.05., 12.09., 05.12. (alle protokolliert)."),
              ("Schulungen 2023",
               [
                   ["Schulung", "Zielgruppe", "Teilnehmer", "Quote", "Format"],
                   ["Code of Conduct Refresher", "Alle MA", "942 / 960", "98,1 %", "E-Learning (poln.)"],
                   ["Antikorruption / Geschenke-Richtlinie", "Fuehrungskraefte + Einkauf",
                    "118 / 124", "95,2 %", "Praesenz + Test"],
                   ["DSGVO / RODO Refresher", "Alle MA mit PC-Arbeitsplatz",
                    "412 / 420", "98,1 %", "E-Learning"],
                   ["Exportkontrolle (Dual-Use, EU-Sanktionen)", "Sales/Logistik/Engineering",
                    "84 / 87", "96,6 %", "Live Webinar"],
                   ["Kartellrecht / Wettbewerbsrecht", "Fuehrungskraefte + Sales",
                    "98 / 102", "96,1 %", "Praesenz"],
                   ["IATF 16949 Q-Awareness", "Produktionsmitarbeiter",
                    "780 / 800", "97,5 %", "Werker-Schulung am Arbeitsplatz"],
               ]),
              ("Whistleblower-Meldungen / Hinweisgeberkanal",
               "Im Berichtszeitraum 2023 sind beim konzernweiten Hinweisgeberkanal (extern "
               "betrieben durch BKMS System / EQS Group AG) 3 Hinweise aus dem Werk Katowice "
               "eingegangen:\n\n"
               "1. Verdacht auf Schichtplan-Manipulation (untersucht, Sachverhalt nicht "
               "bestaetigt; Massnahme: ueberarbeitete Schichtplan-Dokumentation, Roll-out 04/2023).\n"
               "2. Hinweis auf moegliche Datenschutzverletzung im HR-System (untersucht durch "
               "lokalen DPO / Group DPO; technisches Konfigurationsproblem behoben in 24 h; "
               "keine Meldepflicht nach Art. 33 DSGVO).\n"
               "3. Verdacht auf unzulaessige Zuwendungen an einen Lieferanten (untersucht durch "
               "Internal Audit / KPMG Forensic; Verdacht nicht erhaertet, Sachverhalt geschlossen)."),
              ("ZUS / Sozialversicherung / Arbeitsrecht",
               "Saemtliche ZUS-Beitraege (Renten-, Kranken-, Unfall-, Arbeitslosenversicherung, "
               "NFZ, PFRON) fuer 2023 fristgerecht abgefuehrt (PLN 78,6 Mio. Arbeitgeberanteil). "
               "Beschwerden bei der Panstwowa Inspekcja Pracy (PIP – Staatliche Arbeitsinspektion): "
               "keine. Arbeitsgerichtliche Verfahren 2023: 2 Verfahren (1 Kuendigungsschutzklage "
               "Vergleich, 1 Verfahren laufend Sad Rejonowy Katowice-Zachod)."),
              ("Datenschutz / RODO",
               "Lokaler Datenschutzbeauftragter (Inspektor Ochrony Danych): Anna Kowalska "
               "(HR-Leitung, mit Doppelmandat). Berichtsweg an Konzern-DPO Frankfurt. "
               "Verzeichnis von Verarbeitungsvorgaengen (RVV) gepflegt und aktuell. Im "
               "Berichtszeitraum 2 DSGVO-Anfragen Betroffener (Auskunft / Loeschung), beide "
               "fristgerecht beantwortet. Keine meldepflichtigen Datenpannen."),
              ("Exportkontrolle / Sanktionen",
               "Pruefung der Sanktionslisten (EU 833/2014 Russland-Sanktionen, OFAC SDN, BAFA) "
               "monatlich auf Lieferanten- und Kundenstamm. Im Zuge der Sanktionen 2022/2023 "
               "wurden 14 Geschaeftsbeziehungen beendet (russische Distributoren / belarussische "
               "Sublieferanten). Keine Verstoesse identifiziert. Dual-Use-Pruefung fuer "
               "ADAS-V4D-Komponenten erfolgt automatisiert in SAP GTS."),
              ("Bewertung und Ausblick",
               "Insgesamt bewertet der lokale Compliance Officer die Compliance-Lage der "
               "RPL fuer 2023 als »wirksam und stabil«. Fuer 2024 geplant: (i) Roll-out "
               "Lieferanten-Compliance-Audits (5 Lieferanten Stufe A), (ii) Aktualisierung "
               "Geschenke- und Bewirtungsrichtlinie (PLN-Schwellenwerte), (iii) ISO 27001-"
               "Vorbereitung (Konzern-Roll-out).\n\n"
               + signatures("Magdalena Lewandowska", "Local Compliance Officer RPL", RPL["name"],
                            "Dr. Andreas Bühler", "Group Compliance Officer / CAE", R["name"],
                            place="Katowice / Stuttgart", date_str_="22. Februar 2024")),
          ])


# ─────────────────────────────────────────────────────────────────────────────
# 8) RPL_Mietvertrag_Betriebsgelaende_2020.docx
# ─────────────────────────────────────────────────────────────────────────────

write_doc(f"{BASE}/RPL_Mietvertrag_Betriebsgelaende_2020.docx", H_RPL,
          "Mietvertrag Betriebsgelaende Katowice – Umowa najmu nieruchomosci",
          subtitle="Werkserweiterung 2020 – Halle 4 (SMD-Linien 7/8) und Logistikzentrum",
          sections=[
              ("Vertragsparteien / Strony umowy",
               f"Zwischen\n\n(1) Katowicka Specjalna Strefa Ekonomiczna S.A. (»Vermieterin« / "
               f"»Wynajmujacy«), ul. Wojewodzka 42, 40-026 Katowice, KRS 0000106403, NIP "
               f"954-12-67-082, vertreten durch Vorstandsvorsitzenden Janusz Michalek,\n\n"
               f"und\n\n(2) {RPL['name']} (»Mieterin« / »Najemca«), {RPL_ADDR}, "
               f"{RPL_KRS}, NIP {RPL_NIP}, REGON {RPL_REGON}, vertreten durch den Dyrektor "
               f"Zakladu Marek Wojciechowski sowie die Finanzcontrollerin Magdalena Lewandowska,\n\n"
               f"wird folgender Mietvertrag (umowa najmu) ueber die Anmietung von Industrieflaechen "
               f"im Gewerbegebiet Katowice-Wschod (Katowicka SSE Subzone Tychy/Katowice) geschlossen."),
              ("§ 1 Mietgegenstand / Przedmiot najmu",
               "(1) Vermietet wird die Industriehalle 4 (»Halle 4«) im Werkareal "
               "ul. Roozdzienskiego 188/B, 40-203 Katowice, mit folgenden Flaechen:\n"
               "- Produktionshalle 4: 6.840 m² (Stahlfachwerk-Konstruktion, lichte Hoehe 8 m)\n"
               "- Buero- und Sozialraeume: 1.220 m² (zweigeschossig)\n"
               "- Hochregallager: 2.460 m² (12 m hoch)\n"
               "- Aussen-Logistikflaeche: 4.200 m²\n"
               "- Mitarbeiterparkplatz: 280 Stellplaetze\n\n"
               "(2) Gesamt-Nutzflaeche: 14.720 m². Grundstuecks-Kataster: 2310/4 (Obreb Bogucice). "
               "Eintragung im Grundbuch (Ksiega Wieczysta): KA1K/00067834/3, Sad Rejonowy "
               "Katowice-Wschod.\n\n"
               "(3) Der Mietgegenstand wird im Bauphasen-uebergabezustand uebergeben; ein "
               "Uebergabe- und Abnahmeprotokoll (Anhang 1) ist Bestandteil dieses Vertrages."),
              ("§ 2 Mietdauer / Czas trwania najmu",
               "(1) Das Mietverhaeltnis beginnt am 1. Juli 2020 und wird auf bestimmte Zeit "
               "von 15 Jahren bis 30. Juni 2035 geschlossen.\n\n"
               "(2) Die Mieterin hat das Recht, das Mietverhaeltnis zweimal um je 5 Jahre zu "
               "verlaengern; das Verlaengerungsrecht ist 12 Monate vor Vertragsende schriftlich "
               "auszuueben.\n\n"
               "(3) Eine ordentliche Kuendigung waehrend der Festlaufzeit ist ausgeschlossen. "
               "Ausserordentliche Kuendigungsrechte beider Parteien aus wichtigem Grund "
               "(insb. Insolvenz, schwere Vertragsverletzung) bleiben unberuehrt."),
              ("§ 3 Miete und Nebenkosten / Czynsz i koszty dodatkowe",
               "(1) Die monatliche Nettomiete betraegt PLN 218.500 (zweihundertachtzehntausendfuenfhundert "
               "Zloty), entsprechend ca. EUR 48.000 zum Referenzkurs NBP zum Vertragsschluss. "
               "Die Miete ist im Voraus bis zum 10. Tag jedes Monats faellig.\n\n"
               "(2) Indexierung: Die Miete wird jaehrlich zum 1. Juli an den polnischen "
               "Verbraucherpreisindex (CPI / wskaznik cen towarow i uslug konsumpcyjnych) des "
               "Vorjahres angepasst (Indexierungskappe 4,0 % p. a.).\n\n"
               "(3) Nebenkosten (Strom, Gas, Wasser, Abwasser, Abfall) traegt die Mieterin "
               "direkt (Direktvertraege mit Tauron Polska Energia, PGNiG, Katowickie Wodociagi). "
               "Vorauszahlung Nebenkostenpauschale: PLN 18.000 / Monat, jaehrliche Abrechnung.\n\n"
               "(4) Auf alle Mietzahlungen wird zusaetzlich die gesetzliche Mehrwertsteuer "
               "(VAT 23 %) berechnet und in Rechnung gestellt."),
              ("§ 4 Nutzungszweck",
               "Die Mieterin wird den Mietgegenstand ausschliesslich fuer industrielle Zwecke "
               "im Bereich Elektronik-/EMS-Fertigung (SMD-Bestueckung Linien 7 und 8, "
               "ICT/Funktionstest, Endmontage Steckverbinder, Logistik und Lagerhaltung) nutzen. "
               "Eine Aenderung des Nutzungszwecks beduerftiger der vorherigen schriftlichen "
               "Zustimmung der Vermieterin. Buerogeschossnutzung ausschliesslich administrativ."),
              ("§ 5 Investitionen / Mieterausbauten",
               "(1) Die Mieterin investiert zur Inbetriebnahme der Halle 4 ca. EUR 12,5 Mio. in "
               "die Ausstattung der zwei neuen SMD-Linien (ASM Siplace SX2, Heller 1936 Reflow, "
               "Koh Young AOI/SPI, Teradyne ICT), ESD-Bodenbelag, Reinraum-Hilfsbereich "
               "Klasse 8, gebaeudetechnische Infrastruktur (Klima/USV/Druckluft) und "
               "Brandschutz (Sprinkler, Brandfrueherkennung Wagner Titanus).\n\n"
               "(2) Die Investitionen werden als Mieterausbauten aktiviert und ueber die "
               "Restlaufzeit des Mietvertrages abgeschrieben (linear, 15 Jahre).\n\n"
               "(3) Die Vermieterin gewaehrt hierzu einen einmaligen Investitionszuschuss in "
               "Hoehe von PLN 4,2 Mio. (Foerderbescheid Katowicka SSE Nr. KSSE/2020/178)."),
              ("§ 6 Versicherung",
               "Die Mieterin schliesst zugunsten beider Parteien eine Gebaeudeversicherung "
               "(Wiederherstellungswert), eine Inhaltsversicherung (Sachen und Maschinen "
               "ca. PLN 60 Mio.), eine Betriebsunterbrechungsversicherung (12 Monate Deckung) "
               "und eine Betriebshaftpflichtversicherung mit Deckungssumme PLN 25 Mio. bei "
               "Allianz Polska S.A. ab. Versicherungsnachweis ist jaehrlich der Vermieterin "
               "vorzulegen."),
              ("§ 7 Sonderwirtschaftszone (KSSE) und Foerderung",
               "(1) Der Mietgegenstand liegt in der Katowicka Specjalna Strefa Ekonomiczna "
               "(Subzone Katowice). Die Mieterin nutzt im Rahmen der Genehmigung Nr. KSSE/178/2020 "
               "die Koerperschaftsteuerbefreiung gemaess Art. 17 (1) Punkt 34a CIT-Gesetz "
               "(Investitionsvolumen mind. PLN 100 Mio., neue Arbeitsplaetze mind. 250).\n\n"
               "(2) Die Mieterin sichert dem Vermieter zu, die SSE-Auflagen einzuhalten und "
               "jaehrlich Bericht zu erstatten."),
              ("§ 8 Anwendbares Recht / Gerichtsstand",
               "(1) Auf diesen Vertrag findet polnisches Recht Anwendung.\n\n"
               "(2) Ausschliesslicher Gerichtsstand: Sad Okregowy w Katowicach (Landgericht "
               "Katowice).\n\n"
               "(3) Aenderungen und Ergaenzungen beduerftiger der Schriftform. Salvatorische "
               "Klausel: Sollte eine Bestimmung unwirksam sein, bleibt die Wirksamkeit der "
               "uebrigen Bestimmungen unberuehrt."),
              ("Unterschriften / Podpisy",
               signatures("Janusz Michalek", "Praezes Zarzadu KSSE", "Katowicka SSE S.A.",
                          "Marek Wojciechowski", "Dyrektor Zakladu", RPL["name"],
                          place="Katowice", date_str_="22. Juni 2020")),
          ])


# ─────────────────────────────────────────────────────────────────────────────
# 9) RPL_Versicherungsnachweis_2023.docx
# ─────────────────────────────────────────────────────────────────────────────

write_doc(f"{BASE}/RPL_Versicherungsnachweis_2023.docx", H_RPL,
          f"Versicherungsnachweis / Zaswiadczenie ubezpieczeniowe 2023 – {RPL['name']}",
          subtitle="Bestaetigung der bestehenden Versicherungsdeckung fuer das Geschaeftsjahr 2023",
          sections=[
              ("Versicherer / Ubezpieczyciel",
               "Hiermit bestaetigt die\n\n"
               "Allianz Polska S.A.\nul. Rodziny Hiszpanskich 1, 02-685 Warschau\n"
               "KRS 0000028261, NIP 525-15-65-015\n\n"
               "(im Folgenden »Versicherer«), dass die\n\n"
               f"{RPL['name']}, {RPL_ADDR}, KRS {RPL_KRS}, NIP {RPL_NIP}\n\n"
               "(im Folgenden »Versicherungsnehmer«) im Berichtsjahr 2023 die folgenden "
               "Versicherungsvertraege unterhaelt:"),
              ("Bestehende Versicherungspolicen",
               [
                   ["Sparte", "Policen-Nr.", "Deckungssumme", "Selbstbehalt", "Laufzeit"],
                   ["Gebaeude- und Inhaltsversicherung", "POL-2023-RPL-GBK-001",
                    "PLN 280 Mio.", "PLN 50.000 / Schaden", "01.01.–31.12.2023"],
                   ["Betriebsunterbrechung (BU 12 Mon.)", "POL-2023-RPL-BU-002",
                    "PLN 95 Mio.", "7 Tage Wartezeit", "01.01.–31.12.2023"],
                   ["Maschinenbruch / Maschinen-BU", "POL-2023-RPL-MB-003",
                    "PLN 62 Mio.", "PLN 25.000", "01.01.–31.12.2023"],
                   ["Betriebs- und Produkthaftpflicht", "POL-2023-RPL-LIA-004",
                    "PLN 25 Mio. / Jahr", "PLN 15.000", "01.01.–31.12.2023"],
                   ["Erweiterte Produkthaftpflicht (Auto-Sektor)", "POL-2023-RPL-EPL-005",
                    "EUR 20 Mio. (via Konzern-Master AGCS)", "EUR 250.000", "Konzern-Master"],
                   ["Transportversicherung (Stueckgueter / CMR)", "POL-2023-RPL-TR-006",
                    "PLN 12 Mio. / Transport", "PLN 5.000", "01.01.–31.12.2023"],
                   ["Cyber-Versicherung", "POL-2023-RPL-CYB-007",
                    "EUR 15 Mio. (Konzern-Master AGCS)", "EUR 100.000", "Konzern-Master"],
                   ["D&O (Geschaeftsfuehrung)", "POL-2023-RPL-DO-008",
                    "EUR 50 Mio. (Konzern-Master AGCS)", "EUR 50.000", "Konzern-Master"],
                   ["ZUS / Sozialversicherung", "n/a (gesetzlich)",
                    "Gesetzliche Deckung", "—", "fortlaufend"],
               ]),
              ("Erlaeuterungen",
               "Die Konzern-Master-Policen (D&O, Cyber, Erweiterte Produkthaftpflicht) werden "
               "ueber die Allianz Global Corporate & Specialty SE (AGCS, Muenchen) im Rahmen "
               "des konzernweiten Versicherungsprogramms Brennhagen Elektronik AG (Insurance "
               "Master Agreement IMA-2022) abgeschlossen. Lokale Policen werden ueber die "
               "Allianz Polska S.A. als Frontingversicherer erbracht.\n\n"
               "Versicherungsmakler ist die Marsh GmbH (Frankfurt) mit lokaler Repraesentanz "
               "Marsh Polska Sp. z o.o. (Warschau). Ansprechpartner: Tomasz Zielinski "
               "(Marsh Polska Senior Broker, Industriebereich)."),
              ("Schadensverlauf 2023",
               "Im Berichtsjahr 2023 wurden 4 versicherte Schaeden gemeldet:\n\n"
               "1. Wasserschaden Dach Halle 2 (Januar 2023, regulierte Schadenshoehe "
               "PLN 184.000)\n"
               "2. Maschinenschaden Reflow-Ofen Linie 3 (April 2023, PLN 412.000)\n"
               "3. Transportschaden ICP-3-Lieferung an REG (Juli 2023, PLN 38.000)\n"
               "4. Cyber-Vorfall (Phishing-Versuch, kein Versicherungsfall ausgeloest, "
               "praeventive Massnahmen 2024 geplant)\n\n"
               "Gesamte regulierte Leistung 2023: ca. PLN 634.000. Schadensquote (loss "
               "ratio) ca. 18 % der Praemien (regulaer)."),
              ("Bestaetigung / Wystawienie zaswiadczenia",
               "Diese Bestaetigung wird auf Anforderung der Konzernmuttergesellschaft Brennhagen "
               "Elektronik AG fuer Zwecke der Due-Diligence-Pruefung sowie des Konzern-"
               "Risikomanagements ausgestellt.\n\n"
               + signatures("Krzysztof Borowski", "Senior Underwriter Industrie", "Allianz Polska S.A.",
                            "Tomasz Zielinski", "Senior Broker", "Marsh Polska Sp. z o.o.",
                            place="Warschau", date_str_="15. Januar 2024")),
          ])


# ─────────────────────────────────────────────────────────────────────────────
# 10) RPL_WP_Management_Letter_2022 / 2023.docx
# ─────────────────────────────────────────────────────────────────────────────

def wp_mgmt_letter(fname, jahr, findings):
    sections = [
        ("Adressaten",
         f"An die Geschaeftsfuehrung der {RPL['name']} (Marek Wojciechowski, Magdalena "
         f"Lewandowska) sowie nachrichtlich an die Konzern-WP KPMG AG WPG (Lead Partner Konzern: "
         f"Dr. Maximilian Brand) und an den Group Tax Director der Brennhagen Elektronik AG "
         f"(Dr. Heike Berger)."),
        ("Praeambel",
         f"Im Rahmen unserer Abschlusspruefung des Jahresabschlusses {jahr} der {RPL['name']} "
         f"nach polnischem Bilanzrecht (Ustawa o rachunkowosci) sowie der Pruefung des "
         f"Reporting-Packages nach IFRS fuer Zwecke des Konzernabschlusses der Brennhagen "
         f"Elektronik AG haben wir gemaess Pruefungsstandard KSB 265 (analog ISA 265) den "
         f"Aufsichtsorganen wesentliche Feststellungen zum Internen Kontrollsystem und zu "
         f"Bilanzierungsfragen mitzuteilen. Dies ist Gegenstand des vorliegenden "
         f"Management Letters."),
        ("Wesentliche Feststellungen / Kluczowe ustalenia", ("list", findings)),
        ("Bewertung des Internen Kontrollsystems",
         f"Das IKS der RPL ist insgesamt wirksam ausgestaltet. Funktionstrennungen in den "
         f"Bereichen Einkauf, Wareneingang, Produktion und Finanzbuchhaltung sind durchgesetzt; "
         f"automatisierte Kontrollen in SAP S/4HANA (Berechtigungskonzept, Vier-Augen-Prinzip "
         f"fuer Zahlungen > EUR 50.000) sind eingerichtet. Defizite (siehe Findings) sind "
         f"adressiert und mit Massnahmenplan unterlegt. Eine wesentliche Schwaeche (Material "
         f"Weakness) i. S. v. SOX-aequivalenten Anforderungen liegt nicht vor."),
        ("Verrechnungspreise / Ceny transferowe",
         f"Die TP-Dokumentation {jahr} (Local File RPL gemaess Ustawa o cenach transferowych) "
         f"wurde fristgerecht erstellt und liegt fuer das Berichtsjahr vor. Die TNMM-"
         f"Routinemarge von 4,5 % auf Vollkosten ist fremdvergleichskonform; Benchmark-Studie "
         f"durch Deloitte Polska 2022 (Gueltigkeit 3 Jahre). Konsistenz mit Konzern-TP-"
         f"Richtlinie 2018 ist gegeben."),
        ("Empfehlungen und naechste Schritte",
         f"Wir empfehlen, die identifizierten Findings im Q1 {int(jahr)+1} abzuarbeiten und "
         f"die Massnahmenumsetzung im naechsten Audit zu verfolgen. Eine Re-Pruefung im "
         f"Rahmen der Folgejahresabschlusspruefung ist eingeplant."),
        ("Schlusswort",
         f"Wir danken der Geschaeftsfuehrung und den Mitarbeitenden der {RPL['name']} fuer "
         f"die konstruktive Zusammenarbeit waehrend der Pruefung.\n\n"
         + signatures("Adam Kowalczyk", f"Partner / Bieg ly Rewident (PIBR Nr. 12345)",
                      "Deloitte Polska Sp. z o.o.",
                      "Karolina Wisniewska", "Senior Manager Audit",
                      "Deloitte Polska Sp. z o.o.",
                      place="Warschau", date_str_=f"15. April {int(jahr)+1}")),
    ]
    write_doc(f"{BASE}/{fname}", H_RPL,
              f"Management Letter Abschlusspruefung {jahr} – {RPL['name']}",
              subtitle="Pruefer: Deloitte Polska Sp. z o.o. (lokal) / KPMG AG WPG (Konzern)",
              sections=sections, confidential=True)


wp_mgmt_letter("RPL_WP_Management_Letter_2022.docx", "2022", [
    "Inventur-Bestaende SMD-Komponenten zum 31.12.2022: Stichproben-Differenz "
    "0,8 % gegenueber Buchbestand (im akzeptierten Toleranzbereich +/- 1,0 %); "
    "Empfehlung: zusaetzliche Cycle-Counts in Q1/Q3.",
    "Rueckstellung fuer Gewaehrleistungen ICP-3 Plattform: methodische "
    "Aktualisierung der Schadensquoten auf Basis 5-Jahres-Reihe (statt 3 Jahre) "
    "empfohlen; Quantifizierungseffekt ca. PLN 1,8 Mio. (umgesetzt 2023).",
    "Berechtigungen SAP S/4HANA: 4 Faelle mit Doppelrollen (Wareneingangsbuchung "
    "+ Rechnungsfreigabe) identifiziert; Massnahme: Trennung bis 31.03.2023 "
    "umgesetzt; Re-Pruefung bestaetigt.",
    "TP-Dokumentation Local File 2022: termingerecht abgegeben (30.11.2022). "
    "Benchmark-Studie ueberprueft und plausibel; Empfehlung: Aktualisierung "
    "der Vergleichsstudie in 2024 (Drei-Jahres-Turnus).",
    "ZUS-Abgaben Q4/2022 wegen Systemwechsel ZUS-Tool ePlatnik mit eintaegigem "
    "Verzug abgefuehrt; Verzugszinsen PLN 412 (unwesentlich); Prozess in 2023 "
    "stabilisiert.",
    "Latente Steuern auf Investitionsabzug Katowicka SSE: Rechen-Logik "
    "ueberprueft; uebereinstimmend mit Konzern-IFRS-Bilanzierungsrichtlinie "
    "(IAS 12); keine Korrektur.",
])

wp_mgmt_letter("RPL_WP_Management_Letter_2023.docx", "2023", [
    "Vorraete Wareneingang: Re-Klassifizierung von PLN 8,4 Mio. RM-Komponenten "
    "(NXP-Chips) auf 'in Transit' empfohlen (Reisezeit FedEx-Air > 14 Tage); "
    "Reklassifizierung umgesetzt zum 31.12.2023.",
    "Forderungen aus Lieferungen ICP-3 / BMW: Wertberichtigung 'Expected Credit "
    "Losses' (IFRS 9 Stage 1) ueberprueft; Methode angepasst auf "
    "kundenspezifische PD-Werte (S&P Long-Term BBB+ / Aaa-Aa3 Equivalent); "
    "Effekt unwesentlich (< PLN 200k).",
    "Rueckstellung Personal: Urlaubsrueckstellung (zaleglosci urlopowe) zum "
    "31.12.2023 PLN 4,2 Mio. (Vorjahr 3,8 Mio.); Aufbau erklaerbar durch "
    "Wachstum Headcount; Methode unveraendert.",
    "Investitionsfoerderung Katowicka SSE: Antrag fuer Erweiterung Halle 5 "
    "(SMD-Linie 9, geplant 2025) eingereicht 09/2023; geplante steuerliche "
    "Auswirkung ab 2025 (kein Effekt 2023).",
    "ESG-Reporting: Erstmalige Erfassung Scope 1+2 CO2-Daten gemaess GHG "
    "Protocol fuer Konzern-CSRD-Reporting; Datenintegritaet bestaetigt; "
    "Methodische Vorgaben Konzern eingehalten.",
    "Whistleblower-Hinweis Verdacht unzulaessige Zuwendungen Lieferant "
    "(siehe Compliance Report 2023, Hinweis Nr. 3): durch Internal Audit / "
    "KPMG Forensic geprueft; Verdacht nicht erhaertet; sachverhalt geschlossen.",
])


# ─────────────────────────────────────────────────────────────────────────────
# 11) Other misc thin docs (PRJ, REA_FX, REG_to_RSG) — filename-realism leftovers
# ─────────────────────────────────────────────────────────────────────────────

# PRJ-2022-001 Gate G4 Validierung BMS-12 — leftover project doc in PL folder
write_doc(f"{BASE}/PRJ-2022-001_Gate_G4_Validierung_BatteryMS-12_EV_Plattform.docx", H_REA,
          "Stage-Gate-Review G4 (Validierung) – BatteryMS-12 EV-Plattform",
          subtitle="Projekt PRJ-2022-001 / Concept-to-SOP, Gate G4 (Validation Complete)",
          sections=[
              ("Projektkontext",
               "Das Projekt PRJ-2022-001 BatteryMS-12 (BMS-12) ist die Konzern-"
               "Entwicklung des Batteriemanagementsystems Generation 12 fuer die VW-"
               "Plattform-EV (Hauptkunde ID.7-Serie) sowie das Hyundai E-GMP-Programm. "
               "Lead-Werk fuer die Serienfertigung ist Brennhagen Polska Sp. z o.o. (Katowice, "
               "Werkleiter Marek Wojciechowski) mit Linien 3 und 4. Konzept und Software "
               "stammen aus der Brennhagen Software GmbH (Muenchen, Lead Developer Lars Wittmann); "
               "Hardware-Integration durch Brennhagen Elektronik GmbH (Heilbronn)."),
              ("Stage-Gate G4 / Validierungsfreigabe",
               "Das Gate G4 (Validation Complete) ist die formale Freigabe der Produkt- und "
               "Prozessvalidierung vor dem Start-of-Production (SOP) gemaess Konzern-PEP "
               "(Produktentstehungsprozess Brennhagen PEP-2020 Rev. 04). Voraussetzung sind: "
               "(i) erfolgreich abgeschlossene PV/DV (Product Validation / Design Validation), "
               "(ii) PPAP-Level-3 fuer Hauptkunden VW und Hyundai eingereicht und genehmigt, "
               "(iii) Run @ Rate Pruefung im Werk Katowice (8 Stunden / Linientakt erfuellt), "
               "(iv) Q-Berichte FMEA Rev. 07 finalisiert."),
              ("Gate-Review-Ergebnis",
               [
                   ["Gate-Kriterium", "Soll", "Ist", "Status"],
                   ["PPAP-Level VW", "Level 3 freig.", "Level 3 freig. 18.10.2022", "OK"],
                   ["PPAP-Level Hyundai", "Level 3 freig.", "Level 3 freig. 24.10.2022", "OK"],
                   ["Run @ Rate (8 h)", "210 Stk./h", "218 Stk./h Linie 3", "OK"],
                   ["Ausschussquote PV", "<= 0,8 %", "0,62 %", "OK"],
                   ["FMEA Rev. 07", "freigegeben", "freigegeben 30.09.2022", "OK"],
                   ["EMV (IEC 61000-4-x)", "bestanden", "bestanden 12.10.2022", "OK"],
                   ["Funktionssicherheit ASIL D", "TÜV-Bericht freig.", "TÜV SÜD-Bericht 28.10.2022", "OK"],
                   ["MSA Pruefmittel", "Cgk >= 1,33", "Cgk = 1,52", "OK"],
                   ["Werker-Schulung", ">= 95 % geschult", "98 %", "OK"],
               ]),
              ("Entscheidung",
               "Das Gate G4 wird durch das Steering Committee am 04. November 2022 freigegeben. "
               "Naechster Meilenstein: Gate G5 (SOP, Start of Production) am 09. Januar 2023. "
               "Hochlaufkurve Q1/2023: 3.000 → 12.000 Stk./Monat, Volltakt 28.000 Stk./Monat ab "
               "Q3/2023.\n\nFreigeber: CTO (S. Hoffmann), COO (Dr. T. Weber), Werkleiter RPL "
               "(M. Wojciechowski), Lead Customer Account VW (S. Richter CMO/BD).\n\n"
               + signatures("Stefan Hoffmann", "CTO Brennhagen Elektronik AG", R["name"],
                            "Marek Wojciechowski", "Werkleiter RPL", RPL["name"],
                            place="Stuttgart / Katowice", date_str_="04. November 2022")),
          ])


# PRJ-2022-002 Charter — leftover
write_doc(f"{BASE}/PRJ-2022-002_Charter_InfoConnect_Pro_4.0.docx", H_REA,
          "Project Charter PRJ-2022-002 – InfoConnect Pro 4.0 (ICP-4) Generationenwechsel",
          subtitle="Konzern-Innovationsprojekt Infotainment-Generation 4.0 (Folgegeneration ICP-3)",
          sections=[
              ("Projekt-Kurzbeschreibung",
               "Das Projekt PRJ-2022-002 (InfoConnect Pro 4.0, kurz »ICP-4«) ist die Folgegeneration "
               "des heutigen Infotainment-Moduls ICP-3 mit Sprung von Qualcomm Snapdragon 820A auf "
               "die Plattform Snapdragon Ride SA8775P (Aufrueststufe). Zielmaerkte: BMW Neue Klasse "
               "(SOP 2025), Mercedes MMA-Plattform (SOP 2026), Audi PPE/PPC (Option). Lead-Werk "
               "Serie: Brennhagen Polska Sp. z o.o. (Katowice, Linien 1 und 8). Software-Lead: "
               "Brennhagen Software GmbH (Muenchen)."),
              ("Projektziele",
               ("list", [
                   "Time-to-Market: PPAP Submission B-Probe Q1/2024, SOP BMW Q2/2025",
                   "Performance-Sprung: GPU 3,5x, NPU 8x ggue. ICP-3 (Stichworte: AI-In-Cabin, AR-HUD)",
                   "Kostensenkung: Materialkosten -12 % je Einheit (BOM-Optimierung, Konzern-Sourcing)",
                   "Energieeffizienz: durchschnittliche Leistung -22 %, Standby -40 %",
                   "Cybersecurity: UNECE R155/R156 Compliance, ISO/SAE 21434 ab Tag 1",
                   "Plattform-Reuse: 75 % Software-Module aus ICP-3 / Yocto-Linux Basis",
               ])),
              ("Projektorganisation",
               f"Projektleitung: Dr. Petra Hollmann (kommend CTO ab 1.7.2024, vorerst als Programm-"
               f"Sponsor). Operativer PM: Lars Wittmann (RSG, Lead Developer). Werk-Fuehrung "
               f"(RPL Katowice): Marek Wojciechowski / Krzysztof Nowak. Qualitaet: Sabine Brand "
               f"(REG Q-Leitung). Account-Lead BMW: Stefan Richter (CMO/BD). "
               f"Steering Committee tagt monatlich; Stage-Gates G0..G6 gemaess Konzern-PEP."),
              ("Meilensteinplan",
               [
                   ["Gate", "Inhalt", "Zieltermin"],
                   ["G0", "Project Kick-off / Charter Approval", "Q3/2022"],
                   ["G1", "Konzept / Architektur Review", "Q1/2023"],
                   ["G2", "Design Freeze Hardware (A-Probe)", "Q3/2023"],
                   ["G3", "Design Freeze Software (B-Probe)", "Q1/2024"],
                   ["G4", "Validierung (PPAP Submission)", "Q3/2024"],
                   ["G5", "SOP BMW Neue Klasse", "Q2/2025"],
                   ["G6", "Steady State / Closure", "Q1/2026"],
               ]),
              ("Budget und Ressourcen",
               "Geplantes Projektbudget (CAPEX + OPEX): EUR 38,5 Mio. ueber 4 Jahre, davon "
               "EUR 14,8 Mio. CAPEX (Linien-Adaption Katowice Linien 1+8, Pruefstaende, Werkzeuge) "
               "und EUR 23,7 Mio. OPEX (Engineering RSG/REG, Software, Validierung). Headcount "
               "Spitzenlast: 86 FTE (davon 42 RSG, 18 REG, 14 RPL, 12 RCN-Aftermarket). "
               "Foerderpotenzial: BMBF Programm 'Auto-IT' geprueft (Antrag 02/2023)."),
              ("Freigabe",
               "Project Charter ist freigegeben durch Vorstand (Anna Mueller CEO, Stefan Hoffmann "
               "CTO) am 18. August 2022 auf Vorstandssitzung VS-2022-08.\n\n"
               + signatures("Anna Mueller", "CEO Brennhagen Elektronik AG", R["name"],
                            "Stefan Hoffmann", "CTO Brennhagen Elektronik AG", R["name"],
                            place="Stuttgart", date_str_="18. August 2022")),
          ])


# PRJ-2024-001 Pflichtenheft ECU-1000
write_doc(f"{BASE}/PRJ-2024-001_Pflichtenheft_ECU-1000_Concept_Study.docx", H_REA,
          "Pflichtenheft / System Requirements Specification – ECU-1000 Concept Study",
          subtitle="Projekt PRJ-2024-001 Powertrain-ECU Gen4 (Nachfolger ECU-900)",
          sections=[
              ("Dokumenten-Identifikation",
               "Dokument: Pflichtenheft / SyRS ECU-1000\n"
               "Dokumenten-Nr.: SyRS-ECU1000-001 Rev. A (Concept Phase)\n"
               "Projekt: PRJ-2024-001 ECU-1000 Concept Study\n"
               "Status: Concept-Phase Pflichtenheft, NICHT freigegeben fuer Serienentwicklung\n"
               "Erstellt: 14. Maerz 2024 (RSG Muenchen, Lars Wittmann)\n"
               "Review: 28. Maerz 2024 (Engineering, Werkleitung RPL Katowice, OEM-Repraesentanz)\n"
               "Naechster Schritt: Konzept-Gate G1 voraussichtlich Q3/2024."),
              ("Zweck und Geltungsbereich",
               "Das vorliegende Pflichtenheft beschreibt die Anforderungen an den Powertrain-ECU "
               "der Generation 4 (»ECU-1000«), den geplanten Nachfolger des heutigen ECU-900. "
               "Ziel: Skalierbare ECU-Plattform fuer 800V-EV-Architekturen (VW SSP, Stellantis "
               "STLA-Large, Mercedes MMA, ggf. BMW Neue Klasse) mit Software-Defined-Vehicle "
               "(SDV) Faehigkeiten, OTA-Updates und Service-orientierter Architektur (SOA). "
               "Lead-Werk fuer Serie: RPL Katowice (Linien 2 und 5, vorgesehen ab Linie 9 nach "
               "Werkserweiterung)."),
              ("Funktionale Anforderungen",
               ("list", [
                   "Recheneinheit: Multi-Core ARM Cortex-A78 + Lockstep-Pair Cortex-R52 (ASIL D)",
                   "Speicher: 16 GB LPDDR5, 256 GB eMMC, 64 MB Boot-Flash",
                   "Konnektivitaet: 4x Gigabit Automotive Ethernet, 8x CAN-FD, 4x LIN, 1x FlexRay",
                   "Sicherheitsbaustein: Infineon AURIX TC4xx (HSM), separater Boot-ROM",
                   "Stromversorgung: 12V Bordnetz + 48V optional, DC/DC integriert",
                   "Betriebssystem: AUTOSAR Adaptive Platform R23-11, Hypervisor (QNX/Pikevisor)",
                   "Cybersecurity: UN R155/R156, ISO/SAE 21434, sichere Boot-Kette",
                   "OTA: Container-basierte Updates (OCI), Rollback-Garantie",
               ])),
              ("Nicht-funktionale Anforderungen",
               ("list", [
                   "Temperaturbereich: -40 ... +105 °C (Junction-Temp.), Lebensdauer 15 Jahre",
                   "EMV: gemaess CISPR 25, ISO 11452-x (Klasse 5)",
                   "Functional Safety: ASIL D Decomposition; ISO 26262 Pruefung TUV SUD",
                   "Cybersecurity: ISO/SAE 21434 + UN R155 / R156 (Type Approval)",
                   "Performance: Bootzeit <= 1,5 s in App-Layer, OTA-Update <= 30 min",
                   "Power Budget: < 35 W typ., < 65 W max., Standby < 50 mW",
                   "Materialkosten Ziel BOM: ca. EUR 380 (-22 % ggue. ECU-900)",
               ])),
              ("Schnittstellen / Stakeholder",
               "Beteiligte Konzerngesellschaften und Rollen: RSG Muenchen (Software-Lead, Lars "
               "Wittmann); REG Heilbronn (Hardware-Entwicklung); RPL Katowice (Serienfertigung); "
               "RCN Shanghai (Asien-Vertrieb / Lokalanpassung); Konzern-CTO ab 1.7.2024 "
               "Dr. Petra Hollmann (Programm-Sponsor)."),
              ("Naechste Schritte",
               "1. Begutachtung Pflichtenheft durch externe Reviewer (Continental, Bosch via "
               "Hengeler Mueller-NDA) Q2/2024.\n"
               "2. Konzept-Gate G1 mit Steering Committee Q3/2024.\n"
               "3. Lieferanten-Vorqualifizierung (Halbleiter Infineon/NXP/Qualcomm) Q3-Q4/2024.\n"
               "4. RFP-Versand an OEM-Kunden VW/Mercedes Q4/2024.\n\n"
               + signatures("Lars Wittmann", "Lead Developer RSG", "Brennhagen Software GmbH",
                            "Dr. Petra Hollmann", "Designated CTO REA (ab 1.7.2024)", R["name"],
                            place="Muenchen / Stuttgart", date_str_="14. Maerz 2024")),
          ])


# REA_FX_Hedge_EUR_HUF_2022_Q4 — leftover treasury doc misfiled in PL folder
write_doc(f"{BASE}/REA_FX_Hedge_EUR_HUF_2022_Q4.docx", H_REA,
          "FX-Hedge-Quartalsbericht EUR/HUF – Q4 2022",
          subtitle=f"Konzern-Treasury Quartalsbericht (Markus Pflanzer, Group Treasurer)",
          sections=[
              ("Berichtsgegenstand",
               "Dieser Bericht dokumentiert die EUR/HUF-Hedging-Aktivitaeten der Brennhagen "
               "Elektronik AG (Konzern-Treasury, Frankfurt) im Berichtsquartal Q4 2022. "
               "Hedging-Underlying ist die operative HUF-Exposure der ungarischen Tochter "
               "Brennhagen Hungary Kft. (RHU, Gyor) aus Personalkosten, Versorgerrechnungen und "
               "lokalen Lieferantenbeziehungen. Hinweis: Dieser Bericht ist in der Datenraum-"
               "Indexrevision aus dem PL-Ordner in den korrekten Treasury-Ordner zu verlagern."),
              ("Exposure und Hedging-Strategie",
               "Operative HUF-Exposure RHU Q4 2022 (Auszahlungen netto): ca. HUF 2,9 Mrd. "
               "(entspricht EUR 7,2 Mio. zum NBH-Mittelkurs 31.12.2022 von ca. 400 HUF/EUR). "
               "Hedging-Ziel-Quote gemaess Konzern-Treasury-Richtlinie 2021: 80 % der "
               "12-Monats-Forward-Exposure. Hedging-Instrumente: FX Forward (3M / 6M / 12M "
               "rollend) und FX Option Collars (Floor/Cap) bei UniCredit Bank AG und BNP Paribas."),
              ("Q4 2022 Hedging-Transaktionen",
               [
                   ["Trade-Date", "Instrument", "Counterparty", "Volumen", "Rate", "Maturity"],
                   ["05.10.2022", "EUR/HUF Forward Sale", "UniCredit", "HUF 800 Mio.", "418,40", "05.04.2023"],
                   ["18.10.2022", "EUR/HUF Forward Sale", "BNP Paribas", "HUF 600 Mio.", "421,80", "18.04.2023"],
                   ["09.11.2022", "EUR/HUF Forward Sale", "Deutsche Bank", "HUF 900 Mio.", "412,10", "09.05.2023"],
                   ["28.11.2022", "EUR/HUF Collar 6M", "UniCredit", "EUR 4,0 Mio.", "Cap 425 / Floor 395", "28.05.2023"],
                   ["12.12.2022", "EUR/HUF Forward Sale", "BNP Paribas", "HUF 700 Mio.", "405,60", "12.06.2023"],
               ]),
              ("Mark-to-Market und Hedging-Effektivitaet",
               "Mark-to-Market der EUR/HUF-Hedges zum 31.12.2022: positives Hedge-Asset von "
               "EUR 0,42 Mio. (Vorquartal EUR -0,18 Mio.). Hedging-Effektivitaet gemaess "
               "IFRS 9 retrospektiv getestet: 96,4 % (Toleranzgrenze 80-125 %; effektiv). "
               "Cash Flow Hedge Accounting (CFH) angewendet; OCI-Effekt netto nach Steuern "
               "ca. EUR 0,29 Mio. (positiv).\n\nKein Hedge-De-Designation in Q4 2022. "
               "Counterparty-Risk gemaess Konzernrichtlinie auf 5 Hausbanken diversifiziert."),
              ("Ausblick",
               "Fuer 2023 wird die EUR/HUF-Volatilitaet weiter erhoeht erwartet (Inflation HU "
               "20+ %, MNB-Leitzins 13 %). Empfehlung: Hedging-Quote von 80 % auf 90 % erhoehen, "
               "ggf. mehrjaehrige Forward-Strip-Strategie. Themen-Pipeline: Sustainability-"
               "linked FX-Hedges (ESG-Tilt), HUF-Funding via Auslandsanleihe pruefen.\n\n"
               + signatures("Markus Pflanzer", "Group Treasurer", R["name"],
                            "Laura Bauer", "CFO", R["name"],
                            place="Stuttgart", date_str_="15. Januar 2023")),
          ])


# REG_to_RSG_IC_2023_11 — leftover internal-IC doc in PL folder
write_doc(f"{BASE}/REG_to_RSG_IC_2023_11.docx", H_REA,
          "IC-Rechnung November 2023: Brennhagen Elektronik GmbH an Brennhagen Software GmbH",
          subtitle="Rechnungs-Nr. REG-RSG-IC-2023-11 / Engineering-Leistungen Embedded Systems",
          sections=[
              ("Hinweis Datenraum-Ablage",
               "Dieses Dokument betrifft eine Intercompany-Verrechnung zwischen Brennhagen "
               "Elektronik GmbH (REG, Heilbronn) und Brennhagen Software GmbH (RSG, Muenchen) "
               "und wurde im Zuge der Dateneingangs-Massnahme fehlhaft in den Ordner "
               "05_Tochter_PL_Katowice abgelegt. Die Datenraum-Indexrevision verschiebt das "
               "Dokument in den korrekten Konzern-IC-Ordner."),
              ("Lieferant und Empfaenger",
               "Lieferantin (Rechnungsstellerin): Brennhagen Elektronik GmbH (REG), "
               "Gottlieb-Daimler-Strasse 24, 74172 Neckarsulm-Heilbronn, HRB 221456 AG "
               "Heilbronn, USt-IdNr. DE 287 645 109. Werkleiter: Andreas Maier. Bankverbindung "
               "Volksbank Heilbronn IBAN DE89 6209 0100 0124 5678 12.\n\n"
               "Empfaengerin: Brennhagen Software GmbH (RSG), Landsberger Strasse 110, "
               "80339 Muenchen, HRB 319872 AG Muenchen, USt-IdNr. DE 312 887 765. "
               "Ansprechpartner: Werkleiter Dr. Klaus Kessler, Lead Developer Lars Wittmann."),
              ("Rechnungsangaben",
               "Rechnungsnummer: REG-RSG-IC-2023-11\nRechnungsdatum: 30. November 2023\n"
               "Leistungsmonat: November 2023\nWaehrung: EUR (Konzern-IC-Konvention)\n"
               "Faelligkeit: 60 Tage netto (Faelligkeit 29.01.2024)\n"
               "Verrechnungsbasis: Konzern-Service-Level-Agreement REG-RSG-SLA-2022, "
               "Stundensatz Engineering EUR 142 (Cost-Plus 7 % gemaess TP-Richtlinie 2018)."),
              ("Leistungsuebersicht",
               [
                   ["Pos", "Leistung", "Stunden", "Stundensatz", "Netto (EUR)"],
                   ["1", "ASIC-Bringup ICP-3 Plattform (Engineering Support)", "180", "142,00", "25.560,00"],
                   ["2", "EMV-Beratung Mess-Setup Anechoic Chamber", "62", "142,00", "8.804,00"],
                   ["3", "Werkzeug-/Pruefmittelbereitstellung (Leihstellung)", "—", "—", "4.200,00"],
                   ["4", "Reisekosten Lars Wittmann/Team Heilbronn (4 Termine)", "—", "—", "3.840,00"],
                   ["", "Summe (netto)", "", "", "42.404,00"],
               ]),
              ("Steuer und Hinweise",
               "Innerdeutsche Lieferung. USt 19 % wird gesondert berechnet (EUR 8.056,76). "
               "Bruttobetrag EUR 50.460,76. Reverse-Charge nicht anwendbar (Inland). Buchung "
               "in SAP S/4HANA Buchungskreis DE20 (REG) / DE30 (RSG). Konzern-IC-Matching "
               "ueber Group Reporting.\n\n"
               + signatures("Andreas Maier", "Werkleiter REG", "Brennhagen Elektronik GmbH",
                            "Dr. Klaus Kessler", "Werkleiter RSG", "Brennhagen Software GmbH",
                            place="Heilbronn / Muenchen", date_str_="30. November 2023")),
          ])


# ─────────────────────────────────────────────────────────────────────────────
# Done.
# ─────────────────────────────────────────────────────────────────────────────
print("All RPL Katowice thin docs regenerated.")
