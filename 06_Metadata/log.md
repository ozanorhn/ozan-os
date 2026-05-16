# Log

> Append-only Aktivitäts-Chronik. Niemals löschen.
> Format: `## [YYYY-MM-DD] type | titel`
> Types: `init` · `ingest` · `query` · `debrief` · `lint`
> Schnellzugriff: `grep "^## \[" 06_Metadata/log.md | tail -10`

---

## [2026-05-16] init | Karpathy Wiki-Architektur eingeführt

Basierend auf Andrej Karpathys LLM-Wiki-Pattern. Drei Kernprinzipien:
1. **Persistent kumulieren** statt jede Session kalt starten
2. **LLM schreibt wiki** (index.md, Resource-Seiten) – Ozan kuratiert Quellen + fragt
3. **Täglicher Loop:** `/briefing` (Morgen) + `/debrief` (Abend) + `/ingest` (Quellen)

Neue Infrastruktur-Dateien:
- `03_Resources/Wiki/index.md` – Master-Katalog aller Wissensseiten
- `06_Metadata/log.md` – diese Datei

Neue Commands: `/briefing`, `/debrief`, `/ingest`

## [2026-05-16] debrief | System-Reset-Tag

Google Tasks (26 Tasks) + Google Kalender (208 Events) komplett geleert. Fresh Start.
CLAUDE.md erstellt – Vault vollständig mit Claude dokumentiert.
Vault aufgeräumt: Frontmatter, Wikilinks, Vault Übersicht personalisiert.

Nächste Prioritäten:
- Rauchfrei Anker 4: Geldbinde-Regel mit Sedef (morgen, 17.05.)
- Rauchfrei Visualization starten (18.05.)
- Riester anrufen: 0221-3395-7007
- Verlobungsringe kaufen
