###################
About RS-485 Module
###################

.. |pic1| thumbnail:: ../_static/hardware/about-rs485/rs-485-module.png
    :width: 300em
    :height: 300em

+------------------------+--------------------------------------------------------------------------------------------------------------+
| |pic1|                 | | The **RS-485 Module** allows you to communicate over RS-485 bus using MODBUS or your custom protocol.      |
|                        | | Many devices could be connected to the single RS-485 bus and exchange data.                                |
|                        | | This module also contains DC/DC converter so it can power the node. Supported input voltage is 5 - 28 V.   |
|                        | |                                                                                                            |
|                        | | This module has low-power mode when data receiving is not enabled.                                         |
|                        | | This way RS-485 node could work for long time just from batteries.                                         |
+------------------------+--------------------------------------------------------------------------------------------------------------+

+--------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| |microchip| `Schematics <https://github.com/hardwario/bc-hardware/tree/master/out/bc-module-rs-485>`_        | |folder-open| `SDK Library <https://sdk.hardwario.com/group__twr__module__rs485.html>`_ | |code| `Header File <https://github.com/hardwario/twr-sdk/blob/master/twr/inc/twr_module_rs485.h>`_ | |code| `Source File <https://github.com/hardwario/twr-sdk/blob/master/twr/src/twr_module_rs485.c>`_ |
+--------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

********
Features
********

- RS-485 communication
- Only I2C pins are used thanks to I2C to UART converter SC16IS750IPW
- Power supply with DC/DC converter and 5 - 28 V input voltage
- Operating voltage range: 3.0 to 3.6 V
- Operating temperature range: -40 to 85 °C
- Dimensions: 33 x 55 mm
