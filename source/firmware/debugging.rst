#########
Debugging
#########

***************
Starting simple
***************

The easiest way to debug and also the way how all the things started was just print out whatever you consider important to know.

Wait the embedded system does not have any screen or printer connected.

Well you are right, but there used to be a serial port.
And if it is hopefully free to use and can be connected to real PC then you have your first **poor man's debugger**.

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

*************************
Read logs with PlatformIO
*************************

If you want to easily read the logs from the device, you dont have to install any additional program.
You should read the :doc:`PlatformIO installation <platformio-installation>` to know how to install PlatformIO.

After you installed the PlatformIO you can use it for reading the logs from the device.

There are two ways to do it:

* PlatformIO IDE

    .. thumbnail:: ../_static/firmware/debugging/platformioIDE-serial-monitor.png
* PlatformIO Core CLI

    * ``pio device monitor`` in your favourite terminal if you have Platformio Core (CLI) installed

.. thumbnail:: ../_static/firmware/debugging/output-example.png

.. caution::

    The serial monitor button does not **build** nor **flash** the firmware into the device so keep that in mind.

.. ************
.. Colored logs
.. ************
..
.. You can colorized your log output to highlight errors or warnings as you can see below:
..
..
.. As you did debugging in previous chapter by command
..
.. .. code-block:: console
..
..     twr_log_info("Log");
..
.. You can colorized logs to 4 different colors as following commands down below. All colors you can see on screenshot in the beginning of this chapter.
..
.. **Debug (purple)**
..
.. .. code-block:: console
..
..     twr_log_debug("Log");
..
.. **Info (green)**
..
.. .. code-block:: console
..
..     twr_log_info("Log");
..
.. **Warning (orange)**
..
.. .. code-block:: console
..
..     twr_log_warning("Log");
..
.. **Error (red)**
..
.. .. code-block:: console
..
..     twr_log_error("Log");

.. tip::

    You can check those links for more information:

    - `Tips and Tricks for Microcontroller Programming and Debugging <https://www.youtube.com/watch?v=cDaG1CdP5Ew>`_
    - `Poor Man’s Trace <https://mcuoneclipse.com/2015/04/04/poor-mans-trace-free-of-charge-function-entryexit-trace-with-gnu-tools/>`_
    - `The Lauterbach Company <https://www.lauterbach.com/frames.html?home.html>`_
