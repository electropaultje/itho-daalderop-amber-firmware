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
- Circuit 1 maximuim temperature

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