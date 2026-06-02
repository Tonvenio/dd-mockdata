"""Müller / 06_Immobilien, 07_IP_Lizenzen, 08_Versicherungen, 09_Compliance,
10_IT_Infrastruktur, 11_Strategie_Planung – sammelregeneration."""
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

D = f"{_ROOT}/mueller_small"
H = {"name": M["name"], "addr": M["addr"], "hrb": M["hrb"]}

# ──────────────────────────────────────────────────────────────────────────
# 06_Immobilien (10 docs)
# ──────────────────────────────────────────────────────────────────────────
B6 = f"{D}/06_Immobilien"

write_doc(f"{B6}/IMM_Grundriss_Verwaltungsgebäude.docx", H,
    "Grundriss Verwaltungsgebaeude – Industriestrasse 12, 50829 Koeln",
    subtitle="Stand 1. Februar 2024; Quelle: Architekturbuero Hammers + Partner, Koeln",
    sections=[
        ("Lage und Daten",
         "Verwaltungsgebaeude (Bauteil A) auf dem Grundstueck Industriestrasse 12, 50829 Koeln; Flurstueck "
         "Nr. 1278/13, Gemarkung Koeln-Niehl; Gesamtgrundstueck 18.420 m², bebaut 6.840 m². Drei Vollgeschosse "
         "+ DG (Technik). Baujahr 1985, Sanierung/Modernisierung 2018-2019 (Energie KfW 70)."),
        ("Flaechen je Geschoss",
         [["Geschoss", "Hauptnutzflaeche m²", "Nebenflaeche m²", "Mitarbeiter Platz", "Nutzung"],
          ["EG", "412", "118", "8", "Empfang, Besprechung, Kantine, Archiv"],
          ["1. OG", "498", "82", "38", "Vertrieb, Marketing, Einkauf, IT"],
          ["2. OG", "498", "82", "32", "Geschaeftsfuehrung, Personal, Finanzen, Konstruktion"],
          ["DG", "120", "180", "0", "Technik (Lueftung, Server, PV)"],
          ["", "Summe", "1.528", "462", "78"]]),
        ("Erschliessung und Sicherheit",
         "Hauptzugang Industriestrasse 12; Nebenzugang fuer Mitarbeitende ueber Werkstor 2 (mit RFID-Schluessel). "
         "Brandschutz: Brandmeldeanlage gemaess DIN 14675, Anbindung Berufsfeuerwehr Koeln. Alarmanlage VdS-Klasse C. "
         "Aufzug Schindler 3300 (Wartung gemaess LF_SLA004)."),
        ("Modernisierungen",
         ("list", [
             "2018: Fassadendaemmung, Fensteraustausch auf 3-fach-Verglasung",
             "2019: LED-Komplettumruestung Beleuchtung, KNX-Bus-Steuerung",
             "2023: PV-Aufdachanlage 220 kWp, BHKW-Anbindung Bestand",
             "2024: Ladeinfrastruktur 16 Wallboxen 11 kW (geplant Q3)"
         ])),
        ("Anlagen", "Anlage 1: Bauplaene 1985 (Original, gescannt)\nAnlage 2: Sanierungsplaene 2018/2019\nAnlage 3: Brandschutzkonzept aktualisiert 1.7.2022"),
    ])

write_doc(f"{B6}/IMM_Mietvertrag_Kundenparkplatz_2022.docx", H,
    "Mietvertrag Kundenparkplatz 2022 – Vermieter Stadt Koeln (Liegenschaftsamt)",
    subtitle="Mietverhaeltnis ueber Aussenflaeche Industriestrasse / Eckparzelle, gueltig ab 1. Juli 2022",
    sections=[
        ("Mietparteien", "Vermieter: Stadt Koeln, Liegenschaftsamt, Willy-Brandt-Platz 2, 50679 Koeln. "
                          "Mieterin: Halbreiter Maschinenbau GmbH (Bestandskunde seit 1985 fuer Hauptgrundstueck)."),
        ("Mietgegenstand",
         "Aussenflaeche von 480 m² (12 Stellplaetze PKW + 4 Mitarbeiter-Stellplaetze fuer Besucher) angrenzend "
         "an die Industriestrasse 12, eingetragen als Flurstueck 1278/14, Gemarkung Koeln-Niehl. Beschilderung "
         "und Asphaltierung sind Bestandteil der Mietsache. Die Mieterin erhaelt das Hausrecht fuer den "
         "Parkplatz."),
        ("Mietkonditionen",
         "Monatsmiete: 1.620 EUR netto (3,38 EUR/m²/Monat); USt. zzgl. Wert. Nebenkosten (Reinigung, "
         "Beleuchtung, Schneeraeumung) trage die Mieterin (Pauschal 240 EUR/Monat). Mietzeitpunkt: 1. des "
         "Monats; SEPA-Lastschriftmandat erteilt. Indexklausel: Verbraucherpreis-Index (VPI) jaehrlich, "
         "Sockel 2,5 %."),
        ("Laufzeit",
         "5 Jahre vom 1. Juli 2022 bis 30. Juni 2027. Verlaengerungsoption +5 Jahre (auszuueben spaetestens "
         "12 Monate vor Ablauf). Ordentliche Kuendigung beidseits mit 12 Monaten Frist zum Quartalsende "
         "moeglich."),
        ("Pflichten",
         "Verkehrssicherungspflicht obliegt der Mieterin. Bauliche Veraenderungen beduerfen schriftlicher "
         "Genehmigung. Untervermietung nur mit Zustimmung. Rueckgabezustand: besenrein und in dem Zustand bei "
         "Uebergabe (auessere Lebenszustaende ausgenommen)."),
        ("Unterschriften",
         signatures("Sandra Becker", "CFO", M["name"], "Dr. Hannelore Janssen", "Liegenschaftsamt", "Stadt Koeln",
                    place="Koeln", date_str_="22. Juni 2022")),
    ])

write_doc(f"{B6}/IMM_Grundriss_Produktionshalle_A.docx", H,
    "Grundriss Produktionshalle A – Industriestrasse 12, 50829 Koeln",
    subtitle="Stand 1. Februar 2024; verantwortlicher Architekt: Hammers + Partner, Koeln",
    sections=[
        ("Hallendaten",
         "Produktionshalle A; Bauteil B des Gewerbegrundstuecks Industriestrasse 12; Baujahr 1985, "
         "Erweiterung 2003. Grundflaeche 3.180 m² (45 m x 70,7 m); freie Hoehe 12,5 m; Saeulengitter "
         "12,0 m x 18,0 m. Krananlage: 2 Hallenkraene 10 t bzw. 16 t (Wartung Demag Cranes & Components)."),
        ("Nutzung",
         "Halle A beherbergt: Pressenmontage (Pressenlinien PL-500), Schweiss- und Mechanikbereich, "
         "Wareneingang und -ausgang (Tor 1 + Tor 2). Bodenbelastung: 5 t/m² (Stahlbeton). "
         "Sondertraversen bis 32 t Einzelkomponente."),
        ("Versorgung und Sicherheit",
         "Elektrik: 1.250 kVA Trafostation (im Verbund mit Halle B); Druckluft 8 bar; Stickstoff fuer "
         "Schweissprozesse; Industrieabwasser (Schlamm- und OEl-Abscheider gemaess BImSchG-Genehmigung). "
         "Brandschutz: Sprinkleranlage gemaess VdS 2092; CO2-Loeschanlage am Hochregallager."),
        ("Anlagen", "Anlage 1: Bauplaene Original 1985 + Erweiterung 2003\n\nAnlage 2: BImSchG-Genehmigung\n\nAnlage 3: Brandschutzkonzept 2022"),
    ])

write_doc(f"{B6}/IMM_Bauantrag_Hallenanbau_2024.docx", H,
    "Bauantrag Hallenanbau 2024 – Erweiterung Halle B um 1.280 m²",
    subtitle="Antrag bei der Stadt Koeln, Bauaufsichtsamt, eingereicht 18. Maerz 2024",
    sections=[
        ("Vorhabenbeschreibung",
         "Anbau einer Erweiterungshalle (Halle B-Erweiterung) suedseitig an die Bestandshalle B im "
         "Gewerbegebiet Niehl; Grundflaeche 32 m x 40 m = 1.280 m²; freie Hoehe 11,0 m. Nutzung: "
         "Aufstellung der Laserschneidanlage LS-800 5-Achs sowie der erweiterten Foerderband-Fertigung. "
         "Geplante Bauzeit: 8. Juli 2024 bis 31. Maerz 2025."),
        ("Architekt / Statiker / Brandschutz",
         "Architekturbuero: Hammers + Partner, Koeln (HOAI Phasen 1-9). Tragwerk: Ingenieurbuero "
         "Holzhauer + Partner GmbH, Aachen. Brandschutzgutachten: Dipl.-Ing. Hartmut Belz, Bonn "
         "(Loeschwasserversorgung gemaess vfdb 2.2.7; F90-Bauteile Schnittstelle Bestandshalle)."),
        ("BImSchG",
         "Vorhaben unterliegt dem BImSchG (4. BImSchV); eine Genehmigung im vereinfachten Verfahren "
         "(§ 19 BImSchG) wird in Aussicht gestellt. Schallgutachten Gutachter Mueller-BBM GmbH liegt "
         "vor: Immissionen am naechsten Schutzpunkt (Wohnbebauung 240 m) 38 dB(A) tags / 32 dB(A) nachts; "
         "deutlich unter den Richtwerten TA Laerm."),
        ("Investitionsvolumen", "Investitionssumme 2,15 Mio. EUR (Anlage, Halle, Tragwerk, Bauleitung). "
         "Genehmigt im Gesellschafterbeschluss 2023/06."),
        ("Beigelegte Unterlagen",
         "1) Bauantrag amtliches Formular; 2) Lageplan M 1:500; 3) Bauplaene M 1:100; 4) Tragwerksberechnung; "
         "5) Brandschutzgutachten; 6) Schallgutachten; 7) BImSchG-Antrag; 8) Nachbarschaftsanhoerung."),
    ])

write_doc(f"{B6}/Anlagenakte_Maschine_FZ4891.docx", H,
    "Anlagenakte Maschine FZ-4891 – Faserlaser TruDisk 8001",
    subtitle="Stand 31. Januar 2024",
    sections=[
        ("Stammdaten",
         "Anlagen-Nr.: FZ-4891. Bezeichnung: Faserlaser-Resonator TruDisk 8001 (im Verbund mit Laser"
         "schneidanlage LS-800-5Achs). Hersteller: Trumpf SE + Co. KG. Baujahr/Inbetriebnahme: 2022/2023. "
         "Standort: Halle B, Stellplatz B-12. Anschaffungskosten 245.000 EUR. Bilanzwert 31.12.2023: 184.000 EUR. "
         "Nutzungsdauer: 8 Jahre linear."),
        ("Technische Daten",
         "Laserleistung 8 kW; Wellenlaenge 1.030 nm; Strahlqualitaet M² < 1,2; Wirkungsgrad > 38 %; "
         "Wasser-Kuehlung 50 kW; Elektroanschluss 400 V / 3 Phasen / 80 A; Schnittstellen OPC-UA, EtherCAT, "
         "Profinet."),
        ("Wartungshistorie",
         [["Datum", "Massnahme", "Dienstleister", "Stillstand"],
          ["10.10.2023", "Praeventive Wartung 1.000 h", "Trumpf Service GmbH", "8 Std."],
          ["22.12.2023", "Firmware-Update v3.18.2", "Trumpf Service GmbH (Remote)", "2 Std."],
          ["12.03.2024", "Reinigung Optik / Justage", "intern + Trumpf Service GmbH", "4 Std."]]),
        ("Sicherheits- und Genehmigungsdokumente",
         "CE-Konformitaetserklaerung (LS800), Risikobeurteilung gemaess MRL (ISO 12100), Laser-Schutz"
         "klasse 4, Sicherheitsbeauftragter Stefan Bauer. Bedienschulung jaehrlich (Trumpf Akademie)."),
        ("Lebensphasen", "Geplante Modernisierung 2025/2026: Upgrade auf 12 kW. Restwertbetrachtung "
         "Anlage 1; Verkauf am Sekundaermarkt aktuell nicht vorgesehen."),
    ])

write_doc(f"{B6}/IMM_Versicherungskataster_Immobilien_2024.docx", H,
    "Versicherungskataster Immobilien 2024",
    subtitle="Stand 1. Januar 2024; Versicherungsmaklerin: HDI Global SE, Koeln",
    sections=[
        ("Uebersicht",
         "Sammelversicherung fuer alle Immobilien und Liegenschaften der Halbreiter Maschinenbau GmbH am "
         "Standort Koeln, Industriestrasse 12 (Industrie- und Bueroflaechen) sowie Aussenlager Niehler "
         "Strasse 88 (Lagerflaeche 320 m²). Versicherer: Allianz SE (Gebaeudeversicherung) und HDI "
         "Global SE (Inhaltsversicherung Maschinenbruch)."),
        ("Versicherte Werte",
         [["Liegenschaft", "Versicherungswert EUR", "VS-Bedingung", "Praemie p. a. EUR"],
          ["Verwaltungsgebaeude (Bauteil A)", "4.200.000", "Neuwert", "8.400"],
          ["Halle A (Pressenmontage)", "5.200.000", "Neuwert + Verlust", "12.200"],
          ["Halle B (Laser / Robotik)", "4.800.000", "Neuwert + Verlust", "11.400"],
          ["Halle C (Lager / Logistik)", "3.100.000", "Neuwert", "6.800"],
          ["Aussenlager Niehler Str. 88", "780.000", "Neuwert", "2.100"],
          ["Inhalt Maschinen (gesamt)", "12.500.000", "Maschinenbruch + Elektronik", "28.500"],
          ["", "SUMME", "30.580.000", "", "69.400"]]),
        ("Selbstbeteiligungen",
         "Allgemeine SB 5.000 EUR pro Schadensfall; Maschinenbruch 10.000 EUR; Naturgefahren "
         "(Elementar) 25.000 EUR. Innovationsklausel: Anpassung der Versicherungswerte automatisch jaehrlich "
         "ueber den Baupreisindex sowie Anlagenzugaenge ab 25.000 EUR Einzelwert."),
        ("Hinweise",
         "Alle Liegenschaften sind ueber GPS-Trackerkennung mit dem Sicherheitsdienst (Securitas GmbH) "
         "verknuepft. Nachtwachen 22:00-06:00 Uhr Mo-So. Brandschutz nach VdS-Standard, jaehrliche Pruefung. "
         "Daten der Versicherungspolicen siehe VS_Versicherungsuebersicht_Gesamt_2024."),
    ])

write_doc(f"{B6}/IMM_Verkehrswertgutachten_Industriestr_.docx", H,
    "Verkehrswertgutachten – Liegenschaft Industriestrasse 12, 50829 Koeln",
    subtitle="Sachverstaendiger Dr.-Ing. Hartmut Sander, oeffentl. bestellt durch IHK Koeln; Stichtag 30. November 2023",
    sections=[
        ("Auftrag",
         "Auftraggeber: Halbreiter Maschinenbau GmbH (Sandra Becker, CFO). Zweck: Bilanzielle Bewertung im "
         "Rahmen der Jahresabschluss-Pruefung 2023 sowie Sicherheitenbewertung fuer die Investitionslinie "
         "der Deutschen Bank AG. Gutachten gemaess ImmoWertV / WertR."),
        ("Bewertungsobjekt",
         "Grundstueck 18.420 m², Flurstueck Nr. 1278/13, Gemarkung Koeln-Niehl, GE-Gebiet (Industrie- und "
         "Gewerbegebiet). Bebaut mit Verwaltungsgebaeude (Bauteil A, 1.928 m² BGF) und drei Produktions"
         "hallen A/B/C (gesamt 9.620 m² BGF). Erschliessung Industriestrasse 12 (KAG-konform abgerechnet)."),
        ("Wertermittlungsverfahren",
         "Sachwertverfahren (Bodenrichtwert 195 EUR/m² Koelner Industriegebiet 2023; Gebaeudesachwert "
         "linear nach NHK 2010 mit Indexierung). Ertragswertverfahren als Plausibilisierung; aufgrund "
         "Eigennutzung keine reine Ertragsbetrachtung."),
        ("Ergebnis",
         "Bodenwert: 18.420 m² x 195 EUR = 3.591.900 EUR. Gebaeudesachwerte (nach Alterswertabschlag): "
         "Verwaltungsgebaeude 2.420.000 EUR; Halle A 3.180.000 EUR; Halle B 2.820.000 EUR; Halle C 1.480.000 EUR. "
         "Aussenanlagen 318.000 EUR.\n\n**Verkehrswert (gerundet): 13,8 Mio. EUR.** Bilanzansatz HGB derzeit "
         "1,85 Mio. EUR (Grundstueck) + Gebaeude 4,86 Mio. EUR Buchwert = stille Reserve rund 7,1 Mio. EUR."),
        ("Risiken / Hinweise",
         "Bodenrisiken Altlasten: vorgehender Eintrag im Altlastenkataster geprueft, keine Eintragung. "
         "Schadstoffe: Asbestpruefung Halle A Bj. 1985 in 2018 negativ. Naturgefahren: kein Ueberschwemmungs"
         "gebiet. Verkehrsanbindung: Anschluss A57 in 8 Minuten Fahrtzeit."),
        ("Unterschrift",
         signatures("Dr.-Ing. Hartmut Sander", "Oeffentlich bestellter Sachverstaendiger", "i. e. S.",
                    "Sandra Becker", "CFO", M["name"],
                    place="Koeln", date_str_="12. Dezember 2023")),
    ])

