---
layout: default
title: "ITS"
permalink: /its/
---
[Zurück](/)\
[Dateien](/files#its)\
[Klassennotizbuch](https://ip-generation.de/Kip94IKYTnKIWyZXzWWyUw?both)\
[subnetz rechner](https://www.site24x7.com/tools/ipv4-subnetcalculator.html)

- [LS 1](#ls-1)
  - [ITS](#its)
    - [Vorteile Client-Server-Systeme](#vorteile-client-server-systeme)
    - [Fragen an den Kunden](#fragen-an-den-kunden)
  - [LS 1.1: Autohaus mit Server](#ls-11-autohaus-mit-server)
  - [LS 1.3: Active Directory](#ls-13-active-directory)
  - [LS 1.6: Rechte und Berechtigungen](#ls-16-rechte-und-berechtigungen)
  - [LS 1.10: Automatisch verteilt: DHCP](#ls-110-automatisch-verteilt-dhcp)
- [LS2](#ls2)
  - [LS2.1 Datenschutz und -Sicherheit](#ls21-datenschutz-und--sicherheit)
  - [LS2.2 Netzwerke](#ls22-netzwerke)
  - [LS 2.3](#ls-23)
    - [LS 2.3.3 Weiterführende Themen: VLSM und CIDR](#ls-233-weiterführende-themen-vlsm-und-cidr)
  - [LS 2.5 Routing](#ls-25-routing)
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

### LS2.1 Datenschutz und -Sicherheit

- Welche Chancen und Gefahren ergeben sich aus der Nutzung von Kfz-Daten
- Welche Interessen verfolgt die Industrie?
  - Sammeln von so vielen Daten wie möglich um den Kunden Genau zu verstehen
- Welche Interessen, Vor- und Nachteile, Risiken sehen Sie für den Konsumenten?

### LS2.2 Netzwerke

1. Ordnen Sie den Systemen im lokalen Netzwerk geeignete IPv4-Adressen zu (IP-Adresse und Netzmaske1).
   - 192.168.1.1: Server, 192.168.1.11: Drucker, 192.168.1.101 & 192.168.1.102: Clients
   - 192.168.2.101 & 10.0.2.102: Clients, 192.168.2.201: Tester
2. Begründen Sie, wie viele Hostadressen in jedem IP-Netz zur Verfügung stehen.
   - 2^n - 1, wobei n anzahl hostbits (32 - maske): 244 clients
3. Geben Sie jeweils die Netz- und Broadcastadresse an und erklären Sie die Begriffe.
   - 192.168.0.0 Netzadresse: Adresse bei der alle hostbits 0 sind
   - 192.168.255.255 Broadcastadresse: AAdresse bei der alle hostbits 1 sind
4. Begründen Sie wie viele Broadcastdomänen im lokalen Netzwerk existieren.
   - Zwei, da wir mehrere subnetze haben

Aufgaben:

1. Schritweise des Netzes 212.114.150.64/30:
   - 1011 0100.0111 0010.1001 0110.0000 00|00 = 212.114.150.0
   - 1011 0100.0111 0010.1001 0110.0000 01|00 = 212.114.150.4
   - 1011 0100.0111 0010.1001 0110.0000 10|00 = 212.114.150.8
   - 1011 0100.0111 0010.1001 0110.0000 11|00 = 212.114.150.12
   - Schrittweite von 4
2. Folgendes netz (192.168.100.0/24) so unterteilen, dass der Kunde sechs subnetze hat (maximal mögliche Hosts):
   | Netzadresse | Subnetzmaske | Hostbereich | Broadcastadresse |
   | ----------- | ------------ | ----------- | ---------------- |
   | 192.168.100.0 | 192.168.100.0/27 | 1 - 30 | 192.168.100.31 |
   | 192.168.100.32 | 192.168.100.32/27 | 33 - 62 | 192.168.100.63 |
   | 192.168.100.64 | 192.168.100.64/27 | 65 - 94 | 192.168.100.95 |
   | 192.168.100.96 | 192.168.100.96/27 | 97 - 126 | 192.168.100.127 |
   | 192.168.100.128 | 192.168.100.128/27 | 129 - 158 | 192.168.100.159 |
   | 192.168.100.160 | 192.168.100.160/27 | 161 - 190 | 192.168.100.191 |

3. Ein PC besitzt folgende IP Konfiguration (192.168.22.111/26), das Gateway soll die letze adresse im Netz sein. Nenne Netz-, Gateway- und Broadcastadresse:
   - 1111 1111.1111 1111.1111 1111.11|00 0000 = 255.255.255.192
   - 1100 0000.1001 0000.0001 0110.01|10 0110 = 192.168.22.111
   - 1100 0000.1001 0000.0001 0110.01|11 1110 = 192.168.22.126

4. [Aufgabe 4]
5. mind. 80 Subnetze in 130.10.0.0
6. 127.16.200.10 /20
   - Anzahl host: 32 - 20 = 12, 2^12 -2 = 4096 - 2 = 4094
   - Netzadresse: 127.16.192.0
   - Broadcastadresse: 127.16.207.255
7. 135.20.0.0/16
   - 135.20.0000 0000.0|000 0000 -> /16 + 9 = 25
    | Netzadresse | Subnetzmaske | Hostbereich | Broadcastadresse |
    | ----------- | ------------ | ----------- | ---------------- |
    | 135.20.0.0  | 135.20.0.0/25| 1 - 126 | 135.20.0.127 |
    | 135.20.0.128| 135.20.0.128/25 | 129 - 254 | 135.20.0.255 |
    | ... | ... | ... | ... |
    | 135.20.249.128 | 135.20.249.128/25 | 129 - 254 | 135.20.249.255 |
    | 135.20.250.0 | 135.20.250/25 | 1 - 126 | 135.20.250.127 |

### LS 2.3

#### LS 2.3.3 Weiterführende Themen: VLSM und CIDR

1. Einem ISP (Internet-Service-Provider) steht zur Versorgung von vier Kunden folgendes IP-Netz zur Verfügung: 210.20.16.0 /24
  Der Bedarf an IP-Adressen bei den einzelnen Kunden sieht wie folgt aus:
  Kunde A: 100 IP-Adressen -> 210.20.16.126 /25
  Kunde B: 50 IP-Adressen -> 210.20.16.190 /26
  Kunde C: 29 IP-Adressen -> 210.20.16.222 /27
  Kunde D: 23 IP-Adressen -> 210.20.16.254 /27

2. Die Netze der Kunden  A/B/C/D  sind über den Internetserviceprovider ISP1 angebunden. Die Kunden verwalten Netze mit unterschiedlichen Größen. Alle Teilnetze der Kunden fasst der Router ISP1 dann in einen Routingeintrag zusammen, um diesen an den Router ISP2 zu kommunizieren.
  191.168.0.0/23 -> 10111111.10101000.0000|000|0.00000000
  191.168.2.0/23 -> 10111111.10101000.0000|001|0.00000000
  191.168.4.0/22 -> 10111111.10101000.0000|01|00.00000000
  191.168.8.0/21 -> 10111111.10101000.0000|1|000.00000000
  -> *10111111.10101000.0000*0000.00000000 /20 -> 191.168.0.0 /20

### LS 2.5 Routing

[Mebis](https://lernplattform.mebis.bayern.de/mod/page/view.php?id=36431018)

| Ziel-IP-Adresse | Maske         | Gateway        | Schnittstelle | Metrik |
|-----------------|---------------|----------------|---------------|--------|
| 192.168.70.0    | 255.255.255.0 | 192.168.70.254 | Eth_0         | 0      |
| 192.168.50.0    | 255.255.255.0 | 192.168.50.254 | Eth_1         | 0      |

Routing mit mehreren Routern:
Router 1:
| Ziel-IP-Adresse | Maske         | Gateway        | Schnittstelle | Metrik |
|-----------------|---------------|----------------|---------------|--------|
| 192.168.70.0    | 255.255.255.0 | 192.168.70.254 | Eth_0         | 0      |
| 192.168.60.0    | 255.255.255.0 | 192.168.60.254 | Eth_1         | 0      |
| 192.168.50.0    | 255.255.255.0 | 192.168.50.254 | Eth_1         | 1      |

Router 2:
| Ziel-IP-Adresse | Maske         | Gateway        | Schnittstelle | Metrik |
|-----------------|---------------|----------------|---------------|--------|
| 192.168.50.0    | 255.255.255.0 | 192.168.50.254 | Eth_0         | 0      |
| 192.168.60.0    | 255.255.255.0 | 192.168.60.254 | Eth_0         | 0      |
| 192.168.70.0    | 255.255.255.0 | 192.168.70.254 | Eth_1         | 1      |

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
