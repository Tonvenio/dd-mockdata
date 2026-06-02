"""Brennhagen AG / 23_Projekte_Programme – Monatliche Status-/Statusberichte.
~267 docs (Status_YYYY_MM_... and Statusbericht_YYYY_MM_...).

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
import re
import sys
from pathlib import Path
sys.path.insert(0, f"{_ROOT}")
from enhance_lib import ROEHRIG_AG as R, write_doc, signatures

BASE = Path(f"{_ROOT}/roehrig_large/23_Projekte_Programme")
H = {"name": R["name"], "addr": R["addr"], "hrb": R["hrb"]}


# Project metadata - mapping prj_id to (kurztitel, produkt, oem, leiter, sponsor)
PRJ_META = {
    "PRJ-2021-001": ("ECU-900 Gen3 Entwicklung", "ECU-900", "VW / Stellantis",
                     "Dipl.-Ing. Andreas Schultheiss (REG)", "Dr. Thomas Weber (COO)"),
    "PRJ-2021-002": ("ADAS-V4D Kalibrierungsplattform", "ADAS-V4D", "Mercedes-Benz",
                     "Dr. Stefan Brodbeck (RSG)", "Stefan Hoffmann (CTO bis 6/2024)"),
    "PRJ-2022-001": ("BatteryMS-12 EV Plattform", "BMS-12", "VW (ID.7) / Hyundai",
                     "Dr. Petra Hollmann (REG)", "Dr. Thomas Weber (COO)"),
    "PRJ-2022-002": ("InfoConnect Pro 4.0", "ICP-3", "BMW / Mercedes",
                     "Lars Wittmann (RSG)", "Stefan Hoffmann (CTO)"),
    "PRJ-2022-003": ("ECU-900 AUTOSAR Refactoring", "ECU-900", "VW",
                     "Marco Frey (RSG)", "Dr. Thomas Weber (COO)"),
    "PRJ-2023-001": ("ADAS-V4D Radar Fusion", "ADAS-V4D", "Mercedes-Benz / Stellantis",
                     "Dr. Stefan Brodbeck (RSG)", "Dr. Petra Hollmann (CTO)"),
    "PRJ-2023-002": ("BatteryMS-12 China Adaptation", "BMS-12", "CATL / Hyundai (CN)",
                     "Zhang Hao (RCN)", "Dr. Yuki Tanaka (CRO Asia)"),
    "PRJ-2023-003": ("ICP-3 OTA Update Platform", "ICP-3", "BMW / Mercedes",
                     "Lars Wittmann (RSG)", "Dr. Petra Hollmann (CTO)"),
    "PRJ-2023-004": ("Cost Reduction Program CZ", "RCZ Steckverbinder", "intern",
                     "Petr Novak (Werkleiter RCZ)", "Dr. Thomas Weber (COO)"),
    "PRJ-2023-005": ("Heilbronn Plant Expansion", "BMS-12 Linie 4", "intern",
                     "Andreas Maier (Werkleiter REG)", "Dr. Thomas Weber (COO)"),
    "PRJ-2024-001": ("ECU-1000 Concept Study", "ECU-1000", "VW / Stellantis (Konzept)",
                     "Marco Frey (RSG)", "Dr. Petra Hollmann (CTO)"),
    "PRJ-2024-002": ("DSGVO Compliance Remediation", "DSGVO/IT", "intern",
                     "Dr. Anna Brand (Konzern-DSB)", "Anna Mueller (CEO)"),
    "PRJ-2024-003": ("SAP S/4HANA Rollout Polen", "ERP/SAP", "intern RPL",
                     "Marek Wojciechowski (RPL)", "Laura Bauer (CFO)"),
    "PRJ-2024-004": ("LkSG Supply Chain Audit", "Lieferketten-Compliance", "intern",
                     "Dr. Klaudia Hoffmann (Compliance)", "Stefan Richter (CMO/BD)"),
    "PRJ-2024-005": ("Cybersecurity TISAX Level 3", "Cybersecurity", "intern",
                     "Andreas Buehler (CAE)", "Dr. Petra Hollmann (CTO)"),
}

MONATSNAMEN = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni",
               "Juli", "August", "September", "Oktober", "November", "Dezember"]


def _status_ampel(month, year, pid):
    """Deterministic-but-varying ampel pseudo-pattern."""
    # Use month and last digit of pid for deterministic variation
    h = (month + year + int(pid[-1])) % 5
    if h == 0:
        return ("GRUEN", "GRUEN", "GRUEN", "Termin- und Budget-konform; keine kritischen Risiken offen.")
    if h == 1:
        return ("GELB", "GRUEN", "GRUEN", "Termintreue mit leichter Verzoegerung; Massnahmen wirken.")
    if h == 2:
        return ("GRUEN", "GELB", "GRUEN", "Budget-Forecast +3 % – Steuerungsmassnahmen eingeleitet.")
    if h == 3:
        return ("GRUEN", "GRUEN", "GELB", "Qualitaets-Issue B-Muster identifiziert; Hotfix in Validierung.")
    return ("GRUEN", "GRUEN", "GRUEN", "Stabil im Plan.")


def _content_blocks(pid, kt, produkt, oem, month, year, leiter, sponsor):
    a_t, a_b, a_q, ampel_note = _status_ampel(month, year, pid)
    monat_str = MONATSNAMEN[month - 1]

    # Pick rotating progress topics
    rot = (month + year) % 6
    if rot == 0:
        fortschritt = [
            "Architektur-Review mit Vector und dSpace abgeschlossen.",
            "B-Muster-Fertigung in REG Heilbronn angelaufen (12/15 Samples).",
            "HiL-Pruefstand RSG Muenchen mit aktualisierter FW geflasht.",
            "Lieferanten-Onboarding Aurix (Infineon Distributor Avnet) bestaetigt.",
        ]
    elif rot == 1:
        fortschritt = [
            "Code-Review-Quote auf 92 % gesteigert (Ziel 90 %).",
            "Erste EMV-Pre-Test-Reihe im REA-Labor abgeschlossen (PASS).",
            "OEM-Workshop in Wolfsburg / Stuttgart durchgefuehrt (3 Tage).",
            "Aenderungen aus Change-Board CCB-2023-04 eingearbeitet.",
        ]
    elif rot == 2:
        fortschritt = [
            "Detaildesign FuSi (ASIL-D) abgeschlossen; Review-Workshop nachgelagert.",
            "RTM-Coverage auf 98 % der DOORS-Anforderungen.",
            "Cyber-Security-Audit (intern, TISAX-Vorbereitung) ohne Major-Findings.",
            "Personalaufbau +2 Engineers (Senior/Mid) erfolgreich.",
        ]
    elif rot == 3:
        fortschritt = [
            "Validierungs-Kampagne Kalt-/Warm-Test gestartet.",
            "PPAP-Vorbereitung Level 3 mit Q-Team REG abgestimmt.",
            "AUTOSAR-Upgrade auf R20-11 in Integration getestet.",
            "OEM-spezifische Diagnose-Spezifikation (UDS-Layer) eingefroren.",
        ]
    elif rot == 4:
        fortschritt = [
            "Software-Release Candidate v0.9 an OEM ausgeliefert.",
            "Bug-Fix-Rate aus letzter Iteration: 38 Defects, 35 geschlossen.",
            "Doku-Pakete fuer Gate-Review vorbereitet (RTM, FMEA, Q-Plan).",
            "Lieferanten-Audit (VDA 6.3) bei Tier-2-Lieferant abgeschlossen.",
        ]
    else:
        fortschritt = [
            "Erste Fahrzeug-Erprobung bei OEM (closed-area) erfolgreich.",
            "Integrations-Build #142 erfolgreich; CI/CD-Pipeline stabil.",
            "Werkleitung REG / RCZ informiert; Anlauf-Vorbereitung gestartet.",
            "Schulungs-Curriculum fuer Linien-MA erstellt (16 h pro Schicht).",
        ]

    rot2 = (month + int(pid[-2:])) % 4
    if rot2 == 0:
        themen_next = ["Abschluss Detaildesign-Phase", "Vorbereitung Gate-Review",
                       "Risiko-Workshop mit Lieferanten", "OEM-Statusupdate naechster Monat"]
    elif rot2 == 1:
        themen_next = ["B-Muster-Auslieferung an OEM", "Pruefraum-Belegung absichern",
                       "Software-Drop v1.0", "Personalplanung Folgequartal"]
    elif rot2 == 2:
        themen_next = ["EMV-Hauptpruefung", "PPAP-Einreichung",
                       "Cybersecurity-Penetration-Tests", "Schulung Linien-Mitarbeiter"]
    else:
        themen_next = ["Validierungs-Sign-Off", "Type-Approval-Antrag KBA",
                       "Production Readiness Review", "Lessons-Learned-Workshop"]

    risiken = [
        ["Halbleiter-Allocation (Aurix/SoC)", "Hoch", "Strategic-Sourcing Eskalation",
         "Group Purchasing"],
        ["OEM-Spec-Spaetaenderung", "Mittel", "CCB-Steuerung + Change-Control",
         "PMO"],
        ["Personalverfuegbarkeit Engineering", "Mittel", "Capacity-Planning RSG",
         "RSG Werkleitung"],
    ]

    return {
        "ampel": (a_t, a_b, a_q, ampel_note),
        "fortschritt": fortschritt,
        "themen_next": themen_next,
        "risiken": risiken,
        "monat_str": monat_str,
    }


def write_status(path, pid, kt, produkt, oem, leiter, sponsor, year, month, is_long=False):
    blocks = _content_blocks(pid, kt, produkt, oem, month, year, leiter, sponsor)
    a_t, a_b, a_q, ampel_note = blocks["ampel"]
    monat_str = blocks["monat_str"]

    title_prefix = "Statusbericht" if is_long else "Status"
    write_doc(str(path), H,
        f"{title_prefix} {monat_str} {year} – {pid}",
        subtitle=f"{kt} | Projekt-Statusbericht (monatlich)",
        sections=[
            ("1. Projekt-Identifikation",
             [["Feld", "Inhalt"],
              ["Projekt-ID", pid],
              ["Projekt-Titel", kt],
              ["Produktbezug", produkt],
              ["Hauptkunde / OEM", oem],
              ["Projektleitung", leiter],
              ["Projekt-Sponsor", sponsor],
              ["Berichtsmonat", f"{monat_str} {year}"],
              ["Erstellt am", f"05. {MONATSNAMEN[month % 12]} {year if month < 12 else year+1}"]]),
            ("2. Status-Ampel",
             [["Dimension", "Ampel", "Kommentar"],
              ["Termin", a_t, "Bezogen auf Gate-Soll-Termine"],
              ["Budget", a_b, "EAC vs. Genehmigtes Budget"],
              ["Qualitaet", a_q, "Defects, Test-Coverage, Q-KPIs"],
              ["Scope", "GRUEN", "Keine offenen Scope-Aenderungen"],
              ["Risiken", "GELB", "Drei Top-Risiken aktiv, Massnahmen wirksam"]]),
            ("3. Zusammenfassung",
             f"Das Projekt {pid} ({kt}) befindet sich im Berichtsmonat "
             f"{monat_str} {year} planmaessig in der laufenden Phase. {ampel_note} "
             f"Der Hauptkunde {oem} wurde im Rahmen der monatlichen OEM-Steuerung "
             f"informiert und hat den Berichtsstand zur Kenntnis genommen. Die "
             f"Lenkungsausschuss-Sitzung des laufenden Monats hat die "
             f"Massnahmen-Plaene zur Kenntnis genommen und keine Eskalation "
             f"ausgesprochen."),
            ("4. Fortschritt im Berichtsmonat",
             ("list", blocks["fortschritt"])),
            ("5. Top-3-Risiken",
             [["Risiko", "Bewertung", "Massnahme", "Owner"]] + blocks["risiken"]),
            ("6. Budget-/Termin-Forecast",
             "Der Budget-Forecast (EAC) liegt aktuell innerhalb der vom Vorstand "
             "genehmigten Toleranz von 5 %. Die Termin-Verzuege aus den vorausgegangenen "
             "Phasen wurden teilweise durch parallelisierte Validierung kompensiert. "
             "Der naechste Termin-Update erfolgt im Rahmen der monatlichen "
             "Lenkungsausschuss-Sitzung."),
            ("7. Themen / Plan fuer Folgemonat",
             ("list", blocks["themen_next"])),
            ("8. Unterschrift / Freigabe",
             signatures(leiter, "Projektleitung", R["name"],
                        sponsor.split("(")[0].strip(), "Projekt-Sponsor", R["name"],
                        place="Stuttgart",
                        date_str_=f"05. {MONATSNAMEN[month % 12]} {year if month < 12 else year+1}")),
        ])


def main():
    n = 0
    # Pattern A: PRJ-XXXX-YYY_Status_YYYY_MM_<kurz>.docx
    # Pattern B: PRJ-XXXX-YYY_Statusbericht_YYYY_MM_<kurz>.docx
    pat = re.compile(r"^(PRJ-\d{4}-\d{3})_(Status|Statusbericht)_(\d{4})_(\d{2})_.+\.docx$")
    for f in sorted(BASE.iterdir()):
        m = pat.match(f.name)
        if not m:
            continue
        pid, kind, year_s, month_s = m.group(1), m.group(2), m.group(3), m.group(4)
        if pid not in PRJ_META:
            continue
        kt, produkt, oem, leiter, sponsor = PRJ_META[pid]
        year = int(year_s)
        month = int(month_s)
        write_status(f, pid, kt, produkt, oem, leiter, sponsor, year, month,
                     is_long=(kind == "Statusbericht"))
        n += 1
    print(f"Status reports written: {n}")


if __name__ == "__main__":
    main()
