"""Müller / 01_Gesellschaftsrecht – batch B (Gesellschafterbeschluesse + Vollmachten + Erbfolge + Notar-Liste)."""
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

BASE = f"{_ROOT}/mueller_small/01_Gesellschaftsrecht"
H = {"name": M["name"], "addr": M["addr"], "hrb": M["hrb"]}


def beschluss(nr_year, title, subtitle_extra, sections_inner):
    """Common Gesellschafterbeschluss boilerplate frame."""
    praeambel = (
        f"Die Gesellschafter der Halbreiter Maschinenbau GmbH (HRB 47312, Amtsgericht Koeln) "
        f"haben in der heute am Sitz der Gesellschaft, Industriestrasse 12, 50829 Koeln, "
        f"abgehaltenen Gesellschafterversammlung den nachfolgenden Beschluss gefasst. "
        f"Anwesend bzw. wirksam vertreten waren saemtliche Gesellschafter: "
        f"Herr Klaus Mueller (60 % / 150 Geschaeftsanteile) und die Mueller Familien-GbR "
        f"(40 % / 100 Geschaeftsanteile), vertreten durch Herrn Klaus Mueller. "
        f"Das gesamte gezeichnete Stammkapital von 250.000 EUR war vertreten. "
        f"Auf Foermlichkeiten der Einberufung wurde im Sinne des § 51 Abs. 3 GmbHG einstimmig verzichtet."
    )
    schluss = (
        "Die Versammlung wird um 11:45 Uhr geschlossen. Das Protokoll wird in zweifacher Ausfertigung "
        "erstellt; je eine Ausfertigung verbleibt bei der Gesellschaft und der Familien-GbR. "
        "Eine Abschrift wird der Wirtschaftspruefung sowie dem rechtlichen Berater (Heuking Kuehn Lueer Wojtek) "
        "zur Vorlage zur Verfuegung gestellt."
    )
    return [
        ("Praeambel", praeambel),
        *sections_inner,
        ("Schlussfeststellung", schluss),
        ("Unterschriften",
         signatures("Klaus Mueller", "Gesellschafter (60 %)", M["name"],
                    "Klaus Mueller", "fuer Mueller Familien-GbR (40 %)", "Familien-GbR",
                    place="Koeln", date_str_=subtitle_extra)),
    ]


# ── GR_117 Gesellschafterbeschluss 2021 Erweiterung Geschaeftsfelder ────────
write_doc(
    f"{BASE}/GR_117_Gesellschafterbeschluss_2021_Erweiterung_Geschäft.docx", H,
    "Gesellschafterbeschluss 2021/04 – Erweiterung Geschaeftsfelder (Lasermaschinen, Robotik)",
    subtitle="Beschluss-Nr. 2021/04 vom 17. Mai 2021",
    sections=beschluss("2021/04", "Erweiterung", "17. Mai 2021", [
        ("1. Ausgangslage",
         "Die Geschaeftsfuehrung legt einen Strategievorschlag vor, mit dem die Halbreiter Maschinenbau GmbH "
         "ihre traditionelle Kernkompetenz im Sondermaschinenbau um zwei strategische Geschaeftsfelder erweitert: "
         "(a) hochpraezise Laserschneidsysteme fuer den Karosserierohbau und (b) modulare Robotik-Zellen mit "
         "kollaborativen Robotern (Cobots) fuer die Endmontage. Hintergrund sind konkrete Anfragen der Bestandskunden "
         "ThyssenKrupp Steel Europe AG und Dürr AG sowie ein konkreter Pilotauftrag von Hella GmbH & Co. KGaA "
         "im Wert von 2,8 Mio. EUR.\n\n"
         "Eine vom CFO vorgelegte Investitionsrechnung sieht ueber den Planungshorizont 2021–2024 einen "
         "Investitionsbedarf von rund 4,2 Mio. EUR vor (CAPEX). Eine externe Marktanalyse durch Roland Berger "
         "(Bericht vom 12.04.2021) bestaetigt das jaehrliche Marktwachstum dieses Segments im DACH-Raum "
         "auf 7,5 % p. a."),
        ("2. Beschluss",
         ("clauses", [
             ("§ 1 Erweiterung des Geschaeftsgegenstands", [
                 "Die Gesellschafter beschliessen, den im § 2 des Gesellschaftsvertrages vom 14. Maerz 1985 "
                 "festgelegten Unternehmensgegenstand klarstellend dahingehend zu ergaenzen, dass auch "
                 "Laserbearbeitungsanlagen sowie robotergestuetzte Montagesysteme einschliesslich der "
                 "zugehoerigen Steuerungssoftware und Wartungsdienstleistungen erfasst sind.",
                 "Eine notarielle Aenderung des Gesellschaftsvertrages und Eintragung im Handelsregister "
                 "(Notarin Dr. Beate Hoffmann, Koeln) wird unverzueglich, spaetestens jedoch bis 31. Juli 2021, "
                 "veranlasst.",
             ]),
             ("§ 2 Investitionsfreigabe", [
                 "Die Geschaeftsfuehrung wird ermaechtigt, fuer den Aufbau der neuen Geschaeftsfelder bis zu "
                 "4,5 Mio. EUR CAPEX im Zeitraum 2021–2023 verbindlich zu beauftragen.",
                 "Die Finanzierung erfolgt zu rund 60 % aus operativem Cashflow und zu 40 % aus dem mit der "
                 "Deutschen Bank AG, Filiale Koeln, am 11. Maerz 2021 zugesagten Investitionsdarlehen ueber "
                 "3,0 Mio. EUR (Laufzeit 7 Jahre, Zinssatz 1,85 % p. a. fix).",
             ]),
             ("§ 3 Personal", [
                 "Es werden bis Ende 2022 21 zusaetzliche Vollzeitstellen geschaffen (12 in der Produktion, "
                 "5 in der Konstruktion, 4 im Vertrieb).",
                 "Mit dem Betriebsrat ist die Einrichtung einer separaten Kostenstelle 'BU Laser & Robotik' "
                 "sowie ein qualifikatorisches Schulungsprogramm zu vereinbaren.",
             ]),
             ("§ 4 Reporting", [
                 "Die Geschaeftsfuehrung berichtet halbjaehrlich ueber den Ramp-up; KPI: Auftragseingang, "
                 "Stundenproduktivitaet, Deckungsbeitrag II.",
             ]),
         ])),
    ]),
)


