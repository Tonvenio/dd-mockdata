"""Müller / 03_Personal_HR – 29 thin docs."""
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

BASE = f"{_ROOT}/mueller_small/03_Personal_HR"
H = {"name": M["name"], "addr": M["addr"], "hrb": M["hrb"]}


# Arbeitsvertrag template ---------------------------------------------------
def arbeitsvertrag(fname_suffix, name, geb, beginn, position, abteilung, dienstort,
                   eingruppierung_jahresgehalt, urlaubstage=30, wochenstd=35,
                   variabel_pct=None, kuendigung="3 Monate zum Quartalsende"):
    write_doc(
        f"{BASE}/{fname_suffix}.docx", H,
        f"Arbeitsvertrag – {name}",
        subtitle=f"Eintrittsdatum: {beginn}",
        sections=[
            ("Vertragsparteien",
             f"Halbreiter Maschinenbau GmbH, Industriestrasse 12, 50829 Koeln (»Arbeitgeber«), und "
             f"{name}, geboren am {geb} (»Arbeitnehmer«). Es gilt der Manteltarifvertrag der Metall- und "
             f"Elektroindustrie NRW (M+E NRW) sowie der Entgeltrahmentarifvertrag (ERA). Die "
             f"betrieblichen Regelungen (Betriebsvereinbarungen Anlage 4) sind Bestandteil dieses Vertrages."),
            ("Vertragsinhalt",
             ("clauses", [
                 ("§ 1 Beginn / Probezeit", [
                     f"Das Arbeitsverhaeltnis beginnt am {beginn} und wird auf unbestimmte Zeit geschlossen.",
                     "Die ersten sechs Monate sind Probezeit; in dieser Zeit kann das Arbeitsverhaeltnis "
                     "von beiden Seiten mit einer Frist von zwei Wochen schriftlich gekuendigt werden.",
                 ]),
                 ("§ 2 Taetigkeit und Eingruppierung", [
                     f"Der/die Arbeitnehmer:in wird in der Abteilung {abteilung} als {position} eingestellt. "
                     f"Dienstort ist {dienstort}.",
                     f"Eingruppierung: Entgeltgruppe {eingruppierung_jahresgehalt[0]} ERA. "
                     f"Jahresbruttogehalt (inkl. tariflicher Sonderzahlungen): {eingruppierung_jahresgehalt[1]} EUR.",
                     "Die Gesellschaft kann dem/der Arbeitnehmer:in unter Wahrung seiner/ihrer Qualifikation und "
                     "Vergutungsgruppe eine andere zumutbare Taetigkeit zuweisen.",
                 ]),
                 ("§ 3 Arbeitszeit", [
                     f"Die regelmaessige woechentliche Arbeitszeit betraegt {wochenstd} Stunden, verteilt "
                     "ueblicherweise auf Montag bis Freitag (Gleitzeitrahmen 06:30 bis 18:30 Uhr; Kernzeit "
                     "09:00 bis 15:00 Uhr).",
                     "Mehrarbeit ist in den Grenzen des ArbZG zulaessig und wird gemaess BV »Arbeitszeit« "
                     "(HR_011) durch Freizeit ausgeglichen oder mit dem Stundenlohn zuzueglich Zuschlag verguetet.",
                 ]),
                 ("§ 4 Vergutung", [
                     f"Die Vergutung wird monatlich zum Monatsende auf das vom/von der Arbeitnehmer:in "
                     "angegebene Konto ueberwiesen.",
                     "Sonderzahlungen (Urlaubsgeld, Jahresleistung) erfolgen gemaess Tarifvertrag.",
                 ] + ([
                     f"Zusaetzlich wird eine ergebnisabhaengige Pramie von bis zu {variabel_pct} % "
                     "des Jahresbruttogehalts gewaehrt (Zielvereinbarung jaehrlich)."
                 ] if variabel_pct else [])),
                 ("§ 5 Urlaub und Krankheit", [
                     f"Der Jahresurlaub betraegt {urlaubstage} Arbeitstage bei einer 5-Tage-Woche.",
                     "Bei Arbeitsunfaehigkeit infolge Krankheit ist der Arbeitgeber unverzueglich, spaetestens "
                     "vor Beginn der vertraglichen Arbeitszeit, zu informieren. Ein aerztliches Attest ist "
                     "ab dem dritten Krankheitstag vorzulegen.",
                 ]),
                 ("§ 6 Verschwiegenheit und Datenschutz", [
                     "Der/die Arbeitnehmer:in verpflichtet sich, Geschaefts- und Betriebsgeheimnisse waehrend "
                     "und nach Beendigung des Arbeitsverhaeltnisses geheim zu halten.",
                     "Auf die Datenschutzhinweise nach Art. 13 DSGVO (Anlage 1) und die Verpflichtung auf das "
                     "Datengeheimnis (§ 53 BDSG) wird hingewiesen.",
                 ]),
                 ("§ 7 Erfindungen", [
                     "Diensterfindungen unterliegen dem ArbnErfG; eine entsprechende Erfindungsmeldung erfolgt "
                     "schriftlich an die Geschaeftsfuehrung.",
                 ]),
                 ("§ 8 Kuendigung und Versetzung", [
                     f"Nach der Probezeit kann das Arbeitsverhaeltnis von beiden Seiten mit einer Frist von "
                     f"{kuendigung} gekuendigt werden, soweit nicht gesetzlich oder tariflich laengere "
                     "Fristen gelten.",
                     "Eine Aenderungskuendigung mit dem Ziel einer anderen, gleichwertigen Taetigkeit bleibt "
                     "vorbehalten.",
                 ]),
                 ("§ 9 Wettbewerbsverbot / Nebentaetigkeiten", [
                     "Waehrend des Arbeitsverhaeltnisses besteht ein vertragliches Wettbewerbsverbot. "
                     "Entgeltliche Nebentaetigkeiten beduerfen der vorherigen schriftlichen Zustimmung des "
                     "Arbeitgebers.",
                 ]),
                 ("§ 10 Schlussbestimmungen", [
                     "Aenderungen und Ergaenzungen beduerfen der Schriftform. Sollte eine Bestimmung "
                     "unwirksam sein, beruehrt dies die Wirksamkeit der uebrigen Bestimmungen nicht.",
                     "Es gilt deutsches Recht. Gerichtsstand ist Koeln.",
                 ]),
             ])),
            ("Anlagen",
             "Anlage 1: Datenschutzhinweise nach Art. 13 DSGVO\n\n"
             "Anlage 2: Stellenbeschreibung\n\n"
             "Anlage 3: Geltende Tarifvertraege (ERA / Manteltarifvertrag M+E NRW)\n\n"
             "Anlage 4: Geltende Betriebsvereinbarungen"),
            ("Unterschriften",
             signatures("Andrea Hoffmann", "Leiterin Personal & Verwaltung", M["name"],
                        name, position, "i. e. S.",
                        place="Koeln", date_str_=beginn)),
        ],
    )


# 9 Arbeitsvertraege HR_001 … HR_010 (HR_006 ist mit Petra Zimmermann; HR_010 mit Lisa Schulz)
arbeitsvertrag("HR_001_Arbeitsvertrag_Thomas_Schneider", "Thomas Schneider",   "14.03.1981", "1. April 2014",
               "Vorarbeiter Montage Pressenlinie",      "Produktion Halle B",  "Koeln",
               eingruppierung_jahresgehalt=("EG 9", "58.400"), variabel_pct=8)
arbeitsvertrag("HR_002_Arbeitsvertrag_Andrea_Hoffmann", "Andrea Hoffmann",     "22.08.1976", "1. September 2008",
               "Leiterin Personal & Verwaltung",        "Personal & Verwaltung", "Koeln",
               eingruppierung_jahresgehalt=("AT", "98.000"), variabel_pct=15, kuendigung="6 Monate zum Quartalsende")
arbeitsvertrag("HR_003_Arbeitsvertrag_Michael_Weber",  "Michael Weber",       "5.05.1969",  "1. Mai 1996",
               "Senior Konstruktionsingenieur",          "Konstruktion / F&E",   "Koeln",
               eingruppierung_jahresgehalt=("EG 14", "84.200"), variabel_pct=10)
arbeitsvertrag("HR_004_Arbeitsvertrag_Julia_Krause",   "Julia Krause",         "18.11.1988", "1. Maerz 2018",
               "Sachbearbeiterin Vertrieb Innendienst", "Vertrieb",            "Koeln",
               eingruppierung_jahresgehalt=("EG 7", "48.200"))
arbeitsvertrag("HR_005_Arbeitsvertrag_Stefan_Braun",   "Stefan Braun",         "6.05.1972",  "1. Februar 2018",
               "Leiter Strategischer Einkauf",          "Einkauf",             "Koeln",
               eingruppierung_jahresgehalt=("AT", "118.000"), variabel_pct=20, kuendigung="6 Monate zum Quartalsende")
arbeitsvertrag("HR_006_Arbeitsvertrag_Petra_Zimmermann","Petra Zimmermann",   "11.10.1984", "1. Juli 2015",
               "Buchhalterin / Bilanzbuchhalterin",     "Finanzen",            "Koeln",
               eingruppierung_jahresgehalt=("EG 10", "62.400"))
arbeitsvertrag("HR_007_Arbeitsvertrag_Markus_Fischer","Markus Fischer",       "30.04.1980", "1. Januar 2016",
               "Key Account Manager Industrie",         "Vertrieb",            "Koeln",
               eingruppierung_jahresgehalt=("AT", "92.400"), variabel_pct=25)
arbeitsvertrag("HR_008_Arbeitsvertrag_Sabine_Koch",   "Sabine Koch",         "2.02.1983",  "1. Maerz 2019",
               "Sachbearbeiterin Personal / Lohn",      "Personal & Verwaltung", "Koeln",
               eingruppierung_jahresgehalt=("EG 9", "54.600"))
arbeitsvertrag("HR_009_Arbeitsvertrag_Jan_Müller",    "Jan Mueller",         "19.06.1986", "1. Juli 2017",
               "Key Account Manager Automotive",         "Vertrieb",            "Koeln",
               eingruppierung_jahresgehalt=("AT", "98.200"), variabel_pct=25)