write_doc(f"{B6}/Fuhrparkverzeichnis_2024.docx", H,
    "Fuhrparkverzeichnis 2024 – Halbreiter Maschinenbau GmbH",
    subtitle="Stand 1. Maerz 2024; Verwaltung: Personal & Verwaltung (Andrea Hoffmann)",
    sections=[
        ("Uebersicht",
         "Der Fuhrpark der Gesellschaft umfasst 28 Fahrzeuge: 22 PKW (Geschaeftsfuehrung, AT-Manager, "
         "Aussendienst, Vertrieb, Service), 4 Nutzfahrzeuge Vito Tourer (Servicewagen), 2 LKW 7,5 t "
         "(Werks-LKW). Leasingmodell: Operating-Lease mit Mercedes-Benz Bank AG (siehe FIN_Leasingvertrag_Fuhrpark_2023)."),
        ("Fahrzeugliste",
         [["Kennzeichen", "Marke / Modell", "BJ", "Nutzer:in", "Kilometerstand 12/2023"],
          ["K-MM 100", "Mercedes-Benz S500 Plug-in Hybrid", "2023", "Klaus Mueller (CEO)", "12.840"],
          ["K-MM 200", "Mercedes-Benz E300 d", "2022", "Sandra Becker (CFO)", "38.720"],
          ["K-MM 310", "Mercedes-Benz GLC 300 4MATIC", "2023", "Stefan Braun (Leiter Einkauf)", "22.180"],
          ["K-MM 311", "Mercedes-Benz GLC 300 4MATIC", "2022", "Markus Fischer (KAM Industrie)", "62.480"],
          ["K-MM 312", "Mercedes-Benz GLC 300 4MATIC", "2022", "Jan Mueller (KAM Automotive)", "58.380"],
          ["K-MM 401-410", "Mercedes-Benz C220 d (10 Fzg.)", "2022/2023", "Vertrieb / Service", "Ø 42.300"],
          ["K-MM 501-505", "Mercedes-Benz Vito Tourer (5 Fzg.)", "2023", "Service", "Ø 28.420"],
          ["K-MM 701-702", "Mercedes-Benz Actros 1830L", "2018", "Werks-LKW", "Ø 318.000"],
          ]),
        ("Versicherung / Schaeden",
         "Versicherung Fuhrpark gemaess Bestand bei der Allianz SE (Standard-Industriepolice). "
         "Schaeden 2023: 4 (3 KaskoSB-relevant, 1 Haftpflicht-Drittschaden). Schadenquote 2,2 % (Vorjahr 3,1 %).\n\n"
         "Service- und Wartungspartner: Mercedes-Benz Niederlassung Koeln (PKW), Mercedes-Benz Truck Center "
         "Frechen (LKW)."),
        ("Elektromobilitaet",
         "Aktuell 1 PKW vollelektrisch (CEO S500e; nutzt ueberwiegend Elektroreichweite). Ramp-up E-Mobilitaet "
         "ab Q3/2024: 6 EQE im Wandlungs-Option des Leasingrahmens. Aufbau Ladeinfrastruktur 16 Wallboxen "
         "11 kW (Bauantrag in 06_Immobilien)."),
    ])

write_doc(f"{B6}/IMM_001_Mietvertrag_Produktionshalle_plus_V.docx", H,
    "Mietvertrag Produktionshalle + Verwaltung – Industriestrasse 12, 50829 Koeln",
    subtitle="Verlaengerung 2023 fuer 10 Jahre (Optionsausuebung)",
    sections=[
        ("Hinweis",
         "Anmerkung: Die Halbreiter Maschinenbau GmbH ist Eigentuemerin des Grundstuecks Industriestrasse 12. "
         "Dieser »Mietvertrag« stellt eine interne Sale-and-Lease-Back-aehnliche Gestaltung mit der eigens "
         "gegruendeten »Mueller Immobilien GbR« dar. Die GbR ist im Mehrheitsbesitz der Mueller Familien-GbR "
         "und der Gesellschafterin Frau Elke Mueller-Hartmann."),
        ("Mietsache",
         "Industriestrasse 12, 50829 Koeln: Verwaltungsgebaeude (1.928 m²) + Produktionshallen A, B, C "
         "(insgesamt 9.620 m²) + Aussenanlagen / Parkflaechen. Gesamtmiete: 412.000 EUR p. a. (netto)."),
        ("Konditionen",
         "Laufzeit: 1. Januar 2024 bis 31. Dezember 2033 (10 Jahre, Verlaengerung des Vertrages aus 2014). "
         "Mietzins: monatlich 34.333 EUR netto; Indexklausel VPI (Sockel 2,5 % p. a.). "
         "Betriebskosten ueber die Mieterin direkt (Energie, Wasser, Wartung, Versicherung Inhalte)."),
        ("Steuerliche Wuerdigung",
         "Die Gestaltung ist nach Pruefung von Heuking Kuehn Lueer Wojtek und BDO AG WPG steuerlich "
         "anerkannt (Memo vom 18.9.2023); Marktueblichkeit der Miete bestaetigt durch Verkehrswertgutachten "
         "Dr. Sander 2023 (siehe IMM_Verkehrswertgutachten_Industriestr_)."),
        ("Vertragsklauseln (Auszug)",
         ("clauses", [
             ("§ 1 Nutzung", ["Industrielle Fertigung gemaess BImSchG-Genehmigung der Stadt Koeln vom 22.04.2003.",
                              "Unterermietung an Konzernunternehmen / verbundene Unternehmen zustimmungsfrei."]),
             ("§ 2 Bauliche Veraenderungen", ["Bauliche Veraenderungen bis 250.000 EUR Volumen zustimmungsfrei. "
                              "Investitionen werden mit der Eigentuemerin abgerechnet (Einbauten = Eigentum der "
                              "Mieterin)."]),
             ("§ 3 Erhaltungspflicht", ["Ueblicher Mietgebrauch; Schoenheitsreparaturen i. R. der Geschaeftstaetigkeit "
                              "(Mieterin); Dach + Fassade / strukturelle Substanz (Vermieterin)."]),
         ])),
    ])

write_doc(f"{B6}/IMM_002_Mietvertrag_Außenlager_Niehler_.docx", H,
    "Mietvertrag Aussenlager Niehler Strasse 88",
    subtitle="Gueltig ab 1. April 2022; Laufzeit bis 31. Maerz 2027",
    sections=[
        ("Mietparteien",
         "Vermieterin: Immobilien Niehl Verwaltungs GmbH & Co. KG, Niehler Strasse 88, 50735 Koeln. "
         "Mieterin: Halbreiter Maschinenbau GmbH."),
        ("Mietgegenstand",
         "Lagerhalle Niehler Strasse 88, 50735 Koeln; Grundflaeche 1.180 m², Hallenhoehe 8 m; ohne Heizung, "
         "ohne Sanitaer. Erschliessung: Tor 1 fuer LKW (Auflieger), Tor 2 fuer Stapler. "
         "Hochregallager bestehend, 4 Reihen x 480 Stellplaetze."),
        ("Mietkonditionen",
         "Monatsmiete 9.840 EUR netto (8,34 EUR/m²); Nebenkosten Pauschal 1.180 EUR/Monat. "
         "Sicherheitsleistung: Bankbuergschaft 3 Monatsmieten (HDI). VPI-Indexklausel.\n\n"
         "Laufzeit: 60 Monate (1.4.2022 - 31.3.2027), Verlaengerungsoption 5 Jahre."),
        ("Nutzung",
         "Lagerung von Halbzeugen, Fertigware sowie Sondertransport-Vorbereitung. "
         "Brandschutz: Sprinkleranlage (sprinklergerechte Lagerung wird durch Mieterin sichergestellt). "
         "Maximalbelastung Boden 4 t/m².\n\n"
         "Spezialregelung: Mieterin erhaelt Ankaufsoption zum 31.3.2026 ueber 1.420.000 EUR (Verkehrswert "
         "Gutachten beigefuegt). Optionsfee 25.000 EUR auf Kaufpreis anrechenbar."),
        ("Versicherung",
         "Inhaltsversicherung Mieterin (HDI Global SE); Gebaeudeversicherung Vermieterin. "
         "Haftpflicht-Anteile gemaess GHV-Standard."),
    ])

# ──────────────────────────────────────────────────────────────────────────
# 07_IP_Lizenzen (12 docs)
# ──────────────────────────────────────────────────────────────────────────
B7 = f"{D}/07_IP_Lizenzen"

write_doc(f"{B7}/Technische_Dokumentation_PL500_Rev3.docx", H,
    "Technische Dokumentation Pressenlinie PL-500, Rev. 3",
    subtitle="Stand 12. Februar 2024; Verantwortlich: Michael Weber (F&E)",
    sections=[
        ("Produktinformation",
         "Pressenlinie PL-500 (hydraulische Stanzpresse), Modular-Bauweise, Pressenkraft 500/800/1000 t, "
         "Hublaenge 400/500/600 mm, Hubzahl 18-24/min, Servo-Option, Predictive-Maintenance-Modul. "
         "Erstes Modell 2021 ausgeliefert; im Berichtszeitraum 2023 insgesamt 8 Auslieferungen weltweit."),
        ("Strukturmerkmale",
         "(1) Massive Tisch- und Stoesselplatten (Sphaeroguss EN-GJS-700); (2) Stickstoff-Druckspeicher fuer "
         "schnelle Eilgaenge; (3) Servohydraulische Hauptachsen mit Wegmesssystem (Linearmesssystem 0,5 µm); "
         "(4) Beckhoff-/Siemens-Steuerung mit OPC-UA-Anbindung; (5) Selbstdiagnose der Hydraulik."),
        ("Sicherheits- und Konformitaetsbewertung",
         "Maschinenrichtlinie 2006/42/EG, EMV-RL 2014/30/EU, Niederspannungs-RL 2014/35/EU. "
         "Sicherheitsbetrachtung gemaess ISO 12100, ISO 13849-1 Kategorie 3 PL d. "
         "CE-Konformitaetserklaerung Anlagen-individuell ausgestellt (siehe 09_Compliance)."),
        ("Wartungsphilosophie",
         "Predictive Maintenance basierend auf OPC-UA-Streams (Drehmoment-, Druck-, Temperatur-Werte). "
         "Schwellenwerte vorab parametriert; KI-basierte Anomalieerkennung in Pilotphase mit Siemens "
         "Co-Innovation. Standardwartung alle 1.000 Betriebsstunden bzw. mind. jaehrlich."),
        ("Anlagen",
         "Stueckliste / Schaltplaene / Hydraulikplan / Risikobeurteilung / IBN-Checkliste."),
    ])

write_doc(f"{B7}/Wartungshandbuch_FB200.docx", H,
    "Wartungshandbuch Foerderbandanlage FB-200",
    subtitle="Rev. 2.4, gueltig ab 1. Februar 2024",
    sections=[
        ("Zielgruppe",
         "Dieses Handbuch richtet sich an Bediener:innen und Wartungstechniker:innen der Foerderbandanlage "
         "FB-200 (Modul A Gerade, Modul K Kurve). Es ergaenzt die Bedienungsanleitung sowie die spezifischen "
         "Einbau-Unterlagen pro Anlage."),
        ("Wartungsplan",
         [["Intervall", "Massnahme", "Verantwortlich", "Dauer"],
          ["Taeglich", "Sichtkontrolle Antriebskomponenten / Foerderband Spannung", "Bediener", "5 Min."],
          ["Woechentlich", "Reinigung Sensoren / Sichtkontrolle Verschleissteile", "Bediener / Vorarbeiter", "20 Min."],
          ["Monatlich", "Funktionspruefung Notaus / Lichtschranken / Schaltverhalten", "Wartungstechniker", "60 Min."],
          ["Jaehrlich", "Vollwartung (Antrieb, Lager, Steuerung)", "Wartungstechniker (intern oder MMB)", "8 Std."],
          ["Alle 24 Mo.", "VDE 0701/0702 Pruefung elektrische Sicherheit", "Externer Pruefer", "4 Std."]]),
        ("Sicherheit",
         "Vor Wartungseingriffen: Anlage spannungsfrei schalten und gegen Wiedereinschalten sichern. "
         "Schluesselschalter Hauptantrieb in Stellung »Wartung«; Schaltschrank mit Schloss versehen "
         "(Lockout-Tagout). Bei Arbeiten an erhoehten Anlagenteilen: PSA gemaess Vorgaben EnBetrV."),
        ("Verbrauchsmaterialien",
         ("list", [
             "Foerdergurt FB-200-G-650 (Verschleissintervall ~8.000 Betriebsstunden je nach Anwendung)",
             "Lager-Rolle FB-200-LR-50 (Verschleissintervall ~10.000 Betriebsstunden)",
             "Steuerungssoftware Updates (Firmware) mind. 1x p. a.",
             "Stickstoffspeicher (sofern eingesetzt): Tausch alle 5 Jahre",
         ])),
        ("Service-Support",
         "Service-Hotline +49 221 47832-72 (24/7). Online-Diagnose via VPN moeglich; Anlagenstamm im "
         "SAP PM hinterlegt. Anlagenbezogener Wartungsvertrag laut SLA wahlweise Basic / Premium / Total Care "
         "(siehe Preisliste 2024 unter 04_Vertraege_Kunden)."),
    ])

write_doc(f"{B7}/IP_Gebrauchsmuster_DE202021.docx", H,
    "Gebrauchsmuster DE 20 2021 105 482.4 – Hydraulisches Schnellwechselsystem",
    subtitle="Anmeldetag: 12. Oktober 2021; Eingetragen: 18. Maerz 2022",
    sections=[
        ("Inhaber", "Halbreiter Maschinenbau GmbH, Industriestrasse 12, 50829 Koeln."),
        ("Erfinder", "Michael Weber (Senior Konstruktionsingenieur); Felix Engelhardt (Mit-Erfinder, "
                     "ab 2023 bei MMB; vormals Trumpf SE + Co. KG)."),
        ("Bezeichnung",
         "Hydraulisches Schnellwechselsystem fuer Pressenwerkzeuge mit integrierter Werkstueck-Vermessung "
         "(Lasertriangulation; Toleranz < 0,02 mm). Aktenzeichen Patentanwalt: P2021-MMB-014 "
         "(Maiwald Patentanwaelte, Muenchen)."),
        ("Schutzanspruechse",
         ("list", [
             "Hauptanspruch 1: hydraulisches Schnellwechselsystem mit lasergestuetzter Vermessung der "
             "Werkzeugaufnahme.",
             "Nebenanspruch 2: spezifische Hydraulikkupplungs-Geometrie zur druckdichten Aufnahme.",
             "Nebenanspruch 3: integrierte Sicherheitsabfrage (kein Werkzeug, kein Press-Freigabesignal).",
             "Nebenanspruch 4: Datenmodell zur Telemetrie an OPC-UA-Schnittstelle.",
         ])),
        ("Schutzfristen / Status",
         "Eingetragen am 18.3.2022; Laufzeit bis maximal 10 Jahre (i. d. R. 3+3+2+2). Verlaengerung 6.+ "
         "Jahr 2025 bereits beantragt. Patentanmeldung EU (EP-Anmeldung) parallel hinterlegt (siehe IP-Datenbank). "
         "Auslandsanmeldungen US, CN, JP in Pruefung."),
        ("Verwertung",
         "Eingebaut in Pressenlinie PL-500 ab Modelljahr 2023; Lizenzvergabe an Dritte derzeit nicht "
         "geplant. Wertbeitrag (intern geschaetzt, mittel-/langfristig): ~ 0,8 - 1,2 Mio. EUR p. a. "
         "Differenzpotenzial in Pre-Service-Time."),
    ])

