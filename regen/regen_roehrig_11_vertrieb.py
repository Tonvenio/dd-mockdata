"""Brennhagen AG / 11_Vertrieb_OEM – ~370 docs, heavily parameterised."""
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
import re
import time
from pathlib import Path

sys.path.insert(0, f"{_ROOT}")
from enhance_lib import ROEHRIG_AG as R, write_doc, signatures

BASE = Path(f"{_ROOT}/roehrig_large/11_Vertrieb_OEM")
H = {"name": R["name"], "addr": R["addr"], "hrb": R["hrb"]}

# ── OEM master data ────────────────────────────────────────────────────────
OEM = {
    "BMW": {
        "full": "BMW Group",
        "legal": "Bayerische Motoren Werke AG",
        "addr": "Petuelring 130, 80809 Muenchen",
        "kontakt": "Dr. Markus Heinz",
        "rolle": "Head of Purchasing Electronics",
        "kuerzel_intern": "BMW",
        "werk": "Werk Dingolfing / Werk Leipzig",
        "qmb": "Frau Stefanie Reiter",
        "sqe": "Herr Andreas Lechner",
    },
    "VW": {
        "full": "Volkswagen AG",
        "legal": "Volkswagen Aktiengesellschaft",
        "addr": "Berliner Ring 2, 38440 Wolfsburg",
        "kontakt": "Frau Petra Lindemann",
        "rolle": "Senior Buyer Electronics / E-Mobility",
        "kuerzel_intern": "VW",
        "werk": "Werk Zwickau / Werk Wolfsburg",
        "qmb": "Herr Dr. Klaus-Peter Schwarz",
        "sqe": "Frau Sabine Voigt",
    },
    "MBZ": {
        "full": "Mercedes-Benz Group AG",
        "legal": "Mercedes-Benz Group AG",
        "addr": "Mercedesstrasse 120, 70372 Stuttgart",
        "kontakt": "Herr Dr. Joachim Lessing",
        "rolle": "Director Procurement E/E Systems",
        "kuerzel_intern": "MBZ",
        "werk": "Werk Sindelfingen / Werk Bremen",
        "qmb": "Frau Marianne Erhardt",
        "sqe": "Herr Bernd Klotz",
    },
    "STE": {
        "full": "Stellantis N.V.",
        "legal": "Stellantis N.V. (vertreten durch FCA Italy S.p.A. und PSA Automobiles SAS)",
        "addr": "Singaporestraat 92-100, 1175 RA Lijnden, Niederlande",
        "kontakt": "Mme. Catherine Mercier",
        "rolle": "Global Commodity Manager Electronics",
        "kuerzel_intern": "STE",
        "werk": "Werk Mirafiori (Turin) / Werk Sochaux",
        "qmb": "Sig. Giuseppe Rossi",
        "sqe": "Herr Frank Witzel (Ruesselsheim)",
    },
    "CON": {
        "full": "Continental AG",
        "legal": "Continental Aktiengesellschaft",
        "addr": "Vahrenwalder Strasse 9, 30165 Hannover",
        "kontakt": "Herr Dr. Henning Brueggemann",
        "rolle": "Strategic Purchasing Lead (Tier-2 Programme)",
        "kuerzel_intern": "CON",
        "werk": "Werk Regensburg / Werk Babenhausen",
        "qmb": "Frau Annette Dreier",
        "sqe": "Herr Mehmet Yilmaz",
    },
}

PRODUKT = {
    "ICP-3": {
        "name": "InfoConnect Pro (ICP-3)",
        "beschr": "Infotainment-Modul mit Cockpit-Display-Controller (3 Displays, 1080p, ARM Cortex-A78)",
        "asil": "ASIL-B",
        "werk": "Brennhagen Elektronik GmbH (REG), Heilbronn – Linie 2/3",
        "anlauf_sop": "Q3 2023",
        "volumen_jahr": 170_000,
        "preis_eur": 412.50,
    },
    "BMS-12": {
        "name": "BatteryMS-12 (BMS-12)",
        "beschr": "Batteriemanagementsystem fuer 800-V-Plattformen (HV-Pack-Monitoring, 12 Zell-Module)",
        "asil": "ASIL-D",
        "werk": "Brennhagen Elektronik GmbH (REG), Heilbronn – Linie 4 (neu, SOP Q1 2024)",
        "anlauf_sop": "Q1 2024",
        "volumen_jahr": 220_000,
        "preis_eur": 285.00,
    },
    "ADAS-V4D": {
        "name": "Radar Fusion Steuergeraet ADAS-V4D",
        "beschr": "Level-2/3 ADAS-Steuergeraet mit 4D-Radar-Fusion (Nvidia Orin SoC, 77-GHz Front + Side Radar)",
        "asil": "ASIL-D",
        "werk": "Brennhagen Elektronik GmbH (REG), Heilbronn – Linie 1; Software-Stack RSG Muenchen (ASPICE Level 3)",
        "anlauf_sop": "Q2 2023",
        "volumen_jahr": 95_000,
        "preis_eur": 798.00,
    },
    "ECU-900": {
        "name": "Powertrain-ECU Gen3 (ECU-900)",
        "beschr": "Powertrain-Steuergeraet fuer MEB+ / MQB-Evo (Infineon AURIX TC39x, multi-core)",
        "asil": "ASIL-C",
        "werk": "Brennhagen Elektronik GmbH (REG), Heilbronn – Linie 2; SMD via RPL Katowice",
        "anlauf_sop": "Q4 2022",
        "volumen_jahr": 145_000,
        "preis_eur": 198.50,
    },
    "LightCtrl-7": {
        "name": "Matrix-LED Steuermodul (LightCtrl-7)",
        "beschr": "Matrix-LED-Frontscheinwerfersteuerung (1024 Pixel, GMSL2-Anbindung)",
        "asil": "ASIL-B",
        "werk": "Brennhagen Elektronik GmbH (REG), Heilbronn – Linie 3",
        "anlauf_sop": "Q1 2023",
        "volumen_jahr": 320_000,
        "preis_eur": 92.40,
    },
}

# Default product if filename only has OEM (legal/quality docs)
DEFAULT_PROD_KEY = "ICP-3"

# Approximate framework volumes (Mio EUR / Jahre) per (OEM, Produkt)
RAHMEN_VOLUMEN = {
    ("BMW", "ICP-3"): (850, 5),
    ("BMW", "BMS-12"): (220, 5),
    ("BMW", "ADAS-V4D"): (180, 4),
    ("BMW", "ECU-900"): (120, 4),
    ("BMW", "LightCtrl-7"): (95, 4),
    ("VW", "BMS-12"): (280, 7),
    ("VW", "ECU-900"): (210, 5),
    ("VW", "ICP-3"): (140, 5),
    ("VW", "ADAS-V4D"): (160, 4),
    ("MBZ", "ADAS-V4D"): (380, 5),
    ("MBZ", "ICP-3"): (210, 5),
    ("MBZ", "BMS-12"): (180, 5),
    ("MBZ", "ECU-900"): (110, 4),
    ("STE", "ECU-900"): (210, 4),
    ("STE", "ADAS-V4D"): (140, 4),
    ("STE", "ICP-3"): (95, 4),
    ("STE", "BMS-12"): (80, 4),
    ("CON", "ADAS-V4D"): (120, 4),
    ("CON", "ICP-3"): (75, 4),
    ("CON", "BMS-12"): (90, 5),
    ("CON", "ECU-900"): (60, 3),
}

def volumen(oem_key, prod_key):
    return RAHMEN_VOLUMEN.get((oem_key, prod_key), (95, 4))


# ── Filename parsing ───────────────────────────────────────────────────────
def parse(fname):
    """Return dict with keys: oem (key), produkt (key|None), typ, jahr, quartal, extra."""
    stem = fname.replace(".docx", "")
    parts = stem.split("_")
    info = {"raw": stem, "oem": None, "produkt": None, "typ": None,
            "jahr": None, "quartal": None, "extra": ""}
    if not parts:
        return info
    # PRJ-*
    if parts[0].startswith("PRJ-"):
        info["typ"] = "PRJ_STATUS"
        info["raw_prj"] = stem
        m_jahr = re.search(r"_(\d{4})_", stem)
        if m_jahr:
            info["jahr"] = m_jahr.group(1)
        m_prod = re.search(r"(ADAS-V4D|BMS-12|ECU-900|ICP-3|LightCtrl-7|BatteryMS-12)", stem)
        if m_prod:
            p = m_prod.group(1)
            info["produkt"] = "BMS-12" if p == "BatteryMS-12" else p
        return info
    if parts[0] == "REA" and len(parts) > 1:
        oem_part = parts[1]
        if oem_part in OEM:
            info["oem"] = oem_part
        else:
            info["typ"] = "MISC_REA"
            info["raw_segment"] = "_".join(parts[1:])
            return info
        idx = 2
        # Optional Produkt
        if idx < len(parts) and parts[idx] in PRODUKT:
            info["produkt"] = parts[idx]
            idx += 1
        # Typ-keyword
        rest = "_".join(parts[idx:])
        info["rest"] = rest
        # year
        m_jahr = re.search(r"(20\d{2})", rest)
        if m_jahr:
            info["jahr"] = m_jahr.group(1)
        m_q = re.search(r"Q([1-4])", rest)
        if m_q:
            info["quartal"] = "Q" + m_q.group(1)
        # type classification by keyword
        if "QBR" in rest:
            info["typ"] = "QBR"
        elif "ECR" in rest:
            info["typ"] = "ECR"
            m_nr = re.search(r"ECR_\d{4}_(\d{3})", rest)
            info["ecr_nr"] = m_nr.group(1) if m_nr else "001"
        elif "Nomination" in rest:
            info["typ"] = "NOMINATION"
        elif "RFQ" in rest:
            info["typ"] = "RFQ"
        elif "Liefervertrag" in rest:
            info["typ"] = "LIEFERVERTRAG"
        elif "Rahmenliefervertrag" in rest:
            info["typ"] = "RAHMENLIEFERVERTRAG"
        elif "Rahmenvertrag_Kuendigung" in rest or "Kuendigung_Androhung" in rest:
            info["typ"] = "KUENDIGUNG"
        elif "Vertragsaenderung" in rest:
            info["typ"] = "NACHTRAG"
        elif "Versorgungsbestaetigung" in rest:
            info["typ"] = "VERSORGUNG"
        elif "Langfristlieferzusage" in rest:
            info["typ"] = "LANGFRIST"
        elif "Jahrespreisverhandlung" in rest:
            info["typ"] = "JAHRESPREIS"
        elif "Preisanpassungsschreiben" in rest:
            info["typ"] = "PREISANPASSUNG"
        elif "Lobesbriefe" in rest or "Top_Supplier" in rest:
            info["typ"] = "LOB"
        elif "Eskalationsbrief" in rest or "Lieferengpass" in rest:
            info["typ"] = "ESKALATION"
        elif "Claim" in rest:
            info["typ"] = "CLAIM"
        elif "Audit_Einladung" in rest:
            info["typ"] = "AUDIT_EINLADUNG"
        elif "Kundenaudit_Bericht" in rest or "Kundenaudit" in rest:
            info["typ"] = "AUDIT_BERICHT"
        elif "CSR" in rest or "Kundspezifische" in rest:
            info["typ"] = "CSR"
        elif "Qualitaetsvereinbarung" in rest:
            info["typ"] = "QSV"
        elif "Kapazitaetsanfrage" in rest:
            info["typ"] = "KAPAZITAET"
        else:
            info["typ"] = "MISC_OEM"
        return info
    # FX hedge / interne / etc. fallthrough
    info["typ"] = "MISC"
    info["raw_segment"] = stem
    return info


# ── Section helpers ────────────────────────────────────────────────────────
def addr_block(oem_key):
    o = OEM[oem_key]
    return (
        f"Empfaengerin:\n{o['legal']}\n{o['addr']}\n\n"
        f"Ansprechpartner Einkauf: {o['kontakt']} ({o['rolle']})\n"
        f"Werk / Bedarfsstelle: {o['werk']}\n\n"
        f"Absender:\n{R['name']}, {R['addr']}\n"
        f"Verantwortlich: Stefan Richter (CMO / BD), Key-Account-Management OEM\n"
        f"In Kopie: Anna Mueller (CEO), Laura Bauer (CFO)"
    )

def prod_block(prod_key):
    p = PRODUKT[prod_key]
    return (
        f"Produkt: {p['name']}\n"
        f"Kurzbeschreibung: {p['beschr']}\n"
        f"Sicherheitsklassifizierung: {p['asil']} (ISO 26262); IATF 16949 zertifizierter Fertigungsstandort.\n"
        f"Fertigungsstandort: {p['werk']}\n"
        f"SOP-Ziel: {p['anlauf_sop']}; Lebenszyklus-Volumen Jahr 1 (Plan): {p['volumen_jahr']:,} Einheiten\n"
        f"Plan-Stueckpreis (EUR, EXW): {p['preis_eur']:.2f}"
    ).replace(",", ".")


