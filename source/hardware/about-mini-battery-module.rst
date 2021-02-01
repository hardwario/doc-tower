#########################
About Mini Battery Module
#########################

.. |pic1| thumbnail:: ../_static/hardware/about-mini-battery/mini-battery-module.png
    :width: 300em
    :height: 300em

+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| |pic1|                 | | The **Mini Battery Module** is designed as a power supply source for the battery-operated units.                                                    |
|                        | | The integrated low-power boost converter provides an excellent efficiency from the **two AAA 1.5 V Alkaline cells**.                                |
|                        | | It features a bottom-entry socket, so the overall profile of the unit you build remains low.                                                        |
|                        | |                                                                                                                                                     |
|                        | | The load disconnect circuit can disconnect the batteries if any other power supply source is connected to the system (e.g. AC adapter or USB cable).|
|                        | | The **battery voltage can be measured** on one of the analog inputs of the standardized header (P0/A0/TXD0).                                        |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| |shopping-cart| `Shop <https://shop.hardwario.com/mini-battery-module/>`_   | |microchip| `Schematics <https://github.com/hardwario/bc-hardware/tree/master/out/bc-module-battery-mini>`_        | |folder-open| `SDK Library <https://sdk.hardwario.com/group__twr__module__battery>`_ | |code| `Header File <https://github.com/hardwario/twr-sdk/blob/master/twr/inc/twr_module_battery.h>`_ | |code| `Source File <https://github.com/hardwario/twr-sdk/blob/master/twr/src/twr_module_battery.c>`_ | |book| `Projects <https://www.hackster.io/hardwario/projects?part_id=73682>`_  |
+-----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

********
Features
********

- Highly efficient DC/DC converter TPS61099 (TI)
- Very low quiescent current <5 μA
- Efficiency up to 93% at 10 mA
- Recommended types of batteries:
    - 2x AAA 1.5 V Alkaline, or
    - 2x AAA Eneloop NiMH
- Rated output voltage 3.1 V
- Circuit for disconnecting the battery
- Reverse polarity protection
- Input voltage measurement via ADC input
- Operating temperature range: -20 to 70 °C
- Dimensions: 33 x 55 mm