write_doc(f"{B7}/IP_Software_Entwicklungsvertrag_UNITY.docx", H,
    "Software-Entwicklungsvertrag UNITY AG – Vorausschauende Instandhaltung",
    subtitle="Vertrag UN-MMB-2023-PR-014 vom 14. Juli 2023",
    sections=[
        ("Vertragspartner",
         "Auftraggeberin: Halbreiter Maschinenbau GmbH.\n\n"
         "Auftragnehmer: UNITY Innovation Alliance AG, Buerener Strasse 14, 33102 Paderborn, "
         "vertreten durch Vorstandsmitglied Frau Dr. Brigitte Kupke."),
        ("Gegenstand",
         "Entwicklung einer Predictive-Maintenance-Software fuer die Pressenlinie PL-500 und die Foerder"
         "bandanlage FB-200. Funktionen: Echtzeitdaten-Ingest (OPC-UA), Anomalieerkennung mittels "
         "klassischer Statistik und ML (Isolation Forest, LSTM-Autoencoder), Visualisierung im "
         "Dashboard, Alerting via E-Mail / Microsoft Teams."),
        ("Vergutung",
         "Pauschalpreis 285.000 EUR netto inkl. Reisekosten; zahlbar in vier Tranchen "
         "(70.000 / 90.000 / 80.000 / 45.000 EUR) nach Milestones M1-M4. Pflegevertrag fuer 24 Monate "
         "nach Abnahme: 38.000 EUR p. a."),
        ("Rechte / IP",
         "Saemtliche Arbeitsergebnisse / Quellcode gehen mit vollstaendiger Zahlung in das Eigentum der "
         "MMB ueber; ausgenommen UNITY-eigene Frameworks (Vorbestehendes IP), die als nicht-exklusive "
         "Lizenz dauerhaft unentgeltlich mitgeliefert werden. Veroeffentlichungen / Referenzen beduerfen "
         "der Zustimmung der MMB."),
        ("Termine / Milestones",
         "M1 Konzept (30.9.2023); M2 Prototyp (15.12.2023); M3 Pilotbetrieb 3 Monate bei ThyssenKrupp "
         "Steel Europe AG (31.3.2024); M4 Abnahme und Produktivsetzung (30.6.2024)."),
        ("Unterschriften",
         signatures("Sandra Becker / Michael Weber", "GF / F&E", M["name"],
                    "Dr. Brigitte Kupke", "Vorstand", "UNITY Innovation Alliance AG",
                    place="Koeln / Paderborn", date_str_="14. Juli 2023")),
    ])

write_doc(f"{B7}/IP_NDA_Entwicklungspartner_RWTH_2023.docx", H,
    "Vertraulichkeitsvereinbarung (NDA) – RWTH Aachen, Lehrstuhl PtU",
    subtitle="Vereinbarung vom 4. Mai 2023, Laufzeit 5 Jahre",
    sections=[
        ("Parteien",
         "Halbreiter Maschinenbau GmbH (»MMB«) und RWTH Aachen University, Lehrstuhl Produktionssysteme und "
         "Umformtechnik (»PtU«), Schinkelstrasse 2, 52062 Aachen, vertreten durch Univ.-Prof. Dr.-Ing. "
         "Wolfgang Trier."),
        ("Zweck",
         "Beidseitige Vertraulichkeitsvereinbarung im Rahmen der Vorbereitung eines Forschungsvorhabens "
         "»Pressenmaschinen 4.0 - Adaptive Process Control mittels Edge-KI« (Foerderantrag BMWi geplant)."),
        ("Vertraulichkeitsregelungen",
         ("clauses", [
             ("§ 1 Vertrauliche Information", [
                 "»Vertrauliche Informationen« umfassen alle Informationen technischer, kaufmaennischer, "
                 "wissenschaftlicher und sonstiger Art, die im Zusammenhang mit dem Projekt von der "
                 "offenlegenden Partei mitgeteilt werden und als vertraulich gekennzeichnet sind oder "
                 "deren Vertraulichkeit nach den Umstaenden erkennbar ist.",
             ]),
             ("§ 2 Pflichten", [
                 "Die empfangende Partei (a) verwendet die Informationen ausschliesslich fuer den genannten "
                 "Zweck, (b) gibt sie nicht an Dritte weiter, (c) ergreift mindestens den Sorgfaltsstandard, "
                 "den sie auch zum Schutz eigener vertraulicher Informationen anwendet.",
                 "Zugaenglich gemacht werden Informationen nur jenen Mitarbeitenden und Bevollmaechtigten, "
                 "die diese fuer die Erfuellung des Zwecks kennen muessen (»Need-to-know«); diese werden "
                 "vorab schriftlich auf vergleichbare Vertraulichkeitspflichten verpflichtet.",
             ]),
             ("§ 3 Ausnahmen", [
                 "Nicht vertraulich sind Informationen, die (a) zum Zeitpunkt der Offenlegung der "
                 "Allgemeinheit bekannt waren, (b) der empfangenden Partei nachweislich vorher bekannt "
                 "waren, (c) von Dritten ohne Vertraulichkeitspflicht erhalten wurden, oder "
                 "(d) unabhaengig durch die empfangende Partei ohne Verwendung vertraulicher Informationen "
                 "entwickelt wurden.",
             ]),
             ("§ 4 Veroeffentlichungen", [
                 "Veroeffentlichungen / Konferenz- oder Zeitschriftenbeitraege, die ueber das Projekt "
                 "berichten, sind nur mit vorheriger schriftlicher Zustimmung der jeweils anderen Partei "
                 "zulaessig.",
             ]),
             ("§ 5 Dauer", [
                 "Die Pflichten gelten waehrend der Projektphase und 5 Jahre nach deren Beendigung, "
                 "spaetestens jedoch 7 Jahre nach Vertragsunterzeichnung.",
             ]),
         ])),
        ("Unterschriften",
         signatures("Michael Weber", "Senior Konstrukteur F&E", M["name"],
                    "Univ.-Prof. Dr.-Ing. Wolfgang Trier", "Lehrstuhlleiter PtU", "RWTH Aachen University",
                    place="Koeln / Aachen", date_str_="4. Mai 2023")),
    ])

write_doc(f"{B7}/IP_Technologie_Transfer_RWTH.docx", H,
    "Technologietransfervertrag – RWTH Aachen, Lehrstuhl PtU – KI-gestuetzte Adaptive Process Control",
    subtitle="Folgevertrag zur NDA vom 4. Mai 2023; gueltig ab 1. Oktober 2023",
    sections=[
        ("Vertragspartner",
         "Lizenzgeberin: RWTH Aachen University (vertreten durch das Dezernat 4.0 Forschung & Karriere). "
         "Lizenznehmerin: Halbreiter Maschinenbau GmbH."),
        ("Lizenzgegenstand",
         "Nicht-exklusive Lizenz zur kommerziellen Nutzung des am Lehrstuhl PtU entwickelten Algorithmus "
         "»Adaptive-PressCtrl 2.0« (KI-gestuetzte Echtzeitanpassung der Pressparameter zur Reduktion "
         "von Werkzeugverschleiss). Quellcode wird in Python und C++ uebergeben."),
        ("Lizenzgebuehren",
         "Einmalige Initialgebuehr 80.000 EUR (zahlbar bei Vertragsschluss). Laufende Lizenzgebuehren "
         "0,4 % vom Umsatz mit Maschinen, in denen der Algorithmus eingesetzt wird, abzueglich Material"
         "kosten. Mindestlizenzgebuehr 25.000 EUR p. a. Reporting halbjaehrlich, Pruefungsrecht der RWTH."),
        ("Verwertungsrechte",
         "Lizenz umfasst weltweite Nutzung; Lizenz ist nicht-uebertragbar; Unterlizenzierung ist nur an "
         "Tochterunternehmen der MMB gestattet. Eigene Weiterentwicklungen sind erlaubt; Verbesserungen "
         "fallen automatisch der Lizenznehmerin zu (Ownership), bleiben jedoch in den Anwendungsbereich "
         "des Algorithmus rueckkoppelnd (Grant-back)."),
        ("Laufzeit",
         "Laufzeit 10 Jahre (1.10.2023 - 30.9.2033). Vorzeitige Kuendigung bei wesentlichen Vertrags"
         "verletzungen."),
    ])

write_doc(f"{B7}/IP_Marke_MMB_Logo_DPMA.docx", H,
    "Markenrechte MMB – Eintragung Deutsches Patent- und Markenamt (DPMA)",
    subtitle="Stand 31. Januar 2024",
    sections=[
        ("Eingetragene Marken",
         [["Markenname", "Registrierungs-Nr.", "Anmeldetag", "Eingetragen", "Klassen", "Status"],
          ["MUELLER MASCHINENBAU", "DE 39 408 712", "12.06.2002", "18.09.2002", "07, 09, 37, 42", "aktiv"],
          ["MMB (Wortmarke)", "DE 30 712 484", "08.11.2007", "22.02.2008", "07, 09, 37, 42", "aktiv"],
          ["MMB-Logo (Bildmarke)", "DE 30 215 484", "08.11.2007", "22.02.2008", "07, 09, 37", "aktiv"],
          ["PL-500 (Wortmarke)", "DE 30 2019 015 482", "14.03.2019", "22.07.2019", "07, 09", "aktiv"],
          ["LS-800 (Wortmarke)", "DE 30 2019 015 483", "14.03.2019", "22.07.2019", "07, 09", "aktiv"],
          ["FB-200 (Wortmarke)", "DE 30 2020 042 184", "18.08.2020", "12.12.2020", "07, 09", "aktiv"],
          ["MR-150 (Wortmarke)", "DE 30 2023 010 218", "22.02.2023", "14.06.2023", "07, 09", "aktiv"],
          ]),
        ("EU-Marke",
         "EU-Bildmarke »MMB« ist als Unionsmarke beim EUIPO (Alicante) hinterlegt seit 18.04.2008, "
         "Reg-Nr. 006 482 184. Verlaengerung Juli 2028."),
        ("Internationale Marken",
         "WIPO/Madrid-System Anmeldungen fuer China, USA, Mexiko: in Bearbeitung; rechtsanwaltliche "
         "Vertretung Boehmert & Boehmert Partnerschaft."),
        ("Massnahmen 2024",
         "(a) Markenrecherche auf Stoererkennzeichen vor IBN neuer Produktreihe »VLine-Series« (geplant 2025); "
         "(b) DPMA-Recherche Wettbewerbsmarken zu PL-500 und MR-150 quartalsweise; "
         "(c) Markenrechtsstrategie China: Vorab-Anmeldung notwendig wegen First-to-File-Prinzip."),
    ])

write_doc(f"{B7}/IP_005_Lizenz_Salesforce_Sales_Clo.docx", H,
    "Lizenz Salesforce Sales Cloud Enterprise (Lizenzvertrag SF-MMB-2023)",
    subtitle="Master Subscription Agreement; Stand 1. Januar 2024",
    sections=[
        ("Parteien", "Lizenzgeber: Salesforce Inc. (vertreten ueber Salesforce Germany GmbH, Erika-Mann-Strasse 65, "
                     "80636 Muenchen). Lizenznehmer: Halbreiter Maschinenbau GmbH."),
        ("Lizenzumfang",
         "Salesforce Sales Cloud Enterprise inkl. Pardot Marketing Automation, Experience Cloud "
         "(Kunden-Self-Service-Portal), Sandbox-Umgebung und API-Limit Plus. Edition: Enterprise. "
         "Anzahl Lizenzen: 28 Named-User (Vertrieb, Marketing, Service, GF, Bauleitung)."),
        ("Konditionen",
         "Jahresgebuehr 78.400 EUR netto (= 233 EUR pro User pro Monat); Laufzeit 3 Jahre (1.1.2024-31.12.2026) "
         "mit jaehrlicher Preisanpassung 5 %; Verlaengerungsoption +24 Monate. Zahlung jaehrlich im Voraus."),
        ("Dienste",
         "Standard-Support, 99,9 % SLA-Verfuegbarkeit, Salesforce Trust-Compliance (ISO 27001, SOC 2). "
         "Datenexport jederzeit moeglich (zip-Archive)."),
        ("Datenschutz",
         "Auftragsverarbeitungsvertrag (AVV) gemaess Art. 28 DSGVO; Standard Contractual Clauses fuer "
         "EU-Datenuebertragung; primaere Datenhaltung Frankfurt, sekundaer Dublin."),
        ("Verantwortlich", "IT-Leitung MMB: Markus Helmer."),
    ])

write_doc(f"{B7}/IP_008_Lizenz_SOLIDWORKS_Premium_.docx", H,
    "Lizenz SOLIDWORKS Premium / Halbreiter Maschinenbau GmbH",
    subtitle="Subskription / Wartung 2024",
    sections=[
        ("Parteien", "Lizenzgeber: Dassault Systemes Deutschland GmbH (Stuttgart) / Bechtle GmbH & Co. KG "
                     "(Reseller). Lizenznehmer: Halbreiter Maschinenbau GmbH."),
        ("Lizenzumfang",
         "SOLIDWORKS Premium 2024 SP3.1 – 28 Floating-Lizenzen (Konstruktion, Berechnung). Ergaenzend: "
         "SOLIDWORKS Simulation (FEM) Premium 12 Lizenzen; SOLIDWORKS Electrical Schematic 4 Lizenzen; "
         "SOLIDWORKS PDM Professional 30 Bearbeitungslizenzen; DraftSight 8 Lizenzen."),
        ("Konditionen",
         "Subscription-Gebuehr 2024: 84.200 EUR netto (Jahresgebuehr fuer Wartung & Upgrade-Recht). "
         "Floating-Lizenzen ueber NetworkLicense-Server (im Werk Koeln); Software-Heimat: Werk Koeln + "
         "remote ueber VPN. Lizenzkontrolle ueber FlexNet-Lizenzserver."),
        ("Schulung",
         "Im Lizenzpaket inkludiert: 14 Schulungstage p. a. (Anwendertraining, Update-Schulung, "
         "SIMULATIONS-Vertiefung) bei Bechtle Akademie."),
        ("Eigentum",
         "Lizenz ist nicht-uebertragbar; Lizenznehmer haelt Nutzungsrecht; Konstruktionsdaten und "
         "abgeleitete Werkstuecke verbleiben im Eigentum Lizenznehmer. PDM-Server-Datenexport bei "
         "Vertragsende moeglich."),
    ])

write_doc(f"{B7}/IP_004_Lizenz_SAP_S-4HANA_On-Prem.docx", H,
    "Lizenz SAP S/4HANA On-Premise (Standard Maintenance Subscription)",
    subtitle="Vertragsnummer SAP-MMB-2018-014; Wartungsvertrag aktuell 2024",
    sections=[
        ("Lizenzgeber", "SAP SE, Dietmar-Hopp-Allee 16, 69190 Walldorf."),
        ("Lizenzumfang",
         "SAP S/4HANA (On-Premise, Release 2023) – Branchenversion Industrial Manufacturing. Module aktiviert: "
         "FI, CO, MM, SD, PP-PI, QM, PM, PS, HR (Talent Management). Anzahl Named Users: 180 "
         "(davon 32 Professional, 78 Limited, 70 ESS)."),
        ("Konditionen",
         "Wartungsgebuehr 22 % der Lizenzkosten p. a.; aktuelle Wartungsgebuehr 2024: 320.000 EUR. "
         "Inkludiert: 24/7-Hotline, Updates, Support-Pakete, Solution Manager. Service-Level-Agreement "
         "siehe LF_SLA002. Wartungsvertrag laeuft an den Lizenzvertrag gekoppelt; jaehrliche Verlaengerung."),
        ("Berechtigungen",
         "Named-User-Lizenzen sind nicht uebertragbar zwischen Personen; technische User (Background-Jobs) "
         "sind nicht Named-User-pflichtig. Audit durch SAP alle 2-3 Jahre; letzte Auditierung Mai 2023 "
         "ohne Beanstandungen abgeschlossen."),
        ("Erweiterung",
         "Geplante Erweiterung 2024: Aktivierung Modul EHS (Environment Health Safety) sowie GTS "
         "(Global Trade Services) fuer Exportkontrolle. Zusatzlizenzkosten ca. 95.000 EUR."),
    ])

write_doc(f"{B7}/IP_006_Lizenz_SINUMERIK_ONE_CNC-So.docx", H,
    "Lizenz SINUMERIK ONE CNC-Steuerung (Siemens)",
    subtitle="Rahmenlizenz fuer pressentechnische Anlagen",
    sections=[
        ("Lizenzumfang",
         "Lizenzpaket SINUMERIK ONE (Hardware-Bundle + Run-time-Lizenzen) zur Verwendung in den Pressenlinien "
         "PL-500 und Laserschneidanlagen LS-800. Lizenzanzahl: 18 aktive Run-time-Lizenzen (laufende Anlagen) + "
         "6 Engineering-Lizenzen (TIA Portal V18, SIMATIC STEP 7, ePLAN Electric P8 Adapter)."),
        ("Konditionen",
         "Lizenzgebuehren werden pro ausgelieferter Anlage projektbezogen ueber das Materialnummern-Modell "
         "(»TIA-Selection Tool«) gemaess Stueckliste abgerechnet. Run-time-Lizenz-Standardpreis je Achse "
         "1.250 EUR; SINUMERIK Edge / Cloud-Modul 4.200 EUR Aufpreis (Predictive Maintenance)."),
        ("Wartung",
         "Wartungs- und Update-Service ueber Siemens Industry Services GmbH (siehe LF_SLA001) verfuegbar; "
         "umfasst auch Cybersecurity-Patches. Notfallsupport 24/7 mit Reaktionszeit 1 Std. (P1)."),
        ("Vorzugskonditionen",
         "Im Rahmen der Preferred-Supplier-Vereinbarung Siemens (siehe 05_Vertraege_Lieferanten/LF_Preferred_Supplier_Siemens_2023) "
         "Rabatt 6 % auf Listenpreise sowie priorisierter Zugang zu Beta-Programmen (SINUMERIK Edge 2024)."),
    ])

