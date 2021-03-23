#########################
Raspberry Pi Installation
#########################

************
Introduction
************

In the following procedure, we will install the **HARDWARIO Raspbian** Linux distribution.
Raspbian is the official and most widely distributed Linux distribution for Raspberry Pi.

HARDWARIO maintains a modified version of this distribution that facilitates some steps and includes pre-installed packages that are key to **HARDWARIO**.

.. caution::

    If you already have Raspberry Pi with the original Raspbian distribution, go to the section :ref:`Setup on Original Raspbian <setup-original-raspbian>`.
    Or if you have OSMC, go to section Setup on OSMC

.. note::

    Raspberry Pi is a small, affordable, single-board computer that is able to run Linux operating system.
    HARDWARIO TOWER uses this system to process sensor information, actuator control,
    decision logic for automation, data storage, or serve as a gateway to connect cloud services.


************
Requirements
************

- Raspberry Pi 3b or better
- MicroSD card with a minimum capacity of 4 GB
- MicroSD Card Reader (+ optional SD Card Adapter)
- Ethernet cable
- Workstation or laptop
- Router (or LAN switch) with the DHCP server set up
- One of the following operating systems:
    - Windows 7, 8.x, 10 (32-bit or 64-bit)
    - macOS (tested on version 10.12.x)
    - Ubuntu (tested on version 18.04.2 LTS)

***************************
Instructions for Installing
***************************

.. important::

    After you flash SD card, connect Ethernet, Radio Dongle and only after that apply the power to Raspberry Pi.

Download
********

- `HARDWARIO Raspian <https://github.com/hardwario/bc-raspbian/releases/latest>`_
- `balenaEtcher <https://www.balena.io/etcher/>`_

Flash
*****

#. Insert microSD card to reader in you computer
#. Open balenaEtcher you've downloaded
#. Select HARDWARIO Raspian which you also downloaded
#. Select inserted SD card
#. Click flash
#. After flashing is done, insert microSD card to Raspberry Pi, **you have to connect Radio Dongle before applying power**.
#. Connect microUSB power adapter and Ethernet cable or use Wifi setup in next part

*********************
WiFi Setup (optional)
*********************

If you would not like to use ethernet cable, you can connect Raspberry Pi over your WiFi

#. Connect microSD card with HARDWARIO Raspbian to computer
#. Open boot section in your file explorer or Finder
#. Create file **wpa_supplicant.conf**
#. Edit file with next text, then save and insert microSD card back to Raspberry Pi:

.. code-block:: console
    :linenos:

    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1

    network={
        ssid="YOUR_NETWORK_NAME"
        psk="YOUR_PASSWORD"
    }

***************************
Connecting to HARDWARIO HUB
***************************

After Raspberry Pi boots up, use your computer's web browser and enter the Raspberry Pi ``IP`` address to open the HARDWARIO HUB webpage.

.. tip::

    You can also use the hostname `hub.local <http://hub.local>`_

.. note::

    To find out Raspberry Pi IP you can follow the :doc:`next chapter <raspberry-pi-login>`.

.. thumbnail:: ../_static/tutorials/raspberry-pi-installation/hub-example.png
    :width: 90%

.. caution::

    If Start pairing button is disabled and you cannot press it. Please make sure you first connect Radio Dongle and then apply the power to Rasberry Pi.

    If you are still having trouble with connecting to Radio Dongle it can be because you did ``apt update`` and ``apt upgrade``.
    There is an issue with mosquitto that anonymous connections are not allowed.

    To fix this issue just run the following command: ``echo 'allow_anonymous true' | sudo tee /etc/mosquitto/conf.d/auth.conf``
