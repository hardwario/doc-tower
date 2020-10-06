###################
About Sensor Module
###################

.. |pic1| thumbnail:: ../_static/hardware/about-sensor/sensor-module.png
    :width: 300em
    :height: 300em

+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| |pic1|                 | | The **Sensor Module** features **up-to four universal inputs or outputs** on a pluggable terminal block with **1-Wire bus master** support.    |
|                        | | The terminals can be used as both analog and digital input/output.                                                                             |
|                        | | For example you can connect various external digital, analog or resistive sensors.                                                             |
|                        | | Also, you can communicate with other devices on a 1-Wire bus.                                                                                  |
|                        | |                                                                                                                                                |
|                        | | The two terminals - A on the left, B on the right - are connected to the HARDWARIO header signals P4/A4/DAC0 and P5/A5/DAC1.                   |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

.. tip::

    The C pin is in default configuration connected also to the ground GND.
    It is possible to remove zero-ohm resistor R20 and solder it to the place R21.
    This way the C signal is directly connected to P7 and can be used as extra input.

.. note::

    The VCC middle pin is possible to control by software. You can enable 3 V on this pin.

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| |shopping-cart| `E-Shop <https://shop.hardwario.com/sensor-module/>`_ | |microchip| `Schematic drawing <https://github.com/hardwario/bc-hardware/tree/master/out/bc-module-sensor>`_ | |folder-open| `SDK Library <https://sdk.hardwario.com/group__bc__module__sensor>`_ | |code| `Header File <https://github.com/hardwario/bcf-sdk/blob/master/bcl/inc/bc_module_sensor.h>`_ | |code| `Source File <https://github.com/hardwario/bcf-sdk/blob/master/bcl/src/bc_module_sensor.c>`_ | |book| `Projects <https://www.hackster.io/hardwario/projects?part_id=73750>`_  |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

********
Features
********

Configurable terminal modes:

- Analog input or output
- Digital input or output
- Pull-up resistor none/4.7 kΩ/56 Ω

Examples interfaces:

- Digital temperature sensor on a 1-Wire bus (DS18B20)
- Resistance temperature sensor (Pt 100, Pt 1000, etc.)
- Analog temperature sensor (LM35, TMP37, etc.)
- NTC temperature sensor
- Control of digital 1-Wire relay block
- Button or any type of switch
- Voltage measurement
- Plug-in 4-pin screw terminal block
- Operating voltage range: 1.65 V to 5.5 V
- Operating temperature range: -20 to 70 °C
- Dimensions: 33 x 55 mm

