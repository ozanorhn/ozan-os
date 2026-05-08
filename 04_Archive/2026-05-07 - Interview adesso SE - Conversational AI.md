# Interview-Prep: adesso SE — Software Engineer Conversational AI

**Termin:** 2026-05-07
**Bewerbung:** Report 002, Score 3.2/5
**Hauptlücke:** Keine direkte Cognigy/Parloa-Plattformerfahrung
**Stärken:** TypeScript, LLMs, autonome Agenten, n8n, Python/Django

---

## Reflektion nach dem Interview (2026-05-08)

**Outcome:** Durchwachsen – unklar, ob es weitergeht.

**Was nicht ideal lief:**
- Eigene Antworten verbesserungsfähig – Stories/Formulierungen kamen nicht so rund wie geprobt
- Cognigy/Parloa-Lücke wurde Thema im Gespräch – die vorbereitete Antwort hat nicht voll überzeugt

**Learnings für nächstes Mal:**
- Stories nicht nur lesen, sondern laut sprechen bis sie sitzen
- Konkrete Plattform-Demo (Cognigy Trial / Parloa Demo) **vor** dem Interview hands-on machen, nicht nur Doku überfliegen
- "Ich habe mich eingearbeitet" reicht nicht – braucht ein konkretes Mini-Projekt oder Screenshot

---

## 1. Selbstvorstellung (60 Sekunden) — auswendig lernen

> "Ich bin Ozan, gelernter Anlagenmechaniker mit zehn Jahren Praxis. Vor zwei Jahren habe ich mich vollständig in Richtung Softwareentwicklung umorientiert: erst Frontend mit Angular und TypeScript, dann Backend mit Python und Django.
>
> Seit August 2025 arbeite ich als Junior Analytics & AI Specialist bei EOM in Hannover. Mein Tagesgeschäft sind autonome KI-Agenten mit Tool-Calling, n8n-Workflows für Klassifikation und Routing, sowie Python-Backends als strukturierte Schnittstelle für LLMs.
>
> Was mich bei adesso reizt: die Verbindung aus echter technischer Umsetzung und direktem Kundenkontakt. Ich baue Systeme nicht für die Schublade, sondern damit sie laufen."

---

## 2. Die Cognigy/Parloa-Frage — DIE wichtigste Antwort

**Wenn sie fragen "Haben Sie Erfahrung mit Cognigy oder Parloa?"**

> "Ehrlich gesagt: noch nicht produktiv eingesetzt. Ich habe mich aber gezielt in beide Plattformen eingearbeitet — Cognigy.AI und Parloa nutzen unter der Haube genau das, was ich täglich baue: LLM-Calls, Tool-Bindings, Conversation State Management und Webhook-Integration.
>
> Was ich bei EOM mache, ist im Kern dasselbe Prinzip — nur ohne die fertige Plattform-Schicht obendrauf. Das heißt: ich verstehe, was unter der Haube passiert, was die Einarbeitung in eine fertige Plattform eher beschleunigt als bremst."

**Wichtig:** Nicht entschuldigen. Nicht zögern. Selbstbewusst, aber nicht arrogant.

---

## 3. Die 5 STAR+R-Geschichten (Kurzversion)

### Story 1: Conversational AI Agent (Meeting Insights)
- **S:** Meetings im Team blieben oft ohne Follow-up, Action Items gingen verloren.
- **T:** Automatisches System bauen: Sprache rein, strukturierte Action Items raus.
- **A:** Pipeline mit Whisper-Transkription, OpenAI für Extraktion, n8n für Routing nach Slack/Mail. Systemprompt iteriert für konsistente Item-Extraktion.
- **R:** Meetings dokumentieren sich selbst, Items kommen automatisch beim Verantwortlichen an.
- **Reflection:** Hätte früher Eval-Framework gebaut um Prompt-Qualität zu messen statt nur visuell zu prüfen.