# ── 1. RAHMENLIEFERVERTRAG ────────────────────────────────────────────────
def doc_rahmenliefervertrag(fname, oem_key, jahr):
    o = OEM[oem_key]
    # use BMW ICP-3 as default major prod for that OEM, fall back to first known volume
    prod_key = next((p for (ok, p) in RAHMEN_VOLUMEN if ok == oem_key), DEFAULT_PROD_KEY)
    p = PRODUKT[prod_key]
    vol_mio, jahre = volumen(oem_key, prod_key)
    write_doc(BASE / fname, H,
        f"Rahmenliefervertrag {o['full']} – Programmportfolio {jahr}",
        subtitle=f"Master Supply Agreement zwischen {R['name']} und {o['legal']}",
        confidential=True,
        sections=[
            ("Vertragsparteien", addr_block(oem_key)),
            ("Praeambel",
             f"Die Parteien beabsichtigen, im Rahmen der OEM-Tier-1-Lieferbeziehung mehrere Programme "
             f"ueber elektronische Steuergeraete der Brennhagen-Produktreihe (ICP-3, BMS-12, ADAS-V4D, "
             f"ECU-900, LightCtrl-7) abzuwickeln. Dieser Rahmenliefervertrag regelt die uebergeordneten "
             f"Bedingungen; Einzelheiten zu Stueckzahlen, Preisen, Liefer-Incoterms, Werkszuordnungen und "
             f"SOP-/EOP-Daten werden in produkt- bzw. programmbezogenen Liefervertraegen (»Einzelvertraege«) "
             f"sowie monatlichen Lieferabrufen (Forecast + Just-in-Sequence-Calls via EDI VDA 4905 / VDA 4915) "
             f"verbindlich festgelegt."),
            ("§ 1 Vertragsgegenstand und Geltung",
             ("clauses", [
                 (f"§ 1 Vertragsgegenstand",
                  [f"Brennhagen liefert dem Kunden Elektronik-Komponenten und Steuergeraete fuer "
                   f"Fahrzeugprogramme des Kunden, beginnend mit dem Leitprodukt {p['name']}. "
                   f"Voraussichtliches Gesamtvolumen ueber die Vertragslaufzeit: ca. {vol_mio} Mio. EUR.",
                   f"Vertragslaufzeit: {jahr} bis {int(jahr)+jahre}; Verlaengerung um jeweils 12 Monate, "
                   f"sofern keine Partei spaetestens 9 Monate vor Ablauf schriftlich widerspricht.",
                   f"Der Vertrag gilt fuer alle Werke und Bedarfsstellen des Kunden weltweit "
                   f"(insbesondere {o['werk']}); kundenseitige Konzern-Anschlussbestellungen werden "
                   f"als Lieferabrufe behandelt."]),
                 ("§ 2 Mengen und Lieferabruf",
                  ["Verbindliche Mengen werden ueber rollierende 18-Monats-Forecasts mit gefrorenem "
                   "12-Wochen-Horizont (»12-week Frozen Zone«) gemaess VDA 5009 abgestimmt; "
                   "Lieferabrufe erfolgen wochengenau ueber EDI (VDA 4905 / 4915, ggfs. ANSI X.12 830/862).",
                   "Mengenabweichungen +/- 15 % innerhalb des Forecast-Horizonts sind ohne Mehrkostenfolge "
                   "moeglich; darueber hinausgehende Abweichungen werden gesondert verhandelt (Pass-Through "
                   "von Material-Eskalations- und Logistik-Mehrkosten)."]),
                 ("§ 3 Qualitaet und Logistik",
                  [f"Qualitaetsanforderungen gemaess separater Qualitaetssicherungsvereinbarung (QSV) und "
                   f"kundenspezifischer Anforderungen (Customer-Specific Requirements, CSR – siehe Anhang 2). "
                   f"Zielwert ppm < 25 (3-Monatsrollend) fuer Serienlieferungen; ppm < 5 bei "
                   f"Sicherheits-Steuergeraeten ({p['asil']}).",
                   "Lieferung erfolgt FCA Werk Heilbronn (Incoterms 2020) bzw. nach gesonderter "
                   "Vereinbarung DAP Kundenwerk. Verpackungsstandard gemaess VDA 4500 (KLT). "
                   "Notfall-Sondertransporte gehen zu Lasten der verursachenden Partei."]),
                 ("§ 4 Preisanpassung und Materialpass-Through",
                  [f"Listenpreis bei Vertragsabschluss: {p['preis_eur']:.2f} EUR / Einheit (Plan-Stueckpreis EXW). "
                   f"Jaehrliche Preisverhandlung (»Annual Productivity Negotiation«) im November des Vorjahres; "
                   f"Brennhagen-Anspruch auf Produktivitaetsbeteiligung ueblicherweise 1,5 - 3 % p. a. "
                   f"deutlich abhaengig von Volumen- und Material-Konjunktur.",
                   "Material-Pass-Through-Klausel fuer Halbleiter (Mikrocontroller, Speicher, "
                   "Leistungs-MOSFETs), Buntmetalle (Kupfer, Aluminium-Lot) und ausgewaehlte Kunststoffe; "
                   "Quartals-Anpassung anhand definierter Indizes (LME Kupfer, S&P GSCI, Wafer-Indizes). "
                   "Detailregelung Anhang 3.",
                   "Im Ausnahmefall (Force Majeure-aehnlich, Halbleiter-Engpass) sind Ad-hoc-"
                   "Eskalationspreise schriftlich zu vereinbaren (Eskalation an Vorstand beider Parteien). "
                   "Brennhagen verpflichtet sich, technische Alternativen (Second-Source / Re-Design) im "
                   "Anlauffall innerhalb von 90 Tagen zu evaluieren."]),
                 ("§ 5 Gewaehrleistung und Haftung",
                  ["Gewaehrleistungsfrist: 24 Monate ab Inbetriebnahme des Fahrzeugs durch den Endkunden, "
                   "max. 36 Monate ab Lieferung an den Kunden. Sondergarantien (Sicherheits-Steuergeraete) "
                   "gemaess Anhang 1.",
                   "Haftung fuer mittelbare Schaeden (Rueckrufkosten, Werkstoertage) ist auf 5 Mio. EUR "
                   "je Schadensereignis sowie 15 Mio. EUR p. a. begrenzt; ueberschreitende Risiken werden "
                   "durch gemeinsame Produkthaftpflichtversicherung (Allianz Global Corporate & Specialty) "
                   "abgesichert.",
                   "Eskalationsklausel fuer Rueckrufe: Joint Recall Committee binnen 72 h; "
                   "Kostenteilung nach festgelegtem Verursachungsbeitrag (Root-Cause-Analyse extern, "
                   "z. B. KPMG-Pruefer)."]),
                 ("§ 6 Compliance, Nachhaltigkeit, Code of Conduct",
                  [f"Brennhagen bestaetigt die Einhaltung des {o['full']}-Lieferantenkodex sowie die "
                   f"Verpflichtung zur Einhaltung des Lieferkettensorgfaltspflichtengesetzes (LkSG). "
                   f"CO2-Footprint-Reporting (Scope 1/2/3) jaehrlich gemaess CDP / GRI; CO2-Zielpfad "
                   f"-30 % bis 2030 (Basis 2020).",
                   "Mineralien-Compliance (Dodd-Frank, EU-Konfliktmineralien-VO) durch CMRT-Reporting "
                   "(RMI Conflict Minerals Reporting Template) quartalsweise.",
                   f"REACH-/RoHS-/IMDS-Reporting fuer alle Stuecklisten obligatorisch; Aenderungen "
                   f"an Materialien werden via PPAP/ECR-Prozess (siehe § 7) freigegeben."]),
                 ("§ 7 Aenderungsmanagement (PPAP / ECR)",
                  ["Saemtliche Aenderungen an Produkten, Werkzeugen, Materialien, Produktionsorten oder "
                   "Teilelieferanten beduerfen der vorherigen schriftlichen Zustimmung des Kunden im Wege "
                   "des PPAP (Production Part Approval Process, AIAG / VDA-Band 2) bzw. Engineering "
                   "Change Request (ECR).",
                   "Re-PPAP-Pflicht u. a. bei: Wechsel des Halbleiter-Lieferanten, Werkzeugumzug, "
                   "Aenderung der Software-Hauptversion, Wechsel des Verguss-/Loetprozesses."]),
                 ("§ 8 Schlussbestimmungen",
                  ["Anwendbares Recht: Deutsches Recht unter Ausschluss des UN-Kaufrechts (CISG). "
                   "Gerichtsstand: Stuttgart; alternativ Schiedsverfahren nach DIS-Schiedsordnung "
                   "(Sitz Frankfurt am Main) ab Streitwert 5 Mio. EUR.",
                   "Vertraulichkeitsvereinbarung gemaess Anhang 4 (Laufzeit 10 Jahre nach Vertragsende). "
                   "Aenderungen dieses Rahmenvertrages beduerfen der Schriftform; muendliche Nebenabreden "
                   "bestehen nicht.",
                   "Vorrangregelung: (1) Einzelvertraege; (2) Lieferabrufe; (3) dieser Rahmenvertrag; "
                   "(4) Allgemeine Einkaufsbedingungen des Kunden."]),
             ])),
            ("Anlagen",
             ("list", [
                 "Anlage 1: Sicherheitsanforderungen ISO 26262 / SOTIF (ISO 21448) – produktspezifisch",
                 "Anlage 2: Qualitaetssicherungsvereinbarung (QSV) und Customer-Specific Requirements",
                 "Anlage 3: Material-Pass-Through-Klausel mit Indizes-Definitionen",
                 "Anlage 4: Vertraulichkeitsvereinbarung (NDA) – Laufzeit 10 J.",
                 "Anlage 5: Liste der zugelassenen Werke und Sub-Lieferanten (Approved Vendor List, AVL)",
             ])),
            ("Unterschriften",
             signatures("Stefan Richter", "CMO / BD", R["name"],
                        o["kontakt"], o["rolle"], o["legal"],
                        place="Stuttgart", date_str_=f"14. Maerz {jahr}")),
        ])


# ── 2. LIEFERVERTRAG (produktbezogen) ─────────────────────────────────────
def doc_liefervertrag(fname, oem_key, prod_key, jahr):
    o = OEM[oem_key]
    p = PRODUKT[prod_key]
    vol_mio, jahre = volumen(oem_key, prod_key)
    write_doc(BASE / fname, H,
        f"Liefervertrag {p['name']} fuer {o['full']} ({jahr})",
        subtitle=f"Programmbezogener Einzelvertrag zum Rahmenliefervertrag {oem_key}-{jahr-1 if isinstance(jahr,int) else 2022}",
        sections=[
            ("Vertragsparteien", addr_block(oem_key)),
            ("Vertragsgegenstand", prod_block(prod_key)),
            ("§ 1 Programm-Daten",
             [["Position", "Wert"],
              ["Programmname (Kunde)", f"{oem_key}-{prod_key}-{jahr}"],
              ["Plattform (Kunde)", "MEB+ / MQB-Evo / NEUE KLASSE / STLA / EVA2"],
              ["SOP-Ziel", p['anlauf_sop']],
              ["EOP-Ziel", f"Q4 {int(jahr)+jahre}"],
              ["Lebenszyklus-Gesamtvolumen", f"{vol_mio} Mio. EUR ({jahre} Jahre)"],
              ["Plan-Jahresvolumen Steady-State", f"{p['volumen_jahr']:,} Einheiten".replace(",", ".")],
              ["Plan-Stueckpreis EXW", f"{p['preis_eur']:.2f} EUR"],
              ["Fertigungswerk", p['werk']],
              ["Software-Stack", "RSG Muenchen (ASPICE Level 2-3)" if prod_key in ("ADAS-V4D","ICP-3","BMS-12") else "in-house REG"],
              ["Verantwortlich Brennhagen", "Stefan Richter (CMO) / Programm-Manager n. n."]]),
            ("§ 2 Lieferbedingungen",
             "Lieferung FCA Heilbronn (Incoterms 2020), Verpackung KLT VDA 4500, Just-in-Sequence Pull "
             "aus 12-Wochen-Frozen-Zone (EDI VDA 4905/4915). Sondertransporte gehen zu Lasten der "
             "verursachenden Partei. Anlieferung an Bedarfsstelle: " + o['werk'] + ". "
             "Wareneingangspruefung (skip-lot) gemaess Kunden-Q-Verfahren."),
            ("§ 3 Preisgleitklausel",
             f"Der Plan-Stueckpreis EUR {p['preis_eur']:.2f} (EXW) gilt fuer Plan-Volumen. "
             f"Produktivitaetsabschlag {1.5 + (hash(oem_key+prod_key) % 20)/10:.1f} % p. a. (»Annual Productivity«) "
             f"bei Erreichung des Plan-Volumens. Material-Pass-Through-Klausel fuer Halbleiter (MCU "
             f"Infineon AURIX, RAM/Flash, Power-MOSFETs) gemaess Anhang Index-Liste; Quartalsanpassung."),
            ("§ 4 Qualitaet und ppm",
             f"ppm-Ziel: < {15 if p['asil']=='ASIL-D' else 25} (rollierend 3 Monate). "
             f"Bei Ueberschreitung > 50 ppm ueber 3 Monate: Eskalation an Werkleiter REG (Andreas Maier); "
             f"bei > 100 ppm Kunden-Audit innerhalb 30 Tagen. Sondergarantien fuer "
             f"Sicherheits-Steuergeraete ({p['asil']}): 5 Jahre / 150.000 km."),
            ("§ 5 Aenderungsverfahren",
             "Engineering Change Requests (ECR) im 4-stufigen Verfahren: (1) Anfrage Kunde; "
             "(2) Machbarkeitsanalyse Brennhagen (10 AT); (3) Angebot Brennhagen inkl. Re-PPAP-Aufwand; "
             "(4) Kundenfreigabe + Implementierung. ECR-Reporting quartalsweise im QBR (siehe separater "
             "QBR-Prozess)."),
            ("§ 6 Pönalen und SLA",
             "Liefer-SLA: 98,5 % On-Time-Delivery (OTD) rollierend 3 Monate. "
             "Ponale bei OTD < 95 %: 2 % des betroffenen Monatsumsatzes; bei OTD < 90 %: 5 %. "
             "Maximale Ponale-Belastung 1,5 Mio. EUR p. a. pro Programm. "
             "Ausnahmen: Force-Majeure, kundenseitig verursachte Lieferunterbrechungen."),
            ("§ 7 Sonstiges",
             "Geltung des Rahmenliefervertrages " + str(oem_key) + " (siehe REA_" + oem_key + "_Rahmenliefervertrag_2022). "
             "Schriftform fuer Aenderungen; Vorrang dieser Einzelregelung vor Rahmenvertrag. "
             "Geheimhaltungsvereinbarung gemaess Konzern-NDA-Standard."),
            ("Unterschriften",
             signatures("Stefan Richter", "CMO / BD", R["name"],
                        o["kontakt"], o["rolle"], o["legal"],
                        place="Stuttgart", date_str_=f"15. Juni {jahr}")),
        ])


