=============================
Connect to The Things Network
=============================

This guide provides step-by-step instructions for connecting Hardwario LoRa
devices to The Things Network (TTN). It covers the installation of a LoRaWAN
gateway, configuration of a Hardwario LoRa device for TTN, connecting the device
to TTN, and uploading a payload formatter to TTN.

.. note::

    This guide applies to all firmware in the HARDWARIO Playground with the
    prefix ``twr-lora``. The examples are based on TTN console v3.16.0. The
    guide was originally written in November 2021 and uses the AT command
    interface and TTN console available at that time.

Background
==========

The Things Network
------------------

`The Things Network (TTN) <https://www.thethingsnetwork.org>`_ is a global
community-maintained LoRaWAN network. TTN infrastructure is operated by
volunteers. The network is open, i.e., anybody can connect new LoRa devices to
the network via existing gateways. At the highest level, the network is
organized into separate geographical clusters: Europe, North America, Australia.
Gateways and devices are associated with a particular cluster based on their
location. The gateways within each cluster are organized into communities. A
community is a group of volunteers in a specific region, e.g., city or country,
who operate LoRa gateways.

Hardwario LoRa Module
---------------------

The Hardwario `LoRa module <https://shop.hardwario.com/lora-module/>`_ is
compatible with TTN. Thus, you can connect your Hardwario device to TTN and
access its measurements through any of the APIs and protocols supported by the
network, including (but not limited to) HTTP push (webhooks), MQTT, AWS IoT,
Azure IoT. If your LoRa devices are installed in an area that is already covered
by an existing TTN gateway, all you need to do is register your LoRa device to
TTN. If your area is not covered, consider purchasing a small LoRa gateway to
install yourself. There are several affordable and easy to install LoRa gateways
on the market such as `The Things Indoor LoRaWAN Wi-Fi Gateway
<https://www.adafruit.com/product/4345>`_.

Install LoRa Gateway for TTN
============================

.. note::

    If you have no TTN gateway nearby, you may need to install your own. The
    process is quick and easy. This section provides a step-by-step guide to
    connecting `The Things Indoor LoRaWAN Wi-Fi Gateway
    <https://www.adafruit.com/product/4345>`_ to TTN. For more detailed
    instructions please refer to `the official documentation
    <https://www.thethingsindustries.com/docs/gateways/thethingsindoorgateway/>`_.


Locate the sticker (with a QR code) on the back of the gateway. Write down the
12-character alphanumeric string (gateway ID). Convert the ID to a gateway EUI
by inserting the string FFFE between the 6th and 7th character. For example, if
your gateway ID is 58A0CB801AD9, your gateway EUI will be 58A0CB\ **FFFE**\
801AD9.

Write down the Wi-Fi password printed on the same sticker. It will be needed
later.

Optionally, reset the gateway to factory defaults. Press and hold the reset
button at the bottom of the gateway for 5 seconds, or until the LED starts
rapidly blinking red-green.

Press and hold the setup button at the top of the gateway for 10 seconds, or
until the LED starts blinking red. The gateway creates a temporary Wi-Fi network
called ​​MiniHub-XXXXXX, where XXXXXX is the last 6 characters of the gateway ID
recorded earlier. Connect to the temporary Wi-Fi network using the Wi-Fi
password noted earlier.

Once connected, navigate in your browser to `http://192.168.4.1
<http://192.168.4.1>`_. The browser should load the gateway’s setup page. Select
the name of your Wi-Fi network from the list of scanned Wi-Fi networks by
clicking on the + button on the line:

.. thumbnail:: ../_static/tutorials/connect-to-ttn/ttig-wifi-setup.png
   :width: 90%

When prompted, enter the password for the Wi-Fi network. Click the button "Save
& Reboot". The gateway will blink green until it successfully connects to the
configured Wi-Fi network. Once the LED turns solid green, the gateway is
connected to Wi-Fi and to TTN.

Login to the `TTN console <https://console.cloud.thethings.network>`_ and select
a cluster from the left hand side menu. On the next screen, click on "Go to
gateways".  On the next screen, click on the button "Claim gateway". You will be
presented with the following form:

.. thumbnail:: ../_static/tutorials/connect-to-ttn/claim-gateway.png
   :width: 75%

