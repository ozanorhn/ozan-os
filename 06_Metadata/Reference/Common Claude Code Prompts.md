---
title: Nützliche Claude-Prompts
typ: referenz
erstellt: 2026-04-10
aktualisiert: 2026-04-26
tags: [claude, prompts, referenz]
version: "0.15.1"
---

# Nützliche Claude-Prompts

Eine Sammlung hilfreicher Prompts für dein persönliches zweites Gehirn.

## Skills & Schnellbefehle

Ab v0.15.1 werden viele Commands auch automatisch als Skills getriggert – du musst sie nicht immer explizit aufrufen.

| Statt langem Prompt... | einfach... |
|---|---|
| "Mach einen Tagesrückblick für heute" | `/daily-review` |
| "Wochenreview bitte" | `/weekly-synthesis` |
| "Hilf mir das Denken zu [Thema]" | `/thinking-partner` |
| "Inbox verarbeiten" | `/inbox-processor` |
| "Zeig meine Tasks" | `/google-tasks` |
| "Trainingsanalyse" | `/gym-analyse` |
| "Hochzeit Status" | `/hochzeit-update` |

**Vault-Dateien direkt einbinden** mit `@`:
```
Fass @02_Areas/Finanzen/Vermögensübersicht.md zusammen
Update @01_Projects/Fett to Fit/Training/ basierend auf dem letzten Tracking
Was steht in @01_Projects/Hochzeit/Checklisten/ noch offen?
```

**Tiefer nachdenken** mit `ultrathink`:
```
ultrathink: Lohnt sich die BU-Versicherung ab April 2027 gegeben @02_Areas/Finanzen/?
ultrathink: Welche Reihenfolge macht Sinn – Rauchfrei oder erst Gewicht runter?
```

---

## Session starten

### Beginn einer Session
```
Ich setze mich gerade hin, um an meinem Vault weiterzumachen.
Kannst du schauen, was ich zuletzt notiert habe,
und mir helfen, dort anzuknüpfen?
```

### Modus setzen
```
Ich bin im Denkmodus, nicht im Schreibmodus.
Bitte hilf mir, [Thema] zu erkunden, indem du Fragen stellst
und nach relevanten Notizen suchst.
```

## Recherche & Synthese

### Verbindungen finden
```
Durchsuche mein Vault nach allem zu [Thema].
Welche Muster oder Verbindungen siehst du?
```

### Projekt zusammenfassen
```
Überprüfe alle Notizen in [Projektordner].
Erstelle eine Synthese der Hauptthemen, Erkenntnisse und offenen Fragen.
```

### Wöchentlicher Rückblick
```
Schau dir alle diese Woche erstellten Notizen an.
Was sind die Hauptthemen?
Welche Verbindungen gibt es zwischen verschiedenen Projekten?
```

## Organisation

### Eingang verarbeiten
```
Überprüfe Items in 00_Inbox.
Schlage vor, wohin jedes basierend auf der PARA-Methode verschoben werden soll.
Welche Items könnten kombiniert oder verlinkt werden?
```

### Verwaiste Notizen finden
```
Finde Notizen, die mit keiner anderen Notiz verlinkt sind.
Schlage mögliche Verbindungen vor.
```

### Anhänge aufräumen
```
Überprüfe Dateien in 05_Attachments.
Welche werden in keiner Notiz referenziert?
Welche könnten besser benannt werden?
```

## Schreiben & Festhalten

### Gedanken sortieren
```
Ich habe gerade viel im Kopf zu [Thema].
Hilf mir, das zu sortieren, indem du Fragen stellst
und am Ende eine Notiz daraus formst.
```

### Notiz verbessern
```
Schau dir [Notiz] an.
Schreib sie nicht um, aber gib mir konkretes Feedback zu:
- Struktur und Lesbarkeit
- Lücken oder unklare Stellen
- Was noch ergänzt werden könnte
```

## Lernen & Reflexion