### Story 2: Hybride Workflows (Enterprise Automation)
- **S:** Manuelle Berichterstellung kostete das Team über 3 Stunden pro Woche.
- **T:** Vollautomatisierte Pipeline ohne Medienbrüche.
- **A:** n8n als Orchestrierungsschicht: klassische Klassifikation für strukturierte Daten, LLM für unstrukturierte Zusammenfassung. Hybrid-Ansatz weil pure LLM-Lösung zu teuer und fehleranfällig wäre.
- **R:** Berichterstellung von 3+ Stunden auf unter 5 Minuten reduziert.
- **Reflection:** Monitoring war Nachgedanke. Beim nächsten Projekt baue ich Observability von Anfang an mit.

### Story 3: Tool-Calling Architecture (EOM Backend)
- **S:** LLM brauchte kontrollierten Zugriff auf Unternehmensdaten ohne direkte DB-Exposition.
- **T:** Sichere API-Schicht zwischen Agent und Backend.
- **A:** Django-Endpoints als strukturierte Tool-Interfaces, klar definierte Input-Validation, Logging jedes Calls. Konzeptionell sehr nah an MCP.
- **R:** Agenten arbeiten produktiv mit Unternehmensdaten, kein direkter DB-Zugriff nötig.
- **Reflection:** Auth-Layer hätte ich früher einbauen sollen, das hat eine Iteration gekostet.

### Story 4: Prompt Engineering (SEO Content Tool)
- **S:** Generischer LLM-Output war nicht brand-konsistent, jedes Mal anders.
- **T:** Konsistente, publikationsfertige Outputs ohne manuelle Nacharbeit.
- **A:** System-Prompt mit klar definierter Persona, strukturierten Output-Templates, Few-Shot-Beispielen für Tonalität.
- **R:** Outputs waren direkt verwendbar, keine Nachbearbeitung mehr nötig.
- **Reflection:** Eval-Framework wäre sinnvoll gewesen statt manuell zu prüfen ob die Persona hält.

### Story 5: Stakeholder & Wissenstransfer (Auszubildende)
- **S:** 6 Auszubildende mit unterschiedlichen Wissensständen, kein einheitlicher Lehrplan.
- **T:** Alle erfolgreich durch die Prüfung bringen.
- **A:** Individuelle Erklärungen pro Azubi, praxisnahe Beispiele, regelmäßiges Feedback.
- **R:** Alle 6 haben bestanden.
- **Reflection:** Strukturiertes wöchentliches Feedback hätte mir viel Zeit gespart. Heute mache ich das automatisch.

---

## 4. Gehalt — wenn sie fragen

**Frage erwarten:** "Was sind Ihre Gehaltsvorstellungen?"

**Antwort:**
> "Basierend auf Marktdaten für diese Rolle in Deutschland und meinem Profil ziele ich auf 55.000 Euro brutto. Ich bin offen für die Gesamtstruktur — was zählt, ist das Paket aus Gehalt, Weiterbildungsbudget und Entwicklungsperspektive."

**Wenn sie 50.000 oder weniger anbieten:**
> "Das liegt unter dem, was ich anvisiert habe. Können wir über einen Review nach 6 Monaten sprechen, mit klaren Kriterien wie erste Plattform-Zertifizierung und erstes Kundenprojekt? Dann wäre eine Anpassung auf 55.000 möglich."

**Walk-away:** 50.000. Darunter nicht ohne klaren Aufwärtspfad.

---

## 5. Standort-Frage — proaktiv ansprechen

Wenn nicht von selbst geklärt, **DU** fragst:
> "Die Stelle ist für Aachen ausgeschrieben. Ich habe gesehen, adesso hat auch einen Standort in Hannover. Wie flexibel ist die Standortzuordnung für diese Rolle? Mein Lebensmittelpunkt ist Hannover."

---

## 6. Red-Flag-Fragen — Antworten parat haben

### "Warum der Quereinstieg von Anlagenmechaniker zu AI?"
> "Mit Wärmepumpen und Anlagensteuerung habe ich gelernt, komplexe Systeme zu debuggen und zum Laufen zu bringen. Software ist dasselbe, nur anderes Material. Ich wollte den Schritt zu skalierbarer Arbeit machen — Code löst ein Problem einmal und dann tausendmal."

