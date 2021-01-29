###################
How to: Push Button
###################

You can control your device in many ways - you can add switches, sensors, Wi-Fi connection, etc.
But the most simple way is to use button(s) integrated in Core module.

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__button.html>`_

************
Requirements
************

- `Core Module <https://shop.hardwario.com/core-module/>`_
- USB cable
- Example code

******************
Integrated Buttons
******************

Core module comes with two buttons - Reset and Boot. You can take a look at schematics.
Reset (R) button is used for resetting the Core module - which is de facto equal to unplugging and replugging the power/USB cable.
Boot (B) button can be used as you wish.

This tutorial shows how to work with integrated button, but it can be used for your own buttons or switches.

**************************
Recognizable Button Events
**************************

*TWR_BUTTON_EVENT_PRESS* and *TWR_BUTTON_EVENT_RELEASE* are pretty straightforward - the first one stands for pressing the button and the second one for releasing the button.

*TWR_BUTTON_EVENT_CLICK* event is recognized, when button is **pressed and held** for period of time **shorter than defined**
(can be defined by `twr_button_set_click_timeout <https://sdk.hardwario.com/group__twr__button.html#ga88fd3c911e2feb4f5ea8e1eb511ad8e5>`_)

*TWR_BUTTON_EVENT_HOLD* event is recognized, when button is **pressed and held** for period of time **longer than defined** (can be defined by twr_button_set_hold_timeout)

*******
Example
*******

First, an instance of button is needed. You can achieve this by adding this line: ``twr_button_t button;``

Button is initiated by function ``twr_button_init``

- ``*self`` is an address to the instantiated button
- ``gpio_channel`` is GPIO channel number - defined as enum, more in SDK
- ``gpio_pull`` stands for GPIO pull up/down settings
- ``idle_state`` - state of a GPIO pin, when button is not pressed

In our example, we call init function this way:

.. code-block:: c

    twr_button_init(&button, TWR_GPIO_BUTTON, TWR_GPIO_PULL_DOWN, 0);


Then we need to define *event handler* - what function to call when something happens with the button.

.. code-block:: c

    twr_button_set_event_handler(&button, button_event_handler, NULL);

In other words: *when button is triggered, call function called 'button_event_handler' with no additional parameters*

In the *button_event_handler* function we mainly compare the *event*
parameter with callback events defined in `twr_button_event_t <https://sdk.hardwario.com/group__twr__button.html#ga6584b74ad24dd2ca8048fd72c73426fa>`_.

In this example we will use *_HOLD* and *_PRESS* events for better understanding. Programmed Core module will work by these rules:

- when button is **held for 1.5 seconds** (or more), LED starts to blink fast
- when button is **pressed** (simple short press), LED goes off

To set the 1.5 second interval we can use *twr_button_set_hold_time* function (inside *application_init()*) ``twr_button_set_hold_time(&button, 1500);``

Everything else is defined in the *button_event_handler* function.

.. code-block:: c
    :linenos:

        void button_event_handler(twr_button_t *self, twr_button_event_t event, void *event_param)
        {
            (void) self;
            (void) event_param;

            if (event == TWR_BUTTON_EVENT_PRESS)
            {
                twr_led_set_mode(&led, TWR_LED_MODE_OFF);
            }

            else if (event == TWR_BUTTON_EVENT_HOLD )
            {
                twr_led_set_mode(&led,  TWR_LED_MODE_BLINK_FAST);
            }
        }


Full *ready-to-flash* code for this example can be found on `Github <https://github.com/hardwario/twr-sdk/tree/master/_examples/button>`_.

