#################
How to: GPIO Pins
#################

You can use many GPIOs (General Purpose Input/Output pins) to connect the Core Module with the outside world.
The pins are described in the :doc:`Header Pinout <../../hardware/header-pinout>`. The pins in SDK has names ``TWR_GPIO_P0`` to ``TWR_GPIO_P17``.
There are also two special pins dedicated to ``TWR_GPIO_LED`` and ``TWR_GPIO_BUTTON``.

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__gpio.html>`_

******************
GPIO Configuration
******************

First important task is to enable clock to the GPIO peripheral by calling ``twr_gpio_init``.
ARM Cortex micros have **clock gating** which disables the peripheral clock and saves more power.
Then you need to configure the pin mode by calling ``twr_gpio_set_mode``.
The Mode can be input, output, analog, open-drain or alternate mode which is used when configuring UART or SPI peripheral.
Then it is possible to configure `internal **pull-up** or **pull-down** resistor <https://www.electronics-tutorials.ws/logic/pull-up-resistor.html>`_ by calling ``twr_gpio_set_pull`` so can define the default logic
level when there's nothing connected to the GPIO pin.

**************
GPIO as output
**************

This example will turn on the LED on the Core Module.
The usual and more comfortable way to control LED is to use ``twr_led`` code,
but we use the ``twr_gpio`` for now to explain the GPIO basics.

.. code-block:: c
    :linenos:

    #include <application.h>

    void application_init(void)
    {
        twr_gpio_init(TWR_GPIO_LED);
        twr_gpio_set_mode(TWR_GPIO_LED, TWR_GPIO_MODE_OUTPUT);
        twr_gpio_set_output(TWR_GPIO_LED, 1);
    }

*************
GPIO as Input
*************

This example will read the button state and then the value will be written to the LED.

.. code-block:: c
    :linenos:

    #include <application.h>

    void application_init(void)
    {
        twr_gpio_init(TWR_GPIO_LED);
        twr_gpio_set_mode(TWR_GPIO_LED, TWR_GPIO_MODE_OUTPUT);

        twr_gpio_init(TWR_GPIO_BUTTON);
        twr_gpio_set_mode(TWR_GPIO_BUTTON, TWR_GPIO_MODE_INPUT);

        // The Core Module has hardware pull-down so next call is commented out
        // twr_gpio_set_pull(TWR_GPIO_BUTTON, TWR_GPIO_PULL_DOWN);
    }

    void application_task()
    {
        uint8_t button_state = twr_gpio_get_input(TWR_GPIO_BUTTON);
        twr_gpio_set_output(TWR_GPIO_LED, button_state);

        // Repeat this task again after 10 ms
        twr_scheduler_plan_current_relative(10);
    }
