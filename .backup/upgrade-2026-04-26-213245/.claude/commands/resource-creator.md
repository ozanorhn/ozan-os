---
name: resource-creator
description: 'Atomare Wissensnotiz in 03_Resources erstellen – aus URL, Thema oder Buchnotizen'
argument-hint: '[URL oder Thema]'
---

# Resource Creator

Erstelle eine atomare Wissensnotiz in `03_Resources/` – aus einer URL, einem Thema oder eigenen Notizen.

## Schritt 1 – Quelle bestimmen

Falls kein Argument übergeben, frage:
- "URL, Thema oder eigene Notizen?"
- "Zu welchem Themenbereich gehört es?" (Fitness/Ernährung, Finanzen, Hochzeit, Gesundheit, Allgemein)

## Schritt 2 – Inhalt erfassen

**Bei URL:** Rufe den Inhalt ab und extrahiere die Kernaussagen.

**Bei Thema ohne URL:** Frage nach dem Kerninhalt – was soll festgehalten werden? Was ist die wichtigste Erkenntnis?

**Bei eigenen Notizen:** Fasse zusammen, was der Nutzer eingibt.

## Schritt 3 – Kategorie und Pfad bestimmen

Ordne in einen Themenordner ein:

| Thema | Pfad |
|-------|------|
| Fitness / Training | `03_Resources/Fitness/` |
| Ernährung / Makros | `03_Resources/Ernährung/` |
| Finanzen / Investing | `03_Resources/Finanzen/` |
| Hochzeit / Traditionen | `03_Resources/Hochzeit/` |
| Gesundheit / Mental | `03_Resources/Gesundheit/` |
| Sonstiges | `03_Resources/` (direkt) |

Erstelle den Unterordner falls er nicht existiert.

## Schritt 4 – Notiz erstellen

**Dateiname:** `Ressource - [Thema] - [Quelle oder Schlagwort].md`

**Format:**

```markdown
---
datum: YYYY-MM-DD
tags: [ressource, themenbereich]
quelle: [URL oder "Eigene Notizen" oder Buchname]
---

# [Thema]

## Kernaussage

[Ein oder zwei Sätze: Was ist das Wichtigste an dieser Ressource?]

## Inhalt

[Strukturierte Zusammenfassung – in eigenen Worten, nicht copy-paste]

## Anwendung

[Wie ist das für Ozan relevant? Was kann er konkret damit machen?]

## Verknüpfungen

- [[Verwandtes Projekt oder Thema]]
```

**Prinzipien:**
- Atomar: Eine Kernaussage pro Notiz
- Eigene Worte, nicht einfach abschreiben
- Immer den "Wozu"-Kontext für Ozan ergänzen

## Schritt 5 – Ressourcen-Index aktualisieren

Füge einen Eintrag in `03_Resources/Ressourcen.md` hinzu (falls eine Indexliste existiert):

```markdown
- [[Ressource - Thema - Quelle]] – [Ein-Satz-Beschreibung]
```

## Schritt 6 – Bestätigen

Teile mit wo die Notiz gespeichert wurde und welche Verknüpfungen angelegt wurden.