arbeitsvertrag("HR_010_Arbeitsvertrag_Lisa_Schulz",   "Lisa Schulz",         "26.09.1990", "1. April 2020",
               "Servicetechnikerin / Inbetriebnahme",   "Service / After Sales", "Koeln",
               eingruppierung_jahresgehalt=("EG 10", "56.800"))


# ─── HR_011 BV Arbeitszeit und Schichtmodelle ──────────────────────────────
write_doc(
    f"{BASE}/HR_011_BV_Arbeitszeit_und_Schi.docx", H,
    "Betriebsvereinbarung – Arbeitszeit und Schichtmodelle (BV-Nr. 11/2021)",
    subtitle="Wirksam ab 1. Januar 2022; geaendert 14. Juni 2023",
    sections=[
        ("Praeambel",
         "Zwischen der Halbreiter Maschinenbau GmbH (Arbeitgeber, vertreten durch Klaus Mueller und Sandra Becker) "
         "und dem Betriebsrat (vertreten durch den Vorsitzenden Herrn Wolfgang Brettschneider) wird diese "
         "Betriebsvereinbarung gemaess § 87 Abs. 1 Nr. 2 und 3 BetrVG geschlossen. Sie regelt Arbeitszeitkonten, "
         "Schichtmodelle in der Produktion sowie die Verteilung der woechentlichen Arbeitszeit."),
        ("Geltungsbereich",
         "Diese Betriebsvereinbarung gilt fuer alle gewerblichen und kaufmaennischen Mitarbeitenden der "
         "Gesellschaft am Standort Koeln. Sie gilt nicht fuer leitende Angestellte gemaess § 5 Abs. 3 BetrVG "
         "und nicht fuer die Geschaeftsfuehrung."),
        ("Regelarbeitszeit",
         ("clauses", [
             ("§ 1 Woechentliche Arbeitszeit", [
                 "Die regelmaessige woechentliche Arbeitszeit der Vollzeitbeschaeftigten betraegt 35 Stunden, "
                 "verteilt auf Montag bis Freitag.",
                 "Fuer leitende Angestellte AT gilt eine Vertrauensarbeitszeit ohne ausdrueckliche "
                 "stundengenaue Erfassung; die Erfuellung der dienstlichen Aufgaben ist massgeblich.",
             ]),
             ("§ 2 Gleitzeit", [
                 "Im kaufmaennischen Bereich gilt ein Gleitzeitrahmen von Montag bis Freitag 06:30 bis "
                 "18:30 Uhr; Kernzeit 09:00 bis 15:00 Uhr.",
                 "Der/die Mitarbeitende kann Plus-/Minusstunden bis +/- 80 Stunden auf das Arbeitszeitkonto "
                 "buchen. Ein Ausgleich erfolgt vorrangig durch Freizeit.",
             ]),
             ("§ 3 Schichtmodelle Produktion", [
                 "Halle A (Stanzpressen): 2-Schicht-Betrieb Mo-Fr (Fruehschicht 06:00-14:00; Spaetschicht "
                 "14:00-22:00).",
                 "Halle B (Laser / Robotik): 3-Schicht-Betrieb Mo 06:00 bis Fr 22:00 (Frueh-, Spaet-, Nachtschicht).",
                 "Halle C (Foerderbaender / Montage): 2-Schicht-Betrieb Mo-Fr 06:00-22:00; bei Auftragslage "
                 "Erweiterung auf Samstagsschicht moeglich (Zustimmung Betriebsrat erforderlich).",
             ]),
             ("§ 4 Zuschlaege", [
                 "Spaetschicht (ab 14:00 Uhr): 15 %; Nachtschicht (22:00 bis 06:00 Uhr): 25 %; "
                 "Samstagsarbeit: 25 %; Sonn- und Feiertagsarbeit: 75 %.",
                 "Mehrarbeit ueber 8 Std. taeglich: 25 % Zuschlag oder 1:1,25 in Zeit.",
             ]),
             ("§ 5 Arbeitszeitkonten", [
                 "Es werden Langzeitkonten (max. 360 Stunden) angeboten, die zur Reduktion der Arbeitszeit "
                 "vor Renteneintritt oder fuer Bildungsmassnahmen genutzt werden koennen.",
             ]),
             ("§ 6 Pausen und Ruhezeiten", [
                 "Mindestens 30 Min. Pause bei Arbeitszeit > 6 Std., 45 Min. bei > 9 Std. Mindestruhezeit "
                 "zwischen zwei Arbeitstagen 11 Stunden gem. ArbZG.",
             ]),
         ])),
        ("Mitbestimmung",
         "Aenderungen der Schichtplaene mit Wirkung von mehr als 4 Wochen beduerfen der Zustimmung des "
         "Betriebsrats (§ 87 Abs. 1 Nr. 2 BetrVG). Eilfaelle werden gem. § 100 BetrVG behandelt."),
        ("Laufzeit",
         "Diese Vereinbarung tritt am 1. Januar 2022 in Kraft und kann mit einer Frist von 6 Monaten zum "
         "Jahresende gekuendigt werden. Nach Ablauf wirkt sie gem. § 77 Abs. 6 BetrVG nach, bis eine neue "
         "Vereinbarung in Kraft tritt."),
        ("Unterschriften",
         signatures("Klaus Mueller / Sandra Becker", "Geschaeftsfuehrung", M["name"],
                    "Wolfgang Brettschneider", "Betriebsratsvorsitzender", M["name"],
                    place="Koeln", date_str_="20. Dezember 2021")),
    ],
)


# ─── HR_012 BV Mobiles Arbeiten / Homeoffice ───────────────────────────────
write_doc(
    f"{BASE}/HR_012_BV_Mobiles_Arbeiten_Ho.docx", H,
    "Betriebsvereinbarung – Mobiles Arbeiten / Homeoffice (BV-Nr. 12/2022)",
    subtitle="Wirksam ab 1. April 2022",
    sections=[
        ("Praeambel",
         "Mit dieser Betriebsvereinbarung gem. § 87 Abs. 1 Nr. 14 BetrVG werden die Rahmenbedingungen fuer "
         "mobiles Arbeiten und Homeoffice geregelt. Sie loest die Pandemie-Regelung vom 13. Maerz 2020 ab "
         "und stellt mobiles Arbeiten dauerhaft auf eine geregelte Basis."),
        ("Geltungsbereich",
         "Diese BV gilt fuer alle Beschaeftigten, deren Taetigkeit ueberwiegend ortsunabhaengig erbracht "
         "werden kann (i. d. R. kaufmaennische Bereiche, Vertrieb, F&E, Konstruktion, Einkauf, IT). "
         "Sie gilt nicht fuer Schicht- und produktionsgebundene Taetigkeiten."),
        ("Regelungen",
         ("clauses", [
             ("§ 1 Umfang", [
                 "Mobiles Arbeiten ist bis zu 2 Tage pro Woche grundsaetzlich moeglich. Im Einzelfall (z. B. "
                 "Pflege Angehoeriger) kann der Anteil mit Zustimmung des/der Vorgesetzten und der "
                 "Personalleitung erhoeht werden.",
                 "Mobiles Arbeiten ist kein Anspruch; der/die Arbeitgeber kann es aus betrieblichen Gruenden "
                 "(z. B. Praesenztage, Workshops) anordnen oder beschraenken.",
             ]),
             ("§ 2 Arbeitsort und Erreichbarkeit", [
                 "Der mobile Arbeitsort liegt in der Regel im Privathaushalt des/der Beschaeftigten; "
                 "andere Orte (z. B. Bibliothek, Cafe) sind nur zulaessig, wenn Vertraulichkeit, "
                 "Datenschutz und Datensicherheit gewaehrleistet werden koennen.",
                 "Erreichbarkeit waehrend der Kernzeit 09:00-15:00 Uhr; Antworten auf E-Mails und Anrufe "
                 "innerhalb von 4 Stunden wird erwartet.",
             ]),
             ("§ 3 Arbeitsmittel und Ausstattung", [
                 "Der Arbeitgeber stellt Notebook, Headset, Bildschirm und Tastatur. Mobilfunkanschluss "
                 "wird ab Funktion »Aussendienst« gestellt; sonst Privatnutzung der Festnetzleitung "
                 "akzeptiert.",
                 "Eine Pauschale fuer Energie- und Internetkosten in Hoehe von 30 EUR pro Monat "
                 "(steuerlich pauschal, max. 1.260 EUR p. a.) wird auf Antrag gewaehrt.",
             ]),
             ("§ 4 Arbeitszeit", [
                 "Die Arbeitszeit wird im SAP-Zeiterfassungssystem manuell erfasst. Es gelten die "
                 "ArbZG-Vorgaben (max. 10 Std. taeglich, 11 Std. Ruhezeit, Pausen).",
             ]),
             ("§ 5 Datenschutz und Informationssicherheit", [
                 "Es gelten die ISMS-Richtlinien sowie die Verpflichtung auf den Datenschutz (Anlage 1). "
                 "Externe Personen sind vom Arbeitsplatz fernzuhalten; Bildschirmschoner mit Sperre "
                 "nach 5 Minuten Inaktivitaet.",
                 "Vertrauliche Dokumente sind nicht auszudrucken. Eine VPN-Verbindung ist "
                 "verpflichtend (PaloAlto GlobalProtect).",
             ]),
             ("§ 6 Arbeitsschutz und Unfallschutz", [
                 "Der/die Beschaeftigte sorgt fuer eine ergonomische Gestaltung des heimischen "
                 "Arbeitsplatzes; eine Eigenerklaerung wird abgegeben.",
                 "Unfallschutz besteht im Rahmen der gesetzlichen Unfallversicherung im sachlichen "
                 "Zusammenhang mit der Taetigkeit.",
             ]),
             ("§ 7 Beendigung der Vereinbarung", [
                 "Im Einzelfall kann die mobile Arbeit mit einer Frist von 4 Wochen wieder beendet "
                 "werden; Begruendungspflicht durch den Arbeitgeber.",
             ]),
         ])),
        ("Schlussbestimmungen",
         "Diese BV laeuft am 31. Maerz 2027 aus und verlaengert sich automatisch um 24 Monate, soweit "
         "nicht 6 Monate vor Ablauf gekuendigt. Sie wurde mit dem Betriebsrat im Sozialausschuss am "
         "14.3.2022 abgestimmt und einstimmig beschlossen."),
        ("Unterschriften",
         signatures("Klaus Mueller", "Geschaeftsfuehrer", M["name"],
                    "Wolfgang Brettschneider", "Betriebsratsvorsitzender", M["name"],
                    place="Koeln", date_str_="25. Maerz 2022")),
    ],
)


