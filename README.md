# Itho Daalderop Amber Heat Pump control module

## Summary

This repository contains the firmware for the *Itho Daalderop Amber Heat Pump control module*. This module is a custom made hardware solution to control the Amber heat pump. The module can be ordere [here](https://forms.gle/3R2AAtGyy7Cqq65Q9).

When connected, you have the ability to read out sensor values and control switches and numeric values. The complete list of sensors, switches and numeric values can be found here.

The device is based on ESPHome, this means it can be integrated in Home Assistant and can be used in automations. A user interface is available on the device itself through a browser.

**Please be a advised that the Amber firmware version 2.29 has a bug which has the effect that the legionalla prevention schema is corrupted when writing values to the Amber.**

## Connections

The module has several connections:

* Modbus connection
* Two or four relays
* Three temperature sensor connection
* Pulse sensor connection

The modbus connection is used for the communication between the module and the Amber itself. The module can and will work perfectly when only this connection is made.

The relays can be used to control the hardware contacts on the Amber (the heating, cooling and smart grid connections). This way the module can be used as a thermostate through automations in Home Assistant or heat the boiler when there is a PV surplus.

The three temperatur sensors can be connected to Dallas DS18B20 temperature sensors. These can be used to monitor extra temperature values which are not registered by the Amber (for example the temperature of the hot water exiting the DHW boiler).

The pulse sensor connection can be used to connect a flow sensor to determine the flow in the system. In combination with an external power reading the COP can be calculated this way. Compatible flow sensors are [these](https://www.tinytronics.nl/nl/sensoren/vloeistof/yf-b10-water-flow-sensor-messing-g1).

## Firmware updates

When an update is available, this will be shown in Home Assistant (needed version 2024.7.0 or later).

## Installing the control module

**TODO: Explain how to connect the module to the Amber**

Connect the connection M to the Amber computer.

![Amber connection](/images/amber_connection.jpg)

## Amber sensors and switches

### Read only numeric sensors

* Inside temperature (room temperature)
* Ambient temperature
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
* Heating curve ambient temperature (1 through 5)
* Heating curve water temperature (1 through 5)
* Supply voltage
* Running current

### Readonly binary sensors (on / off)

* Heating switch
* Cooling switch
* Defrost
* Domestic hot water in progress
* Heating in progress
* Cooling in progress

### Switches (on / off)

* Domestic hot water mode
* Heating mode
* Cooling mode
* Use heating curve

### Numeric values

* Delta T to stop heat pump
* Delta T to restart heat pump
* Delta T to lower compressor speed
* Domestic hot water setpoint
* Domestic hot water reheating point
* Cooling setpoint (for whencooling curve is not used)
* Heating setpoint (for when heating curve is not used)

### Calculated values

* Delta T
* Calculated heating temperature