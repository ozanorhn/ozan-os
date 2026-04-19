---
title: Profil & Skills
type: reference
bereich: karriere
erstellt: 2026-04-10
aktualisiert: 2026-04-10
tags: [karriere, skills, profil]
---

# Profil & Skills

## Wer bin ich

Ozan Orhan, technischer Kopf bei arcnode (KI- und Automatisierungsagentur).
Angestellter bei EOM (Effektiv Online Marketing) in Hannover.
Ich baue KI-Automatisierungen, Dashboards und KI-Agenten für Firmen.

**Positionierung:** "Wir bauen KI-Lösungen, die echte Probleme lösen." – Hands-on Umsetzung, nicht Showcase.

---

## Technische Skills

### Programmierung & Frameworks
- JavaScript (Hauptsprache)
- Python (Backend, KI-Agenten)
- Angular (Frontend-Framework)
- HTML/CSS

### Infrastruktur & DevOps
- Docker (Container-Management, Self-Hosted)
- Hetzner Server (Linux, SSH)
- Caddy (Reverse Proxy)
- FTP-Deployment
- Git / GitHub (inkl. Team-Workflows, Konfliktlösung)

### Automatisierung
- n8n (Haupt-Automatisierungsplattform, Self-Hosted)
- Make (früher Integromat)
- Webhook-Architektur
- Multi-Step-Workflows

### Datenbanken & Backend
- Supabase (PostgreSQL, Auth, User-Management)
- Datenbankdesign (Tabellenstruktur, Relationen)

### KI & LLMs
- Claude API (Anthropic)
- Perplexity API (Research-Integration)
- Ahrefs API (SEO-Daten)
- Prompt Engineering
- Multi-Agenten-Systeme (Sub-Agenten, spezialisierte Skills)
- LLM-Fallback-Architekturen

### Tools & Plattformen
- Monday.com (Projektmanagement)
- Toggl (Zeiterfassung)
- Slack (Kommunikation, Automatisierungsausgabe)
- Tactiq (Meeting-Transkription)
- Google Drive / Google APIs
- Obsidian (Second Brain / Wissensmanagement)
- Claude Code (KI-gestütztes Coding)

---

## Team (arcnode / EOM)

- **Stefan** – Mitgründer/Partner, Git-Workflow, Kundenkontakt, Monday-Tickets, Termin-Organisation
- **Ernest (Mavriqi)** – Inhaltliche Qualität, Feedback, Agenten-Ideen, Mitarbeiterstruktur
- **Lukas** – GEO Dashboard Stakeholder, Anforderungen
- **Roxy** – Grounding Page, EOM-Marketing-Seite
- **Johanna** – Leistungsnachweise

---

## Arbeitsprinzipien

- Verstehen vor Entscheidung
- Ideen in konkrete Schritte zerlegen
- Offene, direkte Kommunikation
- Lösungsorientiert statt Rechtfertigung
- Qualität im Detail: Vorbereitung, Dokumentation, Termintreue
- Lernen ohne Ego: Feedback ist Teil der Arbeit
- Technologie gezielt einsetzen, nicht blind automatisieren

---

## Learnings aus Projekten

### Architektur
- **Datenbankstruktur spart Token:** Eine "Teilnehmer"-Spalte in der Meetings-Tabelle macht KI-Filtering viel effizienter als den ganzen Text durchsuchen zu lassen.
- **Python-Backend ist schwer zu warten:** Jede Änderung braucht neues Deployment → n8n-Workflows sind flexibler und schneller anpassbar.
- **CORS muss an 3 Stellen konsistent sein:** Supabase .env, kong.yml und Caddyfile. Fehlt eine Stelle, bricht alles. Bei Server-Problemen immer alle 3 gleichzeitig prüfen.

### Produkt & UX
- **Einfach ist besser:** 3 Felder ausfüllen, sofort Ergebnis – kein Overhead, keine Registrierung am Messestand.
- **Qualität vor Quantität:** Lieber 1 perfekte Demo als 5 buggy Tools.
- **Self-Explanatory ist Pflicht:** User muss sofort verstehen, was ein Agent tut – ohne Erklärung.
- **Zentrales Dashboard statt vieler Links:** Mitarbeiter sollen nicht wissen müssen, wo welcher Link ist.

### Prozess
- **Requirements zuerst, dann bauen:** Grounding Page Projekt lief falsch, weil Anforderungen nicht klar waren – Team hat Editor gebaut, Roxy wollte Automation.
- **Human-in-the-Loop bei kreativen KI-Outputs ist Pflicht.** Faktenkontrolle kann nicht vollständig automatisiert werden.
- **Proaktive Kundenkommunikation bei Ausfällen:** Nicht warten bis der Kunde anruft.

### KI-Entwicklung
- **LLM-Kreativität braucht Grenzen:** Wortanzahl-Vorgaben werden ignoriert wenn das Prompt nicht hart begrenzt.
- **Mix aus Schreibstilen:** Journalistisch (flüssig, menschlich) + faktenbasiert (GEO-optimiert, konkret) kombinieren.
- **Fallback-LLM einplanen:** Externe APIs haben echte Ausfälle (Perplexity war am 27.3. mit 221 Fehlern überlastet).
