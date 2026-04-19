---
name: wochen-metriken
description: 'Wöchentliche Metriken aggregieren: Training, Rauchfrei, Körper, Finanzen – Übersicht erstellen'
argument-hint: '[KW-Nummer]'
---

# Wochen-Metriken

Aggregiere alle messbaren Daten der Woche zu einer kompakten Übersicht.

## Schritt 1 – Daten laden

Lese parallel:

**Training (Fett to Fit):**
- Alle Tracking-Dateien dieser Woche aus `01_Projects/Fett to Fit/Tracking/` (Push, Pull, Legs)
- `01_Projects/Fett to Fit/Fett to Fit.md` für Ausgangswerte (94 kg, Startdatum)

**Rauchfrei:**
- `01_Projects/Rauchfrei/Fortschritt.md` – aktuelle Tabelle und Streak

**Finanzen (monatlich, falls neue Woche = Monatswechsel):**
- `02_Areas/Finanzen/Budget.md`
- `02_Areas/Finanzen/Vermögensübersicht.md`

## Schritt 2 – Metriken berechnen

Aus den geladenen Daten ableiten:

**Training:**
- Anzahl Sessions diese Woche (von 3 geplant)
- Gesamtvolumen (Sätze × Wiederholungen × Gewicht) je Session falls ableitbar
- Progressionen: Welche Übungen hatten neue Bestleistungen?

**Rauchfrei:**
- Rauchfreie Tage in dieser Woche
- Aktueller Streak (Gesamttage seit 30.03.2026)
- Durchschnittliche Craving-Stärke (0–10)

**Körper:**
- Gewicht (falls in einer Tracking-Datei eingetragen)
- Delta zum Ausgangswert (94 kg)

## Schritt 3 – Fehlende Daten erfragen

Falls Metriken fehlen (Gewicht, besondere Ereignisse), frage kurz nach:
- "Aktuelles Gewicht diese Woche?"
- "Besondere Ereignisse oder Rückfälle?"

## Schritt 4 – Zusammenfassung ausgeben

```
## Wochen-Metriken KW[N] – [Datum-Range]

### Training
| Metrik              | Wert         |
|---------------------|--------------|
| Sessions            | X / 3        |
| Progressionen       | [Übungen]    |
| Schwächste Session  | [Typ + warum]|

### Rauchfrei
| Metrik                    | Wert |
|---------------------------|------|
| Rauchfreie Tage (Woche)   | X/7  |
| Gesamtstreak              | X Tage |
| Ø Craving-Stärke          | X/10 |
| Schwerster Tag            | [Datum] |

### Körper
| Metrik           | Wert    |
|------------------|---------|
| Gewicht          | X kg    |
| Delta Start      | −X kg   |
| Trend            | ↓ / → / ↑ |

### Woche in einem Satz
[Subjektive Einschätzung: War es eine gute Woche?]
```

## Schritt 5 – Optional speichern

Frage: "Soll ich die Metriken in der Weekly Synthesis oder als eigene Datei speichern?"

Falls ja: Erstelle `03_Resources/Reviews/[DATUM] - Metriken KW[N].md` mit den Daten und passendem Frontmatter:

```yaml
---
datum: YYYY-MM-DD
tags: [metriken, wochenreview]
kw: N
---
```
