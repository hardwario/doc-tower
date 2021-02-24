###########
Devices Tab
###########

On this tab you connect to the Radio Dongle. Choose the Radio Dongle (``twr-usb-dongle``) from the list and click Connect

.. thumbnail:: ../../_static/basics/playground/playground-devices-connect.png
   :width: 40%
   :alt: Playground Device

After connecting to the Radio Dongle you could see all the paired wireless nodes.

.. caution::

    The node alias is later used in MQTT message topic (``node/climate-monitor:0/..``),
    **so change it only when you know what are you doing.**

.. thumbnail:: ../../_static/basics/playground/playground-devices-paired.png
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

.. important::

    Go to the next document to learn about :doc:`Messages Tab <messages>`.
