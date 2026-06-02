"""Regenerate Müller / 01_Gesellschaftsrecht thin docs with rich content."""
# --- portable-paths-prelude --- (do not edit) ---
import sys
from pathlib import Path as _PathlibPath
_RP = _PathlibPath(__file__).resolve().parent
while not (_RP / "enhance_lib.py").exists() and _RP.parent != _RP:
    _RP = _RP.parent
_ROOT = _RP
sys.path.insert(0, str(_ROOT))
# --- end prelude ---
from enhance_lib import MUELLER as M, write_doc, ds, eur, num, signatures

BASE = f"{_ROOT}/mueller_small/01_Gesellschaftsrecht"
H = {"name": M["name"], "addr": M["addr"], "hrb": M["hrb"]}


# ── GR_Gesellschafterbeschluss_Digitalisierung ──────────────────────────────
write_doc(
    f"{BASE}/GR_Gesellschafterbeschluss_Digitalisierung.docx", H,
    "Gesellschafterbeschluss – Digitalisierungsoffensive 2024–2026",
    subtitle="Beschluss-Nr. 2024/03 vom 22. Februar 2024",
    sections=[
        ("Präambel",
         "Die Gesellschafter der Halbreiter Maschinenbau GmbH haben in der heutigen außerordentlichen Gesellschafterversammlung am Sitz der Gesellschaft, Industriestraße 12, 50829 Köln, einstimmig den nachfolgenden Beschluss zur Verabschiedung der Digitalisierungsoffensive 2024–2026 gefasst.\n\nDie Gesellschafter halten fest, dass das gesamte gezeichnete Stammkapital in Höhe von 250.000 EUR vertreten ist und sämtliche Förmlichkeiten der Einladung gemäß § 51 GmbHG sowie § 9 des Gesellschaftsvertrages vom 14. März 1985 (zuletzt geändert am 19. September 2019) gewahrt wurden. Auf die Einhaltung weiterer Förmlichkeiten wurde einvernehmlich verzichtet."),
        ("Tagesordnungspunkt 1 – Ausgangslage",
         "Die Geschäftsführung berichtet, dass die wettbewerbsfähige Fortentwicklung der Gesellschaft im Maschinen- und Anlagenbau eine umfassende Modernisierung der IT-Landschaft sowie der produktionsnahen digitalen Prozesse voraussetzt. Insbesondere die Anforderungen wichtiger Kunden (u. a. ThyssenKrupp Steel Europe AG, Bosch Rexroth AG, Hella GmbH & Co. KGaA, Viessmann Climate Solutions SE und Dürr AG) im Bereich digitaler Lieferanten-Onboardings, EDI-Anbindung und IoT-fähiger Maschinen erfordern absehbar erhebliche Investitionen.\n\nDie vorgelegte Roadmap des CFO Frau Sandra Becker sieht ein Gesamtvolumen von bis zu 3,8 Mio. EUR über drei Geschäftsjahre vor (2024: 1,4 Mio. EUR; 2025: 1,5 Mio. EUR; 2026: 0,9 Mio. EUR)."),
        ("Tagesordnungspunkt 2 – Maßnahmenpaket",
         ("list", [
            "MES-System (Manufacturing Execution System) zur Echtzeitsteuerung der Produktion; Anbieter wird im Q2/2024 nach Ausschreibung ausgewählt; Budget 850.000 EUR.",
            "Erweiterung SAP S/4HANA um die Module PP-PI und QM; Implementierung durch externen Partner; Budget 620.000 EUR.",
            "Predictive-Maintenance-Plattform für die Pressenlinie PL-500 und die Laserschneidanlage LS-800; Pilot bei Großkunde ThyssenKrupp Steel Europe AG; Budget 410.000 EUR.",
            "Cloud-Migration des CRM (Salesforce Sales Cloud Enterprise) sowie Aufbau eines Kunden-Self-Service-Portals; Budget 280.000 EUR.",
            "Cybersecurity-Programm gemaess BSI IT-Grundschutz und TISAX-Vorbereitung; Aufbau eines internen ISMS; Budget 540.000 EUR.",
            'Schulungs- und Change-Programm "MMB Digital 2026"; mind. 1,5 Tage je gewerblichem Mitarbeitenden pro Jahr; Budget 320.000 EUR.',
            'Aufbau einer dedizierten Stabsstelle "Digitalisierung & Daten" (1,0 FTE Lead + 2,0 FTE Spezialist:in) als direkte Berichtsachse an den CFO.',
         ])),
        ("Tagesordnungspunkt 3 – Finanzierung",
         "Die Finanzierung erfolgt aus dem operativen Cashflow sowie aus dem mit der Deutschen Bank AG, Filiale Köln, am 7. November 2023 geschlossenen Rahmenkreditvertrag (Tranche »Investitionslinie«, aktuell unbeansprucht 4,5 Mio. EUR). Eine Inanspruchnahme erfolgt nur, soweit der Zinsdeckungsgrad gemäß Covenant »ICR > 4,0x« gewahrt bleibt. Die Gesellschafter ermächtigen die Geschäftsführung, Kreditinanspruchnahmen bis 1,5 Mio. EUR ohne weiteren Zustimmungsvorbehalt vorzunehmen; darüber hinausgehende Inanspruchnahmen bedürfen eines gesonderten Gesellschafterbeschlusses."),
        ("Tagesordnungspunkt 4 – Beschluss",
         ("clauses", [
            ("§ 1 Genehmigung", [
                "Die Gesellschafter genehmigen das in Tagesordnungspunkt 2 dargestellte Maßnahmenpaket einstimmig und in vollem Umfang.",
                "Die Geschäftsführung wird beauftragt und ermächtigt, sämtliche zur Umsetzung erforderlichen Verträge zu verhandeln, abzuschließen und zu vollziehen.",
            ]),
            ("§ 2 Berichterstattung", [
                "Die Geschäftsführung berichtet den Gesellschaftern quartalsweise schriftlich über Fortschritt, Budgetauslastung, identifizierte Risiken sowie über realisierte Mehrwerte.",
                "Eine Zwischenbilanz erfolgt zum 31. Dezember 2024 sowie ein Abschlussbericht zum 31. März 2027.",
            ]),
            ("§ 3 Aufsichts- und Beiratsbefassung", [
                "Der Beirat ist zur jährlichen Sitzung im November 2024, 2025 und 2026 mit einem Statusbericht zu befassen.",
            ]),
         ])),
        ("Schlussfeststellung",
         "Der Vorsitzende der Versammlung, Herr Klaus Müller, stellt fest, dass der Beschluss einstimmig gefasst wurde. Es wurden keine Einwendungen gegen Form und Inhalt erhoben. Das Protokoll wird zu den Gesellschaftsakten genommen und ist Bestandteil des Beschlussbuchs."),
        ("Unterschriften",
         signatures(
            "Klaus Müller", "Gesellschafter (60 %)", "i. e. S.",
            "für Müller Familien-GbR", "Gesellschafter (40 %)", "vertreten durch Klaus Müller",
            place="Köln", date_str_="22. Februar 2024",
         )),
    ],
)


