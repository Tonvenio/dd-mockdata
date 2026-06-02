"""Brennhagen 18_Immobilien — 37 thin docs.

Real-estate portfolio of the Brennhagen Elektronik AG group:
- REA HQ Stuttgart-Vaihingen (Eigentum REA), Verkehrswert 18,4 Mio. EUR
- REG Werk Heilbronn (Eigentum REG + Bauleihe Stadt), Verkehrswert 31,2 Mio. EUR
- RSG Werk Muenchen-Schwabing (Miete), RPL Katowice (Miete, KSSE),
  RCZ Brno CTP Park (Miete), RHU Gyoer Ipari Park (Miete),
  RCN Shanghai-Minhang Caohejing (Miete).
Head of Real Estate (extern): Dr. Wolfgang Hertz (Drees & Sommer).
REG Heilbronn Real Estate Officer: Sabine Hartlieb (Werkleiter Andreas Maier).
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
from enhance_lib import ROEHRIG_AG as R, write_doc, signatures

BASE = f"{_ROOT}/roehrig_large/18_Immobilien"

REA_H = {"name": R["name"], "addr": R["addr"], "hrb": R["hrb"]}
REG_H = {
    "name": "Brennhagen Elektronik GmbH (REG)",
    "addr": "Wertheimer Strasse 12, 74076 Heilbronn",
    "hrb":  "HRB 221456, Amtsgericht Heilbronn",
}
RSG_H = {
    "name": "Brennhagen Software GmbH (RSG)",
    "addr": "Lyonel-Feininger-Strasse 28, 80807 Muenchen",
    "hrb":  "HRB 245612, Amtsgericht Muenchen",
}
RPL_H = {
    "name": "Brennhagen Polska Sp. z o.o. (RPL)",
    "addr": "KSSE Strefa Aktywnosci Gospodarczej, ul. Wegierska 18, 40-203 Katowice (PL)",
    "hrb":  "KRS 0000412376, Sad Rejonowy Katowice-Wschod",
}
RCZ_H = {
    "name": "Brennhagen CZ s.r.o. (RCZ)",
    "addr": "CTP Park Brno-South, Hala B14, Heshova 17, 627 00 Brno (CZ)",
    "hrb":  "IC 27812234, MS Brno C/47812",
}
RHU_H = {
    "name": "Brennhagen Hungary Kft. (RHU)",
    "addr": "Ipari Park, Gyoeri ut 42, H-9027 Gyoer (HU)",
    "hrb":  "Cg.08-09-018456, Cegbirosag Gyoer",
}
RCN_H = {
    "name": "Brennhagen (Shanghai) Co. Ltd. (RCN)",
    "addr": "Caohejing Hi-Tech Park, Building 7, 888 Hongqiao Road, 200336 Shanghai-Minhang (CN)",
    "hrb":  "Unified Social Credit Code 91310115MA1FL42Q38",
}

# Property masterdata
PROPS = {
    "HQ_Stuttgart": {
        "header": REA_H,
        "werk": "REA Hauptsitz Stuttgart-Vaihingen",
        "addr": "Vaihinger Strasse 120, 70567 Stuttgart-Vaihingen",
        "tenure": "Eigentum REA",
        "flaeche": "14.800 m² bebaut auf 28.000 m² Grundstueck",
        "nutzung": "Konzernverwaltung, Vorstand, ADAS-Testzentrum (V4D-Radarfusion), Showroom, Kantine",
        "miete_jahr": None,
        "grundbuch": "Amtsgericht Stuttgart-Vaihingen, Grundbuch von Vaihingen, Blatt 28741, Flur 17, Flurstuecke 412/3 und 412/4",
        "vw": "18,4 Mio. EUR",
        "vw_gutachter": "Dr. Helmut Schneider, oeffentlich bestellt und vereidigt IHK Stuttgart, Gutachten vom 14. November 2023",
        "miete_per_qm": None,
        "vermieter": None,
        "energie": "Erdgas-BHKW (Stadtwerke Stuttgart) mit PV-Aufdach 720 kWp (seit 2023), End-Energiebedarf 78 kWh/(m²·a), Effizienzklasse B (GEG 2024)",
        "brandschutz": "Brandschutzkonzept nach LBO BW, sachverstaendige Pruefung Dr.-Ing. Manfred Stoll (Heilbronn), Klasse 4 (Verwaltung). Wartung BMA durch Bosch Sicherheitssysteme GmbH.",
        "verant": "Sabine Hartlieb (Real Estate Officer REA) / Dr. Wolfgang Hertz (Head of Real Estate, Drees & Sommer)",
        "stadt": "Stuttgart",
        "ansprechpartner_stadt": "Stadt Stuttgart, Baurechtsamt, Eberhardstrasse 33, Frau Dipl.-Ing. Brigitte Walz",
    },
    "Werk_Heilbronn": {
        "header": REG_H,
        "werk": "REG Werk Heilbronn",
        "addr": "Wertheimer Strasse 12, 74076 Heilbronn (Industriegebiet Heilbronn-Boeckingen)",
        "tenure": "Eigentum REG (mit Bauleihe der Stadt Heilbronn)",
        "flaeche": "42.000 m² bebaut auf 65.000 m² Grundstueck",
        "nutzung": "Hauptwerk Produktion ICP-3, BMS-12, ECU-900, LightCtrl-7 (Linie 1-4), 820 Mitarbeiter",
        "miete_jahr": None,
        "grundbuch": "Amtsgericht Heilbronn, Grundbuch von Heilbronn-Boeckingen, Blatt 4712, Flur 32, Flurstuecke 287/1, 287/2, 287/12",
        "vw": "31,2 Mio. EUR",
        "vw_gutachter": "Dr. Andreas Koehler, oeffentlich bestellt und vereidigt IHK Heilbronn-Franken, Gutachten vom 28. September 2023",
        "miete_per_qm": None,
        "vermieter": None,
        "energie": "Fernwaerme Stadtwerke Heilbronn, PV-Aufdach 1.480 kWp (Inbetriebnahme Q2/2024), End-Energiebedarf 94 kWh/(m²·a), Effizienzklasse B (GEG 2024)",
        "brandschutz": "Brandschutzkonzept Sonderbau Industrie (LBO BW i.V.m. MIndBauRL 2023), Wartung Honeywell. CO2-Loeschanlage SMT-Linien.",
        "verant": "Andreas Maier (Werkleiter REG) / Sabine Hartlieb (Real Estate Officer)",
        "stadt": "Heilbronn",
        "ansprechpartner_stadt": "Stadt Heilbronn, Baurechts- und Denkmalschutzamt, Marktplatz 7, Herr Bauoberrat Dipl.-Ing. Hermann Klotz",
    },
    "Office_München": {
        "header": RSG_H,
        "werk": "RSG Werk Muenchen-Schwabing",
        "addr": "Lyonel-Feininger-Strasse 28, 80807 Muenchen-Schwabing",
        "tenure": "Miete (Hauptvermieter: Allianz Real Estate GmbH)",
        "flaeche": "4.620 m² Buerogebaeude (3. - 6. OG)",
        "nutzung": "Software-Entwicklung Embedded / ADAS, ASPICE-Labor, 340 Mitarbeiter",
        "miete_jahr": 1_080_000,
        "grundbuch": "n/a (Mietverhaeltnis)",
        "vw": "Anschaffungs-/Herstellungskosten n/a; Buchwert Mietsonderausstattung 1,2 Mio. EUR",
        "vw_gutachter": "Mietwertgutachten Jones Lang LaSalle SE (JLL), 4. Quartal 2023: 19,50 EUR/m²/Monat marktueblich",
        "miete_per_qm": "19,50 EUR/m²/Monat Kaltmiete + 4,80 EUR/m²/Monat Nebenkosten (Vorauszahlung)",
        "vermieter": "Allianz Real Estate GmbH, Seidlstrasse 24-24a, 80335 Muenchen",
        "energie": "Fernwaerme (SWM); LED-Komplettumruestung 2022; End-Energiebedarf 64 kWh/(m²·a), Effizienzklasse A (GEG 2024)",
        "brandschutz": "Brandschutzkonzept Buerogebaeude (LBO Bayern), Wartung BMA und Sprinkleranlage durch Minimax Mobile Services GmbH.",
        "verant": "Dr. Klaus Kessler (Werkleiter RSG)",
        "stadt": "Muenchen",
        "ansprechpartner_stadt": "Landeshauptstadt Muenchen, Lokalbaukommission, Blumenstrasse 28b",
    },
    "Werk_Katowice": {
        "header": RPL_H,
        "werk": "RPL Werk Katowice",
        "addr": "KSSE Strefa Aktywnosci Gospodarczej, ul. Wegierska 18, 40-203 Katowice (Polen)",
        "tenure": "Miete (Katowicka Specjalna Strefa Ekonomiczna S.A. – KSSE-Sonderwirtschaftszone)",
        "flaeche": "18.500 m² Produktions-/Lagerhalle + 1.200 m² Buero",
        "nutzung": "EMS / SMD-Bestueckung, Loetung, Konfektionierung; 960 Mitarbeiter",
        "miete_jahr": 1_440_000,
        "grundbuch": "Ksiega Wieczysta KA1K/00187423/2, Sad Rejonowy Katowice-Wschod",
        "vw": "Buchwert Mietsonderausstattung 4,8 Mio. EUR (SMD-Linien + Reinraum)",
        "vw_gutachter": "Mietwertgutachten Cushman & Wakefield Polska Sp. z o.o., Q1/2023: 6,50 EUR/m²/Monat marktueblich (KSSE)",
        "miete_per_qm": "6,30 EUR/m²/Monat Kaltmiete + 1,90 EUR/m²/Monat Nebenkosten",
        "vermieter": "Katowicka Specjalna Strefa Ekonomiczna S.A., ul. Wojewodzka 42, 40-026 Katowice",
        "energie": "Stromversorgung Tauron Polska Energia S.A.; PV-Aufdach 820 kWp in Planung 2024 (Vertrag mit ZAE Solar Sp. z o.o.). End-Energiebedarf 108 kWh/(m²·a).",
        "brandschutz": "Brandschutzkonzept gemaess polnischem Bauordnungsrecht (Prawo budowlane); Wartung Tyco/Johnson Controls Polska.",
        "verant": "Marek Wojciechowski (Werkleiter RPL)",
        "stadt": "Katowice",
        "ansprechpartner_stadt": "Urzad Miasta Katowice / KSSE S.A.",
    },
    "Werk_Brno": {
        "header": RCZ_H,
        "werk": "RCZ Werk Brno",
        "addr": "CTP Park Brno-South, Hala B14, Heshova 17, 627 00 Brno (Tschechien)",
        "tenure": "Miete (CTP Invest, spol. s r.o.)",
        "flaeche": "12.800 m² Produktion + 1.400 m² Buero",
        "nutzung": "Steckverbinder-Fertigung, Spritzguss, Stanzen, Konfektion; 680 Mitarbeiter",
        "miete_jahr": 1_120_000,
        "grundbuch": "Katastr nemovitosti, KU Brno-jih 612065, parcela 1247/8, LV 2841",
        "vw": "Buchwert Mietsonderausstattung 3,4 Mio. EUR",
        "vw_gutachter": "Mietwertgutachten Knight Frank s.r.o., Q4/2023: 5,80 EUR/m²/Monat marktueblich (CTP-Standorte CZ)",
        "miete_per_qm": "5,60 EUR/m²/Monat Kaltmiete + 1,40 EUR/m²/Monat NK",
        "vermieter": "CTP Invest, spol. s r.o., Central Trade Park D1, 396 01 Humpolec (CZ)",
        "energie": "Strom E.ON Energie a.s.; LED 2021; End-Energiebedarf 97 kWh/(m²·a).",
        "brandschutz": "Pozarne projektove reseni dle CSN 73 08xx; Wartung Securitas CZ.",
        "verant": "Petr Novak (Werkleiter RCZ)",
        "stadt": "Brno",
        "ansprechpartner_stadt": "Magistrat mesta Brna, Stavebni urad",
    },
    "Werk_Gyoer": {
        "header": RHU_H,
        "werk": "RHU Werk Gyoer",
        "addr": "Ipari Park, Gyoeri ut 42, H-9027 Gyoer (Ungarn)",
        "tenure": "Miete (Gyoer Industrial Park Kft.)",
        "flaeche": "9.400 m² Produktion + 980 m² Buero",
        "nutzung": "Sensorik (Radar, LiDAR, Beschleunigung); 540 Mitarbeiter",
        "miete_jahr": 760_000,
        "grundbuch": "Foeldhivatal Gyoer, helyrajzi szam 14782/3",
        "vw": "Buchwert Mietsonderausstattung 2,2 Mio. EUR",
        "vw_gutachter": "Mietwertgutachten Colliers Hungary Kft., Q3/2023: 5,90 EUR/m²/Monat marktueblich",
        "miete_per_qm": "5,70 EUR/m²/Monat Kaltmiete + 1,30 EUR/m²/Monat NK",
        "vermieter": "Gyoer Industrial Park Kft., Gyoeri ut 1, H-9027 Gyoer",
        "energie": "Strom MVM Next Energiakereskedelmi Zrt.; End-Energiebedarf 102 kWh/(m²·a).",
        "brandschutz": "Tuezvedelmi terv (OTSZ 2024); Wartung Defendline Kft.",
        "verant": "Laszlo Kovacs (Werkleiter RHU)",
        "stadt": "Gyoer",
        "ansprechpartner_stadt": "Gyoer Megyei Jogu Varos Onkormanyzata",
    },
    "Office_Shanghai": {
        "header": RCN_H,
        "werk": "RCN Bueros Shanghai",
        "addr": "Caohejing Hi-Tech Park, Building 7, 888 Hongqiao Road, 200336 Shanghai-Minhang (China)",
        "tenure": "Miete (Shanghai Caohejing Hi-Tech Park Development Co., Ltd.)",
        "flaeche": "6.200 m² Buero/Showroom/Aftermarket-Lager",
        "nutzung": "Asien-Vertrieb, Aftermarket, OEM-Liaison (BMW Brilliance, CATL); 320 Mitarbeiter",
        "miete_jahr": 980_000,
        "grundbuch": "n/a (Mietverhaeltnis nach chinesischem Recht, Land-Use-Right Caohejing)",
        "vw": "Buchwert Mietsonderausstattung 1,1 Mio. EUR",
        "vw_gutachter": "Mietwertgutachten Savills (Shanghai) Property Services Co. Ltd., 2023: 11,50 EUR/m²/Monat marktueblich (Minhang Class-A)",
        "miete_per_qm": "11,20 EUR/m²/Monat Kaltmiete + 2,80 EUR/m²/Monat Service Charge",
        "vermieter": "Shanghai Caohejing Hi-Tech Park Development Co., Ltd.",
        "energie": "State Grid Shanghai; Klimatisierung Mitsubishi VRF; End-Energiebedarf 118 kWh/(m²·a).",
        "brandschutz": "Brandschutzkonzept nach GB 50016-2014; jaehrliche Pruefung Shanghai Fire Services.",
        "verant": "Zhang Hao (Country Manager RCN)",
        "stadt": "Shanghai",
        "ansprechpartner_stadt": "Shanghai Minhang District Planning & Land Resources Bureau",
    },
}


# ============================================================================
# Helper builders
# ============================================================================

def mietvertrag(fname, key, dauer_von, dauer_bis, miete_eur_jahr, indexierung,
                kuendigung_monate=12, mietzweck_extra=""):
    p = PROPS[key]
    miete_mon = miete_eur_jahr / 12
    nk = miete_mon * 0.32  # Nebenkosten ~32%
    write_doc(f"{BASE}/{fname}", REA_H,
        f"Gewerblicher Mietvertrag – {p['werk']}",
        subtitle=f"Mietobjekt: {p['addr']}; Laufzeit {dauer_von} bis {dauer_bis}",
        sections=[
            ("Vertragsparteien",
             f"Vermieter: {p['vermieter'] or 'n/a (Eigenobjekt)'}, vertreten durch dessen Geschaeftsfuehrung. "
             f"Mieter: {p['header']['name']}, {p['header']['addr']}, {p['header']['hrb']}, vertreten durch "
             f"den Werkleiter / die Geschaeftsfuehrung. Konzern-Garant fuer saemtliche Verpflichtungen des "
             f"Mieters ist die Brennhagen Elektronik AG, Vaihinger Strasse 120, 70567 Stuttgart (HRB 726451, "
             f"Amtsgericht Stuttgart), vertreten durch CFO Laura Bauer. Konzerngarantieerklaerung ist als "
             f"Anlage 3 zu diesem Vertrag genommen."),
            ("Vertragsklauseln",
             ("clauses", [
                ("§ 1 Mietgegenstand", [
                    f"Vermietet wird das Objekt »{p['werk']}« mit der Adresse {p['addr']}. "
                    f"Mietflaeche: {p['flaeche']}. Eine Flaechenaufstellung sowie ein Lageplan sind als "
                    f"Anlage 1 zum Vertrag genommen.",
                    f"Mitvermietet sind: 1 PKW-Tiefgarage / Aussenstellplaetze in marktueblicher Anzahl, "
                    f"Allgemeinflaechen (Treppenhaeuser, Aufzuege), Nebenraeume (Kantine, Sanitaer, "
                    f"Technikraeume) entsprechend Anlage 1, Anschluesse fuer Strom, Wasser, Abwasser, "
                    f"Gas, Fernkommunikation (Glasfaser 10 Gbit/s).",
                    f"Mietzweck: {p['nutzung']}. {mietzweck_extra} Eine Nutzungsaenderung bedarf der "
                    f"vorherigen schriftlichen Zustimmung des Vermieters; die Zustimmung darf nicht "
                    f"unbillig verweigert werden, soweit die Nutzung im Rahmen der baurechtlichen "
                    f"Genehmigung bleibt."]),
                ("§ 2 Mietdauer und Kuendigung", [
                    f"Das Mietverhaeltnis beginnt am {dauer_von} und endet am {dauer_bis}. Beiden "
                    f"Parteien wird eine Option auf Verlaengerung um zweimal je 5 Jahre eingeraeumt, "
                    f"die jeweils 12 Monate vor Vertragsende durch eingeschriebenen Brief auszuueben "
                    f"ist.",
                    f"Eine ordentliche Kuendigung waehrend der Festlaufzeit ist ausgeschlossen. Das "
                    f"Recht zur ausserordentlichen Kuendigung aus wichtigem Grund (§ 543 BGB / "
                    f"jeweiliges lokales Aequivalent) bleibt unberuehrt. Sonderkuendigungsrecht des "
                    f"Mieters bei wesentlicher Veraenderung der Konzern-Standortstrategie mit "
                    f"Vorlauffrist von {kuendigung_monate} Monaten zum Quartalsende, gegen Zahlung "
                    f"einer pauschalierten Entschaedigung in Hoehe von 6 Monatsmieten."]),
                ("§ 3 Miete und Indexierung", [
                    f"Die Jahresnettomiete betraegt {miete_eur_jahr:,.0f} EUR, monatlich "
                    f"{miete_mon:,.0f} EUR. {p['miete_per_qm'] or 'Festmietzins ohne qm-Bezug.'}".replace(",", "."),
                    f"Die Miete ist indexiert nach {indexierung}. Anpassung erstmals 12 Monate nach "
                    f"Vertragsbeginn, sodann jaehrlich zum 1. Januar; Anpassungssprung > 3 % erfolgt zu "
                    f"100 %, dazwischen zu 80 %.",
                    f"Nebenkosten (Heizung, Warm-/Kaltwasser, Klimatisierung, Hausreinigung, Aufzug, "
                    f"Versicherung, Grundsteuer-Anteil, Sicherheit) werden als Vorauszahlung in Hoehe "
                    f"von {nk:,.0f} EUR/Monat erhoben und jaehrlich abgerechnet (siehe Anlage 2 zur "
                    f"Heizkostenverordnung bzw. lokales Aequivalent).".replace(",", ".")]),
                ("§ 4 Kaution und Sicherheiten", [
                    f"Der Mieter leistet eine Mietkaution in Hoehe von 3 Monatsbruttomieten ("
                    f"{3*(miete_mon+nk):,.0f} EUR), zu erbringen durch Bankbuergschaft der Deutsche "
                    f"Bank AG. Zusaetzlich besteht die o.g. Konzerngarantieerklaerung der Brennhagen "
                    f"Elektronik AG.".replace(",", "."),
                    f"Eine Pflichtversicherung (Gebaeudeversicherung Vermieter, "
                    f"Betriebshaftpflicht-/Sach- und Inhaltsversicherung Mieter ueber Allianz Global "
                    f"Corporate & Specialty SE) wird durch beide Parteien gehalten."]),
                ("§ 5 Instandhaltung, Schoenheitsreparaturen und Umbauten", [
                    f"Schoenheitsreparaturen innerhalb der Mietraeume traegt der Mieter; Dach, Fach, "
                    f"tragende Konstruktion, Versorgungsleitungen ab Hausanschluss und Heizungsanlage "
                    f"obliegen dem Vermieter.",
                    f"Bauliche Umbauten (Innenausbau, Stellung weiterer Maschinen >2 t, "
                    f"Reinraum-Aufbau) beduerfen der vorherigen schriftlichen Zustimmung des "
                    f"Vermieters; Genehmigungsfaehigkeit nach Baurecht ist vom Mieter sicherzustellen.",
                    f"Mieter ist berechtigt, im Rahmen seines PV-Programms (Konzern-PV-Strategie 2024) "
                    f"auf dem Dach Photovoltaik-Anlagen zu errichten; Auflagen siehe Anlage 4 "
                    f"(Mustervertrag Dach-Pacht/PV)."]),
                ("§ 6 Schluss- und Formvorschriften", [
                    f"Aenderungen und Ergaenzungen dieses Vertrages beduerfen der Schriftform. Eine "
                    f"Aufhebung des Schriftformerfordernisses bedarf ebenfalls der Schriftform.",
                    f"Gerichtsstand ist {p['stadt']}. Es gilt deutsches / lokales Recht (je nach Sitz "
                    f"des Mietobjekts). Sollten einzelne Bestimmungen unwirksam sein, bleibt die "
                    f"Wirksamkeit der uebrigen Bestimmungen unberuehrt (salvatorische Klausel)."])])),
            ("Anlagenverzeichnis",
             ("list", [
                "Anlage 1 – Lageplan und Flaechenaufstellung",
                "Anlage 2 – Nebenkostenvereinbarung und Heizkostenverteilung",
                "Anlage 3 – Konzerngarantieerklaerung Brennhagen Elektronik AG",
                "Anlage 4 – Mustervertrag Dachflaechen-Pacht (Photovoltaik)",
                "Anlage 5 – Energieausweis gemaess GEG 2024",
                "Anlage 6 – Brandschutzkonzept (Auszug)",
                "Anlage 7 – Uebergabeprotokoll",
             ])),
            ("Unterschriften",
             signatures("Dr. Wolfgang Hertz", "Head of Real Estate (extern, Drees & Sommer)",
                        "fuer die Mieterin (REA / Konzern)",
                        "i.V. Geschaeftsfuehrung Vermieter", "Vermieter-Vertreter",
                        p['vermieter'] or "Vermieter", place=p['stadt'], date_str_=dauer_von)),
        ])


def nachtrag(fname, key, jahr, gegenstand, anpassung_pct, neuer_mietzins_eur_jahr=None):
    p = PROPS[key]
    write_doc(f"{BASE}/{fname}", p["header"],
        f"Nachtragsvereinbarung Nr. 1 zum Mietvertrag – {p['werk']}",
        subtitle=f"Datum: 15. November {jahr}; Mietobjekt {p['addr']}",
        sections=[
            ("Praeambel",
             f"Zwischen dem Vermieter ({p['vermieter'] or 'Vermieter siehe Hauptvertrag'}) und dem "
             f"Mieter ({p['header']['name']}, {p['header']['addr']}) wurde am 1. Januar 2020 ein "
             f"gewerblicher Mietvertrag ueber das Objekt »{p['werk']}« geschlossen ("
             f"»Hauptvertrag«). Mit diesem Nachtrag Nr. 1 werden einzelne Regelungen des "
             f"Hauptvertrages angepasst. Anlass: {gegenstand}. Der Hauptvertrag bleibt im Uebrigen "
             f"unveraendert in Kraft."),
            ("Gegenstand des Nachtrags",
             ("clauses", [
                ("§ 1 Anpassung des Mietzinses", [
                    f"Mit Wirkung zum 1. Januar {jahr+1} wird die Jahresnettomiete um {anpassung_pct} % "
                    f"angepasst. Anlass ist die ueblicherweise im Hauptvertrag § 3 vereinbarte "
                    f"Indexanpassung gemaess Verbraucherpreisindex (VPI) des Statistischen "
                    f"Bundesamtes / lokales Aequivalent.",
                    f"Neue Jahresnettomiete: " + (f"{neuer_mietzins_eur_jahr:,.0f} EUR".replace(",", ".") if neuer_mietzins_eur_jahr else "siehe Anlage 1 zum Nachtrag"),
                    f"Die Nebenkostenvorauszahlung wird im gleichen Schritt um {min(anpassung_pct+1, 8)} % "
                    f"angepasst aufgrund gestiegener Energiekosten (Erdgas, Fernwaerme, Strom) sowie "
                    f"hoeherer Aufwendungen fuer Sicherheit und Reinigung."]),
                ("§ 2 Sonstige Anpassungen", [
                    f"Anlass des Nachtrags im Detail: {gegenstand}",
                    f"Eine Klarstellung der Regelung zur Photovoltaik-Aufdach-Nutzung wird vereinbart: "
                    f"Der Mieter ist berechtigt, eigene PV-Anlagen unter Beachtung der statischen "
                    f"Lastreserven der Dachkonstruktion zu errichten; der Vermieter erhaelt eine "
                    f"jaehrliche Pacht in Hoehe von 0,50 EUR/kWp.",
                    f"Klarstellung Service-Level: Reaktionszeit Stoerung Heizung/Klima < 4 Stunden "
                    f"werktags (Mo-Fr 07:00-18:00); aussertarifliche Stoerungen < 24 Stunden."]),
                ("§ 3 Schlussbestimmungen", [
                    f"Soweit nichts Abweichendes vereinbart wird, bleibt der Hauptvertrag vom 1. Januar "
                    f"2020 in vollem Umfang in Kraft. Die salvatorische Klausel und die "
                    f"Schriftformklausel des Hauptvertrages gelten entsprechend.",
                    f"Dieser Nachtrag wurde in zwei Exemplaren erstellt; jede Partei erhaelt ein "
                    f"Original. Die Anlage 1 (Neue Mietpreiskalkulation) ist Bestandteil dieses "
                    f"Nachtrags."])])),
            ("Unterschriften",
             signatures("Sabine Hartlieb", "Real Estate Officer", "Konzern Brennhagen",
                        "Vermieter-Vertretung", "Property Manager", p['vermieter'] or "Vermieter",
                        place=p['stadt'], date_str_=f"15. November {jahr}")),
        ])


def nebenkostenabrechnung(fname, key, jahr):
    p = PROPS[key]
    # Calculate plausible NK breakdown
    miete_jahr = p["miete_jahr"] or 1_200_000  # for owned, simulate operating cost
    nk_total = miete_jahr * 0.34
    posten = [
        ("Heizung / Fernwaerme / Gas", nk_total * 0.22),
        ("Strom Allgemeinstrom", nk_total * 0.08),
        ("Wasser / Abwasser", nk_total * 0.06),
        ("Klimatisierung / Lueftung", nk_total * 0.10),
        ("Hausreinigung", nk_total * 0.09),
        ("Aufzugswartung", nk_total * 0.04),
        ("Brandmeldeanlage / Sicherheit", nk_total * 0.07),
        ("Aussenanlagen / Winterdienst / Gartenbau", nk_total * 0.05),
        ("Versicherung Gebaeude", nk_total * 0.06),
        ("Grundsteuer-Anteil", nk_total * 0.08),
        ("Hausmeister / Property Management", nk_total * 0.10),
        ("Sonstige Betriebskosten", nk_total * 0.05),
    ]
    tbl = [["Kostenposition", "Verteilerschluessel", "Gesamt (EUR)", "Anteil Mieter (EUR)"]]
    for name, val in posten:
        tbl.append([name, "Flaechenanteil", f"{val:,.0f}".replace(",", "."), f"{val*0.98:,.0f}".replace(",", ".")])
    summe = sum(v for _, v in posten)
    tbl.append(["SUMME", "", f"{summe:,.0f}".replace(",", "."), f"{summe*0.98:,.0f}".replace(",", ".")])
    vorausz = miete_jahr * 0.32
    saldo = summe*0.98 - vorausz
    write_doc(f"{BASE}/{fname}", p["header"],
        f"Nebenkostenabrechnung {jahr} – {p['werk']}",
        subtitle=f"Abrechnungszeitraum: 01.01.{jahr} – 31.12.{jahr}",
        sections=[
            ("Mietobjekt und Vertragsbezug",
             f"Mietobjekt: {p['werk']}, {p['addr']}. Mieter: {p['header']['name']}. "
             f"Vermieter: {p['vermieter'] or 'Eigentuemer (Eigennutzung, interne Verrechnung)'}. "
             f"Grundlage: Gewerblicher Mietvertrag vom 1. Januar 2020, § 3 (3) (Nebenkostenabrechnung) "
             f"i.V.m. Anlage 2 (Nebenkostenkatalog). Verteilerschluessel grundsaetzlich nach "
             f"angemieteter Flaeche ({p['flaeche']}); Heizung anteilig 50 % Flaeche / 50 % Verbrauch."),
            ("Aufstellung der Betriebs- und Nebenkosten", tbl),
            ("Saldenuebersicht",
             f"Geleistete Vorauszahlungen Mieter im Abrechnungsjahr {jahr}: "
             f"{vorausz:,.0f} EUR (12 Monatsraten zu je {vorausz/12:,.0f} EUR).\n\n"
             f"Anteilige Gesamtkosten Mieter: {summe*0.98:,.0f} EUR.\n\n"
             f"Saldo zugunsten {'Vermieter (Nachzahlung Mieter)' if saldo > 0 else 'Mieter (Erstattung)'}: "
             f"{abs(saldo):,.0f} EUR. Die Saldoverrechnung erfolgt mit der naechsten Monatsmiete "
             f"({'Februar' if jahr < 2024 else 'Maerz'} {jahr+1}); ein Widerspruch ist innerhalb von "
             f"12 Monaten nach Zugang dieser Abrechnung beim Vermieter geltend zu machen ("
             f"§ 556 Abs. 3 BGB / lokales Aequivalent).".replace(",", ".")),
            ("Erlaeuterungen zu wesentlichen Posten",
             ("list", [
                f"Heizkosten {jahr}: Anstieg gegenueber Vorjahr um ca. 18 % aufgrund der Erdgas-/Fernwaermeerhoehung infolge Ukrainekrise; Verbrauch wurde durch Programm »Energieeffizienz 2023« (LED, Daemmung, Heizungsoptimierung) um 9 % reduziert.",
                f"Strom Allgemein: Trotz Strompreiserhoehung gleichbleibend, da Eigenstromproduktion aus Photovoltaik (siehe Energieausweis) 22 % des Allgemeinstrombedarfes abdeckt.",
                f"Klimatisierung: Im Sommer {jahr} erhoehter Verbrauch aufgrund Hitzewelle (durchschnittlich +1,8 °C gegenueber 10-Jahres-Mittel).",
                f"Sicherheit: Erhoehter Aufwand wegen 24/7-Werkschutz und Erweiterung Zaehlertelematik / Kameraueberwachung im Aussenbereich.",
                f"Reinigung: Tarifabschluss IG BAU sorgte fuer + 6,1 % Lohnerhoehung der Reinigungsdienste; gegenwirkt durch Wechsel zu Anbieter Sasse Gebaeudemanagement GmbH zum 1.7.{jahr}.",
             ])),
            ("Anlagen / Belege",
             "Belegeinsicht ist nach vorheriger Terminvereinbarung mit dem Property Manager moeglich. "
             "Ein elektronischer Auszug der Originalrechnungen kann auf Anforderung per "
             "verschluesseltem Datenaustausch (SFTP/Drees-&-Sommer-Portal) bereitgestellt werden. "
             "Die Abrechnung wurde durch die interne Revision (Andreas Buehler, Chief Audit Executive) "
             "stichprobenartig geprueft (Pruefungsbericht NK-AB-" + str(jahr) + " vom Maerz "
             f"{jahr+1}). Auswirkung auf Konzern-IFRS-Abschluss: Verbuchung der Mehrbelastung in "
             "GuV-Position »Sonstige betriebliche Aufwendungen«.")
        ])


def inspektion(fname, key, jahr):
    p = PROPS[key]
    write_doc(f"{BASE}/{fname}", p["header"],
        f"Begehungs- und Inspektionsbericht {jahr} – {p['werk']}",
        subtitle=f"Begehung durch Real-Estate-Officer in Begleitung Vermieter / TGA-Sachverstaendigem",
        sections=[
            ("Begehungsrahmen",
             f"Objekt: {p['werk']}, {p['addr']}. Begehungsdatum: 18. Oktober {jahr}, 09:00 – 14:30 Uhr. "
             f"Teilnehmer: Sabine Hartlieb (Real Estate Officer, Konzern Brennhagen), Dr. Wolfgang Hertz "
             f"(Head of Real Estate, Drees & Sommer), {p['verant']}, Vertreter des Vermieters "
             f"({p['vermieter'] or 'Eigentuemerin REA/REG'}), Dipl.-Ing. Markus Reuter "
             f"(Sachverstaendiger TGA, TUEV SUED Industrie Service GmbH).\n\n"
             f"Anlass: Jahresinspektion gemaess Mietvertrag § 5 (Instandhaltung) bzw. interner "
             f"Konzern-Real-Estate-Policy 2023 (Periodizitaet: jaehrlich, Sonderbegehung bei "
             f"wesentlichen Schadensereignissen). Schwerpunkte: Dach (PV-Vorbereitung), Fassade, "
             f"TGA (Heizung/Klima/Lueftung), Brandschutz, Aufzuege, Aussenanlagen."),
            ("Feststellungen",
             ("clauses", [
                ("§ 1 Bauliche Substanz", [
                    f"Dach: Ueberpruefung der Bitumenbahnen-Abdichtung; Lebensdauer bis ca. {jahr+10} "
                    f"(Restbestand 60 %). Empfehlung Daemmungs-Upgrade in Verbindung mit "
                    f"PV-Aufbau; statische Lastreserven (1,15 kN/m²) ausreichend fuer PV-Aufdach.",
                    f"Fassade: Putzschaeden an Nordseite, ca. 18 m² (Rissbildung im uebrigen "
                    f"unauffaellig); Sanierung mit Vermieter zu vereinbaren (Anlage 3).",
                    f"Bodenflaechen (Industrieestrich): keine Auffaelligkeiten; Belastungsproben "
                    f"naechste Pruefung {jahr+2}."]),
                ("§ 2 Technische Gebaeudeausruestung (TGA)", [
                    f"Heizung / Klima / Lueftung: {p['energie']}. Wartungsintervalle eingehalten; "
                    f"Filterwechsel quartalsweise dokumentiert.",
                    f"Elektrotechnik: E-Check nach DGUV V3 durchgefuehrt am 12. September {jahr} durch "
                    f"Elektro-Schmid GmbH; ein Befund (defektes FI in Werkstattbereich) wurde sofort "
                    f"behoben.",
                    f"Aufzuege (3 Personen-/1 Lastenaufzug, Hersteller Thyssenkrupp Elevator): "
                    f"TUEV-Hauptpruefung gueltig bis Dezember {jahr+2}; Wartung Schindler "
                    f"Aufzuege GmbH."]),
                ("§ 3 Brandschutz und Arbeitsschutz", [
                    f"{p['brandschutz']} Probealarm am 18. Oktober {jahr} um 11:30 Uhr durchgefuehrt; "
                    f"Raeumungszeit 4 min 28 sec (Sollwert < 5 min).",
                    f"Flucht- und Rettungswege frei; Beschilderung nach ASR A1.3 vollstaendig. "
                    f"Erste-Hilfe-Material aktuell, naechste Pruefung Januar {jahr+1}.",
                    f"Gefahrstofflager (loethaltige Pasten, Loesemittel) ordnungsgemaess; "
                    f"Auffangwannen mit Restkapazitaet > 30 %."]),
                ("§ 4 Aussenanlagen und Verkehrswege", [
                    f"Parkplaetze (ca. 240 Stellplaetze, davon 12 E-Ladesaeulen): in gutem Zustand; "
                    f"Markierung wird im Fruehjahr {jahr+1} erneuert (Beauftragung erfolgt).",
                    f"Begruenung gepflegt; einzelne Baeume im Sturmtief »Bernd« {jahr-1} geschaedigt, "
                    f"Ersatzpflanzung in Q1 {jahr+1}.",
                    f"Mass-Notification: Zufahrt fuer Feuerwehr / Rettungsdienst frei; Beschilderung "
                    f"Aussenanlagen verbessert nach Empfehlung Werksfeuerwehr."]),
             ])),
            ("Massnahmenliste",
             [["Nr.", "Massnahme", "Verantwortlich", "Termin", "Prioritaet"],
              ["1", "Putzsanierung Nordfassade (18 m²)", "Vermieter", f"Q2 {jahr+1}", "Mittel"],
              ["2", "Dach-Upgrade in Verbindung mit PV-Aufbau", "REA Real Estate", f"Q3 {jahr+1}", "Hoch"],
              ["3", "E-Ladesaeulen Erweiterung +6 Stueck", "Mieter (REA)", f"Q4 {jahr+1}", "Mittel"],
              ["4", "Filterwechsel Klima-Sonderkampagne", "TGA-Sachverstaendiger", f"Januar {jahr+1}", "Niedrig"],
              ["5", "Erneuerung Parkplatzmarkierungen", "Vermieter", f"Q2 {jahr+1}", "Niedrig"]]),
            ("Schlussbemerkung",
             f"Das Objekt {p['werk']} ist in einem ordnungsgemaessen, vertragsgerechten Zustand. "
             f"Der Verkehrswert wird durch die festgestellten Maengel nicht wesentlich beeintraechtigt. "
             f"Naechste turnusmaessige Begehung: Oktober {jahr+1}. Sonderbegehung im Falle eines "
             f"Schadensereignisses oder im Vorlauf zum geplanten PV-Aufdach-Projekt 2024.\n\n"
             f"Berichtersteller: Sabine Hartlieb, Real Estate Officer. Pruefung und Freigabe: "
             f"Dr. Wolfgang Hertz, Head of Real Estate (Drees & Sommer)."),
        ])


def immobilienbewertung(fname, key, stichtag_jahr=2023):
    p = PROPS[key]
    is_eigentum = "Eigentum" in p["tenure"]
    write_doc(f"{BASE}/{fname}", REA_H,
        f"Verkehrswertgutachten / Immobilienbewertung {stichtag_jahr} – {p['werk']}",
        subtitle=f"Stichtag: 31. Dezember {stichtag_jahr}; Gutachter: {p['vw_gutachter']}",
        confidential=True,
        sections=[
            ("Anlass und Gutachter-Bestellung",
             f"Im Rahmen der Konzern-IFRS-Bilanzierung 2023 (IAS 16, IAS 40) sowie der "
             f"Investorenkommunikation der Brennhagen Elektronik AG (Prime Standard, ISIN DE000RHGRP12) "
             f"wurde fuer das Objekt »{p['werk']}« ein Verkehrswertgutachten in Auftrag gegeben. "
             f"Auftraggeber: Brennhagen Holding GmbH (RHO), vertreten durch CFO Laura Bauer. "
             f"Sachverstaendiger: {p['vw_gutachter']}. Methodik: kombiniertes Sachwert- und "
             f"Ertragswertverfahren gemaess ImmoWertV 2021 bzw. Investment Property Standard "
             f"des Royal Institution of Chartered Surveyors (RICS Red Book)."),
            ("Objektbeschreibung",
             [["Merkmal", "Beschreibung"],
              ["Lage", p["addr"]],
              ["Nutzungsart", p["nutzung"]],
              ["Eigentums-/Nutzungsverhaeltnis", p["tenure"]],
              ["Flaeche", p["flaeche"]],
              ["Grundbuch / Kataster", p["grundbuch"]],
              ["Verantwortliche Werksleitung", p["verant"]],
              ["Energiestandard (GEG 2024)", p["energie"]],
              ["Brandschutz", p["brandschutz"]]]),
            ("Bewertungsverfahren",
             ("clauses", [
                ("§ 1 Sachwertverfahren", [
                    f"Bodenrichtwert {p['stadt']} {stichtag_jahr}: Heranziehung des amtlichen "
                    f"Bodenrichtwertes des Gutachterausschusses {p['stadt']} (Daten der BORIS-BW / "
                    f"BORIS-BY bzw. lokales Aequivalent).",
                    f"Gebaeudeherstellungswert (Normalherstellungskosten NHK 2010 fortgeschrieben mit "
                    f"Baupreisindex 2023, Statistisches Bundesamt): Abschlag fuer Altersminderung "
                    f"(Modifizierte Ross-Methode) bei einer wirtschaftlichen Restnutzungsdauer von "
                    f"40 Jahren.",
                    f"Aussenanlagen und Nebenbauten werden mit Pauschalansaetzen aus ImmoWertV "
                    f"Anlage 2 beruecksichtigt."]),
                ("§ 2 Ertragswertverfahren", [
                    f"Roh-Ertraege: Ableitung der nachhaltig erzielbaren Jahresmiete aus "
                    f"Marktbericht JLL / CBRE / Colliers (je nach Region). "
                    f"{'Vergleichsmiete Stuttgart-Vaihingen Industrie/Office: 12,80 EUR/m²/Monat brutto.' if 'Stuttgart' in p['stadt'] else f'Vergleichsmiete {p[chr(34)+chr(115)+chr(116)+chr(97)+chr(100)+chr(116)+chr(34)] if False else p['stadt']} laut Standort-Marktbericht: ' + (p['miete_per_qm'] or 'siehe Anlage 1')}",
                    f"Bewirtschaftungskosten 18 % der Roh-Ertraege (Verwaltung, Instandhaltung, "
                    f"Mietausfallwagnis, Modernisierungsreserve).",
                    f"Liegenschaftszinssatz: {'4,2 % (Industrie/Office Stuttgart, BORIS-BW 2023)' if 'Stuttgart' in p['stadt'] else '5,8 % (Industrie/Logistik je nach Region, Marktbericht 2023)'}; Restnutzungsdauer 40 Jahre."]),
                ("§ 3 Gewichtung und Marktanpassung", [
                    f"Gewichtung Sachwert/Ertragswert: 40 / 60 ({p['stadt']} ist gemischter Industrie- "
                    f"und Office-Markt mit ausreichender Mietnachfrage).",
                    f"Marktanpassung gemaess Marktanpassungsfaktor (MAF) Gutachterausschuss "
                    f"{p['stadt']} 2023.",
                    f"Beruecksichtigung von Sonderwerten: PV-Eignung Dach (+0,5 Mio. EUR), "
                    f"Naehe Hauptverkehrsachsen (+ Anpassung), Altlastenrisiko (Boden-Gutachten "
                    f"unauffaellig; kein Abschlag)."]),
             ])),
            ("Wertermittlung",
             f"Festgestellter Verkehrswert (Marktwert) zum Stichtag 31.12.{stichtag_jahr}: "
             f"**{p['vw']}**. "
             + (f"Buchwert in IFRS-Konzernbilanz {stichtag_jahr}: ca. 80 % des Verkehrswertes "
                f"(Anschaffungs- und Herstellungskosten abzgl. linearer Abschreibung, IAS 16). "
                f"Stille Reserven gegenueber Verkehrswert werden im Anhang erlaeutert."
                if is_eigentum else
                f"Da das Objekt im Mietverhaeltnis steht, wird ein Marktmietwert ermittelt. "
                f"Bilanzielle Beruecksichtigung erfolgt ueber Right-of-Use-Asset (IFRS 16) zzgl. "
                f"Mietsonderausstattung.")),
            ("Annahmen, Vorbehalte und Methodische Grenzen",
             ("list", [
                "Die Bewertung beruht auf den am Stichtag verfuegbaren Daten; spaetere Ereignisse (Krieg, Pandemie, drastische Energiepreissteigerungen) wurden nur in Form anerkannter Marktindizes beruecksichtigt.",
                "Der Gutachter hat das Objekt am 25. Oktober 2023 (Stuttgart/Heilbronn) bzw. zwischen Q3 und Q4 2023 (Auslandsstandorte ueber lokale Partnergutachter) besichtigt.",
                "Boden-/Altlastenrisiken wurden anhand vorgelegter Bodengutachten gewuerdigt; eigene Probennahmen nicht durchgefuehrt.",
                "Steuerliche Auswirkungen (Grunderwerbsteuer, Umsatzsteuer-Option) sind nicht Gegenstand des Gutachtens.",
                "Das Gutachten ist ausschliesslich fuer interne Bilanzierung und Investor-Kommunikation der Brennhagen Elektronik AG bestimmt; eine Weitergabe an Dritte bedarf der schriftlichen Zustimmung des Gutachters und des Auftraggebers.",
             ])),
            ("Unterschrift Sachverstaendiger",
             signatures(p["vw_gutachter"].split(",")[0], "Sachverstaendiger (oeff. best. u. vereidigt)",
                        "IHK " + ("Stuttgart" if "Stuttgart" in p["vw_gutachter"] else
                                  "Heilbronn-Franken" if "Heilbronn-Franken" in p["vw_gutachter"] else "lokal"),
                        "Laura Bauer", "CFO", "Brennhagen Elektronik AG",
                        place=p["stadt"], date_str_=f"14. November {stichtag_jahr}")),
        ])


def umweltgutachten(fname, key, jahr):
    p = PROPS[key]
    write_doc(f"{BASE}/{fname}", p["header"],
        f"Umwelt-/Immissionsschutzgutachten {jahr} – {p['werk']}",
        subtitle=f"Standortbezogenes Boden-, Wasser-, Laerm- und Immissionsgutachten; Stichtag {jahr}",
        sections=[
            ("Anlass und Gutachter",
             f"Im Rahmen der ISO 14001:2015-Rezertifizierung sowie der Vorbereitung des "
             f"Werks-Erweiterungsbauantrags (Heilbronn Linie 4 BMS-12 / Stuttgart ADAS-Erweiterung) "
             f"wurde ein standortbezogenes Umweltgutachten in Auftrag gegeben. Auftraggeber: "
             f"{p['header']['name']}. Sachverstaendige: ERM Group (Environmental Resources Management), "
             f"Niederlassung Frankfurt am Main; lokale Partner: TUEV SUED Industrie Service GmbH "
             f"(Boden, Wasser); Akustikbuero Greiner Ingenieure (Heilbronn) fuer Laerm.\n\n"
             f"Gegenstand: Pruefung der Standortvertraeglichkeit nach BImSchG (Bundes-Immissions"
             f"schutzgesetz, §§ 4 ff., 22 ff.) bzw. polnischem/tschechischem/ungarischem/chinesischem "
             f"Aequivalent. Schwerpunkte: Luftschadstoffe (Loetdaempfe, VOC), Laerm (Lueftung, "
             f"Werksverkehr), Boden- und Grundwasserschutz (Loesemittel, Loetpasten), Abfall- und "
             f"Gefahrstoffmanagement."),
            ("Standortdaten",
             [["Merkmal", "Daten"],
              ["Werk", p["werk"]],
              ["Adresse", p["addr"]],
              ["Naechste Wohnbebauung", "ca. 380 m (in Richtung NW); Mischgebiet"],
              ["Naechste sensible Nutzung (Schule/Kita)", "ca. 720 m (Grundschule)"],
              ["BImSchG-Genehmigung", f"Genehmigung als nicht genehmigungsbeduerftige Anlage gemaess § 22 BImSchG; Erweiterung loest Genehmigungspflicht aus (4. BImSchV Spalte 2 Nr. 3.10)" if "Heilbronn" in p["werk"] or "Stuttgart" in p["werk"] else "Lokales Aequivalent (Polen/CZ/HU/CN) eingehalten; siehe Anlage 3"],
              ["Boden-/Grundwasserschutzgebiet", "Wasserschutzgebiet III (gering); keine Trinkwassergewinnung im Anstrombereich"]]),
            ("Messungen und Ergebnisse",
             ("clauses", [
                ("§ 1 Laerm (Immissionsschutz)", [
                    f"Messzeitraum: 1.6. – 30.9.{jahr}, kontinuierlich. Messpunkte: 4 Aussenpunkte "
                    f"(Werkszaun NW, NO, SO, SW) und 2 Innenpunkte (Halle 2, Lueftungstechnik Dach).",
                    f"Ergebnis Tag (06:00-22:00): Mittelwert 54 dB(A) am naechsten Immissionsort, "
                    f"Grenzwert TA Laerm Mischgebiet 60 dB(A) – eingehalten. Spitzenpegel "
                    f"einzelner Verkehrsbewegungen (LKW-Andienung) 67 dB(A) ueberschritten, "
                    f"jedoch innerhalb der zulaessigen Haeufigkeit nach TA Laerm Nr. 6.1.",
                    f"Ergebnis Nacht (22:00-06:00): 41 dB(A) (Grenzwert 45 dB(A)) – eingehalten. "
                    f"Massnahme: weitere Optimierung Lueftung Dach (Schallhaube Q2 {jahr+1})."]),
                ("§ 2 Luftschadstoffe (VOC, Loetdaempfe, Stickoxide)", [
                    f"Innenraum: VOC-Konzentration < 0,3 mg/m³ (Grenzwert TRGS 900 fuer Loetbereiche "
                    f"2,0 mg/m³) – Abgesicherung durch Punkt-Absaugung an SMD-Loetlinien (Wartung "
                    f"halbjaehrlich, Filtertausch Hahnemuehle Industrial GmbH).",
                    f"Aussenluft: NOx, Feinstaub (PM2,5/PM10) unauffaellig, vergleichbar mit "
                    f"staedtischer Hintergrundkonzentration; eigene Beitrag des Werkes < 5 %.",
                    f"Empfehlung: Erweiterung der Aktivkohlefilter im Bereich Lackierung um eine "
                    f"zweite Stufe bis Q3 {jahr+1}."]),
                ("§ 3 Boden- und Grundwasserschutz", [
                    f"Bodenuntersuchung an 12 Punkten (Bohrungen 2-4 m Tiefe): keine Auffaelligkeiten "
                    f"in Bezug auf PFAS, KW, BTEX, Schwermetalle (Werte unter Pruefwert BBodSchV).",
                    f"Grundwasser-Beprobung an 3 Messstellen (jaehrlich, langjaehrige Reihe): "
                    f"keine signifikanten Veraenderungen; LHKW < Bestimmungsgrenze.",
                    f"Gefahrstofflagerung in WHG-konformer Auffangwanne; Pruefung gemaess AwSV "
                    f"alle 5 Jahre, naechste Pruefung {jahr+2}."]),
                ("§ 4 Abfall- und Gefahrstoffmanagement", [
                    f"Abfallschluesselverordnung AVV: Hauptmengen 12 01 05 (Kunststoffabfaelle), "
                    f"15 02 02* (Loetschlamm, gefaehrlich), 16 02 14 (Elektroaltgeraete). Entsorgung "
                    f"ueber zertifizierte Entsorgungsbetriebe (Veolia, Remondis).",
                    f"Gefahrstoffkataster nach GefStoffV vollstaendig und aktuell; SDB (Sicherheits"
                    f"datenblaetter) im SAP EHS Modul gepflegt. Schulung Mitarbeiter alle 12 Monate.",
                    f"REACH/RoHS-Konformitaet der eingesetzten Stoffe ist Bestandteil des Liefer"
                    f"anten-Auditprogrammes (Konzern-Compliance)."]),
             ])),
            ("Empfehlungen und Massnahmenplan",
             [["Nr.", "Massnahme", "BImSchG/lokal Bezug", "Termin", "Budget (EUR)"],
              ["1", "Schallhaube Lueftungsdach", "TA Laerm Nr. 6.1", f"Q2 {jahr+1}", "85.000"],
              ["2", "Zweite Stufe Aktivkohlefilter Lackierung", "TRGS 900", f"Q3 {jahr+1}", "120.000"],
              ["3", "Erweiterung Grundwasser-Monitoring (+2 Messstellen)", "AwSV / WHG", f"Q4 {jahr+1}", "45.000"],
              ["4", "Energetische Optimierung HVAC", "GEG 2024 / EnEV", f"H2 {jahr+1}", "320.000"],
              ["5", "Vorbereitung BImSchG-Antrag Werkserweiterung", "4. BImSchV", f"H1 {jahr+2}", "60.000"]]),
            ("Schlussfeststellung und Zertifizierung",
             f"Das Werk {p['werk']} betreibt seine Anlagen im Einklang mit dem geltenden "
             f"Immissionsschutz-, Boden- und Wasserrecht. Die Empfehlungen sind Ergebnis einer "
             f"vorsorgenden Pruefung und nicht Folge festgestellter Pflichtverletzungen. Die "
             f"Standortvertraeglichkeit fuer die geplante Werks-Erweiterung (Linie 4 BMS-12 in "
             f"Heilbronn / ADAS-Testzentrum-Erweiterung in Stuttgart) ist gegeben, sofern die "
             f"oben genannten Massnahmen umgesetzt werden.\n\n"
             f"Gutachten erstellt durch: ERM Group, Hanauer Landstrasse 287-289, 60314 Frankfurt am Main; "
             f"Verantwortlicher Sachverstaendiger Dr. Christoph Lehmann (Diplom-Geooekologe). "
             f"Pruefung Konzern-Compliance: Dr. Heike Berger (Group Tax) und Dr. Wolfgang Hertz "
             f"(Head of Real Estate)."),
        ])


# ============================================================================
# Now build all 37 thin files
# ============================================================================

# --- 1. Mietvertraege (7 docs: HQ Stuttgart [internal], Office Muenchen, Office Shanghai, Werk Brno, Werk Gyoer, Werk Heilbronn [internal REA-REG], Werk Katowice)
mietvertrag("REA_Mietvertrag_HQ_Stuttgart_2020.docx", "HQ_Stuttgart",
            "1. Januar 2020", "31. Dezember 2034",
            miete_eur_jahr=1_120_000,  # internal cost allocation
            indexierung="VPI-Bund 2020=100; Schwellenwert 3 %",
            mietzweck_extra="Konzern-interne Kostenverrechnung (Eigentum REA, Nutzung Konzernverwaltung + Holding RHO).")
mietvertrag("REA_Mietvertrag_Werk_Heilbronn_2020.docx", "Werk_Heilbronn",
            "1. Januar 2020", "31. Dezember 2039",
            miete_eur_jahr=2_640_000,  # internal cost allocation REA->REG
            indexierung="VPI-Bund 2020=100",
            mietzweck_extra="Konzern-interne Verrechnung (Eigentum REG; Bauleihe Stadt Heilbronn).")
mietvertrag("REA_Mietvertrag_Office_München_2020.docx", "Office_München",
            "1. Januar 2020", "31. Dezember 2029",
            miete_eur_jahr=1_080_000,
            indexierung="VPI Bayern 2020=100; Schwellenwert 3 %",
            kuendigung_monate=18)
mietvertrag("REA_Mietvertrag_Werk_Katowice_2020.docx", "Werk_Katowice",
            "1. Januar 2020", "31. Dezember 2032",
            miete_eur_jahr=1_440_000,
            indexierung="Polnischer VPI (CPI GUS, Bazowy 2020=100); zusaetzlich KSSE-Preisleitlinie")
mietvertrag("REA_Mietvertrag_Werk_Brno_2020.docx", "Werk_Brno",
            "1. Januar 2020", "31. Dezember 2032",
            miete_eur_jahr=1_120_000,
            indexierung="Tschechischer VPI (CSU), Bazovy index 2020=100")
mietvertrag("REA_Mietvertrag_Werk_Gyoer_2020.docx", "Werk_Gyoer",
            "1. Januar 2020", "31. Dezember 2032",
            miete_eur_jahr=760_000,
            indexierung="Ungarischer VPI (KSH), Alapevi index 2020=100")
mietvertrag("REA_Mietvertrag_Office_Shanghai_2020.docx", "Office_Shanghai",
            "1. Januar 2020", "31. Dezember 2027",
            miete_eur_jahr=980_000,
            indexierung="China CPI (NBS); jaehrliche Anpassung in CNY, EUR-Wechselkurs zum 1.1.")

# --- 2. Nachtraege (7 docs)
for fname, key, jahr, gegenstand, anpass, neue in [
    ("HQ_Stuttgart_Nachtrag_2022.docx", "HQ_Stuttgart", 2022,
     "Indexanpassung 2022 und Klarstellung PV-Aufdach-Nutzung", 5.5, 1_181_600),
    ("Office_München_Nachtrag_2022.docx", "Office_München", 2022,
     "Indexanpassung sowie Erweiterung der angemieteten Flaeche um 320 m² im 6. OG", 4.8, 1_186_240),
    ("Werk_Brno_Nachtrag_2022.docx", "Werk_Brno", 2022,
     "Indexanpassung CSU-VPI und Vereinbarung zu erweiterter Sicherheitsabsicherung (Werkzaun, Kameras)", 6.2, 1_189_440),
    ("Werk_Gyoer_Nachtrag_2022.docx", "Werk_Gyoer", 2022,
     "Indexanpassung KSH-VPI sowie Aufnahme einer Sonderkuendigungs-Klausel fuer den Fall eines Konzern-Standort-Reorganisationsprogramms", 7.8, 819_280),
    ("Werk_Heilbronn_Nachtrag_2022.docx", "Werk_Heilbronn", 2022,
     "Klarstellung Verrechnungssystematik REA-REG (Eigentum bei REG) und Anpassung der Bauleihe-Konditionen mit der Stadt Heilbronn", 4.5, 2_758_800),
    ("Werk_Katowice_Nachtrag_2022.docx", "Werk_Katowice", 2022,
     "Indexanpassung CPI GUS und Vereinbarung zur Errichtung einer PV-Aufdach-Anlage 820 kWp (Pachtnehmer ZAE Solar Sp. z o.o.)", 9.2, 1_572_480),
]:
    nachtrag(fname, key, jahr, gegenstand, anpass, neue)

# --- 3. Nebenkostenabrechnungen (12 docs: 6 properties x 2 Jahre)
for fname, key, jahr in [
    ("HQ_Stuttgart_Nebenkostenabrechnung_2022.docx", "HQ_Stuttgart", 2022),
    ("HQ_Stuttgart_Nebenkostenabrechnung_2023.docx", "HQ_Stuttgart", 2023),
    ("Office_München_Nebenkostenabrechnung_2022.docx", "Office_München", 2022),
    ("Office_München_Nebenkostenabrechnung_2023.docx", "Office_München", 2023),
    ("Werk_Brno_Nebenkostenabrechnung_2022.docx", "Werk_Brno", 2022),
    ("Werk_Brno_Nebenkostenabrechnung_2023.docx", "Werk_Brno", 2023),
    ("Werk_Heilbronn_Nebenkostenabrechnung_2022.docx", "Werk_Heilbronn", 2022),
    ("Werk_Heilbronn_Nebenkostenabrechnung_2023.docx", "Werk_Heilbronn", 2023),
    ("Werk_Katowice_Nebenkostenabrechnung_2022.docx", "Werk_Katowice", 2022),
    ("Werk_Katowice_Nebenkostenabrechnung_2023.docx", "Werk_Katowice", 2023),
]:
    nebenkostenabrechnung(fname, key, jahr)

# --- 4. Inspektionen (6 docs)
for fname, key in [
    ("HQ_Stuttgart_Inspektion_2023.docx", "HQ_Stuttgart"),
    ("Office_München_Inspektion_2023.docx", "Office_München"),
    ("Werk_Brno_Inspektion_2023.docx", "Werk_Brno"),
    ("Werk_Heilbronn_Inspektion_2023.docx", "Werk_Heilbronn"),
    ("Werk_Katowice_Inspektion_2023.docx", "Werk_Katowice"),
]:
    inspektion(fname, key, 2023)

# --- 5. Immobilienbewertungen (6 docs)
for fname, key in [
    ("REA_Immobilienbewertung_HQ_Stuttgart_2023.docx", "HQ_Stuttgart"),
    ("REA_Immobilienbewertung_Office_München_2023.docx", "Office_München"),
    ("REA_Immobilienbewertung_Werk_Brno_2023.docx", "Werk_Brno"),
    ("REA_Immobilienbewertung_Werk_Gyoer_2023.docx", "Werk_Gyoer"),
    ("REA_Immobilienbewertung_Werk_Heilbronn_2023.docx", "Werk_Heilbronn"),
    ("REA_Immobilienbewertung_Werk_Katowice_2023.docx", "Werk_Katowice"),
]:
    immobilienbewertung(fname, key, 2023)

# --- 6. Umweltgutachten (3 docs)
for fname, key in [
    ("REA_Umweltgutachten_REG_2022.docx", "Werk_Heilbronn"),
    ("REA_Umweltgutachten_RHU_2022.docx", "Werk_Gyoer"),
    ("REA_Umweltgutachten_RPL_2022.docx", "Werk_Katowice"),
]:
    umweltgutachten(fname, key, 2022)


# ============================================================================
# 7. Outlier docs (non-property thematics that landed in 18_Immobilien)
# ============================================================================

# --- CAPA_2023_0004 (process CAPA — likely about real-estate-related QMS finding)
write_doc(f"{BASE}/CAPA_2023_0004.docx", REA_H,
    "CAPA-Report Nr. 2023/0004 – Konzern-QMS / Real Estate Compliance",
    subtitle="Corrective and Preventive Action; Trigger: ISO 14001-Auditfeststellung Werk Heilbronn",
    sections=[
        ("Identifikation und Trigger",
         "CAPA-Nr.: 2023/0004. Bereich: Konzern-QMS / Real Estate. Trigger: Major-Findings (2) "
         "und Minor-Findings (4) aus der ISO 14001:2015-Ueberwachungsauditierung 2023 durch "
         "TUEV SUED Management Service GmbH (Lead Auditor: Dipl.-Ing. Andrea Vogt). "
         "Datum Trigger: 12. Juni 2023. Werk: REG Heilbronn (primaer); Standort-Folgewirkung: "
         "Stuttgart HQ, Muenchen, Katowice. Verantwortlich: Sabine Hartlieb (Real Estate Officer) "
         "in Abstimmung mit Andreas Buehler (CAE, Group Internal Audit) und Sabine Brand "
         "(Q-Leitung REG)."),
        ("Sachverhalt",
         "(1) Major: Energieverbrauchs-Reporting der Werke nicht durchgaengig nach ISO 50001 "
         "konsolidiert; vier Standorte (Brno, Gyoer, Katowice, Shanghai) liefern Daten in "
         "uneinheitlichen Formaten (Excel-Templates verschiedener Generationen). Konzern-EHS-"
         "Reporting im Geschaeftsbericht 2022 (Brennhagen Elektronik AG) konnte nur durch manuelle "
         "Korrekturen erstellt werden.\n\n(2) Major: Gefahrstoffkataster in Heilbronn nicht "
         "tagesaktuell (Verzug 11 Wochen). Sicherheitsdatenblaetter fuer 23 Substanzen fehlten "
         "im SAP EHS Modul.\n\n(3) Minor x4: Lueftungsfilterprotokolle Lueckenhaft (2/12 Monate "
         "fehlen); Notausgangsbeschilderung in Halle 2 teilweise verblasst; PSA-Schulungs-"
         "nachweise von 6 Mitarbeitern nicht im Schulungssystem (Cornerstone) eingebucht; "
         "Begehungs-Checklisten nutzen alte Vorlage Version 2.1 statt 3.0."),
        ("Ursachenanalyse (Root Cause)",
         ("clauses", [
            ("§ 1 5-Why-Analyse Major 1 (Energie-Reporting)", [
                "Why 1: Standorte reporten in unterschiedlichen Excel-Formaten – warum? "
                "Konzern-Vorlage 3.0 wurde in 2022 ausgerollt, nicht alle Standorte umgestellt.",
                "Why 2: Umstellung verzoegert – warum? Standortleitungen erhielten kein "
                "verbindliches Roll-out-Schreiben mit Frist und Verantwortlichkeit.",
                "Why 3: Roll-out ohne klare Eskalationspfade – warum? Im Konzern-EHS-Programm "
                "2022 war Real-Estate-Energie-Reporting nicht als Pflicht-Workstream definiert.",
                "Why 4: Pflicht-Workstream gefehlt – warum? Programmplanung 2022 erfolgte vor "
                "Inkrafttreten ESRS (Sustainability Reporting), neue Anforderungen wurden nicht "
                "in den Zielkatalog aufgenommen.",
                "Why 5 (Root Cause): Fehlende Schnittstelle Sustainability-Reporting <-> "
                "Real-Estate-Reporting im Konzern-Governance-Modell."]),
            ("§ 2 Root Cause Major 2 (Gefahrstoffkataster Heilbronn)", [
                "Personalwechsel im EHS-Team Heilbronn (Abgang QA-Officer Februar 2023; "
                "Nachbesetzung erst Juni 2023). Uebergabe der Pflege-Verantwortung fuer SAP EHS "
                "nicht formalisiert; keine Vertretungsregelung."]),
         ])),
        ("Massnahmen (Korrekturen und Vorbeugung)",
         [["CAPA-Nr.", "Massnahme", "Verantwortlich", "Termin", "Status"],
          ["2023/0004-C1", "Konzern-EHS-Reporting-Template 3.0 verbindlich ausrollen; alle 7 Standorte umstellen", "S. Hartlieb / EHS-Lead jedes Werk", "30.11.2023", "in Umsetzung"],
          ["2023/0004-C2", "SAP EHS Gefahrstoffkataster Heilbronn aufholen und tagesaktuell halten; Vertretungsregelung", "EHS-Officer Heilbronn (P. Mueller)", "30.09.2023", "abgeschlossen 12.09.2023"],
          ["2023/0004-C3", "Konzern-Governance-Update: Sustainability + Real Estate gekoppelt; ESRS-Datenfluss definieren", "Dr. W. Hertz / Group Sustainability", "31.12.2023", "in Umsetzung"],
          ["2023/0004-P1", "Pflicht-Schulung Energiemanagement fuer alle Werkleiter (eintaegig, Stuttgart)", "Konzern-HR (Akademie)", "Q4/2023", "geplant 15.11.2023"],
          ["2023/0004-P2", "Quartalsweises EHS-Dashboard fuer Vorstand (Anna Mueller, Laura Bauer)", "Group Controlling (F. Maier)", "ab Q1/2024", "in Vorbereitung"]]),
        ("Wirksamkeitspruefung und Schliessung",
         "Die Wirksamkeit der Korrekturmassnahmen wird in einer Re-Auditrunde im Maerz 2024 durch "
         "TUEV SUED ueberprueft. Konzern-interner Re-Test durch CAE Andreas Buehler im Januar "
         "2024 vorgesehen. CAPA-Schliessung erst nach erfolgreicher Wirksamkeitspruefung; "
         "voraussichtlich 30. April 2024.\n\nFreigabe-Pfad: Real Estate Officer (Hartlieb) -> "
         "Head of Real Estate (Dr. Hertz) -> Group Internal Audit (Buehler) -> Vorstand "
         "(COO Dr. Thomas Weber, Information CFO Laura Bauer)."),
    ])

# --- PRJ-2024-003 Testbericht S/4HANA EOL Funktionstest
write_doc(f"{BASE}/PRJ-2024-003_Testbericht_Funktionstest_EOL_SAP_S_4HANA_Rollout_.docx", REA_H,
    "Testbericht Funktionstest EOL – SAP S/4HANA Rollout Real Estate Modul",
    subtitle="PRJ-2024-003 / Konzern-IT-Programm »S/4HANA Move 2025«; Berichtsdatum: 18. Maerz 2024",
    sections=[
        ("Projekt und Testumfang",
         "Im Rahmen des Konzernprogramms »S/4HANA Move 2025« (Programm-Lead: CIO Stefan "
         "Hoffmann bis 30.6.2024, danach Uebergabe an Dr. Petra Hollmann CTO) wird das alte "
         "SAP ECC 6.0-System durch SAP S/4HANA 2023 abgeloest. Der vorliegende Bericht "
         "dokumentiert den End-of-Line-(EOL)-Funktionstest des Real-Estate-Submoduls (RE-FX "
         "Flexible Real Estate Management) im Rahmen von Projektphase »Test-Welle 3« vom "
         "4. - 15. Maerz 2024.\n\nUmfang: 142 Testfaelle ueber die Geschaeftsprozesse "
         "(P1) Mietvertragsverwaltung, (P2) Nebenkostenabrechnung, (P3) Immobilienbewertung "
         "(IAS 16/IFRS 16), (P4) PV-Aufdach-Vermietung an externe Pachtnehmer und "
         "(P5) Konzern-interne Verrechnung REA-REG und REA-Tochtergesellschaften."),
        ("Testorganisation",
         [["Rolle", "Name", "Bereich"],
          ["Test-Lead", "Lars Wittmann", "RSG Muenchen (Lead Developer)"],
          ["Fachbereich Real Estate", "Sabine Hartlieb", "Real Estate Officer Konzern"],
          ["Fachbereich Accounting", "Dr. Heike Berger", "Group Tax & Accounting Policy"],
          ["IT-Architektur", "Florian Maier (Group Controlling)", "Stuttgart"],
          ["Externer Berater", "PwC Deutschland (Lead Marc Engler)", "Test-Coordination / SAP-Partner"],
          ["Notar / Vertragsmustertest", "Dr. Karin Sonneborn", "Stuttgart"]]),
        ("Testfaelle und Ergebnisse",
         ("clauses", [
            ("§ 1 P1 Mietvertragsverwaltung", [
                "32 Testfaelle ausgefuehrt, 30 PASS, 2 FAIL (TF-018, TF-024). FAIL betraf "
                "Indexierung VPI/CPI mit gemischtem Schwellenwert-Modell: System rechnete "
                "Schwellenwert nicht mehrstufig. Defekt-ID DEF-RE-024.",
                "Workaround: manuelles Override durch RE-Officer; Hotfix von SAP angefordert "
                "(SAP Note 3458291); erwartet Ende April 2024.",
                "Testabdeckung Mietvertraege Brennhagen-Konzern: alle 7 Standorte (REA/REG/RSG/RPL/"
                "RCZ/RHU/RCN); alle Vertragsarten."]),
            ("§ 2 P2 Nebenkostenabrechnung", [
                "28 Testfaelle, 27 PASS, 1 Warning (TF-046): Rundungsdifferenz bei Zweitnachkomma "
                "von 1 ct bei einigen Mehrjahresumlagen. Akzeptable Toleranz; keine Korrektur.",
                "Performance-Test: Abrechnung fuer 14.000 Mietvertraege (Hochrechnung Konzern + "
                "interne Verrechnung) < 6 Minuten. Akzeptanzkriterium < 15 Minuten erfuellt.",
                "PDF-Generierung nach Konzern-Briefkopf erfolgreich; Lokalisierung fuer PL/CZ/HU/CN "
                "in Sprache und Waehrung getestet."]),
            ("§ 3 P3 Immobilienbewertung IAS 16 / IFRS 16", [
                "24 Testfaelle, 24 PASS. Abgleich Verkehrswert (extern gemessen) gegen Buchwert "
                "(intern fortgeschrieben) korrekt; Right-of-Use-Asset-Berechnung fuer Miet-"
                "objekte mit korrekten Diskontierungssaetzen (3,2 % Wpf-Bond-Yield-Equivalent).",
                "Schnittstelle zu Treasury-Modul (TRM) fuer Diskontierungssatz-Anbindung "
                "funktionsfaehig."]),
            ("§ 4 P4 und P5", [
                "26 + 32 Testfaelle, alle PASS bis auf 1 FAIL bei interner Verrechnung REA-RCN "
                "(Waehrungsumrechnung EUR/CNY mit historischem Kurs); DEF-RE-058 dokumentiert.",
                "PV-Aufdach-Pachtvertraege (Pachtnehmer ZAE Solar, MaxSolar etc.) korrekt als "
                "eigener Vertragstyp »LRA« angelegt; monatliche Abrechnung getestet."]),
         ])),
        ("Defekte und Folgemassnahmen",
         "Insgesamt 4 Defekte (2 FAIL Major P1, 1 FAIL Minor P5, 1 Warning P2). Schliessung "
         "DEF-RE-024 abhaengig von SAP-Hotfix; DEF-RE-058 in Konzern-Custom-Code via ABAP "
         "geloest (PR-Reviewer: Lars Wittmann; Merge 15. Maerz 2024).\n\nGo/No-Go-"
         "Empfehlung fuer Steuerungsausschuss: GO mit Auflagen (Aufloesung DEF-RE-024 vor "
         "Cutover; Live-Termin 1. Juli 2024 fuer Welle 3 bestaetigt)."),
        ("Freigabe", signatures("Lars Wittmann", "Test-Lead", "RSG Muenchen",
                                "Sabine Hartlieb", "Real Estate Officer", "Konzern Brennhagen",
                                place="Stuttgart", date_str_="18. Maerz 2024")),
    ])

# --- RCN_IC_Rechnung_2022_09 — internal cost-allocation invoice
write_doc(f"{BASE}/RCN_IC_Rechnung_2022_09.docx", RCN_H,
    "IC-Rechnung 09/2022 – Konzern-interne Verrechnung Immobilien-Services",
    subtitle="Rechnung Nr. RCN-IC-2022-09-021 vom 30. September 2022",
    sections=[
        ("Rechnungsdaten und Vertragsbezug",
         "Rechnungsempfaenger: Brennhagen Holding GmbH (RHO), Vaihinger Strasse 120, 70567 "
         "Stuttgart, HRB 726450, Amtsgericht Stuttgart. Rechnungssteller: Brennhagen (Shanghai) "
         "Co. Ltd. (RCN), Caohejing Hi-Tech Park, Building 7, 888 Hongqiao Road, 200336 "
         "Shanghai-Minhang, China; Unified Social Credit Code 91310115MA1FL42Q38.\n\n"
         "Rechtsgrundlage: Konzern-IC-Verrechnungs-Rahmenvertrag vom 1. Januar 2020 (RHO-RCN) "
         "i.V.m. Transfer-Pricing-Local-File RCN 2022 (TPLF-RCN-2022; Methode TNMM). "
         "Verrechnung gemaess OECD-TP-Guidelines Kapitel VII (Konzern-Dienstleistungen, "
         "Routine-Funktion mit Cost-Plus 5 %)."),
        ("Rechnungsgegenstand: Real-Estate-Services Shanghai",
         [["Position", "Beschreibung", "Menge", "Stundensatz (EUR)", "Betrag (EUR)"],
          ["1", "Standort-Auswahl Shanghai-Pudong fuer zukuenftiges Aftermarket-Logistikzentrum", "120 h", "85,00", "10.200,00"],
          ["2", "Verhandlung Verlaengerung Mietvertrag Caohejing Hi-Tech Park (5 Jahre)", "85 h", "85,00", "7.225,00"],
          ["3", "Koordination ortsansaessiger Sachverstaendiger (Savills) fuer Mietwert-Update 2022", "32 h", "85,00", "2.720,00"],
          ["4", "Sicherheits- und Brandschutz-Reauditierung gemaess GB 50016-2014", "48 h", "85,00", "4.080,00"],
          ["5", "Local-Liaison BMW Brilliance / CATL bzgl. Werks-Erweiterung", "65 h", "85,00", "5.525,00"],
          ["", "ZWISCHENSUMME (Selbstkosten)", "350 h", "", "29.750,00"],
          ["", "Cost-Plus Aufschlag 5 % (Mark-up gemaess TPLF)", "", "", "1.487,50"],
          ["", "RECHNUNGSBETRAG NETTO (EUR)", "", "", "31.237,50"],
          ["", "Reverse-Charge gemaess § 13b UStG (Konzern-Empfaengerin RHO)", "", "", "kein UStAusweis"],
          ["", "ENDSUMME", "", "", "31.237,50"]]),
        ("Zahlungs- und Bankverbindung",
         "Zahlungsziel: 30 Tage netto, faellig 30. Oktober 2022. Bankverbindung Brennhagen "
         "(Shanghai) Co. Ltd.: Bank of China, Shanghai Minhang Branch, IBAN-Aequivalent "
         "(CN): CNAPS 1043 0001 234 5678 90, SWIFT BKCHCNBJ. Waehrungs-Convention: "
         "Rechnung in EUR; Buchung bei RCN in CNY zum EZB-Mittelkurs am Rechnungstag "
         "(1 EUR = 7,1245 CNY am 30.09.2022).\n\nKlaerung Treasury: Markus Pflanzer (Group "
         "Treasurer). Verbuchung RHO: Konto 6320 »Konzern-interne Dienstleistungs"
         "aufwendungen«."),
        ("Compliance und Dokumentationsverweise",
         ("list", [
            "Transfer-Pricing-Konformitaet: Methode Transactional Net Margin Method (TNMM), Cost-Plus 5 % entspricht Marktbenchmark BvD Amadeus Datenbank (Range 4,1 % - 6,8 %).",
            "Local-File RCN 2022 dokumentiert die Verrechnungsleistung (Funktions- und Risikoanalyse).",
            "Master-File Konzern 2022 (KPMG / Dr. Heike Berger Group Tax) verweist auf diese Verrechnungssystematik.",
            "Verstaendigungs-Verfahren CN-DE: keines anhaengig; Vorab-Verstaendigungs-Vereinbarungen (APA) zur Zeit nicht geplant.",
            "Pruefungssicherheit: Rechnungs- und Leistungsbelege im SAP Concur / Coupa Archiv hinterlegt; Aufbewahrungsfrist 10 Jahre.",
            "Freigabe-Workflow: Local CFO RCN (Liang Wei) -> Group Tax (Dr. H. Berger) -> RHO Geschaeftsfuehrung -> Verbuchung.",
         ])),
    ])

# --- RPL_IC_Rechnung_2020_08
write_doc(f"{BASE}/RPL_IC_Rechnung_2020_08.docx", RPL_H,
    "IC-Rechnung 08/2020 – Konzern-interne Verrechnung KSSE-Standortpflege",
    subtitle="Rechnung Nr. RPL-IC-2020-08-017 vom 31. August 2020",
    sections=[
        ("Rechnungsdaten und Vertragsbezug",
         "Rechnungsempfaenger: Brennhagen Holding GmbH (RHO), Vaihinger Strasse 120, 70567 "
         "Stuttgart. Rechnungssteller: Brennhagen Polska Sp. z o.o. (RPL), KSSE Strefa "
         "Aktywnosci Gospodarczej, ul. Wegierska 18, 40-203 Katowice (PL); KRS 0000412376.\n\n"
         "Rechtsgrundlage: Konzern-IC-Verrechnungs-Rahmenvertrag vom 1. Januar 2020 (RHO-RPL); "
         "Transfer-Pricing-Local-File RPL 2020 (TPLF-RPL-2020), Methode TNMM mit "
         "Cost-Plus 4,8 % (Markt-Range fuer EMS-Routine-Funktionen Mitteleuropa)."),
        ("Rechnungsgegenstand: KSSE-Standort- und Immobilien-Services",
         [["Pos.", "Leistung", "Aufwand (h)", "Stundensatz (EUR)", "Betrag (EUR)"],
          ["1", "Verhandlung Mietverlaengerung KSSE Halle 2020-2032 (12 Jahre)", "180", "65,00", "11.700,00"],
          ["2", "Local-Liaison Katowicka SSE (Steuerentlastung Sonderwirtschaftszone)", "95", "65,00", "6.175,00"],
          ["3", "Vorbereitung Bauantrag Hallenerweiterung (Sciany dzialowe) Polski Urzad", "70", "65,00", "4.550,00"],
          ["4", "Energieausweis EUE (Polski odpowiednik GEG) Aktualisierung", "45", "65,00", "2.925,00"],
          ["5", "Koordination polnischer Notar (mec. Tomasz Skiba, Katowice) fuer Mietnachtrag", "28", "65,00", "1.820,00"],
          ["", "ZWISCHENSUMME (Selbstkosten)", "418", "", "27.170,00"],
          ["", "Cost-Plus 4,8 %", "", "", "1.304,16"],
          ["", "ENDSUMME NETTO (EUR)", "", "", "28.474,16"],
          ["", "Reverse-Charge (DE-PL B2B, § 13b UStG)", "", "", "kein UStAusweis"]]),
        ("Zahlungs- und Bankverbindung",
         "Zahlungsziel: 30 Tage netto, faellig 30. September 2020. Bankverbindung RPL: "
         "Bank Pekao S.A., IBAN PL27 1240 0123 4567 8901 2345 6789, SWIFT PKOPPLPW. "
         "Buchung bei RPL in PLN (Konzern-Funktionswaehrung EUR); EZB-Mittelkurs am 31.08.2020: "
         "1 EUR = 4,4012 PLN."),
        ("Compliance und Audit-Trail",
         "Diese IC-Rechnung wurde im Rahmen der Transfer-Pricing-Pruefung 2020 durch Group Tax "
         "(Dr. Heike Berger) ueberprueft und freigegeben. Die Aufschlagshoehe (Cost-Plus 4,8 %) "
         "wurde durch Benchmark-Analyse aus BvD Amadeus-Datenbank (vergleichbare polnische "
         "EMS-/Real-Estate-Service-Provider) gestuetzt. Pruefung KPMG (Dr. Maximilian Brand) "
         "fuer den Jahresabschluss 2020 keine Beanstandungen.\n\nAblage Original im SAP/Concur. "
         "Aufbewahrung 10 Jahre (PL: Ordynacja podatkowa). Verstaendigungsverfahren keines."),
    ])

# --- REA_MBZ_ADAS-V4D_QBR_2023_Q2 (Mercedes-Benz Quarterly Business Review)
write_doc(f"{BASE}/REA_MBZ_ADAS-V4D_QBR_2023_Q2_rev_SRichter.docx", REA_H,
    "Quarterly Business Review Q2/2023 – Mercedes-Benz / ADAS-V4D",
    subtitle="Berichtsperiode 1. April – 30. Juni 2023; Rev. by Stefan Richter (CMO/BD)",
    sections=[
        ("Programm-Status",
         "Programm: ADAS-V4D Radar-Fusion-Steuergeraet Level 2/3 fuer Mercedes-Benz AG "
         "(Programm-Code MBZ-ADAS-2024). Status zum 30.6.2023: B-Sample-Freigabe erteilt "
         "am 12. Mai 2023; C-Sample-Build im August 2023 vorgesehen; SOP 14. Maerz 2024 "
         "(MFA2-Plattform EQE/EQS-Modelljahr 2025).\n\nProjekt-Lead REA: Dr. Petra Hollmann "
         "(designierter CTO ab 1.7.2024); operativ Dr. Klaus Kessler (Werkleiter RSG). "
         "Hauptansprechpartnerin Mercedes-Benz: Frau Dr. Christine Riemer (Director ADAS "
         "Hardware Procurement, Werk Sindelfingen)."),
        ("Standort- und Immobilienbezug",
         "Die Programm-Entwicklung erfolgt vornehmlich im ADAS-Testzentrum am REA-Hauptsitz "
         "Stuttgart-Vaihingen (Eigentum REA, 14.800 m² bebaut, Erweiterung Testzentrum +1.800 m² "
         "in Bauantragsphase – siehe REA-Bauantrag-Stuttgart-ADAS-Erweiterung-2023). "
         "Embedded-Software ASPICE Level 3 wird in RSG Muenchen entwickelt (Lyonel-Feininger-"
         "Strasse 28, 4.620 m² Mietflaeche). EMV-Pruefstand erweitert in Q1 2023 (Investitions"
         "volumen 4,2 Mio. EUR; Foerderung BMWK 'IPCEI ME 2 Microelectronics' 1,1 Mio. EUR)."),
        ("Finanz-Kennzahlen Q2/2023",
         [["Kennzahl", "Plan Q2", "Ist Q2", "Abweichung"],
          ["Umsatz ADAS-V4D (NRE+Serie) Mio. EUR", "12,4", "11,8", "-5 %"],
          ["Auftragseingang Mio. EUR (Lifetime)", "240", "278", "+16 %"],
          ["EBIT-Marge Programm-Sicht", "11,5 %", "10,8 %", "-0,7 pp"],
          ["PPM (Pruefmuster B-Sample)", "< 25", "18", "OK"],
          ["Engineering Resources FTE", "78", "84", "+6 FTE"],
          ["Test-/Werkzeug-Investitionen Mio. EUR", "2,0", "2,3", "+15 %"]]),
        ("Kritische Themen und Aktionen",
         ("list", [
            "DV-Test (Design Verification) Lichtreflex-Empfindlichkeit: 2 Pruefmuster ausserhalb Spezifikation; Root-Cause-Analyse durch Dr. Hollmann; Workaround Antenna-Layout-Patch in C-Sample.",
            "Material-Sourcing TI ADAS-SoC: Verfuegbarkeit ab Q4/2023 wieder normal (Krise 2022 ueberwunden); Alternativlieferant ST Microelectronics (Backup-Design SoP +6 Monate).",
            "Cybersecurity (UN-R 155 / ISO 21434): Audit durch TUEV SUED, Erst-Auditierung 18.-22. September 2023 in Stuttgart und Muenchen; vorbereitende Dokumentation in Bearbeitung.",
            "Tooling-Ausweitung Werkzeugbau REG Heilbronn fuer C-Sample-Spritzguss-Werkzeuge (Investvolumen 1,8 Mio. EUR; Aufstellort Halle 2 Heilbronn).",
            "Bauantrag Erweiterung ADAS-Testzentrum Stuttgart-Vaihingen: Stadt Stuttgart prueft; Genehmigung erwartet Q3/2023.",
         ])),
        ("Freigabe", "Bericht erstellt durch das ADAS-Programmmanagement; Review und Freigabe "
         "durch Stefan Richter (CMO/BD, REA Vorstand). Naechstes QBR Q3/2023 am 17. Oktober "
         "2023 (Stuttgart, Vorstandssitzungsraum) gemeinsam mit Mercedes-Benz Sindelfingen."),
    ])

# --- REA_STE_BMS-12_QBR_2023_Q1 (Stellantis QBR BMS-12)
write_doc(f"{BASE}/REA_STE_BMS-12_QBR_2023_Q1.docx", REA_H,
    "Quarterly Business Review Q1/2023 – Stellantis / BMS-12",
    subtitle="Berichtsperiode 1. Januar – 31. Maerz 2023; Stellantis N.V. (Auftraggeber)",
    sections=[
        ("Programm-Status",
         "Programm: BMS-12 Batteriemanagementsystem fuer Stellantis-Plattform STLA Medium "
         "(Modelle Peugeot E-3008, Opel Grandland-e, Citroen C5 Aircross EV). Status: "
         "C-Sample Build laeuft, SOP 22. April 2024 (Werk Sochaux/Frankreich Pilotlinie).\n\n"
         "Projekt-Lead REA: Dr. Thomas Weber (COO; ueberlappend zu seiner Vorstandsfunktion). "
         "Hauptansprechpartner Stellantis: Monsieur Jean-Luc Marchand (Director Battery "
         "Strategy, Hub Velizy-Villacoublay)."),
        ("Standort- und Immobilien-Bezug",
         "Hauptfertigung BMS-12 erfolgt im REG-Werk Heilbronn (Linie 3 ECU/BMS-Mix, geplante "
         "Erweiterung um eigene Linie 4 BMS-12 in Bauantragsphase – siehe REA_Bauantrag_"
         "Werkserweiterung_REG_Heilbronn_Linie4). EMS-Vorbestueckung erfolgt im Werk Katowice "
         "(RPL, 18.500 m² Halle, Sonderwirtschaftszone KSSE).\n\nKundenanforderungen Stellantis "
         "umfassen jaehrliches On-Site-Audit; naechster Audit-Termin 12.-14. September 2023 "
         "(Heilbronn) und 15.-16. September 2023 (Katowice). Audit-Vorbereitung Real-Estate-"
         "seitig: Sabine Hartlieb in Abstimmung mit Q-Leitungen."),
        ("Finanz-Kennzahlen Q1/2023",
         [["Kennzahl", "Plan Q1", "Ist Q1", "Abweichung"],
          ["Umsatz BMS-12 NRE Mio. EUR", "4,2", "4,5", "+7 %"],
          ["Serien-Lifetime-Volumen MEUR (Letter of Award)", "920", "920", "OK"],
          ["EBIT-Marge Programm", "9,2 %", "8,4 %", "-0,8 pp (Material-Cost-Pass-through anstehend)"],
          ["PPAP-Status (Stellantis Sochaux)", "Phase 3", "Phase 3", "on track"],
          ["Audit-Findings (interne Vor-Audits)", "< 5", "3", "OK"],
          ["Tool-Investitionen Werk Heilbronn (Linie 4 Vorbereitung)", "1,8 Mio. EUR", "1,9", "+5 %"]]),
        ("Risiken und Aktionen",
         ("list", [
            "Material-Cost-Pass-through: Verhandlungen ueber Quartalspreis-Anpassungen (Lithium, Kupfer) laufen; Verschlechterung der Programm-Marge im Plan; erwartete Re-Pricing Q3/2023.",
            "Werkserweiterung REG Heilbronn Linie 4 BMS-12: Bauantrag bei Stadt Heilbronn eingereicht 28. Februar 2023; Anhoerung Nachbarn 20. April 2023; Genehmigung erwartet Q3/2023; Baubeginn Q4/2023; Inbetriebnahme Q3/2024.",
            "Stellantis-Anforderung CO2-Footprint: BMS-12 Lifecycle-Analyse erforderlich; PV-Aufdach Heilbronn 1.480 kWp (Inbetriebnahme 2024) verbessert Scope-1-Footprint signifikant.",
            "Risikomanagement: D&O-Versicherung (Allianz GCS, 50 Mio. EUR VS) deckt programm-spezifische Vorstandsrisiken; Programmhaftpflicht (Liability) ueber Konzernrahmen.",
            "Re-Auditierung IATF 16949 in Q4/2023 vorgesehen (Werke Heilbronn, Katowice, Brno).",
         ])),
        ("Freigabe", "Bericht erstellt durch Programm-Management BMS-12; Review COO Dr. Thomas "
         "Weber. Naechstes QBR Q2/2023 am 18. Juli 2023 in Sochaux (FR)."),
    ])

# --- REA_STE_Claim_Letter_2022 (Stellantis warranty/cost claim letter)
write_doc(f"{BASE}/REA_STE_Claim_Letter_2022.docx", REA_H,
    "Claim-Letter / Schadensanzeige gegenueber Stellantis N.V.",
    subtitle="Bezug: BMS-12 Liefer- und Logistikverpflichtung; Mietausfall Werk Heilbronn",
    sections=[
        ("Adressaten und Bezug",
         "Empfaengerin: Stellantis N.V., 25 Bath Road, Slough SL1 4LU, United Kingdom (Sitz: "
         "Amsterdam); z.Hd. Mr. Jean-Luc Marchand, Director Battery Strategy.\n\n"
         "Absenderin: Brennhagen Elektronik AG, Vaihinger Strasse 120, 70567 Stuttgart, HRB 726451 "
         "AG Stuttgart, vertreten durch CEO Anna Mueller und CFO Laura Bauer; im Konzern "
         "operativ Werkleiter REG Heilbronn (Andreas Maier).\n\nBezug: Rahmenliefervertrag "
         "BMS-12 vom 18. Mai 2022 (Lieferanten-Nr. 4002314, Stellantis Procurement-Code "
         "RE-BMS-001-VEL); Letter of Award fuer STLA Medium Plattform. Datum dieses "
         "Schreibens: 28. Oktober 2022."),
        ("Sachverhalt",
         "Am 12. August 2022 kam es im Werk REG Heilbronn (Wertheimer Strasse 12, Industrie"
         "gebiet Heilbronn-Boeckingen) durch einen Stromausfall im oeffentlichen Netz "
         "(Verursacher: Netze BW GmbH, schadhafte Mittelspannungs-Schaltanlage Heilbronn-"
         "Nord) zu einem ungeplanten Produktionsstillstand der Linie 3 (BMS/ECU-Mix) ueber "
         "37 Stunden. In dieser Zeit konnten 4.180 BMS-12-Einheiten nicht gefertigt werden.\n\n"
         "Die anschliessende Hochfahrphase der SMT-Loetstrassen erforderte einen 8-stuendigen "
         "Re-Kalibrier-Lauf, in dem 240 Pruefmuster nicht den Stellantis-PPAP-Spezifikationen "
         "entsprachen und ausgeschossen werden mussten. Durch die Bauleihe-Konditionen "
         "(Stadt Heilbronn / REG) und die Werks-Eigenversorgung mit Notstrom-Diesel waren "
         "die Werksanlagen zwar geschuetzt; die Werks-Lueftung und einige Reinraum-Module "
         "fielen jedoch auf »Notbetrieb« zurueck."),
        ("Kostenpositionen",
         [["Pos.", "Kostenart", "Betrag (EUR)", "Anmerkung"],
          ["1", "Lohnausfall Produktion Heilbronn (37 h x 95 MA)", "118.480", "Bezahlte Wartezeit gemaess IG Metall TV"],
          ["2", "Diesel-/Notstromkosten Werk Heilbronn", "12.350", "Werks-Notstromaggregat"],
          ["3", "Ausschuss 240 Pruefmuster B-Sample (Material)", "84.000", "350 EUR/Einheit"],
          ["4", "Sonder-Schichten Aufholproduktion (Wochenenden)", "215.200", "Zuschlaege 50 % Sa, 100 % So"],
          ["5", "Erhoehte Mietnebenkosten August 2022 (Lueftung 24/7)", "9.840", "Vermieter-Abrechnung"],
          ["6", "Logistik-Sondersendungen (Airfreight Sochaux)", "62.500", "DHL Industrial Express"],
          ["7", "Anwaltskosten Hengeler Mueller (Stand 28.10.2022)", "18.200", "Kanzleihonorar"],
          ["", "ZWISCHENSUMME", "520.570", ""],
          ["", "Erwartet weitere Folgekosten Q4/2022 (Pruefung)", "ca. 80.000-120.000", "Indikativ"]]),
        ("Anspruchsgrundlage und Forderung",
         "Wir machen unter Hinweis auf § 8 (Liefertreue) und § 14 (Force Majeure mit Vorbehalt) "
         "des Rahmenliefervertrages BMS-12 vom 18. Mai 2022 sowie unter Beruecksichtigung der "
         "fortlaufenden Auditprotokolle Stellantis Sochaux vom 22.-24. August 2022 (Audit-Nr. "
         "STE-AUD-2022-118) folgende Position geltend:\n\n"
         "(1) Wir sehen den Vorfall als Ereignis hoeherer Gewalt (Force Majeure) im Sinne von "
         "§ 14 RV. Eine schuldhafte Lieferverzoegerung durch REA ist nicht gegeben; die "
         "Kausalkette beginnt beim Netze-BW-Verursacher. Eine Vertragsstrafe ist nicht "
         "verwirkt.\n\n"
         "(2) Zugleich bitten wir um partielle Anerkennung Ihrerseits, dass die unter Pos. 1-6 "
         "aufgefuehrten Kosten in Hoehe von EUR 502.370 fuer die Aufrechterhaltung des Liefer"
         "verhaeltnisses (insbesondere Sonder-Schichten und Airfreight zur Schadensminimierung) "
         "anfielen. Wir schlagen vor, diese Position im Wege einer einmaligen Kosten-Teilung "
         "50/50 abzubilden; unser Antrag auf Erstattung aus Ihrer Hand belaeuft sich auf "
         "EUR 251.185, abzueglich anteiliger Pos. 7."),
        ("Naechste Schritte",
         "Wir bitten um schriftliche Stellungnahme bis spaetestens 30. November 2022. Eine "
         "ergaenzende Telefonkonferenz zwischen Frau Bauer (CFO REA), Frau Sabine Hartlieb "
         "(Real Estate Officer / Werks-Operations) und Herrn Marchand sowie Mr. Pierre "
         "Lefevre (Stellantis Procurement Counsel) wird vorgeschlagen am 9. November 2022, "
         "14:00 CET. Anwaltlich begleitet wird REA durch Hengeler Mueller Partnerschaft mbB "
         "(Frankfurt, Partner Dr. Sebastian Henn). Im Falle keiner einvernehmlichen Loesung "
         "behaelt sich REA die gerichtliche oder schiedsgerichtliche Geltendmachung vor "
         "(Stellantis-Rahmenvertrag § 22 Schiedsklausel ICC Paris).\n\n"
         "Mit freundlichen Gruessen, fuer den Vorstand der Brennhagen Elektronik AG: Laura Bauer "
         "(CFO) i.V. Anna Mueller (CEO)."),
    ])

# --- RSG_BR_Korrespondenz_Betriebsaenderung_Interessenausgleich_2022 (RSG works council)
write_doc(f"{BASE}/RSG_BR_Korrespondenz_Betriebsaenderung_Interessenausgleich_2022.docx", RSG_H,
    "Korrespondenz Betriebsrat – Interessenausgleich Betriebsaenderung Standort RSG 2022",
    subtitle="Standort RSG Muenchen-Schwabing; Anlass: Flaechenoptimierung und Hybrid-Working-Konzept",
    sections=[
        ("Anlass und Verfahrensstand",
         "Im Rahmen des Hybrid-Working-Konzeptes »RSG Smart Office 2023« plant die Geschaefts"
         "leitung der Brennhagen Software GmbH (Werkleiter Dr. Klaus Kessler) eine Reduktion der "
         "angemieteten Bueroflaeche am Standort Lyonel-Feininger-Strasse 28, 80807 Muenchen, "
         "um voraussichtlich 1.020 m² (von 4.620 m² auf 3.600 m²) zum 1. April 2023. "
         "Hintergrund: Auswertung der Anwesenheitsdaten 2021/2022 zeigt eine durchschnittliche "
         "Anwesenheitsquote von 38 % bei einer Gesamt-FTE von 340 Mitarbeitenden.\n\n"
         "Die Flaechenreduktion umfasst die Aufgabe des 6. OG (1.020 m²) bei gleichzeitiger "
         "Verdichtung der verbleibenden Flaechen mit modernen Workplace-Konzepten (Desk-Sharing-"
         "Quote 1,3 : 1). Da die Massnahme als Betriebsaenderung im Sinne von § 111 BetrVG zu "
         "qualifizieren ist, wurde der oertliche Betriebsrat (Vorsitzender Lars Wittmann, "
         "stv. Vorsitz Andrea Hofer) am 14. Oktober 2022 informiert."),
        ("Bisheriger Verhandlungsstand",
         ("clauses", [
            ("§ 1 Termine und Sitzungen", [
                "14. Oktober 2022: Erstes Informationsgespraech Geschaeftsleitung – BR (Kessler, Wittmann, Hofer; Real Estate Officer Sabine Hartlieb).",
                "8. November 2022: Sondersitzung BR mit Anhoerung Hartlieb zum Detailkonzept; ausfuehrliche Diskussion zu Arbeitsplatz-Standards (Schallschutz, Akustik, Tageslicht, Frischluft).",
                "22. November 2022: Vorlage erster Entwurf Interessenausgleich; Beteiligung der gewerkschaftlichen Vertretung (IG Metall, KBR-Vorsitzende Marlies Duerr eingebunden).",
                "9. Dezember 2022: Anhoerung Werks-Arbeitssicherheit (Sifa) und Betriebsarzt zu Arbeitsplatz-Mindeststandards.",
                "Naechste Sitzung 19. Dezember 2022 zur Beschlussfassung Interessenausgleich (Ziel)."]),
            ("§ 2 Strittige Punkte", [
                "Desk-Sharing-Quote: BR fordert 1,2 : 1 statt 1,3 : 1 (mehr persoenliche Arbeitsplaetze).",
                "Mindest-Arbeitsplatz-Flaeche: BR fordert 12 m² je Arbeitsplatz (ASR A1.2 plus Sicherheit); Geschaeftsleitung 10 m².",
                "Mobiles Arbeiten: BR fordert Verankerung eines Anspruches auf 50 % Mobile Working (statt »Kann-Regelung«).",
                "Sozialplan: nicht erforderlich (keine Kuendigungen geplant); BR akzeptiert; jedoch Wunsch nach Hardware-Ausstattung Home-Office (Monitor, ergonomischer Stuhl)."]),
            ("§ 3 Konsensbereiche", [
                "Reduktion der angemieteten Flaeche und Aufgabe 6. OG: BR stimmt zu (oekonomisch und oekologisch sinnvoll).",
                "Investitionsprogramm »Smart Office« (4.200 EUR pro verbleibendem Arbeitsplatz inkl. Akustik-Verbesserung, Beleuchtung, Klima): BR stimmt zu.",
                "Vorbereitung Aufgabe 6. OG: Gemeinsamer Begleit-Ausschuss aus 2 BR-Mitgliedern und 2 GL-Vertretern."]),
         ])),
        ("Naechste Schritte",
         "Bis 19.12.2022 soll der Interessenausgleich beschlossen werden. Die Geschaeftsleitung "
         "wird in der Zwischenzeit Verhandlungen mit dem Vermieter (Allianz Real Estate GmbH) "
         "zur Flaechenrueckgabe fuehren; Mietreduktion ab 1.4.2023 angestrebt. Die Real-Estate-"
         "seitige Begleitung erfolgt durch Sabine Hartlieb (in enger Abstimmung mit Dr. Wolfgang "
         "Hertz / Drees & Sommer). Anwaltliche Begleitung der Konzernseite: Hengeler Mueller "
         "(Frankfurt); Begleitung BR-seitig: Kanzlei Schipp & Partner (Muenchen).\n\n"
         "Information KBR und Konzernbetriebsrats-Vorsitzende Marlies Duerr (IG Metall) sowie "
         "Information CFO Laura Bauer und COO Dr. Thomas Weber im Vorstand der Brennhagen "
         "Elektronik AG erfolgt im Rahmen der ueblichen Monatsberichte. Voraussichtliche "
         "Einsparung Konzern-Sicht: 235.000 EUR p.a. (Kaltmiete plus NK-Reduktion 6. OG)."),
    ])

print("Done — all 37 docs written.")
