***************************
Core Module Rev 1 debugging
***************************

.. note::
    You can skip to the next chapter if you don't have Core Module Rev 1.

Core Module revision 1 does not have FTDI serial to USB converter.
You need to connect your own converter to the UART2 to the pins TX2 and RXD2.

For example USB UART from SparkFun:

- `FTDI Basic Breakout - 3.3V <https://www.sparkfun.com/products/9873>`_
- `Jumper Wires <https://www.sparkfun.com/products/11709>`__

Or another example USB UART from Mouser:

- `FTDI cable TTL-232R-3V3 <https://eu.mouser.com/search/ProductDetail.aspx?qs=Xb8IjHhkxj627GFcejHp0Q%3d%3d>`_
- `Jumper Wires <https://eu.mouser.com/search/ProductDetail.aspx?R=0virtualkey0virtualkeyMIKROE-513>`__

Connect USB UART and Core Module into one PC's USB host sockets and interconnect Core Module with USB UART by single wire
USB UART RX (YELLOW wire on cable) and Core Module TXD2 (header pin 22) -
have a look at `Core Module Header drawing <https://developers.hardwario.com/hardware/header-pinout>`_.

.. warning::

    Beware of groud loop and ground voltage difference in case you do not use same PC to power Core Module and to connect USB UART.
