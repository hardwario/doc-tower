##################
How to: PIR Module
##################

The PIR module is mostly used as motion detector. Thanks to its low power consumption it can safely be used with batteries acting as the only power source.

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__module__pir.html>`_

************
How It Works
************

Thanks to the SDK, setting up and using the PIR module is very simple.
You have to do only two things:

- initialize the PIR module and set its sensitivity
- program the event handler (what should happen when PIR senses movement)

Initialization is as simple as for other modules from HARDWARIO TOWER ecosystem.
You have to instantiate variable with type ``twr_module_pir_t`` which represents the PIR module for SDK.

Inside your *application_init* function comes the initialization and first setting of sensitivity (can be later changed in the code).

Example of initialization:

.. code-block:: c
    :linenos:

    #include <application.h>

    twr_module_pir_t pir;

    void application_init(void)
    {
        twr_module_pir_init(&pir);
        twr_module_pir_set_sensitivity(&pir, TWR_MODULE_PIR_SENSITIVITY_MEDIUM);
        twr_module_pir_set_event_handler(&pir, pir_event_handler, NULL);
    }

***********
Sensitivity
***********

SDK offers you four types of sensitivity defined as enum type, so you can use simple names:

- ``TWR_MODULE_PIR_SENSITIVITY_LOW``
- ``TWR_MODULE_PIR_SENSITIVITY_MEDIUM``
- ``TWR_MODULE_PIR_SENSITIVITY_HIGH``
- ``TWR_MODULE_PIR_SENSITIVITY_VERY_HIGH``

It is very hard to predict how exactly the PIR sensor will act in your particular use case,
it is always a good idea to test every type of sensitivity to find out which one to use for the best results.

******************************
Recognizable PIR Module Events
******************************

For now there are only two events - *error* and *motion* detection.

- ``TWR_MODULE_PIR_EVENT_ERROR`` - occurs when error was encountered
- ``TWR_MODULE_PIR_EVENT_MOTION`` - occurs when motion is detected

*******
Example
*******

This example uses **medium** sensitivity. When movement is detected, message ``Movement``! is sent to your computer.

.. code-block:: c
    :linenos:

    #include <application.h>

    twr_module_pir_t pir;
    twr_button_t button;

    void pir_event_handler(twr_module_pir_t *self, twr_module_pir_event_t event, void *event_param)
    {
        (void) self;
        (void) event_param;

        if (event == TWR_MODULE_PIR_EVENT_MOTION)
        {
            twr_log_debug("Movement detected!");
        }
    }

    void application_init(void)
    {
        twr_log_init(TWR_LOG_LEVEL_DEBUG, TWR_LOG_TIMESTAMP_ABS);

        twr_module_pir_init(&pir);
        twr_module_pir_set_sensitivity(&pir, TWR_MODULE_PIR_SENSITIVITY_MEDIUM);
        twr_module_pir_set_event_handler(&pir, pir_event_handler, NULL);
    }
