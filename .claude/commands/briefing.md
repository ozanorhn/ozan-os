# Briefing

Morgen-Kontext: liest den aktuellen Stand und gibt ein kompaktes Briefing aus. Schreibt nichts.

## Was lesen

1. `CLAUDE.md` – aktive Projekte, Jahres-Ziele, Google-Setup
2. `06_Metadata/log.md` – letzte 5 Log-Einträge (`grep "^## \[" 06_Metadata/log.md | tail -5`)
3. Google Tasks: `python3 .claude/skills/google-tasks/scripts/fetch-tasks.py --overdue`
4. Neueste Daily Note in `07_Daily/` (nach Datum sortiert)
5. Aktuellster Wochenplan in `06_Metadata/Plans/` (nach Datum sortiert)

## Output-Format

```
# Briefing – [Datum, Wochentag]

## Fokus heute
[1–2 Sätze: Was ist der wichtigste Kontext für heute?]

## Offene Loops
- [Überfällige Tasks oder Anker, max. 5 Items]

## Nächste Fälligkeiten
| Datum | Was |
|-------|-----|
| ...   | ... |

## Aus dem Log (letzte Aktivitäten)
- [YYYY-MM-DD] type: titel
- ...

## Aktive Projekte – Status
- **Fett to Fit:** [letzte Session, nächstes Training]
- **Rauchfrei:** [aktueller Anker-Status, Tage bis Tag 1]
- **Hochzeit:** [nächster Meilenstein]
```

## Hinweise

- Kein Schreiben, keine Änderungen – nur lesen und ausgeben
- Kompakt halten: max. 30 Zeilen Output
- Wenn Google Tasks leer sind, darauf hinweisen und aus Daily Note / Wochenplan schöpfen