# ── GR_118 Gesellschafterbeschluss 2020 Investitionsfreigabe ────────────────
write_doc(
    f"{BASE}/GR_118_Gesellschafterbeschluss_2020_Investitionsfreigabe.docx", H,
    "Gesellschafterbeschluss 2020/02 – Investitionsfreigabe Pressenlinie PL-500 sowie Modernisierung Halle B",
    subtitle="Beschluss-Nr. 2020/02 vom 14. Februar 2020",
    sections=beschluss("2020/02", "InvestPL500", "14. Februar 2020", [
        ("1. Investitionsvorhaben",
         "Die Geschaeftsfuehrung legt dar, dass die in der Halle B betriebene Pressenlinie PL-300 aus dem Jahr 2004 "
         "das technische Lebensende erreicht hat und sich Stillstandskosten in 2019 auf 412.000 EUR summierten. "
         "Geplant ist die Beschaffung einer neuen hydraulischen Stanzpresse PL-500 (Eigenentwicklung) mit "
         "Pressenkraft 800 t, kombinierter Servo-Steuerung und IoT-Anbindung, einschliesslich Hallenertuechtigung "
         "(neuer Fundamentblock, Schallschutz, Hallenkran 16 t).\n\n"
         "Gesamtinvestitionsvolumen: 2,75 Mio. EUR (davon Maschine 1,95 Mio. EUR, Bau 0,55 Mio. EUR, "
         "Inbetriebnahme/Schulung 0,25 Mio. EUR). ROI 4,3 Jahre auf Basis des vom CFO erstellten Business Case "
         "(Beschluss-Anlage 1)."),
        ("2. Beschluss",
         ("clauses", [
             ("§ 1 Freigabe", [
                 "Die Gesellschafter erteilen die Investitionsfreigabe in Hoehe von bis zu 2,9 Mio. EUR "
                 "(inkl. 5 % Reserve fuer unvorhergesehene Aufwendungen).",
                 "Die Inbetriebnahme soll spaetestens am 30. November 2020 erfolgen.",
             ]),
             ("§ 2 Finanzierung", [
                 "Finanzierung zu 100 % aus dem mit der Deutschen Bank AG zugesagten Investitionskredit "
                 "ueber 3,0 Mio. EUR (KfW-Tilgungszuschuss erwartet: 75.000 EUR).",
             ]),
             ("§ 3 Berichterstattung", [
                 "Quartalsbericht zum Investitionsstatus an die Gesellschafter; ausserplanmaessige Sitzung "
                 "bei Budgetueberschreitung > 10 %.",
             ]),
         ])),
    ]),
)


# ── GR_119 Gesellschafterbeschluss 2019 Aenderung Gesellschaftsvertrag ─────
write_doc(
    f"{BASE}/GR_119_Gesellschafterbeschluss_2019_Änderung_Gesellschaf.docx", H,
    "Gesellschafterbeschluss 2019/03 – Aenderung Gesellschaftsvertrag (Wettbewerbsverbot, Vinkulierung, Beirat)",
    subtitle="Beschluss-Nr. 2019/03 vom 19. September 2019",
    sections=beschluss("2019/03", "GVAend", "19. September 2019", [
        ("1. Anlass",
         "Im Zuge der Vorbereitung einer moeglichen Beteiligung externer Investoren (Phase 'Family & Friends' "
         "fuer max. 10 %) sowie aus Anlass der vorweggenommenen Erbfolge an die Familien-GbR (Anteilsabtretung "
         "9. Juni 2014) erweist sich der bislang aus dem Jahr 1985 stammende Gesellschaftsvertrag in "
         "wesentlichen Punkten als anpassungsbeduerftig. Auf Empfehlung der Heuking Kuehn Lueer Wojtek "
         "(Memorandum vom 22. Juli 2019) werden insbesondere die Klauseln zur Vinkulierung, zum "
         "Wettbewerbsverbot der Gesellschafter und zur Einrichtung eines Beirats angepasst."),
        ("2. Aenderungen im Einzelnen",
         ("list", [
             "§ 8 (Verfuegungen ueber Geschaeftsanteile): Anteilsabtretungen beduerfen kuenftig der Zustimmung "
             "von Gesellschaftern, die mindestens 75 % des Stammkapitals vertreten. Eine Abtretung an "
             "Abkoemmlinge erster Linie sowie an Familienpoolgesellschaften bleibt zustimmungsfrei.",
             "§ 11 (Wettbewerbsverbot der Gesellschafter): Beteiligungen von Gesellschaftern an konkurrierenden "
             "Unternehmen im Maschinen- und Anlagenbau sind nur mit ausdruecklicher Zustimmung der "
             "Gesellschafterversammlung zulaessig.",
             "§ 14 (Beirat): Es wird ein dreikoepfiger Beirat (1 Familienvertreter, 2 externe Mitglieder mit "
             "ausgewiesener Industrieerfahrung) eingerichtet. Sitzungen mind. zweimal jaehrlich; Vorlage von "
             "Mehrjahresplanung und Strategiebericht zur Zustimmung.",
             "§ 15 (Ausschuettungspolitik): Mind. 50 % des Jahresueberschusses werden thesauriert, bis das "
             "Eigenkapital 35 % der Bilanzsumme erreicht. Mehr-Ausschuettungen erfordern qualifizierte Mehrheit.",
             "§ 17 (Schiedsklausel): Streitigkeiten aus dem Vertrag werden durch ein DIS-Schiedsgericht in "
             "Koeln entschieden.",
         ])),
        ("3. Beschluss",
         ("clauses", [
             ("§ 1 Annahme", [
                 "Die Gesellschafter beschliessen einstimmig die in Abschnitt 2 dargestellten Aenderungen.",
                 "Die Geschaeftsfuehrung wird ermaechtigt, die notarielle Beurkundung (Notarin Dr. Beate Hoffmann, "
                 "Koeln, UR-Nr. 218/2019) sowie die Anmeldung zum Handelsregister zu veranlassen.",
             ]),
             ("§ 2 Beirat", [
                 "Als erste externe Beiratsmitglieder werden bestellt: Herr Prof. Dr.-Ing. Bernhard Roth "
                 "(RWTH Aachen, Lehrstuhl Maschinenelemente) sowie Herr Dr. Joerg Wiebold "
                 "(ehem. CFO Voith Industrial Services).",
                 "Familienvertreterin: Frau Elke Mueller-Hartmann (Mueller Familien-GbR).",
             ]),
         ])),
    ]),
)


