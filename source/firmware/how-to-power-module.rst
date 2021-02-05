####################
How to: Power Module
####################

`Power module <https://shop.hardwario.com/power-module/>`_ provides two features - you can control high power device with robust relay (230 V / 16 A) and you can also connect
5V addressable LEDs (WS2812B) and control them.

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__module__power.html>`_

*************
Relay Control
*************

Controlling the relay is very simple. First you have to initialize the power module in your *application_init* function by calling ``twr_module_power_init()``.
It is always good to set an initial state immediately after the initialization, like ``twr_module_power_relay_set_state(false)``.

When the relay is switched on, you will see a small green LED light on the Power module.

You can set the relay state anywhere in your code by calling ``twr_module_power_relay_set_state(bool state)``.
The SDK holds an actual state internally, you can always retrieve it by calling ``twr_module_power_relay_get_state()``.
So if you are going to switch relay state, you don't have to create any variable,
just use this function within function: ``twr_module_power_relay_set_state(!twr_module_power_relay_get_state())``

In the example below we set the relay to off state after initialization. To switch the state, just use the button.

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
            twr_module_power_relay_set_state(!twr_module_power_relay_get_state());
        }
    }

    void application_init(void)
    {
        twr_module_power_init();
        twr_module_power_relay_set_state(false);

        twr_button_init(&button, TWR_GPIO_BUTTON, TWR_GPIO_PULL_DOWN, false);
        twr_button_set_event_handler(&button, button_event_handler, NULL);
    }

***********************
LED / LED Strip Control
***********************

We have :doc:`separate tutorial <how-to-smart-led-strip>` on how to control our LED strip.


