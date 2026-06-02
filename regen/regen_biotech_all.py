"""Sentavia Precision GmbH – Sammelregeneration aller 57 Thin Docs."""
# --- portable-paths-prelude --- (do not edit) ---
import sys
from pathlib import Path as _PathlibPath
_RP = _PathlibPath(__file__).resolve().parent
while not (_RP / "enhance_lib.py").exists() and _RP.parent != _RP:
    _RP = _RP.parent
_ROOT = _RP
sys.path.insert(0, str(_ROOT))
# --- end prelude ---
from enhance_lib import BIOTECH as B, write_doc, signatures

BASE = f"{_ROOT}/biotech_medium"
H = {"name": B["name"], "addr": B["addr"], "hrb": B["hrb"]}


# ── 01_Gesellschaftsrecht: Board Resolutions (22) ──────────────────────────
def board_res(fname, datum, titel, ausgangslage, beschluss_text, abstimmung="einstimmig"):
    write_doc(f"{BASE}/01_Gesellschaftsrecht/{fname}", H,
        f"Beirats-/Gesellschafterbeschluss – {titel}",
        subtitle=f"Vorlage Sitzung vom {datum}; Beschlusserlass {datum}",
        sections=[
            ("Praeambel",
             f"Der Beirat der Sentavia Precision GmbH hat in der Sitzung vom {datum} unter Vorsitz der Beiratsvorsitzenden "
             "Frau Dr. Veronika Stankl den nachfolgenden Beschluss gefasst. Anwesend waren neben dem Vorsitz die "
             "Beiratsmitglieder Dr. Henrik Vossberg (Sofinnova Partners), Frau Ulrike Senn (Lakestar), "
             "Herr Prof. Dr. med. Joerg Lewerenz (CMO-Experte) sowie die Geschaeftsfuehrung "
             "(Dr. Katharina Berger CEO, Dr. Marcus Vogt CTO, Thomas Mueller CFO). "
             "Die Beschlussfaehigkeit war gegeben."),
            ("Ausgangslage", ausgangslage),
            ("Beschluss",
             ("clauses", [
                 ("§ 1 Beschlussfassung",
                  [beschluss_text,
                   f"Die Geschaeftsfuehrung wird ermaechtigt, alle zur Umsetzung erforderlichen Massnahmen zu treffen. "
                   "Die Information der Investoren erfolgt gemaess Shareholder Agreement vom 14. Februar 2020 binnen 10 Geschaeftstagen."]),
                 ("§ 2 Berichterstattung",
                  [f"Die Geschaeftsfuehrung berichtet dem Beirat zur naechsten ordentlichen Sitzung ueber den Umsetzungsstand. "
                   "Wesentliche Abweichungen sind unverzueglich anzuzeigen."]),
             ])),
            ("Abstimmungsergebnis",
             f"Abstimmung: {abstimmung}. Es wurden keine Einwendungen gegen Form und Inhalt erhoben. "
             "Das Protokoll wird dem Investoren-Reporting beigefuegt. Der Beschluss ist sofort wirksam."),
            ("Unterschriften",
             signatures("Dr. Veronika Stankl", "Beiratsvorsitzende", B["name"],
                        "Dr. Katharina Berger", "CEO", B["name"],
                        place="Muenchen", date_str_=datum)),
        ])


board_res("BR_2020_04_Beschluss_Genehmigung Unternehmenss.docx", "14. April 2020",
    "Genehmigung der Unternehmensstrategie 2020-2024",
    "Die Geschaeftsfuehrung hat eine ueberarbeitete Mehrjahresstrategie 'Precision Growth 2024' vorgelegt. Die Strategie sieht eine Verdoppelung des Umsatzes von 58 auf 116 Mio. EUR bis 2024 vor, durch Markteinfuehrung von Cardevio Pro und Ostevo Navigator unter MDR sowie internationale Expansion in den DACH-, BeNeLux- und Frankreich-Markt. Die geplanten F&E-Investitionen belaufen sich auf rund 38 Mio. EUR ueber die Strategie-Periode.",
    "Der Beirat genehmigt die Strategie 'Precision Growth 2024' in der vorgelegten Fassung. Die Umsetzung erfolgt ab Q3/2020 mit halbjaehrlichen Status-Reviews im Beirat.")

board_res("BR_2020_05_Beschluss_Beschluss über Erteilung .docx", "12. Mai 2020",
    "Erteilung Gesamtprokura an Frau Andrea Schneider (Head of Operations)",
    "Frau Andrea Schneider hat seit 1. Januar 2017 die Funktion 'Head of Operations' bei der Sentavia Precision GmbH inne. "
    "Mit Wachstum der Gesellschaft und der zunehmenden internationalen Vertriebsaktivitaet ist die Erteilung einer Prokura "
    "zur Entlastung der Geschaeftsfuehrung im operativen Tagesgeschaeft erforderlich.",
    "Frau Andrea Schneider wird mit Wirkung zum 1. Juni 2020 Gesamtprokura gemaess §§ 48 ff. HGB erteilt. Sie vertritt die "
    "Gesellschaft gemeinsam mit einem weiteren Prokuristen oder einem Geschaeftsfuehrer. Die Anmeldung zum Handelsregister "
    "erfolgt durch Notarin Dr. Hofmann (Muenchen).")

board_res("BR_2021_01_Beschluss_Genehmigung der Kapitalke.docx", "18. Januar 2021",
    "Genehmigung der Kapitalerhoehung Series-B (Vol. 25 Mio. EUR)",
    "Im Rahmen der Finanzierung der MDR-Zertifizierung der Produkte Cardevio Pro und Ostevo Navigator sowie der "
    "Erschliessung des US-Marktes hat die Geschaeftsfuehrung eine Kapitalerhoehung im Rahmen einer Series-B-Finanzierungsrunde "
    "verhandelt. Lead Investor: Sofinnova Partners (Paris) mit 25 Mio. EUR. Die Bewertung pre-money betraegt 105 Mio. EUR.",
    "Der Beirat genehmigt die Kapitalerhoehung im beschriebenen Volumen, die Anpassung des Gesellschaftsvertrages "
    "(Erhoehung Stammkapital auf 500.000 EUR sowie Anpassung der Vinkulierungsklauseln), die Aufnahme der Sofinnova "
    "Partners in den Beirat (1 Sitz) und die Begebung von Vorzugsanteilen mit 1x Liquidation Preference.")

board_res("BR_2021_02_Beschluss_Bestellung von Dr. Marcus.docx", "22. Februar 2021",
    "Bestellung von Dr. Marcus Vogt zum Chief Technology Officer (CTO)",
    "Mit dem rasanten Wachstum der F&E- und Produkt-Roadmap sowie der Vorbereitung der MDR-Zertifizierungen "
    "wird die Funktion eines Chief Technology Officer geschaffen. Dr. Marcus Vogt (Promotion in Medizintechnik, "
    "ETH Zuerich; zuvor 8 Jahre bei Siemens Healthineers AG) wurde als Kandidat ausgewaehlt.",
    "Dr. Marcus Vogt wird mit Wirkung zum 1. Mai 2021 zum Chief Technology Officer (CTO) der Sentavia Precision GmbH "
    "bestellt. Der Anstellungsvertrag (Bestandteil dieses Beschlusses) sieht ein Jahresfixgehalt von 280.000 EUR, "
    "Tantieme bis 50 % sowie Beteiligung am LTI-Programm vor.")

board_res("BR_2021_06_Beschluss_Bestellung Dr. Annika Sch.docx", "14. Juni 2021",
    "Bestellung von Dr. Annika Schmidt zur Chief Medical Officer (CMO)",
    "Im Rahmen der Internationalisierungsstrategie und der Vorbereitung der US-Marktzulassung von Cardevio Pro "
    "wird die Funktion eines Chief Medical Officer geschaffen. Dr. med. Annika Schmidt (Promotion Charite, "
    "Fachaerztin Kardiologie und Innere Medizin, zuvor 6 Jahre bei Boston Scientific) wird in dieser Funktion taetig.",
    "Dr. Annika Schmidt wird mit Wirkung zum 1. August 2021 zur Chief Medical Officer (CMO) bestellt. "
    "Anstellungsvertrag mit Jahresfixgehalt 260.000 EUR, Tantieme bis 40 %, LTI-Programm. Sie berichtet direkt an "
    "die CEO und ist Mitglied des Geschaeftsfuehrungs-Boards.")

board_res("BR_2021_07_Beschluss_Genehmigung Mietvertragsv.docx", "12. Juli 2021",
    "Genehmigung Mietvertragsverlaengerung Hauptsitz Freimannstrasse 45",
    "Der bestehende Mietvertrag fuer den Hauptsitz Freimannstrasse 45, Muenchen (Bueroflaeche 2.480 m², "
    "Reinraum-Produktionsflaeche 820 m²) laeuft zum 31. Dezember 2022 aus. Im Rahmen einer Vertragsverhandlung "
    "hat der Vermieter (Schoerghuber Immobilien GmbH) eine Verlaengerung um 10 Jahre angeboten.",
    "Der Beirat genehmigt die Mietvertragsverlaengerung zu folgenden Konditionen: Laufzeit 10 Jahre "
    "(1.1.2023 - 31.12.2032), Monatsmiete 78.500 EUR netto, jaehrliche Indexierung VPI, Modernisierungs"
    "klausel bis 5 % Mehrkosten zulaessig. Eine Verlaengerungsoption fuer weitere 5 Jahre wird gewahrt.")

board_res("BR_2022_01_Beschluss_Genehmigung des Abschluss.docx", "18. Januar 2022",
    "Genehmigung Abschluss MDR-Zertifizierung Cardevio Pro mit TUEV SUED",
    "Der Cardevio Pro hat die technische Dokumentation gemaess MDR (EU 2017/745) Anhang II/III abgeschlossen. "
    "Die Notified Body TUEV SUED Product Service GmbH (CE 0123) hat die finale Konformitaetsbewertung vorgelegt. "
    "Geplante Auslieferung der CE-Marken-Zertifikate erfolgt im Q1/2022.",
    "Der Beirat genehmigt den Abschluss des Konformitaetsbewertungsverfahrens mit TUEV SUED Product Service GmbH "
    "und die Aufnahme der Cardevio Pro CE-Markierung in alle EU-Maerkte. Die Markteinfuehrung erfolgt ab "
    "Februar 2022; Schwerpunktmaerkte DACH und Frankreich.")

board_res("BR_2022_02_Beschluss_Genehmigung der Eröffnung.docx", "8. Februar 2022",
    "Genehmigung der Eroeffnung einer Vertriebsniederlassung Frankreich",
    "Im Rahmen der Internationalisierungs-Roadmap soll als erster Auslandsstandort die Vertriebsniederlassung "
    "'Sentavia Precision France S.A.S.' in Lyon eroeffnet werden. Geplante Mitarbeitende: 8 (4 KAM Krankenhaeuser, "
    "2 Service-Techniker, 1 Marketing, 1 Verwaltung). Investitionsvolumen 1,2 Mio. EUR Aufbau, "
    "ROI 24 Monate.",
    "Der Beirat genehmigt die Gruendung der Sentavia Precision France S.A.S. (100 % Tochter), Sitz Lyon, "
    "Stammkapital 100.000 EUR. Die Geschaeftsfuehrung wird ermaechtigt, alle erforderlichen Vertrags- und "
    "Gruendungsschritte einzuleiten.")

