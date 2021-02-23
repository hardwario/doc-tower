#################
Quick Start Guide
#################

The goal of this **Quick Start Guide** is to show the basics in a few simple steps.

After this tutorial you will be able to build your device, flash firmware into it and get the data into your computer.

.. tip::

    This tutorial works with `Starter Kit <https://shop.hardwario.com/starter-kit/>`_.
    It is the easiest way to start with the HARDWARIO TOWER.

    Of course, you can do it with every other kit, you will just have to do a few more steps.

.. HARDWARIO TOWER is not just about the hardware but it comes with full documentation, tutorials,
.. software tools and most importantly - it comes with the extensive **technical support**.
.. HARDWARIO doesn't hesitate to use one of these channels In case you run in troubles or if anything is not clear to you:

.. - Write us an email to ask@hardwario.com
.. - Use forum at https://forum.hardwario.com/

*************
Initial steps
*************

.. tip::

    To learn all the basics please follow these steps.

.. toctree::
    :maxdepth: 1
    :hidden:

    quick-start-guide-steps/prepare-basics
    quick-start-guide-steps/build-the-device
    quick-start-guide-steps/put-it-together

- :doc:`Follow the first part on how to prepare the basics <quick-start-guide-steps/prepare-basics>`.
- :doc:`In next part you will find out how to put the device together <quick-start-guide-steps/build-the-device>`.
- :doc:`Last chapter will tell you how to put it all together <quick-start-guide-steps/put-it-together>`.


--------------------------------

***********
Be Inspired
***********

It's always hard to build something without an inspiration.
We motivate our makers to share their work with others
and you can get ideas for your projects by visiting `our hackster.io page <https://www.hackster.io/hardwario/projects>`_.

.. _learn-more:

**********
Learn More
**********

.. note::

    If you have any problems or questions, you can use some of our other channels.

    - Write us an email to ask@hardwario.com
    - Use `our forum <https://forum.hardwario.com/>`_.

Now you can learn more by browsing the **documentation** or by visiting the **links below**.

- Get more information about the :doc:`HARDWARIO Playground <hardwario-playground>`.
- Take a look at the :doc:`Module Overview. <module-overview>`.
- Explore our :doc:`projects to get even more examples <projects>`.
- Learn about :doc:`HARDWARIO MQTT topics <../interfaces/mqtt-topics>` to control LEDs and relays.
- Try other integrations with :doc:`Grafana <../integrations/grafana-for-visualization>`, :doc:`Blynk <../integrations/blynk-mobile-app-builder>`, :doc:`Ubidots <../integrations/ubidots>` and others.
- Use your :doc:`Raspberry PI <../tutorials/raspberry-pi-installation>` or other single board computer (SBC) as a server.
- :ref:`Flash other firmware <flash-firmware>` or :doc:`write your own firmware <../firmware/basic-overview>` for the **Core Module.**.
- Check the :doc:`Core Module pinouts <../hardware/header-pinout>` and add your own buttons, relays and sensors.

.. _troubleshooting-chapter:

***************
Troubleshooting
***************

Cannot find the Radio Dongle or Core Module in the device list

- On Windows 7 and macOS please install the `FTDI VCP drivers <https://www.ftdichip.com/Drivers/VCP.htm>`_
- On Ubuntu you need to be in ``dialout`` user group. Please use command ``sudo usermod -a -G dialout $USER`` and restart computer
- HARDWARIO Playground cannot flash older Core Module Revision 1. Please use the ``bcf`` tool. :doc:`See version comparison <../troubleshooting/core-module-r1-and-r2-comparison>`