# ─── HR_013 BV Nutzung IT-Systeme ──────────────────────────────────────────
write_doc(
    f"{BASE}/HR_013_BV_Nutzung_von_IT-Syste.docx", H,
    "Betriebsvereinbarung – Nutzung von IT-Systemen (BV-Nr. 13/2022)",
    subtitle="Wirksam ab 1. Juli 2022",
    sections=[
        ("Praeambel",
         "Diese Betriebsvereinbarung regelt gemaess § 87 Abs. 1 Nr. 6 BetrVG die Einfuehrung und Nutzung "
         "technischer Einrichtungen, die das Verhalten oder die Leistung der Beschaeftigten ueberwachen "
         "koennen. Sie umfasst die in der Anlage 1 abschliessend aufgefuehrten Systeme (SAP S/4HANA, "
         "Salesforce CRM, MES-Pilot Halle B, EDR/SIEM-Loesung, Active Directory, Webfilter / Proxy)."),
        ("Grundsaetze",
         "Die IT-Systeme dienen ausschliesslich betrieblichen Zwecken. Eine systematische Leistungs- oder "
         "Verhaltensueberwachung der einzelnen Beschaeftigten findet nicht statt. Aggregierte Auswertungen "
         "(z. B. Lizenzauslastung, System-Performance) sind zulaessig, sofern sie keinen Rueckschluss auf "
         "einzelne Personen erlauben."),
        ("Regelungen",
         ("clauses", [
             ("§ 1 Erlaubte Nutzung", [
                 "Dienstliche Nutzung von E-Mail, Internet und Telefon ist gestattet. Private Nutzung in "
                 "geringem Umfang (sog. »normale Sozialadaequanz«) ist toleriert, soweit dienstliche "
                 "Interessen nicht beeintraechtigt werden.",
                 "Es besteht KEIN Anspruch auf private Nutzung der IT-Systeme.",
             ]),
             ("§ 2 Protokollierung und Auswertung", [
                 "Folgende Protokolldaten werden erhoben: Anmeldedaten (Login/Logout), Zugriffsfehler, "
                 "E-Mail-Header (nicht Inhalt), URL-Aufrufe ueber den Webfilter (anonymisiert), "
                 "MES-Anmeldungen, SAP-Audit-Logs, EDR-Events.",
                 "Eine personenbezogene Auswertung ist nur im Einzelfall bei begruendetem Verdacht auf eine "
                 "Straftat oder schwere Pflichtverletzung zulaessig (»4-Augen-Prinzip«: Antrag durch "
                 "Personalleitung, Beteiligung Betriebsrat, Information DSB).",
             ]),
             ("§ 3 Speicherfristen", [
                 "Login-Daten: 30 Tage; E-Mail-Header: 90 Tage; URL-Logs anonymisiert: 14 Tage; "
                 "SAP-Audit-Logs: 12 Monate (gesetzliche GoBD).",
             ]),
             ("§ 4 EDR / SIEM", [
                 "Zur Abwehr von Cybersecurity-Vorfaellen wird eine EDR-Loesung (CrowdStrike Falcon) "
                 "betrieben. Sie wertet Verhaltensmuster der Endgeraete aus; Alerts werden anonymisiert "
                 "geprueft. Bei IT-Sicherheitsvorfaellen koennen Geraete isoliert werden.",
             ]),
             ("§ 5 Mobiles Arbeiten", [
                 "Ergaenzend zur BV »Mobiles Arbeiten« (HR_012) gelten erhoehte Anforderungen: "
                 "VPN-Pflicht, Festplattenverschluesselung (BitLocker), automatischer Bildschirmlock.",
             ]),
             ("§ 6 Schulung", [
                 "Alle Beschaeftigten durchlaufen jaehrlich eine verpflichtende IT-Security-Schulung "
                 "(20 Min., e-Learning). Erstellung und Auswertung erfolgen anonymisiert.",
             ]),
             ("§ 7 Mitbestimmung", [
                 "Aenderungen oder Einfuehrung neuer Tools mit Auswertungsmoeglichkeit beduerfen der "
                 "Zustimmung des Betriebsrats. Eine Liste der eingesetzten Tools wird halbjaehrlich aktualisiert.",
             ]),
         ])),
        ("Unterschriften",
         signatures("Klaus Mueller", "Geschaeftsfuehrer", M["name"],
                    "Wolfgang Brettschneider", "Betriebsratsvorsitzender", M["name"],
                    place="Koeln", date_str_="22. Juni 2022")),
    ],
)


# ─── HR_Sozialplanvereinbarung_2021 ─────────────────────────────────────────
write_doc(
    f"{BASE}/HR_Sozialplanvereinbarung_2021.docx", H,
    "Sozialplanvereinbarung 2021 – Auslauf Pressenlinie PL-300",
    subtitle="Vereinbarung gemaess §§ 111, 112 BetrVG vom 18. Maerz 2021",
    sections=[
        ("Praeambel",
         "Im Rahmen der Investitionsoffensive 2020 (siehe Gesellschafterbeschluss 2020/02) wird die ueber 22 Jahre "
         "betriebene Pressenlinie PL-300 in Halle B durch die neue PL-500 ersetzt. Dieser Wechsel fuehrt zu "
         "tiefgreifenden organisatorischen Aenderungen, die im Sinne von § 111 BetrVG als Betriebsaenderung zu "
         "qualifizieren sind. Geschaeftsfuehrung und Betriebsrat schliessen daher einen Interessenausgleich und "
         "den vorliegenden Sozialplan ab."),
        ("Betroffene",
         "Im Zuge der Modernisierung entfallen drei Vorarbeiterstellen sowie sieben Bedienerpositionen (insgesamt "
         "10 betroffene Beschaeftigte). Sechs davon werden ueber Qualifizierungsmassnahmen in den Bereich "
         "Steuerungstechnik (PL-500) ueberfuehrt; vier Beschaeftigte scheiden ueber Aufhebungsvertraege bzw. "
         "Altersteilzeit / Vorruhestand aus dem Unternehmen aus."),
        ("Regelungen",
         ("clauses", [
             ("§ 1 Qualifizierungsmassnahmen", [
                 "Sechs Beschaeftigte werden gemaess Qualifizierungsplan (Anlage 1) ueber 12 Monate "
                 "fortgebildet. Die Schulungen finden bei der Trumpf Akademie Ditzingen sowie intern statt.",
                 "Die Vergutung bleibt waehrend der Qualifizierungsphase unveraendert.",
             ]),
             ("§ 2 Abfindungsformel", [
                 "Beschaeftigte, die das Unternehmen verlassen, erhalten eine Abfindung nach folgender Formel: "
                 "(Bruttomonatsgehalt) × (Betriebszugehoerigkeit in Jahren) × Faktor 0,85.",
                 "Bei Betriebszugehoerigkeit > 25 Jahre: Faktor 1,1. Bei Schwerbehinderung GdB > 50: "
                 "Zuschlag 5.000 EUR. Bei Unterhaltspflicht fuer minderjaehrige Kinder: Zuschlag "
                 "2.000 EUR je Kind.",
             ]),
             ("§ 3 Vorruhestand / Altersteilzeit", [
                 "Mitarbeitenden ab 58 Jahre wird Altersteilzeit im Blockmodell (3 Jahre Arbeit / 3 Jahre Freistellung) "
                 "angeboten. Aufstockung 85 % des bisherigen Netto.",
             ]),
             ("§ 4 Hilfe bei der Stellensuche", [
                 "Outplacement-Beratung durch von Rundstedt & Partner GmbH (Standort Duesseldorf), Programm "
                 "6 Monate.",
                 "Freistellung fuer Bewerbungsgespraeche: bis zu 3 Tage bezahlt.",
             ]),
             ("§ 5 Verteilungsgrundsatz", [
                 "Sozialauswahl gemaess § 1 Abs. 3 KSchG (Alter, Betriebszugehoerigkeit, Unterhalts-"
                 "verpflichtungen, Schwerbehinderung).",
             ]),
         ])),
        ("Sozialplan-Volumen",
         "Gesamtes Sozialplanvolumen: 412.000 EUR (davon 268.000 EUR Abfindungen, 88.000 EUR Outplacement / "
         "Qualifizierung, 56.000 EUR Aufstockungen ATZ). Buchung als Rueckstellung im Jahresabschluss 2021 "
         "abgestimmt mit BDO AG WPG."),
        ("Unterschriften",
         signatures("Klaus Mueller", "Geschaeftsfuehrer", M["name"],
                    "Wolfgang Brettschneider", "Betriebsratsvorsitzender", M["name"],
                    place="Koeln", date_str_="18. Maerz 2021")),
    ],
)


