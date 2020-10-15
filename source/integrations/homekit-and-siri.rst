################
HomeKit and Siri
################

With HomeKit integration you will be able to control your IoT projects from your iOS or macOS device. After you have your device in your Home app,
you can control it using Siri.
In the end of article you will ask Siri for temperature in your bedroom and she will tell you back temperature from your HARDWARIO temperature sensor!

************
Installation
************

If you want to use following integration on `HARDWARIO Hub <https://shop.hardwario.com/raspberry-pi-4b-4gb-set/>`_ or on Debian and Ubuntu system,
you have to install few dependencies.
Connect to command line of HARDWARIO Hub, use article :doc:`Rasperry Pi Login <../tutorials/raspberry-pi-login>`. After you login in, copy, paste and run commands.

.. code-block:: console

    sudo apt-get update

.. code-block:: console

    sudo apt-get install libavahi-compat-libdnssd-dev

Open HARDWARIO Hub in your Browser (Linux and macOS can use hub.local, on Windows you have to use IP address of HARDWARIO Hub).
In menu select functions and on top right corner click on hamburger menu. Click on manage palette and select Install card, where search:

.. code-block:: console

    node-red-contrib-homekit-bridged

.. thumbnail:: ../_static/integrations/homekit-siri/node-red-pallete.png
   :width: 100%
   :alt: Node-Red palette install

When message with title Installing **'node-red-contrib-homekit-bridged'** pops up, just click Install. After Installation you will see module in advacted group.

.. thumbnail:: ../_static/integrations/homekit-siri/node-red-advanced-tab.png
   :width: 100%
   :alt: Node-Red advanced tab

****************
Connect hardware
****************

.. _flash-firmware:

Step 1: Flash firmware
**********************

We have installed HomeKit plugin to Node-RED. Now open `HARDWARIO Playground <https://www.hardwario.com/download/>`_ on your computer.
Prepare microUSB cable, `Core Module <https://shop.hardwario.com/core-module/>`_
and battery module (`standard <https://shop.hardwario.com/battery-module/>`_ or `mini <https://shop.hardwario.com/mini-battery-module/>`_).
Connect Core Module to computer via microUSB cable. Click on **Firmware** tab in menu,
use hardwario/bcf-radio-push-button and Click Flash.

.. thumbnail:: ../_static/integrations/homekit-siri/playgroud-flash-firmware.png
   :width: 100%
   :alt: Playground Flash Firmware

Step 2: Pair Hardware
*********************

Open HARDWARIO Hub page in browser same as in chapter Instalation and select **Device** tab in menu and click on **Start pairing** button.

.. thumbnail:: ../_static/integrations/homekit-siri/playgroud-pair-hardware.png
   :width: 100%
   :alt: Playground Pair Hardware

Step 3: Assembly Hardware
*************************

Now unplug Core Module from microUSB cable and connect it to battery module (standart or mini).

.. thumbnail:: ../_static/integrations/homekit-siri/homekit-and-siri-Core-standart-battery.jpg
   :width: 100%
   :alt: Core Module with Battery Module

Step 4: Ending
**************

You have to see connected device now. You can look at **Messages** tab and see that temperature is incoming now.

******************
Make it functional
******************

Step 1: Open Functions tab in menu. Open Hamburger menu, select Import > Clipboard and paste following code
***********************************************************************************************************

.. code-block:: json

    [{"id":"c10a49.8c0905b8","type":"mqtt in","z":"2c41a2bd.aa36ae","name":"Temperature from Core Module","topic":"node/push-button:0/thermometer/0:1/temperature","qos":"2","broker":"29fba84a.b2af58","x":230,"y":180,"wires":[["d7033322.3f2d5"]]},{"id":"d7033322.3f2d5","type":"template","z":"2c41a2bd.aa36ae","name":"Convert payload to HomeKit JSON format","field":"payload","fieldType":"msg","format":"handlebars","syntax":"mustache","template":"{\n\"CurrentTemperature\": \"{{payload}}\"\n}","output":"str","x":600,"y":180,"wires":[[]]},{"id":"29fba84a.b2af58","type":"mqtt-broker","z":"","broker":"127.0.0.1","port":"1883","clientid":"","usetls":false,"compatmode":true,"keepalive":"60","cleansession":true,"birthTopic":"","birthQos":"0","birthPayload":"","willTopic":"","willQos":"0","willPayload":""}]

So flow should looks like following:

.. thumbnail:: ../_static/integrations/homekit-siri/playground-flow-basic.png
   :width: 100%
   :alt: Flow Basic

Step 2: Place Homekit node from advanced group and connect it to template node in flow
**************************************************************************************

.. thumbnail:: ../_static/integrations/homekit-siri/homekit-connected.png
   :width: 100%


Step 3: Double-click on HomeKit node in flow, settings should popup
*******************************************************************

.. thumbnail:: ../_static/integrations/homekit-siri/homekit-settings.png
   :width: 100%


Step 4: Setup bridge
********************

Let's setup bridge. Bridge is basically, bridge, between our Hardware sensors and your iPhones,
iPads, Macs, etc... So Click on little pencil icon next to the bridge chapter of setting and fill it as following and click Add:

.. thumbnail:: ../_static/integrations/homekit-siri/home-kit-bridge-settings.png
   :width: 50%
   :alt: Bridge Settings

Step 5: Fill the rest of the settings according to the screenshot below. Click Done and Deploy
**********************************************************************************************

.. thumbnail:: ../_static/integrations/homekit-siri/home-kit-settings.png
   :width: 50%
   :alt: HomeKit Settings

Step 6: Pairing
***************

Now as you can see on your screen and screenshot bellow. Device is waiting for pairing with code 111-11-111.
So open Home app on your iPhone or iPad and click Add Accessory > Don't Have a Code or Can't Scan > HARDWRIO bridge.
Add anyway on next screen. In screen where you have to input code, input just 1 to all boxes:

.. thumbnail:: ../_static/integrations/homekit-siri/homekit-and-siri-iPhones-screens-1.png
   :width: 100%
   :alt: Pairing Home Kit

Step 7: Setup
*************

Now just setup where is your bridge and temperature sensor and your sensor is added!

.. thumbnail:: ../_static/integrations/homekit-siri/homekit-and-siri-iPhones-screens-2.png
   :width: 100%
   :alt: Setup

****
Siri
****
If you have some device in Home app, you can control it or get infromation via Siri.
So if you want to get temperature from Core Module which we just set up, just ask Siri "what's the temperature in bedroom?" (or what room you selected).

.. thumbnail:: ../_static/integrations/homekit-siri/homekit-and-siri-iPhones-screens-siri.png
   :width: 90%
   :alt: Siri Test

**********
Conclusion
**********
With HomeKit plugin you are able to simulate real HomeKit devices.
This plugin can also control things. So you can use it to control `Relay Module <https://shop.hardwario.com/relay-module/>`_, etc...
This plugin have little issue. Every time, you Deploy flow, you have to reset all Node-RED, or the HomeKit plugin won't work.
You can do it by following command (you have to do it on HARDWARIO hub if the plugin is installed there):

.. code-block:: console

    pm2 restart node-red