If not auto-filled, enter your TTN account username into the field "Collaborator
ID". Enter the gateway EUI created earlier into the field "Gateway EUI". Enter
the Wi-Fi password from the sticker on the gateway into the field "Claim
authentication code". Set a unique name for the gateway in "Gateway ID" and
select the appropriate frequency plan for your region in the dropdown "Frequency
plan". Click on the button "Claim gateway" to complete the process. You should
be then redirected to the overview page for the gateway.

Connect Hardwario LoRa Device to TTN
====================================

Connecting a Hardwario LoRa device to TTN consists of the following steps:

#. Create a TTN application (optional if you already have one)
#. Configure Hardwario LoRa device for TTN
#. Register the device in TTN
#. Execute the OTAA join operation on the device
#. Upload a payload formatter to TTN (optional)

TTN-related steps are performed in the web-based `TTN console
<https://console.cloud.thethings.network>`_. LoRa device configuration is
performed via the `AT command interface
<https://tower.hardwario.com/en/latest/tutorials/lora-at-commands-configuration/>`_
provided by the Hardwario Core module over its USB-serial interface.

Create TTN Application
----------------------

.. tip::

    You can skip this section if you already have a TTN application.

A TTN application is a logical group of related LoRa devices and associated
data, e.g., configuration, payload formaters, keys, and stored data.

Log in to the `TTN console <https://console.cloud.thethings.network>`_, select
the appropriate cluster from the left hand side menu, and click on "Go to
applications". Click on the button "Add application" to create a new
application. Fill out the form with application name and unique application ID
and then click on the button "Create application". You will be redirected to the
overview page for the newly created application that looks like this:

.. thumbnail:: ../_static/tutorials/connect-to-ttn/application-overview.png
   :width: 90%

Configure Hardwario LoRa Device for TTN
---------------------------------------

Make sure you have a recent firmware with LoRa module support loaded in the
device. If not, follow the instructions on the `Hardwario developer website
<https://tower.hardwario.com/en/latest/>`_ to load the right firmware into the
device.

Connect to Device
~~~~~~~~~~~~~~~~~

Connect the Hardwario device to your computer with a USB cable. We need to find
out the filename assigned to the device’s serial interface by the Linux kernel.
There are several ways to do this. If you have the Hardwario `firmware flashing
tool
<https://tower.hardwario.com/en/latest/tools/hardwario-firmware-flashing-tool/>`_
installed, run ``bcf devices -v`` to see a list of all connected devices:

.. code-block:: console

    bcf devices -v
    /dev/ttyUSB0
        desc: USB-3003 - USB-3003
        hwid: USB VID:PID=0403:6001 SER=DVAPPPU0 LOCATION=1-1
    /dev/ttyUSB1
        desc: (none) - (none)
        hwid: USB VID:PID=0403:6015 SER=2416968042 LOCATION=1-4

Select the filename corresponding to your device’s serial number (SER=). In the
above example, there is one Hardwario Core module with serial number 2416968042
and its filename is ``/dev/ttyUSB1``.

Next, use `picocom <https://linux.die.net/man/8/picocom>`_, `minicom
<https://salsa.debian.org/minicom-team/minicom>`_, `screen
<https://www.gnu.org/software/screen/>`_ or similar terminal emulator to connect
to the device. Serial port configuration is 115200 8N1 (one start bit, eight
bits, no parity). The Core module uses ``CRFL`` (\\r\\n) as the end-of-line
delimiter. With picocom you can use the the following command line parameters:

.. code-block:: console

    picocom -b 115200 --omap crcrlf --echo /dev/ttyUSB1

In the following sections, we will be using the AT command interface supported
by all Hardwario ``twr-lora`` firmware. If you are unfamiliar with AT commands,
please read the `guide to LoRa AT commands
<https://tower.hardwario.com/en/latest/tutorials/lora-at-commands-configuration/>`_
first.

Reset to Factory Defaults
~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

    This step is optional but highly recommended. Pre-existing LoRa module
    settings and state are a suprisingly common source of problems during device
    activation.

The Hardwario LoRa module has persistent internal memory that is used to store
modem settings. If you are unsure what state your LoRa module is in, e.g.,
whether it has any previous saved settings or configuration, consider resetting
the module to factory defaults.

