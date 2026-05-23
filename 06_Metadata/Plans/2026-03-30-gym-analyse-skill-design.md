---
title: Design – gym-analyse Skill
date: 2026-03-30
tags: [design, skill, training]
status: approved
---

# Design: `/gym-analyse` Skill

## Ziel

Skill analysiert automatisch die letzte Gym-Session, gibt konkrete Tipps pro Übung und erstellt eine neue Tracking-Datei für die nächste Session der gleichen Art (z.B. Push → nächste Woche Push).

---

## Ablauf

1. **Tracking-Dateien lesen** – alle `.md` Dateien in `01_Projects/Fett to Fit/Tracking/` (außer Wochenanalysen)
2. **Letzte Session erkennen** – höchstes Datum im Dateinamen
3. **Nächste Session bestimmen** – Push → Pull → Legs → Push (Zyklus)
4. **Analyse ausgeben** – im Chat:
   - Übungen mit Auffälligkeiten (Gewichtsschwankungen, fehlende Sätze, zu viele/wenige Wdh.)
   - Progressive Overload Check (alle Sätze auf Max-Wdh. → Gewicht erhöhen)
   - Energie/Pump Bewertung
   - Konkrete Tipps pro Übung für nächste Woche
5. **Neue Tracking-Datei erstellen** für die nächste Woche, gleicher Typ:
   - Dateiname: `YYYY-MM-DD - [Typ] W[N].md` (Datum = +7 Tage)
   - Tipps direkt in der Notiz-Spalte der jeweiligen Übung vorausgefüllt

---

## Analyse-Logik

| Situation | Tipp |
|-----------|------|
| Alle Sätze auf Max-Wdh. | „Gewicht um 2,5 kg erhöhen" |
| Gewicht inkonstant über Sätze | „Gewicht konstant halten, dann steigern" |
| Weniger Wdh. als Ziel | „Gewicht reduzieren oder halten" |
| Satz nicht gemacht | „Satz nachholen" |
| Energie ≤ 2 Sterne | Hinweis auf Erholung/Schlaf |

---

## Neue Tracking-Datei

Gleiches Format wie bestehende Dateien, aber Notiz-Spalte vorausgefüllt:

```
| 1 | 25 | – | Zielgewicht aus letzter Woche. Konstant halten! |
| 2 | 25 | – | Alle 3 Sätze schaffen → dann +2,5 kg |
```

---

## Wochenanalyse (in `/weekly-synthesis`)

Zusätzlicher Block in der bestehenden Weekly Synthesis:

- Alle 3 Sessions (Push/Pull/Legs) der Woche zusammenfassen
- Progression je Übung über die Woche
- Schwachstellen + Vorschläge für nächste Woche
- Erstellt: `01_Projects/Fett to Fit/Tracking/YYYY-MM-DD - Wochenanalyse W[N].md`

---

## Dateipfade

| Typ | Pfad |
|-----|------|
| Tracking | `01_Projects/Fett to Fit/Tracking/` |
| PPL Plan | `01_Projects/Fett to Fit/Training/PPL Trainingsplan.md` |
| Design Doc | `06_Metadata/Plans/2026-03-30-gym-analyse-skill-design.md` |
| Skill | `.claude/commands/gym-analyse.md` |
