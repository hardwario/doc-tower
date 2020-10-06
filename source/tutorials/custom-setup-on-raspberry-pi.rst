############################
Custom Setup on Raspberry Pi
############################

If you need more permanent solution than **HARDWARIO Playground** you can install all the services yourself in your system.
This guide will help you to install and configure these services:

- HARDWARIO Gateway ``bcg``
- HARDWARIO Firmware Tool ``bcf``
- HARDWARIO Host Tool ``bch``
- Mosquitto MQTT broker
- Node-RED
- The process manager ``pm2``

**************************************
Differences from the Original Raspbian
**************************************

This is a brief list of differences:

- Hostname is ``hub`` instead of ``raspberrypi``.
- The time zone is set to ``Europe/Prague``.
- The following records were added to the repository APT list:
    - https://deb.nodesource.com/node_8.x
    - http://repo.mosquitto.org/debian
- By default, these packages are also installed:
    - mosquitto
    - mosquitto-clients
    - nodejs
    - python3-pip
    - python3-venv
    - dfu-util
    - git
    - htop
    - mc
    - tmux
    - npm pm2
    - npm node-red
    - pip3 bcf
    - pip3 bcg

.. _setup-original-raspbian:

**************************
Setup on Original Raspbian
**************************

.. caution::

    Apply the following procedure only if you are using Raspberry Pi, on which the original Raspbian distribution is running.
    This is an alternative way of installing ``bc-raspbian`` in [](/doc/tutorials/raspberry-pi-installation/).

Log in to the Raspberry Pi using SSH. Detailed procedure is provided in the document :doc:`Raspberry Pi Login <raspberry-pi-login>`
************************************************************************************************************************************

Upgrade all packages
********************

.. code-block:: console

    sudo apt update && sudo apt upgrade

Install Mosquitto server and clients
************************************

.. code-block:: console

    sudo apt install mosquitto mosquitto-clients

Install Node.js version 8 (required by Node-RED)
************************************************

.. code-block:: console

    curl -sL  https://deb.nodesource.com/setup_8.x | sudo -E bash -

.. code-block:: console

    sudo apt-get install -y nodejs

Install Node-RED
****************

.. code-block:: console

    sudo npm install -g --unsafe-perm node-red

Install PM2
***********

.. code-block:: console

    sudo npm install -g pm2

Tell PM2 to run Node-RED
************************

Make sure you copy next command exactly with the back-tick symbol, you can use the copy button on the right

.. code-block:: console

    pm2 start `which node-red` -- --verbose

.. code-block:: console

    pm2 save

Tell PM2 to run on boot
***********************

.. code-block:: console

    sudo -H PM2_HOME=/home/$(whoami)/.pm2 pm2 startup systemd -u $(whoami)

.. code-block:: console

    sudo -H chmod 644 /etc/systemd/system/pm2-$(whoami).service

Install Python 3 (required by the HARDWARIO Firmware Tool and HARDWARIO Gateway)
********************************************************************************

.. code-block:: console

    sudo apt install python3 python3-pip python3-setuptools

Update pip (Python Package Manager) to the latest version
*********************************************************

.. code-block:: console

    sudo pip3 install --upgrade pip

Install the HARDWARIO Firmware Tools
************************************

HARDWARIO Firmware Tool ``bcf``, HARDWARIO Gateway ``bcg`` and HARDWARIO Host Tool ``bch``.

.. code-block:: console

    sudo pip3 install --upgrade bcf bcg bch

Add udev rules
**************

.. code-block:: console

    echo 'SUBSYSTEMS=="usb", ACTION=="add", KERNEL=="ttyUSB*", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6015", ATTRS{serial}=="bc-usb-dongle*", SYMLINK+="bcUD%n", TAG+="systemd", ENV{SYSTEMD_ALIAS}="/dev/bcUD%n"'  | sudo tee --append /etc/udev/rules.d/58-bigclown-usb-dongle.rules

.. important::

    Unplug and plug gateway.

Run service for Gateway Radio Dongle
************************************

.. code-block:: console

    pm2 start /usr/bin/python3 --name "bcg-ud" -- /usr/local/bin/bcg --device /dev/bcUD0

.. code-block:: console

    pm2 save
