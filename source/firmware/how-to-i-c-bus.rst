###############
How to: I²C Bus
###############

This is the main bus HARDWARIO TOWER uses to communicate with the most of the sensors and modules.
All sensors and modules have their own addres in the :doc:`HARDWARIO TOWER I²C address space <../hardware/i-c-address-space>`.

Normally you don't need to use I²C API, because all the sensors have their own libraries that gives you the measured data.
You will need I²C APIs in case you implement your own I²C sensor or chip.

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__bc__i2c.html>`_

****************************
I²C buses on the Core Module
****************************

There are two busses on the `Core Module <https://shop.hardwario.com/core-module/>`. They are called:

- ``BC_I2C_I2C0`` - Using ``SDA0`` and ``SCL0`` (17, 18) pins in the bottom right corner of the Core Module
- ``BC_I2C_I2C1`` - Using SDA1 and SCL1 (27, 28) pins in the top right corner of the Core Module

If you use `Tag Module <https://shop.hardwario.com/tag-module/>`_ then the right three tag connectors use
``BC_I2C_I2C0`` and left three are using ``BC_I2C_I2C1``. You can see this in `the schematics <https://github.com/hardwario/bc-hardware/tree/master/out/bc-module-tag>`_.

.. note::

    There's even a another **virtual** I2C bus ``BC_I2C_I2C_1W`` which is encapsulated in 1-Wire protocol and can be used with
    Sensor Module and 1-Wire Module to extend the communication distance.

********
Init I²C
********

By default the I²C buses **are not initialized** to save the power.
However when you initialize at least one sensor in the SDK, the bus is initialized with the first sensor in their respective ``bc_xxx_init`` function.
If you use only your sensor in the project, you have to initialize the I²C bus.

.. code-block:: c

    bc_i2c_init(BC_I2C_I2C0, BC_I2C_SPEED_400_KHZ);

********************************
Reading and writing 8 or 16 bits
********************************

You can use functions to write or read 1 byte, 2 bytes or specific number of bytes which is explained in next chapter below.

.. code-block:: c
    :linenos:

    bool bc_i2c_memory_write_8b (bc_i2c_channel_t channel, uint8_t device_address, uint32_t memory_address, uint8_t data)
    bool bc_i2c_memory_write_16b (bc_i2c_channel_t channel, uint8_t device_address, uint32_t memory_address, uint16_t data)

    bool bc_i2c_memory_read_8b (bc_i2c_channel_t channel, uint8_t device_address, uint32_t memory_address, uint8_t *data)
    bool bc_i2c_memory_read_16b (bc_i2c_channel_t channel, uint8_t device_address, uint32_t memory_address, uint16_t *data)

For example to write the data

.. code-block:: c
    :linenos:

    bc_i2c_memory_write_8b(BC_I2C_I2C0, 0x48, 0x01, 0x81);
    bc_i2c_memory_write_16b(BC_I2C_I2C0, 0x48, 0x01, 0x0180);

To read the data

.. code-block:: c
    :linenos:

    uint8_t reg_configuration;
    bc_i2c_memory_read_8b(BC_I2C_I2C0, 0x48, 0x01, &reg_configuration);

*****************************
Reading and writing more data
*****************************

.. code-block:: c
    :linenos:

    bool bc_i2c_write (bc_i2c_channel_t channel, const bc_i2c_transfer_t *transfer)
    bool bc_i2c_read (bc_i2c_channel_t channel, const bc_i2c_transfer_t *transfer)

Example to read more data:

.. code-block:: c
    :linenos:

    bc_i2c_memory_transfer_t transfer;
    uint8_t rx_buffer[6];

    transfer.device_address = 0x48;
    transfer.memory_address = 0x28;
    transfer.buffer = rx_buffer;
    transfer.length = sizeof(rx_buffer);

    bc_i2c_memory_read(BC_I2C_I2C0, &transfer);