# ── 3. AUFTRAGSBESTÄTIGUNG / NOMINATION LETTER ────────────────────────────
def doc_nomination(fname, oem_key, prod_key, jahr):
    o = OEM[oem_key]
    p = PRODUKT[prod_key]
    vol_mio, jahre = volumen(oem_key, prod_key)
    write_doc(BASE / fname, H,
        f"Nomination Letter / Auftragsbestaetigung {o['full']} – {p['name']} ({jahr})",
        subtitle="Verbindliche Programmvergabe an Brennhagen Elektronik AG",
        sections=[
            ("Adressat / Vorgang", addr_block(oem_key)),
            ("Bezug",
             f"RFQ Nr. {oem_key}-{prod_key}-RFQ-{jahr} vom Februar {jahr}; "
             f"Angebot Brennhagen vom 15. April {jahr}; Nachverhandlung 12. Mai {jahr} "
             f"(Teilnehmer Brennhagen: Stefan Richter CMO, n. n. Programm-Manager; Kunde: "
             f"{o['kontakt']}, {o['rolle']})."),
            ("Programm-Vergabe",
             f"Hiermit bestaetigt {o['legal']} die Vergabe des Programms »{p['name']} fuer Plattform "
             f"{oem_key}-Generation {jahr}« an die Brennhagen Elektronik AG als Tier-1-Lieferantin. "
             f"Voraussichtliches Programmvolumen: {vol_mio} Mio. EUR ueber {jahre} Jahre Serien-Laufzeit "
             f"(SOP {p['anlauf_sop']} / EOP Q4 {int(jahr)+jahre})."),
            ("Programmdaten", prod_block(prod_key)),
            ("Stueckzahl- und Preis-Eckdaten",
             [["Position", "Wert"],
              ["Plan-Jahresvolumen Steady-State", f"{p['volumen_jahr']:,} Einheiten".replace(",", ".")],
              ["Plan-Stueckpreis EXW (EUR)", f"{p['preis_eur']:.2f}"],
              ["SOP-Ziel", p['anlauf_sop']],
              ["EOP-Ziel", f"Q4 {int(jahr)+jahre}"],
              ["Gesamtvolumen (Lebenszyklus)", f"{vol_mio} Mio. EUR"],
              ["Werkszuordnung", p['werk']],
              ["Programm-Manager (vorl.)", "wird binnen 14 Tagen benannt"],
              ["EDI-Anbindung", "VDA 4905 / 4915; ggfs. ANSI X.12 830/862"]]),
            ("Naechste Schritte",
             ("list", [
                 f"Vertragsschluss Programm-Liefervertrag (Einzelvertrag): bis Ende Q3 {jahr}",
                 f"Lastenheft-/Pflichtenheft-Freigabe (»SOR / Statement of Requirements«): bis Ende Q2 {jahr}",
                 f"Erstmuster-Lieferung (PPAP Level 3 / VDA 2): 9 Monate vor SOP",
                 f"Werkzeug- und Pruefmittel-Investitionsfreigabe: nach Vertragsschluss; "
                 f"Anschubfinanzierung Kunden-Tools max. 4 Mio. EUR (zu erstatten via Stueckpreis)",
                 f"Q-Audit der Fertigungslinie (IATF 16949) durch SQE {o['sqe']}: Q1 {int(jahr)+1}",
             ])),
            ("Vorbehalte / Bedingungen",
             "Vergabe steht unter Vorbehalt: (1) Erfolgreicher PPAP Level 3; (2) Erreichen "
             "ppm-Ziel < 25 in Vorserie; (3) Bestaetigung Material-Pass-Through-Klausel; "
             "(4) Compliance mit OEM-Code-of-Conduct; (5) Erreichung des Investitionsentscheids "
             "des OEM-Lenkungskreises (»Decision Phase Gate«)."),
            ("Unterschriften",
             signatures("Stefan Richter", "CMO / BD", R["name"],
                        o["kontakt"], o["rolle"], o["legal"],
                        place=o['addr'].split(',')[1].strip(), date_str_=f"22. Mai {jahr}")),
        ])


# ── 4. RFQ RESPONSE ────────────────────────────────────────────────────────
def doc_rfq(fname, oem_key, prod_key, jahr):
    o = OEM[oem_key]
    p = PRODUKT[prod_key]
    vol_mio, jahre = volumen(oem_key, prod_key)
    write_doc(BASE / fname, H,
        f"RFQ-Response {p['name']} fuer {o['full']} ({jahr})",
        subtitle=f"Verbindliches Angebot der Brennhagen Elektronik AG zur Ausschreibung {oem_key}-{prod_key}-RFQ-{jahr}",
        sections=[
            ("Adressat", addr_block(oem_key)),
            ("Bezug",
             f"RFQ Nr. {oem_key}-{prod_key}-RFQ-{jahr} vom Februar {jahr}; "
             f"Lastenheft Rev. 1.0 vom 25. Januar {jahr}; "
             f"Q&A Runde 1+2 abgeschlossen am 12. Maerz {jahr}; "
             f"Angebotsabgabe-Frist: 15. April {jahr}."),
            ("Angebotsgegenstand", prod_block(prod_key)),
            ("Kommerzielle Eckdaten",
             [["Position", "Wert"],
              ["Plan-Stueckpreis EXW (EUR, Jahr 1)", f"{p['preis_eur']:.2f}"],
              ["Plan-Stueckpreis EXW (EUR, Jahr 4 – Productivity 2 % p. a.)",
               f"{p['preis_eur']*0.94:.2f}"],
              ["Werkzeugkosten (Einmal, EUR)", f"{int(vol_mio*1000*0.0035):,}".replace(",", ".")],
              ["Engineering / NRE (Einmal, EUR)", f"{int(vol_mio*1000*0.0070):,}".replace(",", ".")],
              ["Plan-Jahresvolumen Steady-State (Einheiten)", f"{p['volumen_jahr']:,}".replace(",", ".")],
              ["Plan-Gesamtvolumen Lebenszyklus (Mio. EUR)", f"{vol_mio}"],
              ["SOP-Ziel / EOP-Ziel", f"{p['anlauf_sop']} / Q4 {int(jahr)+jahre}"],
              ["Werkszuordnung", p['werk']],
              ["Bindefrist Angebot", f"90 Tage ab Eingang"]]),
            ("Technische Erfuellung",
             "Die Brennhagen Elektronik AG bestaetigt die Erfuellung saemtlicher Anforderungen des "
             "Lastenheftes inkl. der funktionalen Sicherheitsanforderungen gemaess ISO 26262 "
             f"({p['asil']}) sowie SOTIF (ISO 21448). Abweichungen / Klaerungsbedarf siehe Anlage »Deviation List« "
             f"(insgesamt 4 Punkte; alle als »low impact« klassifiziert). Software-Stack {('RSG Muenchen' if prod_key in ('ADAS-V4D','ICP-3','BMS-12') else 'in-house REG Heilbronn')} "
             f"(ASPICE Level 2-3)."),
            ("Annahmen / Vorbehalte",
             ("list", [
                 "Material-Pass-Through-Klausel fuer Halbleiter (Infineon AURIX, NXP, Texas Instruments)",
                 "12-Wochen-Frozen-Zone fuer Lieferabrufe",
                 "Werkzeug- und NRE-Anschubfinanzierung 50 % bei Auftragserteilung",
                 "Volumen-Mindest-Commitment: 80 % des Plan-Volumens je Programm-Jahr",
                 "Vorbehalt Halbleiter-Allokation (Wafer-Kontingente Foundries TSMC / GlobalFoundries)",
             ])),
            ("Programm-Roadmap",
             ("list", [
                 f"Mai {jahr}: Nominierungsentscheidung Kunde",
                 f"Juni-September {jahr}: Vertragsverhandlungen (Rahmen + Einzel)",
                 f"Q4 {jahr} - Q1 {int(jahr)+1}: B-Muster (DV-Phase)",
                 f"Q2-Q3 {int(jahr)+1}: C-Muster (PV-Phase) + PPAP Submission",
                 f"{p['anlauf_sop']}: SOP / Serienanlauf",
             ])),
            ("Unterschriften",
             signatures("Stefan Richter", "CMO / BD", R["name"],
                        o["kontakt"], o["rolle"], o["legal"],
                        place="Stuttgart", date_str_=f"15. April {jahr}")),
        ])


# ── 5. QBR – Quarterly Business Review ────────────────────────────────────
def doc_qbr(fname, oem_key, prod_key, jahr, quartal):
    o = OEM[oem_key]
    p = PRODUKT[prod_key]
    # generate plausible KPIs varying by year/quarter
    seed = (hash(oem_key + prod_key + jahr + quartal) % 100) / 100.0
    ppm = int(10 + seed * 30)
    otd = round(94.5 + seed * 5.0, 1)
    open_ecr = int(2 + seed * 6)
    vol_mio_q = round((PRODUKT[prod_key]['volumen_jahr'] * PRODUKT[prod_key]['preis_eur'] / 4_000_000) * (0.85 + seed*0.3), 1)
    write_doc(BASE / fname, H,
        f"Quarterly Business Review {oem_key} – {p['name']} – {jahr} {quartal}",
        subtitle=f"Programm-Statusbericht zwischen Brennhagen Elektronik AG und {o['full']}",
        sections=[
            ("Teilnehmer",
             f"Brennhagen: Stefan Richter (CMO), Programm-Manager (n. n.), Qualitaetsleitung Sabine Brand (REG), "
             f"Werkleiter Andreas Maier (REG Heilbronn), bei Bedarf Stefan Hoffmann (CTO) bzw. ab 1.7.2024 "
             f"Dr. Petra Hollmann (CTO).\n\n"
             f"Kunde: {o['kontakt']} ({o['rolle']}), {o['sqe']} (SQE), {o['qmb']} (QMB-Werk).\n\n"
             f"Format: 4 Stunden Praesenz / hybrid; Quartalsrhythmus; Vorlage 5 Werktage vor Termin."),
            ("Bezug",
             f"Programm {oem_key}-{prod_key}-{jahr}; Fertigungswerk {p['werk']}; "
             f"SOP-Status {p['anlauf_sop']}; aktuelle Berichtsperiode: {jahr} {quartal}."),
            ("KPI-Uebersicht (Berichtsquartal)",
             [["KPI", "Ist", "Ziel", "Status"],
              ["Liefermenge Quartal (Tsd. Einheiten)",
               f"{int(p['volumen_jahr']/4 * (0.9+seed*0.2)):,}".replace(",", "."),
               f"{int(p['volumen_jahr']/4):,}".replace(",", "."), "OK"],
              ["Umsatz Quartal (Mio. EUR)", f"{vol_mio_q:.1f}", f"{(p['volumen_jahr']*p['preis_eur']/4_000_000):.1f}",
               "OK" if seed > 0.4 else "Watch"],
              ["ppm (rollierend 3 Mon.)", str(ppm), "< 25", "OK" if ppm < 25 else "Watch"],
              ["On-Time-Delivery OTD (%)", f"{otd}", "> 98,5", "OK" if otd > 98.5 else "Watch"],
              ["Offene ECRs", str(open_ecr), "< 5", "OK" if open_ecr < 5 else "Watch"],
              ["Offene 8D-Reports", str(int(seed*3)), "0-1", "OK"],
              ["Forecast-Genauigkeit (+/- %)", f"{round(7+seed*5,1)}", "< 10", "OK"]]),
            ("Programm-Status",
             f"Das Programm {oem_key}-{prod_key} liegt im Quartal {jahr} {quartal} im Wesentlichen im Plan. "
             f"Die geplante Liefermenge wurde mit {int(seed*100+95)} % der vereinbarten Menge erfuellt. "
             f"Der Stueckpreis ist gemaess Vertrag stabil bei {p['preis_eur']:.2f} EUR EXW. "
             f"Material-Pass-Through fuer Halbleiter wurde quartalsweise abgerechnet "
             f"(Bewegung +/- 0,8 % gegenueber Vorquartal)."),
            ("Qualitaet (8D / Reklamationen)",
             "Im Berichtsquartal wurden insgesamt " + str(int(1+seed*3)) + " 8D-Reports erstellt; "
             "alle in Stufe D5 (Wirksamkeit der Massnahme) oder weiter fortgeschritten. "
             "Wesentliche Themen: Loetstellen-Toleranz an Power-MOSFET (geloest via DOE), "
             "Software-Bug Diagnose-Funktion (RSG-Patch v2.4.1), KLT-Beschaedigung Transport "
             "(Verpackungs-Re-Design mit Logistikpartner). "
             "Keine sicherheitsrelevanten Befunde, keine Feldausfaelle eskaliert."),
            ("Logistik und Lieferperformance",
             "OTD im Berichtsquartal " + str(otd) + " % (Ziel > 98,5 %). "
             "Sondertransporte: " + str(int(seed*5)) + " (Vorquartal: " + str(int(seed*7)) + "), "
             "Kosten 18-32 TEUR – traegt Brennhagen. "
             "Frozen-Zone-Adherence durch Kunde " + str(int(92+seed*7)) + " % (Ziel > 95 %); "
             "Auswirkungen auf Werks-Auslastung adressiert."),
            ("Engineering Change Requests (ECR)",
             "Offene ECRs: " + str(open_ecr) + " (davon " + str(int(open_ecr/2)) + " in Bearbeitung, "
             "Rest in Angebotsphase). Wesentliche ECRs: "
             "ECR-001 Software-Update OTA-Capable (geplant Q2 2024), "
             "ECR-002 Connector-Wechsel (TE -> Molex, Re-PPAP), "
             "ECR-003 RoHS-konforme Loetzinn-Substitution."),
            ("Forecast und Volumenplanung",
             f"Forecast Jahr+1 unveraendert {p['volumen_jahr']:,} Einheiten (rollierend 12 Monate). "
             f"Risikofaktoren: Halbleiter-Allokation TSMC N7/N5 (im Plan, jedoch ohne Puffer), "
             f"BEV-Hochlauf Plattform {oem_key} (Risiko Verzoegerung +/- 1 Quartal). "
             f"Brennhagen-seitig Werks-Kapazitaet bestaetigt durch Werkleiter A. Maier."
             .replace(",", ".")),
            ("Aktionspunkte (Action Items)",
             ("list", [
                 f"AI-1: Brennhagen sendet 8D-Status Reports der laufenden 8Ds bis +10 AT an {o['sqe']}",
                 f"AI-2: Kunde liefert verbindliches Forecast-Update fuer {jahr} H2 bis +20 AT",
                 f"AI-3: Re-PPAP Connector-Wechsel (ECR-002) in Angebot bis +30 AT",
                 f"AI-4: Joint Workshop Sondertransport-Reduktion in KW {(int(quartal[1])*13)+2}",
                 f"AI-5: Naechster QBR-Termin {jahr if quartal != 'Q4' else int(jahr)+1} Folge-Quartal",
             ])),
            ("Unterschriften",
             signatures("Stefan Richter", "CMO / BD", R["name"],
                        o["kontakt"], o["rolle"], o["legal"],
                        place="Stuttgart", date_str_=f"{quartal}-Ende {jahr} + 14 AT")),
        ])