To reset the LoRa module, send the AT command ``AT$FRESET``. This command will
reset the LoRa module to factory defaults. Once the module has responded with
"OK", reboot the Core module by sending ``AT$REBOOT``:

.. code-block::

    AT$FRESET
    OK
    AT$REBOOT

Configure LoRa Modem
~~~~~~~~~~~~~~~~~~~~

Configure the Hardwario LoRa module for TTN. First, select the right frequency
band based on your region:

.. code-block::

    AT$BAND=8

The value 8 represents the U.S. 915 MHz band. Note: You can use the command
``AT$HELP`` to see the full list of supported values:

.. code-block::

    ...
    AT$BAND 0:AS923, 1:AU915, 5:EU868, 6:KR920, 7:IN865, 8:US915
    ...

TTN is a public network, so we need to configure the LoRa module to connect to a
public network:

.. code-block::

    AT$NWK=1

Finally, we need to select the activation method. LoRaWAN supports two
activation methods: Over the Air Activation (OTAA) and Activation by
Personalization (ABP). The OTAA method is more convenient and generally
recommended. If you are reading this guide, OTAA is what you probably want to
use. Send the following command to activate the OTAA mode:

.. code-block::

    AT$MODE=1

.. note::

    ``AT$BAND`` and ``AT$NWK`` settings are persistent and only need to be
    configured once after the device has been reset to factory defaults. The
    ``AT$MODE`` setting is temporary and will be reset to 0 (ABP) on device
    reboot. Thus, you should issue ``AT$MODE=1`` before every ``AT$JOIN``
    (discussed below).

Register Hardwario LoRa Device in TTN
-------------------------------------

First, use the AT command interface to obtain a few values from the Hardwario
LoRa module that will be needed to register the device in TTN:

.. code-block::

    AT$DEVEUI?
    $DEVEUI: 3632313691398608
    OK

    AT$APPEUI?
    $APPEUI: 0101010101010101
    OK

    AT$APPKEY?
    $APPKEY: B2E7511628AED2A6ABF7158809CF4F3C
    OK

Note the three values. DevEUI is the unique identifier (address) of your device.
AppEUI (also known as JoinEUI) is a string that identifies the join server
during OTAA activation. AppKey is the root AES-128 secret key unique to the
device. This key will be used to derive various session keys during the OTAA
process.

Switch to the TTN console. Navigate to the overview screen for your newly
created TTN application. Select "End devices" from the left hand side menu.
Click the button "Add end device". You will be redirected to the following
screen:

.. thumbnail:: ../_static/tutorials/connect-to-ttn/register-device.png
   :width: 90%


The Hardwario LoRa module is not included in the TTN LoRaWAN device repository.
Thus, we need to register the device manually. Select the tab "Manually":

.. thumbnail:: ../_static/tutorials/connect-to-ttn/register-device-manually.png
   :width: 90%

In the dropdown "Frequency plan" select the appropriate frequency plan for your
region. Most likely, this will be one of the plans marked with "(used by TTN)".
The frequency plan must match the frequency plan that you configured in the
Hardwario LoRa module with the command ``AT$BAND``.

In the dropdown "LoRaWAN version" select "MAC V1.0.2".
Select "PHY v1.0.2 REV B" in the dropdown "Regional Parameters version".
This is the most recent MAC version supported by the Hardwario LoRa module. 

Paste the DevEUI, AppEUI, and AppKey values obtained through the AT command
interface earlier into the corresponding form fields. The completely filled out
form should look like this:

.. thumbnail:: ../_static/tutorials/connect-to-ttn/register-device-manually-filled.png
   :width: 90%

Click on "Register end device" to complete the registration process.

Execute OTAA Join
-----------------

Now that your LoRa module is properly configured and registered in TTN, you can
execute the OTAA join operation. During the join, the LoRa module needs to be
able to communicate with a LoRa gateway, so make sure it has an antenna
connected and it is located in a place with a good LoRa signal from the gateway.
Send ``AT$JOIN`` to the device to initiate the join:

.. code-block::

    AT$JOIN
    OK