# ── GR_Datenschutz_Verantwortliche_Benennung ────────────────────────────────
write_doc(
    f"{BASE}/GR_Datenschutz_Verantwortliche_Benennung.docx", H,
    "Benennung eines Datenschutzbeauftragten (DSB) gemäß Art. 37 DSGVO i. V. m. § 38 BDSG",
    subtitle="Wirksam ab 1. April 2023",
    sections=[
        ("1. Verantwortlicher",
         "Verantwortlicher im Sinne des Art. 4 Nr. 7 DSGVO ist die Halbreiter Maschinenbau GmbH, Industriestraße 12, 50829 Köln, eingetragen im Handelsregister des Amtsgerichts Köln unter HRB 47312, vertreten durch die Geschäftsführer Herrn Klaus Müller (CEO) und Frau Sandra Becker (CFO).\n\nDie Gesellschaft beschäftigt zum Stichtag 31. März 2023 247 Mitarbeitende (Vollzeitäquivalente) und führt regelmäßig automatisierte Verarbeitungen personenbezogener Daten von Beschäftigten, Bewerbenden, Kund:innen, Lieferanten und Geschäftspartner:innen durch. Daneben werden im Rahmen der Predictive-Maintenance-Plattform sowie der Service-Disposition für die Produktreihen Pressenlinie PL-500, Förderbandanlage FB-200 und Laserschneidanlage LS-800 personenbezogene Servicedaten verarbeitet."),
        ("2. Bestellung",
         "Mit Wirkung zum 1. April 2023 wird zum Datenschutzbeauftragten der Halbreiter Maschinenbau GmbH bestellt:\n\nHerr RA Dr. Markus Lehmann, c/o Lehmann & Partner Datenschutzberatung GmbH, Hohenstaufenring 14, 50674 Köln.\n\nHerr Dr. Lehmann ist externer Datenschutzbeauftragter im Sinne des Art. 37 Abs. 6 DSGVO. Die Bestellung erfolgt für eine Mindestlaufzeit von 24 Monaten und verlängert sich automatisch um jeweils weitere 12 Monate, sofern nicht spätestens drei Monate vor Ablauf schriftlich gekündigt wird."),
        ("3. Aufgaben des DSB",
         "Dem Datenschutzbeauftragten obliegen insbesondere die Aufgaben gemäß Art. 39 DSGVO: Unterrichtung und Beratung der Geschäftsführung und der Beschäftigten zu deren datenschutzrechtlichen Pflichten; Überwachung der Einhaltung der DSGVO, des BDSG sowie der internen Datenschutzrichtlinien; Beratung im Hinblick auf die Datenschutz-Folgenabschätzung (Art. 35 DSGVO) und Überwachung ihrer Durchführung; Zusammenarbeit mit der zuständigen Aufsichtsbehörde (Landesbeauftragte für Datenschutz und Informationsfreiheit Nordrhein-Westfalen, Helga Block) sowie Tätigkeit als Anlaufstelle für Betroffene und Aufsichtsbehörden."),
        ("4. Stellung und Ressourcen",
         "Der Datenschutzbeauftragte wird ordnungsgemäß und frühzeitig in alle datenschutzrelevanten Fragen eingebunden. Er erstattet unmittelbar an die Geschäftsführung Bericht. Ihm wird Zugang zu allen erforderlichen Informationen, Verarbeitungstätigkeiten, Räumlichkeiten, Datenträgern und Anwendungen gewährt.\n\nFür die Erfüllung seiner Aufgaben wird ein jährliches Stundenkontingent von 240 Stunden vereinbart; darüber hinausgehender Aufwand wird nach Aufwand zu einem Stundensatz von 220 EUR (zzgl. USt.) abgerechnet. Im internen IT-Service-Desk wird ein eigenes Ticketsystem (»DSGVO-Anfragen«) implementiert."),
        ("5. Mitteilung an die Aufsichtsbehörde",
         "Die Geschäftsführung beauftragt die Personalabteilung (Frau Andrea Hoffmann), die Bestellung gemäß Art. 37 Abs. 7 DSGVO unverzüglich der zuständigen Aufsichtsbehörde (LDI NRW) sowie über das interne Mitarbeitendenportal allen Beschäftigten bekanntzugeben. Eine Veröffentlichung der Kontaktdaten erfolgt zudem im Impressum von www.halbreiter-maschinenbau.de."),
        ("6. Schlussbestimmungen",
         "Diese Benennung ersetzt die bisherige interne Beauftragung von Herrn Stefan Braun (Einkaufsleiter), der die Funktion seit 2018 in Doppelfunktion ausgeübt hat. Sie wurde dem Betriebsrat am 15. März 2023 zur Kenntnisnahme vorgelegt; Bedenken wurden nicht geäußert.\n\nKöln, den 28. März 2023."),
        ("Unterschriften",
         signatures("Klaus Müller", "Geschäftsführer (CEO)", M["name"],
                    "Sandra Becker", "Geschäftsführerin (CFO)", M["name"],
                    place="Köln", date_str_="28. März 2023")),
    ],
)


