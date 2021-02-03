##################
About Power Module
##################



.. container:: twocol

   .. container:: leftside

        .. thumbnail:: ../_static/hardware/about-power/power-module.png
            :width: 100%

   .. container:: rightside

        The Power Module allows you to connect a 5 V DC power adapter via a standard 2.1 mm power jack socket.
        It features a high-current relay (230 V AC / 16 A) to control your appliances.
        Also you can drive a digital LED strip with it (compatible with WS2812B).

        This module can power a HARDWARIO TOWER - Industrial IoT Kit node thanks to its integrated LDO regulator.
        The LDO generates 3.3 V output from the 5 V input.

        Reliability is important - that's why we have implemented a **smart** overvoltage, undervoltage and **reverse polarity protection** on the power jack input.
        This feature guarantees the input voltage range to always stay within the proper limits.

.. .. |pic1| thumbnail:: ../_static/hardware/about-power/power-module.png
..     :width: 300em
..     :height: 300em
..
.. +------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
.. | |pic1|                 | | The Power Module allows you to connect a 5 V DC power adapter via a standard 2.1 mm power jack socket.                                                         |
.. |                        | | It features a high-current relay (230 V AC / 16 A) to control your appliances.                                                                                 |
.. |                        | | Also you can drive a digital LED strip with it (compatible with WS2812B).                                                                                      |
.. |                        | |                                                                                                                                                                |
.. |                        | | This module can power a HARDWARIO TOWER - Industrial IoT Kit node thanks to its integrated LDO regulator.                                                      |
.. |                        | | The LDO generates 3.3 V output from the 5 V input.                                                                                                             |
.. |                        | |                                                                                                                                                                |
.. |                        | | Reliability is important - that's why we have implemented a **smart** overvoltage, undervoltage and **reverse polarity protection** on the power jack input.   |
.. |                        | | This feature guarantees the input voltage range to always stay within the proper limits.                                                                       |
.. +------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. warning::

    The maximum allowed current is 6 A.

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| |shopping-cart| `Shop <https://shop.hardwario.com/power-module/>`_    | |microchip| `Schematics <https://github.com/hardwario/bc-hardware/tree/master/out/bc-module-power>`_         | |folder-open| `SDK Library <https://sdk.hardwario.com/group__twr__module__power>`_ | |code| `Header File <https://github.com/hardwario/twr-sdk/blob/master/bcl/inc/twr_module_power.h>`_ | |code| `Source File <https://github.com/hardwario/twr-sdk/blob/master/bcl/src/twr_module_power.c>`_ | |book| `Projects <https://www.hackster.io/hardwario/projects?part_id=73717>`_  |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

********
Features
********

- 5 V DC power adapter input (2.1 mm jack) (1)
- Input voltage range: 4.2 V to 5.8 V
- High-current relay output (230 V AC / 16 A)
- Integrated LDO with 3.3 V output voltage
- Addressable/digital RGB(W) LED strip output (1)
- Integrated voltage translator (3.3 V to 5 V)
- 2x position for a HARDWARIO TOWER tag
- Overvoltage, undervoltage and reverse polarity protection
- Pluggable 3-pin terminal block for relay output
- Pluggable 3-pin terminal block for digital LED strip
- Operating temperature range: -20 to 70 °C
- Mechanical dimensions: 88 x 55 mm

