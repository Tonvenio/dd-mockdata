"""Müller / 02_Finanzen – 21 thin docs."""
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

BASE = f"{_ROOT}/mueller_small/02_Finanzen"
H = {"name": M["name"], "addr": M["addr"], "hrb": M["hrb"]}


# ── FIN_BWA_2021_12 (Stub xlsx-Platzhalter) ─────────────────────────────────
write_doc(
    f"{BASE}/FIN_BWA_2021_12_Dez.xlsx_placeholder.docx", H,
    "Betriebswirtschaftliche Auswertung (BWA) – Dezember 2021",
    subtitle="Kurzfassung – ausgelagerte Detailauswertung siehe FIN_BWA_2021_12_Dez.xlsx",
    sections=[
        ("Hinweis",
         "Diese Datei stellt die Begleitnotiz zur monatlichen BWA Dezember 2021 dar. Die vollstaendige "
         "Aufstellung mit Konten- und Kostenstellenstruktur befindet sich in der dazugehoerigen "
         "Excel-Datei FIN_BWA_2021_12_Dez.xlsx (DATEV-Export, Mandantennr. 47312)."),
        ("1. Eckzahlen Dezember 2021 (Monatswerte)",
         [
             ["Position", "Dez 2021", "Plan Dez 2021", "Abweichung", "kum. 2021"],
             ["Umsatzerloese", "3.812.000 EUR", "3.500.000 EUR", "+8,9 %", "41.900.000 EUR"],
             ["Materialaufwand", "1.910.000 EUR", "1.820.000 EUR", "+4,9 %", "21.700.000 EUR"],
             ["Personalaufwand", "1.156.000 EUR", "1.150.000 EUR", "+0,5 %", "13.580.000 EUR"],
             ["Sonst. betr. Aufwand", "287.000 EUR", "275.000 EUR", "+4,4 %", "3.420.000 EUR"],
             ["EBITDA", "459.000 EUR", "255.000 EUR", "+80,0 %", "4.800.000 EUR"],
             ["AfA", "152.000 EUR", "150.000 EUR", "+1,3 %", "1.850.000 EUR"],
             ["EBIT", "307.000 EUR", "105.000 EUR", "+192,4 %", "2.950.000 EUR"],
             ["Zinsergebnis", "-22.000 EUR", "-25.000 EUR", "+12,0 %", "-260.000 EUR"],
             ["Ergebnis vor Steuern", "285.000 EUR", "80.000 EUR", "+256,3 %", "2.690.000 EUR"],
         ]),
        ("2. Kommentar Finanzleitung (Sandra Becker)",
         "Der Dezember verzeichnet erwartungsgemaess einen hohen Auslieferungsschub fuer die Auftraege "
         "Bosch Rexroth AG (Pressenlinie PL-500, 1,2 Mio. EUR) und Dürr AG (Foerderbandanlage FB-200 Linie 2, "
         "0,8 Mio. EUR). Materialaufwand leicht ueber Plan aufgrund Sondereinkauf Wolfram-Komponenten "
         "(Lieferengpass Trumpf SE + Co. KG). Personalaufwand weitgehend planmaessig.\n\n"
         "Liquiditaet zum 31.12.2021: Bestand auf Geschaeftskonto Deutsche Bank AG 4,21 Mio. EUR; "
         "Kontokorrentlinie 5,0 Mio. EUR unbeansprucht. Forderungen aus L+L: 7,82 Mio. EUR "
         "(DSO 58 Tage, Vorjahr 61 Tage). Wertberichtigungen: 95.000 EUR (Pauschal 1 %)."),
        ("3. Anlagen",
         "Anlage 1: BWA-Excel DATEV-Export (FIN_BWA_2021_12_Dez.xlsx)\n\n"
         "Anlage 2: Forderungsstrukturliste 31.12.2021\n\n"
         "Anlage 3: Liquiditaetsplan Q1/2022"),
    ],
)


# ── FIN_Jahresabschluss_2021_Kurzfassung ────────────────────────────────────
write_doc(
    f"{BASE}/FIN_Jahresabschluss_2021_Kurzfassung.docx", H,
    "Jahresabschluss 2021 – Kurzfassung",
    subtitle="Halbreiter Maschinenbau GmbH – Geschaeftsjahr 1. Januar bis 31. Dezember 2021",
    sections=[
        ("1. Allgemeine Angaben",
         "Der Jahresabschluss wurde gemaess den Vorschriften des Handelsgesetzbuchs (HGB) und unter "
         "ergaenzender Anwendung der Vorschriften des GmbH-Gesetzes aufgestellt. Die Gesellschaft "
         "ist eine mittelgrosse Kapitalgesellschaft im Sinne des § 267 Abs. 2 HGB. Die Pruefung erfolgte "
         "durch die BDO AG Wirtschaftspruefungsgesellschaft, Koeln; der Bestaetigungsvermerk wurde am "
         "29. April 2022 uneingeschraenkt erteilt."),
        ("2. Bilanz 31.12.2021 (verkuerzt)",
         [
             ["Aktiva", "31.12.2021 EUR", "31.12.2020 EUR", "Passiva", "31.12.2021 EUR", "31.12.2020 EUR"],
             ["Immaterielle VG", "210.000", "180.000", "Gez. Kapital", "250.000", "250.000"],
             ["Sachanlagen", "12.450.000", "12.080.000", "Gewinnruecklagen", "12.110.000", "10.730.000"],
             ["Finanzanlagen", "320.000", "280.000", "Bilanzgewinn", "1.040.000", "1.420.000"],
             ["Vorraete", "6.890.000", "6.420.000", "Rueckstellungen", "4.180.000", "3.860.000"],
             ["Forderungen L+L", "5.310.000", "5.580.000", "Verbindlichkeiten Banken", "5.640.000", "6.210.000"],
             ["Liquide Mittel", "2.120.000", "1.760.000", "Verb. L+L", "3.760.000", "3.180.000"],
             ["Sonst. Aktiva", "200.000", "240.000", "Sonst. Passiva", "520.000", "490.000"],
             ["SUMME", "27.500.000", "26.540.000", "SUMME", "27.500.000", "26.540.000"],
         ]),
        ("3. Gewinn- und Verlustrechnung 2021 (verkuerzt)",
         [
             ["Position", "2021 EUR", "2020 EUR", "Veraenderung"],
             ["Umsatzerloese", "41.900.000", "39.800.000", "+5,3 %"],
             ["Bestandsveraenderung", "230.000", "180.000", "+27,8 %"],
             ["Gesamtleistung", "42.130.000", "39.980.000", "+5,4 %"],
             ["Materialaufwand", "21.700.000", "20.650.000", "+5,1 %"],
             ["Personalaufwand", "13.580.000", "13.020.000", "+4,3 %"],
             ["Sonst. betr. Aufwand", "3.420.000", "3.260.000", "+4,9 %"],
             ["EBITDA", "4.800.000", "4.150.000", "+15,7 %"],
             ["AfA", "1.850.000", "1.770.000", "+4,5 %"],
             ["EBIT", "2.950.000", "2.380.000", "+23,9 %"],
             ["Zins-/Beteiligungsergebnis", "-260.000", "-300.000", "+13,3 %"],
             ["Steuern v. Eink. u. Ertrag", "-620.000", "-360.000", "+72,2 %"],
             ["Jahresueberschuss", "2.070.000", "1.720.000", "+20,3 %"],
         ]),
        ("4. Lagebericht (Auszuege)",
         "Die Gesellschaft hat das Geschaeftsjahr 2021 trotz fortdauernder Verwerfungen in den globalen "
         "Lieferketten erfolgreich bewaeltigt. Materialengpaesse bei elektronischen Komponenten "
         "(insbesondere Antriebssteuerungen) konnten durch fruehzeitige Bevorratung und enge Abstimmung "
         "mit den Lieferanten Siemens AG, Trumpf SE + Co. KG und Schunk GmbH & Co. KG kompensiert werden. "
         "Wesentliche Risiken bestehen weiterhin im Energiepreisbereich.\n\n"
         "Der Auftragsbestand zum 31.12.2021 belaeuft sich auf 14,8 Mio. EUR (Vorjahr 12,3 Mio. EUR). "
         "Die Mehrheit der Auftragseingaenge entfaellt auf die Schluesselkunden ThyssenKrupp Steel Europe AG, "
         "Bosch Rexroth AG, Hella GmbH & Co. KGaA, Viessmann Climate Solutions SE und Dürr AG.\n\n"
         "Ausblick: Geschaeftsfuehrung erwartet fuer 2022 ein moderates Umsatzwachstum von rund 3-5 %, "
         "EBITDA-Marge stabil im Bereich 11-12 %."),
        ("5. Ergebnisverwendung",
         "Vom Jahresueberschuss 2021 in Hoehe von 2.070.000 EUR werden 1.270.000 EUR in die "
         "anderen Gewinnruecklagen eingestellt; die verbleibenden 800.000 EUR werden als "
         "Ausschuettung an die Gesellschafter ausgekehrt (Beschluss vom 23.06.2022)."),
        ("Unterschriften",
         signatures("Klaus Mueller", "Geschaeftsfuehrer", M["name"],
                    "Sandra Becker", "Geschaeftsfuehrerin / CFO", M["name"],
                    place="Koeln", date_str_="20. April 2022")),
    ],
)


