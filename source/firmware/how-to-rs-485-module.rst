#####################
How to: RS-485 Module
#####################

With RS-485 Module you can send and receive data over RS-485 line using generic byte transfer or other protocols like MODBUS.
See more information in :doc:`About RS-485 Module <../hardware/about-rs-485-module>` page.

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__module__rs485.html>`_

**************
Initialization
**************

.. code-block:: c
    :linenos:

    // Init RS-485 Module
    twr_module_rs485_init();
    twr_module_rs485_set_baudrate(TWR_MODULE_RS485_BAUDRATE_9600);

*********************
Reading input voltage
*********************

If you set update interval, then the RS-485 Module will measure input voltage of the DC/DC converter and report it to your callback

.. code-block:: c
    :linenos:

    void application_init(void)
    {
        // Initialize uart logging
        twr_log_init(TWR_LOG_LEVEL_DUMP, TWR_LOG_TIMESTAMP_ABS);
        ...
        twr_module_rs485_init();
        twr_module_rs485_set_update_interval(5000);
        twr_module_rs485_set_event_handler(module_rs485_event_handler, NULL);
        ...
    }

    void module_rs485_event_handler(twr_module_rs485_event_t event, void *param)
    {
        (void) param;

        if (event == TWR_MODULE_RS485_EVENT_VOLTAGE)
        {
            float voltage;
            twr_module_rs485_get_voltage(&voltage);
            twr_log_debug("%f", voltage);
        }
    }

**************
Synchronous TX
**************

These blocking functions send or receive data and the program is stopped until the data are send.

.. code-block:: c
    :linenos:

    // TX
    buffer[] = {0x01, 0x02, 0x03};
    twr_module_rs485_write(buffer, sizeof(buffer));

**************
Synchronous RX
**************

This application_task example checks if some data are present inside the I2C to UART converter's internal buffer.
If there are new data, you call read function to transfer them to the Core Module.
You can also define blocking timeout in ``twr_module_rs485_read`` function to wait some amount of time until some data arrive.

.. code-block:: c
    :linenos:

    void application_task(void)
    {
        size_t data_size;
        static uint8_t rx_buffer[32];

        twr_module_rs485_available(&data_size);
        twr_log_debug("Available RX: %d", data_size);

        if (data_size)
        {
            size_t b = twr_module_rs485_read(rx_buffer, sizeof(rx_buffer), 0);
            twr_log_dump(rx_buffer, b, "RX bytes %d", b);
        }

        twr_scheduler_plan_current_from_now(500);
    }

********************
Asynchronous RX & TX
********************

You need to define buffers and assign them to the FIFO structures. Then you can call async functions. The received can be read using callback.

.. code-block:: c
    :linenos:

    // Write and read FIFOs for RS-485 Module async tranfers
    twr_fifo_t write_fifo;
    twr_fifo_t read_fifo;
    uint8_t write_fifo_buffer[512];
    uint8_t read_fifo_buffer[512];

    // Button instance
    twr_button_t button;

    void button_event_handler(twr_button_t *self, twr_button_event_t event, void *event_param)
    {
        if (event == TWR_BUTTON_EVENT_PRESS)
        {
            uint8_t toggle_relay_0[] = {0x01, 0x06, 0x00, 0x01, 0x03, 0x00, 0xD8, 0xFA};
            twr_module_rs485_async_write(toggle_relay_0, sizeof(toggle_relay_0));
        }
    }

    void module_rs485_event_handler(twr_module_rs485_event_t event, void *param)
    {
        (void) param;

        if (event == TWR_MODULE_RS485_EVENT_VOLTAGE)
        {
            float voltage;
            twr_module_rs485_get_voltage(&voltage);
            twr_log_debug("%f", voltage);
        }

        if (event == TWR_MODULE_RS485_EVENT_ASYNC_WRITE_DONE)
        {
            twr_log_debug("Async write DONE");
        }

        if (event == TWR_MODULE_RS485_EVENT_ASYNC_READ_DATA)
        {
            twr_log_debug("Async read DATA");
            static uint8_t rx_buffer[32];
            size_t b = twr_module_rs485_async_read(rx_buffer, sizeof(rx_buffer));

            twr_log_dump(rx_buffer, b, "RX bytes %d", b);
        }

        if (event == TWR_MODULE_RS485_EVENT_ASYNC_READ_TIMEOUT)
        {
            // Async receive timeout event
        }
    }

    void application_init(void)
    {
        twr_system_deep_sleep_disable();

        // Initialize logging
        twr_log_init(TWR_LOG_LEVEL_DUMP, TWR_LOG_TIMESTAMP_ABS);

        // Initialize button
        twr_button_init(&button, TWR_GPIO_BUTTON, TWR_GPIO_PULL_DOWN, false);
        twr_button_set_event_handler(&button, button_event_handler, NULL);

        // Init FIFOs
        twr_fifo_init(&write_fifo, write_fifo_buffer, sizeof(write_fifo_buffer));
        twr_fifo_init(&read_fifo, read_fifo_buffer, sizeof(read_fifo_buffer));

        // Init RS-485 Module
        twr_module_rs485_init();
        twr_module_rs485_set_event_handler(module_rs485_event_handler, NULL);
        twr_module_rs485_set_update_interval(5000);
        twr_module_rs485_set_baudrate(TWR_MODULE_RS485_BAUDRATE_9600);
        twr_module_rs485_set_async_fifo(&write_fifo, &read_fifo);

        // Start async reading
        twr_module_rs485_async_read_start(10);
    }
