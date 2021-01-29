######################################
HARDWARIO TOWER Firmware Flashing Tool
######################################

This multi-platform Python tool can flash `Radio Dongle <https://shop.hardwario.com/radio-dongle/>`_
and `Core Module <https://shop.hardwario.com/core-module/>`_ with local binary or latest released firmwares from GitHub.

The installation and usage instructions are in the Quick Tutorial and Projects section.

*****************
Install & Upgrade
*****************

You can install tools with ``pip3`` python tool. Always make sure that you are using the latest version.

.. code-block:: console

    sudo pip3 install --upgrade --no-cache-dir bcf

Autocomplete
************

For Ubuntu/Linux you can enable autocomplete. Add this line to ``~/.bashrc``

.. code-block:: console

    eval "$(_BCF_COMPLETE=source bcf)"

Then run this command to reload .bashrc

.. code-block:: console

    source ~/.bashrc

Now you can for example write ``bcf --de``, press **TAB key** and ``--device`` text is automatically completed.

**************
Usage examples
**************

Update and dowload list of all firmwares from GitHub

.. code-block:: console

    bcf update

List all firmwares

.. code-block:: console

    bcf list

Search for firmware

.. code-block:: console

    bcf search button

Flash Core Module **R2**

.. code-block:: console

    bcf flash hardwario/bcf-radio-push-button:latest

.. tip::

    You can use optional ``--device`` parameter to choose the right serial port. This way the ``bcf`` won't ask you every time.

Flash Core Module R1

.. code-block:: console

    bcf flash --device dfu hardwario/bcf-radio-push-button:latest

Flash **Radio Dongle** with latest firmware

.. code-block:: console

    bcf flash --device /dev/ttyUSB0 hardwario/bcf-gateway-usb-dongle:latest

bcf logging
***********

It is possible to use ``bcf`` as a serial console to see log messages which are printed with ``twr_log_`` APIs.
It is using serial port in the parameter and 115200 baud speed with 8N1 uart format.

.. code-block:: console

    bcf log --device [device]

Flash firmware and immediatelly start logging after upload

.. code-block:: console

    bcf flash --device [device] [firmware]:[version] --log

Reset Core Module and immediatelly start logging after upload

.. code-block:: console

    bcf reset --device [device] --log

bcf --help
**********

.. code-block:: console
    :linenos:

    $ bcf --help
    Usage: bcf [OPTIONS] COMMAND [ARGS]...

    HARDWARIO Firmware Tool.

    Options:
    -d, --device TEXT  Device path.
    --version          Show the version and exit.
    --help             Show this message and exit.

    Commands:
    clean    Clean cache.
    create   Create new firmware.
    devices  Print available devices.
    eeprom   Work with EEPROM.
    flash    Flash firmware.
    help     Show help.
    list     List firmware.
    log      Show log.
    pull     Pull firmware to cache.
    read     Download firmware to file.
    reset    Reset core module.
    search   Search in firmware names and descriptions.
    source   Firmware source.
    test     Test firmware source.
    update   Update list of available firmware.