The device responds with an "OK" which indicates that the command was accepted
and the operation is in progress. After a while, you should receive either
"$JOIN_OK" or "$JOIN_ERROR" in the terminal. The former indicates that your
device has successfully joined TTN and is ready to communicate. The latter
indicates that the join failed and needs to be repeated. The culprit is commonly
incorrect LoRa module settings, e.g., mismatched DevEUI, AppEui, or AppKey. If
your joins fail repeatedly, try resetting the LoRa modem to factory defaults,
reboot the device, and follow the configuration steps mentioned earlier.

Upload Payload Formatter
------------------------

LoRa devices generally send data (sensor measurements) encoded in binary form to
keep messages short and to save air time. Without knowing how the data from a
particular device is encoded, TTN would have to submit the data in the original
binary format to HTTP webhooks or MQTT clients. Internally, TTN must also encode
binary data in Base64 to be able to pass it around in JSON messages. Dealing
with such binary data is inconvenient and places extra burden on application
developers. For that reason, TTN provides a feature called payload formatters
which allows TTN to decode arbitrary binary data into a JSON value more suitable
for HTTP webhooks or MQTT.

Whenever TTN receives a LoRa message from a device, it checks whether a payload
formatter function exists either for the device, or for the TTN application the
device is part of. If a payload formatter exists, TTN passes the binary data to
the formatter function. The return value of the function, usually in the form of
a JSON object, is then provided to applications over HTTP webhooks or MQTT. For
example, a payload formatter could convert the value ``ASAA+Q==`` to the
following JSON object:

.. code-block:: javascript

    {
        "header": 1,
        "temperature": 24.9,
        "voltage": 3.2
    }

A payload formatter function can be defined for a particular LoRa device, or for
the entire TTN application. Application payload formatters are applied to all
devices within the application. Device-specific payload formatters take
precedence over application payload formatters.

To define a new application payload formatter, navigate to the overview screen
for your TTN application. Select "Payload formatters" and "Uplink" in the left
hand side menu. In the dropdown "Formatter type" select "JavaScript". The TTN
console will present you with a JavaScript formatter template that looks as
follows:

.. thumbnail:: ../_static/tutorials/connect-to-ttn/payload-formatter.png
   :width: 90%

Whenever a LoRa device within the application sends a message to TTN, the
function decodeUplink will be invoked with the LoRa message in the parameter
input. The property bytes contains the binary payload generated by the device,
for example, the state of various sensors. The formatter function converts the
binary payload into a JavaScript object and the object is returned in the
property data.

For firmware created by Hardwario, you can often find a default payload
formatter implementation in the Github repository for the firmware. For example,
a payload formatter for the firmware ``twr-lora-climate-monitor`` can be found
`here
<https://github.com/hardwario/twr-lora-climate-monitor/blob/master/ttn.js>`_.

Copy the payload formatter JavaScript program and paste it at the beginning of
the "Formatter parameter" field shown above. Then invoke the function Decoder
with ``input.bytes`` as an argument and assign the returned value to the
property data. The whole JavaScript program should look like this:

.. code-block:: javascript

    function Decoder(bytes, port) {
        // Decode an uplink message from a buffer
        var header = bytes[0];
        var voltage = bytes[1] / 10.0;
        var orientation = bytes[2];
        var temperature = ((bytes[3] << 8) | bytes[4]) / 10.0;
        var humidity = bytes[5] / 2;
        var illuminance = ((bytes[6] << 8) | bytes[7]);
        var pressure = ((bytes[8] << 8) | bytes[9]) * 2.0;

        // (array) of bytes to an object of fields.
        var decoded = {
            header: header,
            voltage: voltage,
            orientation: orientation,
            temperature: temperature,
            humidity: humidity,
            illuminance: illuminance,
            pressure: pressure

        };

        return decoded;
    }

    function decodeUplink(input) {
        return {
            data: Decoder(input.bytes),
            warnings: [],
            errors: []
        };
    }

In LoRa, message payload is encrypted with the application session key
(AppSKey). To apply the payload formatter, the TTN network must have access to
AppSKey. This is generally the case with LoRa devices added with the OTAA method
where AppSKey is generated by the network server.

For devices added via the ABP method that is not necessarily the case. To use
payload formatters with ABP devices, you need to configure the AppSKey into TTN
manually if you wish to use the feature. Otherwise, your HTTP or MQTT endpoints
will be given encrypted message payload and you need to decrypt and parse the
data yourself.
