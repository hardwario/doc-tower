##############
Quick Tutorial
##############

******
Basics
******

.. tip::

    You can follow this tutorial even without Raspberry Pi. You just have to install :doc:`HARDWARIO Playground <../basics/hardwario-playground>` on your desktop.
    The Raspberry Pi approach is the easiest because you can download bc-rasbian image with pre-installed tools.

This document is a practical guide of using the **HARDWARIO TOWER - Industrial IoT Kit.**
It will guide you how **Raspberry Pi** can read the temperature from **Core Module**, control the LED, measure the relative air humidity from **Humidity Tag**,
control small electronic devices using **Relay Module**.

You will also be able to create a wireless network using **Radio Dongle**.
Data acquisition and control process is demonstrated using **Node-RED**, a web application that will run inside the **Raspberry Pi**.
This application allows intuitive graphical automation flow editing directly in your web browser.

.. note::

    Do you have **Radio Dongle** and **wireless kit**? If you would like to start creating you wireless network,
    you can later jump directly to the :ref:`Creation of the wireless network chapter <wireles-network>` when you get the basic knowledge of **Gateway**,
    ``bcf`` **firmware flashing tool** and **Node-RED** in the chapters below.

First we will demonstrate basic functionality without a wireless network. We use just a single **Core Module** connected to the **Raspberry Pi** by a USB cable.

What will we need at minimum:

- `Raspberry Pi <https://shop.hardwario.com/raspberry-pi-4b-4gb-set/>`_ + `MicroSDHC Memory Card 8GB <https://shop.hardwario.com/microsdhc-card-8gb/>`_
- `Core Module <https://shop.hardwario.com/core-module/>`_

Optionally for establishing a wireless network, you will need:

- `Radio Dongle <https://shop.hardwario.com/radio-dongle/>`_ (or second `Core Module <https://shop.hardwario.com/core-module/>`_)
- `Mini Battery Module <https://shop.hardwario.com/mini-battery-module/>`_
- `Humidity Tag <https://shop.hardwario.com/humidity-tag/>`_ or `Climate Module <https://shop.hardwario.com/climate-module/>`_
- `Relay Module <https://shop.hardwario.com/relay-module/>`_

**************
Video Tutorial
**************

.. raw:: html

    <iframe width="750" height="422" src="https://www.youtube.com/embed/FRRhleRNstg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

************
Raspberry Pi
************

Raspberry Pi Installation
*************************

.. tip::

    Detailed instructions can be found in the document :doc:`Raspberry Pi Installation <../tutorials/raspberry-pi-installation>`.

The easiest way to start is to download the `HARDWARIO Raspbian image <https://github.com/hardwario/bc-raspbian/releases>`_.
This image has already pre-installed necessary components.
It contains :doc:`HARDWARIO Gateway <../tools/hardwario-gateway>` ``bcg``,
**Mosquitto** MQTT broker, **Node-RED** and :doc:`HARDWARIO Firmware Tool <../tools/hardwario-firmware-flashing-tool>` ``bcf``.

The downloaded **Raspberry Pi** image has to be written to a MicroSD card using the multi-platform **GUI tool** `balenaEtcher <https://www.balena.io/etcher/>`_,
`Win32DiskImager <https://sourceforge.net/projects/win32diskimager/>`_ or command line ``dd`` tool.

You can also download the official Raspbian and install necessary packages yourself.

Raspberry Pi Login
******************

.. tip::

    Detailed instructions can be found in the document :doc:`Raspberry Pi Login <../tutorials/raspberry-pi-login>`.

#. Insert the MicroSD card with the **Raspbian** image to the **Raspberry Pi**.
#. Connect the Ethernet cable to the **Raspberry Pi**.
#. Connect the **Core Module** or the **Radio Dongle** to the **Raspberry Pi**.
#. Connect the power adapter to the **Raspberry Pi**.

After the **Raspberry Pi** boots up you should be able to find it at address ``http://hub.local``.
You can try the command ``ping hub.local`` and see the response.

