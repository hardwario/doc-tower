################
Power Management
################

.. caution::

    This document goes deep into technical details and explains the HARDWARIO TOWER - Industrial IoT Kit power management on the hardware level.

The **HARDWARIO TOWER - Industrial IoT Kit** has been designed the way to allow connection of multiple power sources.

For example, this allows the **Core Module** to be powered from a USB cable and also have batteries inserted in the **Battery Module** at the same time.
HARDWARIO automatically solves the problem selecting the appropriate power sources.

What does it mean? For example, when an external power supply (adapter or USB) is connected, the battery is disconnected.
It is also possible to have multiple external sources connected at the same time - for example,
the adapter plugged into the Power Module and the USB cable in the Core Module.

.. note::

    In this case, the module that is located in the physically lower layer will take priority and will be the one that will deliver power to the system.

************
How It Works
************

The HARDARIO header has two signals for system power distribution:

- **VDD** - Positive supply rail either 3.1 V when powering from batteries or 3.3 V from the external power supply
- **GND** - Ground (negative rail)

The module that is able to deliver power in the system is called the **energizer**.
The energy is supplied either using an external power supply, or batteries.
In both cases, an **energizer** contains the electronic circuit for intelligent power management.

This additional electronics circuit controls (or is controlled by) two auxiliary signals on the HARDWARIO header:

Signal BAT_OFF
**************

This signal disconnects the batteries and prevents their **discharging** when other power source is available and the batteries are not needed.

.. note::

    An OR-ing diode is used so multiple modules driving this signal at the same time do not interfere.

Signal VDD_OFF
**************

This signal is physically split into two parts:

- Signal **VDD_OFF_IN**

    This signal is on the bottom side of the module **(the side with the pins)** and it disconnects the power supply output of the given module.

- Signal **VDD_OFF_OUT**

    This signal is on the top side of the module **(the side with the sockets)** and it is chained to the VDD_OFF_IN signal of the module above the given one.

.. note::

    The split is easy to implements thanks to **SMT technology** of the connectors.
    Pins and sockets on the header are not electrically connected unless a via is used explicitly.

**************
Implementation
**************

This is the example of the electronic circuit of the battery energizer:

.. thumbnail:: ../_static/hardware/power_management/energizer-circuit-battery.png
   :width: 60%
   :alt: Energizer Circuit Battery

This is the example of the eletronics circuit of the **energizer** powered from an external power supply:

.. thumbnail:: ../_static/hardware/power_management/energizer-circuit-external.png
   :width: 60%
   :alt: Energizer Circuit External
