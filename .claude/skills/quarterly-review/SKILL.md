---
name: quarterly-review
description: Quartalsreview durchführen. 90-Tage-Rückblick mit Fokus auf Areas (Gesundheit, Finanzen, Karriere) statt Projekt-Tagesgeschäft. Use when user asks for quarterly review, Q1/Q2/Q3/Q4 review, 90-day review, Quartalsbilanz, Quartals-Rückblick, oder als regelmäßige Routine alle 3 Monate.
---

# Quartals-Review

Tiefer als Weekly Synthesis. 90 Tage zurück. Fokus auf **Areas** (Verantwortungsbereiche) und Identität-Drift, nicht auf Projekt-Tagesgeschäft.

> Komplementär zu `/weekly-synthesis`. Weekly schaut auf die Woche. Quarterly schaut auf das Quartal und die Areas dahinter.

## Wann ausführen

- Ende März (Q1), Ende Juni (Q2), Ende September (Q3), Ende Dezember (Q4)
- Empfohlen: am letzten Wochenende des Quartals, vor Weekly Synthesis dieser Woche
- Allokation: 60-90 Minuten, nicht in den Tagesablauf reinquetschen

## Schritt 1 — Datenbasis sammeln

1. **Welche Quartal?** Berechnen aus heutigem Datum oder explizit fragen. Format: "Q1 2026", "Q2 2026", etc. Zeitfenster: erste Tag des Quartals bis heute.
2. **Vault-Statistiken für das Quartal:**
   - Anzahl neuer Notes
   - Anzahl modifizierter Notes
   - Welche Areas wurden überhaupt angefasst (Mod-Time von Files in `02_Areas/*`)
3. **Daily-Notes scannen:** Sample 8-12 Daily-Notes über das Quartal verteilt, suche nach wiederkehrenden Themen, Beschwerden, Wins
4. **Decision-Files lesen:** Alle Files in `01_Projects/*/Entscheidungen/`, `02_Areas/*/Entscheidungen/`, `03_Resources/Entscheidungen/` mit Datum im Quartal. Welche Entscheidungen sind Review-fällig?
5. **Cookie Jar prüfen:** Neue Einträge in `02_Areas/Gesundheit/Cookie Jar - Meine Siege.md` seit Quartalsbeginn

## Schritt 2 — Per-Area Reflexion

Für **jeden** Area-Ordner in `02_Areas/` (Gesundheit, Finanzen, Karriere & Entwicklung, etc.):

1. Lies die Hauptdatei des Bereichs
2. Stelle dem Nutzer diese 4 Fragen:
   - **Status:** Wo steht dieser Bereich heute vs. Quartalsbeginn? (besser/gleich/schlechter)
   - **Was hat funktioniert?** Konkret, mit Datum/Beispiel
   - **Was hat NICHT funktioniert?** Konkret, mit Datum/Beispiel
   - **Was muss im nächsten Quartal anders sein?**
3. Antworten direkt unter den Fragen sammeln, nicht zusammenfassen

## Schritt 3 — Entscheidungs-Review

Für jede getroffene Entscheidung im Quartal mit Review-Datum innerhalb dieses Quartals:

1. Datei öffnen
2. Sektion `## Rückblick` ausfüllen:
   - **Datum:** heute
   - **Ergebnis:** Was ist tatsächlich passiert vs. erwartet?
   - **Lernpunkt:** Was würdest du heute anders entscheiden? Oder gleich?
3. Wenn Lernpunkt durabel ist (gilt über die einzelne Entscheidung hinaus): Eintrag in `03_Resources/Wiki/Eigene Lehren.md` vorschlagen

## Schritt 4 — Identitäts-Check

3 stille Fragen, die der Nutzer in einem Block beantwortet (keine Tabelle, keine Bullets):

1. **Bin ich Ende dieses Quartals näher an der Person die ich sein will als Anfang?** Konkret, nicht "ja klar".
2. **Welches Verhalten habe ich dieses Quartal etabliert, das mich vor 3 Monaten überrascht hätte?**
3. **Welches Verhalten habe ich dieses Quartal verloren, das mir wichtig war?**

## Schritt 5 — Nächstes Quartal planen

Maximal **3 Fokus-Themen** für das kommende Quartal. Mehr ist nicht echt. Pro Fokus-Thema:

- 1-Satz-Ziel (überprüfbar, mit Zahl wenn möglich)
- Wichtigster nächster Schritt diese Woche
- Was du explizit NICHT machst, um Platz zu schaffen

## Schritt 6 — Ablage

Erstelle die Review-Datei:

**Pfad:** `02_Areas/Reviews/Q{N} {YYYY} - Quartalsreview.md` (Ordner `Reviews/` anlegen falls noch nicht da)

**Format:**

```markdown
---
typ: quarterly-review
quartal: Q{N} {YYYY}
zeitraum: YYYY-MM-DD bis YYYY-MM-DD
tags: [review, quarterly]
erstellt: YYYY-MM-DD
---

# Q{N} {YYYY} — Quartalsreview

## Datenbasis
- Notes erstellt: {N}
- Notes modifiziert: {N}
- Aktive Areas: [Liste]
- Entscheidungen getroffen: {N}
- Cookie Jar Einträge: {N}

## Per-Area Reflexion

### {Area 1}
- Status:
- Was funktioniert hat:
- Was nicht funktioniert hat:
- Im nächsten Quartal anders:

### {Area 2}
...

## Entscheidungs-Reviews

- [[YYYY-MM-DD - Entscheidung]] — Ergebnis + Lernpunkt
- ...

## Identitäts-Check

[Freitext-Antworten zu den 3 Fragen]

## Nächstes Quartal

### Fokus 1: {Name}
- Ziel:
- Erste Schritte:
- Explizit nicht:

### Fokus 2: ...

### Fokus 3: ...

## Vorschläge für Eigene Lehren

- {Lernpunkt 1, der in 03_Resources/Wiki/Eigene Lehren.md gehört}
- ...
```

## Schritt 7 — Hand-off

Sage dem Nutzer:
1. Pfad der Review-Datei
2. Wie viele Decision-Files Rückblick bekommen haben
3. Wenn Vorschläge für Eigene Lehren existieren: anbieten direkt nach `03_Resources/Wiki/Eigene Lehren.md` zu schreiben

## Hard Rules

- **Nicht zusammenfassen.** Antworten des Nutzers direkt übernehmen, nicht paraphrasieren.
- **Nicht über 3 Fokus-Themen.** Wenn der Nutzer 5 vorschlägt: zurückspielen "welche 3 davon sind real, welche 2 sind Wunsch?"
- **Keine generischen Tipps.** Nur auf Basis dessen was tatsächlich in den Daily-Notes/Entscheidungen steht.
- **Niemals em-Dashes** (User-Regel aus `CLAUDE.md`).
