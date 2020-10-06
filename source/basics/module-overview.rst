###############
Module Overview
###############

*******
Modules
*******

Radio Dongle
************

.. |dongle| thumbnail:: ../_static/basics/module-overview/radio-dongle.png
    :width: 300em
    :height: 300em

+------------------------+-------------------------------------------------------------------------------------------+
| |dongle|               | | The **Radio Dongle** is the main element of the HARDWARIO radio network.                |
|                        | | This product works as a **gateway for the HARWDARIO nodes**. It looks like a USB stick. |
|                        | | You can plug it to your desktop, Raspberry Pi, or Turris Omnia.                         |
|                        | | Also, you can look at it as an access point for up to 32 HARDWARIO nodes.               |
+------------------------+-------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

Core Module
***********

.. |core-module| thumbnail:: ../_static/basics/module-overview/core-module.png
    :width: 300em
    :height: 300em

+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| |core-module|          | | The **Core Module** is the key element of every HARDWARIO node.                                                                                        |
|                        | | It has a **32-bit ARM microcontroller** with 192 kB of flash memory and 20 kB of RAM.                                                                  |
|                        | | Besides the **integrated sub-GHz radio** for the 868/915 MHz band, it also features a digital temperature sensor, 3D accelerometer, and security chip. |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

Cloony
******

.. |cloony| thumbnail:: ../_static/basics/module-overview/cloony.png
    :width: 300em
    :height: 300em

+------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| |cloony|               | | **Cloony** is compact version of the **Core Module**. The size is 23 x 23 mm.                                                        |
|                        | | It has a **32-bit ARM microcontroller** with 192 kB of flash memory and 20 kB of RAM.                                                |
|                        | | Besides the **integrated sub-GHz radio** for the 868/915 MHz band, it also features a digital temperature sensor, and security chip. |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

Mini Battery Module
*******************

.. |mini-battery| thumbnail:: ../_static/basics/module-overview/mini-battery-module.png
    :width: 300em
    :height: 300em

+------------------------+------------------------------------------------------------------------------------------------------------------------+
| |mini-battery|         | | The **Mini Battery Module** is designed as a power supply source for the battery-operated units.                     |
|                        | | The integrated low-power boost converter provides an excellent efficiency from the **two AAA 1.5 V Alkaline cells**. |
|                        | | It features a bottom-entry socket, so the overall profile of the unit you build remains low.                         |
+------------------------+------------------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

Battery Module
**************

.. |battery-module| thumbnail:: ../_static/basics/module-overview/battery-module.png
    :width: 300em
    :height: 300em

+------------------------+-----------------------------------------------------------------------------------------------------------------------+
| |battery-module|       | | The **Battery Module** is designed as a power supply source for the battery-operated units.                         |
|                        | | The integrated low-power buck converter provides an excellent efficiency from the **four AAA 1.5 V Alkaline cells**.|
|                        | | It also features an extra 5-pin socket where you can connect a HARDWARIO tag.                                       |
+------------------------+-----------------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

Power Module
************

.. |power-module| thumbnail:: ../_static/basics/module-overview/power-module.png
    :width: 300em
    :height: 300em

+------------------------+--------------------------------------------------------------------------------------------------------------+
| |power-module|         | | The **Power Module** allows you to connect a 5 V DC power adapter via a standard 2.1 mm power jack socket. |
|                        | | It features a **high-current relay** (230 V AC / 16 A) to control your appliances.                         |
|                        | | Also you can drive a **digital LED strip** with it (compatible with WS2812B).                              |
+------------------------+--------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

PIR Module
**********

.. |pir-module| thumbnail:: ../_static/basics/module-overview/pir-module.png
    :width: 300em
    :height: 300em

+------------------------+----------------------------------------------------------------------------------------------------------+
| |pir-module|           | | The **PIR Module** works as a **motion detector** operating on a **passive infrared (PIR)** principle. |
|                        | | Typical usage of the **PIR Module** can be a wireless motion detector located on a wall or ceiling.    |
|                        | | The module is equipped with an **ultra-low-power digital sensor** from Excelitas' the DigiPyro® family.|
+------------------------+----------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

Climate Module
**************

.. |climate-module| thumbnail:: ../_static/basics/module-overview/climate-module.png
    :width: 300em
    :height: 300em

+------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| |climate-module|       | | The **Climate Module** integrates 4 environmental sensors - **temperature, humidity, light intensity and atmospheric pressure.**   |
|                        | | All sensors are digital, feature low-power operating modes and connected by using the I²C bus.                                     |
|                        | | It is a great product for environmental monitoring, weather stations, etc.                                                         |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

LCD Module
**********

.. |lcd-module| thumbnail:: ../_static/basics/module-overview/lcd-module-bg.png
    :width: 300em
    :height: 300em

+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| |lcd-module|           | | The **LCD Module** uses a unique technology - the so-called **memory display** developed by Sharp.                                         |
|                        | | It provides a resolution of 128 x 128 pixels in 1.28 inch size.                                                                            |
|                        | | It implements an **ultra-low-power display controller**, so you can have active graphical display with a long service time from batteries. |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

Button Module
*************