# ── GR_Handlungsvollmacht_Einkauf_Stefan_Braun ──────────────────────────────
write_doc(
    f"{BASE}/GR_Handlungsvollmacht_Einkauf_Stefan_Braun.docx", H,
    "Handlungsvollmacht für den Einkauf – Herr Stefan Braun",
    subtitle="Bevollmächtigung gemäß §§ 54 ff. HGB",
    sections=[
        ("1. Vollmachtgeberin",
         "Halbreiter Maschinenbau GmbH, Industriestraße 12, 50829 Köln, eingetragen im Handelsregister des Amtsgerichts Köln unter HRB 47312, vertreten durch die Geschäftsführer Klaus Müller und Sandra Becker (jeweils einzelvertretungsberechtigt).\n\nDie Vollmacht wird auf Beschluss der Geschäftsführung vom 12. Januar 2024 (Geschäftsleitungsprotokoll Nr. 2024/01-04) erteilt."),
        ("2. Bevollmächtigter",
         "Herr Stefan Braun, geboren am 6. Mai 1972, wohnhaft Bismarckstraße 47, 50672 Köln, im Betrieb der Vollmachtgeberin tätig als Leiter Strategischer Einkauf seit 1. Februar 2018."),
        ("3. Umfang der Vollmacht",
         ("clauses", [
            ("§ 1 Allgemeines", [
                "Dem Bevollmächtigten wird eine Handlungsvollmacht gemäß § 54 Abs. 1 HGB erteilt, die alle Geschäfte und Rechtshandlungen umfasst, die der Betrieb eines Handelsgewerbes der Vollmachtgeberin gewöhnlich mit sich bringt, insbesondere im Bereich des Einkaufs von Roh-, Hilfs- und Betriebsstoffen, Halbzeugen, Komponenten, Investitionsgütern und Dienstleistungen.",
                "Die Vollmacht berechtigt nicht zu Geschäften, die in § 54 Abs. 2 HGB genannt sind (Veräußerung oder Belastung von Grundstücken, Eingehung von Wechselverbindlichkeiten, Aufnahme von Darlehen, Prozessführung).",
            ]),
            ("§ 2 Betragsmäßige Grenzen", [
                "Einzelbestellungen bis zu einem Auftragsvolumen von 250.000 EUR (netto) je Bestellung dürfen ohne weitere Mitzeichnung getätigt werden.",
                "Bei Einzelbestellungen über 250.000 EUR bis 750.000 EUR ist die Mitzeichnung des CFO Frau Sandra Becker erforderlich.",
                "Über 750.000 EUR hinausgehende Einzelbestellungen bedürfen eines Beschlusses der Gesamtgeschäftsführung.",
                "Rahmenverträge unabhängig vom Jahresvolumen bedürfen stets der Gegenzeichnung durch die Geschäftsführung.",
            ]),
            ("§ 3 Lieferantenbeziehungen", [
                "Die Auswahl, Bewertung und Freigabe von Lieferanten erfolgt gemäß der internen Richtlinie LIEF-RL-001 in Verbindung mit dem Risikomanagement-Handbuch.",
                "Bei Lieferanten mit kritischer Einstufung (Schunk GmbH & Co. KG, Trumpf SE + Co. KG, Siemens AG – Antriebstechnik, Igus GmbH) ist die jährliche Auditierung sicherzustellen.",
            ]),
            ("§ 4 Compliance", [
                "Der Bevollmächtigte verpflichtet sich zur strikten Einhaltung der Compliance-Richtlinie der Gesellschaft, insbesondere der Antikorruptions-Richtlinie COMP-RL-004 sowie der Exportkontroll-Richtlinie COMP-RL-006.",
                "Geschenke und Zuwendungen sind nur im Rahmen der internen Geschenke-Richtlinie zulässig; jede Annahme oberhalb von 50 EUR ist meldepflichtig.",
            ]),
         ])),
        ("4. Eintragung ins Handelsregister",
         "Eine Eintragung als Prokurist gemäß § 48 HGB ist nicht vorgesehen. Eine Anmeldung der Handlungsvollmacht zum Handelsregister findet daher nicht statt; sie ist gleichwohl in der internen Vollmachtsdatenbank zu hinterlegen und im SAP-Bestellsystem hinterlegt (User-Rolle »MMB_EK_HV_250k«)."),
        ("5. Dauer und Widerruf",
         "Die Vollmacht gilt ab Unterzeichnung bis auf Widerruf. Der Widerruf kann jederzeit ohne Angabe von Gründen erfolgen und ist dem Bevollmächtigten schriftlich anzuzeigen; sie endet zudem automatisch mit Beendigung des Anstellungsverhältnisses."),
        ("Unterschriften",
         signatures("Klaus Müller", "Geschäftsführer (CEO)", M["name"],
                    "Sandra Becker", "Geschäftsführerin (CFO)", M["name"],
                    place="Köln", date_str_="15. Januar 2024")),
        ("Kenntnisnahme Bevollmächtigter",
         "Ich, Stefan Braun, habe vorstehende Handlungsvollmacht zur Kenntnis genommen und akzeptiere die darin geregelten Befugnisse und Beschränkungen.\n\nKöln, den 15. Januar 2024\n\n_________________________\nStefan Braun, Leiter Strategischer Einkauf"),
    ],
)


