#################
HARDWARIO Gateway
#################

This multi-platform Python tool connects USB gateway to the MQTT. USB gateway is communicating over virtual USB serial port with JSONs.

Gateway can be run in command line or by ``pm2`` service manager.

*****************
Install & Upgrade
*****************

.. code-block:: console

    sudo pip3 install --upgrade --no-cache-dir bcg

**************
Usage examples
**************

Usually the ``bcg`` is run with ``pm2`` process manager. This direct command line command is more for testing purporses if the service does not run correctly.

Start

.. code-block:: console

    bcg --device /dev/ttyUSB0

Start with **debug**

.. code-block:: console

    bcg --device /dev/ttyUSB0 --debug

**********
bcg --help
**********

.. code-block:: console
    :linenos:

    $ bcg --help
    Usage: bcg [OPTIONS] COMMAND [ARGS]...

    HARDWARIO gateway between USB serial port and MQTT broker

    Options:
    -c, --config FILENAME  configuration file (YAML format).
    -d, --device TEXT      device
    -H, --mqtt-host TEXT   MQTT host to connect to (default is 127.0.0.1)
    -P, --mqtt-port TEXT   MQTT port to connect to (default is 1883)
    --no-wait              no wait on connect or reconnect serial port
    --mqtt-username TEXT   MQTT username
    --mqtt-password TEXT   MQTT password
    --mqtt-cafile TEXT     MQTT cafile
    --mqtt-certfile TEXT   MQTT certfile
    --mqtt-keyfile TEXT    MQTT keyfile
    -v, --verbosity LVL    Either CRITICAL, ERROR, WARNING, INFO or DEBUG
    -D, --debug            Print debug messages, same as --verbosity DEBUG.
    --version              Show the version and exit.
    --help                 Show this message and exit.

    Commands:
    devices  Print available devices.
    help     Show help.

**********
Udev rules
**********

If you would like permanent alias in ``/dev/``, then apply these rules.

For Radio Dongle
****************

.. code-block:: console

    echo 'SUBSYSTEMS=="usb", ACTION=="add", KERNEL=="ttyUSB*", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6015", ATTRS{serial}=="bc-usb-dongle*", SYMLINK+="bcUD%n", TAG+="systemd", ENV{SYSTEMD_ALIAS}="/dev/bcUD%n"'  | sudo tee --append /etc/udev/rules.d/58-hio-usb-dongle.rules

For Gateway with Core Module
****************************

.. code-block:: console

    echo 'SUBSYSTEMS=="usb", ACTION=="add", KERNEL=="ttyACM*", ATTRS{idVendor}=="0483", ATTRS{idProduct}=="5740", SYMLINK+="bcCM%n", TAG+="systemd", ENV{SYSTEMD_ALIAS}="/dev/bcCM%n"' | sudo tee --append /etc/udev/rules.d/59-hio-core-module.rules

************
Config files
************

In case you would like have configuration of ``bcg`` separate and not permanent in the ``pm2``, create a config file and pass the file with ``-c`` parameter to ``bcg``.

Step 1: Create folder for configuration file
********************************************

.. code-block:: console

    sudo mkdir -p /etc/hardwario

Step 2: Configuration file for Gateway Radio Dongle
***************************************************

**Open file**

.. code-block:: console

    sudo nano /etc/hardwario/bcg-ud.yml

**Insert this**

.. code-block:: console
    :linenos:

    device: /dev/bcUD0
    name: "usb-dongle"
    mqtt:
        host: localhost
        port: 1883

Step 3: Run service for Gateway Radio Dongle
********************************************

.. code-block:: console

    pm2 start /usr/bin/python3 --name "bcg-ud" -- /usr/local/bin/bcg -c /etc/hardwario/bcg-ud.yml

.. code-block:: console

    pm2 save

Configuration file for Gateway Core module
******************************************

**Open file**

.. code-block:: console

    sudo nano /etc/hardwario/bcg-cm.yml

**Insert this**

.. code-block:: console
    :linenos:

    device: /dev/bcCM0
    name: "core-module"
    mqtt:
        host: localhost
        port: 1883

Run service for Gateway Core module
***********************************

.. code-block:: console

    pm2 start /usr/bin/python3 --name "bcg-cm" -- /usr/local/bin/bcg -c /etc/hardwario/bcg-cm.yml

.. code-block:: console

    pm2 save

**Bash autocomplete for bcf**

.. code-block:: console

    register-python-argcomplete bcf >> ~/.bashrc

.. code-block:: console

    source ~/.bashrc