# ── Reisekostenabrechnung GF1 Q1 2024 ───────────────────────────────────────
write_doc(
    f"{BASE}/Reisekostenabrechnung_GF1_Q1_2024.docx", H,
    "Reisekostenabrechnung – Geschaeftsfuehrer Klaus Mueller – Q1/2024",
    subtitle="Berichtszeitraum: 1. Januar bis 31. Maerz 2024",
    sections=[
        ("Reisen im Berichtszeitraum",
         [
             ["Nr.", "Datum", "Anlass / Kunde", "Ziel", "VerkM", "uebernacht.", "Verpfleg.", "sonst.", "Summe EUR"],
             ["1", "11.-12.01.2024", "Strategiegespraech Bosch Rexroth", "Stuttgart-Lohr", "PKW (412 km)", "189", "56", "32", "548,40"],
             ["2", "18.01.2024", "Hannover Messe Vorgespraech", "Hannover", "Bahn 1. Kl.", "0", "28", "8", "342,20"],
             ["3", "23.01.2024", "ThyssenKrupp Steel Europe – Auftaktsitzung", "Duisburg", "PKW (118 km)", "0", "28", "0", "94,40"],
             ["4", "5.-8.02.2024", "Messe Euroguss / Branchenvertretung", "Nuernberg", "Bahn 1. Kl.", "640", "168", "78", "1.282,50"],
             ["5", "14.02.2024", "Hella GmbH – Quartalsmeeting", "Lippstadt", "PKW (138 km)", "0", "28", "0", "108,40"],
             ["6", "27.-29.02.2024", "Investorengespraeche", "Frankfurt a. M.", "Bahn 1. Kl.", "412", "112", "44", "1.018,80"],
             ["7", "11.-12.03.2024", "Beiratssitzung Heidelberg", "Heidelberg", "PKW (282 km)", "165", "56", "12", "458,40"],
             ["8", "18.03.2024", "Dürr AG – Vertragsverhandlung", "Bietigheim-Bissingen", "Bahn 1. Kl.", "0", "28", "0", "284,40"],
             ["9", "25.-27.03.2024", "MES-Anbieter-Praesentation", "Muenchen", "Bahn 1. Kl.", "312", "112", "28", "884,40"],
             ["", "SUMME", "", "", "", "1.718,00", "616,00", "202,00", "5.021,90"],
         ]),
        ("Erlaeuterungen",
         "Verkehrsmittelwahl gemaess Reisekostenrichtlinie der Gesellschaft (Stand 01.01.2023): Bahn 1. Klasse, "
         "Flug ab 600 km Direktstrecke. Verpflegungsmehraufwand pauschal nach EStG (28 EUR / 14 EUR). "
         "Eigenes Fahrzeug mit 0,30 EUR/km abgerechnet, soweit kein Dienstwagen verwendet wurde "
         "(Sondersituation: Reparatur GF-Dienstwagen 18.-30.01.2024).\n\n"
         "Saemtliche Belege liegen digitalisiert im Rechnungswesen vor (DATEV Belegwesen). Die "
         "Abrechnung wurde durch die Personalabteilung (Frau Andrea Hoffmann) sachlich und rechnerisch geprueft."),
        ("Genehmigung",
         signatures("Sandra Becker", "Geschaeftsfuehrerin / CFO", M["name"],
                    "Andrea Hoffmann", "Leiterin Personal & Verwaltung", M["name"],
                    place="Koeln", date_str_="4. April 2024")),
    ],
)


# ── FIN_Leasingvertrag_Fuhrpark_2023 ────────────────────────────────────────
write_doc(
    f"{BASE}/FIN_Leasingvertrag_Fuhrpark_2023.docx", H,
    "Leasingvertrag Fuhrpark 2023 – Mercedes-Benz Bank AG",
    subtitle="Rahmenvereinbarung Nr. MBBK-2023-MMB-014 vom 12. Mai 2023",
    sections=[
        ("Vertragsparteien",
         "Leasinggeberin: Mercedes-Benz Bank AG, Siemensstrasse 7, 70469 Stuttgart, vertreten durch "
         "den Vorstand.\n\n"
         "Leasingnehmerin: Halbreiter Maschinenbau GmbH, Industriestrasse 12, 50829 Koeln, "
         "HRB 47312 AG Koeln."),
        ("Gegenstand",
         "Diese Rahmenvereinbarung regelt die Konditionen fuer das im Anhang 1 aufgefuehrte "
         "Fahrzeugleasing fuer den Aussendienst, Vertrieb und die Geschaeftsfuehrung der Leasingnehmerin "
         "(insgesamt 22 Fahrzeuge der Marke Mercedes-Benz; davon 8 PKW C-Klasse, 6 PKW E-Klasse, "
         "2 PKW GLC, 1 PKW S-Klasse, 5 Nutzfahrzeuge Vito Tourer). Die Einzelvertraege werden auf "
         "Basis dieser Rahmenvereinbarung abgeschlossen."),
        ("Konditionen",
         ("clauses", [
             ("§ 1 Laufzeit", [
                 "Die Rahmenvereinbarung gilt vom 1. Juni 2023 bis 31. Mai 2027.",
                 "Einzelvertraege werden auf 48 Monate (Standardvertrag) oder 36 Monate (Geschaeftsfuehrung) "
                 "abgeschlossen mit jeweils 80.000 km Laufleistung p. a.",
             ]),
             ("§ 2 Leasingraten", [
                 "Die Leasingrate je Fahrzeug richtet sich nach der individuellen Konfiguration; "
                 "Basis ist die Mercedes-Benz Standard-Fleet-Rate (Sonderkonditionen Bestandskunde, "
                 "Rabatt 14 %).",
                 "Voraussichtliches Gesamtleasingvolumen pro Jahr: 412.000 EUR (netto).",
             ]),
             ("§ 3 Versicherung und Schaden", [
                 "Vollkasko mit Selbstbeteiligung 500 EUR; Haftpflicht ueber Allianz SE im Rahmen "
                 "der Fuhrparkversicherung der Leasingnehmerin.",
             ]),
             ("§ 4 Rueckgabe", [
                 "Rueckgabe-Bewertung nach VDA-Standard. Sondernutzung / Schaeden ueber Mehrwertabnutzung "
                 "werden gesondert berechnet.",
             ]),
             ("§ 5 Elektromobilitaet", [
                 "Im Rahmenkontingent ist eine Wandlungsoption fuer bis zu 6 Fahrzeuge auf rein "
                 "elektrische Antriebe (EQ-Modelle) vorgesehen; konkret in Planung: 4 Fahrzeuge EQE "
                 "im H2/2025.",
             ]),
         ])),
        ("Anlagen",
         "Anlage 1: Fahrzeugliste mit Konfiguration\n\n"
         "Anlage 2: Allgemeine Geschaeftsbedingungen Leasing\n\n"
         "Anlage 3: Restwerttabelle"),
        ("Unterschriften",
         signatures("Sandra Becker", "Geschaeftsfuehrerin", M["name"],
                    "Markus Helmer", "Fleet Account Manager", "Mercedes-Benz Bank AG",
                    place="Koeln/Stuttgart", date_str_="12. Mai 2023")),
    ],
)