.. caution::

    If the Raspberry Pi is not visible on the network,
    there's something wrong with your network setup or your system doesn't
    support **mDNS** and you have to find the IP address of the **Raspberry Pi** in your router's
    **DHCP** configuration or by using `Fing <https://www.fing.com>`_ which is a simple smartphone application.

Please log on the Raspberry Pi shell by typing ``ssh pi@hub.local`` command or use the Windows program **PuTTY**.

******************
Firmware upload by
******************

HARDWARIO Playground
********************

Download the latest HARDWARIO Playground from :ref:`Quick Start Guide <download-playground>` and open it.
Navigate to Firmware, connect Core Module via USB to computer and choose firmware to flash.

.. thumbnail:: ../_static/tutorials/quick-tutorial/hardwario-playground.png
   :width: 60%


Command-line tool
*****************

.. tip::

    Detailed instructions can be found in the document :doc:`Toolchain Guide <../firmware/toolchain-guide>`.

For quick start we've create a Python command-line utility **bcf**, which automatically downloads latest released firmwares from **GitHub** and will flash the modules.
On the Raspberry Pi you need first to update the list of releases by typing ``bcf update``.
Then by typing ``bcf list`` you get the list of pre-compiled firmwares.

.. caution::

    **Flashing Core Module R1 & R2**

    For differences of flashing older **Core Module 1** and newer **Core Module 2** please read :doc:`Core Module R1 and R2 comparison <../hardware/core-module-r1-and-r2-comparison>`

.. code-block:: console

    bcf flash hardwario/bcf-gateway-core-module:latest

Than you will choose between connected devices:

.. code-block:: console
    :linenos:

    bcf flash hardwario/bcf-gateway-core-module:latest
    0 /dev/ttyUSB0
    Please enter device: 0

.. note::

    After the firmware flashing the **Core Module** will automatically restart and the flashed firmware will be run.

******************************************
Radio Dongle to MQTT communication gateway
******************************************

**Radio Dongle** or **Core Module** with the **gateway** firmware is using virtual serial port over USB to exchange the data.
This communication is then redirected on the **Raspberry Pi** to the **MQTT** messages thanks to the :doc:`bch-gateway <../tools/hardwario-gateway>` ``bcg`` service.

All the messages from modules go through the gateway to the MQTT broker.
The MQTT is an open standard and also our back-bone system for passing the messages both ways.
In the middle of this communication system is the MQTT broker. Which is a server that accepts client connections.
Between the broker and clients are flowing MQTT messages. Each of them contains **topic** and **payload**.
Topic is a text string and has directory-like structure with the ``/`` delimeter (eg. ``node/core-module:0/thermometer/0:1/temperature``).
Payload isn't defined by a MQTT standard and HARDWARIO IoT Kit is sending these data types: numbers, strings, boolean values and JSONs.

Other services can easily connect to the MQTT broker and extend the functionality. Like Node-RED, MQTT-Spy or Android MQTT Dash application.

Another option is to enaable port-formwarding of the MQTT port (1883) on you NAT/network router.
Then you can connect to your broker from anywhere in the world.
It is also possible to set-up a **bridge** with other Mosquitto MQTT brokers.
All the brokers then share the same messages between each other.
Both of these described methods needs proper security settings.
For example by TLS connection.

- :doc:`MQTT explanation article <../interfaces/mqtt-protocol>`
- :doc:`MQTT topics short summary <../interfaces/mqtt-topics>`

****************************************
Subscribing and publishing MQTT messages
****************************************

This chapter is there for completion. Reading of the measured values is explained also in the next chapter with graphical Node-RED application.

There's a **Core Module** connected to the **Raspberry Pi**. Now we display the measured data which are send by the MQTT broker.

First we try to subscribe to the topic with ``mosquitto_sub`` command-line utility.
For publishing MQTT messages there's another utility ``mosquitto_pub``.
Please write the command below to your **Raspberry Pi**

.. code-block:: console

    mosquitto_sub -t "#" -v