write_doc(f"{B7}/IP_007_Lizenz_AutoCAD_Mechanical_2.docx", H,
    "Lizenz AutoCAD Mechanical 2024 (Autodesk Subscription)",
    subtitle="Wartungsvertrag 2024-2026",
    sections=[
        ("Lizenzumfang",
         "AutoCAD Mechanical 2024 – 18 Subscriptions (Konstruktion, Service). Ergaenzend: AutoCAD LT "
         "12 Lizenzen (Auszubildende, Vertriebs-Innendienst). Reseller: CADMAI (Aachen)."),
        ("Konditionen",
         "Jahresgebuehr 2024: 38.400 EUR netto. Laufzeit Multi-Year Subscription 3 Jahre "
         "(1.1.2024-31.12.2026) mit 8 % Multi-Year-Rabatt. Includes Software Updates, Cloud-Services "
         "(Autodesk Drive 25 GB pro User), Customer Support."),
        ("Nutzungsmodalitaeten",
         "Named-User-Lizenzen; Login ueber Autodesk-Account. Roaming-Support fuer Aussendienst und "
         "Homeoffice. Nutzung 5 Jahre lang im Audit-Logbuch nachweisbar (Bekanntmachung Reseller 2022)."),
    ])

# ──────────────────────────────────────────────────────────────────────────
# 08_Versicherungen (4 docs)
# ──────────────────────────────────────────────────────────────────────────
B8 = f"{D}/08_Versicherungen"

write_doc(f"{B8}/VS_Schadensmeldung_2022_Maschinenschaden.docx", H,
    "Schadensmeldung 2022 – Maschinenschaden Pressenlinie PL-300",
    subtitle="HDI Global SE, Schadenakte SM-2022-HDI-0142",
    sections=[
        ("Schadenanzeige",
         "Versicherungsnehmer: Halbreiter Maschinenbau GmbH. Versichertes Risiko: Maschinenbruch "
         "(Versicherungssumme 12,5 Mio. EUR, Selbstbeteiligung 10.000 EUR). Schadenmeldung erfolgt mit "
         "Schreiben vom 18. Maerz 2022 an HDI Global SE, Schadenabteilung, HDI-Platz 1, 30659 Hannover."),
        ("Sachverhalt",
         "Am 14. Maerz 2022 um 02:30 Uhr ist im Verlauf der Nachtschicht in Halle B die Pressenlinie PL-300 "
         "(Bj. 1998) infolge eines Lagerausfalls im Hauptantrieb (Position L4-L7) ausgefallen. Der "
         "Hauptantrieb wurde infolge des Lagerverbruchs erheblich beschaedigt. Verletzungen von Mitarbeitenden "
         "sind nicht eingetreten. Die betroffenen Mitarbeitenden hatten zum Zeitpunkt des Ereignisses einen "
         "vorschriftsmaessigen Abstand."),
        ("Schadensumfang",
         "Reparaturaufwand (Sachverstaendiger Dipl.-Ing. Reinhold Vogt, Bonn): 218.420 EUR netto "
         "(Antrieb 142.000 EUR; Mechanikkomponenten 38.000 EUR; Steuerungsanpassung 18.000 EUR; "
         "Demontage / Wiedereinbau 20.420 EUR). Stillstandszeit: 18 Tage. Stillstandsschaden / "
         "entgangener Deckungsbeitrag (Betriebsunterbrechung): 412.000 EUR (separates SUM-Limit)."),
        ("Reguliertes Ergebnis",
         "HDI hat den Schaden anerkannt: Sachschaden 208.420 EUR (Selbstbeteiligung 10.000 EUR), "
         "Betriebsunterbrechungsschaden 282.000 EUR (Wartezeit 5 Werktage, danach 30 Tage Vollausgleich). "
         "Auszahlung 30. Juni 2022. Schadenakte ist im internen Versicherungsmanagement abgelegt."),
        ("Massnahmen / Lessons Learned",
         "Vorzeitiger Wechsel von PL-300 auf PL-500 (Investitionsbeschluss 2020/02). Lager-Inspektions"
         "intervall in den vorgelagerten Wartungsplaenen verkuerzt. Schwingungsdiagnostik durch "
         "Predictive-Maintenance-Plattform (UNITY-Projekt) ab 2024 produktiv."),
    ])

write_doc(f"{B8}/VS_Schadensmeldung_2023_Wasserschaden.docx", H,
    "Schadensmeldung 2023 – Wasserschaden Verwaltungsgebaeude",
    subtitle="Allianz SE, Schadenakte WS-2023-ALL-0218",
    sections=[
        ("Schadenanzeige",
         "Versicherungsnehmer: Halbreiter Maschinenbau GmbH. Versichertes Risiko: Gebaeudeversicherung "
         "inkl. Leitungswasser (Allianz SE, Police BNR-MMB-2018-014). Selbstbeteiligung 1.500 EUR."),
        ("Sachverhalt",
         "Am 22. Oktober 2023 um 03:15 Uhr platzte im 2. OG des Verwaltungsgebaeudes eine Anschlussleitung "
         "(Heizungsruecklauf, Cu 18 mm) infolge Materialermuedung. Wasseraustritt rund 4,2 m³ ueber "
         "5 Stunden bis Entdeckung. Wassereintritt in Bueros 2-OG (Buchhaltung, Personal) sowie ins 1. OG "
         "(Vertrieb)."),
        ("Schadensumfang",
         "Reinigung, Trocknung: 28.400 EUR (Belfor Deutschland GmbH, Standort Bonn). Bodenbelag-Erneuerung "
         "(Teppich): 18.200 EUR. Trockenbau / Maler 12.400 EUR. Beschaedigte Akten (Personalakten "
         "rekonstruierbar, einige Vertragsoriginale): 4.800 EUR (Restaurierung). "
         "Gesamtschaden: 63.800 EUR netto."),
        ("Reguliertes Ergebnis",
         "Allianz hat den Schaden in Hoehe von 62.300 EUR anerkannt (1.500 EUR SB). "
         "Auszahlung 18. November 2023. Schaden ist abgewickelt."),
        ("Massnahmen",
         "Praeventive Inspektion aller Heizungsanschluesse im Verwaltungsgebaeude (Jahresinspektion durch "
         "Bruni Elektroanlagen GmbH erweitert)."),
    ])

write_doc(f"{B8}/VS_Risikoanalyse_Versicherungsmakler_2024.docx", H,
    "Risikoanalyse 2024 – durchgefuehrt durch Versicherungsmakler",
    subtitle="HDI Risk Consulting GmbH, Bericht vom 8. Februar 2024",
    sections=[
        ("Auftrag", "Im Rahmen der jaehrlichen Maklerueberpruefung hat die HDI Risk Consulting GmbH "
                     "ein umfassendes Risk-Assessment der Halbreiter Maschinenbau GmbH durchgefuehrt. "
                     "Berichtszeitraum 1.1.2023 - 31.12.2023, ergaenzt um Standortbegehung 14./15. November 2023."),
        ("Risikoportfolio",
         [["Risikofeld", "Bewertung", "Versicherungsstatus", "Empfehlung"],
          ["Brand / Feuer", "mittel-hoch", "Allianz Industrieline (12,5 Mio. EUR SUM)", "Anhebung +2 Mio. EUR"],
          ["Maschinenbruch / Elektronik", "mittel", "HDI Global (10 Mio. EUR SUM)", "Adaequat"],
          ["Betriebshaftpflicht / Produkthaftpflicht", "mittel", "Allianz (10/15 Mio.)", "Erhoehung wg. Exportmexiko"],
          ["D&O", "niedrig", "Allianz (10 Mio. EUR)", "Adaequat"],
          ["Cyber / IT", "hoch (steigend)", "Hiscox (2 Mio. EUR)", "Erhoehung auf 5 Mio. empfohlen"],
          ["Transport (Export Mex/CN)", "mittel", "AXA (1 Mio. EUR pro Transport)", "Project-Spezial fuer Schwerlasten"],
          ["Umwelt / Gewaesser", "mittel", "HDI (1 Mio. EUR)", "Adaequat"],
          ]),
        ("Empfehlungen",
         ("list", [
             "Cyber-Versicherung auf 5 Mio. EUR SUM erhoehen (Hintergrund: zunehmende Bedrohungslage "
             "im Maschinenbau, BSI Lagebericht 2023).",
             "Brand-Sprinkler-Pruefung VdS 2092 in Halle A vorziehen (durch Trocknungsphase im Herbst "
             "potenziell Sprinkler-Empfindlichkeit verschoben).",
             "BR (Betriebsunterbrechung) auf 8 Monate (statt 6) erweitern.",
             "Mexico-Risiko separat absichern (zusaetzlich Cargo-Versicherung Aufgabe / Lieferweg "
             "Krefeld -> Bremerhaven -> Veracruz -> Queretaro).",
         ])),
        ("Kostenfolge",
         "Praemienanpassungen 2024 voraussichtlich + 8,2 % (Vorjahr + 6,4 %), aufgrund Cyber- und "
         "Inhaltsanpassungen. Erwartete Gesamtpraemien: 285.000 EUR p. a."),
    ])

write_doc(f"{B8}/VS_Versicherungsübersicht_Gesamt_2024.docx", H,
    "Versicherungsuebersicht Gesamt 2024 – Halbreiter Maschinenbau GmbH",
    subtitle="Stand 1. Januar 2024",
    sections=[
        ("Uebersicht",
         "Die Halbreiter Maschinenbau GmbH unterhaelt einen integrierten Versicherungsschutz, abgestimmt "
         "mit der HDI Risk Consulting GmbH und ueberprueft jaehrlich. Versicherungsmakler: HDI Global SE."),
        ("Policen",
         [["Sparte", "Versicherer", "Versicherungssumme", "Selbstbeteiligung", "Praemie p. a. EUR", "Police Nr."],
          ["Gebaeude (alle Liegenschaften)", "Allianz SE", "30,58 Mio.", "5.000 EUR", "69.400", "BNR-MMB-2018-014"],
          ["Maschinen / Elektronik", "HDI Global SE", "12,50 Mio.", "10.000 EUR", "32.800", "HM-MMB-2019-022"],
          ["Betriebshaftpflicht", "Allianz SE", "10,00 Mio.", "1.500 EUR", "18.200", "BH-MMB-2019-018"],
          ["Produkthaftpflicht", "Allianz SE", "15,00 Mio.", "5.000 EUR", "28.500", "PH-MMB-2019-019"],
          ["D&O", "Allianz SE", "10,00 Mio.", "10 % Schaden", "12.400", "DO-MMB-2017-008"],
          ["Cyber-Versicherung", "Hiscox AG", "5,00 Mio. (erhoeht 2024)", "25.000 EUR", "32.800", "CY-MMB-2022-014"],
          ["Betriebsunterbrechung (BR)", "Allianz SE", "8 Monate / 12 Mio.", "5 Werktage", "42.000", "BR-MMB-2018-015"],
          ["Transport / Export", "AXA Versicherung", "1,00 Mio. pro Lieferung", "n. v.", "18.400", "TR-MMB-2020-014"],
          ["KFZ-Flotte (28 Fzg.)", "Allianz SE", "Vollkasko / Haftpflicht", "500 EUR", "32.200", "KF-MMB-2018-011"],
          ["Umwelt / Gewaesser", "HDI Global SE", "1,00 Mio.", "12.500 EUR", "8.400", "UM-MMB-2020-018"],
          ]),
        ("Schadenshistorie",
         "Schadenquote 2023: 12,3 % bezogen auf Praemienvolumen (Vorjahr 14,8 %). Wesentliche Faelle: "
         "Maschinenschaden PL-300 (2022, abgewickelt; siehe VS_Schadensmeldung_2022); "
         "Wasserschaden Verwaltungsgebaeude (2023, abgewickelt; siehe VS_Schadensmeldung_2023)."),
        ("Verantwortlich", "CFO Sandra Becker; Operatives Versicherungsmanagement: Andrea Hoffmann."),
    ])


# ──────────────────────────────────────────────────────────────────────────
# 09_Compliance (34 docs) – run only the critical ones in this file; remaining covered separately
# ──────────────────────────────────────────────────────────────────────────
B9 = f"{D}/09_Compliance"

def comp_richtlinie(fname, title, schwerpunkte, geltungsbeginn, ansprechpartner):
    write_doc(f"{B9}/{fname}.docx", H, title,
        subtitle=f"In Kraft ab {geltungsbeginn}, freigegeben durch Geschaeftsfuehrung",
        sections=[
            ("Geltungsbereich",
             "Diese Richtlinie gilt fuer alle Beschaeftigten, Geschaeftsfuehrungsmitglieder, Praktikanten:innen, "
             "Werkstudierenden und Leihkraefte der Halbreiter Maschinenbau GmbH sowie fuer alle Tochter- oder "
             "Beteiligungsgesellschaften. Sie ist auch von Dienstleistern und Lieferanten zu beachten, soweit "
             "sie in den Geschaeftsraeumen oder im Auftrag der Gesellschaft taetig sind."),
            ("Schwerpunkte und Regelungen",
             ("list", schwerpunkte)),
            ("Schulung und Einhaltung",
             "Alle Mitarbeitenden werden jaehrlich verpflichtend zu dieser Richtlinie geschult (e-Learning, "
             "Dauer ca. 25 Min.) und bestaetigen die Kenntnisnahme per Klick. Verstoesse koennen arbeits"
             "rechtliche Folgen bis hin zur ausserordentlichen Kuendigung haben sowie zu strafrechtlichen "
             "Konsequenzen fuehren."),
            ("Hinweisgebersystem",
             "Hinweise auf moegliche Verstoesse koennen ueber das vertrauliche Hinweisgebersystem "
             "»SPEAK-UP@MMB« (gehostet durch EQS Group AG) anonym oder offen erfolgen. Telefon-Hotline: "
             "+49 800 999 22 11 (24/7). Eine Repression gegen meldende Personen ist ausgeschlossen "
             "(siehe HinSchG)."),
            ("Verantwortlich",
             f"Inhaltlich verantwortlich: {ansprechpartner}. Diese Richtlinie wird mindestens alle 24 Monate "
             "ueberprueft und bei Bedarf aktualisiert."),
        ])

comp_richtlinie("COMP_004_Richtlinie_Antikorruption_und_Z", "Richtlinie Antikorruption und Zuwendungen",
    schwerpunkte=[
        "Verbot der aktiven und passiven Bestechung im Privat- und Behoerdenverkehr (§§ 299, 332, 333, 334 StGB).",
        "Geschenke / Einladungen bis 50 EUR ohne Anzeige zulaessig; > 50 EUR: vorherige Genehmigung "
        "durch unmittelbare Fuehrungskraft + Vermerk im Compliance-Register.",
        "Spenden / Sponsoring: nur an gemeinnuetzige Organisationen, in Schriftform, vom CFO freigegeben.",
        "Politische Parteispenden ausgeschlossen.",
        "Verbot von Facilitation Payments (FCPA / UKBA i.V.m. § 334 StGB analog).",
        "Sonderpruefung bei Vertretern, Beratern und Vermittlern im Ausland (Mexiko, China) ueber "
        "ComplyCube-Due-Diligence-Tool.",
        "Schulung jaehrlich Pflicht (alle Mitarbeitenden); CEO/CFO und Vertrieb mit Verstaerkung (Praesenz).",
    ],
    geltungsbeginn="1. Januar 2024",
    ansprechpartner="Compliance Officer (CO) Frau Andrea Hoffmann, in Abstimmung mit der externen Anwaltskanzlei Heuking Kuehn")

comp_richtlinie("COMP_005_Richtlinie_Datenschutz_DSGVO", "Datenschutz-Richtlinie (DSGVO / BDSG)",
    schwerpunkte=[
        "Verantwortlicher i.S.d. Art. 4 Nr. 7 DSGVO: Halbreiter Maschinenbau GmbH (siehe GR_Datenschutz_Verantwortliche_Benennung).",
        "Externer Datenschutzbeauftragter Dr. Markus Lehmann (Lehmann & Partner Datenschutzberatung GmbH).",
        "Zentrale Verarbeitungstaetigkeiten erfasst im Verfahrensverzeichnis (Art. 30 DSGVO) – jaehrliche Aktualisierung.",
        "Auftragsverarbeitungsvertraege (AVV) mit allen relevanten Dienstleistern (Salesforce, SAP, Microsoft 365).",
        "Datenschutz-Folgenabschaetzungen (DSFA) fuer hohe Risiken (Beschaeftigtenanalyse, Predictive Maintenance).",
        "Betroffenenrechte (Auskunft, Loeschung, Widerspruch) ueber datenschutz@halbreiter-maschinenbau.de.",
        "Meldepflichten Datenschutzverletzung an LDI NRW innerhalb von 72 Stunden.",
    ],
    geltungsbeginn="1. Januar 2024",
    ansprechpartner="Externer Datenschutzbeauftragter Dr. Markus Lehmann (DSB)")

