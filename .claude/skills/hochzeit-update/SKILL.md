---
name: hochzeit-update
description: Hochzeits-Checklisten und Budget-Status anzeigen und aktualisieren. Use when the user asks about wedding tasks, Hochzeit checklist, Nişan preparation, Gelin Bohçası, wedding budget, or wants to update wedding todos.
---

# Hochzeit Update

Zeige offene Todos, kommende Deadlines und Budget-Status für Nişan und Düğün.

## Ablauf

1. **Dateien laden**
   - Lies `01_Projects/Hochzeit/Hochzeit.md` (Hauptdatei, Timeline, Nächste Schritte)
   - Lies alle Dateien in `01_Projects/Hochzeit/Checklisten/` (Checklisten, Kanban)
   - Lies `02_Areas/Finanzen/Budget.md` für Hochzeitsfonds-Status

2. **Status-Check**
   - Offene Todos aus Nächste Schritte extrahieren (alle `[ ]` Items)
   - Deadline-Prüfung: Was ist in den nächsten 30 Tagen fällig?
   - Gelin Bohçası Fortschritt: Wie viele Kategorien abgehakt?
   - Hochzeitsfonds: Aktueller Stand vs. Ziel (400€/M)

3. **Timeline-Check**
   - Wo stehen wir in der 4-Monate-Regel?
   - Nächster Meilenstein aus der Timeline

## Output Format

```
## Hochzeit Update – [Datum]

### Schlüsseldaten
- Nişan: 19.09.2026 (in X Wochen)
- Düğün: 02.10.2027

### Dringend (nächste 30 Tage)
- [ ] [Task] – Deadline: [Datum]

### Offene Todos
- [ ] [Task 1]
- [ ] [Task 2]

### Gelin Bohçası
[X/Y Kategorien erledigt]

### Hochzeitsfonds
[Aktueller Stand] – Ziel: 400€/M

### Nächster Meilenstein
[Was laut Timeline als nächstes ansteht]
```

## Regeln
- Immer Countdown bis Nişan (19.09.2026) anzeigen
- Überfällige Tasks deutlich markieren
- Bei Updates: Datei direkt bearbeiten (Checkbox von [ ] zu [x])
