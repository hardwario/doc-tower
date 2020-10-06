#################
Azure IoT Central
#################

This guide will help you to publish data from HARDWARIO sensors to Microsoft IoT Central and IoT Hub.
This guide is based on this `Azure and Node-RED official article <https://azure.microsoft.com/es-es/blog/connecting-node-red-to-azure-iot-central/>`_.

In `this official Azure documentation section <https://docs.microsoft.com/cs-cz/azure/iot-central/>`_ you can find how to connect to IoT Central over C#, Python, Node.js.


**************************
Create new Device Template
**************************

Create a new `Application and Device Template in IoT Central <https://docs.microsoft.com/cs-cz/azure/iot-central/core/>`_.
You can name your device push-button:0 so it corresponds with devices' MQTT topic alias.

In the Measurements tab add these telemetry items:

- battery
- push-button
- orientation
- thermometer

We suggest to use **exactly these names**, because in Node-RED the MQTT topics will directly transform into these names.

**************************************
Create new device in Azure IoT Central
**************************************

In the Devices tab `add a new device <https://docs.microsoft.com/en-us/azure/iot-central/tutorial-add-device#add-a-real-device>`_. Copy down the:

#. Device ID
#. Device Key (Primary Key)
#. Scope ID

****************************
Connection string generation
****************************

Install nodejs tool to generate connection string. Detailed information can be found in official Azure IoT Central documentation.

You can also download compiled binaries for your platform of the DPS tool.