# ─── HR_Stellenausschreibung_FuE_Ingenieur ─────────────────────────────────
write_doc(
    f"{BASE}/HR_Stellenausschreibung_FuE_Ingenieur.docx", H,
    "Stellenausschreibung – Senior Entwicklungsingenieur:in Pressen-/Steuerungstechnik (m/w/d)",
    subtitle="Standort Koeln – Vollzeit – Veroeffentlichung 12. Februar 2024",
    sections=[
        ("Unternehmen",
         "Die Halbreiter Maschinenbau GmbH ist ein traditionsreicher familiengefuehrter Spezialist fuer "
         "Sondermaschinen und Anlagen im Bereich der metallverarbeitenden Industrie. Mit 247 Mitarbeitenden "
         "entwickeln und liefern wir an namhafte Industriekunden wie ThyssenKrupp Steel Europe, Bosch Rexroth, "
         "Hella, Viessmann und Dürr. Unser Portfolio umfasst hydraulische Stanzpressen (Pressenlinie PL-500), "
         "Foerderbandanlagen (FB-200), Laserschneidanlagen (LS-800) und Robotik-Zellen (MR-150)."),
        ("Ihre Aufgaben",
         ("list", [
             "Konzeption, Auslegung und Detailentwicklung hydraulischer und servo-elektrischer Pressensteuerungen "
             "auf Basis Siemens SINUMERIK ONE und Beckhoff TwinCAT.",
             "Verantwortung fuer Lastenheft-Analyse bei Schluesselkunden (TKSE, Bosch Rexroth, Dürr) und "
             "Erarbeitung kundenspezifischer Anpassungsloesungen.",
             "Fuehrung von 2-3 Konstrukteur:innen / Berechnungsingenieur:innen in Projektteams (matrix).",
             "Mitarbeit an der Roadmap »Pressen 4.0«: Predictive-Maintenance-Module, OPC-UA-Schnittstellen, "
             "Datenanalytik fuer Praediktivinstandhaltung.",
             "Schnittstelle zu Vertrieb, Einkauf und Produktion in saemtlichen Projektphasen.",
         ])),
        ("Ihr Profil",
         ("list", [
             "Abgeschlossenes Studium (Master/Diplom) in Maschinenbau, Elektrotechnik, Mechatronik oder vergleichbar.",
             "Mind. 6-8 Jahre Berufserfahrung in der Entwicklung pressentechnischer Anlagen oder vergleichbarer "
             "Sondermaschinen.",
             "Fundierte Kenntnisse SPS-Programmierung (Siemens TIA Portal / SINUMERIK ONE) und Servo-/Hydraulik-Steuerungen.",
             "Erfahrung mit IEC 61511 / Funktionaler Sicherheit von Vorteil; Kenntnisse Modellbasierte "
             "Entwicklung (MATLAB/Simulink) wuenschenswert.",
             "Verhandlungssichere Deutsch- und gute Englischkenntnisse.",
             "Reisebereitschaft DACH ca. 20 %.",
         ])),
        ("Was wir bieten",
         ("list", [
             "Vergutung gemaess AT-Tarif M+E NRW (Bandbreite 75.000 - 95.000 EUR p. a. je nach Erfahrung) plus "
             "Ergebnistantieme bis 15 %.",
             "Dienstwagen der oberen Mittelklasse (auch zur privaten Nutzung).",
             "30 Tage Urlaub, Gleitzeit, bis zu 2 Tage Homeoffice pro Woche.",
             "Betriebliche Altersversorgung (12 % AG-Anteil) und Lebensversicherung.",
             "Strukturiertes Onboarding-Programm und individuelles Weiterbildungsbudget (3.500 EUR p. a.).",
         ])),
        ("Kontakt",
         "Bewerbungen bitte mit Angabe des frueh"
         "estmoeglichen Eintrittstermins und der Gehaltsvorstellung per E-Mail an bewerbung@halbreiter-maschinenbau.de, "
         "z. Hd. Frau Andrea Hoffmann (Leiterin Personal). Bewerbungsfrist: 31. Maerz 2024. Datenschutzhinweise "
         "Art. 13 DSGVO sind unter halbreiter-maschinenbau.de/karriere abrufbar."),
    ],
)


# ─── HR_Betriebsratswahl_2023_Protokoll ─────────────────────────────────────
write_doc(
    f"{BASE}/HR_Betriebsratswahl_2023_Protokoll.docx", H,
    "Protokoll der Betriebsratswahl 2023",
    subtitle="Wahltag: 9. Mai 2023 – Wahlleiter: Herr Klaus Bauer",
    sections=[
        ("Wahlausschuss",
         "Der Wahlvorstand wurde am 27. Februar 2023 durch den amtierenden Betriebsrat bestellt und besteht aus "
         "Herrn Klaus Bauer (Vorsitzender), Frau Anette Klein (Schriftfuehrerin) und Herrn Mirko Hentschel (Beisitzer). "
         "Die Wahlordnung wurde gemaess §§ 1 ff. WO zum BetrVG eingehalten. Wahlausschreiben am 13. Maerz 2023 "
         "ausgehangen."),
        ("Stimmberechtigte und Beteiligung",
         "Stimmberechtigte: 247 (alle Beschaeftigten mit Stand 1. Mai 2023). Abgegebene Stimmen: 218 "
         "(Wahlbeteiligung 88,3 %; Vorperiode 84,1 %). Ungueltige Stimmen: 4. Gueltige Stimmen: 214."),
        ("Wahlergebnis",
         [
             ["Liste / Person", "Stimmen", "Anteil", "Mandat"],
             ["Liste 1 »Gemeinsam stark« (5 KandidatInnen)", "132", "61,7 %", "5 Sitze (Hare-Niemeyer)"],
             ["Liste 2 »Frischer Wind« (3 KandidatInnen)", "62", "29,0 %", "2 Sitze"],
             ["Liste 3 »Verwaltung« (2 KandidatInnen)", "20", "9,3 %", "1 Sitz"],
             ["", "SUMME", "100,0 %", "8 Sitze"],
         ]),
        ("Gewaehlte Betriebsratsmitglieder",
         ("list", [
             "Wolfgang Brettschneider (Liste 1) – Vorsitzender",
             "Beate Mayer (Liste 1) – stellv. Vorsitzende, Freistellung 50 %",
             "Markus Reinhardt (Liste 1)",
             "Anja Schwarzbach (Liste 1)",
             "Heiko Lebert (Liste 1)",
             "Ralf Bergstroem (Liste 2)",
             "Tatjana Wagenfeld (Liste 2)",
             "Marlene Kasparek (Liste 3)",
         ])),
        ("Konstituierende Sitzung",
         "Die konstituierende Sitzung fand am 16. Mai 2023 statt. Es wurden gewaehlt: Vorsitzender Wolfgang "
         "Brettschneider (8 von 8 Stimmen), stellv. Vorsitzende Beate Mayer (7/8). Die Ausschuesse "
         "(Personalausschuss, Sozialausschuss, Arbeitsschutzausschuss) wurden besetzt. Erste Sitzung mit der "
         "Geschaeftsfuehrung: 23. Mai 2023."),
        ("Unterschriften",
         signatures("Klaus Bauer", "Wahlleiter", M["name"],
                    "Anette Klein", "Schriftfuehrerin Wahlvorstand", M["name"],
                    place="Koeln", date_str_="9. Mai 2023")),
    ],
)


# ─── HR_Pensionszusage_Klaus_Mueller ────────────────────────────────────────
write_doc(
    f"{BASE}/HR_Pensionszusage_Klaus_Mueller.docx", H,
    "Pensionszusage Geschaeftsfuehrer – Klaus Mueller (Direktzusage)",
    subtitle="Versorgungszusage gemaess BetrAVG i. d. F. vom 12. Dezember 2017",
    sections=[
        ("Zusageempfaenger",
         "Herr Klaus Mueller, geboren am 12. Februar 1963, Geschaeftsfuehrer der Halbreiter Maschinenbau GmbH "
         "seit Gruendung der Gesellschaft am 14. Maerz 1985. Versorgungszusage in der vorliegenden Fassung "
         "(zuletzt geaendert mit Wirkung 1.1.2018 nach Anhebung der Bemessungsgrundlage)."),
        ("Versorgungsleistungen",
         ("clauses", [
             ("§ 1 Altersrente", [
                 "Mit Vollendung des 65. Lebensjahres oder bei Inanspruchnahme einer vorgezogenen "
                 "Altersrente aus der gesetzlichen Rentenversicherung hat Herr Mueller Anspruch auf "
                 "eine lebenslange monatliche Altersrente.",
                 "Hoehe der Altersrente: 12.500 EUR monatlich (150.000 EUR p. a.).",
                 "Die Rente steigt jaehrlich nach § 16 BetrAVG um 1,0 % (Mindestanpassung).",
             ]),
             ("§ 2 Invaliditaetsrente", [
                 "Bei Berufs- oder Erwerbsunfaehigkeit vor Vollendung des 65. Lebensjahres wird die "
                 "Altersrente in voller Hoehe vorzeitig gewaehrt.",
             ]),
             ("§ 3 Witwen- / Hinterbliebenenrente", [
                 "Frau Elke Mueller-Hartmann (Ehefrau) erhaelt im Versorgungsfall 60 % der vorgenannten "
                 "Altersrente als Hinterbliebenenrente.",
                 "Kinderzuschuss: 10 % der Altersrente je Kind, max. fuer zwei Kinder, bis zur Vollendung "
                 "des 18. Lebensjahres (bzw. 25. Lebensjahres bei Ausbildung).",
             ]),
         ])),
        ("Finanzierung und Bilanzierung",
         "Die Versorgungszusage wird im Wege der unmittelbaren Direktzusage (innerbetrieblicher Durchfuehrungsweg) "
         "erteilt. Die Pensionsrueckstellung wird gemaess § 6a EStG (Steuerbilanz) und § 253 Abs. 2 HGB "
         "(Handelsbilanz) bewertet; versicherungsmathematisches Gutachten durch Heubeck AG, Koeln. Stand "
         "31.12.2023: 1.420 TEUR (Steuerbilanz), 1.522 TEUR (Handelsbilanz). Eine Rueckdeckungsversicherung "
         "bei der Allianz Lebensversicherung AG ueber 1,8 Mio. EUR sichert das Anwartschaftsrecht ab; die "
         "Anspruechse hieraus sind an Herrn Mueller verpfaendet."),
        ("Insolvenzsicherung",
         "Beitragspflicht gegenueber dem Pensions-Sicherungs-Verein a. G. (PSVaG) wird quartalsweise erfuellt; "
         "Beitragsmeldung erfolgt ueber den DATEV-Mandanten der Gesellschaft."),
        ("Unterschriften",
         signatures("Klaus Mueller", "Versorgungsempfaenger", M["name"],
                    "Sandra Becker", "Geschaeftsfuehrerin / CFO (Versorgungstraeger)", M["name"],
                    place="Koeln", date_str_="12. Dezember 2017")),
    ],
)