# ── GR_120 Gesellschafterbeschluss 2018 Ausschuettungsbeschluss ────────────
write_doc(
    f"{BASE}/GR_120_Gesellschafterbeschluss_2018_Ausschüttungsbeschlu.docx", H,
    "Gesellschafterbeschluss 2018/05 – Ergebnisverwendung 2017 / Ausschuettung",
    subtitle="Beschluss-Nr. 2018/05 vom 28. Juni 2018",
    sections=beschluss("2018/05", "Aussch2017", "28. Juni 2018", [
        ("1. Jahresabschluss 2017",
         "Der von der Geschaeftsfuehrung aufgestellte und durch BDO AG WPG (Bericht vom 18. April 2018) "
         "geprueft testierte Jahresabschluss 2017 weist folgende Eckdaten aus: Umsatz 39,8 Mio. EUR, "
         "Jahresueberschuss 2,38 Mio. EUR, Bilanzsumme 26,4 Mio. EUR, Eigenkapital 12,9 Mio. EUR (48,9 %). "
         "Der Pruefungsvermerk wurde uneingeschraenkt erteilt."),
        ("2. Ergebnisverwendungsbeschluss",
         ("clauses", [
             ("§ 1 Feststellung", [
                 "Die Gesellschafter stellen den Jahresabschluss 2017 in der vorliegenden Fassung einstimmig fest.",
             ]),
             ("§ 2 Ergebnisverwendung", [
                 "Der Jahresueberschuss in Hoehe von 2.380.413,52 EUR wird wie folgt verwendet:",
                 "(a) Einstellung in andere Gewinnruecklagen: 1.380.413,52 EUR (58,0 %);",
                 "(b) Ausschuettung an die Gesellschafter: 1.000.000,00 EUR (42,0 %), aufgeteilt entsprechend "
                 "der Beteiligungsverhaeltnisse: Klaus Mueller 600.000,00 EUR (60 %); Mueller Familien-GbR "
                 "400.000,00 EUR (40 %).",
                 "Die Auszahlung erfolgt am 10. Juli 2018 unter Einbehalt von Kapitalertragsteuer und "
                 "Solidaritaetszuschlag, soweit gesetzlich erforderlich.",
             ]),
             ("§ 3 Entlastung", [
                 "Den Geschaeftsfuehrern Klaus Mueller und Sandra Becker wird fuer das Geschaeftsjahr 2017 "
                 "Entlastung erteilt.",
             ]),
             ("§ 4 Wahl des Abschlusspruefers 2018", [
                 "Zum Abschlusspruefer fuer das Geschaeftsjahr 2018 wird erneut die BDO AG WPG, "
                 "Niederlassung Koeln, gewaehlt.",
             ]),
         ])),
    ]),
)


# ── GR_121 Gesellschafterbeschluss 2023 Freigabe Investitionspaket ─────────
write_doc(
    f"{BASE}/GR_121_Gesellschafterbeschluss_2023_Freigabe_Investition.docx", H,
    "Gesellschafterbeschluss 2023/06 – Freigabe Investitionspaket Q3/2023",
    subtitle="Beschluss-Nr. 2023/06 vom 11. September 2023",
    sections=beschluss("2023/06", "Inv2023Q3", "11. September 2023", [
        ("1. Investitionsvorhaben Q3/2023",
         "Die Geschaeftsfuehrung legt das ueberarbeitete Investitionsprogramm Q3/2023 vor "
         "(Gesamtvolumen 2,15 Mio. EUR, Anlage 1). Wesentliche Einzelvorhaben:"),
        ("2. Einzelmassnahmen",
         [
             ["Nr.", "Massnahme", "Investition (EUR)", "Inbetriebnahme", "ROI (Jahre)"],
             ["1", "Erweiterung Laserschneidanlage LS-800 um 5-Achs-Modul", "640.000", "Q2/2024", "3,8"],
             ["2", "Servicewagen-Flotte (12 Fzg.) inkl. Wechsel auf E-Fahrzeuge", "415.000", "Q4/2023", "n/a (TCO)"],
             ["3", "Erneuerung Stanzpresse Halle A (Retrofit Steuerung)", "320.000", "Q1/2024", "2,9"],
             ["4", "Erweiterung Foerderbandanlage FB-200 Linie 3", "285.000", "Q2/2024", "3,2"],
             ["5", "Photovoltaik-Aufdachanlage Verwaltungsgebaeude (220 kWp)", "245.000", "Q4/2023", "7,5 (EnergieKost)"],
             ["6", "MES-Pilot Halle B (Schritt 1 von 3)", "245.000", "Q1/2024", "n/a (Effizienz)"],
             ["", "Summe", "2.150.000", "", ""],
         ]),
        ("3. Beschluss",
         ("clauses", [
             ("§ 1", [
                 "Die Gesellschafter genehmigen das Investitionsprogramm Q3/2023 in Hoehe von "
                 "2,15 Mio. EUR vollumfaenglich.",
             ]),
             ("§ 2", [
                 "Die Geschaeftsfuehrung ist ermaechtigt, Einzelmassnahmen flexibel umzusetzen, "
                 "solange das Gesamtbudget nicht ueberschritten wird (+/− 8 % je Einzelposition zulaessig).",
             ]),
             ("§ 3", [
                 "Finanzierung erfolgt 50 % aus Cashflow und 50 % aus der bestehenden Investitionslinie "
                 "der Deutschen Bank AG.",
             ]),
         ])),
    ]),
)


