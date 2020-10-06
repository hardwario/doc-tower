############################
How to: Soil Moisture Sensor
############################

Soil Moisture sensor measures moisture and temperature. See also :doc:`About Soil Moisture Sensor <../hardware/about-soil-moisture-sensor>` article.

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__bc__soil__sensor.html>`_

*********************************************
Reading a single sensor values to the console
*********************************************

This is the simplest example with single connected sensor to the Sensor Module.

.. code-block:: c
    :linenos:

    #include <application.h>

    // Soil sensor instance
    bc_soil_sensor_t soil_sensor;

    void soil_sensor_event_handler(bc_soil_sensor_t *self, uint64_t device_address, bc_soil_sensor_event_t event, void *event_param)
    {
        if (event == BC_SOIL_SENSOR_EVENT_UPDATE)
        {
            uint16_t moisture;
            float temperature;

            bc_soil_sensor_get_cap_raw(self, device_address, &moisture);
            bc_soil_sensor_get_temperature_celsius(self, device_address, &temperature);
            bc_log_debug("Moisture: %d\tTemperature %.2f", moisture, temperature);
        }
    }

    void application_init(void)
    {
        bc_log_init(BC_LOG_LEVEL_DUMP, BC_LOG_TIMESTAMP_ABS);

        // Initialize soil sensor
        bc_soil_sensor_init(&soil_sensor);
        bc_soil_sensor_set_event_handler(&soil_sensor, soil_sensor_event_handler, NULL);
        bc_soil_sensor_set_update_interval(&soil_sensor, 1000);
    }

When you run ``bcf flash --log`` then the firmware is flashed and you immediatelly see the log output:

.. code-block:: console

    112.47 <D> Moisture: 7250 Temperature 34.44

**************************
Multiple connected sensors
**************************

When you connect multiple sensors, you need to initialize them with ``bc_soil_sensor_init_multiple``.
In the event handler you then get the ``device_address`` in the callback parameter, or you can get sensor index by calling ``bc_soil_sensor_get_index_by_device_address()``.

.. code-block:: c
    :linenos:

    #define MAX_SOIL_SENSORS                    5

    // Sensors array
    bc_soil_sensor_sensor_t sensors[MAX_SOIL_SENSORS];

    void soil_sensor_event_handler(bc_soil_sensor_t *self, uint64_t device_address, bc_soil_sensor_event_t event, void *event_param)
    {
        ...
        if (event == BC_SOIL_SENSOR_EVENT_UPDATE)
        {
            int index = bc_soil_sensor_get_index_by_device_address(self, device_address);
        ...
    }

    void application_init(void)
    {
        ...

        // Initialize soil sensors
        bc_soil_sensor_init_multiple(&soil_sensor, sensors, MAX_SOIL_SENSORS);
        bc_soil_sensor_set_event_handler(&soil_sensor, soil_sensor_event_handler, NULL);
        bc_soil_sensor_set_update_interval(&soil_sensor, SENSOR_UPDATE_SERVICE_INTERVAL);

        ...
    }
