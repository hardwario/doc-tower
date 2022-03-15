####################
LoRa Tester Tutorial
####################

This document describes how to use HARDWARIO TOWER LoRa Tester and how to test your private or public network in your area.

- `LoRa Tester Basic set <https://shop.hardwario.com/lora-tester-basic-kit/>`_ on our e-shop
- `LoRa Tester GPS set <https://shop.hardwario.com/lora-tester-gps-kit/>`_ on our e-shop

.. thumbnail:: ../_static/tutorials/lora-tester-tutorial/lora-tester.jpg
   :width: 30%

*******************
LoRa Tester Modules
*******************

The tester consists of these modules:

- Core Module
- LoRa Module
- GPS Module (optional)
- Mini Battery Module (Battery Module when ordered with GPS Module)

********************
LoRa Tester Firmware
********************

If you order tester as a kit, it already has proper firmware. However we suggest to check/update firmware so you use the latest version.
Your **Core Module** needs to be flashed with ``twr-lora-tester`` firmware.

To update the firmware, use :doc:`HARDWARIO Playground <../basics/hardwario-playground>` and in the **Firmware** tab, choose the ``twr-lora-tester`` firmware.

Project code and releases are available on GitHub `twr-lora-tester <https://github.com/hardwario/twr-lora-tester/releases>`_

.. note::

    Older firmware ``twr-lora-tester-lcd-gps-ttnmapper`` which has menu on the **LCD Module** is not maintained anymore. We decided to simplify the tester firmware. However, if you need a more complex menu and you don't need all the new ``twr-lora-tester`` functionality, you can still use the older firmware.

*************************
LoRa Tester Configuration
*************************

To configure the LoRa parameters over USB with AT commands, please follow this :doc:`LoRa AT Commands Configuration <lora-at-commands-configuration>` page.

*******************
LoRa Packet Decoder
*******************

In the project's folder `/src <https://github.com/hardwario/twr-lora-tester/tree/master/src>`_ folder there is a ``*.js`` file that contains the packet decoder. You can use the same script for **ChirpStack** or **The Things Network**. Just replace the whole text-field for the uplink message decoder.

Using the decoder, you will get these values:

- Temperature
- Battery voltage

When using GPS Module, you also get:

- Latitude
- Longitude
- Altitude
- Number of satellites in view

***************
Power-on Screen
***************

.. thumbnail:: ../_static/tutorials/lora-tester-tutorial/ready.jpg
   :width: 30%

When firmware boots up, you can see the **Core Module**'s firmware version ``FW:v1.11.1`` and the **LoRa Module** firmware version ``LM:1.1.03``.
If the initialization of the **LoRa Module** was successful, you will see the ``READY`` message on the screen and green will blink the LED once.

If you have attached the **GPS Module**, then on top of the screen you see the GPS position and other useful info from GPS.

************
JOIN Command
************

In the bottom left corner you can see ``(JOIN)`` in the brackets. This means that the long press of the left button under the screen sends a JOIN command.

After successful **JOIN** you can see ``JOIN: OK`` response.
In case of ``JOIN: ERR`` check your configuration and follow the Troubleshooting chapter in the end of this tutorial.

.. thumbnail:: ../_static/tutorials/lora-tester-tutorial/join.jpg
   :width: 30%

*************
CHECK Command
*************

In the bottom left corner you can see ``CHECK`` command. By short press of the left button you send a LoRa MAC command requesting connection info.

.. thumbnail:: ../_static/tutorials/lora-tester-tutorial/check.jpg
   :width: 30%

If you are connected to the network, you will see two numbers after ``CHK:`` response:

- The first number, in this case ``17``, is a `Link Margin <https://en.wikipedia.org/wiki/Link_margin>`_ of the **sent uplink message from tester to the gateway**. You need to take into account also Automatic Datarate which may lower the transmission power.

- The second number, in this case ``1``, is the number of gateways that received your **CHECK** command. This may be handy if you need to cover same area with more than a one gateway for redundancy.

************
SEND Command
************

The most important command that you will use during testing of your network is ``SEND``.
By short press of this button you send a confirmed packet to your gateway.

.. thumbnail:: ../_static/tutorials/lora-tester-tutorial/send.jpg
   :width: 30%

During tranmission you will see a message, e.g. ``SEND 1/8`` - that means, that it is sending the first packet and in case of not receiving an acknowledge, it will try up to 8 times to retransmit the packet.

*******************************
RSSI + SNR + Counter Statistics
*******************************

Below the main status text line you can see text ``RSSI-76,SNR6,C2/1``:

.. thumbnail:: ../_static/tutorials/lora-tester-tutorial/send.jpg
   :width: 30%

- RSSI of the **ACK message** (downlink, from the gateway to tester)
- SNR - signal to noise ration
- ``C2/1`` is the frame counter. Uplink counter is 2 and downlink is 1 in this case

*********************
Low Power Consumption
*********************

The **LoRa Tester** has extremely low power consumption even with the **LCD Module**. The power consumption is around 50 uA and batteries will work for at least a year.

When the **GPS Module** is used, then it is activated when any button is pressed, then it goes to sleep after 15 minutes since the last press of any button.

***********************
LoRaWAN Troubleshooting
***********************

If you cannot see the incoming packets, or you cannot Join your network, please check:

- Proper setting of private versus public LoRaWAN network. You should see the incoming packets with your device ``DevEUI`` in the gateway's messages. If not, typically the band an/or private/public network scope is not configured properly.

- If you see messages incoming to gateway and ChirpStack but you still cannot join, check keys, make sure that in OTAA you set ``APPKEY`` and not ``APPSKEY`` which is for ABP mode.

**********************
Network Testing Method
**********************

For testing you need your gateways on-site and also your ChirpStack server.

For your network tests, you first need to **join** the network. Then walk around the area and press the **SEND** button and look for the signal RSSI. The RSSI on your screen is the strength of the downlink **ACK** packet.

To check the uplink RSSI and parameters you have to open ChirpStack/TTN on your laptop/phone and watch for RSSI of uplink message. Be sure to test multiple packets in case of worst signal, because ADR (Automatic Datarate) might
lower the transmittion power or change the modulation/datarate.

****************
UART AT Commands
****************

You can control the tester also completely from your laptop with many commands. See ``AT$HELP`` command for all the commands.

The commands that are invoked by buttons could be also invoked by these AT commands:

- ``AT$JOIN``
- ``AT$SEND``
- ``AT$LNCHECK``