After a while you should see a messages from the temperature sensor on the **Core Module**.
You can also see the button events when you press the ``B`` button on the **Core Module**.

.. note::

    For battery saving reasons the temperature is only send when there's a change.
    For testing purporses it is appropriate make the temperature sensor cooler or warmer.

.. code-block:: console
    :linenos:

    pi@hub:~ $ mosquitto_sub -t "#" -v
    node/core-module:0/thermometer/0:1/temperature 24.69
    node/core-module:0/thermometer/0:1/temperature 24.94
    node/core-module:0/push-button/-/event-count 5

The ``-t`` parameter if for topic which we would like to subscribe.
The hash symbol ``#`` means that we would like to subscribe to all topics.
The parameter ``-v`` displays more verbose output to the console, so we can see not only values but also messages topics.

Another MQTT wildcard symbol is question mark ``?``, which has the similar functionality like ``#``,
but it can be used only in one MQTT topic level (topic to read all thermometers ``node/?/thermometer``).

We'll try to turn on an LED on the **Core Module**.

.. code-block:: console

    mosquitto_pub -t "node/core-module:0/led/-/state/set" -m true

Perfect! That was simple, right? Now let's learn the Node-RED.

********
Node-RED
********

**Node-RED** is a web application pre-installed in **HARDWARIO Raspbian** which runs on **Raspberry Pi**.
You can run it in your web browser and display, process measured values and then send commands to other modules like **Relay Module, Power Module, LCD Module**.

Please type the ``hub.local:1880`` address to your web browser.

.. thumbnail:: ../_static/tutorials/quick-tutorial/node-red.png
   :width: 60%


On the left panel you choose the building blocks which you place by dragging and dropping to the middle to the **flow**.
Blocks are divided to several sections, the most important are **input, output, function** and **dashboard**.
After the placement of the blocks you can connect them with wires and create a **flow**.

On the right side of the screen there are tabs **info** and very important tab **debug**.
Later we will use also the **dashboard** tab to open our own designed page with gauges, switches and buttons.

When you create any change in the flow or configuration, you have to apply the changes by pressing the **deploy** button at the top right corner of the screen.

More information is in the Node-RED for Automation.

Subscribing MQTT messages
*************************

First we will output all the incoming MQTT messages to the **debug** output.
The following procedure will explain how to create basic flow printing all MQTT messages to the **debug** tab.
You can follow this instructions or import the flow below by the **Import** option in the top right menu.

.. code-block::

    [{"id":"2c3b9c0.ff19564","type":"tab","label":"Flow 0","disabled":false,"info":""},{"id":"fda6ba0.64ecb48","type":"mqtt in","z":"2c3b9c0.ff19564","name":"","topic":"#","qos":"2","broker":"ba3b2e25.7c8b7","x":170,"y":100,"wires":[["2dbd1aa6.284476"]]},{"id":"2dbd1aa6.284476","type":"debug","z":"2c3b9c0.ff19564","name":"","active":true,"console":"false","complete":"false","x":390,"y":100,"wires":[]},{"id":"ba3b2e25.7c8b7","type":"mqtt-broker","z":"","broker":"127.0.0.1","port":"1883","clientid":"","usetls":false,"compatmode":true,"keepalive":"60","cleansession":true,"willTopic":"","willQos":"0","willPayload":"","birthTopic":"","birthQos":"0","birthPayload":""}]

If you would like to create this flow manually, please follow these instructions.
From the **input** section drag and drop the **mqtt** block to the empty flow.
After that select and place from the **output** section the **debug** block.
Now you need to connect these blocks by the mouse.
This way you have created your first flow.

.. thumbnail:: ../_static/tutorials/quick-tutorial/mqtt-all-flow.png
   :width: 30%


Now it is necessary to configure **mqtt** block. By double clicking on the block open the setting and set these parameters:

- server: localhost:1883
- topic: #

.. thumbnail:: ../_static/tutorials/quick-tutorial/mqtt-configure.png
   :width: 30%


