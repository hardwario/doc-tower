######################
Custom Setup on Ubuntu
######################

************
Introduction
************

If you need more permanent solution than HARDWARIO Playground you can install all the services yourself in your system.
This guide will help you to install and configure these services:

- HARDWARIO Gateway ``bcg``
- HARDWARIO Firmware Tool ``bcf``
- HARDWARIO Host Tool ``bch``
- Mosquitto MQTT broker
- Node-RED
- The process manager ``pm2``

**************************
Playground Setup on Ubuntu
**************************

- open **Terminal** application

Upgrade all packages
********************

.. code-block:: console

    sudo apt update && sudo apt upgrade

Install Mosquitto server and clients
************************************

.. code-block:: console

    sudo apt install mosquitto mosquitto-clients

Install Node.js version 6 (required by Node-RED)
************************************************

.. code-block:: console

    sudo apt install nodejs libnode64 npm

Install Node-RED
****************

.. code-block:: console

    sudo npm install -g --unsafe-perm node-red

Install node-red-dashboard for graphs, gauges, buttons
******************************************************

.. code-block:: console

    sudo npm install -g node-red-dashboard

Install PM2
***********

.. code-block:: console

    sudo npm install -g pm2

Tell PM2 to run Node-RED
************************

.. code-block:: console

    pm2 start `which node-red`

Tell PM2 to run on boot
***********************

.. code-block:: console

    pm2 save

.. code-block:: console

    pm2 startup systemd

.. warning::

    Now you must follow the instructions provided by the command ``pm2 startup systemd``.

Install Python 3 (required by the HARDWARIO Firmware Tool and HARDWARIO Gateway)
********************************************************************************

.. code-block:: console

    sudo apt install python3.8 python3-pip

Update pip (Python Package Manager) to the latest version
*********************************************************

.. code-block:: console

    sudo pip3 install --upgrade --no-cache-dir pip

Install the HARDWARIO Firmware Tool
***********************************

.. code-block:: console

    sudo pip3 install --upgrade --no-cache-dir bcf

Install the HARDWARIO Gateway
*****************************

.. code-block:: console

    sudo pip3 install --upgrade --no-cache-dir bcg

Add yourself to the dialout user group
**************************************

.. code-block:: console

    sudo usermod $USER -a -G dialout

Plug the HARDWARIO Radio Dongle into a USB port
***********************************************

List the available devices
**************************

.. code-block:: console

    bcf devices

.. tip::

    You can use ``-v`` parameter to see verbose information about the connected devices (possibly helping you to identify them).

Upload the latest firmware into the HARDWARIO Radio Dongle
**********************************************************

.. code-block:: console

    bcf update

.. code-block:: console

    bcf flash hardwario/bcf-gateway-usb-dongle:latest

Start the HARDWARIO Gateway as PM2 service
******************************************

.. code-block:: console

    pm2 start `which python3` --name "bcg-ud" -- `which bcg` --device ...

.. important::

    Replace ``...`` with the device listed using ``bcf devices``.

.. warning::

    If you want to update firmware in the **Radio Dongle**, first you have to stop **bcg** by the command ``pm2 stop bcg-ud``.
    After update, restart the service by the command ``pm2 restart bcg-ud``.

Open your web browser with the URL
**********************************

- http://localhost:1880/

****************************
Playground Upgrade on Ubuntu
****************************

Upgrade all the packages
************************

.. code-block:: console

    sudo apt update && sudo apt upgrade

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
