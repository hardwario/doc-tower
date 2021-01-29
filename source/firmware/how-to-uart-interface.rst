######################
How to: UART Interface
######################

Core Module has 3 UARTs you can use. The signal for each channel is named TXD**x**, RXD**x** where **x** is **0**, **1** or **2**.
Please refer to the :doc:`module drawing pinout <../hardware/header-pinout>` where you find the signals positions.

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__uart.html>`_

.. note::

    **Multi-platform serial terminal**

    For UART testing you can try `H-term terminal <http://der-hammer.info/pages/terminal.html>`_.
    This is free multi-platform software which has plenty of configuration, tools and support for macros.

************************
Initialization and write
************************

First you have to set up the UART channel, baud rate and frame format. Then you can send the data.
The transmission can be synchronous which blocks the code until all the data are send,
or asynchronous where you don't wait for transmission and you can get a callback event ``TWR_UART_EVENT_ASYNC_WRITE_DONE`` informing, that the data were sent.


Synchronous write example
*************************

Function ``twr_uart_write`` needs to know how many bytes to send. That's why you need to use ``sizeof(uart_tx)``.

.. code-block:: c
    :linenos:


    void application_init()
    {
        twr_uart_init(TWR_UART_UART1, TWR_UART_BAUDRATE_115200, TWR_UART_SETTING_8N1);
        char uart_tx[] = "Hello world\r\n";
        twr_uart_write(TWR_UART_UART1, uart_tx, strlen(uart_tx));
    }


Asynchronous write example
**************************

This is a little bit complicated because you need to create FIFO structure and FIFO buffer array.
Then you initialize the FIFO and assign the FIFO to the UART. In this example we demonstrate just the async TX

.. code-block:: c
    :linenos:

    twr_fifo_t tx_fifo;
    uint8_t tx_fifo_buffer[32];

    void uart_handler(twr_uart_channel_t channel, twr_uart_event_t event, void *param)
    {
        if (event == TWR_UART_EVENT_ASYNC_WRITE_DONE)
        {
            // here you can for example send more data
        }
    }

    void application_init()
    {
        twr_uart_init(TWR_UART_UART1, TWR_UART_BAUDRATE_115200, TWR_UART_SETTING_8N1);
        twr_uart_set_event_handler(TWR_UART_UART1, uart_handler, NULL);

        twr_fifo_init(&tx_fifo, tx_fifo_buffer, sizeof(tx_fifo_buffer));
        // We set only TX FIFO, for RX_FIFO we pass NULL
        twr_uart_set_async_fifo(TWR_UART_UART1, &tx_fifo, NULL);

        char uart_tx[] = "Hello world\r\n";
        twr_uart_async_write(TWR_UART_UART1, uart_tx, strlen(uart_tx));
    }

*********************
Reading received data
*********************

There are again two options to read received bytes. You can read data synchronously in your task, or asynchronously using callbacks.

Synchronous reading
*******************

We use read function

``size_t twr_uart_read(twr_uart_channel_t channel, void *buffer, size_t length, twr_tick_t timeout);``

**Code example**

.. code-block:: c
    :linenos:

    void application_task()
    {
        // Define receive buffer
        uint8_t uart_rx[32];
        // Synchronous reading
        size_t number_of_rx_bytes = twr_uart_read(TWR_UART_UART1, uart_rx, sizeof(uart_rx), 500);

        char uart_tx[32];
        snprintf(uart_tx, sizeof(uart_tx), "RX bytes: %d\r\n", number_of_rx_bytes);
        twr_uart_write(TWR_UART_UART1, uart_tx, strlen(uart_tx));

        twr_scheduler_plan_current_now();
    }

Note that the last parameter ``timeout`` is ``500`` so the function is waiting 500ms for incoming bytes and stores them in ``uart_rx`` buffer.
The function returns number of received bytes or ``0`` if no byte was received during timeout window.

Asynchronous reading and writing
********************************

This example does asynchronous send and receive of data on ``TWR_UART_UART1``.

.. note::

    **Low power UART**

    When you call ``twr_uart_async_read_start`` then the sheduler stops sleeping the MCU so this function is not low-power friendly.
    After you call ``twr_uart_async_read_stop`` the periodic sleeping of MCU is again activated.
    The only solution to receive over UART in low-power mode is to use ``TWR_UART_UART1`` with ``TWR_UART_BAUDRATE_9600`` which is using ``LPUART`` (low power UART peripheral).
    ``LPUART`` is clocked from the 32 kHz crystal that can run even when the MCU is sleeping so you won't miss a single byte.

.. code-block:: c
    :linenos:

    #include <application.h>

    twr_fifo_t tx_fifo;
    twr_fifo_t rx_fifo;
    uint8_t tx_fifo_buffer[64];
    uint8_t rx_fifo_buffer[64];

    void uart_handler(twr_uart_channel_t channel, twr_uart_event_t event, void *param)
    {
        uint8_t rx_data[32];

        if (event == TWR_UART_EVENT_ASYNC_WRITE_DONE)
        {
            // here you can for example send more data
        }
        if (event == TWR_UART_EVENT_ASYNC_READ_DATA)
        {
            // Read data from FIFO by a single byte as you receive it
            size_t number_of_rx_bytes = twr_uart_async_read(TWR_UART_UART1, rx_data, sizeof(rx_data));
            char uart_tx[32];
            snprintf(uart_tx, sizeof(uart_tx), "RX: %d\r\n", number_of_rx_bytes);
            twr_uart_async_write(TWR_UART_UART1, uart_tx, strlen(uart_tx));
        }
        if (event == TWR_UART_EVENT_ASYNC_READ_TIMEOUT)
        {
            // No data received during set timeout period
            char uart_tx[] = "Timeout\r\n";
            twr_uart_async_write(TWR_UART_UART1, uart_tx, strlen(uart_tx));
            // You can also read received bytes here instead of TWR_UART_EVENT_ASYNC_READ_DATA
        }
    }

    void application_init()
    {
        twr_uart_init(TWR_UART_UART1, TWR_UART_BAUDRATE_115200, TWR_UART_SETTING_8N1);
        twr_uart_set_event_handler(TWR_UART_UART1, uart_handler, NULL);

        twr_fifo_init(&tx_fifo, tx_fifo_buffer, sizeof(tx_fifo_buffer));
        twr_fifo_init(&rx_fifo, rx_fifo_buffer, sizeof(rx_fifo_buffer));

        twr_uart_set_async_fifo(TWR_UART_UART1, &tx_fifo, &rx_fifo);

        twr_uart_async_read_start(TWR_UART_UART1, 500);

        char uart_tx[] = "Hello world\r\n";
        twr_uart_async_write(TWR_UART_UART1, uart_tx, strlen(uart_tx));
    }
