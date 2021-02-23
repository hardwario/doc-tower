#########################
3 / 3 Put it all together
#########################

Now it's time to give your system a logic and connect it with desired platforms.

In next steps we will create a simple dashboard with a temperature gauge

Messages
********

Switch to the **Messages**, you should see incoming messages from the previous step.
Copy the **bold** text (called **topic**) that ends with *temperature* **to the clipboard**.

.. important::

    You can use the copy icon in each message. Make sure you copy just text and no space before or after the text.

Your **topic** could be different based on your kit name.
You can also copy any other topic that your module supports from the :doc:`MQTT topics list. <../../interfaces/mqtt-topics>`

.. thumbnail:: ../../_static/basics/quick-start-guide/playground-messages-topic.png
    :width: 100%

Function
********

Switch to the **Functions** tab and from the color blocks on the left side drag and drop **mqtt input** block and
**gauge** block to the **flow** in the middle of the screen. The color blocks are called **nodes**.
You can use the ``filter nodes`` text box to find the right block. Connect the two created nodes together.

.. thumbnail:: ../../_static/basics/quick-start-guide/playground-functions-tab.png
    :width: 100%


.. thumbnail:: ../../_static/basics/quick-start-guide/playground-functions-connected.png
    :width: 100%

You have to modify the mqtt node and add the broker. Double click on it and then click on the little pencil on the right.

.. thumbnail:: ../../_static/basics/quick-start-guide/playground-functions-mqtt-edit-server.png
    :width: 100%

After that you just have to type in the **localhost** or any of your MQTT broker addresses and then click **Add**. Finally click **Done**.

.. thumbnail:: ../../_static/basics/quick-start-guide/playground-functions-mqtt-edit-server-localhost.png
    :width: 100%

Double click on the **gauge** node. Change **Label**, **Units** and **Range** to your needs.
Then click **Done**.

Double click on the **mqtt node** and paste the previously copied topic from the clipboard.

.. caution::

    Make sure there are not any spaces before and after the copied text.

Then click **Done** and **Deploy** button.

.. note::

    You have to click on the **Deploy** everytime you make changes in your flow.

.. thumbnail:: ../../_static/basics/quick-start-guide/playground-functions-mqtt-node.png
    :width: 100%

Dashboard
*********

Go to Playground's **Dashboard** tab and you should see a gauge with the temperature of the selected device.

.. tip::

    The temperature can take a while to appear. You can breathe on the module or reconnect batteries for immediate update.

.. thumbnail:: ../../_static/basics/quick-start-guide/playground-dashboard.png
    :width: 100%

.. important::

    Now you should know the basics, you can also :ref:`Learn more <learn-more>`.
