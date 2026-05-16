# Debrief

Abend-Conversation: stellt 3–4 kurze Fragen, schreibt dann einen strukturierten Log-Eintrag und aktualisiert die Daily Note.

## Ablauf

### 1. Kontext laden (still, kein Output)
- Heute's Daily Note lesen: `07_Daily/YYYY-MM-DD.md`
- Letzten Log-Eintrag lesen: `tail -20 06_Metadata/log.md`

### 2. Fragen – eine nach der anderen

Stelle die Fragen sequenziell. Warte auf jede Antwort bevor du die nächste stellst.

**Frage 1:** "Was hast du heute geschafft? (kurz, Stichpunkte reichen)"

**Frage 2:** "Was blieb liegen oder hat blockiert?"

**Frage 3:** "Was hast du gelernt oder erkannt – aus dem Tag, einem Gespräch, etwas das du gelesen hast?"

**Frage 4:** "Was ist morgen deine #1-Priorität?"

### 3. Log-Eintrag schreiben

In `06_Metadata/log.md` anhängen:

```markdown
## [YYYY-MM-DD] debrief | [kurzer Titel aus den Antworten]

**Geschafft:** [Antwort 1]
**Blockiert:** [Antwort 2]
**Erkenntnisse:** [Antwort 3]
**Morgen #1:** [Antwort 4]
```

### 4. Daily Note aktualisieren

In `07_Daily/YYYY-MM-DD.md` die Sections befüllen:
- `## Erfassen` / `## Erkenntnisse` / `## Für morgen` – aus den Antworten

### 5. Wiki-Updates prüfen

Wenn Antwort 3 (Erkenntnisse) eine bestehende Resource-Seite berührt:
→ Update vorschlagen, erst fragen: "Soll ich das in [[Seitenname]] eintragen?"
→ Wenn ja: Seite aktualisieren + `03_Resources/Wiki/index.md` Datum anpassen

### 6. Abschluss

Ein-Satz-Zusammenfassung des Tages ausgeben.

---

## $ARGUMENTS-Modus

Wenn `$ARGUMENTS` übergeben wird (z.B. `/debrief Kurze Notiz vom Tag`):
- Fragen überspringen
- Direkt Log-Eintrag mit dem Text als Inhalt schreiben
- Daily Note minimal aktualisieren (Notiz in `## Erfassen`)

---

## Hinweise

- Fragen kurz und direkt halten – keine langen Einleitungen
- Log-Eintrag immer anhängen (append), nie bestehende Einträge ändern
- Wenn Antworten auf Projekte verweisen (Gym, Rauchfrei, Hochzeit) → relevante Projekt-Dateien kurz prüfen und ggf. Status-Update vorschlagen
