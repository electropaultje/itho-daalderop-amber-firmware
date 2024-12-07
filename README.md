# Itho Daalderop Amber Heat Pump control module

**Disclaimer:** This software is not in any way affiliated to the Itho Daalderop company.

## Summary

This repository contains the firmware for the *Itho Daalderop Amber Heat Pump control module*. This control module is a custom made hardware solution to control the Amber heat pump. The control module can be ordered [here](https://forms.gle/3R2AAtGyy7Cqq65Q9).

When connected, you have the ability to read out sensor values and control switches and numeric values. The complete list of sensors, switches and numeric values can be found [here](#amber-sensors-and-switches).

The device is based on ESPHome, this means it can be integrated in Home Assistant and can be used in automations. A user interface is available on the [device itself](http://ithodaalderop-amber.local/) through a browser.

**Please be advised that the Amber firmware version 2.29 has a bug which has the effect that the legionalla prevention schema is corrupted when writing values to the Amber. Reading of the values does not alter the schema.**

## Connections

The module has several connections:

**TODO: Add image of control module**

* Modbus connection (on the lower side of the device, marked **M**)
* Two or four relays (on the right side of the device, marked **R1-4**)
* Three temperature sensor connection (the upper three connection on the left side, marked **T1-3**)
* Pulse sensor connection (the lower connection on the left side, marked **P**)
* USB-C connection for powering the device

The modbus connection is used for the communication between the module and the Amber itself. The module can and will work perfectly when only this connection is made.

The relays can be used to control the hardware contacts on the Amber (the heating, cooling and smart grid connections). This way the module can be used as a thermostat through automations in Home Assistant or heat the boiler when there is a PV surplus.

The three temperature sensors can be connected to Dallas DS18B20 temperature sensors. These can be used to monitor extra temperature values which are not registered by the Amber (for example the temperature of the hot water exiting the DHW boiler).

The pulse sensor connection can be used to connect a flow sensor to determine the flow in the system. In combination with an external power reading the COP can be calculated this way. Compatible flow sensors are [these](https://www.tinytronics.nl/nl/sensoren/vloeistof/yf-b10-water-flow-sensor-messing-g1).

## Installing the control module

### Physical installation
For ease of installation, it is possible to remove the connectors from the control module.

In the image below the modbus connection is highlighted in red:

![Amber connection](/images/amber_connection.jpg)

Connect the connection M to the Amber computer. When holding the control module upright, the left connection is A and the right is B. Connect A to the upper modbus connection in the Amber and B in the lower one.

When using the connection kit, A is the red wire and should be connected to the topmost connection of the indicated positions.

### Connect the control module to the WiFi

The control module comes preinstalled with the latest software. When first powered on the device must be connected to your personal WiFi network. To do this follow the following steps:

1. Connect your phone to the broadcasted network *IthoDaalderop*, use the password *ithodaalderop*. You can also scan the following QR code:  
![qr](/images/qr-wifi.png)
1. A portal should open in which you can select the correct WiFi network and enter the password.  
If this portal does not open automatically, open a browser and go to the address [192.168.4.1](http://192.168.4.1/)  
![Captive portal](/images/captive_portal-ui.png)
1. Select the correct network and enter the password if needed
1. Press Save

Once the network is selected it will be stored on the control module. If the control module can not connect to the configured network after one minute it will start broadcasting the IthoDaalderop network again and you can follow the above steps to select the correct new network. This is for example the case when you make changes to your home network.

### Install the control module in Home Assistant

Once the control module is connected to the WiFi Home Assistant should detect the control module. You will be notified in the menu:

![New devices discoverd](/images/hass-new-device-discoverd-en.png)

By clicking on *Check it out* the Integration page will be openend.

![Configure device](/images/hass-add-device-en.png)

Clicking on *Configure* will start the installation in Home Assistant.

Should the control module not be automatically detected by Home Assistant, you can [manually install it](https://my.home-assistant.io/redirect/config_flow_start?domain=esphome).  
Use the following details to install the control module:

![ESPHome configuration](/images/hass-config-esphome-en.png)

## Firmware updates

When an update is available, this will be shown in Home Assistant (needed version 2024.7.0 or later). 

![Update available](/images/hass-update-device-en.png)

*An update will also be shown in the web interface of the control module. It is at this moment not possible to automatically update the control module. You have to download the latest firmware from GitHub and upload it yourself through the web interface.*

## Amber sensors and switches

### Read only numeric sensors

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

### Readonly binary sensors (on / off)

* Heating switch
* Heating switch circuit 2
* Cooling switch
* Defrost
* Domestic hot water in progress
* Heating in progress
* Cooling in progress
* Water flow switch
* SG ready

### Switches (on / off)

* System on/off
* Domestic hot water mode (M9.01)
* Heating mode (M9.02)
* Cooling mode (M9.03)
* Use heating curve (M1.05)
* Domestic hot water ECO mode (M3.09)
* Use domestic hot water timer (M4.01)
* Use anti legionella mode (M6.01)

### Numeric values

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

### Dropdown value

* Working mode (Heating, Cooling, Domestic hot water, Auto)

### Calculated values

* Delta T  
  *Difference between Tui and Tuo*
* Calculated heating temperature  
  *Interpolated heating setpoint based on the heating ambient and water temperatures and the ambient temperature.*

### Configuration settings

* Flow sensor calibration  
  *Set to the number of pulses per liter when the pulse sensor is connected to correctly calculate the liters and flow*
* Dallas temperature offset (1 through 3)  
  *Use to offset the connected temperature sensors when they need to be corrected because of calibration differences*
* Yellow LED status  
  *Set the function of the yellow LED on the control module*
* Allow anonymouse usage statistics  
  *Allow once every six hours to send anonymized usage statistics (MAC address of the control module, firmware versions, number of connected temperature sensors, modbus reads and writes and state of the onboard memory).  
  **No data is stored that can be linked to the installation!***

## ESPHome configuration

The controle module will be delivered preprogrammed. It is possible to make changes to the configuration by adding the YAML configuration into ESPHome yourself. The last used configuration can be found in this repository ([2 relay](/firmware-2relay/firmware-2relay.yaml), [4 relay](/firmware-4relay/firmware-4relay.yaml)).  
**Note: no support is given on self made changes**