board_res("BR_2022_03_Beschluss_Zustimmung zum Abschluss .docx", "14. Maerz 2022",
    "Zustimmung Abschluss Vertriebsvereinbarung Siemens Healthineers",
    "Die Verhandlungen mit Siemens Healthineers AG (Erlangen) zur Distribution von Cardevio Pro im "
    "DACH-Markt sind abgeschlossen. Die Vereinbarung sieht eine 3-Jahres-Partnerschaft mit Mindestabnahme "
    "180 Geraete/Jahr, exklusiver Vertrieb in der DACH-Region und gegenseitige Co-Marketing-Verpflichtung vor.",
    "Der Beirat stimmt dem Abschluss der Vertriebsvereinbarung mit Siemens Healthineers AG zu. "
    "Vertragsvolumen ueber Laufzeit ca. 28 Mio. EUR (DAP-Preise), erwartete Service-Erloese 8 Mio. EUR.")

board_res("BR_2022_08_Beschluss_Zustimmung zur Teilnahme .docx", "22. August 2022",
    "Zustimmung zur Teilnahme an Studie BfArM 'Adaptive Pathway IVD'",
    "Das BfArM (Bundesinstitut fuer Arzneimittel und Medizinprodukte) hat die Sentavia Precision GmbH "
    "eingeladen, mit dem Veridiq SARS-Flex an einem Pilot zum 'Adaptive Pathway' fuer IVD-Klasse-C-Produkte "
    "teilzunehmen. Die Studie ermoeglicht eine fruehzeitige bedingte Marktzulassung mit verkuerzten "
    "klinischen Vorlaufzeiten.",
    "Der Beirat stimmt der Teilnahme zu. Studienleitung: CMO Dr. Schmidt. Erwarteter wissenschaftlicher und "
    "regulatorischer Nutzen: deutliche Reduktion Time-to-Market (-12 Monate); enge Abstimmung mit Notified Body.")

board_res("BR_2023_01_Beschluss_Genehmigung des Erwerbs d.docx", "18. Januar 2023",
    "Genehmigung Erwerb der Bio-Sensor-Technologie der MedTech-Startup AG",
    "Die MedTech-Startup AG (Lausanne) hat eine bahnbrechende Bio-Sensor-Technologie zur Endotoxin-Detektion "
    "entwickelt. Diese Technologie passt zur Roadmap des Veridiq SARS-Flex und ermoeglicht eine Erweiterung "
    "in 5 weitere IVD-Anwendungen. Erwerbspreis: 8,2 Mio. EUR (5 Mio. cash + 3,2 Mio. Earn-Out).",
    "Der Beirat genehmigt den Asset-Erwerb der Bio-Sensor-Technologie. Die rechtliche Durchfuehrung erfolgt "
    "ueber einen Asset-Purchase-Agreement; Closing geplant Q2/2023. Mitarbeiter-Uebernahme: 6 Wissenschaftler "
    "in das F&E-Team der BTP.")

board_res("BR_2023_02_Beschluss_Bestellung von Dr. Annika.docx", "14. Februar 2023",
    "Bestellung Dr. Annika Schmidt zum stellv. Vorsitzenden Geschaeftsfuehrung",
    "Nach erfolgreicher Markteinfuehrung Cardevio Pro und der CMO-Funktion seit August 2021 wird "
    "Dr. Annika Schmidt zusaetzlich die Funktion 'Stellvertretende Vorsitzende der Geschaeftsfuehrung' uebertragen.",
    "Dr. Annika Schmidt wird mit Wirkung 1. April 2023 zur stellvertretenden Vorsitzenden der Geschaeftsfuehrung "
    "bestellt. Die Funktion umfasst die Stellvertretung in Geschaeftsfuehrungssitzungen, gegenueber Gesellschaftern und "
    "im operativen Tagesgeschaeft. Die Vergutung wird entsprechend angepasst (+15 % Fixgehalt, +5 PP Tantieme-Cap).")

board_res("BR_2023_03_Beschluss_Genehmigung eines Aktieno.docx", "18. Maerz 2023",
    "Genehmigung Aktienoptionsprogramm (ESOP) 2023",
    "Zur langfristigen Bindung der Schluesselpersonen und der Belegschaft wird ein erweitertes Aktien"
    "optionsprogramm (ESOP) aufgelegt. Volumen: 8 % des Stammkapitals (entspricht 40.000 EUR Nennbetrag). "
    "Begueterte Personen: ca. 78 Mitarbeitende und Schluesselpersonen.",
    "Der Beirat genehmigt das ESOP 2023 mit Volumen 8 % des Stammkapitals (Strike Price 1,80x Series-B-Bewertung, "
    "Vesting 4 Jahre / 1 Jahr Cliff, Beschleunigungsklausel bei Change-of-Control). Implementierung durch "
    "Heuking Kuehn (legal) und Buehlmann Compensation Advisors (Bewertung).")

board_res("BR_2023_04_Beschluss_Genehmigung des Jahresabs.docx", "14. April 2023",
    "Genehmigung Jahresabschluss 2022 (HGB)",
    "Der Jahresabschluss 2022 wurde durch PwC AG WPG geprueft und uneingeschraenkt testiert. Kennzahlen: "
    "Umsatz 71,4 Mio. EUR (+23 %); EBITDA 9,8 Mio. EUR; Jahresueberschuss 5,8 Mio. EUR; Bilanzsumme 84,2 Mio. EUR; "
    "Eigenkapital 47,8 Mio. EUR (56,8 %); 512 Mitarbeitende.",
    "Der Beirat genehmigt den Jahresabschluss 2022 in der vorgelegten Fassung. Empfehlung zur Vorlage an die "
    "Gesellschafterversammlung am 22. Juni 2023. Ergebnisverwendung: 50 % Thesaurierung, 50 % als Dividende. "
    "Wiederbestellung PwC fuer Geschaeftsjahr 2023.")

board_res("BR_2023_09_Beschluss_Genehmigung Einführung vi.docx", "12. September 2023",
    "Genehmigung Einfuehrung virtuelle Mitarbeiterbeteiligung VSOP",
    "Ergaenzend zum ESOP (Aktienoptionen fuer Schluesselpersonen) wird ein virtuelles Mitarbeiterbeteiligungs"
    "programm (Virtual Stock Option Plan, VSOP) fuer das breitere Belegschafts-Segment aufgelegt. "
    "Begueterte: alle festangestellten Mitarbeitenden mit > 6 Monaten Betriebszugehoerigkeit. Volumen: 4 % "
    "virtuelles Eigenkapital, Auszahlung in cash bei Exit-Ereignis.",
    "Der Beirat genehmigt das VSOP 2023 mit Volumen 4 % virtueller Anteile. Vesting analog ESOP (4 Jahre / "
    "1 Jahr Cliff). Implementation Q4/2023.")

board_res("BR_2024_01_Beschluss_Genehmigung der Aufnahme .docx", "16. Januar 2024",
    "Genehmigung Aufnahme einer Wachstumsfinanzierung der EIB",
    "Die Europaeische Investitionsbank (EIB) hat eine Wachstumsfinanzierung im Volumen 35 Mio. EUR "
    "(Venture Debt) angeboten, die zur Erweiterung der Produktionskapazitaeten (neue Reinraum-Linie "
    "Ostevo Navigator) und zur weiteren Internationalisierung (USA-Markteintritt Q3/2025) eingesetzt "
    "werden soll. Laufzeit 7 Jahre, Zinssatz EURIBOR 6M + 425 bp, mit Warrants 2 % Equity-Upside.",
    "Der Beirat genehmigt die Aufnahme der EIB-Wachstumsfinanzierung in voller Hoehe. Die Geschaeftsfuehrung "
    "wird ermaechtigt, die finale Vertragsverhandlung in Abstimmung mit der Anwaltskanzlei Noerr zu fuehren. "
    "Closing Q2/2024.")

board_res("BR_2024_02_Beschluss_Beauftragung der Noerr Pa.docx", "14. Februar 2024",
    "Beauftragung Noerr Partnerschaft zur Begleitung der EIB-Finanzierung",
    "Im Rahmen der Aufnahme der EIB-Wachstumsfinanzierung (Beschluss BR-2024-01) wird eine spezialisierte "
    "rechtliche Begleitung benoetigt. Noerr PartGmbB (vertreten durch Dr. Sebastian Wallisch, Bank- und "
    "Finanzrecht) hat ein Mandatsangebot vorgelegt.",
    "Der Beirat genehmigt die Beauftragung von Noerr PartGmbB als rechtliche Berater fuer die EIB-Finanzierung. "
    "Honorar: Pauschalpaket 180.000 EUR (Closing-bezogen) zzgl. Stundenhonorare fuer Sonderthemen. "
    "Mandatsbeginn 18. Februar 2024.")

board_res("BR_2024_03_Beschluss_Genehmigung der Anpassung.docx", "12. Maerz 2024",
    "Genehmigung Anpassung der Notified-Body-Strategie (Dual-NB)",
    "Aufgrund von Engpaessen bei der TUEV SUED Product Service GmbH (CE 0123) bei der MDR-Re-Zertifizierung "
    "und im Hinblick auf eine moegliche zweite NB-Strategie (Risikominimierung, geopolitische Vorsorge) "
    "schlaegt die Geschaeftsfuehrung vor, mit BSI Group (CE 2797) eine Zweitqualifikation fuer "
    "Ostevo Navigator aufzubauen.",
    "Der Beirat genehmigt die Dual-NB-Strategie. Implementierung mit BSI Group als zweiter Notified Body fuer "
    "Ostevo Navigator (Klasse IIa). Vorhaltevolumen 320.000 EUR p. a. ueber 24 Monate; Vollqualifikation "
    "im Q1/2026 erwartet.")

board_res("BR_2024_10_Beschluss_Genehmigung Due-Diligence.docx", "8. Oktober 2024",
    "Genehmigung Due-Diligence-Prozess (potenzielle Series-C / Trade Sale)",
    "Im Hinblick auf die strategische Roadmap 2025-2027 hat die Geschaeftsfuehrung ein Sondierungs-Mandat "
    "an Goldman Sachs (Frankfurt) erteilt zur Bewertung von zwei alternativen Wachstumspfaden: (a) "
    "Series-C-Finanzierungsrunde 60-80 Mio. EUR oder (b) Trade Sale an einen strategischen Investor. "
    "Erste Due-Diligence-Anfragen sind eingegangen.",
    "Der Beirat genehmigt die Eroeffnung eines strukturierten Due-Diligence-Prozesses unter Leitung der "
    "Geschaeftsfuehrung mit Beratung durch Goldman Sachs. Datenraum-Aufbau Q4/2024; LOI-Phase voraussichtlich "
    "Q1/2025. Investoren-Update am 15. Dezember 2024.")

board_res("BR_2024_11_Beschluss_Ausschüttungsbeschluss Vo.docx", "12. November 2024",
    "Ausschuettungsbeschluss Vorab-Dividende 2024",
    "Auf Basis der vorlaeufigen Geschaeftsjahres-Zahlen 2024 (erwarteter Jahresueberschuss 13,8 Mio. EUR) "
    "und unter Beruecksichtigung der gestaerkten Bilanzstruktur sowie der erwarteten Series-C / Trade-Sale-"
    "Transaktion in 2025 schlaegt die Geschaeftsfuehrung eine Vorab-Dividende vor.",
    "Der Beirat genehmigt die Vorab-Dividende 2024 in Hoehe von 4,2 Mio. EUR (entspricht ca. 30 % des "
    "erwarteten Jahresueberschusses). Die Auszahlung erfolgt im Verhaeltnis der Stammkapital-Anteile an die "
    "Gesellschafter (Sofinnova 35 %, Lakestar 25 %, Management-GbR 15 %, HTGF 10 %, Streubesitz 15 %). "
    "Auszahlung 28. November 2024.")

