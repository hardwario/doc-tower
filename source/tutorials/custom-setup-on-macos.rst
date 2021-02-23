#####
macOS
#####

************
Introduction
************

If you need more permanent solution than **HARDWARIO Playground** you can install all the services yourself in your system.
This guide will help you to install and configure these services:

- HARDWARIO Gateway ``bcg``
- HARDWARIO Firmware Tool ``bcf``
-
    - If you want to develop firmware please visit the :doc:`Firmware section <../firmware/basic-overview>`.

- HARDWARIO Host Tool ``bch``
- Mosquitto MQTT broker
- Node-RED
- The process manager ``pm2``

**************************
Playground Setup on macOS
**************************

- open **Terminal** application

Step 1: Install the driver for the HARDWARIO Radio Dongle
*********************************************************

- `Download & Install drivers from FTDI <http://www.ftdichip.com/Drivers/VCP/MacOSX/FTDIUSBSerialDriver_v2_4_2.dmg>`_

Step 2: Restart your computer
*****************************

Step 3: Install `Homebrew <https://brew.sh>`_
*********************************************

.. code-block:: console

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Step 4: Upgrade all packages
****************************

.. code-block:: console

    brew update && brew upgrade

Step 5: Install Mosquitto server and clients
********************************************

.. code-block:: console

    brew install mosquitto

.. code-block:: console

    brew services start mosquitto

Step 6: Install Node.js version 6 (required by Node-RED)
********************************************************

.. code-block:: console

    brew install node

Step 7: Install Node-RED
************************

.. code-block:: console

    sudo npm install -g --unsafe-perm node-red

Step 8: Install node-red-dashboard for graphs, gauges, buttons
**************************************************************

.. code-block:: console

    cd ~/.node-red/

.. code-block:: console

    npm i node-red-dashboard

Step 9: Install PM2
*******************

.. code-block:: console

    sudo npm install -g pm2

.. tip::

    **PM2** is a process manager that will help you to start **Node-RED** and other processes on boot.

Step 10: Tell PM2 to run Node-RED
*********************************

.. code-block:: console

    pm2 start `which node-red`

Step 11: Tell PM2 to run on boot
********************************

.. code-block:: console

    pm2 save

.. code-block:: console

    pm2 startup

.. caution::

    Now you must follow the instructions provided by the command *pm2 startup systemd*.

Step 12: Install Python 3 (required by the HARDWARIO Firmware Tool and HARDWARIO Gateway)
*****************************************************************************************

.. code-block:: console

    brew install python3

Step 13: Update pip (Python Package Manager) to the latest version
******************************************************************

.. code-block:: console

    sudo pip3 install --upgrade --no-cache-dir pip

Step 14: Install the HARDWARIO Firmware Tool
********************************************

.. code-block:: console

    sudo pip3 install --upgrade --no-cache-dir bcf

Step 15: Install the HARDWARIO Gateway
**************************************

.. code-block:: console

    sudo pip3 install --upgrade --no-cache-dir bcg

Step 16: Plug the HARDWARIO Radio Dongle into a USB port
********************************************************

Step 17: List the available devices
***********************************

.. code-block:: console

    bcf devices

.. tip::

    You can use ``-v`` parameter to see verbose information about the connected devices (possibly helping you to identify them).

Step 18: Upload the latest firmware into the HARDWARIO Radio Dongle
*******************************************************************

.. code-block:: console

    bcf update

.. code-block:: console

    bcf flash hardwario/bcf-gateway-usb-dongle:latest

Step 19: Start the HARDWARIO Gateway as PM2 service
***************************************************

.. code-block:: console

    pm2 start `which python3` --name "bcg-ud" -- `which bcg` --device ...

.. important::

    Replace ``...`` with the device listed using ``bcf devices``.

.. caution::

    If you want to update firmware in the **Radio Dongle**, first you have to stop **bcg** by the command ``pm2 stop bcg-ud``.
    After update, restart the service by the command ``pm2 restart bcg-ud``.

Step 20: Open your web browser with the URL
*******************************************

- http://localhost:1880/

***************************
Playground Upgrade on macOS
***************************

Upgrade all the packages
************************

.. code-block:: console

    brew update && brew upgrade

Upgrade Node-RED
****************

.. code-block:: console

    sudo npm update -g node-red

Upgrade PM2
***********

.. code-block:: console

    sudo npm update -g pm2

Upgrade the HARDWARIO Firmware Tool
***********************************

.. code-block:: console

    sudo pip3 install --upgrade --no-cache-dir bcf

Upgrade the HARDWARIO Gateway
*****************************

.. code-block:: console

    sudo pip3 install --upgrade --no-cache-dir bcg

