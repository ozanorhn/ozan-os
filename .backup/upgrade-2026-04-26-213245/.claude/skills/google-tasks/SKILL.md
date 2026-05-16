---
name: google-tasks
description: >
  Google Tasks integration via gws CLI. Use when the user mentions Google Tasks,
  asks to see their tasks, wants to add/complete tasks, or when running a daily
  review that should include task status. Requires `gws` binary installed at
  ~/.cargo/bin/gws.
---

# Google Tasks Skill

Manage Google Tasks using the `gws` CLI.

## Prerequisites

- `gws` binary: `~/.cargo/bin/gws` (already installed)
- Auth: handled automatically via keyring

## Key Quirk

`gws` prints `Using keyring backend: keyring` to **stdout** before the JSON.
Always filter it:

```bash
gws tasks tasklists list | grep -v "keyring" | python3 -c "import sys,json; print(json.dumps(json.load(sys.stdin), indent=2))"
```

Or use the fetch script (preferred):

```bash
python3 .claude/skills/google-tasks/scripts/fetch-tasks.py
```

## Fetch Script

**`scripts/fetch-tasks.py`** — fetches all lists and tasks, outputs Markdown.

```bash
python3 .claude/skills/google-tasks/scripts/fetch-tasks.py            # Markdown output
python3 .claude/skills/google-tasks/scripts/fetch-tasks.py --json     # raw JSON
python3 .claude/skills/google-tasks/scripts/fetch-tasks.py --overdue  # overdue summary only
```

Output categorizes tasks as: **overdue** ⚠️ / **today** 📅 / **upcoming** / **no date**

## Common gws Commands

```bash
# List all task lists (get IDs)
gws tasks tasklists list | grep -v keyring

# List tasks in a list
gws tasks tasks list --params '{"tasklist": "<LIST_ID>"}'  | grep -v keyring

# Mark task complete
gws tasks tasks patch \
  --params '{"tasklist": "<LIST_ID>", "task": "<TASK_ID>"}' \
  --json '{"status": "completed"}' | grep -v keyring

# Add new task
gws tasks tasks insert \
  --params '{"tasklist": "<LIST_ID>"}' \
  --json '{"title": "Task title", "due": "2026-04-05T00:00:00.000Z"}' | grep -v keyring

# Add task with notes
gws tasks tasks insert \
  --params '{"tasklist": "<LIST_ID>"}' \
  --json '{"title": "Task title", "notes": "Notiz hier"}' | grep -v keyring
```

## Known Task List IDs (Ozan)

| Liste | ID |
|-------|-----|
| Meine Aufgaben | `MDExNDAyMDc0NjA5MzQxMDcyNTc6MDow` |
| Hochzeit | `bzZBR1ljWFp4djN6WVRwTA` |
| Immobilie | `b29fSmVicFpCbHRRTjFHWg` |

> IDs können sich ändern – immer via `tasklists list` verifizieren.

## Integration in Daily Review

Nach `/daily-review` die Tasks ergänzen:

```bash
python3 .claude/skills/google-tasks/scripts/fetch-tasks.py
```

Ausgabe als `## Google Tasks` Section in die Daily Note (`07_Daily/YYYY-MM-DD.md`) einfügen.

## Workflow: Task erledigen

1. Task-ID aus `tasks list` holen
2. `tasks patch` mit `{"status": "completed"}` aufrufen
3. In Daily Note als `✓` markieren
