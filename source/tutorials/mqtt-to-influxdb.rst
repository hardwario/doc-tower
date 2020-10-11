################
MQTT to InfluxDB
################

For storing data from our sensors we like to use ``InfluxDB`` - time-series database.
As a bridge between MQTT and InfluxDB we created a ``mqtt2influxdb``.
Service connects to InfluxDB and MQTT broker and by users config subscribe MQTT topics and store data from messages.

************
Installation
************

Step 1: Install the MQTT to InfluxDB service
********************************************

.. code-block:: console

    sudo pip3 install --upgrade mqtt2influxdb

Step 2: Create the ``/etc/hardwario`` directory
***********************************************

.. code-block:: console

    sudo mkdir /etc/hardwario

Step 3: Open the configuration file
***********************************

.. tip::

    For text editing, we use **nano** editor. You can save changes by pressing key combination ``Ctrl + O`` and exit editor by pressing ``Ctrl + X``.

.. code-block:: console

    sudo nano /etc/hardwario/mqtt2influxdb.yml

.. _step-four:

Step 4: Paste this snippet to the configuration file
****************************************************

.. code-block:: console
    :linenos:

mqtt:
    host: 127.0.0.1
    port: 1883

influxdb:
    host: 127.0.0.1
    port: 8086
    database: node

points:
    - measurement: temperature
        topic: node/+/thermometer/+/temperature
        fields:

            value: $.payload

        tags:
            id: $.topic[1]
            channel: $.topic[3]

    - measurement: relative-humidity
        topic: node/+/hygrometer/0:4/relative-humidity
        fields:

            value: $.payload

        tags:
            id: $.topic[1]

    - measurement: illuminance
        topic: node/+/lux-meter/0:0/illuminance
        fields:

            value: $.payload

        tags:
            id: $.topic[1]

    - measurement: pressure
        topic: node/+/barometer/0:0/pressure
        fields:

            value: $.payload

        tags:
            id: $.topic[1]

    - measurement: co2
        topic: node/+/co2-meter/-/concentration
        fields:

            value: $.payload

        tags:
            id: $.topic[1]

    - measurement: voltage
        topic: node/+/battery/+/voltage
        fields:

            value: $.payload

        tags:
            id: $.topic[1]

    - measurement: button
        topic: node/+/push-button/+/event-count
        fields:

            value: $.payload

        tags:
            id: $.topic[1]
            channel: $.topic[3]

.. note::

    In the section tags you can use identifiers, e.g.: ``tags: room: bedroom``

Step 5: Configuration file test
*******************************

.. code-block:: console

    mqtt2influxdb -c /etc/hardwario/mqtt2influxdb.yml --test

Step 6: Start the MQTT to InfluxDB service
******************************************

.. code-block:: console

    pm2 start `which python3` --name "mqtt2influxdb" -- `which mqtt2influxdb` -c /etc/hardwario/mqtt2influxdb.yml

Step 7: Save the PM2 state (so it will start after reboot)
**********************************************************

.. code-block:: console

    pm2 save

.. tip::

    If you want to see temperature records from the database in CSV format, use this command:

    ``influx -database node -execute "select * from temperature;" -format csv``

    Then you must restart the service when you change the configuration file

    ``pm2 restart mqtt2influxdb``

.. _configure-mqtt2influxdb:

**********************************************
Configuration file structure and possibilities
**********************************************

In :ref:`Step 4 <step-four>` we paste the configuration file, here will be described possibilities in the configuration.
In configuration you can use `JSONPath <https://goessner.net/articles/JsonPath/>`_.
For example in measurement you can identify tag id from MQTT topic by syntax $.topic[1] as you can see in :ref:`Step 4 <step-four>`.

MQTT
****

MQTT part of the configuration file is where you define a connection to MQTT broker. ``mqtt2influxdb`` supports secured connection! This section is **required**.

.. code-block:: console
    :linenos:

    mqtt:
        host: MQTT Broker adress (required)
        port: MQTT Broker port (required)
        username: Username to secured MQTT broker (optional)
        password: Users password to secured MQTT broker (optional)
        cafile: CA to secured MQTT broker (optional)
        certfile: Certificate to secured MQTT broker (optional)
        keyfile: Certificate Key file to secured MQTT broker (optional)

HTTP
****

You can define web hooks so data can be posted to your endpoint. This section is **optional**.

.. code-block:: console
    :linenos:

    http:
        destination: Endpoint url (required)
        action: Request type (required)
        username: Username for secured request (optional)
        password: Password for secured request (optional)

InfluxDB
********

An important part of the config is of course the definition of InfluxDB connection. This section is **required**.

.. code-block:: console
    :linenos:

    influxdb:
        host: InfluxDB adress (required)
        port: InfluxDB port (required)
        database: Database name (required)
        username: Username to InfluxDB (optional)
        password: Users password to InfluxDB (optional)
        ssl: SSL connection (optional)

Base64 Decode
*************

Decode base64 messages. This section is **optional**.

.. code-block:: console
    :linenos:

    base64decode:
        source: base64 coded message (required)
        target: encoded message (required)

Points
******

Points section is where you define messages you want to store in database. This section is **required**.

.. code-block:: console
    :linenos:

    points:
        measurement: Measurement name in database (required)
        topic: Define MQTT topic where messages are posting to (required)
        httpcontent: Define payload in http request if filled in HTTP chapter (optional)
    fields:
        value: Value field in InfluxDB (required)
        type: Variable type (required)

Tags
====

Tags are for identification measurement in database. This section is **optional**.

.. code-block:: console
    :linenos:

    tags:
        id: ID field in InfluxDB (optional)

Database
========

For every measurement you can define specific database name. This field is **optional**.

.. code-block:: console

    database: Specific database to store measurement (optional)

