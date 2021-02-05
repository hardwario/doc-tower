##########################
How to: Temperature Sensor
##########################

Core module comes with integrated temperature sensor TMP112. It is high accuracy and low power sensor connected via I2C bus (see :doc:`address space <../hardware/i-c-address-space>`).
If you want to take a look how TMP112 is connected, please take a look at `schematic <https://github.com/hardwario/bc-hardware/tree/master/out/bc-module-core>`_.

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__tmp112.html>`_

*****************
How Does it Work?
*****************

- TMP112 is instantiated
- when measurement happens, event handler can be triggered
- last measured temperature can be retrieved anytime
- SDK provides functions to get temperature in:
    - raw format (``int16_t``)
    - Celsius degrees (``float``)
    - Fahrenheit degrees (``float``)
    - kelvin (``float``)

Types of Measurements
*********************

**Manual**

We can make manual measurement whenever we want to. This is achieved by calling the ``twr_tmp112_measure(twr_tmp112_t *self)`` function from SDK.

**With Scheduler, repeatedly**

Thanks to the :doc:`Scheduler <timing-and-scheduler>` you can define, when the periodic measurement should happen.
For this, we have the ``twr_tmp112_set_update_interval(twr_tmp112_t *self, twr_tick_t interval)`` function.

- ``*self`` is an address to an TMP112 instance
- ``interval`` is number of milliseconds, defining time between measurements

Recognizable TMP112 Events
**************************

- ``TWR_TMP112_EVENT_ERROR``
    - an error occurred during a measurement
- ``TWR_TMP112_EVENT_UPDATE``
    - a measurement was completed successfully

*******
Example
*******

In this example we make measurement every 5 seconds and send data over USB in format:

.. code-block:: console
    :linenos:

    12.3456 °C
    123

Place code below in *application.c* file and flash.

.. warning::

    Please note that in this particular example, the microcontroller never goes to sleep,
    even though the Scheduler is properly used for measurements - this is caused by USB communication running all the time.
    This cause the chip to heat up a bit which may affect temperature measurements. Therefore using Temperature tag is recommended for these situations.

.. code-block:: c
    :linenos:

    #include <application.h>

    twr_tmp112_t temp;

    void tmp112_event_handler(twr_tmp112_t *self, twr_tmp112_event_t event, void *event_param)
    {
        (void) self;
        (void) event_param;

        if (event == TWR_TMP112_EVENT_UPDATE)
        {
            float temperature = 0.0;
            int16_t rawTemperature = 0;
            twr_tmp112_get_temperature_celsius(&temp, &temperature);
            twr_tmp112_get_temperature_raw(&temp, &rawTemperature);
            twr_log_debug("%.4f °C\r\n%d", temperature, rawTemperature);
        }
    }

    void application_init(void)
    {
        // initialize logging
        twr_log_init(TWR_LOG_LEVEL_DEBUG, TWR_LOG_TIMESTAMP_ABS);

        // initialize TMP112 sensor
        twr_tmp112_init(&temp, TWR_I2C_I2C0, 0x49);

        // set measurement handler (call "tmp112_event_handler()" after measurement)
        twr_tmp112_set_event_handler(&temp, tmp112_event_handler, NULL);

        // automatically measure the temperature every 5 seconds
        twr_tmp112_set_update_interval(&temp, 5000);
    }

