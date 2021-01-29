##############
How to: EEPROM
##############

EEPROM is a special kind of memory. It is small (**6 KB on Core module chip**) memory with limited number of write/erase cycles.
It is non-volatile memory - which means that it does not require power to retain stored information.
**Which means that bytes written/stored inside the EEPROM will stay there until erased/rewritten**.

Don't be afraid of limited W/E cycles. In standard conditions the chip guarantees 100 000 cycles.
Remember that those cycles are *Write/Erase*

.. important::

    Reading from the EEPROM do not count, so it is completely safe to read from it as much as you wish.

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__eeprom.html>`_

***********
EEPROM Size
***********

HARDWARIO TOWER Core module has 6 KB EEPROM included. In case you need to find this value out inside your code,
there is a function for this inside the SDK: ``size_t twr_eeprom_get_size(void)``

************
EEPROM Write
************

Writing to EEPROM is very easy. It takes only one call to this function: ``bool twr_eeprom_write(uint32_t address, const void *buffer, size_t length)``

**Parameters taken:**

- ``address`` - start address (starts at 0, ends at 6143)
- ``buffer`` - pointer to source buffer, from which data will be red (can be any type - int, char, float, ...)
- ``length`` - number of bytes to by written

**Returned value** indicates whether the write process was successful or not.

It is completely up to you from what address you start to write.
You can start from 0, 42, 666,... all the way up to circa 6000.

.. note::

    Please note that some of our modules (currently twr_radio_* module only) use few last dozens of bytes in EEPROM.
    If you use those modules, remember to use the memory addresses from 0 up to 6000. This makes sure that no data will be overwritten.

Always make sure that you have correctly chosen the ``length`` parameter.
If you want to write some numeric value, you can use the ``sizeof()`` function to find out the correct number.
Let's say that you have a *float* variable and you want to write this number to address 0:

.. code-block:: c
    :linenos:

    float var = 3.14159;
    twr_eeprom_write(0, &var, sizeof(var));

***********
EEPROM Read
***********

Reading from the EEPROM is similar to writing. There is appropriate function for this task: ``bool c_eeprom_read(uint32_t address, void *buffer, size_t length)``

Same parameters and return value purpose. Only exception is that the buffer is now pointer to the destination ``buffer`` where data from EEPROM will be written to.

Let's say that now you want to read previously saved value and store it inside variable called buf. You also know that *float* value has size of four bytes:

.. code-block:: c
    :linenos:

    float buf;
    twr_eeprom_read(0, &buf, 4);

***********
R/W Example
***********

In this example we will write float value and string to EEPROM immediately after Core boot.
On every press of a button the data will be retrieved from EEPROM and sent to computer.
To test that the memory is really persistent you can try to comment both ``twr_eeprom_write*`` lines out (after running the original example once, of course).
It will still work.

The output in serial console will look like this:

.. code-block:: console

    EEPROM size: 6144
    Data:
    3.141590
    hello world!

Example
*******

.. code-block:: c
    :linenos:

    #include "twr.h"
    #include "twr_usb_cdc.h"

    twr_button_t button;

    void button_event_handler(twr_button_t *self, twr_button_event_t event, void *event_param)
    {
        (void) self;
        (void) event_param;

        if (event == TWR_BUTTON_EVENT_PRESS)
        {
            size_t eeprom = twr_eeprom_get_size();
            char buffer[100];
            char readEeprom[13];
            float readFloat;

            twr_eeprom_read(0, &readFloat, 4);
            twr_eeprom_read(4, readEeprom, 12);
            readEeprom[12] = '\0';

            sprintf(buffer, "EEPROM size: %d\r\nData:\r\n%f\r\n%s\r\n", eeprom, readFloat, readEeprom);

            twr_usb_cdc_write(buffer, strlen(buffer));
        }
    }

    void application_init(void)
    {
        float toWriteFloat = 3.14159;
        char toWrite[] = "hello world!";
        twr_eeprom_write(0, &toWriteFloat, sizeof(toWriteFloat));
        twr_eeprom_write(sizeof(toWriteFloat), toWrite, sizeof(toWrite));

        // Initialize button
        twr_button_init(&button, TWR_GPIO_BUTTON, TWR_GPIO_PULL_DOWN, false);
        twr_button_set_event_handler(&button, button_event_handler, NULL);

        twr_usb_cdc_init();
    }

