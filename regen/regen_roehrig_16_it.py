"""
Re-generation script for roehrig_large/16_IT_Systeme
Agent #14 — Konzern-IT / ISMS / SAP / Cloud / Security.

Overwrites all thin .docx files in that folder with realistic, richer
content (>= 200 words each). Idempotent.
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
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, f"{_ROOT}")
from enhance_lib import ROEHRIG_AG as R, write_doc, signatures

BASE = Path(f"{_ROOT}/roehrig_large/16_IT_Systeme")
H = {"name": R["name"], "addr": R["addr"], "hrb": R["hrb"]}

# Subsidiary headers
HRSG = {"name": "Brennhagen Software GmbH", "addr": "Lindwurmstrasse 88, 80337 Muenchen",
        "hrb": "HRB 319872, Amtsgericht Muenchen"}
HREG = {"name": "Brennhagen Elektronik GmbH", "addr": "Werkstrasse 22, 74076 Heilbronn",
        "hrb": "HRB 221456, Amtsgericht Heilbronn"}
HRPL = {"name": "Brennhagen Polska Sp. z o.o.", "addr": "ul. Brynowska 15, 40-585 Katowice",
        "hrb": "KRS 0000412876, NIP 6342845671"}

# Key persons
CIO   = "Dr. Karin Lehnhardt, CIO (extern beauftragt, BTC AG)"
COPS  = "Christian Roeder, Head of Group IT Operations"
CISO  = "Frank Eisermann, Head of IT Security (CISO)"
SAPCOE = "Dr. Stefan Lichter, Head of SAP Center of Excellence"
ARCH  = "Andreas Behrens, Lead IT-Architekt Konzern"
COO   = "Dr. Thomas Weber, COO"
CFO   = "Laura Bauer, CFO"
CTO_OLD = "Stefan Hoffmann, CTO (bis 30.06.2024)"


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def _systems_table():
    return [["System", "Hersteller / Release", "Hosting", "Verantwortlich"],
            ["ERP", "SAP S/4HANA 2022 (FPS02)", "On-Prem / Private Cloud (Azure)", "SAP CoE / Dr. Lichter"],
            ["MES", "SAP DMC / SAP ME 15.4", "On-Prem (REG, RPL, RCZ, RHU)", "MES-Team / B. Hartmann"],
            ["PLM", "Siemens Teamcenter 14.2", "On-Prem (Stuttgart RZ)", "PLM-Team / J. Schaal"],
            ["CRM", "Salesforce Sales Cloud", "SaaS (Salesforce EU)",        "Vertriebs-IT / M. Voss"],
            ["HR",  "SAP SuccessFactors EC, EP", "SaaS (SAP DC Frankfurt)",  "HR-IT / S. Vollmer"],
            ["ITSM","ServiceNow Vancouver",     "SaaS (Frankfurt Region)",   "IT-Operations / Roeder"],
            ["IDP", "Microsoft Entra ID (Azure AD)", "SaaS",                  "IAM-Team / D. Klett"],
            ["EDR", "CrowdStrike Falcon Enterprise", "SaaS",                  "SecOps / Eisermann"],
            ["Mail-Sec", "Proofpoint Email Protection", "SaaS",               "SecOps / Eisermann"],
            ["Backup", "Veeam Backup & Replication 12", "On-Prem + Wasabi S3","Infra / Tomaszewski"]]


def header_for(fname: str) -> dict:
    n = fname.upper()
    if n.startswith("RSG_") or "_RSG_" in n or "Muenchen" in fname or "AV_" in n[:3] or "JG_" in n[:3]:
        return HRSG
    if n.startswith("REG_") or "_REG_" in n:
        return HREG
    if n.startswith("RPL_") or "_RPL_" in n:
        return HRPL
    return H


# --------------------------------------------------------------------------
# Detail builders for IT operational tickets
# --------------------------------------------------------------------------

CHANGE_CASES = {
    "0003": ("SAP S/4HANA Patch FPS02 SP-04",
             "Einspielung Support-Package SAPK-755BHINS4ECCFI in Produktion (P01) sowie in den Mandanten 100 / 200 / 900. Voraussetzung fuer naechstes Tax-Update der Group Tax (Heike Berger).",
             "Mittel", "Standard", "geplant", "21.04.2023 22:00 - 22.04.2023 04:00 MESZ"),
    "0009": ("Azure Tenant Conditional Access verschaerfen",
             "Aktivierung Conditional-Access-Policy CA-09 (Phishing-resistente MFA fuer alle privilegierten Rollen, FIDO2/WHfB). Pilot mit 25 Admins, danach konzernweiter Rollout.",
             "Hoch", "Normal", "freigegeben", "07.05.2023 19:00 MESZ"),
    "0011": ("Salesforce Sandbox Refresh fuer RSG / ADAS Vertriebs-Use-Case",
             "Refresh der Full-Sandbox ROHRIG-RSG-FULL aus PROD Stand 09.05.2023; Anonymisierung personenbezogener Daten gemaess Konzernrichtlinie KR-DSGVO-04.",
             "Niedrig", "Standard", "geplant", "13.05.2023 06:00 MESZ"),
    "0013": ("Firewall-Regelaenderung OT/IT Werk Heilbronn",
             "Freischaltung neuer DMC/MES-Server (mes-reg-prd-04.reg.local) Richtung Bosch-Rexroth IPC-Steuerung; Segment OT-VLAN 184 -> IT-VLAN 32, Ports TCP/44818 (EtherNet/IP), TCP/4840 (OPC-UA).",
             "Hoch", "Normal", "in Pruefung CAB", "24.05.2023 21:00 MESZ"),
    "0015": ("Teamcenter PLM Upgrade auf TC 14.2.0.4",
             "Upgrade der Produktiv-Umgebung von TC 14.1 auf TC 14.2.0.4 inkl. Active Workspace 6.2. ABAP-RFC-Anbindung an SAP MM bleibt unveraendert.",
             "Mittel", "Normal", "geplant", "16.-18.06.2023 (Wochenende)"),
    "0017": ("CrowdStrike Falcon Sensor Update 7.04",
             "Rollout EDR-Sensor 7.04 (LTS) auf 4.180 verwaltete Endpoints (Windows 10/11) sowie 612 Linux-Server. Phased-Deployment ueber 4 Wellen, Rueckfall auf 7.02 dokumentiert.",
             "Niedrig", "Standard", "freigegeben", "Wellen 19.06. - 03.07.2023"),
}


def it_change_request(fname: str, num: str):
    title, beschr, risiko, typ, status, fenster = CHANGE_CASES[num]
    secs = [
        ("1. Change-Stammdaten",
         [["Feld", "Wert"],
          ["Change-Nummer", f"CHG-2023-{num}"],
          ["Titel", title],
          ["Beantragt durch", "Andreas Behrens, Lead IT-Architekt"],
          ["Genehmigt durch (CAB)", f"{COPS} / {CISO}"],
          ["Implementer", "ITOps Team / SAP CoE"],
          ["Risiko-Klasse", risiko],
          ["Change-Typ", typ],
          ["Status", status],
          ["Geplantes Wartungsfenster", fenster],
          ["ITSM-Ticket", f"ServiceNow CHG{num}-2023"],
          ["Affected CIs", "ca. 12 - 480 CI je nach Change"],
          ["Bezug zu Major Incident", "—"]]),
        ("2. Beschreibung und Begruendung",
         beschr + "\n\nDer Change ist Bestandteil der konzernweiten IT-Roadmap 2023 (Lenkungskreis IT-Strategie vom 09.02.2023, "
         "TOP 4). Die Aenderung wurde gemeinsam mit dem zustaendigen Fachbereich abgestimmt; das Service-Level "
         "wird durch das geplante Wartungsfenster nicht ueber das SLA-Limit (99,5 % Verfuegbarkeit) hinaus belastet."),
        ("3. Risikoeinschaetzung",
         "Die Risikobewertung erfolgte gemaess ITIL-4 Risikomatrix der Brennhagen Elektronik AG (Stand 03/2023). "
         "Wesentliche Risiken: (a) Verfuegbarkeitsverlust durch fehlgeschlagene Implementation; (b) Datenkonsistenz "
         "bei verbundenen Systemen (insb. SAP <-> MES <-> PLM); (c) regulatorische Anforderungen aus IATF 16949, "
         "TISAX, ISO 27001-Vorbereitung. Mitigation: vollstaendiger Rollback-Plan, Vier-Augen-Freigabe durch CAB, "
         "vorab Test in QAS-Mandant 200, Monitoring durch SIEM (Microsoft Sentinel) im erweiterten Modus."),
        ("4. Rollback-Plan",
         [["Schritt", "Aktion", "Verantwortlich"],
          ["R-1", "Pre-Change Snapshot Veeam / SAP Backup ueber DB13", "Infra-Team"],
          ["R-2", "Validierung Snapshot-Konsistenz (CRC, Restore-Test)", "Infra-Team"],
          ["R-3", "Bei Abbruch innerhalb Wartungsfenster: Wiederherstellung Stand Pre-Change", "ITOps"],
          ["R-4", "Eskalation an Major-Incident-Manager (Vinod Kumar) bei MTTR > 60 min", "MIM"],
          ["R-5", "Post-Mortem im naechsten CAB-Meeting", "CAB-Chair"]]),
        ("5. Test- und Freigabekriterien",
         "Akzeptanz-Kriterien: alle Smoke-Tests im Mandanten 200 (QAS) bestanden; SAP TR (Transport-Request) "
         "fehlerfrei importiert (RC <= 4); kein Anstieg der Tickets im ServiceNow-Dashboard innerhalb 24 h nach "
         "Produktivnahme (Schwellwert: 10 % ueber Baseline). Performance-KPI Latenz Dialogtransaktion < 800 ms (Mittelwert)."),
        ("6. Kommunikation",
         "Vorab-Information an Key-User-Verteiler (sap-keyuser@brennhagen-elektronik.de, ca. 240 Empfaenger) 7 Tage vorher; "
         "Status-Mail an Vorstand (Dr. Thomas Weber, COO) bei Risiko-Klasse 'Hoch'; Post-Implementation-Review "
         "im naechsten Lenkungskreis IT-Steering Committee (monatlich Mittwoch 14:00)."),
        ("7. Freigabe CAB",
         signatures(COPS.split(",")[0], "Head of Group IT Operations", "Brennhagen Elektronik AG",
                    CISO.split(",")[0], "CISO", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_="kalenderwoechentlicher CAB Donnerstag 10:00")),
    ]
    write_doc(BASE / fname, H, f"IT Change-Request CHG-2023-{num} - {title}",
              secs, subtitle="ITSM ServiceNow / ITIL-4 Change Management")


PATCH_CASES = {
    "0004": ("Windows Server Cumulative Update April 2023",
             "KB5025229 / KB5025230",
             "612 Windows Server 2019/2022 (alle Werke + RZ Stuttgart, RZ Heilbronn)",
             "21.04.2023 22:00 - 22.04.2023 06:00 MESZ"),
    "0007_intern": ("VMware vSphere ESXi 7.0 U3l Security Patch",
                    "ESXi 7.0 U3l Build 21424296 (CVE-2023-20892, CVE-2023-20893)",
                    "98 ESXi-Hosts in Stuttgart-RZ und Heilbronn-RZ; vMotion-Cluster aktiv",
                    "23.04.2023 22:00 - 24.04.2023 04:00 MESZ"),
    "0010": ("SAP HANA 2.0 SPS07 Revision 73",
             "SAP Note 3320991, Sicherheits-Hinweis HotNews S/4 2022",
             "SAP HANA P01 Produktiv-DB (24 TB), QAS, DEV; Mandanten 100/200/900",
             "06.05.2023 23:00 - 07.05.2023 05:00 MESZ"),
    "0012": ("Linux RHEL 8 / 9 Sicherheits-Patches Mai 2023",
             "RHSA-2023:2502, RHSA-2023:2548 (Kernel, OpenSSL 3.0.7)",
             "412 RHEL-Server (SAP-Application, MES, PLM-Backend)",
             "13.05.2023 22:00 - 14.05.2023 02:00 MESZ"),
    "0016_WIP": ("Cisco IOS XE Sicherheits-Patch (CVE-2023-20198)",
                 "Cisco Advisory cisco-sa-iosxe-webui-privesc-j22SaA4z",
                 "84 Catalyst 9300 / 9500 Switches (Werks-Backbone OT-Trennung)",
                 "GEPLANT 24.06.2023 - aktuell WIP, Hardware-Inventur noch nicht final"),
    "0020": ("Microsoft Exchange Hybrid Cumulative Update CU13",
             "Exchange Server 2019 CU13 (KB5024296)",
             "4 Mailbox-Server Stuttgart + 2 Edge-Transport (DMZ)",
             "29.07.2023 22:00 - 30.07.2023 06:00 MESZ"),
}


def it_patch_protokoll(fname: str, num: str):
    title, kb, scope, fenster = PATCH_CASES[num]
    secs = [
        ("1. Patch-Stammdaten",
         [["Feld", "Wert"],
          ["Patch-Protokoll-Nr.", f"PATCH-2023-{num}"],
          ["Titel", title],
          ["Hersteller / KB", kb],
          ["Scope (CIs)", scope],
          ["Wartungsfenster", fenster],
          ["Change-Referenz", f"CHG-2023-{int(num.split('_')[0])+1:04d}"],
          ["Verantwortlich (Patch-Manager)", "Vinod Kumar, IT Operations"],
          ["Eskalations-Kontakt", COPS],
          ["CISO-Sign-off (sicherheitsrelevant)", CISO],
          ["Status", "abgeschlossen" if "WIP" not in num else "in Bearbeitung"]]),
        ("2. CVSS- und CVE-Bewertung",
         "Die Sicherheitsrelevanz der adressierten Schwachstellen wurde gemaess CVSS 3.1 bewertet. "
         "Schwachstellen mit Score >= 7,0 (High/Critical) werden gemaess Konzernrichtlinie KR-SEC-12 "
         "(Vulnerability Management) innerhalb von 30 Kalendertagen produktiv eingespielt; Critical (>= 9,0) "
         "innerhalb von 14 Tagen. Externes Vulnerability-Reporting erfolgt durch CrowdStrike Spotlight; "
         "interne Validierung durch Tenable.io. Verantwortlich CISO Frank Eisermann."),
        ("3. Vorbereitung",
         "Test im Staging-Cluster STG-01 (Stuttgart) am Vortag des Wartungsfensters. Snapshot-Sicherung "
         "aller betroffenen VMs ueber Veeam B&R 12 (Job 'Werk-Heilbronn-Critical' bzw. 'RZ-Stuttgart-T0'). "
         "Pre-Check-Skript (PowerShell ps-precheck.ps1, intern auf GitHub Enterprise gepflegt) ergab keine "
         "Auffaelligkeiten. Kommunikation an Key-User 5 Tage vorher; OT/Produktions-IT (Werke) explizit "
         "ueber separate Mailingliste 'ot-coord@brennhagen-elektronik.de' informiert."),
        ("4. Durchfuehrung",
         [["Schritt", "Beginn", "Ende", "Ergebnis"],
          ["Pre-Check", fenster.split(" - ")[0], "+0:15", "OK"],
          ["Snapshot / Backup", "+0:15", "+0:45", "OK, Veeam Job-ID 8842"],
          ["Patch-Import / Reboot Welle 1", "+0:45", "+1:30", "OK"],
          ["Patch-Import / Reboot Welle 2", "+1:30", "+2:30", "OK"],
          ["Smoke-Tests (Login, Dialog, Batch)", "+2:30", "+3:00", "OK"],
          ["Freigabe ProductionGo-Live", "+3:00", "+3:15", "freigegeben"]]),
        ("5. Auffaelligkeiten und Massnahmen",
         "Waehrend des Patch-Fensters traten keine kritischen Auffaelligkeiten auf. Geringfuegige Warnungen "
         "in Microsoft Sentinel (3 Events Severity Low) wurden vom SOC (Sopra Steria, 24/7) gepruefte und als "
         "False-Positive klassifiziert. Eine ausstehende Re-Konfiguration des Lastenausgleichs (F5 BIG-IP) "
         "wurde als Folge-Ticket INC2023-0814 erfasst. Die Verfuegbarkeit der betroffenen Services lag im "
         "Berichtsmonat bei 99,87 % (SLA-Ziel 99,5 %)."),
        ("6. Bestaetigung",
         signatures("Vinod Kumar", "IT Operations Patch Manager", "Brennhagen Elektronik AG",
                    CISO.split(",")[0], "CISO", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_=fenster.split(" - ")[0].split(" ")[0])),
    ]
    write_doc(BASE / fname, H, f"IT Patch-Protokoll PATCH-2023-{num}",
              secs, subtitle="Vulnerability- und Patch-Management")


INCIDENT_CASES = {
    "0002_2024-03-01": ("Phishing-Welle gegen Vorstand und Group Treasury",
                        "Spear-Phishing", "Hoch",
                        "Ca. 14 zielgerichtete E-Mails an Vorstandsmitglieder und Group Treasury, Absender "
                        "spoofte 'deutsche-bank-konsortium.de'. Anhang: HTM-Datei mit Microsoft-365-Login-"
                        "Imitation, Credential-Harvesting via evilginx2.",
                        "Proofpoint blockierte 11 / 14 Mails; 3 erreichten Postfaecher (Markus Pflanzer, Florian "
                        "Maier, Vorstands-Assistenz). Keine Credential-Eingabe erfolgt (User-Awareness, Phish-Reporting).",
                        "Sperre der spoofed Domain im Mail-Gateway, Reset der Sessions in Entra ID, "
                        "MFA-Reset, Pflicht-E-Learning fuer betroffene User, Threat-Intel-Bericht an CSIRT-Konsortium."),
    "0005":              ("Ransomware-Versuch Endpoint Werk Heilbronn",
                        "Malware / Ransomware (Lockbit 3.0 Variant)", "Hoch",
                        "Endpoint REG-WS-04812 (Sandra Heinz, Prozessingenieurin SMT) wurde am 22.05.2023 um 13:42 "
                        "MESZ durch CrowdStrike Falcon (Severity Critical) isoliert. Vektor: USB-Stick aus externer "
                        "Quelle (Vorab-Software eines Bestueckungsautomaten-Lieferanten).",
                        "CrowdStrike OverWatch verhinderte Verschluesselung; 1 Endpoint geblockt, kein Lateral Movement.",
                        "USB-Stick beschlagnahmt, forensisches Image (FTK Imager); USB-Massenspeicher-Policy "
                        "konzernweit angepasst (DeviceControl), externe Datentraeger ab 01.07.2023 nur ueber "
                        "freigegebene 'Trusted USB' (Kingston IronKey)."),
    "0014":              ("DDoS-Angriff Web-Auftritt brennhagen-elektronik.de",
                        "Volumetric DDoS", "Mittel",
                        "Layer-7-DDoS, 28.07.2023 09:14-09:47 MESZ. Volumen ca. 12 Gbit/s, Quelle: Botnet (vorrangig RU, IR, CN).",
                        "Cloudflare WAF (Enterprise) absorbierte 99,4 % des Traffics; Backend (Hetzner) "
                        "kurzzeitig 4 min eingeschraenkt erreichbar. Keine Datenabfluesse.",
                        "Cloudflare Pro-Plan auf Enterprise mit Magic Transit erweitert; Rate-Limiting verschaerft; "
                        "Threat-Intel-Sharing mit BSI / Allianz fuer Cyber-Sicherheit."),
    "0018":              ("Unautorisierter Zugriffsversuch SAP S/4HANA",
                        "Brute-Force / Credential Stuffing", "Mittel",
                        "07.09.2023 02:14-02:32 MESZ: 1.840 fehlgeschlagene SAP-Logins gegen Mandant 100 (PROD), "
                        "Quelle IP 185.213.x.x (TOR-Exit-Node). Ziel: SAP-User mit Endung '_DDIC', '_SAP*'.",
                        "Microsoft Sentinel Alert um 02:18 MESZ; SAP Solution Manager Alert um 02:21. "
                        "Standard-User SAP*, DDIC waren bereits konzernweit gesperrt; keine erfolgreiche Anmeldung.",
                        "Geo-Blocking auf SAP-Frontend-Endpoints (Cloudflare Access); Verschaerfung "
                        "Password-Policy (16 Zeichen Minimum, Brute-Force-Lockout nach 5 Versuchen)."),
    "0023_intern":      ("Datenpanne RSG Muenchen - Fehlversand Personalakte",
                        "DSGVO-relevanter Vorfall", "Mittel",
                        "Mitarbeiter HR-IT RSG sendete am 12.10.2023 eine Excel-Datei mit Bonusdaten von 18 ADAS-"
                        "Entwicklern faelschlich an einen externen Verteiler (Auditor KPMG Internal Audit anstelle "
                        "interner HR-Verteiler).",
                        "Datei wurde innerhalb 35 min vom Auditor (Andreas Buehler, CAE) erkannt und geloescht; "
                        "kein Forward / keine externe Weiterverbreitung.",
                        "Meldung an Datenschutzbeauftragten Dr. Markus Holz (LD&P) innerhalb 24 h; "
                        "keine LfD-Meldepflicht nach Art. 33 DSGVO (kein hohes Risiko), aber dokumentiert; "
                        "DLP-Regel Microsoft Purview verschaerft (Bonus-Listen automatisch erkennen und blocken)."),
    "0024":              ("Stoerung CrowdStrike Falcon Console",
                        "Verfuegbarkeitsstoerung externer Dienstleister", "Niedrig",
                        "Konsole nicht erreichbar 19.10.2023 14:20-15:55 MESZ aufgrund regionaler Stoerung "
                        "CrowdStrike Cloud (EMEA-Region). Endpoint-Schutz lokal weiter aktiv.",
                        "Detection und Response ueber Falcon weiterhin funktional (lokaler Sensor); nur Visibility "
                        "/ Investigation aus der Konsole nicht moeglich.",
                        "Reklamationsschreiben SLA-Verletzung an CrowdStrike (Account Manager Sebastian Hahn); "
                        "Pruefung redundanter SOC-Visibility ueber Microsoft Sentinel parallel."),
}


def it_sicherheitsvorfall(fname: str, key: str):
    title, art, schwere, beschreib, detection, massnahmen = INCIDENT_CASES[key]
    inc_nr = key.split("_")[0]
    secs = [
        ("1. Vorfalls-Stammdaten",
         [["Feld", "Wert"],
          ["Vorfalls-Nr.", f"SEC-INC-2023-{inc_nr}"],
          ["Titel", title],
          ["Art / Kategorie", art],
          ["Schwere (Schadenspotenzial)", schwere],
          ["Erfasst durch", "SOC Sopra Steria (24/7) / CISO Frank Eisermann"],
          ["CSIRT-Einsatzleitung", "Frank Eisermann (CISO), Andreas Behrens (Architekt)"],
          ["Meldepflicht §8b BSIG / Art. 33 DSGVO", "geprueft, siehe Abschnitt 6"],
          ["ITSM-Ticket", f"ServiceNow INC{inc_nr}-2023"],
          ["Verbundene Changes", "—"],
          ["Status", "geschlossen mit Lessons-Learned"]]),
        ("2. Sachverhalt",
         beschreib + "\n\nDie initiale Erfassung erfolgte im SIEM Microsoft Sentinel (Severity High) sowie "
         "durch automatisierte Korrelation in CrowdStrike Falcon. Eskalation an CSIRT gemaess Konzern-"
         "Cybersecurity-Policy (ISMS Dokument REA-ISMS-01, Ziff. 8.2) erfolgte innerhalb der vorgesehenen "
         "Reaktionsfrist (T+30 min fuer Severity High)."),
        ("3. Detection und Erstreaktion",
         detection),
        ("4. Massnahmen und Containment",
         massnahmen),
        ("5. Auswirkungen und Schadensbewertung",
         "Direkte Verfuegbarkeitsauswirkungen: keine Produktionsstoerung (Werke). Geschaeftskritische Systeme "
         "(SAP, MES) blieben verfuegbar. Reputationsschaden: gering. Datenabfluss: keiner festgestellt. "
         "Direkte Kosten: ca. 4.500 EUR (forensische Auswertung Sopra Steria), abgerechnet ueber Rahmenvertrag "
         "SOC-Services REA/SOPRA-2022-08."),
        ("6. Meldepflichten",
         "Pruefung gemaess §8b BSIG (KRITIS): nicht einschlaegig, REA ist nicht KRITIS-Betreiberin. "
         "Pruefung gemaess Art. 33 DSGVO: ggf. einschlaegig, je Vorfall separat dokumentiert. "
         "Pruefung NIS-2 Umsetzung 2024: vorsorglich erfasst, Reporting-Prozess im Aufbau (Verantwortlich CISO)."),
        ("7. Lessons Learned",
         "Awareness-Training fuer betroffene Zielgruppe (Vorstand / Fuehrungskraefte) eingeplant in Q4/2023 "
         "ueber KnowBe4-Plattform. Anpassung Detection-Regel in Sentinel (KQL-Query 'phishing_high_value_targets') "
         "umgesetzt. Naechstes CSIRT-Tabletop-Exercise 21.11.2023 unter Leitung Allianz fuer Cyber-Sicherheit."),
        ("8. Freigabe",
         signatures(CISO.split(",")[0], "CISO", "Brennhagen Elektronik AG",
                    COPS.split(",")[0], "Head of Group IT Operations", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_="—")),
    ]
    write_doc(BASE / fname, H, f"IT-Sicherheitsvorfall SEC-INC-2023-{inc_nr} - {title}",
              secs, subtitle="CSIRT / ISMS Incident Report (ISO 27001 / TISAX Anh. A.16)",
              confidential=True)


OUTAGE_CASES = {
    "0001": ("SAP S/4HANA Production - Dialog-Performance-Einbruch",
             "SAP S/4HANA (P01, Mandant 100)", "P2 (high)",
             "14.02.2023 09:18-11:42 MESZ", "ca. 144 Minuten",
             "Hohe Dialog-Antwortzeiten (Mittelwert 4,8 s, Spitze 14 s) in den Modulen FI, CO, MM. "
             "Ca. 1.200 Anwender betroffen, vorrangig Backoffice Stuttgart und Heilbronn.",
             "Ursache: ineffiziente ABAP-Query in Custom-Z-Report ZFI_AGING_ANALYSIS (von Anwender Group "
             "Tax gestartet ohne Selektionsfilter) verursachte massiven Tablescan auf BSEG (1,2 Mrd. Rows).",
             "Hotfix - Anwender-Schulung, Kill der Hintergrund-Jobs, Z-Report umgebaut auf ATR/SELECT-OPTIONS "
             "Pflicht durch SAP CoE. Backup vom Vortag stand bereit, war nicht erforderlich."),
    "0006": ("Teamcenter PLM nicht erreichbar (RSG Muenchen)",
             "Siemens Teamcenter 14.1", "P2 (high)",
             "03.04.2023 13:25-15:50 MESZ", "ca. 145 Minuten",
             "Standort RSG Muenchen konnte nicht auf PLM zugreifen; ADAS-Entwicklung blockiert (ca. 280 Engineers).",
             "Ursache: VPN-Tunnel Stuttgart <-> Muenchen (Cisco ASA, BGP-Peering) ausgefallen nach "
             "kurzfristiger Telekom-Stoerung Hauptanschluss Vaihinger Strasse.",
             "Failover auf Backup-Tunnel ueber MPLS-Carrier 'Colt' aktiviert; Telekom-Ticket TKM-2023-04812 "
             "geoeffnet; Eskalation auf Konzernkonto. SLA-Strafzahlung Telekom: 4.200 EUR Gutschrift."),
    "0008": ("Salesforce CRM Login-Stoerung",
             "Salesforce Sales Cloud", "P3 (medium)",
             "26.04.2023 08:30-10:15 MESZ", "ca. 105 Minuten",
             "Vertriebsmitarbeiter konnten sich nicht ueber Single-Sign-On (Entra ID -> Salesforce SAML) anmelden. "
             "Ca. 380 Vertriebs- und Service-Anwender betroffen.",
             "Ursache: abgelaufenes SAML-Signing-Zertifikat auf Salesforce-Seite (Renewal-Hinweis verloren "
             "im Salesforce-Admin-Postfach des Vorgaengers).",
             "Neues Zertifikat im Wartungsfenster eingespielt; ITIL-CMDB-Eintrag fuer Zertifikate "
             "vervollstaendigt; automatische Renewal-Reminder ueber Microsoft Sentinel KQL-Query etabliert."),
    "0021": ("MES-Ausfall Werk Brno (RCZ)",
             "SAP DMC / SAP ME 15.4", "P1 (critical)",
             "16.10.2023 04:18-06:55 MESZ", "ca. 157 Minuten",
             "Linie 'CON-04' im Werk Brno stand still (Steckverbinder-Endmontage), kein MES-Buchen moeglich. "
             "Produktionsverlust ca. 3.200 Stueck (Wert ca. 28.000 EUR).",
             "Ursache: Festplatten-Ausfall auf MES-Application-Server mes-rcz-prd-02 (Dell PowerEdge R750); "
             "RAID-Rebuild blockierte Schreib-IO.",
             "Ausfall-Plattenwechsel ueber Vor-Ort-Service Dell ProSupport 4h; Lessons-Learned: "
             "Reservekapazitaet (Cold-Standby) muss in RCZ aufgebaut werden, Investitionsantrag im Capex-2024."),
    "0022": ("Microsoft 365 Outlook Online - regionale Stoerung",
             "Microsoft 365 (Exchange Online, Teams)", "P3 (medium)",
             "23.10.2023 11:05-13:30 MESZ (Microsoft-seitig)", "ca. 145 Minuten",
             "Konzernweit eingeschraenkter Zugriff auf Outlook Online und Teams; Offline-Cache lieferte Fallback.",
             "Ursache: regionale Microsoft-365-Stoerung Europe (Tenant-Region 'GERMANY'), bestaetigt im "
             "Service Health Dashboard (Incident EX583240).",
             "Beobachtung / Eskalation ueber Microsoft Premier Support (Account Manager Susanne Schenk); "
             "interne Status-Updates ueber Statuspage im Intranet alle 30 min."),
}


def it_systemstoerung(fname: str, num: str):
    title, system, schwere, zeit, dauer, beschr, ursache, massnahme = OUTAGE_CASES[num]
    secs = [
        ("1. Stoerungs-Stammdaten",
         [["Feld", "Wert"],
          ["Stoerungs-Nr.", f"INC-2023-{num}"],
          ["Titel", title],
          ["Betroffenes System / Service", system],
          ["Schweregrad", schwere],
          ["Stoerungszeitraum", zeit],
          ["Stoerungsdauer", dauer],
          ["Major-Incident-Manager", "Vinod Kumar / Christian Roeder (Eskalation)"],
          ["Service-Owner", SAPCOE.split(',')[0] + " (SAP), Andreas Behrens (Infrastruktur)"],
          ["ITSM-Ticket", f"ServiceNow INC{num}-2023"],
          ["RCA-Status", "abgeschlossen"]]),
        ("2. Stoerungsbeschreibung",
         beschr + "\n\nDie Erstmeldung erfolgte ueber den ServiceDesk (Erstticket eines End-Anwenders) sowie "
         "ueber proaktives Monitoring (Microsoft Sentinel, SAP Solution Manager). Die Eskalation zum Major-"
         "Incident wurde 12 Minuten nach Stoerungsbeginn ausgeloest, MIM-Bruecke (Teams) eroeffnet."),
        ("3. Ursachenanalyse (RCA)",
         ursache + "\n\nDie RCA wurde gemaess ITIL-4-Methode (5-Why-Analyse) durchgefuehrt und im Post-Mortem "
         "am Folgetag mit Service-Owner, Architekt und CISO besprochen. Dokumentation im Confluence-Space "
         "'IT Major Incidents'."),
        ("4. Massnahmen / Sofortmassnahmen",
         massnahme),
        ("5. Auswirkungen",
         [["Dimension", "Wert"],
          ["Betroffene Anwender (geschaetzt)", "ca. 120 - 1.200"],
          ["Direkter Produktionsverlust", "0 - 28.000 EUR (je Vorfall)"],
          ["SLA-Verletzung", "ggf. ja, siehe Berichts-Anhang"],
          ["Kundenbeschwerden / OEM-Impact", "nein"],
          ["Datenverlust", "nein"]]),
        ("6. Praeventive Massnahmen",
         "Aufnahme einer praeventiven Massnahme in das IT-Risikoregister (Eigentuemer Andreas Behrens). "
         "Update der Monitoring-Schwellwerte (Prometheus, Sentinel) und Anpassung Runbooks im Confluence. "
         "Ueberpruefung Lessons-Learned im naechsten IT-Steering Committee."),
        ("7. Freigabe RCA",
         signatures("Vinod Kumar", "Major Incident Manager", "Brennhagen Elektronik AG",
                    COPS.split(",")[0], "Head of Group IT Operations", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_=zeit.split("-")[0].strip())),
    ]
    write_doc(BASE / fname, H, f"IT-Systemstoerung INC-2023-{num} - {title}",
              secs, subtitle="ITSM Major-Incident Bericht / RCA")


# --------------------------------------------------------------------------
# Policy / Strategy big documents
# --------------------------------------------------------------------------

def isms_policy(fname: str, thema: str, kurz: str, kapitel: list):
    """Generic ISMS-policy generator."""
    secs = [
        ("Dokumentenkontrolle",
         [["Feld", "Wert"],
          ["Dokumenttitel", thema],
          ["Dokumentenkuerzel", kurz],
          ["Version", "1.4"],
          ["Status", "freigegeben"],
          ["Klassifizierung", "Intern - Beschraenkter Verteiler"],
          ["Dokumenten-Eigentuemer (Author)", CISO],
          ["Dokumenten-Pruefer", CIO + ", " + COPS],
          ["Freigeber (Vorstand)", COO + ", " + CFO],
          ["Inkrafttreten", "01.04.2023"],
          ["Geltungsbereich", "Brennhagen Elektronik AG, alle Konzerngesellschaften (REG, RSG, RPL, RCZ, RHU, RCN, RHO)"],
          ["Verbindlichkeit", "verbindlich fuer alle Mitarbeitenden, Externe und Drittparteien mit Zugriff"]]),
        ("1. Zweck und Geltungsbereich",
         "Diese Konzernrichtlinie regelt das Thema »" + thema + "« fuer die Brennhagen Elektronik AG und alle "
         "Tochtergesellschaften. Sie ist Bestandteil des Informationssicherheits-Managementsystems (ISMS) "
         "der Brennhagen Elektronik AG, das auf Basis ISO/IEC 27001:2022 sowie der Bausteine des BSI IT-Grundschutzes "
         "betrieben wird. Ein erstes externes ISO-27001-Audit ist gemeinsam mit TUEV NORD CERT GmbH (Lead "
         "Auditor: Dr. Henrik Pfaffenstoll) fuer Q4/2024 vorgesehen. Die Richtlinie integriert TISAX-Anforderungen "
         "der Automobilindustrie (VDA-ISA, gepruefte Stufe AL3 bei REG/RSG)."),
        ("2. Verantwortlichkeiten",
         [["Rolle", "Verantwortung"],
          ["Vorstand (COO, CFO)", "Gesamtverantwortung; Genehmigung Risikoakzeptanz, Budgetfreigabe"],
          ["CIO (Dr. Lehnhardt, BTC AG)", "Sourcing-/Architektur-Verantwortung, Lieferanten-Mgmt"],
          ["CISO (Frank Eisermann)", "Fachverantwortung ISMS, Policy-Management, Audit-Vorbereitung"],
          ["Head of Group IT Operations (Roeder)", "Operative Umsetzung im Tagesgeschaeft"],
          ["Lead Architekt (Behrens)", "Architektur-Reviews, Security-by-Design"],
          ["SAP CoE (Dr. Lichter)", "ERP-spezifische Sicherheitsmassnahmen (SoD, GRC)"],
          ["DSB (LD&P, Dr. Holz)", "Schnittstelle DSGVO"],
          ["Werkleitungen / Subsidiary-IT", "Lokale Implementierung, Awareness, Compliance"]]),
        ("3. Inhaltliche Vorgaben",
         ("list", kapitel)),
        ("4. Technische und organisatorische Massnahmen (TOMs)",
         [["Kontroll-Domaene", "Kontroll-Massnahme", "Status 2023"],
          ["Zugangskontrolle (A.5/A.8)", "Microsoft Entra ID mit Conditional Access, MFA verpflichtend", "umgesetzt"],
          ["Endpoint-Sicherheit (A.8)", "CrowdStrike Falcon Enterprise auf 100 % verwalteten Endpoints", "umgesetzt"],
          ["Netzwerk-Segmentation (A.8)", "OT/IT-Trennung in den Werken (Cisco IE-Switche, Firewalls)", "umgesetzt"],
          ["Backup (A.8)", "Veeam B&R 12, taeglich, Offsite Wasabi S3, Air-Gap-Tape", "umgesetzt"],
          ["E-Mail-Sicherheit (A.8)", "Proofpoint Email Protection, DMARC, SPF, DKIM enforced", "umgesetzt"],
          ["SIEM / SOC", "Microsoft Sentinel + 24/7 SOC durch Sopra Steria", "umgesetzt"],
          ["Penetrationstests", "SySS GmbH halbjaehrlich (intern + perimeter)", "laufend"],
          ["Awareness", "KnowBe4 Plattform, Pflicht-Module quartalsweise", "umgesetzt"],
          ["Lieferantenpruefung", "Sicherheitsfragebogen + TISAX-Pruefung bei Schluessellieferanten", "laufend"]]),
        ("5. Audit, Compliance und kontinuierliche Verbesserung",
         "Das ISMS unterliegt internen Audits durch KPMG Internal Audit (jaehrlich) sowie externen "
         "Pruefungen (TISAX alle 3 Jahre, ISO 27001 ab 2024 jaehrliches Surveillance-Audit nach Erstzertifizierung). "
         "Penetrationstests werden halbjaehrlich durch die SySS GmbH (Tuebingen, Lead Tester Sebastian Schreiber) "
         "durchgefuehrt. Die kontinuierliche Verbesserung erfolgt auf Basis ISMS-Forum (monatlich) und Risiko-"
         "Reviews (quartalsweise im IT-Steering Committee unter Vorsitz CIO)."),
        ("6. Sanktionen bei Verstoss",
         "Verstoesse gegen diese Richtlinie koennen arbeitsrechtliche Massnahmen nach sich ziehen (Abmahnung "
         "bis Kuendigung) und werden bei Externen ueber Vertragsstrafen sanktioniert. Strafanzeige bei "
         "vorsaetzlichen Handlungen mit erheblichem Schadenspotenzial. Verantwortliche Stelle: HR (Vollmer) "
         "in Abstimmung mit Konzernrechtsabteilung (Dr. Hellmig)."),
        ("7. Freigaben",
         signatures(COO.split(",")[0], "COO", "Brennhagen Elektronik AG",
                    CFO.split(",")[0], "CFO", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_="22.03.2023")),
    ]
    write_doc(BASE / fname, H, thema,
              secs, subtitle=f"Konzernrichtlinie {kurz} / ISMS ISO 27001:2022")


def cloud_strategy(fname: str):
    secs = [
        ("Dokumentenkontrolle",
         [["Feld", "Wert"],
          ["Titel", "Konzern-Cloud-Strategie und Sicherheitsarchitektur"],
          ["Kuerzel", "REA-CLOUD-STRAT-2023"],
          ["Version", "2.1"],
          ["Verantwortlich", CIO],
          ["Co-Author", ARCH + ", " + CISO],
          ["Freigegeben (Vorstand)", COO + ", " + CFO],
          ["Verteiler", "IT-Steering Committee, Aufsichtsrat (Pruefungsausschuss) zur Kenntnis"],
          ["Inkrafttreten", "01.05.2023"]]),
        ("1. Cloud-Strategie - Leitlinien",
         "Die Brennhagen Elektronik AG verfolgt seit 2022 eine »Cloud-Smart«-Strategie. Die Konzern-Cloud-"
         "Strategie 2023 baut auf den im Aufsichtsrats-Beschluss vom 18.11.2022 (TOP 6) verankerten Leitlinien auf:\n\n"
         "(a) Microsoft Azure ist Primary Cloud Provider fuer Workloads des Konzerns (SAP, Datenplattform, "
         "IAM, Productivity).\n"
         "(b) AWS ist Secondary Cloud Provider fuer Machine-Learning- und Data-Engineering-Workloads der RSG "
         "Muenchen (ADAS / Embedded SW).\n"
         "(c) Salesforce, SAP SuccessFactors, ServiceNow und KnowBe4 sind SaaS-Best-of-Breed.\n"
         "(d) Kein Multi-Cloud-Active-Active fuer SAP-Kerne (Kostendisziplin).\n"
         "(e) Kein Public-Cloud fuer OT/MES-Steuerung auf Linienebene (Latenz, Souveraenitaet)."),
        ("2. Microsoft Azure - Tenant-Architektur",
         [["Element", "Auspraegung"],
          ["Tenant", "brennhagen-elektronik.onmicrosoft.com"],
          ["Subscriptions", "8 (Prod, NonProd je Domaene: SAP, Data, Workplace, Network)"],
          ["Management Groups", "Hierarchie Konzern -> Domaene -> Umgebung"],
          ["Regionen", "Germany West Central (Frankfurt), West Europe (Amsterdam) als DR"],
          ["Identity", "Entra ID (Azure AD), Hybrid (AAD Connect zu On-Prem AD)"],
          ["Konnektivitaet", "ExpressRoute (2x10 Gbit/s, Equinix Frankfurt FR4)"],
          ["Workloads", "SAP S/4HANA Private Cloud (M192ms_v2), Azure Synapse (Data), AVD Pilot"],
          ["Compliance", "Azure Policy 'Konzern-Baseline' (50+ Policies), Defender for Cloud"]]),
        ("3. AWS - Sekundaer-Account-Struktur (RSG)",
         [["Element", "Auspraegung"],
          ["Organisation", "AWS Organization 'roehrig-rsg' (Master: 612845192753)"],
          ["Accounts", "5: shared-services, ml-prod, ml-dev, data-prod, sandbox"],
          ["Regionen", "eu-central-1 (Frankfurt) primaer, eu-west-1 (Irland) DR"],
          ["Services", "SageMaker, S3, EKS (ADAS-Trainings-Pipelines), Bedrock (Pilot)"],
          ["Compliance", "SCPs (Service Control Policies), CIS-Benchmark, GuardDuty, Macie"]]),
        ("4. Daten-Klassifikation und Cloud-Eignung",
         [["Klassifikation", "Beispiel", "Public Cloud zulaessig?"],
          ["Public",        "Pressemitteilung, IR-Materialien", "ja"],
          ["Intern",        "interne Memos, Org-Charts", "ja"],
          ["Vertraulich",   "Vertraege, Personal, Konstruktionen", "ja, mit CMK + DLP"],
          ["Streng vertraulich", "M&A, Vorstand, Kronjuwelen (ADAS-Algorithmen)", "nur Azure DE + Customer-Lockbox"]]),
        ("5. Sicherheitsarchitektur",
         "Die Cloud-Sicherheitsarchitektur folgt dem Zero-Trust-Modell mit den drei Saeulen: (a) "
         "Identity-First (Entra ID Conditional Access mit FIDO2-Pflicht fuer privilegierte Rollen; Privileged "
         "Identity Management mit Just-in-Time-Aktivierung); (b) Netzwerk-Segmentation (Hub-and-Spoke ueber "
         "Azure Virtual WAN, AWS Transit Gateway, Site-to-Site IPsec zu den Werken); (c) Data-Protection "
         "(Microsoft Purview, AWS Macie, customer-managed keys in Azure Key Vault HSM-backed). "
         "Threat-Detection: Microsoft Sentinel (Primary SIEM) mit ca. 240 Korrelationsregeln; AWS GuardDuty "
         "und CloudTrail nach Sentinel weitergeleitet ueber Azure Monitor Connector."),
        ("6. Lieferanten- und Vertragsmanagement",
         [["Partner", "Vertrag", "Volumen p.a."],
          ["Microsoft (EA)", "Enterprise Agreement 'Brennhagen-EA-2022', Laufzeit 1.4.2022-31.3.2025", "ca. 3,8 Mio. EUR"],
          ["Amazon Web Services", "Enterprise Discount Program 'EDP-Brennhagen-RSG-2023'", "ca. 0,9 Mio. EUR"],
          ["BTC AG (Sourcing-Partner)", "MSP-Vertrag CIO-Sourcing, vereinbart 14.06.2022", "ca. 1,2 Mio. EUR"],
          ["Accenture", "S/4HANA-Implementierungspartner (Lead, ab 2022)", "ca. 4,5 Mio. EUR (Multi-Year)"],
          ["Sopra Steria", "SOC-Managed-Service 24/7", "ca. 0,7 Mio. EUR"]]),
        ("7. Roadmap und Investitionen",
         "Phase 1 (2022): Tenant-Aufbau Microsoft Azure, Entra ID Hybrid, M365 E5 Konzernweit (abgeschlossen). "
         "Phase 2 (2023): S/4HANA-Migration auf Azure (Pilot Mandant 200, Go-Live Heilbronn FI/CO Q3/2023). "
         "Phase 3 (2024): SAP S/4HANA Produktiv-Migration Polen (RPL), Tschechien (RCZ), Ungarn (RHU). "
         "Phase 4 (2025): Datenplattform Azure Synapse / Microsoft Fabric, AWS SageMaker fuer ADAS-Training. "
         "Phase 5 (2026): Konsolidierung, ggf. zweite Azure-Region als Hot-DR."),
        ("8. Freigabe",
         signatures(COO.split(",")[0], "COO", "Brennhagen Elektronik AG",
                    CFO.split(",")[0], "CFO", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_="26.04.2023")),
    ]
    write_doc(BASE / fname, H, "Konzern-Cloud-Strategie und Sicherheitsarchitektur 2023",
              secs, subtitle="REA-CLOUD-STRAT-2023 / IT-Steering Committee Genehmigung")


def backup_konzept(fname: str):
    secs = [
        ("Dokumentenkontrolle",
         [["Feld", "Wert"],
          ["Titel", "Konzern-Backup- und Restore-Konzept"],
          ["Kuerzel", "REA-IT-BCK-2022"],
          ["Version", "3.2"],
          ["Inkrafttreten", "01.01.2022 (Update 03/2023)"],
          ["Verantwortlich", COPS],
          ["Pruefung", CISO + ", Konzernrevision (Buehler)"]]),
        ("1. Grundsatz und Geltungsbereich",
         "Dieses Konzept regelt Backup- und Restore-Prozesse aller geschaeftskritischen IT-Systeme der "
         "Brennhagen Elektronik AG und Tochtergesellschaften. Grundlage sind BSI IT-Grundschutz CON.3 (Datensicherung), "
         "ISO 27001:2022 A.8.13 und IATF 16949 Anhang B (Notfallplanung Produktion)."),
        ("2. Backup-Strategie 3-2-1-1-0",
         "Es gilt der konzernweite Standard 3-2-1-1-0: 3 Kopien jeder produktionskritischen Daten, auf 2 "
         "verschiedenen Medien, davon 1 offsite, 1 unveraenderlich/air-gapped, 0 fehlerhafte Restore-Tests."),
        ("3. RPO/RTO je Anwendungsklasse",
         [["Anwendungs-Klasse", "Beispiele", "RPO", "RTO"],
          ["Klasse A (Tier 0)", "SAP S/4HANA P01, MES (REG, RPL), Active Directory", "<= 15 min", "<= 4 h"],
          ["Klasse B (Tier 1)", "Teamcenter PLM, Salesforce-Replikate", "<= 1 h", "<= 8 h"],
          ["Klasse C (Tier 2)", "Fileservices, SharePoint Online (kopiert)", "<= 4 h", "<= 24 h"],
          ["Klasse D (Tier 3)", "Test-Systeme, Sandbox", "<= 24 h", "<= 72 h"]]),
        ("4. Technologie-Stack",
         [["Schicht", "Loesung", "Anbieter"],
          ["VM / OS Backup", "Veeam Backup & Replication 12", "Veeam Software"],
          ["SAP HANA Backup", "SAP Native Backup, integriert in Backint zu Veeam", "SAP / Veeam"],
          ["File / SharePoint", "Veeam Backup for Microsoft 365 v7", "Veeam"],
          ["Datenbank-Logs", "DB-Native, archiviert auf S3-kompatiblen Storage", "verschiedene"],
          ["Offsite-Storage", "Wasabi Hot Storage Frankfurt + Amsterdam", "Wasabi Technologies"],
          ["Air-Gap / Tape", "LTO-9 Quarterly im Tresor Stuttgart (extern bei Iron Mountain)", "Iron Mountain"]]),
        ("5. Pruefungs- und Restore-Tests",
         "Restore-Tests werden monatlich (Tier 0/1) bzw. quartalsweise (Tier 2/3) durchgefuehrt. Dokumentation "
         "ueber ServiceNow CHG-Template 'Restore-Test'. KPMG Internal Audit pruefte zuletzt am 14.11.2022 "
         "und stellte ein offenes Findings (»Tape-Rotation Heilbronn Werk verspaetet«); geschlossen 28.02.2023. "
         "Naechster Disaster-Recovery-Test geplant November 2023."),
        ("6. Freigabe",
         signatures(COPS.split(",")[0], "Head of Group IT Operations", "Brennhagen Elektronik AG",
                    CISO.split(",")[0], "CISO", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_="14.01.2022")),
    ]
    write_doc(BASE / fname, H, "Konzern-Backup- und Restore-Konzept",
              secs, subtitle="REA-IT-BCK-2022 / IT-Operations")


def bcp_2023(fname: str):
    secs = [
        ("Dokumentenkontrolle",
         [["Feld", "Wert"],
          ["Titel", "Business Continuity Plan IT (BCP)"],
          ["Kuerzel", "REA-BCP-IT-2023"],
          ["Version", "1.7"],
          ["Verantwortlich (BCM-Lead)", COPS],
          ["Mit-Verantwortlich", "Olaf Stege, BCM-Koordinator Konzern"],
          ["Inkrafttreten", "01.03.2023"]]),
        ("1. Zweck",
         "Der BCP IT beschreibt Massnahmen zur Aufrechterhaltung der IT-Services bei Stoerungen, Ausfaellen "
         "oder Katastrophen. Er ist Bestandteil des konzernweiten Business Continuity Managements (BCM) und "
         "ist abgestimmt mit den Werks-Notfallplaenen (REG, RSG, RPL, RCZ, RHU, RCN)."),
        ("2. Geschaeftsprozess-Kritikalitaet (BIA Auszug)",
         [["Geschaeftsprozess", "Kritikalitaet", "max. Ausfall (MTPD)", "RTO IT"],
          ["Produktion REG/RPL/RCZ/RHU (Linie 24/7)", "sehr hoch", "8 h", "4 h"],
          ["OEM-Lieferungen / EDI (JIS/JIT VW, BMW)",  "sehr hoch", "8 h", "4 h"],
          ["Finanzbuchhaltung / Treasury / Zahlungen", "hoch",      "24 h", "8 h"],
          ["Engineering / ADAS-Entwicklung",           "mittel",    "5 Tage", "24 h"],
          ["HR-Gehaltslauf",                           "hoch",      "5 Tage (Stichtag)", "24 h"]]),
        ("3. Szenarien und Reaktion",
         "Definierte Szenarien: (S1) Ausfall RZ Stuttgart Hauptstandort; (S2) Cyberattacke mit Verschluesselung "
         "mehrerer Systeme; (S3) Ausfall Cloud-Provider (Microsoft Azure Germany West Central); (S4) "
         "Ausfall Werk-IT durch Brand/Wasserschaden; (S5) Personalausfall Key-Personen IT (Pandemie). "
         "Je Szenario sind Aktivierungskriterien, Krisenstab-Zusammensetzung und Reaktionsschritte "
         "in einem Runbook hinterlegt (Confluence Space 'BCM')."),
        ("4. Krisenstab",
         [["Rolle", "Person", "Stellvertretung"],
          ["Krisenstab-Leitung", COO, CFO],
          ["IT-Krisenleitung", COPS, ARCH],
          ["Cyber-Krisenleitung", CISO, "Frank Sopra-Steria Account-Manager"],
          ["Kommunikation (intern/extern)", "Stefan Richter (CMO/BD)", "IR-Team Frau Klein"],
          ["Recht und Compliance", "Dr. Maria Hellmig", "Konzernrevision (Buehler)"],
          ["HR / People", "Sandra Vollmer", "Heinz Maier"]]),
        ("5. Tests und Uebungen",
         "Tabletop-Uebung jaehrlich (zuletzt 12.10.2022 Szenario S2 Ransomware unter Moderation der "
         "Allianz fuer Cyber-Sicherheit). Full Disaster-Recovery-Test halbjaehrlich (siehe REA_Disaster_"
         "Recovery_Test_2023). Naechstes Tabletop 21.11.2023 (Szenario S3 Cloud-Ausfall)."),
        ("6. Freigabe",
         signatures(COO.split(",")[0], "COO", "Brennhagen Elektronik AG",
                    COPS.split(",")[0], "Head of Group IT Operations", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_="22.02.2023")),
    ]
    write_doc(BASE / fname, H, "Business Continuity Plan IT (BCP) 2023",
              secs, subtitle="REA-BCP-IT-2023")


def dr_test_2023(fname: str):
    secs = [
        ("Dokumentenkontrolle",
         [["Feld", "Wert"],
          ["Dokument", "Disaster Recovery Test 2023 - Halbjahres-Test H1"],
          ["Kuerzel", "REA-DR-TEST-2023-H1"],
          ["Version", "0.6 (ENTWURF, noch nicht freigegeben)"],
          ["Testleitung", "Olaf Stege, BCM-Koordinator"],
          ["Test-Datum", "Wochenende 17./18.06.2023"]]),
        ("1. Testziel",
         "Validierung der DR-Faehigkeit zentraler IT-Services bei simuliertem Totalausfall RZ Stuttgart "
         "(Szenario S1). Insbesondere: Failover SAP S/4HANA (Pilot Mandant 200), Active Directory, "
         "Microsoft 365 Hybrid, Veeam-Restore aus Wasabi-Offsite, Netzwerk-Routing-Umschaltung auf RZ Heilbronn "
         "(als DR-Standort fuer ausgewaehlte Services)."),
        ("2. Testszenario",
         "Simulation eines vollstaendigen Ausfalls des primaeren Rechenzentrums Stuttgart (Hosting Equinix "
         "Frankfurt FR4 + interner Maschinenraum Vaihinger Strasse) durch geplante Trennung der Anbindung. "
         "Failover-Mechanismen wurden bewusst nicht vorab manuell aktiviert, um Automatisierungsgrad zu pruefen."),
        ("3. Ergebnis Kennzahlen",
         [["Service", "Soll-RTO", "Ist-RTO", "Bewertung"],
          ["SAP S/4HANA QAS Mandant 200", "4 h", "3 h 42 min", "OK"],
          ["Active Directory / Entra Connect", "1 h", "0 h 38 min", "OK"],
          ["Microsoft 365 (geo-redundant)", "0 (immer da)", "n/a", "OK"],
          ["Teamcenter PLM (read-only)", "8 h", "11 h 20 min", "NOK (Lessons-Learned)"],
          ["Veeam Wasabi Restore (200 GB Beispieldatei)", "2 h", "1 h 55 min", "OK"]]),
        ("4. Findings",
         "(F1) Teamcenter PLM Replikation nach Heilbronn ist nicht produktionsnah eingerichtet; Read-Only-"
         "Modus dauert laenger als angenommen. Massnahme: Investitionsantrag Capex 2024 fuer warm-standby PLM.\n"
         "(F2) Failover-Skripte (PowerShell) waren in mehreren Faellen nicht aktuell - dokumentierte Pfade "
         "stimmten nicht mit produktiven Pfaden ueberein. Massnahme: Aufnahme in Konfigurationsmanagement.\n"
         "(F3) Telefon-Bridge (Krisenstab) war fuer 22 Minuten ueberlastet (zu viele Teilnehmer). "
         "Massnahme: Teams Premium Bridge mit Capacity-Management testen."),
        ("5. Naechste Schritte",
         "Massnahmen (F1) bis (F3) werden im Massnahmenplan REA-MNP-2023-DR mit Owner und Faelligkeit "
         "geplant. Naechster DR-Test H2/2023 geplant fuer 18./19.11.2023 mit Szenario S3 (Cloud-Ausfall Azure-Region)."),
        ("6. Status",
         "Dieser Bericht hat den Status ENTWURF. Final-Freigabe nach Closing-Workshop am 11.07.2023. "
         "Verteilung anschliessend an IT-Steering Committee, Vorstand (COO), Pruefungsausschuss "
         "Aufsichtsrat (Prof. Voss)."),
    ]
    write_doc(BASE / fname, H, "Disaster Recovery Test 2023 - Halbjahres-Test H1 (Entwurf)",
              secs, subtitle="REA-DR-TEST-2023-H1 / BCM IT", draft=True)


def endpoint_policy(fname: str):
    chap = [
        "Verbindliche EDR-Loesung: CrowdStrike Falcon Enterprise (inkl. Falcon Prevent, Falcon Insight, Falcon OverWatch).",
        "Voll-Verschluesselung: BitLocker (Windows) bzw. FileVault (macOS) mit Key-Escrow in Entra ID.",
        "Patch-Mgmt: Microsoft Intune mit Patch-Compliance-Reporting, Aktualisierungspflicht 14 Tage (Critical 7 Tage).",
        "Application-Allowlisting: Microsoft Defender for Endpoint Application Control, Privileged Access mit AppLocker.",
        "USB-Massenspeicher: nur Kingston IronKey (verschluesselt) durch DeviceControl freigegeben.",
        "Local-Admin: keine permanenten lokalen Admin-Rechte, JIT-Admin ueber EPM (Endpoint Privilege Management).",
        "Browser-Mgmt: Microsoft Edge Enterprise mit Conditional Access; Chrome nur in Ausnahmefaellen mit Begruendung.",
        "Mobile Devices: BYOD nur fuer M365-Apps via Intune App-Protection; COBO Geraete unter MDM.",
        "macOS Endpoints in der RSG Muenchen (ca. 220 Stk., ADAS-Entwicklung) ueber Jamf Pro verwaltet.",
    ]
    isms_policy(fname, "Konzern-Endpoint-Security-Policy",
                "REA-EPS-2023", chap)


def iam_policy(fname: str):
    chap = [
        "Identitaets-Provider: Microsoft Entra ID (Hybrid-Modell), Konzernweiter Identity-Lifecycle aus SAP SuccessFactors.",
        "Joiner-Mover-Leaver: vollautomatisierte Provisionierung ueber SailPoint IdentityNow (PoC); Ist-Zustand Skript-basiert (PowerShell).",
        "Authentifizierung: MFA verpflichtend (alle Mitarbeitende); FIDO2 + Windows Hello for Business pflicht fuer Admins.",
        "Privileged Access Management: CyberArk Privilege Cloud (PoC); Microsoft Entra Privileged Identity Management produktiv.",
        "Rollenmodell: Best-Role + Best-Position; Konzernrollen-Katalog ca. 320 Rollen, davon 84 SAP-Rollen (SoD-relevant).",
        "Access-Reviews: quartalsweise fuer privilegierte Rollen (REA_User_Access_Review_xxxx_Qx), jaehrlich fuer Standard-User.",
        "SAP GRC Access Control 12.0 fuer SoD-Konflikt-Pruefung; Eskalation an SAP CoE (Dr. Lichter) bei kritischen Konflikten.",
        "Service-Konten: zentrale Verwaltung ueber CyberArk; keine Passwort-Aufbewahrung in Skripten / GitHub Enterprise.",
        "Externe Identitaeten: B2B-Gast in Entra ID, Lebensdauer maximal 12 Monate, mit Renewal-Workflow.",
    ]
    isms_policy(fname, "Konzern-IAM-Richtlinie (Identity and Access Management)",
                "REA-IAM-2023", chap)


def isms_cyber(fname: str):
    chap = [
        "Risikomanagement gemaess ISO 27005 und BSI 200-3, jaehrlicher Risiko-Review.",
        "Assets-Inventar in ServiceNow CMDB; Klassifikation Public/Intern/Vertraulich/Streng vertraulich.",
        "Lieferkette: Lieferantenfragebogen fuer kritische IT-Lieferanten; jaehrliche Re-Bewertung.",
        "Kryptographie: TLS 1.3 fuer alle externen Schnittstellen, RSA-2048 mindestens, ECC bevorzugt.",
        "Loggin & Monitoring: zentrale Sammlung in Microsoft Sentinel; Aufbewahrung 24 Monate online.",
        "Incident Management: CSIRT mit definierter Eskalationsmatrix (Severity 1-4), SOC 24/7 ueber Sopra Steria.",
        "Geschaeftspartner / OEM-Anforderungen: TISAX (VDA-ISA) erfuellt fuer REG (AL3) und RSG (AL3).",
        "Awareness: KnowBe4 - Pflicht-Module quartalsweise; Phishing-Simulation monatlich.",
        "Audit-Programm: KPMG Internal Audit jaehrlich; externes ISO 27001-Audit Q4/2024 (TUEV NORD).",
    ]
    isms_policy(fname, "Cybersecurity-Policy und ISMS (ISO 27001:2022)",
                "REA-ISMS-CYB-2023", chap)


def gov_framework(fname: str):
    secs = [
        ("Dokumentenkontrolle",
         [["Feld", "Wert"],
          ["Dokument", "IT-Governance-Framework"],
          ["Kuerzel", "REA-ITGOV-2023"],
          ["Version", "1.3"],
          ["Verantwortlich", CIO],
          ["Inkrafttreten", "01.04.2023"]]),
        ("1. Zweck und Geltungsbereich",
         "Das IT-Governance-Framework regelt Entscheidungswege, Gremien, Verantwortlichkeiten und Steuerungs-"
         "instrumente der Konzern-IT der Brennhagen Elektronik AG. Es orientiert sich an COBIT 2019 (DSS) und "
         "IT-Service-Management nach ITIL 4. Verantwortlich ist die CIO Dr. Karin Lehnhardt, die ueber den "
         "Sourcing-Partner BTC AG (Stuttgart) eingebunden ist (Vertrag REA/BTC-2022-04, Laufzeit bis 31.12.2025)."),
        ("2. Gremien",
         [["Gremium", "Vorsitz", "Frequenz", "Aufgaben"],
          ["IT-Steering Committee", "COO (Dr. Weber)", "monatlich", "Strategische Steuerung IT, Genehmigung Roadmap"],
          ["Change Advisory Board (CAB)", "Head of Group IT Ops (Roeder)", "woechentlich Do 10:00", "Change-Freigaben"],
          ["IT-Security Forum", "CISO (Eisermann)", "monatlich", "Risiken, Schwachstellen, Vorfaelle"],
          ["Architecture Review Board", "Lead Architekt (Behrens)", "alle 2 Wochen", "Architektur-Reviews"],
          ["SAP Change Board", "SAP CoE (Dr. Lichter)", "woechentlich", "SAP-Spezifische Changes/Releases"],
          ["Konzernrevisions-Lenkungskreis IT", "CAE (Buehler) / CIO", "quartalsweise", "Audit-Findings, Massnahmen"]]),
        ("3. Verantwortlichkeitsmatrix (Auszug RACI)",
         [["Entscheidung", "CIO", "CISO", "COPS", "Architekt", "SAP CoE", "Vorstand"],
          ["IT-Strategie", "A", "C", "C", "C", "C", "R"],
          ["IT-Budget", "R", "I", "C", "I", "C", "A"],
          ["Sicherheits-Architektur", "C", "A", "C", "R", "C", "I"],
          ["Cloud-Roadmap", "A", "C", "C", "R", "C", "I"],
          ["Major Incident Response", "I", "A", "R", "C", "C", "I"],
          ["SAP-Releases", "I", "C", "C", "C", "A/R", "I"]]),
        ("4. Berichtswesen",
         "Monatlicher IT-Lagebericht an Vorstand (COO); quartalsweiser IT-Sicherheitsbericht an Pruefungsausschuss "
         "Aufsichtsrat (Prof. Voss); jaehrlicher IT-Risikobericht an Vorstand; Sofortmeldung an Vorstand bei "
         "Major-Incident Severity 1 innerhalb 2 Stunden."),
        ("5. Kontinuierliche Verbesserung",
         "IT-Governance wird im Jahresrhythmus geprueft und ggf. angepasst. Ergebnisse fliessen in den "
         "Konzernlagebericht ein. Externe Pruefung erfolgt durch KPMG WPG im Rahmen des Jahresabschluss-Audits "
         "(IT-General-Controls IFRS-Bilanzierung)."),
        ("6. Freigabe",
         signatures(CIO.split(",")[0], "CIO", "Brennhagen Elektronik AG / BTC AG",
                    COO.split(",")[0], "COO", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_="22.03.2023")),
    ]
    write_doc(BASE / fname, H, "Konzern-IT-Governance-Framework 2023",
              secs, subtitle="REA-ITGOV-2023")


def it_risikobericht(fname: str):
    secs = [
        ("Berichtskopf",
         [["Feld", "Wert"],
          ["Berichtstitel", "Konzern-IT-Risikobericht 2023"],
          ["Berichtsperiode", "Geschaeftsjahr 2023"],
          ["Erstellt durch", CISO + ", " + CIO],
          ["Adressat", "Vorstand, Aufsichtsrat-Pruefungsausschuss (Prof. Voss)"],
          ["Status", "freigegeben durch Vorstand am 24.10.2023"]]),
        ("1. Methodik",
         "Bewertung gemaess BSI 200-3 (Risikoanalyse) und ISO 27005. Risiko-Score = Eintrittswahrscheinlichkeit "
         "x Schadenshoehe (5x5-Matrix). Eintrittswahrscheinlichkeit (1-5): sehr unwahrscheinlich - sehr wahrscheinlich. "
         "Schadenshoehe (1-5): unerheblich - existenzbedrohend (Schwelle 25 Mio. EUR)."),
        ("2. Top-10 IT-Risiken 2023",
         [["Nr.", "Risiko", "Score", "Eigentuemer", "Status / Massnahme"],
          ["R-01", "Ransomware-Befall Werks-IT (Produktionsstillstand)", "20 (hoch)", CISO, "CrowdStrike, Air-Gap-Backup, BCM-Tabletop 11/2023"],
          ["R-02", "Ausfall SAP S/4HANA P01 > RTO 4 h",                  "16 (hoch)", SAPCOE, "Azure Migration, Geo-Redundanz Phase 5 2026"],
          ["R-03", "Schluesselpersonen-Risiko (CISO, SAP CoE, Architekt)", "12 (mittel)", "HR (Vollmer)", "Nachfolgeplanung, Cross-Training laufend"],
          ["R-04", "OT/IT-Konvergenz - unzureichende Segmentation in Bestandswerken", "12 (mittel)", "Behrens / Werkleitungen", "OT-Audit 2024 geplant"],
          ["R-05", "Cloud-Lieferanten-Konzentration Microsoft (EA)", "10 (mittel)", CIO, "Sekundaer-Cloud AWS in RSG, Exit-Strategie dokumentiert"],
          ["R-06", "Datenschutz-Vorfall (DSGVO)",                     "10 (mittel)", "DSB (Holz)", "DLP Purview, Awareness, AVV-Inventar"],
          ["R-07", "Ungesteuerte KI-Tools (Schatten-IT)",             "9 (mittel)", CIO, "KI-Richtlinie 03/2024 in Vorbereitung"],
          ["R-08", "Lieferketten-Cyber-Risiko (Software-Supply-Chain)","8 (mittel)", CISO, "SBOM-Pflicht ab 2024, Software-Lieferanten-Audit"],
          ["R-09", "Verlust technischer SAP-ABAP-Kompetenz",          "8 (mittel)", SAPCOE, "Accenture-Partnerschaft, Junior-Programm"],
          ["R-10", "Quantum-Computing-Bedrohung (langfristig)",       "6 (gering)", CISO, "PQC-Roadmap ab 2025 (Beobachtung)"]]),
        ("3. Veraenderungen ggue. Vorjahr",
         "R-01 (Ransomware) bleibt Risiko Nr. 1; Score unveraendert hoch trotz verbesserter Massnahmen, da "
         "Bedrohungslage steigt (Lockbit 3.0, Royal). R-07 (KI-Tools) neu im Register. R-05 (Cloud-Konzentration) "
         "weiterhin im Beobachtungsmodus, da Microsoft EA bis 2025 laeuft."),
        ("4. Schaeden und Vorfaelle 2023 (Auszug)",
         "13 erfasste Sicherheitsvorfaelle, davon 3 Severity High; kumulierter direkter Schaden ca. 56.000 EUR; "
         "kein wesentlicher Reputationsverlust; keine OEM-Meldepflicht ausgeloest."),
        ("5. Massnahmenplan",
         "Investitionsbedarf 2024-2026 fuer IT-Sicherheit: 2,4 Mio. EUR (Capex) + 1,8 Mio. EUR p.a. (Opex). "
         "Schwerpunkte: Zero-Trust-Erweiterung, SAP-GRC-Erweiterung, OT-Security-Programm, Cyber-Insurance-Erhoehung."),
        ("6. Freigabe",
         signatures(CISO.split(",")[0], "CISO", "Brennhagen Elektronik AG",
                    COO.split(",")[0], "COO", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_="24.10.2023")),
    ]
    write_doc(BASE / fname, H, "Konzern-IT-Risikobericht 2023",
              secs, subtitle="REA-IT-RISK-2023", confidential=True)


def netzarchitektur(fname: str):
    secs = [
        ("Dokumentenkontrolle",
         [["Feld", "Wert"],
          ["Titel", "Konzern-Netzwerkarchitektur"],
          ["Kuerzel", "REA-NETARCH-2023"],
          ["Version", "2.0"],
          ["Verantwortlich", ARCH],
          ["Inkrafttreten", "01.06.2023"]]),
        ("1. Konzern-Topologie",
         "Die Konzern-Netzwerkarchitektur basiert auf einem Hub-and-Spoke-Modell mit zwei Konzern-Hubs "
         "(Stuttgart und Heilbronn) sowie Werks-Spokes (REG Heilbronn, RPL Katowice, RCZ Brno, RHU Gyoer, "
         "RCN Shanghai, RSG Muenchen). Konnektivitaet zwischen Standorten ueber MPLS (Telekom Konzernvertrag) "
         "mit Backup ueber SD-WAN (Colt) und Internet-VPN."),
        ("2. WAN-Inventar",
         [["Standort", "Primaer", "Backup", "Bandbreite"],
          ["Stuttgart (HQ)", "Telekom MPLS", "Colt SD-WAN", "2x10 Gbit/s"],
          ["Heilbronn (REG)", "Telekom MPLS", "Colt SD-WAN", "2x1 Gbit/s"],
          ["Muenchen (RSG)", "Telekom MPLS", "Colt SD-WAN", "1 Gbit/s"],
          ["Katowice (RPL)", "Orange Business / MPLS", "Internet-VPN", "1 Gbit/s"],
          ["Brno (RCZ)", "T-Mobile CZ / MPLS", "Internet-VPN", "500 Mbit/s"],
          ["Gyoer (RHU)", "Magyar Telekom / MPLS", "Internet-VPN", "500 Mbit/s"],
          ["Shanghai (RCN)", "China Telecom IPLC", "Internet-VPN", "100 Mbit/s"]]),
        ("3. Segmentation OT/IT",
         "Werke verfuegen ueber strikte OT/IT-Trennung mit IEC 62443-orientierter Zonierung: Level 0/1 "
         "(Sensoren, SPS, Roboter) im Industrial-Cell-Netz, Level 2 (SCADA) im OT-DMZ, Level 3 (MES) als "
         "Schnittstelle IT, Level 4 (ERP) im Standard-IT-Netz. Trennung erfolgt ueber Cisco Catalyst IE3300 "
         "Industrial Switches und Stormshield Industrial Firewalls. Datenfluesse OT->IT sind whitelisted "
         "und SIEM-ueberwacht."),
        ("4. Cloud-Anbindung",
         "Azure-Anbindung ueber ExpressRoute (Equinix Frankfurt FR4, 2x10 Gbit/s, redundant). AWS-Anbindung "
         "ueber Direct Connect (Equinix Frankfurt, 1 Gbit/s, RSG-spezifisch). SaaS-Dienste (M365, Salesforce, "
         "SuccessFactors, ServiceNow) ueber Internet mit ZScaler ZIA / Cloudflare Access (SASE-Initiative)."),
        ("5. Naming, IP-Adressierung",
         "Konzern-IPv4-Plan: 10.0.0.0/8 koordiniert ueber Konzern-IPAM (Infoblox). Werke nutzen jeweils ein "
         "/16-Segment, OT-Bereiche separat aus 172.x. IPv6 in Vorbereitung (Pilot Stuttgart 2024)."),
        ("6. Freigabe",
         signatures(ARCH.split(",")[0], "Lead IT-Architekt", "Brennhagen Elektronik AG",
                    COPS.split(",")[0], "Head of Group IT Operations", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_="11.05.2023")),
    ]
    write_doc(BASE / fname, H, "Konzern-Netzwerkarchitektur 2023",
              secs, subtitle="REA-NETARCH-2023")


def pen_test(fname: str):
    secs = [
        ("Berichtskopf",
         [["Feld", "Wert"],
          ["Berichtstitel", "Penetrationstest-Bericht extern 2023 (H1)"],
          ["Kuerzel", "REA-PEN-2023-H1"],
          ["Auftraggeber", "Brennhagen Elektronik AG, CISO Frank Eisermann"],
          ["Auftragnehmer", "SySS GmbH, Tuebingen (Wilhelmstrasse 14)"],
          ["Lead-Pentester", "Sebastian Schreiber (CEO) / Christoph Schade (Senior Consultant)"],
          ["Testzeitraum", "13.03. - 31.03.2023"],
          ["Berichtsversion", "1.2 (final)"],
          ["Klassifizierung", "STRENG VERTRAULICH"]]),
        ("1. Auftrag / Scope",
         "Halbjaehrlicher Penetrationstest gemaess Konzern-Rahmenvertrag REA/SySS-2022 (Vertrag vom "
         "14.03.2022, Laufzeit 3 Jahre). Scope H1/2023: (a) externe Perimeter (32 IP-Adressen), (b) "
         "Web-Applikationen (brennhagen-elektronik.de, karriere.brennhagen-elektronik.de, lieferanten-portal.roehrig.de), "
         "(c) Microsoft 365 Tenant (Phishing-Resilienz, Conditional Access), (d) interner Test Werk Heilbronn "
         "(Insider-Threat-Szenario)."),
        ("2. Methodik",
         "Black-Box (extern) und Grey-Box (intern) gemaess PTES (Penetration Testing Execution Standard) "
         "und OWASP Web Security Testing Guide v4. Tools u.a. Burp Suite Professional, Cobalt Strike, "
         "Bloodhound, Mimikatz, eigenentwickelte SySS-Tools. Reporting nach CVSS 3.1."),
        ("3. Findings Zusammenfassung",
         [["Severity", "Anzahl", "Status"],
          ["Critical (>=9,0)", "1", "geschlossen 21.04.2023"],
          ["High (7,0-8,9)", "4", "3 geschlossen, 1 in Bearbeitung"],
          ["Medium (4,0-6,9)", "11", "8 geschlossen, 3 akzeptiert"],
          ["Low (<4,0)", "18", "Hinweise, kein Handlungszwang"]]),
        ("4. Wesentliche Findings (Auszug, Critical/High)",
         [["ID", "Titel", "CVSS", "Komponente"],
          ["F-001", "Out-of-date SAP-Webdispatcher (CVE-2023-23857)", "9,1", "SAP-Anbindung externes Lieferantenportal"],
          ["F-002", "Subdomain-Takeover karriere-test.brennhagen-elektronik.de", "8,2", "Azure-DNS-Konfiguration"],
          ["F-003", "Schwache Conditional-Access-Regel fuer Service-Accounts", "7,8", "Entra ID"],
          ["F-004", "SSRF-Anfaelligkeit in internem Lieferantenportal", "7,5", "Lieferantenportal"],
          ["F-005", "ADFS-Endpoint mit veralteter Crypto-Konfiguration", "7,2", "ADFS / Federation"]]),
        ("5. Massnahmenplan",
         "Sofortmassnahmen Critical F-001 (Patch SAP-Webdispatcher) wurden innerhalb 7 Tage umgesetzt; "
         "Subdomain-Takeover F-002 innerhalb 24 Stunden bereinigt. Hohe Risiken wurden in den Massnahmenplan "
         "REA-MNP-2023-PEN aufgenommen; Tracking ueber JIRA / ServiceNow GRC."),
        ("6. Empfehlungen",
         "(a) Etablierung Bug-Bounty-Programm (HackerOne / YesWeHack) ab 2024; (b) Continuous Attack Surface "
         "Management (CASM) ueber Tool wie Detectify oder Tenable ASM; (c) Roter Team / TIBER-DE-Uebung "
         "in 2024 unter Begleitung Bundesbank-Aufsicht (sofern Aufsichtsrahmen einschlaegig)."),
        ("7. Freigabe",
         signatures("Sebastian Schreiber", "Lead Pentester", "SySS GmbH",
                    CISO.split(",")[0], "CISO", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_="05.04.2023")),
    ]
    write_doc(BASE / fname, H, "Penetrationstest-Bericht 2023 (H1) - SySS GmbH",
              secs, subtitle="REA-PEN-2023-H1", confidential=True)


def sap_mes(fname: str):
    secs = [
        ("Dokumentenkontrolle",
         [["Feld", "Wert"],
          ["Titel", "SAP MES (Manufacturing Execution) Systemdokumentation"],
          ["Kuerzel", "REA-SAP-MES-2022"],
          ["Version", "1.5"],
          ["Verantwortlich", "Berthold Hartmann, MES-Architekt"],
          ["Sponsor", "Dr. Stefan Lichter, SAP CoE"],
          ["Stand", "Oktober 2022"]]),
        ("1. Loesungsuebersicht",
         "MES-Implementierung der Brennhagen Elektronik AG basiert auf SAP DMC (Digital Manufacturing Cloud, "
         "vormals SAP ME 15.4 on-prem). Es deckt die Werke REG Heilbronn (Hauptwerk), RPL Katowice (EMS/SMD), "
         "RCZ Brno (Steckverbinder) und RHU Gyoer (Sensorik) ab. RCN Shanghai ist als reines Vertriebs-/"
         "Service-Werk nicht mit MES ausgestattet. Implementierungspartner: Accenture (Lead) und SAP "
         "Deutschland AG (Consulting)."),
        ("2. Integration",
         [["Schnittstelle", "Protokoll", "Frequenz"],
          ["SAP ERP <-> MES (Material, Auftrag)", "PI/PO, iDoc, OData", "near-real-time"],
          ["MES <-> SPS (Linien)",                "OPC-UA, MQTT",       "real-time"],
          ["MES <-> Qualitaet / SPC",             "REST",               "near-real-time"],
          ["MES <-> WMS",                         "iDoc",               "asynchron"],
          ["MES <-> Teamcenter (Stueckliste)",    "TC-Integration",     "auf Anforderung"]]),
        ("3. Funktionsumfang",
         "Auftragsabwicklung mit Linienzuordnung, Personal- und Maschinenzeiterfassung, SPC (Statistical "
         "Process Control), elektronische Wareneingangsbestaetigung mit Barcode-Scannern (Honeywell), "
         "Werkzeugmanagement, Traceability (Seriennummer/IMEI bis Bauteilebene fuer ICP-3, BMS-12), "
         "QM-Anbindung (Sperrprozess, 8D-Anstoss)."),
        ("4. Werks-Spezifika",
         [["Werk", "Linien", "MES-Customizing"],
          ["REG Heilbronn", "8 Linien (ICP, BMS, ADAS, ECU, Light)", "Vollumfang inkl. SPC, Traceability"],
          ["RPL Katowice", "12 SMD-Linien + 4 Final-Assembly", "EMS-spezifisch, Yokogawa SCADA-Integration"],
          ["RCZ Brno", "6 Steckverbinder-Linien", "Standard"],
          ["RHU Gyoer", "5 Sensor-Linien", "Standard inkl. Inline-Pruefung"]]),
        ("5. Betrieb und Support",
         "24/7 SLA durch SAP Premium Engagement (Vertrag REA/SAP-2022-PE), Eskalation Severity 1 ueber Vinod "
         "Kumar (MIM) sowie Accenture-Support (24/7). Patch-Management quartalsweise, Tests in QAS-Mandant 200."),
        ("6. Freigabe",
         signatures("Berthold Hartmann", "MES-Architekt", "Brennhagen Elektronik AG",
                    SAPCOE.split(",")[0], "Head of SAP CoE", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_="22.10.2022")),
    ]
    write_doc(BASE / fname, H, "SAP MES (Manufacturing Execution) Systemdokumentation",
              secs, subtitle="REA-SAP-MES-2022")


def sap_s4hana(fname: str):
    secs = [
        ("Dokumentenkontrolle",
         [["Feld", "Wert"],
          ["Titel", "SAP S/4HANA - Konzern-Systemdokumentation und Rollout-Roadmap"],
          ["Kuerzel", "REA-SAP-S4-2022"],
          ["Version", "2.2"],
          ["Verantwortlich", SAPCOE],
          ["Implementierungspartner", "Accenture (Lead, Vertragsvolumen ca. 12 Mio. EUR Multi-Year)"],
          ["Stand", "Dezember 2022 (Rollout-Phase 2)"]]),
        ("1. Programmuebersicht",
         "Konzernweite S/4HANA-Migration auf Basis SAP S/4HANA 2022 (FPS02). Programmname 'PROJECT NEXUS'. "
         "Programm-Sponsor Laura Bauer (CFO), Programm-Manager Dr. Stefan Lichter (SAP CoE), Lead-Partner "
         "Accenture (Programm-Direktorin Birgit Kaltenmark). Phasen-Plan: Phase 1 (2022) Aufsetzen Konzern-"
         "Template; Phase 2 (2023) Pilot Heilbronn FI/CO; Phase 3 (2024) Rollout Polen, Tschechien, Ungarn; "
         "Phase 4 (2025) Rollout Asien (RCN Shanghai) und finale Module; Phase 5 (2026) Optimierung, KI/IBP, "
         "Hyperautomation."),
        ("2. Technische Architektur",
         [["Komponente", "Details"],
          ["SAP S/4HANA Version", "2022 FPS02 (Initial), Upgrade-Plan auf 2023 in 2024"],
          ["Datenbank", "SAP HANA 2.0 SPS07, in-memory, 24 TB Hauptspeicher"],
          ["Hosting", "Microsoft Azure Germany West Central (M192ms_v2, Pilot-Mandant); On-Prem fuer Produktiv-Mandant 100 bis Ende 2023"],
          ["Mandanten", "100 Produktiv, 200 QAS, 300 DEV, 900 Schulung"],
          ["Module aktiv", "FI, CO, MM, SD, PP, PM, QM, EWM, WM, BPC (Konsolidierung)"],
          ["Erweiterungen", "Group Reporting (Konsolidierung), Central Finance Pilot, Cloud-Connector zu SuccessFactors"]]),
        ("3. Mandanten- und Konzernstruktur",
         "Im SAP S/4HANA werden alle 7 Konzerngesellschaften abgebildet (REG, RSG, RPL, RCZ, RHU, RCN, RHO). "
         "Konzernwaehrung EUR, lokale Berichtswaehrungen werden parallel gefuehrt (PLN, CZK, HUF, CNY). "
         "IFRS-Bilanzierung im Konzernkontenplan (Anpassung gemaess REA_IFRS_Bilanzierungsrichtlinie 2022). "
         "Group Reporting (Konsolidierung) ab Geschaeftsjahr 2024 produktiv geplant."),
        ("4. Sicherheit (SAP-GRC)",
         "SAP GRC Access Control 12.0 (Risikoanalyse, Provisionierung, Notfalluser-Mgmt), SAP GRC Process "
         "Control 12.0 (IKS), SAP GRC Risk Management. SoD-Regelwerk ca. 4.200 kritische Risiko-Definitionen "
         "(SAP-Standard + 280 konzernspezifische). Quartalsweise SoD-Reviews."),
        ("5. Betrieb",
         "Operativer Betrieb durch Konzern-Basis-Team (12 FTE) + Accenture Managed-Service (24/7 SLA). "
         "Patching quartalsweise. SAP-Solution-Manager 7.2 als zentrales Werkzeug fuer ChaRM, EWA, Monitoring."),
        ("6. Kosten",
         "Gesamtprogrammkosten 'NEXUS' geschaetzt 26 Mio. EUR (Capex + Opex 2022-2026), davon 14 Mio. EUR "
         "Capex (aktivierungsfaehige Eigenleistungen + Lizenzen) gemaess IAS 38. Genehmigt durch Vorstand am "
         "08.02.2022 und Aufsichtsrat (Beschluss 15.02.2022)."),
        ("7. Freigabe",
         signatures(SAPCOE.split(",")[0], "Head of SAP CoE", "Brennhagen Elektronik AG",
                    CFO.split(",")[0], "CFO / Programm-Sponsor", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_="14.12.2022")),
    ]
    write_doc(BASE / fname, H, "SAP S/4HANA - Konzern-Systemdokumentation und Rollout-Roadmap (Project NEXUS)",
              secs, subtitle="REA-SAP-S4-2022")


def teamcenter(fname: str):
    secs = [
        ("Dokumentenkontrolle",
         [["Feld", "Wert"],
          ["Titel", "Siemens Teamcenter PLM - Konzern-Systemdokumentation"],
          ["Kuerzel", "REA-PLM-TC-2022"],
          ["Version", "0.9 (ENTWURF)"],
          ["Verantwortlich", "Johannes Schaal, PLM-Lead Konzern"],
          ["Stand", "September 2022 (Entwurf, finale Freigabe ausstehend)"]]),
        ("1. Loesungsbeschreibung",
         "Siemens Teamcenter 14.2 als zentrales PLM-System der Brennhagen Elektronik AG. Hauptanwender: RSG "
         "Muenchen (ADAS, Embedded SW), Engineering REG Heilbronn (Konstruktion, Stuecklisten), QM. "
         "Active Workspace 6.2 fuer Web-Zugriff. Implementierungspartner: Siemens Digital Industries Software."),
        ("2. Funktionsumfang",
         "Stuecklisten (BoM) Engineering und Manufacturing, Aenderungsmanagement (ECR/ECN/ECO mit Workflow "
         "ueber Stage-Gate), CAD-Integration (Siemens NX, Catia V5 fuer Mercedes-Templates, Solidworks fuer "
         "RSG), Dokumentenmanagement, Variantenkonfiguration, Anforderungsmanagement (Polarion-Integration "
         "via OSLC), SAP-Integration ueber TC4S (Teamcenter for SAP)."),
        ("3. Werks-Anbindung",
         [["Standort", "Nutzung", "Anbindung"],
          ["RSG Muenchen", "ADAS-Entwicklung, SW-Plattform, ASPICE-Konformitaet", "primaerer PLM-Standort"],
          ["REG Heilbronn", "Mechanische Konstruktion, Werks-BoM", "VPN, lokale Caching-Server"],
          ["RPL/RCZ/RHU", "Lesezugriff Manufacturing-BoM", "VPN read-only"],
          ["Externe Engineering-Dienstleister", "Bertrandt, EDAG (limitiert)", "B2B-Federation"]]),
        ("4. Sicherheit",
         "Authentifizierung ueber Entra ID SAML; Rollenmodell ca. 65 Rollen (Engineering, QM, Vertrieb, Service). "
         "Schutz vertraulicher Konstruktionsdaten (insbesondere ADAS-Algorithmen) ueber Data-Loss-Prevention "
         "(Microsoft Purview) und Watermarking bei externen Sharings."),
        ("5. Offene Punkte (Entwurf)",
         "Warm-Standby PLM in Heilbronn (siehe DR-Test 2023 Finding F1) noch nicht umgesetzt; Investitionsantrag "
         "in Capex-Liste 2024. Polarion-Integration zu RSG noch im PoC-Status. ECO-Workflow fuer kritische "
         "Sicherheits-Aenderungen (ASIL D) wird im Q4/2023 final ueberarbeitet."),
        ("6. Status",
         "Dieser Bericht hat den Status ENTWURF und ist nicht zur externen Weitergabe geeignet. Final-Freigabe "
         "geplant nach finalem Architecture-Review-Board am 15.11.2023."),
    ]
    write_doc(BASE / fname, H, "Siemens Teamcenter PLM - Konzern-Systemdokumentation (Entwurf)",
              secs, subtitle="REA-PLM-TC-2022", draft=True)


def tisax_audit(fname: str):
    secs = [
        ("Dokumentenkontrolle",
         [["Feld", "Wert"],
          ["Berichtstitel", "TISAX-Audit-Bericht 2023 (VDA-ISA 5.1, Assessment Level AL3)"],
          ["Kuerzel", "REA-TISAX-2023"],
          ["Auditor", "DEKRA Certification GmbH, Stuttgart"],
          ["Lead-Auditor", "Reinhard Knoeller (DEKRA)"],
          ["Auditperiode", "16.05. - 27.05.2023 (vor Ort + Remote)"],
          ["Status", "freigegeben, Label-Vergabe erfolgt 14.07.2023"],
          ["TISAX-Scope-IDs", "S00x9712, S00x9713 (Information Security inkl. Prototypenschutz)"]]),
        ("1. Auditgegenstand",
         "TISAX-Audit (Trusted Information Security Assessment Exchange) gemaess VDA-ISA-Katalog Version 5.1 "
         "fuer die Standorte REG Heilbronn (Hauptwerk Produktion) und RSG Muenchen (ADAS-Entwicklung). "
         "Geprueft wurden Anforderungen mit Bezug zu Informationssicherheit und Schutz von Prototypen (insb. "
         "Mercedes-Templates, BMW-ADAS, Stellantis-Powertrain)."),
        ("2. Audit-Ergebnis",
         [["Pruefmodul", "Status", "Reife (Soll/Ist)"],
          ["IS-Module (Informationssicherheit)", "konform mit Major NC: 0, Minor NC: 3, Beobachtungen: 11", "Soll 3,0 / Ist 3,2"],
          ["Prototypenschutz (PT-Module)", "konform mit Minor NC: 1, Beobachtungen: 4", "Soll 3,0 / Ist 3,1"],
          ["Daten-Anbindung (DZ-Module)", "konform", "Soll 3,0 / Ist 3,0"]]),
        ("3. Wesentliche Findings",
         "(NC-1, Minor) Berechtigungsreview im SAP-System nur halbjaehrlich, VDA-ISA fordert quartalsweise "
         "fuer kritische Rollen - Massnahme: Anpassung auf quartalsweise ab Q3/2023.\n"
         "(NC-2, Minor) Loeschkonzept Prototypen-Daten enthielt Luecken bei extern gespiegelten Daten - "
         "Massnahme: Aktualisierung Loeschkonzept und AVV-Inventar bis 30.09.2023.\n"
         "(NC-3, Minor) Awareness-Training fuer externe Engineering-Dienstleister (Bertrandt) war 2022 "
         "ueberfaellig - Massnahme: Refresh durchgefuehrt 06/2023.\n"
         "(NC-4, Minor, Prototypenschutz) Zutritt zu Prototypen-Bereich Heilbronn noch teilweise mit "
         "Schluesselsystem statt Badge - Massnahme: Badge-Rollout abgeschlossen 12/2023."),
        ("4. Massnahmenplan",
         "Massnahmenplan REA-MNP-2023-TISAX wurde am 21.06.2023 freigegeben. Tracking ueber GRC-Tool. "
         "Status-Review zum 15.10.2023 ergab: 2 Findings geschlossen, 2 in Bearbeitung im Plan."),
        ("5. Label und Gueltigkeit",
         "Label-Vergabe: AL3 'Information Security' und AL3 'Prototype Protection' fuer Standorte Heilbronn "
         "und Muenchen. Gueltigkeit 3 Jahre bis 13.07.2026; Surveillance-Audit nach 18 Monaten (geplant Q1/2025)."),
        ("6. Freigabe",
         signatures("Reinhard Knoeller", "Lead Auditor", "DEKRA Certification GmbH",
                    CISO.split(",")[0], "CISO", "Brennhagen Elektronik AG",
                    place="Stuttgart", date_str_="14.07.2023")),
    ]
    write_doc(BASE / fname, H, "TISAX-Audit-Bericht 2023 - DEKRA Certification GmbH",
              secs, subtitle="REA-TISAX-2023 / VDA-ISA 5.1 AL3", confidential=True)


# --------------------------------------------------------------------------
# Misplaced docs (non-IT types that happen to live in this folder)
# --------------------------------------------------------------------------

def av_bjoern_franke(fname: str):
    """RSG-Arbeitsvertrag, Compliance Officer."""
    head = HRSG
    name = "Bjoern Franke"
    rolle = "Compliance Officer"
    secs = [
        ("Vertragsparteien",
         "Diese Vereinbarung wird abgeschlossen zwischen\n\n"
         f"Brennhagen Software GmbH, {head['addr']}, eingetragen im {head['hrb']}, vertreten durch den "
         "Geschaeftsfuehrer Dr. Klaus Kessler (im Folgenden 'Arbeitgeberin')\n\nund\n\n"
         f"Herrn {name}, geb. 1985, wohnhaft Lindwurmstrasse 142, 80337 Muenchen "
         "(im Folgenden 'Arbeitnehmer')."),
        ("Praeambel",
         "Die Brennhagen Software GmbH ist die fuer ADAS und Embedded Software zustaendige Tochtergesellschaft "
         "der Brennhagen Elektronik AG (Konzern, Sitz Stuttgart). Sie verstaerkt zum 01.01.2020 die "
         "Compliance- und Internal-Audit-Funktion im Hinblick auf die geplante Boersennotierung der "
         "Konzernmutter sowie die wachsenden regulatorischen Anforderungen (CRA, NIS-2, DSGVO, IFRS, IATF, "
         "TISAX). Der Arbeitnehmer wurde nach umfassendem Auswahlverfahren ausgewaehlt."),
        ("§§", ("clauses", [
            ("§ 1 Beginn und Probezeit",
             ["Das Arbeitsverhaeltnis beginnt am 1. Januar 2020 und wird unbefristet abgeschlossen. "
              "Die Probezeit betraegt sechs Monate.",
              "Waehrend der Probezeit kann das Arbeitsverhaeltnis mit einer Frist von zwei Wochen "
              "gekuendigt werden."]),
            ("§ 2 Aufgabengebiet",
             [f"Der Arbeitnehmer wird als {rolle} eingestellt und uebernimmt insbesondere Aufgaben "
              "im Compliance-Management-System (CMS), interne Untersuchungen, Hinweisgeber-Bearbeitung, "
              "Schulungsmanagement und Beratung der Geschaeftsfuehrung sowie der Konzernrechtsabteilung.",
              "Direkter Berichtsweg an die Geschaeftsfuehrung RSG sowie fachlich an Dr. Maria Hellmig, "
              "Konzernrechtsabteilung der Brennhagen Elektronik AG."]),
            ("§ 3 Verguetung",
             ["Das Jahresbruttogehalt betraegt EUR 110.000 (in Worten: einhundertzehntausend Euro), "
              "zahlbar in zwoelf gleichen Monatsraten zum Monatsende.",
              "Zusaetzlich besteht Anspruch auf einen variablen Bonus bis zu 15 % des Jahresbruttogehalts "
              "nach Zielvereinbarung."]),
            ("§ 4 Arbeitszeit, Urlaub, Sonstiges",
             ["Die regelmaessige Arbeitszeit betraegt 40 Stunden pro Woche; Mehrarbeit ist mit dem Gehalt "
              "abgegolten. Der Jahresurlaub betraegt 30 Arbeitstage.",
              "Es gilt die Konzern-Compliance-Richtlinie, der Verhaltenskodex sowie die Vertraulichkeits-"
              "vereinbarung in der jeweils gueltigen Fassung."]),
            ("§ 5 Schlussbestimmungen",
             ["Nebenabreden beduerfen der Schriftform. Aenderungen und Ergaenzungen ebenfalls. "
              "Sollte eine Bestimmung unwirksam sein, bleibt der uebrige Vertrag wirksam."]),
        ])),
        ("Unterschriften",
         signatures(name, rolle, "—",
                    "Dr. Klaus Kessler", "Geschaeftsfuehrer", "Brennhagen Software GmbH",
                    place="Muenchen", date_str_="11.12.2019")),
    ]
    write_doc(BASE / fname, head, f"Arbeitsvertrag - {name} ({rolle})",
              secs, subtitle="Brennhagen Software GmbH / Compliance Officer")


def jg_wolfgang_fisch(fname: str):
    """RSG-Jahresgespraech 2023, Dr. Wolfgang Fischer."""
    head = HRSG
    secs = [
        ("Stammdaten",
         [["Feld", "Wert"],
          ["Mitarbeiter", "Dr. Wolfgang Fischer"],
          ["Personalnummer", "RSG-073"],
          ["Position", "Senior Engineer ADAS Embedded SW"],
          ["Eintrittsdatum", "01.10.2008"],
          ["Vorgesetzter", "Lars Wittmann, Lead Developer RSG"],
          ["Berichtsperiode", "01.01.2023 - 31.12.2023"],
          ["Gespraechs-Datum", "08.12.2023"]]),
        ("1. Rueckblick und Zielerreichung 2023",
         "Herr Dr. Fischer hat die im Vorjahr vereinbarten Ziele in 2023 weit ueberwiegend erreicht. "
         "Im Projekt ADAS-V4D (Radar Fusion Steuergeraet) hat er die technische Verantwortung fuer die "
         "Sensordaten-Fusion uebernommen und die ASIL-B Sicherheitsanforderungen gemaess ISO 26262 erfolgreich "
         "implementiert. Sein Team (3 Junior-Entwickler, 2 Werkstudenten) wurde stabil weiterentwickelt; "
         "Mitarbeitendenzufriedenheit (Pulse-Befragung) liegt bei 4,4/5,0 (Vorjahr 4,2)."),
        ("2. Zielerreichungsgrad nach OKR-Bewertung",
         [["Ziel", "Gewichtung", "Ist", "Bewertung"],
          ["ASIL-B Lieferung Mercedes EQS-Projekt", "30 %", "100 %", "5 - uebertroffen"],
          ["Code-Quality KPI (SonarQube)", "20 %", "92 %", "4 - erreicht"],
          ["Patente / IP", "15 %", "1 Anmeldung eingereicht", "4 - erreicht"],
          ["Team-Coaching", "20 %", "alle JG der Mitarbeiter durchgefuehrt", "5"],
          ["Konzern-Awareness (TISAX)", "15 %", "Modul absolviert", "4"]]),
        ("3. Kompetenzen und Entwicklung",
         "Herr Dr. Fischer bringt herausragende technische Tiefe in Sensorfusion, Kalman-Filter und FuSi-"
         "Architektur. Entwicklungsfeld: Fuehrungskommunikation - Coaching durch externen Coach (Frau Dr. "
         "Niemann) wird in 2024 fortgesetzt. Beitrag zur ASPICE Level-3-Vorbereitung der RSG ist sehr "
         "geschaetzt."),
        ("4. Ziele 2024",
         [["Ziel", "KPI", "Gewichtung"],
          ["ADAS-V4D-Plattform: SW-Release v2.1 (BMW)", "Termin 30.06.2024", "30 %"],
          ["Aufbau Junior-Programm (2 neue Engineers)", "2 Onboardings <90 Tage", "20 %"],
          ["IP / Patente", "2 neue Anmeldungen", "15 %"],
          ["Konzern-Wissenstransfer Embedded SW", "4 Sessions an Konzern", "15 %"],
          ["Persoenliche Entwicklung Fuehrungs-KPI", "Pulse-Score >= 4,5", "20 %"]]),
        ("5. Verguetung und Bonus",
         "Verguetungsanpassung 2024 erfolgt im Rahmen der Konzern-Salary-Review (Anhang Tarifgitter RSG). "
         "Bonus 2023 wird mit Faktor 1,15 berechnet (Ziel: 100 %). Auszahlung im Februar 2024 gemaess "
         "Konzern-Bonus-Richtlinie."),
        ("6. Bestaetigung",
         signatures("Dr. Wolfgang Fischer", "Senior Engineer ADAS", "Brennhagen Software GmbH",
                    "Lars Wittmann", "Lead Developer / Vorgesetzter", "Brennhagen Software GmbH",
                    place="Muenchen", date_str_="08.12.2023")),
    ]
    write_doc(BASE / fname, head, "Jahresgespraech 2023 - Dr. Wolfgang Fischer",
              secs, subtitle="Mitarbeiterjahresgespraech / Pers.-Nr. RSG-073")


def ic_rechnung(fname: str, sender_key: str, monat: str, jahr: str, betrag_eur: int):
    """Intercompany invoice between subs."""
    senders = {
        "REG": (HREG, "Brennhagen Elektronik GmbH", "Heilbronn", "DE128456712",
                "Lieferung Baugruppen ICP-3 / BMS-12 an Konzernmutter zur Weiterverarbeitung"),
        "RPL": (HRPL, "Brennhagen Polska Sp. z o.o.", "Katowice", "PL6342845671",
                "EMS / SMD-Bestueckung im Auftrag REA (Konzernmutter)"),
        "RCZ": ({"name": "Brennhagen CZ s.r.o.", "addr": "Vinarska 18, 60300 Brno",
                 "hrb": "OR Bj 12378, NIP CZ29845671"},
                "Brennhagen CZ s.r.o.", "Brno", "CZ29845671",
                "Lieferung Steckverbinder-Baugruppen an Konzernmutter"),
    }
    header_used, name, ort, ust, leistung = senders[sender_key]
    secs = [
        ("Rechnungs-Kopf",
         [["Feld", "Wert"],
          ["Rechnungsnummer", f"{sender_key}-IC-{jahr}-{monat}"],
          ["Rechnungsdatum", f"{monat.lstrip('0')}-tens des Monats {monat}/{jahr}"],
          ["Leistungsdatum", f"Monat {monat}/{jahr}"],
          ["Lieferant", f"{name}, {ort}"],
          ["Empfaenger", "Brennhagen Elektronik AG, Vaihinger Strasse 120, 70567 Stuttgart"],
          ["Empfaenger USt-ID", "DE 815 421 738"],
          ["Lieferant USt-ID", ust],
          ["Zahlungsziel", "60 Tage netto (Konzern-Netting via Group Treasury, Markus Pflanzer)"],
          ["Verrechnungspreis-Grundlage", "Cost-Plus 5 % gemaess konzerneinheitlicher Verrechnungspreis-Richtlinie 2021 (REA_VP_TP_GuideLine_2021)"]]),
        ("Leistungsbeschreibung",
         leistung + ". Die Leistung wird gemaess Konzern-Liefer-Rahmenvertrag (IC-FRA-2022 zwischen "
         "REA und allen 100 %-Toechtern) abgerechnet. Mengen-Details, Materialnummern und Chargen "
         "sind in der separaten Liefer- und Stuecklisten-Aufstellung (SAP-Anhang) enthalten."),
        ("Rechnungspositionen (vereinfachte Konzern-IC-Position)",
         [["Pos.", "Beschreibung", "Menge", "Einzelpreis EUR", "Summe EUR"],
          ["1", f"IC-Leistung {leistung} (Cost-Plus 5 %)", "monatlich", f"{betrag_eur:,.0f}".replace(",", "."), f"{betrag_eur:,.0f}".replace(",", ".")]]),
        ("Steuern und Konditionen",
         [["Feld", "Wert"],
          ["Netto", f"{betrag_eur:,.0f}".replace(",", ".") + " EUR"],
          ["Umsatzsteuer", "Reverse-Charge (B2B EU, §13b UStG / Art. 196 MwStRL); 0 EUR"],
          ["Brutto", f"{betrag_eur:,.0f}".replace(",", ".") + " EUR"],
          ["Bankverbindung", "Konzern-Netting (kein Direkt-Zahlungsfluss, Verrechnung ueber Group Treasury Konto bei Deutsche Bank, IBAN DE89..0001)"],
          ["Verrechnungspreis-Methodik", "Cost-Plus (CP), benchmarked alle 2 Jahre durch KPMG (zuletzt 2022)"]]),
        ("Verweis Verrechnungspreis-Dokumentation",
         "Diese Intercompany-Rechnung ist Teil der konzernweiten Verrechnungspreis-Dokumentation gemaess "
         "§ 90 Abs. 3 AO (Local File / Master File). Verantwortlich: Dr. Heike Berger, Group Tax Director. "
         "Bei Aussenpruefung sind die zugrundeliegenden Cost-Pools, Allokationen und Margen vorzulegen. "
         "Die Konzern-Verrechnungspreis-Richtlinie 2021 (Version 2.0) regelt das Berichtswesen detailliert."),
        ("Unterschriften",
         signatures("CFO " + ort, "kfm. Leiter " + name, name,
                    "Laura Bauer", "CFO Konzern", "Brennhagen Elektronik AG",
                    place=ort, date_str_=f"{monat}/{jahr}")),
    ]
    write_doc(BASE / fname, header_used, f"Intercompany-Rechnung {sender_key}->REA {monat}/{jahr}",
              secs, subtitle="Konzern-Intercompany / Cost-Plus 5 %")


def eco_ecu900(fname: str):
    secs = [
        ("ECO-Stammdaten",
         [["Feld", "Wert"],
          ["ECO-Nummer", "ECO-2022-012"],
          ["Produkt", "ECU-900 (Powertrain-ECU Gen3)"],
          ["Aenderungs-Titel", "Wechsel des Spannungsreglers (LDO) auf alternative Bezugsquelle infolge Allokationsengpass"],
          ["Antragsteller", "Andreas Kurz, Lead-Hardware ECU-900"],
          ["Verantwortlich Engineering", "Stefan Hoffmann (CTO, bis 30.06.2024)"],
          ["Antragsdatum", "14.09.2022"],
          ["Status", "freigegeben durch CCB (Change Control Board) am 28.09.2022"],
          ["Kunden-Genehmigung erforderlich", "ja - VW (MEB+/MQB-Evo), Stellantis"]]),
        ("1. Anlass der Aenderung",
         "Allokationsengpass beim bisherigen Lieferanten (Texas Instruments TPS7B6933QDBVRQ1, AEC-Q100 Grade 1). "
         "Lieferzeiten haben sich auf 52 Wochen erhoeht; alternative Quelle bei Infineon (TLE4972A1H) wurde "
         "qualifiziert und ist mit deutlich kuerzeren Lieferzeiten verfuegbar."),
        ("2. Beschreibung der Aenderung",
         [["Element", "Vorher", "Nachher"],
          ["Bauteil", "TI TPS7B6933QDBVRQ1", "Infineon TLE4972A1H"],
          ["AEC-Qual", "Grade 1", "Grade 1"],
          ["Footprint", "SOT-223", "DPAK"],
          ["Layout-Aenderung", "—", "PCB Rev D02 -> Rev D03 (Pad-Anpassung)"],
          ["Stuecklisten-Position", "Pos. 24", "Pos. 24 (BoM Update)"],
          ["Hersteller-PN", "TPS7B6933QDBVRQ1", "TLE4972A1H"]]),
        ("3. Auswirkungen",
         "Funktionale Eigenschaften (Vout, Iout, Dropout, Temperaturbereich) bleiben in den Spezifikationsgrenzen. "
         "EMV- und Funktionssicherheits-Anforderungen (ISO 26262 ASIL D) wurden durch zusaetzlichen FMEA-Review "
         "und Testreihe (EMV-Halle Heilbronn, Berichtsnummer EMV-2022-094) bestaetigt. Keine Software-Aenderung. "
         "PPAP-Level 3 bei VW (Wolfsburg) und Stellantis (Mulhouse) angefordert."),
        ("4. Aufwand und Kosten",
         "Aufwand intern: 4 PT Hardware, 2 PT Test, 1 PT QA, 1 PT QM-Dokumentation. Einmalkosten Tools: 0 EUR. "
         "Wieder-Qualifizierungs-Kosten (PPAP, EMV): ca. 18.000 EUR. Erwartete Einsparung bei Material: "
         "ca. 0,06 EUR / Bauteil, bei ca. 240.000 Stueck p.a. = 14.400 EUR p.a."),
        ("5. Risiken",
         "Risiko (R1) Wechsel-bedingte Funktionsabweichung - bewertet als gering nach Tests. (R2) "
         "OEM-Genehmigung verzoegert sich - Mitigation: parallele PPAP-Bearbeitung mit beiden OEMs. (R3) "
         "Multi-Source langfristig sichern - Massnahme: STM-Bauteil als 3. Quelle in 2023 qualifizieren."),
        ("6. Freigaben",
         [["Rolle", "Person", "Datum"],
          ["Engineering", "Andreas Kurz", "26.09.2022"],
          ["Qualitaet", "Sabine Brand (Q-Konzern)", "27.09.2022"],
          ["Einkauf", "Heiko Dengler (Einkauf)", "28.09.2022"],
          ["CTO", "Stefan Hoffmann", "28.09.2022"],
          ["VW Wolfsburg (PPAP)", "ausstehend / 11/2022 erwartet", "—"],
          ["Stellantis Mulhouse (PPAP)", "ausstehend / 11/2022 erwartet", "—"]]),
    ]
    write_doc(BASE / fname, H, "Engineering Change Order ECO-2022-012 - ECU-900 LDO-Wechsel",
              secs, subtitle="Powertrain-ECU Gen3 / Multi-Source-Strategie")


def lasten_pflicht_heilbronn(fname: str):
    secs = [
        ("Dokumentenkontrolle",
         [["Feld", "Wert"],
          ["Projekt", "PRJ-2023-005 Heilbronn Plant Expansion"],
          ["Dokument", "Pflichtenheft (Technical Specification)"],
          ["Version", "1.2"],
          ["Projektleitung", "Andreas Maier, Werkleiter REG"],
          ["Sponsor", "Dr. Thomas Weber, COO"],
          ["Architektur-Verantwortung IT", ARCH]]),
        ("1. Projektkontext",
         "Erweiterung des Werks Heilbronn um Halle 4 (BMS-Linie 'BMS-12 EV-Pack 800 V'), inkl. "
         "Neuaufbau der Werks-IT-Infrastruktur (Edge-Cluster, OT-Switche, MES-Lokal), Modernisierung "
         "der bestehenden Linien-Anbindung an SAP DMC / SAP S/4HANA und Integration in Konzern-SIEM."),
        ("2. Systemarchitektur",
         "Halle 4 erhaelt einen lokalen Edge-Cluster (Dell PowerEdge R650, 4 Knoten, VMware vSphere 8) "
         "fuer die latenzkritische MES-Funktionalitaet sowie die Verbindung zu SPS- und Roboter-Steuerungen "
         "(Bosch Rexroth MTX, ABB IRC5). Die Anbindung an das Konzern-RZ Stuttgart erfolgt ueber redundante "
         "10-Gbit-Glasfaser. SAP DMC (MES-Cloud) ist im Konzern-Tenant gehostet."),
        ("3. Softwarearchitektur",
         "MES-Application Layer in SAP DMC; Hardware Abstraction Layer (HAL) basiert auf OPC-UA-Servern "
         "(Kepware) und MQTT-Broker (HiveMQ) im OT-DMZ. Application Layer (Werkerterminals) wird ueber "
         "Microsoft Surface Pro 9 (Defender for Endpoint, Intune) mit Bisson-Werker-App betrieben."),
        ("4. Anforderungen Sicherheit",
         [["Anforderung", "Beschreibung"],
          ["Segmentation", "OT-Level 0-3 strikt durch Stormshield IF-Firewalls getrennt"],
          ["Authentifizierung", "alle Werkertypen ueber Smartcard + PIN; Service-Engineer ueber Entra ID"],
          ["Monitoring", "SIEM-Anbindung an Microsoft Sentinel; OT-Sensoren via Claroty Sensor"],
          ["Patching", "Patch-Fenster wochentlich Sonntag 22-04 Uhr in Abstimmung mit Produktion"],
          ["Backup", "Veeam B&R, RPO 15 min, Offsite zum Stuttgart RZ"]]),
        ("5. Schnittstellen",
         "SAP DMC <-> SAP S/4HANA (PI/PO), SAP DMC <-> SPS (OPC-UA), SAP DMC <-> WMS (iDoc), "
         "Werker-App <-> SAP DMC (REST), Auditing <-> Splunk via Sentinel-Forwarder."),
        ("6. Annahmen, Abhaengigkeiten, Risiken",
         "Annahme: Hallen-Anbindung an Werks-Backbone erfolgt fertiggestellt bis 31.10.2023. "
         "Abhaengigkeit: SAP DMC Release 2403 fuer einige Funktionen. "
         "Risiken: Liefertermin Dell PowerEdge (Q4/2023 Allokationsrisiko); OT-Switche Cisco IE3300 "
         "Lieferzeit derzeit 28 Wochen."),
        ("7. Freigabe",
         signatures("Andreas Maier", "Werkleiter REG Heilbronn", "Brennhagen Elektronik AG",
                    ARCH.split(",")[0], "Lead IT-Architekt", "Brennhagen Elektronik AG",
                    place="Heilbronn", date_str_="22.06.2023")),
    ]
    write_doc(BASE / fname, H, "Pflichtenheft - Heilbronn Plant Expansion (Halle 4 / BMS-12)",
              secs, subtitle="PRJ-2023-005 / Werks-Erweiterung Heilbronn")


def rpl_prozessaudit(fname: str):
    head = HRPL
    secs = [
        ("Audit-Stammdaten",
         [["Feld", "Wert"],
          ["Audit-Nr.", "RPL-PA-2023-001"],
          ["Audit-Typ", "Prozess-Audit (VDA 6.3)"],
          ["Auditierter Prozess", "SMT-Bestueckung Linie SMT-04"],
          ["Auditierter Standort", "Brennhagen Polska Sp. z o.o., Katowice (RPL)"],
          ["Audit-Team", "Marek Wojciechowski (Werkleiter), Tomasz Lewandowski (Q-Leitung), Sabine Brand (Q-Konzern, Lead-Auditorin)"],
          ["Audit-Datum", "14.-16.02.2023"],
          ["Status", "abgeschlossen, Massnahmen verfolgt"]]),
        ("1. Audit-Anlass",
         "Routinemaessiges internes Prozess-Audit gemaess VDA 6.3-Anforderungen, Frequenz jaehrlich pro "
         "kritischer Linie. Linie SMT-04 fertigt PCBA fuer ICP-3 (Infotainment) sowie BMS-12 (Subkomponenten)."),
        ("2. Vorgehen",
         "Audit gemaess VDA 6.3 P5 (Prozessfaehigkeit Produktion). Methodik: Beobachtung der Produktion, "
         "Stichprobenpruefungen, Interviews mit Werkern, Maschinen-Operatoren, Schichtleitern, Auswertung "
         "QM-Kennzahlen (FPY, ppm, Reklamationen 12 Monate)."),
        ("3. Beobachtungen / Findings",
         [["Nr.", "Schweregrad", "Beobachtung"],
          ["B-01", "Hinweis", "Lieferanten-Wareneingang fuer Bauteile mit Datums-Restriktion (MSL) lueckenhaft dokumentiert (vereinzelt)."],
          ["B-02", "Minor",   "Stencil-Reinigungs-Intervall an Linie SMT-04 ueberschritten (Soll 4 h, Ist 5-6 h beobachtet)."],
          ["B-03", "Minor",   "Kalibrierungsplakette an SPI-Geraet abgelaufen seit 14 Tagen."],
          ["B-04", "Hinweis", "Werker-Schulungsnachweise fuer 2 Neumitarbeiter unvollstaendig (PPE-Modul)."]]),
        ("4. Massnahmen",
         "(M-01) WE-Doku-Tool fuer MSL-Bauteile ergaenzt um Pflichtfelder (umgesetzt 28.02.2023, Verantw. "
         "T. Lewandowski). (M-02) Reinigungsintervall im Linien-Steuersystem auf Hard-Stop konfiguriert "
         "(umgesetzt 03.03.2023). (M-03) Kalibrierungsmanagement ueber CMMS-Tool 'eMaint' eingefuehrt, Reminder "
         "ueber Email 14 Tage vor Ablauf (umgesetzt 15.03.2023). (M-04) Schulungsnachweise digitalisiert "
         "und Trigger an HR ueber LMS (Cornerstone) gesetzt (umgesetzt 22.03.2023)."),
        ("5. Bewertung",
         "Gesamtbewertung Linie SMT-04: 92 % (Stufe A nach VDA-6.3-Bewertungsschluessel). Keine Major-Findings. "
         "Vorgesehene Folge-Pruefung im Q3/2023 (Wirksamkeitsnachweis Massnahmen)."),
        ("6. Unterschriften",
         signatures("Sabine Brand", "Lead-Auditorin (Q-Konzern)", "Brennhagen Elektronik AG",
                    "Marek Wojciechowski", "Werkleiter RPL", "Brennhagen Polska Sp. z o.o.",
                    place="Katowice", date_str_="17.02.2023")),
    ]
    write_doc(BASE / fname, head, "Prozess-Audit Bericht RPL-PA-2023-001 - SMT-Bestueckung Linie SMT-04",
              secs, subtitle="VDA 6.3 / Prozess-Audit RPL Katowice")


def loi_hungary(fname: str):
    secs = [
        ("Parteien",
         "Diese Absichtserklaerung (Letter of Intent, »LOI«) wird vereinbart zwischen\n\n"
         "(1) Brennhagen Elektronik AG, Vaihinger Strasse 120, 70567 Stuttgart, eingetragen im "
         "Handelsregister des Amtsgerichts Stuttgart unter HRB 726451 (»Kaeuferin«, vertreten durch "
         "den Vorstand Anna Mueller, CEO, und Laura Bauer, CFO), und\n\n"
         "(2) Industriepark Gyoer GmbH & JV-Partner (»Veraeusserin«, vertreten durch den Geschaeftsfuehrer "
         "Janos Vargas), Gyoer (Ungarn).\n\n"
         "Beraten werden die Parteien durch Hengeler Mueller (Frankfurt) auf Kaeuferseite und CMS "
         "Cameron McKenna (Budapest) auf Veraeussererseite. Notarielle Begleitung erfolgt durch Dr. Karin "
         "Sonneborn, Stuttgart."),
        ("Praeambel",
         "Die Brennhagen Elektronik AG verfolgt eine Wachstumsstrategie mit Schwerpunkt Sensorik fuer "
         "Automotive-Anwendungen. Die Brennhagen Hungary Kft. (»Zielgesellschaft«) ist ein etablierter Sensorik-"
         "Hersteller in Gyoer mit ca. 540 Mitarbeitenden und einem Umsatz von ca. 82 Mio. EUR (2018). "
         "Die Kaeuferin beabsichtigt, durch Erwerb der Zielgesellschaft das Konzernportfolio im Bereich "
         "Sensorik strategisch auszubauen und die Lieferkette fuer ADAS- und Powertrain-Anwendungen zu "
         "staerken."),
        ("§§", ("clauses", [
            ("§ 1 Transaktionsstruktur",
             ["Die Parteien beabsichtigen einen Share Deal: Kaeuferin erwirbt 100 % der Geschaeftsanteile "
              "an der Brennhagen Hungary Kft. von der Veraeusserin.",
              "Der Erwerb erfolgt voraussichtlich ueber eine deutsche Tochtergesellschaft der Kaeuferin "
              "(Brennhagen Holding GmbH, Stuttgart, HRB 821456)."]),
            ("§ 2 Indikativer Kaufpreis",
             ["Der indikative Kaufpreis betraegt vorlaeufig EUR 19.200.000 (in Worten: neunzehn Millionen "
              "zweihunderttausend Euro), zahlbar in bar bei Vollzug (Closing).",
              "Der Kaufpreis ist vorbehaltlich (a) zufriedenstellender Due Diligence (Financial, Tax, Legal, "
              "Commercial, IT, ESG); (b) Genehmigung durch Aufsichtsrat der Kaeuferin sowie ggf. zustaendiger "
              "Kartellbehoerden; (c) keine wesentlichen nachteiligen Veraenderungen (MAC)."]),
            ("§ 3 Due Diligence und Exklusivitaet",
             ["Die Veraeusserin gewaehrt der Kaeuferin Exklusivitaet bis 31.12.2019.",
              "Due Diligence wird durchgefuehrt durch KPMG (Financial/Tax), Hengeler Mueller (Legal), "
              "Roland Berger (Commercial), KPMG Cyber (IT/ITGC)."]),
            ("§ 4 Vertraulichkeit",
             ["Alle Informationen werden gemaess gesonderter NDA vom 14.06.2019 vertraulich behandelt. "
              "Verstoss-Strafzahlung: bis EUR 250.000 je Einzelfall."]),
            ("§ 5 Geltendes Recht",
             ["Auf diese Absichtserklaerung findet deutsches Recht Anwendung. Gerichtsstand: Stuttgart. "
              "Der finale Kaufvertrag wird ungarischem Recht unterliegen (Lex Rei Sitae)."]),
            ("§ 6 Verbindlichkeit",
             ["Diese Absichtserklaerung ist - mit Ausnahme der Regelungen zu Exklusivitaet (§ 3) und "
              "Vertraulichkeit (§ 4) - unverbindlich."]),
        ])),
        ("Unterschriften",
         signatures("Anna Mueller", "CEO", "Brennhagen Elektronik AG",
                    "Janos Vargas", "Geschaeftsfuehrer", "Industriepark Gyoer GmbH",
                    place="Stuttgart", date_str_="22.07.2019")),
    ]
    write_doc(BASE / fname, H, "Letter of Intent - Erwerb Brennhagen Hungary Kft. (Sensorik, Gyoer)",
              secs, subtitle="M&A 2019 / Aktenzeichen RHO-M&A-2019-04",
              confidential=True)


# --------------------------------------------------------------------------
# Main runner
# --------------------------------------------------------------------------

def main():
    written = 0

    # IT change-requests
    for num in CHANGE_CASES:
        it_change_request(f"IT_Change_Request_2023_{num}.docx", num); written += 1

    # IT patch protocols
    for num in PATCH_CASES:
        it_patch_protokoll(f"IT_Patch_Protokoll_2023_{num}.docx", num); written += 1

    # IT incidents (security)
    for key in INCIDENT_CASES:
        it_sicherheitsvorfall(f"IT_Sicherheitsvorfall_2023_{key}.docx", key); written += 1

    # IT system outages
    for num in OUTAGE_CASES:
        it_systemstoerung(f"IT_Systemstörung_2023_{num}.docx", num); written += 1

    # Big policy / strategy docs
    cloud_strategy("REA_Cloud_Strategie_2023.docx"); written += 1
    isms_cyber("REA_Cybersecurity_Policy_ISMS_2023.docx"); written += 1
    endpoint_policy("REA_Endpoint_Security_Policy_2023.docx"); written += 1
    iam_policy("REA_IAM_Identity_Access_Management_2023.docx"); written += 1
    gov_framework("REA_IT_Governance_Framework_2023.docx"); written += 1
    it_risikobericht("REA_IT_Risikobericht_2023.docx"); written += 1
    netzarchitektur("REA_Netzwerkarchitektur_Dokument_2023.docx"); written += 1
    pen_test("REA_Penetrationstest_Bericht_2023.docx"); written += 1
    backup_konzept("REA_Backup_Konzept_2022.docx"); written += 1
    bcp_2023("REA_BCP_Business_Continuity_Plan_2023.docx"); written += 1
    dr_test_2023("REA_Disaster_Recovery_Test_2023_ENTWURF.docx"); written += 1
    sap_mes("REA_SAP_MES_Produktionssteuerung_2022.docx"); written += 1
    sap_s4hana("REA_SAP_S4HANA_Systemdokumentation_2022.docx"); written += 1
    teamcenter("REA_Siemens_Teamcenter_PLM_2022_ENTWURF.docx"); written += 1
    tisax_audit("REA_TISAX_Audit_Bericht_2023.docx"); written += 1

    # Misplaced HR / project / IC / M&A docs
    av_bjoern_franke("AV_085_Björn_Franke_85_Compliance_Officer.docx"); written += 1
    jg_wolfgang_fisch("JG_073_Dr._Wolfgang_Fisch_2023.docx"); written += 1
    ic_rechnung("REG_IC_Rechnung_2021_06.docx", "REG", "06", "2021", 248_500); written += 1
    ic_rechnung("REG_IC_Rechnung_2021_07.docx", "REG", "07", "2021", 261_200); written += 1
    ic_rechnung("RPL_IC_Rechnung_2022_07.docx", "RPL", "07", "2022", 312_400); written += 1
    ic_rechnung("RCZ_IC_Rechnung_2020_02.docx", "RCZ", "02", "2020", 142_800); written += 1
    eco_ecu900("ECO_ECU-900_012_Engineering_Change_2022.docx"); written += 1
    lasten_pflicht_heilbronn("PRJ-2023-005_Pflichtenheft_Heilbronn_Plant_Expansion.docx"); written += 1
    rpl_prozessaudit("RPL_Prozessaudit_Beobachtung_2023_001.docx"); written += 1
    loi_hungary("LOI_Erwerb_Brennhagen_Hungary_Kft._2019.docx"); written += 1

    print(f"WROTE {written} docs")


if __name__ == "__main__":
    main()
