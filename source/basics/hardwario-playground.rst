####################
HARDWARIO Playground
####################

HARDWARIO Playground is free **Windows, macOS** and **Linux** software that enables you to:

- **Flash firmware** to Core Module
- **Manage wireless network** with Radio Dongle and nodes
- **Create programs** with visual programming in the **Node-RED**
- **Visualize** measured values and control nodes with Dashboard

.. thumbnail:: ../_static/basics/playground/playground-node-red.png
   :width: 100%
   :alt: Playground Functions Tab

*****************************
Download HARDWARIO Playground
*****************************

Use `HARDWARIO Playground download page <https://www.hardwario.com/download/>`_ which always have the links of the latest version.

.. thumbnail:: ../_static/basics/playground/download-page.png
   :alt: Playground Functions Tab

Builds are also in `github releases <https://github.com/hardwario/bch-playground/releases>`_.

***************
Video tutorials
***************

If you like video tutorials, you can watch quick guide to the HARDWARIO Playground in 5 videos.
They explain flashing, pairing, Dashboard and Node-RED

.. raw:: html

    <iframe width="700" height="422" src="https://www.youtube.com/embed/nzFtmhLNy-I?list=PLfRfhTxkuiVw0s9UQ8x5irref-EBwOghF" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Devices
*******

On this tab you connect to the Radio Dongle. Choose the Radio Dongle (``twr-usb-dongle``) from the list and click Connect


.. thumbnail:: ../_static/basics/playground/playground-devices-connect.png
   :width: 40%
   :alt: Playground Device

After connecting to the Radio Dongle you could see all the paired wireless nodes.
The node alias is later used in MQTT message topic (``node/climate-monitor:0/..``),
**so change it only when you know what are you doing.**

.. thumbnail:: ../_static/basics/playground/playground-devices-paired.png
   :width: 100%
   :alt: Playground Paired Devices

.. _pairing-new-devices:

**Pairing new modules:**

#. Disconnect power from the wireless node (remove batteries or Battery Module, disconnect the USB cable, remove DC jack from Power Module)
#. Click on the **Start pairing** button
#. Apply power to the wireless module
#. Repeat with all the modules you want to pair

.. raw:: html

    <iframe width="700" height="422" src="https://www.youtube.com/embed/ESrTEdV9PJQ?list=PLfRfhTxkuiVw0s9UQ8x5irref-EBwOghF" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Functions
*********

This tab is the `Node-RED <https://nodered.org/about/>`_ visual programming tool. See :doc:`Projects <projects>` how to use this visual programming tool.

.. thumbnail:: ../_static/basics/playground/playground-node-red-flow.png
   :width: 100%
   :alt: Playground Functions Flow

.. raw:: html

    <iframe width="700" height="422" src="https://www.youtube.com/embed/VW_-RCIZ9rY?list=PLfRfhTxkuiVw0s9UQ8x5irref-EBwOghF" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

*********
Dashboard
*********

Here you can display gauges, graphs, buttons and other widgets. See the `Projects <https://www.hackster.io/hardwario/projects>`_ how to use Dashboard.

.. thumbnail:: ../_static/basics/playground/playground-dashboard.png
   :width: 70%
   :alt: Playground Dashboard

********
Messages
********

Here you can see all the messages from wireless nodes. You can copy the topics to clipboard and use them in Node-RED in the ``topic`` textbox.

.. thumbnail:: ../_static/basics/playground/playground-messages.png
   :width: 100%
   :alt: Playground Messages

Firmware
********

This tab allows you to flash pre-compiled firmware for all HARDWARIO projects from out GitHub.
List of firmware is downloaded automatically.
Choose the firmware or start typing to find project you like to try. You can also flash binary or HEX file from your computer.

Always make sure you are flashing the right Device, usually ``twr-core-module``.
If you would like to update Radio Dongle, disconnect it first in the Devices tab.

.. raw:: html

    <iframe width="700" height="422" src="https://www.youtube.com/embed/3IXLBQ5M6Us?list=PLfRfhTxkuiVw0s9UQ8x5irref-EBwOghF" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

.. thumbnail:: ../_static/basics/playground/playground-firmware.png
   :width: 100%
   :alt: Playground Firmware

***************
Troubleshooting
***************

Cannot find the Radio Dongle or Core Module in the device list

- On Windows 7 and macOS please install the `FTDI VCP drivers <https://www.ftdichip.com/Drivers/VCP.htm>`_
- On Ubuntu you need to be in ``dialout`` user group. Please use command ``sudo usermod -a -G dialout $USER`` and restart computer
- HARDWARIO Playground cannot flash older Core Module Revision 1. Please use the ``bcf`` tool. :doc:`See version comparison <../hardware/core-module-r1-and-r2-comparison>`