# Gesellschafterliste
write_doc(f"{BASE}/01_Gesellschaftsrecht/GR_004_Gesellschafterliste_2024.docx", H,
    "Gesellschafterliste – Sentavia Precision GmbH",
    subtitle="Stand: 15. Januar 2024",
    sections=[
        ("1. Hinterlegung", "Diese Gesellschafterliste wird gemaess § 40 GmbHG beim Handelsregister des Amtsgerichts "
                            "Muenchen unter HRB 218934 hinterlegt. Sie ersetzt die zuletzt am 22. Februar 2023 hinterlegte Liste."),
        ("2. Stammkapital", "Das Stammkapital der Gesellschaft betraegt 500.000 EUR, aufgeteilt in 500 Stammanteile "
                            "zu je 1.000 EUR Nennbetrag. Die Stammeinlagen sind vollstaendig erbracht."),
        ("3. Gesellschafter",
         [["Nr.", "Gesellschafter", "Anschrift", "Anteile (Nr.)", "Nennbetrag EUR", "Anteil %"],
          ["1", "Sofinnova Partners (Paris)", "7-11 Boulevard Haussmann, 75009 Paris", "1-175", "175.000", "35,0"],
          ["2", "Lakestar I LP (Zürich)", "Bleicherweg 50, 8002 Zuerich", "176-300", "125.000", "25,0"],
          ["3", "Management-Beteiligungs-GbR", "Freimannstrasse 45, 80939 Muenchen", "301-375", "75.000", "15,0"],
          ["4", "High-Tech Gruenderfonds (HTGF)", "Schlegelstrasse 2, 53113 Bonn", "376-425", "50.000", "10,0"],
          ["5", "Streubesitz (Mitarbeitende, Privatpersonen)", "diverse", "426-500", "75.000", "15,0"],
          ["", "SUMME", "", "500 Anteile", "500.000", "100,0"]]),
        ("4. Erklaerung",
         "Die unterzeichnende Geschaeftsfuehrung erklaert, dass diese Liste den aktuellen Beteiligungs"
         "verhaeltnissen entspricht und alle Veraenderungen gegenueber der zuletzt hinterlegten Liste "
         "(insbesondere Anteilsuebertragungen im Rahmen des ESOP 2023) ordnungsgemaess beruecksichtigt wurden.\n\n"
         "Muenchen, den 15. Januar 2024."),
        ("Unterschriften",
         signatures("Dr. Katharina Berger", "CEO", B["name"],
                    "Thomas Mueller", "CFO", B["name"],
                    place="Muenchen", date_str_="15. Januar 2024")),
    ])

# Prokura (already at 197w, push to 250+)
write_doc(f"{BASE}/01_Gesellschaftsrecht/Prokura_Erteilung_Hoffmann_Schneider.docx", H,
    "Prokura-Erteilung – Frau Andrea Schneider und Herr Bjoern Hoffmann",
    subtitle="Eintragung Handelsregister HRB 218934, AG Muenchen",
    sections=[
        ("1. Beschluss der Geschaeftsfuehrung",
         "Mit Beschluss vom 12. Mai 2020 hat die Geschaeftsfuehrung der Sentavia Precision GmbH, vertreten "
         "durch die CEO Dr. Katharina Berger, sowie unter Bestaetigung des Beirats (Beschluss BR-2020-05) "
         "der Frau Andrea Schneider (Head of Operations) Gesamtprokura gemaess §§ 48 ff. HGB erteilt. "
         "Ergaenzend wurde mit Beschluss vom 14. Februar 2022 Herrn Bjoern Hoffmann (Head of Finance) "
         "ebenfalls Gesamtprokura erteilt."),
        ("2. Bevollmaechtigte und Umfang",
         "Frau Andrea Schneider, geb. 18.06.1978, wohnhaft Sendlinger-Tor-Platz 4, 80336 Muenchen, "
         "in der Sentavia Precision GmbH seit 1.1.2017 in Funktion Head of Operations. "
         "Herr Bjoern Hoffmann, geb. 4.11.1981, wohnhaft Truderinger Strasse 132, 81825 Muenchen, "
         "in der Gesellschaft seit 1.3.2019 in Funktion Head of Finance.\n\n"
         "Beiden Prokuristen wird Gesamtprokura erteilt: Sie vertreten die Gesellschaft jeweils gemeinsam "
         "mit einem weiteren Prokuristen oder mit einem Geschaeftsfuehrer. Der Umfang der Prokura "
         "ergibt sich aus § 49 HGB."),
        ("3. Beschraenkungen im Innenverhaeltnis",
         "Im Innenverhaeltnis sind die Prokuristen gebunden an die Bestellrichtlinie der Gesellschaft "
         "(Stand 1.1.2024): Genehmigung der Geschaeftsfuehrung bei Einzelgeschaeften > 500.000 EUR, "
         "Beteiligungsverkaeufen, Erwerb / Veraeusserung von Immobilien und Wechselgeschaeften."),
        ("4. Eintragung Handelsregister",
         "Die Anmeldung der Prokuren zum Handelsregister erfolgte durch die Notarin Dr. Susanne Hofmann "
         "(Theatinerstrasse 30, 80333 Muenchen, UR-Nr. 218/2020 vom 18.5.2020 sowie UR-Nr. 78/2022 vom "
         "21.2.2022). Eintragung im Handelsregister: 28.5.2020 bzw. 4.3.2022."),
        ("5. Geltungsdauer",
         "Die Prokuren gelten bis auf Widerruf und enden automatisch mit dem Ende des jeweiligen "
         "Anstellungsverhaeltnisses. Eine Veroeffentlichung im internen Mitarbeiterportal sowie im "
         "Lieferantenverzeichnis ist erfolgt."),
        ("Unterschriften",
         signatures("Dr. Katharina Berger", "CEO", B["name"],
                    "Dr. Marcus Vogt", "CTO", B["name"],
                    place="Muenchen", date_str_="22. Februar 2022")),
    ])


# ── 02_Finanzen: Cash Pooling ──────────────────────────────────────────────
write_doc(f"{BASE}/02_Finanzen/FIN_Cash_Pooling_Agreement.docx", H,
    "Cash-Pooling-Vereinbarung 2024",
    subtitle="Notional Cash Pooling der BTP-Gruppe (Muttergesellschaft + Tochter Frankreich)",
    sections=[
        ("Parteien",
         "Sentavia Precision GmbH (»BTP«, Muttergesellschaft, Pool-Leader) und Sentavia Precision France S.A.S. "
         "(»BTPF«, 100 % Tochter, Sitz Lyon)."),
        ("Pool-Bank",
         "UniCredit Bank AG (HypoVereinsbank), Standort Muenchen Hauptbahnhof, fuehrt das Cash-Pooling als "
         "»Notional Cash Pooling« durch (zinsoptimierender Saldenausgleich, keine physische Liquiditaets"
         "verschiebung). Pool-IBAN: DE42 7002 0270 0012 3456 00."),
        ("Funktionsweise",
         "Tagliche notionale Saldenverrechnung saemtlicher EUR-Konten der teilnehmenden Gesellschaften. "
         "Sollzinsen werden auf das aggregierte Nettosaldo berechnet (Vorteil ca. 70 bp gegenueber Einzel"
         "saldenzins). Aufrechnungsverbot bei Konkurs einer Beteiligten gemaess Cash Pool Master Agreement "
         "vom 14. Januar 2024. Limit: 5 Mio. EUR Sollsaldo aggregiert."),
        ("Verzinsung",
         "Aktivzins: EURIBOR 1M -10 bp; Passivzins: EURIBOR 1M +175 bp. Intercompany-Verzinsung zwischen "
         "BTP und BTPF: marktueblicher Drittvergleichszinssatz (gemaess OECD Verrechnungspreisrichtlinien). "
         "Quartalsweise Verrechnung im Intercompany-Konto."),
        ("Steuerliche / regulatorische Behandlung",
         "Verrechnungspreisdokumentation gemaess § 90 Abs. 3 AO sowie OECD-Verrechnungspreisrichtlinien. "
         "Frankreich: Anwendung der franzoesischen Verrechnungspreisregelungen (Article 57 CGI). "
         "Dokumentation im Local File/Master File der BTP-Gruppe (Erstellung durch PwC AG WPG)."),
        ("Laufzeit / Kuendigung",
         "Vertrag laeuft auf unbestimmte Zeit. Kuendigung mit Frist 3 Monate zum Quartalsende. "
         "Eine ausserordentliche Kuendigung ist bei wesentlichen Vertragsverletzungen oder bei Insolvenz "
         "einer Beteiligten zulaessig."),
        ("Unterschriften",
         signatures("Thomas Mueller", "CFO", B["name"],
                    "Sebastien Renard", "Directeur General", "Sentavia Precision France S.A.S.",
                    place="Muenchen / Lyon", date_str_="22. Januar 2024")),
    ])


# ── 03_Personal_HR: Remote Work + Onboarding ────────────────────────────────
write_doc(f"{BASE}/03_Personal_HR/HR_Remote_Work_Richtlinie.docx", H,
    "Remote-Work-Richtlinie 2024",
    subtitle="Gueltig ab 1. April 2024",
    sections=[
        ("Geltungsbereich",
         "Diese Richtlinie regelt die Bedingungen fuer Remote-Arbeit (Homeoffice und mobiles Arbeiten) bei "
         "der Sentavia Precision GmbH. Sie gilt fuer alle Beschaeftigten, deren Taetigkeit ueberwiegend "
         "ortsunabhaengig erbracht werden kann. Ausgenommen: Reinraum-Produktion, Service-Techniker im "
         "Aussendienst, Laborarbeit."),
        ("Umfang Remote-Arbeit",
         "Standardregelung: bis zu 60 % der woechentlichen Arbeitszeit (3 Tage bei 5-Tage-Woche) koennen "
         "remote erbracht werden. Bei Sondersituationen (z. B. Familienpflege, Schwerbehinderung) kann mit "
         "Zustimmung der Personalleitung der Anteil erhoeht werden. Mind. 2 Praesenztage pro Woche sind "
         "fuer Teams mit ueberwiegend physischer Zusammenarbeit (F&E, QM) verpflichtend."),
        ("Arbeitsort und Erreichbarkeit",
         "Der mobile Arbeitsort liegt in der Regel im Privathaushalt des/der Beschaeftigten innerhalb "
         "Deutschlands. Andere Orte (z. B. Bibliothek, Cafe, Coworking-Space) sind nur zulaessig, wenn "
         "Vertraulichkeit, Datenschutz und Datensicherheit gewaehrleistet sind. Erreichbarkeit Mo-Fr "
         "09:00-15:00 Uhr ueber Microsoft Teams und Telefon."),
        ("Arbeitsmittel und Infrastruktur",
         "Der Arbeitgeber stellt: Notebook, Headset, Bildschirm, Tastatur, ergonomische Maus. "
         "Energie-/Internetpauschale 30 EUR/Monat (max. 6 EUR/Tag, max. 210 Tage/Jahr gemaess EStG). "
         "VPN-Zugang ueber Cisco AnyConnect; MFA verpflichtend. Verschluesselung BitLocker."),
        ("Datenschutz und Informationssicherheit",
         "Externe Personen (Familie, Besuche) sind vom Arbeitsplatz fernzuhalten. Bildschirmschoner aktiviert "
         "(Sperre nach 5 Min.). Patientendaten / klinische Daten duerfen NICHT remote bearbeitet werden "
         "(nur in der gesicherten Klinik-Datenbank REDCap, Zugriff nur im Buero). Dokumente nicht ausdrucken; "
         "wenn unvermeidlich: Vernichtung gemaess DIN 66399 Sicherheitsstufe 3."),
        ("Beendigung der Vereinbarung",
         "Im Einzelfall kann die Remote-Arbeit mit Frist von 4 Wochen wieder beendet werden; Begruendungs"
         "pflicht durch den Arbeitgeber."),
        ("Unterschriften",
         signatures("Dr. Katharina Berger", "CEO", B["name"],
                    "Andrea Schneider", "Head of Operations", B["name"],
                    place="Muenchen", date_str_="22. Maerz 2024")),
    ])

