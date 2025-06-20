# Itho Daalderop Amber Heat Pump control module

**Disclaimer:** Deze software is op geen enkele manier verbonden aan het bedrijf Itho Daalderop.

## Samenvatting

Deze repository bevat de firmware voor de *Itho Daalderop Amber Heat Pump control module*. Deze control module is een door ons ontwikkelde hardware oplossing waarmee Itho Daalderop Amber warmtepompen kunnen worden bestuurd. De control module kan [hier](https://electropaultje.nl/product/itho-daalderop-amber-control-module/) besteld worden.

Zodra de control module is aangesloten bestaat de mogelijkheid om sensorwaarden uit te lezen en schakelaars en numerieke waarden in te stellen. De complete lijst met sensoren, schakelaars en numerieke waarden kan [hier](#amber-sensoren-en-schakelaars) gevonden worden.

Het apparaat is gebasseerd op ESPHome. Dit houdt in dat het kan worden geïntegreerd in Home Assistent en kan worden gebruiken in automatiseringen. Er is een gebruikers interface beschikbaar op het [apparaat zelf](http://ithodaalderop-amber.local/) via een webbrowser.

**Let op: de Amber firmware met versie 2.29 bevat een bug waardoor het legionalla schema wordt aangepast als er een instelling wordt geschreven. Het uitlezen van waarden heeft geen gevolgen voor het schema.**

## Verbindingen

De control module heeft rondom een aantal aansluitingen:

**TODO: Add image of control module**

* Modbus verbinding (aan de onderzijde, gemarkeerd met **M**)
* Twee of vier relais (aan de rechterzijde, gemarkeerd met **R1-4**)
* Drie temperatuur sensoren (de drie bovenste aansluitingen aan de linkerzijde, gemarkeerd met **T1-3**)
* Pulssensor aansluiting (de onderste aansluiting aan de linkerzijde, gemarkeerd met **P**)
* USB-C verbinding om de control module van stroom te voorzien

De modbus verbinding wordt gebruikt voor de communicatie tussen de control module en de Amber zelf. De module werkt als enkel de verbinding is aangesloten.

De relais kunnen worden gebruik om de hardware contacten op de Amber aan te sturen (de verwarming, koelen en smart grid verbindingen). Op deze wijze kan de control module gebruikt worden als thermostaat door middel van automatiseringen in Home Assistant of om het tapwater verder te verwarmen als er een zonnestroom overschot is.

De drie aansluitingen voor temperatuur sensoren kunnen worden gebruikt om Dallas DS18B20 sensoren aan te sluiten. Deze kunnen gebruikt worden om extra temperatuurmetingen toe te voegen welke niet door de Amber worden gemeten (bijvoorbeeld de temperatuur van het tapwater dat uit de boiler gaat).

Aan de verbinding voor de pulssensor kan een watersensor worden aangesloten om de stroomsnelheid van het water in het systeem te meten. Gecombineerd met een externe stroommeting kan de COP uitgerekend worden. Compatibele watersensoren zijn [deze](https://www.tinytronics.nl/nl/sensoren/vloeistof/yf-b10-water-flow-sensor-messing-g1).

## Installeren van de control module

### Fysieke installatie

Voor installatiegemak is het mogelijk om de connectors te verwijderen van de control module.

In de onderstaande afbeelding is de modbus verbinding met rood aangegeven:

![Amber connection](/images/amber_connection.jpg)

Verbind de connector M met de Amber computer. Als de control module rechtop gehouden wordt is de linker aansluiting A en de rechter B. Verbind A met de bovenste aansluiting van de modbus verbinding in de Amber en de B met de onderste.

Als de verbindingskit wordt gebruikt is de rode draad de aansluiting A en moet met de bovenste van de twee aangegeven verbindingen worden verbonden. De zwarte gaat vervolgens op de onderste verbinding.

### Verbind de control module met de WiFi

De control module wordt geleverd met de laatste software. Bij de eerste keer opstarten moet het apparaat verbonden worden met het lokale WiFi netwerk.  
Volg hiervoor de volgende stappen:

1. Verbind een mobiele telefoon met het uitgezonden netwerk *IthoDaalderop* en gebruik het wachtwoord *ithodaalderop*. Voor gemak kan ook de volgende QR code worden gescand:  
![qr](/images/qr-wifi.png)
1. Een portal zou moeten openen waarin het correct WiFi netwerk geselecteerd kan worden en het wachtwoord kan worden ingevoerd.  
Mocht deze portal niet automatisch openen, open dan een webbrowser en ga naar het adres [192.168.4.1](http://192.168.4.1/)  
![Captive portal](/images/captive_portal-ui.png)
1. Selecteer het juiste netwerk en voer indien nodig het wachtwoord van het geselecteerde WiFi netwerk in
1. Druk op Save

Zodra het netwerk is gekozen zal het worden opgeslagen op de control module. Als de control module niet kan verbinden met dit netwerk zal na een minuut automatisch het netwerk *IthoDaalder* weer worden uitgezonden. Door bovenstaande stappen te volgen kan de control module dan aan het correcte netwerk gekoppeld worden. Dit kan bijvoorbeeld nodig zijn als er aanpassingen aan het lokale netwerk zijn gemaakt.

### Installeer de control module in Home Assistant

Zodra de control module is verbonden aan het lokale WiFi netwerk zou Home Assistant het apparaat moeten detecteren. Dit wordt aangegeven in het menu:

![New devices discoverd](/images/hass-new-device-discoverd-en.png)

Door op *Check it out* te klikken zal de integraties pagina openen.

![Configure device](/images/hass-add-device-nl.png)

Klikken op *Configureren* zal de installatie in Home Assistant starten.

Mocht de control module niet automatisch gedetecteerd worden door Home Assistant, dan is het mogelijk om deze [handmatig te installeren](https://my.home-assistant.io/redirect/config_flow_start?domain=esphome).  
Gebruik de volgende gegeven om het apparaat te installeren:

![ESPHome configuration](/images/hass-config-esphome-nl.png)

## Firmware updates

Zodra een update beschikbaar is zal dit in Home Assistant gemeld worden (vanaf versie 2024.7.0).

![Update available](/images/hass-update-device-nl.png)

*Een update is ook zichtbaar in de gebruikers interface op het apparaat zelf. Op dit moment is het niet mogelijk om vanaf deze pagina met een druk op de knop de control module te updaten. Door de laatste software van GitHub te downloaden en handmatig te updaten kan het apparaat alsnog worden bijgewerkt buiten Home Assistant om.*

## Amber sensoren en schakelaars

De namen van de sensoren zijn in het Engels.

### Numerieke sensoren (alleen lezen)

* Inside temperature (room temperature)
* Ambient temperature (outside temperature)
* Domestic hot water temperature (Tw)
* Heating/cooling temperature (Tc)
* Heat exchanger water outlet temperature (Tuo)
* Heat exchanger water inlet temperature (Tui)
* Indoor coil temperature (Tup)
* Heating/cooling circuit 1 temperature (Tv1)
* Heating/cooling circuit 2 temperature (Tv2)
* Outdoor coil temperature (Tp)
* Discharge temperature (Td)
* Suction temperature (Ts)
* High pressure (Pd)
* Low pressure (Ps)
* Compressor working speed
* Fan 1 working speed
* Expansion valve setting
* Supply voltage
* Running current
* Average 1h ambient temperature
* Average 4h ambient temperature
* Average 24h ambient temperature
* SG increase setpoint domestic hot water
* SG decrease setpoint cooling
* SG increase setpoint heating
* Actual setpoint heating zone 1 (*only a valid value when heating is active*)
* Actual setpoint heating zone 2 (*only a valid value when heating is active*)
* Actual setpoint cooling zone 1 (*only a valid value when cooling is active*)
* Actual setpoint cooling zone 2 (*only a valid value when cooling is active*)

### Binaire sensoren (aan / uit, alleen lezen)

* Heating switch
* Heating switch circuit 2
* Cooling switch
* Defrost
* Domestic hot water in progress
* Heating in progress
* Cooling in progress
* Water flow switch
* SG ready

### Schakelaar (aan / uit)

* System on/off
* Domestic hot water mode (M9.01)
* Heating mode (M9.02)
* Cooling mode (M9.03)
* Use heating curve (M1.05)
* Domestic hot water ECO mode (M3.09)
* Use domestic hot water timer (M4.01)
* Reduced mode timer (M5.04)
* Use anti legionella mode (M6.01)

### Numerieke waarden

* Delta T to stop heat pump (M1.01)
* Delta T to restart heat pump (M1.02)
* Delta T to lower compressor speed (M1.03)
* Domestic hot water setpoint (M3.01)
* Domestic hot water reheating point (M3.02)
* Heating curve ambient temperature (1 through 5; M1.06-M1.10; **works for Amber version 2.29 and higher**)
* Heating curve water temperature (1 through 5; M1.11-M1.15; **works for Amber version 2.29 and higher**)
* Cooling setpoint (M1.04; for when cooling curve is not used)
* Heating setpoint (M1.19; for when heating curve is not used)
* Minimum ambient temperature to start domestic hot water ECO mode (M3.10)
* Circuit 1 minimum temperature (M1.20)
* Circuit 1 maximum temperature (M1.21)

### Selectiebox

* Working mode (Heating, Cooling, Domestic hot water, Auto)

### Berekende waarden

* Delta T  
  *Verschil tussen Tui en Tuo*

### Configuratie instellingen

* Flow sensor calibration  
  *Zet deze op het aantal pulsen per liter als de pulssensor is aangesloten om zo correct het aantal liter en de doorstroming te kunnen berekenen*
* Dallas temperature offset (1 through 3)  
  *Gebruik deze instellingen om de aangesloten temperatuur sensoren correct te kalibreren*
* Yellow LED status  
  *Stel de functie in van de gele LED op de control module*

## ESPHome configuratie

De control module wordt voorgeprogrammeerd geleverd. Het is mogelijk om zelf de configuratie via YAML aan te passen. Hiervoor is van de laatste versie de configuratie in deze repo te vinden ([2 relais](/firmware-2relay/firmware-2relay.yaml), [4 relais](/firmware-4relay/firmware-4relay.yaml)). Zodra gebruik gemaakt wordt van een eigen configuratie zal bij een update de eigen configuratie weer overschreven worden.  
**Let op: Er wordt geen support geleverd op zelf aangebrachte wijzigingen.**