---
title: Vault Guide – Was gehört rein
type: reference
tags: [meta, philosophie, vault]
date: 2026-05-18
---

# Vault Guide – Was gehört rein

> **Kernregel:** Lernen → Vault. Erinnerung → Google Tasks / Kalender.

Dieses Vault ist kein Task Manager, kein Kalender, kein Habit-Tracker.
Es ist eine Werkbank für **Wissen, Strategie und Reflexion**.

---

## Was REIN gehört

| Typ | Halbwertszeit | Beispiel hier im Vault |
|-----|---------------|------------------------|
| **Wissen** | Jahre | [[Building a Second Brain - Tiago Forte]], [[Eigene Lehren]], [[Hauskauf – Strategie & Finanzierung]] |
| **Strategie** | Wochen–Monate | [[Rauchfrei]], [[Hochzeit]], [[ETF-Strategie]] |
| **Entscheidungen** | dauerhaft | `01_Projects/*/Entscheidungen/` – was und vor allem **warum** |
| **Reflexion** | täglich verdichtet | Daily Notes (3 Felder), [[Wochenanalysen]] |
| **Referenz** | bei Bedarf | [[Friseur Hannover - Izmir]], [[Karriere Tipps - JobTeaser]] |

---

## Was RAUS gehört

| Typ | Wohin | Warum |
|-----|-------|-------|
| Tagestasks („Riester anrufen") | **Google Tasks** | Hat Erinnerung, Sortierung, Sync |
| Termine | **Google Calendar** | Zeit-Anker, Erinnerungen |
| Routine-Checks (Morgen-/Abendroutine) | **iOS Reminders / Habit-App** | Tägliche Wiederholung skaliert nicht in Markdown |
| Skills, Bots, Configs | **`.claude/`**, **`tgbot/`** | Code, kein Wissen |

---

## Die Test-Frage

Wenn du eine Notiz öffnest oder erstellst:

> **„Lerne ich gerade was – oder erinnere ich mich an was zu tun?"**

- Lernen → bleibt im Vault
- Erinnerung → raus in Google Tasks / Kalender

---

## Die Single-Source-of-Truth-Regel

Eine Aufgabe gehört an **genau eine Stelle**.

**Anti-Pattern (was du vorher gemacht hast):**
- Aufgabe steht in Google Tasks
- UND in `01_Projects/Hochzeit/Hochzeit.md` als `- [ ]`
- UND in einer Daily Note vom 07.04.
- UND in einer Wochenanalyse

→ Du hakst nirgends ab, die Aufgabe verrottet in 4 Layern.

**Richtig:**
- Im Vault steht der **Plan**: „Hochzeitsfonds aufbauen, 400 €/Monat ab Mai 2026, Ziel 20k bis Düğün."
- In Google Tasks steht die **Aktion**: „Konto eröffnen DKB Tagesgeld" mit Fälligkeit.
- Wenn erledigt: Häkchen in Google Tasks. Im Vault bleibt der Plan, evtl. mit Status-Notiz.

---

## Daily Note Disziplin

Die neue Daily ([[Daily Note Template]]) hat 3 Felder:

- **Gemacht** – was heute wirklich passiert ist (max. 3 Bullets)
- **Wichtigster Loop heute** – die EINE Sache mit höchstem Hebel
- **Morgen erstes Tun** – konkrete Aktion, kein Plan

Was die Daily **nicht** ist:
- Keine Task-Liste mit `- [ ]` Checkboxen
- Keine Fragen-Sammlung („Was bin ich neugierig auf?")
- Keine Erkenntnisse-Liste (das gehört in [[Eigene Lehren]] oder ins wöchentliche Review)

---

## Wochenrhythmus

| Tag | Was | Wo |
|-----|-----|-----|
| Mo–Sa | Daily Note (3 Felder, 2 Minuten) | [[07_Daily]] |
| Sa/So | Weekly Synthesis | [[07_Daily/Wochenanalysen]] |
| Letzter Sonntag im Quartal | Quarterly Review | [[06_Metadata/Plans]] |
| Tageweise | Tasks erfassen + abhaken | Google Tasks (außerhalb!) |

---

## Wenn du dabei bist, eine Notiz zu erstellen

Drei Fragen:

1. **Lerne ich was, oder erinnere ich mich?** → Erinnerung: ab in Google Tasks.
2. **Existiert die Notiz schon?** → Ja: alte aktualisieren statt neu erstellen.
3. **Was tue ich heute auf Basis dieser Notiz?** → Keine Antwort: nicht jetzt schreiben, erst handeln.

---

## Verbindungen

- [[Vault Übersicht]] – das MOC
- [[Building a Second Brain - Tiago Forte]] – die zugrundeliegende Methode
- [[Eigene Lehren]] – wo verdichtete Lehren landen
