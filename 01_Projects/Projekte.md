---
title: Projekte
type: moc
aliases: [Projekte, Projects]
---

# 🎯 Projekte

Aktive Vorhaben mit konkreten Ergebnissen und Fristen.

## Zweck

Projekte sind **zeitlich begrenzte Vorhaben** mit:
- Klaren Zielen und Ergebnissen
- Definierten Start- und Enddaten
- Messbaren Erfolgskriterien

## Aktuelle Projekte

- [[Hochzeit]] – Hochzeitsplanung
- [[Fett to Fit]] – Körperliche Transformation
- [[Rauchfrei]] – Dauerhaft rauchfrei leben

## Was hierher gehört

### Gute Projekte
- "Hochzeit planen" ✓
- "Fett to Fit – Transformation" ✓
- "Website erstellen" ✓

### Keine Projekte (diese gehören in Bereiche)
- "Gesundheit" ✗ (laufend, kein Enddatum)
- "Finanzen" ✗ (dauerhafte Verantwortung)
- "Sport treiben" ✗ (fortlaufende Aktivität)

## Projektstruktur

Jedes Projekt sollte haben:
```
Projektname/
├── README.md           # Projektübersicht und Status
├── Research/           # Hintergrundmaterialien
├── Fortschritt/        # Protokoll der Arbeitssitzungen
├── Entwürfe/           # Arbeit in Bearbeitung
├── Ressourcen/         # Unterstützende Dokumente
└── Ergebnisse/         # Finale Lieferergebnisse
```

## Claude-Workflows

### Projekt starten
```
Erstelle ein neues Projekt namens [Name] in 01_Projects.
Richte es mit der Standardordnerstruktur ein.
Ich bin im Denkmodus – hilf mir, die Ziele zu definieren.
```

### Projektrecherche
```
Ich arbeite an [Projektname].
Suche in meinem Vault nach relevanten Notizen.
Welche Verbindungen gibt es zu meiner anderen Arbeit?
```

### Tagesfortschritt
```
Erstelle eine Fortschrittsnotiz für heute in [Projekt]/Fortschritt.
Das habe ich heute geschafft: [Zusammenfassung]
Fragen, die aufgetaucht sind: [Liste]
```

### Projektstatus
```
Überprüfe alle Notizen in [Projektordner].
Was ist der aktuelle Status?
Was sind die wichtigsten Erkenntnisse bisher?
Was fehlt noch?
```

### Projektabschluss
```
Projekt [Name] ist abgeschlossen.
Erstelle eine Retrospektive mit:
- Ziele vs. Ergebnisse
- Wichtigste Lernpunkte
- Was nächstes Mal anders machen
Dann hilf mir, es richtig zu archivieren.
```

## Projektlebenszyklus

1. **Start**: Ziele und Erfolgskriterien definieren
2. **Recherche**: Relevante Informationen sammeln
3. **Umsetzung**: Täglicher Fortschritt, iterative Arbeit
4. **Review**: Regelmäßige Statusprüfungen
5. **Abschluss**: Finales Ergebnis, Retrospektive
6. **Archiv**: Verschieben nach `04_Archive/` mit Zusammenfassung

## Wann archivieren?

Projekte nach `04_Archive/` verschieben wenn:
- Alle Ziele erreicht sind
- Das Projekt abgebrochen wurde
- Es seit 30+ Tagen inaktiv ist
- Es sich in einen Bereich verwandelt hat (laufend)

Immer eine Zusammenfassung erstellen vor dem Archivieren!