After you save the block settings you have to apply the changes by the **deploy** button.
After deploying switch to the **debug** tab and after few moments you'll see incoming messages from connected **Core Module**.
You can also press ``B`` button on the **Core Module** and this event will also appear in the **debug** log.

.. thumbnail:: ../_static/tutorials/quick-tutorial/mqtt-all-debug.png
   :width: 30%


Displaying the temperature
**************************

Now you can see all the incoming messages.
In case we would like to receive only temperature from one module, we have to change the topic in the **mqtt** block.
We need to change ``#`` to the ``node/core-module:0/thermometer/0:1/temperature``.

For the graphical representation of received values you can use **Node-RED dashboard**.
Please insert the **gauge** block, which is in the left list of the block at the bottom. This block needs to be configured.

.. thumbnail:: ../_static/tutorials/quick-tutorial/gauge-flow.png
   :width: 60%


Double click on the **gauge** block for configuration.
First create the new dashboard group by clicking the pencil symbol at the **Add new ui_group** field.
In the next opened dialog again click the pencil symbol at the **Add new ui_tab**.
Now confirm both opened dialogs and the default dashboard tab and group is created.
Before closing the **gauge** settings change the **Range** of the **gauge** to values from **0** to **40** and confirm this last opened dialog.
Press the **deploy** to apply the changes and open the dashboard.

.. tip::

    For battery-saving reasons the temperature is only send when there's a change.
    For testing purposes it is appropriate make the temperature sensor cooler or warmer.

The dashboard can be opened in the right **dashboard** tab by clicking on the arrow symbol or by typing the ``hub.local:1880/ui`` address to your browser.

.. thumbnail:: ../_static/tutorials/quick-tutorial/gauge-dashboard.png
   :width: 30%


Here's the complete flow in case of any issues.

.. code-block::

    [{"id":"3bfb0014.c8ac9","type":"mqtt in","z":"e2a5ec72.0af0b","name":"","topic":"node/core-module:0/thermometer/0:1/temperature","qos":"2","broker":"86ef748c.0f3de8","x":290,"y":160,"wires":[["ba582285.dd04c","17d59ad8.cfa925"]]},{"id":"ba582285.dd04c","type":"debug","z":"e2a5ec72.0af0b","name":"","active":true,"console":"false","complete":"false","x":630,"y":140,"wires":[]},{"id":"17d59ad8.cfa925","type":"ui_gauge","z":"e2a5ec72.0af0b","name":"","group":"761dfbba.bd8604","order":0,"width":0,"height":0,"gtype":"gage","title":"Temperature","label":"°C","format":"{{value}}","min":0,"max":"40","colors":["#00b500","#e6e600","#ca3838"],"seg1":"","seg2":"","x":630,"y":220,"wires":[]},{"id":"86ef748c.0f3de8","type":"mqtt-broker","z":"","broker":"127.0.0.1","port":"1883","clientid":"","usetls":false,"compatmode":true,"keepalive":"60","cleansession":true,"willTopic":"","willQos":"0","willPayload":"","birthTopic":"","birthQos":"0","birthPayload":""},{"id":"761dfbba.bd8604","type":"ui_group","z":"","name":"Default","tab":"bf26a25d.84e25","disp":true,"width":"6"},{"id":"bf26a25d.84e25","type":"ui_tab","z":"","name":"Home","icon":"dashboard"}]

Extending to relative humidity measurement
******************************************

Now we try to connect the relative humidity sensor to the **Core Module**.
It's possible to connect the `Humidity Tag <https://shop.hardwario.com/humidity-tag/>`_ directly to the **Core Module**
as displayed in the picture or you can use also `Tag Module <https://shop.hardwario.com/tag-module/>`_ which can hold many more sensor tags.
Also the `Battery Module <https://shop.hardwario.com/battery-module/>`_ contains spare connector for sensor tag.

.. note::

    This procedure can be used also for other conencted sensors or `Climate Module <https://shop.hardwario.com/climate-module/>`_.
    You only need to change **topic** to the MQTT broker you are subscribing to.