# ── Jahresabschluss_Kennzahlenblatt_2023 ────────────────────────────────────
write_doc(
    f"{BASE}/Jahresabschluss_Kennzahlenblatt_2023.docx", H,
    "Kennzahlenblatt Jahresabschluss 2023",
    subtitle="Halbreiter Maschinenbau GmbH – Stand 7. Mai 2024",
    sections=[
        ("Ueberblick",
         "Das Geschaeftsjahr 2023 verlief mit einer Umsatzsteigerung um 12,4 % auf 48,63 Mio. EUR "
         "deutlich ueber Plan. Wesentliche Treiber waren der Einstieg der Bosch Rexroth AG mit zwei "
         "Pressenlinien (PL-500), eine signifikante Volumenerhoehung bei der Dürr AG sowie das Anlaufen "
         "der neuen Laserschneidanlage LS-800 fuer Hella GmbH & Co. KGaA. EBITDA stieg ueberproportional "
         "auf 5,98 Mio. EUR (Marge 12,3 %)."),
        ("Kennzahlen",
         [
             ["KPI", "2023", "2022", "2021", "Trend"],
             ["Umsatzerloese (EUR)", "48,63 Mio.", "43,25 Mio.", "41,90 Mio.", "+"],
             ["EBITDA (EUR)", "5,98 Mio.", "5,10 Mio.", "4,80 Mio.", "+"],
             ["EBITDA-Marge", "12,3 %", "11,8 %", "11,5 %", "+"],
             ["EBIT (EUR)", "3,89 Mio.", "3,22 Mio.", "2,95 Mio.", "+"],
             ["EBIT-Marge", "8,0 %", "7,4 %", "7,0 %", "+"],
             ["Jahresueberschuss", "2,73 Mio.", "2,22 Mio.", "2,07 Mio.", "+"],
             ["Bilanzsumme", "31,20 Mio.", "28,40 Mio.", "27,30 Mio.", "+"],
             ["Eigenkapital", "16,90 Mio.", "14,10 Mio.", "13,40 Mio.", "+"],
             ["EK-Quote", "54,2 %", "49,6 %", "49,1 %", "+"],
             ["Nettoverschuldung", "1,84 Mio.", "3,40 Mio.", "3,85 Mio.", "+"],
             ["Mitarbeiter (FTE)", "247", "231", "218", "+"],
             ["Umsatz pro FTE (EUR)", "196.880", "187.230", "192.200", "~"],
             ["Investitionen", "2,80 Mio.", "1,90 Mio.", "1,40 Mio.", "+"],
             ["F&E-Quote", "4,1 %", "3,8 %", "3,5 %", "+"],
             ["Auftragsbestand 31.12.", "16,40 Mio.", "13,90 Mio.", "14,80 Mio.", "+"],
             ["Working Capital", "6,90 Mio.", "5,80 Mio.", "5,40 Mio.", "+"],
             ["DSO (Tage)", "54", "57", "58", "+"],
             ["DPO (Tage)", "39", "37", "36", "+"],
             ["Lagerumschlag (Tage)", "84", "92", "94", "+"],
             ["ROCE", "21,4 %", "17,9 %", "16,3 %", "+"],
             ["Krankenstand", "3,2 %", "3,5 %", "3,8 %", "+"],
             ["Reklamationsquote", "0,68 %", "0,84 %", "1,02 %", "+"],
         ]),
        ("Erlaeuterungen",
         "Verhaeltniszahlen sind auf Basis HGB-Einzelabschluss berechnet. Investitionen 2023 enthalten "
         "Sondereffekte aus der Erweiterung der Laserschneidanlage LS-800 (640 TEUR) und dem Hallenkran "
         "in Halle B (185 TEUR). Reklamationsquote berechnet als Anzahl reklamierter Auftraege / Anzahl "
         "ausgelieferter Auftraege. Quelle: SAP S/4HANA (FI/CO/QM) sowie BWA-Auswertungen DATEV."),
    ],
)


# ── Bankbuergschaft_Exportgarantie_2023 ─────────────────────────────────────
write_doc(
    f"{BASE}/Bankbürgschaft_Exportgarantie_2023.docx", H,
    "Bankbuergschaft / Exportgarantie – Deutsche Bank AG / Auftrag Dürr AG Mexiko",
    subtitle="Buergschaftsurkunde Nr. DB-MMB-2023-EXP-018 vom 17. Juli 2023",
    sections=[
        ("Buergin",
         "Deutsche Bank AG, Taunusanlage 12, 60325 Frankfurt am Main, vertreten durch die Filiale Koeln, "
         "handelnd fuer die Halbreiter Maschinenbau GmbH als Auftraggeberin."),
        ("Beguenstigter",
         "Dürr AG, Carl-Benz-Strasse 34, 74321 Bietigheim-Bissingen, fuer Lieferungen im Rahmen des "
         "Auftrages PL-MX-2023-014 (Pressenlinie PL-500 fuer das Werk Queretaro, Mexiko)."),
        ("Buergschaftsumme und -art",
         "Buergschaftsumme: 1.450.000,00 EUR (eine Mio. vierhundertfuenfzigtausend Euro).\n\n"
         "Art: Anzahlungsbuergschaft (Advance Payment Bond) und Vertragserfuellungsbuergschaft (Performance Bond) "
         "in kombinierter Form, gemaess URDG 758 (ICC Uniform Rules for Demand Guarantees, Revision 2010)."),
        ("Konditionen",
         "Avalprovision: 1,2 % p. a. bezogen auf die Buergschaftsumme; Mindestprovision 350 EUR pro Quartal. "
         "Sicherheit: Anrechnung auf die mit der Bank vereinbarte Aval-Linie von 3,5 Mio. EUR (aktuell "
         "ausgeschoepft 2,2 Mio. EUR). Laufzeit: bis zum Bauzeitenende plus 12 Monate Gewaehrleistung, "
         "spaetestens 31. Januar 2026."),
        ("Auszahlungsmodalitaet",
         "Die Buergschaft ist auf erstes Anfordern zahlbar (Garantie auf erstes Anfordern). Eine Auszahlung "
         "erfolgt gegen Vorlage einer schriftlichen Aufforderung des Beguenstigten unter Beifuegung einer "
         "Erklaerung, dass die Auftraggeberin ihren Vertragspflichten nicht ordnungsgemaess nachgekommen ist. "
         "Einwendungen aus dem Grundverhaeltnis sind ausgeschlossen."),
        ("Anwendbares Recht / Streitbeilegung",
         "Anwendbares Recht: deutsches Recht unter Ausschluss des UN-Kaufrechts. Gerichtsstand: "
         "Frankfurt am Main."),
        ("Unterschriften",
         signatures("Dr. Friedhelm Stuetzel", "Senior Account Manager", "Deutsche Bank AG",
                    "Sandra Becker", "Geschaeftsfuehrerin / CFO", M["name"],
                    place="Koeln / Frankfurt a. M.", date_str_="17. Juli 2023")),
    ],
)


# ── Factoring_Rahmenvertrag_2023 ────────────────────────────────────────────
write_doc(
    f"{BASE}/Factoring_Rahmenvertrag_2023.docx", H,
    "Factoring-Rahmenvertrag 2023 – Targo Commercial Finance AG",
    subtitle="Vertrag Nr. TCF-2023-MMB-0091 vom 11. April 2023",
    sections=[
        ("Vertragsparteien",
         "Factor: Targo Commercial Finance AG, Postfach 10 22 80, 40013 Duesseldorf.\n\n"
         "Anschlusskunde: Halbreiter Maschinenbau GmbH, Industriestrasse 12, 50829 Koeln."),
        ("Praeambel",
         "Im Rahmen der Optimierung des Working Capital schliesst die Halbreiter Maschinenbau GmbH einen "
         "echten Factoringvertrag (true sale) mit Uebernahme des Delkredererisikos (non-recourse) zur "
         "Liquiditaetssicherung des Auslandsgeschaeftes ab. Die einbezogenen Debitoren werden im Anhang 1 "
         "abschliessend gelistet (Anlage 'Debitorenkreis')."),
        ("Konditionen",
         ("clauses", [
             ("§ 1 Eingeraeumter Factoringrahmen", [
                 "Der Factor stellt einen Rahmen von 5,0 Mio. EUR (rollierend) zur Verfuegung.",
                 "Der Vorschuss betraegt 90 % der angekauften Forderung; Restkaufpreis (10 %) "
                 "wird nach Eingang der Zahlung beim Factor freigegeben.",
             ]),
             ("§ 2 Factoringgebuehr und Zinsen", [
                 "Factoringgebuehr: 0,42 % je angekaufter Forderung.",
                 "Vorfinanzierungszins: EURIBOR 3M + 1,75 % p. a., berechnet auf Tagesbasis.",
                 "Bonitaetspruefung: jaehrliche Pauschale 8.500 EUR.",
             ]),
             ("§ 3 Debitorenkreis", [
                 "Eingeschlossen sind Forderungen gegenueber Debitoren mit Sitz innerhalb der EU sowie "
                 "den USA, der Schweiz, dem Vereinigten Koenigreich, Mexiko und der Republik Korea.",
                 "Ausgeschlossen sind Forderungen gegen verbundene Unternehmen, oeffentliche "
                 "Auftraggeber und Privatkunden.",
             ]),
             ("§ 4 Bonitaetslimits", [
                 "Limits werden je Debitor individuell vom Factor festgelegt und der Anschlusskundin "
                 "in einer Limitliste mitgeteilt. Bei Aufstockungen entscheidet der Factor binnen "
                 "10 Bankarbeitstagen.",
             ]),
             ("§ 5 Laufzeit und Kuendigung", [
                 "Laufzeit: 36 Monate ab 1. Mai 2023, automatische Verlaengerung um jeweils 12 Monate, "
                 "soweit nicht spaetestens 3 Monate vor Ablauf gekuendigt wird.",
             ]),
         ])),
        ("Buchhalterische Behandlung",
         "Aufgrund der Risikoabnahme erfolgt der Forderungsverkauf bilanziell als Abgang im Sinne des "
         "IDW RS HFA 8 (Bilanzbefreiungswirkung). Im HGB-Einzelabschluss wird die Forderung beim "
         "Verkauf an den Factor ausgebucht. Die Auswirkungen auf die Bilanzkennzahlen (Verkuerzung "
         "der Bilanzsumme um ca. 4,8 Mio. EUR, Verbesserung der DSO um 12 Tage) wurden mit der BDO AG "
         "WPG abgestimmt (Memo vom 28.03.2023)."),
        ("Unterschriften",
         signatures("Sandra Becker", "Geschaeftsfuehrerin / CFO", M["name"],
                    "Dr. Ulrike Sommer", "Prokuristin", "Targo Commercial Finance AG",
                    place="Koeln / Duesseldorf", date_str_="11. April 2023")),
    ],
)