# ── GR_008/009/010 Gesellschafterbeschluss Jahresabschluss ─────────────────
def jahresabschluss_beschluss(year_close, file_year, beschluss_nr, eckwerte, ausschuettung_eur, fnr, prev_year_pruefer="BDO AG WPG"):
    fname = f"{BASE}/GR_{fnr}_Gesellschafterbeschluss_{file_year}_Jahresabschluss_{year_close}.docx"
    write_doc(
        fname, H,
        f"Gesellschafterbeschluss – Feststellung Jahresabschluss {year_close}",
        subtitle=f"Beschluss-Nr. {beschluss_nr} vom {ds_str(file_year)}",
        sections=beschluss(beschluss_nr, "JA", ds_str(file_year), [
            ("1. Vorlage und Pruefungsergebnis",
             f"Die Geschaeftsfuehrung legt den vom Abschlusspruefer {prev_year_pruefer} "
             f"(Bestaetigungsvermerk vom {pruef_datum(file_year)}) uneingeschraenkt testierten "
             f"Jahresabschluss {year_close} (Bilanz, Gewinn- und Verlustrechnung, Anhang) sowie "
             f"den Lagebericht vor. Wesentliche Kennzahlen:"),
            ("2. Kennzahlen",
             [["Kennzahl", f"{year_close}", f"{int(year_close)-1}", "Veraenderung"]] + eckwerte),
            ("3. Beschluss",
             ("clauses", [
                 ("§ 1 Feststellung", [
                     f"Die Gesellschafter stellen den Jahresabschluss {year_close} der "
                     f"Halbreiter Maschinenbau GmbH einstimmig fest.",
                 ]),
                 ("§ 2 Ergebnisverwendung", [
                     f"Vom Jahresueberschuss {year_close} wird ein Betrag von {ausschuettung_eur} EUR "
                     f"als Ausschuettung an die Gesellschafter ausgekehrt; der verbleibende Betrag wird "
                     f"in die anderen Gewinnruecklagen eingestellt.",
                     "Die Ausschuettung erfolgt im Verhaeltnis 60/40 (Klaus Mueller / Mueller Familien-GbR) "
                     "und wird innerhalb von 30 Tagen ueber das Bankkonto bei der Deutschen Bank AG ausgezahlt.",
                 ]),
                 ("§ 3 Entlastung der Geschaeftsfuehrung", [
                     f"Den Geschaeftsfuehrern Klaus Mueller (CEO) und Sandra Becker (CFO) wird fuer "
                     f"das Geschaeftsjahr {year_close} Entlastung erteilt.",
                 ]),
                 ("§ 4 Wahl Abschlusspruefer", [
                     f"Zum Abschlusspruefer fuer das Geschaeftsjahr {int(year_close)+1} wird die "
                     f"{prev_year_pruefer} (Niederlassung Koeln) bestellt.",
                 ]),
             ])),
            ("4. Anlagen",
             "Anlage 1: Bilanz und GuV {year_close} (testiert)\n\n"
             "Anlage 2: Anhang und Lagebericht {year_close}\n\n"
             "Anlage 3: Pruefungsbericht des Abschlusspruefers".format(year_close=year_close)),
        ]),
    )


def ds_str(file_year):
    # rough: beschluss erfolgt im Folgejahr, Juni
    return {"2022": "23. Juni 2022", "2023": "27. Juni 2023", "2024": "25. Juni 2024"}[file_year]


def pruef_datum(file_year):
    return {"2022": "4. Mai 2022", "2023": "9. Mai 2023", "2024": "7. Mai 2024"}[file_year]


# 2021 -> Beschluss 2022
jahresabschluss_beschluss(
    "2021", "2022", "2022/03",
    eckwerte=[
        ["Umsatzerloese", "41,90 Mio. EUR", "39,80 Mio. EUR", "+5,3 %"],
        ["EBITDA", "4,80 Mio. EUR", "4,15 Mio. EUR", "+15,7 %"],
        ["EBIT", "2,95 Mio. EUR", "2,38 Mio. EUR", "+23,9 %"],
        ["Jahresueberschuss", "2,07 Mio. EUR", "1,72 Mio. EUR", "+20,3 %"],
        ["Bilanzsumme", "27,30 Mio. EUR", "26,40 Mio. EUR", "+3,4 %"],
        ["Eigenkapital", "13,40 Mio. EUR", "12,90 Mio. EUR", "+3,9 %"],
        ["EK-Quote", "49,1 %", "48,9 %", "+0,2 PP"],
        ["Mitarbeiter (FTE)", "218", "210", "+8"],
    ],
    ausschuettung_eur="800.000", fnr="008",
)

# 2022 -> Beschluss 2023
jahresabschluss_beschluss(
    "2022", "2023", "2023/04",
    eckwerte=[
        ["Umsatzerloese", "43,25 Mio. EUR", "41,90 Mio. EUR", "+3,2 %"],
        ["EBITDA", "5,10 Mio. EUR", "4,80 Mio. EUR", "+6,3 %"],
        ["EBIT", "3,22 Mio. EUR", "2,95 Mio. EUR", "+9,2 %"],
        ["Jahresueberschuss", "2,22 Mio. EUR", "2,07 Mio. EUR", "+7,2 %"],
        ["Bilanzsumme", "28,40 Mio. EUR", "27,30 Mio. EUR", "+4,0 %"],
        ["Eigenkapital", "14,10 Mio. EUR", "13,40 Mio. EUR", "+5,2 %"],
        ["EK-Quote", "49,6 %", "49,1 %", "+0,5 PP"],
        ["Mitarbeiter (FTE)", "231", "218", "+13"],
    ],
    ausschuettung_eur="900.000", fnr="009",
)