comp_richtlinie("COMP_006_Richtlinie_Exportkontrolle", "Richtlinie Exportkontrolle und Sanktionen",
    schwerpunkte=[
        "Pruefung der Lieferungen anhand der Dual-Use-Verordnung (EU) 2021/821 sowie nationaler "
        "Aussenwirtschaftsverordnung (AWV).",
        "Sanktionspruefung saemtlicher Geschaeftspartner vor Vertragsabschluss (ComplyCube, Eu/UN/US/UK-Listen).",
        "Genehmigungspflichtige Lieferungen (BAFA) werden in der Exportkontroll-Datenbank verfolgt; "
        "Antraege werden 8 Wochen vor Lieferung gestellt.",
        "Verantwortlicher Ausfuhrbeauftragter: Stefan Braun (mit Stellvertretung Markus Helmer).",
        "Schulungspflicht aller Mitarbeitenden im Bereich Vertrieb / Einkauf / Service mit Auslandsbezug "
        "(alle 24 Monate Pflichtschulung).",
        "Sondervorgaben fuer Hochrisikolaender (Belarus, Russland, Iran, Nordkorea): "
        "alle Lieferungen Geschaeftsfuehrungsfreigabe.",
    ],
    geltungsbeginn="1. April 2023",
    ansprechpartner="Ausfuhrbeauftragter Stefan Braun")

comp_richtlinie("COMP_007_Richtlinie_Informationssicherhe", "Richtlinie Informationssicherheit (ISMS)",
    schwerpunkte=[
        "ISMS strukturiert nach BSI IT-Grundschutz, Kompatibilitaet TISAX-Anforderungen.",
        "Klassifizierung Informationen in vier Stufen: oeffentlich / intern / vertraulich / streng vertraulich.",
        "Passwort-Richtlinie: mind. 14 Zeichen, MFA-Pflicht bei Cloud-Diensten, Passwort-Manager (Bitwarden).",
        "Mobile Endgeraete: MDM (Microsoft Intune), Festplattenverschluesselung (BitLocker), Remote-Wipe.",
        "Vorgang bei IT-Sicherheitsvorfall: Meldung Hotline +49 221 47832-911 binnen 1 Std., "
        "Triage durch SOC-as-a-Service (Sopra Steria).",
        "Datentraegervernichtung gemaess DIN 66399 Sicherheitsstufe 3.",
        "Externe Penetrationstests jaehrlich (siehe IT_Penetrationstest-Bericht_2023).",
    ],
    geltungsbeginn="1. Juli 2022",
    ansprechpartner="IT-Leitung MMB (Markus Helmer) und externer Informationssicherheitsbeauftragter ISB")


# Compliance-kurzdokumente (jeweils ca. 250-350 Worte)
def comp_short(fname, title, content_paragraphs, subtitle=None):
    write_doc(f"{B9}/{fname}.docx", H, title, subtitle=subtitle,
        sections=[(None, "\n\n".join(content_paragraphs))])

comp_short("Prüfprotokoll_LS800_SN2023001", "Pruefprotokoll Laserschneidanlage LS-800, SN 2023001",
    [
        "Anlage: Laserschneidanlage LS-800 4kW 3-Achs, Seriennummer 2023001 (Endkunde: interner Test-Aufbau / Schauanlage Halle B). "
        "Pruefung gemaess Werkspruef-Vorgaben PRG-LS800-001 vor Auslieferung.",
        "Pruefungsumfang: (1) Lasersicherheit (Klasse 4) gem. EN 60825-1; (2) Maschinenrichtlinie 2006/42/EG inkl. Risikobeurteilung "
        "nach EN ISO 12100; (3) EMV-Pruefung gemaess EN 61000-6-2/-4; (4) Funktionspruefung Schneidleistung (Test-Bleche S235 8 mm "
        "Schnittgeschwindigkeit, Schnittqualitaet Ra < 6,3 µm); (5) Software-/Firmware-Versionscheck; (6) Software-Backup vor Auslieferung.",
        "Pruefergebnis: alle Pruefpunkte bestanden. Schnittqualitaet entspricht Spezifikation. EMV-Pruefung ohne Beanstandung. Doku"
        "mentation gemaess EN 1090 nicht erforderlich (keine tragende Stahlbauteile).",
        "Pruefer: Andreas Goebel (Qualitaetsmanagement), Felix Engelhardt (F&E). Pruefdatum: 14. Mai 2023.",
        "Ergebnis: Anlage zur Auslieferung freigegeben. Begleitende Dokumente vollstaendig (CE-Konformitaetserklaerung, "
        "Bedienungsanleitung Rev. 3, technische Dokumentation gemaess MRL).",
    ], subtitle="Pruefung gemaess interner Verfahrensanweisung PRG-LS800-001")

comp_short("Prüfprotokoll_PL500_SN2023001", "Pruefprotokoll Pressenlinie PL-500, SN 2023001",
    [
        "Anlage: Pressenlinie PL-500 800 t, Seriennummer 2023001 (Endkunde: ThyssenKrupp Steel Europe AG, Werk Duisburg-Hamborn). "
        "Pruefung gemaess Werkspruefvorgaben PRG-PL500-001 vor Auslieferung.",
        "Pruefungsumfang: (1) Maschinenrichtlinie 2006/42/EG inkl. Risikobeurteilung; (2) Druckgeraete-RL 2014/68/EU (Hydraulik"
        "system); (3) EMV-Pruefung gemaess EN 61000-6-2/-4; (4) Pressenkraft-Verifikation 800 t (statisch und dynamisch); "
        "(5) Funktionspruefung Schnellwechselsystem (Gebrauchsmuster DE 20 2021 105 482); (6) IT-Security (OPC-UA / Netzwerk-Scan).",
        "Pruefergebnis: 99,8 % der Pressenkraft-Pruefpunkte innerhalb +/- 1 % Toleranz, alle restlichen Pruefpunkte bestanden. "
        "Schnellwechselsystem Pre-FAT erfolgreich; Wechselzeit 78 Sekunden gegen Spezifikation < 90 Sekunden.",
        "Pruefer: Andreas Goebel (QM), Michael Weber (F&E), Klaus Bauer (Logistik / IBN-Vorbereitung). Pruefdatum: 22. Februar 2024.",
        "Ergebnis: Anlage freigegeben fuer Verschiffung. CE-Konformitaetserklaerung beigefuegt. Begleitende Dokumente "
        "vollstaendig. Pre-FAT mit Kunde am 8. Maerz 2024 erfolgreich.",
    ], subtitle="Pruefung gemaess interner Verfahrensanweisung PRG-PL500-001")

comp_short("Prüfprotokoll_PL500_SN2023002", "Pruefprotokoll Pressenlinie PL-500, SN 2023002",
    [
        "Anlage: Pressenlinie PL-500 1000 t Servo-Option, Seriennummer 2023002 (Endkunde: Bosch Rexroth AG, Werk Lohr am Main). "
        "Pruefung gemaess Werkspruefvorgaben PRG-PL500-002.",
        "Pruefungsumfang erweitert um Servo-Optionspruefung: (1) Servohydraulikleistung 60 kW; (2) Praezisionsmessung Stoesselposition "
        "(Linear-Messsystem 0,5 µm); (3) Funktionspruefung Predictive-Maintenance-Modul (Stream OPC-UA an UNITY-Plattform).",
        "Pruefergebnis: Servohydraulik liefert spezifizierte Leistung mit 5 % Reserve; Praezision Stoesselposition 0,32 µm (besser "
        "als Spezifikation 0,5 µm); PdM-Stream stabil ueber 72 Std. Testbetrieb.",
        "Pruefer: Andreas Goebel (QM), Michael Weber (F&E), Felix Engelhardt (F&E Servo). Pruefdatum: 18. November 2023.",
        "Ergebnis: Anlage freigegeben fuer Lieferung. Lieferzeit gemaess Auftragsbestaetigung AB-2023-018 eingehalten "
        "(Lieferung 14. Dezember 2023).",
    ], subtitle="Pruefung gemaess interner Verfahrensanweisung PRG-PL500-002")

comp_short("CE_Konformitaetserklaerung_LS800", "EG-Konformitaetserklaerung Laserschneidanlage LS-800",
    [
        "Hiermit erklaeren wir, die Halbreiter Maschinenbau GmbH, Industriestrasse 12, 50829 Koeln, in alleiniger Verantwortung, dass "
        "die Maschine Laserschneidanlage LS-800 (in allen Konfigurationen 4kW/6kW/8kW, 3- und 5-Achs) ab Seriennummer 2023001 "
        "den Anforderungen der folgenden EG-Richtlinien entspricht:",
        "- Maschinenrichtlinie 2006/42/EG; - Niederspannungsrichtlinie 2014/35/EU; - EMV-Richtlinie 2014/30/EU; "
        "- (sofern anwendbar) Druckgeraeterichtlinie 2014/68/EU.",
        "Angewandte harmonisierte Normen: EN ISO 12100:2010 (Risikobeurteilung); EN 60204-1:2018 (Elektrik); EN ISO 13849-1:2015 "
        "Kat. 3 PL d (Sicherheitssteuerung); EN 60825-1:2014 (Laserklasse 4); EN 61000-6-2:2019, EN 61000-6-4:2019 (EMV).",
        "Bevollmaechtigter fuer die Zusammenstellung der technischen Unterlagen: Michael Weber, Senior Konstruktionsingenieur, "
        "Halbreiter Maschinenbau GmbH, Industriestrasse 12, 50829 Koeln.",
        "Ort, Datum: Koeln, 14. Mai 2023. Unterzeichner: Klaus Mueller (Geschaeftsfuehrer)."
    ], subtitle="Maschinenrichtlinie 2006/42/EG, Anhang II A")

comp_short("CE_Konformitaetserklaerung_PL500", "EG-Konformitaetserklaerung Pressenlinie PL-500",
    [
        "Hiermit erklaeren wir, die Halbreiter Maschinenbau GmbH, Industriestrasse 12, 50829 Koeln, in alleiniger Verantwortung, dass "
        "die Pressenlinie PL-500 (in den Konfigurationen 500/800/1000 t, mit/ohne Servo-Option, mit/ohne Predictive-Maintenance-Modul) "
        "ab Seriennummer 2023001 den Anforderungen der folgenden EG-Richtlinien entspricht:",
        "- Maschinenrichtlinie 2006/42/EG; - Niederspannungsrichtlinie 2014/35/EU; - EMV-Richtlinie 2014/30/EU; "
        "- Druckgeraeterichtlinie 2014/68/EU (Hydraulikkomponenten Modul 2 und 3).",
        "Angewandte harmonisierte Normen: EN ISO 12100:2010; EN 60204-1:2018; EN ISO 13849-1:2015 Kat. 3 PL d "
        "(Sicherheitssteuerung); EN 692:2005+A1:2009 (Mechanische Pressen / mech. Sicherheit, sinngemaess angewandt); "
        "EN 61000-6-2:2019, EN 61000-6-4:2019; EN ISO 16092-1:2018 (sicherheitstechnische Anforderungen an Pressen).",
        "Bevollmaechtigter fuer die Zusammenstellung der technischen Unterlagen: Michael Weber, Senior Konstruktionsingenieur.",
        "Ort, Datum: Koeln, 22. Februar 2024. Unterzeichner: Klaus Mueller (Geschaeftsfuehrer)."
    ], subtitle="Maschinenrichtlinie 2006/42/EG, Anhang II A")

comp_short("Sicherheitsdatenblatt_Kuehlschmierstoff", "Sicherheitsdatenblatt – Kuehlschmierstoff Castrol Hyspin AWS 46",
    [
        "Produkt: Castrol Hyspin AWS 46 – Hydraulikoel HLP fuer industrielle Anlagen. Anwendung: Hydraulikoel "
        "fuer Pressenlinien PL-500 und LS-800. Verbrauch im Werk Koeln: ca. 18.000 L p. a.",
        "Hersteller: Castrol Limited (Vertrieb DE: BP Europa SE, Bochum). SDB-Version 4.2 vom 18. Mai 2023. "
        "REACH-Registrierungsnummer: hinterlegt im Lieferanten-Portal.",
        "Gefahrenhinweise: Aspirationsgefahr H304 (verschluckungsbedingte Aspiration). Vorsichtsmassnahmen: "
        "Verschlucken vermeiden; mit Wasser ausspuelen; bei Aspiration sofort Krankenhausuebergabe. "
        "Augenkontakt: 15 Min. mit Wasser spuelen.",
        "Brand- und Explosionsverhalten: nicht entzuendlich (Flammpunkt 220 °C). "
        "Loeschmittel: Schaum / Pulver / CO2 (nicht Wasser direkt).",
        "Lagerung: trocken, kuehl, gut belueftet, fern von Zuendquellen. Lagerklasse 10 (brennbar). "
        "Aufbewahrung in Originalbehaeltern; getrennt von Lebensmitteln.",
        "Entsorgung: gemaess AVV 13 01 10* (Hydraulikoel chlorfrei) ueber zertifizierten Entsorger "
        "(Currenta GmbH, Leverkusen). Recyclingsquote rund 88 %.",
    ], subtitle="EG-Sicherheitsdatenblatt nach VO (EG) 1907/2006 (REACH)")

