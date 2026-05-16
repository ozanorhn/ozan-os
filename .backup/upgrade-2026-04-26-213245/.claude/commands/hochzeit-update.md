---
name: hochzeit-update
description: 'Hochzeitsplanung-Status: offene Aufgaben prüfen, Checklisten aktualisieren, nächste Schritte definieren'
---

# Hochzeit-Update

Aktueller Stand der Hochzeitsplanung – was ist erledigt, was steht an, was ist dringend.

## Schritt 1 – Alle Dateien laden

Lese parallel:
- `01_Projects/Hochzeit/Hochzeit.md` – Übersicht, Eckdaten
- `01_Projects/Hochzeit/Checklisten/Hochzeit Kanban.md` – Gesamtkanban
- `01_Projects/Hochzeit/Checklisten/Türkische Hochzeit Checkliste.md` – Traditionelle Aufgaben
- `01_Projects/Hochzeit/Checklisten/Gelin Bohçası Checkliste.md` – Gelin Bohçası
- `01_Projects/Hochzeit/Budget/Hochzeit Budget.md` – Budgetstand

**Eckdaten (aus Memory):**
- Verlobungsfeier (Nişan): 19.09.2026
- Hochzeit (Düğün): 02.10.2027
- Finanzierung: laufend aus Gehalt

## Schritt 2 – Offene Aufgaben gruppieren

Extrahiere alle `[ ]` Checkboxen aus allen Checklisten und gruppiere nach Dringlichkeit:

**Sofort / Diese Woche:**
- Aufgaben ohne Datum oder mit Frist < 4 Wochen

**Nächste 3 Monate:**
- Aufgaben mit mittlerer Priorität

**Langfristig (Nişan Sep 2026):**
- Aufgaben mit Frist Sept 2026

**Langfristig (Düğün Okt 2027):**
- Aufgaben mit Frist Okt 2027

## Schritt 3 – Was wurde erledigt?

Frage: "Was hast du seit dem letzten Update erledigt?"

Falls der Nutzer erledigte Items nennt:
- Setze die entsprechenden Checkboxen auf `[x]` in den Checklisten-Dateien
- Vermerke das Datum der Erledigung falls sinnvoll

## Schritt 4 – Budget-Check

Zeige aus `Hochzeit Budget.md`:
- Geplantes Gesamtbudget
- Bereits gebuchte/bezahlte Positionen
- Offene Budget-Posten
- Noch verfügbares Budget

Falls Budget-Datei keine aktuellen Zahlen hat: Frage nach dem aktuellen Stand.

## Schritt 5 – Google Tasks abgleichen

Lade die Hochzeits-Tasks aus Google Tasks:

```bash
python3 .claude/skills/google-tasks/scripts/fetch-tasks.py
```

Vergleiche mit den Checklisten-Items. Falls Tasks in Google aber nicht in Checkliste (oder umgekehrt): Hinweis ausgeben.

## Schritt 6 – Zusammenfassung ausgeben

```
## Hochzeit Update – [Datum]

### Zeitleiste
- Heute: [Datum] → Nişan in [X Wochen] → Düğün in [X Monaten]

### Offene Aufgaben
**Dringend (nächste 4 Wochen):**
- [ ] ...

**Nişan-Vorbereitung (bis Sep 2026):**
- [ ] ...

**Düğün-Vorbereitung (bis Okt 2027):**
- [ ] ...

### Budget-Status
Geplant: X € | Verplant: X € | Noch verfügbar: X €

### Nächste 3 Aktionen
1. [Konkrete Aufgabe]
2. [Konkrete Aufgabe]
3. [Konkrete Aufgabe]
```

## Schritt 7 – Hochzeit.md aktualisieren

Aktualisiere den "Letztes Update"-Eintrag in `01_Projects/Hochzeit/Hochzeit.md` mit dem heutigen Datum.