# 2023 -> Beschluss 2024
jahresabschluss_beschluss(
    "2023", "2024", "2024/04",
    eckwerte=[
        ["Umsatzerloese", "48,63 Mio. EUR", "43,25 Mio. EUR", "+12,4 %"],
        ["EBITDA", "5,98 Mio. EUR", "5,10 Mio. EUR", "+17,3 %"],
        ["EBIT", "3,89 Mio. EUR", "3,22 Mio. EUR", "+20,8 %"],
        ["Jahresueberschuss", "2,73 Mio. EUR", "2,22 Mio. EUR", "+22,8 %"],
        ["Bilanzsumme", "31,20 Mio. EUR", "28,40 Mio. EUR", "+9,9 %"],
        ["Eigenkapital", "16,90 Mio. EUR", "14,10 Mio. EUR", "+19,9 %"],
        ["EK-Quote", "54,2 %", "49,6 %", "+4,6 PP"],
        ["Mitarbeiter (FTE)", "247", "231", "+16"],
    ],
    ausschuettung_eur="1.100.000", fnr="010",
)


# ── GR_007 Prokura Erteilung ────────────────────────────────────────────────
write_doc(
    f"{BASE}/GR_007_Prokura_Erteilung.docx", H,
    "Erteilung Gesamtprokura – Frau Sandra Becker (CFO)",
    subtitle="Eintragung Handelsregister HRB 47312, AG Koeln",
    sections=[
        ("1. Beschluss der Gesellschafter",
         "Die Gesellschafter der Halbreiter Maschinenbau GmbH haben in der Gesellschafterversammlung vom "
         "10. Januar 2014 beschlossen, der seit dem 1. Januar 2014 als Geschaeftsfuehrerin und CFO "
         "taetigen Frau Sandra Becker, geboren 7. September 1977, wohnhaft Bonner Strasse 41, 50677 Koeln, "
         "zusaetzlich Gesamtprokura gemaess §§ 48 ff. HGB zu erteilen. Hintergrund ist die mit dem Erwerb "
         "der gewerblichen Trade-Mark-Lizenzen und der internationalen Vertretung verbundene Notwendigkeit, "
         "Frau Becker einen weiterreichenden, im Handelsregister sichtbaren Vertretungsrahmen zu geben."),
        ("2. Umfang",
         "Die Prokura wird als Gesamtprokura erteilt: Frau Becker vertritt die Gesellschaft gemeinsam "
         "mit dem Geschaeftsfuehrer Herrn Klaus Mueller oder gemeinsam mit einem weiteren Prokuristen.\n\n"
         "Die Prokura umfasst alle Arten von gerichtlichen und aussergerichtlichen Geschaeften und "
         "Rechtshandlungen, die der Betrieb des Handelsgewerbes mit sich bringt, einschliesslich der "
         "Belastung von Grundstuecken (§ 49 Abs. 2 HGB)."),
        ("3. Anmeldung Handelsregister",
         "Die Anmeldung der Prokura zum Handelsregister Koeln, HRB 47312, wurde durch den unterzeichnenden "
         "Geschaeftsfuehrer notariell beglaubigt (Notarin Dr. Beate Hoffmann, Koeln, UR-Nr. 18/2014 vom "
         "15. Januar 2014) eingereicht und am 23. Januar 2014 als Prokura eingetragen."),
        ("4. Innenverhaeltnis",
         "Im Innenverhaeltnis ist die Prokuristin verpflichtet, Geschaefte ueber 500.000 EUR Einzelvolumen "
         "der Geschaeftsfuehrung vorab zur Kenntnis zu bringen. Im Falle des Erwerbs, der Veraeusserung "
         "oder Belastung von Grundstuecken ist ein gesonderter Gesellschafterbeschluss einzuholen. "
         "Eine Verletzung dieser internen Beschraenkung wirkt nicht gegenueber Dritten."),
        ("5. Geltung",
         "Die Prokura gilt unbefristet und endet automatisch mit Beendigung der Geschaeftsfuehrer-Anstellung. "
         "Ein Widerruf kann jederzeit durch Gesellschafterbeschluss erfolgen und ist zum Handelsregister "
         "anzumelden."),
        ("Unterschriften",
         signatures("Klaus Mueller", "Geschaeftsfuehrer (CEO)", M["name"],
                    "Sandra Becker", "Prokuristin / Geschaeftsfuehrerin", M["name"],
                    place="Koeln", date_str_="15. Januar 2014")),
    ],
)


