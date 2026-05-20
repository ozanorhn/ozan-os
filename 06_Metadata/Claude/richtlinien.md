# Richtlinien für Claude

## Vor jeder Reorganisation

1. Ordnerstruktur prüfen: `find . -type d | sort`
2. Zielordner verifizieren bevor Dateien bewegt werden
3. `mv` verwenden (nie `cp`) um Duplikate zu vermeiden

## Inhalt erstellen

- Immer auf Deutsch (außer explizit anders gewünscht)
- `[[WikiLinks]]` für interne Verweise
- YAML-Frontmatter mit Datum, Tags, Status
- Direkte, klare Sprache – keine unnötigen Füllwörter

## Einfache Befehle bevorzugen

- Direkte Befehle ohne komplexe Pipes oder Regex-Filter
- Lieber mehrere einfache Schritte als einen komplexen Einzeiler

---

## Verhaltensrichtlinien (Karpathy / LLM Best Practices)

### 1. Erst denken, dann coden

**Keine Annahmen. Keine versteckte Verwirrung. Abwägungen benennen.**

Vor jeder Implementierung:
- Annahmen explizit nennen. Bei Unsicherheit: fragen.
- Wenn mehrere Interpretationen möglich sind, alle vorstellen – nicht still eine wählen.
- Wenn ein einfacherer Ansatz existiert, sagen. Rückfragen sind erlaubt.
- Wenn etwas unklar ist: stoppen, benennen, fragen.

### 2. Einfachheit zuerst

**Minimum an Code, der das Problem löst. Nichts Spekulatives.**

- Keine Features über das Gewünschte hinaus.
- Keine Abstraktionen für einmalig verwendeten Code.
- Keine ungeforderte „Flexibilität" oder „Konfigurierbarkeit".
- Kein Error Handling für unmögliche Szenarien.
- Wenn 200 Zeilen auch 50 sein könnten: neu schreiben.

Frage: „Würde ein Senior Engineer das als überkompliziert bezeichnen?" Falls ja: vereinfachen.

### 3. Chirurgische Änderungen

**Nur anfassen, was nötig ist. Nur den eigenen Dreck aufräumen.**

Bei bestehendem Code:
- Keinen angrenzenden Code, Kommentare oder Formatierung „verbessern".
- Nichts refactoren, was nicht kaputt ist.
- Bestehenden Stil übernehmen, auch wenn man es anders machen würde.
- Ungenutzten Code erwähnen – nicht löschen.

Bei eigenen Änderungen:
- Imports/Variablen/Funktionen entfernen, die durch EIGENE Änderungen überflüssig wurden.
- Vorher vorhandenen toten Code nicht entfernen, außer ausdrücklich gebeten.

Test: Jede geänderte Zeile sollte direkt auf die Anfrage des Nutzers zurückzuführen sein.

### 4. Zielorientierte Ausführung

**Erfolgskriterien definieren. Bis zur Verifikation iterieren.**

Aufgaben in verifizierbare Ziele umwandeln:
- „Validierung hinzufügen" → „Tests für ungültige Eingaben schreiben, dann zum Laufen bringen"
- „Bug fixen" → „Test schreiben, der ihn reproduziert, dann fixen"

Bei mehrstufigen Aufgaben kurzen Plan nennen:

```
1. [Schritt] → prüfen: [check]
2. [Schritt] → prüfen: [check]
3. [Schritt] → prüfen: [check]
```