# ─── HR_Stellenausschreibung_Produktionsleiter ──────────────────────────────
write_doc(
    f"{BASE}/HR_Stellenausschreibung_Produktionsleiter.docx", H,
    "Stellenausschreibung – Produktionsleiter:in Halle B / Pressen & Laser (m/w/d)",
    subtitle="Standort Koeln – Vollzeit – Veroeffentlichung 5. Maerz 2024",
    sections=[
        ("Ueber uns",
         "Die Halbreiter Maschinenbau GmbH ist ein etablierter mittelstaendischer Sondermaschinenbauer mit Sitz "
         "in Koeln, 247 Beschaeftigten und einem Jahresumsatz von ueber 48 Mio. EUR. Wir entwickeln und fertigen "
         "in eigener Produktion hochpraezise Pressen, Laserschneidanlagen, Foerderbaender und Robotik-Zellen "
         "fuer fuehrende Industriekunden in DACH und ausgewaehlten Auslandsmaerkten."),
        ("Ihr Aufgabengebiet",
         ("list", [
             "Operative Leitung der Halle B mit 42 Mitarbeitenden im 3-Schicht-Betrieb (Pressenmontage, "
             "Laserschneidanlagen, Endabnahme).",
             "Verantwortung fuer KPI: OEE (Ziel ≥ 78 %), Liefertreue (Ziel ≥ 95 %), Reklamationsquote "
             "(Ziel < 0,7 %).",
             "Schichtplanung in Abstimmung mit Vertrieb / Logistik; Kapazitaetssteuerung in SAP S/4HANA "
             "und MES (Roll-out in Implementation).",
             "Kontinuierliche Verbesserung gemaess Lean-Methoden (SMED, 5S, KVP), Mitwirkung an Industrie-4.0-Projekten.",
             "Disziplinarische Fuehrung zweier Vorarbeiter:innen sowie Mitarbeit im Produktionsleiterkreis "
             "(Halle A/B/C gemeinsam).",
         ])),
        ("Ihr Profil",
         ("list", [
             "Abgeschlossenes Studium Maschinenbau / Wirtschaftsingenieurwesen oder Meisterabschluss mit "
             "mehrjaehriger Fuehrungserfahrung im Pressenbau.",
             "5+ Jahre Fuehrungserfahrung im Schichtbetrieb; nachweisbare Erfolge in OEE-Verbesserung.",
             "Erfahrung mit SAP PP und MES-Loesungen; idealerweise Lean Six Sigma Black Belt.",
             "Hohe Hands-on-Mentalitaet, Durchsetzungsstaerke und sehr gute Kommunikationsfaehigkeit.",
             "Gute Englischkenntnisse fuer den Austausch mit auslaendischen Niederlassungen unserer Kunden.",
         ])),
        ("Konditionen",
         "Vergutung gemaess AT-Tarif M+E NRW (Bandbreite 82.000 - 105.000 EUR plus 15-25 % Bonus). "
         "Dienstwagen, 30 Urlaubstage, betriebliche Altersversorgung. Berichtsweg direkt an die Geschaeftsfuehrung "
         "(Klaus Mueller / Sandra Becker)."),
        ("Bewerbung",
         "Online-Bewerbung ueber unser Karriereportal halbreiter-maschinenbau.de/karriere oder per E-Mail an "
         "bewerbung@halbreiter-maschinenbau.de, Kennwort »PL-HalleB-2024«, z. Hd. Frau Andrea Hoffmann. Eingangs"
         "bestaetigung erfolgt automatisch; erstes Gespraech ca. 14 Tage nach Bewerbungseingang."),
    ],
)


# ─── HR_Fluktuationsanalyse_2023 ────────────────────────────────────────────
write_doc(
    f"{BASE}/HR_Fluktuationsanalyse_2023.docx", H,
    "Fluktuationsanalyse 2023",
    subtitle="Auswertung HR-Controlling, Stand 31. Januar 2024",
    sections=[
        ("Gesamtbild",
         "Im Geschaeftsjahr 2023 hat die Gesellschaft ihren Personalbestand von 231 (31.12.2022) auf 247 "
         "(31.12.2023) erhoeht. Im selben Zeitraum haben 18 Mitarbeitende das Unternehmen verlassen (8 davon "
         "aus dem Bereich Produktion, 6 kaufmaennisch / Vertrieb, 4 F&E / Service); 34 wurden neu eingestellt. "
         "Brutto-Fluktuationsrate: 7,3 % (Vorjahr 8,1 %). Netto-Fluktuationsrate (ohne altersbedingte "
         "Abgaenge): 5,2 %."),
        ("Aufschluesselung Austrittsgruende",
         [
             ["Grund", "2023", "2022", "Trend"],
             ["Eigenkuendigung", "11", "13", "↓"],
             ["Aufhebungsvertrag", "2", "1", "↑"],
             ["Renteneintritt / ATZ Ende", "3", "4", "↓"],
             ["Befristung ausgelaufen", "1", "2", "↓"],
             ["Sonstiges (Krankheit, Tod, etc.)", "1", "0", "↑"],
             ["SUMME", "18", "20", "↓"],
         ]),
        ("Schwerpunkte / Risiken",
         "1. Bereich Konstruktion / F&E: Wettbewerb um Senior Ingenieur:innen verschaerft. Drei Eigen"
         "kuendigungen 2023; alle drei zu Konkurrenten oder Beratungen mit hoeheren Festgehaltsangeboten. "
         "Massnahmen: AT-Gehaltsanpassung 7 % (per 1.4.2024) sowie Einfuehrung Sabbatical-Modell.\n\n"
         "2. Schichtarbeitende: hohe Fluktuation der Nachtschicht (Halle B); Massnahme: Wechsel-Bonus 250 EUR "
         "monatlich, Schichtwechsel kuerzere Zyklen (Vorschlag Betriebsrat).\n\n"
         "3. Vertrieb: zwei Key-Account-Manager:innen verlassen das Unternehmen Richtung OEM-Industriekunden; "
         "Massnahmen: Nachfolge intern (HR_009 Jan Mueller, HR_007 Markus Fischer) bereits etabliert."),
        ("Verweildauer",
         "Durchschnittliche Betriebszugehoerigkeit zum 31.12.2023: 11,4 Jahre (Vorjahr 11,2 Jahre). "
         "Median: 9,5 Jahre. 38 % der Belegschaft sind > 15 Jahre im Unternehmen."),
        ("Empfehlungen",
         "(a) Fuehrungskraefteentwicklungsprogramm »MMB Lead 2024« startet im Q3/2024. "
         "(b) Mitarbeitendenbefragung im Q2/2024 (zuletzt 2021). "
         "(c) Erweiterung der Praemienmodelle in Halle B."),
    ],
)


# ─── HR_Arbeitszeugnis_Thomas_Schneider ─────────────────────────────────────
write_doc(
    f"{BASE}/HR_Arbeitszeugnis_Thomas_Schneider.docx", H,
    "Qualifiziertes Zwischenzeugnis – Herr Thomas Schneider",
    subtitle="Ausgestellt am 12. Februar 2024",
    sections=[
        ("Persoenliche Angaben",
         "Herr Thomas Schneider, geboren am 14. Maerz 1981, ist seit dem 1. April 2014 als Vorarbeiter "
         "Montage Pressenlinie in unserem Unternehmen taetig."),
        ("Unternehmensportrait",
         "Die Halbreiter Maschinenbau GmbH ist ein etablierter mittelstaendischer Sondermaschinenbauer "
         "mit 247 Mitarbeitenden und einem Jahresumsatz von ueber 48 Mio. EUR. Wir entwickeln, fertigen "
         "und liefern hydraulische Pressen, Laserschneidanlagen, Foerderbandanlagen und Robotik-Zellen "
         "fuer fuehrende Industriekunden in DACH und ausgewaehlten Exportmaerkten."),
        ("Aufgabengebiet",
         "Im Rahmen seiner Taetigkeit verantwortet Herr Schneider die operative Fuehrung von 8 Monteuren "
         "im 2-Schicht-Betrieb der Halle B. Sein Aufgabengebiet umfasst insbesondere:\n\n"
         "- die Planung und Steuerung der Montagereihenfolge fuer die Pressenlinie PL-500;\n\n"
         "- die fachliche Anleitung und Qualifizierung der Monteure (inkl. Anlernen von Auszubildenden);\n\n"
         "- die Sicherstellung der Einhaltung von Qualitaets-, Arbeitsschutz- und Umweltvorgaben "
         "(ISO 9001, EnMS DIN EN ISO 50001);\n\n"
         "- die Erstellung und Pflege der Montagedokumentation in SAP PP sowie die Mitwirkung an "
         "Reklamations- / 8D-Analysen.\n\n"
         "Im Berichtszeitraum war Herr Schneider zudem als Teammitglied im Investitionsprojekt "
         "»Halle B Modernisierung« sowie im Rollout des MES-Pilotsystems eingebunden."),
        ("Leistungsbeurteilung",
         "Herr Schneider hat die ihm uebertragenen Aufgaben stets zu unserer vollsten Zufriedenheit erledigt "
         "(Notenstufe »sehr gut«). Er zeichnet sich durch ein ueberdurchschnittlich hohes Mass an Engagement, "
         "Sorgfalt und Eigeninitiative aus. Sein technisches Fachwissen im Pressenbau ist hervorragend; "
         "neue Verfahren und Werkzeuge eignet er sich schnell und nachhaltig an. Seine Fuehrungskompetenz "
         "innerhalb des Teams ist anerkannt; er versteht es, Mitarbeitende mit klarer, ruhiger und "
         "respektvoller Art zu motivieren."),
        ("Sozialverhalten",
         "Im Umgang mit Vorgesetzten, Kolleg:innen, Kund:innen und Lieferant:innen ist Herr Schneider stets "
         "freundlich, verbindlich und loesungsorientiert. Sein Verhalten ist vorbildlich."),
        ("Anlass und Schlussformel",
         "Dieses Zwischenzeugnis wird ausschliesslich auf Wunsch von Herrn Schneider ausgestellt, um seine "
         "berufliche Entwicklung zu dokumentieren. Wir wuenschen Herrn Schneider fuer seine berufliche "
         "Zukunft – wir hoffen, weiterhin in unserem Hause – weiterhin viel Erfolg."),
        ("Unterschrift",
         "Koeln, den 12. Februar 2024\n\n"
         "_________________________\n"
         "Andrea Hoffmann, Leiterin Personal & Verwaltung\n"
         "Halbreiter Maschinenbau GmbH"),
    ],
)


