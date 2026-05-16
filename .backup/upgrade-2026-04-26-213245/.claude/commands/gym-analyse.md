# Gym Analyse

Analysiert die letzten Gym-Sessions und erstellt eine optimierte Tracking-Datei für die nächste Session.

## Schritt 1 – Tracking-Dateien laden

Lese alle Dateien in `01_Projects/Fett to Fit/Tracking/` **und** `01_Projects/Fett to Fit/Tracking/Vergangen/`. Filtere Wochenanalysen heraus (Dateiname enthält „Wochenanalyse"). Sortiere alle Dateien nach Datum im Dateinamen (Format: `YYYY-MM-DD`).

Lese auch `01_Projects/Fett to Fit/Training/PPL Trainingsplan.md` für die Ziel-Wdh., Satzanzahl und Pausenzeiten.

## Schritt 2 – Letzte Session & nächste Session bestimmen

- **Letzte Session:** Datei mit dem höchsten Datum
- **Typ der letzten Session:** aus Frontmatter-Feld `einheit` (Push / Pull / Legs)
- **Zyklus:** Push → Pull → Legs → Push → ...
- **Nächste Session:** nächster Typ im Zyklus
- **Woche der nächsten Session:** gleiche Wochennummer, außer der Zyklus fängt neu an (dann +1)
- **Datum der nächsten Session:** +7 Tage vom letzten Session-Datum

## Schritt 3 – Trend-Analyse über letzte 4 Sessions desselben Typs

Lese die letzten bis zu 4 Dateien mit demselben `einheit`-Typ wie die letzte Session (z.B. alle Pull-Days sortiert nach Datum).

Analysiere pro Übung über alle verfügbaren Sessions:

### 3a – Ermüdungsmuster erkennen
Bricht ein bestimmter Satz (z.B. immer Satz 3 oder 4) regelmäßig ein (Wdh. < Minimum)?
→ Tipp: "Heute X Min. Pause vor Satz [N] einplanen" oder "Satz [N] weglassen"

### 3b – Progression erkennen
Hat der Nutzer in den letzten Sessions bei einer Übung konstant alle Sätze im Maximalbereich der Wdh. geschafft?
→ Tipp: "Heute +2,5 kg versuchen"

### 3c – Volumen-/Reihenfolge-Problem erkennen
Bricht eine Muskelgruppe (z.B. Bizeps) regelmäßig am Ende der Session ein, obwohl sie früher im Training gut funktioniert?
→ Tipp: "[Übung] heute früher einplanen" oder "3 statt 4 Sätze heute"

### 3d – Inkonstanz bei Gewichten erkennen
Wechselt der Nutzer das Gewicht zwischen Sätzen ohne erkennbare Progression?
→ Tipp: "Gewicht konstant halten bei X kg – erst steigern wenn alle Sätze im Ziel"

### Tipp-Priorisierung pro Übung (nur einen Tipp wählen):
1. Ermüdungsmuster → Pause-Tipp hat Vorrang
2. Progression bereit → Steigerungs-Tipp
3. Inkonstanz → Konstanz-Tipp
4. Volumen/Reihenfolge → struktureller Tipp

## Schritt 3.5 – Analyse in die abgeschlossene Session-Datei schreiben

Schreibe die Analyse am Ende der **letzten Session-Datei** (die gerade abgeschlossene, nicht die neue). Ersetze den bestehenden „Nächstes Mal steigern?" Abschnitt mit folgendem Block:

```markdown
## Nächstes Mal steigern?

- [ ] [Übung]: [Konkrete Empfehlung, z.B. "Gewicht erhöhen auf 72,5 kg wenn alle Sätze 12 Wdh."]

---

## Analyse

| Übung | Status | Tipp für nächstes Mal |
| ----- | ------ | --------------------- |
| [Übungsname] | [✅/⚠️/🔼/❌] | [Konkreter Tipp] |
...
```

- Nur Übungen in „Nächstes Mal steigern?" eintragen, bei denen Steigerung realistisch ist
- Jede trainierte Übung in der Analyse-Tabelle aufführen

## Schritt 4 – Kurze Chat-Ausgabe

Gib genau 3 Bullet-Points aus – die wichtigsten Erkenntnisse aus der Trend-Analyse:

```
**Deine 3 wichtigsten Erkenntnisse für heute:**

- [Übung]: [Konkrete Beobachtung + Empfehlung]
- [Übung]: [Konkrete Beobachtung + Empfehlung]
- [Übung]: [Konkrete Beobachtung + Empfehlung]
```

Danach einzeilig: Dateiname der neu erstellten Tracking-Datei als Markdown-Link.

**Keine lange Analyse im Chat – alles andere steht in der Datei.**

## Schritt 5 – Neue Tracking-Datei erstellen

Erstelle die Datei:
`01_Projects/Fett to Fit/Tracking/[DATUM] - [TYP] W[N].md`

Verwende exakt dieses Format (Übungen aus dem PPL-Plan für den jeweiligen Typ):

```markdown
---
datum: YYYY-MM-DD
tags: [training, tracking, push|pull|legs]
einheit: Push|Pull|Legs
woche: N
---

# Training – YYYY-MM-DD ([Typ])

**Einheit:** [Typ] – [Muskelgruppen]
**Woche:** W[N] von 8
**Gym:** FitX
**Dauer:** min

---

## Übungen

### [Übungsname]

| Satz | Gewicht (kg) | Wdh. | Notiz |
| ---- | ------------ | ---- | ----- |
| 1    | [Gewicht aus letzter Session] | – | [Tipp aus Trend-Analyse] |
| 2    | [Gewicht] | – | |
| 3    | [Gewicht] | – | |

...

---

## Gefühl & Notizen

**Energie:** (1–5)
**Pump:** (1–5)

**Notizen:**

---

## Nächstes Mal steigern?

- [ ] [Übung]: Gewicht erhöhen auf ___ kg (wenn alle Sätze im Maximalbereich)
```

**Regeln für die Notiz-Spalte:**
- Satz 1: Tipp aus der Trend-Analyse (Schritt 3) – kurz und direkt, max. 1 Satz
- Satz 2+: Leer lassen, außer der Tipp betrifft einen späteren Satz explizit (z.B. "Vor diesem Satz 2 Min. Pause!")
- Wenn Steigerung empfohlen: Zielgewicht direkt nennen (z.B. "Versuch 72,5 kg!")
- Wenn Ermüdung in Satz 3/4: Dort eintragen "Extra Pause hier!"
- Gewichte aus der letzten Session vorausfüllen (letztes verwendetes Gewicht je Satz)

**Regeln für "Nächstes Mal steigern?":**
- Nur Übungen eintragen, bei denen laut Trend-Analyse eine Steigerung bald realistisch ist
- Zielgewicht konkret angeben

**Falls keine Daten aus früheren Sessions verfügbar (erste Session eines Typs):**
- Kein Trend-Tipp möglich → Notiz aus dem PPL-Plan eintragen (Zielbereich, Startgewicht)
- Chat-Ausgabe: nur 1 Bullet-Point: "Erste Session – Daten werden ab nächster Einheit für Trends genutzt"
