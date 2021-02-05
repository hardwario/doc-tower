###################
How to: LoRa Module
###################

`LoRa Module <https://shop.hardwario.com/lora-module/>`_ provides a simple way how to connect your kit to the LoRA network. You can use commercial,
community or your own LoRa gateway to receive messages from your device.

The most used community LoRa backends are `The Things Network <https://www.thethingsnetwork.org>`_ and `LorIoT <https://www.loriot.io>`_.

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__cmwx1zzabz.html>`_

*****************
How Does it Work?
*****************

- Message is sent from device
- LoRa gateway receives the message which is processed by the backend
- Backend resends the message to your server

*******
Example
*******

This example sends simple packet after boot. It is also demonstrating handling of the various events in the callback function.
Some parts of the code is commented out for different configuration like OTAA key exchange with JOIN command.

Also there is a example how to read the modem parameters when the device is ready in the ``TWR_CMWX1ZZABZ_EVENT_READY`` event handler.

You can also receive data in **Class A** or **Class C** mode which you can set by calling ``twr_cmwx1zzabz_set_class``.
The received data are handled in the ``TWR_CMWX1ZZABZ_EVENT_MESSAGE_RECEIVED`` event handler.