# ── Reisekostenabrechnung_Vertrieb_Q2_2024 ──────────────────────────────────
write_doc(
    f"{BASE}/Reisekostenabrechnung_Vertrieb_Q2_2024.docx", H,
    "Reisekostenabrechnung Vertrieb – Q2/2024",
    subtitle="Sammelabrechnung Aussendienst – Berichtszeitraum 1. April bis 30. Juni 2024",
    sections=[
        ("Hinweis",
         "Sammelabrechnung fuer die im Aussendienst taetigen Vertriebsmitarbeitenden (Herr Markus Fischer / "
         "Key Account Industrie; Herr Jan Mueller / Key Account Automotive; Herr Stefan Braun / Einkauf "
         "(Lieferantenbesuche); Frau Lisa Schulz / Service Engineering). Erfasst sind alle Reisen mit "
         "Uebernachtung sowie Tagesreisen ueber 300 km Strecke."),
        ("Zusammenfassung",
         [
             ["Mitarbeitende:r", "Reisetage", "km PKW", "Fahrtkosten", "Hotel", "Verpflegung", "Sonst.", "SUMME"],
             ["Markus Fischer", "27", "8.420", "2.526,00", "3.420,00", "1.218,00", "286,00", "7.450,00"],
             ["Jan Mueller", "31", "9.130", "2.739,00", "4.120,00", "1.484,00", "412,00", "8.755,00"],
             ["Stefan Braun", "18", "5.610", "1.683,00", "2.180,00", "812,00", "184,00", "4.859,00"],
             ["Lisa Schulz", "22", "4.180", "1.254,00", "2.640,00", "1.018,00", "320,00", "5.232,00"],
             ["", "SUMME", "27.340", "8.202,00", "12.360,00", "4.532,00", "1.202,00", "26.296,00"],
         ]),
        ("Auffaelligkeiten",
         "Die Mehrkosten bei Herrn Mueller resultieren aus drei zusaetzlichen Werksbesuchen bei Stellantis "
         "Ruesselsheim (Akquise neuer Auftrag Hybrid-Karosseriebau). Eine Buchung der Mehrkosten erfolgte "
         "auf das Projekt MMB-2024-STL-001 (Akquise). Reisekostenbudget Q2: 32.000 EUR; Auslastung 82,2 %."),
        ("Buchung",
         "Verbuchung in SAP FI auf Kostenstelle 4600 (Vertrieb). Auszahlung an die Mitarbeitenden erfolgt "
         "ueber die Juli-Gehaltsabrechnung. Verpflegungsmehraufwand wird steuerlich gemaess EStG behandelt "
         "(pauschal bei Reisen > 8 Std. 14 EUR, > 24 Std. 28 EUR)."),
        ("Unterschriften",
         signatures("Sandra Becker", "Geschaeftsfuehrerin / CFO", M["name"],
                    "Andrea Hoffmann", "Leiterin Personal & Verwaltung", M["name"],
                    place="Koeln", date_str_="9. Juli 2024")),
    ],
)


# ── FIN_Gewinnverteilungsplan_2023 ──────────────────────────────────────────
write_doc(
    f"{BASE}/FIN_Gewinnverteilungsplan_2023.docx", H,
    "Gewinnverteilungsplan – Geschaeftsjahr 2023",
    subtitle="Vorlage zur Beschlussfassung in der Gesellschafterversammlung 2024",
    sections=[
        ("Ausgangswerte",
         "Jahresueberschuss 2023 nach HGB: 2.730.000,00 EUR (testiert durch BDO AG WPG, Bestaetigungsvermerk "
         "vom 7. Mai 2024). Gewinnvortrag aus 2022: 240.000,00 EUR. Verfuegbarer Bilanzgewinn 2023: "
         "2.970.000,00 EUR."),
        ("Vorschlag der Geschaeftsfuehrung",
         [
             ["Verwendung", "Betrag EUR", "Anteil"],
             ["Einstellung in andere Gewinnruecklagen", "1.770.000,00", "59,6 %"],
             ["Ausschuettung an Gesellschafter", "1.100.000,00", "37,0 %"],
             ["Vortrag auf neue Rechnung", "100.000,00", "3,4 %"],
             ["SUMME", "2.970.000,00", "100,0 %"],
         ]),
        ("Aufteilung der Ausschuettung",
         [
             ["Gesellschafter", "Anteil", "Ausschuettung EUR", "KapErtrSt 25 %", "SolZ 5,5 %", "Auszahlung netto"],
             ["Klaus Mueller", "60 %", "660.000,00", "165.000,00", "9.075,00", "485.925,00"],
             ["Mueller Familien-GbR", "40 %", "440.000,00", "110.000,00", "6.050,00", "323.950,00"],
             ["SUMME", "100 %", "1.100.000,00", "275.000,00", "15.125,00", "809.875,00"],
         ]),
        ("Auswirkung Eigenkapital",
         "Nach Beschluss steigt das Eigenkapital von 16,90 Mio. EUR (31.12.2023) um die thesaurierten "
         "1,87 Mio. EUR (1,77 Mio. EUR plus 0,10 Mio. EUR Vortrag) auf einen Pro-forma-Stand von rund "
         "18,77 Mio. EUR. Die EK-Quote (gemessen an Bilanzsumme 31,2 Mio. EUR) verbessert sich entsprechend "
         "von 54,2 % auf rund 60,2 % – Vorbereitung der geplanten Beteiligungstransaktion / Wachstumsphase."),
        ("Empfehlung",
         "Die Geschaeftsfuehrung empfiehlt die Annahme des Vorschlags. Die Wirtschaftspruefung "
         "(BDO AG WPG) hat den Vorschlag als sachgerecht im Lichte der gesellschaftsvertraglichen "
         "Thesaurierungsregelung (§ 15 GV i. d. F. v. 19.09.2019) bestaetigt."),
    ],
)


# ── FIN_Umsatzsteuervoranmeldung_Q4_2023 ────────────────────────────────────
write_doc(
    f"{BASE}/FIN_Umsatzsteuervoranmeldung_Q4_2023.docx", H,
    "Umsatzsteuervoranmeldung Q4/2023",
    subtitle="Voranmeldungszeitraum: 1. Oktober bis 31. Dezember 2023 – Finanzamt Koeln-Nord",
    sections=[
        ("Stammdaten",
         "Steuernummer: 215/5765/9876\n\n"
         "USt-IdNr.: DE 198 765 432\n\n"
         "Voranmeldung uebermittelt via ELSTER am 8. Januar 2024 (Transferticket: 8240711209234567)."),
        ("Position",
         [
             ["Position", "Bemessungsgrundlage EUR", "Steuersatz", "Steuerbetrag EUR"],
             ["Steuerpflichtige Umsaetze § 15 Abs. 1 Nr. 1 UStG", "8.910.420,18", "19 %", "1.692.979,83"],
             ["Steuerpflichtige Umsaetze ermaessigter Satz", "0,00", "7 %", "0,00"],
             ["Innergemeinschaftliche Lieferungen § 4 Nr. 1b", "1.940.382,00", "0 %", "0,00"],
             ["Ausfuhrlieferungen § 4 Nr. 1a", "812.500,00", "0 %", "0,00"],
             ["Innergemeinschaftliche Erwerbe", "318.200,00", "19 %", "60.458,00"],
             ["Vorsteuer aus Eingangsrechnungen", "", "", "-892.412,40"],
             ["Vorsteuer i. g. Erwerbe", "", "", "-60.458,00"],
             ["Reverse-Charge (§ 13b UStG)", "82.500,00", "19 %", "15.675,00"],
             ["VS aus Reverse-Charge", "", "", "-15.675,00"],
             ["SUMME Zahllast", "", "", "800.567,43"],
         ]),
        ("Erlaeuterungen",
         "Die Innergemeinschaftlichen Lieferungen entfallen schwerpunktmaessig auf Auftraege fuer Stellantis "
         "Eisenach (Werk Frankreich) und VW Bratislava (Slowakei). Die Ausfuhrlieferungen entfallen auf den "
         "Auftrag Dürr AG fuer das Werk Queretaro (Mexiko). Innergemeinschaftliche Erwerbe betreffen Servo-"
         "Antriebskomponenten der Siemens AG Oesterreich (Wien). Reverse-Charge betrifft Beratungsleistungen "
         "auslaendischer Berater (Roland Berger Schweiz, McKinsey UK)."),
        ("Zahlung",
         "Die ermittelte Zahllast in Hoehe von 800.567,43 EUR wurde am 10. Januar 2024 fristgerecht "
         "vom Geschaeftskonto Deutsche Bank AG ueberwiesen. Eine SEPA-Lastschriftbevollmaechtigung des "
         "Finanzamtes besteht; auf den Lastschrifteinzug wurde ausnahmsweise verzichtet aufgrund "
         "Liquiditaetsoptimierung Quartalsende."),
        ("Erstellt durch",
         "KPMG AG Wirtschaftspruefungsgesellschaft, Standort Koeln, Frau StB Dr. Carola Lindner. "
         "Internes Review durch Sandra Becker (CFO) am 8. Januar 2024."),
    ],
)


