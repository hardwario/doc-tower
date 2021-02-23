##############
LoRa IoT Radio
##############

LoRa is a proprietary radio technology that allows sending small data packets both directions (uplink & downlink).
Radio modulation was designed by the Semtech company and allows long range and long lifetime when powering device from the batteries.
The message can contain 52 bytes and you can send/receive data about every 10 minutes. Radio is using ISM band 868 MHz in Europe and 915 MHz in the US.

.. tip::

    To learn how to setup the device with AT commands, you can read the :doc:`LoRa AT setup document <../tutorials/lora-at-commands-configuration>`.

Advantage of LoRa is that it's possible to build/buy your own personal gateway,
use some community-based networks like `The Things Network <https://www.thethingsnetwork.org>`_, `LORIOT <https://www.loriot.io>`_ or many others.
It's also possible to use commercial provider's already established LoRa network.

.. thumbnail:: ../_static/interfaces/lora-iot-radio/module-overview-lora-module.png
   :width: 45%
   :alt: HARDWARIO TOWER LoRa Module

HARDWARIO TOWER - Industrial IoT Kit has `LoRa Module <https://shop.hardwario.com/lora-module/>`_ which you can use to create battery operated nodes that are sending or receiving data.
Module supports LoRaWAN Class A and Class C.

.. tip::

    You can go and learn more about LoRa from `our projects on hackster.io <https://www.hackster.io/hardwario/projects?category_id=198>`__
