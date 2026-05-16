---
title: Claude Skills & Commands
typ: referenz
erstellt: 2026-04-10
aktualisiert: 2026-04-26
tags: [claude, skills, commands, referenz]
version: "0.15.1"
---

# Claude Skills & Commands

Übersicht aller verfügbaren Slash-Commands und Skills in diesem Vault.

> **Hinweis (v0.15.1):** Viele Commands existieren jetzt auch als Skills – d.h. sie werden zusätzlich zum manuellen `/`-Aufruf automatisch von Claude aktiviert, wenn der Kontext passt.

## Commands (Slash-Commands)

Aufruf: `/command-name` in Claude Code

### Persönlicher Workflow

| Command          | Aufruf              | Beschreibung                                       |
| ---------------- | ------------------- | -------------------------------------------------- |
| Daily Review     | `/daily-review`     | Tagesrückblick – auch auto-getriggert              |
| Weekly Synthesis | `/weekly-synthesis` | Wöchentliches Review inkl. Gym & Rauchfrei-Analyse |
| Thinking Partner | `/thinking-partner` | Denkpartner-Modus für komplexe Fragen              |
| Inbox Processor  | `/inbox-processor`  | 00_Inbox leeren und nach PARA verarbeiten          |

### Projekte & Bereiche

| Command | Aufruf | Beschreibung |
|---|---|---|
| Hochzeit Update | `/hochzeit-update` | Checklisten prüfen, offene Tasks, Budget-Check |
| Finanz Review | `/finanz-review` | Monatlicher Finanzcheck: Budget, Vermögen, Sparziele |
| Wochen Metriken | `/wochen-metriken` | Training, Rauchfrei, Gewicht als Wochenübersicht |
| Gym Analyse | `/gym-analyse` | Trainingsanalyse für Fett to Fit |

### Wissensmanagement

| Command | Aufruf | Beschreibung |
|---|---|---|
| Resource Creator | `/resource-creator` | URL oder Thema → atomare Wissensnotiz in 03_Resources |
| Entscheidungs-Journal | `/entscheidungs-journal` | Entscheidung dokumentieren: Optionen, Wahl, Begründung |
| Research Assistant | `/research-assistant` | Recherche-Assistent |
| Add Frontmatter | `/add-frontmatter` | YAML-Frontmatter zu Notizen hinzufügen |

### Projektmanagement

| Command | Aufruf | Beschreibung |
|---|---|---|
| Projekt Abschluss | `/projekt-abschluss` | Projekt reviewen und nach 04_Archive verschieben |
| Google Tasks | `/google-tasks` | Tasks anzeigen, hinzufügen, erledigen |
| Brainstorming | `/brainstorming` | Ideen und Anforderungen vor Umsetzung erkunden |

### Technisch / Vault-Pflege

| Command | Aufruf | Beschreibung |
|---|---|---|
| Create Command | `/create-command` | Neuen Slash-Command erstellen |
| De-AI-ify | `/de-ai-ify` | KI-Jargon entfernen, menschliche Sprache wiederherstellen |
| Download Attachment | `/download-attachment` | Anhang herunterladen |
| Pull Request | `/pull-request` | GitHub Pull Request erstellen |
| Release | `/release` | Version bumpen, Changelog, Commit, Tag, Push |
| Upgrade | `/upgrade` | Claudesidian aktualisieren |
| Install Claudesidian | `/install-claudesidian-command` | Claudesidian Shell-Command installieren |
| Init Bootstrap | `/init-bootstrap` | CLAUDE.md Setup-Wizard |
| Pragmatic Review | `/pragmatic-review` | Code-Review: YAGNI & KISS |

---

## Skills (automatisch geladen)

Skills werden von Claude automatisch aktiviert, wenn der Kontext passt – kein manueller Aufruf nötig.

### Vault & Obsidian

| Skill | Trigger | Beschreibung |
|---|---|---|
| `obsidian-markdown` | Beim Arbeiten mit .md Dateien | Obsidian-Markdown: Wikilinks, Callouts, Frontmatter, Embeds |
| `obsidian-bases` | Bei .base Dateien / Datenbank-Views | Obsidian Bases: Tabellen, Filter, Formeln, Views |
| `json-canvas` | Bei .canvas Dateien | Canvas-Dateien: Nodes, Edges, Gruppen |
| `add-frontmatter` | Bei Frontmatter-Arbeit | YAML-Frontmatter hinzufügen/aktualisieren |
| `download-attachment` | Bei Datei-Downloads | Anhänge herunterladen und organisieren |

### Workflow & Produktivität

| Skill | Trigger | Beschreibung |
|---|---|---|
| `daily-review` | EOD / Tagesrückblick | Tagesreview und Planung für morgen |
| `weekly-synthesis` | Wochenreview-Kontext | Wöchentliche Synthese erstellen |
| `thinking-partner` | Problemlösung / Exploration | Kollaboratives Denken, nicht Lösung vorgeben |
| `inbox-processor` | Inbox-Verarbeitung | 00_Inbox nach PARA organisieren |
| `research-assistant` | Recherche-Anfragen | Themen recherchieren und synthetisieren |

### Entwicklung & Tools

| Skill | Trigger | Beschreibung |
|---|---|---|
| `google-tasks` | Bei Erwähnung von Tasks / Google Tasks | Tasks via `gws` CLI abrufen und verwalten |
| `skill-creator` | Beim Erstellen/Verbessern von Skills | Iterativer Skill-Entwicklungs-Workflow mit Evals |
| `git-worktrees` | Bei isolierter Entwicklung / Branch-Arbeit | Git Worktrees für parallele Entwicklung |
| `systematic-debugging` | Bei Bugs / Fehlern / unerwartetem Verhalten | Debugging: Ursache zuerst, dann Fix |
| `pragmatic-review` | Code/Text-Review | YAGNI & KISS Prinzipien |
| `de-ai-ify` | KI-Jargon erkannt | KI-Sprache entfernen, menschliche Stimme wiederherstellen |
| `pull-request` | PR-Erstellung | Branch, Commit, Push, PR öffnen |
| `release` | Release-Workflow | Version, Changelog, Tag, Push |
| `upgrade` | Claudesidian-Update | Intelligentes Upgrade mit Customization-Erhalt |
| `init-bootstrap` | Neues Vault-Setup | CLAUDE.md Setup-Wizard |
| `install-claudesidian-command` | Shell-Setup | Claudesidian als Shell-Command installieren |

---

## Schnellreferenz

```
# Tägliche Nutzung
/daily-review          Tagesrückblick
/google-tasks          Aufgaben checken

# Wöchentlich (Sonntag)
/weekly-synthesis      Wochenreview
/wochen-metriken       Metriken zusammenfassen

# Monatlich
/finanz-review         Finanzen prüfen

# Bei Bedarf
/hochzeit-update       Hochzeitsplanung
/entscheidungs-journal Entscheidung dokumentieren
/resource-creator      Wissen festhalten
/projekt-abschluss     Projekt abschließen
```