# Restliche 09_Compliance docs (28) - kompakt mit ~250-400w pro Doku
COMP_DOCS = [
    ("COMP_Antikorruptions_Training_2023_Protokoll", "Protokoll Antikorruptionsschulung 2023",
     "Pflichtschulung gemaess Richtlinie COMP_004 (Antikorruption). Durchfuehrung: 14.-22. November 2023 (e-Learning) sowie "
     "8. Dezember 2023 (Praesenztraining fuer Vertrieb / GF). Trainer: RA Dr. Stefan Habicht (Heuking Kuehn Lueer Wojtek). "
     "Teilnahmequote: 99,2 % (245 von 247 Mitarbeitenden); zwei laufende Krankheitsausfaelle. Tests bestanden: 100 % "
     "(Mindestpunktzahl 8 von 10).", "Compliance-Schulungspflicht Q4/2023"),
    ("COMP_FuE_Antrag_Foerderung_BMWi", "Foerderantrag BMWi – Pressenmaschinen 4.0 Edge-KI",
     "Foerderantrag »Pressenmaschinen 4.0 – Adaptive Process Control mit Edge-KI« im BMWi-Programm "
     "»Industrielle Forschung Mittelstand«. Antragssteller: Halbreiter Maschinenbau GmbH gemeinsam mit RWTH Aachen, Lehrstuhl PtU. "
     "Antragsvolumen 2,8 Mio. EUR, davon Foerderquote BMWi 40 % (MMB) und 100 % (RWTH); MMB-Eigenanteil rund 1,2 Mio. EUR. "
     "Projektlaufzeit 36 Monate ab Q3/2024. Hauptbearbeiter: Michael Weber (F&E) und Felix Engelhardt. "
     "Antragsstatus: in Pruefung beim Projekttraeger Forschungszentrum Juelich; Bewilligung erwartet Q2/2024.", "Antrag eingereicht 15. Januar 2024"),
    ("COMP_REACH_Verordnung_Dokumentation", "REACH-Verordnung – Compliance-Dokumentation 2024",
     "Die Halbreiter Maschinenbau GmbH erfuellt die Anforderungen der REACH-Verordnung (VO (EG) 1907/2006) als nachgeschalteter "
     "Anwender. Verwendete Chemikalien (Schmieroele, Kuehlschmierstoffe, Reiniger) sind ueber zugelassene Lieferanten (Castrol, "
     "OKS, Brunox) bezogen. SVHC-Substanzen im Sinne der Kandidatenliste werden nicht aktiv eingesetzt; eine jaehrliche "
     "Pruefung gegen die aktuelle Liste der Europaeischen Chemikalienagentur ECHA erfolgt durch das Umwelt- und Qualitaets"
     "management.", "ECHA-Registrierungsnummer hinterlegt"),
    ("COMP_Abfallentsorgungsnachweis_2023", "Abfallentsorgungsnachweis 2023",
     "Jaehrlicher Nachweis gemaess Nachweisverordnung (NachwV) ueber die Entsorgung gefaehrlicher und nicht gefaehrlicher "
     "Abfaelle. Hauptmengen 2023: Metallspaene Stahl (282 t, recycelt durch Scholz Recycling), Aluminiumspaene (42 t, recycelt), "
     "Hydraulikoele AVV 13 01 10* (4,8 t, Currenta Leverkusen), Schmierfett (1,2 t), industriebeschmutzte Putzlappen "
     "(0,8 t), Verpackungen (38 t, Vertragsmuell). Recyclingsquote insgesamt 91 %. ", "Berichtsjahr 2023, vorgelegt 28.2.2024"),
    ("COMP_Datenschutzerklärung_Website", "Datenschutzerklaerung Website halbreiter-maschinenbau.de",
     "Datenschutzerklaerung gemaess Art. 13 DSGVO. Verantwortlich: Halbreiter Maschinenbau GmbH; DSB: Dr. Markus Lehmann. "
     "Verarbeitete Daten: Server-Logs (IP-Adresse anonymisiert, 7 Tage), Cookies (technisch notwendig, analytisch nach "
     "Einwilligung; Matomo on-premise), Kontaktformular-Daten (Loeschung nach 90 Tagen), Karriere-Bewerbungsdaten (6 Monate). "
     "Rechtsgrundlage: Art. 6 Abs. 1 lit. f und a DSGVO. Betroffenenrechte (Auskunft, Loeschung, Widerspruch, Datenuebertragbarkeit) "
     "ueber datenschutz@halbreiter-maschinenbau.de.", "Stand 1. Januar 2024"),
    ("COMP_Exportkontrollbericht_2023", "Exportkontrollbericht 2023",
     "Jaehrlicher Bericht des Ausfuhrbeauftragten Stefan Braun ueber Anwendung der Exportkontroll-Richtlinie. Berichtsjahr 2023: "
     "23 Lieferungen mit Auslandsbezug, davon 4 genehmigungspflichtig (BAFA-Antraege, alle bewilligt: 2 nach Mexiko, 1 nach "
     "Indien, 1 nach Suedkorea). Sanktionspruefungen: 168 Eingangs- und 142 Ausgangspruefungen, keine Treffer. Schulungspflichten "
     "(jaehrlich): alle relevanten Mitarbeitenden Vertrieb / Service / Einkauf absolviert. Keine Verstoesse oder Auflagen.", "Bericht vom 12. Februar 2024"),
    ("COMP_Notfallplan_Produktionsausfall", "Notfallplan Produktionsausfall",
     "Notfallplan fuer Stoerungen mit Produktions-Stillstand > 4 Stunden. Eskalationsstufen: (1) Vorarbeitende "
     "informiert Produktionsleitung; (2) Krisenstab tagt binnen 2 Std. (CEO, COO/CFO, Produktionsleitung, IT, Sicherheit); "
     "(3) Krisenkommunikation an Kunden bei laenger als 24 Std. ueber Key Account Manager. Wiederanlaufplan: dokumentiert in "
     "VA-OPS-014. Kritische Lieferanten (Trumpf, Siemens, Schunk) haben Service-Hotlines und Reaktionszeitenvereinbarungen. "
     "Tabletop-Uebung jaehrlich (zuletzt 7. November 2023, Szenario: »Brand Halle B mit 4-Wochen-Ausfall«).", "Aktualisiert 15. Januar 2024"),
    ("COMP_Whistleblower_Richtlinie", "Hinweisgeber-Richtlinie (HinSchG)",
     "Umsetzung des Hinweisgeberschutzgesetzes (HinSchG, in Kraft 02.07.2023). Internes Hinweisgebersystem »SPEAK-UP@MMB« "
     "extern gehostet (EQS Group AG). Meldemoeglichkeiten: Web-Formular speakup-mmb.eqs.com, Telefon-Hotline +49 800 999 22 11 "
     "(24/7, mehrsprachig), persoenliche Meldung bei Compliance-Officer. Gewaehrleistet: Vertraulichkeit, Anonymitaet (sofern "
     "gewuenscht), Schutz vor Repressalien. Externe Meldestellen: BAFin, BAFA, BKartA, Bundesamt fuer Justiz. Beachtung "
     "EU-Whistleblower-Richtlinie 2019/1937.", "In Kraft ab 17. Dezember 2023"),
    ("COMP_UVV_Prüfprotokoll_Elektro_2023", "UVV-Pruefprotokoll Elektrische Anlagen 2023",
     "Wiederkehrende Pruefung gemaess DGUV V3 (ehemals BGV A3) der elektrischen Anlagen und Betriebsmittel. Pruefer: "
     "Bruni Elektroanlagen GmbH (zertifiziert nach VDE). Pruefumfang: ortsveraenderliche Betriebsmittel (2.140 Stueck), "
     "ortsfeste Anlagen (Hallen A, B, C, Verwaltung). Pruefintervall: alle 2 Jahre. Pruefergebnis: 4 Maengelmeldungen "
     "(2 mittlere, 2 leichte), alle binnen 14 Tagen behoben. Empfehlung: Defibrillator-Standorte mit jaehrlicher "
     "Funktionspruefung. Pruefbericht-Nr.: BRU-2023-MMB-VDE-014, ausgestellt am 18. November 2023.", "Pruefung 14.-18. November 2023"),
    ("COMP_Betriebsbegehungsprotokoll_BG_", "Betriebsbegehungsprotokoll BG Holz und Metall 2023",
     "Begehung durch die Berufsgenossenschaft Holz und Metall (BGHM), Aussendienst Koeln, am 25. September 2023. "
     "Begehungsschwerpunkte: Pressensicherheit Halle A/B, Lagerorganisation Halle C, ergonomische Arbeitsplaetze "
     "Verwaltung, Hautschutz / PSA bei Hydraulik-/Schmiermitteln. 4 Empfehlungen ausgesprochen, davon 2 bereits umgesetzt "
     "(Anti-Rutschstreifen Treppe Halle A, ergonomische Stuehle Buchhaltung). 2 in Bearbeitung "
     "(Schallschutz Spaetschicht Halle B, Laermkapselung Stanzpressen).", "Protokoll vom 28. September 2023"),
    ("COMP_Qualitätsprüfbericht_Q4_2023", "Qualitaetspruefbericht Q4/2023",
     "Pruefbericht Q4/2023 ueber die Qualitaetsperformance des Werkes Koeln. KPI-Ergebnisse: First-Pass-Yield 96,8 % "
     "(Ziel ≥ 95 %), Reklamationsquote 0,68 % (Ziel ≤ 0,80 %), Stillstandsquote 5,2 % (Ziel ≤ 6 %), Wartungs-Compliance "
     "98,1 % (Ziel ≥ 95 %). Erstmusterquote 100 %. Interne Audits (ISO 9001) im Berichtszeitraum: 4 Audits, "
     "8 Nicht-Konformitaeten (alle behoben), 22 Verbesserungsempfehlungen.", "Stand 31. Januar 2024"),
    ("COMP_Revisionsplan_2024", "Revisions- und Auditplan 2024 (Internal Audit)",
     "Internal-Audit-Plan 2024 verantwortet durch das Compliance- und Risikoteam. Geplante Audits: "
     "Q1 2024: Beschaffungsprozess (Purchase-to-Pay); Q2 2024: Reise- und Bewirtungsabrechnungen (Stichprobe 5 %); "
     "Q3 2024: Datenschutz (DSGVO-Audit incl. AVV-Pruefung); Q4 2024: IT-Berechtigungsmanagement (Funktionstrennung). "
     "Daneben: jaehrliche Wiederholungsaudits ISO 9001 (TUEV) und ISO 50001 (Energiemanagement). "
     "Ergebnis-Reporting an Geschaeftsfuehrung und Beirat.", "Genehmigt 14. Februar 2024"),
    ("COMP_FuE_Bericht_2023", "Forschungs- und Entwicklungsbericht 2023",
     "F&E-Aktivitaeten 2023 ueberblicksweise: Aufwendungen 1.994 TEUR (= 4,1 % vom Umsatz, Vorjahr 3,8 %). "
     "Wesentliche Projekte: Predictive Maintenance Plattform (UNITY-Kooperation, siehe IP_Software_Entwicklungsvertrag_UNITY); "
     "Adaptive Process Control RWTH Aachen (Technologietransfer, siehe IP_Technologie_Transfer_RWTH); "
     "Pressenlinie PL-500 Servo-Option (Markteinfuehrung Q3/2023); Laserschneidanlage LS-800 5-Achs-Modul; "
     "Schnellwechselsystem (Gebrauchsmuster). Personal F&E: 18 FTE (Vorjahr 16). Foerdermittel: bewilligt 142 TEUR "
     "(ZIM-Programm); beantragt 1,2 Mio. EUR (BMWi).", "Bericht vom 22. Februar 2024"),
    ("COMP_Einheitliche_Europäische_Eigen", "Einheitliche Europaeische Eigenerklaerung (ESPD) – Vergabe Stadt Koeln 2024",
     "Vorlage der Einheitlichen Europaeischen Eigenerklaerung (ESPD) gemaess EU-Vergaberichtlinie 2014/24/EU im Rahmen der "
     "Ausschreibung der Stadt Koeln »Modernisierung Maschinenpark Stadtreinigung« (Bekanntmachung TED 2024/S 042-0185). "
     "MMB bestaetigt: keine Insolvenz / Liquidation; keine rechtskraeftigen Verurteilungen wg. Korruption, Geldwaesche, "
     "Steuerhinterziehung, Kinderarbeit / Menschenhandel oder Beteiligung an organisiertem Verbrechen; Anerkennung der "
     "Eignungskriterien gemaess Ausschreibungsunterlage; Beteiligung am Auftrag in Bietergemeinschaft mit Dürr AG.", "Eigenerklaerung gemaess EU 2014/24/EU"),
    ("COMP_CO2-Bilanz_2023_Corporate_Car", "CO2-Bilanz 2023 (Corporate Carbon Footprint)",
     "Erstmalige Erstellung des Corporate Carbon Footprint (CCF) gemaess GHG-Protocol nach Scopes 1, 2 und 3 fuer 2023. "
     "Ergebnis: Scope 1 (direkte Emissionen): 1.840 t CO2eq (Verbrennungsmotoren Fuhrpark, Heizung Erdgas); "
     "Scope 2 (Energie eingekauft): 2.180 t CO2eq (Strom-Mix Deutschland 2023, in Q3 Wechsel zu Oekostrom 100 %); "
     "Scope 3 (vor- und nachgelagerte Kette): 12.480 t CO2eq (Material, Logistik, Geschaeftsreisen, Produktnutzung). "
     "Gesamt-Footprint: 16.500 t CO2eq. Intensitaet: 339 t CO2eq / Mio. EUR Umsatz. Reduktionsziel 2030: -50 % (Scope 1+2, "
     "Basisjahr 2021). Massnahmen: Oekostromwechsel, PV-Eigenstrom, E-Mobilitaet, Energieoptimierung Pressen.", "GHG-Protocol CCF 2023, erstellt 8. April 2024"),
    ("COMP_Maßnahmenplan_ISO_9001_Audit_2", "Massnahmenplan ISO 9001:2015 – Audit 2023",
     "Ergebnis Surveillance Audit ISO 9001:2015 durch TUEV Rheinland (Berichts-Nr. TR-MMB-2023-Q3) am 14.-16. Oktober 2023. "
     "Auditergebnis: kein major non-conformity; 3 minor non-conformities, 8 Verbesserungsempfehlungen. "
     "Massnahmenplan (Verantwortlich: Andreas Goebel QM-Leitung): (1) Aktualisierung Prozesslandkarte bis 31.1.2024 "
     "(erfolgt); (2) Erweiterung Risikomanagement-Methodik FMEA bis 31.3.2024 (in Bearbeitung); (3) Schulung interner "
     "Auditoren bis 30.6.2024. Re-Zertifizierung 2025 vorgesehen.", "ISO-Folgeaudit 2024"),
    ("COMP_Datenschutzfolgeabschaetzung_CRM", "Datenschutz-Folgenabschaetzung (DSFA) CRM-System 2024",
     "DSFA gemaess Art. 35 DSGVO fuer das CRM-System Salesforce Sales Cloud Enterprise. Auftraggeber: Vertriebsleitung, "
     "Verantwortlich: DSB Dr. Markus Lehmann. Verarbeitungszweck: Kundenkontaktmanagement, Vertriebssteuerung, "
     "Service-Disposition. Datenkategorien: Stammdaten (Name, Adresse, Funktion), Kommunikationshistorie, "
     "Servicedaten von Maschinen. Rechtsgrundlage: Art. 6 Abs. 1 lit. b und f DSGVO. Risikobewertung: mittel "
     "(Personenbezug, internationale Datenverarbeitung). Schutzmassnahmen: Berechtigungskonzept, "
     "Verschluesselung at-rest und in-transit, EU-Datenhaltung primaer Frankfurt, AVV gemaess Art. 28 DSGVO, "
     "Standard Contractual Clauses, jaehrlicher Audit-Bericht Salesforce Trust.", "Erstellung 18. Januar 2024"),
    ("COMP_Internes_Audit_ISO_9001_2023", "Internes Audit ISO 9001:2015 – Programm 2023",
     "Programm interner Audits 2023 gemaess ISO 9001:2015 Klausel 9.2. Durchgefuehrte Audits: 4 (Beschaffung, "
     "Konstruktion / F&E, Service / After-Sales, Wareneingang). Auditor:innen intern: Andreas Goebel (QM), "
     "Sabine Koch (Personal), Petra Zimmermann (Finanzen). Ergebnisse: 8 Nicht-Konformitaeten (alle behoben), "
     "22 Verbesserungsempfehlungen. Highlights: Erweiterung der Stichprobenpruefung bei Wareneingang; "
     "Aktualisierung des Konstruktions-Review-Prozesses. Vorbereitung externes Audit TUEV Rheinland: "
     "Surveillance Q4/2024.", "Programm-Verantwortlich: Andreas Goebel"),
    ("COMP_Energiemanagementsystem_DIN_EN_ISO_50001", "Energiemanagementsystem DIN EN ISO 50001 – Statusbericht",
     "Statusbericht zur Zertifizierung ISO 50001:2018 (Energiemanagementsystem). Erstzertifizierung 2020 erfolgreich; "
     "Surveillance-Audits 2021, 2022, 2023 bestanden. Re-Zertifizierung 2026 vorgesehen. Energieintensitaet 2023: "
     "318 MWh/Mio. EUR Umsatz (Vorjahr 348 MWh/Mio. EUR Umsatz, -8,6 %). Massnahmen 2023: LED-Komplettumruestung "
     "Hallen abgeschlossen (Einsparung 92 MWh p. a.); PV-Aufdachanlage 220 kWp (Einsparung 198 MWh p. a.); "
     "Energieoptimierung Pressen via Predictive Maintenance (Einsparung geschaetzt 45 MWh p. a.). "
     "Naechste Massnahmen: BHKW-Modernisierung (Q3/2024); Waermerueckgewinnung Hallenlueftung.", "Berichtsperiode 2023"),
    ("COMP_Lieferantenbewertung_Matrix_2023", "Lieferanten-Risikomatrix 2023 (Compliance-Schwerpunkt)",
     "Compliance-orientierte Lieferanten-Risikomatrix 2023 unter Beruecksichtigung der LkSG-Anforderungen "
     "(Lieferkettensorgfaltspflichtengesetz, gueltig fuer MMB ab 2024 aufgrund Schwellenwert >= 1000 MA nicht zwingend, "
     "freiwillige Anwendung). Bewertet wurden 24 strategische Lieferanten (Direct + Indirect). Risikodimensionen: "
     "Menschenrechte, Arbeitsbedingungen, Umweltverhalten, Korruptionsrisiko, Sanktionsrisiko, Geopolitik. "
     "Ergebnis: 18 Lieferanten »niedrig«, 5 »mittel«, 1 »erhoeht« (Lieferant in Suedostasien mit verifiziertem "
     "Audit-Befund). Massnahmen: Risikomonitoring quartalsweise, gezielte Audits bei mittlerem Risiko (24-Monats-Rhythmus), "
     "Eskalation und Massnahmenplan bei erhoehtem Risiko.", "Stand 31. Januar 2024"),
    ("COMP_Arbeitsschutz_Gefaehrdungsbeurteilung_2023", "Gefaehrdungsbeurteilung Arbeitsschutz 2023",
     "Jaehrliche Gefaehrdungsbeurteilung gemaess § 5 ArbSchG ueber alle Arbeitsbereiche und Anlagentypen "
     "des Werkes Koeln. Bewertung durch Sicherheitsfachkraft Dipl.-Ing. Helmut Wiedemann (extern, asecos GmbH). "
     "Schwerpunkte: Pressen-Quetsch- und Scherenrisiken (Halle A/B), Laserstrahlrisiken (Halle B), "
     "Foerdersystem-Klemmrisiken (Halle C), psychische Belastungen Schichtarbeit, Heben und Tragen, "
     "ergonomische Arbeitsplaetze, Hautschutz Hydraulik. Massnahmen: 14 abgeleitete Schutzmassnahmen, "
     "11 davon abgeschlossen. Schulung Mitarbeitende (alle 24 Mo. verpflichtend).", "Berichtszeitraum 2023"),
    ("COMP_Risikoregister_2024", "Risikoregister 2024 (Top-10-Risiken)",
     "Aktualisiertes Risikoregister gemaess KonTraG / DIIR-Risk-Standard. Top-10-Risiken: "
     "(1) Materialverfuegbarkeit Elektronik (hoch), (2) Kundenkonzentration Top-5 (mittel), "
     "(3) Energiepreisschwankungen (mittel), (4) Cyber-Sicherheit (hoch, steigend), "
     "(5) Demografie / Schluesselpersonen (mittel), (6) Geldpolitik / Zinskosten (mittel), "
     "(7) Lieferkettenrisiken Asien-Krise (mittel), (8) ESG / Berichtspflichten (mittel), "
     "(9) Wettbewerber-Konsolidierung (niedrig), (10) Wechselkursrisiko USD/MXN (mittel-niedrig, gehedged). "
     "Mitigationen: Zweitquellen, Hedging, Cyber-Versicherung, Workforce-Planning, Innovationen Pressenlinie 4.0.", "Stand 14. Februar 2024"),
    ("COMP_Aufsichtsbehörden_Kommunikation_2023", "Kommunikation mit Aufsichtsbehoerden 2023",
     "Berichtswesen ueber Schriftverkehr / Antraege / Begehungen mit Aufsichtsbehoerden im Berichtszeitraum 2023. "
     "Anlasslose Begehungen: Bezirksregierung Koeln (BImSchG, 18. April 2023, ohne Beanstandung); BG Holz und Metall "
     "(25. September 2023, 4 Empfehlungen); Hauptzollamt Koeln (Routineaudit AEO-C, ohne Beanstandung). "
     "Antragsverfahren: 4 Ausfuhrgenehmigungen BAFA (alle bewilligt); 1 BImSchG-Aenderungsanzeige (Halle B-Erweiterung, "
     "in Bearbeitung 2024); 1 KfW-Foerderantrag Energieeffizienz (bewilligt 25 TEUR Zuschuss). "
     "Keine Ordnungswidrigkeitsverfahren oder Bussgeldverfahren.", "Berichtsjahr 2023"),
    ("COMP_Nachhaltigkeitsbericht_2023", "Nachhaltigkeitsbericht 2023",
     "Erster freiwilliger Nachhaltigkeitsbericht der Halbreiter Maschinenbau GmbH gemaess GRI Standards 2021 "
     "(Core-Variante). Schwerpunkte: Umwelt (Energie, Treibhausgase, Wasser, Abfaelle), Soziales (Beschaeftigte, "
     "Arbeitssicherheit, Vielfalt, Aus- und Weiterbildung), Governance (Compliance, Lieferkette, Risikomanagement). "
     "Highlights 2023: Erstmaliger CCF (16.500 t CO2eq), Oekostromwechsel 100 % Q3, PV-Aufdachanlage 220 kWp "
     "fertiggestellt, Aufnahme der Lieferantenrisikomatrix (Compliance-Schwerpunkt LkSG). Vorbereitung CSRD: "
     "Anforderungsanalyse Q3/2024, Berichtspflicht ab 2025 fuer das Geschaeftsjahr 2024 (groesse Unternehmen). "
     "Pruefer 2023 freiwillig: BDO AG WPG (Limited Assurance).", "Berichtszeitraum 2023, veroeffentlicht 14. Juni 2024"),
]

