##################
About Relay Module
##################

.. |pic1| thumbnail:: ../_static/hardware/about-relay/relay-module.png
    :width: 300em
    :height: 300em

+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| |pic1|                 | | The Relay Module is suitable for switching small power appliances - e.g. LED strip, cooling fan, siren, buzzer, garage door opener, etc.               |
|                        | | It features a bistable (or latching) relay and that makes it suitable for battery-operated applications - the relay simply remembers its state.        |
|                        | |                                                                                                                                                        |
|                        | | The energy is needed only during transition state. Once the new state has been set, it is not necessary to energize the relay's coil anymore.          |
|                        | | The switching period is indicated using the green LED (in software referred as "true state"), or red LED (in software referred to as "false state").   |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| |shopping-cart| `Shop <https://shop.hardwario.com/relay-module/>`_    | |microchip| `Schematics <https://github.com/hardwario/bc-hardware/tree/master/out/bc-module-relay>`_         | |folder-open| `SDK Library <https://sdk.hardwario.com/group__twr__module__relay>`_ | |code| `Header File <https://github.com/hardwario/twr-sdk/blob/master/twr/inc/twr_module_relay.h>`_ | |code| `Source File <https://github.com/hardwario/twr-sdk/blob/master/twr/src/twr_module_relay.c>`_ | |book| `Projects <https://www.hackster.io/hardwario/projects?part_id=73841>`_  |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

********
Features
********

- Bistable (latching) relay for switching loads up to 60 W:
    - 12 V DC / 5 A
    - 24 V DC / 2.5 A
- Control using I²C bus
- Suitable for battery-operated applications
- Energy for the coil is needed only during the transition states
- Red and green LEDs indicate the coil energizing
- Operating voltage range: 3.0 to 3.6 V
- Operating temperature range: -20 to 70 °C
- Mechanical dimensions: 33 x 55 mm