# ── Bestandsbewertung_Roh_Hilf_Betriebsstoffe_2023 ──────────────────────────
write_doc(
    f"{BASE}/Bestandsbewertung_Roh_Hilf_Betriebsstoffe_2023.docx", H,
    "Bestandsbewertung Roh-, Hilfs- und Betriebsstoffe – Stichtag 31. Dezember 2023",
    subtitle="Stichtags-Inventur und Bewertung, Stand 12. Januar 2024",
    sections=[
        ("Vorgehen",
         "Die Bestandsbewertung erfolgte gemaess § 240 HGB i. V. m. § 256a HGB. Methodik: gleitender "
         "Durchschnitt (LIFO-Methode wird nicht angewandt). Die Bewertung beruecksichtigt Niederstwertprinzip "
         "und – soweit erforderlich – pauschale Wertberichtigungen fuer Gaengigkeitsabschlaege (Reichweite-"
         "Methode auf Basis SAP MM-IM). Die Inventur erfolgte im Wege der permanenten Inventur "
         "(stichprobenartige Erfassung) gemaess interner Verfahrensanweisung VA-LOG-002."),
        ("Bestandswerte 31.12.2023",
         [
             ["Materialart", "Menge Einheiten", "Anschaffungskosten EUR", "Wertberichtigung EUR", "Bilanzwert EUR"],
             ["Rohstoffe – Stahl (S235, S355, S690)", "412 t", "942.580,00", "32.400,00", "910.180,00"],
             ["Rohstoffe – Aluminium (AlMg3, AlMgSi1)", "118 t", "418.300,00", "14.200,00", "404.100,00"],
             ["Rohstoffe – Edelstahl (1.4301, 1.4571)", "82 t", "612.480,00", "8.500,00", "603.980,00"],
             ["Halbzeuge / Profile / Bleche", "n. M.", "1.180.420,00", "94.380,00", "1.086.040,00"],
             ["Kaufteile mechanisch (Lager, Schrauben, Dichtungen)", "n. M.", "892.600,00", "78.420,00", "814.180,00"],
             ["Antriebe und Motoren (Siemens / SEW)", "n. M.", "1.420.180,00", "62.000,00", "1.358.180,00"],
             ["Steuerungstechnik / SPS / HMI", "n. M.", "1.108.520,00", "55.420,00", "1.053.100,00"],
             ["Hydraulik- und Pneumatikbauteile", "n. M.", "612.000,00", "41.000,00", "571.000,00"],
             ["Kuehlschmierstoffe / Betriebsstoffe / OEle", "n. M.", "182.400,00", "8.420,00", "173.980,00"],
             ["Verpackungsmaterial", "n. M.", "62.300,00", "4.800,00", "57.500,00"],
             ["Werkzeuge GWG", "n. M.", "118.200,00", "12.420,00", "105.780,00"],
             ["", "SUMME", "7.550.000,00", "412.000,00", "7.138.000,00"],
         ]),
        ("Bewertungsanpassungen",
         "Eine Wertberichtigung von insgesamt 412.000 EUR wurde vorgenommen, davon 94.380 EUR auf "
         "Halbzeuge (Stahl-Restpostenbloecke aus 2020/2021) sowie 78.420 EUR auf mechanische Kaufteile "
         "(insbesondere Auslaufkomponenten der Pressenlinie PL-300). Die Bewertung wurde mit der "
         "BDO AG WPG abgestimmt; die Pauschalwertberichtigung von 1,2 % auf das gesamte Vorratsvolumen "
         "wurde zusaetzlich angesetzt (90.600 EUR; in 'Halbzeuge' enthalten)."),
        ("Inventurverantwortliche",
         "Aufnahmeleitung: Herr Klaus Bauer (Logistikleiter); Pruefung WP: Herr WP Dr. Michael Erbach (BDO); "
         "Freigabe: Frau Sandra Becker (CFO). Vollstaendigkeitsbestaetigung: 31.12.2023, 18:40 Uhr."),
    ],
)


# ── FIN_Wertpapieranlage_Festgeld_2023 ──────────────────────────────────────
write_doc(
    f"{BASE}/FIN_Wertpapieranlage_Festgeld_2023.docx", H,
    "Wertpapier- und Festgeldanlagen 2023 – Halbreiter Maschinenbau GmbH",
    subtitle="Aufstellung der liquiden Mittel (Anlage gemaess Treasury-Richtlinie)",
    sections=[
        ("Anlagepolitik",
         "Die Treasury-Richtlinie der Gesellschaft (Stand 1. Januar 2023) erlaubt ausschliesslich Anlagen "
         "in Geldmarktinstrumenten und Anlagen mit Investment-Grade-Rating (Mindestrating: A bei Standard & "
         "Poor's). Aktienanlagen und derivative Instrumente sind ausgeschlossen. Anlageziel: Kapitalerhalt "
         "und Liquiditaetssicherung."),
        ("Anlagen zum 31. Dezember 2023",
         [
             ["Anlage", "Emittent / Bank", "Volumen EUR", "Zinssatz", "Laufzeit", "Rating"],
             ["Festgeld 12M", "Deutsche Bank AG", "1.500.000,00", "3,45 % p. a.", "12.03.2024", "A (S&P)"],
             ["Festgeld 6M", "DZ Bank AG", "1.000.000,00", "3,18 % p. a.", "15.04.2024", "AA- (S&P)"],
             ["Tagesgeld", "Sparkasse KoelnBonn", "800.000,00", "2,75 % p. a.", "taeglich", "A+ (S&P)"],
             ["Bundesanleihe 0,5 % 15.02.2026", "Bundesrepublik Deutschland", "500.000,00", "Kurs 96,2 %", "15.02.2026", "AAA"],
             ["Pfandbrief 1,25 % 02.04.2025", "Aareal Bank AG", "400.000,00", "Kurs 98,1 %", "02.04.2025", "A+"],
             ["", "SUMME", "4.200.000,00", "", "", ""],
         ]),
        ("Ertragsuebersicht 2023",
         "Zins- und Ertragsergebnis aus Geldanlagen 2023: 118.420 EUR (Vorjahr 38.250 EUR). Die signifikante "
         "Steigerung resultiert aus der gestiegenen Zinslandschaft (EZB-Leitzins) sowie der konsequenten "
         "Anlage temporaer freier Liquiditaet. Buchung im Finanzergebnis Konto 7610 'Sonstige Zinsertraege'."),
        ("Vorgaben",
         "Die Geschaeftsfuehrung berichtet quartalsweise im Rahmen des Treasury-Reports an die Beirats- "
         "und Gesellschaftersitzung. Eine Anpassung der Treasury-Richtlinie auf eine erweiterte Anlageklasse "
         "(z. B. ESG-Geldmarktfonds) ist fuer 2024 in Pruefung."),
    ],
)