.. |button-module| thumbnail:: ../_static/basics/module-overview/button-module.png
    :width: 300em
    :height: 300em

+------------------------+-------------------------------------------------------------------------------------------------------------------------+
| |button-module|        | | The **Button Module** is as simple as its name speaks. It has one large button that feels good to click.              |
|                        | | You can use it to trigger various actions, e.g. turn on the light, send a push notification, or control an appliance. |
|                        | | It is connected to the BOOT signal on the **Core Module**.                                                            |
+------------------------+-------------------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

Encoder Module
**************

.. |encoder-module| thumbnail:: ../_static/basics/module-overview/encoder-module.png
    :width: 300em
    :height: 300em

+------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| |encoder-module|       | | The **Encoder Module** can be useful for controlling your applications.                                                            |
|                        | | The module is equipped with a high-quality rotary encoder manufactured by Bourns and features high reliability and durability.     |
|                        | | The rotary encoder is also equipped with a **push-button switch.**                                                                 |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

Relay Module
************

.. |relay-module| thumbnail:: ../_static/basics/module-overview/relay-module.png
    :width: 300em
    :height: 300em

+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |relay-module|         | | The **Relay Module** is suitable for switching small power appliances - e.g. LED strip, cooling fan, siren, buzzer, garage door opener, etc.               |
|                        | | It features a **bistable (or latching) relay** and that makes it suitable for battery-operated applications - the relay simply remembers its state.        |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

Sensor Module
*************

.. |sensor-module| thumbnail:: ../_static/basics/module-overview/sensor-module.png
    :width: 300em
    :height: 300em

+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| |sensor-module|        | | The **Sensor Module** features **up-to four universal inputs or outputs** on a pluggable terminal block with **1-Wire bus master** support.    |
|                        | | The terminals can be used as both analog and digital input/output.                                                                             |
|                        | | For example you can connect various external digital, analog or resistive sensors.                                                             |
|                        | | Also, you can communicate with other devices on a 1-Wire bus.                                                                                  |
|                        | |                                                                                                                                                |
|                        | | The two terminals - A on the left, B on the right - are connected to the HARDWARIO header signals P4/A4/DAC0 and P5/A5/DAC1.                   |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

Sigfox Module
*************

.. |sigfox-module| thumbnail:: ../_static/basics/module-overview/sigfox-module.png
    :width: 300em
    :height: 300em

+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| |sigfox-module|        | | The **Sigfox Module** allows you to communicate to the **Sigfox wireless network**, a global network made for the IoT.                         |
|                        | | This technology makes it possible to communicate from a battery-powered device directly to server, even for several years.                     |
|                        | | The **Sigfox Module** uses radio frequency 868 MHz.                                                                                            |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

micro:bit Module
****************

.. |microbit| thumbnail:: ../_static/basics/module-overview/microbit-module.png

+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| |microbit|             | | Let's measure and influence your environment with HARDWARIO micro:bit bundle.                                                                  |
|                        | | It contains everything you need to start using sensors from Industrial IoT Kit in micro:bit environment.                                       |
|                        | |                                                                                                                                                |
|                        | | Run the device on batteries. Measure temperature, humidity, carbon dioxide (CO2), atmospheric pressure, light intensity,                       |
|                        | | volatile organic compounds (VOCs), motion or control other devices using a Relay Module.                                                       |
|                        | |                                                                                                                                                |
|                        | | The bundle also includes a 1-hour STEM webinar.                                                                                                |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

1-Wire Module
*************

.. |1-wire-module| thumbnail:: ../_static/basics/module-overview/1-wire-module.png
    :width: 300em
    :height: 300em

+------------------------+-------------------------------------------------------------------------------------------------------+
| |1-wire-module|        | | The **1-Wire** Module allow you to connect I²C devices over a distance of several meters.           |
|                        | | The I²C protocol is encapsulated to a 1-Wire protocol. The data are protected using **16-bit CRC**. |
|                        | | You can use the **Sensor Module** to create a 1-Wire bus master.                                    |
+------------------------+-------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

Cover Module
************

.. |cover-module| thumbnail:: ../_static/basics/module-overview/cover-module.png
    :width: 300em
    :height: 300em

+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| |cover-module|         | | The **Cover Module** is a simple mechanical part that helps to cover the front face of the HARDWARIO electronics (larger format 88 x 55 mm). |
|                        | | It looks great when combined with one of our 3D-printed enclosure.                                                                           |
|                        | | You simple snap it in the HARDWARIO socket header using the bottom pins.                                                                     |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

Tag Module
**********

.. |tag-module| thumbnail:: ../_static/basics/module-overview/tag-module.png
    :width: 300em
    :height: 300em

+------------------------+-------------------------------------------------------------------------------------------------------+
| |tag-module|           | | The **Tag Module** makes it possible to **connect up to six HARDWARIO tags**.                       |
|                        | | There are two independent I²C buses (I2C0 and I2C1) - one on each side.                             |
|                        | | This allows to connect two tags of the same I²C address to a single HARDWARIO node.                 |
|                        | | It also features pull-up resistors on SDA/SCL signals of I2C1 bus.                                  |
+------------------------+-------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

