###############
How to: SPI bus
###############

Serial Peripheral Bus (SPI) is synchronous serial bus. It's used for fast interconnection of the peripherals inside the device.
HARDWARIO TOWER uses SPI for example in the :doc:`LCD Module <how-to-lcd-module>`.

The SPI uses these signals:

- SCK - **Serial Clock** - SPI transfers are synchronous and needs the clock signal
- MOSI - **Master Out, Slave In** - This is serial output from MCU to the peripheral
- MISO - **Master In, Slave Out** - This is serial input for data from peripheral to MCU
- NSS - **Negative Slave Select** - This signal activates the slave device. It's active low, that's why the word **negative**.
  If you have multiple slave devices you have multiple ``NSS`` signals. It's sometimes also called the Chip Select ``CS``.

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__spi.html>`_

**************
Initialization
**************

SPI on HARDWARIO Core Module has fixed pins, so initialization is simple

.. code-block:: c

    twr_spi_init(TWR_SPI_SPEED_1_MHZ, TWR_SPI_MODE_0);

*****
Speed
*****

You can choose from several communication speeds.
The communication speed is limited by the maximal speed that the slave device can communicate,
the length of the wires, noise, current consumption or electromagnetic radiation limits.

.. code-block:: console
    :linenos:

    TWR_SPI_SPEED_1_MHZ
    TWR_SPI_SPEED_2_MHZ
    TWR_SPI_SPEED_4_MHZ
    TWR_SPI_SPEED_8_MHZ
    TWR_SPI_SPEED_16_MHZ

********
SPI Mode
********

Clock polarity and clock phase defines when the output data is valid. Whether its on the rising or falling edge.
This information can be found in the datasheet of the slave device.

.. code-block:: console
    :linenos:

    TWR_SPI_MODE_0 // SPI mode of operation is 0 (CPOL = 0, CPHA = 0)
    TWR_SPI_MODE_1 // SPI mode of operation is 1 (CPOL = 0, CPHA = 1)
    TWR_SPI_MODE_2 // SPI mode of operation is 2 (CPOL = 1, CPHA = 0)
    TWR_SPI_MODE_3 // SPI mode of operation is 3 (CPOL = 1, CPHA = 1)

******************************
Transmiting and receiving data
******************************

The transmission can be done synchronously (blocking read and write) or asynchronously (non-blocking read and write).
With asynchronous transmition it is neccessary to first check if the previous operation has ended.

.. code-block:: c
    :linenos:

    if (twr_spi_is_ready())
    {
        // Start new stransfer
    }

During transmission you are sending data out at ``MOSI`` pin and at the same time receiving data at ``MISO`` pin.
So every transmission is basically also receiving data. So the functions have always parameters for both buffers.


Synchronous transfer
********************

You need to create transmit and receive buffer. Then you start the blocking transfer.

.. code-block:: c
    :linenos:

    uint8_t tx_buffer[2] = { 0x20, 0x00 };
    uint8_t rx_buffer[2];

    twr_spi_transfer(tx_buffer, rx_buffer, sizeof(rx_buffer));

If you are just transmitting data, then replace the ``rx_buffer`` by ``NULL`` and vice-versa for just receiving.
The function returns ``false`` if the previous asynchronous transfer has not ended yet.

Asynchronous transfer
*********************

This is non-blocking transfer where the callback function is called when the transfer is completed.

.. code-block:: c
    :linenos:

    // In async transmit the buffers must be global or
    // in the function but defined as a static
    uint8_t tx_buffer[2] = { 0x20, 0x00 };
    uint8_t rx_buffer[2];

    void send_data(void)
    {
        // Check if previous asynchronous transfer is not running
        if (twr_spi_is_ready())
        {
            // Set event handler and optional parameter (NULL for now)
            twr_spi_async_transfer(tx_buffer, rx_buffer, sizeof(tx_buffer), _twr_spi_event_handler, NULL)
        }
    }

    void _twr_spi_event_handler(twr_spi_event_t event, void *event_param)
    {
        (void) event_param;

        if (event == TWR_SPI_EVENT_DONE)
        {
            // Transfer done, you can for example handle received data or initiate a new transfer
        }
    }
