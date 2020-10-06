###################
HARDWARIO Host Tool
###################

This multi-platform Python tool is a "Swiss knife" to control the radio and nodes.

*****************
Install & Upgrade
*****************

.. code-block:: console

    sudo pip3 install --upgrade --no-cache-dir bch

**************
Usage examples
**************

Subscribe to all MQTT topics (#)
********************************

.. code-block:: console

    bch sub

Subscribe to MQTT broker running on ``hub.local`` host
******************************************************

.. code-block:: console

    bch -H hub.local sub

Subscribe to specific topic
***************************

.. code-block:: console

    bch sub node/kitchen/#

Publish MQTT message on MQTT broker running localhost
*****************************************************

.. code-block:: console

    bch pub node/kitchen/thermometer/0:0/temperature 21.70

Start pairing mode
******************
.. code-block:: console
    :linenos:

    bch pairing --start
    bch -H hub.local pairing --start

Stop pairing mode
*****************

.. code-block:: console
    :linenos:

    bch pairing --stop
    bch -H hub.local pairing --stop

Rename node
***********

.. code-block:: console
    :linenos:

    bch node rename generic-node:0 kitchen
    bch node rename 836d19831c4a garden

List paired nodes
*****************
.. code-block:: console

    bch node list

Remove node. By name or ID
**************************
.. code-block:: console
    :linenos:

    bch node remove garden
    bch node remove 836d19831c4a

bch --help
**********
.. code-block:: console
    :linenos:

    Usage: bch [OPTIONS] COMMAND [ARGS]...

    Options:
    --gateway TEXT                 Gateway name [default: usb-dongle].
    -H, --mqtt-host TEXT           MQTT host to connect to [default: 127.0.0.1].
    -P, --mqtt-port INTEGER RANGE  MQTT port to connect to [default: 1883].
    --mqtt-username TEXT           MQTT username.
    --mqtt-password TEXT           MQTT password.
    --mqtt-cafile PATH             MQTT cafile.
    --mqtt-certfile PATH           MQTT certfile.
    --mqtt-keyfile PATH            MQTT keyfile.
    -v, --verbosity LVL            Either CRITICAL, ERROR, WARNING, INFO or
                                    DEBUG

    --version                      Show the version and exit.
    -h, --help                     Show this message and exit.

    Commands:
    gw       Gateway
    node
    pairing
    pub
    sub      Subscribe topic.