write_doc(f"{BASE}/03_Personal_HR/HR_Onboarding_Checkliste.docx", H,
    "Onboarding-Checkliste fuer neue Mitarbeitende",
    subtitle="Standardprozess BTP-Onboarding, Stand 1. Januar 2024",
    sections=[
        ("Phase 1: Vor dem ersten Arbeitstag (durch HR / Personal)",
         ("list", [
             "Vertragsunterzeichnung digital ueber DocuSign (Vertragsentwurf, NDA, Datenschutzhinweise Art. 13 DSGVO)",
             "Vorbereitung der Hardware (Notebook, Headset, Monitor, Tastatur, Maus); Bestellung ueber IT-Helpdesk Ticket",
             "AD-Account und E-Mail-Adresse anlegen; Microsoft 365 E5-Lizenz zuweisen",
             "Schluessel / Reinraum-Badges vorbereiten (Empfang + Sicherheit briefen)",
             "Mentor:in benennen und ueber Onboarding-Plan informieren",
             "Welcome-Paket vorbereiten (BTP-Branding, Notizbuch, Trinkflasche, Welcome-Letter CEO)",
         ])),
        ("Phase 2: Erster Tag",
         ("list", [
             "Empfang durch HR (09:00 Uhr Lobby); persoenliche Begruessung",
             "Werkstour Hauptsitz Freimannstrasse 45 (Buero, Reinraum, Labor)",
             "IT-Setup mit IT-Team (Notebook, MFA, Zugaenge: Outlook, Teams, SharePoint, MasterControl QMS, REDCap, SAP)",
             "Pflichtschulung GxP-Grundlagen (Lab-Bereich) bzw. ISO 13485 (alle Bereiche)",
             "Mittagessen mit Team und Mentor:in",
             "Erste 1:1 mit direkter Fuehrungskraft",
         ])),
        ("Phase 3: Erste Woche",
         ("list", [
             "Einweisung Datenschutz / DSGVO (durch DSB Dr. Markus Lehmann)",
             "Pflichtschulung Compliance (Anti-Korruption, HWG, Code of Conduct) – e-Learning",
             "Sicherheits-Briefing (Reinraum, Biolabor-Sicherheit, Notfall)",
             "Vorstellung Geschaeftsfuehrung und Beirat (Welcome Meeting, Freitag 10:00 Uhr)",
             "Erste Zielvereinbarung 90-Tage-Plan mit Fuehrungskraft",
         ])),
        ("Phase 4: Erste 90 Tage",
         ("list", [
             "Schulungsplan abarbeiten (Produktportfolio Cardevio Pro, Ostevo Navigator, Veridiq SARS-Flex)",
             "Funktion-spezifische Schulungen (z. B. R&D: MDR-Grundlagen; Vertrieb: Krankenhaus-Vertrieb)",
             "30-/60-/90-Tage-Feedback mit Fuehrungskraft und Mentor:in",
             "Probezeit-Gespraech (vor Ablauf Monat 5)",
             "Welcome-Lunch mit GF / Fuehrungskreis am Ende der ersten 90 Tage",
         ])),
        ("Verantwortlich",
         "Onboarding-Prozess wird betreut durch das HR-Team (Lead: Anna Becker, HR-Generalistin) sowie "
         "den jeweiligen Mentor:in. Eskalation: Head of People Andrea Schneider."),
    ])


# ── 08_Klinische_Bewertung: 7 Prüfarztverträge ─────────────────────────────
def pruefarzt(fname, product, klinik, klinik_short, leitung, pat_anzahl, honorar_eur, studie_id):
    write_doc(f"{BASE}/08_Klinische_Bewertung/{fname}", H,
        f"Pruefarztvertrag – {product} – {klinik_short}",
        subtitle=f"Klinische Pruefung gemaess EU 2017/745 (MDR) / Studien-ID {studie_id}",
        sections=[
            ("Parteien",
             f"Sponsor: Sentavia Precision GmbH, vertreten durch Dr. Annika Schmidt (CMO).\n\n"
             f"Pruefstelle / Pruefer: {klinik}, vertreten durch {leitung} (Pruefarzt:in)."),
            ("Pruefgegenstand",
             f"Klinische Pruefung des Medizinprodukts {product} (Hersteller: Sentavia Precision GmbH; "
             f"CE 0123-BTP). Studientyp: prospektive, multi-zentrische, kontrollierte Pruefung gemaess "
             f"ISO 14155:2020 und MDR Anhang XV. Vorgesehene Patientenanzahl an dieser Pruefstelle: "
             f"{pat_anzahl}; Gesamt-Studienkohorte: 360. Studiendauer: 18 Monate ab erstem Patienteneinschluss."),
            ("Pflichten des/der Pruefenden",
             ("clauses", [
                 ("§ 1 Allgemeine Pflichten", [
                     "Durchfuehrung der Pruefung gemaess dem Pruefplan (Anlage 1), GCP-Grundsaetzen ICH E6 (R2), "
                     "ISO 14155:2020 sowie der MDR (EU 2017/745) und nationalen Gesetzen (MPDG).",
                     "Vorlage der Studienunterlagen bei der Ethikkommission der Bayerischen Landesaerztekammer "
                     "und beim BfArM (Bundesinstitut fuer Arzneimittel und Medizinprodukte).",
                 ]),
                 ("§ 2 Aufklaerung und Einwilligung", [
                     "Patient:innen sind vor Einschluss in die Studie aufzuklaeren (schriftlich, unter Verwendung "
                     "der genehmigten Patienteninformation, Anlage 3). Schriftliche informierte Einwilligung "
                     "(IC) ist Voraussetzung des Studieneinschlusses.",
                 ]),
                 ("§ 3 Daten und Dokumentation", [
                     "Erfassung der Studiendaten im elektronischen Case Report Form (eCRF) in REDCap "
                     "(Clinical Database der BTP). Saemtliche Source Documents (z. B. KIS-Daten) sind "
                     "verfuegbar zu halten fuer SAE/AE-Bewertung sowie fuer Audits / Inspections.",
                     "Aufbewahrung der Studiendokumente fuer 15 Jahre nach Studienende.",
                 ]),
                 ("§ 4 Adverse Events / Vigilance", [
                     "Schwerwiegende unerwuenschte Ereignisse (SAE) sind binnen 24 Stunden an die Vigilance-Stelle "
                     "BTP (vigilance@sentavia-precision.de) zu melden. Geraetebezogene Vorkommnisse sind "
                     "zusaetzlich gemaess MDR Artikel 87 zu erfassen.",
                 ]),
             ])),
            ("Honorierung",
             f"Pauschalhonorar je vollstaendig abgeschlossenem Patienten-Set (eCRF, alle Visiten, Follow-up): "
             f"{honorar_eur} EUR (zzgl. USt., sofern anwendbar). Auszahlung quartalsweise nach Patientenfortschritt; "
             f"Endabrechnung 90 Tage nach Studienende. Reisekosten gemaess Reisekostengrundsaetzen der BTP "
             f"(Bahn 1. Kl. / Hotel maximal 4-Sterne)."),
            ("Vertraulichkeit / IP",
             "Studiendaten sind vertraulich; eine Veroeffentlichung erfolgt ausschliesslich nach Abstimmung mit "
             "BTP (Lead-Autorschaft Sponsor). Eigentumsrechte an Studienergebnissen liegen beim Sponsor BTP. "
             "Patientendaten unterliegen strenger Pseudonymisierung gemaess DSGVO und nationalem Datenschutzrecht."),
            ("Unterschriften",
             signatures("Dr. Annika Schmidt", "CMO / Sponsor-Vertreter", B["name"],
                        leitung, "Hauptpruefer / Hauptpruefin", klinik,
                        place=f"Muenchen / {klinik.split(',')[-1].strip() if ',' in klinik else 'Klinikstandort'}",
                        date_str_="—")),
        ])


pruefarzt("IA_CSP_UKH2_Pruefarztvtrag.docx", "Cardevio Pro",
    "Universitaetsklinikum Heidelberg, Klinik fuer Kardiologie, Angiologie und Pneumologie, Im Neuenheimer Feld 410, 69120 Heidelberg",
    "UKH (Heidelberg)", "Prof. Dr. med. Hugo Katus", 32, 2400, "BTP-CSP-CT-2022-018")
pruefarzt("IA_OFN_UKH_Pruefarztvtrag.docx", "Ostevo Navigator",
    "Universitaetsklinikum Heidelberg, Klinik fuer Orthopaedie und Unfallchirurgie, Schlierbacher Landstrasse 200a, 69118 Heidelberg",
    "UKH (Heidelberg)", "Prof. Dr. med. Volker Ewerbeck", 28, 2200, "BTP-OFN-CT-2023-004")
pruefarzt("IA_CSP_UKE_Pruefarztvtrag.docx", "Cardevio Pro",
    "Universitaetsklinikum Hamburg-Eppendorf (UKE), Klinik fuer Kardiologie, Martinistrasse 52, 20246 Hamburg",
    "UKE (Hamburg)", "Prof. Dr. med. Stefan Blankenberg", 38, 2500, "BTP-CSP-CT-2022-018")
pruefarzt("IA_DKS_LMU2_Pruefarztvtrag.docx", "Veridiq SARS-Flex",
    "LMU Klinikum Muenchen, Medizinische Klinik IV (Infektiologie), Pettenkoferstrasse 8a, 80336 Muenchen",
    "LMU Klinikum (Muenchen)", "Prof. Dr. med. Michael Hoelscher", 64, 1800, "BTP-DKS-CT-2023-008")
pruefarzt("IA_OFN_LMU_Pruefarztvtrag.docx", "Ostevo Navigator",
    "LMU Klinikum Muenchen, Klinik fuer Orthopaedie und Unfallchirurgie Standort Grosshadern, Marchioninistrasse 15, 81377 Muenchen",
    "LMU Klinikum (Muenchen)", "Prof. Dr. med. Volkmar Jansson", 30, 2200, "BTP-OFN-CT-2023-004")
pruefarzt("IA_CSP_CHR_Pruefarztvtrag.docx", "Cardevio Pro",
    "Charite – Universitaetsmedizin Berlin, Medizinische Klinik m. S. Kardiologie und Angiologie, Augustenburger Platz 1, 13353 Berlin",
    "Charite (Berlin)", "Prof. Dr. med. Burkert Pieske", 42, 2500, "BTP-CSP-CT-2022-018")