# ─── HR_Gehaltsrunde_2024_Protokoll ────────────────────────────────────────
write_doc(
    f"{BASE}/HR_Gehaltsrunde_2024_Protoko.docx", H,
    "Protokoll – Tariferhoehung und AT-Gehaltsrunde 2024",
    subtitle="Sitzung mit Betriebsrat und Personalausschuss am 14. Februar 2024",
    sections=[
        ("Tarifrunde Metall-Elektro NRW",
         "Der Tarifabschluss IG Metall / NRW vom 18. November 2023 sieht in den Geltungsbereich der "
         "Halbreiter Maschinenbau GmbH folgende Erhoehungen vor: 5,2 % zum 1. Mai 2024, weitere 3,3 % zum 1. April "
         "2025. Zusaetzlich: Tarifliche Sonderzahlung 1.500 EUR (Inflationsausgleich) auszahlbar mit der "
         "Maerz-Abrechnung 2024 fuer alle tarifgebundenen Vollzeit-Beschaeftigten (anteilig fuer Teilzeit)."),
        ("AT-Erhoehung",
         "Die Geschaeftsfuehrung hat in Abstimmung mit dem Personalausschuss und mit der zustaendigen Vertretung "
         "der AT-Beschaeftigten festgelegt: AT-Erhoehung in zwei Stufen: 4,0 % zum 1. April 2024, weitere "
         "2,5 % zum 1. Januar 2025. Inflationsausgleichs-Pauschale 1.500 EUR (analog tariflich)."),
        ("Gesamtkostenwirkung",
         [
             ["Bereich", "MA-Anzahl", "Erhoehung 2024", "Mehrkosten p. a. EUR"],
             ["Tarif (Produktion)", "168", "5,2 % + 1.500 EUR", "812.000"],
             ["Tarif (Kfm./Service)", "62", "5,2 % + 1.500 EUR", "298.000"],
             ["AT (Manager / Vertrieb / F&E)", "17", "4,0 %", "118.000"],
             ["", "SUMME", "", "1.228.000"],
         ]),
        ("Auswirkung auf Planung 2024",
         "Personalaufwand 2024 (Plan) steigt von 14,12 Mio. EUR auf 15,35 Mio. EUR. EBITDA-Marge unter "
         "Beruecksichtigung der Tariferhoehung wird auf ca. 11,9 % geplant (Vorjahr 12,3 %). Massnahmen zur "
         "Kompensation: Produktivitaetssteigerung +2 % durch MES-Pilot, Preisanpassungen im Neuauftrags-"
         "geschaeft +3,5 %."),
        ("Betriebsratsbeteiligung",
         "Der Betriebsrat hat der Umsetzung der Tariferhoehung sowie der AT-Anpassung zugestimmt (Sitzung "
         "14.2.2024, einstimmig). Eine Information der Belegschaft erfolgt ueber die Lohnabrechnung "
         "Maerz 2024 sowie ueber den internen Newsletter »MMB intern« Ausgabe 02/2024."),
        ("Unterschriften",
         signatures("Sandra Becker", "Geschaeftsfuehrerin / CFO", M["name"],
                    "Wolfgang Brettschneider", "Betriebsratsvorsitzender", M["name"],
                    place="Koeln", date_str_="14. Februar 2024")),
    ],
)


# ─── Einstellungsprotokoll_Ingenieur_FuE_2023 ───────────────────────────────
write_doc(
    f"{BASE}/Einstellungsprotokoll_Ingenieur_FuE_2023.docx", H,
    "Einstellungsprotokoll – Senior Entwicklungsingenieur, Herr Felix Engelhardt",
    subtitle="Vorgang HR-2023-EIN-014",
    sections=[
        ("Bewerber",
         "Herr Felix Engelhardt, geboren 22. Juli 1985 in Stuttgart, Abschluss Dipl.-Ing. Maschinenbau "
         "(TU Stuttgart, 2010), zuletzt taetig bei der Trumpf SE + Co. KG als Senior Steuerungsingenieur "
         "(2017-2023)."),
        ("Stelle",
         "Position: Senior Entwicklungsingenieur Pressen-/Steuerungstechnik (m/w/d). Bereich Konstruktion / F&E. "
         "Berichtsweg an Herrn Michael Weber (Senior Konstruktionsingenieur, kommissarisch Leiter F&E)."),
        ("Auswahlverfahren",
         "Stellenausschreibung am 14. Juli 2023 (Karriereportal, LinkedIn, Stepstone). Bewerbungseingaenge: "
         "38 (davon 19 vollstaendig). 6 KandidatInnen zum ersten Gespraech eingeladen, 3 zum zweiten "
         "Gespraech. Auswahl im Konsens von Andrea Hoffmann (Personalleitung), Michael Weber (Fach) und "
         "Klaus Mueller (Geschaeftsfuehrung)."),
        ("Bewertung",
         [
             ["Kriterium", "Gewichtung", "Bewertung (1-5)", "Anmerkung"],
             ["Fachliche Eignung Steuerungstechnik", "30 %", "5", "Tiefes Wissen Siemens SINUMERIK"],
             ["Erfahrung Pressen / Servo-Antriebe", "20 %", "5", "8 Jahre einschlaegig"],
             ["Persoenlichkeit / Team-Fit", "20 %", "4", "Ruhig, strukturiert, kollegial"],
             ["Englisch / Internationale Erfahrung", "10 %", "4", "Verhandlungssicher, USA-Erfahrung"],
             ["Lean / KVP / Innovation", "10 %", "4", "Trumpf-Projekt »LEAN+«"],
             ["Verfuegbarkeit / Eintrittstermin", "10 %", "5", "1. November 2023"],
         ]),
        ("Vertragsangebot",
         "Jahresbruttogehalt: 95.000 EUR (AT, Bandobere Grenze), Bonus bis 15 %, Dienstwagen "
         "Mercedes-Benz C-Klasse Hybrid (Elektrisches Fahren bevorzugt), 30 Urlaubstage, "
         "Mobiles Arbeiten gemaess BV HR_012 (bis 2 Tage Woche). Antrittsbonus: 6.500 EUR brutto "
         "(zu zahlen mit der Dezember-Abrechnung 2023, Ratenrueckforderung bei Eigenkuendigung im "
         "ersten Jahr)."),
        ("Genehmigung",
         "Einstellung genehmigt durch GF am 18. September 2023. Vertrag unterzeichnet am 25. September 2023; "
         "Eintrittstermin 1. November 2023. Onboarding-Plan und Mentor (Michael Weber) im Q4/2023 in Vorbereitung."),
        ("Unterschriften",
         signatures("Andrea Hoffmann", "Leiterin Personal", M["name"],
                    "Michael Weber", "Senior Konstruktionsingenieur (Fach)", M["name"],
                    place="Koeln", date_str_="18. September 2023")),
    ],
)


# ─── HR_Entgeltrahmentarifvertrag_ERA ──────────────────────────────────────
write_doc(
    f"{BASE}/HR_Entgeltrahmentarifvertrag_ERA.docx", H,
    "Entgeltrahmentarifvertrag (ERA) – Anwendung in der Halbreiter Maschinenbau GmbH",
    subtitle="Hinweis-/Anwendungsdokument fuer Personalabteilung, Stand 1. Januar 2024",
    sections=[
        ("Geltung",
         "Die Halbreiter Maschinenbau GmbH wendet den Entgeltrahmentarifvertrag (ERA) der Metall- und Elektro"
         "industrie Nordrhein-Westfalen i. d. F. vom 20. September 2003 (zuletzt aktualisiert 18. November "
         "2023) auf alle tariflich beschaeftigten Mitarbeitenden in Vollzeit oder Teilzeit an. Tarifbindung "
         "besteht durch Mitgliedschaft im METALL NRW (Verband der Metall- und Elektroindustrie NRW e.V.)."),
        ("Entgeltgruppen-Uebersicht (gekuerzt)",
         [
             ["EG", "Beschreibung typ. Taetigkeit", "Monatsgrundentgelt 2024 (EUR)", "Beispiel MMB"],
             ["EG 1", "Ungelernte einfache Hilfsarbeiten", "2.612,00", "Saisonale Aushilfen"],
             ["EG 4", "Angelernte Taetigkeit mit Einarbeitung", "3.008,00", "Lagerist:innen"],
             ["EG 7", "Facharbeiter:in 3-jaehrige Ausbildung", "3.612,00", "Sachbearbeitung Vertrieb"],
             ["EG 9", "Facharbeiter:in mit Zusatzqualifikation", "4.012,00", "Vorarbeiter Montage / Lohnbuch."],
             ["EG 10", "Erweiterte Spezialaufgabe", "4.310,00", "Bilanzbuchhalterin / Servicetechnik"],
             ["EG 12", "Selbstaendige Spezialaufgabe", "4.918,00", "Senior Konstrukteur:in"],
             ["EG 14", "Hochqualifiziert / Personalverantwortung", "5.892,00", "Senior Ingenieur F&E"],
             ["AT", "Ausser tariflich (Manager / Spezialist:innen)", "n. V.", "GF-Naehe / Strategische Funktionen"],
         ]),
        ("Leistungs- und Belastungszulagen",
         "ERA sieht zusaetzliche Leistungs- und Belastungszulagen vor: (a) Leistungszulage individuell, "
         "Bandbreite 0-25 % der Grundentgelte, bewertet nach 4 Kriterien (Arbeitsausfuehrung, Arbeitsweise, "
         "Vielseitigkeit/Selbstaendigkeit, Zusammenarbeit) – jaehrliche Beurteilung; (b) Belastungszulagen "
         "bei besonders erschwerten Bedingungen (Hitze, Schmutz, Schwerlast).\n\n"
         "Bei der Halbreiter Maschinenbau GmbH wurden 2023 durchschnittlich Leistungszulagen in Hoehe von "
         "12,4 % der Grundentgelte ausgezahlt; Belastungszulagen wurden in Halle A (Pressen-Schwerlast) "
         "und im Lager (Stapler-Schichten) gewaehrt."),
        ("Sonderzahlungen",
         "Urlaubsgeld: 50 % eines Monatsentgelts (Auszahlung Juni). Jahresleistung (Weihnachtsgeld): "
         "55 % eines Monatsentgelts (Auszahlung November), gestaffelt nach Betriebszugehoerigkeit. "
         "T-Zug A (tarifliches Zusatzgeld): 27,5 % eines Monatsentgelts (Wahl: 8 freie Tage statt Geld "
         "moeglich fuer bestimmte Berechtigte)."),
    ],
)


