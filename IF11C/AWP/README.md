---
layout: page
title: "AWP"
permalink: /awp/
---
[Dateien](/files/#awp)\
[Klassennotizbuch](https://cryptpad.fr/pad/#/2/pad/edit/a5yHproaBJN8nlJdmNrtfmSL/)\
(Wird aber auch rein kopiert)

- [1. Grundlagen](#1-grundlagen)
  - [LS 1.1 Daten und Datenquellen](#ls-11-daten-und-datenquellen)
  - [LS 1.2 Datenbank Grundlagen](#ls-12-datenbank-grundlagen)
- [2. Datenmodellierung](#2-datenmodellierung)
- [2.1 Phasen der Datenmodelierung](#21-phasen-der-datenmodelierung)
  - [Handlungsschritte](#handlungsschritte)
    - [1. Informieren Sie sich über die einzelnen Phasen der Datenbankentwicklung mit Hilfe des Infotextes](#1-informieren-sie-sich-über-die-einzelnen-phasen-der-datenbankentwicklung-mit-hilfe-des-infotextes)
    - [2. Schreiben Sie Tätigkeiten und Ziele der einzelnen Phasen in der Übersicht zusammen](#2-schreiben-sie-tätigkeiten-und-ziele-der-einzelnen-phasen-in-der-übersicht-zusammen)
      - [1. Anforderungsanalyse](#1-anforderungsanalyse)
      - [2. Konzeptioneller Entwurf](#2-konzeptioneller-entwurf)
      - [3. Logischer Entwurf](#3-logischer-entwurf)
      - [4. Physische Phase](#4-physische-phase)
  - [3. Präsentieren Sie Ihre Ergebnisse](#3-präsentieren-sie-ihre-ergebnisse)
- [3. SQL](#3-sql)

## 1. Grundlagen

### LS 1.1 Daten und Datenquellen

[mebis](https://lernplattform.mebis.bayern.de/course/view.php?id=1162649&section=14#tabs-tree-start)

Arbeitsauftrag: Welche Daten fallen an?

- Metadaten
  - IP Adresse
  - Präferenzen der User
  - Verlauf des Users (Wo hat man zuvor hingeklickt?)   - SchufaPrüfung
  - Browser
  - Betriebssystem
- Bewegungsdaten (ProzessdateLSn)
  - Abschluss einer zusätzlichen Garantie (JA/NEIN)
  - tatsächlichen Bankdaten / Bezahlart
  - Gesamtpreis
  - Rechnungsnummer
  - Zahlungsart
  - Zahlungstermin
  - Liefertermin
  - tatsächliche Lieferadresse
- Stammdaten
  - Kunden-Name, Anschrift (Straße, Wohnort, PLZ)
  - gespeicherten Bankdaten
  - Privat- oder Firmenkunde
  - Preis pro Stück
  - Artikelnummer
  - Alter

Verschiedene Datenmodelle erklärt:\
[XML, JSON und CSV](https://lernplattform.mebis.bayern.de/mod/book/view.php?id=35143828)

### LS 1.2 Datenbank Grundlagen

[mebis](https://lernplattform.mebis.bayern.de/course/view.php?id=1162649&section=15#tabs-tree-start)

Einstieg Lernsituation: Warum nutzen wir Datenbanken?

- Einfacher die Korrektheit der Daten zu gewährleisten (Datenprüfung, automatische Nummerierung,...)
- Bessere Dateneingabe
- Einheitliche Daten
- Mehrere Personen können parallel auf die Datenbank zugreifen
- Unabhängig vom Anwendersystem oder Geräten
- Bessere Strukturierung der Daten
- Effizientere Abfragen von Daten
- Zentrale Datenspeicherung
- Vermeidung von Redundanzen

[Zusammenfassung](./Datenbanken_zusammenfassung.md)

## 2. Datenmodellierung

## 2.1 Phasen der Datenmodelierung

[mebis](https://lernplattform.mebis.bayern.de/course/view.php?id=1162649&section=16#tabs-tree-start)

- ER-Modell erstellen
- Ist/soll Zustand bestimmen
- Größe der Datenbank bestimmen
- Skalierbarkeit der Datenbank definieren
- GUI planen
- Zugriffsverwaltung/Rechtekonzept

### Handlungsschritte

#### 1. Informieren Sie sich über die einzelnen Phasen der Datenbankentwicklung mit Hilfe des [Infotextes](./resources/Datenbanken/020_INF_PhasenDatenbankenwicklung_01b.pdf)

#### 2. Schreiben Sie Tätigkeiten und Ziele der einzelnen Phasen in der Übersicht zusammen

  Phasen anhand [dieses Modelles](./resources/Datenbanken/030_AB_PhasenDatenbankenwicklung.pdf)

##### 1. Anforderungsanalyse

- **Tätigkeiten**
  - Datenformat definieren
  - Ziel der Datenbank bestimmen
  - Anforderungen der Benutzer definieren und Klassifizieren
  - Datenbasis bestimmen
- **Dokumente**
  - Lastenheft/Pflichtenheft

##### 2. Konzeptioneller Entwurf

- **Tätigkeiten**
  - Definition der Datenobjekte mit deren Attributen
  - Bestimmung der Beziehungen (zwischen den Daten)
  - Festlegung des Datanbankmodells
  - Erstellung des ER-Modells
- **Dokumente**
  - Konzepttionelles Gesamtschema
  - ER-Modell

##### 3. Logischer Entwurf

- **Tätigkeiten**
  - Überprüfung des ER-Modells anhand von Transformationsregeln in ein Logisches Modell
  - Überprüfung mit Hilfe der Normalisierung
- **Dokumente**
  - Logisches Datenbankmodell
  - Relationales Datenbankmodell

##### 4. Physische Phase

- **Tätigkeiten**
  - Definition der Speicherstrukturen/Zugriffsmechanismen
  - Implementierung des internen und externen Schemas
  - Zugriffsrechte Festlegen
- **Dokumente**
  - Datenbank
  - SQL-Skript

[Arbeitsblatt Anforderungsanalyse](./resources/Datenbanken/040_AB_Anforderungsdefinition_SuS.pdf)

**Tätigkeit: Informationsstruktur ermitteln**\
  In der erstenPhase der Datenmodell-Entwicklung wird die Informationsstruktur des Datenmodells definiert[Top-down-Ansatz (globales Datenmodell) bzw. Bottom-up-Ansatz (anwendungsorientiertes Datenmodell)]\
  Nennen Sie Möglichkeiten die Informationsstrukturdes Autohauses Nettmannszu ermitteln:

- Bottom-Up-Ansatz:
  - Analyse einzelner Dokumente (Rechnungen, Aufträge etc.)
  - Analyse über bestehende Datenbasis (Excellisten, CSVs etc.)
- Top-Down-Ansatz:
  - In Besprechungen/durch Realitätsbeaobachtungen werden Datenobjekte/Beziehungen definiert

### 3. Präsentieren Sie Ihre Ergebnisse

   [Präsentation](n.a.)

## 3. SQL

(Comming Soon)
