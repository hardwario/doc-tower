####################
How to: Relay Module
####################

With our Relay module you can easily control high voltage/current circuits.
This module is specially designed to consume low levels of power. The relay also consumes power when changing state only.

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__module__relay.html>`_

*********************************
Initialization and Simple Control
*********************************

SDK provides simple functions to control your relay.
First you have to instantiate variable typed ``twr_module_relay_t`` which represents the relay and use the *relay init* function.

I2C address of the module is ``0x3B`` but you can use ``TWR_MODULE_RELAY_I2C_ADDRESS_DEFAULT`` macro for it.
It is also a good practice to tell the SDK about actual relay state.
Inside you application_init function you can do something like this to give it OFF state:

.. code-block:: c
    :linenos:

    twr_module_relay_init(&relay, TWR_MODULE_RELAY_I2C_ADDRESS_DEFAULT);
    twr_module_relay_set_state(&relay, false);

.. tip::

    You can actually use two Relay modules at once because there is another macro ``TWR_MODULE_RELAY_I2C_ADDRESS_ALTERNATE``.
    You will just have to move the 0 ohm rezistor to the another spot on the Relay module.

Manual toggle
*************

You can toggle the states manually. That is achieved by calling the ``twr_module_relay_toggle(twr_module_relay_t *self)``,
where the *self* parameter is an address to instantiated variable of type ``twr_module_relay_t``.

SDK holds the information about relay state internally, which means that on every call of this function it will switch the state.

Pulse Control
*************

More interesting is control with the ``twr_module_relay_pulse(twr_module_relay_t *self, bool direction, twr_tick_t duration)`` function.
When called, the relay will be switched to given state for time defined in its last parameter and then automatically switches back.

You can see this in the simple working example (after pressing the button, relay is switched to ON state for 1500 milliseconds and then back to OFF).

*******
Example
*******

.. code-block:: c
    :linenos:

    #include <application.h>

    twr_module_relay_t relay;
    twr_button_t button;

    void button_event_handler(twr_button_t *self, twr_button_event_t event, void *event_param)
    {
        (void) self;
        (void) event_param;

        if (event == TWR_BUTTON_EVENT_PRESS)
        {
            twr_module_relay_pulse(&relay, true, 1500);
        }
    }

    void application_init(void)
    {
        twr_module_relay_init(&relay, TWR_MODULE_RELAY_I2C_ADDRESS_DEFAULT);
        twr_module_relay_set_state(&relay, false);

        twr_button_init(&button, TWR_GPIO_BUTTON, TWR_GPIO_PULL_DOWN, false);
        twr_button_set_event_handler(&button, button_event_handler, NULL);
    }