### "Sie haben erst seit August 2025 in der AI-Rolle. Reicht das?"
> "Neun Monate hands-on, aber davor zwei Jahre fokussiertes Lernen mit über 12 Projekten an der Developer Akademie. Bei EOM arbeite ich an produktiven Systemen, nicht an Tutorials. Was bei mir fehlt ist nicht die Tiefe, sondern die Breite an Projekten — und genau die suche ich bei adesso."

### "Sind Sie bereit zum Reisen / Vor-Ort-Termine bei Kunden?"
> "Ja, im Tagesreich-Modus kein Problem. Bei längeren Auswärtsterminen würde ich gerne abstimmen, aber Kundennähe ist genau das, was mich an der Rolle reizt."

### "Wie würden Sie einen Kunden beraten, der einen Chatbot will?"
> "Erste Frage: Was ist das eigentliche Problem hinter dem Chatbot-Wunsch? Manchmal ist die Lösung eine bessere FAQ oder ein guter Workflow ohne Conversational Layer. Wenn Conversational sinnvoll ist: definierte Use Cases, klare Eskalationspfade zu Menschen, von Anfang an Eval-Mechanismen einplanen."

---

## 7. Fragen DIE DU stellst — Pflicht

Mindestens 3 Fragen vorbereiten, signalisieren Senioritätsdenken:

1. **"Wie ist die typische Verteilung zwischen Beratung beim Kunden und reiner Entwicklung in dieser Rolle?"** (zeigt: du verstehst, dass Consulting anders tickt)

2. **"Welche Plattform — Cognigy oder Parloa — wird in den meisten aktuellen Projekten eingesetzt? Und wie würde meine Einarbeitung aussehen?"** (zeigt: du planst voraus, nimmst die Lücke ernst)

3. **"Wie messt ihr den Erfolg eines Conversational-AI-Projekts beim Kunden? Welche Metriken zählen?"** (zeigt: du denkst in Outcomes, nicht in Features)

4. *Optional, falls Zeit:* **"Wie wird im Team mit Prompt-Iterationen umgegangen? Gibt es Eval-Frameworks oder läuft das eher pragmatisch?"** (zeigt: du kennst das Problem)

5. *Pragmatisch:* **"Wie sehen die nächsten Schritte im Bewerbungsprozess aus?"**

---

## 8. Vor dem Interview — Last Minute Checklist

- [ ] Cognigy.AI Docs überflogen (Hauptbegriffe: Flow, Intent, Lexicon, Snapshot)
- [ ] Parloa Demo-Video geschaut
- [ ] adesso Geschäftsbericht 2025 Zahlen parat (Umsatz +14%, EBITDA +30%, FTE 11.298)
- [ ] LinkedIn der Interviewer angeschaut (kannst du erwähnen, aber subtil)
- [ ] Eigene Projekte im Browser-Tab offen (falls Bildschirm geteilt wird)
- [ ] Stille, gut beleuchtete Umgebung getestet (falls remote)
- [ ] Wasserglas griffbereit
- [ ] CV ausgedruckt (falls vor Ort)

---

## 9. adesso-Insider-Wissen (aus Learning Guide 2026)

Das beeindruckt im Interview, weil es zeigt, dass du dich vorbereitet hast:

### Die drei Schlüsselbegriffe — kennen und nutzen

| Begriff | Was es ist | Wie du es im Gespräch nutzt |
|---------|-----------|------------------------------|
| **New School of AI** | Strategische adesso-Initiative für AI-Integration in der IT | "Die New School of AI hat mich besonders neugierig gemacht — der strategische Rahmen passt zu meinem Ansatz, AI nicht als Spielerei, sondern als integralen Teil von Software zu denken." |
| **AI-Force** | Operativer Arm: KI-Wissen über Teams hinweg verteilen, Pilotprojekte, Communities | "Die AI-Force klingt für mich wie ein perfekter Lernrahmen — gerade als jemand, der gezielt von Plattform-Tiefe (Cognigy/Parloa) profitieren will, ist eine Community, die das Wissen teilt, Gold wert." |
| **GenAI@adesso** | Initiative von Gründer Volker Gruhn | Subtil erwähnen, signalisiert Vorbereitung |

