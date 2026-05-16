---
name: google-tasks
description: 'Google Tasks anzeigen, hinzufügen oder erledigen'
argument-hint: '[add "Aufgabe" | done | daily]'
---

# Google Tasks

Verwalte Google Tasks über die `gws` CLI.

## Modi

- **Kein Argument** → alle offenen Tasks anzeigen, kategorisiert nach Fälligkeit
- **`add "Aufgabe"`** → neue Task hinzufügen (fragt nach Liste und Fälligkeit)
- **`done`** → erledigte Tasks markieren (zeigt Liste zum Auswählen)
- **`daily`** → Tasks als Section in die heutige Daily Note einfügen

## Workflow

### 1. Tasks abrufen

```bash
python3 .claude/skills/google-tasks/scripts/fetch-tasks.py
```

Ausgabe zeigt: ⚠️ überfällig / 📅 heute / demnächst / kein Datum

### 2. Anzeigen

Alle Tasks übersichtlich ausgeben. Überfällige Tasks zuerst als Warning-Callout.

### 3. Interaktion

Je nach Nutzereinagbe:

**Task hinzufügen:**
```bash
gws tasks tasks insert \
  --params '{"tasklist": "<ID>"}' \
  --json '{"title": "<TITEL>", "due": "<ISO-DATUM>"}' | grep -v keyring
```

**Task erledigen:**
```bash
gws tasks tasks patch \
  --params '{"tasklist": "<LIST_ID>", "task": "<TASK_ID>"}' \
  --json '{"status": "completed"}' | grep -v keyring
```

**In Daily Note einfügen:**
Fetch-Script ausführen und Ausgabe als `## Google Tasks` in `07_Daily/YYYY-MM-DD.md` einfügen. Datei wenn nötig anlegen.

### 4. IDs ermitteln

Task-Listen IDs sind im Skill dokumentiert. Immer via `tasklists list` verifizieren wenn unsicher:

```bash
gws tasks tasklists list | grep -v keyring
```

## Hinweis

`gws` schreibt "Using keyring backend: keyring" in stdout → immer `| grep -v keyring` anhängen oder fetch-script verwenden.