# ── 6. ECR – Engineering Change Request ──────────────────────────────────
def doc_ecr(fname, oem_key, prod_key, jahr, ecr_nr):
    o = OEM[oem_key]
    p = PRODUKT[prod_key]
    write_doc(BASE / fname, H,
        f"Engineering Change Request {oem_key}-{prod_key}-ECR-{jahr}-{ecr_nr}",
        subtitle=f"Aenderungsantrag im Rahmen Programm {oem_key}-{prod_key}-{jahr}",
        sections=[
            ("Adressat / Vorgang", addr_block(oem_key)),
            ("ECR-Identifikation",
             [["Position", "Wert"],
              ["ECR-Nummer", f"{oem_key}-{prod_key}-ECR-{jahr}-{ecr_nr}"],
              ["Programm", f"{oem_key}-{prod_key}-{jahr}"],
              ["Produkt", p['name']],
              ["Stand", f"Eingang Kunde: " + ("15.03." if ecr_nr=="001" else "08.06." if ecr_nr=="002" else "22.09.") + jahr],
              ["Initiator", "Kunde (Konstruktion)" if int(ecr_nr) <= 2 else "Brennhagen (Wertanalyse)"],
              ["Prioritaet", "A (kritisch, vor SOP umzusetzen)" if ecr_nr=="001" else "B (mittel)"]]),
            ("Aenderungsbeschreibung",
             {
                 "001": "Software-Patch v2.5.0: Anpassung der Diagnose-Routine (DTC-Erweiterung um 14 neue "
                        "Trouble-Codes), neue UDS-Service-IDs gemaess Kunden-Spezifikation 14-AS-2310.2 "
                        "Rev. C. Lastenheft-Auszug siehe Anhang.",
                 "002": "Aenderung des Steckverbinder-Lieferanten von TE Connectivity HFM-Serie auf "
                        "Molex MX150-Serie aufgrund verbesserter Vibrationsfestigkeit (USCAR-2 Class 3 "
                        "anstatt Class 2) und gleichbleibender Kosten. Re-PPAP Level 3 erforderlich.",
                 "003": "Materialwechsel Power-MOSFET von Infineon IPB019N08N3G auf Infineon IAUC100N04S6L "
                        "wegen Allokations-Risiko und besseren thermischen Eigenschaften (RDS_on -8 %). "
                        "Stueckkostenanpassung -0,18 EUR. Re-PPAP Level 2.",
             }.get(ecr_nr, "Aenderung gemaess separatem technischen Anhang; Re-PPAP-Anforderung gemaess "
                            "AIAG/VDA-Band 2; Material- und Werkzeugaenderungen werden separat ausgewiesen.")),
            ("Auswirkungen",
             [["Bereich", "Auswirkung"],
              ["Funktion / Performance", "Verbesserung bzw. unveraendert"],
              ["Sicherheit (ISO 26262)", f"Re-Validation auf {p['asil']}-Level (Safety Case Update)"],
              ["Werkzeugaufwand (EUR)", "12.500" if ecr_nr=="002" else "0"],
              ["NRE Engineering (EUR)", "28.000"],
              ["Stueckkostenaenderung (EUR)", "-0,18" if ecr_nr=="003" else "+0,42" if ecr_nr=="002" else "0,00"],
              ["Implementierungsdauer", "12 Wochen" if ecr_nr=="002" else "6 Wochen"],
              ["PPAP-Level", "Level 3 (Re-PPAP komplett)" if ecr_nr=="002" else "Level 2"]]),
            ("Stellungnahme Brennhagen",
             "Die beantragte Aenderung ist technisch und qualitativ umsetzbar. Die unter »Auswirkungen« "
             "ausgewiesenen Werkzeug- und NRE-Kosten werden dem Kunden gemaess Rahmenliefervertrag § 7 in "
             "Rechnung gestellt. Stueckkostenaenderung wird ab erfolgreichem PPAP-Approval wirksam. "
             "Brennhagen empfiehlt Annahme. Risiken: Halbleiter-Allokation IAUC100N04S6L (Infineon "
             "bestaetigt Liefersicherheit; LOA bis 2030 vorliegend)."),
            ("Naechste Schritte",
             ("list", [
                 "Freigabe ECR durch Kunden-Konstruktionsleitung erforderlich",
                 "Kostenstellungnahme Brennhagen: bereits in Kommerziellem Angebot enthalten",
                 "Erstmusterlieferung Re-PPAP: +8 Wochen ab Freigabe",
                 "Serienanlauf nach erfolgreichem PPAP: +12 Wochen ab Freigabe",
                 "Reporting im naechsten QBR",
             ])),
            ("Unterschriften",
             signatures("Stefan Richter", "CMO / BD", R["name"],
                        o["kontakt"], o["rolle"], o["legal"],
                        place="Stuttgart", date_str_=f"30. " + ("Maerz" if ecr_nr=="001" else "Juni" if ecr_nr=="002" else "September") + " " + jahr)),
        ])


# ── 7. JAHRESPREISVERHANDLUNG / PREISANPASSUNG ───────────────────────────
def doc_jahrespreis(fname, oem_key, jahr):
    o = OEM[oem_key]
    write_doc(BASE / fname, H,
        f"Jahrespreisverhandlung {oem_key} – Verhandlungsergebnis {jahr}",
        subtitle="Verhandlungsprotokoll und Vereinbarung der Stueckpreise fuer das Geschaeftsjahr",
        sections=[
            ("Verhandlungspartner",
             f"Kunde: {o['legal']}, vertreten durch {o['kontakt']} ({o['rolle']}); "
             f"Stellv. Frau Dr. Eva Brenner (Strategic Sourcing).\n\n"
             f"Brennhagen: Stefan Richter (CMO / BD), Laura Bauer (CFO) – nur Eroeffnung; "
             f"Programm-Manager der jeweiligen Produktlinien."),
            ("Verhandlungstermine",
             f"Kick-off Brennhagen-Vorlage: 18. Oktober {int(jahr)-1}; "
             f"Runde 1 (Daten-Abgleich, Material-Pass-Through): 8. November {int(jahr)-1}; "
             f"Runde 2 (Productivity-Kommerziell): 22. November {int(jahr)-1}; "
             f"Runde 3 (Programm-spezifische Eskalationen): 6. Dezember {int(jahr)-1}; "
             f"Abschluss / Term Sheet: 18. Dezember {int(jahr)-1}; "
             f"Schriftliche Bestaetigung: 12. Januar {jahr}."),
            ("Vereinbarte Stueckpreise (EUR / EXW)",
             [["Produkt", f"Preis {int(jahr)-1}", f"Preis {jahr}", "Aenderung %"],
              ["ICP-3", "412,50", f"{412.50*0.985:.2f}", "-1,5 %"],
              ["BMS-12", "285,00", f"{285.00*0.98:.2f}", "-2,0 %"],
              ["ADAS-V4D", "798,00", f"{798.00*0.99:.2f}", "-1,0 %"],
              ["ECU-900", "198,50", f"{198.50*0.985:.2f}", "-1,5 %"],
              ["LightCtrl-7", "92,40", f"{92.40*0.98:.2f}", "-2,0 %"]]),
            ("Material-Pass-Through (Quartals-Indizes)",
             "Halbleiter-Index (Wafer Composite, Quelle SEMI/SIA): Aenderung gegenueber Vorquartal "
             "+/- 2,1 %; Kupfer LME 3M (London Metal Exchange): Aenderung -8,4 % (Ablauf 2023, "
             "Wirkung Q1 " + jahr + " positiv fuer Kunden); Polymer-Index (S&P GSCI Polymers): "
             "stabil. Pass-Through-Wirkung gemaess Anlage 3 des Rahmenliefervertrages quartals"
             "anteilig."),
            ("Volumen-Commitments",
             f"Kunde bestaetigt Volumen-Commitment fuer das Jahr {jahr} auf Basis des Programm-"
             f"Forecasts; Mindest-Volumen 80 % gemaess Liefervertrag. "
             f"Brennhagen sichert Werks-Kapazitaet (REG Heilbronn Linie 1-4, RPL Katowice SMD) "
             f"bis zur Plan-Menge zu."),
            ("Sonstiges",
             "Brennhagen hat im Verhandlungsverlauf auf eine Eskalation der Sondertransport-Kosten "
             "(7 Faelle in 2023) sowie auf die Notwendigkeit eines Forecast-Genauigkeits-Bonus/Malus "
             "hingewiesen. Beide Punkte werden in QBR Q1 " + jahr + " separat adressiert. "
             "Productivity-Beteiligung des Kunden gemaess Rahmenliefervertrag § 4 ist vollstaendig "
             "umgesetzt."),
            ("Unterschriften",
             signatures("Stefan Richter", "CMO / BD", R["name"],
                        o["kontakt"], o["rolle"], o["legal"],
                        place="Stuttgart", date_str_=f"12. Januar {jahr}")),
        ])


def doc_preisanpassung(fname, oem_key, jahr):
    o = OEM[oem_key]
    write_doc(BASE / fname, H,
        f"Preisanpassungsschreiben an {o['full']} ({jahr})",
        subtitle="Material-Eskalation und ausserordentliche Preisanpassung im Anlauffall",
        sections=[
            ("Adressat", addr_block(oem_key)),
            ("Anlass und Begruendung",
             f"Sehr geehrte/r {o['kontakt']},\n\n"
             f"hiermit teilen wir Ihnen mit, dass die Brennhagen Elektronik AG aufgrund "
             f"einer ausserordentlichen Material-Eskalation am Halbleiter-Markt (insbesondere "
             f"Infineon AURIX MCU, NXP S32-Familie, NOR-Flash) eine ausserordentliche Preisanpassung "
             f"vornehmen muss, die ueber den im Rahmenliefervertrag § 4 (Material-Pass-Through) "
             f"definierten Quartals-Index hinausgeht. Die Anpassung wirkt ab " +
             ("01.07." if jahr=="2021" else "01.10.") + jahr + " bis auf weiteres."),
            ("Konkret betroffene Programme und Preisaenderungen",
             [["Programm", "Aktueller Stueckpreis (EUR)", "Neuer Stueckpreis (EUR)", "Aenderung"],
              ["ICP-3 Infotainment", "412,50", "428,80", "+4,0 %"],
              ["BMS-12 EV-Battery", "285,00", "298,40", "+4,7 %"],
              ["ADAS-V4D Radar", "798,00", "832,40", "+4,3 %"],
              ["ECU-900 Powertrain", "198,50", "208,20", "+4,9 %"]]),
            ("Datengrundlage / Belege",
             ("list", [
                 "Infineon Pricing-Letter vom 12.04." + jahr + " (Preiserhoehung MCU +12 %)",
                 "NXP Allocation Letter (Q2 " + jahr + ") mit Schadens-MoQ-Reduktion",
                 "TSMC Wafer-Pricing-Update (Maerz " + jahr + "): +18 % Allgemein",
                 "Buntmetalle LME Kupfer-Index Anstieg +24 % seit Q4 " + str(int(jahr)-1),
                 "Energiepreise (Werk Heilbronn) Anstieg +35 % gegenueber Plan",
             ])),
            ("Verhandlungsangebot",
             "Wir schlagen vor, die Preisanpassung im Sinne einer partnerschaftlichen Lasten"
             "teilung wie folgt zu strukturieren: (1) 60 % Brennhagen (durch interne Wertanalyse "
             "und Volumen-Bundling); (2) 30 % Kunde (als ausserordentliche Eskalation); "
             "(3) 10 % gemeinsam aus Wertanalyse-Projekt (Re-Design Halbleiter-Konfiguration). "
             "Eine entsprechende Vereinbarung gem. § 6 Rahmenvertrag schlagen wir zum naechsten "
             "Steering-Termin vor."),
            ("Naechste Schritte",
             ("list", [
                 "Telefon-/Video-Konferenz innerhalb 5 Werktagen mit " + o['kontakt'],
                 "Verbindliche Antwort des Kunden binnen 14 Tagen",
                 "Bei Nichteinigung: Eskalation an Vorstand beider Parteien (CEO-Brief)",
                 "Im Falle der Annahme: Vertraglicher Nachtrag binnen 30 Tagen",
             ])),
            ("Unterschriften",
             signatures("Stefan Richter", "CMO / BD", R["name"],
                        o["kontakt"], o["rolle"], o["legal"],
                        place="Stuttgart", date_str_=f"22. Mai {jahr}")),
        ])


# ── 8. AUDIT EINLADUNG / BERICHT ─────────────────────────────────────────
def doc_audit_einladung(fname, oem_key, jahr):
    o = OEM[oem_key]
    write_doc(BASE / fname, H,
        f"Kundenaudit {o['full']} – Einladung / Agenda {jahr}",
        subtitle=f"Lieferantenaudit gemaess VDA 6.3 / IATF 16949 bei Brennhagen Elektronik AG (Werk Heilbronn)",
        sections=[
            ("Einladung",
             f"Sehr geehrte/r {o['qmb']},\n\n"
             f"hiermit moechten wir Sie und Ihr Audit-Team zum Kundenaudit {jahr} bei der "
             f"{R['name']} (Werk Heilbronn der Brennhagen Elektronik GmbH) einladen.\n\n"
             f"Termin (Vorschlag): "
             + ("15.-17. Juni " if jahr=="2021" else "12.-14. September " if jahr=="2022" else "20.-22. Maerz ") + jahr +
             f". Alternativtermine auf Anfrage.\n\n"
             f"Ort: Brennhagen Elektronik GmbH, Industriestrasse 45, 74072 Heilbronn (Werk 1)."),
            ("Audit-Umfang",
             f"Vorgesehen ist ein Prozess-/Produkt-Audit gemaess VDA 6.3 (Prozessaudit) sowie "
             f"Stichproben-Audit zu kundenspezifischen Anforderungen (CSR). Schwerpunkte:\n\n"
             f"- Programme: {oem_key} ICP-3 / BMS-12 / ADAS-V4D / ECU-900\n"
             f"- Prozess-Elemente: P5 (Lieferantenmanagement), P6 (Prozessanalyse Produktion), "
             f"P7 (Kundenbetreuung)\n"
             f"- Audit-Zeit: 2,5 Tage; Kick-off Tag 1 09:00; Abschlussbesprechung Tag 3 15:00"),
            ("Agenda-Vorschlag",
             [["Zeit", "Inhalt", "Beteiligte"],
              ["Tag 1 09:00", "Begruessung, Werksrundgang", "Werkleiter A. Maier, Q-Leitung S. Brand"],
              ["Tag 1 10:30", "Praesentation Q-Kennzahlen + Kennzahlentrend", "S. Brand"],
              ["Tag 1 13:00", "Produktions-Audit Linie 1-3 (Prozessaudit P6)", "Audit-Team + Schichtleiter"],
              ["Tag 1 16:30", "Tagesauswertung", "Audit-Team intern"],
              ["Tag 2 09:00", "Lieferantenmanagement P5; Sub-Tier-Audits", "Einkauf + Q-Leitung"],
              ["Tag 2 13:00", "Audit Programme ADAS-V4D (Software RSG Muenchen via VC)", "Dr. K. Kessler (RSG)"],
              ["Tag 2 16:30", "Tagesauswertung", "Audit-Team intern"],
              ["Tag 3 09:00", "Audit Programme BMS-12, ICP-3", "Programm-Manager"],
              ["Tag 3 13:00", "Massnahmen-Tracking aus Vorjahres-Audit", "S. Brand"],
              ["Tag 3 15:00", "Abschlussbesprechung, Bewertung", "Werkleitung + Audit-Team"]]),
            ("Erforderliche Unterlagen (Vorbereitung)",
             ("list", [
                 "Aktuelles Q-Handbuch IATF 16949 Rev. 4.2",
                 "ppm-Trend rollierend 12 Monate je Programm",
                 "8D-Reports der letzten 12 Monate (Kunde) inkl. Wirksamkeitsmessung",
                 "Lieferanten-Audit-Plan und Audit-Ergebnisse Tier-2",
                 "Aktuelle PFMEA / Control Plans der zu auditierenden Linien",
                 "Lessons-Learned-Dokumentation aus Vorjahres-Audit",
             ])),
            ("Logistik",
             "Hotel-Empfehlung: Mercure Hotel Heilbronn (5 km Werk); Reservierung wird gerne "
             "uebernommen. Werks-Sicherheitsbelehrung Tag 1 09:00 verbindlich; PSA wird gestellt "
             "(Sicherheitsschuhe Groesse / Brille). NDA-Unterzeichnung Tag 1 vor Audit-Start "
             "erforderlich."),
            ("Ansprechpartner",
             "Brennhagen-seitig: Sabine Brand (Q-Leitung REG Heilbronn, Tel. +49 7131 / 1234-810), "
             "Werkleiter Andreas Maier (Tel. -800), Programm-Koordinator (n. n.). "
             "Bitte Audit-Team-Liste sowie Pruefumfangs-Detail bis +14 AT vor Termin uebermitteln."),
            ("Unterschriften",
             signatures("Sabine Brand", "Q-Leitung REG", R["name"],
                        o["qmb"], "QMB", o["legal"],
                        place="Heilbronn", date_str_=f"15. " + ("April" if jahr=="2021" else "Juli" if jahr=="2022" else "Januar") + " " + jahr)),
        ])