pruefarzt("IA_OFN_CHR2_Pruefarztvtrag.docx", "Ostevo Navigator",
    "Charite – Universitaetsmedizin Berlin, Centrum fuer Muskuloskeletale Chirurgie, Charite Platz 1, 10117 Berlin",
    "Charite (Berlin)", "Prof. Dr. med. Carsten Perka", 34, 2200, "BTP-OFN-CT-2023-004")


# ── 09_IP_Patente: 10 thin docs (NDAs + Assignments) ───────────────────────
def ip_assign(fname, name, abteilung, datum):
    write_doc(f"{BASE}/09_IP_Patente/{fname}", H,
        f"Erfindungs- und Rechte-Uebertragung (IP Assignment) – {name}",
        subtitle=f"Mitarbeiter-Vereinbarung gemaess ArbnErfG / IP Assignment Agreement",
        sections=[
            ("Parteien",
             f"Sentavia Precision GmbH (»BTP«, Arbeitgeberin) und {name} (Arbeitnehmer:in, Abteilung {abteilung})."),
            ("Praeambel",
             "Im Rahmen des Arbeitsverhaeltnisses koennen Erfindungen, Designs, Software, Datenbanken und "
             "andere Schutzrechte entstehen. Diese Vereinbarung regelt die Rechte und Pflichten beider "
             "Parteien gemaess Arbeitnehmererfindergesetz (ArbnErfG) und den entsprechenden internationalen "
             "Vorschriften (insbesondere US-Patentrecht / IP-Assignment-Doctrine)."),
            ("Regelungen",
             ("clauses", [
                 ("§ 1 Erfindungen waehrend des Arbeitsverhaeltnisses", [
                     "Alle Erfindungen, die der/die Arbeitnehmer:in waehrend der Beschaeftigung bei BTP und im "
                     "Zusammenhang mit der dienstlichen Taetigkeit macht, sind Diensterfindungen im Sinne des "
                     "ArbnErfG.",
                     "Diensterfindungen sind unverzueglich schriftlich an die Geschaeftsfuehrung (CTO) zu melden "
                     "(Formular IP-Meldung, Anlage 1).",
                 ]),
                 ("§ 2 Inanspruchnahme", [
                     "Die Inanspruchnahme erfolgt gemaess § 6 ArbnErfG durch ausdruckliche Erklaerung der "
                     "Geschaeftsfuehrung; ohne Erklaerung innerhalb von 4 Monaten gilt die Erfindung als "
                     "in Anspruch genommen.",
                 ]),
                 ("§ 3 Verguetung", [
                     "Bei Inanspruchnahme erhaelt der/die Arbeitnehmer:in eine angemessene Erfinder-Verguetung "
                     "gemaess Vergutungsrichtlinien des ArbnErfG (Lizenzanalogie). Pauschal: Anmeldebonus "
                     "1.500 EUR; Eintragungsbonus 2.500 EUR; laufende Verguetung 0,3 % vom Umsatz aus dem "
                     "Patent-geschuetzten Produkt (max. 50.000 EUR p. a. je Erfinder).",
                 ]),
                 ("§ 4 Internationale Rechte / US-Markt", [
                     "Der/die Arbeitnehmer:in tritt hiermit alle internationalen Schutzrechte (insbesondere "
                     "US-Patente, Anmelderechte) an BTP ab und unterstuetzt die Anmeldung / Aufrechterhaltung "
                     "auch nach Beendigung des Arbeitsverhaeltnisses (Mitwirkungspflicht).",
                 ]),
                 ("§ 5 Geheimhaltung", [
                     "Erfindungen sind bis zur Anmeldung streng vertraulich zu behandeln. Veroeffentlichungen / "
                     "Praesentationen beduerfen der vorherigen Freigabe.",
                 ]),
             ])),
            ("Unterschriften",
             signatures("Dr. Marcus Vogt", "CTO", B["name"], name, "Mitarbeiter:in", B["name"],
                        place="Muenchen", date_str_=datum)),
        ])


ip_assign("IP_ASSIGN_01_Dr._Lena_Fischer.docx",      "Dr. Lena Fischer",     "F&E Cardevio Pro",  "1. Juni 2021")
ip_assign("IP_ASSIGN_02_Markus_Bauer_FINAL_v2.docx", "Markus Bauer",         "F&E Ostevo Navigator","1. September 2021")
ip_assign("IP_ASSIGN_03_Sarah_Krause.docx",          "Sarah Krause",         "F&E Veridiq",         "1. November 2021")
ip_assign("IP_ASSIGN_04_Jan_Hoffmann.docx",          "Jan Hoffmann",         "F&E Hardware Engineering","1. Maerz 2022")
ip_assign("IP_ASSIGN_05_Anna_Weber_FINAL.docx",      "Anna Weber",           "F&E Software / Algorithmik","1. Juli 2022")
ip_assign("IP_ASSIGN_06_Felix_Schäfer.docx",         "Felix Schaefer",       "F&E Biosensorik",       "1. November 2022")


def nda(fname, partner, partner_addr, contact, zweck):
    write_doc(f"{BASE}/09_IP_Patente/{fname}", H,
        f"Vertraulichkeitsvereinbarung (NDA) – {partner}",
        subtitle="Gegenseitige NDA",
        sections=[
            ("Parteien",
             f"1. Sentavia Precision GmbH, Freimannstrasse 45, 80939 Muenchen.\n\n"
             f"2. {partner}, {partner_addr}, vertreten durch {contact}."),
            ("Zweck",
             f"Die Parteien beabsichtigen, Informationen im Hinblick auf {zweck} auszutauschen. Beide Parteien "
             "sind verpflichtet, vertrauliche Informationen geheim zu halten und nur fuer den vereinbarten "
             "Zweck zu verwenden."),
            ("Vertraulichkeitsregelungen",
             ("clauses", [
                 ("§ 1 Vertrauliche Informationen", [
                     "»Vertrauliche Informationen« umfassen alle technischen, kaufmaennischen, "
                     "wissenschaftlichen und sonstigen Informationen, die im Rahmen der vorgenannten Zusammenarbeit "
                     "ausgetauscht werden. Vertraulichkeit gilt unabhaengig von der Form der Offenlegung "
                     "(mundliche, schriftliche, elektronische Mitteilung).",
                 ]),
                 ("§ 2 Geheimhaltungspflicht", [
                     "Die empfangende Partei (i) verwendet die Informationen ausschliesslich zur Verwirklichung "
                     "des oben genannten Zwecks, (ii) gibt sie nicht an Dritte weiter, "
                     "(iii) wendet mindestens den Sorgfaltsstandard an, den sie auch zum Schutz eigener "
                     "vertraulicher Informationen anwendet.",
                 ]),
                 ("§ 3 Ausnahmen", [
                     "Nicht vertraulich sind Informationen, die zum Zeitpunkt der Offenlegung allgemein bekannt "
                     "waren, der empfangenden Partei nachweislich vorher bekannt waren, von Dritten ohne "
                     "Vertraulichkeitspflicht erhalten wurden oder unabhaengig entwickelt wurden.",
                 ]),
                 ("§ 4 Schutzrechte", [
                     "Diese NDA gewaehrt keine Lizenzen oder Schutzrechte an dem geistigen Eigentum der jeweils "
                     "anderen Partei. Schutzrechte bleiben beim jeweiligen Inhaber.",
                 ]),
                 ("§ 5 Laufzeit", [
                     "Die Vertraulichkeitspflichten gelten waehrend der Zusammenarbeit und 5 Jahre nach deren "
                     "Beendigung, spaetestens jedoch 7 Jahre nach Unterzeichnung dieser Vereinbarung.",
                 ]),
                 ("§ 6 Anwendbares Recht / Streitbeilegung", [
                     "Es gilt deutsches Recht; Gerichtsstand Muenchen.",
                 ]),
             ])),
            ("Unterschriften",
             signatures("Dr. Katharina Berger", "CEO", B["name"], contact, "Bevollmaechtigte/r", partner,
                        place="Muenchen", date_str_="—")),
        ])


nda("NDA_Fraunhofer IPA_Vertraulichkeitsvereinbarung.docx",
    "Fraunhofer-Institut fuer Produktionstechnik und Automatisierung IPA",
    "Nobelstrasse 12, 70569 Stuttgart", "Prof. Dr.-Ing. Marco Huber",
    "Forschungskooperation 'KI-basierte adaptive Bildgebung Cardevio Pro'")
nda("NDA_Helmholtz Zentrum Mü_Vertraulichkeitsvereinbarung.docx",
    "Helmholtz Zentrum Muenchen, Deutsches Forschungszentrum fuer Gesundheit und Umwelt",
    "Ingolstaedter Landstrasse 1, 85764 Neuherberg", "Prof. Dr. Joerg Hennessey",
    "Wissenschaftliche Kooperation 'Biosensorik fuer Veridiq SARS-Flex Variante B'")
nda("NDA_TU München – Medizin_Vertraulichkeitsvereinbarung.docx",
    "Technische Universitaet Muenchen, Fakultaet fuer Medizin",
    "Ismaninger Strasse 22, 81675 Muenchen", "Prof. Dr. med. Friederike Kelm",
    "Joint Research 'Praezisionsdiagnostik fuer Orthopaedie'")


# IP_002 Fraunhofer Lizenz - already at 169w, push to 280+
write_doc(f"{BASE}/09_IP_Patente/IP_002_Lizenzvertrag_Fraunhofer_Inlicensing.docx", H,
    "Lizenzvertrag (In-Licensing) – Fraunhofer-Institut IPA – KI-Algorithmus Cardevio",
    subtitle="Patent EP 3 421 089 B1 – Auswertelogik EKG-Mehrkanal",
    sections=[
        ("Parteien",
         "Lizenzgeberin: Fraunhofer-Gesellschaft zur Foerderung der angewandten Forschung e.V., "
         "Hansastrasse 27c, 80686 Muenchen (vertreten durch das Fraunhofer-Institut IPA, Stuttgart).\n\n"
         "Lizenznehmerin: Sentavia Precision GmbH."),
        ("Lizenzgegenstand",
         "Exklusive (nicht ausschliessliche, aber bevorrechtigte) Lizenz an dem Patent EP 3 421 089 B1 "
         "und allen nationalen Validierungen (DE, FR, GB, IT, ES, NL, BE, AT, CH) sowie korrespondierenden "
         "internationalen Anmeldungen (US 10 482 105 B2; CN 109 245 088 B). Lizenzfeld: Anwendung in "
         "kardiologischer Diagnostik (Klasse IIb MDR / FDA Class III)."),
        ("Lizenzgebuehren",
         ("clauses", [
             ("§ 1 Initialgebuehr", [
                 "Einmalige Initialgebuehr in Hoehe von 320.000 EUR (zahlbar binnen 30 Tagen nach Vertragsunter"
                 "zeichnung).",
             ]),
             ("§ 2 Lizenz-Royalties", [
                 "Laufende Lizenzgebuehren in Hoehe von 4,5 % vom Netto-Verkaufspreis der lizenzgeschuetzten "
                 "Produkte (Cardevio Pro und ggfs. Nachfolgeprodukte).",
                 "Mindestlizenzgebuehren: Jahr 1 = 80.000 EUR; ab Jahr 2 = 200.000 EUR p. a.",
                 "Verguetungs-Cap bei 1,2 Mio. EUR p. a. (jaehrlich); bei Ueberschreiten wird der Royalty-Satz "
                 "auf 2,5 % reduziert.",
             ]),
             ("§ 3 Berichterstattung", [
                 "Halbjaehrlich vorzulegende Lizenzabrechnung; Pruefungsrecht der Lizenzgeberin (max. 1x p. a., "
                 "Vorlauf 30 Tage). Aufbewahrungsfrist der Verkaufsunterlagen: 5 Jahre.",
             ]),
         ])),
        ("Patenterhaltung",
         "Lizenzgeberin haelt die Patente waehrend der Lizenzlaufzeit aufrecht (Jahresgebuehren). "
         "Verteidigung bei Verletzung: vorrangig Lizenznehmerin (mit Information Lizenzgeberin); "
         "Kostenteilung nach Vereinbarung."),
        ("Laufzeit / Beendigung",
         "Laufzeit bis zum Ablauf der lokalen Patente (laengste Schutzfrist: 2034). Bei wesentlichen "
         "Vertragsverletzungen ist eine ausserordentliche Kuendigung mit Frist 90 Tage moeglich."),
        ("Unterschriften",
         signatures("Dr. Katharina Berger", "CEO", B["name"],
                    "Prof. Dr.-Ing. Marco Huber", "Institutsleiter Fraunhofer IPA", "Fraunhofer-Gesellschaft",
                    place="Muenchen / Stuttgart", date_str_="14. September 2022")),
    ])


