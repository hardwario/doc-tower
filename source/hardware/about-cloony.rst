############
About Cloony
############

.. |pic1| thumbnail:: ../_static/hardware/about-cloony/cloony.png
    :width: 300em
    :height: 300em

+------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| |pic1|                 | | **Cloony** is compact version of the **Core Module**. The size is 23 x 23 mm.                                                        |
|                        | | It has a **32-bit ARM microcontroller** with 192 kB of flash memory and 20 kB of RAM.                                                |
|                        | | Besides the **integrated sub-GHz radio** for the 868/915 MHz band, it also features a digital temperature sensor, and security chip. |
|                        | |                                                                                                                                      |
|                        | | There are two basic difference from the **Core Module**. First, it does not have integrated 3D accelerometer.                        |
|                        | | Second, it does not have any USB interface.                                                                                          |
|                        | | Programming can be done either using an SWD debugger, or using a UART bootloader (you need RESET, BOOT, TXD2 and RXD2 signals).      |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------+

+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| |shopping-cart| `E-Shop <https://shop.hardwario.com/cloony/>`_ | |microchip| `Schematic drawing <https://github.com/hardwario/bc-hardware/tree/master/out/bc-cloony>`_  | |book| `Projects <https://www.hackster.io/hardwario/projects?part_id=74081>`_  |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

.. thumbnail:: ../_static/hardware/about-cloony/cloony-pinout.png
   :width: 60%
   :alt: Cloony Pinout

----------------------------------------------------------------------------------------------

********
Features
********

- ARM Cortex M0+ 32-bit MCU STM32L083CZ (ST)
- 192 kB Flash / 20 kB RAM
- Radio module (868/915 MHz) based on SPIRIT1 (ST)
- Security chip ATSHA204A (Microchip)
- Red color LED
- 10-pin SWD connector for debugging (optional)
- Operating voltage range: 2.0 V to 3.6 V
- Operating temperature range: -20 to 70 °C
- Mechanical dimensions: 23 x 23 mm

