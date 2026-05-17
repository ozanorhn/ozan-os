---
titel: Dashboard
tags: [dashboard]
---

# Dashboard

## System-Reset 16.05.2026

> [!note] Clean Slate – 16.05.2026
> Google Tasks + Kalender geleert. CLAUDE.md erstellt. Fresh Start.

## Inbox
```dataview
LIST
FROM "00_Inbox"
SORT file.mtime DESC
```

## Offene Tasks – Alle Projekte
```dataview
TASK
FROM "01_Projects"
WHERE !completed
SORT file.name ASC
```

## Aktive Projekte
```dataview
TABLE status, aktualisiert
FROM "01_Projects"
WHERE type = "moc" AND contains(file.path, "01_Projects")
SORT file.folder ASC
```

## Kürzlich bearbeitet
```dataview
LIST
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
AND !contains(file.path, "06_Metadata")
AND !contains(file.path, "05_Attachments")
SORT file.mtime DESC
LIMIT 10
```
