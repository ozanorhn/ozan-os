---
title: Metadaten
aliases: [Metadaten, Metadata]
---

# ⚙️ Metadaten

Vault-Konfiguration, Dokumentation und Organisationswerkzeuge.

## Zweck

Der Metadaten-Ordner enthält:
- Dokumentation über das Vault
- Vorlagen für konsistente Notizerstellung
- Referenzanleitungen und How-tos
- Workflow-Dokumentation

## Struktur

```
06_Metadata/
├── Reference/         # Anleitungen und Dokumentation
├── Templates/         # Notizvorlagen
├── Agents/            # Claude-Agenten-Konfigurationen
├── Workflows/         # Dokumentierte Prozesse
└── Archive/           # Alte Konfigurationen
```

## Was hier lebt

### Referenz
- Vault-Dokumentation
- Claude-Prompt-Bibliothek
- Stilrichtlinien
- Workflow-Dokumentation

### Vorlagen
- Projektvorlagen
- Tagesnotiz-Vorlagen
- Meeting-Vorlagen
- Recherche-Vorlagen
- Review-Vorlagen

### Workflows
- Wöchentlicher Review-Prozess
- Projektabschluss-Checkliste
- Eingangs-Verarbeitungsanleitung
- Archivierungsverfahren

## Vorlagen verwenden

### Manuell
1. Vorlageninhalt kopieren
2. Neue Notiz erstellen
3. Einfügen und ausfüllen

### Mit Claude
```
Erstelle ein neues Projekt mit der Projektvorlage.
Nenne es [Projektname] und lege es in 01_Projects ab.
```

## Claude-Befehle

### Vorlagen nutzen
```
Zeig mir verfügbare Vorlagen in 06_Metadata/Templates.
Erstelle eine neue [Typ]-Notiz mit der passenden Vorlage.
```

### Dokumentation
```
Prüfe 06_Metadata/Reference für Dokumentation zu [Thema].
Aktualisiere die Anleitung basierend auf dem, was wir gerade gelernt haben.
```

### Workflow ausführen
```
Führe den wöchentlichen Review-Workflow durch.
Begleite mich durch jeden Schritt.
```

## Pflege

### Regelmäßige Aktualisierungen
- Vorlagen basierend auf Nutzung anpassen
- Neue Workflows dokumentieren sobald sie entstehen
- Veraltete Konfigurationen archivieren
- Referenzdokumente aktuell halten

## Tipps

- **Während des Arbeitens dokumentieren** – Workflows festhalten solange sie frisch sind
- **Vorlagen iterieren** – Basierend auf Nutzung verbessern
- **Einfach halten** – Komplexe Systeme versagen

Metadaten sind das Betriebssystem deines Vaults. Gute Metadaten bedeuten konsistente Struktur, wiederholbare Workflows und skalierbares Wachstum.