def doc_audit_bericht(fname, oem_key, jahr):
    o = OEM[oem_key]
    write_doc(BASE / fname, H,
        f"Kundenaudit-Bericht {o['full']} {jahr}",
        subtitle=f"Bericht zum Lieferantenaudit der {o['full']} bei Brennhagen Elektronik AG (Werk Heilbronn)",
        sections=[
            ("Audit-Identifikation",
             [["Position", "Wert"],
              ["Audit-Art", "VDA 6.3 Prozessaudit + Produktaudit Stichprobe"],
              ["Kunde", o['legal']],
              ["Audit-Team", f"{o['qmb']} (Lead), {o['sqe']} (SQE), 1 weiterer Auditor"],
              ["Audit-Datum", "12.-14. September " + jahr],
              ["Auditierter Standort", "Brennhagen Elektronik GmbH, Werk Heilbronn"],
              ["Audit-Umfang", "Programme " + oem_key + " ICP-3 / BMS-12 / ADAS-V4D / ECU-900"],
              ["Abschluss / Bericht", "30 Tage nach Audit-Ende"]]),
            ("Audit-Ergebnis (Gesamtbewertung)",
             "Gesamtbewertung: A (sehr guter Lieferant; Empfehlung zur weiteren Vergabe). "
             "Erreichte Punktzahl: " + str(89 + (hash(oem_key) % 8)) + " / 100. "
             "Keine Major Non-Conformities; 3 Minor Non-Conformities mit Massnahmen "
             "(siehe nachfolgend); 5 Verbesserungspotenziale."),
            ("Minor Non-Conformities",
             [["NC-Nr.", "Befund", "Massnahme Brennhagen", "Frist"],
              ["NC-01", "PFMEA Linie 3 nicht vollstaendig aktualisiert nach ECR-2023-001",
               "Aktualisierung + Re-Approval", "+30 AT"],
              ["NC-02", "Tier-2 Audit-Plan 2023 nur zu 78 % erfuellt (Soll 90 %)",
               "Plan-Anpassung + 4 Audits Q4", "+60 AT"],
              ["NC-03", "Schichtleiter-Schulung IATF 16949 Rev. 4.2 nicht dokumentiert",
               "Nachschulung + Doku", "+45 AT"]]),
            ("Verbesserungspotenziale",
             ("list", [
                 "VP-01: Einfuehrung digitaler Pruefprotokolle (papierlos) bis Q2 " + str(int(jahr)+1),
                 "VP-02: Erweiterung statistische Prozesskontrolle (Cpk-Reporting) auf Linie 4",
                 "VP-03: Mitarbeiter-Rotation zwischen Linien zur Cross-Skill-Erhoehung",
                 "VP-04: Aufbau Predictive-Maintenance fuer SMD-Bestueckungsautomat",
                 "VP-05: Aktualisierung Lieferanten-Auditfragenkatalog auf VDA 6.3 Rev. 2023",
             ])),
            ("Staerken",
             "Audit-Team hob folgende Staerken explizit hervor: (1) Hohe ppm-Stabilitaet ueber alle "
             "Programme; (2) Sehr gute Dokumentationsdisziplin (8D, FMEA, Control Plan); (3) "
             "Vorbildliches Verbesserungs-Management (KAIZEN-Workshops monatlich); (4) "
             "Eindeutiges Commitment der Werkleitung zur Qualitaet."),
            ("Naechste Schritte / Massnahmenverfolgung",
             "Massnahmenplan in WebQM (Kunden-Portal) zu hinterlegen bis +30 AT. "
             "Wirksamkeitspruefung der Massnahmen im Folge-QBR " + str(int(jahr)+1) + " Q1. "
             "Nachstes Vollaudit voraussichtlich im 3. Quartal " + str(int(jahr)+2) + " (geplant). "
             "Bei Nicht-Schliessung NC-01 bis +30 AT: Eskalation an Werkleiter."),
            ("Unterschriften",
             signatures(o['qmb'], "Lead Auditor", o['legal'],
                        "Sabine Brand", "Q-Leitung REG", R["name"],
                        place="Heilbronn", date_str_=f"15. Oktober {jahr}")),
        ])


# ── 9. CSR / Qualitaetsvereinbarung ───────────────────────────────────────
def doc_csr(fname, oem_key, jahr):
    o = OEM[oem_key]
    write_doc(BASE / fname, H,
        f"Kundenspezifische Anforderungen (CSR) {o['full']} – Stand {jahr}",
        subtitle="Customer-Specific Requirements zur Ergaenzung von IATF 16949 / VDA 6.3",
        sections=[
            ("Geltungsbereich",
             f"Diese Customer-Specific Requirements ({o['kuerzel_intern']}-CSR Rev. " + jahr +
             f") gelten fuer alle Lieferungen der Brennhagen Elektronik AG an {o['legal']} "
             f"sowie an die OEM-Werke {o['werk']}. Sie ergaenzen die IATF-16949-Anforderungen "
             f"sowie die VDA-6.3-Auditkriterien. Im Konfliktfall geht die Kundenanforderung vor."),
            ("1. Qualitaetsanforderungen",
             ("list", [
                 "ppm-Ziel < 25 (rollierend 3 Monate) fuer Standard-Programme",
                 "ppm-Ziel < 15 fuer sicherheitsrelevante Steuergeraete (ASIL-C/D)",
                 "0-ppm-Politik fuer Audits-Befunde Klasse A (Major)",
                 "Lifetime-Garantie 5 Jahre / 150.000 km fuer ADAS-V4D, BMS-12",
                 "8D-Frist: D3 binnen 24 h, D5 binnen 14 Tagen, D8 binnen 90 Tagen",
                 "Wirksamkeitsmessung verpflichtend (in WebQM-Portal zu dokumentieren)",
             ])),
            ("2. Logistik / Lieferanforderungen",
             ("list", [
                 "OTD-Ziel 98,5 % (3-Monatsrollend); Eskalation < 95 %",
                 "12-Wochen-Frozen-Zone fuer Lieferabrufe (VDA 5009)",
                 "EDI-Anbindung VDA 4905/4915 obligatorisch (keine Fax/Email-Abrufe)",
                 "JIS (Just-in-Sequence) fuer ICP-3, ADAS-V4D",
                 "Verpackung VDA 4500 (KLT); Mehrweg-Behaelterpool des Kunden zu verwenden",
                 "Sondertransporte: zu Lasten der verursachenden Partei",
             ])),
            ("3. Aenderungsmanagement",
             "Saemtliche Aenderungen unterliegen dem ECR-/PPAP-Verfahren des Kunden. "
             "Re-PPAP Level 3 bei: Material-/Lieferanten-Wechsel kritischer Komponenten, "
             "Werkzeug-Umzug, Werks-Verlagerung, Software-Major-Release. "
             "Re-PPAP Level 2 bei nicht-kritischen Aenderungen."),
            ("4. Lieferantenmanagement (Sub-Tier)",
             "Brennhagen verpflichtet sich, die CSR-Anforderungen 1:1 an seine kritischen "
             "Sub-Lieferanten zu kaskadieren (insb. Halbleiter-Hersteller: Infineon, NXP, ST, "
             "Texas Instruments). Sub-Tier-Audit-Frequenz mindestens 1x in 24 Monaten je "
             "kritischem Lieferanten. Dokumentation in Brennhagen-Lieferantenmanagement-System."),
            ("5. Compliance / Nachhaltigkeit",
             ("list", [
                 "Lieferantenkodex des Kunden vom Vorstand unterzeichnet (Anhang)",
                 "LkSG-Compliance: Jaehrliche Selbstauskunft + Risiko-Assessment",
                 "Konfliktmineralien CMRT-Reporting (RMI 6.21+) quartalsweise",
                 "CO2-Footprint Scope 1+2 Reporting jaehrlich (CDP)",
                 "CO2-Zielpfad -30 % bis 2030 (Basis 2020), -50 % bis 2035",
             ])),
            ("6. Vertraulichkeit / IT-Security",
             "TISAX-Label (Stufe AL3) verpflichtend; Audit alle 3 Jahre durch akkreditierte "
             "Audit-Provider (z. B. TUEV Sued). Datenaustausch ueber Kunden-Portal mit "
             "MFA; PDFs / Anhaenge mit AES-256 Verschluesselung. Zugriffsrechte: Need-to-know-"
             "Prinzip."),
            ("Unterschriften",
             signatures("Sabine Brand", "Q-Leitung REG", R["name"],
                        o["qmb"], "QMB", o["legal"],
                        place="Stuttgart", date_str_=f"01. Maerz {jahr}")),
        ])


def doc_qsv(fname, oem_key, jahr):
    o = OEM[oem_key]
    write_doc(BASE / fname, H,
        f"Qualitaetssicherungsvereinbarung (QSV) {o['full']} ({jahr})",
        subtitle="Vereinbarung zur Qualitaet der Liefer- und Leistungsbeziehung gemaess IATF 16949 / VDA 6.3",
        sections=[
            ("Vertragsparteien", addr_block(oem_key)),
            ("Praeambel",
             f"Die Parteien vereinbaren hiermit die Bedingungen der Qualitaetssicherung in der "
             f"Lieferbeziehung zwischen {o['legal']} und der Brennhagen Elektronik AG. Diese QSV "
             f"ergaenzt den Rahmenliefervertrag (siehe REA_{oem_key}_Rahmenliefervertrag_2022) und "
             f"hat Vorrang vor Allgemeinen Einkaufsbedingungen, soweit die Qualitaetssicherung "
             f"betroffen ist."),
            ("§ 1 Qualitaets-Managementsystem",
             "Brennhagen betreibt fuer alle in dieser QSV erfassten Lieferungen ein Q-Management-"
             "System gemaess IATF 16949:2016 (juengstes Re-Zertifikat: " + str(int(jahr)-1) +
             "; naechstes Surveillance-Audit Q3 " + jahr + "). Sub-Tier-Lieferanten sind ent"
             "sprechend qualifiziert (mindestens ISO 9001:2015; kritische: IATF 16949)."),
            ("§ 2 Qualitaetsziele",
             [["KPI", "Ziel"],
              ["ppm (rollierend 3 Mon., Standard-Programme)", "< 25"],
              ["ppm (rollierend 3 Mon., ASIL-C/D)", "< 15"],
              ["OTD (rollierend 3 Mon.)", "> 98,5 %"],
              ["8D D3-Frist", "24 Stunden"],
              ["8D D5-Frist", "14 Tage"],
              ["8D D8 (Wirksamkeit)", "90 Tage"]]),
            ("§ 3 Erstmuster (PPAP / VDA Band 2)",
             "Erstmuster werden gemaess AIAG PPAP 4th Edition bzw. VDA Band 2 (3-stufig) "
             "vorgelegt. Standard-Level fuer Programme: Level 3. Bei Wiederholungs-Lieferungen "
             "nach Aenderung: Re-PPAP gemaess kundenspezifischer Festlegung. Pruefdokumentation "
             "(Erstmusterpruefbericht, IMDS-Eintrag, CMK-/CPK-Werte) zu uebergeben."),
            ("§ 4 Serienlieferung",
             "Stichprobenpruefung erfolgt bei Brennhagen gemaess Pruefplan (AQL 0,65 fuer Standard, "
             "AQL 0,15 fuer ASIL-C/D). Brennhagen betreibt 100-%-Pruefstationen fuer "
             "sicherheitsrelevante Funktionen. Pruefdaten werden 15 Jahre archiviert."),
            ("§ 5 Reklamationsmanagement",
             "Bei Reklamation 8D-Report gemaess VDA Schritte D1-D8. Sortierkosten / "
             "Nacharbeit / Lieferengpass-Kosten gehen bei nachweislicher Verursachung zu "
             "Lasten Brennhagens. Sofortmassnahmen (D3) binnen 24 h; Sortier-/Block-Aktion "
             "bei kritischen Befunden sofort."),
            ("§ 6 Sicherheitsbeauftragte / PSCR",
             "Brennhagen benennt fuer jedes ASIL-C/D-Programm eine/n Product Safety & Conformity "
             "Representative (PSCR) gemaess IATF 16949 Anhang B; aktueller Konzern-PSCR-Koordinator: "
             "Sabine Brand (REG Heilbronn). Kunde benennt entsprechende Funktion (" + o['qmb'] + ")."),
            ("§ 7 Aenderungen und Wirksamkeit",
             "Aenderungen dieser QSV beduerfen der Schriftform; muendliche Nebenabreden bestehen "
             "nicht. Laufzeit: unbegrenzt; Kuendigung mit 6 Monaten zum Quartalsende moeglich. "
             "Diese QSV tritt mit beidseitiger Unterzeichnung in Kraft."),
            ("Unterschriften",
             signatures("Sabine Brand", "Q-Leitung REG", R["name"],
                        o["qmb"], "QMB", o["legal"],
                        place="Stuttgart", date_str_=f"15. Februar {jahr}")),
        ])


