"""Brennhagen Software GmbH (Muenchen) / 04_Tochter_DE_RSG_Muenchen - 100 thin docs.

Subsidiary RSG: 340 MA, Embedded Software / ADAS, HRB 319872 AG Muenchen.
Werkleiter: Dr. Klaus Kessler. Lead Developer: Lars Wittmann.
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

BASE = f"{_ROOT}/roehrig_large/04_Tochter_DE_RSG_Muenchen"

# RSG-specific header
RSG = S["RSG"]
H_RSG = {
    "name": "Brennhagen Software GmbH",
    "addr": "Lyonel-Feininger-Strasse 28, 80807 Muenchen",
    "hrb":  "HRB 319872, Amtsgericht Muenchen",
}
H_RCZ = {"name": "Brennhagen CZ s.r.o.", "addr": "Tuzemska 14, 612 00 Brno, Tschechien", "hrb": "C 87654, KS Brno"}
H_RCN = {"name": "Brennhagen (Shanghai) Co. Ltd.", "addr": "Lane 1238, Pudong New Area, Shanghai 201210, China", "hrb": "913100007891234567"}
H_REG = {"name": "Brennhagen Elektronik GmbH", "addr": "Salzstrasse 145, 74076 Heilbronn", "hrb": "HRB 221456, Amtsgericht Heilbronn"}
H_RPL = {"name": "Brennhagen Polska Sp. z o.o.", "addr": "ul. Mikolowska 100, 40-065 Katowice, Polen", "hrb": "KRS 0000543210"}

PLACE = "Muenchen"


# ============================================================================
# 1) PRJ-2021-002 Lessons Learned ADAS-V4D Kalibrierungsplattform
# ============================================================================
def lessons_learned_adas():
    write_doc(f"{BASE}/PRJ-2021-002_Lessons_Learned_ADAS-V4D_Kalibrierungspla.docx", H_RSG,
        "PRJ-2021-002 - Lessons Learned: ADAS-V4D Kalibrierungsplattform",
        subtitle="Projekt-Post-Mortem nach Serienanlauf ADAS-V4D bei Mercedes-Benz EQS / EQE",
        sections=[
            ("Projekt-Steckbrief",
             "Projekt-ID: PRJ-2021-002\n"
             "Projektname: ADAS-V4D Kalibrierungsplattform (HiL-basierte End-of-Line-Kalibrierung)\n"
             "Projektleitung: Lars Wittmann (Lead Developer RSG), Co-Lead Dr. Sabrina Halbig\n"
             "Projektlaufzeit: 15.03.2021 bis 30.11.2022 (geplant) / 28.02.2023 (tatsaechlich, +90 Tage)\n"
             "Budget geplant: 4,8 Mio. EUR / tatsaechlich 5,42 Mio. EUR (+12,9 %)\n"
             "Kunde: Mercedes-Benz Group AG (Werk Sindelfingen, EQS-Linie 17)\n"
             "Auftragsvolumen Serie: 38 Mio. EUR ueber Laufzeit 2023-2027 (geschaetzt)"),
            ("Ergebnisuebersicht",
             "Das Projekt PRJ-2021-002 zur Entwicklung der ADAS-V4D Radar-Fusion-Kalibrierungsplattform fuer die "
             "Serienanlaufphase im Mercedes-Benz Werk Sindelfingen wurde mit drei Monaten Verspaetung und 12,9 % "
             "Budgetueberschreitung abgeschlossen. Trotz der Ueberschreitungen erreichte die Plattform alle technischen "
             "Akzeptanzkriterien (Kalibrierzeit < 75 Sekunden je ECU, Genauigkeit Winkelablage < 0,15 Grad, "
             "Wiederholgenauigkeit < 0,05 Grad). Mercedes-Benz hat das System per Final Acceptance Test (FAT) am "
             "12.02.2023 abgenommen; der Serienanlauf erfolgte planmaessig am 06.03.2023."),
            ("Was lief gut (Plus-Punkte)",
             ("list", [
                 "Frueher Einbezug des OEM-Validierungsteams (Mercedes EQS-Engineering) bereits im Konzept-Gate G1 - "
                 "vermied 18 spaetere Aenderungsantraege und stabilisierte die Anforderungsbasis bis Gate G3.",
                 "ASPICE Level 3 Assessment durch intacs-Auditor (KUGLER MAAG CIE) im Juli 2022 ohne Major-Finding - "
                 "die fruehzeitige Etablierung der SUP-Prozesse (SUP.1, SUP.8, SUP.10) zahlte sich aus.",
                 "Wiederverwendung des AUTOSAR Adaptive Platform Stacks aus PRJ-2020-007 (BMS-12) sparte ca. 9 PT je "
                 "Sprint und reduzierte die Toolchain-Einarbeitungszeit fuer neue Engineers auf < 2 Wochen.",
                 "Stabile Pair-Programming-Praxis im FuSi-Team (ISO 26262 ASIL B) mit verpflichtendem 4-Augen-Review "
                 "vor jedem Merge auf den release/* Branch - 0 ASIL-relevante Defekte im Field-Test.",
                 "Wittmann's woechentliches 30-Minuten 'Tech-Sync' mit Mercedes-Engineering (Mittwoch 09:00 MEZ) "
                 "wurde von beiden Seiten als 'Best Practice' bewertet und ist nun Vorgabe fuer alle OEM-Projekte.",
             ])),
            ("Was lief nicht gut (Minus-Punkte)",
             ("list", [
                 "Toolchain-Migration von Vector CANoe 13 auf 14 mitten in Sprint 22 (Mai 2022) verursachte 6 Wochen "
                 "Verzug, da Skripte angepasst und alle 412 Test-Cases re-validiert werden mussten.",
                 "Personalfluktuation: 3 Senior Engineers (davon 2 ASPICE-Leads) verliessen RSG zwischen Q3/2021 und "
                 "Q1/2022; Wissensverlust bei Radar-Signalverarbeitung erforderte externe Beratung (KPI: +220 TEUR).",
                 "Spaete Verfuegbarkeit der Mercedes-Radar-Frontends (Continental ARS510) erst im Juli 2022 statt "
                 "Maerz 2022 - HiL-Validierung konnte erst Q3 statt Q2 starten.",
                 "Underestimation des Kalibrieralgorithmus-Tunings: geplant 80 PT, tatsaechlich 215 PT. Hauptursache "
                 "Robustheit gegenueber EMV-Stoerungen in der Linie 17 (gepulste Schweissstationen in Nachbarstation).",
                 "Risikomanagement war zu reaktiv: Top-5-Risiken aus dem Risikoregister (R-001 bis R-005) trafen alle "
                 "ein, ohne dass Mitigationsmassnahmen rechtzeitig griffen.",
             ])),
            ("Top-5 Lessons Learned",
             ("list", [
                 "LL-01: Toolchain-Versionsstaende muessen vor Projektbeginn vertraglich fixiert und in der "
                 "Konfigurationsmanagement-Akte (SUP.8) festgeschrieben werden. Migrationen waehrend laufender "
                 "Sprints nur ueber formales Change Control Board (CCB) zulassen.",
                 "LL-02: Retention-Programm fuer Senior Engineers etablieren (Skill-Hochrisiko-Liste; max. 1 Abgang "
                 "pro Quartal je Domain). HR-Konsequenz: Stay-Boni von 6 % Jahresgehalt fuer ASPICE-Leads in "
                 "kritischen Projektphasen.",
                 "LL-03: Hardware-Komponentenverfuegbarkeit als Top-Risiko in jedes Projektrisikoregister; "
                 "Pufferzeit von >= 8 Wochen zwischen Hardware-Bereitstellung und HiL-Validierungsbeginn einplanen.",
                 "LL-04: Tuning-Aufwaende fuer Kalibrieralgorithmen werden systematisch unterschaetzt; "
                 "neue Schaetzformel: 2,5x Basisaufwand bei OEM-Linien mit EMV-kritischer Umgebung.",
                 "LL-05: Monatliches Risiko-Review reicht nicht aus; ab PRJ-2023-001 wird woechentliches Top-Risiken "
                 "Standup (15 Minuten, Freitag 14:00) verpflichtend.",
             ])),
            ("Folge-Massnahmen / Massnahmenplan",
             [["Massnahme", "Verantwortlich", "Termin", "Status"],
              ["Toolchain-Vereinbarung als Vertragsanlage (LL-01)", "Stefan Bayer (PMO)", "31.03.2023", "OFFEN"],
              ["Stay-Bonus-Programm Senior Engineers (LL-02)", "Petra Kessler (HR)", "30.04.2023", "IN ARBEIT"],
              ["Update Risikoregister-Vorlage v3.0 (LL-03)", "Lars Wittmann", "15.04.2023", "OFFEN"],
              ["Schaetzformel-Update (LL-04)", "Dr. Sabrina Halbig", "30.06.2023", "OFFEN"],
              ["Wkl. Top-Risiken Standup einfuehren (LL-05)", "alle PL", "ab 01.04.2023", "GEPLANT"]]),
            ("Schlussfolgerung",
             "Trotz operativer Schwierigkeiten gilt PRJ-2021-002 als strategischer Erfolg: RSG hat sich als "
             "kompetenter ADAS-Software-Partner bei Mercedes-Benz etabliert und konnte parallel den Anschluss"
             "auftrag fuer EQE / EQA-Plattform (PRJ-2023-004) im Volumen von rd. 22 Mio. EUR sichern. Die hier "
             "festgehaltenen Lessons Learned werden in das RSG-Wissensmanagement (Confluence Space 'RSG-LL') "
             "ueberfuehrt und sind verpflichtende Lektuere fuer neue Projektleiter."),
            ("Freigabe",
             signatures("Lars Wittmann", "Lead Developer / Projektleiter PRJ-2021-002", "Brennhagen Software GmbH",
                        "Dr. Klaus Kessler", "Werkleiter / Geschaeftsfuehrer RSG", "Brennhagen Software GmbH",
                        place=PLACE, date_str_="15. Maerz 2023")),
        ])


# ============================================================================
# 2) RSG Arbeitsvertraege (5x)
# ============================================================================
def rsg_arbeitsvertrag(fname, position, name_mitarbeiter, gehalt_eur, bonus_pct,
                       eintritt, taetigkeit_beschreibung, qualifikation):
    write_doc(f"{BASE}/{fname}", H_RSG,
        f"Anstellungsvertrag - {position}",
        subtitle=f"Vertrag zwischen Brennhagen Software GmbH und {name_mitarbeiter}",
        sections=[
            ("Vertragsparteien",
             f"Brennhagen Software GmbH, Lyonel-Feininger-Strasse 28, 80807 Muenchen, "
             f"eingetragen im Handelsregister des Amtsgerichts Muenchen unter HRB 319872, "
             f"vertreten durch den Geschaeftsfuehrer Dr. Klaus Kessler "
             f"(nachfolgend 'Arbeitgeberin' oder 'Gesellschaft' genannt),\n\n"
             f"und\n\n"
             f"{name_mitarbeiter} (nachfolgend 'Arbeitnehmer/in' oder 'Mitarbeiter/in' genannt) - "
             f"gemeinsam die 'Parteien'."),
            ("Praeambel",
             f"Die Brennhagen Software GmbH ist als 100%ige Tochtergesellschaft der Brennhagen Elektronik AG "
             f"(Stuttgart, HRB 726451) das Embedded-Software- und ADAS-Kompetenzzentrum des Brennhagen-Konzerns. "
             f"Die Gesellschaft entwickelt sicherheitskritische Softwarekomponenten gemaess ISO 26262 (ASIL A-D) "
             f"sowie ASPICE Level 2-3 fuer namhafte OEM-Kunden (BMW, Mercedes-Benz, Volkswagen, Stellantis). "
             f"Die Einstellung erfolgt zur Verstaerkung des Standorts Muenchen (340 Mitarbeiter)."),
            ("Vertragsregelungen",
             ("clauses", [
                 ("§ 1 Beginn, Position, Taetigkeit", [
                     f"Das Anstellungsverhaeltnis beginnt am {eintritt}.",
                     f"Der/Die Mitarbeiter/in wird als '{position}' eingestellt. {taetigkeit_beschreibung}",
                     f"Erforderliche Qualifikation und eingebrachte Expertise: {qualifikation}",
                     "Der Arbeitsort ist Muenchen (Standort Lyonel-Feininger-Strasse 28). Mobile Arbeit ist nach "
                     "Massgabe der RSG-Betriebsvereinbarung 'Mobile Arbeit' (BV-MA-2021) bis zu 3 Tagen pro Woche "
                     "moeglich; eine Anwesenheitspflicht am Standort besteht regelmaessig dienstags und donnerstags.",
                 ]),
                 ("§ 2 Probezeit, Befristung", [
                     "Die ersten sechs Monate gelten als Probezeit. Waehrend der Probezeit kann das Arbeitsverhaeltnis "
                     "von beiden Seiten mit einer Frist von zwei Wochen zum Monatsende ordentlich gekuendigt werden.",
                     "Der Vertrag wird auf unbestimmte Zeit geschlossen.",
                 ]),
                 ("§ 3 Verguetung", [
                     f"Das jaehrliche Bruttogrundgehalt betraegt {gehalt_eur:,} EUR, zahlbar in 12 gleichen "
                     f"Monatsraten jeweils zum Monatsende auf das vom Mitarbeiter benannte Konto.".replace(",", "."),
                     f"Zusaetzlich erhaelt der/die Mitarbeiter/in einen variablen Bonus i. H. v. bis zu "
                     f"{bonus_pct} % des Jahresgrundgehalts, abhaengig von Zielerreichung gemaess jaehrlicher "
                     f"Zielvereinbarung. Bewertungskriterien: individuelle Leistung (60 %), Teamziele (20 %), "
                     f"Konzernziel EBITDA-Marge (20 %).",
                     "Auszahlung des variablen Bonus erfolgt im April des Folgejahres nach Feststellung des "
                     "Konzernjahresabschlusses und Bestaetigung durch die Geschaeftsfuehrung.",
                 ]),
                 ("§ 4 Arbeitszeit, Urlaub", [
                     "Die regelmaessige woechentliche Arbeitszeit betraegt 40 Stunden, verteilt von Montag bis "
                     "Freitag. Vertrauensarbeitszeit gemaess BV-Vertrauensarbeitszeit-2019.",
                     "Der Urlaubsanspruch betraegt 30 Arbeitstage pro Kalenderjahr (5-Tage-Woche).",
                     "Ueberstunden sind mit dem Gehalt abgegolten. Mehrarbeit ueber 10 Stunden pro Woche bedarf der "
                     "Genehmigung des/der Vorgesetzten und kann durch Freizeit ausgeglichen werden.",
                 ]),
                 ("§ 5 Nebenleistungen", [
                     "Firmen-Laptop (MacBook Pro 16'' oder Dell Latitude 7440 nach Wahl), Smartphone (iPhone 15 / "
                     "Samsung Galaxy S24), Job-Ticket MVV-Premium fuer den Verbundraum Muenchen.",
                     "Betriebliche Altersvorsorge ueber Allianz Pensionsfonds AG mit Arbeitgeberzuschuss von 5 % des "
                     "Bruttogehalts (Cap: 280 EUR/Monat).",
                     "Weiterbildungsbudget i. H. v. 3.000 EUR/Jahr fuer fachliche Zertifizierungen (z. B. ASPICE, "
                     "ISO 26262 FSE, AUTOSAR Adaptive).",
                     "Mitgliedschaft im Urban Sports Club (Arbeitgeberzuschuss 50 %); Bike-Leasing JobRad.",
                 ]),
                 ("§ 6 Verschwiegenheit, IP", [
                     "Der/Die Mitarbeiter/in verpflichtet sich zu strikter Verschwiegenheit ueber alle Betriebs- und "
                     "Geschaeftsgeheimnisse - insbesondere Quellcode, Algorithmen, Kundenanforderungen, Preise und "
                     "OEM-Spezifikationen. Die Verschwiegenheitspflicht gilt auch nach Beendigung des Arbeitsverhaeltnisses.",
                     "Alle im Rahmen der Taetigkeit geschaffenen Arbeitsergebnisse (Source Code, Dokumentation, "
                     "Erfindungen, Designs) stehen ausschliesslich der Arbeitgeberin zu. Diensterfindungen werden "
                     "nach dem ArbEG behandelt.",
                 ]),
                 ("§ 7 Kuendigung", [
                     "Nach Ablauf der Probezeit gelten die gesetzlichen Kuendigungsfristen (§ 622 BGB), mindestens "
                     "drei Monate zum Monatsende.",
                     "Eine ausserordentliche Kuendigung aus wichtigem Grund bleibt vorbehalten.",
                     "Bei Beendigung sind saemtliche Arbeitsmittel (Laptop, Smartphone, Schluessel, Zugangsausweise) "
                     "unverzueglich zurueckzugeben.",
                 ]),
                 ("§ 8 Schlussbestimmungen", [
                     "Aenderungen und Ergaenzungen beduerfen der Schriftform. Es gilt deutsches Recht. Gerichtsstand "
                     "ist Muenchen.",
                     "Sollten einzelne Bestimmungen unwirksam sein, beruehrt dies nicht die Wirksamkeit der uebrigen "
                     "Bestimmungen. Es gilt die salvatorische Klausel.",
                 ]),
             ])),
            ("Unterschriften",
             signatures("Dr. Klaus Kessler", "Geschaeftsfuehrer", "Brennhagen Software GmbH",
                        name_mitarbeiter, "Mitarbeiter/in", "i. e. S.",
                        place=PLACE, date_str_=eintritt)),
        ])


rsg_arbeitsvertrag("RSG_Arbeitsvertrag_01_Geschäftsführer_in_R_2022.docx",
    "Geschaeftsfuehrer/in / Werkleiter RSG Muenchen", "Dr. Klaus Kessler",
    195_000, 35, "01. Maerz 2022",
    "Verantwortung fuer die Gesamtleitung der Brennhagen Software GmbH mit 340 Mitarbeitern. Berichtslinie an "
    "den Vorstand der Brennhagen Elektronik AG (COO Dr. Thomas Weber). Verantwortung fuer P&L, Strategie, "
    "Personalentwicklung und Kundenbeziehungen (Mercedes, BMW, VW, Stellantis).",
    "Promotion in Informatik (TU Muenchen, 2008); 15 Jahre Erfahrung in Automotive Software (zuvor "
    "Continental AG, Leitung Software-Center Regensburg); Zertifizierungen ASPICE Assessor (intacs), "
    "ISO 26262 FSE Engineer.")

rsg_arbeitsvertrag("RSG_Arbeitsvertrag_02_Produktionsleiter_in_2022.docx",
    "Produktionsleiter/in Software-Release", "Dipl.-Ing. Markus Hofbauer",
    118_000, 22, "15. April 2022",
    "Leitung der Software-Release-Produktion (CI/CD, Build-Pipelines, Release-Management fuer "
    "Embedded-Software-Auslieferungen an OEM-Kunden). Verantwortung fuer 18 Mitarbeiter im Bereich "
    "DevOps / Release Engineering.",
    "Dipl.-Ing. Informationstechnik (FH Regensburg); 12 Jahre Erfahrung im Automotive-Build-Management "
    "(zuvor Elektrobit Automotive). Zertifizierungen: Jenkins CCE, Yocto Project, AUTOSAR Classic.")

rsg_arbeitsvertrag("RSG_Arbeitsvertrag_03_Qualitätsmanagerin_M_2022.docx",
    "Qualitaetsmanagerin / ASPICE-Lead Assessor", "Dr. Sabrina Halbig",
    132_000, 25, "01. Juni 2022",
    "Leitung des Qualitaets- und Prozess-Managements RSG (ASPICE Level 2-3, ISO 9001:2015, "
    "ISO 26262). Verantwortung fuer interne ASPICE-Assessments, OEM-Audits und Lieferanten-Audits "
    "nach VDA 6.3. Direkter Bericht an die Geschaeftsfuehrung.",
    "Promotion Informatik (KIT Karlsruhe, 2014); 10 Jahre Erfahrung als ASPICE-Lead-Assessor "
    "(KUGLER MAAG CIE, dann BMW Group). Zertifizierungen: intacs Principal Assessor ASPICE, "
    "ISO 26262 ASIL D Trainer, Lead Auditor ISO 9001.")

rsg_arbeitsvertrag("RSG_Arbeitsvertrag_04_Finanzcontroller_Mün_2022.docx",
    "Finanzcontroller/in Muenchen", "Christine Weidinger",
    98_000, 18, "01. September 2022",
    "Verantwortung fuer das operative Controlling RSG: Monats-/Quartalsabschluesse (HGB / IFRS), "
    "Forecast, Budgetierung, Projektcontrolling (ca. 25 aktive OEM-Projekte). Schnittstelle zum "
    "Group Controlling Stuttgart (Florian Maier).",
    "Master Finance & Accounting (LMU Muenchen, 2013); CMA-Zertifizierung; 9 Jahre Controlling-"
    "Erfahrung (zuvor MAN Truck & Bus AG, Projektcontrolling).")

rsg_arbeitsvertrag("RSG_Arbeitsvertrag_05_HR-Manager_München_2022.docx",
    "HR-Manager/in Muenchen", "Petra Kessler",
    105_000, 18, "01. Oktober 2022",
    "Verantwortung fuer HR Operations am Standort Muenchen (340 MA), Recruiting (Schwerpunkt Senior "
    "Software Engineers, ASPICE-Leads), Personalentwicklung, Tarif-/Betriebsratverhandlungen. Bericht "
    "an Geschaeftsfuehrung und HR-Direktor Holding Stuttgart.",
    "Master Personalmanagement (Uni Augsburg, 2011); SHRM-SCP-Zertifizierung; 11 Jahre HR-Erfahrung "
    "(zuvor Infineon Technologies AG, Senior HR Business Partner).")


lessons_learned_adas()


# ============================================================================
# 3) RSG Compliance Report 2023
# ============================================================================
write_doc(f"{BASE}/RSG_Compliance_Report_2023.docx", H_RSG,
    "Compliance-Report 2023 - Brennhagen Software GmbH",
    subtitle="Jahresbericht der Compliance-Funktion RSG fuer das Geschaeftsjahr 2023",
    confidential=True,
    sections=[
        ("Berichtszeitraum / Adressaten",
         "Berichtszeitraum: 01.01.2023 bis 31.12.2023\n"
         "Erstellt von: Dr. Sabrina Halbig (Compliance Officer RSG)\n"
         "Adressaten: Dr. Klaus Kessler (Geschaeftsfuehrer RSG), Group Compliance Officer Stuttgart "
         "(Dr. Cornelia Lerch), Aufsichtsrats-Pruefungsausschuss Brennhagen Elektronik AG\n"
         "Klassifizierung: STRENG VERTRAULICH - nur fuer den definierten Empfaengerkreis"),
        ("Zusammenfassung",
         "Im Berichtsjahr 2023 wurde das Compliance-Management-System (CMS) der Brennhagen Software GmbH "
         "weiterentwickelt und an die aktualisierten Konzernvorgaben (REA-Compliance-Richtlinie 2023, "
         "Stand 15.04.2023) angepasst. Es wurden keine wesentlichen Compliance-Verstoesse festgestellt. "
         "Drei meldepflichtige Hinweise gingen ueber das Whistleblower-System ein, davon eine weitere "
         "Untersuchung mit abschliessendem Ergebnis 'unbegruendet'. Die jaehrliche Compliance-Schulung "
         "wurde von 327 der 340 Mitarbeiter absolviert (96,2 %)."),
        ("Compliance-Organisation RSG",
         [["Funktion", "Person", "Berichtslinie"],
          ["Geschaeftsfuehrer / CMS-Verantwortlicher", "Dr. Klaus Kessler", "Vorstand REA"],
          ["Compliance Officer RSG", "Dr. Sabrina Halbig", "GF / Group Compliance"],
          ["Datenschutzbeauftragte (DSB)", "RA Andrea Reiter (extern, BvD)", "Compliance / GF"],
          ["Hinweisgeber-Beauftragter (LkSG)", "Stefan Bayer (PMO)", "Compliance"],
          ["IT-Sicherheitsbeauftragter", "Tobias Schwaiger", "Compliance / IT"]]),
        ("Compliance-Risiken 2023 - Schwerpunkte",
         ("list", [
             "Exportkontrolle / Sanktionen: Ueberwachung von Embargo-Lieferungen (Russland, Iran, "
             "Nordkorea); Dual-Use-Klassifizierung der ADAS-Software (Annex I EU-Verordnung 2021/821).",
             "Datenschutz (DSGVO / BDSG-neu): Verarbeitung von Mitarbeiterdaten, Bewerberdaten, "
             "Fahrzeugdaten aus OEM-Testflotten; ein meldepflichtiger Datenschutzvorfall (Versand falscher "
             "Anhang an Bewerber) wurde fristgerecht (72 Std.) an LDA Bayern gemeldet.",
             "Korruptionspraevention: jaehrliche Geschenke-/Einladungen-Erklaerung aller Fuehrungskraefte; "
             "Limit 50 EUR/Geschenk, 100 EUR/Einladung; alle Vorgaenge ueber 25 EUR sind im Compliance-"
             "Register zu dokumentieren.",
             "Kartellrecht: jaehrliche Kartellrechtsschulung fuer Vertrieb und Einkauf; Verbot von "
             "Preisabsprachen mit Wettbewerbern (Elektrobit, etas, Vector).",
             "Lieferkettensorgfaltspflichtengesetz (LkSG): RSG faellt erst ab 01.01.2024 unter den "
             "Anwendungsbereich; Vorbereitungen 2023 abgeschlossen (Risikoanalyse, Praeventionsmassnahmen).",
         ])),
        ("Hinweise 2023 ueber das BKMS-Whistleblower-System",
         [["Eingang", "Inhalt (anonymisiert)", "Ergebnis", "Abgeschlossen"],
          ["12.03.2023", "Behauptung unzulaessiger Geschenkannahme Einkauf", "unbegruendet (kein Vorfall)", "28.04.2023"],
          ["07.07.2023", "Mobbing-Vorwurf gegen Teamlead R&D", "begruendet teilw., HR-Massnahmen", "30.09.2023"],
          ["19.10.2023", "Datenmissbrauchsverdacht externer Dienstleister", "unbegruendet (Missverstaendnis)", "15.12.2023"]]),
        ("Schulungen und Awareness",
         "2023 wurden folgende verpflichtende Online-Trainings (E-Learning-Plattform LMS-Brennhagen) durchgefuehrt: "
         "Code of Conduct (Quote 96,2 %), Datenschutz/DSGVO (96,2 %), Kartellrecht (Vertrieb/Einkauf, "
         "Quote 100 %), Korruptionspraevention/Geschenke (98,4 %), Informationssicherheit (95,1 %). Die "
         "Schulungsquote von >= 95 % wurde in allen Pflichttrainings erreicht. Die noch fehlenden 3,8 % "
         "(Code of Conduct) sind ueberwiegend Langzeitkranke und Elternzeit-Faelle, fuer die das Training "
         "bei Rueckkehr nachgeholt wird."),
        ("Massnahmen / Roadmap 2024",
         ("list", [
             "LkSG-Konformitaet: Implementierung der vollstaendigen Risikoanalyse fuer alle Tier-1-Lieferanten "
             "(rd. 80 Lieferanten weltweit) bis 30.06.2024.",
             "ISO 27001:2022-Zertifizierung des RSG-Standorts (geplant Q4/2024) - Vorbereitung der Stage-1- und "
             "Stage-2-Audits durch TUEV SUED.",
             "Aktualisierung des Risiko-Register Schwerpunkt KI/AI-Compliance (AI-Act-Vorbereitung).",
             "Ausbau des Whistleblower-Systems um eine Sprachoption (englisch, polnisch, tschechisch) zur "
             "Anbindung weiterer Konzernstandorte.",
         ])),
        ("Unterschriften",
         signatures("Dr. Sabrina Halbig", "Compliance Officer RSG", "Brennhagen Software GmbH",
                    "Dr. Klaus Kessler", "Geschaeftsfuehrer / CMS-Verantwortlicher", "Brennhagen Software GmbH",
                    place=PLACE, date_str_="15. Februar 2024")),
    ])


# ============================================================================
# 4) RSG ControlPlans (4x) - Produktionslenkungsplaene fuer Software-Releases
# ============================================================================
def control_plan(fname, produkt, prod_lang, oem_kunde, sw_version,
                 asil_level, aspice_level, additional_features):
    write_doc(f"{BASE}/{fname}", H_RSG,
        f"Control Plan {produkt} - Software-Produktionslenkungsplan",
        subtitle=f"Erstellt gemaess IATF 16949 Kap. 8.5.1 und VDA Band 4 fuer {produkt} ({prod_lang})",
        sections=[
            ("Produkt-Identifikation",
             f"Produkt: {produkt} - {prod_lang}\n"
             f"Software-Version: {sw_version}\n"
             f"Hauptkunde: {oem_kunde}\n"
             f"Sicherheitsklasse: ISO 26262 {asil_level}\n"
             f"ASPICE-Prozessreife: {aspice_level}\n"
             f"Control-Plan-Status: in Kraft ab 01.01.2023\n"
             f"Verantwortlich Erstellung: Dr. Sabrina Halbig (QM); Lars Wittmann (Tech Lead)"),
            ("Anwendungsbereich",
             f"Dieser Control Plan beschreibt die Pruef- und Lenkungsmassnahmen fuer alle Software-"
             f"Produktionsschritte des Produkts {produkt}. Er gilt fuer alle Releases der Hauptversion "
             f"{sw_version} und nachfolgende Patch-Releases im Jahr 2023. Der Plan ist integraler "
             f"Bestandteil der ASPICE-Akte und wird bei jeder Aenderung des Produktdesigns oder der "
             f"Toolchain (Major-Upgrade) ueberarbeitet."),
            ("Pruef- und Lenkungsplan",
             [["Prozessschritt", "Pruefmerkmal", "Methode", "Frequenz", "Verantwortlich", "Aufzeichnung"],
              ["SWE.1 Anforderungsanalyse", "Vollstaendigkeit / Traceability", "Polarion Review", "je Release", "Anforderungsmanager", "Polarion AuditLog"],
              ["SWE.2 Architekturdesign", "Architekturkonformitaet", "Enterprise Architect Check", "je Release", "Architekt", "EA-Modell"],
              ["SWE.3 Detaildesign", "Coding-Standard MISRA C 2012", "PC-lint Plus", "je Commit", "Entwickler/Reviewer", "Build-Log"],
              ["SWE.4 Unit Test", "Code Coverage >= 95 % (Branch)", "Tessy / VectorCAST", "je Build", "Entwickler", "Coverage-Report"],
              ["SWE.5 Integration", "Integrationstest 100 % Pass", "Vector CANoe 14", "je Release", "Test-Engineer", "CANoe TestReport"],
              ["SWE.6 Software Qualifikation", "HiL-Test 100 % Pass + EMV-Robustheit", "ETAS LABCAR", "je Release", "Validation", "Testprotokoll"],
              ["SUP.8 KM / Versionierung", "Git-Tag konform zu Release-ID", "Git-Hook", "je Release", "Build-Master", "Git-Log"],
              ["SUP.10 CCB-Freigabe", "Aenderungen >= Schwellwert", "Jira CCB-Workflow", "je Change", "CCB-Vorsitz", "Jira CCB-Ticket"],
              ["Final Release Approval", "Vier-Augen-Pruefung", "Release Notes Review", "je Release", "GF + Tech Lead", "Release Letter"]]),
            ("Spezielle Merkmale (Special Characteristics)",
             ("list", [
                 f"Funktional sicherheitsrelevante Funktionen ({asil_level}) sind im Quellcode mit dem "
                 f"Annotations-Tag @ASIL gekennzeichnet und unterliegen einer 100%-Code-Review-Pflicht "
                 f"(4-Augen-Prinzip; mind. ein FSE-zertifizierter Reviewer).",
                 "Cyber-Security-relevante Code-Sektionen (gemaess ISO/SAE 21434) sind mit @SecRel "
                 "gekennzeichnet und unterliegen zusaetzlich einem statischen Security-Scan (Coverity).",
                 "Aenderungen an der Konfigurationsbeschreibung der ECU (XCP-Layer) erfordern "
                 "regressionstest-Komplettlauf vor Release.",
                 f"Zusatzfunktionen: {additional_features}",
             ])),
            ("Lenkungsmassnahmen bei Abweichungen",
             "Bei Abweichungen (z. B. Coverage < 95 %, fehlgeschlagene Integrationstests, MISRA-"
             "Violations Kategorie 'Mandatory') wird der Release-Prozess automatisch durch die "
             "CI/CD-Pipeline (Jenkins) gestoppt. Eine Freigabe darf nur durch die GF oder den "
             "stellv. Tech Lead nach dokumentierter Risikobewertung (Deviation Permit) erfolgen. "
             "Deviation Permits werden monatlich im Q-Review (Sabrina Halbig) eskaliert und im "
             "QSR (Quarterly Quality Review) mit der Konzern-Q-Leitung Heilbronn abgestimmt."),
            ("Reaktionsplan",
             [["Abweichungsart", "Sofortmassnahme", "Eskalationsstufe"],
              ["Coverage < 95 %", "Build-Stopp; ergaenzende Unit-Tests", "Tech Lead binnen 24 h"],
              ["MISRA Mandatory Violation", "Build-Stopp; Refactoring", "Tech Lead + QM binnen 24 h"],
              ["Integrationstest-Fehler", "Bug-Ticket + Sprint-Replan", "PL + QM binnen 48 h"],
              ["HiL-Test EMV-Fehler", "FSE-Review + Mitigation", "FSE-Manager + QM binnen 5 AT"],
              ["Sicherheitsrelevante Findings", "Sofort-Stopp; Field-Action-Pruefung", "GF + Group QM"]]),
            ("Aenderungsmanagement",
             "Jede Aenderung am Control Plan ist ueber Change-Request im ASPICE-Tool (Polarion) zu "
             "beantragen und wird durch das CCB (Change Control Board: GF, QM, Tech Lead, "
             "Anforderungsmanager) bewertet und freigegeben. Aenderungen werden in der QM-Akte "
             "(Polarion Space 'RSG-QM') dokumentiert. Dieser Control Plan tritt zum 01.01.2023 in "
             "Kraft und ersetzt die Vorgaengerversion v2.4 vom 15.07.2022. Das naechste planmaessige "
             "Review erfolgt am 15.01.2024."),
            ("Freigabe",
             signatures("Dr. Sabrina Halbig", "Qualitaetsmanagement-Leitung", "Brennhagen Software GmbH",
                        "Dr. Klaus Kessler", "Geschaeftsfuehrer", "Brennhagen Software GmbH",
                        place=PLACE, date_str_="20. Dezember 2022")),
        ])


control_plan("RSG_ControlPlan_ADAS-V4D_2023.docx",
    "ADAS-V4D", "Radar Fusion Steuergeraet (Level-2/3 ADAS)",
    "Mercedes-Benz Group AG (EQS / EQE Sindelfingen)", "4.2.0-RELEASE",
    "ASIL B (D fuer Bremsanforderungen)", "ASPICE Level 3 (intacs-bestaetigt 07/2022)",
    "Radar-Cluster-Fusion (5 Sensoren 77 GHz); Cyber-Security gemaess ISO/SAE 21434; OTA-Fuselect")

control_plan("RSG_ControlPlan_BMS-12_2023.docx",
    "BMS-12", "BatteryMS-12 (Batteriemanagementsystem EV)",
    "Volkswagen AG (ID.7 / MEB+) und Hyundai Motor (E-GMP)", "3.1.5-RELEASE",
    "ASIL D (Hochvolt-Sicherheit)", "ASPICE Level 3 (intacs-bestaetigt 09/2021)",
    "Cell-Balancing-Algorithmus mit ML-Komponente (TensorFlow Lite Micro); SoH/SoC-Estimation")

control_plan("RSG_ControlPlan_ECU-900_2023.docx",
    "ECU-900", "Powertrain-ECU Gen3 (Hybrid/BEV)",
    "Volkswagen AG (MEB+/MQB-Evo) und Stellantis N.V. (STLA Medium)", "5.0.2-RELEASE",
    "ASIL C", "ASPICE Level 2 (intacs-bestaetigt 03/2022)",
    "AUTOSAR Classic 4.4; CAN-FD / CAN-XL Gateway; Energy-Manager fuer Rekuperation")

control_plan("RSG_ControlPlan_ICP-3_2023.docx",
    "ICP-3", "InfoConnect Pro (Infotainment-Modul)",
    "BMW Group (G70 / iX5) und Mercedes-Benz (EQS MBUX Hyperscreen)", "7.3.1-RELEASE",
    "QM (kein ASIL - QM-Kategorie B)", "ASPICE Level 2 (intacs-bestaetigt 11/2021)",
    "Android Automotive Stack 13; OTA-Updates; HMI fuer 5 Sprachen; Apple CarPlay / Android Auto Wireless")


# ============================================================================
# 5) RSG IC Quartalsberichte 2019-2020 (8x)
# ============================================================================
def ic_quartalsbericht(fname, jahr, q, umsatz_mio, ebit_mio, mitarbeiter, hauptprojekte):
    write_doc(f"{BASE}/{fname}", H_RSG,
        f"Intercompany Quartalsbericht RSG {q}/{jahr}",
        subtitle=f"Intern - Bericht der Geschaeftsfuehrung RSG an die Konzern-Steuerung Brennhagen Elektronik AG",
        sections=[
            ("Berichtsuebersicht",
             f"Berichtsperiode: {q}/{jahr}\n"
             f"Berichtende Gesellschaft: Brennhagen Software GmbH, Muenchen (HRB 319872)\n"
             f"Berichtsempfaenger: COO REA (Dr. Thomas Weber), CFO REA (Laura Bauer), Group Controlling (F. Maier)\n"
             f"Berichtsverfasser: Dr. Klaus Kessler (GF RSG), Christine Weidinger (Controlling RSG)\n"
             f"Stand: Ende {q}/{jahr}"),
            ("Finanz-Kennzahlen RSG ({jahr})".replace("{jahr}", jahr),
             [["Kennzahl", q+"/"+jahr, "Vorjahr (PY)", "Abweichung %"],
              ["Umsatz (Mio. EUR)", f"{umsatz_mio:.1f}", f"{umsatz_mio*0.92:.1f}", "+8,7 %"],
              ["EBIT (Mio. EUR)", f"{ebit_mio:.2f}", f"{ebit_mio*0.85:.2f}", "+17,6 %"],
              ["EBIT-Marge (%)", f"{(ebit_mio/umsatz_mio)*100:.1f} %", f"{(ebit_mio/umsatz_mio)*100*0.94:.1f} %", "+0,9 pp"],
              ["Mitarbeiter (FTE, Periodenende)", str(mitarbeiter), str(int(mitarbeiter*0.94)), "+6 %"],
              ["Konzern-IC-Anteil am Umsatz", "ca. 35 %", "ca. 32 %", "+3 pp"]]),
            ("Operative Entwicklung im Quartal",
             f"Im {q}/{jahr} verzeichnete die Brennhagen Software GmbH eine planmaessige Geschaeftsentwicklung. "
             f"Der Umsatz von {umsatz_mio:.1f} Mio. EUR liegt 2 % oberhalb des Budgetwerts und 8,7 % "
             f"ueber dem Vorjahresquartal. Treiber sind insbesondere die OEM-Ramp-up-Projekte fuer "
             f"ADAS-V4D und BMS-12. Die EBIT-Marge von {(ebit_mio/umsatz_mio)*100:.1f} % entspricht dem Ziel "
             f"(>= 14 %). Der Personalstand stieg auf {mitarbeiter} FTE durch gezielte Einstellungen im "
             f"Bereich Senior Engineers / ASPICE-Leads."),
            ("Hauptprojekte im Quartal",
             ("list", hauptprojekte)),
            ("Risiken / Issues",
             ("list", [
                 "Engpass bei Senior Embedded Software Engineers im Muenchner Arbeitsmarkt - 14 offene "
                 "Vakanzen, durchschnittliche Time-to-Hire 4,5 Monate. Gegenmassnahme: Recruiting in "
                 "Polen / Tschechien (Remote-Modell) sowie Hochschulkooperation TU Muenchen.",
                 "Verschiebung Mercedes-Benz Linienanlauf EQE um 4 Wochen (Hardware-Verzug bei "
                 "Lieferant Continental) - geringe Auswirkung auf Q-Umsatz (< 0,3 Mio. EUR).",
                 "Lizenzkosten Vector CANoe / CANalyzer steigen 2020 um 6 % - bereits im Budget eingeplant.",
             ])),
            ("Ausblick Folge-Quartal",
             "Das Folge-Quartal ist gut abgesichert; das Auftragspolster betraegt 24 Mio. EUR (Coverage > 1,4). "
             "Die EBIT-Marge sollte sich angesichts steigender Effizienz im Software-Engineering und der "
             "vollstaendigen Auslastung der HiL-Kapazitaeten weiter verbessern. Risiken: Lieferanten-"
             "Engpaesse bei OEM-Hardware sowie globale Mikrochip-Knappheit (Auswirkung auf RSG nur "
             "mittelbar ueber OEM-Linienanlauf-Termine)."),
            ("Genehmigung",
             signatures("Dr. Klaus Kessler", "Geschaeftsfuehrer RSG", "Brennhagen Software GmbH",
                        "Christine Weidinger", "Controlling RSG", "Brennhagen Software GmbH",
                        place=PLACE, date_str_=f"30. {['Maerz','Juni','September','Dezember'][int(q[1])-1]} {jahr}")),
        ])


# 2019
ic_quartalsbericht("RSG_IC_Quartalsbericht_2019_Q1.docx", "2019", "Q1", 11.8, 1.55, 268, [
    "ICP-3 Release 5.2 (BMW iX) - planmaessige Auslieferung 15.03.",
    "BMS-12 Konzeptphase fuer VW MEB-Plattform - Gate 2 erreicht",
    "ADAS-V4D Forschungspartnerschaft mit TU Muenchen gestartet (KI-Radar-Fusion)",
    "ASPICE Re-Assessment Vorbereitung (geplant Q3/2019)",
])
ic_quartalsbericht("RSG_IC_Quartalsbericht_2019_Q2.docx", "2019", "Q2", 12.4, 1.68, 274, [
    "ECU-900 Series-Bring-up Stellantis (FIAT 500e) - Erstauslieferung 11.05.",
    "BMS-12 Detail-Design abgeschlossen - Start Implementierung",
    "Erweiterung HiL-Labor um 3 neue Pruefplaetze (Investition 0,8 Mio. EUR)",
    "Kooperation Continental fuer Radar-Frontend ARS510 vertraglich fixiert",
])
ic_quartalsbericht("RSG_IC_Quartalsbericht_2019_Q3.docx", "2019", "Q3", 12.9, 1.78, 281, [
    "ASPICE Level 2 Re-Assessment durch KUGLER MAAG CIE - 'consistently performed' bestaetigt",
    "ICP-3 Release 5.3 mit OTA-Faehigkeit - erste BMW-OTA-Welle ausgespielt",
    "ADAS-V4D Konzept-Bewertung mit Mercedes-Benz (Sindelfingen) - Eingang Pilotauftrag",
    "Stellenaufbau: 7 neue Senior-Engineer-Einstellungen im Quartal",
])
ic_quartalsbericht("RSG_IC_Quartalsbericht_2019_Q4.docx", "2019", "Q4", 13.5, 1.92, 287, [
    "BMS-12 SOP fuer VW e-Golf-Restposten - 1.250 Stueck",
    "ICP-3 Release 5.4 - HMI-Ueberarbeitung fuer BMW iX5",
    "ADAS-V4D PRJ-2021-002 als grosses Folgeprojekt vertraglich fixiert (Volumen 5 Mio. EUR)",
    "Jahresabschluss 2019 vorbereitet - Umsatz 50,6 Mio. EUR (+12 % yoy)",
])
# 2020
ic_quartalsbericht("RSG_IC_Quartalsbericht_2020_Q1.docx", "2020", "Q1", 13.8, 1.95, 291, [
    "COVID-19 Reaktion: 100 % Home-Office ab 16.03., kein operativer Stillstand",
    "ADAS-V4D PRJ-2021-002 Konzeptphase verzoegert (-3 Wochen) wg. Mercedes-Lockdown",
    "ICP-3 Release 6.0 fuer BMW iX (Hauptanlauf) - planmaessiger SOP 28.03.",
    "BMS-12 zweite VW-Plattform (ID.4) - Auftragseingang 8 Mio. EUR Laufzeit 2020-2024",
])
ic_quartalsbericht("RSG_IC_Quartalsbericht_2020_Q2.docx", "2020", "Q2", 13.2, 1.82, 295, [
    "Umsatzrueckgang ggue. Q1 (-4 %) durch OEM-Werksschliessungen (April/Mai); ICP-3 + ECU-900 betroffen",
    "Kurzarbeit fuer Bereich 'Validation' (50 MA) im Mai (60 % Reduktion) - aufgehoben Ende Juni",
    "ADAS-V4D weiter im Plan, Mercedes-Engineering vollstaendig im Home-Office produktiv",
    "Cyber-Security-Audit nach ISO/SAE 21434 (in Entwicklung) durch TUEV SUED gestartet",
])
ic_quartalsbericht("RSG_IC_Quartalsbericht_2020_Q3_v2.docx", "2020", "Q3", 14.1, 2.03, 302, [
    "Vollstaendige Erholung von COVID-Effekten - OEM-Abrufe wieder im Plan",
    "ADAS-V4D Gate G2 erreicht (Konzeptphase abgeschlossen) - 2 Wochen Verzug, im Puffer",
    "BMS-12 Release 2.5 fuer VW ID.4 SOP 21.09. erfolgreich",
    "ASPICE Level 3 Aufstiegsplan beschlossen - Ziel Assessment Sommer 2022",
])
ic_quartalsbericht("RSG_IC_Quartalsbericht_2020_Q4.docx", "2020", "Q4", 14.8, 2.21, 308, [
    "Starkes Schlussquartal - alle OEM-Abrufe vollstaendig erfuellt",
    "Jahresumsatz 2020: 55,9 Mio. EUR (+10,5 % yoy) trotz COVID - Margenausweitung auf 14,0 %",
    "ADAS-V4D Hardware-Bereitstellung Continental verzoegert um 6 Wochen - Pufferpuffer aufgebraucht",
    "Recruiting-Plan 2021: +35 FTE geplant, davon 12 Senior-Engineers",
])


# ============================================================================
# 6) RSG IC Rechnungen 2020-2022 (32x) - intercompany invoices to REA
# ============================================================================
def ic_rechnung_rsg(fname, jahr, monat, leistungspaket, betrag_eur, status=None):
    rn = f"RSG-IC-{jahr}{monat:02d}-001"
    mon_str = ["", "Januar","Februar","Maerz","April","Mai","Juni","Juli","August",
               "September","Oktober","November","Dezember"][monat]
    rd = f"{(monat*3) % 28 + 1}. {mon_str} {jahr}"
    write_doc(f"{BASE}/{fname}", H_RSG,
        f"Rechnung Nr. {rn} - Intercompany Leistung an Brennhagen Elektronik AG",
        subtitle=f"Leistungszeitraum {mon_str} {jahr} - {leistungspaket}",
        draft=(status=="ENTWURF" or status=="WIP"),
        sections=[
            ("Rechnungsdaten",
             f"Rechnungs-Nr.: {rn}\n"
             f"Rechnungsdatum: {rd}\n"
             f"Leistungsdatum: 01. - {28 if monat==2 else 30}. {mon_str} {jahr}\n"
             f"Faelligkeitsdatum: 30 Tage netto (Konzern-Verrechnungsvereinbarung 2020)\n"
             f"Status: {status or 'FINAL'}"),
            ("Rechnungssteller (Leistungserbringer)",
             "Brennhagen Software GmbH\n"
             "Lyonel-Feininger-Strasse 28\n"
             "80807 Muenchen\n"
             "HRB 319872, Amtsgericht Muenchen\n"
             "USt-IdNr. DE 245 678 901\n"
             "Geschaeftsfuehrer: Dr. Klaus Kessler\n"
             "Bankverbindung: Stadtsparkasse Muenchen, IBAN DE89 7015 0000 0123 4567 89"),
            ("Rechnungsempfaenger (Leistungsempfaenger)",
             "Brennhagen Elektronik AG\n"
             "Vaihinger Strasse 120\n"
             "70567 Stuttgart\n"
             "HRB 726451, Amtsgericht Stuttgart\n"
             "USt-IdNr. DE 312 487 901"),
            ("Leistungsbeschreibung",
             f"Die Rechnung umfasst die im Berichtsmonat {mon_str} {jahr} erbrachten konzerninternen "
             f"Entwicklungs-, Beratungs- und Support-Leistungen der Brennhagen Software GmbH fuer die "
             f"Konzernmuttergesellschaft Brennhagen Elektronik AG.\n\n"
             f"Schwerpunkt der Leistungen: {leistungspaket}\n\n"
             f"Die Verrechnung erfolgt nach der konzerninternen Verrechnungsvereinbarung vom 15.12.2019 "
             f"(REA-IC-Pricing 2020) auf Basis Cost-Plus 7,5 % (entspricht dem mittleren Quartil der "
             f"Comparable Profits Method gemaess Transfer-Pricing-Studie KPMG 2019)."),
            ("Rechnungsposten",
             [["Pos.", "Leistungskategorie", "Std.", "Stundensatz", "Betrag (EUR)"],
              ["1", "Senior Embedded Engineering", "—", "135 EUR/h", f"{betrag_eur*0.55:,.0f}".replace(",", ".")],
              ["2", "ASPICE-/QM-Beratung", "—", "150 EUR/h", f"{betrag_eur*0.15:,.0f}".replace(",", ".")],
              ["3", "Integration & HiL-Validierung", "—", "120 EUR/h", f"{betrag_eur*0.20:,.0f}".replace(",", ".")],
              ["4", "Projektmanagement / Reporting", "—", "115 EUR/h", f"{betrag_eur*0.10:,.0f}".replace(",", ".")],
              ["", "Zwischensumme netto", "", "", f"{betrag_eur:,.0f}".replace(",", ".")],
              ["", "USt 19 % (gem. § 13b UStG entfaellt - Reverse Charge)", "", "", "0,00"],
              ["", "Rechnungsbetrag gesamt", "", "", f"{betrag_eur:,.0f}".replace(",", ".")]]),
            ("Zahlungshinweise",
             f"Bitte ueberweisen Sie den Rechnungsbetrag von {betrag_eur:,.0f} EUR ".replace(",", ".") +
             f"unter Angabe der Rechnungs-Nr. {rn} bis zum Faelligkeitsdatum auf das oben angegebene Konto. "
             "Die Verrechnung erfolgt nach Konzern-Verrechnungsvereinbarung im Rahmen des monatlichen "
             "Cash-Pools (Sweep DB-Hauptkonto Stuttgart)."),
            ("Anlagen",
             "Anlage 1: Stundennachweis Mitarbeiter (separates PDF)\n"
             "Anlage 2: Projekt-Zuordnung WBS-Elemente (separates PDF)\n"
             "Anlage 3: Kostenstellenbericht RSG (SAP-Export)"),
        ])


# 2020 (12 rechnungen except 03 and 07 missing)
ic_rechnung_rsg("RSG_IC_Rechnung_2020_01.docx", "2020", 1,
    "ICP-3 Hauptanlauf BMW iX Software-Validierung; BMS-12 Konzeptarbeit VW MEB", 245_800)
ic_rechnung_rsg("RSG_IC_Rechnung_2020_02.docx", "2020", 2,
    "ICP-3 Bugfix-Release 5.4.2; ADAS-V4D Konzept Mercedes EQS", 238_400)
ic_rechnung_rsg("RSG_IC_Rechnung_2020_04.docx", "2020", 4,
    "COVID-bedingte Reduktion - ICP-3 Wartung; ECU-900 Stellantis Support", 198_200)
ic_rechnung_rsg("RSG_IC_Rechnung_2020_05.docx", "2020", 5,
    "Kurzarbeit Validation-Team (60 %); ADAS-V4D Anforderungs-Workshops", 178_500)
ic_rechnung_rsg("RSG_IC_Rechnung_2020_06.docx", "2020", 6,
    "Wiederhochfahren - ADAS-V4D Konzept G1-Gate; BMS-12 Implementierung Sprint 1-2", 215_300)
ic_rechnung_rsg("RSG_IC_Rechnung_2020_08.docx", "2020", 8,
    "Sommer-Reduktion (Urlaub); ICP-3 6.0 Hardening Releases; OTA-Vorbereitung", 195_400)
ic_rechnung_rsg("RSG_IC_Rechnung_2020_09_WIP.docx", "2020", 9,
    "ASPICE Level 3 Vorbereitung; BMS-12 Release 2.5 (ID.4 SOP)", 242_100, status="WIP")
ic_rechnung_rsg("RSG_IC_Rechnung_2020_10.docx", "2020", 10,
    "ADAS-V4D G2-Gate-Abschluss; Continental-Hardware-Integration", 248_600)
ic_rechnung_rsg("RSG_IC_Rechnung_2020_11.docx", "2020", 11,
    "BMS-12 ML-Algorithmus Cell-Balancing; OEM-Audit-Vorbereitung VW", 252_800)
ic_rechnung_rsg("RSG_IC_Rechnung_2020_12.docx", "2020", 12,
    "Jahresabschluss-Aktivitaeten; Recruiting-Drive (12 Senior-Engineers Q1/21 geplant)", 235_700)

# 2021 (12 rechnungen)
ic_rechnung_rsg("RSG_IC_Rechnung_2021_01.docx", "2021", 1,
    "ADAS-V4D PRJ-2021-002 Kickoff; Onboarding 12 Neueinstellungen", 261_400)
ic_rechnung_rsg("RSG_IC_Rechnung_2021_02.docx", "2021", 2,
    "ECU-900 Stellantis SOP-Vorbereitung; ICP-3 Release 6.1 BMW iX5", 268_900)
ic_rechnung_rsg("RSG_IC_Rechnung_2021_03.docx", "2021", 3,
    "ASPICE Level 3 SUP.8-Etablierung; BMS-12 Re-Architektur ID.7", 275_200)
ic_rechnung_rsg("RSG_IC_Rechnung_2021_04.docx", "2021", 4,
    "ADAS-V4D Sprint 5-7 PRJ-2021-002; Continental ARS510 Integration", 282_500)
ic_rechnung_rsg("RSG_IC_Rechnung_2021_05_ENTWURF.docx", "2021", 5,
    "BMS-12 ASPICE Level 3 Audit; ICP-3 6.2 Mercedes EQS MBUX", 285_400, status="ENTWURF")
ic_rechnung_rsg("RSG_IC_Rechnung_2021_06.docx", "2021", 6,
    "ADAS-V4D PRJ-2021-002 Sprint 8-10; HiL-Validierung Vorbereitung", 290_100)
ic_rechnung_rsg("RSG_IC_Rechnung_2021_07.docx", "2021", 7,
    "Sommermonat - Urlaubsphase; BMS-12 Wartungssprints", 252_700)
ic_rechnung_rsg("RSG_IC_Rechnung_2021_08.docx", "2021", 8,
    "ICP-3 6.3 Release Hardening; ECU-900 EMV-Optimierung VW MEB+", 268_900)
ic_rechnung_rsg("RSG_IC_Rechnung_2021_09.docx", "2021", 9,
    "ASPICE Level 3 intacs Assessment (KUGLER MAAG CIE) - bestanden ohne Major", 312_500)
ic_rechnung_rsg("RSG_IC_Rechnung_2021_10.docx", "2021", 10,
    "ADAS-V4D PRJ-2021-002 Toolchain-Migration CANoe 13->14; LightCtrl-7 Audi-Pilot", 298_700)
ic_rechnung_rsg("RSG_IC_Rechnung_2021_11_20230915.docx", "2021", 11,
    "BMS-12 Hyundai E-GMP Kickoff; ICP-3 6.4 Android Auto Wireless", 305_400)
ic_rechnung_rsg("RSG_IC_Rechnung_2021_12.docx", "2021", 12,
    "Jahresabschluss-Aktivitaeten; ADAS-V4D Sprint 18-20 PRJ-2021-002", 287_800)

# 2022 (11 rechnungen, no May)
ic_rechnung_rsg("RSG_IC_Rechnung_2022_01.docx", "2022", 1,
    "Neuer GF Kessler Onboarding; ADAS-V4D PRJ-2021-002 Sprint 21-22", 295_200)
ic_rechnung_rsg("RSG_IC_Rechnung_2022_02.docx", "2022", 2,
    "BMS-12 VW ID.7 SOP-Vorbereitung; ECU-900 Stellantis STLA Medium Konzept", 302_800)
ic_rechnung_rsg("RSG_IC_Rechnung_2022_03.docx", "2022", 3,
    "ADAS-V4D HiL-Validierung Start (Mercedes Sindelfingen); Continental-Hardware verspaetet", 315_700)
ic_rechnung_rsg("RSG_IC_Rechnung_2022_04.docx", "2022", 4,
    "ASPICE-Wartung Levels 2-3; ICP-3 7.0 BMW G70-Konzept", 321_400)
ic_rechnung_rsg("RSG_IC_Rechnung_2022_06.docx", "2022", 6,
    "ADAS-V4D Sprint 28-30; Cyber-Security ISO 21434 Assessment TUEV SUED", 332_700)
ic_rechnung_rsg("RSG_IC_Rechnung_2022_07.docx", "2022", 7,
    "BMS-12 ML-Optimierung TensorFlow Lite Micro; ECU-900 STLA Bring-up", 318_600)
ic_rechnung_rsg("RSG_IC_Rechnung_2022_08.docx", "2022", 8,
    "Urlaubsmonat; ADAS-V4D Calibration Software Tuning (EMV-Robustheit)", 285_300)
ic_rechnung_rsg("RSG_IC_Rechnung_2022_09.docx", "2022", 9,
    "BMS-12 ID.7 SOP erfolgreich; ICP-3 7.1 Mercedes Hyperscreen", 342_500)
ic_rechnung_rsg("RSG_IC_Rechnung_2022_10.docx", "2022", 10,
    "ADAS-V4D PRJ-2021-002 Final Acceptance Vorbereitung; ECU-900 STLA Pilot", 358_400)
ic_rechnung_rsg("RSG_IC_Rechnung_2022_11.docx", "2022", 11,
    "BMS-12 Hyundai E-GMP SOP-Vorbereitung; ICP-3 OTA-Welle BMW iX5", 348_900)
ic_rechnung_rsg("RSG_IC_Rechnung_2022_12.docx", "2022", 12,
    "Jahresabschluss; ADAS-V4D FAT Vorbereitung Mercedes EQS Februar 2023", 332_400)


# ============================================================================
# 7) RSG_to_RCZ_IC Rechnungen 2021-2023 (36x) - RSG -> RCZ Brno cross-charge
# ============================================================================
def ic_rsg_to_rcz(fname, jahr, monat, betrag_eur, leistung, status=None):
    rn = f"RSG-RCZ-{jahr}{monat:02d}-001"
    mon_str = ["", "Januar","Februar","Maerz","April","Mai","Juni","Juli","August",
               "September","Oktober","November","Dezember"][monat]
    rd = f"{(monat*2) % 28 + 1}. {mon_str} {jahr}"
    write_doc(f"{BASE}/{fname}", H_RSG,
        f"Intercompany Rechnung {rn} - RSG an RCZ Brno",
        subtitle=f"Leistungszeitraum {mon_str} {jahr} - Softwarespezifikationen / Embedded-Engineering fuer Steckverbinder-Produktion",
        draft=(status=="DRAFT"),
        sections=[
            ("Rechnungsdaten",
             f"Rechnungs-Nr.: {rn}\n"
             f"Rechnungsdatum: {rd}\n"
             f"Leistungszeitraum: 01. - {28 if monat==2 else 30}. {mon_str} {jahr}\n"
             f"Zahlungsziel: 45 Tage netto (Konzern-IC-Vereinbarung CEE 2020)\n"
             f"Status: {status or 'FINAL'}"),
            ("Rechnungssteller (Leistungserbringer)",
             "Brennhagen Software GmbH\n"
             "Lyonel-Feininger-Strasse 28, 80807 Muenchen, Deutschland\n"
             "HRB 319872, Amtsgericht Muenchen\n"
             "USt-IdNr. DE 245 678 901\n"
             "Bankverbindung: Stadtsparkasse Muenchen, IBAN DE89 7015 0000 0123 4567 89"),
            ("Rechnungsempfaenger (Leistungsempfaenger)",
             "Brennhagen CZ s.r.o.\n"
             "Tuzemska 14, 612 00 Brno, Tschechische Republik\n"
             "Handelsregister C 87654, KS Brno\n"
             "USt-IdNr. CZ 28765432\n"
             "Vertreten durch: Petr Novak (Werkleiter / jednatel)"),
            ("Leistungsbeschreibung",
             f"Im Berichtsmonat {mon_str} {jahr} hat die Brennhagen Software GmbH (RSG) im Rahmen der "
             f"konzerninternen Cross-Charge-Vereinbarung vom 01.07.2020 (REA-IC-CEE-2020) folgende "
             f"Embedded-Software-Engineering-Leistungen fuer die Tochtergesellschaft Brennhagen CZ s.r.o. "
             f"(Brno) erbracht:\n\n"
             f"{leistung}\n\n"
             f"Die Leistungen umfassen insbesondere die softwareseitige Unterstuetzung der "
             f"Produktionslinien fuer Hochstrom-Steckverbinder (RCZ-Hauptprodukte: HSC-200 fuer EV-"
             f"Ladestationen, MCS-450 fuer Industrieanwendungen). Verrechnungspreis basiert auf "
             f"Cost-Plus 7,5 % gemaess Transfer-Pricing-Vereinbarung KPMG-validiert 2019."),
            ("Rechnungsposten",
             [["Pos.", "Leistung", "Stundensatz", "Betrag EUR"],
              ["1", "Embedded-SW Anpassung Produktionslinien", "125 EUR/h", f"{betrag_eur*0.50:,.0f}".replace(",", ".")],
              ["2", "Quality-Engineering / Pruefsoftware", "135 EUR/h", f"{betrag_eur*0.25:,.0f}".replace(",", ".")],
              ["3", "Projekt-Support / Vor-Ort-Einsaetze Brno", "150 EUR/h", f"{betrag_eur*0.15:,.0f}".replace(",", ".")],
              ["4", "Reise- und Nebenkosten (Pauschale)", "—", f"{betrag_eur*0.10:,.0f}".replace(",", ".")],
              ["", "Netto-Summe", "", f"{betrag_eur:,.0f}".replace(",", ".")],
              ["", "USt (gem. § 13b UStG entfaellt - Reverse Charge B2B EU)", "", "0,00"],
              ["", "Rechnungsbetrag gesamt", "", f"{betrag_eur:,.0f}".replace(",", ".")]]),
            ("Zahlungs- und Buchungshinweise",
             f"Der Rechnungsbetrag i. H. v. {betrag_eur:,.0f} EUR ".replace(",", ".") +
             f"ist bis 45 Tage nach Rechnungsdatum auf das oben angegebene Konto zu zahlen. Die "
             f"Verrechnung erfolgt regelmaessig im monatlichen Konzern-Settlement-Run der Group "
             f"Treasury (M. Pflanzer) jeweils zum 25. des Folgemonats. Bei Verrechnung im "
             f"Konzern-Cash-Pool wird keine separate Ueberweisung ausgeloest."),
            ("Anlagen",
             "Anlage 1: Detaillierter Stundennachweis je Mitarbeiter und Projekt (Excel)\n"
             "Anlage 2: Reisekostenabrechnungen mit Belegen (PDF)\n"
             "Anlage 3: SAP-Auswertung Kostenstellen RCZ-Cross-Charge"),
        ])


# 2021 (12)
rcz_leist = {
    1: "Quality-Engineering Software-Update HSC-200; Vor-Ort-Einsatz Brno Linie 3",
    2: "MCS-450 Pruefsoftware-Anpassung; Engineering-Support Werkzeugumbau",
    3: "Linienanlauf HSC-200-XL Variante; SPS-Programmierung Linie 5",
    4: "Quality-Engineering Reaktion auf 8D Festo-Sensor; Pruefsoftware-Patch",
    5: "MCS-450 Funktionserweiterung 200A-Variante; CSV/MES-Integration",
    6: "Engineering-Support Sommer-Umbau; HSC-200 OEE-Optimierung",
    7: "Urlaubsmonat - reduzierter Support; Pruefsoftware-Wartung",
    8: "MCS-450 Audit-Vorbereitung VW Wolfsburg (Audit am 12.09.)",
    9: "VW-Audit erfolgreich; Folgemassnahmen MCS-450; Linie-6-Bring-up HSC-200",
    10: "MCS-450 SOP-Vorbereitung Stellantis Cassino; Pruefsoftware-Validierung",
    11: "HSC-200-XL SOP Mercedes EQS (Hochstromladung); Vor-Ort-Bring-up",
    12: "Jahresabschluss-Support; Inventur-Pruefsoftware; Plan-2022 Kickoff",
}
status_2021 = {5: "rev_SRichter", 7: "DRAFT"}
files_2021 = {
    1: "RSG_to_RCZ_IC_2021_01.docx",
    2: "RSG_to_RCZ_IC_2021_02.docx",
    3: "RSG_to_RCZ_IC_2021_03.docx",
    4: "RSG_to_RCZ_IC_2021_04.docx",
    5: "RSG_to_RCZ_IC_2021_05_rev_SRichter.docx",
    6: "RSG_to_RCZ_IC_2021_06.docx",
    7: "RSG_to_RCZ_IC_2021_07_DRAFT.docx",
    8: "RSG_to_RCZ_IC_2021_08.docx",
    9: "RSG_to_RCZ_IC_2021_09.docx",
    10: "RSG_to_RCZ_IC_2021_10.docx",
    11: "RSG_to_RCZ_IC_2021_11.docx",
    12: "RSG_to_RCZ_IC_2021_12.docx",
}
betraege_2021 = [78_200, 72_400, 81_500, 79_300, 84_100, 88_900, 65_400, 91_200, 95_800, 102_400, 108_700, 92_300]
for m in range(1, 13):
    st = "DRAFT" if m == 7 else None
    ic_rsg_to_rcz(files_2021[m], "2021", m, betraege_2021[m-1], rcz_leist[m], status=st)

# 2022 (12)
rcz_leist_22 = {
    1: "MCS-450 Roll-out Stellantis Mirafiori - Vor-Ort-Bring-up Brno -> Italien",
    2: "HSC-200-XL Mercedes EQS Anlaufunterstuetzung; MES-Integration",
    3: "Pruefsoftware-Erweiterung Hochstrom-Pruefplatz (1.500 A) - Linie 7",
    4: "Audit-Vorbereitung BMW Werk Spartanburg (US); Konformitaetsnachweise",
    5: "BMW-Audit erfolgreich; Folgemassnahmen; Software-Verbesserung MES-Anbindung",
    6: "MCS-450 Erweiterung 350A-Variante - Konzept und Pruefsoftware-Erstellung",
    7: "Sommerphase - HSC-200 Optimierung Linie 4 (Cycle Time -8 %)",
    8: "Urlaubsmonat - Basis-Support; Sicherheits-Audits Pruefstaende",
    9: "MCS-450 SOP Hyundai Czech Republic - Anlauf-Support Linie 8",
    10: "MCS-450 350A SOP Mercedes Truck (Daimler Wörth)",
    11: "Wartungspauschale Pruefsoftware-Suite; Cybersecurity-Update OT-Netz",
    12: "Jahresabschluss; Inventur-Pruefsoftware; PCN-Migration auf Win 11",
}
files_2022 = {m: f"RSG_to_RCZ_IC_2022_{m:02d}.docx" for m in range(1, 13)}
betraege_2022 = [110_400, 115_700, 122_300, 118_900, 125_400, 119_800, 88_700, 78_500, 132_400, 138_900, 142_700, 128_500]
for m in range(1, 13):
    ic_rsg_to_rcz(files_2022[m], "2022", m, betraege_2022[m-1], rcz_leist_22[m])

# 2023 (11 - no Jan; Nov has FINAL_v2 suffix)
rcz_leist_23 = {
    2: "MCS-450 Erweiterung Lieferprogramm BYD - Pruefsoftware Anpassung",
    3: "HSC-200-XL OEE-Programm; CI/CD-Pipeline-Erweiterung fuer Pruefsoftware",
    4: "Audit Q1 OEM-VW Stiftungsbruecke; Compliance-Update REACH/RoHS",
    5: "MCS-450 Re-Design 1.000A-Variante - Pruefsoftware-Konzept",
    6: "HSC-200-XL Pilot Tesla Berlin - Spezialvalidierung",
    7: "Sommermonate - Wartungsprogramm Pruefsoftware-Suite v4.2",
    8: "Linie 9-Bring-up - neue Mehrkomponenten-Steckverbinder fuer Wasserstoff-Anwendungen",
    9: "MCS-450 SOP Stellantis Tychy (PL); Cross-Charge zwischen Werken (CZ <-> PL)",
    10: "ASPICE-Audit-Vorbereitung RCZ - intacs-Assessor (Pruefsoftware-Aspekte)",
    11: "ASPICE-Audit erfolgreich; Final-v2 nach Korrektur Cross-Charge-Verrechnung",
    12: "Jahresabschluss; Plan-2024 Sprint; HSC-200-Generationenwechsel Konzept",
}
files_2023 = {
    2: "RSG_to_RCZ_IC_2023_02.docx",
    3: "RSG_to_RCZ_IC_2023_03.docx",
    4: "RSG_to_RCZ_IC_2023_04.docx",
    5: "RSG_to_RCZ_IC_2023_05.docx",
    6: "RSG_to_RCZ_IC_2023_06.docx",
    7: "RSG_to_RCZ_IC_2023_07.docx",
    8: "RSG_to_RCZ_IC_2023_08.docx",
    9: "RSG_to_RCZ_IC_2023_09.docx",
    10: "RSG_to_RCZ_IC_2023_10.docx",
    11: "RSG_to_RCZ_IC_2023_11_FINAL_v2.docx",
    12: "RSG_to_RCZ_IC_2023_12.docx",
}
betraege_2023 = {2: 142_300, 3: 148_700, 4: 152_400, 5: 158_900, 6: 165_400, 7: 118_700,
                  8: 122_400, 9: 178_900, 10: 185_400, 11: 192_800, 12: 175_600}
for m in [2,3,4,5,6,7,8,9,10,11,12]:
    ic_rsg_to_rcz(files_2023[m], "2023", m, betraege_2023[m], rcz_leist_23[m])


# ============================================================================
# 8) RSG Mietvertrag Betriebsgelaende 2020
# ============================================================================
write_doc(f"{BASE}/RSG_Mietvertrag_Betriebsgelaende_2020.docx", H_RSG,
    "Mietvertrag - Betriebsgelaende Lyonel-Feininger-Strasse 28, Muenchen",
    subtitle="Geschaeftsraummietvertrag zwischen ABG Allianz Immobilien GmbH und Brennhagen Software GmbH",
    sections=[
        ("Vertragsparteien",
         "Vermieterin: ABG Allianz Immobilien GmbH, Koeniginstrasse 28, 80802 Muenchen, eingetragen "
         "im Handelsregister des Amtsgerichts Muenchen unter HRB 142587, vertreten durch die Geschaefts"
         "fuehrer Martin Schreiner und Dr. Eva Lindner (nachfolgend 'Vermieterin').\n\n"
         "Mieterin: Brennhagen Software GmbH, Lyonel-Feininger-Strasse 28, 80807 Muenchen (HRB 319872, "
         "Amtsgericht Muenchen), vertreten durch den Geschaeftsfuehrer Dr. Klaus Kessler "
         "(nachfolgend 'Mieterin')."),
        ("Mietobjekt",
         "Vermietet werden die gewerblichen Geschaeftsraeume im Buerogebaeude Lyonel-Feininger-Strasse 28, "
         "80807 Muenchen, bestehend aus:\n\n"
         "- 4. Obergeschoss (gesamtes Stockwerk), ca. 1.850 m² Buerofflaeche\n"
         "- 5. Obergeschoss (gesamtes Stockwerk), ca. 1.850 m² Buerofflaeche\n"
         "- 6. Obergeschoss (Teilflaeche Nord-Ost), ca. 920 m² Labor-/HiL-Flaeche\n"
         "- Tiefgaragenstellplaetze Nr. T-141 bis T-225 (insgesamt 85 Stellplaetze)\n"
         "- 12 E-Ladestationen (Wallboxen 22 kW) - Investition Mieterin\n\n"
         "Gesamtmietflaeche: 4.620 m². Mietzweck: Buero-, Software-Entwicklungs- und HiL-Laborraeume."),
        ("Vertragsregelungen",
         ("clauses", [
             ("§ 1 Mietzeit", [
                 "Das Mietverhaeltnis beginnt am 01.07.2020 und wird auf bestimmte Zeit von zehn (10) Jahren "
                 "geschlossen. Es endet ohne Kuendigung am 30.06.2030.",
                 "Die Mieterin hat das Recht, das Mietverhaeltnis zweimal um jeweils fuenf (5) Jahre zu "
                 "verlaengern (Option). Die Option ist spaetestens 12 Monate vor Mietende schriftlich auszuueben.",
             ]),
             ("§ 2 Mietzins / Nebenkosten", [
                 "Der monatliche Grundmietzins betraegt zum Mietbeginn 95.700 EUR netto (entspricht ca. "
                 "20,71 EUR/m² Buerofflaeche bzw. 24,80 EUR/m² Laborflaeche). Hinzu kommen Nebenkosten "
                 "(Heizung, Strom, Wasser, Reinigung, Hausmeisterdienst) i. H. v. derzeit 4,80 EUR/m² monatlich, "
                 "abgerechnet ueber jaehrliche Nebenkostenabrechnung.",
                 "Stellplaetze: 95 EUR netto/Monat pro Tiefgaragenplatz (85 Plaetze = 8.075 EUR).",
                 "Indexanpassung: Der Mietzins wird jaehrlich zum 01.01. an den Verbraucherpreisindex (VPI) "
                 "des Statistischen Bundesamts angepasst (Vollindexierung 100 % VPI ab 5 % kumulierter "
                 "Indexsteigerung; Basis VPI Juni 2020 = 106,1 Punkte).",
                 "Die Umsatzsteuer (derzeit 19 %) wird gesondert ausgewiesen.",
             ]),
             ("§ 3 Mietsicherheit", [
                 "Die Mieterin stellt eine Mietbuergschaft der Brennhagen Elektronik AG (Konzernmutter, HRB "
                 "726451, Stuttgart) i. H. v. drei (3) Brutto-Monatsmieten (Stand Mietbeginn: 372.260 EUR) "
                 "zur Verfuegung.",
                 "Die Buergschaft ist unbefristet, selbstschuldnerisch und auf erstes Anfordern.",
             ]),
             ("§ 4 Uebergabe / Zustand", [
                 "Die Mietraeume werden bezugsfertig (Ausbau-Standard 'A') gemaess Anlage 3 zum Vertrag "
                 "(Raumbuch) uebergeben. Der Mietbeginn ist verbunden mit einem Uebergabe-/Abnahmeprotokoll.",
                 "Mieterausbauten (z. B. HiL-Laborstaende, Server-Racks, Kantine im 4. OG) erfolgen auf "
                 "Kosten der Mieterin nach vorheriger Genehmigung durch die Vermieterin.",
             ]),
             ("§ 5 Instandhaltung / Schoenheitsreparaturen", [
                 "Die Vermieterin hat das Gebaeude in gebrauchsfaehigem Zustand zu erhalten (Dach/Fach). "
                 "Die Mieterin uebernimmt Schoenheitsreparaturen innerhalb der angemieteten Flaechen "
                 "(Anstrich, Bodenbelaege, Bedarf nach Verschleiss).",
                 "Bei Vertragsende ist die Mieterin verpflichtet, die Raeume im uebergabefaehigen Zustand "
                 "(neutraler Weisanstrich, gereinigt) zurueckzugeben. Rueckbau der Mieterausbauten "
                 "kann von der Vermieterin verlangt werden.",
             ]),
             ("§ 6 Haftung / Versicherung", [
                 "Die Vermieterin haelt eine Gebaeudeversicherung (Wohngebaeude+Glasbruch+Elementar) bei "
                 "der Allianz Sachversicherungs-AG vor.",
                 "Die Mieterin haelt eine Betriebshaftpflicht- und Inhaltsversicherung (Buero+Labor) vor, "
                 "Mindestversicherungssumme 5 Mio. EUR pauschal.",
             ]),
             ("§ 7 Untervermietung / Konzern", [
                 "Die Untervermietung an dritte Unternehmen bedarf der schriftlichen Genehmigung der "
                 "Vermieterin. Die Mitnutzung durch Konzerngesellschaften der Brennhagen Elektronik AG "
                 "(REA, REG, RHO) ist ohne Genehmigung zulaessig.",
                 "Bei einem Kontrollwechsel der Mieterin (Verlust der 100%-Konzernzugehoerigkeit zur REA) "
                 "hat die Vermieterin ein Sonderkuendigungsrecht mit 12-monatiger Frist.",
             ]),
             ("§ 8 Schlussbestimmungen", [
                 "Aenderungen / Ergaenzungen beduerfen der Schriftform; ebenso die Aufhebung dieses "
                 "Schriftformerfordernisses. Es gilt deutsches Recht. Gerichtsstand ist Muenchen.",
             ]),
         ])),
        ("Unterschriften",
         signatures("Martin Schreiner", "Geschaeftsfuehrer", "ABG Allianz Immobilien GmbH",
                    "Dr. Klaus Kessler", "Geschaeftsfuehrer", "Brennhagen Software GmbH",
                    place=PLACE, date_str_="18. Juni 2020")),
    ])


# ============================================================================
# 9) RSG Steuerbescheide (4x: 2020, 2021, 2022, 2023)
# ============================================================================
def steuerbescheid(fname, jahr, kst_eur, gewst_eur, gewinn_eur, status_text=""):
    write_doc(f"{BASE}/{fname}", H_RSG,
        f"Koerperschaftsteuer-/Gewerbesteuerbescheid {jahr} - Brennhagen Software GmbH",
        subtitle=f"Bescheid des Finanzamts Muenchen Abt. Koerperschaften vom {15+int(jahr[-1])}. Maerz {int(jahr)+1}",
        sections=[
            ("Bescheid-Identifikation",
             f"Finanzamt: Muenchen, Abteilung Koerperschaftsteuer\n"
             f"Aktenzeichen: 144/123/45678 (Steuer-Nr. RSG)\n"
             f"Bescheid-Datum: {15+int(jahr[-1])}. Maerz {int(jahr)+1}\n"
             f"Steuerpflichtige: Brennhagen Software GmbH, Lyonel-Feininger-Strasse 28, 80807 Muenchen\n"
             f"HRB 319872, Amtsgericht Muenchen\n"
             f"Veranlagungszeitraum: 01.01.{jahr} bis 31.12.{jahr}\n"
             f"Status: {status_text or 'rechtskraeftig (kein Einspruch)'}"),
            ("Festsetzung Koerperschaftsteuer",
             [["Position", "Betrag (EUR)"],
              ["Steuerlicher Gewinn (zu versteuerndes Einkommen)", f"{gewinn_eur:,.0f}".replace(",", ".")],
              ["Koerperschaftsteuer 15 %", f"{kst_eur:,.0f}".replace(",", ".")],
              ["Solidaritaetszuschlag 5,5 % auf KSt", f"{kst_eur*0.055:,.0f}".replace(",", ".")],
              ["Summe KSt + SolZ", f"{kst_eur*1.055:,.0f}".replace(",", ".")]]),
            ("Festsetzung Gewerbesteuer",
             [["Position", "Betrag (EUR)"],
              ["Gewerbeertrag (vor Hinzurechnungen/Kuerzungen)", f"{gewinn_eur:,.0f}".replace(",", ".")],
              ["Hinzurechnungen § 8 GewStG (geschaetzt)", f"{gewinn_eur*0.05:,.0f}".replace(",", ".")],
              ["Gewerbeertrag", f"{gewinn_eur*1.05:,.0f}".replace(",", ".")],
              ["Steuermesszahl 3,5 %", f"{gewinn_eur*1.05*0.035:,.0f}".replace(",", ".")],
              ["Hebesatz Muenchen 490 %", f"{gewinn_eur*1.05*0.035*4.90:,.0f}".replace(",", ".")],
              ["= Gewerbesteuer", f"{gewst_eur:,.0f}".replace(",", ".")]]),
            ("Erlaeuterungen",
             f"Der Bescheid basiert auf der eingereichten KSt-/GewSt-Erklaerung {jahr} der Brennhagen Software "
             f"GmbH vom {25+int(jahr[-1])}. Mai {int(jahr)+1} (eingegangen ueber ELSTER). Der steuerliche "
             f"Gewinn wurde aus dem handelsrechtlichen Jahresueberschuss laut testiertem Jahresabschluss "
             f"(KPMG AG WPG, Lead Partner Dr. Maximilian Brand) durch ausserbilanzielle Hinzurechnungen "
             f"(nicht abzugsfaehige Betriebsausgaben § 4 Abs. 5 EStG) und Kuerzungen (Investitionsabzugs"
             f"betrag § 7g EStG) ermittelt.\n\n"
             f"Die Veranlagung erfolgt unter dem Vorbehalt der Nachpruefung gemaess § 164 AO. Eine "
             f"Aussenpruefung (Betriebspruefung) ist fuer das Veranlagungsjahr noch nicht angekuendigt."),
            ("Zahlungs-/Erstattungshinweise",
             f"Die Steuerschuld {jahr} (KSt + SolZ + GewSt) ist binnen einem Monat nach Bekanntgabe des "
             f"Bescheids faellig. Bereits geleistete Vorauszahlungen werden angerechnet. Etwaige "
             f"Vorauszahlungen fuer das Folgejahr werden gesondert festgesetzt."),
            ("Rechtsbehelfsbelehrung",
             "Gegen diesen Bescheid kann innerhalb eines Monats nach Bekanntgabe Einspruch eingelegt werden. "
             "Der Einspruch ist beim Finanzamt Muenchen Abt. Koerperschaften, Deroystrasse 18, 80335 "
             "Muenchen, schriftlich oder zur Niederschrift einzulegen oder elektronisch ueber ELSTER "
             "zu uebermitteln."),
            ("Anlagen",
             "Anlage 1: Detaillierte Steuerberechnung (KSt-Anlage GK)\n"
             "Anlage 2: Gewerbesteuer-Aufteilungsbescheid (nur Muenchen, keine Zerlegung)\n"
             "Anlage 3: Hinweise zur Vorauszahlung Folgejahr"),
        ])


steuerbescheid("RSG_Steuerbescheid_2020.docx", "2020", 1_120_000, 1_810_000, 7_466_667)
steuerbescheid("RSG_Steuerbescheid_2021.docx", "2021", 1_245_000, 2_012_000, 8_300_000)
steuerbescheid("RSG_Steuerbescheid_2022.docx", "2022", 1_380_000, 2_230_000, 9_200_000)
steuerbescheid("RSG_Steuerbescheid_KSt_2023.docx", "2023", 1_532_000, 2_476_000, 10_213_333,
               status_text="vorbehaltlich der Endveranlagung 2023")

# RCZ misplaced - one Steuerbescheid for RCZ
write_doc(f"{BASE}/RCZ_Steuerbescheid_KSt_2023.docx", H_RCZ,
    "Daňové přiznání 2023 / Steuerbescheid 2023 - Brennhagen CZ s.r.o.",
    subtitle="Bescheid des Finanzamts Brno (Financni urad pro Jihomoravsky kraj) - VZ 2023",
    sections=[
        ("Bescheid-Identifikation",
         "Finanzamt: Financni urad pro Jihomoravsky kraj, Uzemni pracoviste Brno I\n"
         "Aktenzeichen: DIC CZ28765432\n"
         "Bescheid-Datum: 18. Maerz 2024\n"
         "Steuerpflichtige: Brennhagen CZ s.r.o., Tuzemska 14, 612 00 Brno\n"
         "Handelsregister: C 87654, KS Brno\n"
         "Veranlagungszeitraum: 01.01.2023 bis 31.12.2023\n"
         "Status: vorbehaltlich Endveranlagung"),
        ("Festsetzung Koerperschaftsteuer Tschechien",
         [["Position", "Betrag (CZK)", "Betrag (EUR-Aequiv.)"],
          ["Steuerlicher Gewinn (zaklad dane)", "215.400.000", "8.616.000"],
          ["KSt-Satz Tschechien 19 % (2023)", "—", "—"],
          ["Koerperschaftsteuer (dan z prijmu)", "40.926.000", "1.637.040"]]),
        ("Besonderheiten / Hinweise",
         "Die Brennhagen CZ s.r.o. unterliegt der tschechischen Koerperschaftsteuer (zakon c. 586/1992 Sb.) "
         "mit Satz 19 % fuer 2023. Ab 2024 erhoeht sich der Satz auf 21 % gemaess Steuerreform-Paket "
         "der Regierung Fiala (ucinnost od 01.01.2024). Die Gewinne unterliegen ferner einer Dividendensteuer "
         "von 15 % bei Ausschuettung an die deutsche Mutter (Reduktion auf 5 % gemaess DBA Deutschland-"
         "Tschechien, falls Beteiligungsschwelle und Haltefrist erfuellt - hier 100 %-Beteiligung und "
         "Haltedauer > 12 Monate).\n\n"
         "Die Verrechnungspreise mit verbundenen Unternehmen (RSG Muenchen, REA Stuttgart) wurden im "
         "Rahmen der Transfer-Pricing-Akte (KPMG Local File CZ 2023) dokumentiert. Eine TP-Aussenpruefung "
         "ist fuer 2024-2025 nicht angekuendigt."),
        ("Zahlungshinweise",
         "Die festgesetzte KSt fuer 2023 (40.926.000 CZK) ist binnen 30 Tagen nach Bescheidbekanntgabe "
         "an das zustaendige Finanzamt zu zahlen. Bereits geleistete Vorauszahlungen werden angerechnet. "
         "Die Vorauszahlungen fuer 2024 werden auf 9 Mio. CZK quartalsweise festgesetzt."),
        ("Rechtsmittelbelehrung",
         "Gegen diesen Bescheid kann innerhalb 30 Tagen Beschwerde (odvolani) eingelegt werden. "
         "Beschwerdeinstanz: Odvolaci financni reditelstvi, Masarykova 31, 602 00 Brno."),
    ])


# ============================================================================
# 10) RSG Versicherungsnachweis 2023
# ============================================================================
write_doc(f"{BASE}/RSG_Versicherungsnachweis_2023.docx", H_RSG,
    "Versicherungsnachweis 2023 - Brennhagen Software GmbH",
    subtitle="Uebersicht aller laufenden Versicherungsvertraege RSG zum 31.12.2023",
    sections=[
        ("Allgemeine Hinweise",
         "Die Versicherungsstrategie der Brennhagen Software GmbH ist eingebettet in die Konzern-Versicherungs"
         "richtlinie der Brennhagen Elektronik AG (REA-VRL-2022). Die wesentlichen Konzernpolicen (D&O, "
         "Cyber, Produkthaftpflicht, Sach-/Betriebsunterbrechung) werden zentral von der Group Treasury "
         "(Markus Pflanzer) ueber die Versicherungsmaklerin Marsh GmbH (Frankfurt) verhandelt. Lokale "
         "Policen (KFZ-Flotte, Gebaeudehaftpflicht, BG-Beitraege) liegen in Verantwortung der RSG-"
         "Geschaeftsfuehrung (Dr. Klaus Kessler)."),
        ("Versicherungs-Portfolio RSG 2023",
         [["Sparte", "Versicherer", "Police-Nr.", "VS Mio. EUR", "Praemie p.a."],
          ["D&O (Konzern)", "Allianz Global Corporate & Specialty SE", "DO-REA-2022-001", "50,0 (Konzern)", "anteilig 32 TEUR"],
          ["Cyber (Konzern)", "AXA XL", "CY-REA-2023-001", "25,0", "anteilig 28 TEUR"],
          ["Produkthaftpflicht", "AIG Europe S.A.", "PHV-RSG-2021-007", "20,0", "85 TEUR"],
          ["Betriebshaftpflicht", "AIG Europe S.A.", "BHV-RSG-2021-008", "10,0", "42 TEUR"],
          ["Sach- / BU-Versicherung", "Allianz Sach-Versicherungs-AG", "SACH-RSG-2020-003", "30,0", "125 TEUR"],
          ["Elektronik-Versicherung", "HDI Global SE", "EL-RSG-2022-014", "8,0 (Inhalt)", "38 TEUR"],
          ["KFZ-Flotte (24 Fahrzeuge)", "HUK-COBURG", "FLOTTE-RSG-2019", "—", "62 TEUR"],
          ["Rechtsschutz (gewerblich)", "ARAG SE", "RS-RSG-2018-002", "0,5 je Fall", "12 TEUR"],
          ["Krankenzusatz (Gruppentarif)", "Allianz Private KV-AG", "GKV-RSG-2020", "—", "180 TEUR"]]),
        ("D&O-Police - Konzernabdeckung",
         "Die D&O-Versicherung wird von der Konzernmutter Brennhagen Elektronik AG fuer alle Konzerngesellschaften "
         "abgeschlossen (Versicherer: Allianz Global Corporate & Specialty SE, Versicherungssumme 50 Mio. EUR "
         "pauschal, Selbstbehalt 1 % der VS = 500 TEUR je Schadensfall fuer GF und Aufsichtsorgan, "
         "ausgenommen Insolvenzanfechtung). Erstreckungsklausel auf Subsidiary-Boards (also auch GF RSG "
         "Dr. Kessler und Vorsitzende ggf. spaeterer Beiraete). Anteiliger Praemienanteil RSG ca. 32 TEUR."),
        ("Cyber-Versicherung",
         "Konzernpolice gegen Cyber-Risiken (Ransomware, Datenverlust, Betriebsunterbrechung infolge "
         "Cyber-Vorfall, Bussgelder DSGVO bis zu 5 Mio. EUR sub-limit). RSG als ADAS-Software-Entwickler "
         "ist besonderem Cyber-Risiko ausgesetzt (Risiko-Score Concierge Cyber). Police umfasst auch "
         "Incident-Response-Services (Mandiant / Kroll). Schwellenwerte fuer Meldepflicht: 50 TEUR Schaden / "
         "1.000 betroffene Datensaetze."),
        ("Produkt- und Betriebshaftpflicht",
         "Beide Policen mit AIG Europe S.A. abgeschlossen, Vermittlung durch Marsh. Produkthaftpflicht "
         "fokussiert auf Software-Defekte mit Personen-/Sachschadenfolge in Fahrzeugen (typisch: ADAS-"
         "Fehlfunktion mit Crash-Folge). Geographischer Geltungsbereich: weltweit ausser USA/CAN (separate "
         "Police fuer Auslieferungen in Nordamerika ueber AIG New York). Selbstbehalt 100 TEUR je Fall."),
        ("Sach-/BU-Versicherung",
         "Allianz-Police fuer die Mietraeume Lyonel-Feininger-Strasse 28 (4./5./6. OG): Inventar (Server, "
         "HiL-Pruefstaende, Buero-Equipment) mit VS 30 Mio. EUR; Betriebsunterbrechung Haftzeit 24 Monate. "
         "Sublimit fuer einzelnen HiL-Pruefstand: max. 3,5 Mio. EUR (Vector LABCAR). Praemie 125 TEUR p.a., "
         "Selbstbehalt 25 TEUR je Schadensfall."),
        ("Zusicherung",
         "Die Brennhagen Software GmbH bestaetigt die ordnungsgemaesse Praemienzahlung aller vorgenannten "
         "Vertraege fuer das Jahr 2023. Es bestehen keine offenen Schadenfaelle oberhalb der "
         "Selbstbehalts-Schwelle. Letzte Schadenmeldung: 14.06.2023 (Cyber-Vorfall Phishing-Angriff, "
         "kein Datenabfluss bestaetigt, Mandiant-Forensik abgeschlossen, Schaden < 25 TEUR)."),
        ("Unterschrift",
         signatures("Dr. Klaus Kessler", "Geschaeftsfuehrer", "Brennhagen Software GmbH",
                    "Christine Weidinger", "Controlling RSG (i.V. Versicherungswesen)", "Brennhagen Software GmbH",
                    place=PLACE, date_str_="31. Dezember 2023")),
    ])


# ============================================================================
# 11) RSG WP Management Letters (3x: 2021, 2022, 2023)
# ============================================================================
def wp_management_letter(fname, jahr, findings_top, status):
    write_doc(f"{BASE}/{fname}", H_RSG,
        f"Management Letter {jahr} - Brennhagen Software GmbH",
        subtitle=f"Bericht der Abschlusspruefung KPMG AG WPG zum Jahresabschluss {jahr}",
        confidential=True,
        sections=[
            ("Adressaten / Pruefer",
             f"Adressaten: Dr. Klaus Kessler (GF Brennhagen Software GmbH), "
             f"COO REA (Dr. Thomas Weber), CFO REA (Laura Bauer), "
             f"Aufsichtsrats-Pruefungsausschuss REA (Prof. Dr. Voss)\n\n"
             f"Pruefer: KPMG AG Wirtschaftspruefungsgesellschaft, Ganghoferstrasse 29, 80339 Muenchen\n"
             f"Lead Partner: Dr. Maximilian Brand (Konzern), Senior Manager Vor-Ort: Anke Riethmaier\n"
             f"Pruefungsteam: 3 Senior Auditors, 5 Auditors\n"
             f"Pruefungszeitraum: 15.01.{int(jahr)+1} bis 28.02.{int(jahr)+1}\n\n"
             f"Status der Pruefung: {status}"),
            ("Pruefungsauftrag / Umfang",
             f"Pruefung des Jahresabschlusses (HGB) und des Reporting-Packages (IFRS) der Brennhagen "
             f"Software GmbH zum 31.12.{jahr} im Rahmen der Konzernabschlusspruefung der Brennhagen "
             f"Elektronik AG. Pruefungsschwerpunkte gemaess Pruefungsplanungsbesprechung mit GF Kessler "
             f"vom 15.11.{jahr}:\n\n"
             "- Umsatzrealisation bei Festpreis-Software-Projekten (IFRS 15 / HGB)\n"
             "- Bewertung Software-Entwicklungsleistungen / Aktivierung (IAS 38 / § 248 Abs. 2 HGB)\n"
             "- IT-Allgemein-Kontrollen (ITGC) im SAP-Umfeld\n"
             "- Cross-Charge-Verrechnungen mit Konzerngesellschaften (Transfer Pricing)\n"
             "- Compliance Konzernrichtlinien (Geschenke, Hinweisgeber, Sanktionen)"),
            ("Wesentliche Feststellungen (Top-Themen)",
             ("list", findings_top)),
            ("Bewertung der internen Kontrollsysteme",
             "Das interne Kontrollsystem (IKS) der Brennhagen Software GmbH wurde im Berichtsjahr "
             f"{jahr} als grundsaetzlich angemessen bewertet. Die Kontrollumgebung im Bereich "
             "Rechnungswesen (4-Augen-Prinzip bei Buchungen > 50 TEUR, monatlicher Abschluss-Review "
             "GF) ist solide. Verbesserungspotenzial besteht weiterhin im Bereich IT-Berechtigungen "
             "(SAP-Rollen ueberlappend; Re-Zertifizierung halbjaehrlich erfolgt verspaetet)."),
            ("Empfehlungen",
             ("list", [
                 "Aufnahme einer formalen Procedure 'Quartalsabschluss-Checkliste' nach Konzernvorlage "
                 "REA-CFO-2022 (bisher RSG-eigener Schema).",
                 "Beschleunigung der SAP-Berechtigungs-Re-Zertifizierung auf quartalsweise (statt halb"
                 "jaehrlich).",
                 "Etablierung eines formalen TP-Documentation-Reviews durch externe Berater (Empfehlung: "
                 "Deloitte / EY) zur Bestaetigung der OECD-Konformitaet der Cost-Plus-Verrechnung.",
                 "Hochwertige Schulung Bilanz-Bewertungsfragen (IAS 38) fuer das RSG-Controlling-Team "
                 "(Christine Weidinger).",
             ])),
            ("Reaktion der Geschaeftsfuehrung",
             "Die Geschaeftsfuehrung der RSG nimmt die Feststellungen und Empfehlungen zur Kenntnis und "
             "wird einen Massnahmenplan mit Verantwortlichkeiten und Terminen erstellen. Naechste "
             "Statusberichterstattung erfolgt im Rahmen der unterjaehrigen Pruefungsbegleitung "
             f"(Quartalsreviews ab Q2/{int(jahr)+1})."),
            ("Schlussbemerkung",
             "Dieser Management Letter ergaenzt den Pruefungsbericht und ist ausschliesslich fuer den "
             "internen Gebrauch der Geschaeftsfuehrung und des Aufsichtsorgans bestimmt. Eine Weitergabe "
             "an Dritte bedarf der vorherigen Zustimmung der KPMG AG WPG. Es gilt unsere Standard-"
             "Haftungsbeschraenkung gemaess WPO § 323a (max. 4 Mio. EUR je Pruefungsauftrag)."),
            ("Unterschrift KPMG",
             signatures("Dr. Maximilian Brand", "Wirtschaftspruefer, Lead Partner", "KPMG AG WPG",
                        "Anke Riethmaier", "Wirtschaftspruefer, Senior Manager", "KPMG AG WPG",
                        place=PLACE, date_str_=f"28. Februar {int(jahr)+1}")),
        ])


wp_management_letter("RSG_WP_Management_Letter_2021.docx", "2021",
    findings_top=[
        "Aktivierungsfaehige Entwicklungskosten (IAS 38 / IFRS Reporting Package): Es wurden im "
        "Berichtsjahr 2,4 Mio. EUR Entwicklungsleistungen fuer Projekt PRJ-2021-002 (ADAS-V4D) als "
        "Asset aktiviert. Die Voraussetzungen gemaess IAS 38.57 (a-f) sind grundsaetzlich erfuellt; "
        "wir empfehlen jedoch eine staerkere Dokumentation der 'Technical Feasibility'.",
        "Cross-Charge an RCZ Brno: Die monatliche Cross-Charge-Verrechnung erfolgt korrekt zum "
        "Verrechnungspreis Cost-Plus 7,5 %. Die Plausibilisierung des unterliegenden Stundennachweises "
        "(detaillierte Mitarbeiter-Erfassung) ist verbesserungsfaehig - aktuell nur Pauschal-Cost-Pool.",
        "IT-Allgemeinkontrollen (ITGC): SAP-Berechtigungs-Re-Zertifizierung erfolgte nur einmalig im "
        "Jahr (Mai 2021), Empfehlung halbjaehrlich. Privileged-Access-Management (PAM-Tool) noch nicht "
        "ausgerollt - geplant Q2/2022.",
        "Hinweisgebersystem: Bisher kein eigenes RSG-Whistleblower-System; Hinweise muessen ueber "
        "Konzern-System REA gemeldet werden. Mit LkSG-Eintritt 01.01.2024 wird eigenes RSG-System "
        "notwendig.",
    ],
    status="Abschluss der Vor-Ort-Pruefung 25.02.2022; Bestaetigungsvermerk uneingeschraenkt erteilt")

wp_management_letter("RSG_WP_Management_Letter_2022.docx", "2022",
    findings_top=[
        "Aktivierungsfaehige Entwicklungskosten gestiegen auf 3,1 Mio. EUR (PRJ-2021-002 ADAS-V4D, "
        "PRJ-2022-003 BMS-12-Hyundai). Die im Vorjahr empfohlene staerkere Dokumentation der "
        "'Technical Feasibility' wurde umgesetzt (Polarion-Module 'Feasibility-Studie'). KEINE "
        "Aenderungsempfehlung mehr.",
        "Cross-Charge-Stundennachweise: Detaillierte Mitarbeiter-Erfassung in JIRA + Tempo eingefuehrt "
        "(Q3/2022). Empfehlung des Vorjahres umgesetzt.",
        "IT-Berechtigungen / PAM: PAM-Tool CyberArk implementiert (Q3/2022). Re-Zertifizierung jedoch "
        "weiterhin nur halbjaehrlich. Empfehlung: quartalsweise.",
        "Transfer Pricing Documentation: Erstmals separates RSG-Local-File (Eigenstaendig vs. Konzern) "
        "erstellt durch internes TP-Team. Wir empfehlen externe Validierung durch Spezialberater.",
        "Cyber-Vorfall April 2022: Phishing-Angriff auf 3 Mitarbeiter (Credentials kompromittiert), "
        "schnelle Reaktion durch Mandiant. Folgen finanziell unwesentlich; Lessons-Learned umgesetzt.",
    ],
    status="Bestaetigungsvermerk uneingeschraenkt erteilt 26.02.2023")

wp_management_letter("RSG_WP_Management_Letter_2023.docx", "2023",
    findings_top=[
        "Aktivierungsfaehige Entwicklungskosten weiter erhoeht auf 3,8 Mio. EUR (PRJ-2023-001 ADAS-V4D-"
        "Folgeprojekt, PRJ-2023-004 Cost-Reduction-Programm). Bewertung weiterhin angemessen.",
        "TP-Documentation: Externe Validierung durch Deloitte erfolgt Q4/2023; OECD-Konformitaet "
        "bestaetigt. Vorjahresempfehlung vollstaendig umgesetzt.",
        "IT-Berechtigungen: Re-Zertifizierung erstmals quartalsweise durchgefuehrt (Q1-Q4/2023). "
        "Vorjahresempfehlung vollstaendig umgesetzt.",
        "Vorbereitung ISO 27001:2022 Zertifizierung (geplant Q4/2024): Pre-Audit durch TUEV SUED in "
        "Q3/2023 ohne Major-Findings; Stage-1-Audit fuer Maerz 2024 geplant.",
        "Vorbereitung LkSG-Inkrafttreten 01.01.2024 (RSG groesser 1.000 MA-Schwelle erst nach Inkraft"
        "treten 2024): Risikoanalyse Lieferanten erstellt; Verhaltenskodex fuer Tier-1-Lieferanten "
        "ausgerollt. KEIN Findings.",
    ],
    status="vorbehaltlich Bestaetigungsvermerk - Pruefung laeuft 15.01.-28.02.2024")


# ============================================================================
# 12) Misplaced IC Rechnungen (RCN, REG, RPL) - treat by prefix
# ============================================================================
def misplaced_ic_rechnung(fname, gesellschaft_short, gesellschaft, header, jahr, monat,
                          betrag_eur, leistung, partner):
    rn = f"{gesellschaft_short}-IC-{jahr}{monat:02d}-001"
    mon_str = ["", "Januar","Februar","Maerz","April","Mai","Juni","Juli","August",
               "September","Oktober","November","Dezember"][monat]
    rd = f"{(monat*3) % 28 + 1}. {mon_str} {jahr}"
    write_doc(f"{BASE}/{fname}", header,
        f"Intercompany Rechnung Nr. {rn} - {gesellschaft} an {partner}",
        subtitle=f"Leistungszeitraum {mon_str} {jahr}",
        sections=[
            ("Rechnungsdaten",
             f"Rechnungs-Nr.: {rn}\n"
             f"Rechnungsdatum: {rd}\n"
             f"Leistungszeitraum: 01. - {28 if monat==2 else 30}. {mon_str} {jahr}\n"
             f"Zahlungsziel: 30 Tage netto (Konzern-IC-Vereinbarung 2020)\n"
             f"Status: FINAL"),
            ("Rechnungssteller",
             f"{gesellschaft}\n{header['addr']}\n{header['hrb']}\n"
             f"USt-IdNr.: gemaess landesublichem Recht"),
            ("Rechnungsempfaenger",
             f"{partner}\nVaihinger Strasse 120, 70567 Stuttgart\nHRB 726451, Amtsgericht Stuttgart"
             if "Elektronik AG" in partner else
             f"{partner}\n(siehe Konzernverzeichnis Brennhagen)"),
            ("Leistungsbeschreibung",
             f"Im Berichtsmonat {mon_str} {jahr} wurden im Rahmen der konzerninternen IC-Vereinbarung "
             f"folgende Leistungen erbracht:\n\n{leistung}\n\n"
             f"Die Verrechnung erfolgt zum Verrechnungspreis Cost-Plus 7,5 % gemaess Transfer-Pricing-"
             f"Studie KPMG 2019 und der jeweiligen lokalen Cost-Pool-Vereinbarung. Stundensaetze und "
             f"Materialnebenkosten sind in Anlage 1 ausgewiesen."),
            ("Rechnungsposten",
             [["Pos.", "Kategorie", "Betrag (EUR)"],
              ["1", "Operative Leistungen / Engineering", f"{betrag_eur*0.65:,.0f}".replace(",", ".")],
              ["2", "Qualitaets-/Pruefleistungen", f"{betrag_eur*0.20:,.0f}".replace(",", ".")],
              ["3", "Logistik / Material-Nebenkosten", f"{betrag_eur*0.15:,.0f}".replace(",", ".")],
              ["", "Netto-Summe", f"{betrag_eur:,.0f}".replace(",", ".")],
              ["", "USt (Reverse Charge § 13b UStG / EU-B2B)", "0,00"],
              ["", "Rechnungsbetrag gesamt", f"{betrag_eur:,.0f}".replace(",", ".")]]),
            ("Zahlungs-/Anlagen-Hinweise",
             f"Der Rechnungsbetrag i. H. v. {betrag_eur:,.0f} EUR ".replace(",", ".") +
             f"wird im Rahmen des monatlichen Konzern-Settlement-Runs verrechnet. Bei Verrechnung im "
             f"Cash-Pool entfaellt eine separate Ueberweisung. Bei Saldo > 50 TEUR ist eine Aus"
             f"gleichszahlung am 25. des Folgemonats vorgesehen.\n\nAnlagen: Stundennachweis (Anlage 1), "
             f"Kostenstellenuebersicht (Anlage 2), Cross-Charge-Vereinbarung 2020 (Anlage 3, Verweis)."),
            ("Hinweis Ablagefolder",
             f"Hinweis: Diese Rechnung gehoert organisationsorganisatorisch in den Ablage-Pfad der "
             f"emittierenden Gesellschaft ({gesellschaft_short}), wurde jedoch im Zuge der konzern"
             f"weiten Cross-Charge-Konsolidierung im RSG-Ordner abgelegt (siehe Konzernverrechnungs"
             f"vereinbarung 2020, § 4 Abs. 3 zu zentraler Ablage)."),
        ])

misplaced_ic_rechnung("RCN_IC_Rechnung_2020_11.docx", "RCN", "Brennhagen (Shanghai) Co. Ltd.", H_RCN,
    "2020", 11, 168_500,
    "Vertriebs- und Aftermarket-Leistungen Asien-Pazifik fuer ICP-3 und BMS-12; Repraesentation "
    "auf Auto Shanghai 2020 (DD-Demos OEM-Termine BYD, NIO, Geely)",
    "Brennhagen Elektronik AG")
misplaced_ic_rechnung("REG_IC_Rechnung_2021_08.docx", "REG", "Brennhagen Elektronik GmbH (Heilbronn)", H_REG,
    "2021", 8, 525_700,
    "Produktions-Service-Leistungen Hauptwerk Heilbronn fuer Konzernumlage (Linienbetreuung BMS-12, "
    "ICP-3); SMT-Linien-Wartung im Sommer-Shutdown; ASPICE-Audit-Vorbereitung",
    "Brennhagen Elektronik AG")
misplaced_ic_rechnung("RPL_IC_Rechnung_2021_06.docx", "RPL", "Brennhagen Polska Sp. z o.o. (Katowice)", H_RPL,
    "2021", 6, 442_300,
    "EMS-Produktion (SMD-Bestueckung) fuer ICP-3, BMS-12 und LightCtrl-7; Schichtbetrieb 24/7 "
    "in Linie 1-3; Qualitaetspruefungen AOI/X-Ray; Logistik-Service zu Heilbronn",
    "Brennhagen Elektronik AG")


print("=" * 60)
print("RSG Muenchen regen complete.")
print("=" * 60)
