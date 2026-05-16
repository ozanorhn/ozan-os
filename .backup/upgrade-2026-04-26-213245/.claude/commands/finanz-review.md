---
name: finanz-review
description: 'Monatliches Finanz-Review: Budget vs. Ausgaben, Vermögen, Fortschritt Sparziele prüfen und aktualisieren'
argument-hint: '[Monat YYYY-MM]'
---

# Finanz-Review

Monatliche Bestandsaufnahme der Finanzen – Ist vs. Soll, Vermögensentwicklung, nächste Schritte.

## Schritt 1 – Aktuellen Stand laden

Lese parallel:
- `02_Areas/Finanzen/Budget.md` – Fixkosten, Budget-Kategorien
- `02_Areas/Finanzen/Vermögensübersicht.md` – Nettovermögen, Positionen
- `02_Areas/Finanzen/Scalable-Portfolio.md` – ETF-Depotstand
- `02_Areas/Finanzen/Trade-Republic-Portfolio.md` – Einzelaktien + Cash
- `02_Areas/Finanzen/Generali-Riester.md` – Riester-Stand
- `02_Areas/Finanzen/ETF-Strategie.md` – Sparplan-Strategie

Feste Werte aus Memory:
- Netto: 2.224,31 €/Monat
- Fixkosten: 531,60 €/Monat
- Verfügbar: 1.692,71 €/Monat

## Schritt 2 – Aktuelle Zahlen erfragen

Frage nach den Werten für diesen Monat:

1. "Aktueller Kontostand (nach Fixkosten)?"
2. "Scalable-Depot aktuell (€)?"
3. "Trade Republic Cash aktuell (€)?"
4. "Trade Republic Aktien aktuell (€)?"
5. "Hast du diesen Monat gespart? Wie viel?"
6. "Besondere Ausgaben diesen Monat?"

## Schritt 3 – Analyse berechnen

Aus den Angaben ableiten:

**Budget-Check:**
- Verfügbar (Plan): 1.692,71 €
- Tatsächlich gespart: [eingegeben]
- Konsumausgaben: [Differenz]
- Bewertung: Gut / Okay / Überzogen

**Vermögensentwicklung:**
| Position | Vormonat | Aktuell | Delta |
|----------|----------|---------|-------|
| Scalable ETF | [aus Datei] | [eingegeben] | |
| TR Cash | [aus Datei] | [eingegeben] | |
| TR Aktien | [aus Datei] | [eingegeben] | |
| Riester | [aus Datei] | [ggf.] | |
| Badenia Bauspar | [aus Datei] | [ggf.] | |
| Badenia Darlehen | [aus Datei] | [ggf.] | |
| **Nettovermögen** | | | |

**Sparziel-Fortschritt:**
- Eigenkapital-Ziel: 15.000–20.000 €
- Aktuell: [berechnet]
- Noch fehlend: [berechnet]
- Prognose: [Monate bis Ziel bei aktuellem Tempo]

## Schritt 4 – Review-Datei erstellen

Erstelle `02_Areas/Finanzen/Reviews/YYYY-MM - Finanz-Review.md`:

```markdown
---
datum: YYYY-MM-DD
tags: [finanzen, monatsreview]
monat: YYYY-MM
---

# Finanz-Review [Monat]

## Budget

| | Geplant | Ist |
|--|---------|-----|
| Verfügbar | 1.692,71 € | |
| Gespart | | |
| Konsumausgaben | | |

**Bewertung:** 

## Vermögen

| Position | Stand |
|----------|-------|
| Scalable ETF | |
| TR Cash | |
| TR Aktien | |
| Nettovermögen | |

**Delta Vormonat:** 

## Eigenkapital-Fortschritt

Ziel: 15.000–20.000 €
Aktuell: 
Prognose: 

## Besondere Ausgaben / Ereignisse

- 

## Nächste Schritte

- [ ] 
```

## Schritt 5 – Vermögensübersicht aktualisieren

Aktualisiere die Werte in `02_Areas/Finanzen/Vermögensübersicht.md` mit den neuen Ständen.

## Schritt 6 – Offene Punkte prüfen

Aus Memory bekannte offene Punkte ansprechen:
- BU-Versicherung (fällig ab April 2027) – schon recherchiert?
- Haftpflicht bei Eltern prüfen – erledigt?
- Badenia-Darlehen: aktueller Schuldenstand

Berichte Ergebnis kompakt und nenne den nächsten Review-Termin (nächster Monatserster).