### Der Killer-Satz von Volker Gruhn (Gründer)

> *"Anwendungswissen bleibt die Basis für gute Lösungen. Wer Branchen, Prozesse und Nutzende versteht, entwickelt mit Prompts und KI-Interfaces bessere Ergebnisse."*

**Wie du den nutzt:** Wenn die Frage nach deinem "consulting mindset" kommt:
> "Volker Gruhn hat es im Learning Guide auf den Punkt gebracht: Wer die Branche und die Nutzenden versteht, baut bessere KI-Lösungen. Das ist genau mein Ansatz — bei EOM frage ich nicht 'welches Tool nehmen wir', sondern erst 'was ist das eigentliche Problem'."

### Konkrete Trainings, die für deine Rolle relevant sind

Du kannst sagen: *"Ich habe gesehen, dass adesso folgende Trainings anbietet — die wären für mich besonders relevant:"*

- **GenAI-Onboarding-Programm** (Pflicht für neue AI-Rollen)
- **Grundlagen der GenAI für die Projektarbeit** (mit Zertifikat)
- **KI Ethik und der EU AI Act** (wichtig für Kundenprojekte!)
- **Testen mit generativer KI** (relevant für Conversational AI Quality)
- **Vibe Coding** (neu, AI-gestütztes Coding)

### Karriere-Pfad (zeigt, dass du langfristig denkst)

- adesso hat klare Laufbahnstufen: Software Engineer → Senior Software Engineer
- **Karrierebooster** — Programm für High Potentials
- Strukturiertes **Jahresgespräch** + Probezeitende-Gespräch
- **Pluralsight SKILLS** als Lernplattform für alle Mitarbeitenden

### Einer der schlauesten Sätze, den du ablassen kannst

> *"Was mich an adesso konkret reizt, ist die Verbindung aus 'New School of AI' als Strategie und der AI-Force als operativem Wissensnetzwerk. Bei vielen Firmen gibt's entweder Tools oder Theorie. Bei euch sehe ich beides — und das ist genau das Umfeld, in dem ich schnell von Cognigy- und Parloa-Anwender zu echtem Plattform-Experten werde."*

---

## 10. adesso-Kultur (aus Kulturbroschüre)

### Die drei Säulen des Culture Code (auswendig kennen)

1. **"We are ONEadesso"** — ein Team, Standort-übergreifend
2. **"We work hands-on"** — pragmatisch, anpacken
3. **"We behave open-minded"** — Offenheit, Diversität

**Wenn du gefragt wirst, was dir an adesso gefällt:**
> "Der Culture Code mit 'hands-on' und 'open-minded' beschreibt ziemlich genau, wie ich arbeite — pragmatisch und ohne Berührungsängste vor neuen Tools. Das passt zu meinem Quereinsteiger-Weg."

### Konkrete Kulturbausteine (kennen, aber nicht aufzählen)

| Programm | Was es ist |
|----------|-----------|
| **Welcome Days** | Monatliches Onboarding für neue adessi mit gemeinsamem Abendessen |
| **Patenschaft** | Jede:r neue adessi bekommt eine:n erfahrene:n Paten/Patin |
| **Duz-Kultur** | Über alle Hierarchieebenen hinweg |
| **adessi go abroad** | Bis zu 2 Monate pro Jahr Mobile Work aus EU-Ausland |
| **Choose your own device** | Mac oder Windows, iPhone oder Samsung |
| **care[4]adessi** | Body & Health, Family & Finance Support 24/7 |
| **JobRad / gadgets[4]adessi** | Bike-Leasing + Hardware-Leasing für privat |
| **Auszeit-Programm** | Bis zu 2 Monate unbezahlt frei + Bonus-Fortzahlung |
| **Charta der Vielfalt** | Unterzeichnet — Diversity ernst gemeint |

### Die Auszeichnungen (Zahlen kennen, falls Smalltalk)