# ── FIN_Anlagenverzeichnis_2023 ─────────────────────────────────────────────
write_doc(
    f"{BASE}/FIN_Anlagenverzeichnis_2023.docx", H,
    "Anlagenverzeichnis – Stand 31. Dezember 2023",
    subtitle="Auszug aus dem SAP-FI-AA-Modul (sachliche Pruefung mit Inventur abgestimmt)",
    sections=[
        ("Uebersicht Anlagenwerte",
         [
             ["Anlagengruppe", "Anschaffungswert EUR", "kum. AfA EUR", "Buchwert 31.12.2023 EUR"],
             ["Immaterielle VG (Software / Lizenzen)", "1.420.380,00", "1.062.180,00", "358.200,00"],
             ["Grundstuecke (Industriestrasse 12)", "1.850.000,00", "0,00", "1.850.000,00"],
             ["Gebaeude (Halle A, B, C, Verwaltung)", "8.480.180,00", "3.620.420,00", "4.859.760,00"],
             ["Technische Anlagen / Maschinen (Pressen, Laser, Foerderbaender)", "14.820.180,00", "8.940.380,00", "5.879.800,00"],
             ["Betriebsausstattung (Hallenkran, Krananlagen)", "1.480.420,00", "920.180,00", "560.240,00"],
             ["Fuhrpark (LKW, Stapler)", "412.420,00", "248.180,00", "164.240,00"],
             ["GWG / digitale Ausstattung", "182.380,00", "118.420,00", "63.960,00"],
             ["Anlagen im Bau (Erweiterung LS-800 5-Achs)", "640.000,00", "0,00", "640.000,00"],
             ["", "SUMME", "29.285.960,00", "14.909.760,00", "14.376.200,00"],
         ]),
        ("Zugaenge 2023",
         "Wesentliche Zugaenge: (1) Stanzpresse Modul Halle B Servo-Steuerungs-Upgrade 320.000 EUR; "
         "(2) Laserschneidanlage LS-800 5-Achs-Modul (im Bau) 640.000 EUR; (3) PV-Anlage Verwaltungs-"
         "gebaeude 245.000 EUR; (4) MES-Lizenzpaket 185.000 EUR; (5) Fuhrpark-Erneuerung 12 Servicewagen "
         "415.000 EUR. Investitionsvolumen gesamt: 2,80 Mio. EUR."),
        ("Abgaenge 2023",
         "Veraeusserung Stanzpresse Halle A (Baujahr 1998, BW 0 EUR, Erloes 18.500 EUR); Verschrottung "
         "Foerderband Linie 1 (BW 0 EUR); Veraeusserung 4 Aussendienstfahrzeuge (BW 18.420 EUR, Erloes "
         "32.400 EUR; Buchgewinn 13.980 EUR)."),
        ("AfA-Methode",
         "Linearer AfA gemaess amtlicher AfA-Tabelle (Steuer) bzw. wirtschaftlicher Nutzungsdauer (Handelsbilanz). "
         "Maschinen i. d. R. 10 Jahre, Hallen 33 Jahre, IT-Hardware 3 Jahre, Software 3 Jahre, Fuhrpark 6 Jahre."),
    ],
)


# ── FIN_Rückstellungsübersicht_2023 ─────────────────────────────────────────
write_doc(
    f"{BASE}/FIN_Rückstellungsübersicht_2023.docx", H,
    "Rueckstellungsuebersicht – Stand 31. Dezember 2023",
    subtitle="Pruefungsabstimmung mit BDO AG WPG (Bericht vom 7.5.2024)",
    sections=[
        ("Uebersicht",
         [
             ["Rueckstellung", "Stand 1.1.2023 EUR", "Inanspruchnahme EUR", "Aufloesung EUR", "Zufuehrung EUR", "Stand 31.12.2023 EUR"],
             ["Pensionsrueckstellungen (Direktzusage GF)", "1.420.380,00", "82.418,00", "0,00", "184.300,00", "1.522.262,00"],
             ["Urlaubsrueckstellungen", "412.180,00", "412.180,00", "0,00", "548.420,00", "548.420,00"],
             ["Gleitzeit-/UEberstunden", "118.420,00", "118.420,00", "0,00", "142.180,00", "142.180,00"],
             ["Tantieme Geschaeftsfuehrung", "184.000,00", "184.000,00", "0,00", "228.000,00", "228.000,00"],
             ["Gewaehrleistung / Kulanz", "412.000,00", "118.400,00", "32.400,00", "184.200,00", "445.400,00"],
             ["Drohende Verluste (Auftraege)", "62.000,00", "62.000,00", "0,00", "0,00", "0,00"],
             ["Schadensersatz / Rechtsstreitigkeiten", "120.000,00", "0,00", "60.000,00", "30.000,00", "90.000,00"],
             ["Pruefungs- und Beratungskosten", "182.000,00", "182.000,00", "0,00", "212.000,00", "212.000,00"],
             ["Aufbewahrungspflichten (10 Jahre)", "118.000,00", "0,00", "0,00", "12.000,00", "130.000,00"],
             ["Sonstige", "192.020,00", "62.420,00", "18.400,00", "78.220,00", "189.420,00"],
             ["", "SUMME", "3.221.000,00", "1.221.838,00", "110.800,00", "1.619.520,00", "3.507.882,00"],
         ]),
        ("Erlaeuterungen",
         "Pensionsrueckstellungen: Direktzusage zugunsten Herr Klaus Mueller (Anwartschaft ab 1985) und "
         "Frau Sandra Becker (Anwartschaft ab 2014); versicherungsmathematisches Gutachten von Heubeck AG "
         "(Bericht vom 22.03.2024). Zinssatz 1,82 % gemaess BilMoG-Durchschnitt 10 Jahre.\n\n"
         "Gewaehrleistung: pauschal 0,9 % vom Jahresumsatz (gestaffelt nach Produktgruppe), gemaess "
         "Bewertungsverfahren VA-FIN-008.\n\n"
         "Schadensersatz: ein laufender Rechtsstreit mit ehem. Lieferanten Kunz Antriebstechnik GmbH "
         "(Streitwert 220 TEUR); Erfolgswahrscheinlichkeit Klage durch Heuking Kuehn auf 40 % geschaetzt."),
    ],
)


# ── FIN_Bürgschaft_Deutsche_Bank ────────────────────────────────────────────
write_doc(
    f"{BASE}/FIN_Bürgschaft_Deutsche_Bank.docx", H,
    "Bankbuergschaft – Deutsche Bank AG zugunsten ThyssenKrupp Steel Europe AG",
    subtitle="Buergschaftsurkunde Nr. DB-MMB-2023-VEM-022 vom 8. September 2023",
    sections=[
        ("Buergin",
         "Deutsche Bank AG, Filiale Koeln, Unter Sachsenhausen 17, 50667 Koeln."),
        ("Beguenstigte",
         "ThyssenKrupp Steel Europe AG, Kaiser-Wilhelm-Strasse 100, 47166 Duisburg."),
        ("Hauptverbindlichkeit",
         "Vertrag Nr. TKSE-MMB-2023-PL500-007 ueber Lieferung und Montage einer Pressenlinie PL-500 "
         "(Auftragsvolumen 3,8 Mio. EUR) im Werk Duisburg-Hamborn, Werkstor 7, Halle A41. Lieferzeitpunkt: "
         "Inbetriebnahme bis 30. April 2024. Gewaehrleistungszeit: 24 Monate ab Inbetriebnahme."),
        ("Buergschaftsumme und Art",
         "Vertragserfuellungsbuergschaft (Performance Bond) in Hoehe von 380.000 EUR (10 % des Vertragspreises) "
         "bis Inbetriebnahme; sodann Umwandlung in Gewaehrleistungsbuergschaft in Hoehe von 190.000 EUR "
         "(5 %) fuer die 24-monatige Gewaehrleistungsphase."),
        ("Zahlungsmodalitaet",
         "Selbstschuldnerische Buergschaft auf erstes Anfordern unter Verzicht auf die Einreden der Vorausklage "
         "(§ 771 BGB), der Aufrechenbarkeit (§ 770 Abs. 2 BGB) und der Anfechtbarkeit (§ 770 Abs. 1 BGB)."),
        ("Avalprovision",
         "1,1 % p. a., berechnet auf die jeweils gueltige Buergschaftssumme; Mindestprovision 250 EUR pro "
         "Quartal. Anrechnung auf die Aval-Linie 3,5 Mio. EUR (Stand: ausgeschoepft 2,2 Mio. EUR)."),
        ("Geltungsdauer",
         "Bis Bauzeitende plus Gewaehrleistung, spaetestens 30. April 2026. Rueckgabe der Buergschafts-"
         "urkunde im Original durch den Beguenstigten ist Voraussetzung fuer die Befreiung."),
        ("Unterschriften",
         signatures("Dr. Friedhelm Stuetzel", "Senior Account Manager", "Deutsche Bank AG",
                    "Sandra Becker", "Geschaeftsfuehrerin", M["name"],
                    place="Koeln", date_str_="8. September 2023")),
    ],
)