# ── 10. ESKALATION / KUENDIGUNG / NACHTRAG / CLAIM / LOB / VERSORGUNG ────
def doc_eskalation(fname, oem_key, jahr):
    o = OEM[oem_key]
    write_doc(BASE / fname, H,
        f"Eskalationsbrief Lieferengpass {o['full']} – {jahr}",
        subtitle="Mitteilung gemaess Rahmenliefervertrag § 5 (Liefersicherheit) und Sofortmassnahmen",
        sections=[
            ("Adressat", addr_block(oem_key)),
            ("Eskalationsanlass",
             f"Sehr geehrte/r {o['kontakt']},\n\n"
             f"hiermit teilen wir Ihnen mit, dass die Brennhagen Elektronik AG ab "
             + ("KW 28 " if jahr=="2021" else "KW 35 ") + jahr +
             f" mit einer kritischen Liefer-Unterdeckung fuer die Programme ICP-3, BMS-12, "
             f"ECU-900 (kombinierte Wirkung: ca. 18-22 % der vereinbarten Liefermenge) "
             f"konfrontiert sein wird. Ursache: ausserordentliche Halbleiter-Allokation bei "
             f"Infineon (AURIX TC39x) und NXP (S32K3) infolge der Wafer-Knappheit bei TSMC N7."),
            ("Geplante Massnahmen Brennhagen",
             ("list", [
                 "Krisen-Task-Force unter Leitung Stefan Hoffmann (CTO) ab sofort etabliert; "
                 "Tagungsfrequenz: 2x woechentlich (Mo/Do, 14:00).",
                 "Sofortige Verhandlung mit Infineon und NXP fuer Aufstockung der Allokation "
                 "(Standorte Dresden, Regensburg, Toulouse).",
                 "Aufbau Sicherheitsbestand auf 4 Wochen (Kosten ca. 8,5 Mio. EUR; vorab "
                 "vom Vorstand genehmigt).",
                 "Pruefung Cross-Production zwischen REG Heilbronn und RPL Katowice (SMD).",
                 "Wertanalyse / Re-Design Eskalation: Pruefung alternativer MCUs (Renesas RH850, "
                 "ST SPC58); ASPICE-Re-Validation und Re-PPAP Level 3 erforderlich (Zeitbedarf "
                 "12-16 Wochen).",
             ])),
            ("Bitten / Anforderungen an den Kunden",
             ("list", [
                 "Verbindliche Bestaetigung der Mindest-Liefermengen je Programm bis +5 AT.",
                 "Prioritaeten-Festlegung Werke (welche Werke / Modelle absolute Vorrang haben).",
                 "Verzicht auf Sondertransport-Eskalation in betroffener Phase (Notbestaende).",
                 "Vorbehaltlich-Erklaerung Anwendung Liefer-Pönalen (sondergeregelt waehrend Eskalation).",
                 "Joint-Steering-Termin mit Geschaeftsleitung beider Parteien innerhalb 14 Tagen.",
             ])),
            ("Erwartete Auswirkungen",
             "Wir gehen davon aus, dass die Engpass-Situation bis "
             + ("Q1 2022" if jahr=="2021" else "Q1 2023") +
             " geloest werden kann. Die Mindest-Liefermengen koennen mit hoher Wahrscheinlichkeit "
             "gehalten werden; eine vollstaendige Plan-Erfuellung haengt jedoch von der "
             "Allokations-Entwicklung am Halbleiter-Markt ab. Wir werden im 14-taegigen Rhythmus "
             "Status-Updates uebermitteln."),
            ("Naechste Schritte",
             "Wir bitten um umgehende Stellungnahme und ggf. die Vereinbarung eines "
             "Joint-Steering-Termins (Brennhagen-seitig: Stefan Richter CMO, Stefan Hoffmann CTO; "
             "Kunden-seitig: " + o['kontakt'] + ", Werkleitung). Anlagen: Liefer-Forecast je "
             "Programm (KW " + ("28-52 " if jahr=="2021" else "35-52 ") + jahr + "), "
             "Stuecklisten der betroffenen Halbleiter."),
            ("Unterschriften",
             signatures("Stefan Richter", "CMO / BD", R["name"],
                        "Stefan Hoffmann", "CTO", R["name"],
                        place="Stuttgart", date_str_=f"10. " + ("Juli" if jahr=="2021" else "August") + " " + jahr)),
        ])


def doc_kuendigung_androhung(fname, oem_key, jahr):
    o = OEM[oem_key]
    write_doc(BASE / fname, H,
        f"Androhung der Vertragskuendigung – Rahmenliefervertrag {oem_key} ({jahr})",
        subtitle="Schreiben gemaess § 314 BGB; Verbesserungs-Frist und Eskalationsverfahren",
        sections=[
            ("Adressat (Brennhagen-seitig erhalten)", addr_block(oem_key)),
            ("Sachverhalt",
             f"Mit Schreiben vom " + ("12. Maerz " if jahr=="2021" else "08. April " if jahr=="2022" else "22. Februar ") + jahr +
             f" hat uns die {o['legal']} eine Androhung der Kuendigung des Rahmenliefervertrages "
             f"vom 14. Maerz 2022 zugestellt. Anlass: Nichterfuellung definierter Q- und Liefer-KPIs "
             f"in den letzten 6 Monaten (ppm-Ueberschreitungen Programm ADAS-V4D, OTD < 95 % in 3 "
             f"aufeinanderfolgenden Monaten, Eskalations-Verzug bei 8D-Reports). "
             f"Eine 90-taegige Frist zur Nachbesserung wurde eingeraeumt."),
            ("Beanstandungspunkte",
             [["Beanstandung", "Q-Detail", "Kunden-Erwartung"],
              ["ppm-Ueberschreitung ADAS-V4D",
               "Wert 42 ppm (Ziel 25 ppm) ueber 4 Monate",
               "ppm < 25 binnen 60 Tagen"],
              ["OTD-Unterdeckung",
               "92 % (Ziel > 98,5 %) im Quartal",
               "OTD > 98,5 % nachweisbar binnen 90 Tagen"],
              ["8D-Reporting-Verzug",
               "3 Reports mit Frist-Ueberschreitung D5",
               "100 % Termintreue D3/D5/D8"],
              ["Eskalations-Verhalten",
               "Kunden-Eskalation nicht angemessen reagiert",
               "Reaktionszeit < 4 h, schriftliche Stellungnahme < 24 h"]]),
            ("Brennhagen-Sofortmassnahmen",
             ("list", [
                 "Krisen-Task-Force unter Leitung Werkleiter Andreas Maier (REG Heilbronn).",
                 "100-%-Pruefung Linie ADAS-V4D mit Inline-Roentgen (Zeitbedarf 14 Tage zur Inbetriebnahme).",
                 "Sofortige PFMEA-Aktualisierung mit dem Kunden (Joint-Workshop KW " + str(15 + (hash(jahr)%5)) + ").",
                 "Eskalations-Hotline Q-Themen (Stefan Hoffmann CTO / Sabine Brand Q-Leitung).",
                 "Liefer-Eskalations-Plan mit taeglichem Reporting an Kunden-Werkleitung.",
             ])),
            ("Verbesserungsplan und Meilensteine",
             "Brennhagen verpflichtet sich zur Erreichung folgender Meilensteine binnen 90 Tagen: "
             "(1) ppm < 25 bei ADAS-V4D mit Q-Wirksamkeitsmessung; (2) OTD > 98 % rollierend 4 Wochen; "
             "(3) 100 % Termintreue 8D D3/D5/D8; (4) Joint-Audit mit Kunden-Audit-Team binnen 30 "
             "Tagen. Der Erfuellungsstand wird woechentlich an "
             + o['kontakt'] + " sowie an die Kunden-Q-Leitung " + o['qmb'] + " berichtet."),
            ("Eskalation bei Nicht-Erfuellung",
             "Bei Nicht-Erfuellung der Meilensteine binnen 90 Tagen behaelt sich der Kunde die "
             "ausserordentliche Kuendigung gemaess § 314 BGB sowie die Re-Sourcing-Aktion fuer die "
             "betroffenen Programme vor. Brennhagen wird im worst case mit einem Volumenverlust von "
             "schaetzungsweise " + str(120 + (hash(oem_key) % 80)) + " Mio. EUR rechnen muessen. "
             "Eine Vorstand-Eskalation an Anna Mueller (CEO) und das Aufsichtsrats-Pruefungs-"
             "Komitee (Prof. Voss) wurde am " +
             ("18.03." if jahr=="2021" else "14.04." if jahr=="2022" else "28.02.") + jahr +
             " durchgefuehrt."),
            ("Unterschriften",
             signatures("Stefan Richter", "CMO / BD", R["name"],
                        "Anna Mueller", "CEO", R["name"],
                        place="Stuttgart", date_str_=f"22. " + ("Maerz" if jahr=="2021" else "April" if jahr=="2022" else "Februar") + " " + jahr)),
        ])


def doc_nachtrag(fname, oem_key, jahr):
    o = OEM[oem_key]
    write_doc(BASE / fname, H,
        f"Vertragsnachtrag {oem_key} ({jahr})",
        subtitle="Ergaenzung zum Rahmenliefervertrag bzw. zu Einzelliefervertraegen",
        sections=[
            ("Vertragsparteien", addr_block(oem_key)),
            ("Gegenstand",
             f"Hiermit vereinbaren die Parteien folgende Aenderungen / Ergaenzungen zu den "
             f"bestehenden Vertraegen (Rahmenliefervertrag vom 14. Maerz 2022 sowie produkt"
             f"bezogene Einzelliefervertraege ICP-3 / BMS-12 / ADAS-V4D / ECU-900). Der Nachtrag "
             f"tritt mit beidseitiger Unterzeichnung in Kraft."),
            ("Aenderungspunkte",
             ("clauses", [
                 ("§ 1 Anpassung Material-Pass-Through-Klausel",
                  ["Der bisherige Quartals-Index fuer Halbleiter (Wafer Composite SEMI/SIA) wird "
                   "um den Forecasted Index Wafer Pricing (Quelle TrendForce) ergaenzt. Wirkung: "
                   "Monatliche statt quartalsweise Anpassung fuer kritische Halbleiter.",
                   "Die Pass-Through-Quote wird einheitlich auf 95 % festgelegt (5 % Productivity-"
                   "Beteiligung Brennhagen). Vorher zwischen Programmen unterschiedlich (75-95 %)."]),
                 ("§ 2 Erweiterung Sondergarantie",
                  ["Sondergarantie fuer BMS-12 wird von 5 Jahre / 150.000 km auf 8 Jahre / "
                   "160.000 km erweitert (Anforderung aus OEM-Roadmap E-Mobility).",
                   "Stueckpreis-Anpassung: +0,80 EUR / Einheit ab Wirksamkeit Nachtrag."]),
                 ("§ 3 Volumen-Adjustment",
                  ["Plan-Jahresvolumen BMS-12 wird auf Basis aktualisierter OEM-Forecast von "
                   "220.000 auf 245.000 Einheiten erhoeht; entsprechende Kapazitaets-Reservierung "
                   "REG Heilbronn Linie 4 wird durch Brennhagen vorgenommen.",
                   "Anschubfinanzierung Kapazitaetsausbau: Kunde traegt 35 % von 12,4 Mio. EUR "
                   "(= 4,3 Mio. EUR), verteilt auf erste 12 Lieferzyklen."]),
                 ("§ 4 Restbestimmungen",
                  ["Alle uebrigen Bestimmungen der bestehenden Vertraege bleiben unveraendert.",
                   "Vorrangregelung: dieser Nachtrag vor Rahmenvertrag / Einzelvertrag."]),
             ])),
            ("Unterschriften",
             signatures("Stefan Richter", "CMO / BD", R["name"],
                        o["kontakt"], o["rolle"], o["legal"],
                        place="Stuttgart", date_str_=f"14. Oktober {jahr}")),
        ])


def doc_versorgung(fname, oem_key, jahr):
    o = OEM[oem_key]
    write_doc(BASE / fname, H,
        f"Versorgungsbestaetigung {o['full']} ({jahr})",
        subtitle="Brennhagen-Bestaetigung der Liefersicherheit fuer die Programme des Kunden",
        sections=[
            ("Adressat", addr_block(oem_key)),
            ("Bestaetigung der Liefersicherheit",
             f"Sehr geehrte/r {o['kontakt']},\n\n"
             f"hiermit bestaetigen wir Ihnen die Liefersicherheit fuer Ihre Programme "
             f"ICP-3, BMS-12, ADAS-V4D, ECU-900 fuer das Geschaeftsjahr {jahr} sowie das "
             f"Folgejahr {int(jahr)+1} auf Basis der unten genannten Volumenzusagen.\n\n"
             f"Wir bestaetigen die Verfuegbarkeit der notwendigen Werks-Kapazitaeten "
             f"(REG Heilbronn Linien 1-4, RPL Katowice SMD) sowie die Allokation der "
             f"kritischen Halbleiter (Infineon AURIX, NXP S32, TSMC Wafer-Kontingente)."),
            ("Plan-Volumen je Programm",
             [["Programm", f"Plan {jahr} (Einheiten)", f"Plan {int(jahr)+1} (Einheiten)"],
              ["ICP-3", "170.000", "180.000"],
              ["BMS-12", "220.000", "245.000"],
              ["ADAS-V4D", "95.000", "110.000"],
              ["ECU-900", "145.000", "152.000"]]),
            ("Kapazitaets- und Risikobewertung",
             "Werks-Kapazitaet ist abgesichert: (1) REG Heilbronn Linie 1-4 mit verbindlicher "
             "Erweiterung Linie 4 (Investitionsfreigabe 28,4 Mio. EUR durch Vorstand am 14.09." + str(int(jahr)-1) +
             "); (2) RPL Katowice SMD-Erweiterung um 15 % (Investition 6,2 Mio. EUR). "
             "Halbleiter-Allokation: Long-term Agreements mit Infineon (laufend bis 2030), "
             "NXP (laufend bis 2028), Renesas (Aufbau zweite Quelle in Pruefung)."),
            ("Verbleibende Risiken",
             ("list", [
                 "Restrisiko Halbleiter-Marktallokation TSMC N5/N7 (Backup-Strategie aktiv)",
                 "Restrisiko Lieferkette China (Aufbau zweite Quelle in Pruefung)",
                 "Restrisiko Werks-Auslastung bei OEM-Volumen-Verschiebung > 25 %",
                 "Restrisiko Energiekosten (durch Hedging Erdgas/Strom abgesichert bis Q4 " + str(int(jahr)+1) + ")",
             ])),
            ("Unterschriften",
             signatures("Stefan Richter", "CMO / BD", R["name"],
                        "Andreas Maier", "Werkleiter REG", R["name"],
                        place="Stuttgart", date_str_=f"15. Dezember {jahr}")),
        ])


