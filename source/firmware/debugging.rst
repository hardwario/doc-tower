#########
Debugging
#########

.. attention::
    We are migrating to our own **Visual Studio Code extension** and a portable version of Visual Studio Code. For more information on how to install and use it visit
    :doc:`HARDWARIO Code Installation <hardwario-code-installation>`.

***************
Starting simple
***************

The easiest way to debug and also the way how all the things started was just print out whatever you consider important to know.

Wait the embedded system does not have any screen or printer connected.

Well you are right, but there used to be a serial port.
And if it is hopefully free to use and can be connected to real PC then you have your first **poor man's debugger**.

.. tip::
    This chapter is about debugging with the log messages.
    If you are interested in advanced debugging with JLink, you can visit the :doc:`Advanced Debugging chapter <advanced-debugging>`.

***********
Core Module
***********

.. note::
    If you have older version of Core Module you can visit :doc:`another chapter to see how to connect it with UART <../troubleshooting/core-module-r1-debugging>`.

Core Module have integrated FTDI chip connected to the UART2.
You do not need to use separate serial converter, just connect USB cable to your computer.

************
Example code
************

You need to add just two function calls into your application:

- ``twr_log_init`` into ``application_init``
- ``twr_log_debug``, ``twr_log_info``, ``twr_log_warning``, ``twr_log_error`` of ``twr_log_dump`` into handlers

.. tip::

    Have a look into `HARDWARIO TOWER SDK twr_log <https://sdk.hardwario.com/group__twr__log.html>`_ for more detailed info.

Example of modified ``src/application.c`` from default project ``twr-skeleton`` `available at GitHub <https://github.com/hardwario/twr-skeleton>`_:

.. code-block:: c
    :linenos:

    #include <application.h>

    // LED instance
    twr_led_t led;

    // Button instance
    twr_button_t button;

    void button_event_handler(twr_button_t *self, twr_button_event_t event, void *event_param)
    {
        (void) self;
        (void) event_param;

        if (event == TWR_BUTTON_EVENT_PRESS)
        {
            twr_led_set_mode(&led, TWR_LED_MODE_TOGGLE);
        }
        // Logging in action
        twr_log_info("Button event handler - event: %i", event);
    }

    void application_init(void)
    {
        // Initialize logging
        twr_log_init(TWR_LOG_LEVEL_DUMP, TWR_LOG_TIMESTAMP_ABS);

        // Initialize LED
        twr_led_init(&led, TWR_GPIO_LED, false, false);
        twr_led_set_mode(&led, TWR_LED_MODE_ON);

        // Initialize button
        twr_button_init(&button, TWR_GPIO_BUTTON, TWR_GPIO_PULL_DOWN, false);
        twr_button_set_event_handler(&button, button_event_handler, NULL);
    }

After flashing of Core Module execute terminal emulator, open serial port with USB UART and set communication parameters:

- speed: 115 200 baud
- 8 bits, no parity (8N)

Example of output:

.. code-block:: c
    :linenos:

        # 4.54 <I> Button event handler - event: 0
        # 4.84 <I> Button event handler - event: 1
        # 4.84 <I> Button event handler - event: 2
        # 10.24 <I> Button event handler - event: 0
        # 12.24 <I> Button event handler - event: 3
        # 13.64 <I> Button event handler - event: 1

For mapping number to event type have a look into `HARDWARIO SDK documentation for twr_button <https://sdk.hardwario.com/twr__button_8h_source.html#l00013>`_

************
Colored logs
************

You can colorized logs to 4 different colors as following commands down below.

**Debug (purple)**

.. code-block:: console

    twr_log_debug("Log");

.. thumbnail:: ../_static/firmware/debugging/debugColoredLog.png
    :width: 10%

**Info (green)**

.. code-block:: console

    twr_log_info("Log");

.. thumbnail:: ../_static/firmware/debugging/infoColoredLog.png
    :width: 10%

**Warning (orange)**

.. code-block:: console

    twr_log_warning("Log");

.. thumbnail:: ../_static/firmware/debugging/warningColoredLog.png
    :width: 10%

**Error (red)**

.. code-block:: console

    twr_log_error("Log");

.. thumbnail:: ../_static/firmware/debugging/errorColoredLog.png
    :width: 10%

.. _debug-hardwario-code:

*****************************
Read logs with HARDWARIO Code
*****************************

.. important::
    If you didn't already, you should :doc:`install HARDWARIO Code extension <hardwario-code-installation>`

You can use our Visual Studio Code extension to attach console to the connected Core Module.

You can use two commands in the extension to attach console:

#. :ref:`Build + Flash (Console) <build-flash-console>`
#. :ref:`Attach console <attach-console>`.

It is advised to use the first one. It will build the firmware so it includes all the changes that you did and flash it to the device.
After the flashing is done the console will be attached and you can see all the logs.

If you just want to attach the console to the running Core Module without building and flashing, you can use the **Attach console** command.

Either way you should see the log messages in the console at the bottom of the Visual Studio Code.

.. tip::
    To learn more about this console you can visit :doc:`HARDWARIO Console chapter<hardwario-console>`.

.. thumbnail:: ../_static/firmware/debugging/debuggingHardwarioCode.png
    :width: 100%

.. tip::

    You can check those links for more information:

    - `Tips and Tricks for Microcontroller Programming and Debugging <https://www.youtube.com/watch?v=cDaG1CdP5Ew>`_
    - `Poor Man’s Trace <https://mcuoneclipse.com/2015/04/04/poor-mans-trace-free-of-charge-function-entryexit-trace-with-gnu-tools/>`_
    - `The Lauterbach Company <https://www.lauterbach.com/frames.html?home.html>`_
