######################
How to: Battery Module
######################

Battery Module and Mini Battery Module allows you to power your product with four or two AAA batteries.
It automatically recognizes if external power is applied (AC module, USB, ...) and disconnects batteries from the circuit.

With this module you can check battery voltage (manually or periodically with Scheduler) and schedule appropriate actions for certain voltage levels.

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__module__battery.html>`_

*****************
How Does it Work?
*****************

This module uses high efficiency `buck converter <https://en.wikipedia.org/wiki/Buck_converter>`_ which provides 3.1 V output voltage.
Voltage level is measured on the analog input.

SDK provides functions to:

- Manually and periodically (with Scheduler) trigger battery voltage measurement
- Get exact battery voltage (*float* value)
- Get voltage charge level (percentage, int value)
- Create event handler
- Define voltage threshold levels

********************
Battery Module Types
********************

There are two types of modules - `Standard <https://developers.hardwario.com/hardware/about-battery-module>`_
and `Mini <https://developers.hardwario.com/hardware/about-mini-battery-module>`_.

The type of the connected module is detected automatically. In your ``application_init()`` function you have to init the module by calling:

.. code-block:: c

    twr_module_battery_init();

**********************************
Recognizable Battery Module Events
**********************************

- ``TWR_MODULE_BATTERY_EVENT_LEVEL_LOW`` - battery crossed "low voltage threshold"
- ``TWR_MODULE_BATTERY_EVENT_LEVEL_CRITICAL`` - battery crossed "critical voltage threshold"
- ``TWR_MODULE_BATTERY_EVENT_UPDATE`` - voltage measurement happened

*****
Usage
*****

Because SDK can inform your application about *low* and *critical* level, you can easily modify it, so it will adapt to the "insufficient power" mode.

Let's say you are building a battery powered climate/weather station with Sigfox connectivity.
You know that it won't be possible to change batteries immediately when they will be "soon dead".
For that, you can use the **low voltage trigger**. Program your app to send warning message that will alert you about the need to change batteries.
The interval for sending climate data report over Sigfox can also be made higher to prolong battery life.

And when the voltage level goes critical (critical voltage trigger), just send warning message that batteries are almost dead and disable other transmissions.

You can set `your own threshold levels <https://sdk.hardwario.com/group__twr__module__battery.html#gae316b29ba7391e57703b4e0e01a69f9f>`_,
so with a bit of research, you can know that when "critical level warning occurs at x.y voltage,
there is enough power to make m Sigfox transmissions".

************************
Voltage over USB example
************************

In this example, voltage and charge levels will be sent to your computer over USB every time you press a button.

.. code-block:: c
    :linenos:

    #include <application.h>

    twr_button_t button;

    void button_event_handler(twr_button_t *self, twr_button_event_t event, void *event_param)
    {
        (void) self;
        (void) event_param;

        if (event == TWR_BUTTON_EVENT_PRESS)
        {
            twr_module_battery_measure();

            float voltage = 0.0;
            twr_module_battery_get_voltage(&voltage);

            int chargePercentage = -1;
            twr_module_battery_get_charge_level(&chargePercentage);

            twr_log_debug("Voltage %.3f", voltage);
            twr_log_debug("Charge: %d", chargePercentage);
        }
    }

    void application_init(void)
    {
        twr_log_init(TWR_LOG_LEVEL_DEBUG, TWR_LOG_TIMESTAMP_ABS);

        twr_button_init(&button, TWR_GPIO_BUTTON, TWR_GPIO_PULL_DOWN, false);
        twr_button_set_event_handler(&button, button_event_handler, NULL);

        twr_module_battery_init();
    }


**********************
Voltage on LCD example
**********************

For this example, we are going to use LCD module to show voltage level.
Place code below in application.c file and flash. Use of application.h file is not required here.
Values on your LCD panel will be updated every time you press any of LCD's buttons.

.. code-block:: c
    :linenos:

    #include <application.h>

    void application_init(void)
    {
        twr_module_battery_init();
        twr_module_lcd_init();
    }

    void application_task()
    {
        twr_module_battery_measure();

        twr_module_lcd_clear();
        twr_module_lcd_set_font(&twr_font_ubuntu_15);

        float voltage = 0.0;
        twr_module_battery_get_voltage(&voltage);
        static char volt[25];
        sprintf(volt, "Voltage: %.3f", voltage);

        int charge_percentage = -1;
        twr_module_battery_get_charge_level(&charge_percentage);
        static char charge[25];
        sprintf(charge, "Charge: %d%c", charge_percentage, 37);

        static char format[50];
        static const char* battery_format_text[] = {"unknown", "standard", "mini"};
        sprintf(format, "Format: %s", battery_format_text[twr_module_battery_get_format()]);

        twr_module_lcd_draw_string(10, 5, volt, true);
        twr_module_lcd_draw_string(10, 25, charge, true);
        twr_module_lcd_draw_string(10, 45, format, true);

        twr_module_lcd_update();

        twr_scheduler_plan_current_relative(500);
    }
