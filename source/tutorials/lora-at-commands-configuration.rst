##############################
LoRa AT Commands Configuration
##############################

This document describes how to configure HARDWARIO TOWER LoRa devices over USB virtual serial port and AT commands.

This document does not explain project-specific firmware commands and functions. They are explained in the project itself.

.. note::

    This guide applies to all firmware in the HARDWARIO Playground with the prefix ``twr-lora``

******************
LoRa Configuration
******************

For configuration you can use ``AT`` commands over a USB virtual serial port. Use your serial
terminal application (`Hterm <http://der-hammer.info/pages/terminal.html>`_, putty, minicom).

- Baudrate 115200
- 8 data bits, 1 stop bit, no parity
- End of line sequence is ``CR+LF`` (both transmit and receive)

*****
HTerm
*****

You can download `Hterm <http://der-hammer.info/pages/terminal.html>`_ for Windows and Linux.
It also supports macros and sequences in the left panel for most used commands.
Type the command and press **ENTER**. Not the ASend button.

.. thumbnail:: ../_static/tutorials/lora-at-commands-configuration/hterm.png
   :width: 75%


*******
Picocom
*******

If you use picocom, start the program with the following parameters

.. code-block:: console

    picocom -b 115200 --omap crcrlf --echo /dev/ttyUSB0

To exit the program press ``CTRL+A`` followed by ``CTRL+Q``.

*****
Putty
*****

The configuration option "Implicit LF every CR" in Putty only works with received data.
To send ``CR+LF`` to the device, press ``CTRL+J`` followed by Enter.

***********
AT Commands
***********

To list all possible commands use ``AT$HELP``. You will get:

.. code-block:: console
    :linenos:

    AT$DEVEUI
    AT$DEVADDR
    AT$NWKSKEY
    AT$APPSKEY
    AT$APPKEY
    AT$APPEUI
    AT$BAND 0:AS923, 1:AU915, 5:EU868, 6:KR920, 7:IN865, 8:US915
    AT$MODE 0:ABP, 1:OTAA
    AT$NWK Network type 0:private, 1:public (TTN, your own)
    AT$JOIN Send OTAA Join packet
    AT$SEND Immediately send packet
    AT$STATUS Show status
    AT$BLINK LED blink 3 times
    AT$LED LED on/off
    AT+CLAC
    AT$HELP This help

To read the value, append a question mark at the end of the AT command:

.. code-block:: console

    AT$APPSKEY?

You receive the key:

.. code-block:: console

    $APPSKEY: BF22C15EB89237A65DAABB05B2C91EB4

Use the following syntax to update the value:

.. code-block:: console

    AT$APPSKEY=BF22C15EB89237A65DAABB05B2C91EB4

.. tip::

    You can use `online key generators <https://www.loratools.nl/#/keys>`_ for testing purposes

******************************
OTAA - Over-the-Air Activation
******************************

OTAA means that the session keys (the ones with **S** in the name) are generated in the LoRa network during **JOIN**.
The keys are then automatically transferred to your LoRa Module.
If your LoRa network does not support the OTAA activation method, read the **ABP** section below.
If you are not sure which activation type to use, start with ``OTAA``.

For the OTAA activation method, the LoRa network needs to know the ``DevEUI`` of your LoRa Module.
You can read the value with the command ``AT$DEVEUI?``:

.. code-block:: console

    $DEVEUI: 009335FF931FEADC

.. code-block:: console

    OK

The network also needs to know the ``APPKEY`` and ``APPEUI`` values.
You can either read the values from your LoRa Module and transfer them into your LoRa network, or you can let the LoRa
network generate new values for you to set in your module, for example:

.. code-block:: console
    :linenos:

    AT$APPEUI=324502A5676BADD7
    OK
    AT$APPKEY=44D4A5DA7A9507F036C5A2750211F052
    OK

Each time you get an ``OK``, the value has been saved in the LoRa Module's internal flash memory.

.. tip::

    Some LoRa networks also support generating ``DEVEUI`` but we do not recommend changing this value.

Finally, switch the modem into ``OTAA`` mode and send a ``JOIN`` command to exchange the session keys.
Make sure your modem has good signal because it needs bidirectional communication with the gateway to complete the join.

Enter:

.. code-block:: console
    :linenos:

    AT$MODE=1  // Set OTAA(1)
    OK
    AT$NWK=1   // Public(1) or private(0) network config (TTN is public)
    OK    
    AT$JOIN
    OK
    $JOIN_OK

Note that the ``OK`` response to ``JOIN`` command does not mean that the join was sucessful.
Wait for a few seconds to get either ``$JOIN_OK`` (join was successful) or ``$JOIN_ERROR`` (join failed).
If the join was successful, the LoRa Module is ready to communicate.

***********************************
ABP - Activation by Personalization
***********************************

ABP means that you set up session keys manually. ``AT$MODE`` has to be set to ``0`` (ABP), which is the default setting after a LoRa Module power reset.

If you use the **ABP** mode, you need to set the ``APPSKEY`` and ``NWKSKEY`` values manually via the corresponding AT commands.
For example:

.. code-block:: console
    :linenos:

    AT$APPSKEY=5505CA3E4620843B324502A5676BADD7
    OK
    AT$NWKSKEY=44D4A5DA7A9507F036C5A2750211F050
    OK

Each time you get an ``OK``, the value has been saved in the LoRa Module's internal flash memory.

Also, the LoRa network will need to know the ``DEVEUI`` and ``DEVADDR`` values from your LoRa Module.
Use the commands ``AT$DEVEUI?`` and ``AT$DEVADDR?` to read the values, for example:

.. code-block:: console
    :linenos:

    $DEVEUI: 009335FF931FEADC
    OK
    $DEVADDR: 26012C39
    OK

****************
Read Sensor Values
****************

You can use the command ``AT$STATUS`` to obtain the curent values from all available sensors.
This command only prints the values to the terminal.
It does not send anything through the LoRa network.

.. code-block:: console
    :linenos:

    AT$STATUS
    $STATUS: "Voltage",3.2
    $STATUS: "Temperature",23.0
    $STATUS: "Orientation",1
    OK

****************
Send Data
****************

To send sensor values to the LoRa network immediately, send the ``AT$SEND`` command to your module:

.. code-block:: console
    :linenos:

    AT$SEND
    OK
