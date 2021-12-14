---
layout: default
title: "ITS"
permalink: /its/
---
[Zurück](/)\
[Dateien](/files#its)\
[Klassennotizbuch](https://ip-generation.de/Kip94IKYTnKIWyZXzWWyUw?both)

- [LS 1](#ls-1)
  - [ITS](#its)
    - [Vorteile Client-Server-Systeme](#vorteile-client-server-systeme)
    - [Fragen an den Kunden](#fragen-an-den-kunden)
  - [LS 1.1: Autohaus mit Server](#ls-11-autohaus-mit-server)
  - [LS 1.3: Active Directory](#ls-13-active-directory)
  - [LS 1.6: Rechte und Berechtigungen](#ls-16-rechte-und-berechtigungen)
  - [LS 1.10: Automatisch verteilt: DHCP](#ls-110-automatisch-verteilt-dhcp)
- [LS2](#ls2)
  - [Datenschutz und -Sicherheit](#datenschutz-und--sicherheit)
  - [Gruppen Labor Herbst](#gruppen-labor-herbst)
  - [Gruppen Labor Graf](#gruppen-labor-graf)

<!-- ## sponsored by [noris network AG](https://www.noris.de/) -->

## LS 1

### ITS

#### Vorteile Client-Server-Systeme

Hauptvorteile:

- Zentrale Datenablage- u. Sicherung
- Zentrale Benutzerverwaltung
- Serverbasierte Dienste u. Anwendungen,
  wie z.B. Druckdienst, Maildienst, DHCP,
  Distribution von Installationspaketen, etc.
- Richtlinien- u. Zugriffssteuerung
  (z.B. via Gruppenrichtlinien)

Diese Vorteile führen zu weiteren positiven Merkmalen:

- Bessere Zugriffssicherheit
- Einfachere Administration u. Wartung
- Gut skalierbar (Stabile Struktur)

#### Fragen an den Kunden

- Wie viele PC's?
  - Eigentlich 32
  - -> 8 Clients
- Brauchen Sie einen Exchange Server?
  - Wird nicht benötigt (extern)
- Welche Art von PC's (Tower, Workstation, Thin Client)?
  - Desktop-PCs (Tower)
- Welche Benutzerrollen werden benötigt? (AD)
  - Detailiertes Rechtekonzept
- Budget?
  - Erstmal irrelevant
- Redundanz?
  - Erstmal irrelevant
  - Theoretisch durch replizieren denkbar
- Komplexität des Netzwerks?
  - Einfaches Netzwerk
- Laufwerkkonzept
  - Benötigt, Erklärung folgt
- Soll ein Netzwerkspeicher bereitgestellt werden?
  - Wird benötigt, läuft auf haupt Server
- Homeoffice benötigt? (VPN-Verbindung)
  - Wird nicht benötigt
- Gebäudeplan?
  - Denkbar
- Terminal Server(?)
  - kein Terminalserver
- Intranet/Website auf dem Server?
  - Nicht Benötigt
- vor Ort oder als Cloud-Lösung
  - Vor Ort
- WLAN? - APs
  - Folgt später
- Nur im internen Netz erreichbar?
  - ?
- Physische Clients oder virtuelle Computer?
  - VMs
- WINDOWS LINUX MACOS?
  - Windows

![Serverplanung](../IF11C/ITS/resources/image/Serverplanung.png)

### LS 1.1: Autohaus mit Server

[mebis](https://lernplattform.mebis.bayern.de/mod/page/view.php?id=34978720)

Benutzer:
![Benutzerliste](https://rgw.noris.net/hedgedoc-prod/uploads/upload_47795d321f3b661120e2f2922f9d1e0b.png)

![Benutzerliste2](https://rgw.noris.net/hedgedoc-prod/uploads/upload_bbfaf13cdb5eeb4ffe7f1ec45ec4d283.png)

Gruppen:
![Gruppenliste](https://rgw.noris.net/hedgedoc-prod/uploads/upload_aed8a9e3409716993265f9369857e043.png)

Client-Konfiguration:
![clients](https://rgw.noris.net/hedgedoc-prod/uploads/upload_837e5ef9c457fd3c7bcc2587638a8e07.png)

Ordnerstruktur:
![Ordner](https://rgw.noris.net/hedgedoc-prod/uploads/upload_e71c17ded4e32bf770edff6d23453daa.png)

Rechtemanagement:
![Rechte](https://rgw.noris.net/hedgedoc-prod/uploads/upload_b5abebb8a0856da507f04e16824a152c.png)

### LS 1.3: Active Directory

[mebis](https://lernplattform.mebis.bayern.de/mod/page/view.php?id=34978722)

**Gliederung Autohaus Nettmann in einer Domäne
und jeweils eine OU für die Abteilung**

![Aufgabe 2](https://rgw.noris.net/hedgedoc-prod/uploads/upload_fafe608fb51dfa686371e0c4c6ca4937.jpg)

### LS 1.6: Rechte und Berechtigungen

[mebis](https://lernplattform.mebis.bayern.de/mod/page/view.php?id=35737949)

|  Freigabe  |  NTFS  |
| :--------: | :----: |
| Jeder Voll | Rechte wie gewünscht einstellen |
| Rechte Kummulativ: | |
| z.B Jeder Voll <br> Azubi Lesen <br> => Vollzugriff | |
| -> Sind beide Systeme ativ wirkt die größere Einschränkung | |

### LS 1.10: Automatisch verteilt: DHCP

[mebis](https://lernplattform.mebis.bayern.de/mod/page/view.php?id=35316070)

**Vorteil**:

- Einsparung von IP-Adressen
- Geringer Aufwand für Administration
- Flexibilität (ortswechsel) einfacher möglich
- Zentrale Verwaltung möglich
- Keine Doppelvergabe von IP-Adr.

**Wichtiger Befehl**: ipconfig bzw. ipconfig /all
Dynamische Zuweiseung:
  Automatische Zuweisung einer IP-Adr. aus einem Pool von Adr.\
**Statische Zuweisung**:
  Zuweisung einer festen IP-Adr. via *Reservierung* mit hilfe der MAC-Adr.

**Weitere Stichworte**:
  APIPA-Adresse (Automatic Private IP Adressing) - 169.254.0.0\
  Broadcastdomäne

Das Abrufen einer IP-Adresse erfolgt nach einem festen vorgegebenen Schema. Das Protokoll sieht dazu vier Schritte vor:

1. **IP-Anforderung (DHCP-Discover)**
   Der ***DHCP-Client*** sucht per Broadcast (ff-ff-ff-ff-ff-ff bzw. 255.255.255.255) nach einem ***DHCP-Server***. Seine MAC-Adresse ist Absendeadresse. Da der Client selbst noch keine IP-Adresse besitzt, verwendet er die 0.0.0.0 .\
   <span style="font-size: small; color: rgb(128, 128, 128">
    Hinweis:  DHCP nutzt das Protokoll UDP, Ports 67+68
   </span>
2. **IP-Angebot (DHCP-Offer)**
   Der oder die gefundene/n DHCP-Server melden sich mit einem DHCP-Offer. Dieses enthält die notwendigen Netzwerkeinstellungen, wie z.B. IP-Adresse, Subnetzmaske, Standardgateway und IP-Adresse des DNS-Servers. Ergänzt werden die Informationen durch die Lease-Dauer. Diese gibt die Zeit an, für die die Adresse im Netzwerk gültig ist.
3. **IP-Nachfrage (DHCP-Request)**
   Sobald der Client das Angebot eines DHCP-Servers erhalten bzw. sich für ein Angebot entschieden hat, teilt er diese Entscheidung allen DHCP-Servern per Broadcast mit.
4. **IP-Bestätigung (DHCP-Acknowledge)**
   Um die Konfiguration der Netzwerkeinstellungen eines Client abschließen zu können, schickt der DHCP-Server eine Bestätigung an den Client. Damit wird sichergestellt, dass auf beiden Seiten die Daten bekannt und gültig sind. Der DHCP-Prozess ist damit abgeschlossen.

|   | ***CLIENT***      |                 | <-<br>-> | ***SERVER***      |                 |
|---|-------------------|-----------------|----------|-------------------|-----------------|
|   | **MAC**           | **IP**          |          | **MAC**           | **IP**          |
| 1 | B8-E9-37-A6-CA-A0 | 0.0.0.0         | --<br>-> | FF-FF-FF-FF-FF-FF | 255.255.255.255 |
| 2 | FF-FF-FF-FF-FF-FF | 255.255.255.255 | <-<br>-- | 94-9F-3E-7C-1E-4C | 192.168.99.1    |
| 3 | B8-E9-37-A6-CA-A0 | 0.0.0.0         | --<br>-> | FF-FF-FF-FF-FF-FF | 255.255.255.255 |
| 4 | FF-FF-FF-FF-FF-FF | 255.255.255.255 | <-<br>-- | 94-9F-3E-7C-1E-4C | 192.168.99.1    |

## LS2

### Datenschutz und -Sicherheit

- Welche Chancen und Gefahren ergeben sich aus der Nutzung von Kfz-Daten
- Welche Interessen verfolgt die Industrie?
  - Sammeln von so vielen Daten wie möglich um den Kunden Genau zu verstehen
- Welche Interessen, Vor- und Nachteile, Risiken sehen Sie für den Konsumenten?

---

### Gruppen Labor Herbst

| Gruppe | Mitglieder              | IP-Adresse       | Server |
| :----: | ----------------------- | ---------------- | :----: |
| 1      | Aris                    | 192.168.6.1/24   | **X**  |
|        | Sebastian               | 192.168.6.11/24  |        |
|        | Alwinci                 | 192.168.6.12/24  |        |
| 2      | Tea                     | 192.168.7.11/24  |        |
|        | Rita                    | 192.168.7.12/24  |        |
|        | Hoang                   | 192.168.7.1/24   | **X**  |
| 3      | Bayer, Nico             | 192.168.8.11/24  |        |
|        | Hingelbaum, Florian     | 192.168.8.1/24   | **X**  |
|        | Hingelbaum, Florian     | 192.168.8.13/24  |        |
|        | Tränkler, Benjamin      | 192.168.8.12/24  |        |
| 4      | Bühner, Lukas           | 192.168.9.11/24  |        |
|        | Nguyen, Max             | 192.168.9.1/24   | **X**  |
| 5      | Maria                   | 192.168.10.1/24  | **X**  |
|        | Kai                     | 192.168.10.11/24 |        |

---

### Gruppen Labor Graf

| Gruppe |     Mitglieder    | Netzadresse  |Inventarnummer| Verantwortlich für |
| :----: |     ---------     | -----------  |--------------|--------|
|   1    | Tobias Mayer      | 192.162.1.16 |  00054575    | Server |
|        | Viet Nguyen       | 192.162.1.18 |  00054580    | Client |
|        | Michael Heidler   | 192.162.1.14 |  00054594    | Client |
|   2    | Sandra            | 192.168.2.22 |  00054572    | Client |
|        | Lijon             | 192.168.2.29 |  00054581    | Server |
|   3    | Moritz v d Grün   | 192.168.3.4  |  00054586    | Server |
|        | Julian Vogl       | 192.168.3.6  |  00054589    | Client |
|        | Alisa Dinkel      | 192.168.3.2  |  00054583    | Client |
|   4    | Alexander B       | 192.168.4.30 |  00054587    | Client |
|        | Philip T          | 192.168.4.32 |  00054596    | Client |
|        | Tobias W          | 192.168.4.26 |  00054585    | Server |
|   5    | Felix             | 192.168.5.12 |  00054588    | Client |
|        | Dominik           | 192.168.5.13 |  00054584    | Client |
|        | Josiah            | 192.168.5.8  |  00054591    | Server |
