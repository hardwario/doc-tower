#####################
How to: Accelerometer
#####################

Core module comes with three-axis ultra-low-power linear accelerometer connected via :doc:`I2C bus <../../hardware/i-c-address-space>`.
It is capable of motion detection and a free-fall based on interrupts.

Basically you have **two options how to use the accelerometer - continuous measurement of acceleration or as an alarm**,
which triggers event handler if defined conditions occurs.

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__lis2dh12.html>`_

*********************************
Recognizable Accelerometer Events
*********************************

- TWR_LIS2DH12_EVENT_ERROR
- TWR_LIS2DH12_EVENT_UPDATE
- TWR_LIS2DH12_EVENT_ALARM

**********************
Continuous Measurement
**********************

This can be achieved by setting the update interval in your code with function ``twr_lis2dh12_set_update_interval``,
which takes pointer to instantiated accelerometer and time before measurements in milliseconds as parameters.

You also have to instantiate a struct ``twr_lis2dh12_result_g_t`` to store the results of measurements.
Those values can be retrieved by calling ``twr_lis2dh12_get_result_g`` function.
In the simple example below, we measure exact values of acceleration in g every second and send them over USB.

.. code-block:: c

    #include <application.h>

    twr_led_t led;

    twr_lis2dh12_t a;
    twr_lis2dh12_result_g_t a_result;

    void lis2_event_handler(twr_lis2dh12_t *self, twr_lis2dh12_event_t event, void *event_param)
    {
        (void) self;
        (void) event_param;

        if (event == TWR_LIS2DH12_EVENT_UPDATE) {
            twr_lis2dh12_get_result_g(&a, &a_result);
            twr_log_debug("X: %f\r\nY: %f\r\nZ: %f\r\n", a_result.x_axis, a_result.y_axis, a_result.z_axis);
        } else {
            twr_log_debug("error");
        }
    }

    void application_init(void)
    {
        twr_log_init(TWR_LOG_LEVEL_DEBUG, TWR_LOG_TIMESTAMP_OFF);

        twr_lis2dh12_init(&a, TWR_I2C_I2C0, 0x19);
        twr_lis2dh12_set_event_handler(&a, lis2_event_handler, NULL);
        twr_lis2dh12_set_update_interval(&a, 1000);
    }


*****
Alarm
*****

Alarm is a very interesting "feature".
This allows you to set up certain conditions when the "alarm" should be triggered
(like "wake up, when module is moved in direction of X-axis && acceleration is higher than 1g").
The module uses interrupts to inform the microcontroller,
which means that the microcontroller can sleep when it is not being moved and only be awaken when moved.

You can set conditions for the alarm in struct `twr_lis2dh12_alarm_t <https://sdk.hardwario.com/structtwr__lis2dh12__alarm__t.html>`_.

When the accelerometer checks these settings it uses logical AND operation (so every set condition needs to occur for the alarm to be triggered).

In the example below, we set the alarm to be triggered when core module is moved in direction of X-axis with acceleration > 1g. When triggered,
integrated red LED will switch on for one second.

After flashing, try to move your Core module very slowly. It will do nothing in any direction.
Then try to move it quickly up and down - once again nothing happens, because this movement is in Z-axis.
Now try to make a quick move in X-axis and the LED should light up.

.. code-block:: c
    :linenos:

    #include <application.h>

    twr_led_t led;

    twr_lis2dh12_t a;
    twr_lis2dh12_result_g_t a_result;

    // alarm settings
    twr_lis2dh12_alarm_t alarm1;

    twr_scheduler_task_id_t disable_led_task;

    void disable_led(void* params)
    {
        (void) params;
        twr_led_set_mode(&led, TWR_LED_MODE_OFF);
    }

    void lis2_event_handler(twr_lis2dh12_t *self, twr_lis2dh12_event_t event, void *event_param)
    {
        (void) self;
        (void) event_param;

        if (event == TWR_LIS2DH12_EVENT_ALARM) {
            twr_led_set_mode(&led, TWR_LED_MODE_ON);
            twr_scheduler_plan_from_now(disable_led_task, 1000);
        }
    }

    void application_init(void)
    {
        // here you can set conditions for the alarm to be triggered
        alarm1.x_high = true;
        alarm1.threshold = 1;

        twr_led_init(&led, TWR_GPIO_LED, false, false);
        twr_led_set_mode(&led, TWR_LED_MODE_OFF);

        twr_lis2dh12_init(&a, TWR_I2C_I2C0, 0x19);
        twr_lis2dh12_set_alarm(&a, &alarm1);
        twr_lis2dh12_set_event_handler(&a, lis2_event_handler, NULL);

        disable_led_task = twr_scheduler_register(disable_led, NULL, TWR_TICK_INFINITY);
    }