for fn, title, body, subt in COMP_DOCS:
    comp_short(fn, title, [body], subtitle=subt)


# ──────────────────────────────────────────────────────────────────────────
# 10_IT_Infrastruktur (9 docs)
# ──────────────────────────────────────────────────────────────────────────
B10 = f"{D}/10_IT_Infrastruktur"

def short_doc(folder, fname, title, body_text, subtitle):
    write_doc(f"{folder}/{fname}.docx", H, title, subtitle=subtitle,
        sections=[(None, body_text)])

short_doc(B10, "IT_IT-Notfallhandbuch", "IT-Notfallhandbuch (BCM)",
    "Das IT-Notfallhandbuch der Halbreiter Maschinenbau GmbH regelt das Vorgehen bei IT-bedingten Notfaellen "
    "(Ausfall Rechenzentrum, Ransomware, Datenverlust, Cyberangriff). Verantwortlich: IT-Leitung Markus Helmer; "
    "Krisenstab unter Leitung CEO Klaus Mueller.\n\n"
    "Definierte Stufen: (1) Stoerung (Reaktion 1 Std., Standardprozess); (2) Notfall (Reaktion 30 Min., Krisenstab); "
    "(3) Katastrophe (Reaktion 15 Min., externe Eskalation incl. Krisenkommunikation an Kunden / Behoerden).\n\n"
    "Wesentliche Massnahmen: Off-Site-Backups taeglich (Bunker Frankfurt), Datenwiederherstellungs-Test halbjaehrlich, "
    "definierte RTO (Recovery Time Objective) je System: kritisch 4 Std., wichtig 24 Std., normal 5 Werktage. "
    "Notfall-Hotline +49 221 47832-911 (24/7). Tabletop-Uebung jaehrlich (zuletzt 7. November 2023, Szenario "
    "»Ransomware mit SAP-Verschluesselung«). Externe Partner: Sopra Steria SOC-as-a-Service, BSI-Beratung "
    "BTC Business Technology Consulting AG.\n\nDas Handbuch wird mindestens alle 24 Monate ueberprueft und "
    "bei Bedarf aktualisiert.",
    "Version 4.1, Stand 1. Februar 2024")

short_doc(B10, "IT_Penetrationstest-Bericht_2023", "Penetrationstest-Bericht 2023",
    "Externer Penetrationstest der IT-Infrastruktur der Halbreiter Maschinenbau GmbH, durchgefuehrt durch die "
    "SySS GmbH (Tuebingen) im Zeitraum 12.-26. Oktober 2023. Pruefumfang: externe Internet-Schnittstellen "
    "(Webserver, VPN-Gateways, Microsoft 365-Zugaenge), interne Netzwerke (Office-Netz, OT-Netz Produktion), "
    "Active Directory, SAP S/4HANA und CRM Salesforce.\n\n"
    "Ergebnis: 3 Findings high (umgehend behoben), 7 Findings medium (behoben innerhalb 30 Tage), "
    "14 Findings low (Massnahmenplan 2024). Wesentliche Befunde: (1) veralteter VPN-Client auf einem "
    "Sub-Tier-Lieferanten-Notebook; (2) Service-Account mit ueberzogenen Rechten in Active Directory; "
    "(3) ungepatchte Firmware OT-Switch in Halle B. Alle Findings durch Massnahmenplan adressiert und "
    "verifiziert. Re-Test 2024 vorgesehen.\n\n"
    "Empfehlung: Aufbau eines Schwachstellenmanagement-Tools (Nessus Professional oder OpenVAS); "
    "Implementierung in Q2/2024.",
    "Bericht-Nr. SYSS-MMB-2023-014, Datum 8. November 2023")

short_doc(B10, "IT_Backup-Restore-Konzept", "Backup- und Restore-Konzept",
    "Backup-Konzept der Halbreiter Maschinenbau GmbH. Strategie: 3-2-1-Regel (3 Kopien, 2 Medien, 1 off-site). "
    "Backup-Loesung: Veeam Backup & Replication Enterprise (HCI-Storage von HPE). Sicherungsfrequenz: "
    "produktive Systeme alle 4 Std. (Incremental), taeglich Vollsicherung. Aufbewahrung: 30 Tage Online, "
    "12 Monate Offline (Tape), 7 Jahre Archive (GoBD-Pflicht).\n\nKritische Systeme: SAP S/4HANA "
    "(RTO 4 Std., RPO 1 Std.), Salesforce CRM (Cloud-Backup separat), File-Server (RTO 8 Std., RPO 4 Std.), "
    "MES Halle B (RTO 12 Std., RPO 4 Std.), CAD-/PDM-Server SOLIDWORKS (RTO 8 Std., RPO 4 Std.).\n\n"
    "Off-Site-Backup: bunker-gesicherter Standort Frankfurt (Iron Mountain Deutschland GmbH). Daily-Sync "
    "ueber dedizierte 1 Gbit-Leitung. Disaster-Recovery-Test halbjaehrlich; letzter Test 14. November 2023 "
    "erfolgreich (SAP-Wiederherstellung in 3 Std. 18 Min., innerhalb RTO).\n\n"
    "Verantwortlich: Markus Helmer (IT-Leitung); externer Partner: Computacenter AG fuer Backup-Operations.",
    "Version 3.1, Stand 1. Februar 2024")

short_doc(B10, "IT_Netzwerkdokumentation_2024", "Netzwerkdokumentation 2024",
    "Netzwerkarchitektur der Halbreiter Maschinenbau GmbH: getrenntes Office- und OT-Netzwerk mit "
    "definierten Schnittstellen (Datendiode / FW-Cluster). \n\n"
    "Office-Netz: Cisco Catalyst 9300-Switche (12 Stueck), redundant. Firewall: Palo Alto PA-3260 HA-Cluster. "
    "WLAN: Cisco Meraki MR-Serie (Standort: 12 Access Points). Endpoints: 218 Notebooks/Desktops; "
    "MDM ueber Microsoft Intune.\n\n"
    "OT-Netz: separater Switch-Stack (Cisco IE-4000) je Halle (A, B, C). VLAN-Segmentierung gemaess "
    "IEC 62443 (Purdue-Modell). Industrial Firewall an Schnittstelle Office<->OT (Hirschmann Eagle). "
    "Remote-Wartung Maschinen: dedizierter Reverse-Proxy mit Tagesfreischaltung; Audit-Log SIEM.\n\n"
    "Internetanbindung: 2x 1 Gbit Glasfaser (Telekom + NetCologne) als Active-Standby. WAN-Backup: "
    "LTE-Router fuer Notfallbetrieb.\n\nDie Netzwerkdokumentation wird quartalsweise aktualisiert und ist im "
    "internen ECM hinterlegt. Verantwortlich: Markus Helmer.",
    "Stand 1. Februar 2024")

short_doc(B10, "IT_IT-Sicherheitskonzept_2024", "IT-Sicherheitskonzept 2024",
    "IT-Sicherheitskonzept der Halbreiter Maschinenbau GmbH gemaess BSI IT-Grundschutz Bausteinen "
    "(2023-Version) sowie unter Beruecksichtigung der TISAX-Anforderungen (Vorbereitung Assessment 2025). "
    "Schutzbedarfsfeststellung: Verfuegbarkeit hoch (Produktion), Integritaet hoch (Konstruktionsdaten), "
    "Vertraulichkeit hoch (Kundendaten, IP).\n\n"
    "Schutzmassnahmen: (1) Zero-Trust-Architektur (Schrittweise Einfuehrung 2024-2025); "
    "(2) MFA-Pflicht fuer alle Cloud-Dienste (Microsoft Entra ID); (3) EDR CrowdStrike Falcon auf allen "
    "Endpoints und Servern; (4) SIEM-System (Sopra Steria SOC-as-a-Service, 24/7-Monitoring); "
    "(5) Berechtigungsmanagement (Least Privilege; Quartals-Review aller AD-Gruppen); "
    "(6) Awareness-Programm (jaehrliche Pflichtschulung, Phishing-Simulationen 4x p. a.).\n\n"
    "Sicherheitsvorfaelle 2023: 4 Vorfaelle (3 niedrig, 1 mittel; alle innerhalb von 4 Std. eingedaemmt). "
    "Keine Datenexfiltration. Keine produktionswirksamen Ausfaelle.\n\n"
    "Audit-/Zertifizierungsstatus: ISO 27001 nicht (noch nicht) erforderlich, aber TISAX-Vorbereitung Q4/2024. "
    "Externe Berater: BTC Business Technology Consulting AG.",
    "Version 5.2, Stand 14. Februar 2024")

short_doc(B10, "IT_Disaster_Recovery_Plan_2024", "Disaster-Recovery-Plan 2024",
    "Disaster-Recovery-Plan (DRP) der Halbreiter Maschinenbau GmbH; ergaenzt zum IT-Notfallhandbuch (BCM-Doku). "
    "Festgelegt sind Wiederanlaufverfahren fuer 12 kritische IT-Systeme. RTO/RPO-Klassen: "
    "Klasse A (kritisch: SAP S/4HANA, AD, Datei-/CAD-Server) RTO 4 Std., RPO 1 Std.; "
    "Klasse B (wichtig: CRM Salesforce, MES, BI) RTO 24 Std., RPO 4 Std.; "
    "Klasse C (normal: Tools, Sharepoint) RTO 5 WT, RPO 24 Std.\n\n"
    "Wiederanlauf-Prozeduren dokumentiert in Runbooks (Sharepoint /it/runbooks). Backup-Standort: Iron Mountain "
    "Frankfurt. Wiederanlauf-Test halbjaehrlich. Letzter Vollst-Test: 14. November 2023 - alle Klasse-A-Systeme "
    "innerhalb RTO wiederhergestellt; Klasse B mit minimaler Abweichung +2 Std. (akzeptiert).\n\n"
    "Eskalationspfad bei DR-Ausloeser: IT-Leitung Markus Helmer -> CFO Sandra Becker -> CEO Klaus Mueller. "
    "Externe Partner: Computacenter AG (Restore-Operations), Sopra Steria (Forensik bei Cyber).\n\n"
    "Der DRP wird jaehrlich ueberarbeitet und nach jedem Test aktualisiert.",
    "Version 3.2, Stand 14. Februar 2024")

short_doc(B10, "IT_ISMS-Richtlinie_Passwortmanage", "ISMS-Richtlinie Passwortmanagement",
    "Diese Richtlinie regelt die Erstellung, Verwendung und Aufbewahrung von Passwoertern bei der "
    "Halbreiter Maschinenbau GmbH. Sie gilt fuer alle Beschaeftigten und externen Beteiligten, die Zugriff "
    "auf MMB-IT-Systeme erhalten.\n\n"
    "Anforderungen: Mindestlaenge 14 Zeichen (Passphrasen erlaubt); Komplexitaet: 3 von 4 Zeichenklassen "
    "(Klein- und Grossbuchstaben, Ziffern, Sonderzeichen); maximale Lebensdauer 365 Tage (nur bei "
    "Sicherheitsvorfall vorzeitige Erneuerung); Sperre nach 5 fehlgeschlagenen Anmeldeversuchen.\n\n"
    "MFA-Pflicht: alle Cloud-Dienste (Microsoft 365, Salesforce, SAP Concur), VPN, privilegierte Konten "
    "(Domain Admin etc.). MFA-Methoden: Microsoft Authenticator (App), Hardware-Token (YubiKey) fuer "
    "GF und IT-Admin-Konten.\n\n"
    "Passwort-Manager: Bitwarden (Enterprise-Lizenz, on-premise gehostet). Personliche Passwoerter sowie "
    "Team-Vaults fuer geteilte Konten. Speicherung von Passwoertern in Klartext-Notizen, E-Mails oder "
    "Browser-Standardspeichern ist verboten.\n\n"
    "Sanktionierung von Verstoessen: Information IT-Sicherheitsbeauftragter, ggf. arbeitsrechtliche "
    "Konsequenzen bei wiederholten Verstoessen. Schulung jaehrlich verpflichtend.",
    "Version 2.1, Stand 1. Februar 2024")

short_doc(B10, "IT_Software-Inventar_2024", "Software-Inventar 2024",
    "Inventarisierung der eingesetzten Anwendungs- und Systemsoftware der Halbreiter Maschinenbau GmbH "
    "(zentral verwaltet ueber Microsoft Endpoint Configuration Manager + Lansweeper).\n\n"
    "Wesentliche Anwendungen:\n"
    "- ERP: SAP S/4HANA On-Premise Release 2023 (IP_004); 180 Named-User-Lizenzen.\n"
    "- CRM: Salesforce Sales Cloud Enterprise (IP_005); 28 User.\n"
    "- CAD/PDM: SOLIDWORKS Premium 2024 + SOLIDWORKS PDM (IP_008); 28 + 30 Lizenzen.\n"
    "- CAD ergaenzend: AutoCAD Mechanical 2024 (IP_007); 18 + 12 Lizenzen LT.\n"
    "- CNC-Steuerung: Siemens SINUMERIK ONE (IP_006); 18 Run-time-Lizenzen.\n"
    "- Office: Microsoft 365 E3 (218 Lizenzen).\n"
    "- Buchhaltung: DATEV Eigenorganisation Comfort (Externer Steuerberater).\n"
    "- IT-Security: CrowdStrike Falcon (Endpoint), Microsoft Defender for OT, Palo Alto Firewall.\n"
    "- Backup: Veeam Backup & Replication Enterprise.\n"
    "- Personal: Sage HR Suite (subscription).\n"
    "- Predictive Maintenance: UNITY Custom-Loesung (in Pilot).\n\n"
    "Lizenz-Compliance: SAP Audit Mai 2023 ohne Beanstandung. Microsoft-Audit zuletzt 2022. "
    "Open-Source-Komponenten (z. B. Linux-Server, Python, Apache) gemaess interner OSS-Compliance-Vorgaben.",
    "Stand 1. Februar 2024")