- **Great Place to Work 2023**: bester Arbeitgeber Deutschlands (ITK) + #2 Europa
- **100%** der adessi fühlen sich willkommen
- **98%** sagen, dass sich Kollegen umeinander kümmern
- **96%** finden, dass sie einen sehr guten Arbeitsplatz haben

### Originalzitate aus der Broschüre — für den Echo-Moment

> *"Bei uns zählt immer das Sachargument, nicht die Stellung derjenigen, die es verwenden."*

**Wie du das einbaust:**
> "In eurer Kulturbroschüre steht: bei adesso zählt das Sachargument, nicht die Position. Genau das suche ich — überzeugen mit dem besten Argument, nicht mit dem dicksten Titel."

> *"Grow Together"* — adessos Lern-Motto

> *"Great Place to Learn"* — Selbstbeschreibung der Lernkultur

> *"Diversity ist unsere Chance, Inklusion unser Ziel."*

### Eine richtig gute Frage zum Schluss

> "Aus der Kulturbroschüre weiß ich, dass jede:r neue adessi eine:n Paten/Patin bekommt. Wie würde das in meiner Rolle aussehen — gibt es jemanden in der AI-Force, der die Cognigy- oder Parloa-Einarbeitung begleitet?"

Diese Frage zeigt:
- Du hast die Broschüre gelesen
- Du planst proaktiv deine Einarbeitung
- Du behandelst die Plattform-Lücke offen und konstruktiv

---

## 11. LLM-Match: Claude / GPT / Gemini — DEIN HEIMSPIEL

**Direkt aus der Stellenausschreibung:**
> *"LLMs (z.B. GPT, Claude, Gemini)"*

Und in deinem Portfolio (SEO-Redakteur & Research-Workflow) steht wörtlich:
> *Python · Datenbank · DataForSEO API · Firecrawl · Claude*

**Du hast also konkrete produktive Claude-Erfahrung.** Das ist kein "habe ich mal probiert", das läuft in deinem Workflow.

### Wenn die LLM-Frage kommt

> "GPT, Claude und Gemini, je nach Use Case. In meinem SEO-Research-Workflow nutze ich Claude produktiv für Inhaltsanalyse und Empfehlungen — Claude ist bei strukturiertem Long-Context-Reasoning oft präziser. Bei agentenbasierten Workflows nutze ich aktuell OpenAI, weil das Tool-Calling dort etwas robuster ist."

Was das signalisiert:
- Du kennst die Modelle nicht nur namentlich, sondern **mit Meinung**
- Du wählst **nach Use Case**, nicht nach Hype
- Du sprichst die **gleiche Sprache wie der JD**

### Der MCP-Bonus

MCP wurde von **Anthropic** entwickelt — denselben Leuten, die Claude bauen. Wenn du das verknüpfst:

> "MCP ist von Anthropic. Das passt gut zu meiner Claude-Erfahrung — die Standardisierung von Tool-Bindings über MCP ist genau der nächste Schritt nach dem, was ich aktuell mit handgebauten Tool-Interfaces in meinen Django-Backends mache."

Das hebt dich von "Quereinsteiger" auf "denkt strategisch über LLM-Ökosysteme". Senioritätssignal.

### Was du NICHT sagen solltest

- "Ich habe mal mit ChatGPT gespielt" (zu schwach)
- "Claude ist besser als GPT" (Pauschalurteile vermeiden)
- "Welches LLM würden Sie empfehlen?" (du sollst antworten, nicht zurückfragen)

---

## 12. Mindset

- Du bist nicht der unterlegene Bewerber. Du bist ein Quereinsteiger mit echter Produktionserfahrung in genau dem Stack, den sie brauchen.
- Cognigy/Parloa sind Werkzeuge. Du hast die Grundlagen verstanden. Tools lernt man in Wochen.
- Wenn etwas unklar ist: nachfragen. Senioritätssignal.
- Wenn du etwas nicht weißt: ehrlich sagen "Damit habe ich noch nicht gearbeitet, würde mich aber so rangehen: ..." — niemals raten.
