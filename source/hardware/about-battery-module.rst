####################
About Battery Module
####################

.. |pic1| thumbnail:: ../_static/hardware/about-battery/battery-module.png
    :width: 300em
    :height: 300em

+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| |pic1|                 | | The **Battery Module** is designed as a power supply source for the battery-operated units.                                                        |
|                        | | The integrated low-power buck converter provides an excellent efficiency from the **four AAA 1.5 V Alkaline cells**.                               |
|                        | | It also features an extra 5-pin socket where you can connect a HARDWARIO tag.                                                                      |
|                        | |                                                                                                                                                    |
|                        | | If the for AAA batteries are not suitable for your application, you can use the **external voltage input**, which can handle up to 10 V.           |
|                        | | You can find the external input on the two pins in the middle. These pins are compatible with the popular JST connector used for Lithium batteries.|
|                        | |                                                                                                                                                    |
|                        | | Another useful feature is a **prototyping area** for soldering your circuits.                                                                      |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+


+------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| |shopping-cart| `E-Shop <https://shop.hardwario.com/battery-module/>`_ | |microchip| `Schematic drawing <https://github.com/hardwario/bc-hardware/tree/master/out/bc-module-battery>`_ | |folder-open| `SDK Library <https://sdk.hardwario.com/group__bc__module__battery>`_ | |code| `Header File <https://github.com/hardwario/bcf-sdk/blob/master/bcl/inc/bc_module_battery.h>`_ | |code| `Source File <https://github.com/hardwario/bcf-sdk/blob/master/bcl/src/bc_module_battery.c>`_ | |book| `Projects <https://www.hackster.io/hardwario/projects?part_id=737348>`_ |
+------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

********
Features
********

- High-efficiency buck converter TPS62745 (TI)
- Ultra-low quiescent current: 400 nA
- Recommended battery types:
    - 4x AAA 1.5 V Alkaline or
    - 4x AAA Eneloop NiMH
- Output supply voltage: 3.1 V
- Battery disconnect circuit
- Battery voltage measurement using an ADC input
- Prototyping area for soldering custom circuits
- One extra position for HARDWARIO tag
- Operating voltage range: 3.3 to 10 V
- Operating temperature range: -20 to 70 °C
- Mechanical dimensions: 88 x 55 mm