# ── FIN_Inventurliste_Vorräte_31.12.20 ─────────────────────────────────────
write_doc(
    f"{BASE}/FIN_Inventurliste_Vorräte_31.12.20.docx", H,
    "Inventurliste Vorraete – Stichtag 31. Dezember 2023",
    subtitle="Stichtagsinventur Halle A, B und Lager Nord – Vorlage zur Pruefung BDO AG WPG",
    sections=[
        ("Stichproben",
         "Stichprobenartige Auswahl 28 Positionen ueber alle Lagerbereiche, gewichtet nach Wertbeitrag "
         "(ABC-Klasse): 14 A-Positionen, 8 B-Positionen, 6 C-Positionen. Aufnahme erfolgte am 31. Dezember "
         "2023 zwischen 06:00 und 14:30 Uhr. Aufnahmeleitung: Klaus Bauer (Logistik); Begleitung WP: "
         "Dr. Michael Erbach (BDO)."),
        ("Auszug Stichprobenliste",
         [
             ["Pos.", "Material-Nr.", "Bezeichnung", "Buchbestand", "Zaehlbestand", "Differenz", "Bewertung EUR"],
             ["1", "1000-0021-S355", "Stahlblech S355 8 mm 1500x3000", "82 St.", "82 St.", "0", "32.418,00"],
             ["2", "1000-0044-AL", "Alublech AlMg3 6 mm 1250x2500", "118 St.", "117 St.", "-1", "18.420,00"],
             ["3", "2200-3814-SIE", "SPS Siemens S7-1500 CPU 1517", "12 St.", "12 St.", "0", "16.840,00"],
             ["4", "3300-1180-SCH", "Schunk Kraftspannblock 250", "8 St.", "8 St.", "0", "12.480,00"],
             ["5", "3400-2280-IGS", "Igus Energiekette 14er Profil", "240 m", "238 m", "-2 m", "8.420,00"],
             ["6", "5500-1112-TRU", "Trumpf Laserkopf BC-040", "1 St.", "1 St.", "0", "42.180,00"],
             ["7", "6600-0118-SEW", "SEW-EURODRIVE Servo 11 kW", "6 St.", "6 St.", "0", "18.420,00"],
             ["8", "8800-0042-KSS", "Kuehlschmierstoff Castrol 200 l", "18 St.", "18 St.", "0", "4.860,00"],
         ]),
        ("Inventurdifferenzen",
         "Wertmaessige Inventurdifferenz: -218 EUR (entsprechend < 0,003 % vom Vorratswert). "
         "Differenzen werden mit Buchungsbeleg INV-2023-12-031 an SAP MM gemeldet und bewertet. "
         "Die Geschaeftsfuehrung sieht keinen Anlass fuer organisatorische Veraenderungen."),
        ("Bestaetigung",
         "Aufnahmeleitung: Klaus Bauer (Logistik) sowie Anette Klein (Buchhaltung). "
         "Anwesend WP: Dr. Michael Erbach (BDO AG WPG). Unterschriften liegen im Inventurordner Q4/2023 vor."),
    ],
)


# ── Korrespondenz_WP_Prüfungsauftrag_2023 ──────────────────────────────────
write_doc(
    f"{BASE}/Korrespondenz_WP_Prüfungsauftrag_2023.docx", H,
    "Korrespondenz mit BDO AG WPG – Pruefungsauftrag Jahresabschluss 2023",
    subtitle="Mandatierungsschreiben und Auftragsbestaetigung",
    sections=[
        ("Adressat",
         "BDO AG Wirtschaftspruefungsgesellschaft, Standort Koeln, Im Zollhafen 18, 50678 Koeln, "
         "z. Hd. WP/StB Dr. Michael Erbach (mandatsfuehrender Partner)."),
        ("Mandatierungsschreiben",
         "Sehr geehrter Herr Dr. Erbach,\n\n"
         "die Gesellschafterversammlung der Halbreiter Maschinenbau GmbH hat am 25. Juni 2024 die "
         "BDO AG Wirtschaftspruefungsgesellschaft erneut zur Abschlusspruefer fuer das Geschaeftsjahr 2024 "
         "bestellt. Wir bestaetigen hiermit den damit verbundenen Pruefungsauftrag und konkretisieren "
         "Auftragsgegenstand und Honorierung wie folgt:\n\n"
         "- Pruefungsgegenstand: Jahresabschluss (Bilanz, GuV, Anhang) und Lagebericht fuer das "
         "Geschaeftsjahr 2024 nach HGB; ergaenzende Pruefung der Buchfuehrung und des internen "
         "Kontrollsystems; ergaenzende Pruefung der Risikomanagement-Funktion gemaess § 91 Abs. 2 AktG "
         "analog (freiwillig).\n\n"
         "- Pruefungstermin: Vorpruefung 14. bis 25. Oktober 2024; Hauptpruefung 4. bis 22. Maerz 2025; "
         "abschliessende Schlussbesprechung 9. Mai 2025.\n\n"
         "- Honorar: Pauschalhonorar von 78.000 EUR (netto, zzgl. USt.); inkludiert Reisekosten und "
         "Auslagen. Ein Plus-Stundenkontingent fuer Sonderpruefungen (z. B. Working-Capital-Analyse, "
         "Bewertung Anlagen) wird im Bedarfsfall auf Basis Stundensaetze (WP-Partner 380 EUR, Manager "
         "230 EUR, Senior 165 EUR) gesondert vergueteet.\n\n"
         "- Erforderliche Unterlagen werden ueber den IDW PS 314.1 Datenroom uebergeben."),
        ("Auftragsbestaetigung BDO",
         "BDO AG WPG hat mit Schreiben vom 28. Juni 2024 (Az. WP-MMB-2024-001) den Pruefungsauftrag in "
         "den vorgenannten Eckpunkten bestaetigt. Beigefuegt ist die Mandatsdokumentation gemaess "
         "IDW QS 1, Erklaerung zur Unabhaengigkeit gemaess § 319 HGB sowie die aktualisierten allgemeinen "
         "Auftragsbedingungen (AAB)."),
        ("Unterzeichner",
         "Halbreiter Maschinenbau GmbH: Sandra Becker (CFO).\n\n"
         "BDO AG WPG: WP/StB Dr. Michael Erbach (Partner), WP Andreas Goebel (Senior Manager)."),
    ],
)


# ── FIN_Devisensicherung_2024 ───────────────────────────────────────────────
write_doc(
    f"{BASE}/FIN_Devisensicherung_2024.docx", H,
    "Devisensicherung 2024 – Rahmenvereinbarung Forwards EUR/USD und EUR/MXN",
    subtitle="Vereinbarung mit Deutsche Bank AG (FX-Desk Frankfurt), Stand 14. Maerz 2024",
    sections=[
        ("Hintergrund",
         "Die Halbreiter Maschinenbau GmbH erzielt rund 18 % ihrer Umsaetze 2024 in Fremdwaehrung "
         "(11 % USD, 5 % MXN, 2 % CHF). Die Geschaeftsfuehrung verfolgt eine konservative Hedging-"
         "Strategie: 100 % der Fremdwaehrungs-Forderungen werden zum Zeitpunkt der Auftragsbestaetigung "
         "ueber Devisentermingeschaefte abgesichert (Microhedge). Spekulative Geschaefte sind gemaess "
         "Treasury-Richtlinie ausdruecklich verboten."),
        ("Eingesetzte Instrumente",
         [
             ["Instrument", "Volumen 2024 (geplant)", "Sicherungsquote", "Anwendung"],
             ["Devisentermingeschaeft EUR/USD", "5,8 Mio. USD", "100 %", "Dürr AG Werk Queretaro, Mexiko (Anzahlungen in USD)"],
             ["Devisentermingeschaeft EUR/MXN", "44 Mio. MXN", "100 %", "Endrate Mexiko (Liefertranchen 2024)"],
             ["FX-Swap EUR/CHF", "1,2 Mio. CHF", "100 %", "Schweizer Lieferanten (Sensirion AG)"],
         ]),
        ("Konditionen",
         "Spread Marge gegenueber dem Mid-Rate: 8 Basispunkte (EUR/USD), 25 Basispunkte (EUR/MXN), "
         "12 Basispunkte (EUR/CHF). Mindest-Tranchenvolumen pro Geschaeft 100.000 EUR-Aequivalent. "
         "Abwicklung Spot-Settlement T+2 oder T+30 bis T+360 (je nach Auftragslaufzeit). "
         "Counterparty-Risiko: Deutsche Bank AG (Rating A bei S&P)."),
        ("Bilanzierung",
         "Sicherungsbeziehungen werden gemaess § 254 HGB bilanziell zusammengefasst (Bewertungseinheit). "
         "Eine ineffective Portion wird – soweit relevant – im sonstigen betrieblichen Ergebnis erfasst. "
         "Bewertungsstichtag 31.12. Marktwerte der offenen Positionen werden im Anhang erlaeutert."),
        ("Verantwortlich",
         "Sandra Becker (CFO), Markus Helmer (Treasury / Sub-Ledger). Quartalsweises Reporting an die "
         "Geschaeftsfuehrung; Limit-Ueberwachung erfolgt im SAP TRM-Modul."),
    ],
)


