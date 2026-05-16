# Weekly Synthesis

Create a comprehensive synthesis of the week's work and thinking.

## Analysis Process

1. **Gather Week's Work**
   - All notes created this week
   - All notes modified this week
   - Projects that saw activity

2. **Identify Patterns**
   - Recurring themes
   - Common challenges
   - Breakthrough moments
   - Energy patterns (what energized vs drained)

3. **Synthesize Learning**
   - Key insights that emerged
   - How thinking evolved
   - Connections discovered
   - Questions answered and raised

4. **Assess Progress**
   - Projects advanced
   - Areas maintained
   - Resources added
   - Items archived

## Output Format

Create a weekly synthesis note:

```markdown
# Weekly Synthesis - Week of [Date]

## Week at a Glance

- Notes created: [X]
- Projects active: [List]
- Major accomplishments: [List]

## Key Themes

### Theme 1: [Name]

- Where it appeared: [contexts]
- Why it matters: [significance]
- Next actions: [what to do]

### Theme 2: [Name]

- Where it appeared: [contexts]
- Why it matters: [significance]
- Next actions: [what to do]

## Major Insights

1. [Insight with context]
2. [Insight with context]

## Progress by Project

### [Project Name]

- What advanced:
- What's blocked:
- Next week's focus:

## Questions Emerged

- [Question 1 - and why it matters]
- [Question 2 - and why it matters]

## Energy Audit

- What gave energy:
- What drained energy:
- What to adjust:

## Connections Made

- [Note A] ←→ [Note B]: [Why significant]
- [Concept X] ←→ [Concept Y]: [New understanding]

## Next Week's Intentions

1. [Primary focus]
2. [Secondary focus]
3. [Thing to explore]

## To Process

- Inbox items: [count]
- Orphaned notes: [list]
- Missing connections: [identified]
```

## Gym-Analyse (Fett to Fit)

Führe am Ende der Weekly Synthesis immer auch eine Gym-Wochenanalyse durch:

### Schritt 1 – Session-Dateien der Woche laden

Lese alle Tracking-Dateien der aktuellen Woche aus `01_Projects/Fett to Fit/Tracking/` (Push, Pull, Legs – keine Wochenanalysen). Lese auch `01_Projects/Fett to Fit/Training/PPL Trainingsplan.md`.

### Schritt 2 – Wochenanalyse ausgeben

```
## 🏋️ Gym-Woche W[N]

### Sessions dieser Woche
- Push ([Datum]): [kurze Einschätzung]
- Pull ([Datum]): [kurze Einschätzung]
- Legs ([Datum]): [kurze Einschätzung]

### Progression diese Woche
| Übung | Letzte Woche | Diese Woche | Trend |
|-------|-------------|-------------|-------|
| [Übung] | [kg × Wdh.] | [kg × Wdh.] | 🔼 / ✅ / ⚠️ |

### Stärken der Woche
- [Was gut lief]

### Schwachstellen & Fokus nächste Woche
- [Was zu verbessern ist + konkreter Tipp]

### Vorschläge für W[N+1]
- [Übung]: [spezifischer Tipp]
```

### Schritt 3 – Wochenanalyse-Datei erstellen

Erstelle: `01_Projects/Fett to Fit/Tracking/[DATUM-SONNTAG] - Wochenanalyse W[N].md`

Frontmatter:
```yaml
---
datum: YYYY-MM-DD
tags: [training, wochenanalyse]
woche: N
---
```

Inhalt: vollständige Analyse aus Schritt 2 plus Abschnitt „Nächste Woche" mit konkreten Gewichtszielen je Übung.

## Rauchfrei-Analyse

Führe am Ende der Weekly Synthesis immer auch eine Rauchfrei-Wochenanalyse durch, solange das Projekt aktiv ist.

### Schritt 1 – Fortschritt laden

Lese `01_Projects/Rauchfrei/Fortschritt.md` und `01_Projects/Rauchfrei/Trigger-Analyse.md`.

### Schritt 2 – Analyse ausgeben

```
## 🚭 Rauchfrei-Woche W[N]

### Statistik der Woche
| Datum | Tag # | Geraucht? | Craving-Stärke | Notiz |
|-------|-------|-----------|---------------|-------|
[bestehende Einträge aus der Tabelle übernehmen]

### Auswertung
- Rauchfreie Tage: [X von 7]
- Durchschnittliche Craving-Stärke: [X]
- Schwierigster Tag: [Datum + warum]
- Stärkster Trigger diese Woche: [aus Einträgen ableiten]

### Was gut funktioniert hat
- [konkrete Beobachtung]

### Was schwierig war
- [konkrete Beobachtung + Verbesserungsvorschlag]

### Nächste Woche
- Fokus-Trigger: [der schwierigste Trigger]
- Konkrete Maßnahme: [was ändern/beibehalten]
```

### Schritt 3 – Fortschritt-Datei aktualisieren

Trage die Wochenanalyse in `01_Projects/Rauchfrei/Fortschritt.md` unter `## Wochenanalyse` ein.

Füge danach die nächsten 7 Tage als leere Tabellenzeilen an (Datum, Tag-Nummer fortlaufend, Rest leer).

Prüfe außerdem welche Meilensteine erreicht wurden und setze die entsprechenden Checkboxen auf `[x]`.

## Follow-up Actions

- Archive completed projects
- Clean up inbox
- Update project status
- Plan next week's focus