# ── GR_002_Gesellschafterliste_2024 ─────────────────────────────────────────
write_doc(
    f"{BASE}/GR_002_Gesellschafterliste_2024.docx", H,
    "Gesellschafterliste – Halbreiter Maschinenbau GmbH",
    subtitle="Stand: 15. Januar 2024 – Hinterlegung beim Handelsregister gemäß § 40 GmbHG",
    sections=[
        ("1. Gegenstand",
         "Diese Gesellschafterliste stellt den aktuellen Stand der Beteiligungsverhältnisse an der Halbreiter Maschinenbau GmbH (HRB 47312, Amtsgericht Köln) dar. Sie wurde erstellt durch die Geschäftsführer Klaus Müller und Sandra Becker und ersetzt die bislang im Handelsregister hinterlegte Liste vom 18. September 2019."),
        ("2. Stammkapital",
         "Das Stammkapital der Gesellschaft beträgt unverändert 250.000,00 EUR (in Worten: zweihundertfünfzigtausend Euro), aufgeteilt in 250 Geschäftsanteile zu je nominal 1.000,00 EUR. Die Stammeinlagen sind vollständig erbracht; eine Nachschusspflicht der Gesellschafter besteht nicht."),
        ("3. Gesellschafter",
         [
            ["Nr.", "Gesellschafter", "Anschrift", "Geschäftsanteile (Nr.)", "Nennbetrag", "Anteil"],
            ["1", "Klaus Müller, geb. 12.02.1963", "Lindenallee 14, 50935 Köln", "1–150", "150.000,00 EUR", "60,00 %"],
            ["2", "Müller Familien-GbR, vertreten durch Klaus Müller", "Lindenallee 14, 50935 Köln", "151–250", "100.000,00 EUR", "40,00 %"],
            ["", "Gesamt", "", "250 Anteile", "250.000,00 EUR", "100,00 %"],
         ]),
        ("4. Erwerbsketten",
         "Die Geschäftsanteile Nr. 1–150 wurden bei Gründung der Gesellschaft am 14. März 1985 von Herrn Klaus Müller übernommen (Gründungsurkunde des Notars Dr. Helmut Vogel, Köln, UR-Nr. 312/1985).\n\nDie Geschäftsanteile Nr. 151–250 wurden mit notarieller Anteilsabtretung vom 9. Juni 2014 (UR-Nr. 482/2014 des Notars Dr. Friedrich Wagner, Köln) von Herrn Klaus Müller an die Müller Familien-GbR übertragen und unentgeltlich im Wege vorweggenommener Erbfolge übergeben. Die Gesellschaft hat der Abtretung gemäß § 8 des Gesellschaftsvertrages zugestimmt (Gesellschafterbeschluss vom 4. Juni 2014)."),
        ("5. Belastungen",
         "Die Geschäftsanteile Nr. 1–80 sind zugunsten der Deutschen Bank AG verpfändet (Pfandvertrag vom 7. November 2023, im Rahmen der Investitionsfinanzierung über 4,5 Mio. EUR). Eine Eintragung des Pfandrechts erfolgt nicht; die Bank hat von ihrem Recht auf Eintragung verzichtet (siehe Anlage 2).\n\nWeitere Belastungen, insbesondere Treuhandverhältnisse, Unterbeteiligungen oder Vorkaufsrechte Dritter, bestehen nach Erklärung der Gesellschafter nicht."),
        ("6. Erklärung der Geschäftsführung",
         "Die unterzeichnenden Geschäftsführer versichern, dass diese Liste den aktuellen Beteiligungsverhältnissen entspricht und alle Veränderungen seit der zuletzt hinterlegten Liste berücksichtigt sind. Die Liste wird mit der Anmeldung der Veränderung im Hinblick auf die Anschriftenangaben (Aktualisierung 2024) gemäß § 40 Abs. 1 GmbHG eingereicht.\n\nKöln, den 15. Januar 2024."),
        ("Unterschriften",
         signatures("Klaus Müller", "Geschäftsführer", M["name"],
                    "Sandra Becker", "Geschäftsführerin", M["name"],
                    place="Köln", date_str_="15. Januar 2024")),
    ],
)