# ── GR_Vollmacht_Rechtsanwalt_Heuking ───────────────────────────────────────
write_doc(
    f"{BASE}/GR_Vollmacht_Rechtsanwalt_Heuking.docx", H,
    "Prozess- und Generalvollmacht – Heuking Kuehn Lueer Wojtek Partnerschaft mbB",
    subtitle="Wirksam ab 1. Januar 2024",
    sections=[
        ("1. Vollmachtgeberin",
         "Halbreiter Maschinenbau GmbH, vertreten durch die Geschaeftsfuehrer Klaus Mueller und Sandra Becker."),
        ("2. Bevollmaechtigte",
         "Heuking Kuehn Lueer Wojtek Partnerschaft mbB, Standort Koeln, Magnusstrasse 13, 50672 Koeln, "
         "vertreten durch die mandatsfuehrenden Rechtsanwaelte: Frau Dr. Sabine Erbach (Gesellschaftsrecht / M&A), "
         "Herr RA Dr. Maximilian Brandl (Arbeitsrecht), Herr RA Dr. Constantin Wilms (Litigation)."),
        ("3. Gegenstand der Vollmacht",
         "Die Bevollmaechtigte wird ermaechtigt, die Vollmachtgeberin in allen rechtlichen Angelegenheiten "
         "umfassend zu vertreten. Die Vollmacht umfasst insbesondere:\n\n"
         "(a) die Vertretung vor allen Gerichten und Behoerden samtlicher Instanzen einschliesslich "
         "Schiedsgerichten und Mediationsverfahren;\n\n"
         "(b) die Verhandlung, Pruefung und den Abschluss von Vertraegen (insbesondere Liefer-, Kunden-, "
         "Konzern- und Beteiligungsvertraege) im Rahmen einer fallbezogenen Beauftragung;\n\n"
         "(c) die Vertretung in arbeitsrechtlichen Streitigkeiten, Aufhebungs- und Sozialplan-Verhandlungen, "
         "Einigungsstellenverfahren sowie Einstweilige-Verfuegungs-Verfahren;\n\n"
         "(d) die Vertretung gegenueber Behoerden und Kartellbehoerden im Rahmen von M&A-Transaktionen, "
         "Fusionskontroll- und Beihilfeverfahren;\n\n"
         "(e) die Entgegennahme und Zustellung saemtlicher Schriftstuecke."),
        ("4. Untervollmacht",
         "Die Bevollmaechtigte ist berechtigt, im Rahmen der internen Mandatsfuehrung Untervollmachten "
         "an weitere Mitglieder der Sozietaet zu erteilen."),
        ("5. Honorierung und Mandat",
         "Die Honorierung erfolgt auf Grundlage des Mandatsvertrages vom 5. Januar 2014 (zuletzt geaendert "
         "am 10. Dezember 2023), in der Regel auf Basis von Stundensaetzen (Partner 540 EUR, Senior Associate "
         "390 EUR, Associate 280 EUR, jeweils zzgl. USt.). Pauschalvergaben sind im Einzelfall vereinbar."),
        ("6. Laufzeit",
         "Die Vollmacht gilt unbefristet bis auf jederzeitigen schriftlichen Widerruf. Sie ersetzt alle "
         "vorhergehenden Vollmachten an die Bevollmaechtigte."),
        ("Unterschriften",
         signatures("Klaus Mueller", "Geschaeftsfuehrer", M["name"],
                    "Sandra Becker", "Geschaeftsfuehrerin", M["name"],
                    place="Koeln", date_str_="2. Januar 2024")),
    ],
)


# ── GR_Erbfolgeklausel_Testament_Hinweis ───────────────────────────────────
write_doc(
    f"{BASE}/GR_Erbfolgeklausel_Testament_Hinweis.docx", H,
    "Hinweis – Erbfolgeregelung & Testamentaehnliche Verfuegungen Herr Klaus Mueller",
    subtitle="Interner Vermerk zur Nachlassplanung, Stand 4. November 2023",
    sections=[
        ("1. Zweck",
         "Der vorliegende interne Vermerk dokumentiert die im Hinblick auf die Anteile von Herrn "
         "Klaus Mueller (geb. 12.02.1963, 60 % / 150 Geschaeftsanteile) bestehende Nachfolgeplanung "
         "der Halbreiter Maschinenbau GmbH. Er soll im Rahmen einer Due Diligence den potentiellen "
         "Erwerbern bzw. Pruefern Auskunft zur Stabilitaet der Anteilseignerstruktur geben."),
        ("2. Gesellschaftsvertragliche Regelungen",
         "Der Gesellschaftsvertrag vom 14. Maerz 1985 (Fassung 19. September 2019) enthaelt in § 16 "
         "eine Erbfolgeklausel: Beim Tod eines Gesellschafters gehen dessen Geschaeftsanteile von "
         "Gesetzes wegen auf die jeweiligen Erben ueber; eine Einziehung kann nur erfolgen, wenn die "
         "Erben innerhalb von 12 Monaten keinen einheitlichen Bevollmaechtigten benennen oder die "
         "Gesellschaft durch das Verhalten der Erben in ihrer Geschaeftstaetigkeit ernsthaft beeintraechtigt wird."),
        ("3. Testament und Erbvertrag",
         "Herr Klaus Mueller hat ein notarielles Testament errichtet (Notar Dr. Friedrich Wagner, Koeln, "
         "UR-Nr. 411/2019 vom 4. Juli 2019), das die Familien-GbR zur Alleinerbin der Geschaeftsanteile "
         "einsetzt. Ergaenzend besteht ein Erbvertrag mit Frau Elke Mueller-Hartmann (Ehefrau) sowie "
         "den Toechtern Frau Carolin Mueller (geb. 1994) und Frau Lena Mueller (geb. 1997). Letztwillige "
         "Verfuegungen zugunsten Dritter ausserhalb der Familie bestehen nach Erklaerung des Notars nicht."),
        ("4. Familien-GbR",
         "Die Mueller Familien-GbR (gegruendet 8. Juni 2014) buendelt die Familienanteile dauerhaft. "
         "Geschaeftsfuehrer der GbR ist Herr Klaus Mueller; nachfolgend nach gesellschaftsvertraglicher "
         "Regelung der GbR Frau Elke Mueller-Hartmann und nachgelagert die juengere Tochter Frau Lena Mueller, "
         "die im Anschluss an ihr Ingenieurstudium an der TU Muenchen voraussichtlich ab 2026 in das "
         "Unternehmen eintritt."),
        ("5. Risiken / Empfehlungen",
         "Eine Pflichtteils-Konstellation gegenueber Dritten ist nicht zu erwarten. Im Rahmen der "
         "Nachlassplanung wird mit der Heuking Kuehn Lueer Wojtek (Memo vom 12.09.2023) eine "
         "lebzeitige Uebertragung weiterer 10 % bis 2026 unter Vorbehalt eines Niessbrauchsrechts "
         "geprueft, um Erbschaftsteuer-Implikationen zu glaetten."),
        ("Hinweis", "Dieses Dokument enthaelt sensible familienrechtliche Angaben und ist nur fuer den "
                    "Datenraum-Index Q-VR 'Confidential' freigegeben."),
    ],
)


