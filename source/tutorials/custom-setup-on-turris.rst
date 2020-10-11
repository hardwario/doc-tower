######################
Custom Setup on Turris
######################

If you need more permanent solution than **HARDWARIO Playground** you can install all the services yourself in your system.
This guide will help you to install and configure these services:

- HARDWARIO Gateway ``bcg``
- HARDWARIO Firmware Tool ``bcf``
- HARDWARIO Host Tool ``bch``
- Mosquitto MQTT broker
- Node-RED
- The process manager ``pm2``

.. _turris-instalation:

************
Installation
************

Step 1: Update the package
**************************

.. code-block:: console

    opkg update

Step 2: Install the driver for the HARDWARIO Radio Dongle and HARDWARIO Core module
***********************************************************************************

.. code-block:: console
    :linenos:

    opkg install kmod-usb-serial-ftdi kmod-usb-acm
    insmod ftdi_sio
    insmod cdc_acm

Step 3: Install `Mosquitto <https://mosquitto.org>`_ server and clients
***********************************************************************

.. code-block:: console

    opkg install mosquitto mosquitto-client

Step 4: Enable service for Mosquitto
************************************

.. code-block:: console

    /etc/init.d/mosquitto enable

Step 5: Start Mosquitto service
*******************************

.. code-block:: console

    /etc/init.d/mosquitto start

Step 6: Install Python 3 (required by the HARDWARIO Gateway and HARDWARIO Firmware Tool)
****************************************************************************************

.. code-block:: console

    opkg install python3 python3-pip

Step 7: Install the HARDWARIO Gateway, HARDWARIO Flash Tool and HARDWARIO Host Tool
************************************************************************************

.. code-block:: console

    pip3 install --upgrade --no-cache-dir bcg

.. code-block:: console

    pip3 install --upgrade --no-cache-dir bcf

.. code-block:: console

    pip3 install --upgrade --no-cache-dir bch

***************************************
Finishing for Radio Dongle as a gateway
***************************************

Follow these steps if you have `Radio Dongle <https://shop.hardwario.com/radio-dongle/>`_ as a gateway.

Step 1: Finish :ref:`installation <turris-instalation>` part
************************************************************

Step 2: Download configuration
******************************

.. code-block:: console

    wget "https://raw.githubusercontent.com/bigclownlabs/bch-gateway/master/turris/etc/config/bc-gateway-usb-dongle" -O /etc/config/bc-gateway-usb-dongle

Step 3: Make sure the configuration works
*****************************************

.. code-block:: console

    uci show bc-gateway-usb-dongle

Step 4: Download Init Script
****************************

.. code-block:: console

    wget "https://raw.githubusercontent.com/bigclownlabs/bch-gateway/master/turris/etc/init.d/bc-gateway-usb-dongle" -O /etc/init.d/bc-gateway-usb-dongle

Step 5: Add execute permission
******************************

.. code-block:: console

    chmod u+x /etc/init.d/bc-gateway-usb-dongle

Step 6: Enable service for gateway
**********************************

.. code-block:: console

    /etc/init.d/bc-gateway-usb-dongle enable

Step 7: Start service
*********************

.. code-block:: console

    /etc/init.d/bc-gateway-usb-dongle start
