#################
Quick Start Guide
#################

**********************
Thank You, Dear Maker!
**********************

If you are reading this QUICK START GUIDE you have probably purchased our HARDWARIO TOWER - Industrial IoT Kit.
If not, `go shopping <https://shop.hardwario.com>`_ to do so :)

Once again **THANK YOU** for being our supporter, we really appreciate this.

HARDWARIO is not just about the hardware but it comes with full documentation, tutorials,
software tools and most importantly - it comes with the extensive **technical support**.
HARDWARIO doesn't hesitate to use one of these channels In case you run in troubles or if anything is not clear to you:

- Write us an email to ask@hardwario.com
- Use forum at https://forum.hardwario.com/
- Use the online chat icon in the bottom right corner

***********
Be Inspired
***********

It's always hard to build something without an inspiration.
We motivate our makers to share their work with others and you can get ideas for your projects by subscribing to our Clownsletter.

*********
Get Ready
*********

In our world it means to prepare a center of your IoT system - the Hub. In QUICK START GUIDE we will use your computer as a Hub. Just follow these steps:

Delivery
********

In delivered box find a **Radio Dongle** and plug it to any USB port of your computer.

.. _download-playground:

Download the latest Playground
******************************

- Go to the `HARDWARIO Playground Download page. <https://www.hardwario.com/download/>`_

Run the HARDWARIO Playground
****************************

Go to the **Devices** tab, choose the **Radio Dongle** serial port and click **Connect**

.. thumbnail:: ../_static/basics/quick-start-guide/playground-devices-tab.png
    :width: 60%

.. tip::

    If you cannot see Radio Dongle in the devices, please see the :ref:`Troubleshooting chapter. <troubleshooting-chapter>`

Radio kits delivered together with your `Radio Dongle <https://shop.hardwario.com/radio-dongle/>`_ are already programmed and paired,
please check that out in the image below.

.. thumbnail:: ../_static/basics/quick-start-guide/playground-devices-paired.png
    :width: 60%

*************
Build devices
*************

By building devices we mean putting modules and enclosure together, optionally flashing a new firmware and pairing devices with a Radio Dongle.

Build delivered kits or build devices from modules (check the `video guides <https://www.youtube.com/playlist?list=PLfRfhTxkuiVyc9P1TWw_DnAeh2INXwpFK>`_ how to do so).
Do not put batteries to the battery module yet.

.. caution::

    Be careful how you connect Mini Battery Module to the other modules. Look at the image below so you know how to do it.

.. thumbnail:: ../_static/basics/quick-start-guide/mini-battery-module-orientation.png
    :width: 60%

As mentioned, delivered kits are already programmed with a right firmware.
If you would like to change it to another firmware in the Core Module, please follow this :ref:`firmware flash chapter. <flash-firmware>`


Radio Pairing
*************

As mentioned, kits delivered together with Radio Dongle are already paired and should be visible in Playground's **Devices** tab.
In case you need to pair new devices, please follow these :ref:`radio pairing instructions. <pairing-new-devices>`


Playground's Messages
*********************

Switch to Playground's **Messages** tab and put batteries to your kit, you should see incoming messages.
Every kit sends different messages. Here the **Button kit** sends temperature, voltage, event-count (everytime you press the button) and other messages.

.. thumbnail:: ../_static/basics/quick-start-guide/playground-messages.png
    :width: 60%

3D-printed enclosure
********************

Put modules to the 3D-printed enclosure and fix it with O-rings.

************
Add function
************

Now it's time to give your system a logic and connect it with desired platforms.

In **QUICK START GUIDE** we will create a simple dashboard with a temperature gauge. Again, just follow these steps:

Messages
********

Switch to the **Messages**, you should see incoming messages from the previous step.
Copy the **bold** text (called **topic**) that ends with *temperature* **to the clipboard**.

.. important::

    You can use the copy icon in each message. Make sure you copy just text and no space before or after the text.

Your **topic** could be different based on your kit name.
You can also copy any other topic that your module supports from the :doc:`MQTT topics list. <../interfaces/mqtt-topics>`

.. thumbnail:: ../_static/basics/quick-start-guide/playground-messages-topic.png
    :width: 60%

Function
********

Switch to the **Functions** tab and from the color blocks on the left side drag and drop **mqtt input** block and
**gauge** block to the **flow** in the middle of the screen. The color blocks are called **nodes**.
You can use the ``filter nodes`` text box to find the right block. Connect the two created nodes together.

.. thumbnail:: ../_static/basics/quick-start-guide/playground-functions-tab.png
    :width: 60%


.. thumbnail:: ../_static/basics/quick-start-guide/playground-functions-connected.png
    :width: 60%

You have to modify the mqtt node and add the broker. Double click on it and then click on the little pencil on the right.

.. thumbnail:: ../_static/basics/quick-start-guide/playground-functions-mqtt-edit-server.png
    :width: 60%

After that you just have to type in the **localhost** or any of your MQTT broker addresses and then click **Add**. Finally click **Done**.

.. thumbnail:: ../_static/basics/quick-start-guide/playground-functions-mqtt-edit-server-localhost.png
    :width: 60%

Double click on the **gauge** node. Change **Label**, **Units** and **Range** to your needs.
Then click **Done**. Double click on the **mqtt node** and paste the previously copied topic from the clipboard.
Make sure there are not any spaces before and after the copied text. Then click **Done** and **Deploy** button.
You have to click on the **Deploy** everytime you make changes in your flow.

.. thumbnail:: ../_static/basics/quick-start-guide/playground-functions-mqtt-node.png
    :width: 60%

Dashboard
*********

Go to Playground's **Dashboard** tab and you should see a gauge with the temperature of the selected device.

.. tip::

    The temperature can take a while to appear. You can breathe on the module or reconnect batteries for immediate update.

.. thumbnail:: ../_static/basics/quick-start-guide/playground-dashboard.png
    :width: 60%

*****
Share
*****

.. note::

    Don't be shy and share your projects with others. We will reward you by a **100 EUR** discount coupon if your project will be displayed on our web.

**********
Learn More
**********

The goal of this **QUICK START GUIDE** is to show the basics in a few simple steps.
Now you can learn more by browsing the **documentation** or by visiting the **links below**.

- Take a look at the :doc:`Module Overview. <module-overview>`
- Learn about :doc:`HARDWARIO MQTT topics <../interfaces/mqtt-topics>` to control LEDs and relays.
- Try other integrations with :doc:`Grafana <../integrations/grafana-for-visualization>`, :doc:`Blynk <../integrations/blynk-mobile-app-builder>`, :doc:`Ubidots <../integrations/ubidots>` and others.
- Use your :doc:`Raspberry PI <../tutorials/raspberry-pi-installation>` or other single board computer (SBC) as a server.
- :ref:`Flash other firmware <flash-firmware>` or :doc:`write your own firmware <../firmware/basic-overview>` for the **Core Module.**
- Check the :doc:`Core Module pinouts <../hardware/header-pinout>` and add your own buttons, relays and sensors.

.. _troubleshooting-chapter:

***************
Troubleshooting
***************

Cannot find the Radio Dongle or Core Module in the device list

- On Windows 7 and macOS please install the `FTDI VCP drivers <https://www.ftdichip.com/Drivers/VCP.htm>`_
- On Ubuntu you need to be in ``dialout`` user group. Please use command ``sudo usermod -a -G dialout $USER`` and restart computer
- HARDWARIO Playground cannot flash older Core Module Revision 1. Please use the ``bcf`` tool. :doc:`See version comparison <../hardware/core-module-r1-and-r2-comparison>`