short_doc(B10, "IT_Cloud_Strategie_2024_2026", "Cloud-Strategie 2024-2026",
    "Cloud-Strategie der Halbreiter Maschinenbau GmbH fuer den Zeitraum 2024-2026; verabschiedet im Rahmen "
    "der Digitalisierungsoffensive (Gesellschafterbeschluss 2024/03). Leitlinie: "
    "»Cloud-First fuer nicht-produktionskritische Anwendungen, On-Premise fuer OT und Konstruktion«.\n\n"
    "Geplante Cloud-Migrationen 2024: (1) CRM Salesforce – bereits in der Cloud; (2) Microsoft 365 – "
    "bereits in der Cloud; (3) Personal-Software Sage HR – Wechsel zu Sage Cloud bis Q3/2024; "
    "(4) BI/Reporting (Microsoft Power BI Premium); (5) Lernplattform (talentsoft, Q2/2024).\n\n"
    "Bleibt On-Premise: SAP S/4HANA (mind. bis 2027, dann Pruefung S/4HANA Cloud Private Edition); "
    "CAD/PDM SOLIDWORKS (auch in 2026 noch on-prem aus Performance-Gruenden); "
    "MES (Halle B Pilot, anlagennah).\n\n"
    "Anbieter-Politik: Multi-Cloud (Microsoft Azure primaer, Salesforce Cloud, einzelne SaaS). "
    "Datenresidenz: EU (Frankfurt / Dublin) bevorzugt. Compliance: AVV Art. 28 DSGVO, SCC fuer "
    "Datenexport. Cloud-Sicherheit gemaess CSA STAR und ISO 27001-Standard der Anbieter.\n\n"
    "Investitionsbedarf 2024-2026: ca. 480.000 EUR (Lizenzen + Migrationsaufwand + Schulung).",
    "Beschlossen 14. Februar 2024")


# ──────────────────────────────────────────────────────────────────────────
# 11_Strategie_Planung (7 docs)
# ──────────────────────────────────────────────────────────────────────────
B11 = f"{D}/11_Strategie_Planung"

short_doc(B11, "STRAT_Energieverbrauchsanalyse_2023", "Energieverbrauchsanalyse 2023",
    "Detaillierte Analyse des Energieverbrauchs des Werkes Koeln im Geschaeftsjahr 2023, vorbereitet "
    "durch das Energiemanagement-Team (verantwortlich: Klaus Bauer Logistikleitung) im Rahmen des "
    "zertifizierten Energiemanagementsystems ISO 50001:2018.\n\nGesamtverbrauch 2023: Strom 5.420 MWh "
    "(Vorjahr 5.910 MWh, -8,3 %), Erdgas 2.180 MWh (Vorjahr 2.420 MWh, -9,9 %), Heizoel 80 MWh. "
    "Energieintensitaet 318 MWh / Mio. EUR Umsatz (Vorjahr 348 MWh).\n\nGroesste Verbraucher: "
    "Pressenlinien Halle A/B (2.420 MWh, 45 % vom Strom), Laser- und Robotik-Anlagen Halle B "
    "(1.620 MWh, 30 %), Lueftung und Klima (520 MWh), Verwaltung (310 MWh), Druckluft (380 MWh).\n\n"
    "Massnahmenwirkung 2023: LED-Komplettumruestung (-92 MWh p. a.), PV-Aufdachanlage 220 kWp ab "
    "Q4/2023 (-198 MWh p. a. erwartet, erste Daten in 2024), Predictive Maintenance Pressen "
    "(geschaetzt -45 MWh p. a.), KNX-Bus-Steuerung Verwaltung (-32 MWh).\n\nAusblick 2024: "
    "BHKW-Modernisierung (Investitionsfreigabe Q2 erwartet); Waermerueckgewinnung Hallenlueftung; "
    "Wechsel zu Oekostrom 100 % seit Q3/2023; Pruefung Erweiterung PV-Anlage Halle A.",
    "Berichtszeitraum 2023, Stand 14. Februar 2024")

short_doc(B11, "STRAT_Beiratssitzung_Protokoll_2024", "Protokoll Beiratssitzung Q1/2024",
    "Sitzung des Beirats der Halbreiter Maschinenbau GmbH am 22. Februar 2024, 14:00-18:00 Uhr, "
    "Konferenzraum »Rhein« am Hauptsitz Koeln.\n\nAnwesend: Prof. Dr.-Ing. Bernhard Roth (Vorsitzender, "
    "RWTH Aachen Lehrstuhl Maschinenelemente), Dr. Joerg Wiebold (externes Mitglied, ehem. CFO Voith "
    "Industrial Services), Frau Elke Mueller-Hartmann (Familienvertreterin, Mueller Familien-GbR). "
    "Geladen GF: Klaus Mueller, Sandra Becker. Protokoll: Andrea Hoffmann.\n\nTagesordnung: "
    "(1) Genehmigung Protokoll Sitzung Q4/2023; (2) Bericht der Geschaeftsfuehrung zum Geschaeftsverlauf "
    "2023 (vorlaeufige Zahlen); (3) Strategie 2024-2026 / Digitalisierungsoffensive (Gesellschafterbeschluss "
    "2024/03); (4) Beratung Investitionsplan 2024 (Volumen 2,15 Mio. EUR); (5) Personalentwicklung und "
    "Nachfolgeplanung (Demografie); (6) Markt- und Wettbewerbsanalyse 2024; (7) Verschiedenes.\n\n"
    "Wesentliche Punkte: Beirat lobt die positive Geschaeftsentwicklung 2023 (Umsatz +12,4 %, "
    "Auftragsbestand +18 %) und befuerwortet einstimmig die Digitalisierungsoffensive 2024-2026 sowie "
    "den Investitionsplan 2024. Anregung: vertiefte Befassung mit Stellantis und VW als potenzielle "
    "Neukunden in 2024/2025 (Roadmap praesentiert von KAM Markus Fischer); Pruefung strategischer "
    "Partnerschaften mit Predictive-Maintenance-Anbietern (Co-Innovation Siemens, UNITY).\n\nNaechste "
    "Beiratssitzung: 13. Juni 2024.",
    "Sitzungsnr. BR-2024-01 vom 22. Februar 2024")

short_doc(B11, "STRAT_Roadmap_Internationalisierung_2025", "Roadmap Internationalisierung 2025-2027",
    "Strategische Roadmap zur internationalen Markterschliessung 2025-2027. Hintergrund: aktueller "
    "Auslandsanteil am Umsatz rund 14 % (2023), Steigerung auf 25 % bis 2027 angestrebt.\n\n"
    "Phase 1 (2024/2025): Ausbau Mexiko (Werk Queretaro Dürr AG) als Brueckenkopf; Lokal-Praesenz "
    "ueber Vertretungs-Office bei Dürr de México; erste eigene Servicestaerke (2 Techniker, jeweils mit "
    "Mexiko-Mandat). Erwarteter Umsatz Mexiko 2025: 3,8 Mio. EUR.\n\nPhase 2 (2025/2026): "
    "Asien-Strategie (China + Suedostasien). Aufbau Service-Hub Suzhou (Ostchina); Kooperationspartner: "
    "Trumpf China (Service-Kapazitaeten); Pilotkunde: in Verhandlung (VDA-Tier-1 mit Werk Suzhou).\n\n"
    "Phase 3 (2026/2027): USA-Markteintritt; Vertriebspartnerschaft mit nordamerikanischem "
    "Sondermaschinenbauer (Letter of Intent geplant Q3/2025); Schwerpunkt Suedost-USA (Automotive-Hub "
    "Tennessee / Alabama).\n\nInvestitionsbedarf: ca. 1,8 Mio. EUR ueber 3 Jahre (Personalaufbau, "
    "Lokale-Niederlassungen, Marketing, Zertifizierungen). Finanzierung aus Cashflow; KfW-Foerderung "
    "im Programm »ERP-Auslandsfinanzierung« vorgesehen.",
    "Genehmigt Beiratssitzung 22. Februar 2024")

short_doc(B11, "STRAT_Digitalisierungsbericht_Q2_2024", "Digitalisierungsbericht Q2/2024",
    "Bericht zur Umsetzung der Digitalisierungsoffensive 2024-2026 (Gesellschafterbeschluss 2024/03). "
    "Berichtsperiode: 1. April bis 30. Juni 2024.\n\nFortschritt nach Massnahmenpaket:\n\n"
    "(1) MES-System: Ausschreibung Q2 abgeschlossen; Anbieter ISTOS GmbH ausgewaehlt (Vertragsvolumen "
    "850 TEUR); Implementierung Halle B beginnt Q3/2024.\n\n"
    "(2) SAP S/4HANA Erweiterung PP-PI / QM: Anbieter NTT Data ausgewaehlt; Projektstart 8. Juli 2024.\n\n"
    "(3) Predictive Maintenance: UNITY-Vertrag laeuft; Pilotbetrieb bei ThyssenKrupp Steel Europe AG "
    "Halle A41 erfolgreich angelaufen; Produktivsetzung 30. Juni 2024 erfolgt.\n\n"
    "(4) Salesforce Experience Cloud (Kunden-Portal): Konzept fertig, Implementation Q3-Q4/2024 geplant.\n\n"
    "(5) Cybersecurity-Programm: TISAX-Vorpruefung beauftragt; ISMS-Erweiterung in Arbeit.\n\n"
    "(6) Schulungs- und Change-Programm »MMB Digital 2026«: Wave 1 (Awareness + Tools-Onboarding) "
    "abgeschlossen; 87 % der Belegschaft geschult.\n\n"
    "(7) Stabsstelle Digitalisierung: Frau Dr. Bettina Wirth zum 1. Mai 2024 als Head of Digital "
    "eingestellt; zwei weitere FTE in Rekrutierung.\n\n"
    "Budgetauslastung Q2: 1,12 Mio. EUR (24 % vom Gesamtbudget 4,5 Mio. EUR; im Rahmen der Q2-Erwartung).",
    "Berichtszeitraum Q2/2024, Stand 8. Juli 2024")

short_doc(B11, "STRAT_Wettbewerbsanalyse_2024", "Wettbewerbsanalyse 2024 – Pressen- und Sondermaschinenbau",
    "Wettbewerbsanalyse zum Stichtag 31. Januar 2024, erstellt durch das Strategieteam in Zusammenarbeit "
    "mit dem Marktforschungsanbieter VDMA (Verband Deutscher Maschinen- und Anlagenbau).\n\n"
    "Marktumfeld DACH: Maschinenbau-Markt 2023 leichte Erholung gegenueber 2022; Sondermaschinen-"
    "Segment +4,8 %, in das MMB taetig ist. Auftragsbestand-Indikatoren sind positiv (VDMA-Q4-Umfrage).\n\n"
    "Wesentliche Wettbewerber im Segment (DACH):\n"
    "- Schuler AG (Goeppingen) – Marktfuehrer Pressen, Umsatz > 1 Mrd. EUR.\n"
    "- AIDA Engineering (Tokyo / Frankreich) – starker Wettbewerber bei Großserienpressen.\n"
    "- Trumpf SE (Ditzingen) – fuehrend bei Faserlaser-Systemen (zugleich Lieferant von MMB).\n"
    "- Schiess GmbH (Aschersleben) – mittelstaendischer Wettbewerber, Schwerpunkt Sondermaschinen.\n"
    "- Wuerth Industrie Service (Industriebevorratung, indirekter Wettbewerb).\n\n"
    "Positionierung MMB: Nische »customized mid-sized presses + integrated services«; "
    "Wettbewerbsvorteil durch enge Kundenbindung Top-5-Kunden, Sondermaschinen-Kompetenz, "
    "Predictive-Maintenance-Vorsprung, Familienunternehmen-Stabilitaet. Wettbewerbsnachteil: "
    "Skaleneffekte gegenueber Schuler / AIDA, internationale Praesenz schwach.\n\n"
    "Empfehlung: Investitions-Roadmap »Pressen 4.0« forcieren; Internationalisierung gemaess Roadmap "
    "vorantreiben; Geschaeftsfelderweiterung Laser und Robotik (Beschluss 2021/04) konsequent ausschoepfen.",
    "Stand 31. Januar 2024")

short_doc(B11, "STRAT_Pressemitteilung_Auftrag_ThyssenKrupp_2023", "Pressemitteilung – Auftrag ThyssenKrupp Steel Europe 2023",
    "Halbreiter Maschinenbau GmbH erhaelt 3,8-Mio.-EUR-Grossauftrag von ThyssenKrupp Steel Europe AG\n\n"
    "Koeln, 12. Juni 2023 – Die Halbreiter Maschinenbau GmbH, ein traditionsreicher Spezialist fuer "
    "Sondermaschinen und Anlagen, hat von der ThyssenKrupp Steel Europe AG einen Großauftrag ueber die "
    "Lieferung einer Pressenlinie PL-500 (800 t) erhalten. Der Auftragswert betraegt rund 3,8 Mio. EUR; "
    "die Lieferung erfolgt im Werk Duisburg-Hamborn, Halle A41. Die Inbetriebnahme ist fuer den "
    "30. April 2024 vorgesehen.\n\n"
    "Klaus Mueller, Geschaeftsfuehrer der Halbreiter Maschinenbau GmbH, zeigt sich erfreut: "
    "»Die langjaehrige Partnerschaft mit ThyssenKrupp Steel Europe gehoert zu den Eckpfeilern unseres Geschaefts. "
    "Mit der Pressenlinie PL-500 setzen wir auf hoechste Praezision, vollintegrierte Sensorik und unsere "
    "neue Predictive-Maintenance-Plattform – Schluesselelemente fuer das digitale Werk der Zukunft.«\n\n"
    "Die Pressenlinie PL-500 verfuegt ueber ein servo-hydraulisches Antriebssystem, Pressenkraefte "
    "bis 1.000 t und integriert ein hauseigen entwickeltes Schnellwechselsystem (Gebrauchsmuster DE 20 "
    "2021 105 482), das die Werkzeugwechselzeit auf unter 90 Sekunden senkt. Diese Innovation steigert "
    "die Anlagenproduktivitaet messbar.\n\n"
    "Ueber Halbreiter Maschinenbau GmbH: Familiengefuehrtes Unternehmen mit Sitz in Koeln, gegruendet 1985. "
    "247 Mitarbeitende, Jahresumsatz 48,6 Mio. EUR (2023). Schwerpunkte: hydraulische Stanzpressen, "
    "Foerderbandanlagen, Laserschneidanlagen, Robotik-Zellen.\n\n"
    "Pressekontakt: Andrea Hoffmann, Leiterin Personal & Verwaltung; presse@halbreiter-maschinenbau.de.",
    "Veroeffentlicht 12. Juni 2023")

short_doc(B11, "STRAT_SWOT-Analyse_2024", "SWOT-Analyse 2024",
    "SWOT-Analyse der Halbreiter Maschinenbau GmbH zur strategischen Standortbestimmung 2024, erstellt vom "
    "Strategieteam und ueberprueft vom Beirat (Sitzung 22.2.2024).\n\n"
    "STAERKEN (Strengths):\n"
    "- Lange Tradition (seit 1985), hohe Reputation bei Bestandskunden Top-5.\n"
    "- Patentierte Innovationen (Schnellwechselsystem, Adaptive Process Control RWTH).\n"
    "- Hohe Eigenkapitalquote (54 %), solide Finanzierung, niedriger Verschuldungsgrad.\n"
    "- Loyale Mitarbeitende (durchschn. Betriebszugehoerigkeit 11,4 Jahre).\n"
    "- Predictive Maintenance Vorsprung im Mittelstand-Segment.\n\n"
    "SCHWAECHEN (Weaknesses):\n"
    "- Kundenkonzentration: Top-5 Kunden = 62 % vom Umsatz.\n"
    "- Schwache Internationalisierung (Auslandsanteil 14 %).\n"
    "- Begrenzte Skaleneffekte gegenueber Schuler AG, AIDA.\n"
    "- Demografisches Risiko: 24 % der Belegschaft > 55 Jahre.\n"
    "- Cyber-Reife im Aufbau (noch nicht TISAX-zertifiziert).\n\n"
    "CHANCEN (Opportunities):\n"
    "- Industrie 4.0 / Smart Manufacturing als Wachstumstreiber.\n"
    "- Reshoring-Trend in der EU (Onshoring von Produktion).\n"
    "- Markteintritt Mexiko (Dürr AG Pilot), USA (mittelfristig).\n"
    "- Predictive Maintenance als Service-Markt (recurring revenue).\n"
    "- ESG-Anforderungen schaffen Nachfrage nach modernen, energieeffizienten Anlagen.\n\n"
    "RISIKEN (Threats):\n"
    "- Rezession in Schluesselbranchen (Automotive).\n"
    "- Materialverfuegbarkeit Elektronik (Halbleiter).\n"
    "- Cyber-Bedrohungen (steigend laut BSI-Lagebericht).\n"
    "- Wettbewerb durch chinesische Hersteller im mittleren Preissegment.\n"
    "- Regulatorische Verschaerfung (CSRD, CO2-Bepreisung).",
    "Stand 31. Januar 2024; freigegeben Beiratssitzung 22.2.2024")


print("OK regen_mueller_06_11.py – ~76 docs total written (06+07+08+09+10+11)")
