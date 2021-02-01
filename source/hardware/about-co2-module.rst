################
About CO2 Module
################

.. |pic1| thumbnail:: ../_static/hardware/about-co2/co2-module.png
    :width: 300em
    :height: 300em

+------------------------+--------------------------------------------------------------------------------------------------------------------------+
| |pic1|                 | | The **CO2 Module** is a gas sensor for measuring the **carbon dioxide (CO₂) concentration**.                           |
|                        | | This module achieves ±50 ppm accuracy. It uses a non-dispersive infrared (NDIR) sensor manufactured in Sweden.         |
|                        | | Thanks to its **low-power operation** it can be powered from batteries for years.                                      |
|                        | |                                                                                                                        |
|                        | |  Carbon dioxide (or CO₂) is a colorless and odorless gas that is vital to life on Earth.                               |
|                        | |  Its nominal concentration is about 400 ppm (0.04 %).                                                                  |
|                        | |  There are many occurrences of CO₂ in nature. For example humans produce CO₂ when exhaling.                            |
|                        | |                                                                                                                        |
|                        | |  We have equipped the LP8 sensor with additional circuitry for efficient power management and I²C-only interfacing.    |
|                        | |  This module also features three 5-pin sockets allowing you to connect HARDWARIO tags.                                 |
+------------------------+--------------------------------------------------------------------------------------------------------------------------+

.. important::

    The high concentration of CO₂ leads to acidity and various health-related problems.

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| |shopping-cart| `Shop <https://shop.hardwario.com/co2-module/>`_      | |microchip| `Schematics <https://github.com/hardwario/bc-hardware/tree/master/out/bc-module-co2>`_           | |folder-open| `SDK Library <https://sdk.hardwario.com/group__twr__module__co2>`_ | |code| `Header File <https://github.com/hardwario/twr-sdk/blob/master/twr/inc/twr_module_co2.h>`_ | |code| `Source File <https://github.com/hardwario/twr-sdk/blob/master/twr/src/twr_module_co2.c>`_ | |book| `Projects <https://www.hackster.io/hardwario/projects?part_id=73699>`_  |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

********
Features
********

- Carbon dioxide (CO₂) sensor LP8 (SenseAir)
- Non-dispersive infrared (NDIR) technology
- Measurement range of CO₂: 0 to 10 000 ppm
- Measurement accuracy: ±50 ppm CO₂ ±3 % of reading (Note 1)
- I²C-only interface (integrated UART bridge and I/O expander)
- Constant current source for 470 mF supercap
- Long battery life-time
- 3 sockets for a HARDWARIO TOWER tag
- Low power consumption:
    - 6 µA (6 measurements per hour)
    - 61 µA (1 measurement per minute)
- Operating voltage range: 3 V to 3.6 V
- Operating temperature range: 0 to 50 °C
- Mechanical dimensions: 88 x 55 mm

.. caution::

    Accuracy ±50 ppm is achieved after 24 days of operation and auto-calibration process.

