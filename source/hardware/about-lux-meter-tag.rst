###################
About Lux Meter Tag
###################

.. |pic1| thumbnail:: ../_static/hardware/about-lux/lux-meter-tag.png
    :width: 300em
    :height: 300em

+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| |pic1|                 | | The **Lux Meter Tag** uses a high dynamic range **light intensity sensor OPT3001** that can measure illuminance from 0.01 to 83,000 lux. |
|                        | | This sensor is digital and calibrated.                                                                                                   |
|                        | | It communicates using an I²C bus and features a very low power operation and shutdown mode.                                              |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+

.. tip::

    You can use the sensor to detect day and night or it could be used as auxiliary information about someone's presence.

    The spectral response of the sensor tightly matches the photopic response of the human eye and includes **significant infrared rejection**.

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| |shopping-cart| `Shop <https://shop.hardwario.com/lux-meter-tag/>`_   | |microchip| `Schematics <https://github.com/hardwario/bc-hardware/tree/master/out/bc-tag-lux-meter>`_        | |folder-open| `SDK Library <https://sdk.hardwario.com/group__twr__tag__lux__meter>`_ | |code| `Header File <https://github.com/hardwario/twr-sdk/blob/master/twr/inc/twr_tag_lux_meter.h>`_ | |code| `Source File <https://github.com/hardwario/twr-sdk/blob/master/twr/src/twr_tag_lux_meter.c>`_ | |book| `Projects <https://www.hackster.io/hardwario/projects?part_id=80227>`_  |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

********
Features
********

- Digital ambient light sensor OPT3001 (TI)
- Communication using I²C bus
- Measures in the range from 0.01 to 83,000 lux
- 23-bit effective dynamic range
- Optional interrupt output
- Power consumption:
    - Active current: 1.8 µA
    - Shutdown current: 0.3 µA
- Operating voltage range: 1.6 V to 3.6 V
- Operating temperature range: -20 to 70 °C
- Mechanical dimensions: 16 x 16 mm