### Neues Thema erkunden
```
Ich möchte mehr über [Thema] lernen (z. B. Ernährung, Investieren, Hochzeitsplanung).
Schau zuerst, was ich dazu schon im Vault habe.
Hilf mir dann zu sehen, wo meine Wissenslücken sind.
```

### Entscheidung durchdenken
```
Ich überlege [Entscheidung].
Durchsuche meine Notizen nach allem, was relevant ist.
Welche Aspekte habe ich noch nicht bedacht?
```

## Projekte & Bereiche

### Projektstatus
```
Schau dir [01_Projects/Hochzeit | Fett to Fit | Rauchfrei] an.
Wo stehe ich gerade?
Was sind sinnvolle nächste Schritte?
```

### Projekt abschließen
```
[Projekt] ist abgeschlossen.
Geh alle Notizen durch und erstelle eine kurze Retrospektive:
- Was habe ich erreicht
- Was habe ich gelernt
- Was würde ich beim nächsten Mal anders machen
Verschiebe das Projekt danach ins 04_Archive.
```

## Finanzen

### Finanz-Check
```
Schau dir 02_Areas/Finanzen an.
- Wie sieht mein aktueller Stand bei Fixkosten, Sparen und Investitionen aus?
- Passt mein Budget noch zu meinen Zielen (Hochzeit, Notgroschen, ETF)?
- Wo könnte ich optimieren, ohne Lebensqualität einzubüßen?
```

### Sparziel planen
```
Ich möchte für [Ziel] sparen: [Betrag] bis [Datum].
Schau in 02_Areas/Finanzen, was realistisch ist,
und schlag mir einen monatlichen Sparplan vor.
```

### ETF- & Investment-Review
```
Geh meine Notizen zu Investments und ETF-Strategie durch.
- Passt die aktuelle Aufteilung noch zu meiner Strategie?
- Gibt es Klumpenrisiken oder offene Fragen?
- Was sollte ich mir als Nächstes anschauen?
```

## Tägliche Abläufe

### Morgenstart
```
Guten Morgen. Zeig mir:
- Was ich gestern in der Daily Note festgehalten habe
- Offene Punkte aus den aktiven Projekten
- Worauf ich mich heute konzentrieren sollte
```

### Tagesabschluss
```
Tagesabschluss für heute:
- Was lief gut, was nicht?
- Welche Gedanken oder Ideen sind aufgekommen?
- Was nehme ich mir für morgen vor?
Schreib das in 07_Daily/YYYY-MM-DD.md.
```

## Fortgeschrittene Techniken

### Verbindungen zwischen Lebensbereichen
```
Vergleiche meine Notizen aus [z. B. Gesundheit] und [z. B. Finanzen].
Welche Muster oder Wechselwirkungen siehst du?
```

### Wissenslücken
```
Analysiere meine Notizen zu [Thema].
Welche Aspekte fehlen mir?
Welche Fragen habe ich noch nicht gestellt?
```

### Idee entwickeln
```
Ich habe diese grobe Idee: [Idee]
Such nach verwandten Notizen in meinem Vault.
Hilf mir, daraus etwas Konkreteres zu machen.
```

## Tipps für effektive Prompts

1. **Modus angeben** (Denken vs. Schreiben)
2. **`@Ordner` nutzen** statt Claude erst selbst suchen zu lassen
3. **Nach Fragen fragen**, nicht nur nach Antworten
4. **Synthese verlangen**, nicht nur Suche
5. **`ultrathink` voranstellen** bei komplexen Abwägungen
6. **Skills nutzen** für strukturierte Workflows (`/daily-review` etc.)
7. **Frei iterieren** – führe ein Gespräch

## Denk daran

- Claude hat Zugang zu deinem gesamten Vault
- Es kann Dateien erstellen, bearbeiten und organisieren
- Skills werden automatisch aktiviert – du musst sie nicht immer explizit aufrufen
- Nutze es als Denkpartner, nicht nur als Werkzeug
- Die besten Prompts entstehen aus deinen spezifischen Bedürfnissen
