# Release notes

## Version 1.0

First release of the *Itho Daalderop Amber heat pump control module* software

## Version 1.1

Added three config settings to offset the temperature sensors for calibration purposes
- Dallas temperature 1 offset
- Dallas temperature 2 offset
- Dallas temperature 3 offset

## Version 1.2

**This version should fix the extreme values sometimes reported by several sensors**

Added three new temperature sensors:
- Average 1h ambient temperature
- Average 4h ambient temperature
- Average 24h ambient temperature

Increased modbus command throttle for stability

## Version 1.2.1

Added support for hardware Factory reset button introduced on PCB v2.3
Update not needed when not using PCB v2.3

## Version 1.3.0

Changed type from sensor to numeric value for the heating curve fields (works for Amber version 2.29 and above)

Added switch:
- Use anti legionalle mode

Added numbers:
- Circuit 1 minimum temperature
- Circuit 1 maximum temperature

Added select:
- Working mode (options: Heating, Cooling, Domestic hot water, Auto)

## Version 1.4.0

Fixed defrost state binary sensor

Added sensors:
- SG decrease setpoint cooling
- SG increase setpoint heating
- SG increase setpoint domestic hot water

Added binary sensor:
- SG ready

## Version 1.4.1

Restore the last state of the relais at startup

## Version 1.4.2

Updated ESPHome to version 2024.12.4 to fix an error in the update component which resulted in a crash

## Version 1.5.0

This version retrieves the acutal setpoints from the Amber, instead of calculating themself. Note that the returned value is the fixed setpoint (without the heating/cooling curve) if the Amber is not currently working in the mode (so, when not heating, the actual setpoint heating will be the fixed setpoint as if the heating curve is not used).

Added sensors:
  - Actual setpoint heating zone 1
  - Actual setpoint heating zone 2
  - Actual setpoint cooling zone 1
  - Actual setpoint cooling zone 2

Added switch:
  - Reduced mode timer

**Removed sensor:**
  - Calculated heating temperature  

## Version 1.6.0

Prepared the installation for the Itho Daalderop change in communication protocol. All control modules should automatically update to the version with the current 'old' settings. If your Amber is updated there could be a problem in the communication and you must install the parity EVEN version.

## Version 1.7.0

Added fault codes
Grouped entities in ESPHome web interface
Added two buttons to flash firmware for EVEN and NONE parity communication

## Version 1.7.1

Updated to latest version of ESPHome
Changed temperature sensors to make use of OneWire library instead of deprecated Dallas library