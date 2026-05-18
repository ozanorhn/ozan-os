---
name: gym-analyse
description: Analysiere Ozans Trainingsfortschritt im Fett-to-Fit Projekt. Use when the user asks for a training analysis, wants to see gym progress, asks about workout progression, wants to check last sessions, or needs training recommendations.
---

# Gym Analyse

Analysiere den Trainingsfortschritt und gib datenbasierte Empfehlungen.

## Ablauf

1. **Letzte Sessions laden**
   - Lies alle Dateien in `01_Projects/Fett to Fit/Tracking/` (neueste zuerst)
   - Lies `01_Projects/Fett to Fit/Fett to Fit.md` für Kontext (aktueller Block, Plan, Ziele)
   - Lies `2026-05-17 - Baseline.md` für Ausgangswerte

2. **Progression analysieren**
   - Gewichtsentwicklung über Zeit
   - Trainingsvolumen (Sätze × Wiederholungen × Gewicht) pro Übung
   - Vergleich Session zu Session: Hat sich das Gewicht erhöht?
   - Fehlende Sessions / Gaps identifizieren

3. **Nächste Einheit bestimmen**
   - Aktuelle Rotation: Upper A → Upper B → Upper C → Upper A...
   - Welche Einheit kommt als nächstes?
   - Welche Gewichte sollten angestrebt werden (letzte Leistung + Progression)?

## Output Format

```
## Gym Analyse – [Datum]

### Letzte Sessions
| Datum | Einheit | Highlights |
|-------|---------|------------|
| ...   | ...     | ...        |

### Progression
**[Übungsname]:** [letztes Gewicht] → Ziel heute: [Empfehlung]

### Nächste Einheit: [Upper A/B/C]
- [Übung 1]: [Gewicht × Sätze × Reps]
- [Übung 2]: ...

### Insights
- [Positive Entwicklung]
- [Was verbessert werden kann]

### Körpergewicht
Letzter Eintrag: [X] kg am [Datum] – [Trend]
```

## Regeln
- Immer konkrete Zahlen aus den Tracking-Dateien verwenden
- Keine vagen Empfehlungen – spezifische Gewichte nennen
- Wenn Gewicht seit >5 Tagen nicht eingetragen: daran erinnern (Montag morgens nüchtern)
- Progressive Overload: wenn 3×10 mit einem Gewicht geschafft → nächste Session +2,5 kg
