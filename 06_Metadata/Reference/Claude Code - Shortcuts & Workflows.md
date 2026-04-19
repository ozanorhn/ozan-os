---
title: Claude Code – Shortcuts & Workflows
created: 2026-04-19
tags: [reference, claude-code, shortcuts]
status: aktiv
---

# Claude Code – Shortcuts & Workflows

Persönlich kuratierte Referenz für Ozans Second-Brain-Workflow. Nur was im Vault-Kontext relevant ist. Copy-paste-ready.

Quellen:
- https://code.claude.com/docs/en/interactive-mode
- https://code.claude.com/docs/en/common-workflows

---

## Die wichtigsten Tastenkürzel

| Shortcut | Funktion |
|---|---|
| `Shift+Tab` | Permission-Modi durchschalten (Default → Auto-Accept → **Plan Mode**) |
| `Esc Esc` | Gespräch/Änderungen zu früherem Punkt zurückspulen (Rewind) |
| `Ctrl+R` | Rückwärts durch Prompt-History suchen |
| `Ctrl+T` | Task-Liste ein-/ausblenden |
| `Ctrl+O` | Transcript-Viewer öffnen (zeigt Tool-Calls + Thinking) |
| `Ctrl+G` | Aktuelle Prompt-Eingabe im Texteditor öffnen |
| `Ctrl+B` | Bash-Command in den Hintergrund schieben |
| `Ctrl+L` | Eingabe löschen + Terminal neu zeichnen |
| `Ctrl+D` | Claude Code beenden |
| `Option+T` (Mac) | Extended Thinking an/aus |
| `Option+P` (Mac) | Modell wechseln ohne Prompt zu verlieren |
| `Option+O` (Mac) | Fast Mode an/aus |
| Hold `Space` | Push-to-Talk Diktat (falls Voice aktiviert) |
| `Cmd+V` | Bild aus Clipboard einfügen |

---

## Input-Präfixe

| Präfix | Bedeutung | Beispiel |
|---|---|---|
| `/` | Slash-Command oder Skill | `/weekly-synthesis` |
| `!` | Bash-Modus (direkt ausführen) | `!git status` |
| `@` | Datei/Ordner einbinden | `@02_Areas/Finanzen/` |

---

## Plan Mode (wichtig für Vault-Änderungen)

**Was:** Claude analysiert nur lesend und schlägt einen Plan vor, bevor etwas geändert wird.

**Wann nutzen:**
- Vault-Reorganisation
- Projekt-Archivierung
- Größere Umstrukturierung in `02_Areas/`
- Wenn du unsicher bist, was Claude tun wird

**Aktivieren:**
- Während Session: `Shift+Tab` zweimal drücken
- Beim Start: `claude --permission-mode plan`
- Als Default setzen in `.claude/settings.json`:

```json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

**Tipp:** Im Plan Mode `Ctrl+G` drücken, um den Plan im Editor direkt zu bearbeiten, bevor Claude weitermacht.

---

## Copy-Paste Prompts

### Sessions benennen (direkt beim Start)

```bash
claude -n hochzeit-research
claude -n fit-woche-8
claude -n finanz-review-april
claude -n rauchfrei-vorbereitung
```

### Session fortsetzen

```bash
claude --continue                    # letzte Session in diesem Ordner
claude --resume                      # Picker öffnen
claude --resume hochzeit-research    # direkt per Name
```

### Session umbenennen (innerhalb)

```
/rename hochzeit-gaesteliste
```

### Plan Mode starten

```bash
claude --permission-mode plan
```

### Recap auf Abruf

```
/recap
```

### Nebenfrage ohne Kontext-Müll

```
/btw wie hieß nochmal die Datei mit den Supplements?
```

---

## `@`-Referenzen (Vault-Dateien einbinden)

Statt Claude erst lesen zu lassen, direkt einbinden:

```
Fass @02_Areas/Finanzen/Vermögensübersicht.md zusammen
```

```
Was steht in @01_Projects/Hochzeit/Checklisten/ drin?
```

```
Vergleiche @07_Daily/Wochenanalysen/2026-KW16.md mit der Vorwoche
```

```
Update @02_Areas/Gesundheit/PPL-Plan.md basierend auf @01_Projects/Fett to Fit/Tracking/
```

Mehrere Dateien gleichzeitig:

```
Erstelle eine Übersicht aus @datei1.md und @datei2.md
```

---

## `ultrathink` – Tieferes Nachdenken

Wenn `ultrathink` im Prompt steht, denkt Claude länger nach. Nutzen für:

```
ultrathink: Lohnt sich die Berufsunfähigkeitsversicherung ab April 2027, 
gegeben meine Fixkosten in @02_Areas/Finanzen/ und das Einkommen?
```

```
ultrathink: Welche Reihenfolge macht Sinn – erst Rauchfrei (27.04.) 
oder erst Gewicht runter? Kontext: @01_Projects/Rauchfrei/ und @01_Projects/Fett to Fit/
```

```
ultrathink: Wie priorisiere ich die offenen Hochzeits-Tasks bis zur 
Verlobung am 19.09.2026? @01_Projects/Hochzeit/Checklisten/
```

---

## Bilder nutzen

Drei Wege:
1. **Drag & Drop** ins Claude-Code-Fenster
2. **Copy + `Ctrl+V`** (nicht `Cmd+V`!)
3. **Pfad angeben**: `Analysiere dieses Bild: /path/to/screenshot.png`

Beispiel-Prompts:

```
Das ist ein Screenshot meiner Trainings-App. Übertrage die Werte in 
@01_Projects/Fett to Fit/Tracking/2026-04-19.md
```

```
Rechnung als Bild angehängt – extrahiere Betrag und Datum für die Finanzübersicht
```

---

## Bash-Modus (`!`)

Direkt ausführen ohne Claude zu fragen:

```
!git pull
!git status
!git add . && git commit -m "Weekly Sync KW17"
!pnpm vault:stats
!pnpm attachments:orphans
```

Output landet im Kontext, Claude kann darauf antworten.

---

## Nützliche Slash-Commands (deine eigenen)

Aus deinem Vault (siehe `.claude/commands/` und `.claude/skills/`):

```
/weekly-synthesis        # Sonntags-Review
/daily-review            # Tagesrückblick
/thinking-partner        # Denkpartner-Modus
/inbox-processor         # Inbox leeren
/gym-analyse             # Training auswerten
/wochen-metriken         # KPIs aggregieren
/finanz-review           # Monatliches Finanz-Review
/hochzeit-update         # Hochzeits-Status
/google-tasks            # Tasks abrufen
/entscheidungs-journal   # Entscheidung dokumentieren
/projekt-abschluss       # Projekt archivieren
/resource-creator        # Wissensnotiz in 03_Resources
/pragmatic-review        # Code/Text kritisch prüfen
/de-ai-ify               # AI-Sprache rauseditieren
```

---

## Scheduled Tasks / Automatisierung

Drei Optionen für wiederkehrende Tasks:

| Option | Läuft auf | Gut für |
|---|---|---|
| **Routines** | Anthropic-Infra (auch wenn Mac aus) | Tasks, die immer laufen sollen |
| **Desktop Scheduled Tasks** | Lokal | Tasks mit Dateizugriff (**für dich besser**) |
| **`/loop`** | Aktuelle Session | Quick-Polling während Session offen ist |

Konfiguration: https://claude.ai/code/routines

Ideen für Automatisierung:
- Sonntag 10 Uhr → `/weekly-synthesis` vorbereiten
- Montag früh → Inbox-Check-Reminder
- Monatsende → `/finanz-review` Entwurf

---

## Extended Thinking / Verbose Mode

- `Ctrl+O` → Transcript-Viewer, zeigt Claudes internes Denken
- `Option+T` → Thinking-Modus an/aus für diese Session
- Default: aktiv (adaptiv bei Opus 4.7)

---

## Rewind – der Rückgängig-Knopf

`Esc Esc` = Gespräch oder Dateiänderungen zu einem früheren Punkt zurückspulen.

Nutzen wenn:
- Claude was kaputt gemacht hat im Vault
- Du eine falsche Richtung eingeschlagen hast
- Du den Kontext zurücksetzen willst ohne `/clear`

---

## Was ignoriert werden kann

Für Ozans Vault-Use-Case irrelevant:
- PR-Workflow (`gh pr create`)
- Subagents für Code-Review
- Git Worktrees (`--worktree`)
- `--output-format json` / Unix-Piping
- Vim-Editor-Modus
- CI/CD-Linter-Integration

---

## Empfohlene Defaults für Ozan

In `.claude/settings.json`:

```json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

→ Schützt vor versehentlichen Vault-Änderungen. Bei kleinen Edits einfach `Shift+Tab` drücken.

---

## Quick-Reference Spickzettel

```
Shift+Tab    = Plan Mode
Esc Esc      = Rewind
Ctrl+O       = Thinking sehen
Ctrl+R       = Prompt-History
Ctrl+T       = Tasks ein/aus
Ctrl+G       = Im Editor öffnen
Cmd+V        = Bild einfügen
Hold Space   = Diktat

/            = Command/Skill
!            = Bash direkt
@            = Datei/Ordner

/btw X       = Nebenfrage ohne Kontext-Belastung
/recap       = Session-Zusammenfassung
/rename X    = Session benennen
ultrathink   = tiefer nachdenken

claude -n X           = Session mit Name starten
claude --continue     = letzte Session weiter
claude --resume X     = per Name fortsetzen
claude --permission-mode plan  = Plan Mode beim Start
```