# ── 11_Immobilien: Leasingvertrag Prüfausrüstung ──────────────────────────
write_doc(f"{BASE}/11_Immobilien/PROP_003_Leasingvertrag_Pruefausruestung.docx", H,
    "Leasingvertrag Pruefausruestung – Atlas Copco Industriedienstleistungen GmbH",
    subtitle="Operating-Lease Reinraum-Pruefausruestung 2023-2028",
    sections=[
        ("Parteien",
         "Leasinggeberin: Atlas Copco Industriedienstleistungen GmbH, Langemarckstrasse 35, 45141 Essen.\n\n"
         "Leasingnehmerin: Sentavia Precision GmbH."),
        ("Leasinggegenstand",
         "Reinraum-Pruefausruestung der Reinraum-Klasse ISO 14644-1 Klasse 7 (Produktion / FAT): "
         "Helium-Lecktester Pfeiffer Smartline HL3, Roentgenpruefanlage Comet MXR (fuer Implantatpruefung), "
         "Pruefkabine fuer EMV-Pruefungen (CE Anhang II Anwendung MDR Klasse IIb), Klimakammern (4 Stueck) "
         "fuer Stresstest. Gesamtwert 1,84 Mio. EUR."),
        ("Konditionen",
         "Leasingrate: 38.420 EUR netto monatlich; Laufzeit 60 Monate; Kaufoption am Ende Restwert "
         "180.000 EUR (oder Verlaengerungsoption). Service-Levels: Reaktion 24/7 P1 = 8 Std., P2 = 24 Std. "
         "Wartung im Leasing inkludiert (jaehrlich, Atlas Copco Service-Mitarbeitende vor Ort).\n\n"
         "Versicherung: Maschinenbruchversicherung ueber Allianz SE; Selbstbeteiligung 5.000 EUR. "
         "Standortbeschraenkung: Geraete duerfen nur in den von BTP angemieteten Reinraum-Bereichen "
         "Freimannstrasse 45 betrieben werden."),
        ("Buchhalterische Behandlung",
         "Operating-Lease nach HGB-Wahlrecht; buchungstechnisch off-balance. IFRS 16 nicht relevant "
         "(HGB-Einzelabschluss). Leasingaufwand wird linear auf 60 Monate verteilt."),
        ("Kuendigung",
         "Vorzeitige Rueckgabe zulaessig ab Monat 36 mit 12 Monatsraten Aufloesungsgebuehr. "
         "Ausserordentliche Kuendigung bei wesentlichen Vertragsverletzungen."),
        ("Unterschriften",
         signatures("Thomas Mueller", "CFO", B["name"],
                    "Markus Lendle", "Senior Account Manager", "Atlas Copco Industriedienstleistungen GmbH",
                    place="Muenchen / Essen", date_str_="14. Juli 2023")),
    ])


# ── 12_IT_Digital: 4 docs ──────────────────────────────────────────────────
def it_policy(fname, title, beschreibung, kernpunkte, verantwortlich, geltung):
    write_doc(f"{BASE}/12_IT_Digital/{fname}", H, title,
        subtitle=f"Verbindlich ab {geltung}",
        sections=[
            ("Zweck",
             beschreibung),
            ("Kernregelungen", ("list", kernpunkte)),
            ("Geltungsbereich",
             "Diese Richtlinie gilt fuer alle Mitarbeitenden, externen Dienstleister, Praktikanten und "
             "Studierenden, die mit IT-Systemen der Sentavia Precision GmbH arbeiten. Sie ergaenzt die "
             "internen ISMS-Richtlinien und die Vorgaben aus IEC 62443 (Industrial Security) sowie "
             "IEC 81001-5-1 (Cybersecurity Medizinprodukte)."),
            ("Verstoss / Sanktion",
             "Verstoesse gegen diese Richtlinie koennen arbeitsrechtliche Konsequenzen haben "
             "(Abmahnung bis ausserordentliche Kuendigung). Bei Vorsatz oder grober Fahrlaessigkeit "
             "behaelt sich die Gesellschaft zivil- und strafrechtliche Schritte vor."),
            ("Verantwortlich", verantwortlich),
        ])

it_policy("IT_024_MDM_Policy.docx", "Mobile Device Management (MDM) Policy",
    "Diese Richtlinie regelt die Nutzung mobiler Endgeraete (Smartphones, Tablets) im Kontext der "
    "Sentavia Precision GmbH. Alle Geraete, die auf BTP-Daten zugreifen, muessen ueber das Microsoft "
    "Intune MDM-System registriert und konfiguriert sein.",
    [
        "Pflichten Mitarbeitende: Anmeldung des Endgeraets im MDM bei Beschaeftigungsbeginn; "
        "Sofortmeldung bei Verlust oder Diebstahl an IT-Hotline.",
        "Konfiguration: PIN/Biometrie verpflichtend; Geraetespeicher-Verschluesselung; automatische "
        "Bildschirmsperre nach 5 Min.; Drittanbieter-Apps nur aus zugelassenem Application-Store.",
        "Datenbereich-Containerisierung: BTP-Daten (E-Mail, Sharepoint, Teams) in einem geschuetzten "
        "Container; private Apps und Daten haben keinen Zugriff darauf.",
        "Remote Wipe Faehigkeit: bei Verlust / Mitarbeiteraustritt kann der BTP-Container ohne Auswirkung "
        "auf private Daten geloescht werden.",
        "BYOD (Bring Your Own Device) zulaessig nach Anmeldung und schriftlicher Einverstaendnis"
        "erklaerung (Anlage 1); zum BTP-Container gilt das BTP-Datenschutz- und Sicherheitsregime.",
        "OS-Updates: Geraete muessen aktuellen Sicherheitsstand haben (max. 1 Major-Release zurueck); "
        "MDM erzwingt Updates.",
        "Risikoklassifizierung: Geraete der Geschaeftsfuehrung / F&E / Klinik werden mit erhoehter "
        "Sicherheitsstufe konfiguriert (Hardware-Token, Conditional Access).",
    ],
    "IT-Leitung (Markus Helmer); externer Cybersecurity-Beauftragter Dr. Hartmut Krieger (extern, "
    "BTC Business Technology Consulting AG).", "1. April 2024")

it_policy("IT_005_Sicherheitskonzept_2024.docx", "IT-Sicherheitskonzept 2024",
    "Das Sicherheitskonzept der Sentavia Precision GmbH orientiert sich an BSI IT-Grundschutz, "
    "ISO 27001 (in Vorbereitung Zertifizierung 2025) sowie den spezifischen Anforderungen der "
    "Medizinprodukteindustrie (IEC 81001-5-1, MDCG 2019-16 Cybersecurity Guidance). Schutzbedarfsklassen: "
    "Verfuegbarkeit (sehr hoch fuer Produktion / Vigilance), Integritaet (sehr hoch fuer klinische Daten / "
    "Regulatory), Vertraulichkeit (sehr hoch fuer Patentanmeldungen / klinische Daten).",
    [
        "Zero-Trust-Architektur: keine implizite Vertrauensstellung; jeder Zugriff wird kontextbezogen "
        "geprueft (Microsoft Entra ID Conditional Access).",
        "Netzwerk-Segmentierung: Office, F&E, Produktion (Reinraum), Klinik (REDCap) in separaten VLANs "
        "mit dedizierten Firewalls.",
        "EDR (Endpoint Detection & Response): CrowdStrike Falcon auf allen Endpoints, 24/7 Monitoring "
        "ueber SOC-as-a-Service (Sopra Steria).",
        "SIEM: zentrale Log-Sammlung Splunk Cloud; Anomalie-Detektion mit ML; Alerts an SOC.",
        "Patch-Management: monatlicher Patch-Cycle Windows / Linux; Sicherheits-Patches binnen 72 Std.",
        "Pflichtschulung: jaehrlich 60 Min. Awareness-Training; quartalsweise Phishing-Simulationen.",
        "Audit-Programm: jaehrliches internes Audit; externes Audit alle 24 Mo. (zuletzt SySS GmbH 2023).",
        "Incident-Response-Plan: definierte Eskalationsstufen; Krisenstab-Aktivierung bei P1-Vorfaellen.",
        "Datenschutz: enge Verzahnung mit DSB Dr. Markus Lehmann; AVV-Verzeichnis vollstaendig.",
    ],
    "IT-Leitung (Markus Helmer); Informationssicherheitsbeauftragter ISB.",
    "1. Februar 2024")

it_policy("IT_006_Disaster_Recovery_Plan_ENTWURF.docx", "Disaster-Recovery-Plan (ENTWURF v0.9)",
    "Dieser Disaster-Recovery-Plan (DRP) regelt die Wiederherstellung der kritischen IT-Systeme der "
    "Sentavia Precision GmbH im Falle eines Disaster-Events (Ausfall Rechenzentrum, Ransomware, "
    "physische Beschaedigung). Status: ENTWURF v0.9 zur Beirats-Pruefung; finale Freigabe in Q2/2024.",
    [
        "Klassifizierung kritischer Systeme: Klasse A (SAP, MasterControl QMS, REDCap, AD) RTO 4 Std., "
        "RPO 1 Std.; Klasse B (CRM, Outlook, Sharepoint) RTO 24 Std., RPO 4 Std.; Klasse C (Tools) "
        "RTO 5 WT, RPO 24 Std.",
        "Backup-Strategie: 3-2-1-Regel (3 Kopien, 2 Medien, 1 off-site). Off-site-Backup bei AWS "
        "Frankfurt (Region eu-central-1). Verschluesselung at-rest und in-transit (AES-256).",
        "Wiederanlauf-Verfahren: dokumentiert in Runbooks (Sharepoint /it/runbooks). Test halbjaehrlich.",
        "Externe Partner: Computacenter AG (Restore-Operations), Sopra Steria (Forensik bei Cyber-Vorfall).",
        "Eskalationspfad: IT-Leitung -> CFO -> CEO. Krisenkommunikation an Kunden / Notified Body / Behoerden.",
        "Geographic redundancy: bei langen Ausfaellen Failover auf AWS-Region eu-west-1 (Dublin) moeglich.",
        "Tabletop-Uebung jaehrlich; Letzte Uebung: 14. November 2023 (Szenario: Ransomware MasterControl).",
        "Update-Zyklus: DRP wird halbjaehrlich auf Aktualitaet geprueft; vollstaendige Ueberarbeitung 24 Mo.",
    ],
    "IT-Leitung (Markus Helmer); Beauftragter Risiko / Compliance Dr. Hartmut Krieger.",
    "geplant 1. Mai 2024")