# ─── HR_Gehaltsstruktur_AT_Mitarbeiter_2024 ────────────────────────────────
write_doc(
    f"{BASE}/HR_Gehaltsstruktur_AT_Mitarbeiter_2024.docx", H,
    "AT-Gehaltsstruktur 2024 – Halbreiter Maschinenbau GmbH",
    subtitle="Strukturuebersicht der ausser-tariflichen Beschaeftigten, Stand 1. April 2024",
    sections=[
        ("Hinweis",
         "Diese Aufstellung dient der internen Steuerung der Vergutungs-Architektur fuer ausser-tarifliche "
         "(AT) Beschaeftigte (n=17). Ausgenommen ist die Geschaeftsfuehrung."),
        ("Vergutungsbaender 2024",
         [
             ["Band", "Funktion (Beispiele)", "Fixgehalt min. (EUR)", "Fixgehalt max. (EUR)", "Bonus-Range"],
             ["AT-1", "Spezialist:innen (Senior FuE / Senior Vertrieb / IT-Lead)", "78.000", "98.000", "10-15 %"],
             ["AT-2", "Senior Manager:innen (Bereichsleitung Produktion, Personal, Konstruktion)", "92.000", "118.000", "15-25 %"],
             ["AT-3", "Direktor:innen / 2. Fuehrungsebene", "118.000", "150.000", "20-30 %"],
         ]),
        ("Vergutungs-Mix",
         "Fix : Variabel = 80 : 20 (Standard). Bei Vertriebsfunktionen 70 : 30. Variable Komponente: 70 % "
         "Unternehmensziele (EBITDA-Erreichung), 30 % individuelle Ziele.\n\n"
         "Zusatzleistungen: Dienstwagen (auch privat); 30 Urlaubstage; betriebliche Altersversorgung (12 % "
         "Arbeitgeberanteil auf das Fixgehalt); Weiterbildungsbudget 3.500 EUR p. a.; subventionierte "
         "Kantine; JobRad."),
        ("Aktuelle Besetzung (anonymisiert)",
         [
             ["Band", "Anzahl Beschaeftigte", "Durchschn. Fixgehalt EUR", "Durchschn. Bonus 2023 EUR"],
             ["AT-1", "11", "88.300", "11.420"],
             ["AT-2", "5", "104.800", "21.620"],
             ["AT-3", "1", "138.000", "33.500"],
         ]),
        ("Governance",
         "Aenderungen der Vergutungsbaender beduerfen der Zustimmung der Geschaeftsfuehrung sowie der "
         "Information des Beirats. Eine externe Validierung erfolgt alle zwei Jahre durch Mercer "
         "(zuletzt: Mercer Total Compensation Survey, Februar 2024)."),
    ],
)


# ─── Zeugnis_Michael_Weber_Senior ───────────────────────────────────────────
write_doc(
    f"{BASE}/Zeugnis_Michael_Weber_Senior.docx", H,
    "Qualifiziertes Zwischenzeugnis – Herr Michael Weber",
    subtitle="Ausgestellt am 7. Maerz 2024",
    sections=[
        ("Persoenliche Angaben",
         "Herr Michael Weber, geboren am 5. Mai 1969, ist seit dem 1. Mai 1996 (rund 28 Jahre) als "
         "Konstruktionsingenieur in unserem Unternehmen taetig. Seit dem 1. Januar 2018 ist Herr Weber "
         "in der Funktion Senior Konstruktionsingenieur eingesetzt und kommissarisch Leiter F&E."),
        ("Unternehmensportrait",
         "Die Halbreiter Maschinenbau GmbH ist ein etablierter mittelstaendischer Sondermaschinenbauer mit "
         "Sitz in Koeln und Standortexpansion in Asien (Vertretungsbuero Suzhou). Mit 247 Mitarbeitenden "
         "und ueber 48 Mio. EUR Jahresumsatz beliefern wir fuehrende Industriekunden mit Pressen, "
         "Laserschneidanlagen, Foerderbandanlagen und Robotik-Loesungen."),
        ("Aufgabengebiet",
         "Herr Weber verantwortet ein Team von 7 Konstrukteur:innen und 2 Berechnungsingenieur:innen im "
         "Bereich Konstruktion / F&E. Sein Aufgabengebiet umfasst:\n\n"
         "(1) die konstruktive Auslegung und Detailgestaltung von Sondermaschinen einschliesslich der "
         "elektromechanischen und steuerungstechnischen Schnittstellen;\n\n"
         "(2) die Leitung der Produktreihe Pressenlinie PL-500 von der Konzeptphase bis zur Serienreife "
         "einschliesslich der CE-Konformitaetsbewertung;\n\n"
         "(3) Schnittstelle zu Vertrieb und Kunden bei kundenspezifischen Anpassungen "
         "(insb. ThyssenKrupp Steel Europe AG, Bosch Rexroth AG, Dürr AG);\n\n"
         "(4) Mitwirkung an der Forschungs-Roadmap »Pressen 4.0« sowie der Predictive-Maintenance-Plattform.\n\n"
         "Im Berichtszeitraum hat Herr Weber massgeblich zur Markteinfuehrung der Laserschneidanlage LS-800 "
         "5-Achs-Modul beigetragen (Inbetriebnahme Q2/2024 bei Hella GmbH & Co. KGaA)."),
        ("Leistungsbeurteilung",
         "Herr Weber hat die ihm uebertragenen Aufgaben stets zu unserer vollsten Zufriedenheit erledigt. "
         "Seine konstruktive Loesungskompetenz und sein in nahezu drei Jahrzehnten gewachsenes Erfahrungs"
         "wissen im Sondermaschinenbau sind herausragend. Er gestaltet komplexe technische Konzepte "
         "praezise, normgerecht und unter Beruecksichtigung wirtschaftlicher und fertigungstechnischer "
         "Aspekte. Auch unter terminlichem Druck arbeitet er strukturiert, qualitaetsorientiert und "
         "verlaesslich. Seine Fuehrungsqualitaet ist hoch geschaetzt; er versteht es, juengere "
         "Kolleg:innen mit Geduld und Substanz weiterzuentwickeln."),
        ("Sozialverhalten",
         "Im Umgang mit Vorgesetzten, Kolleg:innen, Kunden und Lieferanten zeigt Herr Weber stets ein "
         "verbindliches, ruhiges und kollegiales Auftreten. Sein Verhalten war jederzeit vorbildlich."),
        ("Schlussformel",
         "Dieses Zwischenzeugnis wird Herrn Weber zur Vorlage bei einem Stipendienprogramm der Hochschule "
         "Bochum (Lehrauftrag »Pressentechnik«, fuer den er sich beworben hat) ausgestellt. Wir wuenschen "
         "Herrn Weber persoenlich wie beruflich – wir hoffen, weiterhin in unserem Hause – viel Erfolg und "
         "alles Gute."),
        ("Unterschrift",
         "Koeln, den 7. Maerz 2024\n\n"
         "_________________________      _________________________\n"
         "Klaus Mueller, Geschaeftsfuehrer       Andrea Hoffmann, Leiterin Personal & Verwaltung"),
    ],
)


# ─── Betriebsrat_Sitzungsprotokoll_Q1_2024 ──────────────────────────────────
write_doc(
    f"{BASE}/Betriebsrat_Sitzungsprotokoll_Q1_2024.docx", H,
    "Sitzungsprotokoll Betriebsrat Q1/2024",
    subtitle="Sitzung 06/2024 vom 14. Maerz 2024, Konferenzraum »Mosel«",
    sections=[
        ("Teilnehmende",
         "Anwesend: Wolfgang Brettschneider (Vorsitzender), Beate Mayer (stellv. Vors.), Markus Reinhardt, "
         "Anja Schwarzbach, Heiko Lebert, Ralf Bergstroem, Tatjana Wagenfeld, Marlene Kasparek.\n\n"
         "Geladen / GF: Klaus Mueller (CEO), Sandra Becker (CFO), Andrea Hoffmann (HR-Leitung). "
         "Entschuldigt: keine. Protokoll: Beate Mayer."),
        ("Tagesordnung",
         ("list", [
             "TOP 1 Genehmigung Protokoll Sitzung 05/2024 vom 14.2.2024 (Gehaltsrunde) – einstimmig angenommen",
             "TOP 2 Bericht der Geschaeftsfuehrung zum Geschaeftsverlauf Q1/2024",
             "TOP 3 Beratung BV »Mobiles Arbeiten« – Erweiterung Pflegezeiten",
             "TOP 4 Schichtplan Halle B Sommer 2024 (Urlaubsblock)",
             "TOP 5 Stellenausschreibungen (Produktionsleitung Halle B, FuE-Ingenieur)",
             "TOP 6 Schulungsplan 2024 / Qualifizierungsoffensive »MMB Digital 2026«",
             "TOP 7 Mitarbeitendenbefragung Q2/2024 – Konzept und Vorgehen",
             "TOP 8 Verschiedenes",
         ])),
        ("Wesentliche Beschluesse",
         "Zu TOP 3: Der Betriebsrat stimmt der Erweiterung der BV HR_012 um die Pflege-Ausnahme zu. "
         "Mitarbeitende mit Pflegebelastung kommen befristet auf bis zu 4 Tage Homeoffice pro Woche.\n\n"
         "Zu TOP 4: Der Schichtplan Halle B Sommer 2024 (Urlaubsblock 2 Wochen Werksferien 5.-19. August) "
         "wird einstimmig genehmigt.\n\n"
         "Zu TOP 6: Schulungsplan wird genehmigt; zusaetzliche Schulungen zum Thema "
         "»Datenschutz im Serviceeinsatz« werden aufgenommen.\n\n"
         "Zu TOP 7: Mitarbeitendenbefragung wird durch Great Place to Work Deutschland GmbH unterstuetzt; "
         "Befragungsfenster 6.-31. Mai 2024; anonyme Auswertung; Ergebnispraesentation Juli 2024."),
        ("Aktionspunkte",
         [
             ["#", "Aktion", "Verantwortlich", "Termin"],
             ["1", "Aktualisierung BV HR_012 (Pflegeregelung)", "A. Hoffmann + W. Brettschneider", "31.3.2024"],
             ["2", "Roll-out Schulungsplan 2024 (Wave 1)", "A. Hoffmann", "30.4.2024"],
             ["3", "Mitarbeitendenbefragung – Briefing GPtW", "B. Mayer + A. Hoffmann", "15.4.2024"],
             ["4", "Stellenbesetzung Produktionsleiter:in Halle B", "A. Hoffmann", "31.5.2024"],
         ]),
        ("Naechste Sitzung",
         "Sitzung 07/2024 am Donnerstag, 11. April 2024, 13:30 Uhr, Konferenzraum »Mosel«."),
    ],
)