Then you can use debug nodes in **Node-RED** to get the right MQTT topic and copy and paste it to your new flow.

The MQTT topic will have the format ``node/core-module:0/hygrometer/0:2/relative-humidity``.


Extending to control the relay
******************************

Now let's add the relay control. You can use **Relay Module** or **Power Module**.
Connect the module to the Core Module.
Based on selected module with relay you have to change the topic.

`Power Module <https://shop.hardwario.com/power-module/>`_ has topic ``node/core-module:0/relay/-/state/set``

`Relay Module <https://shop.hardwario.com/relay-module/>`_ has topic ``node/core-module:0/relay/0:0/state/set``

Then you send ``true`` or ``false`` as a payload.


The **Relay Module** has also command to make a single pulse with set duration and relay direction.

Topic is ``node/core-module:0/relay/0:0/pulse/set`` and you have to publish this JSON ``{ "duration": 500, "direction": true}``. Duration is time in milliseconds.

.. code-block:: console

    mosquitto_pub -t "node/core-module:0/relay/0:0/pulse/set" -m "{ \"duration\": 500, \"direction\": true}"

.. _wireles-network:

********************************
Creation of the wireless network
********************************

Currently it is possible to create a wireless network with a star topology.
The middle of the star is the device called the **gateway** which handles communication to all wireless nodes.
Gateway can be **Core Module** or **Radio Dongle**.

All other wireless devices we call as a **node**.

The used radio module **SPIRIT** is comunicating at 868 MHz frequency and with its reach will cover a larger family house and its surroundings.

.. tip::

    More radio information is in the :doc:`Sub-GHz Radio <../interfaces/sub-ghz-radio>` article.

******************************
Flashing Radio Dongle firmware
******************************

If you don't have `Radio Dongle <https://shop.hardwario.com/radio-dongle/>`_ you can use **Core Module** you have already connected to your **Raspberry Pi**.
This module with already flashed firmware can act also as a wireless gateway.

If you own the **Radio Dongle** then disconnect the **Core Module** from **Raspberry Pi** and connect the **Radio Dongle**.
Then follow next steps to flash the latest firmware. Connect the **Radio Dongle** to the **Raspberry Pi**.
The **Radio Dongle** will switch to the programming mode automatically. Just execute the next command:

.. code-block:: console

    bcf flash hardwario/bcf-gateway-usb-dongle:latest

.. note::

    In case you get ``Could not lock device /dev/ttyUSB0`` error,
    that means that the ``bcg`` gateway service is running and uses the same virtual serial port.
    You need to stop bcg temporarily by ``pm2 stop bcg-ud``, then do the ``bcf flash`` and start the service again by ``pm2 restart bcg-ud``.

***************************************
Conversion to the battery operated node
***************************************

HARWDARIO building kit is from the ground-up designed for the efficient battery operation.
Battery powered module with **bcf-generic-node** firmware will automatically scan connected sensors and modules when powered-up.
In the regular intervals the measured values are sent by wireless radio to the gateway.

Place two AAA batteries to the `Mini Battery Module <https://shop.hardwario.com/mini-battery-module/>`_ and connect the **Core Module** to it.

.. note::

    **Core Module** contains active control circuit which selects the best power source available.
    So in case you use the **Battery Module** and at the same time you are flashing/debugging the **Core Module** by USB,
    then the whole is powered by USB to save the battery power.

************************
Flashing the remote node
************************

Upload the ``bcf-generic-node`` firmware to the remote node unit.
This universal firmware contains drivers for all HARDWARIO sensors, tags and modules.
After start-up all the connected devices are automatically detected and their values are sent by wireless network to the **gateway**.

.. tip::

    For longest **battery life** of remote nodes it is best to use firmware with the **kit** in the name.
    They are specially tuned for the longest battery life. You can list them with ``bcf search kit`` command.

