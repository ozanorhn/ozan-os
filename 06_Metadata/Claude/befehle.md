# Nützliche Befehle

## Vault-Pflege

```bash
pnpm vault:stats           # Vault-Statistiken
pnpm attachments:list      # Nicht verarbeitete Anhänge
pnpm attachments:orphans   # Verwaiste Dateien finden
```

## Claude-Workflows

```bash
claude run weekly-synthesis    # Wöchentliches Review
claude run thinking-partner    # Denkpartner-Modus
claude run daily-review        # Tagesrückblick
```

## Google Tasks Integration

Tasks werden über das `gws` CLI (`~/.cargo/bin/gws`) abgerufen.

- **Skill:** `.claude/skills/google-tasks/` – auto-triggered bei Task-Erwähnungen
- **Command:** `/google-tasks` – expliziter Aufruf
- **Hinweis:** `gws` schreibt „Using keyring backend: keyring" in stdout → immer `| grep -v keyring` anhängen

```bash
python3 .claude/skills/google-tasks/scripts/fetch-tasks.py   # Alle Tasks anzeigen
gws tasks tasklists list | grep -v keyring                   # Task-Listen auflisten
```

### Task-Listen

- **Meine Aufgaben** – allgemeine Todos
- **Hochzeit** – Hochzeitsplanung
- **Immobilie** – Immobilienprojekt
- **Karriere & Netzwerk** – berufliche Entwicklung