# IT_003 Cybersecurity Policy Medizinprodukte – bereits 160w, push to 280+
write_doc(f"{BASE}/12_IT_Digital/IT_003_Cybersecurity_Policy_Medizinprodukte.docx", H,
    "Cybersecurity-Policy fuer Medizinprodukte (IEC 81001-5-1)",
    subtitle="Verbindlich ab 1. Januar 2024",
    sections=[
        ("Zweck",
         "Diese Policy regelt die Cybersecurity-Anforderungen an die von der Sentavia Precision GmbH "
         "in Verkehr gebrachten Medizinprodukte. Sie umfasst die Anforderungen aus der MDR (EU 2017/745), "
         "der IEC 81001-5-1 (Health software and health IT systems safety, effectiveness and security – "
         "Part 5-1: Security – Activities in the product life cycle) sowie der MDCG 2019-16 (Guidance on "
         "Cybersecurity for medical devices)."),
        ("Kern-Schutzziele",
         ("list", [
             "Vertraulichkeit (Confidentiality): Verhinderung des unautorisierten Zugriffs auf Patientendaten "
             "und Geraetekonfigurationen.",
             "Integritaet (Integrity): Erkennung und Verhinderung unautorisierter Aenderungen an Software / Daten.",
             "Verfuegbarkeit (Availability): Sicherstellung der bestimmungsgemaessen Funktion des Medizin"
             "produkts auch im Cybersecurity-Vorfall.",
             "Patientensicherheit: keine Cybersecurity-Vorfaelle, die zu Risiken fuer Patient:innen fuehren koennen.",
         ])),
        ("Anforderungen waehrend des gesamten Lebenszyklus",
         ("clauses", [
             ("§ 1 Design-Phase", [
                 "Security-by-Design: Bedrohungsmodellierung (Threat Modeling, STRIDE) ab Konzept-Phase.",
                 "Secure Coding Guidelines (OWASP Top 10, CWE Top 25) verbindlich fuer Software-Entwicklung.",
                 "Cybersecurity Risk Assessment gemaess AAMI TIR57 / FDA Pre-Market Cybersecurity Guidance.",
             ]),
             ("§ 2 Verifizierung & Validierung", [
                 "Static Code Analysis (SonarQube), Dependency Scanning (OWASP Dependency-Check).",
                 "Penetrationstest pro Major-Release vor Marktauslieferung (extern, durchgefuehrt SySS GmbH).",
                 "Software Bill of Materials (SBOM) – Pflicht ab MDR Annex IV.",
             ]),
             ("§ 3 Post-Market Surveillance", [
                 "Monitoring auf neue Schwachstellen (CVE-Feeds, US-CERT, ENISA).",
                 "Security-Patch-Versorgung fuer 10 Jahre nach Marktauslieferung.",
                 "Incident-Response-Prozess gemaess MDR Artikel 87 (Vigilance).",
             ]),
         ])),
        ("Verantwortlich",
         "CTO Dr. Marcus Vogt; Cybersecurity-Lead Felix Schaefer; externe Beratung BTC Business "
         "Technology Consulting AG. Schulungen jaehrlich verpflichtend fuer R&D Software und Hardware."),
    ])


# ── 13_Compliance_Recht: 10 thin docs ──────────────────────────────────────
def comp_richtlinie_btp(fname, title, schwerpunkte, verantwortlich, geltung):
    write_doc(f"{BASE}/13_Compliance_Recht/{fname}", H, title,
        subtitle=f"Verbindlich ab {geltung}; Anwendung in der gesamten BTP-Gruppe",
        sections=[
            ("Geltungsbereich",
             "Diese Richtlinie gilt fuer alle Beschaeftigten, Geschaeftsfuehrungsmitglieder, Praktikanten, "
             "Werkstudierenden und Leihkraefte der Sentavia Precision GmbH sowie deren Tochtergesellschaften "
             "(Sentavia Precision France S.A.S.). Sie ist auch von Dienstleistern, Beratern und Lieferanten "
             "zu beachten, soweit sie in den Geschaeftsraeumen oder im Auftrag der Gesellschaft taetig sind."),
            ("Wesentliche Regelungen", ("list", schwerpunkte)),
            ("Schulung und Compliance",
             "Alle Mitarbeitenden werden jaehrlich verpflichtend zu dieser Richtlinie geschult "
             "(e-Learning, Dauer ca. 25 Min.) und bestaetigen die Kenntnisnahme per Klick. Vertriebs- und "
             "Aussendienstmitarbeitende sowie die Geschaeftsfuehrung erhalten zusaetzlich jaehrlich eine "
             "Praesenzschulung."),
            ("Hinweisgebersystem",
             "Hinweise auf moegliche Verstoesse koennen ueber das vertrauliche Hinweisgebersystem 'SPEAK-UP@BTP' "
             "(extern gehostet, EQS Group AG) anonym oder offen erfolgen. Telefon-Hotline +49 800 555 33 22 "
             "(24/7). Es gelten die Regeln des HinSchG; Repression gegen meldende Personen ist verboten."),
            ("Verantwortlich",
             verantwortlich),
        ])


comp_richtlinie_btp("COMP_01_Anti-Korruptions-Richtlin.docx", "Anti-Korruptions-Richtlinie",
    ["Verbot der aktiven und passiven Bestechung im Privat- und Behoerdenverkehr (§§ 299, 332-334 StGB, "
     "FCPA, UKBA).",
     "Geschenke und Einladungen an HCPs (Health Care Professionals) nur im Rahmen der Vorgaben des "
     "Heilmittelwerbegesetzes (HWG, §§ 7, 7a) sowie der Berufsordnung der Aerzte (MBO-Ae § 32).",
     "Geschenke oberhalb 30 EUR an Aerzt:innen sind ausnahmslos unzulaessig.",
     "Einladungen zu Kongressen / Fortbildungen nur mit klarem fortbildungsbezogenem Mehrwert; "
     "keine Begleitperson, keine touristischen Programme.",
     "Vergutungsregelungen mit HCPs (Advisory Board, Referent, klinische Pruefer) gemaess "
     "transparenter Vertragsvorlage; Hoehe orientiert an angemessenem Stundensatz (Fair Market Value).",
     "Vertretungs- und Vermittler-Vertraege im Ausland (Frankreich, USA) durchlaufen Compliance-Due-Diligence."],
    "Compliance Officer (CO) Frau Andrea Schneider; rechtliche Begleitung Noerr PartGmbB.", "1. Januar 2024")

comp_richtlinie_btp("COMP_02_HWG-Compliance – Medizinp.docx", "HWG-Compliance Medizinprodukte",
    ["Beachtung des Heilmittelwerbegesetzes (HWG) bei Werbung gegenueber Fachkreisen und Publikum.",
     "Werbung gegenueber Patient:innen / Publikum (z. B. Webseite, Broschueren) erfordert klare, "
     "wissenschaftlich abgesicherte Aussagen; subjektive Heilversprechen sind verboten.",
     "Werbung gegenueber Fachkreisen (Aerzte, Kliniken) ist zulaessig, soweit sie sachlich, wahr und "
     "wissenschaftlich begruendet ist; klinische Studienreferenzen sind transparent darzustellen.",
     "Vor jeder Marketing-Aktion (Print, Web, Social Media, Messe) ist die Compliance-Freigabe einzuholen "
     "(BTP-Material-Reviewprozess, Tool COMPLIANT-Material).",
     "Schulung Marketing / Vertrieb / KAM jaehrlich verpflichtend.",
     "Bei Verstoss: Stilllegung der Massnahme, Korrektur, ggfs. Selbstanzeige bei Wettbewerbszentrale."],
    "Marketing-Leitung (Felix Schmidt) in Abstimmung mit Compliance Officer Andrea Schneider.", "1. Juli 2023")

comp_richtlinie_btp("COMP_03_MBO-Ä und Antikorruptions.docx", "MBO-Ä und Antikorruptionsstrafrecht",
    ["Verbot von Zuwendungen jeder Art (Geld, Vorteile, Sachleistungen) an Aerzt:innen, die im "
     "Zusammenhang mit der Verschreibung / Empfehlung / Anwendung von BTP-Medizinprodukten stehen.",
     "Beachtung der Musterberufsordnung der Aerzte (MBO-Ae § 32) sowie der einschlaegigen Strafvorschriften "
     "§§ 299a, 299b StGB (Bestechung / Bestechlichkeit im Gesundheitswesen).",
     "Zulaessig sind: angemessen verguterte Beratungs- und Referenten-Honorare auf Basis schriftlicher "
     "Vertraege (Anlage 1); Fortbildungsfinanzierungen ohne touristischen Charakter; freie wissenschaftliche "
     "Spenden an Kliniken (nur mit GF-Freigabe).",
     "Vorgabe Beratungsvertrag: Tagessatz max. 1.800 EUR (Top-Senior-HCP), 1.200 EUR (Senior-HCP), 800 EUR (HCP). "
     "Pruefung gegen Mexikanische Pharmaverbands-Standards / EFPIA Disclosure Code.",
     "Verstoesse koennen arbeitsrechtliche und strafrechtliche Konsequenzen haben."],
    "Compliance Officer Andrea Schneider, in Abstimmung mit Anwalt Noerr (Dr. Lara Walther) und der CMO Dr. Annika Schmidt.",
    "1. Januar 2024")

comp_richtlinie_btp("COMP_04_Code of Conduct.docx", "Code of Conduct (Verhaltensregeln)",
    ["Wir achten die Wuerde und das Selbstbestimmungsrecht jedes Menschen, insbesondere von Patient:innen.",
     "Wir handeln integer, transparent und gemaess geltendem Recht.",
     "Wir achten Compliance-Vorgaben (HWG, MBO-Ae, Anti-Korruption, DSGVO, MDR/IVDR).",
     "Wir foerdern Diversitaet und schaffen ein diskriminierungsfreies Arbeitsumfeld (keine Diskriminierung "
     "aufgrund Geschlecht, Alter, Herkunft, Religion, sexueller Orientierung, Behinderung).",
     "Wir sind Steward unseres Planeten: Umweltbewusstes Verhalten und Reduktion des CO2-Fussabdrucks.",
     "Wir respektieren Menschenrechte in unserer Lieferkette gemaess LkSG (auch wenn nicht formal pflichtig).",
     "Wir trennen Privates von Beruflichem (keine Interessenkonflikte) und melden Konflikte proaktiv.",
     "Wir nutzen Unternehmensressourcen sorgsam und ausschliesslich fuer betriebliche Zwecke."],
    "Compliance Officer Andrea Schneider; Verhaltenscharta Bestandteil des Arbeitsvertrages.",
    "1. Januar 2024")