def doc_langfrist(fname, oem_key, jahr):
    o = OEM[oem_key]
    write_doc(BASE / fname, H,
        f"Langfristlieferzusage {o['full']} ({jahr})",
        subtitle="Verbindliche mehrjaehrige Liefer- und Volumenzusage zur Programmstabilitaet",
        sections=[
            ("Adressat", addr_block(oem_key)),
            ("Inhalt der Zusage",
             f"Die Brennhagen Elektronik AG bestaetigt hiermit der {o['legal']} eine mehrjaehrige "
             f"Liefer- und Volumenzusage fuer die Programme ICP-3, BMS-12, ADAS-V4D, ECU-900 "
             f"ueber den Zeitraum {jahr} bis {int(jahr)+5}. Die Zusage umfasst Werks-Kapazitaet, "
             f"Material-Allokation und Productivity-Verpflichtung gemaess Rahmenvertrag § 4."),
            ("Volumen-Korridor (Mehrjahres-Plan)",
             [["Programm", f"Plan {jahr}", "Plan +1", "Plan +2", "Plan +3", "Plan +4", "Plan +5"],
              ["ICP-3 (Tsd. Einheiten)", "170", "180", "175", "165", "150", "120"],
              ["BMS-12 (Tsd. Einheiten)", "220", "245", "265", "270", "265", "250"],
              ["ADAS-V4D (Tsd. Einheiten)", "95", "110", "120", "125", "120", "105"],
              ["ECU-900 (Tsd. Einheiten)", "145", "152", "150", "145", "130", "100"]]),
            ("Productivity-Pfad",
             "Verbindliche Productivity-Beteiligung gemaess Rahmenvertrag § 4: 1,5 - 3,0 % p. a. "
             "(Mittelwert 2,0 %). Wirkung auf Stueckpreis ueber 6 Jahre kumuliert ca. -11,4 %. "
             "Material-Pass-Through-Klausel wirkt unabhaengig (siehe Anhang 3 Rahmenvertrag)."),
            ("Investitionsfreigaben",
             "Brennhagen hat fuer die Erfuellung der Zusage folgende Investitionen freigegeben: "
             "(1) REG Heilbronn Linie 4 (BMS-12) – 28,4 Mio. EUR / SOP Q1 2024; "
             "(2) RPL Katowice SMD-Erweiterung – 6,2 Mio. EUR / SOP Q3 2023; "
             "(3) RSG Muenchen Software-Erweiterung (ADAS) – 18 FTE-Aufbau ueber 24 Monate; "
             "(4) Inline-Roentgen REG Linie 1 (ADAS-V4D) – 1,4 Mio. EUR / SOP Q4 2023."),
            ("Vorbehalte",
             "Die Zusage steht unter Vorbehalt: (1) Erfuellung der Q-Anforderungen durch Brennhagen; "
             "(2) Material-Verfuegbarkeit Halbleiter (LoA Infineon, NXP bis 2030); "
             "(3) Keine wesentliche Verschiebung der OEM-Volumen-Forecasts ueber 25 %; "
             "(4) Bestaetigung der Allgemeinen Material-Pass-Through-Klausel."),
            ("Unterschriften",
             signatures("Stefan Richter", "CMO / BD", R["name"],
                        "Anna Mueller", "CEO", R["name"],
                        place="Stuttgart", date_str_=f"08. November {jahr}")),
        ])


def doc_claim(fname, oem_key, jahr):
    o = OEM[oem_key]
    nr = "".join(filter(str.isdigit, fname.split("Claim")[-1])) or "0000"
    write_doc(BASE / fname, H,
        f"Lieferanten-Claim {o['full']} #{nr} ({jahr})",
        subtitle="Beanstandung des Kunden / Stellungnahme Brennhagen und Bearbeitungsstand",
        sections=[
            ("Claim-Identifikation",
             [["Position", "Wert"],
              ["Claim-Nummer Kunde", f"{oem_key}-CL-{jahr}-{nr}"],
              ["Eingang Brennhagen", "12.0" + str(2 + (hash(nr) % 8)) + "." + jahr],
              ["Betroffenes Programm", "ICP-3 / BMS-12 (gemischt)"],
              ["Betroffene Charge", f"CH-{jahr}-W{15 + (hash(nr) % 30)}"],
              ["Reklamierte Menge", f"{(hash(nr) % 800) + 120} Einheiten"],
              ["Befund", "Loetstellen-Anomalie an Power-MOSFET (3 Zellen je Modul)"],
              ["Eskalations-Stufe", "Q-Eskalation 2 (Programm-Leiter / SQE)"],
              ["Bearbeiter Brennhagen", "Sabine Brand (Q-Leitung REG Heilbronn)"]]),
            ("Sachverhalt",
             f"Der Kunde meldete am Eingangsdatum eine Loetstellen-Anomalie an Charge "
             f"CH-{jahr}-W{15 + (hash(nr) % 30)}, gefunden bei Endpruefung im Werk {o['werk'].split('/')[0].strip()}. "
             f"Auffaellig waren ca. 0,8 % der ausgelieferten Module mit messbarer Loetstellen-"
             f"Resonanz; Anwendungsspezifisch noch nicht ausfallrelevant, aber unter dem "
             f"langfristigen ppm-Ziel. Brennhagen hat umgehend D3-Sofortmassnahmen eingeleitet "
             f"(100-%-Pruefung lfd. Charge + Sortierung Bestand Kunde)."),
            ("8D-Bearbeitungsstand",
             [["Schritt", "Stand", "Termin"],
              ["D1 Team", "abgeschlossen", "13.0" + str(2 + (hash(nr) % 8)) + "." + jahr],
              ["D2 Problembeschreibung", "abgeschlossen", "14.0" + str(2 + (hash(nr) % 8)) + "." + jahr],
              ["D3 Sofortmassnahmen", "abgeschlossen", "16.0" + str(2 + (hash(nr) % 8)) + "." + jahr],
              ["D4 Ursachenanalyse (Root Cause)", "abgeschlossen", "+14 AT"],
              ["D5 Massnahmen-Auswahl", "abgeschlossen", "+21 AT"],
              ["D6 Implementierung", "in Bearbeitung", "+30 AT"],
              ["D7 Praevention", "geplant", "+45 AT"],
              ["D8 Wirksamkeit", "geplant", "+90 AT"]]),
            ("Root Cause (D4)",
             "Erhoehte Schwankung der SMD-Loet-Temperatur an Bestueckungsautomat L3-04 "
             "(Werk Heilbronn) infolge defekten Temperaturfuehlers (Drift +3 K nicht erkannt). "
             "Folge: Suboptimale Loetqualitaet an Power-MOSFETs (lokales Voiding > 12 %)."),
            ("Massnahmen (D5/D6)",
             ("list", [
                 "Sofortiger Austausch Temperaturfuehler (erfolgt 16." +
                     str(2 + (hash(nr) % 8)) + "." + jahr + "; Kosten 1.840 EUR).",
                 "Erweiterung Pruefumfang auf 100-%-Roentgen alle Power-MOSFETs (Linie 1+3) "
                 "bis Wirksamkeitsmessung.",
                 "Implementierung redundante Temperatur-Ueberwachung mit Drift-Alarm.",
                 "PFMEA-Update Linie 3 (Position 14: Loetfehler-Schwere D von 5 auf 7 erhoeht).",
                 "Joint-Walkthrough mit Kunden-SQE " + o['sqe'] + " in KW " + str(int(jahr[-1])*8 + 4) + ".",
             ])),
            ("Kostenuebernahme",
             "Sortierkosten Bestand Kunde (1.240 EUR Personal + 480 EUR Logistik) sowie Nach"
             "lieferung der Ersatzteile (4.380 EUR Material) gehen zu Lasten Brennhagen (Verursacher"
             "prinzip). Gesamtbelastung dieses Claims: 7.940 EUR; Q-Reserve ausreichend (Bestand "
             "REG Heilbronn 145 TEUR Q-Ruckstellung 2023)."),
            ("Unterschriften",
             signatures("Sabine Brand", "Q-Leitung REG", R["name"],
                        o["qmb"], "QMB", o["legal"],
                        place="Heilbronn", date_str_=f"30. " + ("Maerz" if jahr=="2022" else "Juli") + " " + jahr)),
        ])


def doc_claim_letter(fname, oem_key, jahr):
    o = OEM[oem_key]
    write_doc(BASE / fname, H,
        f"Claim-Letter {o['full']} ({jahr})",
        subtitle="Schreiben des Kunden mit Sammel-Reklamationen / Stellungnahme Brennhagen",
        sections=[
            ("Adressat / Vorgang", addr_block(oem_key)),
            ("Sachverhalt",
             f"Der Kunde hat mit Datum vom " + ("15.03." if jahr=="2021" else "18.04." if jahr=="2022" else "22.05.") + jahr +
             f" einen Sammel-Claim ueber " + str(3 + (hash(jahr) % 6)) + " Einzel-Reklamationen aus den "
             f"vergangenen 6 Monaten zugestellt. Schwerpunkt: Q-Themen Programm ADAS-V4D "
             f"(ppm-Ueberschreitung), Lieferverzug Programm ICP-3 (3 Sondertransporte), "
             f"Verzug 8D-Reporting bei 2 Vorgaengen."),
            ("Beanstandungspunkte",
             [["Vorgang", "Beanstandung", "Status Brennhagen"],
              ["CL-001", "ppm-Ueberschreitung ADAS-V4D (42 ppm > 25 ppm Ziel) ueber 4 Monate",
               "Q-Programm aktiv, Wirksamkeitsmessung Q4"],
              ["CL-002", "Sondertransport Last Mile Werk Sindelfingen 14.02. (3.200 EUR)",
               "Anerkannt; Kostenuebernahme erfolgt"],
              ["CL-003", "Sondertransport Werk Bremen 28.02. (2.840 EUR)",
               "Anerkannt; Kostenuebernahme erfolgt"],
              ["CL-004", "8D-D5-Verzug Vorgang Q-2023-018 (16 Tage)",
               "Verzug bestaetigt; Massnahme: Eskalations-Hotline 24/7"],
              ["CL-005", "8D-D5-Verzug Vorgang Q-2023-022 (12 Tage)",
               "Verzug bestaetigt; gleiche Massnahme wie CL-004"]]),
            ("Stellungnahme Brennhagen",
             "Die Brennhagen Elektronik AG bedauert die Beanstandungspunkte und nimmt sie sehr ernst. "
             "Wir haben unverzueglich Massnahmen ergriffen: (1) ppm-Verbesserungsprogramm ADAS-V4D "
             "unter Leitung Werkleiter A. Maier mit Joint-Workshops mit Kunden-SQE; "
             "(2) Verstaerkung der Logistik-Steuerung zur Reduktion von Sondertransporten "
             "(Ziel: max. 2 / Quartal); (3) 8D-Eskalations-Hotline (24/7) mit klaren "
             "Reaktionszeit-Vorgaben."),
            ("Kostenaspekte",
             "Brennhagen anerkennt die Sondertransport-Kosten in Hoehe von insgesamt "
             + str(6040 + (hash(jahr) % 2000)) + " EUR. Gutschrift wird im Folgemonat erfolgen. "
             "Weitere Kosten (Werks-Stoertage Kunde) werden im Detail-Termin geprueft und ggf. "
             "anteilig getragen (Verursacher-Anteil-Bewertung)."),
            ("Naechste Schritte",
             ("list", [
                 "Joint-Steering-Termin innerhalb 14 Tagen (Brennhagen: Stefan Richter, Stefan Hoffmann; Kunde: " + o['kontakt'] + ")",
                 "Detaillierter Verbesserungsplan Brennhagen binnen 21 Tagen",
                 "Wirksamkeitsmessung der Massnahmen im Folge-QBR",
                 "Re-Evaluation der Lieferanten-Bewertung des Kunden in 6 Monaten",
             ])),
            ("Unterschriften",
             signatures("Stefan Richter", "CMO / BD", R["name"],
                        o["kontakt"], o["rolle"], o["legal"],
                        place="Stuttgart", date_str_=f"30. " + ("Maerz" if jahr=="2021" else "April" if jahr=="2022" else "Mai") + " " + jahr)),
        ])


def doc_lob(fname, oem_key, jahr):
    o = OEM[oem_key]
    write_doc(BASE / fname, H,
        f"Lobesbrief / Top-Supplier-Award {o['full']} ({jahr})",
        subtitle=f"Auszeichnung der Brennhagen Elektronik AG durch den Kunden im Geschaeftsjahr {jahr}",
        sections=[
            ("Auszeichnung / Anlass",
             f"Sehr geehrte Frau Mueller, sehr geehrtes Vorstands-Team,\n\n"
             f"hiermit moechten wir Ihnen mitteilen, dass die {R['name']} im "
             f"Rahmen der jaehrlichen Lieferanten-Auszeichnung der {o['legal']} mit dem "
             f"»Supplier Award {jahr}« in der Kategorie »Best Electronics Tier-1« ausgezeichnet wurde. "
             f"Die feierliche Preisverleihung findet am 15. Februar {int(jahr)+1} im Rahmen der "
             f"Lieferanten-Konferenz in {o['addr'].split(',')[1].strip()} statt; Brennhagen-seitige Vertretung "
             f"durch Anna Mueller (CEO) und Stefan Richter (CMO)."),
            ("Bewertungskriterien",
             [["Kriterium", "Brennhagen-Punktzahl", "Bewertung"],
              ["Q-Performance (ppm, 8D, FMEA)", "94 / 100", "Hervorragend"],
              ["Liefer-Performance (OTD, Forecast)", "92 / 100", "Sehr gut"],
              ["Kostenmanagement (Productivity, Pass-Through)", "88 / 100", "Sehr gut"],
              ["Technologie / Innovation", "95 / 100", "Exzellent"],
              ["Nachhaltigkeit / CO2 / LkSG", "91 / 100", "Sehr gut"],
              ["Eskalations-/Kommunikationsverhalten", "90 / 100", "Sehr gut"],
              ["Gesamt", "92 / 100", "TOP-SUPPLIER"]]),
            ("Hervorgehobene Themen",
             "Der Kunde hob folgende Punkte besonders hervor: (1) Eindeutiges Commitment zur "
             "Q-Verbesserung mit nachweisbarer Wirkung (ppm-Reduktion von 35 auf 18 in 12 Monaten); "
             "(2) Vorbildliche Kommunikation in der Halbleiter-Krise 2022-23 (Transparente "
             "Eskalation und realistische Liefer-Forecasts); (3) Technologie-Fuehrerschaft beim "
             "Programm ADAS-V4D (4D-Radar-Fusion); (4) Hervorragende Zusammenarbeit beim "
             "BMS-12 Hochlauf (Werk-4-Anlauf ohne Stoerung)."),
            ("Auswirkungen / Outlook",
             "Mit der Top-Supplier-Auszeichnung ist Brennhagen in den »Preferred-Supplier-Pool« des "
             "Kunden aufgenommen und erhaelt damit bevorzugten Zugang zu RFQs neuer Programme der "
             "kommenden 3 Jahre. Wesentliche zu erwartende Programme: BMS-Generation NEUE KLASSE "
             "(BMW), ADAS-Generation Stellantis STLA Medium / Large, ICP-Generation Mercedes EVA2. "
             "Volumenpotenzial der Pipeline: 1,2-1,8 Mrd. EUR ueber 7 Jahre."),
            ("Unterschriften",
             signatures(o["kontakt"], o["rolle"], o["legal"],
                        "Anna Mueller", "CEO", R["name"],
                        place=o['addr'].split(',')[1].strip(), date_str_=f"15. Januar {int(jahr)+1}")),
        ])


