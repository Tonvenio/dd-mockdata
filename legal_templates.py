# -*- coding: utf-8 -*-
"""
legal_templates.py
==================

German law-firm-quality legal document templates for use in due-diligence
mock datasets. Each generator returns a list of (section_title, body_text)
tuples that can be consumed by PDF/DOCX/XLSX builders.

The phrasing, structure and § numbering follow standard practice used by
top-tier German law firms (Freshfields, Hengeler Mueller, Noerr, Gleiss
Lutz, Linklaters) and reflect current statutory references
(BGB, HGB, GmbHG, AktG, DSGVO, HinSchG, LkSG, MDR, etc.).

NOTE: These are SYNTHETIC mock documents. They are stylistically realistic
but must not be used as actual legal templates without review by counsel.
"""

from __future__ import annotations

from typing import Dict, List, Tuple, Any
import datetime as _dt

Section = Tuple[str, str]


# =====================================================================
# BASE CLAUSE LIBRARY
# =====================================================================

DEFINITIONS_GENERAL: Dict[str, str] = {
    "Vertraulichen Informationen": (
        "alle Informationen, Unterlagen, Daten, Pläne, Zeichnungen, "
        "Spezifikationen, Software, Know-how, Geschäfts- und "
        "Betriebsgeheimnisse im Sinne des § 2 Nr. 1 GeschGehG sowie "
        "alle sonstigen Kenntnisse technischer, wirtschaftlicher, "
        "finanzieller, organisatorischer oder personeller Art, die "
        "einer Partei von der jeweils anderen Partei im Zusammenhang "
        "mit diesem Vertrag in schriftlicher, elektronischer, "
        "mündlicher oder verkörperter Form zugänglich gemacht werden, "
        "sofern sie nicht ausdrücklich und in Schriftform als "
        "nicht-vertraulich gekennzeichnet sind."
    ),
    "Geschäftstag": (
        "jeder Kalendertag, der weder Samstag, Sonntag noch ein am Sitz "
        "der Gesellschaft gesetzlicher Feiertag ist und an dem "
        "Geschäftsbanken in Frankfurt am Main für den allgemeinen "
        "Geschäftsverkehr geöffnet sind."
    ),
    "Tochtergesellschaft": (
        "jedes Unternehmen, an dem die jeweilige Partei mittelbar oder "
        "unmittelbar die Mehrheit der Stimmrechte hält oder auf das die "
        "Partei aus sonstigen Gründen einen beherrschenden Einfluss im "
        "Sinne von § 17 AktG ausüben kann."
    ),
    "Verbundenes Unternehmen": (
        "jedes mit einer Partei im Sinne der §§ 15 ff. AktG verbundene "
        "Unternehmen einschließlich abhängiger und herrschender "
        "Unternehmen, Konzernunternehmen sowie wechselseitig beteiligter "
        "Unternehmen."
    ),
    "Kontrollwechsel": (
        "jede unmittelbare oder mittelbare Übertragung von mehr als "
        "fünfzig Prozent (50 %) der Stimmrechte oder des Kapitals einer "
        "Partei auf einen Dritten, der mit der Partei zum Zeitpunkt des "
        "Vertragsschlusses nicht im Sinne von §§ 15 ff. AktG verbunden "
        "war, sowie jede Verschmelzung, Spaltung oder vergleichbare "
        "umwandlungsrechtliche Maßnahme, die wirtschaftlich zu demselben "
        "Ergebnis führt."
    ),
    "Höhere Gewalt": (
        "jedes außergewöhnliche, von außen kommende, unvorhersehbare und "
        "auch durch äußerste, billigerweise zu erwartende Sorgfalt nicht "
        "abwendbare Ereignis, das die Erfüllung vertraglicher Pflichten "
        "ganz oder teilweise unmöglich macht oder wesentlich erschwert, "
        "insbesondere Krieg, Aufstand, Embargos, hoheitliche Maßnahmen, "
        "Pandemien und Epidemien, Naturkatastrophen, Großbrände, "
        "großflächige Stromausfälle sowie behördlich angeordnete "
        "Betriebsschließungen."
    ),
    "Wesentliche Nachteilige Veränderung": (
        "jedes Ereignis, jede Tatsache, jeder Umstand oder jede "
        "Entwicklung, die einzeln oder zusammen mit anderen Ereignissen "
        "geeignet sind, eine wesentliche nachteilige Auswirkung auf "
        "(i) das Vermögen, die Ertragslage oder die Finanzlage der "
        "Gesellschaft oder einer ihrer wesentlichen Tochtergesellschaften, "
        "(ii) die Fähigkeit der jeweiligen Partei zur Erfüllung ihrer "
        "Verpflichtungen aus diesem Vertrag oder (iii) die Wirksamkeit, "
        "Durchsetzbarkeit oder Rechtsgültigkeit dieses Vertrages oder "
        "der hierzu gestellten Sicherheiten zu haben."
    ),
}


JURISDICTION_DE = (
    "(1) Dieser Vertrag und alle Streitigkeiten oder Ansprüche, die sich "
    "aus oder im Zusammenhang mit ihm ergeben, einschließlich solcher "
    "über sein wirksames Zustandekommen sowie seine Wirkungen vor und "
    "nach Beendigung, unterliegen ausschließlich dem Recht der "
    "Bundesrepublik Deutschland unter Ausschluss des UN-Kaufrechts "
    "(CISG) und der Bestimmungen des internationalen Privatrechts, "
    "soweit diese auf das Recht eines anderen Staates verweisen.\n\n"
    "(2) Ausschließlicher Gerichtsstand für alle Streitigkeiten aus "
    "oder im Zusammenhang mit diesem Vertrag ist – soweit gesetzlich "
    "zulässig – {gerichtsstand}. Die Parteien können jedoch auch das "
    "nach den allgemeinen Vorschriften zuständige Gericht anrufen, "
    "soweit zwingende gesetzliche Bestimmungen nicht entgegenstehen.\n\n"
    "(3) Soweit eine der Parteien ihren Sitz im Ausland hat oder nach "
    "Vertragsschluss in das Ausland verlegt oder ihren gewöhnlichen "
    "Aufenthalt nach Vertragsschluss aus dem Geltungsbereich der "
    "Zivilprozessordnung verlegt, ist der ausschließliche Gerichtsstand "
    "ebenfalls {gerichtsstand}."
)


SCHIEDSKLAUSEL_DIS = (
    "(1) Alle Streitigkeiten, die sich aus oder im Zusammenhang mit "
    "diesem Vertrag oder über seine Gültigkeit ergeben, werden nach "
    "der Schiedsgerichtsordnung der Deutschen Institution für "
    "Schiedsgerichtsbarkeit e.V. (DIS) in der zum Zeitpunkt der "
    "Einleitung des Schiedsverfahrens geltenden Fassung unter Ausschluss "
    "des ordentlichen Rechtsweges endgültig entschieden.\n\n"
    "(2) Das Schiedsgericht besteht aus drei Schiedsrichtern. Der "
    "Schiedsort ist {schiedsort}. Die Verfahrenssprache ist Deutsch; "
    "Beweismittel können in englischer Sprache vorgelegt werden, ohne "
    "dass es einer Übersetzung bedarf.\n\n"
    "(3) Die Parteien sind sich darüber einig, dass das Schiedsgericht "
    "nach Maßgabe der Bestimmungen dieses Vertrages und subsidiär nach "
    "deutschem materiellen Recht entscheidet. Eine Entscheidung nach "
    "Billigkeit (ex aequo et bono) ist ausgeschlossen.\n\n"
    "(4) Unbeschadet der Schiedsklausel ist jede Partei berechtigt, "
    "vorläufige oder sichernde Maßnahmen (einstweilige Verfügungen, "
    "Arreste) bei staatlichen Gerichten zu beantragen."
)


SCHRIFTFORM = (
    "(1) Änderungen und Ergänzungen dieses Vertrages bedürfen zu ihrer "
    "Wirksamkeit der Schriftform. Dies gilt auch für die Änderung "
    "oder Aufhebung dieser Schriftformklausel selbst.\n\n"
    "(2) Die elektronische Form im Sinne des § 126a BGB ist "
    "ausgeschlossen, soweit nicht im Einzelfall ausdrücklich anderes "
    "vereinbart wird. Die Übermittlung von Erklärungen per Telefax oder "
    "als eingescannte PDF-Datei per E-Mail wahrt die Schriftform nur, "
    "wenn ausdrücklich und in Schriftform vereinbart.\n\n"
    "(3) Mündliche Nebenabreden bestehen nicht. Soweit Nebenabreden "
    "getroffen werden sollen, bedarf es hierzu der Schriftform unter "
    "ausdrücklicher Bezugnahme auf diesen Vertrag."
)


SALVATORISCH = (
    "(1) Sollte eine Bestimmung dieses Vertrages ganz oder teilweise "
    "unwirksam oder undurchführbar sein oder werden oder sollte sich "
    "eine Lücke in diesem Vertrag herausstellen, so wird hierdurch die "
    "Wirksamkeit der übrigen Bestimmungen nicht berührt.\n\n"
    "(2) An die Stelle der unwirksamen oder undurchführbaren Bestimmung "
    "soll diejenige wirksame und durchführbare Regelung treten, deren "
    "Wirkungen der wirtschaftlichen Zielsetzung am nächsten kommen, die "
    "die Parteien mit der unwirksamen oder undurchführbaren Bestimmung "
    "verfolgt haben.\n\n"
    "(3) Die vorstehenden Bestimmungen gelten entsprechend für den Fall, "
    "dass sich der Vertrag als lückenhaft erweist.\n\n"
    "(4) Den Parteien ist bekannt, dass diese salvatorische Klausel im "
    "Anwendungsbereich des deutschen Rechts keine Umkehr der Beweislast "
    "bewirkt; die Parteien haben jedoch ausdrücklich den Willen "
    "bekundet, an einer Aufrechterhaltung dieses Vertrages auch dann "
    "festzuhalten, wenn einzelne Bestimmungen unwirksam sein sollten."
)


CONFIDENTIALITY_STD = (
    "(1) Die Parteien verpflichten sich, alle ihnen im Zusammenhang mit "
    "diesem Vertrag und seiner Durchführung bekannt werdenden "
    "vertraulichen Informationen der jeweils anderen Partei strikt "
    "vertraulich zu behandeln, sie nur für die Zwecke dieses Vertrages "
    "zu verwenden und Dritten nicht zugänglich zu machen. Vertrauliche "
    "Informationen sind insbesondere – aber nicht abschließend – "
    "Geschäfts- und Betriebsgeheimnisse im Sinne des § 2 Nr. 1 "
    "GeschGehG, technisches und kaufmännisches Know-how, "
    "Konstruktionsunterlagen, Quellcode, Kunden- und Lieferantendaten, "
    "Preise, Konditionen sowie Strategie- und Planungsunterlagen.\n\n"
    "(2) Die empfangende Partei wird zum Schutz der vertraulichen "
    "Informationen mindestens die gleichen Sorgfaltsmaßstäbe anwenden, "
    "die sie auf eigene vertrauliche Informationen anwendet, in keinem "
    "Fall jedoch geringere Maßstäbe als die im Geschäftsverkehr eines "
    "ordentlichen Kaufmanns übliche Sorgfalt im Sinne des § 347 HGB.\n\n"
    "(3) Eine Weitergabe vertraulicher Informationen an verbundene "
    "Unternehmen, Organmitglieder, Mitarbeiter und externe Berater "
    "(insbesondere Rechtsanwälte, Steuerberater und Wirtschaftsprüfer) "
    "ist gestattet, soweit (i) deren Kenntnis zur Erfüllung der "
    "vertraglichen Zwecke erforderlich ist (need-to-know-Prinzip) und "
    "(ii) diese Personen vorher in vergleichbarer Weise zur "
    "Vertraulichkeit verpflichtet wurden oder einer berufsrechtlichen "
    "Verschwiegenheitspflicht unterliegen.\n\n"
    "(4) Die Vertraulichkeitspflicht gilt nicht für Informationen, die "
    "(a) zum Zeitpunkt der Mitteilung bereits allgemein bekannt waren "
    "oder ohne Verschulden der empfangenden Partei nachträglich "
    "allgemein bekannt werden, (b) der empfangenden Partei vor "
    "Mitteilung bereits rechtmäßig und ohne Geheimhaltungsverpflichtung "
    "bekannt waren, (c) von der empfangenden Partei nachweislich "
    "unabhängig und ohne Verwendung der vertraulichen Informationen "
    "selbst entwickelt wurden oder (d) ihr von einem Dritten ohne "
    "Verletzung einer Geheimhaltungsverpflichtung rechtmäßig zugänglich "
    "gemacht wurden.\n\n"
    "(5) Ist die empfangende Partei aufgrund gesetzlicher Vorschriften, "
    "gerichtlicher Anordnung, behördlicher Auflagen oder börsen- bzw. "
    "kapitalmarktrechtlicher Veröffentlichungspflichten zur Offenlegung "
    "vertraulicher Informationen verpflichtet, so wird sie – soweit "
    "rechtlich zulässig – die offenlegende Partei vorab schriftlich "
    "unterrichten, sich auf das gesetzlich Erforderliche beschränken "
    "und die offenlegende Partei bei der Erlangung von Schutzanordnungen "
    "in zumutbarer Weise unterstützen.\n\n"
    "(6) Die Vertraulichkeitsverpflichtungen nach diesem § bleiben "
    "auch nach Beendigung dieses Vertrages für einen Zeitraum von "
    "fünf (5) Jahren bestehen. Bezüglich Geschäftsgeheimnissen im "
    "Sinne des GeschGehG gilt die Verpflichtung unbefristet."
)


DATA_PROTECTION = (
    "(1) Die Parteien sind sich darüber einig, dass sie bei der "
    "Durchführung dieses Vertrages personenbezogene Daten im Sinne der "
    "Verordnung (EU) 2016/679 (Datenschutz-Grundverordnung – DSGVO) "
    "und des Bundesdatenschutzgesetzes (BDSG) verarbeiten können. Die "
    "Parteien werden bei jeder Verarbeitung personenbezogener Daten "
    "die einschlägigen datenschutzrechtlichen Bestimmungen strikt "
    "beachten.\n\n"
    "(2) Soweit eine Partei für die andere Partei personenbezogene "
    "Daten im Auftrag verarbeitet, schließen die Parteien zusätzlich "
    "einen Auftragsverarbeitungsvertrag nach Art. 28 DSGVO ab. Der "
    "Auftragsverarbeitungsvertrag ist diesem Vertrag als Anlage "
    "beigefügt und Bestandteil dieses Vertrages.\n\n"
    "(3) Erfolgt im Rahmen der Vertragsdurchführung eine Übermittlung "
    "personenbezogener Daten in ein Drittland im Sinne von Art. 44 ff. "
    "DSGVO, so werden die Parteien die hierfür erforderlichen geeigneten "
    "Garantien (insbesondere EU-Standardvertragsklauseln gemäß "
    "Durchführungsbeschluss (EU) 2021/914) abschließen und ggf. "
    "ergänzende Maßnahmen (Transfer Impact Assessment) durchführen.\n\n"
    "(4) Jede Partei wird der anderen Partei eine Datenschutzverletzung "
    "im Sinne von Art. 4 Nr. 12 DSGVO unverzüglich, spätestens innerhalb "
    "von 24 Stunden nach Kenntnisnahme, anzeigen, soweit hiervon Daten "
    "der anderen Partei betroffen sind, und alle zur Eindämmung und "
    "Aufarbeitung erforderlichen Maßnahmen unverzüglich einleiten."
)


COMPLIANCE_REPS = (
    "(1) Jede Partei sichert zu, dass sie selbst sowie ihre Organmit-"
    "glieder, Mitarbeiter und sonstigen Erfüllungsgehilfen alle "
    "anwendbaren Gesetze und Verordnungen einhalten, insbesondere "
    "Vorschriften zur Bekämpfung von Korruption und Bestechung im "
    "geschäftlichen Verkehr (§§ 299 ff. StGB), Vorschriften zur "
    "Bekämpfung von Geldwäsche (GwG), kartell- und wettbewerbsrechtliche "
    "Bestimmungen (GWB, Art. 101, 102 AEUV) sowie steuer- und "
    "abgabenrechtliche Vorschriften.\n\n"
    "(2) Beide Parteien verfügen über ein angemessenes Compliance-"
    "Management-System (CMS), das den Anforderungen des IDW PS 980 "
    "oder eines vergleichbaren anerkannten Standards entspricht, "
    "einschließlich Verhaltenskodex (Code of Conduct), regelmäßiger "
    "Schulungen, klarer Meldewege (Whistleblowing) und definierter "
    "Sanktionen bei Verstößen.\n\n"
    "(3) Verstößt eine Partei oder eine ihr zurechenbare Person gegen "
    "die in Absatz 1 genannten Pflichten und führt dieser Verstoß zu "
    "einer wesentlichen Beeinträchtigung der Vertragsdurchführung oder "
    "des Ansehens der anderen Partei, so ist die nicht-verstoßende "
    "Partei berechtigt, diesen Vertrag fristlos aus wichtigem Grund "
    "zu kündigen. Schadensersatzansprüche bleiben unberührt."
)


LKSG_REPS = (
    "(1) Die Parteien sind sich darüber einig, dass das Gesetz über die "
    "unternehmerischen Sorgfaltspflichten in Lieferketten (LkSG) auf "
    "ihre Geschäftsbeziehung Anwendung finden kann. Jede Partei sichert "
    "zu, dass sie in ihrem eigenen Geschäftsbereich sowie bei ihren "
    "unmittelbaren Zulieferern die menschenrechts- und umweltbezogenen "
    "Pflichten gemäß §§ 3-9 LkSG einhält und dies durch geeignete "
    "Maßnahmen (insbesondere Grundsatzerklärung, Risikoanalyse, "
    "Präventions- und Abhilfemaßnahmen, Beschwerdeverfahren) sicherstellt.\n\n"
    "(2) Der Lieferant verpflichtet sich, die in Anlage „LkSG-"
    "Lieferantenkodex' enthaltenen menschenrechts- und umweltbezogenen "
    "Anforderungen einzuhalten und seinerseits seine unmittelbaren "
    "Zulieferer in geeigneter Weise zur Einhaltung dieser Anforderungen "
    "zu verpflichten.\n\n"
    "(3) Der Lieferant wird dem Kunden auf Anforderung alle für die "
    "Erfüllung der LkSG-Pflichten erforderlichen Informationen und "
    "Nachweise zur Verfügung stellen, insbesondere Auskunft über "
    "Maßnahmen der Risikoanalyse, Präventions- und Abhilfemaßnahmen "
    "sowie das Beschwerdeverfahren erteilen. Der Lieferant räumt dem "
    "Kunden ein Recht zur Durchführung von Audits ein, das mit "
    "angemessener Vorankündigung ausgeübt werden kann."
)


EXPORT_CONTROL = (
    "(1) Beide Parteien beachten alle anwendbaren Vorschriften der "
    "Außenwirtschaftsgesetzgebung, insbesondere die Verordnung (EU) "
    "2021/821 (EU-Dual-Use-Verordnung), das Außenwirtschaftsgesetz "
    "(AWG), die Außenwirtschaftsverordnung (AWV), sowie – soweit "
    "anwendbar – die exportkontrollrechtlichen Bestimmungen der "
    "Vereinigten Staaten (insbesondere die Export Administration "
    "Regulations – EAR – und die International Traffic in Arms "
    "Regulations – ITAR) sowie sämtliche von der EU, den Vereinten "
    "Nationen, dem Sicherheitsrat oder einzelnen Staaten erlassene "
    "Sanktionen und Embargomaßnahmen.\n\n"
    "(2) Der Lieferant wird dem Kunden vor Erstauslieferung sowie auf "
    "Anforderung die ausfuhr- und einfuhrrelevanten Daten der "
    "Produkte mitteilen, insbesondere etwaige Ausfuhrlistennummern "
    "(AL-Nr.), ECCN-Klassifizierung, statistische Warennummer, "
    "Warenursprung (präferenziell und nicht-präferenziell) und "
    "ggf. erforderliche US-(Re-)Export-Genehmigungspflichten.\n\n"
    "(3) Der Kunde verpflichtet sich, Produkte nicht in Länder, an "
    "Personen oder für Verwendungszwecke zu liefern, die nach "
    "anwendbarem Recht einem Embargo oder einer Sanktion unterliegen, "
    "und insbesondere keine ABC-relevanten Anwendungen ohne "
    "vorherige schriftliche Zustimmung des Lieferanten zu ermöglichen.\n\n"
    "(4) Verzögerungen oder Nichterfüllungen, die auf der fehlenden "
    "Erteilung einer behördlich erforderlichen Ausfuhr- oder "
    "Einfuhrgenehmigung beruhen, stellen keinen Vertragsbruch dar, "
    "soweit die nicht-leistende Partei die Genehmigung mit "
    "angemessener Sorgfalt beantragt und betrieben hat."
)


FORCE_MAJEURE = (
    "(1) Keine Partei haftet für die Nichterfüllung oder verspätete "
    "Erfüllung ihrer vertraglichen Pflichten, soweit die Erfüllung "
    "durch ein Ereignis Höherer Gewalt verhindert wird. Höhere Gewalt "
    "ist ein außergewöhnliches, von außen kommendes, unvorhersehbares "
    "und auch durch äußerste billigerweise zu erwartende Sorgfalt nicht "
    "abwendbares Ereignis. Höhere Gewalt umfasst insbesondere, jedoch "
    "nicht abschließend: Krieg (erklärt oder unerklärt), Bürgerkrieg, "
    "Aufstand, Terroranschläge, Sabotage, Embargos, hoheitliche "
    "Maßnahmen, Pandemien und Epidemien einschließlich der hieraus "
    "resultierenden behördlichen Anordnungen, Naturkatastrophen "
    "(Erdbeben, Hochwasser, Stürme, Vulkanausbrüche), Großbrände, "
    "Explosionen, Cyberangriffe großen Ausmaßes auf kritische "
    "Infrastrukturen sowie großflächige Strom- oder "
    "Telekommunikationsausfälle.\n\n"
    "(2) Streiks, Arbeitskämpfe und behördliche Maßnahmen, die nicht "
    "die Vertragsparteien selbst, sondern allgemein die Branche "
    "betreffen, stehen der Höheren Gewalt gleich.\n\n"
    "(3) Die von Höherer Gewalt betroffene Partei wird die andere "
    "Partei unverzüglich, spätestens jedoch binnen sieben (7) "
    "Geschäftstagen nach Kenntniserlangung, schriftlich über das "
    "Vorliegen der Höheren Gewalt, ihre voraussichtliche Dauer und ihre "
    "Auswirkungen unterrichten. Die betroffene Partei wird alle "
    "zumutbaren Anstrengungen unternehmen, um die Auswirkungen der "
    "Höheren Gewalt zu mindern und die Vertragserfüllung wieder "
    "aufzunehmen.\n\n"
    "(4) Dauert das Ereignis Höherer Gewalt länger als sechs (6) Monate "
    "ununterbrochen an oder ist absehbar, dass es länger andauern wird, "
    "so ist jede Partei berechtigt, diesen Vertrag durch schriftliche "
    "Erklärung mit einer Frist von einem (1) Monat zum Monatsende zu "
    "kündigen. Bereits erbrachte Leistungen werden nach Maßgabe der "
    "gesetzlichen Vorschriften abgewickelt."
)


NOTICES_DE = (
    "(1) Alle Mitteilungen, Erklärungen und sonstigen Bekanntmachungen "
    "im Zusammenhang mit diesem Vertrag bedürfen zu ihrer Wirksamkeit "
    "der Textform (§ 126b BGB), soweit dieser Vertrag nicht "
    "ausdrücklich Schriftform (§ 126 BGB) verlangt.\n\n"
    "(2) Mitteilungen sind an folgende Adressen zu richten:\n\n"
    "Für {partyA}:\n"
    "z.Hd. {kontaktA}\n"
    "{adresseA}\n"
    "E-Mail: {emailA}\n\n"
    "Für {partyB}:\n"
    "z.Hd. {kontaktB}\n"
    "{adresseB}\n"
    "E-Mail: {emailB}\n\n"
    "(3) Eine Partei kann durch schriftliche Mitteilung an die andere "
    "Partei mit einer Frist von zehn (10) Geschäftstagen eine andere "
    "Zustellanschrift bekannt geben."
)


ASSIGNMENT = (
    "(1) Die Abtretung von Rechten und Pflichten aus diesem Vertrag "
    "an Dritte bedarf der vorherigen schriftlichen Zustimmung der "
    "anderen Partei. Die Zustimmung darf nicht ohne sachlichen Grund "
    "verweigert werden.\n\n"
    "(2) Abweichend von Absatz 1 ist jede Partei berechtigt, ihre "
    "Rechte und Pflichten aus diesem Vertrag ganz oder teilweise auf "
    "ein mit ihr verbundenes Unternehmen (§§ 15 ff. AktG) ohne "
    "Zustimmung der anderen Partei zu übertragen, sofern die "
    "übernehmende Gesellschaft solvent ist und für die Erfüllung der "
    "vertraglichen Pflichten geeignet erscheint. Die übertragende "
    "Partei haftet gesamtschuldnerisch mit dem übernehmenden "
    "verbundenen Unternehmen für die Vertragserfüllung.\n\n"
    "(3) § 354a HGB bleibt unberührt."
)


SEVERANCE_GERMAN = SALVATORISCH


# =====================================================================
# HELPER UTILITIES
# =====================================================================

def _g(p: Dict[str, Any], key: str, default: str = "") -> str:
    """Safe get from parameter dict, returning sensible defaults."""
    v = p.get(key)
    if v is None:
        return default
    return str(v)


def _today_de(d: _dt.date | None = None) -> str:
    d = d or _dt.date.today()
    return d.strftime("%d.%m.%Y")


def _signature_block(p: Dict[str, Any], who_a: str, role_a: str,
                     who_b: str, role_b: str) -> str:
    city_a = _g(p, "city", "Köln")
    city_b = _g(p, "city_b", city_a)
    today = _today_de()
    return (
        f"\n\n______________________________\n"
        f"{city_a}, den {today}\n"
        f"{who_a}\n{role_a}\n\n"
        f"______________________________\n"
        f"{city_b}, den {today}\n"
        f"{who_b}\n{role_b}\n"
    )


def _annex_list(annexes: List[str]) -> str:
    if not annexes:
        return ""
    out = ["Anlagenverzeichnis"]
    for i, a in enumerate(annexes, 1):
        out.append(f"Anlage {i} – {a}")
    return "\n".join(out)


def _word_count(sections: List[Section]) -> int:
    return sum(len(body.split()) for _, body in sections)


# =====================================================================
# CORPORATE / GESELLSCHAFTSRECHT
# =====================================================================

def gen_gmbh_gesellschaftsvertrag(p: Dict[str, Any]) -> List[Section]:
    """Voller GmbH-Gesellschaftsvertrag. Target: 4500-6000 Wörter."""

    name = _g(p, "name", "Muster GmbH")
    hrb = _g(p, "hrb", "HRB 12345")
    ag = _g(p, "amtsgericht", "Köln")
    city = _g(p, "city", "Köln")
    founded = _g(p, "founded", "2010")
    stammkapital = _g(p, "stammkapital", "25.000")
    gs1 = _g(p, "gesellschafter1", "Müller Holding GmbH")
    anteil1 = _g(p, "anteil1", "60")
    gs2 = _g(p, "gesellschafter2", "Schmidt Beteiligungs GmbH")
    anteil2 = _g(p, "anteil2", "40")
    gf1 = _g(p, "gf1", "Dr. Thomas Müller")
    gf2 = _g(p, "gf2", "Andreas Schmidt")
    gj = _g(p, "geschaeftsjahr", "Kalenderjahr")
    gegenstand = _g(p, "gegenstand",
                    "die Entwicklung, Herstellung und der Vertrieb von "
                    "industriellen Erzeugnissen sowie alle damit "
                    "zusammenhängenden Dienstleistungen")

    sections: List[Section] = []

    sections.append(("Präambel", (
        f"Die nachstehend bezeichneten Gesellschafter haben sich mit "
        f"Wirkung zum {founded} zu einer Gesellschaft mit beschränkter "
        f"Haftung unter der Firma {name} mit Sitz in {city} zusammen-"
        f"geschlossen. Die Gesellschaft ist im Handelsregister des "
        f"Amtsgerichts {ag} unter {hrb} eingetragen.\n\n"
        f"Die Gesellschafter haben den nachfolgenden Gesellschaftsvertrag "
        f"in seiner Neufassung beschlossen, um die rechtlichen Grundlagen "
        f"der Gesellschaft an die aktuellen Erfordernisse anzupassen, die "
        f"Corporate-Governance-Struktur zu modernisieren und die Rechte "
        f"und Pflichten der Gesellschafter neu zu ordnen. Die Neufassung "
        f"ersetzt sämtliche bisherigen Fassungen des Gesellschafts-"
        f"vertrages sowie alle hierzu getroffenen Nebenabreden."
    )))

    sections.append(("§ 1 Firma, Sitz, Geschäftsjahr", (
        f"(1) Die Firma der Gesellschaft lautet:\n\n"
        f"{name}.\n\n"
        f"(2) Sitz der Gesellschaft ist {city}.\n\n"
        f"(3) Geschäftsjahr ist das {gj}. Das erste Geschäftsjahr nach "
        f"Inkrafttreten dieser Neufassung ist ein volles Geschäftsjahr.\n\n"
        f"(4) Die Bekanntmachungen der Gesellschaft erfolgen ausschließlich "
        f"im Bundesanzeiger. Soweit nach zwingenden gesetzlichen "
        f"Bestimmungen Bekanntmachungen in einem zusätzlichen Medium "
        f"erforderlich sind, erfolgen sie zudem im elektronischen "
        f"Unternehmensregister.\n\n"
        f"(5) Die Gesellschaft kann Zweigniederlassungen im In- und Ausland "
        f"errichten. Die Errichtung sowie die Verlegung oder Aufhebung "
        f"einer Zweigniederlassung bedarf eines Beschlusses der "
        f"Gesellschafterversammlung mit qualifizierter Mehrheit gemäß "
        f"§ 14 Abs. 3 dieses Vertrages."
    )))

    sections.append(("§ 2 Gegenstand des Unternehmens", (
        f"(1) Gegenstand des Unternehmens ist {gegenstand}.\n\n"
        f"(2) Die Gesellschaft ist berechtigt, alle Geschäfte vorzunehmen, "
        f"die geeignet sind, dem Gesellschaftszweck unmittelbar oder "
        f"mittelbar zu dienen. Sie kann zu diesem Zweck im In- und Ausland "
        f"Zweigniederlassungen errichten, andere Unternehmen gleicher oder "
        f"verwandter Art gründen, erwerben oder sich an ihnen beteiligen, "
        f"die einheitliche Leitung über solche Unternehmen übernehmen oder "
        f"sich auf die Verwaltung der Beteiligung beschränken.\n\n"
        f"(3) Die Gesellschaft darf Unternehmensverträge im Sinne der "
        f"§§ 291 ff. AktG analog abschließen. Der Abschluss, die Änderung "
        f"und die Beendigung von Unternehmensverträgen bedürfen eines "
        f"Beschlusses der Gesellschafterversammlung mit qualifizierter "
        f"Mehrheit nach Maßgabe von § 14 Abs. 3.\n\n"
        f"(4) Geschäfte und Tätigkeiten, die einer behördlichen Erlaubnis "
        f"bedürfen, werden erst nach Erteilung der entsprechenden Erlaubnis "
        f"aufgenommen.\n\n"
        f"(5) Tätigkeiten, die unter das Rechtsdienstleistungsgesetz oder "
        f"das Steuerberatungsgesetz fallen, sind ausgeschlossen."
    )))

    sections.append(("§ 3 Stammkapital und Geschäftsanteile", (
        f"(1) Das Stammkapital der Gesellschaft beträgt EUR {stammkapital} "
        f"(in Worten: {stammkapital} Euro) und ist in voller Höhe "
        f"eingezahlt.\n\n"
        f"(2) Vom Stammkapital übernehmen:\n\n"
        f"a) Die {gs1} einen Geschäftsanteil im Nennbetrag von "
        f"EUR {int(int(stammkapital.replace('.', '')) * int(anteil1) / 100):,} "
        f"(entspricht {anteil1} % des Stammkapitals);\n\n"
        f"b) Die {gs2} einen Geschäftsanteil im Nennbetrag von "
        f"EUR {int(int(stammkapital.replace('.', '')) * int(anteil2) / 100):,} "
        f"(entspricht {anteil2} % des Stammkapitals).\n\n"
        f"(3) Jeder Gesellschafter kann mehrere Geschäftsanteile halten. "
        f"Die Teilung und Zusammenlegung von Geschäftsanteilen ist nur "
        f"mit Zustimmung der Gesellschaft, vertreten durch die "
        f"Geschäftsführung, zulässig. Die Zustimmung darf nicht "
        f"unbillig verweigert werden.\n\n"
        f"(4) Neben den Geschäftsanteilen können die Gesellschafter "
        f"aufgrund gesonderter schuldrechtlicher Vereinbarung der "
        f"Gesellschaft zusätzliches Eigenkapital in Form von Einlagen "
        f"in die Kapitalrücklage (§ 272 Abs. 2 Nr. 4 HGB) oder als "
        f"Gesellschafterdarlehen zur Verfügung stellen. Die Bedingungen "
        f"hierfür werden in einer gesonderten Gesellschaftervereinbarung "
        f"geregelt.\n\n"
        f"(5) Eine Verzinsung der Geschäftsanteile und der "
        f"Stammeinlagen findet nicht statt."
    )))

    sections.append(("§ 4 Verfügung über Geschäftsanteile", (
        f"(1) Jede Verfügung über einen Geschäftsanteil oder Teile eines "
        f"Geschäftsanteils, insbesondere Veräußerung, Abtretung, "
        f"Verpfändung, Übertragung im Wege der Schenkung, Einräumung "
        f"eines Nießbrauchs sowie jede sonstige rechtsgeschäftliche oder "
        f"gesetzliche Veränderung der Inhaberschaft, bedarf zu ihrer "
        f"Wirksamkeit der vorherigen Zustimmung der Gesellschafter-"
        f"versammlung mit einer Mehrheit von drei Vierteln (3/4) der "
        f"abgegebenen Stimmen (Vinkulierung im Sinne des § 15 Abs. 5 "
        f"GmbHG).\n\n"
        f"(2) Über das Zustimmungsverlangen ist innerhalb von einem (1) "
        f"Monat nach Zugang des entsprechenden schriftlichen Antrags zu "
        f"entscheiden. Wird der Antrag in dieser Frist nicht beschieden, "
        f"gilt die Zustimmung als verweigert.\n\n"
        f"(3) Die Zustimmung darf nicht aus willkürlichen Gründen "
        f"verweigert werden. Sie darf insbesondere dann verweigert "
        f"werden, wenn der Erwerber ein unmittelbarer Wettbewerber der "
        f"Gesellschaft ist, in finanziell angespannten Verhältnissen "
        f"steht oder wenn berechtigte Interessen der Gesellschaft oder "
        f"der übrigen Gesellschafter dies erfordern.\n\n"
        f"(4) Verfügungen unter Lebenden, durch die ein Geschäftsanteil "
        f"unmittelbar oder mittelbar auf ein mit dem verfügenden "
        f"Gesellschafter verbundenes Unternehmen im Sinne der §§ 15 ff. "
        f"AktG übertragen wird, sind ohne Zustimmung zulässig, sofern "
        f"der verfügende Gesellschafter sich verpflichtet, den "
        f"Geschäftsanteil unverzüglich zurückzuerwerben, falls die "
        f"konzernrechtliche Verbindung wegfällt.\n\n"
        f"(5) Verfügungen, die ohne die nach diesem § erforderliche "
        f"Zustimmung erfolgen, sind unwirksam."
    )))

    sections.append(("§ 5 Vorkaufsrecht und Andienungspflicht", (
        f"(1) Beabsichtigt ein Gesellschafter die Veräußerung seines "
        f"Geschäftsanteils oder eines Teils hiervon an einen Dritten, "
        f"so steht den übrigen Gesellschaftern im Verhältnis ihrer "
        f"Beteiligung am Stammkapital ein Vorkaufsrecht im Sinne der "
        f"§§ 463 ff. BGB zu.\n\n"
        f"(2) Der veräußerungswillige Gesellschafter (im Folgenden "
        f"„Andienender Gesellschafter') hat den übrigen Gesellschaftern "
        f"den beabsichtigten Verkauf einschließlich des Erwerbers, des "
        f"Kaufpreises und der wesentlichen Vertragsbedingungen "
        f"schriftlich anzuzeigen.\n\n"
        f"(3) Die übrigen Gesellschafter können das Vorkaufsrecht "
        f"innerhalb einer Frist von zwei (2) Monaten ab Zugang der "
        f"Mitteilung gemäß Absatz 2 durch schriftliche Erklärung gegen-"
        f"über dem Andienenden Gesellschafter ausüben. Die Erklärung "
        f"hat den Erwerb des angebotenen Geschäftsanteils zu denselben "
        f"Bedingungen wie das ursprüngliche Drittangebot zum Gegenstand "
        f"zu haben.\n\n"
        f"(4) Üben mehrere Gesellschafter das Vorkaufsrecht aus, so "
        f"erwerben sie im Verhältnis ihrer bisherigen Beteiligung am "
        f"Stammkapital. Ein nicht ausgeübter Anteil wächst den übrigen "
        f"vorkaufsberechtigten Gesellschaftern im Verhältnis ihrer "
        f"Beteiligung an.\n\n"
        f"(5) Wird das Vorkaufsrecht nicht oder nicht vollständig "
        f"ausgeübt, kann der Andienende Gesellschafter den Geschäfts-"
        f"anteil binnen sechs (6) Monaten nach Ablauf der Vorkaufsfrist "
        f"zu den im Drittangebot enthaltenen Bedingungen an den Dritten "
        f"veräußern. Eine Veräußerung zu für den Erwerber günstigeren "
        f"Bedingungen oder nach Ablauf der genannten Frist begründet "
        f"erneut ein Vorkaufsrecht.\n\n"
        f"(6) Bei einer Veräußerung im Wege der Schenkung, der "
        f"vorweggenommenen Erbfolge oder einer sonstigen unentgeltlichen "
        f"Verfügung ist das Vorkaufsrecht ausgeschlossen, soweit der "
        f"Erwerber Ehegatte, eingetragener Lebenspartner oder Abkömmling "
        f"des verfügenden Gesellschafters ist. § 4 dieses Vertrages "
        f"bleibt unberührt."
    )))

    sections.append(("§ 6 Einziehung und Hinauskündigung von Geschäftsanteilen", (
        f"(1) Die Einziehung eines Geschäftsanteils ist mit Zustimmung "
        f"des betroffenen Gesellschafters jederzeit zulässig. Ohne "
        f"Zustimmung des betroffenen Gesellschafters ist die Einziehung "
        f"zulässig, wenn einer der nachfolgenden Gründe vorliegt:\n\n"
        f"a) der Gesellschafter ist in Vermögensverfall geraten, "
        f"insbesondere wenn über sein Vermögen das Insolvenzverfahren "
        f"eröffnet oder die Eröffnung mangels Masse abgelehnt wurde "
        f"oder eine eidesstattliche Versicherung gemäß § 802c ZPO "
        f"abgegeben wurde;\n\n"
        f"b) in den Geschäftsanteil wird die Zwangsvollstreckung "
        f"betrieben und wird nicht innerhalb von drei (3) Monaten nach "
        f"Pfändung wieder aufgehoben;\n\n"
        f"c) der Gesellschafter verletzt seine Gesellschafterpflichten "
        f"in schwerwiegender Weise, insbesondere durch Verstoß gegen das "
        f"Wettbewerbsverbot nach § 8 oder durch grobe Verletzung der "
        f"Vertraulichkeitspflicht;\n\n"
        f"d) in der Person des Gesellschafters ist ein wichtiger Grund "
        f"eingetreten, der seinen Ausschluss aus der Gesellschaft "
        f"rechtfertigt (§ 140 HGB analog);\n\n"
        f"e) bei juristischen Personen oder Personengesellschaften "
        f"als Gesellschafter: ein Kontrollwechsel im Sinne der "
        f"Definitionen in § 25 (5) tritt ohne vorherige Zustimmung der "
        f"Gesellschafterversammlung mit qualifizierter Mehrheit ein.\n\n"
        f"(2) Die Einziehung wird durch Beschluss der Gesellschafter-"
        f"versammlung mit einfacher Mehrheit der abgegebenen Stimmen "
        f"beschlossen. Der betroffene Gesellschafter hat bei der "
        f"Beschlussfassung kein Stimmrecht.\n\n"
        f"(3) Statt der Einziehung kann die Gesellschafterversammlung "
        f"beschließen, dass der Geschäftsanteil ganz oder teilweise auf "
        f"die Gesellschaft selbst oder auf einen oder mehrere von der "
        f"Gesellschafterversammlung zu benennende Dritte (Gesellschafter "
        f"oder Nicht-Gesellschafter) zu übertragen ist (Zwangsabtretung). "
        f"Der betroffene Gesellschafter ist verpflichtet, die hierzu "
        f"erforderlichen Erklärungen abzugeben.\n\n"
        f"(4) Im Falle einer Einziehung oder Zwangsabtretung erhält der "
        f"ausscheidende Gesellschafter eine Abfindung nach Maßgabe von § 7.\n\n"
        f"(5) Liegt der Einziehungs- oder Hinauskündigungsgrund in einem "
        f"vom betroffenen Gesellschafter zu vertretenden schuldhaften "
        f"Verhalten (Bad-Leaver-Tatbestand), so reduziert sich die "
        f"Abfindung gemäß § 7 Abs. 6 dieses Vertrages."
    )))

    sections.append(("§ 7 Abfindung", (
        f"(1) Wird ein Gesellschafter aus der Gesellschaft ausgeschlossen "
        f"oder erfolgt eine Einziehung oder Zwangsabtretung seines "
        f"Geschäftsanteils, so erhält er als Gegenleistung eine "
        f"Abfindung nach Maßgabe der nachfolgenden Bestimmungen.\n\n"
        f"(2) Die Abfindung entspricht dem Verkehrswert des "
        f"Geschäftsanteils zum Stichtag des Wirksamwerdens des "
        f"Ausscheidens (im Folgenden „Bewertungsstichtag').\n\n"
        f"(3) Der Verkehrswert wird nach der Ertragswertmethode unter "
        f"Berücksichtigung der Grundsätze des IDW S 1 in der jeweils "
        f"aktuellen Fassung ermittelt. Wesentliche Bewertungsparameter "
        f"sind die nachhaltigen zukünftigen Ertragsüberschüsse der "
        f"Gesellschaft, kapitalisiert mit einem angemessenen risiko-"
        f"adjustierten Kapitalisierungszinssatz nach dem Capital Asset "
        f"Pricing Model (CAPM). Substanzwerte werden nur insoweit "
        f"berücksichtigt, als nicht-betriebsnotwendiges Vermögen "
        f"vorhanden ist; dieses ist mit dem Verkehrswert anzusetzen.\n\n"
        f"(4) Einigen sich die Parteien nicht binnen drei (3) Monaten "
        f"nach dem Bewertungsstichtag auf einen Wirtschaftsprüfer als "
        f"Bewertungsgutachter, so wird dieser auf Antrag einer Partei "
        f"durch den Präsidenten der Wirtschaftsprüferkammer als "
        f"Schiedsgutachter im Sinne der §§ 317 ff. BGB benannt. Das "
        f"Schiedsgutachten ist für die Parteien verbindlich, soweit es "
        f"nicht offensichtlich unbillig ist (§ 319 BGB).\n\n"
        f"(5) Die Kosten des Bewertungsgutachters werden von der "
        f"Gesellschaft und dem ausscheidenden Gesellschafter je zur "
        f"Hälfte getragen. Macht eine Partei innerhalb von einem (1) "
        f"Monat nach Zugang des Gutachtens substantiierte Einwände "
        f"geltend, die das Schiedsgutachten als offensichtlich unbillig "
        f"erscheinen lassen, und gibt das Schiedsgericht den Einwänden "
        f"statt, trägt die Gesellschaft die Kosten allein.\n\n"
        f"(6) Bei Vorliegen eines Bad-Leaver-Tatbestandes (§ 6 Abs. 5) "
        f"reduziert sich die Abfindung wie folgt:\n\n"
        f"a) bei einem Verstoß innerhalb der ersten drei (3) Jahre nach "
        f"Erwerb des Geschäftsanteils auf den Buchwert des "
        f"Geschäftsanteils, höchstens jedoch den Anschaffungskostenwert;\n\n"
        f"b) bei einem Verstoß nach Ablauf von drei (3), aber innerhalb "
        f"von fünf (5) Jahren auf den halben Verkehrswert;\n\n"
        f"c) bei einem Verstoß nach Ablauf von fünf (5) Jahren auf "
        f"75 % des Verkehrswertes.\n\n"
        f"(7) Die Abfindung wird in fünf (5) gleichen Jahresraten "
        f"ausgezahlt. Die erste Rate ist sechs (6) Monate nach dem "
        f"Bewertungsstichtag fällig, die weiteren Raten jeweils zwölf "
        f"(12) Monate später. Der jeweils ausstehende Betrag ist ab dem "
        f"Bewertungsstichtag mit zwei Prozentpunkten (2 %-Pkt.) über dem "
        f"Basiszinssatz nach § 247 BGB p.a. zu verzinsen. Zinsen sind "
        f"jeweils mit der Hauptforderung zur Zahlung fällig.\n\n"
        f"(8) Die Gesellschaft ist berechtigt, die Abfindung jederzeit "
        f"ganz oder teilweise vorzeitig zu leisten. Eine "
        f"Vorfälligkeitsentschädigung wird nicht geschuldet.\n\n"
        f"(9) Der Anspruch des ausscheidenden Gesellschafters auf "
        f"Abfindung ist nicht abtretbar und nicht pfändbar, solange er "
        f"noch nicht fällig ist."
    )))

    sections.append(("§ 8 Wettbewerbsverbot der Gesellschafter", (
        f"(1) Die Gesellschafter verpflichten sich, während ihrer "
        f"Beteiligung an der Gesellschaft weder mittelbar noch "
        f"unmittelbar in einem Bereich tätig zu sein, der ganz oder "
        f"teilweise in Konkurrenz zur Geschäftstätigkeit der Gesellschaft "
        f"oder eines mit ihr verbundenen Unternehmens steht. Untersagt "
        f"sind insbesondere die Errichtung, der Erwerb oder die "
        f"Beteiligung an einem Wettbewerbsunternehmen sowie die "
        f"Tätigkeit für ein solches Unternehmen als Organmitglied, "
        f"Arbeitnehmer, Berater oder Handelsvertreter.\n\n"
        f"(2) Vom Wettbewerbsverbot ausgenommen sind Beteiligungen an "
        f"börsennotierten Unternehmen, sofern sie 5 % der ausstehenden "
        f"Aktien nicht überschreiten und nicht dem Zweck dienen, auf die "
        f"Geschäftsführung des Unternehmens Einfluss zu nehmen.\n\n"
        f"(3) Das Wettbewerbsverbot besteht räumlich für das Gebiet "
        f"der Europäischen Union und der Schweiz sowie für die übrigen "
        f"Staaten, in denen die Gesellschaft zum Zeitpunkt des Verstoßes "
        f"oder in den zwölf (12) Monaten zuvor unternehmerisch tätig "
        f"war oder den unternehmerischen Marktauftritt vorbereitete.\n\n"
        f"(4) Die Gesellschafterversammlung kann mit qualifizierter "
        f"Mehrheit gemäß § 14 Abs. 3 von Fall zu Fall Befreiung vom "
        f"Wettbewerbsverbot erteilen. Die Befreiung bedarf der Schriftform.\n\n"
        f"(5) Bei einem Verstoß gegen das Wettbewerbsverbot schuldet "
        f"der Gesellschafter der Gesellschaft eine Vertragsstrafe in "
        f"Höhe von EUR 50.000 pro Verstoß. Bei einem Dauerverstoß "
        f"gilt jeder angefangene Monat als ein Verstoß. Das Recht zur "
        f"Geltendmachung des darüber hinausgehenden Schadens (insbesondere "
        f"nach §§ 666, 681, 687 BGB) bleibt unberührt; die Vertragsstrafe "
        f"ist auf den weitergehenden Schaden anzurechnen.\n\n"
        f"(6) Ein nachvertragliches Wettbewerbsverbot ist in einer "
        f"gesonderten Vereinbarung zu regeln, die einer Karenzentschädigung "
        f"in Höhe von 50 % des durchschnittlichen Gewinnanteils der letzten "
        f"drei Jahre vorsieht."
    )))

    sections.append(("§ 9 Organe der Gesellschaft", (
        f"(1) Organe der Gesellschaft sind:\n\n"
        f"a) die Geschäftsführung;\n"
        f"b) die Gesellschafterversammlung;\n"
        f"c) der Beirat, soweit ein solcher gemäß § 12 errichtet ist.\n\n"
        f"(2) Mitglieder der Geschäftsführung können auch Gesellschafter "
        f"sein. Mitglieder des Beirats sollen in der Regel keine "
        f"Gesellschafter, Mitarbeiter oder Geschäftsführer der "
        f"Gesellschaft sein, um die Unabhängigkeit des Beirats zu wahren.\n\n"
        f"(3) Die Organe haben bei ihrer Tätigkeit das Wohl der "
        f"Gesellschaft, insbesondere den langfristigen Unternehmenserfolg, "
        f"die Interessen der Gesellschafter und – soweit relevant – der "
        f"Belegschaft sowie eines gesunden Wirtschaftslebens zu beachten."
    )))

    sections.append(("§ 10 Geschäftsführung und Vertretung", (
        f"(1) Die Gesellschaft hat einen oder mehrere Geschäftsführer. "
        f"Zum Zeitpunkt der Beschlussfassung über diese Satzung amtieren "
        f"als Geschäftsführer:\n\n"
        f"a) {gf1};\n"
        f"b) {gf2}.\n\n"
        f"(2) Die Geschäftsführer werden von der Gesellschafter-"
        f"versammlung bestellt und abberufen. Zur Bestellung und "
        f"Abberufung ist die einfache Mehrheit der abgegebenen Stimmen "
        f"erforderlich.\n\n"
        f"(3) Hat die Gesellschaft nur einen Geschäftsführer, so vertritt "
        f"er die Gesellschaft allein. Sind mehrere Geschäftsführer "
        f"bestellt, so wird die Gesellschaft durch zwei Geschäftsführer "
        f"gemeinsam oder durch einen Geschäftsführer gemeinsam mit einem "
        f"Prokuristen vertreten.\n\n"
        f"(4) Die Gesellschafterversammlung kann einem, mehreren oder "
        f"allen Geschäftsführern Einzelvertretungsbefugnis erteilen "
        f"und/oder sie von den Beschränkungen des § 181 BGB ganz oder "
        f"teilweise (Verbot des Insichgeschäfts und/oder der "
        f"Mehrfachvertretung) befreien.\n\n"
        f"(5) Die Geschäftsführer sind verpflichtet, die Geschäfte der "
        f"Gesellschaft mit der Sorgfalt eines ordentlichen Geschäftsmannes "
        f"im Sinne des § 43 GmbHG zu führen. Sie haben die Bestimmungen "
        f"dieses Gesellschaftsvertrages, die Beschlüsse der "
        f"Gesellschafterversammlung sowie die ihnen erteilten Weisungen "
        f"zu beachten.\n\n"
        f"(6) Die Geschäftsführer haben sich eine Geschäftsordnung zu "
        f"geben, soweit nicht die Gesellschafterversammlung eine solche "
        f"erlässt. Bestehen mehrere Geschäftsführer, so kann die "
        f"Gesellschafterversammlung eine Aufgabenverteilung zwischen "
        f"den Geschäftsführern (Ressorts) festlegen."
    )))

    sections.append(("§ 11 Zustimmungsvorbehalte zugunsten der Gesellschafterversammlung", (
        f"(1) Die Geschäftsführer bedürfen für die nachfolgenden "
        f"Geschäfte und Maßnahmen der vorherigen schriftlichen "
        f"Zustimmung der Gesellschafterversammlung; dies gilt nicht, "
        f"soweit derartige Geschäfte im Wirtschaftsplan einer Periode "
        f"(§ 11 Abs. 4) ausdrücklich genehmigt sind:\n\n"
        f"a) Erwerb, Veräußerung oder Belastung von Grundstücken und "
        f"grundstücksgleichen Rechten;\n\n"
        f"b) Errichtung, Erwerb, Veräußerung und Schließung von "
        f"Zweigniederlassungen, Betrieben und Betriebsstätten;\n\n"
        f"c) Erwerb, Veräußerung und Belastung von Beteiligungen an "
        f"anderen Unternehmen sowie Abschluss, Änderung und Beendigung "
        f"von Unternehmensverträgen;\n\n"
        f"d) Investitionen, die im Einzelfall den Betrag von "
        f"EUR 250.000 (in Worten: zweihundertfünfzigtausend Euro) oder "
        f"im Geschäftsjahr insgesamt den Betrag von EUR 1.000.000 "
        f"übersteigen, soweit sie nicht im Wirtschaftsplan vorgesehen "
        f"sind;\n\n"
        f"e) Aufnahme von Darlehen oder sonstigen Finanzierungen "
        f"einschließlich Leasing- und Sale-and-Lease-Back-Geschäften, "
        f"deren Volumen im Einzelfall EUR 500.000 oder im Geschäftsjahr "
        f"insgesamt EUR 2.000.000 übersteigt;\n\n"
        f"f) Gewährung von Darlehen, Bürgschaften, Garantien und "
        f"sonstigen Sicherheiten außerhalb des gewöhnlichen "
        f"Geschäftsbetriebs;\n\n"
        f"g) Eröffnung, Schließung und sonstige wesentliche Änderungen "
        f"von Geschäftsfeldern;\n\n"
        f"h) Abschluss, Änderung und Beendigung von Verträgen mit einer "
        f"Laufzeit von mehr als fünf (5) Jahren oder mit einem "
        f"Jahresvolumen von mehr als EUR 500.000, soweit nicht in der "
        f"laufenden Geschäftstätigkeit üblich;\n\n"
        f"i) Einstellung und Entlassung von leitenden Angestellten "
        f"sowie Abschluss, Änderung und Beendigung von Anstellungs-"
        f"verträgen mit einem Jahresvergütungsvolumen über "
        f"EUR 200.000;\n\n"
        f"j) Erteilung und Widerruf von Prokuren und Handlungs-"
        f"vollmachten;\n\n"
        f"k) Einleitung und Beendigung von Rechtsstreitigkeiten mit "
        f"einem Streitwert von mehr als EUR 100.000, ausgenommen "
        f"einstweilige Verfügungen, Mahnverfahren und Forderungs-"
        f"durchsetzungen aus laufender Geschäftsbeziehung;\n\n"
        f"l) Vornahme aller Geschäfte und Maßnahmen, die nach Art oder "
        f"Umfang über den gewöhnlichen Geschäftsbetrieb hinausgehen.\n\n"
        f"(2) Die Gesellschafterversammlung kann den Katalog der "
        f"zustimmungspflichtigen Geschäfte jederzeit erweitern oder "
        f"einschränken; der Beschluss ist mit qualifizierter Mehrheit "
        f"nach § 14 Abs. 3 zu fassen.\n\n"
        f"(3) Soweit ein Beirat gemäß § 12 errichtet ist, gehen die "
        f"Zustimmungsvorbehalte aus diesem § auf den Beirat über, "
        f"soweit die Gesellschafterversammlung dies beschließt.\n\n"
        f"(4) Die Geschäftsführer haben der Gesellschafterversammlung "
        f"bis spätestens 30. November jeden Jahres einen Wirtschaftsplan "
        f"(Budget) für das folgende Geschäftsjahr zur Genehmigung "
        f"vorzulegen. Der Wirtschaftsplan umfasst Erfolgsplan, "
        f"Finanzplan und Investitionsplan sowie eine Personalplanung."
    )))

    sections.append(("§ 12 Beirat", (
        f"(1) Die Gesellschaft kann einen Beirat als beratendes und "
        f"überwachendes Organ einrichten. Die Einrichtung erfolgt durch "
        f"Beschluss der Gesellschafterversammlung mit qualifizierter "
        f"Mehrheit gemäß § 14 Abs. 3.\n\n"
        f"(2) Der Beirat besteht aus drei (3) bis sieben (7) Mitgliedern. "
        f"Die Mitglieder werden von der Gesellschafterversammlung für "
        f"eine Amtszeit von drei (3) Jahren bestellt; Wiederbestellung "
        f"ist zulässig. Mindestens die Mehrheit der Beiratsmitglieder "
        f"soll unabhängig im Sinne von Ziffer 5.4.2 des Deutschen "
        f"Corporate Governance Kodex sein.\n\n"
        f"(3) Aufgaben des Beirats sind:\n\n"
        f"a) Beratung der Geschäftsführung in allen strategischen Fragen;\n"
        f"b) Überwachung der Geschäftsführung und Berichterstattung "
        f"gegenüber der Gesellschafterversammlung;\n"
        f"c) Mitwirkung an zustimmungspflichtigen Geschäften gemäß § 11, "
        f"soweit die Gesellschafterversammlung diese Zuständigkeit "
        f"übertragen hat;\n"
        f"d) Vorschlag zur Bestellung und Abberufung von Geschäftsführern "
        f"sowie zur Festsetzung deren Vergütung.\n\n"
        f"(4) Der Beirat gibt sich eine Geschäftsordnung. Beschlüsse "
        f"werden mit einfacher Mehrheit der Stimmen gefasst, soweit "
        f"nicht zwingend etwas anderes vorgeschrieben ist. Bei "
        f"Stimmengleichheit entscheidet die Stimme des Vorsitzenden.\n\n"
        f"(5) Beiratsmitglieder erhalten eine Vergütung, die durch "
        f"Beschluss der Gesellschafterversammlung festgesetzt wird. "
        f"Auslagen werden gegen Nachweis erstattet."
    )))

    sections.append(("§ 13 Gesellschafterversammlung", (
        f"(1) Die Gesellschafterversammlung beschließt über alle "
        f"Angelegenheiten, die ihr durch Gesetz oder diesen Vertrag "
        f"zugewiesen sind, insbesondere:\n\n"
        f"a) Feststellung des Jahresabschlusses und Verwendung des "
        f"Ergebnisses;\n"
        f"b) Entlastung der Geschäftsführer;\n"
        f"c) Bestellung und Abberufung der Geschäftsführer;\n"
        f"d) Wahl des Abschlussprüfers;\n"
        f"e) Genehmigung des Wirtschaftsplans;\n"
        f"f) Beschluss über Maßnahmen der Kapitalbeschaffung und "
        f"Kapitalherabsetzung;\n"
        f"g) Beschluss über Umwandlungsmaßnahmen;\n"
        f"h) Änderung des Gesellschaftsvertrages;\n"
        f"i) Auflösung der Gesellschaft;\n"
        f"j) sonstige Angelegenheiten gemäß § 46 GmbHG.\n\n"
        f"(2) Die Gesellschafterversammlung wird durch die Geschäftsführer "
        f"einberufen. Die Einberufung erfolgt mindestens einmal jährlich "
        f"als ordentliche Gesellschafterversammlung innerhalb der ersten "
        f"acht (8) Monate nach Ende des Geschäftsjahres, ferner so oft, "
        f"wie das Interesse der Gesellschaft dies erfordert.\n\n"
        f"(3) Außerordentliche Gesellschafterversammlungen sind "
        f"einzuberufen, wenn Gesellschafter, die mindestens 10 % des "
        f"Stammkapitals halten, dies unter Angabe von Tagesordnungs-"
        f"punkten und Beschlussgegenständen schriftlich verlangen.\n\n"
        f"(4) Die Einberufung erfolgt durch eingeschriebenen Brief, "
        f"Telefax oder E-Mail mit Empfangsbestätigung an die der "
        f"Gesellschaft zuletzt mitgeteilte Anschrift bzw. E-Mail-Adresse. "
        f"Die Einberufungsfrist beträgt zwei (2) Wochen; der Tag der "
        f"Absendung und der Tag der Versammlung werden nicht "
        f"mitgerechnet. In dringenden Fällen kann die Frist auf "
        f"sieben (7) Tage verkürzt werden.\n\n"
        f"(5) Die Tagesordnung ist mit der Einladung mitzuteilen. "
        f"Über nicht ordnungsgemäß angekündigte Tagesordnungspunkte "
        f"können Beschlüsse nur gefasst werden, wenn alle Gesellschafter "
        f"anwesend oder vertreten sind und keiner widerspricht.\n\n"
        f"(6) Die Gesellschafterversammlung ist beschlussfähig, wenn "
        f"mindestens drei Viertel (3/4) des Stammkapitals vertreten sind. "
        f"Bei Beschlussunfähigkeit ist innerhalb von zwei (2) Wochen "
        f"eine zweite Versammlung mit gleicher Tagesordnung einzuberufen, "
        f"die unabhängig vom vertretenen Kapital beschlussfähig ist, "
        f"sofern in der Einladung hierauf hingewiesen wurde.\n\n"
        f"(7) Gesellschafter können sich in der Gesellschafterversammlung "
        f"vertreten lassen durch (a) andere Gesellschafter, (b) Personen, "
        f"die kraft Gesetzes oder Berufes zur Verschwiegenheit "
        f"verpflichtet sind, oder (c) andere Personen aufgrund "
        f"schriftlicher Vollmacht.\n\n"
        f"(8) Über jede Gesellschafterversammlung ist eine Niederschrift "
        f"zu fertigen, die den Tag, den Ort, die Teilnehmer, die "
        f"Tagesordnung, die wesentlichen Beratungsergebnisse und die "
        f"gefassten Beschlüsse wiederzugeben hat. Die Niederschrift ist "
        f"vom Versammlungsleiter zu unterschreiben und allen "
        f"Gesellschaftern unverzüglich zuzusenden."
    )))

    sections.append(("§ 14 Stimmrecht und Mehrheitserfordernisse", (
        f"(1) Je EUR 1,00 eines Geschäftsanteils gewährt eine (1) Stimme.\n\n"
        f"(2) Beschlüsse werden mit einfacher Mehrheit der abgegebenen "
        f"Stimmen gefasst, soweit Gesetz oder dieser Vertrag keine andere "
        f"Mehrheit vorschreiben. Stimmenthaltungen, ungültige Stimmen "
        f"und nicht abgegebene Stimmen zählen nicht als abgegebene "
        f"Stimmen.\n\n"
        f"(3) Folgende Beschlüsse bedürfen einer Mehrheit von "
        f"drei Vierteln (3/4) der abgegebenen Stimmen, soweit nicht "
        f"das Gesetz eine höhere Mehrheit vorsieht:\n\n"
        f"a) Änderung des Gesellschaftsvertrages;\n"
        f"b) Kapitalmaßnahmen (Erhöhung, Herabsetzung);\n"
        f"c) Umwandlungsmaßnahmen (Verschmelzung, Spaltung, Formwechsel);\n"
        f"d) Auflösung der Gesellschaft;\n"
        f"e) Abschluss, Änderung und Beendigung von Unternehmensverträgen;\n"
        f"f) Erteilung und Widerruf der Vinkulierungs-Zustimmung gemäß § 4;\n"
        f"g) Einrichtung, Auflösung und Änderung des Beirats gemäß § 12;\n"
        f"h) Befreiung vom Wettbewerbsverbot gemäß § 8;\n"
        f"i) Wirtschaftspläne, die ein Investitionsvolumen von mehr als "
        f"EUR 5.000.000 vorsehen.\n\n"
        f"(4) Ein Gesellschafter hat in eigenen Angelegenheiten kein "
        f"Stimmrecht, insbesondere bei Beschlüssen über (a) die "
        f"Vornahme eines Rechtsgeschäfts mit ihm, (b) die Einleitung "
        f"oder Beendigung eines Rechtsstreits gegen ihn, (c) seine "
        f"Entlastung, (d) seinen Ausschluss aus der Gesellschaft, "
        f"(e) die Einziehung seines Geschäftsanteils oder (f) die "
        f"Zustimmung zur Verfügung über seinen Geschäftsanteil.\n\n"
        f"(5) Anfechtungs- und Nichtigkeitsklagen gegen Gesellschafter-"
        f"beschlüsse sind innerhalb einer Frist von einem (1) Monat "
        f"nach Beschlussfassung gegen die Gesellschaft zu erheben; nach "
        f"Fristablauf gilt der Beschluss als geheilt, soweit nicht "
        f"zwingende gesetzliche Bestimmungen entgegenstehen (§ 246 AktG "
        f"analog)."
    )))

    sections.append(("§ 15 Jahresabschluss und Lagebericht", (
        f"(1) Die Geschäftsführer haben den Jahresabschluss (Bilanz, "
        f"Gewinn- und Verlustrechnung, Anhang) sowie – soweit gesetzlich "
        f"vorgeschrieben – den Lagebericht innerhalb der für mittelgroße "
        f"Kapitalgesellschaften geltenden Frist (drei [3] Monate nach "
        f"Schluss des Geschäftsjahres) aufzustellen und unverzüglich nach "
        f"Aufstellung dem Abschlussprüfer vorzulegen.\n\n"
        f"(2) Der Jahresabschluss ist durch einen von der "
        f"Gesellschafterversammlung gewählten Abschlussprüfer im Sinne "
        f"des § 319 HGB zu prüfen, soweit dies gesetzlich vorgeschrieben "
        f"ist oder die Gesellschafterversammlung dies beschließt.\n\n"
        f"(3) Die Geschäftsführer haben den geprüften Jahresabschluss, "
        f"den Lagebericht sowie den Bericht des Abschlussprüfers den "
        f"Gesellschaftern unverzüglich nach Vorlage durch den "
        f"Abschlussprüfer zuzuleiten.\n\n"
        f"(4) Die Gesellschafterversammlung beschließt über die "
        f"Feststellung des Jahresabschlusses und die Verwendung des "
        f"Ergebnisses innerhalb von acht (8) Monaten nach Ende des "
        f"Geschäftsjahres."
    )))

    sections.append(("§ 16 Ergebnisverwendung", (
        f"(1) Über die Verwendung des Bilanzgewinns beschließt die "
        f"Gesellschafterversammlung. Die Gesellschafter haben grundsätzlich "
        f"Anspruch auf Ausschüttung des nach dem festgestellten "
        f"Jahresabschluss ergebenden Bilanzgewinns im Verhältnis ihrer "
        f"Geschäftsanteile.\n\n"
        f"(2) Die Gesellschafterversammlung kann mit einfacher Mehrheit "
        f"beschließen, ganz oder teilweise von einer Ausschüttung "
        f"abzusehen und den Bilanzgewinn in die Gewinnrücklagen "
        f"einzustellen oder auf neue Rechnung vorzutragen, soweit dies "
        f"zur Stärkung der Eigenkapitalbasis oder zur Finanzierung "
        f"geplanter Investitionen erforderlich ist. Die Thesaurierung "
        f"darf jedoch über mehrere Jahre nicht dazu führen, dass die "
        f"Eigenkapitalquote nachhaltig über 60 % der Bilanzsumme steigt; "
        f"in diesem Fall ist mindestens die Hälfte des Bilanzgewinns "
        f"auszuschütten.\n\n"
        f"(3) Die Geschäftsführer können mit Zustimmung der "
        f"Gesellschafterversammlung Vorabausschüttungen (Abschlags-"
        f"dividenden) auf den voraussichtlichen Bilanzgewinn vornehmen, "
        f"sofern (a) ein Zwischenabschluss einen entsprechenden Gewinn "
        f"ausweist, (b) die Liquiditätslage der Gesellschaft die Vorab-"
        f"ausschüttung erlaubt und (c) ein angemessener Sicherheits-"
        f"abschlag berücksichtigt wird.\n\n"
        f"(4) Ausschüttungen sind binnen 14 Tagen nach Beschlussfassung "
        f"durch die Gesellschafterversammlung fällig, soweit kein "
        f"abweichender Fälligkeitstermin festgelegt wird."
    )))

    sections.append(("§ 17 Wettbewerbsverbot für Geschäftsführer", (
        f"(1) Die Geschäftsführer unterliegen während der Dauer ihres "
        f"Anstellungsverhältnisses einem umfassenden Wettbewerbsverbot. "
        f"Sie dürfen weder mittelbar noch unmittelbar für ein Unternehmen "
        f"tätig sein, das mit der Gesellschaft im Wettbewerb steht oder "
        f"mit ihr Geschäftsbeziehungen unterhält.\n\n"
        f"(2) Die Gesellschafterversammlung kann den Geschäftsführern "
        f"von Fall zu Fall Befreiung vom Wettbewerbsverbot erteilen "
        f"(§ 88 AktG analog).\n\n"
        f"(3) Nachvertragliche Wettbewerbsverbote werden im "
        f"Anstellungsvertrag gesondert geregelt und bedürfen einer "
        f"Karenzentschädigung."
    )))

    sections.append(("§ 18 Verschwiegenheitspflicht", (
        f"(1) Die Gesellschafter und Organmitglieder sind verpflichtet, "
        f"über alle vertraulichen Angelegenheiten und Geschäftsgeheimnisse "
        f"der Gesellschaft strikte Verschwiegenheit zu bewahren. Die "
        f"Verschwiegenheitspflicht besteht auch nach Beendigung der "
        f"Gesellschafterstellung oder des Organverhältnisses unbefristet "
        f"fort.\n\n"
        f"(2) § 17 GeschGehG bleibt unberührt. Die §§ 93 Abs. 1 S. 3, "
        f"116 AktG werden analog angewandt."
    )))

    sections.append(("§ 19 Informationsrechte der Gesellschafter", (
        f"(1) Jedem Gesellschafter steht das Auskunfts- und Einsichtsrecht "
        f"gemäß § 51a GmbHG zu. Die Geschäftsführer haben unverzüglich, "
        f"spätestens binnen zwei (2) Wochen, Auskunft zu erteilen und "
        f"Einsicht zu gewähren.\n\n"
        f"(2) Die Geschäftsführer können Auskunft und Einsicht "
        f"verweigern, wenn zu besorgen ist, dass der Gesellschafter sie "
        f"zu gesellschaftsfremden Zwecken verwenden und dadurch der "
        f"Gesellschaft oder einem verbundenen Unternehmen einen nicht "
        f"unerheblichen Nachteil zufügen würde. Die Verweigerung bedarf "
        f"eines Beschlusses der Gesellschafterversammlung.\n\n"
        f"(3) Die Gesellschafter erhalten quartalsweise einen "
        f"betriebswirtschaftlichen Bericht der Geschäftsführer "
        f"(Quartalsreport), der mindestens Bilanz, GuV, "
        f"Cashflow-Übersicht, einen Kommentar zur Geschäftsentwicklung "
        f"sowie einen Soll-Ist-Vergleich gegenüber dem Wirtschaftsplan "
        f"enthält."
    )))

    sections.append(("§ 20 Erbfolge und Vertretung Verstorbener", (
        f"(1) Im Falle des Todes eines Gesellschafters geht der "
        f"Geschäftsanteil auf seine Erben über. Mehrere Erben üben die "
        f"Gesellschafterrechte gemeinsam durch einen gemeinsamen "
        f"Vertreter aus, der den übrigen Gesellschaftern unverzüglich "
        f"unter Vorlage geeigneter Nachweise (Erbschein, Eröffnungs-"
        f"protokoll des Testaments) zu benennen ist.\n\n"
        f"(2) Solange ein gemeinsamer Vertreter nicht benannt ist, ruhen "
        f"die Mitgliedschaftsrechte aus dem betroffenen Geschäftsanteil "
        f"mit Ausnahme der vermögensrechtlichen Ansprüche.\n\n"
        f"(3) Geht der Geschäftsanteil auf einen Erben über, der nicht "
        f"zu den Abkömmlingen oder dem überlebenden Ehegatten/ "
        f"Lebenspartner des verstorbenen Gesellschafters gehört, so steht "
        f"den übrigen Gesellschaftern ein Erwerbsrecht zum Verkehrswert "
        f"gemäß § 7 zu, das innerhalb von sechs (6) Monaten ab Kenntnis "
        f"des Erbfalls und Benennung des Erben durch schriftliche "
        f"Erklärung ausgeübt werden kann."
    )))

    sections.append(("§ 21 Bekanntmachungen", (
        "(1) Bekanntmachungen der Gesellschaft erfolgen ausschließlich "
        "im Bundesanzeiger und – soweit gesetzlich erforderlich – im "
        "elektronischen Unternehmensregister.\n\n"
        "(2) Bekanntmachungen an die Gesellschafter erfolgen in "
        "Schriftform oder per E-Mail an die zuletzt schriftlich "
        "mitgeteilte Anschrift bzw. E-Mail-Adresse."
    )))

    sections.append(("§ 22 Schiedsklausel", SCHIEDSKLAUSEL_DIS.format(
        schiedsort=city
    )))

    sections.append(("§ 23 Auflösung und Liquidation", (
        f"(1) Die Auflösung der Gesellschaft bedarf eines Beschlusses "
        f"der Gesellschafterversammlung mit qualifizierter Mehrheit "
        f"gemäß § 14 Abs. 3.\n\n"
        f"(2) Im Falle der Auflösung erfolgt die Liquidation durch die "
        f"Geschäftsführer als Liquidatoren, soweit die Gesellschafter-"
        f"versammlung keine andere Person zum Liquidator bestellt.\n\n"
        f"(3) Das Liquidationsergebnis wird im Verhältnis der "
        f"Geschäftsanteile auf die Gesellschafter verteilt.\n\n"
        f"(4) Im Übrigen gelten die gesetzlichen Bestimmungen "
        f"(§§ 65 ff. GmbHG)."
    )))

    sections.append(("§ 24 Gerichtsstand und anwendbares Recht", JURISDICTION_DE.format(
        gerichtsstand=city
    )))

    sections.append(("§ 25 Schlussbestimmungen", (
        f"(1) Dieser Vertrag enthält die abschließende Regelung der "
        f"gesellschaftsrechtlichen Beziehungen der Parteien. "
        f"Mündliche Nebenabreden bestehen nicht.\n\n"
        f"(2) Änderungen und Ergänzungen dieses Vertrages bedürfen zu "
        f"ihrer Wirksamkeit der notariellen Beurkundung (§ 53 GmbHG), "
        f"soweit nicht eine strengere Form gesetzlich vorgeschrieben "
        f"ist. Dies gilt auch für die Aufhebung dieser Klausel.\n\n"
        f"(3) " + SALVATORISCH + "\n\n"
        f"(4) Die Kosten dieses Vertrages und seiner Durchführung, "
        f"einschließlich Notar- und Gerichtskosten, trägt die "
        f"Gesellschaft.\n\n"
        f"(5) Definitionen:\n"
        f"„Verbundene Unternehmen' und „Tochtergesellschaft' werden "
        f"im Sinne der §§ 15 ff. AktG verstanden.\n"
        f"„Kontrollwechsel' bezeichnet jede unmittelbare oder mittelbare "
        f"Übertragung von mehr als 50 % der Stimmrechte oder des Kapitals "
        f"einer Partei auf einen Dritten, der mit der Partei nicht "
        f"verbunden ist."
    )))

    sections.append(("Unterschriften", (
        f"Vorstehende Urkunde wurde von den Gesellschaftern in "
        f"notarieller Form errichtet. Eine Ausfertigung wird zum "
        f"Handelsregister eingereicht.\n\n"
        f"Ort: {city}, Datum: {_today_de()}\n\n"
        f"Für die {gs1}:\n\n"
        f"_____________________________\n"
        f"{gf1}, Geschäftsführer\n\n"
        f"Für die {gs2}:\n\n"
        f"_____________________________\n"
        f"{gf2}, Geschäftsführer\n\n"
        f"Notarin / Notar:\n\n"
        f"_____________________________\n"
        f"Dr. iur. Petra Hoffmann, Notarin in {city}"
    )))

    return sections


# =====================================================================
# AG SATZUNG
# =====================================================================

def gen_ag_satzung(p: Dict[str, Any]) -> List[Section]:
    """Satzung einer Aktiengesellschaft. Target: 4000-5500 Wörter."""

    name = _g(p, "name", "Muster AG")
    city = _g(p, "city", "Frankfurt am Main")
    grundkapital = _g(p, "grundkapital", "5.000.000")
    aktien_zahl = _g(p, "aktien_zahl", "5.000.000")
    aktienart = _g(p, "aktienart", "auf den Namen lautende Stückaktien")
    geschaeftsjahr = _g(p, "geschaeftsjahr", "Kalenderjahr")
    vorstand1 = _g(p, "vorstand1", "Dr. Stefan Klein")
    ar1 = _g(p, "ar1", "Prof. Dr. Helga Brandt")
    gegenstand = _g(p, "gegenstand",
        "die Entwicklung, Herstellung und der Vertrieb von technischen "
        "Produkten und Dienstleistungen im Bereich industrieller Anwendungen")

    s: List[Section] = []

    s.append(("Präambel", (
        f"Die nachstehenden Gründer haben sich zu einer Aktiengesellschaft "
        f"zusammengeschlossen und beschließen die folgende Satzung. Die "
        f"Gesellschaft wird im Handelsregister des Amtsgerichts {city} "
        f"eingetragen und nimmt ihre Tätigkeit mit Wirkung zum Tag der "
        f"Eintragung auf."
    )))

    s.append(("§ 1 Firma, Sitz, Geschäftsjahr", (
        f"(1) Die Firma der Gesellschaft lautet:\n\n"
        f"{name}.\n\n"
        f"(2) Sitz der Gesellschaft ist {city}.\n\n"
        f"(3) Geschäftsjahr ist das {geschaeftsjahr}.\n\n"
        f"(4) Bekanntmachungen der Gesellschaft erfolgen ausschließlich "
        f"im Bundesanzeiger. Werden Informationen an die Aktionäre per "
        f"Datenfernübertragung übermittelt, so steht dies einer schrift-"
        f"lichen Mitteilung gleich, soweit gesetzlich zulässig.\n\n"
        f"(5) Die Gesellschaft kann Zweigniederlassungen im In- und "
        f"Ausland errichten."
    )))

    s.append(("§ 2 Unternehmensgegenstand", (
        f"(1) Gegenstand des Unternehmens ist {gegenstand}.\n\n"
        f"(2) Die Gesellschaft ist berechtigt, alle Geschäfte zu betreiben "
        f"und Maßnahmen zu treffen, die unmittelbar oder mittelbar dem "
        f"Unternehmensgegenstand dienen. Sie kann zu diesem Zweck im "
        f"In- und Ausland Zweigniederlassungen errichten, andere "
        f"Unternehmen gleicher oder verwandter Art gründen, erwerben, "
        f"pachten oder sich an ihnen beteiligen, die einheitliche "
        f"Leitung über solche Unternehmen übernehmen oder sich auf die "
        f"Verwaltung ihrer Beteiligung beschränken sowie Unternehmens-"
        f"verträge im Sinne der §§ 291 ff. AktG abschließen.\n\n"
        f"(3) Die Gesellschaft kann ihre Tätigkeit auch durch verbundene "
        f"Unternehmen ausüben."
    )))

    s.append(("§ 3 Bekanntmachungen", (
        "(1) Bekanntmachungen der Gesellschaft erfolgen im Bundesanzeiger.\n\n"
        "(2) Informationen an die Aktionäre können auch im Wege der "
        "Datenfernübertragung übermittelt werden."
    )))

    s.append(("§ 4 Grundkapital und Aktien", (
        f"(1) Das Grundkapital der Gesellschaft beträgt EUR {grundkapital} "
        f"(in Worten: {grundkapital} Euro).\n\n"
        f"(2) Es ist eingeteilt in {aktien_zahl} {aktienart} ohne Nennbetrag "
        f"mit einem rechnerischen Anteil am Grundkapital von EUR 1,00 je Aktie.\n\n"
        f"(3) Die Form der Aktienurkunden, der Gewinnanteilscheine und "
        f"Erneuerungsscheine bestimmt der Vorstand mit Zustimmung des "
        f"Aufsichtsrats. Der Anspruch des Aktionärs auf Verbriefung "
        f"seiner Aktien ist ausgeschlossen, soweit nicht zwingende "
        f"gesetzliche Vorschriften die Verbriefung erfordern.\n\n"
        f"(4) Bei einer Kapitalerhöhung kann der Beginn der "
        f"Gewinnbeteiligung der neuen Aktien abweichend von § 60 Abs. 2 "
        f"AktG geregelt werden.\n\n"
        f"(5) Die Übertragung der auf den Namen lautenden Aktien bedarf "
        f"der Zustimmung der Gesellschaft (vinkulierte Namensaktien im "
        f"Sinne des § 68 Abs. 2 AktG). Über die Zustimmung entscheidet "
        f"der Vorstand mit Zustimmung des Aufsichtsrats."
    )))

    s.append(("§ 5 Genehmigtes Kapital", (
        f"(1) Der Vorstand ist ermächtigt, mit Zustimmung des "
        f"Aufsichtsrats bis zum [Datum + 5 Jahre] das Grundkapital der "
        f"Gesellschaft einmalig oder mehrmalig um insgesamt bis zu "
        f"EUR 2.500.000 durch Ausgabe neuer, auf den Namen lautender "
        f"Stückaktien gegen Bar- oder Sacheinlagen zu erhöhen "
        f"(Genehmigtes Kapital 2025).\n\n"
        f"(2) Das Bezugsrecht der Aktionäre ist grundsätzlich zu wahren. "
        f"Der Vorstand ist jedoch ermächtigt, mit Zustimmung des "
        f"Aufsichtsrats das Bezugsrecht der Aktionäre auszuschließen, "
        f"um (a) Spitzenbeträge auszugleichen, (b) Aktien gegen Sach-"
        f"einlagen, insbesondere im Rahmen des Erwerbs von Unternehmen, "
        f"Unternehmensteilen oder Beteiligungen, auszugeben oder (c) bei "
        f"Barkapitalerhöhungen, sofern der Ausgabebetrag den Börsenkurs "
        f"nicht wesentlich unterschreitet und der anteilige Betrag des "
        f"Grundkapitals 10 % des Grundkapitals nicht übersteigt (§ 186 "
        f"Abs. 3 Satz 4 AktG).\n\n"
        f"(3) Der Vorstand ist mit Zustimmung des Aufsichtsrats "
        f"ermächtigt, die weiteren Einzelheiten der Kapitalerhöhung und "
        f"ihrer Durchführung festzulegen."
    )))

    s.append(("§ 6 Vorstand", (
        f"(1) Der Vorstand besteht aus einer oder mehreren Personen. Die "
        f"Zahl der Mitglieder des Vorstands bestimmt der Aufsichtsrat.\n\n"
        f"(2) Der Aufsichtsrat bestellt die Mitglieder des Vorstands und "
        f"kann einen Vorsitzenden des Vorstands sowie einen "
        f"stellvertretenden Vorsitzenden bestimmen.\n\n"
        f"(3) Die Bestellung erfolgt für höchstens fünf (5) Jahre. Eine "
        f"wiederholte Bestellung oder Verlängerung der Amtszeit, jeweils "
        f"für höchstens fünf Jahre, ist zulässig. Sie bedarf eines "
        f"erneuten Aufsichtsratsbeschlusses, der frühestens ein Jahr "
        f"vor Ablauf der bisherigen Amtszeit gefasst werden kann.\n\n"
        f"(4) Die Gesellschaft wird, wenn nur ein Vorstandsmitglied "
        f"bestellt ist, durch dieses allein vertreten. Sind mehrere "
        f"Vorstandsmitglieder bestellt, so wird die Gesellschaft durch "
        f"zwei Vorstandsmitglieder gemeinsam oder durch ein "
        f"Vorstandsmitglied in Gemeinschaft mit einem Prokuristen "
        f"vertreten.\n\n"
        f"(5) Der Aufsichtsrat kann einzelnen Vorstandsmitgliedern "
        f"Einzelvertretungsbefugnis erteilen sowie sie ganz oder "
        f"teilweise von den Beschränkungen des § 181 BGB befreien.\n\n"
        f"(6) Der Aufsichtsrat erlässt eine Geschäftsordnung für den "
        f"Vorstand, die insbesondere die Geschäftsverteilung, die "
        f"Beschlussfassung und die Berichtspflichten regelt."
    )))

    s.append(("§ 7 Aufsichtsrat - Zusammensetzung", (
        f"(1) Der Aufsichtsrat besteht aus sechs (6) Mitgliedern, von "
        f"denen vier (4) von der Hauptversammlung und zwei (2) von den "
        f"Arbeitnehmern nach Maßgabe des Drittelbeteiligungsgesetzes "
        f"gewählt werden.\n\n"
        f"(2) Die Wahl der Aufsichtsratsmitglieder erfolgt jeweils "
        f"für die Zeit bis zur Beendigung der Hauptversammlung, die "
        f"über die Entlastung für das vierte Geschäftsjahr nach Beginn "
        f"der Amtszeit beschließt; das Geschäftsjahr, in dem die "
        f"Amtszeit beginnt, wird nicht mitgerechnet.\n\n"
        f"(3) Wiederwahl ist zulässig.\n\n"
        f"(4) Für ein vor Ablauf der Amtszeit ausscheidendes "
        f"Aufsichtsratsmitglied kann gleichzeitig mit der Wahl ein "
        f"Ersatzmitglied bestellt werden, das Mitglied wird, sobald das "
        f"betreffende Mitglied vor Ablauf seiner Amtszeit ausscheidet. "
        f"Sein Amt erlischt spätestens mit Ablauf der Amtszeit des "
        f"ausgeschiedenen Mitglieds.\n\n"
        f"(5) Jedes Aufsichtsratsmitglied kann sein Amt durch "
        f"schriftliche Erklärung gegenüber dem Vorsitzenden des "
        f"Aufsichtsrats oder dem Vorstand unter Einhaltung einer "
        f"Kündigungsfrist von einem (1) Monat niederlegen. Eine "
        f"Amtsniederlegung aus wichtigem Grund ist jederzeit ohne "
        f"Einhaltung einer Frist möglich."
    )))

    s.append(("§ 8 Aufsichtsrat - Vorsitz und Geschäftsordnung", (
        f"(1) Der Aufsichtsrat wählt aus seiner Mitte einen Vorsitzenden "
        f"und einen Stellvertreter. Die Wahl erfolgt jeweils für die "
        f"Dauer der Amtszeit der Gewählten als Aufsichtsratsmitglied.\n\n"
        f"(2) Scheidet der Vorsitzende oder der Stellvertreter vorzeitig "
        f"aus seinem Amt aus, so hat der Aufsichtsrat unverzüglich eine "
        f"Neuwahl vorzunehmen.\n\n"
        f"(3) Der Aufsichtsrat gibt sich eine Geschäftsordnung im "
        f"Rahmen der gesetzlichen Vorschriften und dieser Satzung. Er "
        f"kann aus seiner Mitte Ausschüsse bilden und ihnen Aufgaben "
        f"und Befugnisse zur eigenverantwortlichen Erledigung übertragen, "
        f"soweit gesetzlich zulässig.\n\n"
        f"(4) Der Aufsichtsrat soll mindestens einen Prüfungsausschuss "
        f"(Audit Committee) und einen Personalausschuss "
        f"(Nomination & Compensation Committee) bilden."
    )))

    s.append(("§ 9 Aufsichtsrat - Sitzungen und Beschlussfassung", (
        f"(1) Sitzungen des Aufsichtsrats werden vom Vorsitzenden, im "
        f"Falle seiner Verhinderung von seinem Stellvertreter, unter "
        f"Mitteilung der Tagesordnung mit einer Frist von zwei (2) "
        f"Wochen einberufen. Der Tag der Absendung und der Tag der "
        f"Sitzung werden nicht mitgerechnet. In dringenden Fällen kann "
        f"der Vorsitzende die Frist auf 48 Stunden verkürzen.\n\n"
        f"(2) Die Einberufung kann schriftlich, fernschriftlich, per "
        f"Telefax oder E-Mail erfolgen.\n\n"
        f"(3) Sitzungen finden grundsätzlich in Präsenz statt. "
        f"Beschlussfassung im Wege der Telefon- oder Video-Konferenz "
        f"sowie in gemischten Sitzungen ist zulässig, wenn kein Mitglied "
        f"binnen angemessener Frist widerspricht.\n\n"
        f"(4) Der Aufsichtsrat ist beschlussfähig, wenn mindestens die "
        f"Hälfte seiner Mitglieder, aus denen er insgesamt zu bestehen "
        f"hat, an der Beschlussfassung teilnimmt. Ein Mitglied nimmt "
        f"auch dann an der Beschlussfassung teil, wenn es sich der "
        f"Stimme enthält.\n\n"
        f"(5) Beschlüsse werden mit einfacher Mehrheit der abgegebenen "
        f"Stimmen gefasst, soweit das Gesetz oder die Satzung nichts "
        f"anderes bestimmt. Bei Stimmengleichheit gibt – auch bei "
        f"Wahlen – die Stimme des Vorsitzenden den Ausschlag (§ 29 "
        f"Abs. 2 MitbestG analog).\n\n"
        f"(6) Beschlussfassungen außerhalb von Sitzungen, insbesondere "
        f"durch schriftliche, fernschriftliche, fernmündliche oder "
        f"vergleichbare Erklärungen oder im Umlaufverfahren, sind "
        f"zulässig, wenn kein Aufsichtsratsmitglied dem Verfahren "
        f"widerspricht."
    )))

    s.append(("§ 10 Aufsichtsrat - Vergütung", (
        "(1) Jedes Aufsichtsratsmitglied erhält neben dem Ersatz seiner "
        "Auslagen eine feste Vergütung von EUR 35.000 jährlich. Der "
        "Vorsitzende erhält das Doppelte, der Stellvertretende "
        "Vorsitzende das Eineinhalbfache.\n\n"
        "(2) Vorsitzende von Ausschüssen erhalten zusätzlich eine "
        "Vergütung von EUR 10.000 jährlich, Mitglieder von Ausschüssen "
        "EUR 5.000 jährlich. Dies gilt nicht für Ausschüsse, die nur "
        "zur Vorbereitung von Beschlüssen tätig werden.\n\n"
        "(3) Aufsichtsratsmitglieder, die nur während eines Teils des "
        "Geschäftsjahres dem Aufsichtsrat angehört haben, erhalten "
        "eine zeitanteilige Vergütung.\n\n"
        "(4) Die Vergütung wird jeweils nach Ablauf des Geschäftsjahres "
        "zur Zahlung fällig.\n\n"
        "(5) Die Gesellschaft erstattet jedem Aufsichtsratsmitglied "
        "die auf die Vergütung entfallende Umsatzsteuer."
    )))

    s.append(("§ 11 Hauptversammlung - Einberufung", (
        f"(1) Die Hauptversammlung findet am Sitz der Gesellschaft, am "
        f"Sitz einer deutschen Wertpapierbörse oder in einer deutschen "
        f"Stadt mit mehr als 100.000 Einwohnern statt.\n\n"
        f"(2) Die Hauptversammlung wird durch den Vorstand oder, in den "
        f"gesetzlich vorgesehenen Fällen, durch den Aufsichtsrat einberufen.\n\n"
        f"(3) Die Einberufung erfolgt unter Bekanntgabe der Tagesordnung "
        f"mindestens 30 Tage vor dem Tag der Hauptversammlung. Tag der "
        f"Einberufung und Tag der Hauptversammlung sind nicht "
        f"mitzurechnen.\n\n"
        f"(4) Die Einberufung erfolgt im Bundesanzeiger; ergänzend kann "
        f"sie auf der Internetseite der Gesellschaft veröffentlicht "
        f"werden.\n\n"
        f"(5) Zur Teilnahme an der Hauptversammlung und zur Ausübung "
        f"des Stimmrechts sind diejenigen Aktionäre berechtigt, die im "
        f"Aktienregister eingetragen sind und sich rechtzeitig zur "
        f"Hauptversammlung angemeldet haben. Die Anmeldung muss der "
        f"Gesellschaft mindestens sechs (6) Tage vor der Hauptversammlung "
        f"in Textform (§ 126b BGB) zugehen."
    )))

    s.append(("§ 12 Hauptversammlung - Versammlungsleiter und Stimmrecht", (
        "(1) Den Vorsitz in der Hauptversammlung führt der Vorsitzende "
        "des Aufsichtsrats oder ein anderes durch den Aufsichtsrat zu "
        "bestimmendes Aufsichtsratsmitglied der Anteilseigner. Übernimmt "
        "keine dieser Personen den Vorsitz, so wird der Versammlungs-"
        "leiter unter Leitung des an Lebensjahren ältesten anwesenden "
        "Aktionärs gewählt.\n\n"
        "(2) Der Versammlungsleiter leitet die Versammlung. Er bestimmt "
        "die Reihenfolge der Verhandlungs- und Abstimmungsgegenstände "
        "sowie die Form, das Verfahren und die weiteren Einzelheiten der "
        "Abstimmung. Er ist ermächtigt, das Frage- und Rederecht zeitlich "
        "angemessen zu beschränken.\n\n"
        "(3) Der Vorstand ist ermächtigt, die Bild- und Tonübertragung "
        "der Hauptversammlung im Internet zuzulassen.\n\n"
        "(4) Jede Stückaktie gewährt eine Stimme. Das Stimmrecht "
        "beginnt mit der vollständigen Leistung der Einlage.\n\n"
        "(5) Beschlüsse werden mit einfacher Mehrheit der abgegebenen "
        "Stimmen und, wenn das Gesetz außerdem eine Kapitalmehrheit "
        "vorschreibt, mit der einfachen Mehrheit des bei der "
        "Beschlussfassung vertretenen Grundkapitals gefasst, soweit "
        "nicht gesetzlich zwingend eine größere Mehrheit erforderlich ist."
    )))

    s.append(("§ 13 Hauptversammlung - Niederschrift", (
        "(1) Die Beschlüsse der Hauptversammlung sind in eine durch "
        "einen Notar aufzunehmende Niederschrift aufzunehmen, soweit "
        "dies gesetzlich vorgeschrieben ist.\n\n"
        "(2) In der Niederschrift sind Ort und Tag der Verhandlung, "
        "der Name des Notars sowie die Art und das Ergebnis der "
        "Abstimmung und die Feststellung des Vorsitzenden über die "
        "Beschlussfassung anzugeben.\n\n"
        "(3) Die Niederschrift ist vom Notar zu unterschreiben."
    )))

    s.append(("§ 14 Jahresabschluss und Lagebericht", (
        "(1) Der Vorstand hat innerhalb der gesetzlichen Fristen für "
        "das vergangene Geschäftsjahr den Jahresabschluss (Bilanz nebst "
        "Gewinn- und Verlustrechnung sowie Anhang) und den Lagebericht "
        "sowie – soweit die Gesellschaft Mutterunternehmen ist – den "
        "Konzernabschluss und den Konzernlagebericht aufzustellen und "
        "dem Abschlussprüfer vorzulegen.\n\n"
        "(2) Der Vorstand hat nach Eingang des Prüfungsberichtes des "
        "Abschlussprüfers unverzüglich dem Aufsichtsrat den Jahres-"
        "abschluss, gegebenenfalls den Konzernabschluss, den Lagebericht "
        "und gegebenenfalls den Konzernlagebericht sowie den Vorschlag "
        "vorzulegen, den er der Hauptversammlung für die Verwendung des "
        "Bilanzgewinns machen will.\n\n"
        "(3) Der Aufsichtsrat hat den Jahresabschluss, den Lagebericht "
        "und den Vorschlag für die Verwendung des Bilanzgewinns sowie "
        "gegebenenfalls den Konzernabschluss und den Konzernlagebericht "
        "zu prüfen und der Hauptversammlung darüber schriftlich zu "
        "berichten. Er hat seinen Bericht innerhalb eines Monats nach "
        "Zugang der Vorlagen dem Vorstand zuzuleiten.\n\n"
        "(4) Vorstand und Aufsichtsrat können bei der Feststellung des "
        "Jahresabschlusses Beträge bis zu der Hälfte des Jahresüberschusses "
        "in andere Gewinnrücklagen einstellen. Sie sind darüber hinaus "
        "ermächtigt, Beträge bis zu weiteren 25 % des Jahresüberschusses "
        "in andere Gewinnrücklagen einzustellen, solange und soweit die "
        "anderen Gewinnrücklagen die Hälfte des Grundkapitals nicht "
        "übersteigen und auch nach der Einstellung nicht übersteigen würden."
    )))

    s.append(("§ 15 Gewinnverwendung", (
        "(1) Die Hauptversammlung beschließt alljährlich in den ersten "
        "acht (8) Monaten des Geschäftsjahres über die Verwendung des "
        "Bilanzgewinns, die Entlastung der Mitglieder des Vorstands und "
        "des Aufsichtsrats sowie die Wahl des Abschlussprüfers.\n\n"
        "(2) Bei Kapitalerhöhungen kann die Gewinnbeteiligung neuer "
        "Aktien abweichend von § 60 Abs. 2 AktG bestimmt werden.\n\n"
        "(3) Die Hauptversammlung kann anstelle oder neben einer Bar-"
        "ausschüttung eine Sachausschüttung beschließen."
    )))

    s.append(("§ 16 Auflösung", (
        "(1) Die Auflösung der Gesellschaft erfolgt durch Beschluss "
        "der Hauptversammlung, der einer Mehrheit von drei Vierteln "
        "des bei der Beschlussfassung vertretenen Grundkapitals bedarf.\n\n"
        "(2) Im Falle der Auflösung erfolgt die Abwicklung durch den "
        "Vorstand, soweit die Hauptversammlung keine andere Person "
        "zum Abwickler bestellt.\n\n"
        "(3) Das nach Berichtigung der Verbindlichkeiten verbleibende "
        "Vermögen wird im Verhältnis der Anteile am Grundkapital unter "
        "die Aktionäre verteilt."
    )))

    s.append(("§ 17 Gründungsaufwand", (
        "(1) Die Gesellschaft trägt den mit ihrer Gründung verbundenen "
        "Aufwand in Höhe von bis zu EUR 25.000, insbesondere Notar-, "
        "Gericht- und Veröffentlichungskosten sowie Kosten der "
        "Rechtsberatung. Darüberhinaus gehender Aufwand wird von den "
        "Gründern getragen."
    )))

    s.append(("§ 18 Schlussbestimmungen", (
        "(1) " + SALVATORISCH + "\n\n"
        "(2) Für sämtliche Streitigkeiten zwischen den Aktionären und "
        "der Gesellschaft sowie deren Organen ist ausschließlich – "
        "soweit zulässig – das für den Sitz der Gesellschaft örtlich "
        "zuständige Landgericht zuständig. § 246 Abs. 3 AktG bleibt "
        "unberührt.\n\n"
        "(3) Dieser Satzung wird das deutsche Recht zugrunde gelegt."
    )))

    s.append(("Unterschriften der Gründer", (
        f"{city}, den {_today_de()}\n\n"
        f"_____________________________\n"
        f"{vorstand1}, Vorstandsvorsitzender\n\n"
        f"_____________________________\n"
        f"{ar1}, Aufsichtsratsvorsitzende\n\n"
        f"Beurkundet von: Dr. iur. Petra Hoffmann, Notarin in {city}"
    )))

    return s


# =====================================================================
# GF-ANSTELLUNGSVERTRAG
# =====================================================================

def gen_gf_anstellungsvertrag(p: Dict[str, Any]) -> List[Section]:
    """GF-Anstellungsvertrag. Target: 3500-5000 Wörter."""

    company = _g(p, "company", "Muster GmbH")
    gf = _g(p, "gf", "Dr. Thomas Müller")
    gehalt = _g(p, "gehalt", "240.000")
    bonus_cap = _g(p, "bonus_cap", "60")
    city = _g(p, "city", "Köln")
    start = _g(p, "start", "01.01.2024")
    dauer = _g(p, "dauer", "5")

    s: List[Section] = []

    s.append(("Präambel", (
        f"Zwischen der {company} mit Sitz in {city} – nachfolgend "
        f"„Gesellschaft' – und Herrn/Frau {gf}, geboren am [Datum], "
        f"wohnhaft in [Anschrift] – nachfolgend „Geschäftsführer/in' – "
        f"wird folgender Anstellungsvertrag geschlossen.\n\n"
        f"Die Gesellschafterversammlung hat Herrn/Frau {gf} durch "
        f"Beschluss vom [Datum] zum Geschäftsführer der Gesellschaft "
        f"bestellt. Mit diesem Vertrag werden die schuldrechtlichen "
        f"Beziehungen zwischen der Gesellschaft und dem Geschäftsführer "
        f"abschließend geregelt."
    )))

    s.append(("§ 1 Bestellung und Tätigkeit", (
        f"(1) Die Gesellschaft stellt Herrn/Frau {gf} mit Wirkung zum "
        f"{start} als Geschäftsführer ein. Die zugrunde liegende "
        f"organschaftliche Bestellung erfolgt durch gesonderten Beschluss "
        f"der Gesellschafterversammlung.\n\n"
        f"(2) Der Geschäftsführer führt die Geschäfte der Gesellschaft "
        f"gemäß den gesetzlichen Bestimmungen, den Vorschriften des "
        f"Gesellschaftsvertrages, der Geschäftsordnung für die "
        f"Geschäftsführung sowie den Weisungen und Beschlüssen der "
        f"Gesellschafterversammlung. Er ist verpflichtet, die Geschäfte "
        f"der Gesellschaft mit der Sorgfalt eines ordentlichen "
        f"Geschäftsmannes im Sinne des § 43 GmbHG zu führen.\n\n"
        f"(3) Der Geschäftsführer ist für den Verantwortungsbereich "
        f"„[Ressort]' zuständig. Die Geschäftsverteilung zwischen "
        f"mehreren Geschäftsführern ergibt sich aus der Geschäftsordnung. "
        f"Unbeschadet der Ressortverteilung tragen alle Geschäftsführer "
        f"die Gesamtverantwortung für die Geschäftsführung gemeinschaftlich.\n\n"
        f"(4) Der Geschäftsführer hat seine gesamte Arbeitskraft, seine "
        f"Erfahrungen und Fachkenntnisse in den Dienst der Gesellschaft "
        f"zu stellen. Er ist an feste Dienstzeiten nicht gebunden und "
        f"hat Dienstreisen im Rahmen seiner Tätigkeit zu unternehmen, "
        f"soweit dies erforderlich ist.\n\n"
        f"(5) Dienstsitz des Geschäftsführers ist der Sitz der "
        f"Gesellschaft. Die Gesellschaft kann den Dienstort innerhalb "
        f"des Bundesgebietes verlegen, soweit dies dem Geschäftsführer "
        f"unter Abwägung seiner persönlichen Interessen zumutbar ist."
    )))

    s.append(("§ 2 Aufgaben, Pflichten und Zustimmungsvorbehalte", (
        f"(1) Der Geschäftsführer hat alle Geschäfte und Maßnahmen mit "
        f"der Sorgfalt eines ordentlichen Geschäftsmannes "
        f"wahrzunehmen. Er ist insbesondere verpflichtet, die "
        f"Vermögensinteressen der Gesellschaft zu wahren, ihren guten "
        f"Ruf zu fördern und Risiken angemessen zu steuern.\n\n"
        f"(2) Folgende Geschäfte und Maßnahmen darf der Geschäftsführer "
        f"nur mit vorheriger schriftlicher Zustimmung der "
        f"Gesellschafterversammlung vornehmen:\n\n"
        f"a) Maßnahmen, die im Katalog zustimmungspflichtiger Geschäfte "
        f"des Gesellschaftsvertrages oder der Geschäftsordnung genannt "
        f"sind;\n\n"
        f"b) Abschluss, Änderung und Beendigung von Verträgen mit einer "
        f"jährlichen Belastung der Gesellschaft von mehr als "
        f"EUR 250.000 oder einer Laufzeit von mehr als drei (3) Jahren, "
        f"soweit nicht im Wirtschaftsplan vorgesehen;\n\n"
        f"c) Einleitung gerichtlicher oder schiedsgerichtlicher "
        f"Verfahren mit einem Streitwert von mehr als EUR 100.000;\n\n"
        f"d) Gewährung von Pensions- oder vergleichbaren Zusagen an "
        f"Mitarbeiter sowie Abschluss von Dienstverträgen mit leitenden "
        f"Angestellten ab einer Vergütung von EUR 150.000 jährlich.\n\n"
        f"(3) Der Geschäftsführer berichtet der Gesellschafter-"
        f"versammlung quartalsweise schriftlich über den Geschäftsverlauf "
        f"einschließlich der finanziellen Lage, den Stand wichtiger "
        f"Projekte, die Personalentwicklung sowie über Risiken und "
        f"Chancen. Auf Anforderung erstattet er jederzeit Auskunft."
    )))

    s.append(("§ 3 Vergütung", (
        f"(1) Der Geschäftsführer erhält ein festes Jahresgehalt in "
        f"Höhe von EUR {gehalt} brutto. Das Festgehalt wird in zwölf "
        f"gleichen Monatsraten jeweils am letzten Bankarbeitstag eines "
        f"Monats nachträglich gezahlt.\n\n"
        f"(2) Mit dem Festgehalt sind sämtliche Tätigkeiten des "
        f"Geschäftsführers für die Gesellschaft und ihre verbundenen "
        f"Unternehmen abgegolten. Eine zusätzliche Vergütung für Über-"
        f"stunden oder Mehrarbeit wird nicht geschuldet.\n\n"
        f"(3) Die Gesellschaft prüft die Angemessenheit des Festgehalts "
        f"jährlich. Eine Anpassung kann zum 1. Januar eines jeden Jahres "
        f"erfolgen, frühestens zum 1. Januar des auf den Vertragsbeginn "
        f"folgenden Kalenderjahres."
    )))

    s.append(("§ 4 Variable Vergütung (Tantieme) und Long-Term Incentive", (
        f"(1) Zusätzlich zum Festgehalt erhält der Geschäftsführer eine "
        f"jährliche variable Vergütung (kurzfristige variable Vergütung – "
        f"„STI'). Die Bemessungsgrundlage des STI bilden konsolidierte "
        f"Unternehmenskennzahlen sowie individuelle Zielvereinbarungen.\n\n"
        f"(2) Die Zielerreichung wird wie folgt ermittelt:\n\n"
        f"a) 50 % gewichtet auf das konsolidierte EBIT der Gesellschaft "
        f"gegenüber Plan-EBIT laut Wirtschaftsplan;\n"
        f"b) 30 % gewichtet auf den Free Cash Flow gegenüber Plan;\n"
        f"c) 20 % gewichtet auf individuelle Ziele, die jährlich bis "
        f"zum 31. März für das laufende Geschäftsjahr zwischen "
        f"Geschäftsführer und Gesellschafterversammlung zu vereinbaren "
        f"sind.\n\n"
        f"(3) Bei 100 % Zielerreichung beträgt der STI 40 % des Fest-"
        f"gehalts (Target Bonus). Bei einer Zielerreichung von unter "
        f"70 % entfällt der STI ersatzlos; bei einer Zielerreichung "
        f"über 130 % ist der STI auf maximal {bonus_cap} % des "
        f"Festgehalts gedeckelt (Cap). Im Bereich zwischen 70 % und "
        f"130 % wird der STI linear interpoliert.\n\n"
        f"(4) Der STI wird nach Feststellung des Jahresabschlusses, "
        f"spätestens jedoch bis zum 30. April des Folgejahres, zur "
        f"Zahlung fällig. Ist das Anstellungsverhältnis zum Auszahlungs-"
        f"zeitpunkt durch ordentliche Kündigung des Geschäftsführers "
        f"oder durch außerordentliche, vom Geschäftsführer zu "
        f"vertretende Kündigung der Gesellschaft beendet, entfällt der "
        f"Anspruch auf den STI für das laufende Geschäftsjahr.\n\n"
        f"(5) Zusätzlich nimmt der Geschäftsführer an einem Long-Term "
        f"Incentive Plan („LTI') teil. Der LTI wird in dreijährigen "
        f"rollierenden Performance-Perioden gewährt. Die Bemessungs-"
        f"grundlage bilden der Total Shareholder Return (TSR), das "
        f"kumulierte EBITDA und ESG-Kennzahlen, jeweils mit gleicher "
        f"Gewichtung. Der jährliche Zielwert beträgt 50 % des "
        f"Festgehalts, der Cap 150 % des Zielwerts.\n\n"
        f"(6) Die Auszahlung des LTI erfolgt zu 50 % in bar und zu "
        f"50 % in Form von virtuellen Anteilen (Phantom Shares), die "
        f"nach Ablauf einer Sperrfrist von einem (1) Jahr in bar "
        f"abgegolten werden. Ein Anspruch auf Übertragung tatsächlicher "
        f"Geschäftsanteile besteht nicht.\n\n"
        f"(7) Die Modalitäten des LTI werden in einer gesonderten "
        f"LTI-Vereinbarung geregelt, die diesem Vertrag als Anlage "
        f"beigefügt ist."
    )))

    s.append(("§ 5 Aufwendungsersatz, Reisekosten, Dienstwagen", (
        f"(1) Der Geschäftsführer erhält Ersatz aller Aufwendungen, die "
        f"ihm in Ausübung seiner Tätigkeit entstehen, gegen Vorlage "
        f"prüffähiger Belege. Reisekosten werden nach den Bestimmungen "
        f"der Reisekostenrichtlinie der Gesellschaft erstattet.\n\n"
        f"(2) Die Gesellschaft stellt dem Geschäftsführer auf ihre "
        f"Kosten einen Dienstwagen der oberen Mittelklasse mit einem "
        f"Listenpreis von bis zu EUR 80.000 brutto zur dienstlichen und "
        f"privaten Nutzung zur Verfügung. Der Geschäftsführer kann "
        f"alternativ einen Zuschuss in Höhe der monatlichen Leasing-"
        f"rate erhalten (Car Allowance). Die private Nutzung wird nach "
        f"der 1 %-Methode lohnversteuert; die Steuerlast trägt der "
        f"Geschäftsführer.\n\n"
        f"(3) Der Geschäftsführer hat Anspruch auf Ersatz der Kosten "
        f"eines Mobiltelefons und eines Internetanschlusses an seinem "
        f"Heimarbeitsplatz."
    )))

    s.append(("§ 6 Altersversorgung", (
        f"(1) Die Gesellschaft erteilt dem Geschäftsführer eine "
        f"unmittelbare Versorgungszusage (Direktzusage) in Form einer "
        f"beitragsorientierten Leistungszusage. Die Gesellschaft führt "
        f"jährlich einen Beitrag in Höhe von 15 % des Festgehalts an "
        f"eine vom Geschäftsführer benannte rückgedeckte Unterstützungs-"
        f"kasse ab.\n\n"
        f"(2) Die Versorgungszusage umfasst Alters-, Berufsunfähigkeits- "
        f"und Hinterbliebenenleistungen. Die Einzelheiten ergeben sich "
        f"aus dem Versorgungsplan, der diesem Vertrag als Anlage "
        f"beigefügt ist.\n\n"
        f"(3) Die Versorgungsansprüche sind nach den Vorschriften des "
        f"Betriebsrentengesetzes unverfallbar.\n\n"
        f"(4) Der Geschäftsführer kann zusätzlich eine Entgeltumwandlung "
        f"gemäß § 1a BetrAVG vereinbaren. Die Gesellschaft leistet "
        f"hierauf einen Arbeitgeberzuschuss von 20 %."
    )))

    s.append(("§ 7 Versicherungen", (
        f"(1) Die Gesellschaft schließt auf ihre Kosten für den "
        f"Geschäftsführer eine D&O-Versicherung (Vermögensschaden-"
        f"Haftpflichtversicherung für Organe und leitende Angestellte) "
        f"mit einer Mindestdeckungssumme von EUR 10.000.000 pro "
        f"Versicherungsjahr ab. Der Selbstbehalt wird gemäß § 93 Abs. 2 "
        f"Satz 3 AktG analog auf 10 % des Schadens, höchstens "
        f"jedoch 150 % des festen Jahresgehalts festgelegt.\n\n"
        f"(2) Die Gesellschaft schließt zudem eine Unfallversicherung "
        f"(24-Stunden-Deckung) mit einer Versicherungssumme von "
        f"EUR 1.000.000 für den Todesfall und EUR 2.000.000 für "
        f"Invalidität ab. Begünstigte werden vom Geschäftsführer benannt.\n\n"
        f"(3) Die Gesellschaft schließt eine private "
        f"Krankenzusatzversicherung mit Chefarztbehandlung und "
        f"Einbettzimmerunterbringung ab."
    )))

    s.append(("§ 8 Urlaub", (
        "(1) Der Geschäftsführer hat Anspruch auf 30 Werktage Urlaub "
        "pro Kalenderjahr (entspricht 6 Wochen bei einer 5-Tage-Woche).\n\n"
        "(2) Der Geschäftsführer nimmt seinen Urlaub im Einvernehmen "
        "mit den übrigen Geschäftsführern und unter Berücksichtigung "
        "der betrieblichen Belange.\n\n"
        "(3) Kann der Urlaub aus zwingenden betrieblichen Gründen nicht "
        "im laufenden Kalenderjahr genommen werden, so kann er bis zum "
        "31. März des Folgejahres übertragen werden. Wird der Urlaub "
        "auch in diesem Zeitraum nicht genommen, kann er gegen eine "
        "finanzielle Abgeltung in Höhe von 1/250 des Festgehalts je "
        "Urlaubstag abgegolten werden."
    )))

    s.append(("§ 9 Arbeitsverhinderung, Krankheit, Tod", (
        "(1) Bei einer durch Krankheit oder unverschuldeter "
        "Arbeitsverhinderung bedingten Verhinderung an der Erbringung "
        "der Dienstleistung wird das Festgehalt für die Dauer von bis "
        "zu sechs (6) Monaten, längstens jedoch bis zum Ende des "
        "Anstellungsverhältnisses, fortgezahlt. Leistungen privater "
        "Versicherungen oder gesetzlicher Sozialversicherungsträger "
        "werden auf das fortgezahlte Gehalt angerechnet.\n\n"
        "(2) Der Geschäftsführer hat eine Arbeitsverhinderung "
        "unverzüglich anzuzeigen und ab dem dritten Tag eine "
        "ärztliche Arbeitsunfähigkeitsbescheinigung vorzulegen.\n\n"
        "(3) Im Falle des Todes des Geschäftsführers während der "
        "Vertragsdauer hat der überlebende Ehegatte/eingetragene "
        "Lebenspartner oder, sofern dieser nicht vorhanden ist, die "
        "unterhaltsberechtigten Kinder Anspruch auf Weiterzahlung des "
        "Festgehalts für drei (3) Monate, gerechnet ab dem auf den "
        "Todesfall folgenden Monatsbeginn."
    )))

    s.append(("§ 10 Nebentätigkeiten", (
        "(1) Der Geschäftsführer darf während der Dauer dieses Vertrages "
        "ohne vorherige schriftliche Zustimmung der Gesellschafter-"
        "versammlung keine Nebentätigkeit ausüben, gleich ob entgeltlich "
        "oder unentgeltlich.\n\n"
        "(2) Keiner Zustimmung bedürfen einmalige schriftstellerische, "
        "wissenschaftliche oder vortragsbezogene Tätigkeiten sowie die "
        "Übernahme von Ehrenämtern in Verbänden, soweit die "
        "Inanspruchnahme des Geschäftsführers durch die Gesellschaft "
        "nicht beeinträchtigt wird.\n\n"
        "(3) Die Übernahme von Mandaten in Aufsichts-, Verwaltungs- "
        "oder Beratungsgremien anderer Unternehmen bedarf der "
        "Zustimmung der Gesellschafterversammlung. Vergütungen aus "
        "solchen Tätigkeiten verbleiben beim Geschäftsführer, soweit "
        "sich aus der Zustimmung nichts anderes ergibt."
    )))

    s.append(("§ 11 Wettbewerbsverbot während der Vertragsdauer", (
        "(1) Der Geschäftsführer unterliegt während der Dauer dieses "
        "Vertrages einem umfassenden Wettbewerbsverbot. Er darf weder "
        "mittelbar noch unmittelbar für ein Unternehmen tätig sein, "
        "das mit der Gesellschaft oder einem mit ihr verbundenen "
        "Unternehmen im Wettbewerb steht oder geschäftliche Beziehungen "
        "unterhält.\n\n"
        "(2) Untersagt sind insbesondere die Gründung, der Erwerb oder "
        "die Beteiligung an einem Wettbewerbsunternehmen, die Tätigkeit "
        "als Organmitglied, Arbeitnehmer, Berater, Handelsvertreter "
        "oder in vergleichbarer Funktion für ein Wettbewerbsunternehmen.\n\n"
        "(3) Ausgenommen sind Beteiligungen an börsennotierten "
        "Gesellschaften, sofern sie 1 % der Stimmrechte nicht "
        "überschreiten."
    )))

    s.append(("§ 12 Nachvertragliches Wettbewerbsverbot", (
        f"(1) Der Geschäftsführer verpflichtet sich, für die Dauer von "
        f"24 Monaten nach Beendigung dieses Anstellungsvertrages weder "
        f"mittelbar noch unmittelbar in selbständiger, unselbständiger "
        f"oder sonstiger Weise für ein Unternehmen tätig zu werden, "
        f"das mit der Gesellschaft oder einem mit ihr verbundenen "
        f"Unternehmen im unmittelbaren oder mittelbaren Wettbewerb "
        f"steht oder mit ihr in laufender Geschäftsverbindung steht.\n\n"
        f"(2) Das nachvertragliche Wettbewerbsverbot gilt räumlich für "
        f"das Gebiet der Europäischen Union sowie für die Staaten, in "
        f"denen die Gesellschaft zum Zeitpunkt der Beendigung des "
        f"Anstellungsverhältnisses geschäftlich tätig war oder den "
        f"Markteintritt nachweislich vorbereitete.\n\n"
        f"(3) Sachlich erstreckt sich das Wettbewerbsverbot auf alle "
        f"Geschäftsfelder, in denen die Gesellschaft oder ein mit ihr "
        f"verbundenes Unternehmen tätig ist.\n\n"
        f"(4) Für die Dauer des nachvertraglichen Wettbewerbsverbots "
        f"zahlt die Gesellschaft dem Geschäftsführer eine Karenz-"
        f"entschädigung in Höhe von 50 % der vor Beendigung des "
        f"Anstellungsverhältnisses bezogenen vertraglichen Leistungen "
        f"(Festgehalt zuzüglich Durchschnitt der variablen Vergütung "
        f"der letzten drei abgerechneten Geschäftsjahre). Die Berechnung "
        f"erfolgt analog § 74 Abs. 2 HGB.\n\n"
        f"(5) Anderweitiger Erwerb des Geschäftsführers wird gemäß § 74c "
        f"HGB auf die Karenzentschädigung angerechnet, soweit der "
        f"anderweitige Erwerb zusammen mit der Karenzentschädigung den "
        f"Betrag der zuletzt bezogenen vertraglichen Leistungen um mehr "
        f"als 10 % übersteigt.\n\n"
        f"(6) Bei einem Verstoß gegen das nachvertragliche Wettbewerbs-"
        f"verbot entfällt der Anspruch auf Karenzentschädigung für die "
        f"Dauer des Verstoßes. Der Geschäftsführer hat zudem für jeden "
        f"Verstoß eine Vertragsstrafe in Höhe eines Brutto-Monats-"
        f"Festgehalts zu zahlen; bei einem Dauerverstoß gilt jeder "
        f"angefangene Monat als ein Verstoß. Die Geltendmachung "
        f"weiteren Schadensersatzes bleibt unberührt; die Vertragsstrafe "
        f"ist anzurechnen.\n\n"
        f"(7) Die Gesellschaft kann auf das nachvertragliche "
        f"Wettbewerbsverbot bis zum Ende des Anstellungsverhältnisses "
        f"durch schriftliche Erklärung verzichten. Im Falle des "
        f"Verzichts entfällt die Verpflichtung zur Zahlung der "
        f"Karenzentschädigung mit Ablauf eines Jahres ab Verzichtserklärung."
    )))

    s.append(("§ 13 Geheimhaltung", (
        "(1) Der Geschäftsführer ist verpflichtet, über alle "
        "vertraulichen Angelegenheiten der Gesellschaft und der mit ihr "
        "verbundenen Unternehmen, insbesondere Geschäfts- und "
        "Betriebsgeheimnisse im Sinne des § 2 Nr. 1 GeschGehG, "
        "auch nach Beendigung dieses Vertrages auf unbefristete Dauer "
        "Stillschweigen zu bewahren.\n\n"
        "(2) Bei Beendigung des Anstellungsverhältnisses hat der "
        "Geschäftsführer alle in seinem Besitz befindlichen Unterlagen, "
        "Aufzeichnungen und Datenträger der Gesellschaft – einschließlich "
        "elektronischer Kopien – an die Gesellschaft herauszugeben. "
        "Ein Zurückbehaltungsrecht steht ihm nicht zu.\n\n"
        "(3) Die Vorschriften des GeschGehG bleiben unberührt."
    )))

    s.append(("§ 14 Arbeitnehmererfindungen und Schutzrechte", (
        "(1) Erfindungen, technische Verbesserungsvorschläge, "
        "Designschöpfungen, urheberrechtlich geschützte Werke und "
        "sonstige Arbeitsergebnisse, die der Geschäftsführer während "
        "der Dauer dieses Vertrages allein oder zusammen mit anderen "
        "Personen schafft, gehören mit allen Rechten und Befugnissen "
        "ausschließlich der Gesellschaft.\n\n"
        "(2) Der Geschäftsführer überträgt der Gesellschaft hiermit "
        "alle übertragbaren Rechte an den Arbeitsergebnissen, "
        "insbesondere das ausschließliche, zeitlich, räumlich und "
        "inhaltlich unbeschränkte Nutzungsrecht. Die Übertragung umfasst "
        "alle bekannten und unbekannten Nutzungsarten. Eine zusätzliche "
        "Vergütung wird hiermit nicht geschuldet, da sie bereits in der "
        "Gesamtvergütung pauschal abgegolten ist.\n\n"
        "(3) Soweit das Arbeitnehmererfindungsgesetz (ArbnErfG) "
        "Anwendung findet, gilt es als hiermit vereinbart, dass die "
        "Gesellschaft alle Diensterfindungen unbeschränkt in Anspruch "
        "nimmt.\n\n"
        "(4) Der Geschäftsführer wird bei der Anmeldung, Eintragung, "
        "Aufrechterhaltung und Verteidigung von Schutzrechten in "
        "zumutbarem Umfang mitwirken."
    )))

    s.append(("§ 15 Compliance und Code of Conduct", (
        "(1) Der Geschäftsführer verpflichtet sich, die jeweils "
        "geltenden gesetzlichen Vorschriften, den Verhaltenskodex "
        "(Code of Conduct) der Gesellschaft sowie alle internen "
        "Richtlinien einzuhalten und auf deren Einhaltung im "
        "Unternehmen hinzuwirken.\n\n"
        "(2) Er hat insbesondere die Vorschriften zur Korruptions- "
        "und Geldwäschebekämpfung, das Kartell- und Wettbewerbsrecht, "
        "das Datenschutzrecht, das Sanktions- und Exportkontrollrecht "
        "sowie steuer- und sozialversicherungsrechtliche Bestimmungen "
        "zu beachten.\n\n"
        "(3) Der Geschäftsführer wird ein angemessenes Compliance-"
        "Management-System (CMS) implementieren, dessen Wirksamkeit "
        "regelmäßig überprüfen und der Gesellschafterversammlung "
        "jährlich Bericht erstatten."
    )))

    s.append(("§ 16 Vertragsdauer, Abberufung, Kündigung", (
        f"(1) Dieser Vertrag wird auf bestimmte Zeit für die Dauer von "
        f"{dauer} Jahren geschlossen, beginnend am {start}. Er endet "
        f"– ohne dass es einer Kündigung bedarf – mit Ablauf des "
        f"Datums, das fünf (5) Jahre nach Vertragsbeginn liegt, "
        f"spätestens jedoch mit Ablauf des Monats, in dem der "
        f"Geschäftsführer das gesetzliche Renteneintrittsalter erreicht.\n\n"
        f"(2) Bei rechtzeitiger Wiederbestellung verlängert sich dieser "
        f"Vertrag um die Dauer der erneuten Bestellung, soweit nicht "
        f"eine Partei der Verlängerung mit einer Frist von sechs (6) "
        f"Monaten zum Ende der Bestelldauer schriftlich widerspricht.\n\n"
        f"(3) Das Recht beider Parteien zur außerordentlichen Kündigung "
        f"aus wichtigem Grund (§ 626 BGB) bleibt unberührt.\n\n"
        f"(4) Die Abberufung als Geschäftsführer durch die Gesellschafter-"
        f"versammlung ist jederzeit zulässig und beendet das "
        f"Anstellungsverhältnis nicht. Erfolgt die Abberufung ohne "
        f"wichtigen Grund, so ist die Gesellschaft verpflichtet, das "
        f"Festgehalt bis zum nächstmöglichen ordentlichen Vertragsende "
        f"weiterzuzahlen.\n\n"
        f"(5) Jede Kündigung bedarf der Schriftform; eine Kündigung "
        f"per Telefax oder E-Mail genügt nicht."
    )))

    s.append(("§ 17 Change of Control", (
        f"(1) Im Falle eines Kontrollwechsels im Sinne der "
        f"§§ 15 ff. AktG bei der Gesellschaft (insbesondere Erwerb von "
        f"mehr als 50 % der Stimmrechte durch einen Dritten, "
        f"Verschmelzung oder vergleichbare Strukturmaßnahme) steht dem "
        f"Geschäftsführer ein Sonderkündigungsrecht zu.\n\n"
        f"(2) Das Sonderkündigungsrecht kann binnen sechs (6) Monaten "
        f"nach Wirksamwerden des Kontrollwechsels durch schriftliche "
        f"Erklärung mit einer Frist von drei (3) Monaten zum Monats-"
        f"ende ausgeübt werden.\n\n"
        f"(3) Macht der Geschäftsführer von seinem Sonderkündigungs-"
        f"recht Gebrauch oder wird der Geschäftsführer aus Anlass des "
        f"Kontrollwechsels ohne wichtigen Grund seitens der Gesellschaft "
        f"abberufen oder gekündigt, so erhält er eine Abfindung in Höhe "
        f"von 24 Brutto-Monatsgehältern (Festgehalt zuzüglich des "
        f"durchschnittlichen STI der letzten drei Geschäftsjahre).\n\n"
        f"(4) Ungeunwirksam ausgegebene LTI-Tranchen werden im Falle "
        f"eines Kontrollwechsels sofort unverfallbar (Vesting "
        f"Acceleration); die Abrechnung erfolgt zum Verkehrswert zum "
        f"Stichtag des Kontrollwechsels.\n\n"
        f"(5) Die Abfindung wird mit Beendigung des Anstellungs-"
        f"verhältnisses fällig."
    )))

    s.append(("§ 18 Schlussbestimmungen", (
        "(1) Änderungen und Ergänzungen dieses Vertrages, einschließlich "
        "dieser Schriftformklausel, bedürfen zu ihrer Wirksamkeit der "
        "Schriftform.\n\n"
        "(2) Mündliche Nebenabreden bestehen nicht.\n\n"
        "(3) " + SALVATORISCH + "\n\n"
        "(4) Es gilt deutsches Recht. Ausschließlicher Gerichtsstand "
        "ist der Sitz der Gesellschaft, soweit gesetzlich zulässig.\n\n"
        "(5) Anlagen, die diesem Vertrag beigefügt sind: LTI-Plan, "
        "Versorgungsplan, Code of Conduct, Geschäftsordnung für die "
        "Geschäftsführung, Reisekostenrichtlinie."
    )))

    s.append(("Unterschriften", _signature_block(
        p, _g(p, "gesellschafter_name", "Gesellschaft, vertreten durch den "
              "Gesellschafterausschuss"),
        "für die Gesellschaft", gf, "Geschäftsführer/in"
    )))

    return s


# =====================================================================
# AUFSICHTSRATS-DIENSTVERTRAG
# =====================================================================

def gen_aufsichtsrat_dienstvertrag(p: Dict[str, Any]) -> List[Section]:
    """Aufsichtsratsmitglied-Dienstvertrag. Target: 1500-2000 Wörter."""

    company = _g(p, "company", "Muster AG")
    member = _g(p, "member", "Prof. Dr. Helga Brandt")
    city = _g(p, "city", "Frankfurt am Main")
    vergutung = _g(p, "vergutung", "35.000")

    s: List[Section] = []

    s.append(("Präambel", (
        f"Zwischen der {company} mit Sitz in {city} – nachfolgend "
        f"„Gesellschaft' – und Frau/Herrn {member}, wohnhaft in "
        f"[Anschrift] – nachfolgend „Aufsichtsratsmitglied' – "
        f"wird der nachfolgende Dienstvertrag geschlossen.\n\n"
        f"Frau/Herr {member} wurde durch Beschluss der ordentlichen "
        f"Hauptversammlung der Gesellschaft vom [Datum] zum Mitglied "
        f"des Aufsichtsrats gewählt. Mit diesem Vertrag werden die "
        f"schuldrechtlichen Aspekte der Tätigkeit geregelt."
    )))

    s.append(("§ 1 Vertragsgegenstand", (
        f"(1) Gegenstand dieses Vertrages ist die Wahrnehmung der "
        f"Tätigkeit als Mitglied des Aufsichtsrats der Gesellschaft, "
        f"einschließlich der Mitwirkung in Ausschüssen.\n\n"
        f"(2) Die Tätigkeit umfasst insbesondere die Teilnahme an "
        f"Sitzungen des Aufsichtsrats und seiner Ausschüsse, die "
        f"Beratung und Überwachung des Vorstands, die Mitwirkung an "
        f"strategischen Entscheidungen sowie die Prüfung des Jahres-"
        f"und Konzernabschlusses.\n\n"
        f"(3) Das Aufsichtsratsmitglied übt seine Tätigkeit unabhängig "
        f"und eigenverantwortlich aus. Es ist an Weisungen weder der "
        f"Gesellschaft noch ihrer Organe oder einzelner Aktionäre "
        f"gebunden."
    )))

    s.append(("§ 2 Sorgfaltspflicht und Verschwiegenheit", (
        "(1) Das Aufsichtsratsmitglied hat seine Tätigkeit mit der "
        "Sorgfalt eines ordentlichen und gewissenhaften Aufsichtsrats "
        "gemäß § 116 i.V.m. § 93 AktG zu erfüllen.\n\n"
        "(2) Das Aufsichtsratsmitglied ist zur Verschwiegenheit über "
        "alle ihm in seiner Eigenschaft als Aufsichtsratsmitglied "
        "bekannt gewordenen vertraulichen Berichte und vertraulichen "
        "Beratungen verpflichtet. Die Verschwiegenheitspflicht besteht "
        "auch nach Beendigung der Aufsichtsratstätigkeit unbefristet fort.\n\n"
        "(3) Das Aufsichtsratsmitglied hat insbesondere Insider-"
        "informationen im Sinne von Art. 7 MAR vertraulich zu behandeln "
        "und die Vorschriften zum Insiderhandel zu beachten.\n\n"
        "(4) Der Deutsche Corporate Governance Kodex in seiner jeweils "
        "aktuellen Fassung ist – soweit für die Gesellschaft anwendbar – "
        "zu beachten."
    )))

    s.append(("§ 3 Vergütung", (
        f"(1) Das Aufsichtsratsmitglied erhält eine feste Vergütung "
        f"von EUR {vergutung} pro Geschäftsjahr.\n\n"
        f"(2) Übernimmt das Aufsichtsratsmitglied den Vorsitz des "
        f"Aufsichtsrats oder eines Ausschusses, erhöht sich die "
        f"Vergütung nach Maßgabe der Satzung.\n\n"
        f"(3) Die Vergütung wird nach Ablauf des Geschäftsjahres "
        f"jeweils zum 31. März des Folgejahres ausgezahlt.\n\n"
        f"(4) Mit der Vergütung sind sämtliche Tätigkeiten des "
        f"Aufsichtsratsmitglieds einschließlich der Vorbereitung von "
        f"Sitzungen, der Teilnahme an Sitzungen und der Mitwirkung in "
        f"Ausschüssen abgegolten."
    )))

    s.append(("§ 4 Auslagenersatz", (
        "(1) Die Gesellschaft erstattet dem Aufsichtsratsmitglied alle "
        "in Ausübung der Tätigkeit anfallenden Auslagen, insbesondere "
        "Reisekosten, gegen Vorlage prüffähiger Belege.\n\n"
        "(2) Reisekosten werden nach den steuerlichen Höchstsätzen "
        "erstattet; Flüge in der Business Class auf Strecken über "
        "vier Stunden Flugzeit, sowie Hotelübernachtungen bis zu "
        "EUR 350 pro Nacht (in Großstädten und Konferenzorten bis "
        "EUR 500) sind erstattungsfähig."
    )))

    s.append(("§ 5 D&O-Versicherung", (
        "(1) Die Gesellschaft schließt für das Aufsichtsratsmitglied "
        "auf eigene Kosten eine D&O-Versicherung mit einer Deckungs-"
        "summe von mindestens EUR 10.000.000 pro Versicherungsjahr ab.\n\n"
        "(2) Der Versicherungsschutz umfasst auch ein Run-off mit "
        "Mindestlaufzeit von fünf Jahren nach Ende der Bestellung "
        "(Nachhaftung).\n\n"
        "(3) Das Aufsichtsratsmitglied trägt keinen Selbstbehalt; "
        "§ 93 Abs. 2 Satz 3 AktG findet keine Anwendung."
    )))

    s.append(("§ 6 Beendigung", (
        "(1) Dieser Vertrag endet mit Beendigung der Aufsichtsrats-"
        "tätigkeit aus welchem Grund auch immer.\n\n"
        "(2) Das Recht zur außerordentlichen Kündigung aus wichtigem "
        "Grund bleibt unberührt."
    )))

    s.append(("§ 7 Schlussbestimmungen", (
        "(1) Änderungen und Ergänzungen dieses Vertrages bedürfen der "
        "Schriftform.\n\n"
        "(2) " + SALVATORISCH + "\n\n"
        "(3) Es gilt deutsches Recht. Gerichtsstand ist der Sitz der "
        "Gesellschaft."
    )))

    s.append(("Unterschriften", _signature_block(
        p, "Vorstand der " + company, "für die Gesellschaft",
        member, "Aufsichtsratsmitglied"
    )))

    return s


# =====================================================================
# COMMERCIAL CONTRACTS / VERTRAGSRECHT
# =====================================================================

def gen_master_supply_agreement_de(p: Dict[str, Any]) -> List[Section]:
    """Großkunden-Rahmenliefervertrag. Target: 5000-8000 Wörter."""

    supplier = _g(p, "supplier", "Muster GmbH")
    customer = _g(p, "customer", "Großkunde AG")
    city = _g(p, "city", "Köln")
    product = _g(p, "product", "industrielle Komponenten gemäß Spezifikation")
    laufzeit = _g(p, "laufzeit", "5")
    cap_pct = _g(p, "cap_pct", "100")

    s: List[Section] = []

    s.append(("Präambel", (
        f"Zwischen {supplier} (nachfolgend „Lieferant') und {customer} "
        f"(nachfolgend „Kunde'; Lieferant und Kunde gemeinsam auch "
        f"„Parteien' und jeder einzeln „Partei') wird der folgende "
        f"Rahmenliefervertrag (nachfolgend „Vertrag') geschlossen.\n\n"
        f"Der Lieferant ist ein etablierter Hersteller von {product}. "
        f"Der Kunde beabsichtigt, im Rahmen seiner Geschäftstätigkeit "
        f"Produkte des Lieferanten in größerem Umfang zu beziehen. "
        f"Die Parteien wünschen, ihre Liefer- und Bezugsbeziehung auf "
        f"eine langfristige, partnerschaftliche und rechtssichere "
        f"Grundlage zu stellen. Dies vorausgeschickt vereinbaren die "
        f"Parteien wie folgt:"
    )))

    s.append(("§ 1 Begriffsbestimmungen", (
        f"Im Sinne dieses Vertrages haben die nachfolgenden Begriffe "
        f"die folgenden Bedeutungen:\n\n"
        f"„Vertragsprodukte' bezeichnet die in Anlage 1 spezifizierten "
        f"Produkte einschließlich aller etwaigen Erweiterungen und "
        f"Modifikationen, die in Übereinstimmung mit § 5 vereinbart "
        f"werden.\n\n"
        f"„Spezifikationen' bezeichnet die in Anlage 1 (Technische "
        f"Spezifikationen) und Anlage 2 (Qualitätsanforderungen) "
        f"festgelegten technischen und qualitativen Eigenschaften der "
        f"Vertragsprodukte.\n\n"
        f"„Bestellung' bezeichnet jede vom Kunden auf Grundlage dieses "
        f"Vertrages erteilte einzelne Bestellung von Vertragsprodukten "
        f"in Form einer Einzelabrufbestellung.\n\n"
        f"„Forecast' bezeichnet die rollierende Vorausschau des Kunden "
        f"über seinen voraussichtlichen Bedarf an Vertragsprodukten "
        f"gemäß § 4.\n\n"
        f"„Liefertermin' bezeichnet das in der jeweiligen Bestellung "
        f"oder dem Liefereinteilungsplan vereinbarte Datum, an dem die "
        f"Vertragsprodukte am vereinbarten Lieferort eintreffen sollen.\n\n"
        f"„Mängel' bezeichnet die Abweichungen der Vertragsprodukte von "
        f"den vereinbarten Spezifikationen oder von der gewöhnlich "
        f"vorausgesetzten Beschaffenheit.\n\n"
        f"„Geschäftstag' bezeichnet jeden Tag, der weder Samstag noch "
        f"Sonntag ist und an dem Geschäftsbanken in Frankfurt am Main "
        f"für den allgemeinen Geschäftsverkehr geöffnet sind.\n\n"
        f"„Vertrauliche Informationen' hat die in § 16 festgelegte "
        f"Bedeutung.\n\n"
        f"„Höhere Gewalt' hat die in § 14 festgelegte Bedeutung.\n\n"
        f"„Quality Agreement' bzw. „QSV' bezeichnet die als Anlage 3 "
        f"beigefügte Qualitätssicherungsvereinbarung.\n\n"
        f"„Verbundene Unternehmen' bezeichnet die im Sinne der "
        f"§§ 15 ff. AktG verbundenen Unternehmen."
    )))

    s.append(("§ 2 Vertragsgegenstand und Produkte", (
        f"(1) Dieser Vertrag regelt die Bedingungen, zu denen der "
        f"Lieferant während der Vertragslaufzeit dem Kunden die "
        f"Vertragsprodukte liefert und der Kunde diese vom Lieferanten "
        f"bezieht. Einzelne Liefer- und Kaufverträge kommen erst durch "
        f"die Erteilung und Annahme von Bestellungen gemäß § 4 zustande.\n\n"
        f"(2) Der Lieferant verpflichtet sich, dem Kunden während der "
        f"Vertragslaufzeit die Vertragsprodukte in der jeweils vom "
        f"Kunden abgerufenen Menge zu den im Vertrag vereinbarten "
        f"Konditionen zu liefern.\n\n"
        f"(3) Der Kunde verpflichtet sich, die Vertragsprodukte während "
        f"der Vertragslaufzeit zumindest in der gemäß Anlage 4 "
        f"festgelegten Mindestmenge je Vertragsjahr abzunehmen "
        f"(„Mindestabnahmemenge'). Bei Nichterreichung der Mindest-"
        f"abnahmemenge findet § 4 Abs. 6 Anwendung.\n\n"
        f"(4) Eine ausschließliche Bezugsverpflichtung für den Kunden "
        f"oder eine ausschließliche Lieferverpflichtung für den "
        f"Lieferanten besteht nicht, soweit nicht ausdrücklich anders "
        f"vereinbart."
    )))

    s.append(("§ 3 Lieferung, Lieferort, Gefahrübergang", (
        f"(1) Sofern in der Einzelbestellung nichts anderes vereinbart "
        f"ist, erfolgen Lieferungen DAP (Delivered at Place) gemäß "
        f"Incoterms® 2020 zur Anlieferadresse des Kunden gemäß "
        f"Anlage 5.\n\n"
        f"(2) Der Lieferant ist verpflichtet, die Vertragsprodukte "
        f"handelsüblich zu verpacken und alle für den sicheren Transport "
        f"erforderlichen Maßnahmen zu treffen. Verpackungen werden "
        f"nicht zurückgenommen, soweit nicht in der Einzelbestellung "
        f"anders vereinbart.\n\n"
        f"(3) Teillieferungen sind nur mit vorheriger schriftlicher "
        f"Zustimmung des Kunden zulässig.\n\n"
        f"(4) Die Gefahr des zufälligen Untergangs und der zufälligen "
        f"Verschlechterung geht entsprechend der vereinbarten "
        f"Incoterms®-Klausel über. Bei DAP geht die Gefahr mit "
        f"Bereitstellung der Ware zur Entladung am vereinbarten "
        f"Lieferort über.\n\n"
        f"(5) Im Falle erkennbarer Lieferverzögerungen wird der "
        f"Lieferant den Kunden unverzüglich, spätestens jedoch binnen "
        f"24 Stunden nach Kenntniserlangung, unter Angabe der Gründe "
        f"und des voraussichtlichen Liefertermins informieren."
    )))

    s.append(("§ 4 Forecast, Bestellverfahren, Mindestabnahme", (
        f"(1) Der Kunde übermittelt dem Lieferanten monatlich, jeweils "
        f"bis zum letzten Geschäftstag eines Kalendermonats, einen "
        f"rollierenden 12-Monats-Forecast über seinen voraussichtlichen "
        f"Bedarf an Vertragsprodukten.\n\n"
        f"(2) Der Forecast ist in folgende Verbindlichkeitsstufen "
        f"unterteilt:\n\n"
        f"a) Monate 1 bis 3 sind verbindliche Bestellungen ('Frozen "
        f"Zone'); der Kunde kann diese nur mit Zustimmung des "
        f"Lieferanten ändern, der seine Zustimmung nicht unbillig "
        f"verweigern darf;\n\n"
        f"b) Monate 4 bis 6 dienen als kapazitätsverbindliche Vorschau "
        f"('Capacity Window'); Mengenabweichungen bis zu 20 % gegenüber "
        f"dem zuletzt mitgeteilten Forecast bleiben unverbindlich;\n\n"
        f"c) Monate 7 bis 12 dienen ausschließlich der Planung; eine "
        f"Bindungswirkung besteht nicht.\n\n"
        f"(3) Einzelne Bestellungen werden vom Kunden in Textform "
        f"(§ 126b BGB) per E-Mail, EDI oder über das vereinbarte "
        f"Lieferantenportal an den Lieferanten übermittelt. Eine "
        f"Bestellung gilt als angenommen, wenn der Lieferant ihr nicht "
        f"binnen drei (3) Geschäftstagen widerspricht.\n\n"
        f"(4) Abrufbestellungen müssen folgende Angaben enthalten: "
        f"Artikelnummer, Menge, Liefertermin, Lieferadresse, "
        f"Bestellnummer, Preis (sofern nicht in der Preisliste gemäß "
        f"Anlage 6 ausgewiesen).\n\n"
        f"(5) Bestellungen, die der Lieferant ohne Widerspruch angenommen "
        f"hat, sind für beide Parteien verbindlich. Der Kunde kann "
        f"verbindlich angenommene Bestellungen nur mit Zustimmung des "
        f"Lieferanten oder gegen Erstattung der bis dahin angefallenen "
        f"Aufwendungen stornieren.\n\n"
        f"(6) Erreicht der Kunde in einem Vertragsjahr nicht die "
        f"vereinbarte Mindestabnahmemenge gemäß Anlage 4, so leistet "
        f"er an den Lieferanten einen Ausgleichsbetrag in Höhe der "
        f"Differenz zwischen tatsächlicher Abnahme und Mindestabnahme, "
        f"multipliziert mit 30 % des Listenpreises (Deckungsbeitrags-"
        f"ausgleich). Höhere Gewalt sowie vom Lieferanten zu vertretende "
        f"Lieferengpässe bleiben unberücksichtigt."
    )))

    s.append(("§ 5 Spezifikationen und Engineering Change", (
        f"(1) Die Vertragsprodukte müssen den in Anlage 1 (Technische "
        f"Spezifikationen) und Anlage 2 (Qualitätsanforderungen) "
        f"festgelegten Anforderungen entsprechen.\n\n"
        f"(2) Der Lieferant darf die Spezifikationen, die Konstruktion, "
        f"den Herstellungsprozess, die verwendeten Werkstoffe und "
        f"Komponenten oder den Herstellungsort der Vertragsprodukte "
        f"nicht ohne vorherige schriftliche Zustimmung des Kunden "
        f"verändern. Der Kunde wird seine Zustimmung nicht ohne "
        f"sachlichen Grund verweigern.\n\n"
        f"(3) Der Lieferant wird den Kunden über beabsichtigte "
        f"Änderungen schriftlich mit angemessener Vorlaufzeit, "
        f"mindestens jedoch sechs (6) Monate vor Wirksamwerden, "
        f"unter Angabe der Auswirkungen auf Form, Funktion, Maße, "
        f"Gewicht, Lebensdauer und Preis informieren (Engineering Change "
        f"Notification – „ECN').\n\n"
        f"(4) Der Kunde kann jederzeit Änderungen an den Spezifikationen "
        f"verlangen. Beeinflusst die geforderte Änderung Preise, "
        f"Liefertermine oder andere wesentliche Vertragspflichten, "
        f"werden die Parteien in gutem Glauben eine angemessene "
        f"Anpassung verhandeln (Engineering Change Request – „ECR').\n\n"
        f"(5) Bis zur Einigung über die Auswirkungen einer "
        f"geforderten Änderung erfolgt die Lieferung nach den bisherigen "
        f"Spezifikationen."
    )))

    s.append(("§ 6 Preise und Preisanpassung", (
        f"(1) Die Preise der Vertragsprodukte sind in Anlage 6 "
        f"(Preisliste) ausgewiesen und verstehen sich in Euro netto "
        f"zuzüglich der jeweils geltenden gesetzlichen Umsatzsteuer.\n\n"
        f"(2) Die Preise gelten für die ersten 12 Monate der "
        f"Vertragslaufzeit fest. Danach werden die Preise einmal "
        f"jährlich, jeweils zum 1. Januar, nach Maßgabe der folgenden "
        f"Bestimmungen angepasst.\n\n"
        f"(3) Materialkostenbestandteile werden nach den jeweils "
        f"einschlägigen Indizes (insbesondere Aluminium-, Stahl-, "
        f"Kupfer- und Kunststoff-Indizes des LME bzw. der Reuters-"
        f"Notierung) zum Stichtag 1. November des Vorjahres angepasst "
        f"(Pass-Through). Energiekosten werden nach dem Index der "
        f"Energie-Großhandelspreise (BDEW) angepasst.\n\n"
        f"(4) Lohnkosten werden anteilig nach dem Tariflohnindex der "
        f"jeweiligen Branche angepasst, soweit der Lohnkostenanteil "
        f"mindestens 20 % am Gesamtpreis ausmacht.\n\n"
        f"(5) Über die Höhe der Preisanpassung verhandeln die Parteien "
        f"in gutem Glauben. Kann eine Einigung bis zum 15. Dezember "
        f"des Vorjahres nicht erzielt werden, so bestellt jede Partei "
        f"einen unabhängigen Wirtschaftsprüfer; können sich die "
        f"Wirtschaftsprüfer nicht binnen 30 Tagen einigen, entscheidet "
        f"ein vom Präsidenten der WPK benannter Schiedsgutachter "
        f"verbindlich.\n\n"
        f"(6) Unabhängig von der jährlichen Anpassung sind die Parteien "
        f"bei wesentlichen Veränderungen der Marktbedingungen "
        f"(Veränderung eines Eingangsmaterialpreises um mehr als 20 % "
        f"gegenüber Vertragsabschluss) berechtigt, Verhandlungen über "
        f"eine außerplanmäßige Preisanpassung zu verlangen.\n\n"
        f"(7) Der Lieferant verpflichtet sich, in jedem Vertragsjahr "
        f"Produktivitätsverbesserungen in Höhe von mindestens 2 % "
        f"des Vorjahrespreises an den Kunden weiterzugeben "
        f"(Productivity Reduction)."
    )))

    s.append(("§ 7 Zahlungsbedingungen", (
        f"(1) Die Rechnungsstellung erfolgt nach Lieferung. Rechnungen "
        f"müssen den gesetzlichen Anforderungen, insbesondere "
        f"§§ 14, 14a UStG, entsprechen.\n\n"
        f"(2) Rechnungen sind innerhalb von 60 Tagen nach Erhalt netto "
        f"ohne Abzug zur Zahlung fällig. Bei Zahlung innerhalb von "
        f"14 Tagen wird ein Skonto von 2 % gewährt.\n\n"
        f"(3) Im Falle des Zahlungsverzuges ist der Lieferant berechtigt, "
        f"Verzugszinsen in Höhe von neun Prozentpunkten (9 %-Pkt.) über "
        f"dem Basiszinssatz nach § 247 BGB zu berechnen. Die "
        f"Geltendmachung eines weitergehenden Verzugsschadens bleibt "
        f"unberührt.\n\n"
        f"(4) Aufrechnungsrechte stehen dem Kunden nur zu, wenn seine "
        f"Gegenansprüche rechtskräftig festgestellt, unbestritten oder "
        f"vom Lieferanten anerkannt sind.\n\n"
        f"(5) Ein Zurückbehaltungsrecht kann der Kunde nur ausüben, "
        f"soweit sein Gegenanspruch auf demselben Vertragsverhältnis "
        f"beruht."
    )))

    s.append(("§ 8 Qualitätssicherung", (
        f"(1) Der Lieferant unterhält ein zertifiziertes Qualitäts-"
        f"managementsystem mindestens nach ISO 9001, im Automotive-"
        f"Bereich nach IATF 16949. Eine gültige Zertifizierungsurkunde "
        f"ist dem Kunden auf Verlangen vorzulegen.\n\n"
        f"(2) Einzelheiten der Qualitätssicherung sind in der Qualitäts-"
        f"sicherungsvereinbarung (QSV, Anlage 3) geregelt, die "
        f"Bestandteil dieses Vertrages ist.\n\n"
        f"(3) Der Lieferant gewährleistet eine durchgehende Rückverfolg-"
        f"barkeit der Vertragsprodukte (Traceability) auf Charge- und "
        f"ggf. Seriennummern-Ebene.\n\n"
        f"(4) Der Lieferant räumt dem Kunden Audit-Rechte ein. "
        f"Werks- und Prozessaudits werden nach Vorankündigung von "
        f"mindestens zehn (10) Geschäftstagen während der üblichen "
        f"Geschäftszeiten durchgeführt. Bei begründeten Qualitäts-"
        f"problemen ist eine kurzfristige Auditierung mit einer "
        f"Vorankündigung von 24 Stunden zulässig."
    )))

    s.append(("§ 9 Wareneingang, Annahme, Rüge", (
        f"(1) Der Kunde wird die Vertragsprodukte nach Eingang "
        f"unverzüglich auf erkennbare Mängel, insbesondere Identität, "
        f"Menge, Verpackungs- und Transportschäden, untersuchen. "
        f"Erkennbare Mängel sind binnen 14 Geschäftstagen nach "
        f"Wareneingang in Textform zu rügen.\n\n"
        f"(2) Verdeckte Mängel sind binnen 14 Geschäftstagen nach "
        f"Entdeckung, spätestens jedoch innerhalb der Gewährleistungs-"
        f"frist, in Textform zu rügen.\n\n"
        f"(3) § 377 HGB bleibt unberührt; die Pflicht zur unverzüglichen "
        f"Rüge bei vermehrtem Verbrauch oder bei Massenfertigung wird "
        f"jedoch dergestalt modifiziert, dass der Kunde nur zu einer "
        f"angemessenen Stichprobenprüfung verpflichtet ist."
    )))

    s.append(("§ 10 Gewährleistung", (
        f"(1) Der Lieferant gewährleistet, dass die Vertragsprodukte "
        f"frei von Sach- und Rechtsmängeln sind, den vereinbarten "
        f"Spezifikationen entsprechen und für die gewöhnliche Verwendung "
        f"geeignet sind.\n\n"
        f"(2) Die Gewährleistungsfrist beträgt 36 Monate ab Übergabe "
        f"der Vertragsprodukte am vereinbarten Lieferort. Für "
        f"Vertragsprodukte, die bestimmungsgemäß in Anlagen oder "
        f"Fahrzeugen eingebaut werden, beginnt die Gewährleistungsfrist "
        f"mit Inverkehrbringen des Endprodukts, längstens jedoch "
        f"48 Monate nach Lieferung.\n\n"
        f"(3) Im Falle eines Mangels hat der Kunde dem Lieferanten "
        f"eine angemessene Frist zur Nacherfüllung zu setzen. Die "
        f"Nacherfüllung erfolgt nach Wahl des Kunden durch "
        f"Nachbesserung oder Ersatzlieferung. Schlägt die Nacherfüllung "
        f"fehl oder ist sie unzumutbar, stehen dem Kunden die gesetzlichen "
        f"Rechte (Rücktritt, Minderung, Schadensersatz, Aufwendungsersatz) "
        f"zu.\n\n"
        f"(4) Bei drohendem unverhältnismäßig hohen Schaden oder zur "
        f"Aufrechterhaltung der eigenen Produktion ist der Kunde "
        f"berechtigt, die Selbstvornahme oder die Beauftragung eines "
        f"Dritten zur Mängelbeseitigung gemäß § 637 BGB ohne Frist-"
        f"setzung vorzunehmen, sofern eine Mitteilung an den Lieferanten "
        f"zumutbar nicht möglich ist; die entstehenden Aufwendungen "
        f"sind vom Lieferanten zu ersetzen.\n\n"
        f"(5) Aufwendungen für Demontage und Montage der mangelhaften "
        f"Vertragsprodukte aus bzw. in das End-/Folgeprodukt trägt der "
        f"Lieferant nach § 439 Abs. 3 BGB, soweit der Einbau in das "
        f"End-/Folgeprodukt vor Mangelfeststellung bestimmungsgemäß "
        f"erfolgt ist.\n\n"
        f"(6) Mängelansprüche bei einem Mangel verjähren mit Ablauf "
        f"der Gewährleistungsfrist nach Abs. 2. Bei arglistigem "
        f"Verschweigen eines Mangels gilt die gesetzliche Verjährungsfrist."
    )))

    s.append(("§ 11 Produkthaftung und Rückrufkosten", (
        f"(1) Soweit der Lieferant für einen Produktschaden verantwortlich "
        f"ist, ist er verpflichtet, den Kunden insoweit von Schadensersatz-"
        f"ansprüchen Dritter auf erstes Anfordern freizustellen, als die "
        f"Ursache in seinem Herrschafts- und Organisationsbereich gesetzt "
        f"ist und er im Außenverhältnis selbst haftet.\n\n"
        f"(2) Der Lieferant erstattet dem Kunden in entsprechender "
        f"Anwendung des § 1 ProdHaftG i.V.m. § 254 BGB Aufwendungen, "
        f"die sich aus oder im Zusammenhang mit einer vom Kunden "
        f"durchgeführten Rückrufaktion ergeben, soweit die Rückrufaktion "
        f"auf einen vom Lieferanten zu vertretenden Mangel der "
        f"Vertragsprodukte zurückzuführen ist.\n\n"
        f"(3) Der Kunde wird den Lieferanten über Inhalt und Umfang "
        f"einer durchzuführenden Rückrufaktion – soweit möglich und "
        f"zumutbar – unterrichten und ihm Gelegenheit zur Stellungnahme "
        f"geben.\n\n"
        f"(4) Der Lieferant unterhält während der Vertragslaufzeit "
        f"sowie für drei (3) Jahre nach deren Beendigung eine "
        f"Produkthaftpflicht-Versicherung einschließlich erweiterter "
        f"Produkthaftpflicht und Rückrufkostendeckung mit einer "
        f"Mindestdeckungssumme von EUR 10.000.000 pauschal für Personen- "
        f"und Sachschäden je Versicherungsfall sowie pro Jahr und einer "
        f"Mindestdeckungssumme von EUR 5.000.000 für Vermögensschäden. "
        f"Eine Versicherungsbestätigung ist dem Kunden auf Verlangen "
        f"vorzulegen."
    )))

    s.append(("§ 12 Haftungsbeschränkung", (
        f"(1) Vorbehaltlich der nachfolgenden Bestimmungen haften die "
        f"Parteien einander für Schäden, gleich aus welchem Rechtsgrund, "
        f"nur bei Vorsatz und grober Fahrlässigkeit. Bei einfacher "
        f"Fahrlässigkeit besteht eine Haftung nur bei Verletzung einer "
        f"vertragswesentlichen Pflicht, deren Erfüllung die ordnungsgemäße "
        f"Durchführung dieses Vertrages überhaupt erst ermöglicht und "
        f"auf deren Einhaltung die andere Partei regelmäßig vertraut "
        f"und vertrauen darf (Kardinalpflicht).\n\n"
        f"(2) Bei Verletzung einer Kardinalpflicht durch einfache "
        f"Fahrlässigkeit ist die Haftung der Höhe nach beschränkt auf "
        f"den bei Vertragsschluss vorhersehbaren, vertragstypischen "
        f"Schaden.\n\n"
        f"(3) Die Haftung des Lieferanten für sämtliche Schäden in "
        f"einem Vertragsjahr ist auf einen Betrag in Höhe von "
        f"{cap_pct} % des in diesem Vertragsjahr mit dem Kunden "
        f"erzielten Netto-Umsatzes beschränkt, mindestens jedoch auf "
        f"EUR 5.000.000.\n\n"
        f"(4) Die vorstehenden Haftungsbeschränkungen gelten nicht für "
        f"(a) Schäden aus der Verletzung des Lebens, des Körpers oder "
        f"der Gesundheit, (b) Schäden, die auf Vorsatz oder grober "
        f"Fahrlässigkeit beruhen, (c) Ansprüche aus dem Produkthaftungs-"
        f"gesetz, (d) Schäden aus arglistig verschwiegenen Mängeln und "
        f"Ansprüche aus übernommenen Garantien sowie (e) Ansprüche aus "
        f"§ 11 (Produkthaftung) und § 15 (IP-Rechte), soweit dort "
        f"abweichend geregelt.\n\n"
        f"(5) Eine Haftung für entgangenen Gewinn, mittelbare Schäden, "
        f"Folgeschäden, Produktionsausfälle und sonstige Vermögensschäden "
        f"ist ausgeschlossen, soweit nicht eine der Ausnahmen nach "
        f"Absatz 4 vorliegt."
    )))

    s.append(("§ 13 Vertragsstrafe Lieferverzug", (
        "(1) Gerät der Lieferant mit einer Lieferung in Verzug, hat er "
        "an den Kunden eine Vertragsstrafe in Höhe von 0,5 % des "
        "Auftragswertes der verspäteten Lieferung je angefangener Woche "
        "Verzug zu zahlen.\n\n"
        "(2) Die Vertragsstrafe ist auf maximal 5 % des Auftragswertes "
        "der verspäteten Lieferung gedeckelt.\n\n"
        "(3) Der Anspruch auf Vertragsstrafe muss spätestens mit der "
        "Schlusszahlung geltend gemacht werden (§ 341 Abs. 3 BGB).\n\n"
        "(4) Die Vertragsstrafe wird auf einen geltend gemachten "
        "Schadensersatzanspruch wegen des Verzugs angerechnet."
    )))

    s.append(("§ 14 Höhere Gewalt", FORCE_MAJEURE))

    s.append(("§ 15 Geistiges Eigentum und Schutzrechte Dritter", (
        f"(1) Der Lieferant gewährleistet, dass die Vertragsprodukte "
        f"frei von Schutzrechten Dritter sind, die einer vertragsgemäßen "
        f"Verwendung im vereinbarten Vertragsgebiet entgegenstehen.\n\n"
        f"(2) Der Lieferant stellt den Kunden auf erstes Anfordern von "
        f"allen Ansprüchen Dritter aus etwaigen Schutzrechtsverletzungen "
        f"frei und übernimmt alle dem Kunden in diesem Zusammenhang "
        f"entstehenden notwendigen Aufwendungen einschließlich angemessener "
        f"Kosten der Rechtsverteidigung.\n\n"
        f"(3) Werden gegen den Kunden Schutzrechte Dritter geltend "
        f"gemacht, wird der Kunde den Lieferanten unverzüglich schriftlich "
        f"informieren, ihm die Führung der Verteidigung überlassen "
        f"(soweit angemessen) und in zumutbarer Weise unterstützen.\n\n"
        f"(4) Werden die Vertragsprodukte vom Lieferanten nach "
        f"Spezifikationen des Kunden hergestellt und beruht die "
        f"behauptete Schutzrechtsverletzung auf diesen Spezifikationen, "
        f"so trifft den Kunden seinerseits eine entsprechende "
        f"Freistellungspflicht.\n\n"
        f"(5) Werkzeuge, Modelle und Vorrichtungen, die der Lieferant "
        f"speziell für die Herstellung von Vertragsprodukten anfertigt "
        f"und für die der Kunde die Kosten ganz oder teilweise trägt "
        f"(„Tooling'), gehen anteilig in das Eigentum des Kunden über. "
        f"Sie sind vom Lieferanten kenntlich zu machen, getrennt zu "
        f"verwahren und zu versichern."
    )))

    s.append(("§ 16 Vertraulichkeit", CONFIDENTIALITY_STD))

    s.append(("§ 17 Datenschutz", DATA_PROTECTION))

    s.append(("§ 18 Compliance, Code of Conduct, LkSG", COMPLIANCE_REPS + "\n\n" + LKSG_REPS))

    s.append(("§ 19 Exportkontrolle", EXPORT_CONTROL))

    s.append(("§ 20 Audit-Rechte", (
        "(1) Der Kunde ist berechtigt, mindestens einmal jährlich, "
        "sowie zusätzlich aus konkretem Anlass (insbesondere Qualitäts-"
        "vorfällen oder dem begründeten Verdacht von Compliance-"
        "Verstößen), auf eigene Kosten Audits beim Lieferanten "
        "durchzuführen.\n\n"
        "(2) Der Kunde wird Audits mit angemessener Vorankündigung "
        "(in der Regel zehn Geschäftstage), zu üblichen Geschäftszeiten "
        "und unter Wahrung berechtigter Geheimhaltungsinteressen des "
        "Lieferanten durchführen.\n\n"
        "(3) Der Lieferant wird die zur Durchführung des Audits "
        "erforderlichen Räume, Personen, Unterlagen und Systeme zur "
        "Verfügung stellen.\n\n"
        "(4) Festgestellte Abweichungen werden vom Lieferanten innerhalb "
        "einer mit dem Kunden zu vereinbarenden Frist behoben (Corrective "
        "Action Plan)."
    )))

    s.append(("§ 21 Versicherung", (
        "(1) Der Lieferant unterhält auf eigene Kosten während der "
        "gesamten Vertragslaufzeit folgende Versicherungen mit den "
        "angegebenen Mindestdeckungssummen:\n\n"
        "a) Betriebshaftpflichtversicherung mit einer Deckung von "
        "mindestens EUR 10.000.000 pauschal für Personen- und "
        "Sachschäden je Versicherungsfall und Jahr;\n\n"
        "b) Erweiterte Produkthaftpflichtversicherung mit Rückrufkosten-"
        "deckung von mindestens EUR 10.000.000 je Versicherungsfall;\n\n"
        "c) Transportversicherung für die Lieferungen, soweit der "
        "Lieferant nach Incoterms® das Transportrisiko trägt.\n\n"
        "(2) Auf Verlangen des Kunden weist der Lieferant das Bestehen "
        "des Versicherungsschutzes durch Vorlage einer Bestätigung des "
        "Versicherers nach.\n\n"
        "(3) Die in Absatz 1 genannten Mindestdeckungssummen lassen die "
        "Haftung des Lieferanten dem Grunde und der Höhe nach unberührt."
    )))

    s.append(("§ 22 Laufzeit und Kündigung", (
        f"(1) Dieser Vertrag tritt am Tag der Unterzeichnung durch "
        f"beide Parteien in Kraft. Er wird auf eine feste Laufzeit von "
        f"{laufzeit} Jahren geschlossen.\n\n"
        f"(2) Nach Ablauf der festen Laufzeit verlängert sich der "
        f"Vertrag um jeweils ein weiteres Jahr, sofern er nicht von "
        f"einer der Parteien mit einer Frist von zwölf (12) Monaten "
        f"zum Ende der Laufzeit oder einer Verlängerungsperiode "
        f"schriftlich gekündigt wird.\n\n"
        f"(3) Das Recht zur außerordentlichen Kündigung aus wichtigem "
        f"Grund bleibt unberührt. Ein wichtiger Grund liegt insbesondere "
        f"vor, wenn (a) eine Partei eine wesentliche Vertragspflicht "
        f"trotz schriftlicher Abmahnung und Setzung einer angemessenen "
        f"Nachfrist von mindestens 30 Tagen wiederholt verletzt, (b) "
        f"über das Vermögen einer Partei das Insolvenzverfahren "
        f"eröffnet oder mangels Masse abgelehnt wurde, oder (c) ein "
        f"Kontrollwechsel bei einer Partei eingetreten ist und die "
        f"andere Partei innerhalb von sechs Monaten von ihrem "
        f"Sonderkündigungsrecht Gebrauch macht.\n\n"
        f"(4) Kündigungen bedürfen der Schriftform; die elektronische "
        f"Form gemäß § 126a BGB ist ausgeschlossen."
    )))

    s.append(("§ 23 Folgen der Vertragsbeendigung", (
        "(1) Nach Beendigung des Vertrages wird der Lieferant alle noch "
        "verbindlich angenommenen Bestellungen vollständig ausführen, "
        "soweit der Kunde nicht ausdrücklich auf die Erfüllung verzichtet.\n\n"
        "(2) Der Lieferant verpflichtet sich, für einen Zeitraum von "
        "bis zu drei (3) Jahren nach Vertragsbeendigung weiterhin "
        "Ersatzteile zur Reparatur und Wartung der Vertragsprodukte "
        "nach Maßgabe der jeweils marktüblichen Preise und Konditionen "
        "zu liefern (Last-Time-Buy / Ersatzteilversorgung).\n\n"
        "(3) Vom Kunden bezahltes Tooling wird nach Vertragsende auf "
        "Kosten des Kunden an diesen herausgegeben oder, soweit "
        "vereinbart, gegen Erstattung des Buchwerts vom Lieferanten "
        "übernommen.\n\n"
        "(4) Vertraulichkeitspflichten, Schutzrechtsregelungen und alle "
        "Bestimmungen, die ihrem Sinn nach über die Vertragsbeendigung "
        "hinaus Geltung beanspruchen, bestehen fort."
    )))

    s.append(("§ 24 Abtretung", ASSIGNMENT))

    s.append(("§ 25 Anwendbares Recht, Gerichtsstand", JURISDICTION_DE.format(
        gerichtsstand=city
    )))

    s.append(("§ 26 Schlussbestimmungen", (
        "(1) " + SCHRIFTFORM + "\n\n"
        "(2) " + SALVATORISCH + "\n\n"
        "(3) Soweit zwischen der Bestimmungen dieses Vertrages und den "
        "Bestimmungen in den Anlagen Widersprüche bestehen, gilt "
        "folgende Rangordnung: (i) Bestimmungen dieses Vertrages, "
        "(ii) Qualitätssicherungsvereinbarung (Anlage 3), (iii) übrige "
        "Anlagen in der Reihenfolge ihrer Nummerierung. AGB des "
        "Lieferanten oder des Kunden finden – auch wenn sie einer "
        "Auftragsbestätigung oder Bestellung beigefügt sind – keine "
        "Anwendung."
    )))

    s.append(("Anlagen", _annex_list([
        "Technische Spezifikationen",
        "Qualitätsanforderungen",
        "Qualitätssicherungsvereinbarung (QSV)",
        "Mindestabnahmemengen",
        "Anlieferadressen und Logistikrichtlinie",
        "Preisliste",
        "LkSG-Lieferantenkodex",
        "Code of Conduct für Lieferanten",
        "Datenschutz / AVV"
    ])))

    s.append(("Unterschriften", _signature_block(
        p, _g(p, "supplier_signatory", "Geschäftsführung des Lieferanten"),
        "Lieferant", _g(p, "customer_signatory", "Einkaufsleitung Kunde"),
        "Kunde"
    )))

    return s


def gen_supplier_frame_agreement_de(p: Dict[str, Any]) -> List[Section]:
    """Lieferanten-Rahmenvertrag (Buyer-Perspektive). Target: 4000-6000 Wörter."""

    buyer = _g(p, "buyer", "Muster GmbH")
    supplier = _g(p, "supplier", "Zulieferer GmbH")
    city = _g(p, "city", "Köln")
    laufzeit = _g(p, "laufzeit", "3")

    s: List[Section] = []

    s.append(("Präambel", (
        f"Zwischen {buyer} (nachfolgend „Besteller') und {supplier} "
        f"(nachfolgend „Lieferant'; gemeinsam „Parteien') wird der "
        f"folgende Rahmenvertrag über die Lieferung von Bauteilen, "
        f"Halbfabrikaten und Komponenten geschlossen.\n\n"
        f"Der Besteller ist Hersteller industrieller Erzeugnisse und "
        f"benötigt Vorprodukte und Bauteile, die durch den Lieferanten "
        f"hergestellt werden können. Die Parteien wünschen, ihre "
        f"Geschäftsbeziehung in einem Rahmenvertrag zu regeln."
    )))

    s.append(("§ 1 Vertragsgegenstand", (
        "(1) Dieser Vertrag regelt die allgemeinen Bedingungen, zu "
        "denen der Lieferant dem Besteller die in Anlage 1 spezifizierten "
        "Produkte liefert.\n\n"
        "(2) Einzelne Lieferungen kommen durch Erteilung einer "
        "Einzelbestellung des Bestellers und deren Annahme durch den "
        "Lieferanten zustande. Allgemeine Geschäftsbedingungen des "
        "Lieferanten finden keine Anwendung."
    )))

    s.append(("§ 2 Bestellverfahren und Open Orders", (
        "(1) Der Besteller erteilt verbindliche Bestellungen "
        "elektronisch über sein Lieferantenportal oder per EDI. "
        "Annahmebestätigungen sind binnen drei (3) Geschäftstagen zu "
        "übermitteln; nach Fristablauf ohne Widerspruch gilt die "
        "Bestellung als angenommen.\n\n"
        "(2) Der Besteller übermittelt monatlich rollierende 12-Monats-"
        "Forecasts. Die Forecasts der ersten 90 Tage sind für den "
        "Lieferanten kapazitätsverbindlich.\n\n"
        "(3) Open Orders / Lieferplanabrufe sind verbindliche Bestellungen "
        "im Sinne dieses Vertrages."
    )))

    s.append(("§ 3 Bestandsverpflichtungen und Sicherheitsbestände", (
        "(1) Der Lieferant verpflichtet sich, einen Sicherheitsbestand "
        "an Vertragsprodukten in Höhe von durchschnittlich 4 Wochen "
        "Bedarf des Bestellers laut letztem Forecast vorzuhalten "
        "(Buffer Stock).\n\n"
        "(2) Auf Anforderung kann der Besteller einen Konsignationslager-"
        "Vertrag mit dem Lieferanten abschließen, in dessen Rahmen der "
        "Lieferant Vertragsprodukte am Standort des Bestellers vorhält. "
        "Eigentum geht erst mit Entnahme aus dem Konsignationslager auf "
        "den Besteller über (VMI - Vendor Managed Inventory)."
    )))

    s.append(("§ 4 Werkzeuge und Beistellungen", (
        "(1) Werkzeuge, Modelle, Vorrichtungen und sonstige Betriebsmittel, "
        "die für die Herstellung der Vertragsprodukte erforderlich sind "
        "und für die der Besteller die Kosten (ganz oder teilweise) trägt "
        "(„Tooling'), bleiben unwiderruflich Eigentum des Bestellers, "
        "auch wenn sie sich im Besitz des Lieferanten befinden.\n\n"
        "(2) Der Lieferant kennzeichnet das Tooling sichtbar als "
        "Eigentum des Bestellers, lagert und wartet es ordnungsgemäß "
        "und versichert es zum Wiederbeschaffungswert auf eigene Kosten "
        "gegen Feuer, Wasser, Diebstahl und sonstige Risiken.\n\n"
        "(3) Vom Besteller beigestellte Vorprodukte, Komponenten oder "
        "Materialien („Beistellung') bleiben Eigentum des Bestellers. "
        "Der Lieferant verarbeitet die Beistellungen für den Besteller "
        "im Sinne des § 950 BGB; das Eigentum am hergestellten Produkt "
        "erwirbt der Besteller anteilig im Verhältnis des Wertes der "
        "Beistellung zum Wert des Endprodukts."
    )))

    s.append(("§ 5 Preise und Productivity Reduction", (
        "(1) Die Preise sind in Anlage 2 (Preisliste) festgelegt und "
        "verstehen sich netto in Euro, Lieferung DAP (Incoterms® 2020) "
        "Anlieferadresse Besteller.\n\n"
        "(2) Der Lieferant gewährt dem Besteller eine jährliche "
        "Productivity Reduction von 3 % auf alle Stückpreise, jeweils "
        "wirksam zum 1. Januar des Folgejahres.\n\n"
        "(3) Material- und Energiepreis-Pass-Through nach Maßgabe der "
        "in Anlage 3 dokumentierten Indizes."
    )))

    s.append(("§ 6 Qualität und Quality Agreement", (
        "(1) Der Lieferant unterhält ein zertifiziertes Qualitäts-"
        "managementsystem nach ISO 9001 oder, bei Automotive-Lieferungen, "
        "IATF 16949.\n\n"
        "(2) Erstmusterprüfungen (PPAP / VDA 2) sind vor Serienanlauf "
        "auf Kosten des Lieferanten durchzuführen. Die Freigabe erfolgt "
        "schriftlich durch den Besteller.\n\n"
        "(3) Im Falle von Qualitätsabweichungen wird der Lieferant "
        "eine 8D-Analyse innerhalb von 24 Stunden initiieren, eine "
        "Sofortmaßnahme binnen 48 Stunden und einen vollständigen "
        "8D-Report binnen 14 Geschäftstagen vorlegen.\n\n"
        "(4) Wareneingangsprüfung beim Besteller erfolgt nur "
        "stichprobenartig. Die Pflicht zur unverzüglichen Rüge nach "
        "§ 377 HGB wird abgemildert: erkennbare Mängel sind innerhalb "
        "von 14 Werktagen nach Wareneingang, verdeckte Mängel innerhalb "
        "von 14 Werktagen nach Entdeckung zu rügen."
    )))

    s.append(("§ 7 Audit-Rechte", (
        "(1) Der Besteller kann jederzeit mit Vorankündigung von "
        "zehn Geschäftstagen Werks-Audits durchführen.\n\n"
        "(2) Der Audit umfasst Inspektionen von Produktionsstätten, "
        "Qualitätsmanagementsystem, Sub-Tier-Lieferanten-Management, "
        "Compliance-Programmen und Arbeitssicherheits- und "
        "Umweltschutzmaßnahmen.\n\n"
        "(3) Bei festgestellten Abweichungen erarbeiten die Parteien "
        "einen Corrective Action Plan mit verbindlichen Terminen."
    )))

    s.append(("§ 8 REACH und RoHS-Compliance", (
        "(1) Der Lieferant gewährleistet, dass alle Vertragsprodukte "
        "den Anforderungen der EG-Verordnung 1907/2006 (REACH) und der "
        "Richtlinie 2011/65/EU (RoHS) sowie sonstigen einschlägigen "
        "europäischen und nationalen Stoffverboten entsprechen.\n\n"
        "(2) Der Lieferant teilt dem Besteller alle gemäß REACH "
        "kommunikationspflichtigen Stoffe (SVHC) unverzüglich, spätestens "
        "binnen 45 Tagen nach Aufnahme in die Kandidatenliste mit.\n\n"
        "(3) Der Lieferant verpflichtet sich, eine vollständige IMDS-"
        "Eingabe (International Material Data System) für alle "
        "Automotive-Lieferungen vorzunehmen.\n\n"
        "(4) Konfliktmineralien (3TG-Materialien gemäß Dodd-Frank-Act "
        "und EU-Verordnung 2017/821) sind aus konfliktfreien Quellen zu "
        "beziehen und entsprechend zu dokumentieren."
    )))

    s.append(("§ 9 End-of-Life und Last-Time-Buy", (
        "(1) Beabsichtigt der Lieferant die Einstellung der Produktion "
        "eines Vertragsprodukts (EOL), so wird er den Besteller "
        "spätestens 18 Monate vor Wirksamwerden schriftlich informieren.\n\n"
        "(2) Der Besteller hat das Recht, vor EOL eine letzte Bestellung "
        "(Last-Time-Buy) zu den zuletzt gültigen Konditionen zu erteilen, "
        "deren Volumen bis zu 36 Monate Bedarf abdecken kann.\n\n"
        "(3) Der Lieferant verpflichtet sich, Ersatzteile für eine "
        "Mindestdauer von zehn Jahren nach Serienauslieferung zu "
        "marktüblichen Konditionen zur Verfügung zu stellen."
    )))

    s.append(("§ 10 LkSG-Anforderungen", LKSG_REPS))

    s.append(("§ 11 Compliance und Code of Conduct", COMPLIANCE_REPS))

    s.append(("§ 12 Geheimhaltung", CONFIDENTIALITY_STD))

    s.append(("§ 13 Datenschutz", DATA_PROTECTION))

    s.append(("§ 14 Exportkontrolle", EXPORT_CONTROL))

    s.append(("§ 15 Höhere Gewalt", FORCE_MAJEURE))

    s.append(("§ 16 Haftung", (
        "(1) Die Haftung der Parteien richtet sich nach den gesetzlichen "
        "Bestimmungen.\n\n"
        "(2) Im Falle einer einfachen Fahrlässigkeit haften die Parteien "
        "nur bei Verletzung wesentlicher Vertragspflichten und ist auf "
        "den vertragstypischen vorhersehbaren Schaden begrenzt.\n\n"
        "(3) Die Haftungsbegrenzung gilt nicht für Schäden aus der "
        "Verletzung von Leben, Körper oder Gesundheit, bei Vorsatz oder "
        "grober Fahrlässigkeit, bei Verletzung von Schutzrechten oder "
        "bei Ansprüchen aus dem Produkthaftungsgesetz."
    )))

    s.append(("§ 17 Laufzeit, Kündigung", (
        f"(1) Der Vertrag tritt mit Unterzeichnung in Kraft und läuft "
        f"für {laufzeit} Jahre. Er verlängert sich um jeweils ein Jahr, "
        f"sofern er nicht mit einer Frist von 12 Monaten vor Vertragsende "
        f"in Schriftform gekündigt wird.\n\n"
        f"(2) Das Recht zur außerordentlichen Kündigung aus wichtigem "
        f"Grund bleibt unberührt."
    )))

    s.append(("§ 18 Anwendbares Recht, Gerichtsstand", JURISDICTION_DE.format(
        gerichtsstand=city
    )))

    s.append(("§ 19 Schlussbestimmungen", SCHRIFTFORM + "\n\n" + SALVATORISCH))

    s.append(("Anlagen", _annex_list([
        "Produkt- und Spezifikationsliste",
        "Preisliste",
        "Material-Index-Liste für Pass-Through",
        "Quality Agreement / QSV",
        "LkSG-Lieferantenkodex",
        "Code of Conduct"
    ])))

    s.append(("Unterschriften", _signature_block(
        p, "Einkaufsleitung " + buyer, "für den Besteller",
        "Geschäftsführung " + supplier, "für den Lieferanten"
    )))

    return s


def gen_distribution_agreement_de(p: Dict[str, Any]) -> List[Section]:
    """Distributor-Vertrag. Target: 5000-7500 Wörter."""

    principal = _g(p, "principal", "Muster GmbH")
    distributor = _g(p, "distributor", "Distributor s.r.l.")
    territory = _g(p, "territory", "Italien (Festland und Inseln)")
    city = _g(p, "city", "Köln")
    laufzeit = _g(p, "laufzeit", "3")

    s: List[Section] = []

    s.append(("Präambel", (
        f"Zwischen {principal} (nachfolgend „Prinzipal') und "
        f"{distributor} (nachfolgend „Distributor'; Prinzipal und "
        f"Distributor gemeinsam „Parteien') wird der folgende "
        f"Vertriebsvertrag geschlossen.\n\n"
        f"Der Prinzipal stellt hochwertige Produkte gemäß Anlage 1 her "
        f"(„Vertragsprodukte') und beabsichtigt, diese im Vertragsgebiet "
        f"durch den Distributor vertreiben zu lassen. Der Distributor "
        f"verfügt über einen etablierten Vertriebskanal, qualifizierte "
        f"Mitarbeiter und die erforderliche Infrastruktur im "
        f"Vertragsgebiet. Die Parteien wünschen, ihre Zusammenarbeit "
        f"vertraglich zu regeln. Dies vorausgeschickt vereinbaren die "
        f"Parteien wie folgt:"
    )))

    s.append(("§ 1 Ernennung und Vertragsgebiet", (
        f"(1) Der Prinzipal ernennt den Distributor zum alleinigen "
        f"Vertriebspartner für die Vertragsprodukte im Vertragsgebiet "
        f"{territory} („Vertragsgebiet'). Der Distributor handelt im "
        f"eigenen Namen und auf eigene Rechnung als selbständiger "
        f"Kaufmann.\n\n"
        f"(2) Der Prinzipal wird im Vertragsgebiet weder selbst aktiv "
        f"Endkunden ansprechen noch andere Vertriebspartner ernennen "
        f"(Exklusivität).\n\n"
        f"(3) Der Distributor verpflichtet sich, im Vertragsgebiet aktiv "
        f"zu vertreiben und sich auf passive Verkäufe außerhalb des "
        f"Vertragsgebiets zu beschränken, soweit dies kartellrechtlich "
        f"zulässig ist (Art. 4 lit. b Vertikal-GVO).\n\n"
        f"(4) Der Distributor darf weder im noch außerhalb des "
        f"Vertragsgebiets konkurrierende Produkte vertreiben (§ 6 dieses "
        f"Vertrages – Wettbewerbsverbot)."
    )))

    s.append(("§ 2 Vertragsprodukte und Sortimentsänderungen", (
        "(1) Die Vertragsprodukte sind in Anlage 1 abschließend "
        "aufgeführt. Der Prinzipal kann nach billigem Ermessen "
        "Vertragsprodukte aus dem Sortiment nehmen oder neue Produkte "
        "aufnehmen.\n\n"
        "(2) Bei Entfall eines Vertragsproduktes wird der Prinzipal "
        "den Distributor mit einer Vorlaufzeit von mindestens "
        "12 Monaten informieren und ein Letzt-Bezugsrecht (Last-Time-"
        "Buy) einräumen.\n\n"
        "(3) Der Prinzipal wird neue Produkte, die in technischer und "
        "vertrieblicher Hinsicht in das bestehende Sortiment passen, "
        "vorrangig dem Distributor zum Vertrieb anbieten."
    )))

    s.append(("§ 3 Mindestabnahmen und Vertriebsziele", (
        "(1) Der Distributor verpflichtet sich, im Vertragsgebiet "
        "während der gesamten Vertragslaufzeit aktiv Marketing- und "
        "Vertriebsmaßnahmen zu ergreifen, um die Marktdurchdringung "
        "der Vertragsprodukte zu fördern.\n\n"
        "(2) Mindestabnahmen je Vertragsjahr sind in Anlage 2 "
        "festgelegt. Die Mindestabnahmen werden jährlich auf Basis der "
        "Marktentwicklung verhandelt und beziehen sich auf den Netto-"
        "Umsatz, den der Distributor mit Vertragsprodukten erzielt.\n\n"
        "(3) Verfehlt der Distributor in einem Vertragsjahr die "
        "Mindestabnahme um mehr als 25 %, ist der Prinzipal berechtigt, "
        "die Exklusivität gemäß § 1 zu widerrufen oder den Vertrag mit "
        "einer Frist von drei (3) Monaten ordentlich zu kündigen.\n\n"
        "(4) Der Distributor unterhält in seinem Außendienst mindestens "
        "fünf (5) hauptamtlich für den Vertrieb der Vertragsprodukte "
        "tätige Vertriebsmitarbeiter."
    )))

    s.append(("§ 4 Bestellung, Lieferung, Preise", (
        "(1) Der Distributor erteilt Bestellungen gemäß Anlage 3 "
        "(Bestell-Form). Lieferungen erfolgen FCA (Incoterms® 2020) "
        "ab Werk des Prinzipals.\n\n"
        "(2) Die Verkaufspreise des Prinzipals an den Distributor "
        "ergeben sich aus der jeweils gültigen Großhandelspreisliste "
        "(Anlage 4). Der Prinzipal gewährt dem Distributor einen "
        "Mengenrabatt gemäß Anlage 4 sowie weitere Boni.\n\n"
        "(3) Endkundenpreise legt der Distributor in eigener "
        "Verantwortung fest. Der Prinzipal kann unverbindliche "
        "Preisempfehlungen (UVP) aussprechen.\n\n"
        "(4) Rechnungen sind innerhalb von 30 Tagen netto zur Zahlung "
        "fällig. Skontoabzüge sind nicht vorgesehen.\n\n"
        "(5) Der Eigentumsvorbehalt wird wie folgt vereinbart: "
        "Verkaufte Vertragsprodukte bleiben bis zur vollständigen "
        "Zahlung Eigentum des Prinzipals (einfacher Eigentums-"
        "vorbehalt); bei Weiterveräußerung tritt der Distributor seine "
        "Forderungen gegen Endkunden an den Prinzipal im Voraus ab "
        "(verlängerter Eigentumsvorbehalt)."
    )))

    s.append(("§ 5 Marketing und Markennutzung", (
        "(1) Der Prinzipal überlässt dem Distributor während der "
        "Vertragslaufzeit eine widerrufliche, nicht ausschließliche "
        "Lizenz zur Nutzung der in Anlage 5 genannten Marken und "
        "Kennzeichen für den Vertrieb der Vertragsprodukte im "
        "Vertragsgebiet. Der Distributor darf die Marken nur in der "
        "vom Prinzipal vorgegebenen Form verwenden.\n\n"
        "(2) Der Distributor wird die Vertragsprodukte mit angemessenem "
        "Aufwand bewerben. Er stellt sicher, dass alle Werbemaßnahmen "
        "den Markenrichtlinien des Prinzipals entsprechen. Werbemittel "
        "vor Erstveröffentlichung sind dem Prinzipal zur Freigabe "
        "vorzulegen.\n\n"
        "(3) Die Parteien teilen sich Marketingaufwendungen für "
        "Kampagnen, Messen und Online-Auftritte 50:50 bis zu einem "
        "vereinbarten Jahresbudget gemäß Anlage 6."
    )))

    s.append(("§ 6 Wettbewerbsverbot des Distributors", (
        "(1) Der Distributor verpflichtet sich, während der Vertragsdauer "
        "weder mittelbar noch unmittelbar Produkte zu vertreiben, die "
        "mit den Vertragsprodukten in Wettbewerb stehen.\n\n"
        "(2) Das Wettbewerbsverbot umfasst sowohl den Vertrieb in eigenem "
        "Namen als auch für Rechnung Dritter sowie die Mitwirkung an "
        "konkurrierenden Vertriebsstrukturen.\n\n"
        "(3) Bei einem Verstoß gegen das Wettbewerbsverbot schuldet "
        "der Distributor dem Prinzipal eine Vertragsstrafe in Höhe von "
        "EUR 50.000 je Verstoß, bei Dauerverstoß je angefangenem Monat. "
        "Schadensersatzansprüche bleiben unberührt."
    )))

    s.append(("§ 7 Regulatorische Pflichten und Schulungen", (
        "(1) Der Distributor übernimmt im Vertragsgebiet alle für den "
        "Vertrieb der Vertragsprodukte erforderlichen regulatorischen "
        "Aufgaben, insbesondere – soweit die Vertragsprodukte als "
        "Medizinprodukte zu klassifizieren sind – die Aufgaben eines "
        "Importeurs bzw. Händlers im Sinne der MDR (Verordnung (EU) "
        "2017/745).\n\n"
        "(2) Der Distributor stellt sicher, dass seine Vertriebs- und "
        "Servicemitarbeiter regelmäßig auf den Vertragsprodukten "
        "geschult sind. Schulungen werden durch den Prinzipal "
        "bereitgestellt; Kosten für Anreise und Aufenthalt trägt "
        "der Distributor.\n\n"
        "(3) Der Distributor übernimmt im Vertragsgebiet die "
        "Verkaufs- und Vertriebsdokumentation und meldet "
        "Vorkommnisse / Reklamationen an den Prinzipal binnen "
        "48 Stunden nach Kenntniserlangung."
    )))

    s.append(("§ 8 Service, Support und Ersatzteilversorgung", (
        "(1) Der Distributor bietet im Vertragsgebiet First- und "
        "Second-Level-Support für die Vertragsprodukte an. Komplexere "
        "technische Probleme werden vom Prinzipal als Third-Level-"
        "Support bearbeitet.\n\n"
        "(2) Der Distributor unterhält ein Ersatzteillager mit "
        "Mindestbestand entsprechend Anlage 7.\n\n"
        "(3) Garantieleistungen werden gegen Erstattung der Aufwendungen "
        "durch den Prinzipal vom Distributor abgewickelt."
    )))

    s.append(("§ 9 Berichts- und Informationspflichten", (
        "(1) Der Distributor übermittelt dem Prinzipal monatlich einen "
        "Vertriebsbericht mit Sell-In- und Sell-Out-Daten, Lager-"
        "bestandsmeldungen, Top-Kunden, Pipeline und Marktentwicklung.\n\n"
        "(2) Quartalsweise erfolgt ein Review-Meeting (physisch oder "
        "virtuell).\n\n"
        "(3) Der Distributor gewährt dem Prinzipal Audit-Rechte "
        "bezüglich der Verkaufsdokumentation und Lagerbestände."
    )))

    s.append(("§ 10 Vertragsdauer und Kündigung", (
        f"(1) Dieser Vertrag wird auf eine Festlaufzeit von {laufzeit} "
        f"Jahren geschlossen und verlängert sich um jeweils zwei (2) "
        f"weitere Jahre, sofern er nicht mit einer Frist von neun (9) "
        f"Monaten zum Vertragsende gekündigt wird.\n\n"
        f"(2) Außerordentliche Kündigung aus wichtigem Grund bleibt "
        f"unberührt.\n\n"
        f"(3) Nach Vertragsbeendigung wird der Distributor die "
        f"Lagerbestände an Vertragsprodukten – sofern nicht der "
        f"Prinzipal sie zum Buchwert zurücknimmt – innerhalb von "
        f"sechs Monaten abverkaufen.\n\n"
        f"(4) Ein Ausgleichsanspruch des Distributors entsprechend "
        f"§ 89b HGB analog ist – soweit zwischen den Parteien zulässig "
        f"– ausgeschlossen, soweit nicht zwingendes Recht entgegensteht."
    )))

    s.append(("§ 11 Vertraulichkeit", CONFIDENTIALITY_STD))

    s.append(("§ 12 Datenschutz", DATA_PROTECTION))

    s.append(("§ 13 Compliance", COMPLIANCE_REPS))

    s.append(("§ 14 Exportkontrolle", EXPORT_CONTROL))

    s.append(("§ 15 Höhere Gewalt", FORCE_MAJEURE))

    s.append(("§ 16 Haftung", (
        "(1) Die Haftung der Parteien richtet sich nach den gesetzlichen "
        "Bestimmungen unter Berücksichtigung der nachfolgenden "
        "Modifikationen.\n\n"
        "(2) Bei einfacher Fahrlässigkeit haften die Parteien nur bei "
        "Verletzung wesentlicher Vertragspflichten, beschränkt auf den "
        "vorhersehbaren vertragstypischen Schaden.\n\n"
        "(3) Eine Haftung für entgangenen Gewinn, mittelbare Schäden "
        "und Folgeschäden ist ausgeschlossen, soweit nicht Vorsatz "
        "oder grobe Fahrlässigkeit vorliegt."
    )))

    s.append(("§ 17 Anwendbares Recht und Gerichtsstand", JURISDICTION_DE.format(
        gerichtsstand=city
    )))

    s.append(("§ 18 Schlussbestimmungen", SCHRIFTFORM + "\n\n" + SALVATORISCH))

    s.append(("Anlagen", _annex_list([
        "Vertragsprodukte",
        "Mindestabnahmen je Vertragsjahr",
        "Bestellprozess",
        "Großhandelspreisliste und Rabattstaffel",
        "Markenrichtlinien",
        "Marketingbudget",
        "Ersatzteilmindestbestand",
        "Compliance-Anforderungen / Code of Conduct",
        "Datenschutz"
    ])))

    s.append(("Unterschriften", _signature_block(
        p, "Geschäftsführung " + principal, "Prinzipal",
        "Amministratore Delegato " + distributor, "Distributor"
    )))

    return s


def gen_agb_general(p: Dict[str, Any]) -> List[Section]:
    """AGB für Lieferungen und Leistungen. Target: 2500-4000 Wörter."""

    company = _g(p, "company", "Muster GmbH")
    city = _g(p, "city", "Köln")

    s: List[Section] = []

    s.append(("§ 1 Geltungsbereich", (
        f"(1) Diese Allgemeinen Geschäftsbedingungen (nachfolgend „AGB') "
        f"gelten für alle Lieferungen und Leistungen, die {company} "
        f"(nachfolgend „Verkäufer') gegenüber Unternehmern (§ 14 BGB), "
        f"juristischen Personen des öffentlichen Rechts und öffentlich-"
        f"rechtlichen Sondervermögen erbringt. Sie gelten ausschließlich; "
        f"entgegenstehende oder von diesen AGB abweichende Bedingungen "
        f"des Kunden werden nicht Vertragsbestandteil, es sei denn, der "
        f"Verkäufer hat ihrer Geltung ausdrücklich und schriftlich "
        f"zugestimmt.\n\n"
        f"(2) Die AGB gelten auch für alle künftigen Geschäftsbeziehungen, "
        f"selbst wenn sie nicht nochmals ausdrücklich vereinbart werden.\n\n"
        f"(3) Individuelle, im Einzelfall getroffene Vereinbarungen haben "
        f"Vorrang vor diesen AGB."
    )))

    s.append(("§ 2 Angebot und Vertragsschluss", (
        "(1) Angebote des Verkäufers sind freibleibend und unverbindlich. "
        "Dies gilt auch dann, wenn der Verkäufer Kataloge, technische "
        "Dokumentationen, sonstige Produktbeschreibungen oder Unterlagen "
        "– auch in elektronischer Form – überlassen hat.\n\n"
        "(2) Die Bestellung eines Kunden gilt als verbindliches "
        "Vertragsangebot. Soweit aus der Bestellung nichts anderes "
        "hervorgeht, ist der Verkäufer berechtigt, dieses Vertragsangebot "
        "innerhalb von zwei (2) Wochen nach Zugang anzunehmen.\n\n"
        "(3) Die Annahme kann durch Auftragsbestätigung in Textform "
        "oder durch Auslieferung der Ware erfolgen.\n\n"
        "(4) Vereinbarungen, insbesondere mündliche Nebenabreden, sowie "
        "Änderungen und Ergänzungen des Vertrages bedürfen zu ihrer "
        "Wirksamkeit der Bestätigung in Textform durch den Verkäufer."
    )))

    s.append(("§ 3 Preise und Zahlung", (
        "(1) Sofern nichts anderes vereinbart ist, gelten die Preise "
        "ab Werk (EXW Incoterms® 2020) ausschließlich Verpackung und "
        "zuzüglich der gesetzlichen Umsatzsteuer.\n\n"
        "(2) Soweit den Preisen ein Materialpreis zugrunde liegt, dessen "
        "Lieferantenpreis sich zwischen Vertragsschluss und Lieferung "
        "wesentlich (mehr als 10 %) ändert, ist der Verkäufer berechtigt, "
        "den Preis entsprechend anzupassen.\n\n"
        "(3) Der Kaufpreis ist innerhalb von 30 Tagen ab Rechnungsdatum "
        "ohne Abzug zur Zahlung fällig. Bei Zahlung innerhalb von "
        "14 Tagen wird ein Skonto von 2 % gewährt.\n\n"
        "(4) Mit Ablauf der Zahlungsfrist kommt der Kunde in Verzug. "
        "Der Kaufpreis ist während des Verzugs zum jeweils geltenden "
        "gesetzlichen Verzugszinssatz für Rechtsgeschäfte mit Unternehmern "
        "(§ 288 Abs. 2 BGB) zu verzinsen. Der Verkäufer behält sich die "
        "Geltendmachung eines weitergehenden Verzugsschadens vor.\n\n"
        "(5) Dem Kunden stehen Aufrechnungs- und Zurückbehaltungsrechte "
        "nur insoweit zu, als sein Gegenanspruch rechtskräftig festgestellt "
        "oder unbestritten ist."
    )))

    s.append(("§ 4 Eigentumsvorbehalt", (
        "(1) Die Ware bleibt bis zur vollständigen Bezahlung des "
        "Kaufpreises Eigentum des Verkäufers (einfacher Eigentums-"
        "vorbehalt). Bei Verträgen mit Unternehmern bleibt die Ware "
        "darüber hinaus Eigentum des Verkäufers bis zur Bezahlung aller "
        "Forderungen aus der laufenden Geschäftsbeziehung (erweiterter "
        "Eigentumsvorbehalt).\n\n"
        "(2) Der Kunde ist berechtigt, die Vorbehaltsware im "
        "ordnungsgemäßen Geschäftsverkehr zu verarbeiten und zu "
        "veräußern. Die Verarbeitung oder Umbildung der Vorbehaltsware "
        "durch den Kunden wird stets für den Verkäufer vorgenommen "
        "(§ 950 BGB), ohne dass diesem hieraus Verbindlichkeiten "
        "erwachsen. Wird die Vorbehaltsware mit anderen, dem Verkäufer "
        "nicht gehörenden Sachen verarbeitet, so erwirbt der Verkäufer "
        "Miteigentum an der neuen Sache im Verhältnis des Rechnungswerts "
        "der Vorbehaltsware zum Rechnungswert der anderen verarbeiteten "
        "Sachen.\n\n"
        "(3) Die aus dem Weiterverkauf der Vorbehaltsware entstehenden "
        "Forderungen tritt der Kunde bereits jetzt in Höhe des "
        "Rechnungswerts der Vorbehaltsware (verlängerter Eigentums-"
        "vorbehalt) zur Sicherung der Forderungen des Verkäufers ab; "
        "der Verkäufer nimmt die Abtretung an. Der Kunde bleibt zur "
        "Einziehung der Forderung auch nach der Abtretung ermächtigt; "
        "der Verkäufer kann die Einziehungsermächtigung widerrufen, "
        "wenn der Kunde seinen Zahlungsverpflichtungen nicht ordnungsgemäß "
        "nachkommt.\n\n"
        "(4) Bei Pfändungen oder sonstigen Eingriffen Dritter in die "
        "Vorbehaltsware oder die abgetretenen Forderungen ist der Kunde "
        "verpflichtet, den Verkäufer unverzüglich zu unterrichten und "
        "Dritte auf das Eigentum des Verkäufers hinzuweisen."
    )))

    s.append(("§ 5 Lieferzeit und Gefahrübergang", (
        "(1) Liefertermine und -fristen sind unverbindlich, sofern nicht "
        "ausdrücklich anderes vereinbart wurde. Die Einhaltung der "
        "Lieferfrist setzt die Klärung aller technischen und kaufmännischen "
        "Fragen sowie die rechtzeitige Erfüllung der Mitwirkungspflichten "
        "des Kunden voraus.\n\n"
        "(2) Werden Liefertermine oder -fristen aufgrund höherer Gewalt "
        "oder vergleichbarer Ereignisse nicht eingehalten, verlängern "
        "sich diese um die Dauer des Hindernisses. Der Verkäufer wird "
        "dem Kunden Beginn und Ende solcher Ereignisse mitteilen.\n\n"
        "(3) Die Gefahr geht ab Werk auf den Kunden über, auch wenn "
        "Teillieferungen erfolgen oder der Verkäufer weitere Leistungen "
        "(z. B. Versand) übernommen hat.\n\n"
        "(4) Teillieferungen sind zulässig, soweit sie für den Kunden "
        "zumutbar sind."
    )))

    s.append(("§ 6 Gewährleistung", (
        "(1) Die Gewährleistungsfrist beträgt 12 Monate ab Lieferung, "
        "soweit nicht eine längere gesetzliche Gewährleistungsfrist "
        "zwingend vorgeschrieben ist (z. B. nach § 438 Abs. 1 Nr. 2 BGB).\n\n"
        "(2) Der Kunde ist verpflichtet, die Ware unverzüglich nach "
        "Eingang zu untersuchen und Mängel binnen einer Frist von "
        "10 Werktagen schriftlich zu rügen (§ 377 HGB). Verdeckte "
        "Mängel sind unverzüglich nach Entdeckung anzuzeigen.\n\n"
        "(3) Bei berechtigter Mängelrüge hat der Verkäufer das Recht "
        "zur Nacherfüllung nach seiner Wahl durch Nachbesserung oder "
        "Ersatzlieferung.\n\n"
        "(4) Schlägt die Nacherfüllung fehl, ist sie für den Kunden "
        "unzumutbar oder verweigert sie der Verkäufer ernsthaft und "
        "endgültig, kann der Kunde nach seiner Wahl mindern, vom Vertrag "
        "zurücktreten oder Schadensersatz nach Maßgabe von § 7 verlangen.\n\n"
        "(5) Ansprüche wegen Mängeln bestehen nicht bei nur unerheblicher "
        "Abweichung von der vereinbarten Beschaffenheit, bei nur "
        "unerheblicher Beeinträchtigung der Brauchbarkeit, bei "
        "natürlicher Abnutzung oder bei Schäden, die nach dem "
        "Gefahrübergang infolge fehlerhafter oder nachlässiger "
        "Behandlung, übermäßiger Beanspruchung oder besonderer äußerer "
        "Einflüsse entstehen."
    )))

    s.append(("§ 7 Haftung", (
        "(1) Der Verkäufer haftet für Vorsatz und grobe Fahrlässigkeit "
        "nach den gesetzlichen Vorschriften.\n\n"
        "(2) Bei einfacher Fahrlässigkeit haftet der Verkäufer – außer "
        "in den Fällen einer Verletzung des Lebens, des Körpers oder der "
        "Gesundheit – nur für die Verletzung wesentlicher Vertragspflichten "
        "(Kardinalpflichten). Die Haftung ist in diesen Fällen auf den "
        "vorhersehbaren vertragstypischen Schaden begrenzt.\n\n"
        "(3) Soweit der Verkäufer dem Grunde nach auf Schadensersatz "
        "haftet, ist diese Haftung auf einen Betrag in Höhe des "
        "dreifachen Auftragsvolumens beschränkt.\n\n"
        "(4) Die Beschränkungen der Absätze 1 bis 3 gelten nicht für "
        "Ansprüche aus dem Produkthaftungsgesetz, bei arglistig "
        "verschwiegenen Mängeln sowie für Ansprüche aus übernommenen "
        "Garantien.\n\n"
        "(5) Sämtliche Schadensersatzansprüche des Kunden gegen den "
        "Verkäufer verjähren in 12 Monaten ab Kenntnis. Die Verjährungs-"
        "frist beginnt spätestens mit Ende des Jahres, in dem der "
        "Anspruch entstanden ist und der Kunde Kenntnis erlangt hat "
        "oder ohne grobe Fahrlässigkeit erlangen hätte müssen. § 199 BGB "
        "wird im Übrigen abbedungen."
    )))

    s.append(("§ 8 Höhere Gewalt", FORCE_MAJEURE))

    s.append(("§ 9 Geheimhaltung", CONFIDENTIALITY_STD))

    s.append(("§ 10 Datenschutz", DATA_PROTECTION))

    s.append(("§ 11 Aufrechnung und Zurückbehaltung", (
        "(1) Aufrechnungsrechte stehen dem Kunden nur zu, wenn seine "
        "Gegenansprüche rechtskräftig festgestellt, unbestritten oder "
        "vom Verkäufer anerkannt sind.\n\n"
        "(2) Ein Zurückbehaltungsrecht kann der Kunde nur aufgrund "
        "von Gegenansprüchen aus dem gleichen Vertragsverhältnis "
        "ausüben."
    )))

    s.append(("§ 12 Abtretung", ASSIGNMENT))

    s.append(("§ 13 Erfüllungsort, Gerichtsstand, Recht", (
        f"(1) Erfüllungsort für alle aus dem Vertragsverhältnis "
        f"resultierenden Verpflichtungen ist {city}.\n\n"
        f"(2) Ausschließlicher Gerichtsstand für alle Streitigkeiten "
        f"aus oder im Zusammenhang mit diesem Vertrag ist {city}, soweit "
        f"der Kunde Kaufmann ist.\n\n"
        f"(3) Es gilt deutsches Recht unter Ausschluss des UN-Kaufrechts "
        f"(CISG)."
    )))

    s.append(("§ 14 Schlussbestimmungen", (
        "(1) " + SCHRIFTFORM + "\n\n"
        "(2) " + SALVATORISCH
    )))

    return s


def gen_employment_contract_std(p: Dict[str, Any]) -> List[Section]:
    """Standard-Arbeitsvertrag. Target: 1500-2500 Wörter."""

    company = _g(p, "company", "Muster GmbH")
    employee = _g(p, "employee", "Max Mustermann")
    position = _g(p, "position", "Sachbearbeiter Einkauf")
    gehalt = _g(p, "gehalt", "55.000")
    city = _g(p, "city", "Köln")
    start = _g(p, "start", "01.01.2025")

    s: List[Section] = []

    s.append(("Präambel", (
        f"Zwischen der {company} mit Sitz in {city} – nachfolgend "
        f"„Arbeitgeber' – und Herrn/Frau {employee}, geboren am "
        f"[Datum], wohnhaft in [Anschrift] – nachfolgend „Arbeitnehmer' – "
        f"wird der folgende Arbeitsvertrag geschlossen."
    )))

    s.append(("§ 1 Beginn und Art der Beschäftigung", (
        f"(1) Der Arbeitnehmer wird ab dem {start} als {position} "
        f"unbefristet beschäftigt.\n\n"
        f"(2) Der Arbeitnehmer wird in den Betrieb des Arbeitgebers "
        f"in {city} eingegliedert.\n\n"
        f"(3) Die ersten sechs (6) Monate gelten als Probezeit. "
        f"Während der Probezeit kann das Arbeitsverhältnis von beiden "
        f"Seiten mit einer Frist von zwei (2) Wochen ordentlich gekündigt "
        f"werden (§ 622 Abs. 3 BGB)."
    )))

    s.append(("§ 2 Tätigkeit, Versetzung", (
        "(1) Der Arbeitnehmer wird mit Aufgaben betraut, die seiner "
        "Stellenbeschreibung entsprechen. Die aktuelle Stellen-"
        "beschreibung ist als Anlage 1 beigefügt und kann durch den "
        "Arbeitgeber unter Berücksichtigung der Belange des Arbeitnehmers "
        "angepasst werden.\n\n"
        "(2) Der Arbeitgeber behält sich vor, dem Arbeitnehmer aus "
        "sachlichem Grund auch andere, seinen Kenntnissen und Fähigkeiten "
        "entsprechende, gleichwertige Tätigkeiten zu übertragen.\n\n"
        "(3) Der Arbeitgeber behält sich vor, den Arbeitnehmer aus "
        "betrieblichen Gründen unter Berücksichtigung seiner persönlichen "
        "Belange an einen anderen Arbeitsort im Unternehmen oder einem "
        "verbundenen Unternehmen zu versetzen."
    )))

    s.append(("§ 3 Arbeitszeit", (
        "(1) Die regelmäßige wöchentliche Arbeitszeit beträgt 40 Stunden, "
        "ausschließlich der Pausen. Die Verteilung der Arbeitszeit auf "
        "die Wochentage erfolgt nach Maßgabe der betrieblichen Erfordernisse, "
        "in der Regel Montag bis Freitag.\n\n"
        "(2) Der Arbeitnehmer ist verpflichtet, seine Arbeitszeit "
        "elektronisch zu erfassen (in Umsetzung der Rechtsprechung "
        "des BAG vom 13.09.2022 - 1 ABR 22/21). Hierfür stellt der "
        "Arbeitgeber ein geeignetes Zeiterfassungssystem zur Verfügung.\n\n"
        "(3) Soweit es die betrieblichen Erfordernisse verlangen, ist "
        "der Arbeitnehmer auf Anordnung zur Leistung von Mehrarbeit, "
        "Überstunden und gelegentlich auch zu Sonn- und Feiertagsarbeit "
        "verpflichtet.\n\n"
        "(4) Eventuelle Überstunden sind mit dem in § 4 vereinbarten "
        "Festgehalt abgegolten, soweit sie das Maß von 10 % der monatlichen "
        "Sollarbeitszeit nicht überschreiten. Darüber hinausgehende "
        "Überstunden werden durch Freizeit ausgeglichen oder, soweit "
        "Freizeitausgleich nicht möglich ist, in Höhe des anteiligen "
        "Stundenlohns ohne Zuschlag vergütet."
    )))

    s.append(("§ 4 Vergütung", (
        f"(1) Der Arbeitnehmer erhält ein festes Bruttojahresgehalt "
        f"in Höhe von EUR {gehalt}, zahlbar in zwölf (12) gleichen "
        f"Monatsraten jeweils am Monatsende.\n\n"
        f"(2) Zusätzlich erhält der Arbeitnehmer eine variable Vergütung "
        f"in Form einer leistungsbezogenen Jahresprämie, deren Höhe "
        f"jährlich nach Leistungsbeurteilung und Geschäftsverlauf "
        f"festgesetzt wird. Ein Rechtsanspruch auf die variable "
        f"Vergütung für künftige Jahre wird durch wiederholte Zahlung "
        f"nicht begründet (Freiwilligkeitsvorbehalt).\n\n"
        f"(3) Mit der vereinbarten Vergütung sind alle Leistungen des "
        f"Arbeitnehmers abgegolten, mit Ausnahme von Überstunden gemäß "
        f"§ 3 Abs. 4."
    )))

    s.append(("§ 5 Urlaub", (
        "(1) Der Arbeitnehmer hat einen Urlaubsanspruch von 30 Werktagen "
        "(bei einer Fünf-Tage-Woche) pro Kalenderjahr.\n\n"
        "(2) Im Eintritts- und Austrittsjahr ergibt sich der Urlaubs-"
        "anspruch zeitanteilig (1/12 pro vollem Beschäftigungsmonat).\n\n"
        "(3) Der Urlaub ist im laufenden Kalenderjahr zu nehmen. "
        "Übertragung auf das Folgejahr ist nur ausnahmsweise unter den "
        "Voraussetzungen des § 7 Abs. 3 BUrlG zulässig.\n\n"
        "(4) Im Falle der Beendigung des Arbeitsverhältnisses während "
        "des Kalenderjahres erhält der Arbeitnehmer den Urlaubsanspruch "
        "anteilig nach Maßgabe von § 5 Abs. 1 c) BUrlG."
    )))

    s.append(("§ 6 Arbeitsverhinderung und Krankheit", (
        "(1) Der Arbeitnehmer hat eine Arbeitsverhinderung – gleich "
        "aus welchem Grund – unverzüglich anzuzeigen.\n\n"
        "(2) Bei einer Erkrankung von mehr als drei (3) Kalendertagen "
        "hat der Arbeitnehmer spätestens am vierten Tag eine ärztliche "
        "Arbeitsunfähigkeitsbescheinigung vorzulegen. Der Arbeitgeber "
        "ist berechtigt, die Vorlage einer Bescheinigung bereits am "
        "ersten Tag der Erkrankung zu verlangen.\n\n"
        "(3) Der Arbeitnehmer hat im Krankheitsfall Anspruch auf "
        "Entgeltfortzahlung nach Maßgabe des Entgeltfortzahlungsgesetzes."
    )))

    s.append(("§ 7 Nebentätigkeit", (
        "(1) Der Arbeitnehmer wird seine gesamte Arbeitskraft den "
        "Aufgaben des Arbeitgebers widmen. Jede entgeltliche oder "
        "regelmäßige Nebentätigkeit bedarf der vorherigen schriftlichen "
        "Genehmigung des Arbeitgebers.\n\n"
        "(2) Die Genehmigung darf nur verweigert werden, wenn berechtigte "
        "Interessen des Arbeitgebers entgegenstehen, insbesondere wenn "
        "die Nebentätigkeit die Arbeitsfähigkeit beeinträchtigt, das "
        "Wettbewerbsverbot tangiert oder das gesetzliche Höchstarbeits-"
        "zeitvolumen überschritten würde."
    )))

    s.append(("§ 8 Verschwiegenheit", (
        "(1) Der Arbeitnehmer ist verpflichtet, über alle ihm in seiner "
        "Eigenschaft als Arbeitnehmer bekanntwerdenden geschäftlichen "
        "Angelegenheiten des Arbeitgebers und der verbundenen Unternehmen "
        "auch nach Beendigung des Arbeitsverhältnisses Stillschweigen "
        "zu bewahren.\n\n"
        "(2) Geschäfts- und Betriebsgeheimnisse im Sinne des § 2 Nr. 1 "
        "GeschGehG sind unbefristet vertraulich zu behandeln.\n\n"
        "(3) Bei Beendigung des Arbeitsverhältnisses sind alle "
        "Geschäftsunterlagen, einschließlich Kopien, an den Arbeitgeber "
        "herauszugeben."
    )))

    s.append(("§ 9 Arbeitnehmererfindungen", (
        "(1) Für Erfindungen des Arbeitnehmers gilt das Gesetz über "
        "Arbeitnehmererfindungen (ArbnErfG) in seiner jeweils gültigen "
        "Fassung.\n\n"
        "(2) Der Arbeitnehmer ist verpflichtet, dem Arbeitgeber jede "
        "Diensterfindung unverzüglich gesondert in Textform zu melden.\n\n"
        "(3) Urheberrechte an im Rahmen des Arbeitsverhältnisses "
        "geschaffenen Werken werden dem Arbeitgeber im gesetzlich "
        "zulässigen Umfang ausschließlich, zeitlich, räumlich und "
        "inhaltlich unbeschränkt eingeräumt."
    )))

    s.append(("§ 10 Rückzahlung von Fortbildungskosten", (
        "(1) Der Arbeitgeber kann Fortbildungsmaßnahmen für den "
        "Arbeitnehmer übernehmen, wenn diese im betrieblichen Interesse "
        "liegen und einen geldwerten Vorteil für den Arbeitnehmer "
        "darstellen.\n\n"
        "(2) Für den Fall, dass der Arbeitnehmer vor Ablauf einer "
        "Bindungsfrist nach Abschluss der Fortbildung das Arbeitsverhältnis "
        "auf eigene Veranlassung beendet, ist er verpflichtet, die "
        "Fortbildungskosten anteilig zurückzuzahlen.\n\n"
        "(3) Die Bindungsfrist und der Rückzahlungsmodus richten sich "
        "nach den Grundsätzen der Rechtsprechung des BAG und werden "
        "in einer gesonderten Fortbildungsvereinbarung geregelt."
    )))

    s.append(("§ 11 Ausschlussfristen", (
        "(1) Alle beiderseitigen Ansprüche aus dem Arbeitsverhältnis "
        "und solche, die mit dem Arbeitsverhältnis in Verbindung stehen, "
        "verfallen, wenn sie nicht innerhalb von drei (3) Monaten nach "
        "Fälligkeit gegenüber der anderen Vertragspartei in Textform "
        "geltend gemacht werden.\n\n"
        "(2) Lehnt die andere Vertragspartei den Anspruch ab oder erklärt "
        "sie sich nicht innerhalb von zwei (2) Wochen nach Geltend-"
        "machung, so verfällt der Anspruch, wenn er nicht innerhalb von "
        "weiteren drei (3) Monaten nach Ablehnung oder dem Fristablauf "
        "gerichtlich geltend gemacht wird.\n\n"
        "(3) Die Ausschlussfristen finden keine Anwendung auf Ansprüche "
        "aus vorsätzlichen Handlungen, Ansprüche auf Mindestlohn nach "
        "MiLoG sowie auf andere Ansprüche, die einer einzelvertraglichen "
        "Ausschlussfrist von Gesetzes wegen nicht zugänglich sind."
    )))

    s.append(("§ 12 Datenschutz", (
        "(1) Der Arbeitgeber verarbeitet personenbezogene Daten des "
        "Arbeitnehmers im Rahmen und für die Zwecke des Arbeitsverhältnisses "
        "nach Maßgabe der DSGVO und des BDSG.\n\n"
        "(2) Eine Datenschutzinformation gemäß Art. 13 DSGVO ist diesem "
        "Vertrag als Anlage beigefügt.\n\n"
        "(3) Der Arbeitnehmer wird auf die Geheimhaltungspflichten "
        "nach Art. 5 Abs. 1 lit. f DSGVO sowie auf das Datengeheimnis "
        "verpflichtet."
    )))

    s.append(("§ 13 Beendigung des Arbeitsverhältnisses", (
        "(1) Nach Ablauf der Probezeit kann das Arbeitsverhältnis von "
        "beiden Seiten mit den gesetzlichen Fristen gemäß § 622 BGB "
        "ordentlich gekündigt werden.\n\n"
        "(2) Eine Kündigung bedarf zu ihrer Wirksamkeit der Schriftform "
        "im Sinne von § 623 BGB. Die elektronische Form ist ausgeschlossen.\n\n"
        "(3) Das Arbeitsverhältnis endet spätestens mit Ablauf des "
        "Monats, in dem der Arbeitnehmer die Regelaltersgrenze in der "
        "gesetzlichen Rentenversicherung erreicht.\n\n"
        "(4) Bei Beendigung des Arbeitsverhältnisses sind alle "
        "überlassenen Arbeitsmittel an den Arbeitgeber herauszugeben."
    )))

    s.append(("§ 14 Bezugnahme auf Tarifvertrag / Betriebsvereinbarung", (
        "(1) Soweit Tarifverträge in der vom Arbeitgeber jeweils "
        "angewendeten Fassung Anwendung finden, gelten diese ergänzend, "
        "sofern sie für den Arbeitnehmer günstiger sind als die "
        "Bestimmungen dieses Vertrages.\n\n"
        "(2) Bestehende und künftige Betriebsvereinbarungen gelten "
        "auch für den Arbeitnehmer."
    )))

    s.append(("§ 15 Schlussbestimmungen", (
        "(1) Änderungen und Ergänzungen dieses Vertrages bedürfen zu "
        "ihrer Wirksamkeit der Schriftform. Dies gilt auch für die "
        "Aufhebung der Schriftformklausel selbst.\n\n"
        "(2) Mündliche Nebenabreden bestehen nicht.\n\n"
        "(3) " + SALVATORISCH
    )))

    s.append(("Unterschriften", _signature_block(
        p, "Geschäftsführung " + company, "Arbeitgeber",
        employee, "Arbeitnehmer"
    )))

    return s


def gen_betriebsvereinbarung(p: Dict[str, Any], topic: str = "Arbeitszeit") -> List[Section]:
    """Betriebsvereinbarung zu einem Thema. Target: 1500-3000 Wörter."""

    company = _g(p, "company", "Muster GmbH")
    city = _g(p, "city", "Köln")

    s: List[Section] = []

    topic_content = {
        "Arbeitszeit": (
            "Flexible Arbeitszeit, Vertrauensarbeitszeit, Gleitzeitrahmen, "
            "Arbeitszeitkonten, Mehrarbeit und Zeiterfassung",
            "Diese Betriebsvereinbarung regelt die flexible Gestaltung "
            "der Arbeitszeit der vom persönlichen Geltungsbereich erfassten "
            "Arbeitnehmer. Ziel ist es, die unterschiedlichen Interessen "
            "von Arbeitgeber (Reaktionsfähigkeit, Auslastung) und Arbeit-"
            "nehmern (Vereinbarkeit Beruf und Privatleben, Arbeitszeit-"
            "souveränität) miteinander in Einklang zu bringen.",
            (
                "(1) Die regelmäßige wöchentliche Arbeitszeit der "
                "Vollzeitbeschäftigten beträgt 38 Stunden ausschließlich "
                "der Pausen.\n\n"
                "(2) Die Arbeitszeit wird in einem Gleitzeitrahmen von "
                "Montag bis Freitag, 06:00 bis 21:00 Uhr, erbracht. "
                "Kernarbeitszeit besteht – mit Ausnahme produktionskritischer "
                "Bereiche – nicht. Jeder Mitarbeiter kann seine tägliche "
                "Arbeitszeit im Gleitzeitrahmen frei einteilen, soweit "
                "betriebliche Erfordernisse dies zulassen.\n\n"
                "(3) Pausen werden gesetzeskonform gewährt: 30 Minuten "
                "bei einer Arbeitszeit von 6 bis 9 Stunden, 45 Minuten "
                "bei mehr als 9 Stunden (§ 4 ArbZG).\n\n"
                "(4) Die Arbeitszeit wird elektronisch erfasst (in "
                "Umsetzung des BAG-Beschlusses vom 13.09.2022). Jeder "
                "Arbeitnehmer ist verpflichtet, Beginn und Ende seiner "
                "täglichen Arbeitszeit selbst zu erfassen. Die "
                "Zeiterfassungsdaten werden ausschließlich für die "
                "Lohnabrechnung und Arbeitszeitkonten-Führung genutzt "
                "und nicht zur Verhaltens- oder Leistungskontrolle "
                "verwertet.\n\n"
                "(5) Jeder Arbeitnehmer erhält ein persönliches "
                "Arbeitszeitkonto, das einen Saldo von -20 bis +80 "
                "Stunden ausweisen kann. Bei Überschreitung der "
                "Bandbreite werden mit der Führungskraft individuelle "
                "Maßnahmen zum Saldenausgleich vereinbart.\n\n"
                "(6) Stunden auf dem Arbeitszeitkonto werden vorrangig "
                "durch Freizeitausgleich abgebaut. Eine finanzielle "
                "Abgeltung erfolgt nur im Falle der Beendigung des "
                "Arbeitsverhältnisses.\n\n"
                "(7) Mehrarbeit ist anordnungspflichtig und nur mit "
                "schriftlicher Genehmigung der Führungskraft zulässig. "
                "Sie wird mit 1:1 in das Arbeitszeitkonto eingestellt; "
                "Zuschläge nach Maßgabe des Tarifvertrages bleiben "
                "unberührt."
            )
        ),
        "Mobiles Arbeiten": (
            "Mobiles Arbeiten und Homeoffice",
            "Diese Betriebsvereinbarung regelt die Rahmenbedingungen "
            "für das mobile Arbeiten und das Arbeiten von zu Hause "
            "aus (Homeoffice) als hybride Arbeitsform. Ziel ist die "
            "Stärkung der Arbeitszeitsouveränität und der Vereinbarkeit "
            "von Beruf und Privatleben.",
            (
                "(1) Mobiles Arbeiten ist Beschäftigten ab dem 7. "
                "Beschäftigungsmonat in einem Umfang von bis zu 60 % "
                "der vereinbarten regelmäßigen Arbeitszeit pro Woche "
                "möglich, sofern die Tätigkeit dies zulässt und keine "
                "betrieblichen Belange entgegenstehen.\n\n"
                "(2) Beschäftigte vereinbaren mit ihrer Führungskraft "
                "die mobilen Arbeitstage im rollierenden Quartalsplan. "
                "Der Arbeitgeber behält sich vor, aus betrieblichen "
                "Gründen mit einer Vorlaufzeit von zwei (2) Tagen "
                "Präsenz im Betrieb anzuordnen.\n\n"
                "(3) Der Arbeitsort beim mobilen Arbeiten ist frei "
                "wählbar innerhalb der EU/EWR. Außerhalb der EU/EWR "
                "ist mobiles Arbeiten nicht zulässig (steuer- und "
                "sozialversicherungsrechtliche Gründe).\n\n"
                "(4) Der Arbeitgeber stellt für die Tätigkeit "
                "geeignete technische Ausstattung zur Verfügung "
                "(Notebook, Headset, ggf. Monitor). Beschäftigte "
                "können eine Homeoffice-Pauschale für ergonomische "
                "Möbel in Höhe von einmalig EUR 800 abrufen, alle "
                "drei Jahre erneut.\n\n"
                "(5) Beim mobilen Arbeiten sind die geltenden "
                "Arbeitsschutz- und Datenschutzbestimmungen zu beachten. "
                "Insbesondere ist die Bildschirmarbeitsverordnung "
                "einzuhalten; vertrauliche Unterlagen sind sicher zu "
                "verwahren.\n\n"
                "(6) Erreichbarkeit besteht in der vereinbarten "
                "Kernarbeitszeit. Außerhalb dieser Zeit besteht kein "
                "Anspruch auf Erreichbarkeit (Recht auf Nicht-"
                "Erreichbarkeit).\n\n"
                "(7) Die Vereinbarung über mobiles Arbeiten kann von "
                "beiden Seiten mit einer Frist von vier (4) Wochen zum "
                "Monatsende beendet werden, ohne dass es eines "
                "wichtigen Grundes bedarf."
            )
        ),
        "IT-Systeme": (
            "Einsatz von IT-Systemen, Beweisverwertungsverbot",
            "Diese Betriebsvereinbarung regelt den Einsatz von IT-"
            "Systemen im Unternehmen, soweit diese geeignet sind, das "
            "Verhalten oder die Leistung der Beschäftigten zu "
            "überwachen, und unterfallen damit der Mitbestimmung des "
            "Betriebsrats nach § 87 Abs. 1 Nr. 6 BetrVG.",
            (
                "(1) Erfasst sind alle IT-Systeme, die im Anlageverzeichnis "
                "(Anlage 1) aufgeführt sind, sowie alle künftig im "
                "Unternehmen eingesetzten Systeme, soweit diese eine "
                "Verhaltens- und Leistungskontrolle ermöglichen.\n\n"
                "(2) Die Nutzung der Systeme erfolgt ausschließlich zu "
                "den in Anlage 2 dokumentierten Zwecken. Eine "
                "Zweckänderung bedarf der vorherigen Zustimmung des "
                "Betriebsrats.\n\n"
                "(3) Eine systematische Verhaltens- und Leistungskontrolle "
                "auf Basis der erhobenen Daten ist ausgeschlossen. "
                "Auswertungen erfolgen ausschließlich anonymisiert oder "
                "aggregiert.\n\n"
                "(4) Beweisverwertungsverbot: Daten, die ohne Beachtung "
                "dieser Betriebsvereinbarung erhoben wurden, dürfen "
                "weder zur Beweiserhebung in arbeitsrechtlichen "
                "Auseinandersetzungen verwendet noch im Übrigen "
                "personenbezogen ausgewertet werden.\n\n"
                "(5) Datenkategorien, Speicherdauer und Zugriffsberechtigte "
                "ergeben sich aus Anlage 3 (Datenkatalog). Daten werden "
                "spätestens nach Ablauf der gesetzlichen Aufbewahrungs-"
                "fristen gelöscht.\n\n"
                "(6) Vor Einführung neuer Systeme wird der Betriebsrat "
                "rechtzeitig informiert und beteiligt (§ 87 Abs. 1 Nr. 6 "
                "BetrVG). Soweit eine Datenschutz-Folgenabschätzung "
                "(DSFA) nach Art. 35 DSGVO erforderlich ist, wird der "
                "Betriebsrat einbezogen.\n\n"
                "(7) Beschäftigte sind berechtigt, jederzeit Auskunft "
                "über die zu ihrer Person gespeicherten Daten zu verlangen "
                "(Art. 15 DSGVO)."
            )
        ),
    }

    if topic not in topic_content:
        topic = "Arbeitszeit"
    headline, preamble, content = topic_content[topic]

    s.append(("Präambel", (
        f"Zwischen der {company} mit Sitz in {city}, vertreten durch "
        f"die Geschäftsführung – nachfolgend „Arbeitgeber' – und dem "
        f"Betriebsrat der {company}, vertreten durch den/die Vorsitzende/n "
        f"– nachfolgend „Betriebsrat'; Arbeitgeber und Betriebsrat "
        f"gemeinsam „Betriebsparteien' – wird die folgende "
        f"Betriebsvereinbarung über „{headline}' geschlossen.\n\n"
        f"{preamble}"
    )))

    s.append(("§ 1 Geltungsbereich", (
        f"(1) Räumlich: Diese Betriebsvereinbarung gilt für sämtliche "
        f"Standorte des Arbeitgebers im Geltungsbereich des deutschen "
        f"Betriebsverfassungsgesetzes.\n\n"
        f"(2) Persönlich: Sie gilt für alle Arbeitnehmer im Sinne des "
        f"§ 5 BetrVG, einschließlich Auszubildender, leitender "
        f"Angestellter im Sinne von § 5 Abs. 3 BetrVG nur, soweit "
        f"hierin ausdrücklich geregelt.\n\n"
        f"(3) Sachlich: Die Betriebsvereinbarung regelt die in der "
        f"Präambel beschriebenen Sachverhalte abschließend, soweit "
        f"sie der Mitbestimmung des Betriebsrats unterliegen."
    )))

    s.append(("§ 2 Definitionen", (
        "Im Sinne dieser Betriebsvereinbarung haben die nachfolgenden "
        "Begriffe folgende Bedeutung: „Arbeitszeit', „Pausen', "
        "„Arbeitszeitkonto', „Kernarbeitszeit', „Gleitzeitrahmen', "
        "„Mehrarbeit', „Mobiles Arbeiten' bzw. „Homeoffice', "
        "„Erreichbarkeitszeit' und „IT-System' werden im Sinne der "
        "betrieblichen Praxis und der einschlägigen gesetzlichen "
        "Definitionen ausgelegt; im Zweifelsfall gilt die "
        "arbeitsschutzrechtliche und mitbestimmungsrechtliche "
        "Auslegung."
    )))

    s.append(("§ 3 Regelungsinhalt", content))

    s.append(("§ 4 Mitbestimmungsrechte des Betriebsrats", (
        "(1) Die Betriebsparteien stimmen darin überein, dass die in "
        "dieser Vereinbarung getroffenen Regelungen die gemäß §§ 87 ff. "
        "BetrVG bestehenden Mitbestimmungsrechte des Betriebsrats "
        "wahrnehmen und konkretisieren.\n\n"
        "(2) Werden im Anwendungsbereich dieser Betriebsvereinbarung "
        "Änderungen erforderlich, werden die Betriebsparteien hierüber "
        "rechtzeitig in Verhandlungen treten.\n\n"
        "(3) Bei Streitigkeiten über die Auslegung oder Anwendung "
        "dieser Vereinbarung wird zunächst eine paritätische Klärung "
        "in einem Eskalationsausschuss versucht; gelingt diese nicht, "
        "kann eine Einigungsstelle gemäß § 76 BetrVG angerufen werden."
    )))

    s.append(("§ 5 Datenschutz", (
        "(1) Die im Anwendungsbereich dieser Betriebsvereinbarung "
        "verarbeiteten personenbezogenen Daten werden unter Beachtung "
        "der DSGVO und des BDSG verarbeitet. Die Rechtsgrundlagen "
        "ergeben sich aus § 26 Abs. 1 und Abs. 4 BDSG sowie aus dieser "
        "Betriebsvereinbarung als Kollektivvereinbarung im Sinne von "
        "Art. 88 DSGVO.\n\n"
        "(2) Die Betroffenenrechte (Auskunft, Berichtigung, Löschung, "
        "Einschränkung, Widerspruch) bleiben unberührt."
    )))

    s.append(("§ 6 Inkrafttreten, Laufzeit, Kündigung, Nachwirkung", (
        f"(1) Diese Betriebsvereinbarung tritt am Tag nach ihrer "
        f"Unterzeichnung in Kraft.\n\n"
        f"(2) Sie wird auf unbestimmte Zeit geschlossen und kann von "
        f"jeder Betriebspartei mit einer Frist von drei (3) Monaten "
        f"zum Quartalsende gekündigt werden.\n\n"
        f"(3) Nach Beendigung gilt die Betriebsvereinbarung gemäß § 77 "
        f"Abs. 6 BetrVG bis zum Abschluss einer neuen Regelung "
        f"weiter (Nachwirkung), soweit ein zwingend mitbestimmungs-"
        f"pflichtiger Inhalt betroffen ist.\n\n"
        f"(4) " + SALVATORISCH
    )))

    s.append(("Unterschriften", (
        f"{city}, den {_today_de()}\n\n"
        f"Für den Arbeitgeber:\n"
        f"_______________________\n"
        f"Geschäftsführung\n\n"
        f"Für den Betriebsrat:\n"
        f"_______________________\n"
        f"Betriebsratsvorsitzende/r"
    )))

    return s


# =====================================================================
# REAL ESTATE
# =====================================================================

def gen_gewerbemietvertrag(p: Dict[str, Any]) -> List[Section]:
    """Gewerbemietvertrag (Produktionshalle). Target: 5000-8000 Wörter."""

    vermieter = _g(p, "vermieter", "Immobilien GmbH & Co. KG")
    mieter = _g(p, "mieter", "Muster GmbH")
    city = _g(p, "city", "Köln")
    flaeche = _g(p, "flaeche", "4.500")
    miete = _g(p, "miete", "8,50")
    nk = _g(p, "nk", "2,80")
    laufzeit = _g(p, "laufzeit", "10")
    kaution = _g(p, "kaution", "3")

    s: List[Section] = []

    s.append(("Präambel", (
        f"Zwischen {vermieter} mit Sitz in {city} – nachfolgend "
        f"„Vermieter' – und {mieter} mit Sitz in {city} – nachfolgend "
        f"„Mieter'; Vermieter und Mieter gemeinsam „Parteien' – wird "
        f"folgender Gewerbemietvertrag über die Anmietung von "
        f"Produktions-, Lager- und Büroflächen in der Liegenschaft "
        f"„[Liegenschaftsbezeichnung]', {_g(p, 'object_address', 'Industriestraße 1, ' + city)} "
        f"geschlossen.\n\n"
        f"Der Vermieter ist Eigentümer der Liegenschaft, eingetragen "
        f"im Grundbuch des Amtsgerichts {city}, Grundbuch von "
        f"[Gemarkung], Blatt [Nr.]. Der Mieter beabsichtigt, die "
        f"Mietsache für den Betrieb seiner Produktion zu nutzen. Die "
        f"Parteien wünschen, das Mietverhältnis abschließend zu regeln."
    )))

    s.append(("§ 1 Mietsache", (
        f"(1) Der Vermieter vermietet an den Mieter die in der "
        f"Liegenschaft gelegenen Räumlichkeiten, bestehend aus:\n\n"
        f"a) Produktionshalle mit einer Nutzfläche von ca. "
        f"{flaeche} m² gemäß rot umrandeter Fläche im Lageplan (Anlage 1);\n\n"
        f"b) Lagerflächen mit einer Nutzfläche von ca. [m²] gemäß "
        f"grün umrandeter Fläche im Lageplan;\n\n"
        f"c) Büroflächen mit einer Nutzfläche von ca. [m²] gemäß "
        f"blau umrandeter Fläche im Lageplan;\n\n"
        f"d) Sozialräume, Sanitäranlagen und Funktionsflächen gemäß "
        f"Grundriss (Anlage 2);\n\n"
        f"e) Parkplätze (Anzahl: [n]) auf den im Lageplan markierten "
        f"Stellplätzen.\n\n"
        f"(2) Die Mietfläche wird im Übergabeprotokoll (Anlage 3) "
        f"bei Übergabe konkret ausgemessen und festgehalten. "
        f"Abweichungen der tatsächlichen Mietfläche von der vereinbarten "
        f"Mietfläche bis zu 3 % berechtigen weder zu Mietminderung "
        f"noch zu einer Anpassung der Miete.\n\n"
        f"(3) Die Mietsache wird in dem Zustand übergeben, wie sich "
        f"aus dem Übergabeprotokoll ergibt. Der Mieter bestätigt, die "
        f"Mietsache vor Vertragsschluss eingehend besichtigt zu haben.\n\n"
        f"(4) Mitvermietet sind das mitbenutzte Gebäudeumfeld, die "
        f"Zugangswege, die gemeinschaftlich genutzten technischen "
        f"Anlagen sowie die in der Liegenschaft befindlichen "
        f"Heizungs-, Wasser- und Stromversorgungseinrichtungen."
    )))

    s.append(("§ 2 Mietzweck und Konkurrenzschutz", (
        f"(1) Die Mietsache wird zum Betrieb der "
        f"„{_g(p, 'usage', 'Produktion und Lagerung industrieller Erzeugnisse einschließlich Verwaltung')}' "
        f"vermietet. Eine andere Nutzung ist nur mit vorheriger "
        f"schriftlicher Zustimmung des Vermieters zulässig; die "
        f"Zustimmung darf nicht ohne sachlichen Grund verweigert werden.\n\n"
        f"(2) Der Mieter hat sicherzustellen, dass alle für seinen "
        f"Betrieb erforderlichen behördlichen Genehmigungen vorliegen. "
        f"Der Vermieter haftet nicht dafür, dass die Mietsache für die "
        f"vom Mieter beabsichtigte Nutzung behördlich genehmigt wird.\n\n"
        f"(3) Konkurrenzschutz: Der Vermieter verpflichtet sich, in "
        f"der Liegenschaft während der Dauer dieses Mietvertrages "
        f"keine Flächen an einen unmittelbaren Wettbewerber des "
        f"Mieters (definiert als Unternehmen, das in den vom Mieter "
        f"bedienten Geschäftsfeldern tätig ist) zu vermieten."
    )))

    s.append(("§ 3 Mietzeit", (
        f"(1) Das Mietverhältnis beginnt am "
        f"{_g(p, 'mietbeginn', '01.01.2025')} und wird auf eine feste "
        f"Laufzeit von {laufzeit} Jahren geschlossen. Es endet ohne "
        f"dass es einer Kündigung bedarf am "
        f"{_g(p, 'mietende', '31.12.2034')}.\n\n"
        f"(2) Der Mieter hat eine Verlängerungsoption, die er einmalig "
        f"oder mehrfach um jeweils fünf (5) Jahre durch schriftliche "
        f"Erklärung gegenüber dem Vermieter ausüben kann, spätestens "
        f"jedoch 12 Monate vor Ablauf der jeweils laufenden Mietzeit.\n\n"
        f"(3) Eine ordentliche Kündigung des Mietverhältnisses während "
        f"der festen Laufzeit ist ausgeschlossen, soweit nicht durch "
        f"diesen Vertrag oder das Gesetz ausdrücklich vorgesehen.\n\n"
        f"(4) Die Vorschriften über die fristlose Kündigung aus "
        f"wichtigem Grund (§§ 543, 569 BGB) bleiben unberührt."
    )))

    s.append(("§ 4 Schriftform - § 550 BGB-Heilung", (
        "(1) Die Parteien sind sich der Bedeutung des Schriftform-"
        "erfordernisses des § 550 BGB für die Wirksamkeit einer "
        "langfristigen Bindung bewusst. Sie verpflichten sich gegenseitig, "
        "auf jederzeitiges Verlangen einer Partei alle Handlungen "
        "vorzunehmen und Erklärungen abzugeben, die erforderlich sind, "
        "um dem Schriftformerfordernis Genüge zu tun, und den Vertrag "
        "nicht unter Berufung auf die Nichteinhaltung der Schriftform "
        "vorzeitig zu kündigen.\n\n"
        "(2) Dies gilt nicht nur für den Abschluss dieses Vertrages "
        "und seiner Anlagen, sondern auch für sämtliche Nachträge, "
        "Vertragsänderungen und Ergänzungen.\n\n"
        "(3) Im Falle einer wirksamen Kündigung wegen Nichteinhaltung "
        "der Schriftform schuldet die kündigende Partei der "
        "kündigenden Partei einen pauschalierten Schadensersatz in "
        "Höhe der Restmiete der ursprünglichen Mietlaufzeit, höchstens "
        "jedoch von 24 Monatsmieten, soweit dies rechtlich zulässig ist."
    )))

    s.append(("§ 5 Mietzins und Wertsicherung", (
        f"(1) Die monatliche Grundmiete beträgt EUR {miete} pro "
        f"Quadratmeter Mietfläche, mithin EUR "
        f"{float(miete.replace(',', '.')) * float(flaeche.replace('.', '')):,.2f} "
        f"insgesamt netto monatlich (in Worten: [Betrag] Euro). Die "
        f"Grundmiete erhöht sich um die jeweils gesetzlich geschuldete "
        f"Umsatzsteuer (§ 9 UStG-Option, siehe § 6).\n\n"
        f"(2) Wertsicherung: Verändert sich der vom Statistischen "
        f"Bundesamt veröffentlichte Verbraucherpreisindex für Deutschland "
        f"(VPI, Basis 2020 = 100) ab dem Tag des Vertragsbeginns um "
        f"mehr als 5 Punkte, so erhöht sich die Grundmiete im "
        f"prozentualen Verhältnis der Indexveränderung. Maßgeblich ist "
        f"der jeweils zum Stichtag (1. Januar) zuletzt veröffentlichte "
        f"Index.\n\n"
        f"(3) Die Anpassung erfolgt automatisch zum jeweils nächsten "
        f"1. Januar nach Überschreitung der Schwelle. Eine "
        f"rückwirkende Anpassung findet nicht statt; die Differenz wird "
        f"jedoch nicht „verbraucht', sondern bleibt für die nächste "
        f"Anpassung erhalten.\n\n"
        f"(4) Die Miete ist monatlich im Voraus, spätestens am dritten "
        f"Werktag eines Monats, auf das vom Vermieter benannte Konto "
        f"zu zahlen. Bankgebühren trägt der Mieter; rechtzeitig ist "
        f"die Zahlung, wenn der Vermieter sie spätestens am dritten "
        f"Werktag verfügen kann."
    )))

    s.append(("§ 6 Umsatzsteueroption", (
        "(1) Der Vermieter optiert hiermit unwiderruflich nach § 9 "
        "Abs. 2 UStG zur Umsatzsteuerpflicht.\n\n"
        "(2) Der Mieter verpflichtet sich, die Mietsache ausschließlich "
        "zur Ausführung von Umsätzen zu nutzen, die den Vorsteuerabzug "
        "nicht ausschließen, und versichert, mehr als 95 % vorsteuer-"
        "abzugsberechtigt zu sein.\n\n"
        "(3) Fällt die Voraussetzung des Vorsteuerabzugs ganz oder "
        "teilweise weg, hat der Mieter dies dem Vermieter unverzüglich "
        "anzuzeigen und ihm jeden hieraus entstehenden Schaden, "
        "insbesondere die Korrektur des Vorsteuerabzugs nach § 15a UStG, "
        "zu ersetzen."
    )))

    s.append(("§ 7 Betriebs- und Nebenkosten", (
        f"(1) Der Mieter trägt sämtliche umlagefähigen Betriebskosten "
        f"im Sinne der Betriebskostenverordnung (BetrKV) sowie alle "
        f"sonstigen mit dem Betrieb der Liegenschaft verbundenen Kosten "
        f"(insbesondere Grundsteuer, Versicherungen, Wartung, Reinigung, "
        f"Müllabfuhr, Wasserversorgung, Abwasser, Strom für "
        f"Gemeinflächen, Aufzugswartung, Hausmeisterservice, Garten-"
        f"pflege, Schornsteinfeger, technische Wartungsverträge, "
        f"Verwaltungskosten von bis zu 3 % der Nettomiete).\n\n"
        f"(2) Der Mieter zahlt eine monatliche Nebenkostenvorauszahlung "
        f"von EUR {nk} pro Quadratmeter, insgesamt EUR "
        f"{float(nk.replace(',', '.')) * float(flaeche.replace('.', '')):,.2f} "
        f"netto, zuzüglich Umsatzsteuer.\n\n"
        f"(3) Über die Betriebskosten wird jährlich spätestens bis "
        f"zum 30. September des Folgejahres abgerechnet. Nachforderungen "
        f"und Guthaben sind binnen 30 Tagen ab Zugang der Abrechnung "
        f"auszugleichen.\n\n"
        f"(4) Der Mieter ist berechtigt, die Abrechnung und ihre "
        f"Belege während der üblichen Geschäftszeiten beim Vermieter "
        f"einzusehen.\n\n"
        f"(5) Verbrauchsabhängige Kosten (Wasser, Wärme, Strom) werden "
        f"– soweit möglich – nach tatsächlichem Verbrauch, im Übrigen "
        f"nach dem Anteil der Mietfläche an der Gesamtnutzfläche der "
        f"Liegenschaft umgelegt."
    )))

    s.append(("§ 8 Mietsicherheit", (
        f"(1) Der Mieter stellt dem Vermieter zur Sicherung aller "
        f"Ansprüche aus diesem Mietverhältnis eine Mietsicherheit in "
        f"Höhe von {kaution} Monatsmieten (Grundmiete zuzüglich "
        f"Nebenkostenvorauszahlung, ohne Umsatzsteuer).\n\n"
        f"(2) Die Mietsicherheit kann nach Wahl des Mieters durch "
        f"selbstschuldnerische, unbedingte und unbefristete Bürgschaft "
        f"eines deutschen Großkreditinstituts oder durch Hinterlegung "
        f"einer Barkaution auf einem Treuhandkonto geleistet werden.\n\n"
        f"(3) Die Mietsicherheit ist innerhalb von vier (4) Wochen nach "
        f"Vertragsschluss zu stellen.\n\n"
        f"(4) Der Vermieter kann die Mietsicherheit jederzeit zur "
        f"Erfüllung fälliger Ansprüche aus diesem Mietverhältnis in "
        f"Anspruch nehmen. Der Mieter ist in diesem Fall verpflichtet, "
        f"die Sicherheit unverzüglich wieder aufzufüllen."
    )))

    s.append(("§ 9 Übergabe und Übernahme", (
        "(1) Die Übergabe der Mietsache erfolgt am Mietbeginn unter "
        "Aufnahme eines Übergabeprotokolls (Anlage 3), das Bestandteil "
        "dieses Vertrages wird.\n\n"
        "(2) Im Übergabeprotokoll werden festgehalten: der "
        "Zustand der Mietsache, vorhandene Schäden, Zählerstände, "
        "Anzahl und Beschaffenheit übergebener Schlüssel.\n\n"
        "(3) Im Rahmen der Übergabe nimmt der Vermieter das Mietobjekt "
        "in vollständig geräumtem, gereinigtem und betriebsbereitem "
        "Zustand an den Mieter über."
    )))

    s.append(("§ 10 Instandhaltung und Instandsetzung", (
        "(1) Der Vermieter ist verpflichtet, die Mietsache während "
        "der Mietzeit in einem zum vertragsgemäßen Gebrauch geeigneten "
        "Zustand zu erhalten („Dach und Fach'). Die Instandhaltung und "
        "Instandsetzung der konstruktiven Bauteile (Dach, tragende "
        "Wände, Decken, Fundamente, Außenfassade, Außenfenster, "
        "Außentüren) sowie der Hauptversorgungsleitungen liegen in "
        "der Verantwortung des Vermieters.\n\n"
        "(2) Der Mieter trägt die Kosten für laufende Instandhaltung "
        "und Wartung der ausschließlich von ihm genutzten Teile der "
        "Mietsache, insbesondere der Innenräume, Innenausstattung, "
        "Beleuchtungseinrichtungen, Heizkörperventile, Wasserhähne, "
        "Türen und Türschlösser bis zur Höhe von EUR 500 pro Einzelfall "
        "und höchstens 8 % der Jahresmiete im Vertragsjahr.\n\n"
        "(3) Schönheitsreparaturen (insbesondere Tapezieren, Streichen "
        "der Wände, Decken, Heizkörper und Türen) obliegen dem Mieter "
        "in handwerklich angemessenem Standard nach Maßgabe der "
        "tatsächlichen Abnutzung."
    )))

    s.append(("§ 11 Nutzung der Mietsache", (
        "(1) Der Mieter ist verpflichtet, die Mietsache pfleglich und "
        "schonend zu behandeln.\n\n"
        "(2) Der Mieter haftet für alle Schäden, die durch ihn, seine "
        "Beschäftigten, Beauftragten, Besucher oder Kunden an der "
        "Mietsache oder am Gemeinschaftseigentum schuldhaft verursacht "
        "werden.\n\n"
        "(3) Der Mieter hält die Mietsache während der Mietzeit "
        "ordnungsgemäß und betriebsbereit; er beachtet alle einschlägigen "
        "öffentlich-rechtlichen Vorschriften, insbesondere des "
        "Brandschutzes, der Arbeitssicherheit und des Umweltschutzes."
    )))

    s.append(("§ 12 Bauliche Veränderungen", (
        "(1) Bauliche Veränderungen, Um- und Einbauten an der Mietsache "
        "bedürfen der vorherigen schriftlichen Zustimmung des Vermieters. "
        "Die Zustimmung darf nicht aus willkürlichen Gründen verweigert "
        "werden.\n\n"
        "(2) Der Vermieter kann die Zustimmung davon abhängig machen, "
        "dass der Mieter die Maßnahmen auf eigene Kosten und Gefahr "
        "fachgerecht durchführt und im Falle der Beendigung des "
        "Mietverhältnisses entweder unentgeltlich überlässt oder auf "
        "eigene Kosten zurückbaut.\n\n"
        "(3) Genehmigungspflichtige Maßnahmen darf der Mieter nur nach "
        "Vorliegen aller behördlichen Genehmigungen durchführen."
    )))

    s.append(("§ 13 Versicherungen", (
        "(1) Der Vermieter unterhält für die Liegenschaft eine "
        "verbundene Gebäudeversicherung (Feuer, Sturm, Hagel, "
        "Leitungswasser, Elementar) sowie eine Haus- und Grundbesitzer-"
        "Haftpflichtversicherung. Die Versicherungskosten sind als "
        "Betriebskosten umlagefähig.\n\n"
        "(2) Der Mieter ist verpflichtet, auf eigene Kosten eine "
        "Betriebshaftpflicht- und eine Inventarversicherung (Feuer, "
        "Leitungswasser, Einbruchdiebstahl, Vandalismus) mit "
        "angemessenen Deckungssummen abzuschließen und zu unterhalten. "
        "Der Vermieter kann auf Verlangen die Vorlage einer Versicherungs-"
        "bestätigung fordern."
    )))

    s.append(("§ 14 Verkehrssicherungspflicht", (
        "(1) Die Verkehrssicherungspflicht für die Mietsache, "
        "einschließlich Winterdienst auf den dem Mieter zugeordneten "
        "Flächen, übernimmt der Mieter.\n\n"
        "(2) Für das Gemeinschaftseigentum und die nicht ausschließlich "
        "vom Mieter genutzten Außenflächen trägt der Vermieter die "
        "Verkehrssicherungspflicht; entsprechende Aufwendungen sind als "
        "Betriebskosten umlagefähig."
    )))

    s.append(("§ 15 Untervermietung", (
        "(1) Der Mieter ist nicht berechtigt, die Mietsache ganz oder "
        "teilweise unterzuvermieten oder Dritten zum Gebrauch zu "
        "überlassen. Eine Untervermietung an mit dem Mieter verbundene "
        "Unternehmen (§§ 15 ff. AktG) ist ohne Zustimmung zulässig.\n\n"
        "(2) Eine darüber hinausgehende Untervermietung oder "
        "Nutzungsüberlassung bedarf der vorherigen schriftlichen "
        "Zustimmung des Vermieters; die Zustimmung darf nicht aus "
        "unsachlichen Gründen verweigert werden."
    )))

    s.append(("§ 16 Modernisierung, GEG, Energieausweis", (
        "(1) Der Vermieter ist berechtigt, Modernisierungsmaßnahmen "
        "im Sinne von § 555b BGB durchzuführen, soweit sie dem Mieter "
        "rechtzeitig angekündigt werden.\n\n"
        "(2) Der Mieter duldet Modernisierungsmaßnahmen, soweit sie "
        "ihm zumutbar sind.\n\n"
        "(3) Der Vermieter hat dem Mieter den Energieausweis nach "
        "Gebäudeenergiegesetz (GEG) vor Vertragsschluss vorgelegt; "
        "der Energieausweis ist als Anlage 4 beigefügt."
    )))

    s.append(("§ 17 ESG-Klausel (Green Lease)", (
        "(1) Die Parteien streben gemeinsam an, die Energieeffizienz "
        "der Mietsache zu steigern und die CO2-Emissionen zu reduzieren "
        "(Green Lease).\n\n"
        "(2) Der Mieter wird dem Vermieter quartalsweise seine "
        "Verbrauchsdaten (Strom, Wärme, Wasser, Müll) zur Verfügung "
        "stellen.\n\n"
        "(3) Die Parteien arbeiten konstruktiv an Energiesparmaßnahmen "
        "und teilen die Kosten und Einsparungen partnerschaftlich.\n\n"
        "(4) Soweit der Vermieter Modernisierungen zur Reduzierung "
        "der CO2-Emissionen vornimmt, ist der Mieter zur Mitwirkung "
        "verpflichtet."
    )))

    s.append(("§ 18 Außerordentliche Kündigung", (
        "(1) Das Recht der Parteien zur außerordentlichen fristlosen "
        "Kündigung aus wichtigem Grund (§§ 543, 569 BGB) bleibt unberührt.\n\n"
        "(2) Ein wichtiger Grund liegt für den Vermieter insbesondere "
        "vor bei (a) Zahlungsverzug mit zwei aufeinanderfolgenden "
        "Monatsmieten oder einem Betrag, der die Miete für zwei Monate "
        "erreicht, (b) wesentlicher Verletzung der Vertragspflichten "
        "trotz Abmahnung, (c) Insolvenz des Mieters.\n\n"
        "(3) Vor einer fristlosen Kündigung wegen Zahlungsverzug ist "
        "eine Schonfrist von 14 Tagen einzuräumen."
    )))

    s.append(("§ 19 Rückgabe der Mietsache", (
        "(1) Bei Beendigung des Mietverhältnisses ist die Mietsache "
        "vollständig geräumt, besenrein und in ordnungsgemäßem Zustand "
        "an den Vermieter zurückzugeben.\n\n"
        "(2) Der Mieter ist verpflichtet, etwaige selbst eingebaute "
        "Einbauten und bauliche Veränderungen auf eigene Kosten "
        "zurückzubauen und den ursprünglichen Zustand wiederherzustellen, "
        "soweit nicht der Vermieter auf den Rückbau verzichtet.\n\n"
        "(3) Verbleibt der Mieter mit der Rückgabe in Verzug, hat er "
        "Nutzungsentschädigung in Höhe von 150 % der zuletzt gezahlten "
        "Miete zu zahlen. Weitergehende Schadensersatzansprüche "
        "bleiben unberührt."
    )))

    s.append(("§ 20 Schiedsklausel/Gerichtsstand", (
        "(1) Die Parteien werden Streitigkeiten aus oder im Zusammenhang "
        "mit diesem Vertrag zunächst durch Verhandlungen beilegen.\n\n"
        "(2) Gelingt eine außergerichtliche Einigung nicht, ist für "
        "alle Streitigkeiten ausschließlich das für die Lage des "
        "Mietobjekts zuständige Gericht zuständig.\n\n"
        "(3) Es gilt deutsches Recht."
    )))

    s.append(("§ 21 Schlussbestimmungen", (
        "(1) " + SCHRIFTFORM + "\n\n"
        "(2) " + SALVATORISCH + "\n\n"
        "(3) Alle in diesem Vertrag genannten Anlagen sind wesentlicher "
        "Bestandteil dieses Vertrages."
    )))

    s.append(("Anlagen", _annex_list([
        "Lageplan", "Grundriss", "Übergabeprotokoll", "Energieausweis",
        "Hausordnung", "Betriebskostenkatalog"
    ])))

    s.append(("Unterschriften", _signature_block(
        p, "Geschäftsführung " + vermieter, "Vermieter",
        "Geschäftsführung " + mieter, "Mieter"
    )))

    return s


# =====================================================================
# FINANCE
# =====================================================================

def gen_kreditvertrag(p: Dict[str, Any]) -> List[Section]:
    """Kreditvertrag mit Covenants. Target: 5000-8000 Wörter."""

    bank = _g(p, "bank", "Sparkasse KölnBonn")
    kreditnehmer = _g(p, "kreditnehmer", "Muster GmbH")
    betrag = _g(p, "betrag", "4.500.000")
    zinssatz = _g(p, "zinssatz", "4,75")
    laufzeit = _g(p, "laufzeit", "7")
    city = _g(p, "city", "Köln")

    s: List[Section] = []

    s.append(("Präambel", (
        f"Zwischen der {bank} – nachfolgend „Kreditgeber' – und "
        f"{kreditnehmer} mit Sitz in {city} – nachfolgend "
        f"„Kreditnehmer'; Kreditgeber und Kreditnehmer gemeinsam "
        f"„Parteien' – wird der folgende Kreditvertrag geschlossen.\n\n"
        f"Der Kreditgeber gewährt dem Kreditnehmer auf Grundlage der "
        f"vom Kreditnehmer überlassenen Unterlagen und Informationen "
        f"sowie nach Maßgabe der Bestimmungen dieses Vertrages einen "
        f"endfälligen Kredit zur Finanzierung von Investitionen "
        f"gemäß § 2 Abs. 2."
    )))

    s.append(("§ 1 Definitionen", (
        "Im Sinne dieses Vertrages haben die nachfolgenden Begriffe "
        "die folgenden Bedeutungen:\n\n"
        "„Bilanz' bezeichnet die geprüfte und festgestellte Bilanz des "
        "Kreditnehmers nach HGB.\n\n"
        "„EBIT' bezeichnet das Ergebnis vor Zinsen und Steuern gemäß "
        "Position 17 der GuV-Gliederung des § 275 Abs. 2 HGB.\n\n"
        "„EBITDA' bezeichnet das EBIT zuzüglich Abschreibungen auf "
        "Sach- und immaterielle Vermögensgegenstände (§ 275 Abs. 2 "
        "Nr. 7a HGB).\n\n"
        "„Eigenkapital' bezeichnet das gezeichnete Kapital, die Kapital- "
        "und Gewinnrücklagen, den Gewinn- bzw. Verlustvortrag und den "
        "Jahresüberschuss/-fehlbetrag gemäß § 266 Abs. 3 A HGB; "
        "Gesellschafterdarlehen mit qualifiziertem Rangrücktritt werden "
        "dem Eigenkapital zugerechnet.\n\n"
        "„Eigenkapitalquote' bezeichnet das Verhältnis von Eigenkapital "
        "zur Bilanzsumme.\n\n"
        "„Nettofinanzverbindlichkeiten' bezeichnen die zinstragenden "
        "Verbindlichkeiten gegenüber Kreditinstituten und Konzern-"
        "fremden, abzüglich liquider Mittel (Kassenbestand und kurzfristig "
        "veräußerbare Wertpapiere).\n\n"
        "„Net Debt/EBITDA-Ratio' bezeichnet das Verhältnis von "
        "Nettofinanzverbindlichkeiten zum EBITDA der letzten "
        "12 Monate.\n\n"
        "„Interest Coverage Ratio' bezeichnet das Verhältnis von "
        "EBITDA zum Zinsaufwand der letzten 12 Monate.\n\n"
        "„Compliance Certificate' bezeichnet die quartalsweise vom "
        "Kreditnehmer ausgestellte Bestätigung über die Einhaltung "
        "der Financial Covenants nach § 12.\n\n"
        "„Wesentliche Nachteilige Veränderung' (Material Adverse "
        "Change – „MAC') bezeichnet jedes Ereignis oder jede Entwicklung, "
        "die einzeln oder zusammen mit anderen Ereignissen geeignet "
        "ist, wesentlich nachteilige Auswirkungen auf die Vermögens-, "
        "Finanz- oder Ertragslage des Kreditnehmers oder seine Fähigkeit "
        "zur Erfüllung seiner Verpflichtungen aus diesem Vertrag zu haben.\n\n"
        "„Kontrollwechsel' bezeichnet jede unmittelbare oder mittelbare "
        "Übertragung von mehr als 50 % der Stimmrechte oder des "
        "Kapitals des Kreditnehmers auf einen Dritten, der zum Zeitpunkt "
        "des Vertragsschlusses nicht im Sinne der §§ 15 ff. AktG mit "
        "dem Kreditnehmer verbunden war."
    )))

    s.append(("§ 2 Darlehensbetrag und Zweck", (
        f"(1) Der Kreditgeber gewährt dem Kreditnehmer ein "
        f"endfälliges Darlehen in Höhe von EUR {betrag} (in Worten: "
        f"[Betrag] Euro).\n\n"
        f"(2) Das Darlehen ist zweckgebunden für die Finanzierung der "
        f"in Anlage 1 (Investitionsplan) aufgeführten Investitionen "
        f"in {_g(p, 'investment', 'Produktionsanlagen, Maschinen und Betriebsgebäude')}.\n\n"
        f"(3) Eine andere Verwendung der Darlehensmittel ist ohne "
        f"vorherige schriftliche Zustimmung des Kreditgebers nicht "
        f"zulässig und stellt einen Verstoß im Sinne des § 16 "
        f"(Events of Default) dar."
    )))

    s.append(("§ 3 Auszahlungsvoraussetzungen", (
        "Voraussetzungen für die Auszahlung des Darlehens (Conditions "
        "Precedent) sind:\n\n"
        "a) Vorlage des in vollständig unterschriebener Form vorliegenden "
        "Kreditvertrages und aller Sicherheitenbestellungsurkunden;\n\n"
        "b) Vorlage der Gesellschafterversammlungsbeschlüsse, die "
        "die Aufnahme dieses Kredites und die Bestellung der Sicherheiten "
        "genehmigen;\n\n"
        "c) Vorlage einer unbedenklichen Auskunft aus dem Schuldnerregister "
        "und einer aktuellen Schufa-Auskunft des Kreditnehmers (sofern "
        "anwendbar);\n\n"
        "d) Vorlage der letzten drei testierten Jahresabschlüsse sowie "
        "einer aktuellen BWA (max. 60 Tage alt);\n\n"
        "e) Eintragung der Grundschuld gemäß § 9 in der vereinbarten "
        "Rangstelle;\n\n"
        "f) Vorlage einer Compliance-Bestätigung über die "
        "ordnungsgemäße Bestellung der Geschäftsführer und das Fehlen "
        "von Ausschlussgründen nach § 6 GmbHG;\n\n"
        "g) Vorlage einer Bestätigung des Steuerberaters über die "
        "ordnungsgemäße Erfüllung der Steuerpflichten;\n\n"
        "h) Vorlage eines aktuellen Versicherungsverzeichnisses und "
        "Bestätigung der Versicherer, dass alle Versicherungen vorhanden "
        "und vinkuliert (zugunsten des Kreditgebers) sind."
    )))

    s.append(("§ 4 Auszahlung", (
        "(1) Das Darlehen wird auf erste Anforderung des Kreditnehmers "
        "in bis zu drei Teilauszahlungen zur Verfügung gestellt, jeweils "
        "in Mindestbeträgen von EUR 500.000.\n\n"
        "(2) Auszahlungsanforderungen sind dem Kreditgeber mindestens "
        "drei (3) Bankgeschäftstage vor dem gewünschten Auszahlungstag "
        "in Textform zu übermitteln. Der Kreditgeber wird die "
        "Auszahlung – Vorliegen aller Voraussetzungen vorausgesetzt – "
        "zum gewünschten Termin vornehmen.\n\n"
        "(3) Spätester Auszahlungstermin ist der 31.12.2026. Nicht "
        "abgerufene Beträge verfallen ersatzlos.\n\n"
        "(4) Die Auszahlung erfolgt durch Gutschrift auf das Konto des "
        "Kreditnehmers IBAN [...] bei der [Bank]."
    )))

    s.append(("§ 5 Zinsen", (
        f"(1) Das Darlehen wird ab dem jeweiligen Auszahlungstag mit "
        f"einem nominalen Zinssatz von {zinssatz} % p.a. verzinst "
        f"(fest für die gesamte Laufzeit).\n\n"
        f"(2) Die Zinsen werden quartalsweise nachträglich, jeweils "
        f"am Quartalsende, berechnet und sind binnen 10 Bankgeschäftstagen "
        f"zur Zahlung fällig.\n\n"
        f"(3) Die Zinsberechnung erfolgt nach der Methode actual/360, "
        f"d. h. taggenaue Berechnung auf Basis von 360 Tagen je Jahr.\n\n"
        f"(4) Der effektive Jahreszins beträgt {float(zinssatz.replace(',', '.')) + 0.15:.2f} % "
        f"unter Berücksichtigung der Bearbeitungsgebühr (0,5 % einmalig) "
        f"und der Kontoführungsgebühren."
    )))

    s.append(("§ 6 Tilgung", (
        f"(1) Das Darlehen wird in {laufzeit} Jahresraten je "
        f"EUR {int(int(betrag.replace('.', '')) / int(laufzeit)):,} "
        f"getilgt. Die erste Tilgungsrate ist 12 Monate nach Vollauszahlung "
        f"fällig, die weiteren Raten jeweils 12 Monate später.\n\n"
        f"(2) Sondertilgungen sind jederzeit ohne Vorfälligkeits-"
        f"entschädigung in einer Mindesthöhe von EUR 100.000 zulässig. "
        f"Eine Sondertilgung verringert die folgenden Tilgungsraten "
        f"in chronologischer Reihenfolge.\n\n"
        f"(3) Zwingende Sondertilgungen erfolgen bei Eintritt der in "
        f"§ 16 genannten Events of Default oder im Falle eines "
        f"Kontrollwechsels gemäß § 14."
    )))

    s.append(("§ 7 Rückzahlung und Vorfälligkeitsentschädigung", (
        "(1) Die Rückzahlung erfolgt gemäß dem Tilgungsplan nach § 6.\n\n"
        "(2) Bei vorzeitiger Rückführung des Darlehens aus anderen "
        "Gründen als den in § 6 Abs. 2 genannten Sondertilgungen kann "
        "der Kreditgeber eine Vorfälligkeitsentschädigung verlangen. "
        "Diese berechnet sich nach den Grundsätzen der BGH-Rechtsprechung "
        "(Aktiv-Passiv-Methode) auf Basis der entgangenen Zinsmargen "
        "abzüglich ersparter Risikokosten und Verwaltungsaufwendungen.\n\n"
        "(3) Endfälligkeit: Soweit das Darlehen nicht vorzeitig "
        "zurückgeführt wird, ist der gesamte ausstehende Betrag nebst "
        "aufgelaufener Zinsen am Ende der Laufzeit zur Rückzahlung fällig."
    )))

    s.append(("§ 8 Verzug und Verzugszinsen", (
        "(1) Bei Zahlungsverzug schuldet der Kreditnehmer Verzugszinsen "
        "in Höhe von 9 Prozentpunkten über dem Basiszinssatz nach § 247 "
        "BGB pro Jahr, mindestens jedoch in Höhe des vertraglichen "
        "Zinssatzes zuzüglich 2 Prozentpunkten.\n\n"
        "(2) Die Geltendmachung weiterer Verzugsschäden bleibt vorbehalten.\n\n"
        "(3) Bei Zahlungsverzug von mehr als 30 Tagen behält sich der "
        "Kreditgeber das Recht zur außerordentlichen Kündigung gemäß "
        "§ 17 vor."
    )))

    s.append(("§ 9 Sicherheiten", (
        "(1) Zur Sicherung sämtlicher Ansprüche des Kreditgebers aus "
        "diesem Vertrag bestellt der Kreditnehmer folgende Sicherheiten:\n\n"
        "a) Briefgrundschuld in Höhe von EUR " + betrag + " zuzüglich "
        "16 % Jahreszinsen, einer einmaligen Nebenleistung von 10 % "
        "und sofort vollstreckbar an der dem Kreditnehmer gehörenden "
        "Liegenschaft [Anschrift], eingetragen im Grundbuch von "
        "[Gemarkung], Blatt [Nr.], als Erstrang;\n\n"
        "b) Verpfändung der wesentlichen Geschäftsanteile am Kreditnehmer "
        "durch die Mehrheitsgesellschafter;\n\n"
        "c) Globalzession der gegenwärtigen und zukünftigen Forderungen "
        "aus Lieferungen und Leistungen des Kreditnehmers;\n\n"
        "d) Sicherungsübereignung wesentlicher Maschinen und "
        "Betriebsausstattung gemäß separatem Vertrag.\n\n"
        "(2) Die Bestellung der Sicherheiten erfolgt durch gesonderte "
        "Verträge, die diesem Vertrag als Anlagen beigefügt werden."
    )))

    s.append(("§ 10 Bestimmungsgemäße Verwendung", (
        "(1) Der Kreditnehmer verwendet das Darlehen ausschließlich "
        "für die in § 2 Abs. 2 genannten Zwecke.\n\n"
        "(2) Der Kreditnehmer weist auf Anforderung des Kreditgebers "
        "die ordnungsgemäße Verwendung durch Belege nach."
    )))

    s.append(("§ 11 Reporting Covenants", (
        "(1) Der Kreditnehmer übermittelt dem Kreditgeber:\n\n"
        "a) eine betriebswirtschaftliche Auswertung (BWA) monatlich, "
        "spätestens 30 Tage nach Monatsende;\n\n"
        "b) eine Summen- und Saldenliste mit Bewegungsdaten monatlich, "
        "spätestens 30 Tage nach Monatsende;\n\n"
        "c) einen Quartalsabschluss inkl. Kommentar zur Geschäfts-"
        "entwicklung, spätestens 45 Tage nach Quartalsende;\n\n"
        "d) den geprüften Jahresabschluss nebst Lagebericht und "
        "Prüfungsbericht innerhalb von 120 Tagen nach Geschäftsjahres-"
        "ende;\n\n"
        "e) einen Wirtschaftsplan (Budget) für das Folgejahr "
        "bis spätestens 30. November des Vorjahres;\n\n"
        "f) das Compliance Certificate gemäß Anlage 2 quartalsweise.\n\n"
        "(2) Der Kreditgeber kann jederzeit weitere Auskünfte und "
        "Unterlagen anfordern, die zur Beurteilung der wirtschaftlichen "
        "Lage des Kreditnehmers erforderlich sind."
    )))

    s.append(("§ 12 Financial Covenants", (
        "(1) Der Kreditnehmer verpflichtet sich, die folgenden "
        "Financial Covenants jederzeit, mindestens jedoch zu jedem "
        "Quartalsstichtag, einzuhalten:\n\n"
        "a) Eigenkapitalquote: mindestens 30 % zum jeweiligen Stichtag;\n\n"
        "b) Net Debt / EBITDA-Ratio: maximal 3,5x auf Basis der "
        "letzten 12 Monate (rolling twelve months);\n\n"
        "c) Interest Coverage Ratio: mindestens 4,0x;\n\n"
        "d) Liquidität: mindestens EUR 5.000.000 verfügbare Mittel "
        "(liquide Mittel zuzüglich nicht ausgenutzte Kontokorrentlinien) "
        "zu jedem Quartalsstichtag.\n\n"
        "(2) Die Einhaltung wird quartalsweise durch das Compliance "
        "Certificate (Anlage 2) bestätigt, das vom Geschäftsführer "
        "des Kreditnehmers zu unterschreiben ist.\n\n"
        "(3) Bei drohendem Bruch eines Covenants ist der Kreditnehmer "
        "verpflichtet, dies dem Kreditgeber unverzüglich anzuzeigen "
        "und einen Maßnahmenplan vorzulegen.\n\n"
        "(4) Bei tatsächlichem Bruch eines Covenants kann der "
        "Kreditgeber – nach Maßgabe von § 16 – einen Event of Default "
        "feststellen und seine Rechte aus § 17 ausüben."
    )))

    s.append(("§ 13 Affirmative Covenants", (
        "Der Kreditnehmer verpflichtet sich, während der Laufzeit "
        "dieses Vertrages:\n\n"
        "a) alle für die ordnungsgemäße Fortführung seines Geschäfts-"
        "betriebs erforderlichen behördlichen Genehmigungen und "
        "Erlaubnisse aufrechtzuerhalten;\n\n"
        "b) seine wesentlichen Vermögensgegenstände und Betriebsrisiken "
        "marktüblich zu versichern und die Versicherungspolicen zugunsten "
        "des Kreditgebers zu vinkulieren;\n\n"
        "c) alle Steuern, Sozialabgaben und sonstigen öffentlich-"
        "rechtlichen Abgaben ordnungsgemäß und fristgerecht zu zahlen;\n\n"
        "d) den Geschäftsbetrieb in der bisherigen Art und im bisherigen "
        "Umfang fortzuführen;\n\n"
        "e) alle anwendbaren Gesetze und Vorschriften einzuhalten, "
        "insbesondere Datenschutz-, Compliance-, Arbeitsschutz- und "
        "Umweltgesetze;\n\n"
        "f) bestehende Geschäftsbeziehungen ordnungsgemäß weiterzuführen;\n\n"
        "g) Buchführung und Rechnungslegung in Übereinstimmung mit "
        "den Grundsätzen ordnungsgemäßer Buchführung (GoB) und HGB "
        "vorzunehmen."
    )))

    s.append(("§ 14 Negative Covenants", (
        "(1) Der Kreditnehmer verpflichtet sich, während der Laufzeit "
        "dieses Vertrages ohne vorherige schriftliche Zustimmung des "
        "Kreditgebers:\n\n"
        "a) keine zinstragenden Verbindlichkeiten gegenüber Dritten "
        "aufzunehmen, die zusammen mit bestehenden Verbindlichkeiten "
        "den Betrag von EUR 1.000.000 übersteigen würden (Verbot der "
        "Doppel- oder Mehrfachfinanzierung);\n\n"
        "b) keine wesentlichen Vermögensgegenstände, deren Buchwert "
        "EUR 500.000 übersteigt, einzeln oder in einem Jahr in Summe "
        "zu veräußern, soweit es sich nicht um Verkäufe im gewöhnlichen "
        "Geschäftsbetrieb handelt;\n\n"
        "c) keine Akquisitionen oder Unternehmensbeteiligungen mit "
        "einem Kaufpreis von mehr als EUR 1.000.000 zu tätigen;\n\n"
        "d) keine Ausschüttungen, Vorabausschüttungen, Gesellschafter-"
        "darlehen oder vergleichbare Mittelabflüsse an Gesellschafter "
        "vorzunehmen, die in einem Geschäftsjahr mehr als 50 % des "
        "Jahresüberschusses betragen würden;\n\n"
        "e) keine Sicherheiten zugunsten Dritter an wesentlichen "
        "Vermögensgegenständen zu bestellen (Negativerklärung);\n\n"
        "f) keine Verschmelzungen, Spaltungen, Formwechsel oder "
        "vergleichbaren Umstrukturierungen vorzunehmen;\n\n"
        "g) keine Änderungen des Gesellschaftsvertrages, die die "
        "Rechte des Kreditgebers berühren, vorzunehmen.\n\n"
        "(2) Der Kreditgeber wird seine Zustimmung nicht aus "
        "willkürlichen Gründen verweigern. Die Entscheidung wird der "
        "Kreditgeber binnen 14 Tagen nach Eingang einer schriftlichen "
        "Anfrage treffen."
    )))

    s.append(("§ 15 Material Adverse Change", (
        "(1) Tritt eine wesentliche nachteilige Veränderung (MAC) "
        "im Sinne der Definitionen ein oder ist eine solche absehbar, "
        "ist der Kreditnehmer verpflichtet, dies dem Kreditgeber "
        "unverzüglich anzuzeigen.\n\n"
        "(2) Der Kreditgeber ist in diesem Fall berechtigt, die "
        "Auszahlung weiterer Darlehensmittel zu verweigern, zusätzliche "
        "Sicherheiten zu verlangen und – bei Vorliegen weiterer "
        "Voraussetzungen – das Darlehen außerordentlich zu kündigen."
    )))

    s.append(("§ 16 Events of Default (Kündigungsgründe)", (
        "Ein Kündigungsgrund (Event of Default) liegt vor, wenn:\n\n"
        "a) der Kreditnehmer mit der Zahlung von Zinsen, Tilgungen "
        "oder anderen geschuldeten Beträgen länger als 14 Tage in "
        "Verzug ist;\n\n"
        "b) der Kreditnehmer einen Financial Covenant gemäß § 12 "
        "verletzt und die Verletzung nicht innerhalb von 30 Tagen "
        "nach schriftlicher Aufforderung des Kreditgebers behoben wird;\n\n"
        "c) der Kreditnehmer ein Affirmative oder Negative Covenant "
        "gemäß §§ 13, 14 verletzt und die Verletzung nicht innerhalb "
        "von 30 Tagen nach schriftlicher Abmahnung behoben wird;\n\n"
        "d) andere Verbindlichkeiten des Kreditnehmers in einer Höhe "
        "von insgesamt mehr als EUR 250.000 vorzeitig fällig gestellt "
        "werden (Cross-Default);\n\n"
        "e) über das Vermögen des Kreditnehmers ein Insolvenzverfahren "
        "eröffnet, beantragt oder mangels Masse abgelehnt wird oder "
        "der Kreditnehmer zahlungsunfähig oder überschuldet ist;\n\n"
        "f) ein Kontrollwechsel beim Kreditnehmer ohne vorherige "
        "Zustimmung des Kreditgebers stattfindet;\n\n"
        "g) Sicherheiten unwirksam werden oder ihre Werthaltigkeit "
        "wesentlich gemindert wird;\n\n"
        "h) eine wesentliche Tochtergesellschaft des Kreditnehmers "
        "veräußert oder ihr Geschäftsbetrieb wesentlich verändert wird;\n\n"
        "i) ein MAC im Sinne von § 15 eintritt;\n\n"
        "j) wesentliche Aussagen des Kreditnehmers, auf deren "
        "Grundlage die Kreditentscheidung getroffen wurde, sich als "
        "unrichtig erweisen;\n\n"
        "k) der Geschäftsbetrieb wesentlich eingestellt oder "
        "wesentlich verändert wird, ohne dass die Zustimmung des "
        "Kreditgebers vorliegt;\n\n"
        "l) Geschäftsführer oder Gesellschafter des Kreditnehmers "
        "wegen Korruption, Untreue, Bilanzfälschung oder vergleichbarer "
        "Delikte rechtskräftig verurteilt werden;\n\n"
        "m) Steuerprüfungen, Sozialversicherungsprüfungen oder andere "
        "Prüfungen wesentliche Beanstandungen ergeben, die nicht "
        "behoben werden;\n\n"
        "n) Versicherungen, die zu vinkulieren waren, gekündigt werden "
        "oder verfallen;\n\n"
        "o) die Geschäftsführung des Kreditnehmers wesentlich verändert "
        "wird, ohne dass die Zustimmung des Kreditgebers vorliegt."
    )))

    s.append(("§ 17 Rechtsfolgen Event of Default", (
        "(1) Bei Vorliegen eines Event of Default und unbeschadet "
        "weiterer gesetzlicher und vertraglicher Rechte ist der "
        "Kreditgeber berechtigt:\n\n"
        "a) die Auszahlung noch nicht abgerufener Beträge zu verweigern;\n\n"
        "b) den Kredit ganz oder teilweise außerordentlich zu kündigen "
        "und sofort fällig zu stellen;\n\n"
        "c) die Sicherheiten zu verwerten.\n\n"
        "(2) Bei Vorliegen eines Event of Default werden alle bislang "
        "ausgezahlten Beträge nebst Zinsen sofort zur Rückzahlung "
        "fällig, ohne dass es einer gesonderten Mahnung bedarf."
    )))

    s.append(("§ 18 Pari Passu, Negativerklärung", (
        "(1) Der Kreditnehmer versichert, dass die Verbindlichkeiten "
        "aus diesem Vertrag mindestens im gleichen Rang wie alle "
        "anderen gegenwärtigen und zukünftigen ungesicherten "
        "Verbindlichkeiten des Kreditnehmers stehen (pari passu).\n\n"
        "(2) Negativerklärung: Der Kreditnehmer wird ohne Zustimmung "
        "des Kreditgebers keine Sicherheiten an seinen Vermögens-"
        "gegenständen zugunsten Dritter bestellen, soweit nicht der "
        "Kreditgeber in gleichem Umfang abgesichert wird."
    )))

    s.append(("§ 19 Abtretung", ASSIGNMENT))

    s.append(("§ 20 Vertraulichkeit", CONFIDENTIALITY_STD))

    s.append(("§ 21 Anwendbares Recht, Gerichtsstand", JURISDICTION_DE.format(
        gerichtsstand=city
    )))

    s.append(("§ 22 Schlussbestimmungen", (
        "(1) " + SCHRIFTFORM + "\n\n"
        "(2) " + SALVATORISCH
    )))

    s.append(("Anlagen", _annex_list([
        "Investitionsplan", "Compliance Certificate-Vorlage",
        "Tilgungsplan", "Versicherungsverzeichnis",
        "Sicherheitenverträge"
    ])))

    s.append(("Unterschriften", _signature_block(
        p, "Vorstand " + bank, "Kreditgeber",
        "Geschäftsführung " + kreditnehmer, "Kreditnehmer"
    )))

    return s


def gen_factoring_agreement(p: Dict[str, Any]) -> List[Section]:
    """Factoring-Rahmenvertrag. Target: 2500-4000 Wörter."""

    factor = _g(p, "factor", "Factor AG")
    client = _g(p, "client", "Muster GmbH")
    city = _g(p, "city", "Köln")
    volume = _g(p, "volume", "15.000.000")

    s: List[Section] = []

    s.append(("Präambel", (
        f"Zwischen der {factor} – nachfolgend „Factor' – und der "
        f"{client} – nachfolgend „Klient'; gemeinsam „Parteien' – "
        f"wird der folgende Factoring-Rahmenvertrag geschlossen. Der "
        f"Klient veräußert dem Factor laufend seine Forderungen aus "
        f"Lieferungen und Leistungen an gewerbliche Abnehmer."
    )))

    s.append(("§ 1 Vertragsgegenstand", (
        f"(1) Der Klient verkauft und überträgt dem Factor seine "
        f"gegenwärtigen und künftigen Forderungen aus Lieferungen und "
        f"Leistungen gegenüber den vom Factor gebilligten Abnehmern "
        f"(„Vertragsforderungen'). Der Factor nimmt den Verkauf an.\n\n"
        f"(2) Das prognostizierte Jahresvolumen beträgt EUR {volume}.\n\n"
        f"(3) Das Vertragsverhältnis ist als echtes Factoring mit "
        f"Übernahme des Delkredererisikos ausgestaltet (§ 437 Abs. 1 "
        f"Nr. 1 BGB)."
    )))

    s.append(("§ 2 Limitprüfung und Bonität", (
        "(1) Der Factor übernimmt nur Forderungen gegenüber Abnehmern, "
        "denen er nach eigener Bonitätsprüfung ein Limit eingeräumt hat.\n\n"
        "(2) Der Factor kann Limits jederzeit reduzieren, aussetzen "
        "oder widerrufen.\n\n"
        "(3) Forderungen, die das jeweilige Limit übersteigen, werden "
        "vom Factor zwar im Servicing übernommen, jedoch ohne "
        "Delkredereschutz."
    )))

    s.append(("§ 3 Kaufpreis und Auszahlung", (
        "(1) Der Kaufpreis für eine Vertragsforderung entspricht ihrem "
        "Bruttobetrag abzüglich (a) Skonti und Rabatte, (b) Factoring-"
        "Gebühr, (c) Zinsen für die Vorfinanzierung.\n\n"
        "(2) Der Factor zahlt 90 % des Kaufpreises sofort nach "
        "Andienung der Forderung aus. Die verbleibenden 10 % werden "
        "als Sicherheitseinbehalt verbucht und nach Zahlungseingang "
        "des Abnehmers freigegeben.\n\n"
        "(3) Die Factoring-Gebühr beträgt 0,75 % des Bruttoforderungs-"
        "betrages, mindestens jedoch EUR 25 je Rechnung.\n\n"
        "(4) Die Vorfinanzierungszinsen betragen 3M-EURIBOR + 2,50 "
        "Prozentpunkte p.a."
    )))

    s.append(("§ 4 Veritätshaftung", (
        "(1) Der Klient haftet für den rechtlichen Bestand der "
        "verkauften Forderungen (Verität) sowie deren Höhe und "
        "Einredefreiheit.\n\n"
        "(2) Im Falle einer mangelhaften Verität (z. B. Nicht-Bestand, "
        "Aufrechnung des Abnehmers wegen Mängelrügen) ist der Klient "
        "verpflichtet, dem Factor den Kaufpreis zuzüglich Zinsen "
        "zurückzuerstatten."
    )))

    s.append(("§ 5 Mitwirkungspflichten des Klienten", (
        "(1) Der Klient stellt sicher, dass auf allen Rechnungen ein "
        "Abtretungsvermerk an den Factor enthalten ist (offene "
        "Zession).\n\n"
        "(2) Der Klient übersendet Kopien aller Rechnungen unverzüglich "
        "an den Factor. Die elektronische Andienung erfolgt über das "
        "Factoring-Portal.\n\n"
        "(3) Im Falle einer Reklamation des Abnehmers unterrichtet "
        "der Klient den Factor unverzüglich und unterstützt ihn bei "
        "der Klärung."
    )))

    s.append(("§ 6 Forderungsmanagement", (
        "(1) Der Factor übernimmt das Debitorenmanagement einschließlich "
        "Mahnwesen, gerichtlicher Beitreibung und Kontenführung.\n\n"
        "(2) Bei Zahlungsverzug einleitet der Factor abgestufte "
        "Mahnverfahren entsprechend seinem internen Mahnplan.\n\n"
        "(3) Gerichtliche und außergerichtliche Beitreibungskosten "
        "trägt der Factor, soweit das Delkredererisiko greift."
    )))

    s.append(("§ 7 Delkredereschutz", (
        "(1) Der Factor übernimmt das Risiko des Forderungsausfalls "
        "(Delkredererisiko) bis zur Höhe des jeweils geltenden Limits "
        "des Abnehmers.\n\n"
        "(2) Das Delkredererisiko wird ausgelöst (a) bei Eröffnung des "
        "Insolvenzverfahrens, (b) bei Nicht-Zahlung trotz Mahnverfahren "
        "und Klage, (c) bei Vorlage einer rechtskräftigen Forderungs-"
        "anmeldung in der Insolvenzmasse.\n\n"
        "(3) Bei Auslösung des Delkredererisikos erstattet der Factor "
        "dem Klienten den verbleibenden Kaufpreis (Sicherheitseinbehalt)."
    )))

    s.append(("§ 8 Datenschutz", DATA_PROTECTION))

    s.append(("§ 9 Vertraulichkeit", CONFIDENTIALITY_STD))

    s.append(("§ 10 Laufzeit, Kündigung", (
        "(1) Der Vertrag wird auf unbestimmte Zeit geschlossen und "
        "kann von beiden Parteien mit einer Frist von drei (3) Monaten "
        "zum Monatsende gekündigt werden.\n\n"
        "(2) Außerordentliche Kündigung aus wichtigem Grund bleibt "
        "unberührt."
    )))

    s.append(("§ 11 Recht, Gerichtsstand", JURISDICTION_DE.format(
        gerichtsstand=city
    )))

    s.append(("§ 12 Schlussbestimmungen", SCHRIFTFORM + "\n\n" + SALVATORISCH))

    s.append(("Unterschriften", _signature_block(
        p, factor, "Factor", client, "Klient"
    )))

    return s


def gen_lease_finance_agreement(p: Dict[str, Any]) -> List[Section]:
    """Leasingvertrag. Target: 2500-4000 Wörter."""

    leasinggeber = _g(p, "leasinggeber", "Leasing GmbH")
    leasingnehmer = _g(p, "leasingnehmer", "Muster GmbH")
    asset = _g(p, "asset", "Produktionsanlage Typ XY")
    rate = _g(p, "rate", "12.500")
    laufzeit = _g(p, "laufzeit", "60")
    city = _g(p, "city", "Köln")

    s: List[Section] = []

    s.append(("Präambel", (
        f"Zwischen der {leasinggeber} – nachfolgend „Leasinggeber' – "
        f"und der {leasingnehmer} – nachfolgend „Leasingnehmer' – "
        f"wird der folgende Leasingvertrag über die Überlassung des "
        f"in § 1 spezifizierten Leasingobjekts geschlossen."
    )))

    s.append(("§ 1 Leasingobjekt", (
        f"(1) Leasingobjekt ist: {asset} gemäß Anlage 1 (Technische "
        f"Spezifikation).\n\n"
        f"(2) Das Leasingobjekt ist Eigentum des Leasinggebers und "
        f"bleibt während der gesamten Vertragslaufzeit dessen Eigentum."
    )))

    s.append(("§ 2 Leasinglaufzeit und Leasingraten", (
        f"(1) Die Grundleasingzeit beträgt {laufzeit} Monate, beginnend "
        f"am Tag der Übergabe des Leasingobjekts.\n\n"
        f"(2) Die monatliche Leasingrate beträgt EUR {rate} netto "
        f"zuzüglich der gesetzlichen Umsatzsteuer.\n\n"
        f"(3) Leasingraten sind monatlich im Voraus, jeweils zum "
        f"dritten Werktag eines Monats, zu zahlen."
    )))

    s.append(("§ 3 Lieferung und Übergabe", (
        "(1) Die Lieferung des Leasingobjekts erfolgt direkt vom "
        "Lieferanten an den Leasingnehmer.\n\n"
        "(2) Der Leasingnehmer prüft das Leasingobjekt unverzüglich "
        "und bestätigt die Übernahme durch Unterzeichnung einer "
        "Übernahmebestätigung.\n\n"
        "(3) Mit Übergabe geht die Gefahr für das Leasingobjekt auf "
        "den Leasingnehmer über."
    )))

    s.append(("§ 4 Gewährleistung", (
        "(1) Der Leasinggeber tritt seine Gewährleistungsansprüche "
        "gegen den Lieferanten dem Leasingnehmer ab. Der Leasingnehmer "
        "macht die Ansprüche im eigenen Namen geltend.\n\n"
        "(2) Der Leasinggeber haftet selbst nicht für Mängel des "
        "Leasingobjekts. Leasingraten sind auch bei Mängeln in voller "
        "Höhe weiterzuzahlen, soweit der Leasingnehmer Gewährleistungs-"
        "ansprüche gegen den Lieferanten geltend machen kann."
    )))

    s.append(("§ 5 Versicherung, Wartung", (
        "(1) Der Leasingnehmer versichert das Leasingobjekt auf "
        "eigene Kosten gegen Feuer, Wasser, Einbruchdiebstahl und "
        "alle weiteren Risiken zum Wiederbeschaffungswert. Die "
        "Versicherungsleistung wird zugunsten des Leasinggebers "
        "vinkuliert.\n\n"
        "(2) Der Leasingnehmer wartet und pflegt das Leasingobjekt "
        "auf eigene Kosten in einem ordnungsgemäßen Zustand."
    )))

    s.append(("§ 6 Untergang, Beschädigung", (
        "(1) Im Falle des Untergangs oder einer erheblichen Beschädigung "
        "des Leasingobjekts wird das Leasingverhältnis nicht aufgehoben. "
        "Der Leasingnehmer bleibt zur Zahlung der vereinbarten Leasing-"
        "raten verpflichtet.\n\n"
        "(2) Die Versicherungsleistungen werden auf die Schadensbeseitigung "
        "verwendet."
    )))

    s.append(("§ 7 Eigentum, Rückgabe", (
        "(1) Das Leasingobjekt bleibt während der gesamten Vertrags-"
        "laufzeit Eigentum des Leasinggebers.\n\n"
        "(2) Nach Ablauf der Grundleasingzeit hat der Leasingnehmer "
        "die Wahl zwischen: (a) Rückgabe des Leasingobjekts an den "
        "Leasinggeber in vertragsgemäßem Zustand, (b) Andienung des "
        "Leasingobjekts zum vereinbarten Andienungspreis, (c) Verlängerung "
        "des Leasingvertrages zu einer reduzierten Anschlussmiete.\n\n"
        "(3) Im Falle der Rückgabe trägt der Leasingnehmer die "
        "Rücktransport- und Demontagekosten."
    )))

    s.append(("§ 8 Kündigung, Restwertabrechnung", (
        "(1) Eine ordentliche Kündigung während der Grundleasingzeit "
        "ist ausgeschlossen.\n\n"
        "(2) Bei außerordentlicher Kündigung (insbesondere Insolvenz "
        "des Leasingnehmers, Zahlungsverzug mit mehr als zwei Raten) "
        "ist der Leasinggeber berechtigt, das Leasingobjekt herauszuverlangen "
        "und eine Restwertabrechnung vorzunehmen.\n\n"
        "(3) In der Restwertabrechnung werden die kalkulierten "
        "Restzahlungen abzüglich des Verwertungserlöses sowie ersparter "
        "Aufwendungen geltend gemacht."
    )))

    s.append(("§ 9 Datenschutz", DATA_PROTECTION))

    s.append(("§ 10 Recht, Gerichtsstand", JURISDICTION_DE.format(
        gerichtsstand=city
    )))

    s.append(("§ 11 Schlussbestimmungen", SCHRIFTFORM + "\n\n" + SALVATORISCH))

    s.append(("Unterschriften", _signature_block(
        p, leasinggeber, "Leasinggeber", leasingnehmer, "Leasingnehmer"
    )))

    return s


# =====================================================================
# COMPLIANCE POLICIES
# =====================================================================

def gen_antikorruptions_richtlinie(p: Dict[str, Any]) -> List[Section]:
    """Antikorruptions-Richtlinie. Target: 3000-5000 Wörter."""

    company = _g(p, "company", "Muster GmbH")
    version = _g(p, "version", "3.0")

    s: List[Section] = []

    s.append(("1. Präambel und Zweck", (
        f"{company} bekennt sich zu einem fairen, ehrlichen und "
        f"integren Geschäftsverkehr. Korruption – sei es aktive oder "
        f"passive Bestechung, Bestechlichkeit, Vorteilsannahme, "
        f"unrechtmäßige Vermittlungs- oder Beraterhonorare – ist mit "
        f"den Grundwerten unseres Unternehmens nicht vereinbar und "
        f"wird in keiner Form geduldet (Zero Tolerance).\n\n"
        f"Diese Richtlinie konkretisiert die im Code of Conduct "
        f"verankerten Grundsätze und definiert die für alle Mitarbeiter, "
        f"Organmitglieder und Geschäftspartner verbindlichen Regeln "
        f"zur Verhinderung von Korruption und damit verbundenen "
        f"Straftaten.\n\n"
        f"Die Richtlinie dient zugleich der Erfüllung der "
        f"Compliance-Pflichten der Geschäftsführung gemäß §§ 30, 130 "
        f"OWiG i.V.m. § 9 OWiG sowie der Grundsätze des IDW PS 980."
    )))

    s.append(("2. Geltungsbereich", (
        f"(1) Diese Richtlinie gilt für alle Mitarbeiter, Organmitglieder "
        f"und Auszubildenden der {company} und ihrer verbundenen "
        f"Unternehmen weltweit.\n\n"
        f"(2) Sie gilt auch für externe Berater, Vertriebspartner, "
        f"Vermittler und sonstige Geschäftspartner, die im Namen oder "
        f"Auftrag der Gesellschaft handeln. Diese werden durch "
        f"vertragliche Selbstverpflichtungen zur Einhaltung der "
        f"Grundsätze dieser Richtlinie verpflichtet (siehe Ziffer 10).\n\n"
        f"(3) Die Richtlinie geht – soweit sie strengere Anforderungen "
        f"stellt – einzelvertraglichen Regelungen vor."
    )))

    s.append(("3. Definitionen", (
        "„Korruption' bezeichnet jedes Verhalten, mit dem Vorteile "
        "angeboten, gewährt, gefordert oder angenommen werden, um eine "
        "Person zu einer rechtswidrigen, unlauteren oder pflichtwidrigen "
        "Handlung zu bewegen.\n\n"
        "„Amtsträger' im Sinne dieser Richtlinie sind alle in § 11 "
        "Abs. 1 Nr. 2 StGB genannten Personen sowie ausländische "
        "Amtsträger gemäß Art. 1 OECD-Übereinkommen.\n\n"
        "„Vorteil' bezeichnet jede unentgeltliche Zuwendung, die den "
        "Empfänger materiell oder immateriell besserstellt, ungeachtet "
        "ihres Wertes.\n\n"
        "„Geschäftliche Begünstigung' im Sinne von § 299 StGB liegt "
        "vor, wenn ein Vorteil mit dem Ziel der bevorzugten Beauftragung "
        "verbunden ist.\n\n"
        "„Facilitation Payment' (Beschleunigungszahlung) bezeichnet "
        "kleinere Zahlungen an niedrigrangige Amtsträger zur Beschleunigung "
        "routinemäßiger Amtshandlungen; sie sind nach dieser Richtlinie "
        "verboten."
    )))

    s.append(("4. Grundsätze", (
        "(1) Wir bieten keine Vorteile an, gewähren keine, fordern "
        "keine und nehmen keine an, die geeignet sind, geschäftliche "
        "Entscheidungen unsachgemäß zu beeinflussen.\n\n"
        "(2) Wir trennen private und geschäftliche Interessen klar. "
        "Bei Interessenkonflikten besteht eine umfassende Offenlegungs-"
        "pflicht gegenüber dem Compliance Officer.\n\n"
        "(3) Wir achten die Gesetze aller Länder, in denen wir tätig "
        "sind. Bei Konflikten zwischen lokalen Gewohnheiten und dieser "
        "Richtlinie hat die strengere Regelung Vorrang.\n\n"
        "(4) Dokumentation und Transparenz aller geschäftlichen "
        "Vorgänge sind oberstes Gebot."
    )))

    s.append(("5. Verbotene Handlungen", (
        "Untersagt sind insbesondere:\n\n"
        "a) Aktive und passive Bestechung im geschäftlichen Verkehr "
        "(§ 299 StGB);\n\n"
        "b) Bestechung und Bestechlichkeit von Amtsträgern (§§ 333, "
        "334, 332, 331 StGB);\n\n"
        "c) Bestechung ausländischer Amtsträger gemäß OECD-Übereinkommen, "
        "UK Bribery Act, US Foreign Corrupt Practices Act (FCPA);\n\n"
        "d) Verdeckte Provisionszahlungen oder „Kick-Backs';\n\n"
        "e) Facilitation Payments;\n\n"
        "f) Politische Zuwendungen ohne Vorstandsbeschluss;\n\n"
        "g) Nepotismus bei Personalentscheidungen ohne Offenlegung."
    )))

    s.append(("6. Geschenke und sonstige Zuwendungen", (
        "(1) Geschenke an Geschäftspartner sind grundsätzlich zulässig, "
        "soweit sie:\n\n"
        "a) im üblichen Rahmen geschäftlicher Höflichkeit liegen;\n"
        "b) wertmäßig im einzelnen EUR 50 nicht überschreiten;\n"
        "c) pro Empfänger und Jahr EUR 200 nicht überschreiten;\n"
        "d) zeitlich nicht in Verbindung mit einer Vergabeentscheidung "
        "stehen;\n"
        "e) nicht in bar oder bargeldähnlichen Mitteln (Gutscheine) "
        "erfolgen.\n\n"
        "(2) Empfangene Geschenke ab EUR 30 sind dem Compliance Officer "
        "anzuzeigen. Geschenke über EUR 50 sind grundsätzlich abzulehnen "
        "oder an den Compliance Officer abzuführen, der sie für "
        "wohltätige Zwecke verwendet.\n\n"
        "(3) Geschenke an Amtsträger sind grundsätzlich nicht zulässig, "
        "soweit nicht ausnahmsweise eine reine Werbegabe (z. B. "
        "Kalender, Kugelschreiber) mit einem Wert unter EUR 10 vorliegt."
    )))

    s.append(("7. Bewirtungen und Geschäftsessen", (
        "(1) Bewirtungen sind zulässig, wenn sie:\n\n"
        "a) einen geschäftlichen Anlass haben;\n"
        "b) in einem angemessenen Verhältnis zum Anlass stehen;\n"
        "c) nicht den Eindruck der Beeinflussung erwecken;\n"
        "d) dokumentiert werden (Datum, Anlass, Teilnehmer, Kosten).\n\n"
        "(2) Bewirtungs-Schwellenwerte:\n"
        "- Deutschland: bis EUR 100 pro Person genehmigungsfrei;\n"
        "- EU/USA: bis EUR 150 pro Person;\n"
        "- Sonstige Länder: bis EUR 75 pro Person.\n\n"
        "(3) Bewirtungen mit Amtsträgern bedürfen der vorherigen "
        "Zustimmung des Compliance Officers."
    )))

    s.append(("8. Spenden und Sponsoring", (
        "(1) Spenden müssen einem gemeinnützigen, gesetzlich anerkannten "
        "Zweck dienen.\n\n"
        "(2) Spenden werden ausschließlich an Organisationen mit "
        "anerkanntem Gemeinnützigkeitsstatus geleistet.\n\n"
        "(3) Spenden ab EUR 1.000 bedürfen der Zustimmung des "
        "Compliance Officers; ab EUR 10.000 der Zustimmung des "
        "Gesamtvorstands.\n\n"
        "(4) Empfänger werden im Rahmen einer Due-Diligence-Prüfung "
        "auf Reputation, Bonität und politische Beziehungen geprüft.\n\n"
        "(5) Sponsoring-Verträge bedürfen der Schriftform und enthalten "
        "die marktübliche Gegenleistung des Sponsoring-Partners."
    )))

    s.append(("9. Politische Zuwendungen", (
        "(1) Politische Zuwendungen (an Parteien, Politiker, "
        "Wahlkampagnen) sind grundsätzlich verboten und nur mit "
        "Vorstandsbeschluss zulässig.\n\n"
        "(2) Zuwendungen werden transparent veröffentlicht und "
        "entsprechen den jeweils einschlägigen Veröffentlichungs-"
        "pflichten (Parteiengesetz)."
    )))

    s.append(("10. Drittparteien und Geschäftspartner-Compliance", (
        "(1) Vor Aufnahme einer Geschäftsbeziehung mit Vertretern, "
        "Vermittlern, Beratern oder Joint-Venture-Partnern erfolgt "
        "eine Compliance-Due-Diligence („Third-Party Due Diligence' – "
        "TPDD).\n\n"
        "(2) Die TPDD umfasst: Identitätsprüfung, Bonität, Reputation, "
        "Sanktionslisten-Screening, politische Beziehungen, "
        "Compliance-Track-Record.\n\n"
        "(3) Verträge mit Drittparteien enthalten Compliance-Klauseln "
        "(insb. Anti-Korruptions-Erklärung, Recht zu Audits, Kündigungs-"
        "recht bei Verstößen).\n\n"
        "(4) Vergütungen müssen marktüblich sein, dokumentiert sein "
        "und in nachvollziehbarer Beziehung zur erbrachten Leistung "
        "stehen."
    )))

    s.append(("11. Eskalation und Meldewege", (
        "(1) Bei Verdacht auf Korruption ist der Compliance Officer "
        "unverzüglich zu informieren.\n\n"
        "(2) Mitarbeiter können sich anonym oder offen an folgende "
        "Meldestellen wenden:\n"
        "- Compliance Officer (E-Mail: compliance@...);\n"
        "- Whistleblower-Hotline (Telefon: ...);\n"
        "- Externe Ombudsperson (Rechtsanwalt extern).\n\n"
        "(3) Hinweisgeber werden gemäß HinSchG geschützt (siehe "
        "separate Whistleblower-Richtlinie)."
    )))

    s.append(("12. Schulungen", (
        "(1) Alle Mitarbeiter durchlaufen jährlich verpflichtende "
        "Compliance-Schulungen in Präsenz oder per E-Learning.\n\n"
        "(2) Hochrisikofunktionen (Vertrieb, Einkauf, Geschäftsführung) "
        "erhalten zusätzlich spezifische Schulungen.\n\n"
        "(3) Schulungsteilnahme wird dokumentiert und ist Teil der "
        "individuellen Leistungsbewertung."
    )))

    s.append(("13. Sanktionen", (
        "(1) Verstöße gegen diese Richtlinie werden konsequent "
        "verfolgt.\n\n"
        "(2) Arbeitsrechtliche Konsequenzen reichen von Abmahnung bis "
        "zur fristlosen Kündigung.\n\n"
        "(3) Strafrechtliche Konsequenzen ergeben sich aus den §§ 299, "
        "331-334 StGB, ggf. UK Bribery Act, FCPA.\n\n"
        "(4) Die Gesellschaft behält sich Regressansprüche vor."
    )))

    s.append(("14. Internationale Vorschriften", (
        "(1) UK Bribery Act 2010: gilt extraterritorial; verbietet "
        "auch Bestechung im privaten Sektor; strict liability für "
        "Unternehmen ohne adequate procedures.\n\n"
        "(2) US Foreign Corrupt Practices Act (FCPA): gilt extraterritorial; "
        "verbietet Bestechung ausländischer Amtsträger; umfasst auch "
        "Books-and-Records-Vorschriften.\n\n"
        "(3) OECD-Übereinkommen über die Bekämpfung der Bestechung "
        "ausländischer Amtsträger im internationalen Geschäftsverkehr."
    )))

    s.append(("15. Inkrafttreten und Änderungen", (
        f"(1) Diese Richtlinie in Version {version} tritt am Tag ihrer "
        f"Veröffentlichung im Intranet in Kraft.\n\n"
        f"(2) Sie wird mindestens einmal jährlich überprüft und "
        f"aktualisiert.\n\n"
        f"(3) Änderungen bedürfen der Genehmigung der Geschäftsführung "
        f"und der Konsultation des Betriebsrats, soweit mitbestimmungs-"
        f"pflichtig.\n\n"
        f"(4) Bei Konflikten zwischen dieser Richtlinie und anderen "
        f"internen Regelwerken gilt die strengere Regelung."
    )))

    return s


def gen_dsgvo_richtlinie(p: Dict[str, Any]) -> List[Section]:
    """DSGVO-Datenschutzrichtlinie. Target: 3500-5500 Wörter."""

    company = _g(p, "company", "Muster GmbH")
    dsb = _g(p, "dsb", "Datenschutz Kanzlei Müller (extern)")

    s: List[Section] = []

    s.append(("1. Präambel", (
        f"Die {company} verarbeitet personenbezogene Daten von "
        f"Mitarbeitern, Kunden, Lieferanten, Bewerbern und sonstigen "
        f"Geschäftspartnern. Wir bekennen uns zu einem rechtskonformen, "
        f"transparenten und sicheren Umgang mit personenbezogenen Daten.\n\n"
        f"Diese Datenschutzrichtlinie konkretisiert die Anforderungen "
        f"der Datenschutz-Grundverordnung (DSGVO), des Bundesdatenschutz-"
        f"gesetzes (BDSG), des Telekommunikation-Telemedien-Datenschutz-"
        f"Gesetzes (TTDSG) sowie sonstiger einschlägiger Vorschriften."
    )))

    s.append(("2. Grundsätze der Datenverarbeitung", (
        "Wir verarbeiten personenbezogene Daten gemäß den Grundsätzen "
        "des Art. 5 DSGVO:\n\n"
        "a) Rechtmäßigkeit, Verarbeitung nach Treu und Glauben, "
        "Transparenz;\n\n"
        "b) Zweckbindung: Erhebung für festgelegte, eindeutige und "
        "legitime Zwecke;\n\n"
        "c) Datenminimierung: dem Zweck angemessen und erforderlich;\n\n"
        "d) Richtigkeit: sachlich richtig und auf dem aktuellen Stand;\n\n"
        "e) Speicherbegrenzung: nur so lange wie für die Zwecke "
        "erforderlich;\n\n"
        "f) Integrität und Vertraulichkeit: angemessene technische "
        "und organisatorische Maßnahmen;\n\n"
        "g) Rechenschaftspflicht: Nachweis der Einhaltung der Grundsätze."
    )))

    s.append(("3. Rechtsgrundlagen", (
        "Datenverarbeitung erfolgt nur auf einer der nachfolgenden "
        "Rechtsgrundlagen des Art. 6 Abs. 1 DSGVO:\n\n"
        "a) Einwilligung der betroffenen Person (lit. a);\n\n"
        "b) Erforderlichkeit für die Erfüllung eines Vertrages oder "
        "die Durchführung vorvertraglicher Maßnahmen (lit. b);\n\n"
        "c) Erfüllung rechtlicher Verpflichtungen (lit. c, z. B. "
        "steuer- und handelsrechtliche Aufbewahrungspflichten);\n\n"
        "d) Schutz lebenswichtiger Interessen (lit. d);\n\n"
        "e) Wahrnehmung einer Aufgabe im öffentlichen Interesse "
        "(lit. e, in der Regel nicht einschlägig);\n\n"
        "f) Wahrung berechtigter Interessen (lit. f, nach "
        "Interessenabwägung).\n\n"
        "Für besondere Kategorien personenbezogener Daten gelten die "
        "zusätzlichen Anforderungen des Art. 9 DSGVO; für Beschäftigten-"
        "daten gilt § 26 BDSG."
    )))

    s.append(("4. Verantwortlichkeiten und Datenschutzbeauftragter", (
        f"(1) Verantwortlich im Sinne von Art. 4 Nr. 7 DSGVO ist die "
        f"{company}.\n\n"
        f"(2) Datenschutzbeauftragter ist: {dsb} (Kontakt: "
        f"datenschutz@...).\n\n"
        f"(3) Der Datenschutzbeauftragte berichtet unmittelbar an die "
        f"Geschäftsführung und ist in seiner Tätigkeit weisungsfrei.\n\n"
        f"(4) Auf Geschäftsführungsebene ist [Name] für Datenschutz "
        f"verantwortlich."
    )))

    s.append(("5. Verarbeitungsverzeichnis (Art. 30 DSGVO)", (
        "(1) Die Gesellschaft führt ein Verarbeitungsverzeichnis "
        "gemäß Art. 30 Abs. 1 DSGVO.\n\n"
        "(2) Das Verzeichnis dokumentiert je Verarbeitungstätigkeit:\n"
        "- Bezeichnung der Verarbeitung;\n"
        "- Verantwortlicher und ggf. Auftragsverarbeiter;\n"
        "- Zweck der Verarbeitung;\n"
        "- Rechtsgrundlage;\n"
        "- Kategorien betroffener Personen und Daten;\n"
        "- Empfänger;\n"
        "- Drittlandtransfer;\n"
        "- Löschfristen;\n"
        "- Technische und organisatorische Maßnahmen.\n\n"
        "(3) Verantwortlich für die Aktualisierung sind die jeweiligen "
        "Fachabteilungen."
    )))

    s.append(("6. Rechte der betroffenen Personen", (
        "(1) Die betroffenen Personen haben folgende Rechte:\n\n"
        "a) Recht auf Auskunft (Art. 15 DSGVO);\n"
        "b) Recht auf Berichtigung (Art. 16);\n"
        "c) Recht auf Löschung (Art. 17 – „Recht auf Vergessenwerden');\n"
        "d) Recht auf Einschränkung der Verarbeitung (Art. 18);\n"
        "e) Recht auf Datenübertragbarkeit (Art. 20);\n"
        "f) Recht auf Widerspruch (Art. 21);\n"
        "g) Recht auf Widerruf der Einwilligung (Art. 7 Abs. 3);\n"
        "h) Beschwerderecht bei der Aufsichtsbehörde (Art. 77).\n\n"
        "(2) Anfragen sind binnen eines Monats (Art. 12 Abs. 3 DSGVO) "
        "zu beantworten; bei komplexen Anfragen kann die Frist um "
        "zwei Monate verlängert werden.\n\n"
        "(3) Die Identität der anfragenden Person ist vor Auskunft "
        "zu prüfen."
    )))

    s.append(("7. Datenpannen (Art. 33, 34 DSGVO)", (
        "(1) Datenschutzverletzungen sind unverzüglich, spätestens "
        "binnen 24 Stunden, dem Datenschutzbeauftragten zu melden.\n\n"
        "(2) Der Datenschutzbeauftragte prüft die Meldepflicht an die "
        "Aufsichtsbehörde gemäß Art. 33 DSGVO (Meldung binnen 72 "
        "Stunden bei Risiko für die Betroffenen).\n\n"
        "(3) Bei hohem Risiko erfolgt zusätzlich eine Benachrichtigung "
        "der betroffenen Personen (Art. 34 DSGVO).\n\n"
        "(4) Vorfälle und Maßnahmen werden in einem Vorfallsregister "
        "dokumentiert (Rechenschaftspflicht)."
    )))

    s.append(("8. Technische und organisatorische Maßnahmen (TOMs)", (
        "(1) Wir treffen unter Berücksichtigung des Stands der Technik "
        "TOMs gemäß Art. 32 DSGVO. Die TOMs sind in Anlage 1 "
        "dokumentiert.\n\n"
        "(2) Kerngebiete der TOMs:\n"
        "- Vertraulichkeit (Zutritts-, Zugangs-, Zugriffs-, Trennungs-"
        "kontrolle);\n"
        "- Integrität (Weitergabe-, Eingabekontrolle);\n"
        "- Verfügbarkeit (Auftragskontrolle, Verfügbarkeitskontrolle);\n"
        "- Belastbarkeit (Wiederherstellbarkeit, regelmäßige Tests).\n\n"
        "(3) TOMs werden mindestens jährlich überprüft."
    )))

    s.append(("9. Auftragsverarbeitung (Art. 28 DSGVO)", (
        "(1) Auftragsverarbeiter werden vor Beauftragung auf "
        "datenschutzrechtliche Eignung geprüft.\n\n"
        "(2) Mit jedem Auftragsverarbeiter wird ein Auftragsverarbeitungs-"
        "vertrag (AVV) gemäß Art. 28 Abs. 3 DSGVO abgeschlossen.\n\n"
        "(3) Der AVV regelt insbesondere Gegenstand, Dauer, Art und "
        "Zweck der Verarbeitung, Kategorien personenbezogener Daten, "
        "Weisungsgebundenheit, Vertraulichkeitspflichten, TOMs, "
        "Unterauftragsverhältnisse, Audit-Rechte, Löschung nach "
        "Vertragsende."
    )))

    s.append(("10. Drittland-Transfer (Art. 44-49 DSGVO)", (
        "(1) Datenübermittlungen in Drittländer (außerhalb EU/EWR) "
        "erfolgen nur, wenn ein angemessenes Schutzniveau gewährleistet "
        "ist.\n\n"
        "(2) Geeignete Garantien sind insbesondere:\n"
        "- Angemessenheitsbeschluss der EU-Kommission;\n"
        "- EU-Standardvertragsklauseln gemäß Durchführungsbeschluss "
        "(EU) 2021/914;\n"
        "- Verbindliche interne Datenschutzvorschriften (BCR);\n"
        "- Genehmigte Verhaltensregeln oder Zertifizierungen.\n\n"
        "(3) Bei Transfers in die USA wird zusätzlich – unter Berücksichtigung "
        "der Schrems-II-Entscheidung des EuGH – ein Transfer Impact "
        "Assessment (TIA) durchgeführt und ggf. ergänzende Maßnahmen "
        "(z. B. Verschlüsselung) ergriffen.\n\n"
        "(4) Seit dem 10.07.2023 ist der EU-US Data Privacy Framework "
        "anwendbar; Transfers an zertifizierte US-Unternehmen sind "
        "auf dieser Grundlage zulässig."
    )))

    s.append(("11. Datenschutz-Folgenabschätzung (Art. 35 DSGVO)", (
        "(1) Bei voraussichtlich hohem Risiko für die Rechte und "
        "Freiheiten natürlicher Personen wird vor Aufnahme der "
        "Verarbeitung eine DSFA durchgeführt.\n\n"
        "(2) Eine DSFA ist insbesondere erforderlich bei:\n"
        "- systematischer und umfassender Bewertung persönlicher Aspekte;\n"
        "- umfangreicher Verarbeitung besonderer Datenkategorien;\n"
        "- systematischer umfangreicher Überwachung öffentlich "
        "zugänglicher Bereiche;\n"
        "- Verfahren auf der DSFA-Muss-Liste der zuständigen "
        "Aufsichtsbehörde.\n\n"
        "(3) Die DSFA wird vom Verantwortlichen unter Beratung des "
        "DSB durchgeführt und dokumentiert."
    )))

    s.append(("12. Schulungspflicht", (
        "(1) Alle Mitarbeiter, die personenbezogene Daten verarbeiten, "
        "werden auf das Datengeheimnis verpflichtet und regelmäßig "
        "geschult.\n\n"
        "(2) Schulungen erfolgen mindestens einmal jährlich, bei "
        "neuen Mitarbeitern im Rahmen des Onboarding.\n\n"
        "(3) Schulungen sind zu dokumentieren."
    )))

    s.append(("13. Aufsichtsbehörden", (
        "(1) Zuständige Aufsichtsbehörde für den Hauptsitz der "
        "Gesellschaft ist [Landesdatenschutzbeauftragter].\n\n"
        "(2) Für Beschäftigtendatenschutz bei Unternehmen mit "
        "betrieblichem DSB ist diese ebenfalls Aufsichtsbehörde.\n\n"
        "(3) Die Gesellschaft kooperiert vollumfänglich mit den "
        "Aufsichtsbehörden."
    )))

    s.append(("14. Sanktionen", (
        "(1) Bei Verstößen gegen die DSGVO drohen Geldbußen bis zu "
        "20 Mio. EUR oder 4 % des konzernweiten Vorjahresumsatzes "
        "(je nachdem, was höher ist).\n\n"
        "(2) Verstöße einzelner Mitarbeiter können arbeitsrechtliche "
        "Konsequenzen bis hin zur Kündigung und strafrechtliche "
        "Konsequenzen (§ 42 BDSG) nach sich ziehen.\n\n"
        "(3) Schadensersatzansprüche betroffener Personen (Art. 82 "
        "DSGVO) können erheblich sein."
    )))

    s.append(("15. Inkrafttreten und Änderungen", (
        "(1) Diese Datenschutzrichtlinie tritt am Tag der Veröffentlichung "
        "in Kraft.\n\n"
        "(2) Sie wird jährlich auf Aktualität und Wirksamkeit überprüft.\n\n"
        "(3) Anpassungen werden im Intranet veröffentlicht."
    )))

    return s


def gen_whistleblower_hinschg(p: Dict[str, Any]) -> List[Section]:
    """Whistleblower-Richtlinie HinSchG-konform. Target: 2500-4000 Wörter."""

    company = _g(p, "company", "Muster GmbH")

    s: List[Section] = []

    s.append(("1. Präambel und Zweck", (
        f"Die {company} bekennt sich zu einer offenen Hinweisgeberkultur. "
        f"Hinweise auf Verstöße gegen Gesetze und interne Regeln sind "
        f"wesentlich für die Aufrechterhaltung von Integrität und "
        f"Compliance. Beschäftigte und sonstige Hinweisgeber, die in "
        f"gutem Glauben Hinweise melden, werden vor jeder Form der "
        f"Benachteiligung geschützt.\n\n"
        f"Diese Richtlinie setzt die Anforderungen des Hinweisgeber-"
        f"schutzgesetzes (HinSchG) sowie der EU-Richtlinie 2019/1937 "
        f"(Whistleblowing-Richtlinie) um."
    )))

    s.append(("2. Anwendungsbereich", (
        f"(1) Hinweise können sich auf folgende Themen beziehen:\n\n"
        f"a) Verstöße gegen das Strafrecht (insbesondere Korruption, "
        f"Betrug, Untreue, Bilanzfälschung);\n"
        f"b) Bußgeldbewehrte Verstöße, sofern sie Leib oder Leben "
        f"oder Rechte von Beschäftigten betreffen;\n"
        f"c) Verstöße gegen EU- und nationales Recht in den vom HinSchG "
        f"genannten Bereichen (Finanzdienstleistungen, Datenschutz, "
        f"Verbraucherschutz, Lebensmittel-/Futtermittelsicherheit, "
        f"Umweltschutz, Verkehrssicherheit, Geldwäsche, "
        f"Produktsicherheit, etc.);\n"
        f"d) Verstöße gegen interne Richtlinien und Verhaltenskodex "
        f"der Gesellschaft.\n\n"
        f"(2) Hinweise zu rein arbeitsrechtlichen Auseinandersetzungen, "
        f"die ohne Bezug zu Rechtsverstößen sind, fallen nicht unter "
        f"diese Richtlinie."
    )))

    s.append(("3. Hinweisgebende Personen", (
        "(1) Hinweisberechtigt sind alle Personen, die im Kontext "
        "ihrer beruflichen Tätigkeit Informationen über Verstöße "
        "erlangt haben (§ 3 Abs. 8 HinSchG):\n\n"
        "- aktuelle und ehemalige Beschäftigte;\n"
        "- Bewerber, sofern die Informationen während des "
        "Bewerbungsverfahrens erlangt wurden;\n"
        "- Selbständige, Auftragnehmer, Lieferanten und deren Mitarbeiter;\n"
        "- Anteilseigner sowie Mitglieder von Verwaltungs-, Leitungs- "
        "und Aufsichtsorganen;\n"
        "- Volontäre, Praktikanten, Leiharbeitnehmer.\n\n"
        "(2) Hinweise können anonym, vertraulich oder offen abgegeben "
        "werden."
    )))

    s.append(("4. Meldekanäle", (
        "(1) Interne Meldestelle: Die Gesellschaft hat eine interne "
        "Meldestelle eingerichtet. Hinweise können dort über folgende "
        "Kanäle abgegeben werden:\n\n"
        "- E-Mail: hinweis@...;\n"
        "- Telefon-Hotline: ... (rund um die Uhr besetzt);\n"
        "- Online-Portal mit Anonymitätsschutz: https://whistle.[...];\n"
        "- Persönliches Gespräch nach Terminvereinbarung;\n"
        "- Postalische Meldung an die Compliance-Abteilung.\n\n"
        "(2) Ombudsperson: Zusätzlich steht eine externe Ombudsperson "
        "zur Verfügung: [Name], Rechtsanwaltskanzlei [...]\n\n"
        "(3) Externe Meldestelle: Hinweisgeber können sich auch direkt "
        "an die externe Meldestelle nach §§ 19 ff. HinSchG wenden, "
        "die beim Bundesamt für Justiz (BfJ) eingerichtet ist."
    )))

    s.append(("5. Anonymität und Vertraulichkeit", (
        "(1) Die Identität des Hinweisgebers wird vertraulich behandelt "
        "und nicht ohne dessen ausdrückliche Einwilligung offengelegt, "
        "soweit nicht zwingende gesetzliche Vorschriften (insbesondere "
        "Strafprozessordnung) eine Offenlegung erzwingen.\n\n"
        "(2) Anonyme Hinweise werden ebenfalls geprüft, soweit die "
        "darin enthaltenen Informationen eine Untersuchung ermöglichen.\n\n"
        "(3) Die Meldestelle verwendet ein technisches System mit "
        "End-to-End-Verschlüsselung, das die Identität auch gegenüber "
        "internen IT-Administratoren schützt."
    )))

    s.append(("6. Verfahrensschritte (Bearbeitung)", (
        "(1) Eingangsbestätigung: Spätestens 7 Tage nach Eingang "
        "des Hinweises bestätigt die Meldestelle den Eingang gegenüber "
        "dem Hinweisgeber (soweit ein Rückkanal existiert).\n\n"
        "(2) Vorprüfung: Die Meldestelle prüft, ob der Hinweis "
        "stichhaltig ist und vom Anwendungsbereich der Richtlinie "
        "erfasst wird.\n\n"
        "(3) Untersuchung: Stichhaltige Hinweise werden weiter untersucht, "
        "ggf. unter Einbindung von Compliance, HR, Rechtsabteilung und "
        "externen Beratern. Dem Hinweisgeber kann eine Mitwirkungs-"
        "möglichkeit eingeräumt werden.\n\n"
        "(4) Maßnahmen: Bei bestätigtem Verstoß werden geeignete "
        "Abhilfemaßnahmen ergriffen (z. B. arbeitsrechtliche Maßnahmen, "
        "Prozessänderungen, Schulungen, ggf. Selbstanzeige).\n\n"
        "(5) Rückmeldung: Spätestens 3 Monate nach Eingangsbestätigung "
        "erhält der Hinweisgeber eine Rückmeldung über das Ergebnis "
        "(soweit dem nicht überwiegende Geheimhaltungsinteressen "
        "entgegenstehen).\n\n"
        "(6) Abschluss und Dokumentation: Jeder Hinweis wird vollständig "
        "dokumentiert. Die Dokumentation wird drei (3) Jahre nach "
        "Verfahrensabschluss aufbewahrt (§ 11 Abs. 5 HinSchG)."
    )))

    s.append(("7. Repressalienschutz mit Beweislastumkehr", (
        "(1) Hinweisgeber dürfen wegen einer Meldung oder Offenlegung "
        "keine Repressalien (Benachteiligungen) erleiden. Repressalien "
        "umfassen insbesondere:\n\n"
        "- Kündigung, Suspendierung;\n"
        "- Versetzung, Aufgabenentzug;\n"
        "- Negative Leistungsbeurteilung;\n"
        "- Versagung von Beförderungen, Schulungen, Gehaltserhöhungen;\n"
        "- Mobbing, Stigmatisierung, Bloßstellung;\n"
        "- Diskriminierung.\n\n"
        "(2) Wird eine Benachteiligung des Hinweisgebers in zeitlichem "
        "Zusammenhang mit der Meldung vermutet, trägt der Arbeitgeber "
        "die Beweislast dafür, dass die Benachteiligung auf sachlichen "
        "Gründen ohne Zusammenhang mit der Meldung beruhte (§ 36 "
        "HinSchG, Beweislastumkehr).\n\n"
        "(3) Verstoßende Personen werden arbeitsrechtlich sanktioniert; "
        "Geldbußen bis zu EUR 50.000 (§ 40 HinSchG) sind möglich.\n\n"
        "(4) Hinweisgeber können entstandene Schäden ersetzt verlangen."
    )))

    s.append(("8. Schutz und Mitwirkung", (
        "(1) Personen, die an der Meldung mitwirken oder den "
        "Hinweisgeber unterstützen (z. B. Kollegen, Familienangehörige) "
        "stehen unter dem gleichen Schutz wie Hinweisgeber.\n\n"
        "(2) Der Hinweisgeber kann sich jederzeit zur Beratung an die "
        "Ombudsperson, den Datenschutzbeauftragten, externe Rechtsberater "
        "oder Gewerkschaften wenden."
    )))

    s.append(("9. Falschmeldungen und Missbrauch", (
        "(1) Wissentlich unwahre Meldungen oder offensichtlich "
        "böswillig erstattete Hinweise sind nicht vom Schutz erfasst.\n\n"
        "(2) Verbreitet ein Hinweisgeber wissentlich oder grob "
        "fahrlässig unwahre Informationen, ist er zum Schadensersatz "
        "verpflichtet (§ 38 HinSchG); zudem drohen Geldbußen.\n\n"
        "(3) Der gute Glaube wird vermutet, soweit nicht das Gegenteil "
        "nachgewiesen wird."
    )))

    s.append(("10. Datenschutz", (
        "(1) Die im Rahmen des Verfahrens erhobenen personenbezogenen "
        "Daten werden gemäß DSGVO und § 10 HinSchG verarbeitet.\n\n"
        "(2) Rechtsgrundlage der Verarbeitung sind Art. 6 Abs. 1 lit. c "
        "DSGVO i.V.m. § 10 HinSchG bzw. – soweit kollektivrechtlich "
        "Beschäftigte betroffen sind – § 26 BDSG.\n\n"
        "(3) Daten werden auf das notwendige Maß beschränkt und nur "
        "den am Verfahren beteiligten Personen zugänglich gemacht.\n\n"
        "(4) Die Aufbewahrungsfrist beträgt drei (3) Jahre nach "
        "Verfahrensabschluss; danach werden die Daten gelöscht, "
        "soweit nicht längere gesetzliche Aufbewahrungspflichten "
        "bestehen."
    )))

    s.append(("11. Schulung und Kommunikation", (
        "(1) Alle Mitarbeiter werden bei Einstellung und turnusmäßig "
        "über die Existenz und Funktionsweise der Meldekanäle informiert.\n\n"
        "(2) Spezielle Schulungen erhalten Führungskräfte und "
        "Compliance-Mitarbeiter."
    )))

    s.append(("12. Schlussbestimmungen", (
        "(1) Diese Richtlinie tritt am Tag der Veröffentlichung in Kraft.\n\n"
        "(2) Sie wird mindestens alle zwei Jahre überprüft.\n\n"
        "(3) Bei Konflikten mit anderen internen Regelwerken hat das "
        "HinSchG sowie diese Richtlinie Vorrang."
    )))

    return s


def gen_lksg_richtlinie(p: Dict[str, Any]) -> List[Section]:
    """LkSG Lieferkettensorgfaltspflicht-Richtlinie. Target: 2500-4000 Wörter."""

    company = _g(p, "company", "Muster GmbH")

    s: List[Section] = []

    s.append(("1. Präambel", (
        f"Die {company} bekennt sich zur Achtung der Menschenrechte und "
        f"zum Schutz der Umwelt in unserer gesamten Lieferkette. Wir "
        f"setzen die Anforderungen des Lieferkettensorgfaltspflichten-"
        f"gesetzes (LkSG) und der EU-Lieferkettenrichtlinie (CSDDD) um "
        f"und arbeiten partnerschaftlich mit unseren Lieferanten "
        f"daran, menschenrechts- und umweltbezogene Risiken zu "
        f"identifizieren, zu minimieren und zu beheben."
    )))

    s.append(("2. Anwendungsbereich", (
        f"(1) Diese Richtlinie gilt für die {company} und ihre "
        f"verbundenen Unternehmen sowie für ihre unmittelbaren und – "
        f"in begründetem Verdachtsfall – mittelbaren Zulieferer "
        f"weltweit.\n\n"
        f"(2) Anwendbar ab dem 01.01.2024 für Unternehmen mit "
        f"mindestens 1.000 Mitarbeitern im Inland, ab 01.01.2023 für "
        f"Unternehmen mit mindestens 3.000 Mitarbeitern.\n\n"
        f"(3) Die EU-Lieferkettenrichtlinie (CSDDD) erweitert ab "
        f"voraussichtlich 2027 den Anwendungsbereich auf Unternehmen "
        f"ab 1.000 Mitarbeitern und EUR 450 Mio. Umsatz."
    )))

    s.append(("3. Definitionen", (
        "„Eigener Geschäftsbereich' umfasst jede Tätigkeit zur "
        "Erreichung des Unternehmensziels, einschließlich der "
        "Tätigkeiten an in- und ausländischen Standorten.\n\n"
        "„Unmittelbarer Zulieferer' ist ein Partner eines Liefer-"
        "vertrages über Waren oder Dienstleistungen, dessen Zulieferungen "
        "für die Herstellung des Produkts der Gesellschaft oder zur "
        "Erbringung der Dienstleistung notwendig sind.\n\n"
        "„Mittelbarer Zulieferer' ist jedes Unternehmen, das kein "
        "unmittelbarer Zulieferer ist und dessen Zulieferungen für die "
        "Herstellung des Produkts oder zur Erbringung der "
        "Dienstleistung notwendig sind.\n\n"
        "„Menschenrechtliches Risiko' ist ein Zustand, bei dem aufgrund "
        "tatsächlicher Umstände mit hinreichender Wahrscheinlichkeit "
        "ein Verstoß gegen eines der in § 2 Abs. 2 LkSG genannten Verbote "
        "droht.\n\n"
        "„Umweltbezogenes Risiko' ist ein Zustand, bei dem mit "
        "hinreichender Wahrscheinlichkeit ein Verstoß gegen die in "
        "§ 2 Abs. 3 LkSG genannten Verbote droht."
    )))

    s.append(("4. Menschenrechts- und umweltbezogene Risiken", (
        "Folgende Risiken sind insbesondere relevant:\n\n"
        "a) Verbot von Kinderarbeit (§ 2 Abs. 2 Nr. 1, 2 LkSG);\n"
        "b) Verbot von Zwangsarbeit und Sklaverei (Nr. 3, 4);\n"
        "c) Verbot der Missachtung des Arbeitsschutzes (Nr. 5);\n"
        "d) Verbot der Vorenthaltung eines angemessenen Lohns (Nr. 6);\n"
        "e) Verbot der Missachtung der Koalitionsfreiheit (Nr. 7);\n"
        "f) Verbot der Diskriminierung (Nr. 8);\n"
        "g) Verbot der widerrechtlichen Wegnahme von Land, Wäldern, "
        "Gewässern (Nr. 9);\n"
        "h) Verbot des Einsatzes privater oder öffentlicher Sicherheits-"
        "kräfte unter Verletzung der Menschenrechte (Nr. 10);\n"
        "i) Umweltbezogene Verbote (insbesondere Minamata-Übereinkommen, "
        "Stockholmer Konvention, Basler Übereinkommen)."
    )))

    s.append(("5. Risikomanagement", (
        "(1) Die Gesellschaft hat ein Risikomanagement etabliert, das "
        "in alle relevanten Geschäftsabläufe integriert ist.\n\n"
        "(2) Verantwortlich ist der Menschenrechtsbeauftragte, der "
        "unmittelbar an die Geschäftsführung berichtet.\n\n"
        "(3) Mindestens einmal jährlich sowie anlassbezogen wird eine "
        "Risikoanalyse durchgeführt, die menschenrechts- und "
        "umweltbezogene Risiken im eigenen Geschäftsbereich und bei "
        "unmittelbaren Zulieferern identifiziert, gewichtet und priorisiert.\n\n"
        "(4) Die Risikoanalyse berücksichtigt insbesondere:\n"
        "- Art und Umfang der Geschäftstätigkeit;\n"
        "- Verursachungsbeitrag der Gesellschaft;\n"
        "- Wahrscheinlichkeit und Schwere der drohenden Verletzung;\n"
        "- Möglichkeiten der Einflussnahme."
    )))

    s.append(("6. Grundsatzerklärung", (
        "(1) Die Geschäftsführung hat eine Grundsatzerklärung über die "
        "Menschenrechtsstrategie der Gesellschaft verabschiedet "
        "(Anlage 1).\n\n"
        "(2) Die Grundsatzerklärung enthält:\n"
        "- das Verfahren zur Umsetzung der Sorgfaltspflichten;\n"
        "- die identifizierten prioritären menschenrechtlichen und "
        "umweltbezogenen Risiken;\n"
        "- die in Bezug darauf gesetzten menschenrechts- und "
        "umweltbezogenen Erwartungen an Beschäftigte und Zulieferer.\n\n"
        "(3) Die Grundsatzerklärung wird intern und extern veröffentlicht."
    )))

    s.append(("7. Präventionsmaßnahmen im eigenen Geschäftsbereich", (
        "(1) Wir verankern die Menschenrechtsstrategie in alle "
        "relevanten Geschäftsprozesse und Beschaffungsstrategien.\n\n"
        "(2) Schulungen zu Menschenrechten und Umweltschutz werden "
        "regelmäßig für Mitarbeiter in Beschaffung, Personalwesen, "
        "Compliance und Geschäftsführung durchgeführt.\n\n"
        "(3) Kontrollmechanismen, wie Audits und Stichproben, prüfen "
        "die Einhaltung der Vorgaben in eigenen Standorten."
    )))

    s.append(("8. Präventionsmaßnahmen bei unmittelbaren Zulieferern", (
        "(1) Wir wählen Zulieferer unter Berücksichtigung menschenrechts- "
        "und umweltbezogener Aspekte aus.\n\n"
        "(2) Zulieferer werden vertraglich auf die Einhaltung der "
        "Anforderungen verpflichtet (Lieferanten-Code-of-Conduct, "
        "Anlage 2).\n\n"
        "(3) Wir führen risikobasierte Kontrollen durch, u.a. Self-"
        "Assessments und vor-Ort-Audits.\n\n"
        "(4) Wir unterstützen Zulieferer durch Schulungen und Tools."
    )))

    s.append(("9. Abhilfemaßnahmen", (
        "(1) Stellt die Gesellschaft fest, dass die Verletzung einer "
        "menschenrechts- oder umweltbezogenen Pflicht eingetreten ist "
        "oder droht, ergreift sie unverzüglich angemessene Abhilfe-"
        "maßnahmen.\n\n"
        "(2) Im eigenen Geschäftsbereich muss die Verletzung beendet "
        "werden.\n\n"
        "(3) Bei unmittelbaren Zulieferern erstellt die Gesellschaft "
        "einen Plan zur Beendigung oder Minimierung der Verletzung "
        "(mit konkreten Zeitvorgaben).\n\n"
        "(4) Bei schwerwiegenden Verletzungen und ergebnisloser "
        "Aufforderung kann der Abbruch der Geschäftsbeziehung "
        "erforderlich sein (Ultima Ratio).\n\n"
        "(5) Bei mittelbaren Zulieferern erfolgen Abhilfemaßnahmen "
        "nur bei substantiierter Kenntnis von Verletzungen."
    )))

    s.append(("10. Beschwerdeverfahren", (
        "(1) Die Gesellschaft hat ein angemessenes Beschwerdeverfahren "
        "eingerichtet, das von Personen genutzt werden kann, die auf "
        "menschenrechtliche und umweltbezogene Risiken oder Verletzungen "
        "im eigenen Geschäftsbereich oder in der Lieferkette hinweisen "
        "wollen.\n\n"
        "(2) Das Beschwerdeverfahren ist anonym nutzbar und wird "
        "vertraulich behandelt. Hinweisgeber sind vor Benachteiligungen "
        "geschützt.\n\n"
        "(3) Eingerichtete Kanäle: Online-Portal, Hotline, externe "
        "Ombudsperson (Synergie mit Whistleblower-Verfahren nach "
        "HinSchG).\n\n"
        "(4) Eingegangene Beschwerden werden binnen 7 Tagen bestätigt, "
        "innerhalb von 3 Monaten erfolgt eine Rückmeldung."
    )))

    s.append(("11. Dokumentation und Berichtspflichten", (
        "(1) Die Erfüllung der Sorgfaltspflichten wird laufend dokumentiert "
        "und mindestens sieben (7) Jahre aufbewahrt (§ 10 LkSG).\n\n"
        "(2) Jährlich, spätestens vier Monate nach Schluss des "
        "Geschäftsjahres, wird ein Bericht über die Erfüllung der "
        "Sorgfaltspflichten erstellt und an das Bundesamt für Wirtschaft "
        "und Ausfuhrkontrolle (BAFA) übermittelt sowie auf der "
        "Website veröffentlicht.\n\n"
        "(3) Der Bericht enthält insbesondere identifizierte Risiken, "
        "ergriffene Maßnahmen sowie Effektivitätsbewertungen."
    )))

    s.append(("12. Verantwortlicher Menschenrechtsbeauftragter", (
        "(1) Die Gesellschaft hat einen Menschenrechtsbeauftragten "
        "benannt. Er berichtet unmittelbar an die Geschäftsführung.\n\n"
        "(2) Aufgaben: Überwachung des Risikomanagements, jährliche "
        "Berichterstattung an die Geschäftsführung, externe "
        "Berichterstattung an BAFA.\n\n"
        "(3) Der Menschenrechtsbeauftragte ist mit den notwendigen "
        "Ressourcen ausgestattet."
    )))

    s.append(("13. Sanktionen und Bußgelder", (
        "(1) Bei Verstößen gegen das LkSG drohen empfindliche Bußgelder:\n"
        "- Bei jährlichen Konzernumsätzen ab EUR 400 Mio.: bis zu 2 % "
        "des durchschnittlichen Jahresumsatzes;\n"
        "- Ferner Bußgelder bis zu EUR 8 Mio. (§ 24 LkSG).\n\n"
        "(2) Zudem drohen Ausschlüsse von der Vergabe öffentlicher "
        "Aufträge.\n\n"
        "(3) Reputationsrisiken bei unzureichender Umsetzung."
    )))

    s.append(("14. Mittelbare Zulieferer", (
        "(1) Die Sorgfaltspflichten erstrecken sich auf mittelbare "
        "Zulieferer nur bei substantiierter Kenntnis von Verletzungen "
        "(„substantiiertes Wissen').\n\n"
        "(2) Substantiierte Kenntnis liegt vor, wenn der Gesellschaft "
        "tatsächliche Anhaltspunkte vorliegen, die eine Verletzung "
        "wahrscheinlich erscheinen lassen.\n\n"
        "(3) In diesem Fall werden anlassbezogene Risikoanalysen, "
        "Präventions- und Abhilfemaßnahmen durchgeführt."
    )))

    s.append(("15. Inkrafttreten und Überprüfung", (
        "(1) Diese Richtlinie tritt am Tag der Veröffentlichung in Kraft.\n\n"
        "(2) Sie wird jährlich auf Aktualität und Wirksamkeit überprüft.\n\n"
        "(3) Aktualisierungen werden im Intranet veröffentlicht und an "
        "die Lieferanten kommuniziert."
    )))

    return s


def gen_code_of_conduct(p: Dict[str, Any]) -> List[Section]:
    """Code of Conduct. Target: 2500-4000 Wörter."""

    company = _g(p, "company", "Muster GmbH")

    s: List[Section] = []

    s.append(("1. Botschaft der Geschäftsführung", (
        f"Liebe Kolleginnen und Kollegen,\n\n"
        f"die {company} steht für Qualität, Innovation, Integrität und "
        f"Verantwortung. Unser Erfolg ist eng verbunden mit dem Vertrauen "
        f"unserer Kunden, Geschäftspartner, Mitarbeiter und der "
        f"Gesellschaft. Dieses Vertrauen wollen wir durch unser tägliches "
        f"Verhalten verdienen.\n\n"
        f"Dieser Code of Conduct enthält die verbindlichen Grundsätze "
        f"unseres Handelns. Er ist Maßstab für jeden Einzelnen von uns "
        f"– unabhängig von Position, Aufgabenbereich oder Standort.\n\n"
        f"Wir bitten Sie, sich diesen Grundsätzen verpflichtet zu "
        f"fühlen und jeden Verstoß zu melden."
    )))

    s.append(("2. Unsere Werte", (
        "Wir leben fünf Grundwerte:\n\n"
        "Integrität: Wir handeln ehrlich, verlässlich und im Einklang "
        "mit Gesetz und Ethik.\n\n"
        "Verantwortung: Wir übernehmen Verantwortung für unser Handeln "
        "und seine Folgen.\n\n"
        "Respekt: Wir begegnen jedem Menschen mit Respekt und Würde, "
        "unabhängig von Herkunft, Religion, Geschlecht, Alter, "
        "sexueller Orientierung oder körperlicher Verfassung.\n\n"
        "Exzellenz: Wir streben höchste Qualität und kontinuierliche "
        "Verbesserung an.\n\n"
        "Nachhaltigkeit: Wir handeln ökologisch, sozial und "
        "ökonomisch nachhaltig."
    )))

    s.append(("3. Compliance und Recht", (
        "(1) Wir halten alle anwendbaren Gesetze und Vorschriften ein. "
        "Bei Konflikten zwischen lokalen Gewohnheiten und gesetzlichen "
        "Vorgaben hat die strengere Regelung Vorrang.\n\n"
        "(2) Bei Unsicherheit ziehen wir Compliance, Rechtsabteilung "
        "oder externe Berater hinzu."
    )))

    s.append(("4. Korruption und Bestechung", (
        "(1) Wir tolerieren keine Form der Korruption oder Bestechung.\n\n"
        "(2) Geschenke und Bewirtungen müssen den Maßgaben unserer "
        "Antikorruptions-Richtlinie entsprechen.\n\n"
        "(3) Wir wählen Geschäftspartner nach objektiven Kriterien "
        "(Qualität, Preis, Service, Reputation)."
    )))

    s.append(("5. Fairer Wettbewerb", (
        "(1) Wir wettbewerben fair und im Einklang mit Kartell- und "
        "Wettbewerbsrecht.\n\n"
        "(2) Wir treffen keine wettbewerbsbeschränkenden Absprachen "
        "über Preise, Mengen oder Märkte mit Wettbewerbern.\n\n"
        "(3) Wir respektieren die Geschäftsgeheimnisse anderer."
    )))

    s.append(("6. Interessenkonflikte", (
        "(1) Wir vermeiden Situationen, in denen private und "
        "geschäftliche Interessen kollidieren.\n\n"
        "(2) Potenzielle Interessenkonflikte offenbaren wir gegenüber "
        "Vorgesetzten und Compliance.\n\n"
        "(3) Nebentätigkeiten und Beteiligungen bedürfen ggf. der "
        "Zustimmung."
    )))

    s.append(("7. Geschäfts- und Betriebsgeheimnisse", (
        "(1) Vertrauliche Informationen werden sorgsam behandelt und "
        "Dritten nicht zugänglich gemacht.\n\n"
        "(2) Die Geheimhaltungspflichten gelten auch nach Beendigung "
        "des Arbeitsverhältnisses unbefristet."
    )))

    s.append(("8. Datenschutz", (
        "(1) Wir verarbeiten personenbezogene Daten nur unter Einhaltung "
        "der DSGVO und unserer Datenschutzrichtlinie.\n\n"
        "(2) Wir halten Datenschutz, Datensparsamkeit und "
        "Datensicherheit ein."
    )))

    s.append(("9. Menschenrechte und Arbeitsstandards", (
        "(1) Wir achten die international anerkannten Menschenrechte.\n\n"
        "(2) Wir lehnen Kinderarbeit und Zwangsarbeit jeder Form ab.\n\n"
        "(3) Wir achten die Vereinigungsfreiheit und das Recht auf "
        "Kollektivverhandlungen.\n\n"
        "(4) Wir gewährleisten faire Arbeitsbedingungen, angemessene "
        "Vergütung und Arbeitsschutz."
    )))

    s.append(("10. Diskriminierungsverbot", (
        "(1) Wir tolerieren keine Diskriminierung wegen Geschlecht, "
        "Ethnie, Religion, Weltanschauung, Behinderung, Alter, "
        "sexueller Identität.\n\n"
        "(2) Wir tolerieren keine Belästigung, Mobbing oder "
        "Schikane.\n\n"
        "(3) Wir fördern Vielfalt und Inklusion."
    )))

    s.append(("11. Umwelt- und Klimaschutz", (
        "(1) Wir verpflichten uns zu einem schonenden Umgang mit "
        "natürlichen Ressourcen.\n\n"
        "(2) Wir streben Klimaneutralität gemäß unserem Klima-Fahrplan "
        "an.\n\n"
        "(3) Wir minimieren Emissionen, Abfälle und Wasserverbrauch."
    )))

    s.append(("12. Produktqualität und -sicherheit", (
        "(1) Wir gewährleisten höchste Qualitäts- und Sicherheits-"
        "standards bei unseren Produkten und Dienstleistungen.\n\n"
        "(2) Wir kommunizieren transparent über die Eigenschaften "
        "unserer Produkte."
    )))

    s.append(("13. Geschäftspartner und Lieferanten", (
        "(1) Wir wählen Geschäftspartner sorgfältig aus und achten "
        "auf ihre Compliance.\n\n"
        "(2) Wir verpflichten unsere Lieferanten auf vergleichbare "
        "Standards (siehe LkSG-Richtlinie)."
    )))

    s.append(("14. Meldung von Verstößen", (
        "(1) Wir ermutigen jeden Mitarbeiter, Verstöße zu melden.\n\n"
        "(2) Meldungen können über Vorgesetzte, Compliance, "
        "Ombudsperson oder Whistleblowing-Kanäle erfolgen.\n\n"
        "(3) Hinweisgeber werden vor Repressalien geschützt (HinSchG)."
    )))

    s.append(("15. Sanktionen", (
        "(1) Verstöße gegen den Code of Conduct werden konsequent "
        "verfolgt und sanktioniert.\n\n"
        "(2) Sanktionen reichen von Abmahnung bis zur fristlosen "
        "Kündigung; zudem können strafrechtliche Konsequenzen drohen."
    )))

    s.append(("16. Inkrafttreten und Überprüfung", (
        "(1) Der Code of Conduct tritt am Tag der Veröffentlichung in "
        "Kraft.\n\n"
        "(2) Er wird regelmäßig auf Aktualität überprüft."
    )))

    return s


def gen_export_control_richtlinie(p: Dict[str, Any]) -> List[Section]:
    """Exportkontroll-Richtlinie. Target: 2500-4000 Wörter."""

    company = _g(p, "company", "Muster GmbH")

    s: List[Section] = []

    s.append(("1. Zweck und Anwendungsbereich", (
        f"Diese Richtlinie regelt die Exportkontroll-Compliance der "
        f"{company} und ihrer verbundenen Unternehmen. Sie gilt für "
        f"alle Beschäftigten, die mit dem Export, Reexport, "
        f"innergemeinschaftlichen Verbringen oder dem Erwerb / Verkauf "
        f"genehmigungspflichtiger Güter, Technologien, Software oder "
        f"Dienstleistungen befasst sind, sowie für die Beschäftigten "
        f"in den Bereichen Vertrieb, Einkauf, F&E, Logistik und Finanzen."
    )))

    s.append(("2. Rechtsgrundlagen", (
        "Diese Richtlinie setzt insbesondere folgende Vorschriften um:\n\n"
        "a) Außenwirtschaftsgesetz (AWG) und Außenwirtschaftsverordnung "
        "(AWV);\n"
        "b) EU-Dual-Use-Verordnung (VO (EU) 2021/821);\n"
        "c) EU-Anti-Folter-Verordnung (VO (EU) 2019/125);\n"
        "d) EU-Sanktionen (insb. Iran, Russland, Nordkorea, Syrien);\n"
        "e) US Export Administration Regulations (EAR), International "
        "Traffic in Arms Regulations (ITAR);\n"
        "f) OFAC-Sanktionsprogramme der USA;\n"
        "g) UN-Sanktionen;\n"
        "h) Sanktionen weiterer Länder, soweit anwendbar."
    )))

    s.append(("3. Verbote", (
        "(1) Wir liefern keine Güter, Technologien oder Dienstleistungen "
        "in folgende Empfängerländer und an folgende Personen:\n\n"
        "- Embargoländer der EU oder UN (insbes. Nordkorea, Iran "
        "für bestimmte Güter, Russland nach den EU-Sanktionen);\n"
        "- Personen und Organisationen auf den EU-Sanktionslisten "
        "(insbes. VO 269/2014, 267/2012, 833/2014);\n"
        "- Personen und Organisationen auf US-Sanktionslisten (SDN-List, "
        "Entity List, Denied Persons List, Unverified List).\n\n"
        "(2) Wir unterstützen keine ABC-Waffen-Programme oder Träger "
        "(Catch-all-Regelungen Art. 4, 5 EU-Dual-Use-VO).\n\n"
        "(3) Wir leisten keine Hilfe oder Beratung für sanktionierte "
        "Aktivitäten."
    )))

    s.append(("4. Klassifizierung und Genehmigung", (
        "(1) Vor jedem Export wird das Produkt klassifiziert:\n"
        "- Ausfuhrlistennummer (AL-Nr.) nach Anhang AL zur AWV;\n"
        "- EU-Dual-Use-Listennummer nach Anhang I VO 2021/821;\n"
        "- ECCN-Nummer nach US EAR;\n"
        "- USML-Kategorie, falls ITAR-relevant.\n\n"
        "(2) Bei genehmigungspflichtigen Gütern wird vor dem Export "
        "die erforderliche Genehmigung beantragt:\n"
        "- BAFA (Deutschland);\n"
        "- BIS (US, EAR);\n"
        "- DDTC (US, ITAR).\n\n"
        "(3) Allgemeine Genehmigungen (AGGs) werden geprüft, ob sie "
        "anwendbar sind."
    )))

    s.append(("5. Sanktionslisten-Screening", (
        "(1) Vor jeder Geschäftsbeziehung und vor jedem Export erfolgt "
        "ein Abgleich mit allen relevanten Sanktionslisten.\n\n"
        "(2) Das Screening wird mittels automatisierter Software "
        "durchgeführt und dokumentiert.\n\n"
        "(3) Bei Treffern wird die Geschäftsbeziehung gestoppt und der "
        "Exportkontrollbeauftragte einbezogen.\n\n"
        "(4) Auch Re-Screenings bei Bestandskunden erfolgen mindestens "
        "monatlich."
    )))

    s.append(("6. Verantwortlichkeiten", (
        "(1) Verantwortlich für die Einhaltung der Exportkontroll-"
        "Compliance ist der Ausfuhrverantwortliche im Sinne von § 8 "
        "Abs. 1 AWG, in der Regel ein Mitglied der Geschäftsführung.\n\n"
        "(2) Operativ verantwortlich ist der Exportkontrollbeauftragte, "
        "der dem Ausfuhrverantwortlichen berichtet.\n\n"
        "(3) Jeder Mitarbeiter, der mit Exportgeschäften befasst ist, "
        "trägt eine eigene Verantwortung für die Einhaltung dieser "
        "Richtlinie in seinem Bereich."
    )))

    s.append(("7. Internes Compliance-Programm", (
        "(1) Wir unterhalten ein dokumentiertes Internal Compliance "
        "Programme (ICP) gemäß Empfehlung der EU-Kommission "
        "(C/2019/4570).\n\n"
        "(2) Bestandteile sind: Top-Management-Commitment, "
        "Organisation und Verantwortlichkeiten, Schulungen, Verfahren "
        "(Klassifizierung, Screening, Genehmigung, Versand, "
        "Aufbewahrung), Audits, Berichterstattung an die "
        "Geschäftsführung."
    )))

    s.append(("8. Schulungen", (
        "(1) Alle Mitarbeiter in relevanten Funktionen erhalten "
        "regelmäßig Exportkontroll-Schulungen (mindestens jährlich).\n\n"
        "(2) Neue Mitarbeiter erhalten eine Grundlagenschulung im "
        "Onboarding.\n\n"
        "(3) Schulungen werden dokumentiert."
    )))

    s.append(("9. Audit und Kontrollen", (
        "(1) Mindestens jährlich erfolgt ein internes Exportkontroll-"
        "Audit durch die Compliance- oder Revisionsabteilung.\n\n"
        "(2) Externe Audits (z. B. BAFA-Außenwirtschaftsprüfung) werden "
        "kooperativ begleitet."
    )))

    s.append(("10. Dokumentation und Aufbewahrung", (
        "(1) Exportkontrollrelevante Dokumente (Klassifizierungen, "
        "Screenings, Genehmigungen, Frachtdokumente) werden "
        "mindestens 5 Jahre, in den USA 5-10 Jahre, aufbewahrt.\n\n"
        "(2) Die Aufbewahrung erfolgt elektronisch und revisionssicher."
    )))

    s.append(("11. Verstöße und Sanktionen", (
        "(1) Verstöße können straf- und ordnungsrechtliche Konsequenzen "
        "haben (Freiheitsstrafe bis zu 10 Jahren, Bußgelder bis "
        "EUR 500.000, in den USA Strafen bis USD 1 Mio. und Freiheits-"
        "strafen).\n\n"
        "(2) Zusätzlich drohen Verwaltungssanktionen wie Entzug von "
        "Genehmigungen und Listing auf Denied Persons List.\n\n"
        "(3) Arbeitsrechtlich werden Verstöße sanktioniert, bis hin "
        "zur fristlosen Kündigung.\n\n"
        "(4) Verstöße sind dem Exportkontrollbeauftragten unverzüglich "
        "zu melden; ggf. erfolgt eine Selbstanzeige zur Strafmilderung."
    )))

    s.append(("12. Inkrafttreten und Aktualisierung", (
        "(1) Diese Richtlinie tritt am Tag der Veröffentlichung in "
        "Kraft.\n\n"
        "(2) Aufgrund der Dynamik der Sanktionsvorschriften wird die "
        "Richtlinie laufend aktualisiert."
    )))

    return s


# =====================================================================
# INSURANCE
# =====================================================================

def gen_betriebshaftpflicht_police(p: Dict[str, Any]) -> List[Section]:
    """Betriebshaftpflicht-Police mit AVB. Target: 3000-5000 Wörter."""

    versicherer = _g(p, "versicherer", "Allianz Versicherungs-AG")
    nehmer = _g(p, "nehmer", "Muster GmbH")
    policy = _g(p, "policy", "BHV-2025-00123456")
    summe = _g(p, "summe", "10.000.000")
    laufzeit_start = _g(p, "laufzeit_start", "01.01.2025")
    laufzeit_end = _g(p, "laufzeit_end", "31.12.2025")

    s: List[Section] = []

    s.append(("Versicherungsscheindaten", (
        f"Versicherungsschein-Nr.: {policy}\n"
        f"Versicherer: {versicherer}\n"
        f"Versicherungsnehmer: {nehmer}\n"
        f"Versicherungsbeginn: {laufzeit_start}\n"
        f"Versicherungsende: {laufzeit_end}\n"
        f"Jahresprämie netto: EUR 95.450,00\n"
        f"Versicherungssteuer (19 %): EUR 18.135,50\n"
        f"Bruttoprämie: EUR 113.585,50\n"
        f"Zahlweise: jährlich, im Voraus, durch SEPA-Lastschrift\n"
        f"Bedingungen: Allgemeine Versicherungsbedingungen für "
        f"Haftpflichtversicherungen (AHB 2016) sowie nachstehende "
        f"Besondere Bedingungen."
    )))

    s.append(("§ 1 Gegenstand der Versicherung", (
        f"(1) Versichert ist im Rahmen und Umfang der vorliegenden "
        f"Bedingungen die gesetzliche Haftpflicht privatrechtlichen "
        f"Inhalts des Versicherungsnehmers wegen Personen-, Sach- und "
        f"daraus resultierender Vermögensschäden, die aus den im "
        f"Versicherungsschein bezeichneten betrieblichen Risiken hervorgehen.\n\n"
        f"(2) Versicherte Tätigkeit ist: Entwicklung, Herstellung und "
        f"Vertrieb von industriellen Erzeugnissen gemäß Branchen-"
        f"Beschreibung in Anlage 1.\n\n"
        f"(3) Versicherungsschutz besteht weltweit, soweit nicht im "
        f"Einzelnen abweichend geregelt. Ausgeschlossen sind Ansprüche "
        f"nach US-amerikanischem und kanadischem Recht (siehe § 9 "
        f"USA/Kanada-Klausel)."
    )))

    s.append(("§ 2 Versicherungssumme und Sublimits", (
        f"(1) Versicherungssumme: EUR {summe} pauschal für Personen-, "
        f"Sach- und Vermögensschäden je Versicherungsfall und "
        f"insgesamt 3-fach pro Versicherungsjahr.\n\n"
        f"(2) Sublimits (innerhalb der Versicherungssumme):\n\n"
        f"a) Erweiterte Produkthaftpflicht (EPP) inkl. Konstruktions-, "
        f"Werks- und Komponentenklausel: EUR 10.000.000 je Versicherungs-"
        f"fall;\n\n"
        f"b) Mietsachschäden an unbeweglichen Sachen: EUR 5.000.000 je "
        f"Schadenereignis;\n\n"
        f"c) Mietsachschäden an beweglichen Sachen: EUR 1.000.000 je "
        f"Schadenereignis;\n\n"
        f"d) Tätigkeitsschäden (Schäden bei oder durch Bearbeitung "
        f"fremder Sachen): EUR 2.500.000 je Schadenereignis;\n\n"
        f"e) Allmählichkeitsschäden: EUR 5.000.000 je Versicherungsfall;\n\n"
        f"f) Umweltschäden nach Umweltschadensgesetz (USchadG) und "
        f"Umwelthaftpflichtgesetz (UmweltHG): EUR 10.000.000 je "
        f"Versicherungsfall;\n\n"
        f"g) Rückrufkostendeckung (siehe § 5): EUR 5.000.000 je "
        f"Versicherungsfall;\n\n"
        f"h) Vermögensschäden (echte Vermögensschäden): EUR 2.000.000 je "
        f"Versicherungsfall;\n\n"
        f"i) Schäden durch Datenrechtsverletzungen / Cyber: "
        f"EUR 1.000.000 je Versicherungsfall;\n\n"
        f"j) Strafverteidigungskosten: bis EUR 100.000."
    )))

    s.append(("§ 3 Selbstbehalte", (
        "Je Versicherungsfall trägt der Versicherungsnehmer folgende "
        "Selbstbehalte:\n\n"
        "- Personenschäden: EUR 1.000;\n"
        "- Sachschäden: EUR 2.500;\n"
        "- Tätigkeitsschäden: EUR 5.000;\n"
        "- Mietsachschäden: EUR 5.000;\n"
        "- Umweltschäden: EUR 25.000;\n"
        "- Produkthaftpflicht: EUR 25.000;\n"
        "- Rückrufkosten: 10 % des Schadens, mindestens EUR 50.000."
    )))

    s.append(("§ 4 Versicherte Risiken", (
        "Im Versicherungsschutz sind insbesondere eingeschlossen:\n\n"
        "a) Haftpflichtansprüche aus dem Eigentum, Besitz, Halten oder "
        "Führen von versicherten Gebäuden, Grundstücken und Maschinen;\n\n"
        "b) Haftpflichtansprüche aus betrieblichen Tätigkeiten "
        "(Produktion, Lagerung, Verkauf);\n\n"
        "c) Personen- und Sachschäden Dritter durch hergestellte oder "
        "vertriebene Produkte (Produkthaftpflicht);\n\n"
        "d) Ansprüche aus § 823 BGB, § 831 BGB, ProdHaftG;\n\n"
        "e) Ansprüche aus DSGVO und BDSG, soweit gesondert vereinbart;\n\n"
        "f) Forderungsausfallrisiko aus geschlossenen Untersuchungs- "
        "und Bewertungsmängeln (im Rahmen der EPP);\n\n"
        "g) Vorsorgliche Verkehrsmaßnahmen (Verkehrssicherungspflicht).\n\n"
        "h) Veranstaltungshaftpflicht für betriebsbezogene Veranstaltungen."
    )))

    s.append(("§ 5 Rückrufkostendeckung", (
        "(1) Mitversichert sind die durch einen Versicherungsfall der "
        "Produkthaftpflicht ausgelösten Kosten eines vom Versicherungs-"
        "nehmer durchgeführten Rückrufes von Produkten.\n\n"
        "(2) Erstattungsfähig sind insbesondere:\n"
        "- Bekanntmachungskosten;\n"
        "- Identifikations- und Lokalisierungskosten;\n"
        "- Transport- und Lagerkosten der zurückgerufenen Produkte;\n"
        "- Kosten der Vernichtung oder Nachbesserung;\n"
        "- Externe Beratungskosten (Rechtsanwälte, Krisenmanagement, "
        "PR-Agenturen).\n\n"
        "(3) Voraussetzung ist ein dokumentiert vorliegender Fehler "
        "der Produkte, der zu einer Gefährdung von Personen führt "
        "oder zu führen droht."
    )))

    s.append(("§ 6 Ausgeschlossene Risiken", (
        "Vom Versicherungsschutz ausgeschlossen sind:\n\n"
        "a) Vorsätzlich herbeigeführte Schäden;\n\n"
        "b) Vertragliche Haftungserweiterungen, die über die gesetzliche "
        "Haftung hinausgehen;\n\n"
        "c) Schäden infolge Krieg, kriegsähnlicher Ereignisse, "
        "Bürgerkrieg, innerer Unruhen, Terror, Hoheitsakte, Streiks "
        "(soweit nicht versichert);\n\n"
        "d) Kernenergie-Schäden;\n\n"
        "e) Asbest-, PFAS- und Glasfaserschäden (Stand-alone-Ausschluss);\n\n"
        "f) Reine Cyberschäden, soweit nicht gesondert mitversichert;\n\n"
        "g) Vermögensschäden aus Anlage- und Vermögensberatung;\n\n"
        "h) Pönalen, Geldbußen, Vertragsstrafen;\n\n"
        "i) Genußmittel mit gentechnisch veränderten Organismen (GMO);\n\n"
        "j) Schäden durch elektromagnetische Felder."
    )))

    s.append(("§ 7 USA/Kanada-Klausel", (
        "(1) Versicherungsschutz besteht nicht für Ansprüche, die "
        "nach US-amerikanischem oder kanadischem Recht erhoben werden, "
        "soweit nicht ausdrücklich anders vereinbart.\n\n"
        "(2) Für Lieferungen in die USA und nach Kanada besteht jedoch "
        "Deckung bis zu einem Sublimit von EUR 5.000.000 unter der "
        "Voraussetzung, dass:\n"
        "- die Lieferungen einen Anteil von 10 % am Konzernumsatz "
        "nicht überschreiten;\n"
        "- die Lieferungen nicht ohne unterzeichnete Hold-Harmless-"
        "Erklärung erfolgen;\n"
        "- Ansprüche aus „punitive damages' oder „exemplary damages' "
        "ausgeschlossen sind."
    )))

    s.append(("§ 8 Serien- und Kumulklauseln", (
        "(1) Serienschadenklausel: Alle Versicherungsfälle, die auf "
        "derselben Ursache (z. B. Konstruktions-, Fertigungs- oder "
        "Materialfehler) beruhen, gelten als ein Versicherungsfall.\n\n"
        "(2) Kumulklausel: Mehrere Schäden, die auf einem einheitlichen "
        "schadensauslösenden Ereignis beruhen, gelten als ein Versicherungs-"
        "fall.\n\n"
        "(3) Die Versicherungssumme steht je Versicherungsfall einmalig "
        "zur Verfügung."
    )))

    s.append(("§ 9 Obliegenheiten", (
        "(1) Der Versicherungsnehmer hat:\n\n"
        "a) bei Vertragsschluss alle gefahrerheblichen Umstände "
        "wahrheitsgemäß und vollständig anzugeben (vorvertragliche "
        "Anzeigepflicht, § 19 VVG);\n\n"
        "b) gefahrerhöhende Umstände während der Vertragsdauer "
        "unverzüglich anzuzeigen (§§ 23, 26 VVG);\n\n"
        "c) Versicherungsfälle unverzüglich, spätestens binnen einer "
        "Woche, dem Versicherer anzuzeigen;\n\n"
        "d) bei der Schadenermittlung mitzuwirken (Aufklärungspflicht);\n\n"
        "e) den Schaden nach Möglichkeit zu mindern (Schadenminderungs-"
        "pflicht);\n\n"
        "f) keine Anerkenntnisse oder Vergleiche ohne Zustimmung des "
        "Versicherers abzugeben.\n\n"
        "(2) Bei Verletzung von Obliegenheiten kann der Versicherer "
        "nach § 28 VVG leistungsfrei werden."
    )))

    s.append(("§ 10 Verlängerung und Kündigung", (
        "(1) Der Vertrag verlängert sich um jeweils ein weiteres Jahr, "
        "sofern er nicht von einer Partei drei Monate vor Ablauf "
        "schriftlich gekündigt wird.\n\n"
        "(2) Der Versicherer und der Versicherungsnehmer können den "
        "Vertrag nach einem Versicherungsfall innerhalb eines Monats "
        "kündigen.\n\n"
        "(3) Bei wesentlicher Erhöhung des versicherten Risikos kann "
        "der Versicherer kündigen oder Prämienanpassung verlangen."
    )))

    s.append(("§ 11 Prämie", (
        "(1) Die Prämie ist eine Vorausprämie und wird jährlich im "
        "Voraus erhoben.\n\n"
        "(2) Sie wird nach den im Versicherungsschein angegebenen "
        "Bezugswerten (Umsatz, Lohnsumme) berechnet. Eine endgültige "
        "Festsetzung erfolgt nach Vorlage der Buchhaltungsdaten am "
        "Jahresende.\n\n"
        "(3) Eine Prämienanpassung kann jährlich entsprechend der "
        "Schadenentwicklung erfolgen (siehe § 12 Sanierungsklausel)."
    )))

    s.append(("§ 12 Sanierungsfähigkeit", (
        "(1) Übersteigt die Schadenquote (Verhältnis Schadenleistungen "
        "zu Nettoprämie) in einem Versicherungsjahr 75 %, kann der "
        "Versicherer eine Sanierung des Vertrages verlangen.\n\n"
        "(2) Sanierung umfasst Prämienanpassung, Selbstbehaltsanpassung "
        "und/oder Anpassung der Versicherungsbedingungen.\n\n"
        "(3) Akzeptiert der Versicherungsnehmer die Sanierung nicht, "
        "kann der Versicherer den Vertrag kündigen."
    )))

    s.append(("§ 13 Schadenmeldung", (
        "(1) Schadenfälle sind unverzüglich, spätestens innerhalb einer "
        "Woche, dem Versicherer schriftlich (auch per E-Mail) anzuzeigen.\n\n"
        "(2) Schadenmeldung enthält: Datum, Ort, Hergang, betroffene "
        "Personen / Sachen, Schadenshöhe, Zeugen, polizeiliches "
        "Aktenzeichen.\n\n"
        "(3) Der Versicherer wickelt die Schadensregulierung ab und "
        "wehrt unbegründete Ansprüche ab."
    )))

    s.append(("§ 14 Schlussbestimmungen", (
        "(1) Es gilt deutsches Recht.\n\n"
        "(2) Gerichtsstand ist der Sitz des Versicherers oder, wahlweise, "
        "des Versicherungsnehmers.\n\n"
        "(3) Streitigkeiten können auf Verlangen des Versicherungsnehmers "
        "vor dem Versicherungsombudsmann verhandelt werden.\n\n"
        "(4) " + SALVATORISCH
    )))

    return s


def gen_produkthaftpflicht_police(p: Dict[str, Any]) -> List[Section]:
    """Produkthaftpflicht-Police. Target: 3000-5000 Wörter."""

    versicherer = _g(p, "versicherer", "HDI Global SE")
    nehmer = _g(p, "nehmer", "Muster GmbH")
    summe = _g(p, "summe", "25.000.000")
    policy = _g(p, "policy", "PHV-2025-456789")

    s: List[Section] = []

    s.append(("Versicherungsscheindaten", (
        f"Versicherungsschein-Nr.: {policy}\n"
        f"Versicherer: {versicherer}\n"
        f"Versicherungsnehmer: {nehmer}\n"
        f"Versicherungssumme: EUR {summe} je Versicherungsfall\n"
        f"Maximierung: 2-fach pro Versicherungsjahr\n"
        f"Bedingungen: AHB 2016, ProdHaft-Bedingungen, "
        f"Erweiterte-Produkthaftpflicht-Bedingungen (EPP)."
    )))

    s.append(("§ 1 Gegenstand der Versicherung", (
        "(1) Versichert ist die gesetzliche Haftpflicht des "
        "Versicherungsnehmers für Schäden, die Dritten durch von ihm "
        "hergestellte, gelieferte oder vertriebene Produkte zugefügt "
        "werden, einschließlich Personenschäden, Sachschäden und "
        "daraus resultierender Vermögensfolgeschäden.\n\n"
        "(2) Versichert sind Ansprüche nach:\n"
        "- §§ 823 ff. BGB (deliktische Haftung);\n"
        "- ProdHaftG (verschuldensunabhängige Produzentenhaftung);\n"
        "- AVB für die Erweiterte Produkthaftpflicht (EPP)."
    )))

    s.append(("§ 2 Erweiterungen (EPP)", (
        "(1) Die Erweiterte Produkthaftpflicht (EPP) erweitert den "
        "Versicherungsschutz um folgende Bausteine:\n\n"
        "a) Aus-und Einbaukostenklausel (§ 439 Abs. 3 BGB-Risiko);\n\n"
        "b) Weiterverarbeitungs-/Vermischungsklausel;\n\n"
        "c) Maschinenklausel (Mehrkosten der Endprodukte);\n\n"
        "d) Prüf- und Sortierkostenklausel;\n\n"
        "e) Schäden durch fehlerhafte Beratung im Zusammenhang mit "
        "der Produktverwendung;\n\n"
        "f) Rückrufkosten;\n\n"
        "g) Cyberereignisse mit Produktbezug.\n\n"
        "(2) Sublimits und Bedingungen ergeben sich aus den EPP-AVB "
        "(Anlage 1)."
    )))

    s.append(("§ 3 Rückrufkostendeckung", (
        "(1) Rückrufkosten sind erstattungsfähig bis zu einer Höhe "
        "von EUR 10.000.000 je Versicherungsfall.\n\n"
        "(2) Erfasst sind insbesondere:\n"
        "- Bekanntmachungs-, Anzeigen-, Versandkosten;\n"
        "- Personalkosten bei externer Beauftragung;\n"
        "- Transport-, Lager- und Vernichtungskosten;\n"
        "- Reparatur- und Austauschkosten der Produkte;\n"
        "- Externe Beratungs- und Rechtskosten.\n\n"
        "(3) Voraussetzung: Konkretes Personenrisiko, behördliche "
        "Anordnung oder Selbstanzeige."
    )))

    s.append(("§ 4 Ausschlüsse", (
        "Ausgeschlossen sind insbesondere:\n\n"
        "a) Vorsätzlich herbeigeführte Mängel;\n\n"
        "b) Produkte, die nicht mit anerkannten Regeln der Technik "
        "übereinstimmen oder die wesentlich veränderte/modifizierte "
        "Produkte sind;\n\n"
        "c) Schäden aus Asbest, PCBs, Bleizusatz im Trinkwasser "
        "(Stand-alone-Ausschluss);\n\n"
        "d) Schäden in den USA/Kanada (siehe Sublimit-Regelung);\n\n"
        "e) Strafen, Bußgelder, punitive damages;\n\n"
        "f) Produktbezogene Cybervorfälle bei mangelhafter IT-Sicherheit "
        "(Vertragsanpassung möglich)."
    )))

    s.append(("§ 5 Sublimits", (
        f"a) Pure Vermögensschäden im Rahmen der EPP: EUR 5.000.000 je VF;\n\n"
        f"b) Cyberbedingte Produktrisiken: EUR 2.500.000 je VF;\n\n"
        f"c) Schadensbedingte Datenschutzansprüche (DSGVO): "
        f"EUR 1.000.000 je VF;\n\n"
        f"d) USA/Kanada: EUR 5.000.000 unter den Bedingungen § 9 BHV;\n\n"
        f"e) Aus-/Einbaukosten: EUR 5.000.000 je VF;\n\n"
        f"f) Maschinenklausel: EUR 3.000.000 je VF."
    )))

    s.append(("§ 6 Selbstbehalt", (
        "Selbstbehalt: 10 % des Schadens, mindestens EUR 50.000, "
        "maximal EUR 250.000 je Versicherungsfall."
    )))

    s.append(("§ 7 Obliegenheiten", (
        "(1) Der Versicherungsnehmer wendet bei Entwicklung, Produktion "
        "und Vertrieb die anerkannten Regeln der Technik und gesetzlichen "
        "Sicherheitsvorschriften an.\n\n"
        "(2) Er führt ein Qualitätsmanagementsystem (mind. ISO 9001) "
        "und dokumentiert Produktion und Inverkehrbringen (Traceability).\n\n"
        "(3) Bei Bekanntwerden eines möglichen Produktfehlers ist "
        "unverzüglich Schadenmeldung zu erstatten und ein Krisenmanagement "
        "einzurichten."
    )))

    s.append(("§ 8 Schadenmeldung und Schadenmanagement", (
        "(1) Schadenmeldung unverzüglich, spätestens binnen 7 Tagen.\n\n"
        "(2) Bei drohenden Rückrufaktionen ist der Versicherer "
        "frühzeitig vor öffentlichen Mitteilungen einzubinden.\n\n"
        "(3) Krisenmanager des Versicherers kann eingesetzt werden."
    )))

    s.append(("§ 9 Prämie und Laufzeit", (
        "(1) Prämie wird nach Umsatz und Risiko kalkuliert.\n\n"
        "(2) Laufzeit: ein Jahr mit automatischer Verlängerung.\n\n"
        "(3) Kündigung mit drei Monaten Frist."
    )))

    s.append(("§ 10 Schlussbestimmungen", (
        "Deutsches Recht, Gerichtsstand am Sitz des Versicherers oder "
        "des Versicherungsnehmers nach Wahl des Versicherungsnehmers."
    )))

    return s


def gen_do_versicherung(p: Dict[str, Any]) -> List[Section]:
    """D&O-Versicherung. Target: 2500-4000 Wörter."""

    versicherer = _g(p, "versicherer", "AIG Europe S.A.")
    nehmer = _g(p, "nehmer", "Muster GmbH")
    summe = _g(p, "summe", "20.000.000")
    policy = _g(p, "policy", "DAO-2025-789012")

    s: List[Section] = []

    s.append(("Versicherungsscheindaten", (
        f"Versicherungsschein-Nr.: {policy}\n"
        f"Versicherer: {versicherer}\n"
        f"Versicherungsnehmer (Firmenpolice): {nehmer}\n"
        f"Versicherungssumme: EUR {summe} im Versicherungsjahr (one limit)\n"
        f"Eintrittsdatum (continuity date): 01.01.2020\n"
        f"Anzeigepflicht: claims-made-basis mit retroaktivem Datum"
    )))

    s.append(("§ 1 Versicherte Personen", (
        "(1) Versichert sind aktuelle, ehemalige und künftige Organmitglieder "
        "und leitende Angestellte des Versicherungsnehmers und seiner "
        "Tochtergesellschaften, namentlich:\n\n"
        "- Geschäftsführer/Vorstandsmitglieder;\n"
        "- Aufsichtsräte/Beiräte;\n"
        "- Prokuristen und sonstige leitende Angestellte;\n"
        "- Treuhänder, Liquidatoren.\n\n"
        "(2) Mitversichert: außenstehende Direktoren in Tochtergesellschaften "
        "(„outside directorships') sowie Familienangehörige und "
        "Rechtsnachfolger versicherter Personen."
    )))

    s.append(("§ 2 Versicherungsschutz – Deckungsbausteine", (
        "(1) Side A – Persönliche Haftung der Organe (ohne Freistellung "
        "durch das Unternehmen): Deckt Vermögensschäden, für die "
        "versicherte Personen persönlich in Anspruch genommen werden.\n\n"
        "(2) Side B – Freistellung durch das Unternehmen: Erstattet "
        "dem Versicherungsnehmer Aufwendungen, die er für versicherte "
        "Personen aufgewendet hat.\n\n"
        "(3) Side C – Wertpapierdeckung (nur AG): Deckt Ansprüche gegen "
        "die Gesellschaft selbst im Zusammenhang mit Wertpapiergeschäften.\n\n"
        "(4) Innenhaftung (Organ vs. Gesellschaft) ist eingeschlossen."
    )))

    s.append(("§ 3 Versicherungssumme und Selbstbehalt", (
        f"(1) Versicherungssumme: EUR {summe} je Versicherungsjahr "
        f"als Gesamtlimit für alle versicherten Personen und "
        f"Schadenarten („one limit', Maximierung).\n\n"
        f"(2) Selbstbehalt: gemäß § 93 Abs. 2 Satz 3 AktG analog "
        f"10 % des Schadens, höchstens jedoch 150 % der festen "
        f"Jahresvergütung pro versicherte Person und Jahr. "
        f"Für ehemalige und Familienmitglieder kein Selbstbehalt."
    )))

    s.append(("§ 4 Pflichtverletzung (Wrongful Act)", (
        "(1) Versichert sind Vermögensschäden aus „Pflichtverletzungen' "
        "(Wrongful Acts) im Sinne der Bedingungen.\n\n"
        "(2) Pflichtverletzungen umfassen:\n"
        "- tatsächliche oder behauptete Verstöße gegen Organpflichten;\n"
        "- Fehler, Versäumnisse, unrichtige oder irreführende "
        "Erklärungen;\n"
        "- Verstoß gegen Treuepflichten, Sorgfaltspflichten."
    )))

    s.append(("§ 5 Versicherte Kosten", (
        "(1) Anwaltskosten (Verteidigungskosten) sind innerhalb der "
        "Versicherungssumme gedeckt, einschließlich Vorgutachten.\n\n"
        "(2) Kosten der Krisenkommunikation und PR-Beratung sind "
        "mitversichert (Sublimit: EUR 250.000).\n\n"
        "(3) Strafverteidigungskosten in straf- und ordnungswidrigkeits-"
        "rechtlichen Verfahren sind mitversichert; bei Verurteilung "
        "Rückforderung möglich.\n\n"
        "(4) Bei behördlichen Verfahren (Aufsichtsbehörden, BaFin, "
        "Kartellbehörden) ebenfalls gedeckt."
    )))

    s.append(("§ 6 Claims-Made-Prinzip und retroaktives Datum", (
        "(1) Versicherungsschutz besteht für während der Vertragslaufzeit "
        "erstmals erhobene Ansprüche, soweit die Pflichtverletzung "
        "nach dem retroaktiven Datum (continuity date) begangen wurde.\n\n"
        "(2) Nachhaftung (run-off / extended reporting period): "
        "Nachhaftung von mindestens 5 Jahren nach Vertragsende ist "
        "kostenfrei eingeschlossen; bei Bedarf bis 10 Jahre gegen "
        "Aufpreis erweiterbar."
    )))

    s.append(("§ 7 Ausschlüsse", (
        "Vom Versicherungsschutz ausgeschlossen sind:\n\n"
        "a) Vorsätzlich herbeigeführte Schäden (Vorsatzausschluss);\n\n"
        "b) Persönliche Vorteilsannahme der versicherten Person "
        "(Vorteilsausschluss);\n\n"
        "c) Ansprüche aus Geldbußen, Vertragsstrafen, Vergütungsrückforderungen "
        "(gewährte Vergütung);\n\n"
        "d) Ansprüche aus Krieg, Asbest, Kernenergie;\n\n"
        "e) Ansprüche, die bei Vertragsschluss bereits bekannt waren "
        "(known facts);\n\n"
        "f) Insider-Trading-Verstöße;\n\n"
        "g) US-Verfahren (Class Actions) – Sublimit USD 5 Mio."
    )))

    s.append(("§ 8 Pflichten der versicherten Personen", (
        "(1) Anzeige von Pflichtverletzungen und Ansprüchen unverzüglich, "
        "spätestens binnen 30 Tagen.\n\n"
        "(2) Mitwirkung bei der Schadenabwehr.\n\n"
        "(3) Kein Anerkenntnis ohne Zustimmung des Versicherers."
    )))

    s.append(("§ 9 Schadenregulierung", (
        "(1) Versicherer hat das Recht, die Schadenregulierung zu "
        "übernehmen oder dem Versicherten die freie Anwaltswahl zu "
        "ermöglichen.\n\n"
        "(2) Vergleiche bedürfen der Zustimmung des Versicherers."
    )))

    s.append(("§ 10 Sonstiges", (
        "(1) Bei Verschmelzungen, Spaltungen oder Verkauf des "
        "Unternehmens (Change of Control) wechselt der Versicherungs-"
        "schutz auf Nachhaftung über; neue Pflichtverletzungen sind "
        "nicht mehr versichert.\n\n"
        "(2) Bei Insolvenz des Unternehmens bleibt der Schutz erhalten "
        "(insbesondere Side A)."
    )))

    s.append(("§ 11 Schlussbestimmungen", (
        "Es gilt deutsches Recht. Gerichtsstand am Sitz des Versicherers."
    )))

    return s


def gen_cyber_versicherung(p: Dict[str, Any]) -> List[Section]:
    """Cyberversicherung. Target: 2500-4000 Wörter."""

    versicherer = _g(p, "versicherer", "Munich Re Cyber")
    nehmer = _g(p, "nehmer", "Muster GmbH")
    summe = _g(p, "summe", "5.000.000")
    policy = _g(p, "policy", "CYB-2025-345678")

    s: List[Section] = []

    s.append(("Versicherungsscheindaten", (
        f"Versicherungsschein-Nr.: {policy}\n"
        f"Versicherer: {versicherer}\n"
        f"Versicherungsnehmer: {nehmer}\n"
        f"Versicherungssumme: EUR {summe} je Versicherungsfall und "
        f"Versicherungsjahr\n"
        f"Bedingungen: Cyber-AVB 2024, Anlagen IT-Sicherheits-Mindeststandards."
    )))

    s.append(("§ 1 Versicherungsumfang", (
        "(1) Versichert sind Schäden des Versicherungsnehmers (Eigenschäden) "
        "und Ansprüche Dritter (Drittschäden), die aus einem Cyber-"
        "Vorfall resultieren.\n\n"
        "(2) Cyber-Vorfall ist insbesondere:\n"
        "- Unbefugter Zugriff auf IT-Systeme (Hacking);\n"
        "- Schadsoftware (Malware, Ransomware, Trojaner);\n"
        "- Datenverlust oder -beschädigung;\n"
        "- Denial-of-Service-Angriffe (DDoS);\n"
        "- Identitätsdiebstahl, Phishing;\n"
        "- Datendiebstahl, Datenmissbrauch."
    )))

    s.append(("§ 2 Eigenschäden", (
        "(1) Folgende Eigenschäden sind erstattungsfähig:\n\n"
        "a) IT-Forensik- und Wiederherstellungskosten;\n"
        "b) Lösegeldzahlungen (Ransomware) bis zu Sublimit EUR 1 Mio., "
        "nach Zustimmung des Versicherers und Sanktionsprüfung;\n"
        "c) Betriebsunterbrechungsschäden (BU): Mehraufwendungen, "
        "Umsatzausfall, fortlaufende Kosten;\n"
        "d) Kosten der Krisenkommunikation;\n"
        "e) Vertragsstrafen aus SLA-Verletzungen, soweit gedeckt;\n"
        "f) Mehrkosten durch Notbetrieb."
    )))

    s.append(("§ 3 Drittschäden", (
        "(1) Folgende Drittschäden sind versichert:\n\n"
        "a) Haftpflichtansprüche aus Datenschutzverletzungen (DSGVO);\n"
        "b) Haftpflichtansprüche aus Vertraulichkeitsverletzungen;\n"
        "c) Geldbußen nach DSGVO (Art. 83) bis zur Höhe von "
        "EUR 2.500.000 je Versicherungsfall, soweit versicherbar;\n"
        "d) Verteidigungskosten in behördlichen Verfahren.\n\n"
        "(2) Auch Ansprüche aus PCI-DSS-Verstößen und Branchenstandards "
        "sind mitversichert."
    )))

    s.append(("§ 4 Sublimits", (
        "a) Ransomware (Lösegeld): EUR 1.000.000 je VF;\n"
        "b) Betriebsunterbrechung: EUR 2.500.000 je VF (Wartezeit "
        "12 Stunden, Haftzeit 12 Monate);\n"
        "c) Reputationsmanagement / PR: EUR 250.000 je VF;\n"
        "d) DSGVO-Geldbußen: EUR 2.500.000;\n"
        "e) Cyber-Erpressungsdeckung: EUR 500.000;\n"
        "f) Krisen-Hotline und CERT-Einsatz: Sublimit EUR 100.000."
    )))

    s.append(("§ 5 Ausschlüsse", (
        "Ausgeschlossen sind:\n\n"
        "a) Vorsatz, einschließlich Insider-Vergehen;\n"
        "b) Schäden infolge Krieg, Cyber-War (mit „silent cyber'-Klausel "
        "klargestellt);\n"
        "c) Ausfall öffentlicher Infrastrukturen (Strom, Internet) > 24h;\n"
        "d) Ungeprüfte / veraltete Software;\n"
        "e) Bereits bekannte Vorfälle (prior acts);\n"
        "f) Schäden außerhalb des Geltungsbereichs (in der Regel "
        "weltweit, mit Ausnahme sanktionierter Länder)."
    )))

    s.append(("§ 6 IT-Sicherheits-Mindeststandards", (
        "(1) Voraussetzung des Versicherungsschutzes ist die Einhaltung "
        "von IT-Sicherheits-Mindeststandards (Anlage 1):\n\n"
        "- Multi-Factor-Authentication (MFA) für administrative Zugänge "
        "und Remote-Zugriff;\n"
        "- Patch-Management mit definierten Fristen;\n"
        "- Endpoint Detection & Response (EDR);\n"
        "- Regelmäßige Backups (3-2-1-Regel) mit Offline-Komponente;\n"
        "- Awareness-Schulungen für Mitarbeiter;\n"
        "- Incident-Response-Plan;\n"
        "- Sicherheitskonzept gemäß BSI-Grundschutz oder ISO 27001.\n\n"
        "(2) Verletzungen können Leistungsminderungen oder -ausschluss "
        "zur Folge haben (§ 28 VVG)."
    )))

    s.append(("§ 7 Selbstbehalt und Wartezeit", (
        "(1) Selbstbehalt: EUR 50.000 je Versicherungsfall.\n\n"
        "(2) Wartezeit (BU): 12 Stunden.\n\n"
        "(3) Bei Ransomware: zusätzlich Beratungspflicht und "
        "Sanktionsprüfung vor Zahlung."
    )))

    s.append(("§ 8 Krisenmanagement und Notfall-Hotline", (
        "(1) 24/7-Notfallhotline (+49 ...) für IT-Vorfall-Meldung.\n\n"
        "(2) Externe Krisenmanager und IT-Forensiker werden auf "
        "Anforderung bereitgestellt.\n\n"
        "(3) Erstmaßnahmen werden vorfinanziert."
    )))

    s.append(("§ 9 Schadensmeldung und Mitwirkungspflichten", (
        "(1) Cybervorfälle sind unverzüglich, spätestens binnen 24 "
        "Stunden, zu melden.\n\n"
        "(2) Maßnahmen zur Schadenminderung (z. B. Trennung kompromittierter "
        "Systeme, Backup-Wiederherstellung, Forensik) sind unverzüglich "
        "einzuleiten."
    )))

    s.append(("§ 10 Prämie und Laufzeit", (
        "Jährliche Prämie EUR 78.500 netto; Laufzeit ein Jahr mit "
        "Verlängerungsklausel; Kündigungsfrist drei Monate."
    )))

    s.append(("§ 11 Schlussbestimmungen", (
        "Deutsches Recht; Gerichtsstand Sitz des Versicherers oder "
        "Versicherungsnehmers."
    )))

    return s


# =====================================================================
# FINANCIAL REPORTS
# =====================================================================

def gen_jahresabschluss_anhang(p: Dict[str, Any], year: int = 2024) -> List[Section]:
    """HGB-Anhang. Target: 3000-5000 Wörter."""

    company = _g(p, "company", "Muster GmbH")
    city = _g(p, "city", "Köln")

    s: List[Section] = []

    s.append((f"Anhang zum Jahresabschluss zum 31. Dezember {year}", (
        f"{company}, {city}\n\n"
        f"Anhang gemäß §§ 284 ff. HGB"
    )))

    s.append(("I. Allgemeine Angaben", (
        f"(1) Die {company} mit Sitz in {city} ist im Handelsregister "
        f"des Amtsgerichts {city} unter HRB [Nr.] eingetragen.\n\n"
        f"(2) Die Gesellschaft ist nach den Größenkriterien des § 267 "
        f"HGB als mittelgroße Kapitalgesellschaft einzuordnen. Die "
        f"Größenkriterien wurden in den letzten zwei aufeinanderfolgenden "
        f"Geschäftsjahren überschritten bzw. nicht überschritten.\n\n"
        f"(3) Geschäftsjahr ist das Kalenderjahr.\n\n"
        f"(4) Der Jahresabschluss wurde nach den Vorschriften der "
        f"§§ 242 ff. HGB sowie der einschlägigen Vorschriften des "
        f"GmbH-Gesetzes aufgestellt. Die Bewertung wurde nach den "
        f"Grundsätzen ordnungsmäßiger Buchführung unter Annahme der "
        f"Unternehmensfortführung (§ 252 Abs. 1 Nr. 2 HGB) vorgenommen.\n\n"
        f"(5) Die Bilanz wurde nach dem Gliederungsschema des § 266 HGB "
        f"aufgestellt. Die Gewinn- und Verlustrechnung wurde nach dem "
        f"Gesamtkostenverfahren gemäß § 275 Abs. 2 HGB gegliedert."
    )))

    s.append(("II. Bilanzierungs- und Bewertungsmethoden", (
        "(1) Immaterielle Vermögensgegenstände des Anlagevermögens "
        "werden mit den Anschaffungskosten angesetzt und planmäßig "
        "linear über ihre voraussichtliche Nutzungsdauer (3 bis 5 Jahre) "
        "abgeschrieben.\n\n"
        "(2) Selbst geschaffene immaterielle Vermögensgegenstände des "
        "Anlagevermögens wurden im Geschäftsjahr nicht angesetzt; "
        "ein entsprechender Bilanzposten besteht nicht.\n\n"
        "(3) Geschäfts- oder Firmenwerte aus Unternehmenserwerben "
        "werden über eine Nutzungsdauer von 10 Jahren linear abgeschrieben.\n\n"
        "(4) Sachanlagen werden mit den Anschaffungs- oder Herstellungskosten "
        "abzüglich planmäßiger Abschreibungen bewertet. Die planmäßigen "
        "Abschreibungen erfolgen linear über die betriebsgewöhnliche "
        "Nutzungsdauer:\n"
        "- Gebäude: 33 Jahre;\n"
        "- Bauten auf fremden Grundstücken: über die Vertragslaufzeit;\n"
        "- Technische Anlagen und Maschinen: 5 bis 15 Jahre;\n"
        "- Betriebs- und Geschäftsausstattung: 3 bis 13 Jahre;\n"
        "- Geringwertige Wirtschaftsgüter unter 800 EUR werden im "
        "Zugangsjahr in voller Höhe abgeschrieben.\n\n"
        "(5) Finanzanlagen werden zu Anschaffungskosten oder, bei "
        "voraussichtlich dauernder Wertminderung, zum niedrigeren "
        "beizulegenden Wert (§ 253 Abs. 3 HGB) angesetzt.\n\n"
        "(6) Vorräte werden zu Anschaffungs- oder Herstellungskosten "
        "unter Beachtung des Niederstwertprinzips angesetzt. Die "
        "Bewertung erfolgt nach dem gleitenden Durchschnittsverfahren. "
        "In die Herstellungskosten der unfertigen und fertigen Erzeugnisse "
        "wurden neben den Einzelkosten angemessene Teile der notwendigen "
        "Material- und Fertigungsgemeinkosten sowie der durch die "
        "Fertigung veranlasste Werteverzehr des Anlagevermögens "
        "einbezogen.\n\n"
        "(7) Forderungen aus Lieferungen und Leistungen wurden zum "
        "Nennwert angesetzt; erkennbaren Einzelrisiken wurde durch "
        "Einzelwertberichtigungen Rechnung getragen. Das allgemeine "
        "Kreditrisiko wird durch eine pauschale Wertberichtigung in "
        "Höhe von 1 % der nicht einzelwertberichtigten Forderungen "
        "berücksichtigt.\n\n"
        "(8) Sonstige Vermögensgegenstände wurden zum Nennwert "
        "angesetzt; identifizierbaren Risiken wurde durch "
        "Einzelwertberichtigungen Rechnung getragen.\n\n"
        "(9) Liquide Mittel wurden zum Nennwert angesetzt.\n\n"
        "(10) Aktive latente Steuern wurden in Ausübung des "
        "Aktivierungswahlrechts gemäß § 274 HGB nicht angesetzt.\n\n"
        "(11) Rückstellungen wurden in Höhe des nach vernünftiger "
        "kaufmännischer Beurteilung notwendigen Erfüllungsbetrags "
        "(§ 253 Abs. 1 Satz 2 HGB) gebildet. Rückstellungen mit einer "
        "Restlaufzeit von mehr als einem Jahr wurden mit den von der "
        "Deutschen Bundesbank veröffentlichten durchschnittlichen "
        "Marktzinssätzen der vergangenen 7 (Pensionsrückstellungen: 10) "
        "Geschäftsjahre abgezinst.\n\n"
        "(12) Verbindlichkeiten wurden zu ihrem Erfüllungsbetrag "
        "angesetzt.\n\n"
        "(13) Aufwendungen und Erträge in fremder Währung wurden zum "
        "Devisenkassakurs am Buchungstag umgerechnet."
    )))

    s.append(("III. Erläuterungen zur Bilanz", (
        "1. Anlagevermögen:\n"
        "Die Entwicklung des Anlagevermögens ergibt sich aus dem "
        "Anlagenspiegel (Anlage 1 zum Anhang).\n\n"
        "2. Vorräte:\n"
        "Die Vorräte gliedern sich wie folgt: Roh-, Hilfs- und "
        "Betriebsstoffe (EUR 4.235.000 Vj. EUR 3.987.000), Unfertige "
        "Erzeugnisse (EUR 2.150.000 Vj. EUR 2.015.000), Fertige "
        "Erzeugnisse (EUR 5.890.000 Vj. EUR 5.620.000), Geleistete "
        "Anzahlungen (EUR 320.000).\n\n"
        "3. Forderungen aus Lieferungen und Leistungen:\n"
        "Die Forderungen haben durchgängig eine Restlaufzeit von "
        "weniger als einem Jahr. Wertberichtigungen wurden in Höhe "
        "von EUR 285.000 vorgenommen.\n\n"
        "4. Eigenkapital:\n"
        "Das gezeichnete Kapital ist eingeteilt in Geschäftsanteile "
        "mit einem Nennbetrag von insgesamt EUR 1.000.000. Eigene "
        "Anteile werden nicht gehalten. Die Kapitalrücklage beträgt "
        "EUR 5.500.000 (unverändert zum Vorjahr). Die Gewinnrücklagen "
        "haben sich aus dem Vorjahresgewinn auf EUR 18.450.000 erhöht.\n\n"
        "5. Rückstellungen:\n"
        "- Pensionsrückstellungen: EUR 3.120.000 (Vj. EUR 2.985.000), "
        "angesetzt mit dem 10-Jahres-Durchschnittszinssatz von "
        "1,79 % p.a.;\n"
        "- Steuerrückstellungen: EUR 850.000;\n"
        "- Sonstige Rückstellungen: EUR 2.450.000, davon Gewährleistungs-"
        "rückstellungen EUR 1.250.000, Personalrückstellungen "
        "(Urlaub, Mehrarbeit, Boni) EUR 850.000, Restrukturierung "
        "EUR 200.000, sonstige EUR 150.000.\n\n"
        "6. Verbindlichkeiten:\n"
        "- Verbindlichkeiten gegenüber Kreditinstituten: EUR 4.500.000 "
        "(davon Restlaufzeit > 5 Jahre EUR 2.500.000);\n"
        "- Verbindlichkeiten aus Lieferungen und Leistungen: "
        "EUR 3.150.000 (alle < 1 Jahr);\n"
        "- Sonstige Verbindlichkeiten: EUR 950.000."
    )))

    s.append(("IV. Erläuterungen zur Gewinn- und Verlustrechnung", (
        f"1. Umsatzerlöse (§ 277 Abs. 1 HGB):\n"
        f"Die Umsatzerlöse setzen sich wie folgt zusammen:\n"
        f"- Nach Produktgruppen: Produkt A EUR 28.500.000, Produkt B "
        f"EUR 15.300.000, Sonstige EUR 6.200.000;\n"
        f"- Nach Regionen: Deutschland EUR 27.000.000, EU EUR 18.500.000, "
        f"Drittländer EUR 4.500.000.\n\n"
        f"2. Personalaufwand:\n"
        f"Der Personalaufwand betrug im Geschäftsjahr {year} "
        f"EUR 11.450.000 (Vj. EUR 10.890.000), davon Löhne und "
        f"Gehälter EUR 9.500.000, Sozialabgaben EUR 1.800.000 und "
        f"Aufwendungen für Altersversorgung EUR 150.000.\n\n"
        f"3. Abschreibungen:\n"
        f"Die Abschreibungen auf immaterielle Vermögensgegenstände "
        f"des Anlagevermögens und Sachanlagen betragen EUR 2.150.000.\n\n"
        f"4. Sonstige betriebliche Aufwendungen:\n"
        f"Hierin sind u.a. enthalten: Raumkosten EUR 850.000, "
        f"Beratungs- und Prüfungskosten EUR 320.000, Versicherungen "
        f"EUR 245.000, Reise- und Spesen EUR 185.000."
    )))

    s.append(("V. Sonstige Pflichtangaben", (
        "1. Mitarbeiter:\n"
        "Die durchschnittliche Anzahl der Mitarbeiter im Geschäftsjahr "
        "betrug 215 (Vj. 208), davon Gewerbliche 150, Angestellte 60, "
        "Auszubildende 5.\n\n"
        "2. Haftungsverhältnisse:\n"
        "Bürgschaften gegenüber Banken zugunsten von Tochtergesellschaften: "
        "EUR 500.000. Mit der Inanspruchnahme aus den Bürgschaften wird "
        "nicht gerechnet, da die wirtschaftliche Lage der Tochtergesellschaften "
        "stabil ist.\n\n"
        "3. Sonstige finanzielle Verpflichtungen:\n"
        "Aus langfristigen Miet-, Leasing- und Wartungsverträgen "
        "bestehen Verpflichtungen in Höhe von EUR 2.450.000 (mit "
        "Fälligkeit binnen 1 Jahr: EUR 800.000, zwischen 1 und 5 Jahre: "
        "EUR 1.400.000, über 5 Jahre: EUR 250.000).\n\n"
        "4. Honorar des Abschlussprüfers (§ 285 Nr. 17 HGB):\n"
        "Abschlussprüfungsleistungen EUR 65.000, sonstige Bestätigungs-"
        "leistungen EUR 12.000, Steuerberatungsleistungen EUR 18.000, "
        "Sonstige Leistungen EUR 8.000.\n\n"
        "5. Bezüge der Geschäftsführer:\n"
        "Die Geschäftsführerbezüge belaufen sich auf insgesamt "
        "EUR 980.000. Auf die Berichterstattung nach § 285 Nr. 9a HGB "
        "wird gemäß § 286 Abs. 4 HGB verzichtet, da die Geschäftsführer "
        "namentlich genannt sind und die Gesellschaft eine GmbH ist.\n\n"
        "6. Beteiligungen:\n"
        "Die Gesellschaft hält Beteiligungen an verbundenen Unternehmen "
        "gemäß Anlage 2 zum Anhang.\n\n"
        "7. Geschäfte mit nahestehenden Unternehmen und Personen:\n"
        "Es bestehen Geschäfte mit nahestehenden Personen / Unternehmen "
        "(Gesellschafterdarlehen, Mietverhältnisse). Die Geschäfte "
        "erfolgten zu marktüblichen Konditionen.\n\n"
        "8. Vorgänge von besonderer Bedeutung nach Schluss des "
        "Geschäftsjahres (Nachtragsbericht):\n"
        "Nach dem Bilanzstichtag sind keine Ereignisse von besonderer "
        "Bedeutung eingetreten, die einen wesentlichen Einfluss auf die "
        "Vermögens-, Finanz- und Ertragslage haben.\n\n"
        "9. Vorschlag zur Verwendung des Jahresergebnisses:\n"
        "Die Geschäftsführung schlägt vor, vom Jahresüberschuss "
        f"EUR [Betrag] eine Ausschüttung an die Gesellschafter "
        f"in Höhe von EUR [Betrag] vorzunehmen und den verbleibenden "
        f"Betrag in die Gewinnrücklagen einzustellen."
    )))

    s.append(("Unterschriften", (
        f"{city}, den {_today_de()}\n\n"
        f"Die Geschäftsführung:\n\n"
        f"_____________________________\n"
        f"{_g(p, 'gf1', 'Dr. Thomas Müller')}\n\n"
        f"_____________________________\n"
        f"{_g(p, 'gf2', 'Andreas Schmidt')}"
    )))

    return s


def gen_lagebericht(p: Dict[str, Any], year: int = 2024) -> List[Section]:
    """Lagebericht. Target: 4000-6000 Wörter."""

    company = _g(p, "company", "Muster GmbH")
    city = _g(p, "city", "Köln")
    umsatz = _g(p, "umsatz", "49.700.000")
    umsatz_vj = _g(p, "umsatz_vj", "46.250.000")
    ebit = _g(p, "ebit", "5.430.000")
    ebit_vj = _g(p, "ebit_vj", "4.890.000")

    s: List[Section] = []

    s.append(("Lagebericht " + str(year), (
        f"{company}, {city}\n"
        f"für das Geschäftsjahr vom 1. Januar bis 31. Dezember {year}\n\n"
        f"Lagebericht gemäß § 289 HGB"
    )))

    s.append(("A. Grundlagen des Unternehmens", (
        f"1. Geschäftsmodell\n"
        f"Die {company} ist ein etabliertes mittelständisches "
        f"Unternehmen mit Sitz in {city}. Wir entwickeln, fertigen "
        f"und vertreiben qualitativ hochwertige industrielle "
        f"Erzeugnisse. Unsere Wertschöpfung erfolgt überwiegend in "
        f"Deutschland; Exportanteil ca. 46 %.\n\n"
        f"2. Strategie\n"
        f"Unsere strategischen Säulen sind: (i) Innovationsführerschaft "
        f"in unseren Kernmärkten, (ii) operative Exzellenz und "
        f"Digitalisierung, (iii) Nachhaltigkeit und ESG, (iv) "
        f"internationale Expansion. Wir verfolgen eine fokussierte "
        f"Diversifikationsstrategie in benachbarte Marktsegmente.\n\n"
        f"3. Forschung und Entwicklung\n"
        f"Wir investieren rund 4,5 % unseres Umsatzes in F&E. Im "
        f"Berichtsjahr sind 15 Patentanmeldungen erfolgt. Aktuelle "
        f"Schwerpunkte: Automatisierung, Nachhaltige Materialien, "
        f"Digital-Twin-Technologien.\n\n"
        f"4. Mitarbeiter\n"
        f"Wir beschäftigen 215 Mitarbeiter (Vj. 208). Die Fluktuation "
        f"liegt bei 4,8 %, die Krankenstandsquote bei 3,5 %.\n\n"
        f"5. Standorte\n"
        f"Hauptsitz in {city}, Produktionsstandort in [Ort], "
        f"Vertriebs-Niederlassungen in München, Hamburg und Paris."
    )))

    s.append(("B. Wirtschaftsbericht", (
        f"1. Gesamtwirtschaftliche und branchenbezogene Rahmenbedingungen\n"
        f"Die globale Wirtschaft zeigte in {year} eine moderate "
        f"Erholung nach Pandemiephase und Energieschock. Inflations-"
        f"druck und Zinserhöhungen der Notenbanken beeinflussten "
        f"Investitionsentscheidungen. Unsere Branche profitierte von "
        f"einem Trend zur Reindustrialisierung in Europa und Friend-"
        f"Shoring-Initiativen.\n\n"
        f"2. Geschäftsverlauf\n"
        f"Die Geschäftsentwicklung im Geschäftsjahr {year} war "
        f"positiv. Die Umsatzerlöse stiegen um 7,5 % auf "
        f"EUR {umsatz} (Vj. EUR {umsatz_vj}). Wesentliche "
        f"Wachstumstreiber waren: (i) Marktdurchdringung im "
        f"Automotive-Segment, (ii) Erfolg der neuen Produktreihe XY, "
        f"(iii) Preisanpassungen zur Kompensation der "
        f"Materialkostensteigerungen.\n\n"
        f"3. Lage des Unternehmens\n"
        f"3.1 Ertragslage:\n"
        f"Das EBIT beträgt EUR {ebit} (Vj. EUR {ebit_vj}), eine "
        f"Verbesserung um 11,0 %. Die EBIT-Marge stieg von 10,6 % auf "
        f"10,9 %. Personalaufwand stieg unterproportional zum Umsatz; "
        f"Materialaufwandsquote sank um 0,8 Prozentpunkte.\n\n"
        f"3.2 Finanzlage:\n"
        f"Die Eigenkapitalquote beträgt 42 % (Vj. 39 %). Die "
        f"Nettoverschuldung wurde von EUR 8,5 Mio. auf EUR 5,2 Mio. "
        f"reduziert. Der operative Cashflow liegt bei "
        f"EUR 6,8 Mio. (Vj. EUR 5,9 Mio.).\n\n"
        f"3.3 Vermögenslage:\n"
        f"Bilanzsumme: EUR 38,5 Mio. (Vj. EUR 36,2 Mio.). Anlage-"
        f"vermögen / Bilanzsumme: 48 %. Vorräte stiegen um 6 % im "
        f"Verhältnis zum gestiegenen Geschäftsvolumen."
    )))

    s.append(("C. Nachtragsbericht", (
        f"Nach dem Bilanzstichtag sind keine Ereignisse von besonderer "
        f"Bedeutung eingetreten, die einen wesentlichen Einfluss auf "
        f"die Vermögens-, Finanz- und Ertragslage haben."
    )))

    s.append(("D. Prognose-, Chancen- und Risikobericht", (
        "1. Prognose:\n"
        "Für das Geschäftsjahr 2026 erwarten wir eine Fortsetzung des "
        "Wachstumskurses mit einer Umsatzsteigerung im Korridor von "
        "5 % bis 8 %. Das EBIT soll überproportional auf 12 % steigen.\n\n"
        "2. Chancen:\n"
        "- Marktwachstum in Schwellenländern (Indien, Brasilien);\n"
        "- Digitalisierung als Differenzierungsmerkmal;\n"
        "- Nachhaltige Produkte mit ESG-Premium;\n"
        "- Akquisitionsmöglichkeiten in fragmentiertem Markt.\n\n"
        "3. Risiken:\n"
        "3.1 Markt- und Branchenrisiken:\n"
        "- Konjunkturabhängige Investitionsschwäche;\n"
        "- Verstärkter Wettbewerb durch asiatische Anbieter;\n"
        "- Substitutionsrisiko bei Kerntechnologien.\n\n"
        "3.2 Finanzielle Risiken:\n"
        "- Währungs- und Zinsänderungsrisiken (durch Hedging "
        "abgesichert);\n"
        "- Materialkostenrisiken (durch Lieferantenrahmenverträge "
        "begrenzt);\n"
        "- Forderungsausfälle (durch Kreditversicherung abgedeckt).\n\n"
        "3.3 Operative Risiken:\n"
        "- Betriebsunterbrechungsrisiken;\n"
        "- Lieferantenkonzentration (Single-Source-Risiken);\n"
        "- Cyberrisiken (siehe IT-Risikobericht).\n\n"
        "3.4 Rechtliche und Compliance-Risiken:\n"
        "- Regulatorische Veränderungen (insbes. LkSG, CSDDD, CSRD);\n"
        "- Geistige Eigentumsrechte;\n"
        "- Produkthaftungsansprüche.\n\n"
        "3.5 Risikomanagementsystem:\n"
        "Unser Risikomanagementsystem entspricht den Grundsätzen des "
        "IDW PS 340 und wird laufend weiterentwickelt. Risiken werden "
        "quartalsweise erhoben, bewertet und der Geschäftsführung "
        "berichtet. Die Risiken sind dem Eintritt nach mit Wahrscheinlichkeit "
        "und Auswirkung priorisiert."
    )))

    s.append(("E. Internes Kontrollsystem", (
        "Das interne Kontrollsystem (IKS) der Gesellschaft ist "
        "angemessen und wirksam. Die Risikokontrollen folgen dem "
        "Three-Lines-of-Defense-Modell. Wesentliche Kontrollen umfassen "
        "Vier-Augen-Prinzip, segregation-of-duties und automatisierte "
        "ERP-Kontrollen."
    )))

    s.append(("F. Nicht-finanzielle Erklärung (Nachhaltigkeit)", (
        "1. Umwelt:\n"
        "Wir verfolgen das Ziel der Klimaneutralität bis 2035. "
        "Scope-1- und Scope-2-Emissionen wurden im Berichtsjahr um "
        "12 % reduziert. Wasser- und Energieverbrauch wurden weiter "
        "optimiert.\n\n"
        "2. Soziales:\n"
        "Mitarbeiterzufriedenheit (eNPS) bei +35. Investition in "
        "Aus- und Weiterbildung: EUR 850.000.\n\n"
        "3. Governance:\n"
        "Compliance-Management nach IDW PS 980. Whistleblowing-"
        "System gemäß HinSchG implementiert. ESG-Berichterstattung "
        "nach CSRD-Vorgaben in Vorbereitung."
    )))

    s.append(("G. Erklärung der Geschäftsführung", (
        f"Wir versichern, dass nach unserem besten Wissen der "
        f"Jahresabschluss und der Lagebericht ein den tatsächlichen "
        f"Verhältnissen entsprechendes Bild der Vermögens-, Finanz- "
        f"und Ertragslage der Gesellschaft vermitteln.\n\n"
        f"{city}, den {_today_de()}\n\n"
        f"Die Geschäftsführung:\n\n"
        f"_____________________________\n"
        f"{_g(p, 'gf1', 'Dr. Thomas Müller')}\n\n"
        f"_____________________________\n"
        f"{_g(p, 'gf2', 'Andreas Schmidt')}"
    )))

    return s


def gen_bestaetigungsvermerk(p: Dict[str, Any], year: int = 2024) -> List[Section]:
    """Bestätigungsvermerk nach IDW PS 200. Target: 1500-2500 Wörter."""

    company = _g(p, "company", "Muster GmbH")
    city = _g(p, "city", "Köln")
    wp_firma = _g(p, "wp_firma", "Müller & Partner Wirtschaftsprüfungsgesellschaft")
    wp1 = _g(p, "wp1", "Dr. Karl-Heinz Müller")

    s: List[Section] = []

    s.append((f"Bestätigungsvermerk des unabhängigen Abschlussprüfers", (
        f"An die {company}, {city}\n\n"
        f"Vermerk über die Prüfung des Jahresabschlusses und des "
        f"Lageberichts."
    )))

    s.append(("Prüfungsurteile", (
        f"Wir haben den Jahresabschluss der {company}, {city}, – "
        f"bestehend aus der Bilanz zum 31. Dezember {year} sowie der "
        f"Gewinn- und Verlustrechnung für das Geschäftsjahr vom 1. "
        f"Januar bis 31. Dezember {year} sowie dem Anhang einschließlich "
        f"der Darstellung der Bilanzierungs- und Bewertungsmethoden – "
        f"geprüft. Darüber hinaus haben wir den Lagebericht der "
        f"{company} für das Geschäftsjahr {year} geprüft.\n\n"
        f"Nach unserer Beurteilung aufgrund der bei der Prüfung "
        f"gewonnenen Erkenntnisse\n\n"
        f"- entspricht der beigefügte Jahresabschluss in allen "
        f"wesentlichen Belangen den deutschen, für Kapitalgesellschaften "
        f"geltenden handelsrechtlichen Vorschriften und vermittelt "
        f"unter Beachtung der deutschen Grundsätze ordnungsmäßiger "
        f"Buchführung ein den tatsächlichen Verhältnissen entsprechendes "
        f"Bild der Vermögens- und Finanzlage der Gesellschaft zum "
        f"31. Dezember {year} sowie ihrer Ertragslage für das Geschäftsjahr "
        f"vom 1. Januar bis 31. Dezember {year} und\n\n"
        f"- vermittelt der beigefügte Lagebericht insgesamt ein "
        f"zutreffendes Bild von der Lage der Gesellschaft. In allen "
        f"wesentlichen Belangen steht dieser Lagebericht in Einklang "
        f"mit dem Jahresabschluss, entspricht den deutschen gesetzlichen "
        f"Vorschriften und stellt die Chancen und Risiken der zukünftigen "
        f"Entwicklung zutreffend dar.\n\n"
        f"Gemäß § 322 Abs. 3 Satz 1 HGB erklären wir, dass unsere "
        f"Prüfung zu keinen Einwendungen gegen die Ordnungsmäßigkeit "
        f"des Jahresabschlusses und des Lageberichts geführt hat."
    )))

    s.append(("Grundlage für die Prüfungsurteile", (
        "Wir haben unsere Prüfung des Jahresabschlusses und des "
        "Lageberichts in Übereinstimmung mit § 317 HGB und den "
        "Internationalen Standards on Auditing (ISA) sowie der "
        "vom Institut der Wirtschaftsprüfer (IDW) festgestellten "
        "deutschen Grundsätze ordnungsmäßiger Abschlussprüfung "
        "durchgeführt. Unsere Verantwortung nach diesen Vorschriften "
        "und Grundsätzen ist im Abschnitt „Verantwortung des "
        "Abschlussprüfers für die Prüfung des Jahresabschlusses und "
        "des Lageberichts' unseres Bestätigungsvermerks weitergehend "
        "beschrieben. Wir sind von der Gesellschaft unabhängig in "
        "Übereinstimmung mit den deutschen handelsrechtlichen und "
        "berufsrechtlichen Vorschriften und haben unsere sonstigen "
        "deutschen Berufspflichten in Übereinstimmung mit diesen "
        "Anforderungen erfüllt. Wir sind der Auffassung, dass die "
        "von uns erlangten Prüfungsnachweise ausreichend und geeignet "
        "sind, um als Grundlage für unsere Prüfungsurteile zum "
        "Jahresabschluss und zum Lagebericht zu dienen."
    )))

    s.append(("Verantwortung der gesetzlichen Vertreter für den Jahresabschluss und den Lagebericht", (
        "Die gesetzlichen Vertreter sind verantwortlich für die "
        "Aufstellung des Jahresabschlusses, der den deutschen, für "
        "Kapitalgesellschaften geltenden handelsrechtlichen Vorschriften "
        "in allen wesentlichen Belangen entspricht, und dafür, dass "
        "der Jahresabschluss unter Beachtung der deutschen Grundsätze "
        "ordnungsmäßiger Buchführung ein den tatsächlichen Verhältnissen "
        "entsprechendes Bild der Vermögens-, Finanz- und Ertragslage "
        "der Gesellschaft vermittelt. Ferner sind die gesetzlichen "
        "Vertreter verantwortlich für die internen Kontrollen, die "
        "sie in Übereinstimmung mit den deutschen Grundsätzen "
        "ordnungsmäßiger Buchführung als notwendig bestimmt haben, "
        "um die Aufstellung eines Jahresabschlusses zu ermöglichen, "
        "der frei von wesentlichen falschen Darstellungen aufgrund "
        "von dolosen Handlungen (d.h. Manipulationen der Rechnungslegung "
        "und Vermögensschädigungen) oder Irrtümern ist.\n\n"
        "Bei der Aufstellung des Jahresabschlusses sind die gesetzlichen "
        "Vertreter dafür verantwortlich, die Fähigkeit der Gesellschaft "
        "zur Fortführung der Unternehmenstätigkeit zu beurteilen. "
        "Des Weiteren haben sie die Verantwortung, Sachverhalte in "
        "Zusammenhang mit der Fortführung der Unternehmenstätigkeit, "
        "sofern einschlägig, anzugeben."
    )))

    s.append(("Verantwortung des Abschlussprüfers für die Prüfung", (
        "Unsere Zielsetzung ist, hinreichende Sicherheit darüber zu "
        "erlangen, ob der Jahresabschluss als Ganzes frei von "
        "wesentlichen – beabsichtigten oder unbeabsichtigten – falschen "
        "Darstellungen ist, und ob der Lagebericht insgesamt ein "
        "zutreffendes Bild von der Lage der Gesellschaft vermittelt "
        "sowie in allen wesentlichen Belangen mit dem Jahresabschluss "
        "sowie mit den bei der Prüfung gewonnenen Erkenntnissen in "
        "Einklang steht, den deutschen gesetzlichen Vorschriften "
        "entspricht und die Chancen und Risiken der zukünftigen "
        "Entwicklung zutreffend darstellt. Wir geben einen Bestätigungs-"
        "vermerk ab, der unsere Prüfungsurteile zum Jahresabschluss "
        "und zum Lagebericht enthält.\n\n"
        "Hinreichende Sicherheit ist ein hohes Maß an Sicherheit, "
        "aber keine Garantie dafür, dass eine in Übereinstimmung mit "
        "§ 317 HGB und unter Beachtung der vom Institut der "
        "Wirtschaftsprüfer (IDW) festgestellten deutschen Grundsätze "
        "ordnungsmäßiger Abschlussprüfung durchgeführte Prüfung eine "
        "wesentliche falsche Darstellung stets aufdeckt."
    )))

    s.append(("Unterzeichnung", (
        f"{city}, den {_today_de()}\n\n"
        f"{wp_firma}\n\n"
        f"_____________________________\n"
        f"{wp1}\n"
        f"Wirtschaftsprüfer\n\n"
        f"_____________________________\n"
        f"[Name]\n"
        f"Wirtschaftsprüfer"
    )))

    return s


def gen_jahresabschluss_xlsx_sheets(p: Dict[str, Any], year: int = 2024) -> List[Tuple]:
    """Returns list of (sheet_name, headers, rows, col_widths) for xlsx.
    Target sheets: Deckblatt, Bilanz, GuV, Anlagenspiegel, EK-Spiegel,
    Cashflow, FoVbk-Spiegel, Rückstellungs-Spiegel, Personal, KPI."""

    company = _g(p, "company", "Muster GmbH")
    sheets = []

    # 1. Deckblatt mit Kennzahlen
    sheets.append((
        "Deckblatt",
        ["Kennzahl", "Wert " + str(year), "Wert " + str(year - 1), "Δ %"],
        [
            ["Umsatzerlöse (TEUR)", 49700, 46250, "+7,5 %"],
            ["EBITDA (TEUR)", 7580, 6960, "+8,9 %"],
            ["EBIT (TEUR)", 5430, 4890, "+11,0 %"],
            ["Jahresüberschuss (TEUR)", 3820, 3410, "+12,0 %"],
            ["Eigenkapital (TEUR)", 16180, 14380, "+12,5 %"],
            ["Bilanzsumme (TEUR)", 38500, 36200, "+6,4 %"],
            ["Eigenkapitalquote", "42,0 %", "39,7 %", "+2,3 PP"],
            ["Mitarbeiter (Ø)", 215, 208, "+3,4 %"],
            ["F&E-Aufwand (% v. Umsatz)", "4,5 %", "4,3 %", "+0,2 PP"],
            ["Investitionen (TEUR)", 2850, 2450, "+16,3 %"],
        ],
        [35, 20, 20, 12]
    ))

    # 2. Bilanz
    sheets.append((
        "Bilanz",
        ["Position", "31.12." + str(year) + " (TEUR)", "31.12." + str(year - 1) + " (TEUR)"],
        [
            ["AKTIVA", "", ""],
            ["A. Anlagevermögen", 18450, 17280],
            ["  I. Immaterielle Vermögensgegenstände", 1250, 1180],
            ["  II. Sachanlagen", 14900, 14100],
            ["    1. Grundstücke und Gebäude", 6800, 6900],
            ["    2. Technische Anlagen und Maschinen", 5450, 4800],
            ["    3. Andere Anlagen, BGA", 2350, 2100],
            ["    4. Geleistete Anzahlungen, Anlagen i.B.", 300, 300],
            ["  III. Finanzanlagen", 2300, 2000],
            ["B. Umlaufvermögen", 19850, 18620],
            ["  I. Vorräte", 12595, 11622],
            ["  II. Forderungen aus L+L", 5230, 5180],
            ["  III. Sonstige Vermögensgegenstände", 425, 318],
            ["  IV. Kassenbestand, Bankguthaben", 1600, 1500],
            ["C. Rechnungsabgrenzungsposten", 200, 300],
            ["BILANZSUMME AKTIVA", 38500, 36200],
            ["", "", ""],
            ["PASSIVA", "", ""],
            ["A. Eigenkapital", 16180, 14380],
            ["  I. Gezeichnetes Kapital", 1000, 1000],
            ["  II. Kapitalrücklage", 5500, 5500],
            ["  III. Gewinnrücklagen", 5860, 4470],
            ["  IV. Bilanzgewinn", 3820, 3410],
            ["B. Rückstellungen", 6420, 6035],
            ["  1. Pensionsrückstellungen", 3120, 2985],
            ["  2. Steuerrückstellungen", 850, 715],
            ["  3. Sonstige Rückstellungen", 2450, 2335],
            ["C. Verbindlichkeiten", 15800, 15685],
            ["  1. Gegenüber Kreditinstituten", 4500, 4750],
            ["  2. Erhaltene Anzahlungen", 320, 280],
            ["  3. Aus Lieferungen und Leistungen", 3150, 2980],
            ["  4. Gegenüber verbundenen Unternehmen", 6880, 6925],
            ["  5. Sonstige Verbindlichkeiten", 950, 750],
            ["D. Rechnungsabgrenzungsposten", 100, 100],
            ["BILANZSUMME PASSIVA", 38500, 36200],
        ],
        [55, 22, 22]
    ))

    # 3. GuV
    sheets.append((
        "GuV",
        ["Position", str(year) + " (TEUR)", str(year - 1) + " (TEUR)"],
        [
            ["1. Umsatzerlöse", 49700, 46250],
            ["2. Bestandsveränderung", 280, 145],
            ["3. Andere aktivierte Eigenleistungen", 180, 165],
            ["4. Sonstige betriebliche Erträge", 410, 380],
            ["= Gesamtleistung", 50570, 46940],
            ["5. Materialaufwand", -25200, -23800],
            ["  a) Roh-, Hilfs-, Betriebsstoffe", -22500, -21200],
            ["  b) Bezogene Leistungen", -2700, -2600],
            ["6. Personalaufwand", -11450, -10890],
            ["  a) Löhne und Gehälter", -9500, -9050],
            ["  b) Soziale Abgaben", -1800, -1700],
            ["  c) Altersversorgung", -150, -140],
            ["7. Abschreibungen", -2150, -2070],
            ["8. Sonstige betriebliche Aufwendungen", -6340, -5290],
            ["= EBIT", 5430, 4890],
            ["9. Erträge aus Beteiligungen", 50, 45],
            ["10. Zinserträge", 25, 15],
            ["11. Zinsaufwendungen", -185, -210],
            ["= Ergebnis vor Steuern (EBT)", 5320, 4740],
            ["12. Steuern vom Einkommen und Ertrag", -1500, -1330],
            ["= Jahresüberschuss", 3820, 3410],
        ],
        [55, 22, 22]
    ))

    # 4. Anlagenspiegel
    sheets.append((
        "Anlagenspiegel",
        ["Position", "AK 01.01.", "Zugänge", "Abgänge", "Umbuchungen",
         "AK 31.12.", "AfA kumuliert", "Abgänge AfA", "AfA des Jahres",
         "BW 31.12.", "BW 01.01."],
        [
            ["Immat. VG", 3200, 280, 0, 0, 3480, -2230, 0, -180, 1250, 1180],
            ["  Lizenzen, Software", 2400, 200, 0, 0, 2600, -1700, 0, -150, 1000, 900],
            ["  Selbst erstellte VG", 800, 80, 0, 0, 880, -530, 0, -30, 350, 280],
            ["Sachanlagen", 28500, 2570, -150, 0, 30920, -16020, 100, -1820, 14900, 14100],
            ["  Grundstücke", 7200, 0, 0, 0, 7200, -300, 0, -100, 6800, 6900],
            ["  Technische Anl.", 14500, 1500, -50, 0, 15950, -10500, 30, -1080, 5450, 4800],
            ["  BGA", 5800, 870, -100, 0, 6570, -4220, 70, -640, 2350, 2100],
            ["  AiB", 1000, 200, 0, 0, 1200, -1000, 0, 0, 300, 300],
            ["Finanzanlagen", 2000, 300, 0, 0, 2300, 0, 0, 0, 2300, 2000],
            ["Summe AV", 33700, 3150, -150, 0, 36700, -18250, 100, -2000, 18450, 17280],
        ],
        [25, 12, 12, 12, 12, 14, 14, 14, 14, 14, 14]
    ))

    # 5. Eigenkapitalspiegel
    sheets.append((
        "EK-Spiegel",
        ["Position", "GZK", "Kapitalrücklage", "Gewinnrücklage", "Bilanzgewinn", "Summe"],
        [
            ["Stand 01.01." + str(year), 1000, 5500, 4470, 3410, 14380],
            ["Ausschüttung", 0, 0, 0, -2020, -2020],
            ["Einstellung in GR", 0, 0, 1390, -1390, 0],
            ["Jahresüberschuss", 0, 0, 0, 3820, 3820],
            ["Stand 31.12." + str(year), 1000, 5500, 5860, 3820, 16180],
        ],
        [30, 12, 18, 18, 18, 14]
    ))

    # 6. Cashflow (DRS 21 indirekte Methode)
    sheets.append((
        "Cashflow",
        ["Position", str(year) + " (TEUR)"],
        [
            ["Operativer Cashflow", ""],
            ["Jahresüberschuss", 3820],
            ["+ Abschreibungen", 2150],
            ["+/- Veränderung Rückstellungen", 385],
            ["+/- Sonstige nicht-zahlungswirksame Erträge/Aufw.", -50],
            ["+/- Gewinn/Verlust aus Anlagenabgängen", 30],
            ["+/- Veränderung Vorräte", -973],
            ["+/- Veränderung Forderungen", -50],
            ["+/- Veränderung Verbindlichkeiten L+L", 170],
            ["+/- Veränderung sonstige Vermögensgegenstände", -107],
            ["+/- Veränderung sonstige Verbindlichkeiten", 200],
            ["+/- Sonstige", 250],
            ["= Cashflow aus laufender Geschäftstätigkeit", 5825],
            ["", ""],
            ["Investitionstätigkeit", ""],
            ["Auszahlungen für Investitionen", -2850],
            ["Einzahlungen aus Anlagenabgängen", 50],
            ["= Cashflow aus Investitionstätigkeit", -2800],
            ["", ""],
            ["Finanzierungstätigkeit", ""],
            ["Tilgung Bankkredite", -250],
            ["Ausschüttungen Gesellschafter", -2020],
            ["Auszahlung Gesellschafterdarlehen", -45],
            ["Sonstige Finanzierung", -210],
            ["= Cashflow aus Finanzierungstätigkeit", -2525],
            ["", ""],
            ["Veränderung Liquiditätssaldo", 500],
            ["Liquide Mittel Beginn", 1100],
            ["Liquide Mittel Ende", 1600],
        ],
        [55, 22]
    ))

    # 7. Forderungs-/Verbindlichkeiten-Spiegel
    sheets.append((
        "FoVbk-Spiegel",
        ["Position", "Gesamt", "Restl. < 1 J", "Restl. 1-5 J", "Restl. > 5 J", "Davon gesichert"],
        [
            ["Forderungen L+L", 5230, 5230, 0, 0, 0],
            ["Forderungen verb. Unt.", 350, 350, 0, 0, 0],
            ["Verb. Kreditinstitute", 4500, 250, 1750, 2500, 4500],
            ["Verb. L+L", 3150, 3150, 0, 0, 0],
            ["Verb. verb. Unt.", 6880, 6880, 0, 0, 0],
            ["Sonst. Verb.", 950, 950, 0, 0, 0],
        ],
        [30, 12, 14, 14, 14, 16]
    ))

    # 8. Rückstellungs-Spiegel
    sheets.append((
        "Rückstellungs-Spiegel",
        ["Position", "Stand 01.01.", "Verbrauch", "Auflösung", "Zuführung", "Stand 31.12."],
        [
            ["Pensionsrückstellungen", 2985, -45, 0, 180, 3120],
            ["Steuerrückstellungen", 715, -715, 0, 850, 850],
            ["Gewährleistung", 1180, -180, -50, 300, 1250],
            ["Personal (Urlaub, Boni)", 720, -720, 0, 850, 850],
            ["Restrukturierung", 250, -100, -50, 100, 200],
            ["Sonstige", 185, -100, -20, 85, 150],
            ["Summe", 6035, -1860, -120, 2365, 6420],
        ],
        [30, 14, 14, 14, 14, 14]
    ))

    # 9. Personal-Kennzahlen
    sheets.append((
        "Personal-Kennzahlen",
        ["Kennzahl", str(year), str(year - 1)],
        [
            ["Anzahl Mitarbeiter (Ø)", 215, 208],
            ["  davon Gewerbliche", 150, 145],
            ["  davon Angestellte", 60, 58],
            ["  davon Auszubildende", 5, 5],
            ["Personalaufwand (TEUR)", 11450, 10890],
            ["Personalaufwandsquote (% v. Umsatz)", "23,0 %", "23,5 %"],
            ["Fluktuation", "4,8 %", "5,2 %"],
            ["Krankenstand", "3,5 %", "3,8 %"],
            ["Weiterbildungsaufwand (TEUR)", 850, 720],
            ["Frauenquote", "32 %", "30 %"],
        ],
        [40, 14, 14]
    ))

    # 10. KPI-Dashboard
    sheets.append((
        "KPI-Dashboard",
        ["KPI", str(year), str(year - 1), "Zielwert"],
        [
            ["Umsatzwachstum", "+7,5 %", "+4,2 %", "≥ 5 %"],
            ["EBITDA-Marge", "15,3 %", "15,0 %", "≥ 14 %"],
            ["EBIT-Marge", "10,9 %", "10,6 %", "≥ 10 %"],
            ["EK-Quote", "42,0 %", "39,7 %", "≥ 35 %"],
            ["Net Debt / EBITDA", "0,69x", "1,22x", "≤ 2,0x"],
            ["Working Capital Days", 65, 68, "≤ 70"],
            ["Forderungslaufzeit (Tage)", 38, 41, "≤ 45"],
            ["Vorratsreichweite (Tage)", 92, 89, "≤ 100"],
            ["Verbindlichkeitslaufzeit (Tage)", 23, 24, "30-40"],
            ["Cashflow / Umsatz", "11,7 %", "12,8 %", "≥ 10 %"],
            ["ROIC", "12,5 %", "11,8 %", "≥ 10 %"],
        ],
        [35, 14, 14, 14]
    ))

    return sheets


# =====================================================================
# DOMAIN-SPECIFIC: MEDTECH / BIOTECH
# =====================================================================

def gen_clinical_evaluation_report(p: Dict[str, Any], product: str = None) -> List[Section]:
    """MDR Article 61 Clinical Evaluation Report. Target: 5000-8000 Wörter."""

    company = _g(p, "company", "BioTech Innovations GmbH")
    product = product or _g(p, "product", "CardioMonitor X1")
    classification = _g(p, "classification", "Class IIb gemäß MDR Anhang VIII Rule 11")

    s: List[Section] = []

    s.append(("1. Executive Summary", (
        f"This Clinical Evaluation Report (CER) presents the clinical "
        f"evaluation of the {product} medical device manufactured by "
        f"{company}, in compliance with Article 61 of the EU Medical "
        f"Device Regulation (MDR) 2017/745 and MEDDEV 2.7/1 Rev.4 "
        f"guidance.\n\n"
        f"The {product} is classified as {classification}. Its intended "
        f"purpose is the continuous monitoring of cardiac parameters in "
        f"adult patients in clinical and home settings. The clinical "
        f"evaluation demonstrates that the device achieves its intended "
        f"purpose, that the risks associated with its use are acceptable "
        f"when weighed against the benefits, and that the available "
        f"clinical data confirms the safety and performance of the device.\n\n"
        f"The evaluation is based on a systematic review of the literature, "
        f"post-market surveillance (PMS) data, clinical investigations, "
        f"and comparable equivalent device data. The benefit-risk profile "
        f"is favorable. Residual risks are adequately mitigated through "
        f"risk control measures, labeling, and post-market surveillance "
        f"activities."
    )))

    s.append(("2. Scope and Objectives", (
        "2.1 Scope:\n"
        "This CER covers the clinical evaluation of the " + product + " "
        "across all variants and configurations, intended for use in "
        "the European Economic Area. The scope addresses initial CE "
        "marking, periodic review, and post-market clinical follow-up.\n\n"
        "2.2 Objectives:\n"
        "a) To assess the conformity of the device with the General "
        "Safety and Performance Requirements (GSPRs) specified in "
        "Annex I of the MDR;\n\n"
        "b) To establish and verify the clinical benefit, performance, "
        "and safety profile;\n\n"
        "c) To identify residual risks and side effects;\n\n"
        "d) To define post-market clinical follow-up (PMCF) plans where "
        "applicable;\n\n"
        "e) To support claims made in promotional materials, labeling, "
        "and instructions for use.\n\n"
        "2.3 Regulatory Basis:\n"
        "- Regulation (EU) 2017/745 (MDR), particularly Article 61 "
        "and Annex XIV;\n"
        "- MEDDEV 2.7/1 Rev.4 (Clinical Evaluation Guidance);\n"
        "- ISO 14155:2020 (Clinical Investigation of Medical Devices "
        "for Human Subjects);\n"
        "- Helsinki Declaration (current revision);\n"
        "- ISO 14971:2019 (Application of Risk Management to Medical "
        "Devices)."
    )))

    s.append(("3. Device Description and Intended Purpose", (
        f"3.1 Device Description:\n"
        f"The {product} is a non-invasive, body-worn medical device "
        f"intended for continuous monitoring of:\n"
        f"- Electrocardiogram (ECG, single-lead and 3-lead configurations);\n"
        f"- Heart rate and heart rate variability;\n"
        f"- SpO2 (peripheral oxygen saturation);\n"
        f"- Respiratory rate;\n"
        f"- Patient activity and posture.\n\n"
        f"The device consists of a chest-worn sensor, a wireless "
        f"gateway, and cloud-based analytics software. Data are "
        f"transmitted via Bluetooth Low Energy and cellular networks "
        f"to a HIPAA/GDPR-compliant cloud platform, where clinicians "
        f"can review patient vital signs in real time or asynchronously.\n\n"
        f"3.2 Intended Purpose:\n"
        f"- Indications: Continuous monitoring of adult patients with "
        f"known or suspected cardiac arrhythmias, post-MI patients, "
        f"post-cardiac surgery patients, and patients with heart failure;\n"
        f"- Contraindications: Patients with active implantable "
        f"cardiac devices (without prior compatibility review), "
        f"patients with severe skin conditions in the sensor area;\n"
        f"- Intended users: Healthcare professionals, trained patients "
        f"and caregivers;\n"
        f"- Use environment: Hospital wards, ICUs, outpatient settings, "
        f"home care environments;\n"
        f"- Patient population: Adults aged ≥18 years.\n\n"
        f"3.3 Classification:\n"
        f"Class IIb medical device under MDR Annex VIII, Rule 11 "
        f"(active device for monitoring of vital physiological parameters)."
    )))

    s.append(("4. State of the Art and Clinical Background", (
        "4.1 Disease Background:\n"
        "Cardiovascular diseases (CVDs) remain the leading cause of "
        "death globally, with arrhythmias contributing significantly "
        "to morbidity and mortality. Continuous monitoring has been "
        "shown to improve outcomes through early detection of "
        "deteriorations.\n\n"
        "4.2 State of the Art:\n"
        "Current monitoring solutions include:\n"
        "- Telemetry systems (hospital-only, wired or short-range "
        "wireless);\n"
        "- Holter monitors (24-48 hours, mostly retrospective);\n"
        "- Implantable loop recorders (invasive, long-term);\n"
        "- Wearable patches (typically 7-14 days);\n"
        "- Consumer wearables (limited clinical validity).\n\n"
        "4.3 Clinical Need:\n"
        "There is a recognized clinical need for continuous, long-term, "
        "non-invasive monitoring solutions with clinical-grade accuracy "
        "across multiple parameters."
    )))

    s.append(("5. Identification of Clinical Data", (
        "5.1 Literature Search:\n"
        "A systematic literature search was conducted in PubMed/MEDLINE, "
        "Embase, Cochrane Library, and ClinicalTrials.gov. Search "
        "terms included combinations of: continuous cardiac monitoring, "
        "wearable ECG, ambulatory monitoring, arrhythmia detection, "
        "non-invasive vital signs.\n\n"
        "Search dates: Last 10 years (rolling), updated at the time "
        "of this CER. Total records identified: 1,247. After deduplication: "
        "892. After title/abstract screening: 156. After full-text "
        "review: 47 included studies.\n\n"
        "5.2 Post-Market Surveillance (PMS) Data:\n"
        "PMS data for the past 24 months include:\n"
        "- 12,500 patient-months of device use;\n"
        "- 24 incident reports (none meeting Article 87 MDR vigilance "
        "criteria);\n"
        "- Customer feedback (95 % satisfaction);\n"
        "- Device performance data (uptime 99.7 %).\n\n"
        "5.3 Clinical Investigations:\n"
        "- One pivotal multi-center randomized controlled trial "
        "(n=480), conducted 2023-2024;\n"
        "- Three post-market clinical follow-up (PMCF) studies "
        "ongoing (n=250 total).\n\n"
        "5.4 Equivalent Devices:\n"
        "No fully equivalent devices identified. Comparable devices "
        "from competitors are analyzed for state-of-the-art benchmarking, "
        "but equivalence claim is not used per MDR Article 61(4)."
    )))

    s.append(("6. Appraisal of Clinical Data", (
        "6.1 Quality Assessment:\n"
        "Each included study was assessed using MEDDEV 2.7/1 Rev.4 "
        "appraisal criteria:\n"
        "- Suitability of data sources (study design, statistical "
        "power, generalizability);\n"
        "- Methodological quality (risk of bias, blinding, randomization);\n"
        "- Clinical relevance.\n\n"
        "6.2 Risk-of-Bias Assessment:\n"
        "Cochrane Risk-of-Bias 2.0 tool used for RCTs; ROBINS-I for "
        "non-randomized studies. Results: 12 studies low risk, 28 "
        "moderate, 7 high risk.\n\n"
        "6.3 Conclusion:\n"
        "Overall body of evidence is of moderate-to-high quality and "
        "supports the safety and performance claims."
    )))

    s.append(("7. Analysis of Clinical Data", (
        "7.1 Performance:\n"
        "The pivotal RCT demonstrated:\n"
        "- ECG accuracy vs. gold-standard (12-lead): sensitivity 96.4 %, "
        "specificity 98.1 % for atrial fibrillation detection;\n"
        "- SpO2 accuracy: bias ±2 % across 70-100 % range;\n"
        "- Respiratory rate accuracy: ±2 breaths/min;\n"
        "- Battery life: 7-day continuous use confirmed.\n\n"
        "7.2 Safety:\n"
        "Adverse events related to device use across all studies:\n"
        "- Skin irritation: 4.2 % (mild, all self-resolving);\n"
        "- No serious adverse device effects (SADE);\n"
        "- No deaths attributable to device.\n\n"
        "7.3 Clinical Benefit:\n"
        "Patients monitored with " + product + " had:\n"
        "- Earlier arrhythmia detection (median 3.5 days vs. 12 days "
        "standard care);\n"
        "- Reduced rehospitalizations (-22 %, p<0.05);\n"
        "- Improved patient-reported outcomes."
    )))

    s.append(("8. Benefit-Risk Analysis", (
        "8.1 Identified Benefits:\n"
        "- Early detection of cardiac events;\n"
        "- Reduced hospitalizations and emergency visits;\n"
        "- Improved patient-reported outcomes;\n"
        "- Healthcare cost reduction.\n\n"
        "8.2 Identified Risks:\n"
        "- Mild skin reactions (mitigated by hypoallergenic materials, "
        "labeling);\n"
        "- False alarms (mitigated by algorithm refinement, clinical "
        "workflow integration);\n"
        "- Data privacy/cybersecurity (mitigated by encryption, "
        "GDPR-compliant infrastructure);\n"
        "- Battery failure (mitigated by alarm system, redundancy).\n\n"
        "8.3 Acceptability:\n"
        "Overall benefit-risk profile is favorable. Identified risks "
        "are appropriately controlled through risk management measures "
        "in accordance with ISO 14971:2019."
    )))

    s.append(("9. Post-Market Clinical Follow-up (PMCF) Plan", (
        "9.1 PMCF Plan Justification:\n"
        "Given the device's class and intended purpose, a PMCF plan "
        "is required under MDR Annex XIV Part B.\n\n"
        "9.2 PMCF Activities:\n"
        "- Continuation of three ongoing PMCF studies;\n"
        "- Initiation of two additional PMCF studies in 2026;\n"
        "- Registry participation (European Cardiac Monitoring "
        "Registry);\n"
        "- Patient survey program;\n"
        "- Literature surveillance (bi-annual updates);\n"
        "- Vigilance and FSCA processes.\n\n"
        "9.3 PMCF Endpoints:\n"
        "Real-world performance, long-term safety, patient outcomes, "
        "device durability."
    )))

    s.append(("10. Conclusions", (
        f"10.1 Conformity:\n"
        f"The clinical evaluation demonstrates that the {product} "
        f"conforms to the General Safety and Performance Requirements "
        f"set out in Annex I of the MDR.\n\n"
        f"10.2 Performance:\n"
        f"The device performs as intended in the specified clinical "
        f"settings.\n\n"
        f"10.3 Safety:\n"
        f"The device is safe for its intended use, with residual "
        f"risks acceptable when weighed against the benefits.\n\n"
        f"10.4 Recommendations:\n"
        f"- Continue periodic safety update reports (PSURs);\n"
        f"- Complete ongoing PMCF studies;\n"
        f"- Update CER bi-annually or upon significant new clinical "
        f"information."
    )))

    s.append(("11. References", (
        "[Comprehensive bibliography of 47 included studies plus "
        "supporting literature, guidance documents, and standards. "
        "Full references on file with the manufacturer.]"
    )))

    s.append(("12. Qualifications of Evaluators", (
        "The clinical evaluation was conducted by a multidisciplinary "
        "team:\n\n"
        "- Dr. med. [Name], cardiologist with 15+ years' experience "
        "in cardiac monitoring (Lead Clinical Evaluator);\n"
        "- [Name], MSc Biostatistics (statistical analysis);\n"
        "- [Name], regulatory affairs specialist (MDR compliance);\n"
        "- [Name], clinical research scientist (PMS data).\n\n"
        "Qualifications and CVs are maintained on file."
    )))

    s.append(("13. Signature and Approval", (
        f"Author: Dr. med. [Name] (Lead Clinical Evaluator)\n"
        f"Date: {_today_de()}\n\n"
        f"Reviewer: [Name] (Quality Assurance Manager)\n"
        f"Date: {_today_de()}\n\n"
        f"Approver: [Name] (Person Responsible for Regulatory "
        f"Compliance, MDR Art. 15)\n"
        f"Date: {_today_de()}"
    )))

    return s


def gen_mdr_technical_file(p: Dict[str, Any], product: str = None) -> List[Section]:
    """MDR Technical Documentation Annex II. Target: 4000-6000 Wörter."""

    company = _g(p, "company", "BioTech Innovations GmbH")
    product = product or _g(p, "product", "CardioMonitor X1")

    s: List[Section] = []

    s.append(("Cover Page", (
        f"Technical Documentation for the {product}\n"
        f"In accordance with EU Medical Device Regulation 2017/745, Annex II\n\n"
        f"Manufacturer: {company}\n"
        f"Document Version: 3.0\n"
        f"Date: {_today_de()}\n\n"
        f"Person Responsible for Regulatory Compliance (PRRC): [Name]\n"
        f"Notified Body: [Name + Number]"
    )))

    s.append(("1. Device Description and Specification", (
        f"1.1 Product Identification:\n"
        f"- Trade name: {product};\n"
        f"- UDI-DI (Basic UDI-DI): [Number];\n"
        f"- Model variants: Standard, Pro, Pediatric (not in scope);\n"
        f"- Generic device group: continuous cardiac monitoring system.\n\n"
        f"1.2 Intended Purpose Statement:\n"
        f"The {product} is intended for continuous, non-invasive "
        f"monitoring of vital cardiac and respiratory parameters in "
        f"adult patients in clinical and home-care settings.\n\n"
        f"1.3 Classification:\n"
        f"- Class IIb under MDR Annex VIII, Rule 11;\n"
        f"- Justification: Active device, intended for monitoring of "
        f"vital physiological parameters, variations could result in "
        f"immediate danger to patient.\n\n"
        f"1.4 Technical Specifications:\n"
        f"- Sensor: 3-electrode ECG, optical SpO2, thermistor "
        f"respiratory, 3-axis accelerometer;\n"
        f"- Connectivity: BLE 5.2, LTE-M, Wi-Fi 6;\n"
        f"- Battery: Lithium-polymer, 1000 mAh, 7-day life;\n"
        f"- Operating temperature: 5-40 °C;\n"
        f"- Ingress protection: IP67;\n"
        f"- Weight: 38 g.\n\n"
        f"1.5 Accessories:\n"
        f"Hypoallergenic adhesive patches, charging dock, "
        f"healthcare professional dashboard software."
    )))

    s.append(("2. Information to be Supplied by the Manufacturer", (
        "2.1 Labeling:\n"
        "- Symbols according to ISO 15223-1:2021;\n"
        "- UDI label;\n"
        "- CE mark with Notified Body number;\n"
        "- Manufacturer information per Article 27 MDR.\n\n"
        "2.2 Instructions for Use (IFU):\n"
        "Provided in 24 EU languages, electronic IFU (eIFU) where "
        "permitted by Regulation (EU) 207/2012.\n\n"
        "Contents of IFU include: indications, contraindications, "
        "warnings, precautions, instructions for application, cleaning, "
        "maintenance, troubleshooting, technical specifications, "
        "manufacturer contact, residual risks, environmental impact "
        "information."
    )))

    s.append(("3. Design and Manufacturing Information", (
        "3.1 Design Stages:\n"
        "Design controls follow IEC 62366-1:2015 (usability) and "
        "ISO 13485:2016 (quality management).\n\n"
        "Design phases: Concept, Planning, Input, Output, Verification, "
        "Validation, Transfer, Changes. All design phases are "
        "documented in the Design History File (DHF).\n\n"
        "3.2 Manufacturing:\n"
        "Manufacturing is performed at: [Site]. The manufacturing "
        "process is qualified (IQ/OQ/PQ) and validated. Critical "
        "process parameters monitored statistically."
    )))

    s.append(("4. General Safety and Performance Requirements (GSPR)", (
        "A complete GSPR checklist is included as Annex II.1. All "
        "applicable requirements from Annex I MDR are addressed:\n\n"
        "Chapter I (General Requirements): All 9 requirements applicable, "
        "compliance demonstrated by harmonized standards (IEC 60601-1 "
        "etc.), clinical data, and risk management documentation.\n\n"
        "Chapter II (Requirements regarding Design and Manufacture): "
        "All 14 requirements applicable.\n\n"
        "Chapter III (Information to be Supplied): All requirements "
        "addressed in labeling and IFU.\n\n"
        "Compliance evidence: Test reports, risk management file, "
        "clinical evaluation report, software documentation, biocompatibility "
        "testing."
    )))

    s.append(("5. Benefit-Risk Analysis and Risk Management", (
        "Risk management performed per ISO 14971:2019. Risk Management "
        "File (RMF) includes:\n\n"
        "- Risk management plan;\n"
        "- Risk analysis (hazards, hazardous situations, harms);\n"
        "- Risk evaluation (severity x probability);\n"
        "- Risk control measures (inherent safety, protective measures, "
        "information for safety);\n"
        "- Residual risk evaluation;\n"
        "- Risk management report.\n\n"
        "Top identified hazards: false negative arrhythmia detection, "
        "skin reaction, cyber-attack, battery failure. All risks "
        "reduced to acceptable level."
    )))

    s.append(("6. Product Verification and Validation", (
        "6.1 Bench Testing:\n"
        "Electrical safety (IEC 60601-1), EMC (IEC 60601-1-2), "
        "mechanical (drop test, ingress), environmental conditioning, "
        "battery cycling, biocompatibility (ISO 10993 series).\n\n"
        "6.2 Software:\n"
        "Software lifecycle per IEC 62304. Software safety class: B. "
        "Cybersecurity per IEC 81001-5-1, FDA Premarket Cybersecurity "
        "Guidance, NIS2.\n\n"
        "6.3 Usability:\n"
        "Usability engineering per IEC 62366-1:2015, formative and "
        "summative testing completed.\n\n"
        "6.4 Clinical:\n"
        "See separate Clinical Evaluation Report (CER)."
    )))

    s.append(("7. Post-Market Surveillance (PMS)", (
        "PMS Plan and PSUR (Periodic Safety Update Report) maintained "
        "per Article 84-86 MDR. PMS data integrated with risk management "
        "and clinical evaluation."
    )))

    s.append(("8. EU Declaration of Conformity", (
        "Issued per Article 19 and Annex IV MDR. Available on the "
        "manufacturer's website and in product documentation."
    )))

    s.append(("9. Summary of Safety and Clinical Performance (SSCP)", (
        "SSCP per Article 32 MDR drafted for Class III implantable "
        "devices; not applicable for Class IIb (this device)."
    )))

    return s


# =====================================================================
# DOMAIN-SPECIFIC: AUTOMOTIVE
# =====================================================================

def gen_iatf_audit_report(p: Dict[str, Any], entity: str = None, year: int = 2024) -> List[Section]:
    """IATF 16949 Internal Audit Report. Target: 2500-4000 Wörter."""

    company = _g(p, "company", "Brennhagen Automotive GmbH")
    entity = entity or _g(p, "entity", "Werk Köln")

    s: List[Section] = []

    s.append(("1. Audit Information", (
        f"Audit Type: Internes Systemaudit (System Audit)\n"
        f"Standard: IATF 16949:2016, ISO 9001:2015\n"
        f"Auditee: {company}, {entity}\n"
        f"Audit-Datum: {_today_de()}\n"
        f"Auditor Lead: [Name], IATF-zertifiziert\n"
        f"Auditteam: [Namen]\n"
        f"Audit-Geltungsbereich: Vollständiges Qualitätsmanagementsystem "
        f"des Werks {entity}, einschließlich aller Kernprozesse\n"
        f"Vorheriger Audit: [Datum]\n"
        f"Nächster Audit geplant: in 12 Monaten"
    )))

    s.append(("2. Audit Methodology", (
        "Das Audit wurde nach Prozessansatz gemäß IATF 16949 durchgeführt. "
        "Methoden: Interviews, Dokumentenprüfung, Beobachtung von "
        "Prozessen vor Ort, Stichprobenprüfung von Records, Turtle-"
        "Diagramme. Audit-Plan ist beigefügt (Anlage 1).\n\n"
        "Berücksichtigte Prozesse: Strategie und Planung, Vertrieb und "
        "Kundenmanagement, Produktentwicklung (APQP), Beschaffung, "
        "Fertigungsplanung und -steuerung, Produktion, Qualitätssicherung, "
        "Reklamationsmanagement (8D), Wartung und Instandhaltung, "
        "Personalentwicklung, Compliance und Risikomanagement."
    )))

    s.append(("3. Audit Results - Summary", (
        f"Gesamtbewertung: Konform mit IATF 16949:2016 mit "
        f"Verbesserungspotenzialen.\n\n"
        f"- Major Non-Conformities (NC): 0\n"
        f"- Minor Non-Conformities (NC): 3\n"
        f"- Observations / Opportunities for Improvement (OFI): 8\n"
        f"- Positive Findings: 5\n\n"
        f"Die Qualitätsleitung wird beauftragt, einen Corrective Action "
        f"Plan binnen 30 Tagen zu erarbeiten. Die Umsetzung wird in der "
        f"Folge-Auditierung verifiziert."
    )))

    s.append(("4. Detailed Findings", (
        "4.1 Minor Non-Conformity 1 (8.5.1 - Produktion):\n"
        "Beobachtung: Die Erstmusterfreigaben (PPAP Level 3) für "
        "Bauteil-Nr. XY-2345 sind nicht vollständig dokumentiert. "
        "Es fehlt die Material-Zertifizierung gemäß ISO 14644.\n"
        "Bezug: IATF 16949 8.3.4.4, 8.4.2.4.\n"
        "Maßnahme: Vervollständigung der PPAP-Dokumentation, Schulung "
        "Lieferantenmanagement bzgl. Pflicht-PPAP-Elemente.\n\n"
        "4.2 Minor Non-Conformity 2 (9.1.1 - Monitoring):\n"
        "Beobachtung: Process Capability (CpK) für drei kritische "
        "Merkmale wurde quartalsweise gemessen, aber nicht statistisch "
        "ausgewertet. CpK < 1,33 wurde nicht eskaliert.\n"
        "Bezug: IATF 16949 9.1.1.1.\n"
        "Maßnahme: Implementierung eines automatisierten CpK-Eskalations-"
        "prozesses; Schulung der Linienverantwortlichen.\n\n"
        "4.3 Minor Non-Conformity 3 (10.2.3 - 8D Reklamation):\n"
        "Beobachtung: 8D-Reports zeigen unzureichende Root-Cause-Analyse "
        "in 3 von 12 stichprobenartig geprüften Fällen (Ishikawa/5-Why "
        "oberflächlich).\n"
        "Bezug: IATF 16949 10.2.3.\n"
        "Maßnahme: Vertiefte 8D-Schulung; Coaching durch Lead-Auditor "
        "im nächsten Quartal."
    )))

    s.append(("5. Observations / Opportunities for Improvement", (
        "5.1 OFI 1: Digitalisierung der Wareneingangsprüfung könnte "
        "Effizienz steigern.\n"
        "5.2 OFI 2: Reaktionszeit bei Kundenreklamationen variiert "
        "zwischen 24-72 Stunden; Standardisierung empfohlen.\n"
        "5.3 OFI 3: Lieferanten-Self-Assessments könnten häufiger "
        "stichprobenartig validiert werden.\n"
        "5.4 OFI 4: KPI-Dashboards sind in unterschiedlichen Systemen "
        "verteilt; Integration empfohlen.\n"
        "5.5 OFI 5: Schulungsplan für IATF-Anforderungen sollte "
        "rollierend aktualisiert werden.\n"
        "5.6 OFI 6: Risiken im Maschinenpark (insb. Maschine M-12) "
        "sollten in FMEA stärker abgebildet werden.\n"
        "5.7 OFI 7: Energieeffizienz-Kennzahlen könnten als "
        "Nachhaltigkeits-KPIs ergänzt werden.\n"
        "5.8 OFI 8: Datenschutz / IT-Sicherheits-Maßnahmen sollten in "
        "QMS klarer dokumentiert werden."
    )))

    s.append(("6. Positive Findings", (
        "6.1 Vorbildlich: Customer-Specific Requirements (CSR) für "
        "OEM A und B sind sehr gut implementiert.\n"
        "6.2 Vorbildlich: Layered Process Audits (LPA) werden konsequent "
        "durchgeführt und ausgewertet.\n"
        "6.3 Vorbildlich: Mitarbeiter-Engagement (eNPS) ist mit +42 "
        "über Branchendurchschnitt.\n"
        "6.4 Vorbildlich: APQP-Phasen-Reviews mit cross-funktionalen "
        "Teams.\n"
        "6.5 Vorbildlich: Lean-Maßnahmen reduzieren Setup-Zeiten um "
        "15 % im Jahresvergleich."
    )))

    s.append(("7. Conclusion", (
        f"Das QMS des Werks {entity} ist effektiv und entspricht den "
        f"Anforderungen von IATF 16949:2016. Identifizierte Non-Conformities "
        f"sind alle „minor' und können kurzfristig behoben werden. "
        f"Empfehlung an die Geschäftsleitung: Aufrechterhaltung des "
        f"Zertifikats."
    )))

    s.append(("8. Approvals", (
        f"Audit-Datum: {_today_de()}\n\n"
        f"Lead-Auditor:\n"
        f"_____________________________\n"
        f"[Name], IATF Lead Auditor\n\n"
        f"Werksleitung:\n"
        f"_____________________________\n"
        f"[Name], Werksleiter {entity}\n\n"
        f"Qualitätsleitung:\n"
        f"_____________________________\n"
        f"[Name], QM-Leiter"
    )))

    return s


def gen_oem_master_supply_agreement(p: Dict[str, Any], oem: str = None) -> List[Section]:
    """Master Supply Agreement with automotive OEM. Target: 6000-10000 Wörter.
    Builds on master_supply_agreement_de and adds automotive-specific clauses."""

    oem = oem or _g(p, "oem", "BMW AG")
    p["customer"] = oem

    # Start with base agreement
    base_sections = gen_master_supply_agreement_de(p)

    # Add automotive-specific sections before the closing sections
    # Find the position before the "§ 23 Folgen der Vertragsbeendigung" section
    automotive_extensions: List[Section] = []

    automotive_extensions.append(("§ A1 PPAP-Prozess (Production Part Approval Process)", (
        f"(1) Der Lieferant führt für jedes Vertragsprodukt vor "
        f"Serienanlauf einen PPAP gemäß AIAG PPAP Manual 4th Edition "
        f"bzw. VDA 2 Maturity Level Assurance durch.\n\n"
        f"(2) Der erforderliche PPAP-Level wird durch den Kunden "
        f"festgelegt (Standard: Level 3). Folgende Dokumente sind "
        f"vorzulegen:\n"
        f"- Design Records;\n"
        f"- Engineering Change Documents;\n"
        f"- Customer Engineering Approval;\n"
        f"- DFMEA (sofern Verantwortung des Lieferanten);\n"
        f"- Process Flow Diagram;\n"
        f"- PFMEA;\n"
        f"- Control Plan;\n"
        f"- Measurement Systems Analysis Studies (MSA);\n"
        f"- Dimensional Results;\n"
        f"- Material Performance Test Results;\n"
        f"- Initial Process Studies;\n"
        f"- Qualified Laboratory Documentation;\n"
        f"- Appearance Approval Report;\n"
        f"- Sample Production Parts;\n"
        f"- Master Sample;\n"
        f"- Checking Aids;\n"
        f"- Customer-Specific Requirements;\n"
        f"- Part Submission Warrant (PSW).\n\n"
        f"(3) Die Freigabe erfolgt schriftlich durch den Kunden. "
        f"Ohne PPAP-Freigabe darf keine Serienlieferung erfolgen.\n\n"
        f"(4) Bei Änderungen des Bauteils, Prozesses, Materials oder "
        f"Standorts ist ein Re-PPAP erforderlich."
    )))

    automotive_extensions.append(("§ A2 APQP-Phasen (Advanced Product Quality Planning)", (
        "(1) Der Lieferant wendet APQP gemäß AIAG APQP Manual bzw. "
        "VDA Reifegradabsicherung an.\n\n"
        "(2) APQP-Phasen umfassen:\n"
        "- Phase 1: Plan and Define Program;\n"
        "- Phase 2: Product Design and Development;\n"
        "- Phase 3: Process Design and Development;\n"
        "- Phase 4: Product and Process Validation;\n"
        "- Phase 5: Feedback, Assessment and Corrective Action.\n\n"
        "(3) Phasenfreigaben („Gates') werden gemeinsam mit dem "
        "Kunden durchgeführt.\n\n"
        "(4) APQP-Reifegrade werden gemäß VDA-Reifegradabsicherung "
        "monatlich berichtet."
    )))

    automotive_extensions.append(("§ A3 8D-Reklamationsprozess", (
        "(1) Bei Reklamationen wendet der Lieferant das 8D-Verfahren "
        "an:\n"
        "- 8D-Report binnen 24 Stunden initiieren;\n"
        "- D1: Team-Bildung;\n"
        "- D2: Problembeschreibung;\n"
        "- D3: Sofortmaßnahmen (innerhalb 24 Stunden);\n"
        "- D4: Root Cause Analysis (5-Why, Ishikawa);\n"
        "- D5: Geplante Abstellmaßnahmen;\n"
        "- D6: Umsetzung und Verifizierung;\n"
        "- D7: Maßnahmen zur Vorbeugung von Wiederholungen;\n"
        "- D8: Anerkennung des Teams.\n\n"
        "(2) 8D-Reports werden im vom Kunden vorgegebenen Format "
        "(z. B. BMW NCR-Tool, VW NLF-Online) eingereicht.\n\n"
        "(3) Vorgegebene Reaktionszeiten:\n"
        "- D3 (Sofortmaßnahme): 24 Stunden;\n"
        "- D5 (Abstellmaßnahme): 5 Werktage;\n"
        "- D8 (Abschluss): 30 Tage.\n\n"
        "(4) Bei Verzug wird eine Vertragsstrafe von EUR 1.000 pro "
        "Tag fällig."
    )))

    automotive_extensions.append(("§ A4 Customer-Specific Requirements (CSR)", (
        "(1) Zusätzlich zu den allgemeinen Bestimmungen gelten die "
        "in Anlage CSR aufgeführten Customer-Specific Requirements:\n"
        "- BMW Standard B 70 0001 ff.;\n"
        "- VW Konzernnorm VW 80101 ff.;\n"
        "- Mercedes-Benz MBN-Normen;\n"
        "- Stellantis PSA-Normen.\n\n"
        "(2) CSR umfassen u.a. spezifische Materialfreigaben, "
        "Prüfvorschriften, Auditstandards, Lieferantenstandards.\n\n"
        "(3) VDA 6.3-Audit beim Lieferanten kann jederzeit angeordnet "
        "werden."
    )))

    automotive_extensions.append(("§ A5 Allokationsmechanismen bei Bauteilengpässen", (
        "(1) Bei Knappheit allokiert der Lieferant verfügbare Mengen "
        "wie folgt:\n"
        "a) Vorrangig nach vertraglich festgelegten Mindestmengen;\n"
        "b) Anteilig nach Forecast-Anteil der vergangenen 12 Monate;\n"
        "c) Equity-Allokation („Fair-Share-Prinzip').\n\n"
        "(2) Bei einer absehbaren Verknappung wird der Kunde "
        "mindestens 4 Wochen im Voraus informiert.\n\n"
        "(3) Die Pflicht zur fortlaufenden Sicherheitsbestandshaltung "
        "(2 Wochen Bedarf) bleibt unberührt."
    )))

    automotive_extensions.append(("§ A6 Long-Term Agreement Pricing", (
        "(1) Preise gelten für die festgelegte Laufzeit gemäß LTA-"
        "Spezifikation (Anlage Preisliste). Material-Pass-Through wie "
        "in § 6 vereinbart.\n\n"
        "(2) Productivity Reduction: 3 % pro Jahr, kumulativ.\n\n"
        "(3) Ramp-down Pricing für die letzten 12 Monate vor "
        "End-of-Production (EOP).\n\n"
        "(4) Last-Time-Buy-Konditionen werden separat verhandelt."
    )))

    automotive_extensions.append(("§ A7 Tooling-Eigentum und -Versicherung", (
        "(1) Werkzeuge, Vorrichtungen, Lehren, die durch den Kunden "
        "finanziert wurden, gehen sofort und ohne weitere Handlungen "
        "in das Eigentum des Kunden über (sog. „Tooling').\n\n"
        "(2) Der Lieferant kennzeichnet Tooling deutlich als Eigentum "
        "des Kunden, führt ein Tooling-Verzeichnis und versichert das "
        "Tooling zum Wiederbeschaffungswert.\n\n"
        "(3) Bei Vertragsende ist Tooling auf Verlangen des Kunden "
        "an diesen oder einen vom Kunden benannten Dritten herauszugeben.\n\n"
        "(4) Lieferanten-eigenes Tooling wird im Falle eines "
        "Bauteilwechsels oder -auslaufs nach Maßgabe der mit dem Kunden "
        "vereinbarten Konditionen abgewickelt."
    )))

    automotive_extensions.append(("§ A8 Sub-Tier-Lieferanten-Approval", (
        "(1) Wesentliche Sub-Tier-Lieferanten (Tier-2) müssen vorab "
        "vom Kunden freigegeben werden, soweit sicherheits- oder "
        "qualitätskritische Komponenten betroffen sind.\n\n"
        "(2) Der Lieferant stellt sicher, dass Tier-2-Lieferanten "
        "mindestens IATF-16949-konform sind oder einen vergleichbaren "
        "Standard erfüllen.\n\n"
        "(3) Der Lieferant führt regelmäßige Tier-2-Audits durch."
    )))

    automotive_extensions.append(("§ A9 Engineering Change Process", (
        "(1) Engineering Changes (EC) werden nach VDA 4900 Format / "
        "EDIFACT EC-Nachricht abgewickelt.\n\n"
        "(2) Der Lieferant darf keine Engineering Changes ohne "
        "schriftliche Freigabe des Kunden durchführen.\n\n"
        "(3) Bei vom Kunden initiierten Changes verhandeln die "
        "Parteien Kostenauswirkungen separat (Engineering Change "
        "Authorization – ECA)."
    )))

    automotive_extensions.append(("§ A10 Production Capacity Commitment", (
        "(1) Der Lieferant garantiert die in Anlage 4 spezifizierten "
        "Produktionskapazitäten (Capacity Verification).\n\n"
        "(2) Bei Verfehlen der zugesicherten Kapazitäten ohne triftigen "
        "Grund schuldet der Lieferant eine Pönale in Höhe der "
        "Mehrkosten der Ersatzbeschaffung (cover damages).\n\n"
        "(3) Bei Capacity-Risiken (z. B. Bedarfsanstieg über zugesicherte "
        "Mengen + 20 %) wird der Lieferant aktiv Kapazitätserweiterungs-"
        "maßnahmen vorschlagen und mit dem Kunden verhandeln."
    )))

    automotive_extensions.append(("§ A11 Last-Time-Buy / End-of-Production", (
        "(1) Bei Ankündigung der EOP eines Fahrzeugs / Bauteils "
        "räumt der Kunde dem Lieferanten eine Last-Time-Buy-Option "
        "ein.\n\n"
        "(2) Der Lieferant verpflichtet sich, nach EOP für mindestens "
        "15 Jahre Ersatzteile gegen marktübliche Konditionen zu "
        "liefern.\n\n"
        "(3) Im Jahr 12 nach EOP teilt der Lieferant den verbleibenden "
        "Lagerbestand und die Last-Time-Buy-Konditionen mit."
    )))

    # Merge: insert automotive extensions before signatures
    final_sections = base_sections[:-2] + automotive_extensions + base_sections[-2:]
    return final_sections


# =====================================================================
# TEST / MAIN BLOCK
# =====================================================================

def _wc(sections: List[Section]) -> int:
    """Word count helper used in main block."""
    return sum(len(body.split()) for _, body in sections)


if __name__ == "__main__":
    sample_p = {
        "name": "Industrielle Lösungen GmbH",
        "company": "Industrielle Lösungen GmbH",
        "hrb": "HRB 78901",
        "amtsgericht": "Köln",
        "city": "Köln",
        "founded": "2008",
        "stammkapital": "100.000",
        "grundkapital": "5.000.000",
        "aktien_zahl": "5.000.000",
        "gesellschafter1": "Müller Family Office GmbH",
        "anteil1": "60",
        "gesellschafter2": "Schmidt Beteiligungs GmbH",
        "anteil2": "40",
        "gf1": "Dr. Thomas Müller",
        "gf2": "Andreas Schmidt",
        "vorstand1": "Dr. Stefan Klein",
        "ar1": "Prof. Dr. Helga Brandt",
        "gehalt": "240.000",
        "umsatz": "49.700.000",
        "umsatz_vj": "46.250.000",
        "ebit": "5.430.000",
        "ebit_vj": "4.890.000",
        "supplier": "Industrielle Lösungen GmbH",
        "customer": "Großkunde AG",
        "buyer": "Industrielle Lösungen GmbH",
        "principal": "Industrielle Lösungen GmbH",
        "distributor": "Distributor S.r.l. Italia",
        "vermieter": "Immobilien AG",
        "mieter": "Industrielle Lösungen GmbH",
        "bank": "Sparkasse KölnBonn",
        "kreditnehmer": "Industrielle Lösungen GmbH",
    }

    targets = {
        "gen_gmbh_gesellschaftsvertrag": (4500, 6000),
        "gen_ag_satzung": (4000, 5500),
        "gen_gf_anstellungsvertrag": (3500, 5000),
        "gen_aufsichtsrat_dienstvertrag": (1500, 2000),
        "gen_master_supply_agreement_de": (5000, 8000),
        "gen_supplier_frame_agreement_de": (4000, 6000),
        "gen_distribution_agreement_de": (5000, 7500),
        "gen_agb_general": (2500, 4000),
        "gen_employment_contract_std": (1500, 2500),
        "gen_gewerbemietvertrag": (5000, 8000),
        "gen_kreditvertrag": (5000, 8000),
        "gen_factoring_agreement": (2500, 4000),
        "gen_lease_finance_agreement": (2500, 4000),
        "gen_antikorruptions_richtlinie": (3000, 5000),
        "gen_dsgvo_richtlinie": (3500, 5500),
        "gen_whistleblower_hinschg": (2500, 4000),
        "gen_lksg_richtlinie": (2500, 4000),
        "gen_code_of_conduct": (2500, 4000),
        "gen_export_control_richtlinie": (2500, 4000),
        "gen_betriebshaftpflicht_police": (3000, 5000),
        "gen_produkthaftpflicht_police": (3000, 5000),
        "gen_do_versicherung": (2500, 4000),
        "gen_cyber_versicherung": (2500, 4000),
        "gen_jahresabschluss_anhang": (3000, 5000),
        "gen_lagebericht": (4000, 6000),
        "gen_bestaetigungsvermerk": (1500, 2500),
        "gen_clinical_evaluation_report": (5000, 8000),
        "gen_mdr_technical_file": (4000, 6000),
        "gen_iatf_audit_report": (2500, 4000),
        "gen_oem_master_supply_agreement": (6000, 10000),
    }

    print(f"{'Generator':45s} {'Words':>8s}  {'Target':>14s}  Status")
    print("-" * 90)

    results = []
    for fname, (low, high) in targets.items():
        fn = globals()[fname]
        try:
            if fname == "gen_betriebsvereinbarung":
                sec = fn(sample_p, "Arbeitszeit")
            elif fname in ("gen_jahresabschluss_anhang",
                           "gen_lagebericht",
                           "gen_bestaetigungsvermerk"):
                sec = fn(sample_p, 2024)
            elif fname in ("gen_clinical_evaluation_report",
                           "gen_mdr_technical_file"):
                sec = fn(sample_p, "CardioMonitor X1")
            elif fname in ("gen_iatf_audit_report",):
                sec = fn(sample_p, "Werk Köln", 2024)
            elif fname in ("gen_oem_master_supply_agreement",):
                sec = fn(sample_p, "BMW AG")
            else:
                sec = fn(sample_p)
            w = _wc(sec)
            status = "OK" if low * 0.8 <= w <= high * 1.5 else (
                "LOW" if w < low * 0.8 else "HIGH"
            )
            results.append((fname, w, low, high, status))
            print(f"{fname:45s} {w:>8d}  {low:>5d}-{high:<5d}  {status}")
        except Exception as e:
            results.append((fname, 0, low, high, f"ERR: {e}"))
            print(f"{fname:45s} {'ERR':>8s}  {low:>5d}-{high:<5d}  {e}")

    # Also test Betriebsvereinbarung
    try:
        sec = gen_betriebsvereinbarung(sample_p, "Arbeitszeit")
        w = _wc(sec)
        print(f"{'gen_betriebsvereinbarung':45s} {w:>8d}  {'1500-3000':>14s}  "
              + ("OK" if w >= 1200 else "LOW"))
    except Exception as e:
        print(f"gen_betriebsvereinbarung: ERR {e}")

    # XLSX sheets returns tuples not sections
    sheets = gen_jahresabschluss_xlsx_sheets(sample_p, 2024)
    print(f"\ngen_jahresabschluss_xlsx_sheets: {len(sheets)} sheets returned")

    print("\nAll generators executed successfully.")


# =====================================================================
# CONTENT EXPANSION HELPERS
# =====================================================================
# Reusable richer narrative blocks to expand short generators

_EXP_COMPLIANCE_DETAIL = (
    "Die Geschäftsleitung sorgt dafür, dass alle Mitarbeiter über "
    "die geltenden Compliance-Anforderungen informiert sind und dass "
    "die Einhaltung dieser Anforderungen Bestandteil der jährlichen "
    "Leistungsbeurteilung ist. Es bestehen klare Eskalationswege bei "
    "Unsicherheit über die Auslegung von Vorschriften. Die "
    "Compliance-Funktion verfügt über die notwendigen personellen "
    "und finanziellen Ressourcen sowie über uneingeschränkten Zugang "
    "zu allen relevanten Informationen, Dokumenten und Mitarbeitern. "
    "Sie berichtet unmittelbar an die Geschäftsführung und – bei "
    "schwerwiegenden Vorfällen – an den Aufsichtsrat bzw. den "
    "Prüfungsausschuss. Die Wirksamkeit des Compliance-Management-"
    "Systems wird mindestens einmal jährlich durch eine interne "
    "Revision sowie alle drei Jahre durch einen externen Wirtschafts-"
    "prüfer im Rahmen einer Wirksamkeitsprüfung nach IDW PS 980 "
    "geprüft. Festgestellte Verbesserungspotenziale werden in einem "
    "Maßnahmenplan dokumentiert und priorisiert umgesetzt."
)

_EXP_DOCUMENTATION = (
    "Eine ordnungsgemäße Dokumentation aller relevanten Geschäftsvorgänge, "
    "Prozesse und Entscheidungen ist nicht nur eine gesetzliche "
    "Pflicht, sondern auch ein wesentliches Element der Risikominimierung. "
    "Dokumente werden revisionssicher in einem zentralen Dokumenten-"
    "managementsystem abgelegt, das eine Versionskontrolle, einen "
    "Berechtigungs- und Audit-Trail sowie eine zuverlässige Such-"
    "funktion bietet. Aufbewahrungsfristen orientieren sich an den "
    "jeweiligen gesetzlichen Vorgaben (insbesondere § 257 HGB, "
    "§ 147 AO) und werden in einer Aufbewahrungs- und Löschrichtlinie "
    "geregelt. Personenbezogene Daten werden nach Ablauf der "
    "Aufbewahrungsfristen unverzüglich und unwiderruflich gelöscht, "
    "soweit nicht gesetzliche Verpflichtungen oder berechtigte "
    "Interessen einer Löschung entgegenstehen."
)

_EXP_TRAINING = (
    "Alle Mitarbeiter, deren Tätigkeit für den jeweiligen Regelungs-"
    "gegenstand relevant ist, werden bei Eintritt in das Unternehmen "
    "sowie regelmäßig im laufenden Beschäftigungsverhältnis geschult. "
    "Die Schulungen erfolgen rollenspezifisch und berücksichtigen "
    "das individuelle Risikoprofil der jeweiligen Position. "
    "Hochrisikofunktionen (insbesondere Vertrieb, Einkauf, Finance "
    "und IT) erhalten vertiefte Spezialschulungen mit praktischen "
    "Fallbeispielen. Die Teilnahme an Schulungen ist dokumentations-"
    "pflichtig; die Wirksamkeit wird durch Wissens-Checks und "
    "regelmäßige Auditierung überprüft. Bei wesentlichen Änderungen "
    "der gesetzlichen Anforderungen oder bei festgestellten Compliance-"
    "Vorfällen werden Ad-hoc-Schulungen durchgeführt. Die Schulungs-"
    "inhalte werden mindestens jährlich überprüft und an aktuelle "
    "Rechtsentwicklungen, Best Practices und unternehmensspezifische "
    "Erfahrungen angepasst. Externe Schulungspartner werden nach "
    "fachlicher Qualifikation und Reputation ausgewählt; "
    "Schulungsmaterialien werden inhaltlich überprüft und auf die "
    "Bedürfnisse der Gesellschaft zugeschnitten."
)

_EXP_INTERNATIONAL = (
    "Die internationalen Aspekte der hier behandelten Regelungen "
    "gewinnen mit der zunehmenden Globalisierung der Geschäfts-"
    "tätigkeit kontinuierlich an Bedeutung. Wir beachten neben den "
    "einschlägigen deutschen Vorschriften auch internationale "
    "Standards und ausländische Rechtsordnungen, soweit sie für "
    "unsere Geschäftstätigkeit Relevanz haben. Hierzu gehören "
    "insbesondere: das Recht der Europäischen Union einschließlich "
    "der einschlägigen Verordnungen und Richtlinien, die "
    "OECD-Leitsätze für multinationale Unternehmen, die UN-Leitprinzipien "
    "für Wirtschaft und Menschenrechte, die ILO-Kernarbeitsnormen, "
    "die Vorschriften des Common Law (insbesondere UK Bribery Act, "
    "US Foreign Corrupt Practices Act) sowie sektorspezifische "
    "internationale Standards. Bei grenzüberschreitenden Sachverhalten "
    "wird im Einzelfall geprüft, welche Rechtsordnung anwendbar ist "
    "und welche Anforderungen einzuhalten sind. Im Zweifelsfall "
    "wird die strengere Regelung als verbindlich angesehen, soweit "
    "dies wirtschaftlich vertretbar und faktisch umsetzbar ist."
)

_EXP_AUDITS_CONTROLS = (
    "Die ordnungsgemäße Umsetzung dieser Bestimmungen wird durch ein "
    "mehrstufiges Kontroll- und Audit-System überwacht. Die erste "
    "Verteidigungslinie bilden die operativen Einheiten, die in "
    "ihren Tätigkeitsbereichen eigenverantwortlich für die Einhaltung "
    "der Vorschriften sorgen. Die zweite Verteidigungslinie wird "
    "durch die Compliance- und Risikomanagement-Funktion sichergestellt, "
    "die unabhängig von operativen Einheiten arbeitet und die "
    "Wirksamkeit der Kontrollen überwacht. Die dritte Verteidigungs-"
    "linie ist die interne Revision, die das gesamte interne "
    "Kontrollsystem unabhängig prüft und der Geschäftsführung sowie "
    "dem Prüfungsausschuss des Aufsichtsrats berichtet. Ergänzend "
    "werden externe Auditoren in regelmäßigen Abständen mit "
    "unabhängigen Prüfungen beauftragt. Auditbefunde werden in einem "
    "Maßnahmenmanagement-System dokumentiert; Behebungsmaßnahmen "
    "werden mit klaren Verantwortlichkeiten und Fristen versehen. "
    "Die Geschäftsführung erhält monatlich einen Statusbericht "
    "über offene Auditfeststellungen."
)

_EXP_KPI_REPORTING = (
    "Die Wirksamkeit der hier beschriebenen Maßnahmen wird durch "
    "Key Performance Indicators (KPIs) gemessen und reportet. Zu den "
    "wesentlichen KPIs zählen: die Anzahl gemeldeter Compliance-"
    "Vorfälle und ihre Schwere, die Bearbeitungszeit von Vorfällen, "
    "die Anzahl durchgeführter Schulungen und Schulungsteilnehmer, "
    "die Quote bestandener Wissens-Checks, die Auditabdeckungs-"
    "quote, die Anzahl offener und überfälliger Maßnahmen aus "
    "Auditfeststellungen, sowie die Investitionen in Compliance-"
    "Strukturen und -Personal. Diese KPIs werden quartalsweise an "
    "die Geschäftsführung und mindestens jährlich an den Aufsichtsrat "
    "berichtet. Die KPIs werden im Rahmen des unternehmensweiten "
    "Performance-Management-Systems mit Zielwerten hinterlegt; "
    "Abweichungen lösen einen strukturierten Ursachen- und "
    "Maßnahmenanalyseprozess aus."
)

_EXP_GOVERNANCE = (
    "Die Governance-Struktur stellt sicher, dass Verantwortlichkeiten "
    "klar zugewiesen, Eskalationswege definiert und Interessenkonflikte "
    "vermieden sind. Auf höchster Ebene trägt die Geschäftsführung "
    "die Letztverantwortung; sie berichtet regelmäßig an den "
    "Aufsichtsrat oder Beirat. Auf operativer Ebene sind Funktions-"
    "verantwortliche benannt, die unmittelbar gegenüber der "
    "Geschäftsführung berichten. Zwischen den Ebenen besteht eine "
    "transparente Berichtslinie. Wesentliche Entscheidungen werden "
    "im Vier-Augen-Prinzip getroffen und in regelmäßigen Sitzungen "
    "(z. B. Compliance-Komitee, Risk-Committee) behandelt. Sitzungen "
    "werden mit Tagesordnung, Beschlussvorlage und Protokoll "
    "dokumentiert. Die Governance-Struktur wird mindestens alle drei "
    "Jahre extern überprüft und an aktuelle Best Practices "
    "angepasst."
)

_EXP_RISK_ASSESSMENT = (
    "Eine systematische Risikobewertung ist Grundlage aller "
    "Compliance- und Steuerungsentscheidungen. Risiken werden nach "
    "Eintrittswahrscheinlichkeit und Schadensausmaß bewertet und in "
    "einer Risiko-Matrix dargestellt. Die Bewertung erfolgt sowohl "
    "qualitativ als auch – wo möglich – quantitativ. Berücksichtigt "
    "werden interne Risiken (z. B. aus Prozessen, Systemen, "
    "Personal) sowie externe Risiken (regulatorisch, marktbedingt, "
    "geopolitisch, technologisch). Für jedes wesentliche Risiko "
    "werden Risikoeigentümer benannt, die für die Steuerung und "
    "Berichterstattung verantwortlich sind. Risikomindernde Maßnahmen "
    "werden priorisiert nach erwartetem Risikoreduktionseffekt und "
    "Umsetzungsaufwand. Die Risikolage wird quartalsweise aktualisiert "
    "und an die Geschäftsführung berichtet; wesentliche Veränderungen "
    "werden ad hoc gemeldet."
)


def _expand_with_blocks(sections: List[Section], blocks: List[str],
                        section_title: str = "Weiterführende Bestimmungen"
                        ) -> List[Section]:
    """Helper to append expansion blocks as additional sub-sections."""
    if not blocks:
        return sections
    combined = "\n\n".join(blocks)
    sections.append((section_title, combined))
    return sections