Base Module
***********

.. |base-module| thumbnail:: ../_static/basics/module-overview/base-module.png
    :width: 300em
    :height: 300em

+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| |base-module|          | | The **Base Module** works as a mechanical stand for the HARDWARIO units.                                                                |
|                        | | With the exception of the **Battery Module**,                                                                                           |
|                        | | you can plug any other HARDWARIO TOWER - Industrial IoT Kit module into a standardized socket available on the **Base Module**.         |
|                        | |                                                                                                                                         |
|                        | | It also features a **prototyping area** for soldering your circuits.                                                                    |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

Breadboard Module
*****************

.. |breadboard-module| thumbnail:: ../_static/basics/module-overview/breadboard-module.png
    :width: 300em
    :height: 300em

+------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| |breadboard-module|    | | The **Breadboard Module** offers an easy way to connect any HARDWARIO TOWER - Industrial IoT Kit module to your breadboard.          |
|                        | | The narrowed breakout provides more space for wiring and prototyping.                                                                |
|                        | | The precision pin headers from the bottom side allow smooth insertion to your breadboard and do not stress the breadboard's sockets. |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

Probe Module
************

.. |probe-module| thumbnail:: ../_static/basics/module-overview/probe-module.png
    :width: 300em
    :height: 300em

+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |probe-module|         | | The **Probe Module** allows you to easily hook up an **oscilloscope** or **logic analyzer** on any signal of the HARDWARIO TOWER - Industrial IoT Kit header.  |
|                        | | Sometimes during the development, you need to analyze the signals and see what's going on.                                                                     |
|                        | | And this module makes the task fast and convenient.                                                                                                            |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

****
Tags
****

Temperature Tag
***************

.. |temperature-tag| thumbnail:: ../_static/basics/module-overview/temperature-tag.png
    :width: 300em
    :height: 300em

+------------------------+------------------------------------------------------------------------------------------------------------------------------+
| |temperature-tag|      | | The **Temperature Tag** uses a **high-accuracy temperature sensor TMP11** 2 with a typical accuracy of ±0.1 °C at 25 °C.   |
|                        | | This sensor is digital and calibrated.                                                                                     |
|                        | | It communicates using an I²C bus and features a very low power operation and shutdown mode.                                |
+------------------------+------------------------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

Humidity Tag
************

.. |humidity-tag| thumbnail:: ../_static/basics/module-overview/humidity-tag.png
    :width: 300em
    :height: 300em

+------------------------+--------------------------------------------------------------------------------------------------------------------------+
| |humidity-tag|         | | The **Humidity Tag** uses a high-accuracy **humidity sensor** SHT20 with a typical accuracy of ±3 % from 20 % to 80 %. |
|                        | | This sensor is digital and calibrated.                                                                                 |
|                        | | It communicates using an I²C bus and features a very low power operation and shutdown mode.                            |
+------------------------+--------------------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

Lux Meter Tag
*************

.. |lux-meter-tag| thumbnail:: ../_static/basics/module-overview/lux-meter-tag.png
    :width: 300em
    :height: 300em

+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| |lux-meter-tag|        | | The **Lux Meter Tag** uses a high dynamic range **light intensity sensor OPT3001** that can measure illuminance from 0.01 to 83,000 lux. |
|                        | | This sensor is digital and calibrated.                                                                                                   |
|                        | | It communicates using an I²C bus and features a very low power operation and shutdown mode.                                              |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

Barometer Tag
*************

.. |barometer-tag| thumbnail:: ../_static/basics/module-overview/barometer-tag.png
    :width: 300em
    :height: 300em

+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| |barometer-tag|        | | The **Barometer Tag** allows you to measure absolute pressure in the range from 20 kPa to 110 kPa, or altitude above the sea level in meters. |
|                        | | It uses a low-power I²C sensor **MPL3115A2** with an absolute accuracy of ±0.4 kPa. It features a very low active and standby current.        |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

VOC Tag
*******

.. |voc-tag| thumbnail:: ../_static/basics/module-overview/voc-lp-tag.png
    :width: 300em
    :height: 300em

+------------------------+-------------------------------------------------------------------------------------------------------+
| |voc-tag|              | | The **VOC Tag** is a gas sensor for measuring **volatile organic compounds (VOC) concentration**.   |
|                        | | This is useful for indoor air quality monitoring applications.                                      |
|                        | | This module uses a metal-oxide multi-pixel sensor SGP30 from Sensirion measuring total VOC level.   |
+------------------------+-------------------------------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

NFC Tag
*******

.. |nfc-tag| thumbnail:: ../_static/basics/module-overview/nfc-tag.png
    :width: 300em
    :height: 300em

+------------------------+-------------------------------------------------------------------------------------------------------+
| |nfc-tag|              | | The **NFC Tag** operates as a **dual port memory**.                                                 |
|                        | | You have the the NFC protocol from one side and the I²C bus interface from the other side.          |
|                        | | It features a 1 kB EEPROM memory.                                                                   |
|                        | | The chip does not have to be powered when being accessed from the NFC side.                         |
+------------------------+-------------------------------------------------------------------------------------------------------+