# ── GR_Notarielle_Urkundenliste ─────────────────────────────────────────────
write_doc(
    f"{BASE}/GR_Notarielle_Urkundenliste.docx", H,
    "Notarielle Urkundenliste – Halbreiter Maschinenbau GmbH",
    subtitle="Vollstaendige Aufstellung notarieller Urkunden mit Bezug zur Gesellschaft, Stand 31. Dezember 2023",
    sections=[
        ("Hinweis",
         "Diese Aufstellung wurde aus den Akten der Geschaeftsfuehrung sowie aus den Bestaetigungen der "
         "beteiligten Notariate (Notar Dr. Helmut Vogel, Koeln / Notar Dr. Friedrich Wagner, Koeln / "
         "Notarin Dr. Beate Hoffmann, Koeln) erstellt. Sie umfasst alle die Gesellschaft betreffenden "
         "notariellen Vorgaenge seit Gruendung am 14. Maerz 1985."),
        ("Urkunden",
         [
             ["UR-Nr.", "Datum", "Notariat", "Gegenstand"],
             ["312/1985", "14.03.1985", "Dr. Helmut Vogel, Koeln", "Gruendung Halbreiter Maschinenbau GmbH, Stammkapital 100.000 DM"],
             ["89/1991",  "21.05.1991", "Dr. Helmut Vogel, Koeln", "Kapitalerhoehung auf 250.000 DM"],
             ["311/2001", "12.07.2001", "Dr. Helmut Vogel, Koeln", "Umstellung Stammkapital auf 250.000 EUR"],
             ["218/2014", "10.06.2014", "Dr. Friedrich Wagner, Koeln", "Anteilsabtretung Klaus Mueller -> Mueller Familien-GbR (40 %)"],
             ["482/2014", "9.06.2014",  "Dr. Friedrich Wagner, Koeln", "Gruendung Mueller Familien-GbR"],
             ["18/2014",  "15.01.2014", "Dr. Beate Hoffmann, Koeln", "Anmeldung Gesamtprokura Sandra Becker"],
             ["219/2017", "3.05.2017",  "Dr. Beate Hoffmann, Koeln", "Aenderung Gesellschaftsvertrag (Bilanzfeststellung)"],
             ["411/2019", "4.07.2019",  "Dr. Friedrich Wagner, Koeln", "Notarielles Testament Klaus Mueller"],
             ["218/2019", "20.09.2019", "Dr. Beate Hoffmann, Koeln", "Aenderung Gesellschaftsvertrag (Vinkulierung / Beirat)"],
             ["344/2020", "18.03.2020", "Dr. Beate Hoffmann, Koeln", "Grundschuldbestellung Industriestrasse 12 (Erweiterung Halle B)"],
             ["77/2021",  "23.04.2021", "Dr. Beate Hoffmann, Koeln", "Aenderung Gesellschaftsvertrag (Geschaeftszweck Laser/Robotik)"],
             ["156/2023", "12.07.2023", "Dr. Friedrich Wagner, Koeln", "Grundschuld zugunsten Deutsche Bank AG (Investitionslinie)"],
             ["219/2023", "11.10.2023", "Dr. Beate Hoffmann, Koeln", "Verpfaendung Geschaeftsanteile Nr. 1-80 (Deutsche Bank AG)"],
         ]),
        ("Erklaerung Geschaeftsfuehrung",
         "Die Geschaeftsfuehrung erklaert, dass nach bestem Wissen keine weiteren notariellen Urkunden mit "
         "Bezug zur Gesellschaft bestehen, die fuer einen potentiellen Erwerber von Bedeutung sein koennten. "
         "Eine Bestaetigung der Notariate ueber die Vollstaendigkeit wurde am 18. Dezember 2023 angefordert "
         "und liegt bei (Anlage 1).\n\nKoeln, den 22. Dezember 2023."),
        ("Unterschriften",
         signatures("Klaus Mueller", "Geschaeftsfuehrer", M["name"],
                    "Sandra Becker", "Geschaeftsfuehrerin", M["name"],
                    place="Koeln", date_str_="22. Dezember 2023")),
    ],
)