# ── GR_Vollmacht_Steuerberater ──────────────────────────────────────────────
write_doc(
    f"{BASE}/GR_Vollmacht_Steuerberater.docx", H,
    "Generalvollmacht in Steuerangelegenheiten – KPMG AG WPG",
    subtitle="Vollmacht gemäß §§ 80 ff. AO",
    sections=[
        ("1. Vollmachtgeberin",
         "Halbreiter Maschinenbau GmbH, Industriestraße 12, 50829 Köln, USt-IdNr.: DE 198 765 432, Steuernummer 215/5765/9876, Finanzamt Köln-Nord, vertreten durch die Geschäftsführer Klaus Müller (CEO) und Sandra Becker (CFO)."),
        ("2. Bevollmächtigte",
         "KPMG AG Wirtschaftsprüfungsgesellschaft, Standort Köln, Barbarossaplatz 1a, 50674 Köln, vertreten durch Partner Herrn StB Dr. Hendrik Vossberg sowie die mandatsführende Steuerberaterin Frau Dr. Carola Lindner."),
        ("3. Umfang der Vollmacht",
         "Die Bevollmächtigten werden ermächtigt, die Vollmachtgeberin in allen steuerlichen Angelegenheiten gegenüber Finanzbehörden, Finanzgerichten und sonstigen Behörden zu vertreten. Die Vollmacht umfasst insbesondere:\n\n– die Anfertigung und Einreichung sämtlicher Steuererklärungen (Körperschaftsteuer, Gewerbesteuer, Umsatzsteuer, Lohnsteuer, Kapitalertragsteuer, sonstige Steuern und Abgaben);\n\n– die Wahrnehmung von Anhörungs- und Auskunftsersuchen sowie Außenprüfungen (Betriebsprüfungen, Lohnsteuer- und Umsatzsteuersonderprüfungen);\n\n– die Einlegung und Begründung von Einsprüchen, Klagen und Anträgen auf Aussetzung der Vollziehung;\n\n– die Entgegennahme aller Steuerbescheide, Festsetzungs- und Prüfungsmitteilungen sowie sonstiger Verwaltungsakte;\n\n– die Korrespondenz mit der Finanzverwaltung in elektronischer Form über ELSTER (das Vollmachtsdatenbank-Verfahren der Bundessteuerberaterkammer ist mit der Übermittlung der Vollmachtsanzeige aktivierbar)."),
        ("4. Ausgenommene Befugnisse",
         "Nicht von dieser Vollmacht umfasst sind: der Verzicht auf Steueransprüche; die Abgabe von Selbstanzeigen gemäß § 371 AO ohne vorherige Rücksprache mit der Geschäftsführung; und die Aufnahme von Zahlungsverpflichtungen, die nicht aus rechtskräftigen Steuerbescheiden resultieren."),
        ("5. Geltungsdauer",
         "Die Vollmacht gilt ab Unterzeichnung und ersetzt sämtliche zuvor erteilten Vollmachten in steuerlichen Angelegenheiten. Sie ist jederzeit schriftlich widerruflich. Sie erlischt nicht durch den Tod der Vollmachtgeberin (§ 80 Abs. 1 S. 4 AO i. V. m. § 168 BGB)."),
        ("6. Anmeldung Vollmachtsdatenbank",
         "Die Bevollmächtigten sind berechtigt und beauftragt, diese Vollmacht in die Vollmachtsdatenbank der Bundessteuerberaterkammer einzustellen und die Übermittlung an die zuständige Finanzverwaltung über das amtlich bestimmte Verfahren zu veranlassen."),
        ("Unterschriften",
         signatures("Klaus Müller", "Geschäftsführer", M["name"],
                    "Sandra Becker", "Geschäftsführerin", M["name"],
                    place="Köln", date_str_="8. Januar 2024")),
    ],
)
print("OK regen_mueller_01.py (set A) – 5 docs written")
