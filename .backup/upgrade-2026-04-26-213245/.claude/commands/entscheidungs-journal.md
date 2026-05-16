---
name: entscheidungs-journal
description: 'Wichtige Entscheidung dokumentieren – Kontext, Optionen, Wahl, Begründung, Erwartung'
argument-hint: '[Entscheidungsthema]'
---

# Entscheidungs-Journal

Dokumentiere eine wichtige Entscheidung strukturiert, bevor sie (oder nachdem sie) getroffen wurde.

## Schritt 1 – Kontext erfassen

Frage den Nutzer (falls nicht als Argument übergeben):
- Um welche Entscheidung geht es?
- Zu welchem Projekt oder Bereich gehört sie? (Hochzeit, Fett to Fit, Finanzen, Rauchfrei, Allgemein)
- Ist die Entscheidung bereits getroffen oder noch offen?

## Schritt 2 – Entscheidung dokumentieren

Erstelle eine Datei nach diesem Schema:

**Pfad:**
- Projektspezifisch: `01_Projects/[Projekt]/Entscheidungen/YYYY-MM-DD - [Thema].md`
- Bereichsspezifisch: `02_Areas/[Bereich]/Entscheidungen/YYYY-MM-DD - [Thema].md`
- Allgemein: `03_Resources/Entscheidungen/YYYY-MM-DD - [Thema].md`

Erstelle den Unterordner `Entscheidungen/` falls er nicht existiert.

**Format:**

```markdown
---
datum: YYYY-MM-DD
tags: [entscheidung, projekt-oder-bereich]
status: offen | getroffen
bereich: Hochzeit | Finanzen | Gesundheit | Rauchfrei | Allgemein
---

# Entscheidung: [Thema]

## Kontext

[Warum steht diese Entscheidung an? Was ist die Ausgangslage?]

## Optionen

### Option A: [Name]
- Vorteile: 
- Nachteile: 
- Kosten/Aufwand: 

### Option B: [Name]
- Vorteile: 
- Nachteile: 
- Kosten/Aufwand: 

### Option C: [Name] *(falls relevant)*
...

## Entscheidung

**Gewählt:** Option [X]

**Begründung:** [Warum diese Option? Was war ausschlaggebend?]

## Erwartetes Ergebnis

[Was erhoffst du dir? Wie sieht Erfolg aus?]

## Review-Datum

Rückblick geplant: [YYYY-MM-DD] *(empfohlen: 4–8 Wochen nach der Entscheidung)*

## Rückblick *(später ausfüllen)*

**Datum:**
**Ergebnis:**
**Lernpunkt:**
```

## Schritt 3 – Verlinken

Füge in der Hauptdatei des betreffenden Projekts/Bereichs einen Verweis ein:

```markdown
- [[YYYY-MM-DD - Thema]] – [ein Satz Kontext]
```

## Schritt 4 – Bestätigen

Teile dem Nutzer mit:
- Wo die Datei gespeichert wurde
- Das empfohlene Review-Datum