.. caution::

    **Flashing Core Module R1 & R2**

    For differences of flashing older **Core Module 1** and newer **Core Module 2** please read :doc:`Core Module R1 and R2 comparison <../hardware/core-module-r1-and-r2-comparison>`

Connect the **Core Module** to the **Raspberry Pi**. Upload the ``generic-node`` with ``firmware-battery-mini`` option.

.. code-block:: console

    bcf flash --device /dev/ttyUSB0 hardwario/bcf-generic-node-battery-mini:latest

In case you would power the remote note with a power adapter,
you can flash ``power module`` firmware for a corresponding number of LED diodes (RGB or RGBWhite) ``hardwario/bcf-generic-node-power-module-rgbw144:latest``.
This firmware is also always listening on the radio and can receive commands co control the LED pixels,
relay and display the measured data on the connected **LCD Module**.
Moreover it is possible to display custom texts on the display with various sized fonts.

`List of bcf-generic-node released firmwares <https://github.com/hardwario/bcf-generic-node/releases>`_

:doc:`Detailed flashing instructions <../firmware/toolchain-guide>`

***************
Pairing process
***************

We need to pair the **gateway** with the remote **node**.
In case you are using **Core Module** as a **gateway** you can start the pairing by long press of the ``B`` button.
Then the red LED will start blinking.

Radio Dongle do not have pairing button and the pairing process needs to be started in the **Playground** or in the **Hub**.

.. thumbnail:: ../_static/tutorials/quick-tutorial/playground-devices-start-pairing.png
   :width: 60%


In command line you enable pairing by commands below.

Command for pairing when you have Radio Dongle as a radio gateway.

.. code-block:: console

    mosquitto_pub -t 'gateway/usb-dongle/pairing-mode/start' -n

Command for pairing when you have Core Module as a radio gateway.

.. code-block:: console

    mosquitto_pub -t 'gateway/core-module/pairing-mode/start' -n

After enabling the pairing the red LED on the **Radio Dongle/Core Module** will start to blink.
Now its the time to send pairing command from the **remote node**.
This is done by power cycling or reseting the **remote node**.

- **Power Cycle** - unplug and then plug again the power to the Core Module. USB cable, battery or Battery Module.
- **Reset the Core Module** - short press of the ``R`` Reset button on the Core Module.

When the node is booting it sends pairing command. If you are subscribed to the ``#`` topic, you will see a message with new paired address.

.. note::

    Older firmwares send remote pairing packet by long-press of ``B`` button.
    Current firmwares are sending remote pairing packet by **power cycling** or **reseting** the module.

Now it is possible to pair other **remote** nodes, by power cycling or reset of other **remote** nodes.

After the pairing of the remotes is completed, stop the pairing process on the **gateway** by command:

.. code-block:: console
    :linenos:

    For Radio Dongle:
    mosquitto_pub -t 'gateway/usb-dongle/pairing-mode/stop' -n
    For Core Module:
    mosquitto_pub -t 'gateway/core-module/pairing-mode/stop' -n

.. tip::

    In the Playground the Pairing process is disabled after each paired device so you never forget to turn it off

************************************
Measuring and controlling over radio
************************************

Remote nodes which has **battery** in the firmware name just transmits measured data and then they sleep.
They cannot receive the commands over the wireless radio while they sleep.

Remote nodes which has **power module** in the firmware name are powered by power adapter or
USB and can transmit measured data and also receive commands send from the **gateway**.
Thanks to this it is possible to control practically all the connected modules over the radio:

- Power Module - control the relay, colors and effects on the LED strip
- Relay Module - control bistable relay with commands to toggle, switch or make a pulse
- LCD Module - display text on the display on any position with different font sizes
- Control red LED on the **Core Module**

:doc:`List of all MQTT topics <../interfaces/mqtt-topics>`

****************************
Conclusion and further steps
****************************

This tutorial explained how to lean HARDWARIO basics with single a module connected to the Raspberry Pi.
The principle is the same with other nodes which you can connect wirelessly.
Now you can extend your home automation and create new rules thanks to **Node-RED**.