# ─── HR_Schulungsplan_2024 ─────────────────────────────────────────────────
write_doc(
    f"{BASE}/HR_Schulungsplan_2024.docx", H,
    "Schulungs- und Qualifizierungsplan 2024",
    subtitle="Genehmigt durch Geschaeftsfuehrung am 7. Februar 2024",
    sections=[
        ("Ueberblick",
         "Der Schulungsplan 2024 setzt vier strategische Schwerpunkte: (1) Digitale Kompetenzen "
         "(Industrie 4.0, MES, Datenanalytik); (2) Fuehrung und Zusammenarbeit; (3) Arbeitsschutz und "
         "Pflichtschulungen; (4) Fachkompetenzen (CE/MRL, Schweissen, CNC-Technik). Gesamtbudget 2024: "
         "320.000 EUR (Vorjahr 240.000 EUR), entspricht 2,1 % des Personalaufwands. Durchschnittliche "
         "Schulungstage je Beschaeftigte/n: 4,8 (Ziel 5,0)."),
        ("Schwerpunkte und Massnahmen",
         [
             ["Schwerpunkt", "Inhalt / Anbieter", "Zielgruppe", "Tage je TN", "Budget EUR"],
             ["Industrie 4.0 / MES-Roll-out", "interner Train-the-Trainer + ISTOS GmbH", "Produktion / Vorarbeitende", "2-3", "78.000"],
             ["Predictive Maintenance Datenanalyse", "Bosch Rexroth Academy (extern)", "Service Engineering", "5", "42.000"],
             ["Fuehrungskraefteentwicklung »MMB Lead«", "Personalentwicklung CRO Beratung", "AT-Manager:innen, Teamleads", "8", "98.000"],
             ["Pflichtschulungen Arbeitsschutz / DSGVO", "VdSI / interner DSB Dr. Lehmann", "alle MA", "0,5-1", "32.000"],
             ["CE-Kennzeichnung / Maschinenrichtlinie", "TUEV Rheinland", "Konstruktion / F&E", "2", "12.000"],
             ["CNC-Steuerungen SINUMERIK ONE", "Siemens Industry Academy", "Konstruktion / Service", "3", "26.000"],
             ["Schweissfachkraft DVS", "DVS Aachen", "Produktion Halle A", "10", "18.000"],
             ["Sprachen Englisch (B2)", "Berlitz", "Vertrieb, Service, F&E", "individuell", "14.000"],
         ]),
        ("Foerderprogramme",
         "Es werden Fortbildungszuschuesse der Bezirksregierung Koeln (»Bildungsscheck«) sowie der "
         "Bundesagentur fuer Arbeit (»WeGebAU«) genutzt, wo die Voraussetzungen erfuellt sind. Geplante "
         "Foerdersumme 2024: ca. 28.000 EUR; bisher bewilligt 12.500 EUR."),
        ("Verantwortlich",
         "Personalleitung (Andrea Hoffmann); Inhaltliche Abstimmung Bereiche (Klaus Bauer Logistik, Michael "
         "Weber F&E, Stefan Braun Einkauf, GF). Quartalsweises Reporting an Geschaeftsfuehrung und Betriebsrat."),
    ],
)


# ─── HR_Arbeitnehmererfindungsgesetz_Meldung_2021 ───────────────────────────
write_doc(
    f"{BASE}/HR_Arbeitnehmererfindungsgesetz_Meldung_2021.docx", H,
    "Erfindungsmeldung gemaess Arbeitnehmererfindungsgesetz (ArbnErfG)",
    subtitle="Meldenummer MMB-AEM-2021-007 vom 18. November 2021",
    sections=[
        ("Erfinder",
         "Herr Michael Weber (Senior Konstruktionsingenieur, Personal-Nr. 1003) sowie Herr Felix Engelhardt "
         "(zum Meldezeitpunkt noch Trumpf SE + Co. KG; spaeter Wechsel zu MMB; siehe Hinweis Section 5)."),
        ("Gegenstand der Erfindung",
         "Hydraulisches Schnellwechselsystem fuer Pressenwerkzeuge mit integrierter Werkstueck-Vermessung. "
         "Das System ermoeglicht den Werkzeugwechsel in unter 90 Sekunden (Stand der Technik > 6 Minuten) "
         "und kombiniert die Werkzeugaufnahme mit einer optischen Vermessung (Lasertriangulation), die das "
         "korrekte Positionieren mit Toleranz < 0,02 mm absichert. Die Erfindung soll in der Pressenlinie "
         "PL-500 (sowie deren Weiterentwicklung) integriert werden."),
        ("Inanspruchnahme",
         "Die Geschaeftsfuehrung erklaert mit Schreiben vom 21. November 2021 die unbeschraenkte "
         "Inanspruchnahme gemaess § 6 ArbnErfG. Es liegt ein Auslandsanmeldebeschluss (EU, USA, China) "
         "vor (Patentanwalt: Maiwald Patentanwaelte, Muenchen, Az. P2021-MMB-014)."),
        ("Verguetung",
         "Verguetung gemaess Richtlinien ArbnErfG (in Anlehnung an die Richtlinien fuer die Verguetung von "
         "Arbeitnehmererfindungen im privaten Dienst, »Vergutungsrichtlinien«). Berechnung erfolgt auf "
         "Basis der zu erwartenden Lizenzanalogie (geschaetzter Umsatz aus PL-500 5 Jahre, 4 % Lizenzsatz). "
         "Eine erste Vorabverguetung in Hoehe von 8.000 EUR wurde am 30. Januar 2022 zur Auszahlung "
         "freigegeben."),
        ("Hinweise",
         "Herr Felix Engelhardt war zum Meldungszeitpunkt nicht in der Halbreiter Maschinenbau GmbH "
         "beschaeftigt. Mit seinem Eintritt am 1. November 2023 wurde ein Mit-Erfinder-Status anteilig "
         "rueckwirkend zugesprochen (Mit-Erfinder-Anteil 40 %); eine Abrechnungskorrektur erfolgte mit "
         "Korrekturbeleg ABR-2023-MMB-AEM-007R im Dezember 2023."),
        ("Unterschriften",
         signatures("Michael Weber", "Erfinder", M["name"],
                    "Klaus Mueller", "Geschaeftsfuehrer", M["name"],
                    place="Koeln", date_str_="21. November 2021")),
    ],
)


# ─── HR_Altersstrukturanalyse_2024 ──────────────────────────────────────────
write_doc(
    f"{BASE}/HR_Altersstrukturanalyse_2024.docx", H,
    "Altersstrukturanalyse 2024",
    subtitle="HR-Controlling, Stand 1. Maerz 2024",
    sections=[
        ("Ausgangslage",
         "Mit 247 Beschaeftigten zum 31.12.2023 (Vorjahr 231) und einer durchschnittlichen Betriebs"
         "zugehoerigkeit von 11,4 Jahren ist die Belegschaft der Halbreiter Maschinenbau GmbH ueberdurch"
         "schnittlich erfahren, weist aber zugleich ein erhoehtes demografisches Risiko in den naechsten "
         "10 Jahren auf."),
        ("Altersstruktur",
         [
             ["Altersgruppe", "Anzahl", "Anteil", "Tendenz"],
             ["< 25 Jahre", "12", "4,9 %", "Auszubildende / Berufseinsteiger"],
             ["25-34 Jahre", "38", "15,4 %", "Junge Profis / Akquise-Schwerpunkt"],
             ["35-44 Jahre", "62", "25,1 %", "Tragender Kern operativ"],
             ["45-54 Jahre", "76", "30,8 %", "Senior Fachkraefte"],
             ["55-64 Jahre", "54", "21,9 %", "Wissenstraegerinnen"],
             ["65+", "5", "2,0 %", "Befristete Weiterbeschaeftigung"],
             ["", "247", "100,0 %", ""],
         ]),
        ("Renteneintritte Prognose",
         "In den naechsten 5 Jahren (2024-2028) gehen voraussichtlich 28 Beschaeftigte in den (Vor-)"
         "Ruhestand, davon: 6 in Schluesselfunktionen (Konstruktion 2, Produktion 3, Buchhaltung 1). "
         "In den naechsten 10 Jahren (2024-2033) summieren sich die Abgaenge auf 56 Beschaeftigte; ca. "
         "23 % der heutigen Belegschaft."),
        ("Massnahmen",
         "(a) Ausbildungsoffensive: Erhoehung der Ausbildungsplaetze in 2024 von 8 auf 12; Schwerpunkt "
         "Mechatroniker:in, Industriekauffrau/-mann, Fachinformatiker:in.\n\n"
         "(b) Nachfolgeplanung: Mentoring-Programm fuer alle Schluesselfunktionen ab Q3/2024; Pat:innen "
         "definiert.\n\n"
         "(c) Wissenstransfer / Job-Shadowing: Pro Schluesselfunktion 6-12 Monate Doppelbesetzung "
         "(Senior + Nachfolge) verankert.\n\n"
         "(d) Altersgerechtes Arbeiten: Erweiterung Langzeitkonten, Pruefung Gleitende-Uebergang-Modelle "
         "(Vorruhestand 50 %)."),
    ],
)


print("OK regen_mueller_03.py – 19 docs (10 Arbeitsvertraege + 9 weitere) written")