# ── FIN_Abschlussprüfungsbericht_WP_2023 ────────────────────────────────────
write_doc(
    f"{BASE}/FIN_Abschlussprüfungsbericht_WP_2023.docx", H,
    "Abschlusspruefungsbericht 2023 – Auszug (Hauptbericht)",
    subtitle="BDO AG WPG, Koeln – Bericht vom 7. Mai 2024",
    sections=[
        ("Mandat",
         "Pruefungsmandat ueber den Jahresabschluss zum 31.12.2023 und den Lagebericht der Halbreiter Maschinenbau "
         "GmbH; Pruefung gemaess §§ 316 ff. HGB und unter Beachtung der IDW Prufungsstandards "
         "(insbesondere IDW PS 200, 240, 261, 300, 314, 400 sowie 450)."),
        ("Wesentliche Pruefungsfelder",
         ("list", [
             "Bewertung der Vorraete (kritisches Pruefungsfeld): Stichprobenpruefung 28 Positionen; "
             "Bewertungsabschlaege auf Auslaufmaterial (Pressenlinie PL-300, Halbzeuge Stahl) ueberprueft.",
             "Forderungen aus Lieferungen und Leistungen: Saldenbestaetigungsverfahren bei 12 Schluessel-"
             "kunden (TKSE, Bosch Rexroth, Hella, Viessmann, Dürr u. a.); Antwortquote 100 %.",
             "Umsatzrealisierung Sondermaschinenbau: Pruefung Percentage-of-Completion vs. Completed-Contract "
             "(Wahlrecht HGB); Methode 'Completed-Contract' wird angewandt.",
             "Pensionsrueckstellungen: Pruefung des versicherungsmathematischen Gutachtens Heubeck AG.",
             "Going-Concern-Pruefung: Cashflow-Forecast 2024-2026 plausibilisiert; keine Risiken erkennbar.",
             "Interne Kontrollsystem: Walkthrough auf Order-to-Cash und Purchase-to-Pay; gesonderter "
             "Management Letter zur Verbesserung der Funktionstrennung im Bestellprozess.",
         ])),
        ("Bestaetigungsvermerk",
         "Der Bestaetigungsvermerk wurde uneingeschraenkt erteilt: 'Nach unserer Beurteilung aufgrund "
         "der bei der Pruefung gewonnenen Erkenntnisse vermittelt der Jahresabschluss in Uebereinstimmung "
         "mit den deutschen handelsrechtlichen Vorschriften ein den tatsaechlichen Verhaeltnissen "
         "entsprechendes Bild der Vermoegens-, Finanz- und Ertragslage der Gesellschaft.'"),
        ("Risikohinweise",
         "Wesentliche Risiken: (a) Materialverfuegbarkeit elektronischer Komponenten und Antriebs-"
         "elektronik; (b) Kundenkonzentration (Top-5 Kunden 62 % vom Umsatz); (c) Energiepreis-"
         "schwankungen (PV-Aufdachanlage Q4/2023 reduziert Risiko partiell)."),
        ("Empfehlungen",
         "Die Wirtschaftspruefung empfiehlt: (a) Staerkere Funktionstrennung im Bestellwesen "
         "(separater Freigeber > 250 TEUR); (b) Einfuehrung formaler Quartalsreviews der "
         "Working-Capital-Kennzahlen; (c) Aufnahme einer Cyber-Risiko-Position im Risikoregister "
         "(in Umsetzung)."),
        ("Unterzeichnung",
         "WP/StB Dr. Michael Erbach (Partner), WP Andreas Goebel (Senior Manager). "
         "Koeln, den 7. Mai 2024."),
    ],
)


# ── FIN_Abschlussprüfungsbericht_WP_2022 ────────────────────────────────────
write_doc(
    f"{BASE}/FIN_Abschlussprüfungsbericht_WP_2022.docx", H,
    "Abschlusspruefungsbericht 2022 – Auszug",
    subtitle="BDO AG WPG, Koeln – Bericht vom 9. Mai 2023",
    sections=[
        ("Pruefungsmandat",
         "Pruefung Jahresabschluss 2022 und Lagebericht der Halbreiter Maschinenbau GmbH gemaess "
         "§§ 316 ff. HGB; IDW PS 200 ff."),
        ("Wesentliche Pruefungsfelder",
         ("list", [
             "Bewertung Vorraete (Niederstwertpruefung)",
             "Umsatzrealisierung in Bauauftraegen / Sondermaschinen",
             "Forderungspruefung und Saldenbestaetigung (10 Schluesselkunden)",
             "Pensionsrueckstellungen, versicherungsmathematische Gutachten Heubeck AG",
             "Going-Concern-Annahme (Cashflow-Forecast 2023-2025)",
             "IKS: Order-to-Cash und Purchase-to-Pay (Stichprobenpruefung)",
         ])),
        ("Bestaetigungsvermerk",
         "Bestaetigungsvermerk uneingeschraenkt erteilt. Hinweise: keine Risiken, die die Fortfuehrung "
         "der Gesellschaft gefaehrden; Auftragsbestand zum 31.12.2022 in Hoehe von 13,9 Mio. EUR gibt "
         "Visibilitaet fuer die kommenden 6-9 Monate."),
        ("Empfehlungen",
         "Verbesserungspotenziale (Management Letter, zugeleitet am 9.5.2023): formale Genehmigungs-"
         "workflows fuer Material-Sonderbeschaffungen ueber 50 TEUR; Aktualisierung der Treasury-"
         "Richtlinie um Hedging-Schwellen; Erweiterung des Berichtswesens um eine monatliche Working-"
         "Capital-Auswertung."),
        ("Unterzeichnung",
         "WP/StB Dr. Michael Erbach (Partner), WP/StB Anette Bremke (Senior Manager). "
         "Koeln, den 9. Mai 2023."),
    ],
)


# ── Korrespondenz_Bank_Jahresgespräch_2024 ──────────────────────────────────
write_doc(
    f"{BASE}/Korrespondenz_Bank_Jahresgespräch_2024.docx", H,
    "Korrespondenz – Jahresgespraech Deutsche Bank AG 2024",
    subtitle="Vorbereitung des jaehrlichen Bonitaetsgespraechs mit der Hausbank",
    sections=[
        ("Termin / Teilnehmende",
         "Termin: 22. Februar 2024, 10:00 Uhr, Filiale Deutsche Bank AG Koeln, Unter Sachsenhausen 17. "
         "Teilnehmende: Klaus Mueller (CEO), Sandra Becker (CFO), Dr. Friedhelm Stuetzel (Senior Account "
         "Manager Deutsche Bank), Stefan Adams (Risk Manager Mittelstand Deutsche Bank), Anette Klein "
         "(Buchhaltung MMB)."),
        ("Tagesordnung",
         ("list", [
             "Geschaeftsverlauf 2023 (Umsatz, EBITDA, Auftragsbestand, Liquiditaet)",
             "Vorlage testierter Jahresabschluss 2023 (vorlaeufig) und Mehrjahresplanung 2024-2026",
             "Status Aval-Linie (3,5 Mio. EUR, ausgeschoepft 2,2 Mio. EUR)",
             "Status Investitionslinie (4,5 Mio. EUR, unbeansprucht)",
             "Covenant-Reporting (ICR > 4,0x, Net Debt / EBITDA < 2,5x)",
             "FX-Sicherungsgeschaefte 2024 (Forwards EUR/USD, EUR/MXN)",
             "Nachhaltigkeitsfinanzierung / KfW-Foerderprogramme (PV, E-Mobilitaet)",
             "Aktuelles Rating und Konditionen",
         ])),
        ("Wesentliche Ergebnisse",
         "1) Die Deutsche Bank bestaetigt das interne Kreditrating der Gesellschaft (KR-Score 7+ auf einer "
         "21-stufigen Skala; entspricht etwa BBB+ extern) und sieht die Bonitaetsentwicklung positiv. "
         "Vorlage des aktualisierten KSAS-Ratings im Mai 2024 erwartet.\n\n"
         "2) Konditionen Investitionslinie bleiben bei 1,85 % p. a. fix unveraendert; eine Aufstockung um "
         "1,0 Mio. EUR auf 5,5 Mio. EUR zur Finanzierung des MES-Projektes wird befuerwortet und kann "
         "im Q2/2024 strukturiert werden.\n\n"
         "3) Covenants 2023 vollumfaenglich eingehalten: ICR (Zinsdeckungsgrad) bei 14,2x deutlich ueber "
         "Mindestschwelle; Net Debt / EBITDA bei 0,31x ebenfalls deutlich unter Schwellwert.\n\n"
         "4) Empfehlung der Bank: Pruefung Schuldscheindarlehen 5 Mio. EUR fuer 2025/2026 als "
         "Diversifizierung der Finanzierungsquellen; Vorgespraech mit Konsorten im H2/2024 geplant."),
        ("Naechste Schritte",
         "- Uebergabe testierter Jahresabschluss 2023 bis 31. Mai 2024.\n\n"
         "- Vorlage Mehrjahresplanung 2024-2026 bis 30. April 2024.\n\n"
         "- Folgegespraech ueber Aufstockung Investitionslinie: 25. April 2024."),
    ],
)

print("OK regen_mueller_02.py – 18 docs written")
