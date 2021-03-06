##################
How to: CO2 Module
##################

With CO2 Module you can easily measure the concentration of carbon dioxide.

It is low power device which can be used with battery power.
Remember that the device can require calibration and **to get best results it has to be in active state for few days**.

************
How It Works
************

Technically it uses infrared light for measurements. More information on `Wikipedia <https://en.wikipedia.org/wiki/Carbon_dioxide_sensor>`_

And how it works within the SDK? As any other TOWER module. There are init, periodical + manual measurements and calibration functions available in the SDK

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__module__co2.html>`_

******************************
Recognizable CO2 Module Events
******************************

For now there are just two events - *error* and *update*.

- TWR_MODULE_CO2_EVENT_ERROR
- TWR_MODULE_CO2_EVENT_UPDATE

*****
Usage
*****

You can measure the CO2 level manually or periodically. Every measure can trigger function within event handler.

To set periodic measurements, just use this function in your ``application_init``: ``twr_module_co2_set_update_interval(twr_tick_t interval)``.
interval is time between measurements, in milliseconds.

To make a manual measurement, just use ``twr_module_co2_measure(void)``.

To get CO2 concentration from last measurement you have to use this function: ``twr_module_co2_get_concentration_ppm(float *ppm)``.

*******
Example
*******

In this example, CO2 levels will be measured and sent to computer every time button is pressed.

.. code-block:: c
    :linenos:

    #include <application.h>

    twr_button_t button;

    void button_event_handler(twr_button_t *self, twr_button_event_t event, void *event_param)
    {
        (void) self;
        (void) event_param;

        float ppm = 0.0;

        if (event == TWR_BUTTON_EVENT_PRESS)
        {
            twr_module_co2_measure();
            twr_module_co2_get_concentration_ppm(&ppm);

            twr_log_debug("CO2 level: %.4fppm", ppm);
        }
    }

    void application_init(void)
    {
        twr_log_init(TWR_LOG_LEVEL_DEBUG, TWR_LOG_TIMESTAMP_ABS);

        twr_module_co2_init();

        twr_button_init(&button, TWR_GPIO_BUTTON, TWR_GPIO_PULL_DOWN, false);
        twr_button_set_event_handler(&button, button_event_handler, NULL);
    }


