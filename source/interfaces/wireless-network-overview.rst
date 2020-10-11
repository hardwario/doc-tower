#########################
Wireless Network Overview
#########################

*******************************************
HARDWARIO TOWER radio, LoRa, Sigfox, NB-IoT
*******************************************
This article compares the wireless technologies you can use with HARDWARIO TOWER - Industrial IoT Kit.
The Kit supports not just generic 868 MHz communication, bud can communicate also by other Low Power Wide Area Networks (LPWAN):

- HARDWARIO 868/915 MHz FSK radio
- LoRa
- Sigfox
- NB-IoT

.. tip::

    More information could be found in this `LPWAN comparison article <https://www.iotforall.com/iot-connectivity-comparison-lora-sigfox-rpma-lpwan-technologies/>`_.

HARDWARIO 868/915 MHz FSK radio
*******************************
:doc:`HARDWARIO 868/915 MHz radio article <sub-ghz-radio>`

Every Core Module has a SPIRIT1 radio module on it. This radio works up to 400 meters in open area or convers regular family house.

**Parameters:**

- Range in open area: 400 m
- Packet size: 50 bytes

**References:**

- `HARDWARIO Radio Projects on GitHub <https://www.github.com/hardwario?q=radio>`_

LoRa Network
************
:doc:`HARDWARIO LoRa Module article <../hardware/about-lora-module>`

This is a network build by companies, municipalities and public.
You can try to google if some company in your country/area provides this network (`CRA <https://www.cra.cz/iot-services>`_, `Starnet <https://www.starnet.cz/iot/>`_).
You can also buy your own gateway and create your own network for school or city,
or use the community `The Things Network <https://www.thethingsnetwork.org>`_ (`coverage map <https://www.thethingsnetwork.org/map>`_).

**Gateways:**

- `IMST IC880A Lite Gateway <https://shop.imst.de/wireless-modules/lora-products/36/lite-gateway-demonstration-platform-for-lora-technology>`_
- `Multitech <https://www.multitech.com/brands/multiconnect-conduit>`_
- and many others - `just google <https://www.google.com/search?sxsrf=ALeKk02UhD2IjBoP5XTjEIFe5-nyauCxZQ%3A1597246404491&source=hp&ei=xAs0X8D9GvCclwSgyIDQBg&q=LoRa+gateways&oq=LoRa+gateways&gs_lcp=CgZwc3ktYWIQAzIFCAAQywEyBQgAEMsBMggIABAWEAoQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgcIIxDqAhAnOgkIIxDqAhAnEBM6BAgjECc6BAguECc6BQgAELEDOggIABCxAxCDAToCCC46BggjECcQEzoFCC4QsQM6AggAOggILhCxAxCDAToICC4QsQMQkwI6BAgAEApQz0lYr2FguGNoAnAAeACAAdUBiAGTCpIBBjEwLjIuMZgBAKABAaoBB2d3cy13aXqwAQo&sclient=psy-ab&ved=0ahUKEwjA77jE_pXrAhVwzoUKHSAkAGoQ4dUDCAY&uact=5>`_

**Parameters:**

- Range in open area: 10 km
- Packet size: 50 - 200 bytes

**References:**

- `HARDWARIO LoRa Projects on GitHub <https://www.github.com/hardwario?q=lora>`_

Sigfox Network
**************
:doc:`HARDWARIO Sigfox Module article <../hardware/about-sigfox-module>`

.. warning::

    The Sigfox has a subscription model, you can check it out on `their page <https://buy.sigfox.com>`_

Because Sigfox is global network, you don't have to deal with SIM cards or roaming.
You do not have to buy or manage gateway. You just use already working infrastructure.

Check `Sigfox coverage map <https://www.sigfox.com/en/coverage>`_ to see if your area is covered.

**Parameters:**

- Range in open area: 10 km
- Packet size: 12 bytes

**References:**

- `Sigfox Projects on GitHub <https://www.github.com/hardwario?q=sigfox>`_

NB-IoT network
**************
For this network you can use our platform `CHESTER <https://www.hardwario.com/chester>`_.

NB-IoT Module for HARDWARIO TOWER - Industrial IoT Kit is in the development.