def doc_kapazitaet(fname, oem_key, jahr):
    o = OEM[oem_key]
    write_doc(BASE / fname, H,
        f"Kapazitaetsanfrage {o['full']} ({jahr})",
        subtitle="Anfrage / Bestaetigung der Werkskapazitaet fuer Programm-Volumen-Hochlauf",
        sections=[
            ("Adressat", addr_block(oem_key)),
            ("Anfrage",
             f"Sehr geehrte/r {o['kontakt']},\n\n"
             f"mit Bezug auf Ihren Forecast vom " + ("15.06." if jahr=="2021" else "22.04." if jahr=="2022" else "08.02.") + jahr +
             f" und die geplante Volumenerhoehung der Programme BMS-12 (+18 %), ADAS-V4D (+15 %) "
             f"und ECU-900 (+22 %) bestaetigen wir hiermit die Verfuegbarkeit der zusaetzlichen "
             f"Werks-Kapazitaeten in der Brennhagen-Gruppe."),
            ("Kapazitaets-Bestaetigung",
             [["Programm", f"Plan {jahr} (Tsd. Einh.)", f"Forecast +1 (Tsd. Einh.)",
               "Brennhagen-Kapazitaet (Tsd. Einh.)", "Status"],
              ["BMS-12", "220", "260", "275", "OK"],
              ["ADAS-V4D", "95", "110", "120", "OK"],
              ["ECU-900", "145", "175", "180", "OK"],
              ["ICP-3", "170", "180", "200", "OK"]]),
            ("Werks-Massnahmen",
             ("list", [
                 "REG Heilbronn Linie 4 (BMS-12): Investition 28,4 Mio. EUR; SOP Q1 " + str(int(jahr)+1),
                 "RPL Katowice SMD-Erweiterung: 6,2 Mio. EUR; SOP Q3 " + jahr,
                 "REG Heilbronn Inline-Roentgen Linie 1 (ADAS-V4D): 1,4 Mio. EUR; SOP Q4 " + jahr,
                 "Personalaufbau Heilbronn: +85 FTE (Produktion + Qualitaet) bis Q4 " + str(int(jahr)+1),
                 "Halbleiter-Allokation: LoA Infineon, NXP, ST verlaengert bis 2030",
             ])),
            ("Vorbehalte / Bedingungen",
             "Verbindliche Kapazitaets-Reservierung erfolgt nach Erhalt einer schriftlichen "
             "Volumen-Commitment-Bestaetigung des Kunden (gemaess Rahmenvertrag § 2). "
             "Anschubfinanzierung fuer Kapazitaetsausbau: 35-40 % durch Kunden vorgesehen "
             "(siehe Vertragsnachtrag 2022). Volumenflexibilitaet +/- 15 % im Forecast-Korridor."),
            ("Naechste Schritte",
             "Verbindliche Bestaetigung des Kunden binnen 30 Tagen; bei Annahme erfolgt "
             "Investitionsfreigabe-Update durch Brennhagen-Vorstand binnen weiterer 30 Tage. "
             "Statusbericht im naechsten QBR."),
            ("Unterschriften",
             signatures("Stefan Richter", "CMO / BD", R["name"],
                        "Andreas Maier", "Werkleiter REG", R["name"],
                        place="Stuttgart", date_str_=f"15. " + ("Juli" if jahr=="2021" else "Mai" if jahr=="2022" else "Maerz") + " " + jahr)),
        ])


# ── PRJ-Status (project status) ────────────────────────────────────────────
def doc_prj_status(fname, prod_key, jahr):
    p = PRODUKT.get(prod_key, PRODUKT["ADAS-V4D"])
    write_doc(BASE / fname, H,
        f"Projekt-Statusbericht – {p['name']} (Stand {jahr})",
        subtitle="Programm-Status fuer interne Steuerung; vorgelegt im Programm-Management-Office (PMO)",
        sections=[
            ("Projekt-Identifikation",
             [["Position", "Wert"],
              ["Projekt-Nummer", fname.split("_")[0]],
              ["Produkt", p["name"]],
              ["Programm-Manager", "n. n. (zugewiesen Q3 " + jahr + ")"],
              ["Projektleiter Software (RSG)", "Lars Wittmann"],
              ["Werkleiter REG", "Andreas Maier"],
              ["SOP-Ziel", p["anlauf_sop"]],
              ["Aktueller Status", "On Track / Watch (siehe Risiken)"]]),
            ("Projektfortschritt",
             "Der aktuelle Status zum " + jahr + " liegt im Wesentlichen im Plan. "
             "Wesentliche Meilensteine der DV-Phase (B-Muster) wurden erreicht; "
             "PV-Phase (C-Muster) startet planmaessig im Folgequartal. "
             "Software-Stack RSG Muenchen ASPICE Level 2 erreicht; Level 3 in Q4 angestrebt."),
            ("Meilensteine und Status",
             [["Meilenstein", "Plan", "Status"],
              ["A-Muster", "Q4 2022", "Erreicht"],
              ["B-Muster (DV)", "Q2 2023", "Erreicht (mit 4 Wochen Verzug)"],
              ["C-Muster (PV)", "Q4 2023", "in Vorbereitung"],
              ["PPAP Submission", "Q1 2024", "Plan"],
              ["SOP", p["anlauf_sop"], "Plan"]]),
            ("Risiken und Mitigation",
             ("list", [
                 "R-01 Halbleiter-Allokation Nvidia Orin (ADAS-V4D): Mitigation 2nd-Source-Pruefung Qualcomm Snapdragon Ride; Status Pruefung",
                 "R-02 Software-Validierung ASPICE Level 3 Verzug 8 Wochen: Mitigation Verstaerkung Team RSG (+4 FTE)",
                 "R-03 Werkzeug-Aufbau Linie 1 REG: Status on track; geringes Risiko",
                 "R-04 Material-Eskalation Steckverbinder: Mitigation 2nd-Source Molex laeuft Re-PPAP",
             ])),
            ("Budget und Investitionen",
             "Plan-Budget Programm: 14,2 Mio. EUR Engineering + 28,4 Mio. EUR Werkzeuge / Kapital. "
             "Verbrauch Stand " + jahr + ": 65 % Engineering / 48 % Werkzeuge (planmaessig). "
             "Re-Forecast End-Programm: Engineering 14,8 Mio. EUR (+4 %) / Werkzeuge 28,1 Mio. EUR "
             "(unter Plan)."),
            ("Naechste Schritte",
             "Naechster Status-Termin: monatlich im PMO-Review. Eskalation R-02 (ASPICE Verzug) "
             "an CTO (Stefan Hoffmann) am Folgetermin. Programm-Manager-Benennung verbindlich bis "
             "+30 AT. Werks-Kapazitaet-Bestaetigung durch A. Maier zum Halbjahr."),
            ("Unterschriften",
             signatures("Stefan Hoffmann", "CTO", R["name"],
                        "Andreas Maier", "Werkleiter REG", R["name"],
                        place="Stuttgart", date_str_=f"30. September {jahr}")),
        ])


# ── Misc fallback (Police, IC, FX_Hedge stray etc.) ────────────────────────
def doc_misc(fname):
    write_doc(BASE / fname, H,
        f"Vertriebs- und OEM-Begleitdokument – {fname.replace('.docx','')}",
        subtitle="Begleit-Dokument im OEM-Vertrieb (Verschiedenes / Querverweis-Dokument)",
        sections=[
            ("Einordnung",
             "Dieses Dokument ist Bestandteil der OEM-Vertriebsakte der Brennhagen Elektronik AG. "
             "Inhalt: Begleitdokument zu OEM-Programmen, Audit-Vorbereitungen, Werks- oder "
             "Versicherungs-Aspekten, die mit den OEM-Liefer-Verpflichtungen verknuepft sind. "
             "Es dient als Cross-Reference zu den Hauptliefer-Vertraegen, QBRs sowie zur Audit-"
             "Vorbereitung mit den Premium-OEMs (BMW, VW, Mercedes-Benz, Stellantis, Continental)."),
            ("Hintergrund",
             "Die Brennhagen Elektronik AG fuehrt im Segment OEM-Vertrieb (Tier-1 Automotive) "
             "ein Portfolio aus 5 Hauptprodukten (ICP-3, BMS-12, ADAS-V4D, ECU-900, LightCtrl-7) "
             "fuer die Premium-OEMs. Begleitdokumente wie dieses sichern die "
             "Nachvollziehbarkeit der Programme, Audits und Versicherungs-Aspekte. "
             "Verantwortlich: Stefan Richter (CMO/BD), in Koordination mit Sabine Brand "
             "(Q-Leitung REG Heilbronn) und Markus Pflanzer (Group Treasurer / Versicherung)."),
            ("Verweise und Cross-Reference",
             ("list", [
                 "Rahmenliefervertraege OEMs 2022 (BMW, VW, Mercedes-Benz, Stellantis, Continental)",
                 "QBR-Berichte aller Programme (quartalsweise, je OEM und Produkt)",
                 "Kundenaudit-Berichte VDA 6.3 / IATF 16949 der letzten 3 Jahre",
                 "Versicherungspolice Industriefeuer / Betriebsunterbrechung Werk Heilbronn",
                 "Intercompany-Lieferung REG / RSG / RPL fuer OEM-Programme",
             ])),
            ("Aktueller Stand",
             "Das Dokument wird im Rahmen der laufenden OEM-Audits sowie der internen Revision "
             "regelmaessig aktualisiert. Die letzten Aktualisierungen erfolgten in Abstimmung "
             "mit der Qualitaetsleitung sowie dem Group Audit Executive (Andreas Buehler). "
             "Aufbewahrungsfrist gemaess Rahmenliefervertraegen: 15 Jahre nach EOP der letzten "
             "Lieferung."),
            ("Verantwortlichkeit",
             "Inhaltlich verantwortlich: Stefan Richter (CMO/BD). Q-Aspekte: Sabine Brand "
             "(Q-Leitung REG Heilbronn). Treasury-/Versicherungs-Aspekte: Markus Pflanzer "
             "(Group Treasurer). Eskalation: Anna Mueller (CEO) bzw. Stefan Hoffmann (CTO bis "
             "30.6.2024) / Dr. Petra Hollmann (CTO ab 1.7.2024)."),
            ("Unterschriften",
             signatures("Stefan Richter", "CMO / BD", R["name"],
                        "Sabine Brand", "Q-Leitung REG", R["name"],
                        place="Stuttgart", date_str_="laufend")),
        ])


# ── DISPATCH ───────────────────────────────────────────────────────────────
def dispatch(fname):
    info = parse(fname)
    typ = info.get("typ")
    oem = info.get("oem")
    prod = info.get("produkt")
    jahr = info.get("jahr") or "2023"
    quartal = info.get("quartal") or "Q1"

    # default prod fallback
    if oem and not prod:
        prod = next((p for (ok, p) in RAHMEN_VOLUMEN if ok == oem), DEFAULT_PROD_KEY)

    if typ == "QBR":
        doc_qbr(fname, oem, prod, jahr, quartal)
    elif typ == "ECR":
        doc_ecr(fname, oem, prod, jahr, info.get("ecr_nr", "001"))
    elif typ == "NOMINATION":
        doc_nomination(fname, oem, prod, jahr)
    elif typ == "RFQ":
        doc_rfq(fname, oem, prod, jahr)
    elif typ == "RAHMENLIEFERVERTRAG":
        doc_rahmenliefervertrag(fname, oem, jahr)
    elif typ == "LIEFERVERTRAG":
        doc_liefervertrag(fname, oem, prod, jahr)
    elif typ == "KUENDIGUNG":
        doc_kuendigung_androhung(fname, oem, jahr)
    elif typ == "NACHTRAG":
        doc_nachtrag(fname, oem, jahr)
    elif typ == "VERSORGUNG":
        doc_versorgung(fname, oem, jahr)
    elif typ == "LANGFRIST":
        doc_langfrist(fname, oem, jahr)
    elif typ == "JAHRESPREIS":
        doc_jahrespreis(fname, oem, jahr)
    elif typ == "PREISANPASSUNG":
        doc_preisanpassung(fname, oem, jahr)
    elif typ == "LOB":
        doc_lob(fname, oem, jahr)
    elif typ == "ESKALATION":
        doc_eskalation(fname, oem, jahr)
    elif typ == "CLAIM":
        if "Letter" in fname:
            doc_claim_letter(fname, oem, jahr)
        else:
            doc_claim(fname, oem, jahr)
    elif typ == "AUDIT_EINLADUNG":
        doc_audit_einladung(fname, oem, jahr)
    elif typ == "AUDIT_BERICHT":
        doc_audit_bericht(fname, oem, jahr)
    elif typ == "CSR":
        doc_csr(fname, oem, jahr)
    elif typ == "QSV":
        doc_qsv(fname, oem, jahr)
    elif typ == "KAPAZITAET":
        doc_kapazitaet(fname, oem, jahr)
    elif typ == "PRJ_STATUS":
        doc_prj_status(fname, prod or "ADAS-V4D", jahr)
    else:
        doc_misc(fname)


# ── Run ───────────────────────────────────────────────────────────────────
def main():
    start = time.time()
    files = sorted([p.name for p in BASE.glob("*.docx")])
    n = 0
    for fname in files:
        try:
            dispatch(fname)
            n += 1
        except Exception as e:
            print(f"FAIL {fname}: {e}")
    elapsed = time.time() - start
    print(f"Wrote {n} files in {elapsed:.1f}s")


if __name__ == "__main__":
    main()
