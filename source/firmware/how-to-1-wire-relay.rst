####################
How to: 1-Wire Relay
####################

To make it easier to work with certain 1-Wire devices we implemented module called ``twr_onewire_relay`` which allows you to control
relay modules connected via 1-Wire bus, for example the Relay module developed by Denkovi.

************
Requirements
************

For this tutorial you will need:

- `Core Module <https://shop.hardwario.com/core-module/>`_
- `Sensor Module <https://shop.hardwario.com/sensor-module/>`_
- `Relay Module controlled over 1-Wire bus <https://shop.hardwario.com/1-wire-8-channel-relay-module-with-din-rail-box/>`_

***
SDK
***

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__onewire__relay.html>`_

There is very simple workflow for controlling the relay:

- you have to instantiate a variable representing the relay ``twr_onewire_relay_t relay``;
- relay connection has to be initiated in *application_init()* function by calling ``twr_onewire_relay_init(&relay, TWR_GPIO_P4, 0x00)``;
    - the second parameter represents ports **A** and **B** on the Sensor module. Use _P4 for A and _P5 for B.
    - the third parameter represents number of connected device represented as *uint64_t* value
- now you only have to use the ``twr_onewire_relay_set_state()`` function to set desired state of every relay

*******
Example
*******

In this example we allow the relays to be controlled with button integrated to Core module.
On every press of the button one more relay will be activated. When all relays are active,
the next push of button will switch off all of them and the cycle repeats.

.. code-block:: c
    :linenos:

    #include <application.h>

    twr_onewire_relay_t relay;
    twr_button_t button;

    twr_onewire_relay_channel_t relays[] = {
            TWR_ONEWIRE_RELAY_CHANNEL_Q1,
            TWR_ONEWIRE_RELAY_CHANNEL_Q2,
            TWR_ONEWIRE_RELAY_CHANNEL_Q3,
            TWR_ONEWIRE_RELAY_CHANNEL_Q4,
            TWR_ONEWIRE_RELAY_CHANNEL_Q5,
            TWR_ONEWIRE_RELAY_CHANNEL_Q6,
            TWR_ONEWIRE_RELAY_CHANNEL_Q7,
            TWR_ONEWIRE_RELAY_CHANNEL_Q8
    };

    int activated = 0;

    void button_event_handler(twr_button_t *self, twr_button_event_t event, void *event_param)
    {
        (void) self;
        (void) event_param;

        if (event == TWR_BUTTON_EVENT_PRESS)
        {
            if (activated == 8) {
                for (int i = 0; i < 8; ++i) {
                    twr_onewire_relay_set_state(&relay, relays[i], false);
                }

                activated = 0;
            } else {
                twr_onewire_relay_set_state(&relay, relays[activated], true);
                activated++;
            }
        }
    }

    void application_init(void)
    {
        twr_onewire_relay_init(&relay, TWR_GPIO_P4, 0x00);

        twr_button_init(&button, TWR_GPIO_BUTTON, TWR_GPIO_PULL_DOWN, 0);
        twr_button_set_event_handler(&button, button_event_handler, NULL);
    }


.. tip::

    You can get a complete example in our `GitHub repository <https://github.com/hardwario/twr-sdk/tree/master/_examples/onewire-relay>`_