comp_richtlinie_btp("COMP_05_Interessenkonflikt-Richtl.docx", "Interessenkonflikt-Richtlinie",
    ["Beschaeftigte und Geschaeftsfuehrungsmitglieder sind verpflichtet, alle bestehenden oder potenziellen "
     "Interessenkonflikte unverzueglich offen zu legen.",
     "Ein Interessenkonflikt liegt insbesondere vor bei: persoenlicher Beziehung zu Lieferanten / Kunden / "
     "Pruefenden; Nebentaetigkeiten bei Wettbewerbern; finanzieller Beteiligung an Geschaeftspartnern; "
     "Familienangehoerige bei Geschaeftspartnern.",
     "Pflicht zur Offenlegung: schriftlich an Compliance Officer (interessenkonflikt@sentavia-precision.de); "
     "jaehrliche Pflichterklaerung Geschaeftsfuehrung und C-Level.",
     "Nach Pruefung: Verbot der Beteiligung an entsprechenden Geschaefts-/Auswahlentscheidungen; "
     "ggfs. Massnahmen zur Vermeidung (z. B. Funktionswechsel, Auflage der Auflage).",
     "Geschenke / Einladungen von Geschaeftspartnern: nicht ueber 30 EUR Wert ohne vorherige Anzeige.",
     "Verstoss kann arbeitsrechtliche Konsequenzen haben (bis ausserordentliche Kuendigung)."],
    "Compliance Officer Andrea Schneider.", "1. Januar 2024")

comp_richtlinie_btp("COMP_06_Sanktionslisten-Screening.docx", "Sanktionslisten-Screening-Richtlinie",
    ["Vor jeder Geschaeftsbeziehung (Kunden, Lieferanten, Berater, externe Mitarbeitende) erfolgt ein "
     "Sanktionslisten-Screening gegen die einschlaegigen Listen: EU-Konsoldierte Liste, OFAC SDN List, "
     "UK HM Treasury Consolidated List, UN Security Council Consolidated List.",
     "Tool: 'ComplyCube' Sanctions Screening; tagliche Aktualisierungen.",
     "Treffer-Behandlung: bei Match wird der Geschaeftsvorgang gestoppt und sofort an Compliance Officer "
     "eskaliert. Pruefung durch externe Anwaltskanzlei Noerr.",
     "Geographische Risikolaender: erhoehte Sorgfalt bei Russland, Belarus, Iran, Nordkorea, Syrien, Kuba; "
     "Geschaefte mit diesen Laendern grundsaetzlich nicht zulaessig (Ausnahme: humanitaere Lieferungen "
     "mit GF-Freigabe).",
     "Schulung Vertrieb / Aussendienst / Einkauf jaehrlich verpflichtend.",
     "Audit-Trail: Screening-Ergebnisse werden 7 Jahre archiviert (BAFA-Anforderungen)."],
    "Compliance Officer Andrea Schneider; technische Umsetzung IT-Leitung Markus Helmer.",
    "1. Januar 2024")

comp_richtlinie_btp("COMP_07_Datenschutzrichtlinie _DS.docx", "Datenschutzrichtlinie (DSGVO / BDSG)",
    ["Sentavia Precision GmbH ist Verantwortliche i. S. d. Art. 4 Nr. 7 DSGVO. Externer Datenschutzbeauftragter "
     "(DSB) ist Dr. Markus Lehmann (Lehmann & Partner Datenschutzberatung GmbH).",
     "Verarbeitungstaetigkeiten sind im Verfahrensverzeichnis (Art. 30 DSGVO) dokumentiert; jaehrliche Aktualisierung.",
     "Auftragsverarbeitungsvertraege (AVV) mit allen relevanten Auftragsverarbeitern (Microsoft, Salesforce, "
     "REDCap-Hoster, AWS, ECS).",
     "Datenschutz-Folgenabschaetzungen (DSFA) fuer hohe Risiken (klinische Daten REDCap, Beschaeftigtendaten "
     "Sage HR).",
     "Betroffenenrechte (Auskunft, Loeschung, Widerspruch) ueber datenschutz@sentavia-precision.de.",
     "Meldepflichten Datenschutzverletzung an Bayerisches Landesamt fuer Datenschutzaufsicht (BayLDA) "
     "innerhalb von 72 Stunden.",
     "Spezialfall klinische Daten: Pseudonymisierung obligatorisch; Datenhaltung primaer im EU-Raum.",
     "Schulung aller Mitarbeitenden jaehrlich (60 Min. e-Learning + Onboarding).",
     "Audit jaehrlich durch DSB (zuletzt 18. November 2023, ohne wesentliche Beanstandungen)."],
    "DSB Dr. Markus Lehmann (extern); intern: Compliance Officer Andrea Schneider und IT-Leitung Markus Helmer.",
    "1. Januar 2024")

comp_richtlinie_btp("COMP_08_Social Media Policy.docx", "Social Media Policy",
    ["Die Mueller-Maschinenbau, vertreten durch Mitarbeitende, sowie der offizielle BTP-Auftritt auf "
     "LinkedIn / Xing / YouTube / Twitter sind professionell und sachlich zu betreiben.",
     "Persoenliche Aeusserungen ueber das Unternehmen, Patient:innen, Studienergebnisse oder Wettbewerber "
     "sind ohne Freigabe der PR-Abteilung untersagt.",
     "Werbung gegenueber Patient:innen mit Aussagen ueber konkrete Heilerfolge ist HWG-konform zu pruefen.",
     "Klinische Daten oder Pruefergebnisse duerfen NICHT vor offizieller Publikation kommuniziert werden "
     "(Embargo-Pflicht).",
     "Tags / Markierungen von Aerzt:innen / KOLs nur mit deren expliziter Zustimmung.",
     "Verstoesse werden im Rahmen der Antikorruptions- / Compliance-Verfahren geahndet; in schweren Faellen "
     "rechtliche Schritte.",
     "Schulung Marketing, Vertrieb, GF / C-Level jaehrlich."],
    "Marketing-Leitung Felix Schmidt; Compliance Officer Andrea Schneider.", "1. Februar 2024")

# Other compliance docs
write_doc(f"{BASE}/13_Compliance_Recht/COMP_DSGVO_Einwilligung_Prozess.docx", H,
    "DSGVO-Einwilligungsprozess (intern)",
    subtitle="Beschreibung des Einwilligungsmanagements gemaess Art. 7 DSGVO",
    sections=[
        ("Zweck",
         "Diese Verfahrensanweisung regelt den Einwilligungsprozess fuer Verarbeitungstaetigkeiten der "
         "Sentavia Precision GmbH, die auf Art. 6 Abs. 1 lit. a DSGVO (Einwilligung) gestuetzt sind. "
         "Anwendungsbereiche: Marketing-Newsletter, Bewerbungsverfahren (laengere Aufbewahrung), "
         "klinische Studien (im Rahmen ICH GCP), Mitarbeiter-Foto-Veroeffentlichungen."),
        ("Anforderungen an die Einwilligung",
         ("list", [
             "Freiwilligkeit: keine Kopplung an Vertragserfuellung (es sei denn unbedingt erforderlich).",
             "Informiertheit: klare Information ueber Zweck, Datenverarbeiter, Dauer, Widerrufsmoeglichkeit.",
             "Bestimmtheit: Einwilligung muss zweckbezogen sein (kein 'Block-Consent').",
             "Eindeutigkeit: aktive Handlung (z. B. Anklicken eines Kontrollkaestchens); kein Opt-Out.",
             "Schriftform empfehlenswert (Online: Tracking der Einwilligungstransaktion mit Zeitstempel)."
         ])),
        ("Prozess",
         "Schritt 1: Identifikation der Verarbeitung (durch verantwortlichen Fachbereich). "
         "Schritt 2: Erstellung des Einwilligungstextes durch DSB; rechtliche Pruefung. "
         "Schritt 3: Technische Implementierung im jeweiligen Tool (Mailchimp Newsletter, Workday "
         "Bewerbung, REDCap Studie). "
         "Schritt 4: Speicherung der Einwilligung mit Zeitstempel und IP-Adresse (gemaess Beweislast). "
         "Schritt 5: Widerrufsmoeglichkeit jederzeit muehelos (One-Click-Unsubscribe).\n\n"
         "Verantwortlich: DSB Dr. Markus Lehmann; technische Umsetzung IT-Leitung Markus Helmer."),
        ("Audit-Trail",
         "Saemtliche Einwilligungen werden im DSB-Audit-Tool dokumentiert. Loeschung erfolgt automatisch "
         "12 Monate nach Widerruf bzw. Zweckwegfall."),
    ])

write_doc(f"{BASE}/13_Compliance_Recht/COMP_HinSchG_Hinweisgebersystem_Richtlinie.docx", H,
    "Hinweisgebersystem-Richtlinie (HinSchG)",
    subtitle="Umsetzung des Hinweisgeberschutzgesetzes; in Kraft ab 17. Dezember 2023",
    sections=[
        ("Zweck",
         "Diese Richtlinie regelt das interne Hinweisgebersystem 'SPEAK-UP@BTP' der Sentavia Precision GmbH "
         "gemaess Hinweisgeberschutzgesetz (HinSchG, in Kraft seit 02.07.2023). Die Pflicht zur Einrichtung "
         "eines Meldekanals besteht aufgrund der Mitarbeiterzahl ab 50 Mitarbeitenden (BTP zaehlt > 600)."),
        ("Meldemoeglichkeiten",
         ("list", [
             "Web-Formular: https://speakup-btp.eqs.com (anonym oder offen)",
             "Telefon-Hotline: +49 800 555 33 22 (24/7, mehrsprachig: DE/EN/FR)",
             "Persoenliche Meldung beim Compliance Officer Andrea Schneider (Termin via compliance@sentavia-precision.de)",
             "Schriftlich postalisch an: Sentavia Precision GmbH, z. Hd. Compliance, Freimannstrasse 45, 80939 Muenchen",
         ])),
        ("Gewaehrleistung",
         "(a) Vertraulichkeit der Identitaet der hinweisgebenden Person; (b) Anonyme Meldungen sind moeglich; "
         "(c) Schutz vor Repressalien (Versetzung, Kuendigung, Diskriminierung); (d) Beweisumkehr bei "
         "behaupteten Repressalien; (e) Verbot von Geheimhaltungsklauseln, die das Recht zur Meldung "
         "beschneiden."),
        ("Bearbeitung",
         "Meldungen werden binnen 7 Tagen bestaetigt. Erste Rueckmeldung zur Bearbeitung erfolgt binnen "
         "3 Monaten. Pruefung durch unabhaengigen Compliance Officer; bei Verdacht auf schwere Vergehen "
         "Einschaltung externer Anwaltskanzlei Noerr und ggfs. Behoerden. Dokumentation gemaess HinSchG-"
         "Anforderungen (5-Jahres-Aufbewahrung)."),
        ("Externe Meldestellen",
         "BAFin (Finanzaufsicht), BAFA (Aussenhandel), BKartA (Kartell), Bundesamt fuer Justiz, "
         "Datenschutzbehoerden. Hinweisgebende Personen koennen sich auch direkt an diese externen Stellen "
         "wenden, ohne Pflicht zur vorherigen internen Meldung."),
        ("Verantwortlich",
         "Compliance Officer Andrea Schneider; externe technische Plattform EQS Group AG; "
         "externe rechtliche Beratung Noerr PartGmbB."),
    ])


print("OK regen_biotech_all.py – ~57 docs written")
