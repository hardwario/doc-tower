####################
HARDWARIO Playground
####################

HARDWARIO Playground is free **Windows, macOS** and **Linux** software.
It is made for easy working with our IoT Kit.

********
Download
********

First we will start with the download.

Use `HARDWARIO Playground download page <https://www.hardwario.com/download/>`_ which always have the links to the latest version.

.. tip::

    Builds are also in `github releases <https://github.com/hardwario/bch-playground/releases>`_.

.. thumbnail:: ../_static/basics/playground/download-page.png
   :alt: Playground Functions Tab

.. - **Flash firmware** to Core Module
.. - **Manage wireless network** with Radio Dongle and nodes
.. - **Create programs** with visual programming in the **Node-RED**
.. - **Visualize** measured values and control nodes with Dashboard

***************
Playground tabs
***************

To learn more about all the features, visit separate chapters for each tab:

.. toctree::
    :maxdepth: 1
    :hidden:

    playground-tabs/devices
    playground-tabs/functions
    playground-tabs/dashboard
    playground-tabs/messages
    playground-tabs/firmware

- :doc:`Devices Tab <playground-tabs/devices>`
- :doc:`Messages Tab <playground-tabs/messages>`
- :doc:`Functions Tab <playground-tabs/functions>`
- :doc:`Dashboard Tab <playground-tabs/dashboard>`
- :doc:`Firmware Tab <playground-tabs/firmware>`
- Help tab should send you right back here

***************
Troubleshooting
***************

Cannot find the Radio Dongle or Core Module in the device list

- On Windows 7 and macOS please install the `FTDI VCP drivers <https://www.ftdichip.com/Drivers/VCP.htm>`_
- On Ubuntu you need to be in ``dialout`` user group. Please use command ``sudo usermod -a -G dialout $USER`` and restart computer
- HARDWARIO Playground cannot flash older Core Module Revision 1. Please use the ``bcf`` tool. :doc:`See version comparison <../troubleshooting/core-module-r1-and-r2-comparison>`
