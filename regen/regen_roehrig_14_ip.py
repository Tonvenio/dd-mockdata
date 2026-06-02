"""Brennhagen AG / 14_IP_Technologie – Patente, Bescheide, Jahresgebuehren,
Erteilungsurkunden, Antwortschriften Anmelder, ECOs, FTOs, Technologielizenzen,
Source-Escrow, OpenSource-Compliance, Exportkontrolle, JDA. ~157 thin docs.

Idempotent: overwrites only files that exist at expected paths.
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
from enhance_lib import ROEHRIG_AG as R, write_doc, signatures

BASE = Path(f"{_ROOT}/roehrig_large/14_IP_Technologie")
H = {"name": R["name"], "addr": R["addr"], "hrb": R["hrb"]}


# ── Master Patent Catalog ─────────────────────────────────────────────────
# Patent_NR → (kurztitel, voll_titel, produktbezug, technologie_feld,
#              anwalt_kanzlei, anwalt_lead, erfinder_liste, anmeldejahr,
#              ipc_klasse, jurisdiktionen)
PATENTS = {
    "01": ("Adaptive Zykluszeit-Optimierung",
           "Verfahren und Vorrichtung zur adaptiven Zykluszeit-Optimierung in Automotive-Steuergeraeten",
           "ECU-900",
           "AUTOSAR-Schedulertechnik, Task-Priorisierung in Multicore-Aurix-Architekturen",
           "Maiwald Patentanwaelte", "Dr. Dipl.-Ing. Hartmut Reinkemeier",
           ["Marco Frey (RSG)", "Dr. Stefan Brodbeck (RSG)"],
           2021, "G06F 9/48", "DE / EP / US"),
    "02": ("4D-Radarfusion-Kamerasystem",
           "Kamerasystem mit 4D-Radarfusion zur Objekt-Klassifikation in ADAS-Anwendungen",
           "ADAS-V4D",
           "Sensor-Fusion 4D-Radar (77 GHz) + Mono-/Stereo-Kamera, ML-Klassifikator",
           "Maiwald Patentanwaelte", "Dr. Dipl.-Ing. Hartmut Reinkemeier",
           ["Dr. Stefan Brodbeck (RSG)", "Prof. Dr. Markus Lienkamp (TUM, Mit-Erfinder)"],
           2022, "G01S 13/86", "DE / EP / US / CN / JP"),
    "03": ("Praediktives BMS mit ML",
           "Batteriemanagementsystem mit praediktivem State-of-Health-Modell auf Basis neuronaler Netze",
           "BMS-12",
           "SOH-/SOC-Estimation mittels LSTM-Netzen, Cell-Balancing-Steuerung",
           "Maiwald Patentanwaelte", "Dr. Dipl.-Ing. Hartmut Reinkemeier",
           ["Dr. Petra Hollmann (REG)", "Dr. Markus Lehmann (Fraunhofer ISC)"],
           2023, "G01R 31/367", "DE / EP / US / CN"),
    "04": ("CAN-FD-Priorisierung",
           "CAN-FD-Priorisierungsalgorithmus fuer gemischte sicherheitskritische Bus-Topologien",
           "ECU-900",
           "Bus-Scheduling CAN-FD, Mixed-Criticality, ISO 26262 ASIL-D Konformitaet",
           "Maiwald Patentanwaelte", "Dr. Dipl.-Ing. Hartmut Reinkemeier",
           ["Marco Frey (RSG)", "Andreas Schultheiss (REG)"],
           2020, "H04L 12/40", "DE / EP / US"),
    "05": ("EMV-Unterdrueckung Matrix-LED",
           "Verfahren zur EMV-Unterdrueckung bei pixelgenauer Ansteuerung von Matrix-LED-Modulen",
           "LightCtrl-7",
           "EMV-Filterung in PWM-Pixelansteuerung, Spreizspektrum-Modulation",
           "Boehmert & Boehmert", "Dr. Stefan Rueber",
           ["Dipl.-Ing. Thomas Krause (REG)", "Dr. Klaus Kessler (RSG)"],
           2021, "H05B 45/00", "DE / EP / US"),
    "06": ("Selbstkalibrierendes Sensorsystem",
           "Selbstkalibrierendes Sensorsystem fuer Radar-Lidar-Kamera-Fusion in Level-3-ADAS",
           "ADAS-V4D",
           "Autokalibrierung Multi-Sensor, Online-Detektion Dejustage waehrend Fahrt",
           "Maiwald Patentanwaelte", "Dr. Dipl.-Ing. Hartmut Reinkemeier",
           ["Dr. Stefan Brodbeck (RSG)", "Prof. Dr. Lutz Eckstein (RWTH Aachen)"],
           2022, "G01S 7/40", "DE / EP / US / CN / JP"),
    "07": ("OTA-Updateverfahren",
           "OTA-Updateverfahren fuer Automotive-ECUs mit fehlertoleranter Dual-Bank-Architektur",
           "ICP-3",
           "OTA Software-Updates, Dual-Bank-Flash, Rollback-Mechanismus, Signatur-Validierung",
           "Boehmert & Boehmert", "Dr. Stefan Rueber",
           ["Lars Wittmann (RSG)", "Dr. Klaus Kessler (RSG)"],
           2023, "G06F 8/65", "DE / EP / US / CN"),
    "08": ("Redundantes Ueberwachungssystem",
           "Redundantes Ueberwachungssystem fuer Powertrain-ECUs nach ASIL-D",
           "ECU-900",
           "Watchdog-Architektur Dual-Lockstep, sicherheitsrelevante Plausibilisierung",
           "Maiwald Patentanwaelte", "Dr. Dipl.-Ing. Hartmut Reinkemeier",
           ["Andreas Schultheiss (REG)", "Marco Frey (RSG)"],
           2020, "G06F 11/16", "DE / EP / US"),
    "09": ("Spurwechsel-Detektion",
           "Verfahren zur Detektion von Spurwechselabsichten benachbarter Fahrzeuge mittels Verhaltenspraediktion",
           "ADAS-V4D",
           "Trajektorienpraediktion, Bayes'sche Inferenz, ML-Verhaltensmodell",
           "Maiwald Patentanwaelte", "Dr. Dipl.-Ing. Hartmut Reinkemeier",
           ["Dr. Stefan Brodbeck (RSG)", "Prof. Dr. Markus Lienkamp (TUM)"],
           2021, "G08G 1/16", "DE / EP / US / CN / JP"),
    "10": ("Waermemanagement EV-Batterie",
           "Waermemanagement-Optimierung in EV-Batteriemodulen durch praediktive Stroemungssteuerung",
           "BMS-12",
           "Thermisches Modell, CFD-basierte praediktive Kuehlsteuerung, Cell-Temperatur-Egalisierung",
           "Maiwald Patentanwaelte", "Dr. Dipl.-Ing. Hartmut Reinkemeier",
           ["Dr. Petra Hollmann (REG)", "Dr. Markus Lehmann (Fraunhofer ISC)"],
           2022, "H01M 10/625", "DE / EP / US / CN"),
    "11": ("Hochintegrierte Sensor-PCB",
           "Prozess zur Herstellung von Hochintegrationssensor-Leiterplatten mit eingebetteten Halbleitern",
           "ADAS-V4D",
           "Embedded-Die-Technologie, LDI-Strukturierung, Hochfrequenz-Substrate",
           "Boehmert & Boehmert", "Dr. Stefan Rueber",
           ["Dipl.-Ing. Frank Hahn (RPL)", "Dr.-Ing. Thomas Becker (Fraunhofer IPA)"],
           2023, "H05K 3/46", "DE / EP / US"),
    "12": ("Galvanische Trennung",
           "Vorrichtung zur galvanischen Entkopplung in Hochvolt-Batteriesystemen",
           "BMS-12",
           "Hochvolt-Isolationsmonitoring, Optokoppler-Topologie, ASIL-D",
           "Maiwald Patentanwaelte", "Dr. Dipl.-Ing. Hartmut Reinkemeier",
           ["Dr. Petra Hollmann (REG)", "Dipl.-Ing. Bernd Mueller (REG)"],
           2020, "H02M 7/00", "DE / EP / US / CN"),
    "13": ("Praezise Strommessung",
           "Verfahren zum praezisen Strommessen in EV-Hochvolt-Systemen mittels kompensierter Hall-Sensoren",
           "BMS-12",
           "Hall-Sensorik mit Temperatur-Kompensation, Closed-Loop-Architektur",
           "Maiwald Patentanwaelte", "Dr. Dipl.-Ing. Hartmut Reinkemeier",
           ["Dr. Petra Hollmann (REG)", "Dr. Klaus Kessler (RSG)"],
           2021, "G01R 19/00", "DE / EP / US"),
    "14": ("Datenschutzkonformes Logging",
           "Datenschutzkonformes Logging-Verfahren fuer fahrzeuginterne Telematikdaten",
           "ICP-3",
           "DSGVO-konformes Event-Logging, anonymisierte Telematik, Pseudonymisierung",
           "Boehmert & Boehmert", "Dr. Stefan Rueber",
           ["Lars Wittmann (RSG)", "Dr. Klaus Kessler (RSG)"],
           2022, "G06F 21/62", "DE / EP / US"),
    "15": ("Laser-Direct-Imaging",
           "Laser-Direct-Imaging (LDI) Verfahren fuer hochpraezise Leiterplattenfertigung",
           "BMS-12 / ECU-900 (Fertigung)",
           "LDI-Strukturierungstechnik fuer Multilayer-PCB, Aufloesung < 25 um",
           "Boehmert & Boehmert", "Dr. Stefan Rueber",
           ["Dipl.-Ing. Frank Hahn (RPL)", "Marek Wojciechowski (RPL)"],
           2023, "H05K 3/00", "DE / EP / US"),
    "16": ("Hochfrequenz-Substrat",
           "Hochfrequenz-Substratmaterial fuer 77-GHz-Radaranwendungen mit reduzierter Dielektrizitaetskonstante",
           "ADAS-V4D",
           "Material-Substrate fuer mmWave, Dielektrika mit Dk < 3.0",
           "Maiwald Patentanwaelte", "Dr. Dipl.-Ing. Hartmut Reinkemeier",
           ["Dipl.-Ing. Frank Hahn (RPL)", "Dr.-Ing. Thomas Becker (Fraunhofer IPA)"],
           2020, "H05K 1/03", "DE / EP / US"),
    "17": ("Praediktiver Bremseingriff",
           "Verfahren zum praediktiven Bremseingriff in Notbrems-Assistenzsystemen",
           "ADAS-V4D",
           "AEB-Algorithmik, Eskalationsstrategie, Konfidenz-Schwellwerte",
           "Maiwald Patentanwaelte", "Dr. Dipl.-Ing. Hartmut Reinkemeier",
           ["Dr. Stefan Brodbeck (RSG)", "Prof. Dr. Lutz Eckstein (RWTH Aachen)"],
           2021, "B60T 7/22", "DE / EP / US / CN / JP"),
    "18": ("Glare-Free-Beam Matrix-LED",
           "Verfahren zur blendfreien Lichtverteilung bei Matrix-LED-Scheinwerfersystemen",
           "LightCtrl-7",
           "Pixel-genaue Lichtausblendung, Kamera-basierte Objekterkennung, Glare-Reduction",
           "Boehmert & Boehmert", "Dr. Stefan Rueber",
           ["Dipl.-Ing. Thomas Krause (REG)", "Dr. Klaus Kessler (RSG)"],
           2022, "B60Q 1/14", "DE / EP / US"),
}

# Patent-Aktenzeichen-Generator
def aktenz(nr, jahr, jurisdiktion="EP"):
    base = 10_240_000 + int(nr) * 137 + (jahr - 2020) * 1000
    return f"{jurisdiktion} {base}.{3 + int(nr) % 7}"


# ── PATENTSCHRIFT (15 docs) ───────────────────────────────────────────────
def patentschrift(nr):
    matches = list(BASE.glob(f"Patent_{nr}_*[!Antwort]*[!Bescheid]*[!Erteilungs]*[!Jahresgebuehr]*_2023*.docx"))
    matches = [m for m in matches if all(x not in m.name for x in
               ("Antwort", "Bescheid", "Erteilungsurkunde", "Jahresgebuehr"))]
    if not matches:
        return None
    path = matches[0]
    kt, voll, prod, feld, kanzlei, lead, erfinder, anm_jahr, ipc, jurisd = PATENTS[nr]

    write_doc(str(path), H,
        f"Patentschrift Nr. {nr} – {voll}",
        subtitle=f"Aktenzeichen {aktenz(nr, anm_jahr)}, IPC-Klasse {ipc}",
        sections=[
            ("1. Bibliographische Daten",
             [["Feld", "Inhalt"],
              ["Aktenzeichen (EP)", aktenz(nr, anm_jahr, "EP")],
              ["Anmeldedatum", f"15. Maerz {anm_jahr}"],
              ["Veroeffentlichungstag", f"22. September {anm_jahr + 1}"],
              ["Anmelder", R["name"] + ", Vaihinger Strasse 120, 70567 Stuttgart"],
              ["Erfinder", "; ".join(erfinder)],
              ["Vertreter", f"{kanzlei} ({lead})"],
              ["IPC-Klasse", ipc],
              ["Bestimmungsstaaten", jurisd],
              ["Produktbezug", prod],
              ["Status", "erteilt" if anm_jahr <= 2022 else "in Pruefung"]]),
            ("2. Zusammenfassung der Erfindung",
             f"Die vorliegende Erfindung betrifft {voll.lower()}. Stand der "
             f"Technik im Bereich {feld.lower()} weist insbesondere die Nachteile "
             f"auf, dass bestehende Loesungen entweder eine unzureichende "
             f"Skalierbarkeit fuer Automotive-Echtzeitanwendungen zeigen, eine "
             f"hohe Latenz im Bereich kritischer Funktionspfade aufweisen oder "
             f"den Anforderungen der Funktionssicherheit gemaess ISO 26262 ASIL-D "
             f"nicht in vollem Umfang gerecht werden. Die erfindungsgemaesse "
             f"Loesung zeichnet sich dadurch aus, dass durch eine neuartige "
             f"Kombination aus Hardware-Architektur und Software-Algorithmik "
             f"gleichzeitig die Anforderungen an Echtzeitfaehigkeit, "
             f"Funktionssicherheit (ASIL-D nach ISO 26262) und Cybersecurity "
             f"(ISO/SAE 21434) erfuellt werden. Hierdurch wird die fuer das "
             f"Produkt {prod} der {R['name']} typische Performance- und "
             f"Sicherheitsanforderung erfuellt, ohne dass dies zu erhoehten "
             f"Stueckkosten oder Bauraumbedarf fuehrt."),
            ("3. Patentansprueche (Auszug)",
             ("list", [
                f"Anspruch 1 (Hauptanspruch): {kt} nach dem in der Beschreibung "
                f"definierten erfindungsgemaessen Prinzip, dadurch gekennzeichnet, "
                f"dass eine Kombination der Merkmale a) bis e) verwendet wird, "
                f"wobei Merkmal a) die spezifische Architektur-Topologie und "
                f"Merkmal b) das erfindungsgemaesse Steuerungsverfahren umfasst.",
                f"Anspruch 2: Vorrichtung nach Anspruch 1, dadurch gekennzeichnet, "
                f"dass das Steuerungsverfahren auf einem Multicore-Aurix-TC397-"
                f"Mikrocontroller implementiert ist.",
                f"Anspruch 3: Verfahren nach Anspruch 1 oder 2, dadurch "
                f"gekennzeichnet, dass die Datenuebertragung ueber einen CAN-FD- "
                f"oder Automotive-Ethernet-Bus erfolgt und ASIL-D-konform "
                f"plausibilisiert wird.",
                "Anspruch 4: Vorrichtung nach einem der Ansprueche 1 bis 3, "
                "dadurch gekennzeichnet, dass eine Cybersecurity-Funktion gemaess "
                "ISO/SAE 21434 implementiert ist (HSM-basierte Schluesselverwaltung).",
                "Anspruch 5: Computerprogrammprodukt zur Ausfuehrung des "
                "Verfahrens nach einem der Ansprueche 1 bis 4 auf einer "
                "Steuerung eines Kraftfahrzeugs.",
                "Anspruch 6: Kraftfahrzeug mit einem Steuergeraet, das eine "
                "Vorrichtung nach einem der Ansprueche 1 bis 5 enthaelt.",
             ])),
            ("4. Hintergrund / Stand der Technik",
             f"Der einschlaegige Stand der Technik im Bereich {feld} ist "
             f"insbesondere aus den Druckschriften DE 10 2018 213 547 A1, "
             f"EP 3 421 218 B1 sowie US 2020/0123456 A1 bekannt. Allerdings "
             f"loesen die dort beschriebenen Ansaetze die hier vorliegende "
             f"Aufgabenstellung nicht oder nur unzureichend. Insbesondere "
             f"fehlt eine integrierte Behandlung von Funktionssicherheit "
             f"(ISO 26262) und Cybersecurity (ISO/SAE 21434), wie sie fuer "
             f"das Produkt {prod} erforderlich ist."),
            ("5. Erfindungsgemaesse Loesung – Beschreibung",
             f"Die Erfindung loest die o.g. Aufgabe durch eine neuartige "
             f"Kombination der Merkmale gemaess Hauptanspruch. Im "
             f"Ausfuehrungsbeispiel wird die Loesung in einem Steuergeraet der "
             f"{R['name']} (Produkt {prod}) implementiert. Die "
             f"Hardware-Architektur basiert auf einem Aurix-Mikrocontroller "
             f"(Infineon TC397) im Lockstep-Modus. Die Software-Komponente ist "
             f"als AUTOSAR-konformer Software-Baustein (BSW-Modul) realisiert "
             f"und nach ASPICE Level 3 entwickelt. Validierung und Verifikation "
             f"erfolgten gemaess ISO 26262-6 (Software-Lebenszyklus) und "
             f"ISO 21434 (Cybersecurity Engineering). Die Patentanmeldung "
             f"wurde durch {kanzlei} ({lead}) ausgearbeitet und "
             f"begleitet."),
            ("6. Industrielle Anwendbarkeit",
             f"Die Erfindung findet industrielle Anwendung im Bereich der "
             f"Automobil-Elektronik, insbesondere im Produkt {prod} der "
             f"{R['name']}. Die geschaetzte Stueckzahl belaeuft sich auf "
             f"ueber 1 Mio. Einheiten pro Jahr. Die wirtschaftliche Bedeutung "
             f"der Erfindung wird als hoch eingestuft. Erfindervergueutungen "
             f"gem. ArbnErfG wurden mit den genannten Erfindern vereinbart "
             f"(Vergueutungsschema gemaess Konzernrichtlinie 14.3 'Erfindungsverwaltung')."),
        ])
    return path


# ── BESCHEID EPA (Patent_NN_Bescheid_EPA_YYYY) ────────────────────────────
def bescheid_epa(nr, jahr):
    matches = list(BASE.glob(f"Patent_{nr}_Bescheid_EPA_{jahr}*.docx"))
    if not matches:
        return None
    path = matches[0]
    kt, voll, prod, feld, kanzlei, lead, erfinder, anm_jahr, ipc, jurisd = PATENTS[nr]

    write_doc(str(path), H,
        f"Bescheid des Europaeischen Patentamts – Patent Nr. {nr}",
        subtitle=f"EPA-Pruefbescheid gemaess Art. 94(3) EPUe, Aktenzeichen {aktenz(nr, anm_jahr)}",
        sections=[
            ("1. Verfahrensdaten",
             [["Feld", "Inhalt"],
              ["EPA-Aktenzeichen", aktenz(nr, anm_jahr, "EP")],
              ["Anmelder", R["name"]],
              ["Vertreter", f"{kanzlei}, {lead}"],
              ["Pruefer EPA", "M. Vandermeer (Hauptpruefer), Den Haag"],
              ["Bescheid-Datum", f"14. Juni {jahr}"],
              ["Frist zur Stellungnahme", f"4 Monate, d.h. bis 14. Oktober {jahr}"],
              ["Rechtsgrundlage", "Art. 94(3) EPUe, Regel 71(1) EPUe"],
              ["Bezugnehmende Anmeldung", f"Patent-Akte Nr. {nr} ({kt})"]]),
            ("2. Pruefungssachstand",
             f"Das Europaeische Patentamt hat die Anmeldung mit dem Aktenzeichen "
             f"{aktenz(nr, anm_jahr)} (Erfindung: »{voll}«) inhaltlich gepruefte. "
             f"Im Ergebnis sind die Ansprueche 1 bis 6 in der eingereichten "
             f"Fassung nicht in vollem Umfang gewaehrbar. Die Pruefungsabteilung "
             f"hat folgende Beanstandungen erhoben, die in der vorliegenden "
             f"Mitteilung erlaeutert werden:"),
            ("3. Beanstandungen im Einzelnen",
             ("list", [
                f"Anspruch 1 weist gegenueber dem Stand der Technik gemaess "
                f"D1 (EP 3 421 218 B1) keine erfinderische Taetigkeit gemaess "
                f"Art. 56 EPUe auf. Die im kennzeichnenden Teil genannten "
                f"Merkmale sind dem Fachmann aus D1, Spalte 4, Z. 18-32, in "
                f"naheliegender Weise zu entnehmen.",
                f"Anspruch 2 ist unklar formuliert (Art. 84 EPUe). Insbesondere "
                f"die Angabe 'Multicore-Aurix-TC397-Mikrocontroller' ist eine "
                f"Marken-/Produkbezeichnung und muss durch generische "
                f"Merkmalsangaben ersetzt werden.",
                f"Anspruch 3 enthaelt eine unzulaessige Erweiterung gegenueber "
                f"den urspruenglich eingereichten Unterlagen (Art. 123(2) EPUe). "
                f"Die Variante 'Automotive-Ethernet' ist in der urspruenglichen "
                f"Anmeldung nicht offenbart.",
                f"Die Ansprueche 4 bis 6 teilen die Maengel der Bezugsansprueche. "
                f"Eine erneute Pruefung erfolgt nach Vorlage der geaenderten "
                f"Anspruchsfassung.",
             ])),
            ("4. Im Pruefungsverfahren beruecksichtigte Druckschriften",
             [["Code", "Druckschrift", "Relevanz"],
              ["D1", "EP 3 421 218 B1 (Continental AG)", "Stand der Technik – naechstliegend"],
              ["D2", "US 2020/0123456 A1 (Bosch GmbH)", "Stand der Technik – relevant"],
              ["D3", "DE 10 2018 213 547 A1 (ZF Friedrichshafen)", "Stand der Technik – relevant"],
              ["D4", "WO 2019/118432 A1 (Mobileye)", "ergaenzend zitiert"]]),
            ("5. Aufforderung an den Anmelder",
             f"Der Anmelder wird aufgefordert, innerhalb der oben genannten "
             f"Frist von 4 Monaten (bis 14. Oktober {jahr}) zu den vorgenannten "
             f"Beanstandungen Stellung zu nehmen und ggf. eine geaenderte "
             f"Anspruchsfassung einzureichen. Anderenfalls wird die Anmeldung "
             f"gemaess Art. 94(4) EPUe zurueckgewiesen. Eine muendliche Verhandlung "
             f"kann hilfsweise beantragt werden (Art. 116 EPUe)."),
            ("6. Interne Bewertung – Patentanwalt",
             f"Aus Sicht von {kanzlei} ({lead}) sind die Beanstandungen zu "
             f"Anspruch 1 und 2 mit hoher Wahrscheinlichkeit ueberwindbar. Die "
             f"Beanstandung zu Anspruch 3 (Art. 123(2) EPUe) erfordert eine "
             f"Anspruchsumformulierung; die Streichung der Variante 'Automotive-"
             f"Ethernet' wird empfohlen. Eine vollstaendige Erteilung mit "
             f"reduziertem Schutzumfang gegenueber dem ursprueglich beantragten "
             f"wird erwartet. Empfehlung: Antwortschrift binnen 8 Wochen "
             f"einreichen, Erfinder-Rueckkopplung zu Anspruch 3 einholen."),
        ])
    return path


# ── ANTWORTSCHRIFT ANMELDER ───────────────────────────────────────────────
def antwort_anmelder(nr, jahr, suffix=""):
    pattern = f"Patent_{nr}_Antwort_Anmelder_{jahr}{suffix}.docx"
    path = BASE / pattern
    if not path.exists():
        # try wildcard
        m = list(BASE.glob(f"Patent_{nr}_Antwort_Anmelder_{jahr}*.docx"))
        if not m: return None
        path = m[0]
    kt, voll, prod, feld, kanzlei, lead, erfinder, anm_jahr, ipc, jurisd = PATENTS[nr]

    write_doc(str(path), H,
        f"Antwort auf EPA-Bescheid – Patent Nr. {nr} ({kt})",
        subtitle=f"Erwiderung gemaess Art. 94(3) EPUe, Aktenzeichen {aktenz(nr, anm_jahr)}",
        sections=[
            ("1. Anrede und Bezug",
             f"An das Europaeische Patentamt, Pruefungsabteilung 2.4.6 "
             f"(Hauptpruefer M. Vandermeer). Sehr geehrte Damen und Herren, "
             f"namens und im Auftrag der Anmelderin, {R['name']}, "
             f"vertreten durch {kanzlei} ({lead}), erwidern wir hiermit "
             f"fristwahrend auf den Bescheid des Europaeischen Patentamts vom "
             f"14. Juni {jahr} in der Patentanmeldung Aktenzeichen "
             f"{aktenz(nr, anm_jahr)} (»{voll}«) wie folgt."),
            ("2. Verfahrensdaten",
             [["Feld", "Inhalt"],
              ["Anmelder", R["name"]],
              ["Aktenzeichen EPA", aktenz(nr, anm_jahr, "EP")],
              ["Vertreter", f"{kanzlei} ({lead})"],
              ["Bezugnehmender Bescheid", f"14. Juni {jahr}"],
              ["Eingangsdatum dieser Erwiderung", f"28. September {jahr}"],
              ["Frist gemaess Bescheid", f"14. Oktober {jahr}"],
              ["Status", "fristwahrend eingereicht"]]),
            ("3. Stellungnahme zur erfinderischen Taetigkeit (Anspruch 1)",
             f"Der Auffassung der Pruefungsabteilung, der Anspruch 1 beruhe "
             f"gegenueber D1 (EP 3 421 218 B1) nicht auf einer erfinderischen "
             f"Taetigkeit, koennen wir nicht folgen. D1 offenbart zwar Merkmale "
             f"a) und b) des Hauptanspruchs, jedoch nicht die erfindungsgemaesse "
             f"Kombination mit Merkmal c) (sicherheitsrelevante Plausibilisierung "
             f"nach ASIL-D) und Merkmal d) (HSM-basierte Cybersecurity gemaess "
             f"ISO/SAE 21434). Diese Kombination ist dem Fachmann zum "
             f"Anmeldetag nicht naheliegend gewesen, da der einschlaegige Stand "
             f"der Technik weder die Notwendigkeit noch die technische "
             f"Realisierbarkeit dieser Kombination nahelegte. Die "
             f"erfindungsgemaesse Loesung erzielt einen ueberraschenden "
             f"technischen Effekt (Reduktion der Latenz im kritischen Pfad um "
             f">35 % bei gleichzeitiger Erhaltung der ASIL-D-Konformitaet), der "
             f"in keiner der zitierten Entgegenhaltungen nahegelegt wird."),
            ("4. Geaenderte Anspruchsfassung (Art. 123(2) EPUe)",
             ("list", [
                "Anspruch 1 (Hauptanspruch) wurde unveraendert beibehalten.",
                "Anspruch 2 wurde umformuliert: Die markenrechtliche Bezeichnung "
                "'Aurix-TC397' wurde durch die generische Formulierung 'Multicore-"
                "Mikrocontroller mit Lockstep-Faehigkeit' ersetzt (Art. 84 EPUe).",
                "Anspruch 3 wurde geaendert: Die Variante 'Automotive-Ethernet' "
                "wurde gestrichen, da diese in den urspruenglich eingereichten "
                "Unterlagen nicht offenbart war (Art. 123(2) EPUe).",
                "Ansprueche 4 bis 6 wurden redaktionell an die geaenderten "
                "Bezugsansprueche angepasst.",
                "Hilfsantrag wird vorsorglich eingereicht: Anspruch 1 mit "
                "zusaetzlichem Merkmal 'wobei die Funktionssicherheit nach "
                "ISO 26262 ASIL-D nachgewiesen ist'.",
             ])),
            ("5. Antrag",
             f"Wir beantragen, die Patentanmeldung in der mit dieser "
             f"Erwiderung eingereichten geaenderten Fassung (Hauptantrag) zu "
             f"erteilen. Hilfsweise wird die Erteilung in der Fassung des "
             f"Hilfsantrags beantragt. Vorsorglich wird eine muendliche "
             f"Verhandlung gemaess Art. 116 EPUe beantragt, sofern die "
             f"Pruefungsabteilung der vorliegenden Erwiderung nicht in vollem "
             f"Umfang folgen sollte."),
            ("6. Anlagen",
             ("list", [
                "Anlage 1: Geaenderte Anspruchsfassung (Hauptantrag), 6 Seiten",
                "Anlage 2: Geaenderte Anspruchsfassung (Hilfsantrag), 6 Seiten",
                "Anlage 3: Vergleichsdarstellung urspruengliche vs. neue Fassung",
                "Anlage 4: Pruefbericht ASIL-D Konformitaet (Auszug)",
                "Anlage 5: Vollmacht (bereits aktenkundig)",
             ])),
            ("7. Schlussbemerkung und Unterschrift",
             signatures(lead, "Patentanwalt", kanzlei,
                        "Dr. Dipl.-Ing. Florian Maier", "IP-Manager", R["name"],
                        place="Muenchen", date_str_=f"28. September {jahr}")),
        ])
    return path


# ── ERTEILUNGSURKUNDE ─────────────────────────────────────────────────────
def erteilungsurkunde(nr, jahr, suffix=""):
    m = list(BASE.glob(f"Patent_{nr}_Erteilungsurkunde_{jahr}*.docx"))
    if not m: return None
    path = m[0]
    kt, voll, prod, feld, kanzlei, lead, erfinder, anm_jahr, ipc, jurisd = PATENTS[nr]

    write_doc(str(path), H,
        f"Erteilungsurkunde Patent Nr. {nr}",
        subtitle=f"Europaeisches Patentamt – Erteilung gemaess Art. 97(1) EPUe",
        sections=[
            ("1. Patentdaten",
             [["Feld", "Inhalt"],
              ["Patentnummer (EP)", f"EP {3_400_000 + int(nr)*317} B1"],
              ["Anmeldetag", f"15. Maerz {anm_jahr}"],
              ["Erteilungstag", f"22. November {jahr}"],
              ["Veroeffentlichung Erteilung", f"22. November {jahr}"],
              ["Patentinhaber", R["name"] + ", Vaihinger Strasse 120, 70567 Stuttgart"],
              ["Erfinder", "; ".join(erfinder)],
              ["Vertreter", f"{kanzlei} ({lead})"],
              ["IPC-Klasse", ipc],
              ["Benennungsstaaten", jurisd],
              ["Schutzdauer bis", f"15. Maerz {anm_jahr + 20}"]]),
            ("2. Bezeichnung der Erfindung",
             f"»{voll}«. Die Erfindung gehoert dem technischen Gebiet {feld} "
             f"an und findet Anwendung im Produkt {prod} der "
             f"{R['name']}."),
            ("3. Erteilungsformel",
             f"Das Europaeische Patentamt erteilt hiermit gemaess Art. 97(1) "
             f"des Europaeischen Patentuebereinkommens (EPUe) auf die "
             f"Patentanmeldung mit dem Aktenzeichen {aktenz(nr, anm_jahr)} "
             f"vom 15. Maerz {anm_jahr} fuer die Patentinhaberin {R['name']} "
             f"das vorliegende Patent. Das Patent tritt mit der heutigen "
             f"Veroeffentlichung am 22. November {jahr} in Kraft und gilt "
             f"in den nachfolgend genannten Vertragsstaaten."),
            ("4. Benennungsstaaten und Validierung",
             f"Das vorliegende EP-Patent wird in folgenden Staaten validiert "
             f"und in Kraft gesetzt: {jurisd}. Die nationalen Validierungen "
             f"erfolgen durch {kanzlei} ({lead}) in Zusammenarbeit mit den "
             f"jeweiligen lokalen Anwaltskanzleien (USA: Fish & Richardson, "
             f"China: CCPIT, Japan: Sonderhoff & Einsel). Die Validierungs- "
             f"und Uebersetzungsgebuehren belaufen sich auf insgesamt "
             f"ca. 18.500 EUR und wurden durch die IP-Abteilung der "
             f"{R['name']} freigegeben."),
            ("5. Zur Anmeldung gehoerende Unterlagen",
             ("list", [
                "Patentbeschreibung (32 Seiten)",
                "Patentansprueche 1 bis 6 (4 Seiten)",
                "Zeichnungen Fig. 1 bis Fig. 7 (8 Seiten)",
                "Zusammenfassung der Erfindung (1 Seite)",
                "Pruefungs- und Erteilungsakte (vollstaendig)",
             ])),
            ("6. Anweisungen an die Patentabteilung",
             f"Die Patentabteilung der {R['name']} (Lead: Dr. Dipl.-Ing. "
             f"Florian Maier) wird angewiesen, das Patent in das interne "
             f"Patent-Management-System (IPMS, Anaqua) einzupflegen und die "
             f"Jahresgebuehren ab dem 3. Patentjahr automatisch via Maiwald "
             f"Patentanwaelte / Boehmert & Boehmert an das EPA zu entrichten. "
             f"Die Erfinder erhalten gemaess ArbnErfG eine Vergueutung; die "
             f"Bewertung erfolgt durch das Erfinder-Bewertungs-Komitee "
             f"(Lead: Dr. Petra Hollmann, CTO)."),
        ])
    return path


# ── JAHRESGEBUEHR ─────────────────────────────────────────────────────────
def jahresgebuehr(nr, jahr):
    m = list(BASE.glob(f"Patent_{nr}_Jahresgebuehr_{jahr}*.docx"))
    if not m: return None
    path = m[0]
    kt, voll, prod, feld, kanzlei, lead, erfinder, anm_jahr, ipc, jurisd = PATENTS[nr]
    patentjahr = jahr - anm_jahr + 1
    gebuehr_de = 90 + patentjahr * 35
    gebuehr_ep = 470 + patentjahr * 95

    write_doc(str(path), H,
        f"Jahresgebuehr-Quittung Patent Nr. {nr}",
        subtitle=f"Patent {kt} – Aktenzeichen {aktenz(nr, anm_jahr)}, Patentjahr {patentjahr}",
        sections=[
            ("1. Verfahrensdaten",
             [["Feld", "Inhalt"],
              ["Patentinhaber", R["name"]],
              ["Aktenzeichen EPA", aktenz(nr, anm_jahr, "EP")],
              ["Bezeichnung", voll],
              ["Patentjahr", str(patentjahr)],
              ["Faelligkeitsdatum", f"15. Maerz {jahr}"],
              ["Zahlungseingang", f"03. Maerz {jahr}"],
              ["Vertreter", f"{kanzlei} ({lead})"],
              ["IPMS-Vorgang", f"ANAQUA-{30000 + int(nr) * 17}-{jahr}"]]),
            ("2. Aufstellung der entrichteten Jahresgebuehren",
             [["Jurisdiktion", "Patentjahr", "Gebuehr (EUR)", "Status", "Zahlungs-Ref."],
              ["Deutschland (DPMA)", str(patentjahr), f"{gebuehr_de:.2f}", "bezahlt",
               f"DPMA-{40000 + int(nr) * 11}-{jahr}"],
              ["Europaeisches Patent (EPA)", str(patentjahr), f"{gebuehr_ep:.2f}", "bezahlt",
               f"EPA-{50000 + int(nr) * 13}-{jahr}"],
              ["USA (USPTO)", str(patentjahr), f"{gebuehr_ep * 0.85:.2f}", "bezahlt",
               f"USPTO-{60000 + int(nr) * 7}-{jahr}"],
              ["China (CNIPA)", str(patentjahr), f"{gebuehr_ep * 0.55:.2f}", "bezahlt",
               f"CNIPA-{70000 + int(nr) * 19}-{jahr}"]]),
            ("3. Gesamtaufwand fuer das Patentjahr",
             f"Die Gesamtaufwendung fuer das Patentjahr {patentjahr} der "
             f"Schutzrechte zur Erfindung »{voll}« belaeuft sich auf "
             f"{gebuehr_de + gebuehr_ep + gebuehr_ep*0.85 + gebuehr_ep*0.55:.2f} "
             f"EUR (Summe aller Jurisdiktionen DE/EP/US/CN). Anwaltsgebueren "
             f"in Hoehe von 850,00 EUR (Pauschale {kanzlei}) wurden separat "
             f"in Rechnung gestellt. Die Buchung erfolgt auf Kostenstelle "
             f"5910 (IP-Verwaltung), Sachkonto 6815 (Schutzrechtsgebueren)."),
            ("4. Empfehlung der IP-Abteilung",
             f"Die IP-Abteilung empfiehlt, das Patent Nr. {nr} ({kt}) "
             f"weiterhin in allen Jurisdiktionen aufrechtzuerhalten. Das "
             f"Patent ist fuer das Produkt {prod} strategisch relevant; "
             f"eine Aufgabe wird nicht empfohlen. Der naechste Review erfolgt "
             f"im Rahmen der jaehrlichen Patentportfolio-Sitzung (Q4 {jahr}). "
             f"Verantwortlich: Dr. Dipl.-Ing. Florian Maier (IP-Manager)."),
            ("5. Zahlungsbestaetigung",
             f"Die Jahresgebuehren wurden fristgerecht und ohne Aufschlag "
             f"entrichtet. Die entsprechenden Zahlungsquittungen liegen "
             f"elektronisch im IPMS (Anaqua) sowie in der Akte "
             f"{kanzlei} vor. Verbuchung erfolgte am {jahr}-03-05 durch "
             f"Florian Maier (Group Controller). Eine Kopie dieser "
             f"Bestaetigung wurde an Group Treasury (Markus Pflanzer) "
             f"sowie an die Wirtschaftspruefer (KPMG, Dr. Maximilian "
             f"Brand) im Rahmen der Pruefung 2023 verteilt."),
        ])
    return path


# ── ECO – Engineering Change Order ────────────────────────────────────────
PRODUKT_INFO = {
    "ADAS-V4D": ("ADAS-Vision 4D Radar-Fusion-Steuergeraet",
                 "Mercedes-Benz, Stellantis",
                 "Dr. Stefan Brodbeck (RSG)",
                 "Sensor-Fusion, ML-Modelle, ISO 26262 ASIL-D"),
    "BMS-12": ("BatteryMS-12 Batteriemanagementsystem",
               "VW (ID.7), Hyundai",
               "Dr. Petra Hollmann (REG)",
               "Cell-Supervisor, Balancing, Thermomanagement"),
    "ECU-900": ("Powertrain-ECU Gen3",
                "VW (MEB+/MQB-Evo), Stellantis",
                "Andreas Schultheiss (REG)",
                "Aurix TC397, AUTOSAR 4.3, OBD/UDS"),
    "ICP-3": ("InfoConnect Pro Infotainment-Modul",
              "BMW, Mercedes",
              "Lars Wittmann (RSG)",
              "Linux Yocto, Android Automotive, OTA-Updates"),
    "LightCtrl-7": ("LightCtrl-7 Matrix-LED Steuermodul",
                    "Audi, BMW",
                    "Dipl.-Ing. Thomas Krause (REG)",
                    "Pixel-Control, Glare-Free-Beam"),
}


def eco(produkt, nr, jahr, fn=None):
    if fn is None:
        fn = BASE / f"ECO_{produkt}_{nr:03d}_Engineering_Change_{jahr}.docx"
    if not fn.exists(): return None
    prod_voll, kunden, leiter, technik = PRODUKT_INFO[produkt]
    eco_id = f"ECO-{produkt}-{nr:03d}-{jahr}"

    # ECO themes vary by produkt
    themen = {
        "ADAS-V4D": "Update des Radar-Fusion-Algorithmus auf Version 4.7 mit verbesserter "
                    "Mehrziel-Verfolgung in Stauszenarien, ausgeloest durch Field-Issue Mercedes",
        "BMS-12": "Anpassung der SOC-Schaetzung fuer Niedertemperatur-Betrieb (-20 degC bis 0 degC) "
                  "nach Feldbeobachtungen bei VW ID.7, Reduktion der SOC-Abweichung von 4,2 % auf 2,1 %",
        "ECU-900": "AUTOSAR-Stack-Update von R20-11 auf R21-11 mit Anpassung des RTE-Generators "
                   "und Korrektur eines Latenzproblems im CAN-FD-Sendebuffer",
        "ICP-3": "Integration der neuen BMW Style-Guide 2023 in die HMI-Schicht, Wechsel des "
                 "Compositors auf Wayland 1.21, Verbesserung der App-Cold-Start-Zeit",
        "LightCtrl-7": "Anpassung der Pixel-PWM-Frequenz auf 1.6 kHz zur EMV-Verbesserung, "
                       "Aktualisierung der Glare-Free-Beam-Logik fuer Stadt-Szenarien",
    }
    thema = themen[produkt]

    write_doc(str(fn), H,
        f"Engineering Change Order {eco_id}",
        subtitle=f"Produkt {prod_voll} – ECO Nr. {nr:03d}/{jahr}",
        sections=[
            ("1. Antragsdaten",
             [["Feld", "Inhalt"],
              ["ECO-Nummer", eco_id],
              ["Produkt", prod_voll],
              ["Antragsteller", leiter],
              ["Antragsdatum", f"15. Juni {jahr}"],
              ["Fachbereich", "Engineering / R&D"],
              ["Betroffene Kunden", kunden],
              ["Klassifizierung", "Major Change" if nr % 3 == 0 else "Minor Change"],
              ["Kostenstelle", "5210 / R&D"],
              ["CCB-Termin", f"22. Juni {jahr}"]]),
            ("2. Beschreibung der Aenderung",
             f"Im Rahmen der laufenden Produktpflege des {prod_voll} (Produkt-"
             f"Code {produkt}) wird die folgende Aenderung beantragt: {thema}. "
             f"Die Aenderung wird sowohl auf der Hardware- (sofern betroffen) "
             f"als auch auf der Software-Ebene umgesetzt. Die technische "
             f"Verantwortung liegt bei {leiter}, die Implementierung erfolgt "
             f"durch die zustaendigen Entwicklungsteams in Heilbronn (REG) "
             f"und Muenchen (RSG)."),
            ("3. Begruendung",
             f"Die Aenderung ist erforderlich, um die mit den OEM-Kunden "
             f"({kunden}) abgestimmten Anforderungen zu erfuellen sowie um "
             f"identifizierte Field-Issues und/oder regulatorische Vorgaben "
             f"abzudecken. Die technischen Themen umfassen: {technik}. Eine "
             f"Nichtumsetzung wuerde zu Vertragsabweichungen und ggf. "
             f"Reklamationen fuehren. Die Aenderung ist ferner Voraussetzung "
             f"fuer die Freigabe der naechsten Software-Release "
             f"(SW-R-{jahr}.{nr % 5 + 2})."),
            ("4. Auswirkungen (Impact-Analyse)",
             [["Dimension", "Bewertung", "Kommentar"],
              ["Funktionssicherheit (ISO 26262)", "GERING", "ASIL-D-Konformitaet bleibt erhalten"],
              ["Cybersecurity (ISO/SAE 21434)", "GERING", "Keine Aenderung der Threat-Modell-Grundlage"],
              ["EMV (LV124, CISPR 25)", "MITTEL", "Re-Test EMV erforderlich"],
              ["Klima-/Mechanikvalidierung", "GERING", "Keine HW-Aenderung"],
              ["Produktion / EOL-Test", "MITTEL", "EOL-Skript-Update erforderlich"],
              ["Kostenwirkung (Stueck)", "± 0,12 EUR", "Vernachlaessigbar"],
              ["PPAP-Relevanz", "JA" if nr % 3 == 0 else "NEIN",
               "Bei Major Change PPAP-Update erforderlich"],
              ["Zeitplan", "8 Wochen", "Implementierung bis Q4"]]),
            ("5. Umsetzungsplan",
             ("list", [
                "Woche 1-2: Detail-Spezifikation und Lastenheft-Update",
                "Woche 3-5: Implementierung Software / ggf. HW-Aenderung",
                "Woche 6: Modul-/Integrationstest",
                "Woche 7: Systemtest + Validierung (EMV, Klima sofern betroffen)",
                "Woche 8: Freigabe durch CCB, Roll-out via SW-OTA / Werks-Update",
             ])),
            ("6. Genehmigungen",
             [["Funktion", "Name", "Status", "Datum"],
              ["Engineering Lead", leiter, "GENEHMIGT", f"22.06.{jahr}"],
              ["Quality (Q)", "Sabine Brand (REG)", "GENEHMIGT", f"22.06.{jahr}"],
              ["Functional Safety", "Dr. Klaus Kessler (RSG)", "GENEHMIGT", f"22.06.{jahr}"],
              ["Production", "Andreas Maier (REG)", "GENEHMIGT", f"22.06.{jahr}"],
              ["Procurement", "Anette Schmidt", "GENEHMIGT", f"22.06.{jahr}"],
              ["Customer Mgmt", "Stefan Richter (CMO/BD)", "GENEHMIGT", f"23.06.{jahr}"]]),
            ("7. Kundeninformation",
             f"Die betroffenen OEM-Kunden ({kunden}) werden ueber die "
             f"Aenderung mittels Customer Change Request (CCR) Nr. "
             f"CCR-{produkt}-{nr:03d}-{jahr} informiert. Die Freigabe durch "
             f"die OEM-Kunden wird bis Ende Q3 {jahr} erwartet."),
        ])
    return fn


# ── FTO Analyse ────────────────────────────────────────────────────────────
def fto(produkt, kunde):
    fn = BASE / f"FTO_{produkt}_{kunde}_2023.docx"
    if not fn.exists(): return None
    prod_voll, _, _, technik = PRODUKT_INFO[produkt]
    kunden_voll = {"BMW": "BMW Group", "VW": "Volkswagen AG", "MBZ": "Mercedes-Benz Group AG"}[kunde]

    write_doc(str(fn), H,
        f"Freedom-to-Operate Analyse – {prod_voll} (Kunde {kunden_voll})",
        subtitle=f"FTO-Analyse zur Lieferung Produkt {produkt} an {kunden_voll}, Stand 2023",
        confidential=True,
        sections=[
            ("1. Zusammenfassung (Executive Summary)",
             f"Die vorliegende FTO-Analyse untersucht die patentrechtliche "
             f"Risikolage bei der Lieferung des Produkts {prod_voll} ({produkt}) "
             f"an den OEM-Kunden {kunden_voll}. Im Rahmen der Analyse wurden "
             f"insgesamt 247 relevante Patentfamilien in den Jurisdiktionen "
             f"DE, EP, US, CN und JP recherchiert. Im Ergebnis wird das "
             f"Freedom-to-Operate-Risiko fuer das Produkt {produkt} als "
             f"GERING bis MITTEL eingestuft (Ampel: GELB)."),
            ("2. Auftragsdaten",
             [["Feld", "Inhalt"],
              ["Auftraggeber intern", "Stefan Richter (CMO/BD), Dr. Petra Hollmann (CTO)"],
              ["Auftragsdatum", "08. Januar 2023"],
              ["Externer Berater", "Maiwald Patentanwaelte, Dr. Reinkemeier"],
              ["FTO-Scope", f"Produkt {produkt} fuer Lieferung an {kunden_voll}"],
              ["Jurisdiktionen", "DE / EP / US / CN / JP"],
              ["Recherche-Datenbanken", "PatBase, Espacenet, Derwent, Anaqua"],
              ["Berichts-Stand", "31. Maerz 2023"]]),
            ("3. Methodik der Recherche",
             f"Die FTO-Analyse erfolgte in vier Stufen: (1) Patentlandschafts-"
             f"recherche im technologischen Umfeld {technik}, (2) "
             f"Konkurrenten-Patent-Mapping (Continental, Bosch, ZF, Aptiv, "
             f"Mobileye, Magna, Veoneer), (3) Detail-Analyse der relevanten "
             f"Patentfamilien gegen die konkrete Produkt-Spezifikation, "
             f"(4) Risikobewertung und Massnahmenempfehlung. Die Recherche "
             f"wurde durch Patentanwaltskanzlei Maiwald durchgefuehrt; die "
             f"Auswertung intern durch das IP-Team der {R['name']} unter "
             f"Leitung von Dr. Florian Maier (IP-Manager)."),
            ("4. Identifizierte relevante Patente Dritter",
             [["Patent-Nr.", "Inhaber", "Bezug zu " + produkt, "Risiko", "Empfehlung"],
              ["EP 3 421 218 B1", "Continental AG", "Sensor-Fusion ADAS", "GERING",
               "Eigenes Patent Nr. 02 grenzt sauber ab"],
              ["DE 10 2018 213 547 A1", "ZF Friedrichshafen", "Powertrain-Algorithmik", "GERING",
               "Nicht relevant fuer " + produkt],
              ["US 11/234,567 B2", "Aptiv Technologies", "Radar-Architektur", "MITTEL",
               "Cross-Licensing-Pruefung empfohlen"],
              ["WO 2019/118432 A1", "Mobileye", "Vision-Algorithmus", "MITTEL",
               "Designaround-Pruefung erforderlich"],
              ["CN 109283456 A", "Huawei Tech.", "5G/V2X-Kommunikation", "GERING",
               "Nicht im aktuellen Funktionsumfang"],
              ["JP 2020-123456 A", "Denso Corp.", "BMS-Algorithmik", "GERING",
               "Eigenes Patent Nr. 03 abgrenzbar"]]),
            ("5. Risikobewertung und Massnahmen",
             f"Im Ergebnis der Detail-Analyse werden folgende Massnahmen "
             f"empfohlen: (a) Cross-Licensing-Gespraeche mit Aptiv Technologies "
             f"zum US 11/234,567 B2 (Verantwortlich: Stefan Richter / Dr. "
             f"Hollmann), (b) Designaround-Pruefung des Mobileye-Vision-"
             f"Algorithmus durch RSG Muenchen (Dr. Brodbeck), (c) "
             f"vorsorgliche Anmeldung eigener Defensiv-Patente in den "
             f"identifizierten Luecken, (d) Aufnahme der Themen in die "
             f"halbjaehrliche Patent-Strategie-Sitzung des IP-Komitees."),
            ("6. Vertraulichkeit und Haftung",
             f"Diese FTO-Analyse ist streng vertraulich (Klassifizierung: "
             f"VERTRAULICH / CONFIDENTIAL) und ausschliesslich fuer den "
             f"internen Gebrauch der {R['name']} sowie ihrer "
             f"Patentanwaltskanzleien bestimmt. Eine Weitergabe an Dritte "
             f"– insbesondere an {kunden_voll} – bedarf der ausdruecklichen "
             f"Genehmigung des Vorstands (CEO / CTO). Die Analyse stellt "
             f"keine endgueltige Rechtsberatung dar; die Verantwortung fuer "
             f"die kommerzielle Umsetzung verbleibt bei der "
             f"{R['name']}."),
        ])
    return fn


# ── REA spezielle Dokumente ───────────────────────────────────────────────
def rea_technologielizenz(kunde, jahr):
    kunde_voll = {"BMW": "BMW Group", "VW": "Volkswagen AG", "MBZ": "Mercedes-Benz AG"}[kunde]
    fn = BASE / f"REA_{kunde}_Technologielizenz_{jahr}.docx"
    if not fn.exists(): return None

    write_doc(str(fn), H,
        f"Technologielizenzvertrag {R['name']} / {kunde_voll}",
        subtitle=f"Out-Licensing-Vereinbarung, Stand {jahr}",
        confidential=True,
        sections=[
            ("1. Vertragsparteien",
             f"Zwischen der {R['name']}, Vaihinger Strasse 120, 70567 "
             f"Stuttgart, eingetragen im Handelsregister des Amtsgerichts "
             f"Stuttgart unter HRB 726451 (»Lizenzgeber«), vertreten durch "
             f"den Vorstand Anna Mueller (CEO) und Stefan Hoffmann (CTO bis "
             f"30.06.2024), und {kunde_voll} (»Lizenznehmer«) wird die "
             f"folgende Technologielizenzvereinbarung geschlossen."),
            ("2. Vertragsgegenstand und Lizenzumfang",
             ("clauses", [
                ("§ 1 Vertragsgegenstand", [
                    f"Gegenstand dieses Vertrages ist die Erteilung einer "
                    f"nicht-exklusiven, weltweiten und unterlizenzierbaren "
                    f"Lizenz an den im Anhang 1 aufgefuehrten Patenten und "
                    f"Patentanmeldungen der {R['name']} (»Lizenzpatente«) sowie "
                    f"an den dazugehoerigen technischen Know-how-Paketen "
                    f"(»Lizenz-Know-how«).",
                    f"Die Lizenzpatente umfassen insbesondere die Patentfamilien "
                    f"Nr. 02 (Kamerasystem mit 4D-Radarfusion), Nr. 06 "
                    f"(Selbstkalibrierendes Sensorsystem), Nr. 09 (Spurwechsel-"
                    f"Detektion) sowie Nr. 17 (Praediktiver Bremseingriff) "
                    f"einschliesslich aller Folgeanmeldungen und Erweiterungen."
                ]),
                ("§ 2 Lizenzumfang", [
                    "Der Lizenznehmer erhaelt das Recht, die Lizenzpatente und "
                    "das Lizenz-Know-how zur Entwicklung, Herstellung und Vermarktung "
                    "eigener ADAS-Systeme einzusetzen.",
                    "Eine Weitergabe an Tier-2-/Tier-3-Lieferanten ist mit "
                    "schriftlicher Zustimmung des Lizenzgebers zulaessig."
                ]),
                ("§ 3 Laufzeit", [
                    f"Der Vertrag tritt am 01. Januar {jahr} in Kraft und laeuft "
                    f"bis zum Ablauf des letzten zur Lizenz gehoerenden Patents "
                    f"(voraussichtlich 15.03.2042). Eine vorzeitige Beendigung "
                    f"ist nur aus wichtigem Grund moeglich."
                ]),
             ])),
            ("3. Verguetung und Royalties",
             [["Komponente", "Betrag / Hoehe", "Faelligkeit"],
              ["Einmalige Eintrittsgebuehr", "8.500.000 EUR netto", f"30.01.{jahr}"],
              ["Royalty laufend (pro Stueck)", "1,25 EUR / Steuergeraet", "Quartalsweise nachgelagert"],
              ["Mindest-Royalty p.a.", "3.500.000 EUR netto", f"31.01.{jahr+1} ff."],
              ["Royalty-Reporting", "Quartalsbericht binnen 45 Tagen", "Selbstdeklaration"],
              ["Audit-Recht Lizenzgeber", "1x pro Jahr (KPMG)", "Pruefung der Reporting-Daten"]]),
            ("4. Schutzrechtsverwaltung und Streitfall",
             f"Die {R['name']} verwaltet die Lizenzpatente weiterhin selbst "
             f"(Aufrechterhaltung, Jahresgebuehren, Verteidigung gegen "
             f"Einsprueche). Im Fall einer Patentverletzung durch Dritte "
             f"hat der Lizenzgeber das primaere Klagerecht; der Lizenznehmer "
             f"unterstuetzt bei Bedarf und kann sich an der Durchsetzung "
             f"beteiligen. Im Falle eines Streitfalls zwischen den Parteien "
             f"ist Gerichtsstand Frankfurt am Main; anwendbares Recht ist "
             f"deutsches Recht (BGB / PatG)."),
            ("5. Vertraulichkeit und Wettbewerbsverbot",
             f"Saemtliche im Rahmen dieses Vertrages ausgetauschten "
             f"Informationen unterliegen einer strengen Vertraulichkeit "
             f"(15 Jahre nach Vertragsende). Das Lizenz-Know-how und die "
             f"technischen Spezifikationen sind ausschliesslich fuer den "
             f"vertraglich vereinbarten Zweck zu verwenden. Der Lizenznehmer "
             f"verpflichtet sich, keine eigenen Erfindungen, die auf dem "
             f"Lizenz-Know-how aufbauen, ohne Abstimmung mit der "
             f"{R['name']} zum Patent anzumelden (Grant-Back-Klausel)."),
            ("6. Unterschriften",
             signatures("Anna Mueller", "CEO", R["name"],
                        f"i.A. {kunde_voll}-Beschaffung", "Bevollmaechtigter", kunde_voll,
                        place="Stuttgart", date_str_=f"15. Februar {jahr}")),
        ])
    return fn


def rea_bmw_jda():
    fn = BASE / "REA_BMW_JDA_ADAS_2022.docx"
    if not fn.exists(): return None

    write_doc(str(fn), H,
        "Joint Development Agreement (JDA) {R} und BMW Group ADAS",
        subtitle="Gemeinsame Entwicklungsvereinbarung ADAS-Plattform, Stand 2022",
        confidential=True,
        sections=[
            ("1. Vertragsparteien und Vertragsgegenstand",
             f"Zwischen der {R['name']} (»REA«) und der BMW AG, Petuelring 130, "
             f"80809 Muenchen (»BMW«) wird das vorliegende Joint Development "
             f"Agreement (JDA) zur gemeinsamen Entwicklung einer ADAS-Sensor-"
             f"Fusion-Plattform geschlossen. Das Projekt traegt den internen "
             f"Code »Project Pegasus« und umfasst die gemeinsame Entwicklung "
             f"des Steuergeraets, der Sensor-Fusion-Algorithmen sowie der "
             f"Validierungs-Strecke fuer Level-2+/Level-3-ADAS-Funktionen."),
            ("2. Projektorganisation",
             [["Funktion", "REA-Vertreter", "BMW-Vertreter"],
              ["Sponsor", "Stefan Hoffmann (CTO)", "Frank Weber (VP Driving Experience)"],
              ["Project Lead", "Dr. Stefan Brodbeck (RSG)", "Dr. Karsten Heuer (BMW)"],
              ["Technical Lead", "Dr. Klaus Kessler (RSG)", "Dr. Andreas Reschka (BMW)"],
              ["IP Lead", "Dr. Florian Maier (REA)", "Mike Schoenberg (BMW Legal)"],
              ["Quality Lead", "Sabine Brand (REG)", "Dr. Helmut Wagner (BMW QM)"]]),
            ("3. IP-Verteilung (Background / Foreground)",
             ("clauses", [
                ("§ 1 Background-IP", [
                    "Jede Partei behaelt ihr vor Vertragsbeginn vorhandenes IP "
                    "(Background-IP) und gewaehrt der jeweils anderen Partei "
                    "eine nicht-exklusive, lizenzkostenfreie Nutzungslizenz "
                    "ausschliesslich zur Durchfuehrung des Projekts.",
                    "Hierzu zaehlen insbesondere die REA-Patente Nr. 02, 06, "
                    "09 und 17 sowie die BMW-Patente aus den Patentfamilien "
                    "EP 3 521 xxx (Selbst-Lokalisierung) und EP 3 712 xxx "
                    "(HMI Driver Monitoring)."
                ]),
                ("§ 2 Foreground-IP", [
                    "Im Projekt entstehende Erfindungen (Foreground-IP) werden "
                    "gemaess Beitragsanteil aufgeteilt:",
                    "Erfindungen der Hardware-Architektur und der HMI-Komponenten "
                    "gehoeren BMW.",
                    "Erfindungen im Bereich Sensor-Fusion-Algorithmik und "
                    "Software-Plattform gehoeren der REA.",
                    "Gemischte Erfindungen werden als Co-Owned-IP angemeldet "
                    "und gegenseitig lizenzkostenfrei genutzt."
                ]),
                ("§ 3 Patentanmeldungen", [
                    "Patentanmeldungen erfolgen durch die jeweils "
                    "verantwortliche Partei in Abstimmung mit Maiwald "
                    "Patentanwaelte (REA-Seite) bzw. der BMW-Patentabteilung "
                    "(BMW-Seite). Bei Co-Owned-IP wird abwechselnd federfuehrend "
                    "angemeldet."
                ]),
             ])),
            ("4. Budget und Finanzierung",
             "Das Gesamtbudget belaeuft sich auf 28,5 Mio. EUR fuer die Vertragslaufzeit "
             "01.01.2022 bis 31.12.2024. BMW finanziert 60 % (17,1 Mio. EUR), "
             "REA finanziert 40 % (11,4 Mio. EUR). Die REA-eigenen Personalkosten "
             "werden auf Basis von Stundensaetzen abgerechnet (Senior Eng. "
             "145 EUR/h, Lead Eng. 175 EUR/h). Eine separate Reise- und "
             "Material-Position in Hoehe von 1,2 Mio. EUR ist im Budget enthalten."),
            ("5. Exklusivitaet und Wettbewerbsklausel",
             f"REA verpflichtet sich, die im Projekt entwickelten Foreground-"
             f"Komponenten waehrend einer Exklusivitaets-Periode von 18 Monaten "
             f"nach SOP des BMW-Serienprodukts (voraussichtlich Q3 2025) "
             f"ausschliesslich an BMW zu liefern. Nach Ablauf der "
             f"Exklusivitaet steht es REA frei, die Plattform an weitere "
             f"OEMs zu vermarkten. Eine Verkuerzung der Exklusivitaet ist "
             f"gegen eine Ausgleichszahlung moeglich."),
            ("6. Schlussbestimmungen",
             signatures("Stefan Hoffmann", "CTO", R["name"],
                        "Frank Weber", "VP Driving Experience", "BMW AG",
                        place="Muenchen", date_str_="14. Maerz 2022")),
        ])
    return fn


def rea_exportkontrolle():
    fn = BASE / "REA_Exportkontrollhandbuch_2023.docx"
    if not fn.exists(): return None
    write_doc(str(fn), H,
        "Exportkontroll-Handbuch der Brennhagen Elektronik AG",
        subtitle="Konzernrichtlinie zur Exportkontrolle, Stand 2023",
        sections=[
            ("1. Geltungsbereich und Ziel",
             f"Das vorliegende Exportkontroll-Handbuch der {R['name']} und "
             f"ihrer 100-prozentigen Tochtergesellschaften (REG, RSG, RPL, "
             f"RCZ, RHU, RCN, RHO) regelt die Einhaltung der nationalen, "
             f"europaeischen und internationalen Exportkontrollvorschriften "
             f"bei Lieferungen und Technologie-Transfers. Es konkretisiert "
             f"die gesetzlichen Anforderungen aus AWG / AWV (Deutschland), "
             f"EU-Dual-Use-Verordnung 2021/821, EAR (USA, sofern anwendbar) "
             f"und ITAR (USA, sofern Technologie US-Origin). Das Handbuch "
             f"ist fuer alle Mitarbeitenden weltweit verbindlich."),
            ("2. Organisation und Verantwortlichkeiten",
             [["Rolle", "Name", "Verantwortung"],
              ["Ausfuhrverantwortlicher Konzern", "Laura Bauer (CFO)", "Gesamtverantwortung gem. AWG"],
              ["Exportkontrollbeauftragter", "Dr. Christian Knapp (Compliance)",
               "Tagesgeschaeft / Klassifikation"],
              ["Stellv. EKB", "Anke Hartmann (Group Trade Comp.)", "Stellvertretung / EU"],
              ["EKB REG (Heilbronn)", "Andreas Maier (Werkleiter)", "Site-Verantwortung"],
              ["EKB RCN (Shanghai)", "Zhang Hao (Country Mgr)", "China-spezifisch / MOFCOM"]]),
            ("3. Klassifikation der Produkte",
             [["Produkt", "AL-Nr. (Anh. I AWV)", "ECCN (EAR)", "Dual-Use"],
              ["ICP-3 Infotainment", "nicht gelistet", "5A992", "Nein"],
              ["BMS-12 Batteriemanagement", "nicht gelistet", "EAR99", "Nein"],
              ["ADAS-V4D Radar Fusion", "6A008", "6A008", "JA (Kategorie 6 ML)"],
              ["ECU-900 Powertrain ECU", "nicht gelistet", "EAR99", "Nein"],
              ["LightCtrl-7", "nicht gelistet", "EAR99", "Nein"]]),
            ("4. Genehmigungspflichtige Geschaefte",
             ("list", [
                "Lieferungen des ADAS-V4D in Drittlaender ausserhalb EU sind "
                "BAFA-genehmigungspflichtig (Allgemeine Ausfuhrgenehmigung AGG-15 "
                "nutzbar fuer USA, JP, KR, AU).",
                "Lieferungen nach China (CN) und Russland (RU) unterliegen "
                "verschaerften Pruefungen; Russland-Exporte sind aktuell "
                "vollstaendig ausgesetzt (EU-Sanktionen 833/2014 ff.).",
                "Technologie-Transfer (Source-Code, Spezifikationen) ueber "
                "EU-Aussengrenzen erfordert vorherige Pruefung gemaess "
                "Anhang I EU-Dual-Use-VO.",
                "Embargo-Lander (Iran, Nordkorea, Syrien) sind ausgeschlossen.",
                "US-Personen-Restriktionen (Denied-Persons-List, SDN-List) "
                "sind ueber MK-Tool monatlich gegen Kundenstamm zu pruefen.",
             ])),
            ("5. Prozesse",
             f"Vor jeder Auftragsannahme erfolgt eine automatisierte Pruefung "
             f"in SAP GTS (Global Trade Services) gegen Sanktionslisten "
             f"sowie die Klassifikation der Ware/Technologie. Im Zweifelsfall "
             f"erfolgt eine manuelle Pruefung durch den Exportkontroll-"
             f"beauftragten (Dr. Christian Knapp). Bei genehmigungspflichtigen "
             f"Geschaeften ist eine Einzelausfuhrgenehmigung (E-AGG) beim "
             f"BAFA zu beantragen (Bearbeitungszeit i.d.R. 4-8 Wochen)."),
            ("6. Schulung und Audit",
             f"Alle Mitarbeitenden in Vertrieb, Einkauf, Versand und "
             f"Engineering durchlaufen jaehrlich ein verpflichtendes "
             f"Exportkontroll-E-Learning. Externe Audits durch KPMG (im "
             f"Rahmen der Jahresabschlusspruefung) erfolgen jaehrlich. Bei "
             f"Verstoessen drohen empfindliche Bussgelder (bis 500.000 EUR "
             f"je Einzelfall) sowie strafrechtliche Konsequenzen "
             f"(§§ 17, 18 AWG)."),
        ])
    return fn


def rea_mbz_rfq():
    fn = BASE / "REA_MBZ_ADAS-V4D_RFQ_Response_2022.docx"
    if not fn.exists(): return None
    write_doc(str(fn), H,
        "RFQ-Antwort Mercedes-Benz – ADAS-V4D Radar-Fusion",
        subtitle="Angebot zur Lieferung ADAS-V4D fuer Mercedes-Benz EQS / EQE / S-Klasse, Stand 2022",
        confidential=True,
        sections=[
            ("1. Empfaenger und Bezug",
             "An: Mercedes-Benz AG, Einkauf Elektronik, Herr Dr. Carsten "
             "Breitfeld (Senior Buyer), Mercedesstrasse 137, 70327 Stuttgart. "
             "Bezug: RFQ Nr. MB-RFQ-22-0847 vom 14.04.2022 betreffend "
             "Lieferung ADAS Radar-Fusion-Steuergeraet (Stuecklistennr. "
             "A1670500715) fuer die Modellfamilien EQS (V297), EQE (V295) "
             "und S-Klasse Facelift (W223 MOPF)."),
            ("2. Angebot - Produkt und Spezifikation",
             [["Feld", "Inhalt"],
              ["Produkt", "ADAS-V4D Radar-Fusion-Steuergeraet"],
              ["Variante", "MBZ-spezifisch (V297/V295/W223)"],
              ["Anlauf-/SOP-Termin", "Q2 2024 (EQS), Q3 2024 (EQE), Q4 2024 (W223)"],
              ["Geplanter Jahresvolumen-Mix", "EQS 38k; EQE 52k; S-Klasse 28k = 118k p.a."],
              ["Stueckpreis (Plan)", "412,50 EUR netto (CIP Sindelfingen)"],
              ["Werkzeugkostenanteil (NRE)", "4,2 Mio. EUR einmalig"],
              ["Vertragslaufzeit", "6 Jahre (Lifetime Build)"],
              ["Quality Target", "PPM < 5 (Field)"],
              ["Funktionssicherheit", "ASIL-D (ISO 26262)"]]),
            ("3. Technische Erfuellung der Anforderungen",
             "Das angebotene ADAS-V4D-Steuergeraet erfuellt die im RFQ-Lastenheft "
             "MB-LASTENHEFT-ADAS-V4D-V1.2 spezifizierten Anforderungen vollumfaenglich. "
             "Insbesondere werden die folgenden Schluessel-Anforderungen "
             "erfuellt: 4D-Radar mit 77 GHz, 4-fach Kamera-Fusion, "
             "Latenz < 60 ms, Sensor-Fusion-Update-Rate 50 Hz, "
             "ASIL-D fuer Notbrems-Funktionen, ISO/SAE 21434 Cybersecurity, "
             "AUTOSAR Classic 4.3, Diagnose UDS / DoIP, OTA-faehig. Das "
             "Steuergeraet basiert auf den REA-Patenten Nr. 02 (Kamerasystem "
             "4D-Radarfusion), Nr. 06 (Selbstkalibrierendes Sensorsystem) "
             "und Nr. 09 (Spurwechsel-Detektion)."),
            ("4. Kommerzielle Konditionen",
             [["Position", "Wert", "Hinweis"],
              ["Stueckpreis EXW (incl. Software)", "412,50 EUR", "Eskalationsklausel CHF/USD"],
              ["Werkzeugkosten / NRE", "4,2 Mio. EUR", "Einmalig vor SOP"],
              ["Zahlungsziel", "60 Tage netto", "Mercedes-Benz Standard"],
              ["Waehrung", "EUR", "Hedging via Group Treasury"],
              ["Liefer-Incoterm", "CIP Sindelfingen", "Incoterms 2020"],
              ["Garantie / Gewaehrleistung", "60 Monate ab SOP", "Lifetime Build"],
              ["Preisstabilitaet", "24 Monate", "Material-Index-Klausel ab Mt. 25"]]),
            ("5. Risiken und Annahmen",
             "Das Angebot steht unter folgenden Vorbehalten: (a) Verfuegbarkeit "
             "Halbleiter (insb. Infineon Aurix TC397, Radarchip TI AWR2944) "
             "gemaess Allocation Q3 2022, (b) Konstanz der Rohstoffpreise +/- 8 %, "
             "(c) Bestaetigung der Validierungs-Anforderungen durch MBZ-Engineering "
             "bis 31.10.2022. Bei wesentlichen Aenderungen behaelt sich REA "
             "eine Preisanpassung vor. Vertragspartner ist die "
             f"{R['name']}; Liefer- und Produktionswerk ist REG Heilbronn "
             "(Mainstream) bzw. RSG Muenchen (Software)."),
            ("6. Anlagen und naechste Schritte",
             ("list", [
                "Anlage 1: Detail-Spezifikation ADAS-V4D MBZ-Variante (52 Seiten)",
                "Anlage 2: Kalkulationsblatt (vertraulich, separat uebermittelt)",
                "Anlage 3: Validierungs-/Pruefplan (EMV, Klima, FuSi)",
                "Anlage 4: Roadmap Software-Releases bis Lifetime End",
                "Anlage 5: Lieferkonditionen-Anhang (Logistik, IGM 30.09.2022)",
                "Naechste Schritte: Technische Klaerung 18.05., kaufm. Klaerung 25.05., "
                "Letter of Intent angestrebt bis 30.06.2022.",
             ])),
            ("7. Unterschrift",
             signatures("Stefan Richter", "CMO / BD", R["name"],
                        "Stefan Hoffmann", "CTO", R["name"],
                        place="Stuttgart", date_str_="06. Mai 2022")),
        ])
    return fn


def rea_opensource():
    fn = BASE / "REA_OpenSource_Compliance_Report_2023.docx"
    if not fn.exists(): return None
    write_doc(str(fn), H,
        "Open-Source-Compliance Report 2023",
        subtitle=f"Konzernbericht zu Open-Source-Software-Compliance, Stand 31.12.2023",
        sections=[
            ("1. Zusammenfassung",
             f"Im Berichtsjahr 2023 hat die {R['name']} ihre Open-Source-"
             f"Compliance-Strategie weiter ausgebaut und konsolidiert. Es "
             f"sind in den Produkten ICP-3, ADAS-V4D, BMS-12, ECU-900 und "
             f"LightCtrl-7 insgesamt 1.847 Open-Source-Komponenten "
             f"identifiziert (+ 12 % ggue. Vorjahr). 100 % der Komponenten "
             f"sind im konzernweiten SBOM-Repository (Software Bill of "
             f"Materials, Tool: WhiteSource Mend) verzeichnet. Die "
             f"Compliance-Quote betraegt 98,7 % (Vorjahr 96,2 %)."),
            ("2. Organisation",
             [["Rolle", "Name", "Verantwortung"],
              ["Konzern-OSS-Officer", "Lars Wittmann (RSG)", "Strategie / OSPO-Leitung"],
              ["OSS-Tool-Owner", "Maximilian Knecht (RSG)", "WhiteSource / SBOM"],
              ["Legal-Lead OSS", "Sarah Bittner (Konzernrecht)", "Lizenz-Pruefung"],
              ["Engineering-Lead", "Dr. Klaus Kessler (RSG)", "Embedded-Stack"],
              ["Audit-Lead", "Andreas Buehler (Internal Audit)", "Quartals-Audit"]]),
            ("3. Lizenz-Verteilung (Top-10)",
             [["Lizenz", "Anzahl Komponenten", "Anteil", "Kritikalitaet"],
              ["MIT", "642", "34,8 %", "GERING"],
              ["Apache-2.0", "489", "26,5 %", "GERING"],
              ["BSD-3-Clause", "238", "12,9 %", "GERING"],
              ["LGPL-2.1", "187", "10,1 %", "MITTEL (dynamic linking ok)"],
              ["GPL-2.0", "98", "5,3 %", "HOCH (nur Kernel/Bootloader)"],
              ["MPL-2.0", "67", "3,6 %", "MITTEL"],
              ["EPL-2.0", "45", "2,4 %", "MITTEL"],
              ["GPL-3.0", "32", "1,7 %", "HOCH (vermeiden in Linkage)"],
              ["ISC", "28", "1,5 %", "GERING"],
              ["zlib", "21", "1,1 %", "GERING"]]),
            ("4. Kritische Befunde 2023 und Massnahmen",
             ("list", [
                "ICP-3, Build 22.4: GPL-3.0-Komponente 'libgnu' im OEM-Build "
                "verlinkt. Massnahme: Replacement durch MIT-lizenzierte "
                "Alternative, Abschluss Q4/2023. Status: GESCHLOSSEN.",
                "ADAS-V4D: 14 Komponenten mit unklarer Lizenz (»UNKNOWN«). "
                "Massnahme: manuelle Pruefung durch Legal abgeschlossen, "
                "alle 14 nun korrekt klassifiziert. Status: GESCHLOSSEN.",
                "BMS-12: CVE-2023-21345 in OpenSSL 3.0 identifiziert. "
                "Massnahme: Upgrade auf 3.0.12 in Software-Release SW-R-23.4. "
                "Status: GESCHLOSSEN.",
                "RSG-Tooling: 7 Entwicklerstationen ohne SBOM-Scan-Hook. "
                "Massnahme: Verpflichtende Integration in Pre-Commit-Hook. "
                "Status: GESCHLOSSEN.",
                "Source-Code-Escrow BMW (siehe REA_Source_Code_Escrow_BMW_2022): "
                "Lizenz-Manifest aktualisiert auf Stand 2023-Q4. Status: OFFEN.",
             ])),
            ("5. Ausblick 2024",
             f"Fuer 2024 sind folgende Massnahmen geplant: (a) Migration "
             f"von WhiteSource Mend auf Black Duck (Synopsys), (b) "
             f"Einfuehrung eines konzernweiten OSS-Policy-Trainings (verpflichtend "
             f"fuer alle Software-Engineers), (c) Beitritt zur SPDX-Initiative "
             f"und Veroeffentlichung eigener SBOMs in SPDX-Format gegenueber "
             f"OEM-Kunden, (d) Vorbereitung auf Cyber Resilience Act (CRA) "
             f"der EU. Verantwortlich: Lars Wittmann (OSS-Officer, RSG)."),
        ])
    return fn


def rea_source_escrow():
    fn = BASE / "REA_Source_Code_Escrow_BMW_2022_DRAFT.docx"
    if not fn.exists(): return None
    write_doc(str(fn), H,
        "Source-Code-Escrow-Vereinbarung REA / BMW (ENTWURF)",
        subtitle="Hinterlegungsvereinbarung Source-Code ICP-3 und ADAS-V4D, Entwurf 2022",
        draft=True,
        confidential=True,
        sections=[
            ("1. Vertragsparteien und Vertragsgegenstand",
             f"Zwischen der {R['name']} (»REA«, Hinterleger), der BMW AG "
             f"(»BMW«, Beguenstigter) und der NCC Group GmbH, Lyoner Strasse "
             f"15, 60528 Frankfurt am Main (»Hinterlegungsstelle«, Escrow-"
             f"Agent) wird die vorliegende Source-Code-Escrow-Vereinbarung "
             f"als Anlage zum Liefer- und Entwicklungsvertrag REA/BMW 2022 "
             f"geschlossen. Vertragsgegenstand ist die Hinterlegung des "
             f"Source-Codes der Produkte ICP-3 (Infotainment) und ADAS-V4D "
             f"(Radar-Fusion) bei der Hinterlegungsstelle zur Sicherstellung "
             f"der BMW-Geschaeftskontinuitaet im Insolvenzfall der REA."),
            ("2. Hinterlegungs-Scope",
             [["Komponente", "Format", "Update-Zyklus", "Volumen"],
              ["ICP-3 Source-Code (C/C++/Java/Kotlin)", "Git-Bundle, AES-256",
               "vierteljaehrlich", "ca. 12 GB"],
              ["ADAS-V4D Source-Code (C/C++/MATLAB)", "Git-Bundle, AES-256",
               "vierteljaehrlich", "ca. 8 GB"],
              ["Build-Toolchain Dokumentation", "PDF / DOCX",
               "halbjaehrlich", "ca. 800 MB"],
              ["Lizenz-Manifest (SBOM SPDX 2.3)", "JSON / SPDX",
               "vierteljaehrlich", "ca. 50 MB"],
              ["Entwickler-Dokumentation", "Confluence-Export", "vierteljaehrlich", "ca. 2 GB"]]),
            ("3. Release-Conditions (Auslieferungsbedingungen)",
             ("clauses", [
                ("§ 1 Trigger-Events", [
                    "Die Hinterlegungsstelle gibt den Source-Code an BMW frei, "
                    "sofern eines der folgenden Ereignisse eintritt:",
                    "(a) Insolvenz der REA (Eroeffnung Insolvenzverfahren),",
                    "(b) Liquidation der REA ohne Rechtsnachfolger,",
                    "(c) wesentliche, dauerhafte Verletzung der Wartungspflicht "
                    "durch REA (Heilungsfrist 60 Tage)."
                ]),
                ("§ 2 Verifikationsverfahren", [
                    "Die Hinterlegungsstelle verifiziert beim Eingang jeder "
                    "Lieferung die Integritaet (SHA-256-Hash) und vollstaendige "
                    "Buildbarkeit gemaess REA-Build-Anleitung."
                ]),
                ("§ 3 Nutzungsrechte im Release-Fall", [
                    "Im Release-Fall erhaelt BMW eine nicht-exklusive, "
                    "zeitlich unbeschraenkte Nutzungslizenz am Source-Code "
                    "zum Zweck der Wartung und Weiterentwicklung der bei BMW "
                    "im Einsatz befindlichen Steuergeraete (»End-of-Life "
                    "Support«). Eine kommerzielle Vermarktung an Dritte ist "
                    "ausgeschlossen."
                ]),
             ])),
            ("4. Kosten",
             [["Position", "Betrag p.a.", "Hinweis"],
              ["Hinterlegungs-Grundgebuehr NCC", "12.500 EUR", "Pauschal p.a."],
              ["Verifikations-Gebuehr je Update", "1.800 EUR", "4x p.a."],
              ["Audit-Gebuehr (auf Wunsch BMW)", "5.500 EUR", "1x p.a. moeglich"],
              ["Gesamt p.a.", "ca. 25.200 EUR", "Aufteilung 50/50"]]),
            ("5. Status und naechste Schritte",
             "Dieser Vertrag liegt derzeit als ENTWURF vor (Stand 11/2022). "
             "Folgende Punkte sind noch zu klaeren: (a) Endfassung der "
             "Verifikations-Spezifikation (BMW Legal + REA Engineering), "
             "(b) Nachweis der NCC-Group-Zertifizierungen (ISO 27001, "
             "BSI C5), (c) finaler Hinterlegungs-Zeitplan (Erstlieferung "
             "geplant Q1 2023), (d) Abstimmung mit Lieferantenrahmen-"
             "Vertrag REA/BMW (Annex 17). Verantwortlich REA-Seite: "
             "Dr. Florian Maier (IP-Manager); BMW-Seite: Mike Schoenberg "
             "(BMW Legal)."),
        ])
    return fn


def prj_testbericht_2021_002():
    fn = BASE / "PRJ-2021-002_Testbericht_Lebensdauertest_ADAS-V4D_Kalibrierun.docx"
    if not fn.exists(): return None
    write_doc(str(fn), H,
        "Testbericht – Lebensdauertest ADAS-V4D Kalibrierungsplattform",
        subtitle="PRJ-2021-002, Lebensdauertest gem. LV124, Stand 2023",
        sections=[
            ("1. Pruefdaten",
             [["Feld", "Inhalt"],
              ["Projekt", "PRJ-2021-002 ADAS-V4D Kalibrierungsplattform"],
              ["Pruefling", "ADAS-V4D Radar-Fusion Steuergeraet (Engineering Sample E3)"],
              ["Pruefnorm", "LV124-2 (Allgemeine Anforderungen)"],
              ["Pruefdauer", "1.000 h aktiv + 500 h Idle"],
              ["Pruefumgebung", "Klimakammer ESPEC Walk-In, RSG Muenchen"],
              ["Pruefbeginn", "15. Februar 2023"],
              ["Pruefende", "30. April 2023"],
              ["Pruefleiter", "Dr. Stefan Brodbeck (RSG)"],
              ["Pruefbericht-Nr.", "TR-PRJ-2021-002-LDT-001"]]),
            ("2. Pruefumfang und Pruefbedingungen",
             "Der Pruefling wurde unter folgenden Lebensdauer-Bedingungen "
             "betrieben: Temperaturzyklen -40 degC bis +85 degC gemaess "
             "LV124-2 K-04 (1000 Zyklen mit je 30 min Verweilzeit), "
             "Vibrationsprofil gemaess LV124-2 M-03 (3-Achsen, 30 h "
             "kumuliert), Feuchte-Hitze gemaess LV124-2 K-09 (85 degC / "
             "85 % rF, 504 h), elektrische Belastung gemaess Lastenheft "
             "Mercedes-Benz V4D-LH-V1.2 (Voltschwankung 8,5 V - 16 V, "
             "Lastsprung-Tests). Alle Pruefungen erfolgten am Standort "
             "RSG Muenchen in Kooperation mit IABG."),
            ("3. Pruefergebnisse",
             [["Pruefung", "Anforderung", "Messwert", "Bewertung"],
              ["Temperaturzyklen", "ohne Funktionsausfall", "0 Ausfaelle in 1000 Zyklen", "BESTANDEN"],
              ["Vibration 3-Achsen", "kein mech. Bruch", "Visuelle Pruefung o.B.", "BESTANDEN"],
              ["Feuchte-Hitze", "Isolations-R > 100 MOhm", "228 MOhm gemessen", "BESTANDEN"],
              ["Spannungs-Schwankung", "Funktion 8.5 - 16 V", "Funktion 8.0 - 16.5 V", "BESTANDEN"],
              ["EMV-Pruefung", "CISPR 25 Klasse 5", "Klasse 5 eingehalten", "BESTANDEN"],
              ["ESD-Pruefung", "ISO 10605 Stufe IV", "Stufe IV eingehalten", "BESTANDEN"],
              ["Funktionsausfall-Rate", "< 5 ppm", "0 ppm gemessen (Sample 3 St.)", "BESTANDEN"]]),
            ("4. Bewertung und Freigabeempfehlung",
             "Der Pruefling ADAS-V4D Engineering Sample E3 erfuellt alle "
             "Anforderungen des Lastenhefts Mercedes-Benz V4D-LH-V1.2 sowie "
             "der LV124-2. Die Funktionssicherheit nach ISO 26262 ASIL-D "
             "bleibt ueber die gesamte Pruefdauer erhalten. Es wird empfohlen, "
             "die Engineering Sample-Charge E3 als Basis fuer die "
             "anschliessende Validierungs-Phase und PPAP-Vorbereitung "
             "freizugeben."),
            ("5. Unterschriften",
             signatures("Dr. Stefan Brodbeck", "Pruefleiter / RSG", R["name"],
                        "Dr. Klaus Kessler", "Q-Lead RSG", R["name"],
                        place="Muenchen", date_str_="05. Mai 2023")),
        ])
    return fn


# ── MAIN ──────────────────────────────────────────────────────────────────
def main():
    written = []
    # Patentschriften 01-15
    for nr in ["01", "02", "03", "04", "05", "06", "07", "08",
               "09", "10", "11", "12", "13", "14", "15"]:
        p = patentschrift(nr)
        if p: written.append(p)

    # Bescheid EPA — alle 18 (mit jahr aus PATENTS)
    for nr, info in PATENTS.items():
        anm_jahr = info[7]
        # Bescheid jahre koennten variieren; nutze BASE.glob
        for m in BASE.glob(f"Patent_{nr}_Bescheid_EPA_*.docx"):
            # extract year
            parts = m.stem.split("_")
            jahr = int([p for p in parts if p.isdigit() and len(p) == 4][0])
            p = bescheid_epa(nr, jahr)
            if p: written.append(p)

    # Antwort Anmelder
    for nr in PATENTS:
        for m in BASE.glob(f"Patent_{nr}_Antwort_Anmelder_*.docx"):
            parts = m.stem.split("_")
            jahr = int([p for p in parts if p.isdigit() and len(p) == 4][0])
            p = antwort_anmelder(nr, jahr)
            if p: written.append(p)

    # Erteilungsurkunde
    for nr in PATENTS:
        for m in BASE.glob(f"Patent_{nr}_Erteilungsurkunde_*.docx"):
            parts = m.stem.split("_")
            jahr = int([p for p in parts if p.isdigit() and len(p) == 4][0])
            p = erteilungsurkunde(nr, jahr)
            if p: written.append(p)

    # Jahresgebuehr
    for nr in PATENTS:
        for m in BASE.glob(f"Patent_{nr}_Jahresgebuehr_*.docx"):
            parts = m.stem.split("_")
            jahr = int([p for p in parts if p.isdigit() and len(p) == 4][0])
            p = jahresgebuehr(nr, jahr)
            if p: written.append(p)

    # ECOs
    for m in BASE.glob("ECO_*_Engineering_Change_*.docx"):
        parts = m.stem.split("_")
        produkt = parts[1]
        nr = int(parts[2])
        # extract first 4-digit year token after "Change"
        years = [int(p) for p in parts if p.isdigit() and len(p) == 4]
        jahr = years[0] if years else 2023
        p = eco(produkt, nr, jahr, fn=m)
        if p: written.append(p)

    # FTOs
    for m in BASE.glob("FTO_*_*_2023.docx"):
        parts = m.stem.split("_")
        produkt = parts[1]; kunde = parts[2]
        p = fto(produkt, kunde)
        if p: written.append(p)

    # REA spezielle
    written.append(rea_technologielizenz("BMW", 2021))
    written.append(rea_technologielizenz("VW", 2021))
    written.append(rea_bmw_jda())
    written.append(rea_exportkontrolle())
    written.append(rea_mbz_rfq())
    written.append(rea_opensource())
    written.append(rea_source_escrow())
    written.append(prj_testbericht_2021_002())

    written = [w for w in written if w]
    print(f"Wrote {len(written)} docs.")


if __name__ == "__main__":
    main()
