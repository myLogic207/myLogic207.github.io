# Datenbanken

## Definitionen

###### Datenintegration

Daten aus verschiedenen Quellen werden zu einer Datenbank zusammengeführt

##### Prozessintegration

Mehrere Teilprozesse werden zu einem Gesamtprozess zusammengeführt

##### Integrierte Informationsverarbeitung

Zusammenführung der Datenintegration und der Prozessintegration

## Wissenspyramide

#### Daten

"Rohmaterial", unverknüpfte Daten

#### Informationen

Aussagen/Daten die mit einer gewissen Bedeutung verknüpft wurden, Strukturierte Daten

#### Wissen

Informationen mit intelligentem Netzwerk, Informationen wurden mit Kontext und Erfahrungen verknüpft, Wissen kann zu Entscheidungen/Aktionen führen

## Datenbankmodelle

#### Hierarchisches Datenbankmodell

- Abbildung der realen Welt
- Realisierung durch hierarchische Baumstruktur
- Jeder Satz hat genau einen Vorgänger (one parent, multiple childs)
- Nachteil: keine Beziehungen darstellbar

#### Relationales Datenbankmodell

- Sammlung aus Tabellen
- Tabellen bestehen aus Datensätzen, die eindeutig identifizierbar sind
- keine Parent-Child-Beziehungen
- Mehrere Tabellen können in Beziehung stehen
- Abfragesprache: **SQL**

#### Netzwerkartiges Datenbankmodell

- Erfordert keine strenge Hierarchie
- kein Root-Objekt
- Multiple Parents, multiple Childs

#### Objektorientiertes Datenbankmodelle

- Basiert auf OOP
- Objekte einer Anwendung können ohne Konvertierung gespeichert werden

#### No-SQL Datenbanken

- Key-value Pärchen
- Dokumentenorientiert
- Spaltenorientiert
- Graphendatenbanken (ähnlich Netzwerkartig)

## Datenaustauschformate

- XML, JSON und CSV
- XML-Dokumente besitzen immer ein Root-Objekt (umschließt gesamte Datei)
- besitzen vor Root-Element eine Versionsdeklaration
- JSON: True & False sind case-sensitive ( : true & : false)

## Ziele der Datenorganisation

1. Datenunabhängigkeit (Daten existieren unabhängig von der Anwendung, verschiedene Anwendungen greifen auf gleiche Datenbank zu)
2. Benutzerfreundlichkeit (leicht zu erlernende Benutzersprachen, grafische Oberfläche)
3. Mehrfachzugriff (jeder mit Autorisierung darf in Echtzeit auf Daten zugreifen, simultaner Readzugriff)
4. Dateneffizienz (Zeiten für Abfragen müssen kurz sein, nur relevante Daten speichern, klare Organisation, zentrale Speicherung, geregelte Datenpflege)
5. Datenschutz (Persönliche Daten vor unberechtigtem Zugriff geschützt, Schutz vor Zugriff)
6. Datensicherheit (Daten müssen durch Backups und Recoveries gesichert werden, Schutz vor Datenverlust)
7. Datenintegrität (Daten müssen korrekt, vollständig, konsistent und widerspruchsfrei vorliegen, Änderungen müssen dokumentiert werden)
8. Redundanzfreiheit (jede Information kommt nur einmal vor)
9. Flexibilität (Daten müssen flexibel miteinander verknüpfbar sein)

Datenschutz kann nur duch Datensicherheit aufrecht erhalten werden.

## ANSI Architekturmodell

- American National Standards Institute (Normenaussschuss der USA)
- Aufgeteilt in Datenbasis und DBMS (Datenbasis - Speicher für Daten, DBMS - Verwaltungssoftware)

#### Fünf Funktionen eines Datenbanksystems

- Datendefinition (Strukturaufbau)
- Datenmanipulation (Datenabänderung)
- Datenabfrage (Datenlesezugriff)
- Datenkontrolle ()
- Datenübertragung ()

#### 3-Sichten-Modell

- Externe Ebene (Benutzersichten, Software) -> Benutzerdefinierte Sichten
- Konzeptionelle Ebene (logische Sicht, Datenmodellebene)
- Interne Ebene (physische Sicht, File-Ebene) -> Read/Write-Geschwindigkeiten
- Interne Ebene von Konzeptioneller und Externer Ebene getrennt -> keine Auswirkungen von Datenträgerwechsel auf Benutzersicht oder Datenmodell
