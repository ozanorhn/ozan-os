# Ingest

Nimmt eine URL oder ein Thema, liest die Quelle, integriert sie ins Wiki und aktualisiert index.md + log.md.

## Aufruf

```
/ingest https://example.com/article
/ingest "Buch: Deep Work - Cal Newport"
/ingest                               ← ohne Argument: fragt nach der Quelle
```

## Ablauf

### 1. Quelle bestimmen
- Wenn `$ARGUMENTS` leer: Frage "Was möchtest du einlesen? (URL, Buch, Artikel, Gedanke)"
- Wenn URL: `WebFetch` aufrufen und Inhalt laden
- Wenn Buch/Thema: mit vorhandenem Wissen + ggf. `WebSearch` arbeiten

### 2. Key Takeaways besprechen (optional)
Kurze Zusammenfassung der wichtigsten Punkte ausgeben und fragen:
"Soll ich noch etwas besonders betonen oder weglassen?"

### 3. Resource-Seite erstellen/aktualisieren
Dateiname nach Vault-Konvention:
- Bücher: `03_Resources/Bücher/[Buchtitel] - [Autor].md`
- Artikel/Web: `03_Resources/Ressource - [Thema] - [Quelle].md`
- Gedanken/Notizen: `03_Resources/Ressource - [Thema].md`

Frontmatter:
```yaml
---
title: [Titel]
type: ressource
quelle: [URL oder Buchname]
autor: [Autor falls bekannt]
ingest-datum: YYYY-MM-DD
tags: [relevante Tags]
---
```

Inhalt: Zusammenfassung, Key Takeaways, Verbindungen zu anderen Seiten im Vault.

### 4. Wiki Index aktualisieren
In `03_Resources/Wiki/index.md` neue Zeile in passende Tabelle eintragen:
```
| [[Seitenname]] | Kurzbeschreibung | #tags | YYYY-MM |
```

### 5. Verbindungen prüfen
Bestehende Seiten durchsuchen, die das Thema berühren:
- Wenn eine bestehende Resource-Seite aktualisiert werden sollte → Vorschlagen, erst fragen
- Wikilinks zur neuen Seite in verwandten Projekt-Dateien ergänzen (vorschlagen)

### 6. Log-Eintrag schreiben
In `06_Metadata/log.md` anhängen:
```markdown
## [YYYY-MM-DD] ingest | [Titel der Quelle]

Quelle: [URL oder Buchname]
Key Takeaways: [2–3 Sätze]
Verbunden mit: [[Seite1]], [[Seite2]]
```

### 7. Abschluss
Kurze Bestätigung: "Eingelesen: [[Seitenname]] · index.md aktualisiert · log.md aktualisiert"

---

## Hinweise

- Bestehende Seiten ergänzen statt Duplikate erstellen (erst prüfen ob Seite existiert)
- Wikilinks großzügig setzen – Querverbindungen sind der Wert des Wikis
- Keine Quelle ohne log.md-Eintrag abschließen
