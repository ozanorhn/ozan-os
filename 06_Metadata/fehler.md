---
title: Fehler & Verbesserungen
type: system
aktualisiert: 2026-05-18
---

# Fehler & Verbesserungen

Claude loggt hier Probleme, die er beim Arbeiten entdeckt. Offene Einträge werden beim nächsten Session-Start angezeigt und automatisch behoben wenn möglich.

**Format:** `- [ ] [YYYY-MM-DD] Kategorie: Beschreibung`
**Behoben:** Checkbox auf `[x]` setzen + Datum ergänzen

---

## Offen

- [x] [2026-05-18] Vault: 00_Inbox Verzeichnis fehlte – angelegt
- [x] [2026-05-18] Skills: /gym-analyse, /hochzeit-update, /resource-creator fehlten – erstellt
- [x] [2026-05-18] CLAUDE.md: gws Pfad war ~/.cargo/bin/gws, korrekt ist /usr/local/bin/gws – korrigiert
- [x] [2026-05-18] CLAUDE.md: Wochenplan KW 20 Referenz veraltet – entfernt
- [x] [2026-05-18] tgbot: requirements.txt fehlte – erstellt
- [x] [2026-05-18] Telegram: MCP-Plugin + bot.py Konflikt durch doppeltes Polling – systemd-Service als alleinige Instanz konfiguriert

## Behoben

_(werden nach oben verschoben wenn erledigt)_

---

## Wie Claude dieses File nutzt

1. **Entdeckt Claude ein Problem** → trägt es als `- [ ]` ein
2. **Beim Session-Start** → SessionStart-Hook zeigt offene Einträge an
3. **Beim Beheben** → Checkbox auf `[x]`, Datum ergänzen
4. **Monatliches Cleanup** → behobene Einträge archivieren oder löschen
