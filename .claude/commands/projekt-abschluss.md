---
name: projekt-abschluss
description: 'Projekt formal abschließen: Review, Learnings, Dateien nach 04_Archive verschieben'
argument-hint: '[Projektname]'
---

# Projekt-Abschluss

Schließe ein abgeschlossenes oder aufgegebenes Projekt formal ab und archiviere es sauber.

## Schritt 1 – Projekt identifizieren

Falls kein Argument übergeben: Frage welches Projekt abgeschlossen werden soll.
Zeige aktive Projekte in `01_Projects/` zur Auswahl.

## Schritt 2 – Projekt analysieren

Lese alle Dateien des Projekts:
- Hauptdatei (z.B. `01_Projects/[Projekt]/[Projekt].md`)
- Alle Unterordner und Dateien
- Verweise auf Google Tasks falls vorhanden

Erstelle eine Zusammenfassung:
- Ursprüngliches Ziel
- Was wurde erreicht?
- Was blieb offen?
- Zeitraum (Start → Abschluss)

## Schritt 3 – Abschluss-Review dokumentieren

Erstelle `01_Projects/[Projekt]/Abschluss-Review.md`:

```markdown
---
datum: YYYY-MM-DD
tags: [abschluss, projekt]
status: abgeschlossen | aufgegeben
---

# Abschluss-Review: [Projektname]

## Projektziel

[Was sollte erreicht werden?]

## Ergebnis

**Status:** Erfolgreich abgeschlossen / Teilweise erreicht / Aufgegeben

[Was wurde tatsächlich erreicht?]

## Zeitraum

Start: [Datum]
Abschluss: [Datum]
Dauer: [X Wochen/Monate]

## Was gut funktioniert hat

- 
- 

## Was ich anders machen würde

- 
- 

## Wichtigste Erkenntnis

[Ein Satz – die wichtigste Lektion aus diesem Projekt]

## Offene Punkte

*Falls aufgegeben oder unvollständig:*
- [ ] [Was noch offen ist und wohin es gehört]

## Weiterführende Notizen

- [[Verknüpfte Ressource oder Bereich]]
```

## Schritt 4 – Archivieren

1. Verschiebe den gesamten Projektordner nach `04_Archive/[Projektname]/`:
   ```bash
   mv "01_Projects/[Projektname]" "04_Archive/[Projektname]"
   ```

2. Aktualisiere `04_Archive/Archiv.md`: Füge einen Eintrag hinzu:
   ```markdown
   - [[Abschluss-Review]] – [Datum] – [Ein-Satz-Beschreibung]
   ```

3. Entferne Verweise aus aktiven Notizen (Projekte-Index, CLAUDE.md falls nötig).

## Schritt 5 – Bestätigen

Berichte:
- Projekt archiviert unter: `04_Archive/[Projektname]/`
- Review gespeichert: `04_Archive/[Projektname]/Abschluss-Review.md`
- Was noch offen bleibt (falls vorhanden)