# ── GR_004 GF Anstellungsvertrag Klaus Mueller ─────────────────────────────
def gf_vertrag(name, geb_date, position, jahresgehalt, variabel_pct, bestellung_date, fname_suffix):
    write_doc(
        f"{BASE}/GR_{fname_suffix}.docx", H,
        f"Anstellungsvertrag Geschaeftsfuehrung – {name}",
        subtitle=f"in der Fassung vom {bestellung_date}",
        sections=[
            ("Vertragsparteien",
             f"Zwischen der Halbreiter Maschinenbau GmbH, Industriestrasse 12, 50829 Koeln, "
             f"vertreten durch die Gesellschafterversammlung (Beschluss vom {bestellung_date}) – "
             f"nachfolgend 'Gesellschaft' genannt – und Herrn/Frau {name}, geboren am {geb_date}, "
             f"– nachfolgend 'Geschaeftsfuehrer(in)' genannt – wird folgender Anstellungsvertrag geschlossen."),
            ("Praeambel",
             "Der/die Geschaeftsfuehrer(in) wird mit Wirkung des in § 2 genannten Datums zum Mitglied "
             "der Geschaeftsfuehrung der Gesellschaft bestellt. Der Anstellungsvertrag konkretisiert "
             "die korrespondierenden Rechte und Pflichten."),
            ("Vertragstext",
             ("clauses", [
                 ("§ 1 Aufgaben und Vertretungsbefugnis", [
                     f"Der/die Geschaeftsfuehrer(in) fuehrt die Geschaefte der Gesellschaft in der "
                     f"Funktion {position}. Die Aufgabenverteilung wird in einer von der Gesellschafterversammlung "
                     f"verabschiedeten Geschaeftsordnung geregelt (zuletzt: Geschaeftsordnung Geschaeftsfuehrung "
                     f"vom 19.09.2019, Anlage 1).",
                     "Der/die Geschaeftsfuehrer(in) ist im Aussenverhaeltnis einzelvertretungsbefugt und von "
                     "den Beschraenkungen des § 181 BGB befreit. Im Innenverhaeltnis gelten die "
                     "Zustimmungsvorbehalte gemaess Anlage 2 (insbesondere bei Investitionen ueber 500.000 EUR, "
                     "Krediteinraeumung, Veraeusserung wesentlicher Vermoegenswerte, Anteilsuebertragungen und "
                     "Personalmassnahmen oberhalb tariflicher Ebene).",
                 ]),
                 ("§ 2 Vertragsdauer", [
                     f"Der Vertrag beginnt am {bestellung_date} und ist auf unbestimmte Zeit geschlossen.",
                     "Die ordentliche Kuendigung ist beiderseits mit einer Frist von zwoelf Monaten zum Ende "
                     "eines Kalenderhalbjahres zulaessig. Die Bestellung als Geschaeftsfuehrer und der "
                     "Anstellungsvertrag sind rechtlich unabhaengig (sog. Trennungsprinzip).",
                 ]),
                 ("§ 3 Vergutung", [
                     f"Der/die Geschaeftsfuehrer(in) erhaelt ein Jahresbruttofixgehalt von {jahresgehalt} EUR, "
                     f"zahlbar in zwoelf gleichen Monatsraten jeweils nachschuessig.",
                     f"Zusaetzlich wird eine variable Vergutung (Tantieme) in Hoehe von bis zu {variabel_pct} % "
                     "des Jahresbruttofixgehalts gewaehrt. Bemessungsgrundlage sind die EBIT-Zielerreichung "
                     "(70 %) sowie individuelle Ziele (30 %), die von der Gesellschafterversammlung jaehrlich "
                     "vorab festgelegt werden.",
                     "Die Gesellschaft stellt einen Dienstwagen der oberen Mittelklasse (Listenpreis "
                     "bis 75.000 EUR brutto) auch zur privaten Nutzung; geldwerter Vorteil wird nach 1 %-Regel "
                     "versteuert.",
                     "Die Gesellschaft schliesst eine D&O-Versicherung mit einer Versicherungssumme von "
                     "10 Mio. EUR (Allianz SE) ab, der/die Geschaeftsfuehrer(in) ist mitversicherte Person; "
                     "der Selbstbehalt entspricht den Anforderungen des § 93 Abs. 2 S. 3 AktG analog "
                     "(10 % des Schadens, max. 150 % der Festvergutung).",
                 ]),
                 ("§ 4 Sonstige Leistungen", [
                     "Beitraege zur betrieblichen Altersversorgung in Hoehe von 12.000 EUR p. a. (Direktzusage), "
                     "Versorgungsregelung gemaess BetrAVG.",
                     "Krankheits- und Unfallzusatzversicherung (Top-Tarif), Beitraege werden von der Gesellschaft "
                     "uebernommen.",
                 ]),
                 ("§ 5 Urlaub und Arbeitszeit", [
                     "Jahresurlaub: 30 Arbeitstage. Eine feste Arbeitszeit besteht nicht; geschuldet ist die "
                     "Erfuellung der Aufgaben. Die Wahrnehmung von bis zu zwei Aufsichtsrats- oder "
                     "Beiratsmandaten ausserhalb der Gesellschaft ist nach vorheriger Anzeige zulaessig.",
                 ]),
                 ("§ 6 Wettbewerbsverbot", [
                     "Waehrend der Vertragsdauer besteht ein umfassendes Wettbewerbsverbot.",
                     "Nachvertraglich besteht fuer einen Zeitraum von zwoelf Monaten ein Wettbewerbsverbot "
                     "(Maschinenbau / Industrieautomation, raeumlich DACH); die Karenzentschaedigung betraegt "
                     "50 % des zuletzt bezogenen Jahresbruttofixgehalts.",
                 ]),
                 ("§ 7 Verschwiegenheit", [
                     "Verschwiegenheitspflicht ueber alle vertraulichen Informationen waehrend und unbefristet "
                     "nach Beendigung des Vertrages. Bei Verstoss kann eine Vertragsstrafe in Hoehe von bis zu "
                     "drei Bruttomonatsgehaeltern verhaengt werden; weitergehende Schadenersatzansprueche bleiben "
                     "unberuehrt.",
                 ]),
                 ("§ 8 Schlussbestimmungen", [
                     "Es gilt deutsches Recht. Gerichtsstand: Koeln. Aenderungen und Ergaenzungen beduerfen "
                     "der Schriftform; dies gilt auch fuer die Aufhebung der Schriftformklausel.",
                 ]),
             ])),
            ("Anlagen",
             "Anlage 1: Geschaeftsordnung Geschaeftsfuehrung\n\n"
             "Anlage 2: Zustimmungsbeduerftige Geschaefte\n\n"
             "Anlage 3: Zielvereinbarung Tantieme (jaehrlich)\n\n"
             "Anlage 4: D&O-Versicherungspolice (Allianz SE)"),
            ("Unterschriften",
             signatures("Klaus Mueller", "Vorsitzender Gesellschafterversammlung", "fuer die Gesellschaft",
                        name, position, "i. e. S.",
                        place="Koeln", date_str_=bestellung_date)),
        ],
    )


gf_vertrag("Klaus Mueller",  "12.02.1963", "CEO / Vorsitzender der Geschaeftsfuehrung",
           "320.000", "40", "10. Januar 2014", "004_GF_Anstellungsvertrag_Klaus_Müller")
gf_vertrag("Sandra Becker", "07.09.1977", "CFO / kaufm. Geschaeftsfuehrerin",
           "260.000", "30", "10. Januar 2014", "005_GF_Anstellungsvertrag_Sandra_Becker")

print("OK regen_mueller_01b.py")
