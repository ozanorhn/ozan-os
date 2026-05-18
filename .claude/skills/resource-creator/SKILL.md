---
name: resource-creator
description: Atomare Wissensnotiz in 03_Resources erstellen – aus URL, Thema oder Buchnotizen. Use when the user provides a URL to save, wants to create a knowledge note, asks to capture a resource, wants to add book notes, or says 'speichere das', 'erstelle eine Ressource', 'mach eine Notiz zu'.
---

# Resource Creator

Erstelle eine strukturierte, atomare Wissensnotiz in `03_Resources/`.

## Ablauf

### Input-Typen

**A) URL**
1. Hole den Inhalt der URL (WebFetch)
2. Extrahiere: Titel, Kernaussagen, wichtige Zitate, Relevanz für Ozan
3. Erstelle Notiz

**B) Thema / freier Text**
1. Strukturiere das gegebene Wissen
2. Verknüpfe mit bestehenden Vault-Notizen via [[WikiLink]]
3. Erstelle Notiz

**C) Buchnotizen**
1. Extrahiere Key Takeaways, Zitate, anwendbare Konzepte
2. Format: `03_Resources/Ressource - [Buchtitel] - [Autor].md`

## Namenskonvention

```
03_Resources/Ressource - [Thema] - [Quelle/Autor].md
```

Beispiele:
- `Ressource - Progressive Overload - Stronger by Science.md`
- `Ressource - ETF-Strategie - Finanzfluss.md`
- `Ressource - Cant Hurt Me - David Goggins.md`

## Output Format

```markdown
---
title: [Titel]
type: resource
quelle: [URL oder Autor]
erstellt: [YYYY-MM-DD]
aktualisiert: [YYYY-MM-DD]
tags: [relevante Tags]
---

# [Titel]

## Was ist das?
[1-2 Sätze: Worum geht es?]

## Kernaussagen
- [Kernaussage 1]
- [Kernaussage 2]
- [Kernaussage 3]

## Relevanz für mich
[Warum ist das für Ozan relevant? Verknüpfung zu Projekten/Zielen]

## Anwendbare Konzepte
- [Konkreter Ansatz 1]
- [Konkreter Ansatz 2]

## Zitate / Highlights
> "[Wichtiges Zitat]"

## Verwandte Notizen
- [[WikiLink zu verwandter Notiz]]
```

## Regeln
- Notiz ist atomar: ein Thema, eine Quelle
- Immer [[WikiLinks]] zu verwandten Vault-Notizen setzen
- Nach Erstellung: Pfad der neuen Notiz bestätigen
- Wiki-Index updaten: `03_Resources/Wiki/index.md` prüfen ob Kategorie existiert
