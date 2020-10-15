#############
MQTT Protocol
#############

* MQTT is open, simple and low overhead communication protocol for sending messages between many clients which are connected to the central MQTT broker.
* Every **message** contains two parts - **topic** and **payload**.
* Topic describes the content of the message.
* Topic name contains "directory" structure - each level is divided with a symbol '/'.
* Topic can be ``bedroom/temperature`` or ``kitchen/light/set``.
* MQTT server is called the **broker** and clients can **publish** messages and **subscribe** to different topics.
* The task of the MQTT broker is to deliver messages from **publishers** to the **subscribers**.
* You can use the ``+`` symbol to subscribe to all topics in the current topic (``+/light/set``) and ``#`` symbol to subscribe to all sub-topics (``kitchen/#``).

.. caution::

    The symbol **#** can be used only at the end of the topic name.

.. tip::

    `More information about MQTT topics <https://www.hivemq.com/blog/mqtt-essentials-part-5-mqtt-topics-best-practices/>`_

*********************
Mosquitto MQTT broker
*********************
IoT Kit uses the open-source `Mosquitto <https://mosquitto.org>`_ MQTT broker. All messages are routed through the MQTT broker. This allows further expansion of IoT Kit system.
When you connect the Core Module or Radio Dongle with connected remote node, you can display all incoming messages using mosquitto-cli package by typing:

.. code-block:: console

    mosquitto_sub -t "#" -v

Response:

.. code-block:: console
    :linenos:

    pi@hub:~ $ mosquitto_sub -t "#" -v
    node/836d19821664/thermometer/0:1/temperature 24.69
    node/836d19821664/thermometer/0:1/temperature 24.94
    node/836d19821664/push-button/-/event-count 5

**************************************************
HARDWARIO Playground as GUI tool for MQTT messages
**************************************************
You can use `HARDWARIO Playground <https://www.hardwario.com/download/>`_ for subscribing and publishing MQTT messages. You can do it in Messages tab.

.. thumbnail:: ../_static/interfaces/mqtt-protocol/HARDWARIO-Playground/playground-messages-tab.png
   :width: 100%
   :alt: Playground Messages Tab

Subscribe
*********
Subscribe mode is default mode when you open Messages tab in Playground.
In beginning you have already subscribed ``node/#`` topic. We can try to send MQTT messages with payload ``test message`` and topic ``node/test`` by typing following command.

.. code-block:: console

    mosquitto_pub -t "node/test" -m "test message"

Now you can see test message in Playground message window.

.. thumbnail:: ../_static/interfaces/mqtt-protocol/HARDWARIO-Playground/playground-messages-tab-test-message.png
   :width: 100%
   :alt: Playground Messages Tab Test Message

Publish
*******
You can also publish message from Playground.
Just switch to Publish mode, type topic, payload and Publish your message.

.. note::

    If you are subscribed to correct topics you can see your published messages appear on top of the Messages Tab

.. thumbnail:: ../_static/interfaces/mqtt-protocol/HARDWARIO-Playground/playground-messages-tab-publish.png
   :width: 100%
   :alt: Playground Messages Tab Publish


