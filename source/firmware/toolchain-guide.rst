###############
Toolchain Guide
###############

.. warning::

    This document assumes that you have necessary tools installed according to the document :doc:`Toolchain Setup <toolchain-setup>`.

    All of the steps below assume work with **HARDWARIO Toolchain** in Windows or with the **Terminal** application in macOS or Ubuntu.

*******************************
Program HARDWARIO Firmware Tool
*******************************

The program HARDWARIO Firmware Tool (**bcf**) simplifies the firmware workflow.

This tool allows to:

- Manipulate with firmware packages:
    - Update package database (``bcf update``)
    - Listing from package database (``bcf list``)
    - Search in package database (``bcf search``)
    - Download package for offline use (``bcf pull``)
- Upload firmware (``bcf flash``)
- Create empty project for firmware development (``bcf create``)

We will show the individual operations in the following chapters.

.. tip::

    HARDWARIO projects offer pre-compiled firmware binary images in the section **Releases** of the given GitHub repository.

The **bcf** tool has a built-in help system. You can see the basic list of commands by using ``bcf help``:

.. code-block:: console
    :linenos:

    usage: bcf [-h] [-v] COMMAND ...

    HARDWARIO Firmware Tool

    positional arguments:
    COMMAND
        update       update list of available firmware
        list         list firmware
        flash        flash firmware
        devices      show devices
        search       search in firmware names and descriptions
        pull         pull firmware to cache
        clean        clean cache
        create       create new firmware
        read         download firmware to file
        help         show help

    optional arguments:
    -h, --help     show this help message and exit
    -v, --version  show program's version number and exit

Detailed usage of a given command using e.g. ``bcf help flash``:

.. code-block:: console
    :linenos:

    usage: bcf flash
           bcf flash <firmware>
           bcf flash <file>
           bcf flash <url>

    optional arguments:
        -h, --help            show this help message and exit
        --device {/dev/ttyUSB0}
                                device
        --dfu                 use dfu mode

.. note::

    Device Firmware Upgrade (DFU) is a vendor- and device-independent mechanism for upgrading the firmware of USB devices


************************
Firmware Package Listing
************************

Use this command to update the list of available firmware packages:

.. code-block:: console

    bcf update

.. caution::

    Always use this command before listing the available packages.

Use this command to list the available firmware packages:

.. code-block:: console

    bcf list

Example output:

.. code-block:: console

    hardwario/bcf-gateway-usb-dongle:v1.13.0
    hardwario/bcf-radio-8-ball:v1.0.0
    hardwario/bcf-radio-air-quality-monitor:v1.1.0
    hardwario/bcf-radio-burglar-alarm:v1.1.0
    hardwario/bcf-radio-climate-monitor:v1.5.0
    hardwario/bcf-radio-co2-monitor:v1.5.1
    hardwario/bcf-radio-co2-voc-lp-monitor:v1.2.0
    hardwario/bcf-radio-door-lock:v1.1.0
    hardwario/bcf-radio-door-sensor:v0.2.0
    hardwario/bcf-radio-ds18b20-with-lcd:v1.1.0
    hardwario/bcf-radio-flood-detector:v1.3.0
    hardwario/bcf-radio-fridge-monitor:v1.1.0
    hardwario/bcf-radio-infragrid-sensor:v1.0.0
    hardwario/bcf-radio-key-code:v1.1.0
    hardwario/bcf-radio-lcd-as504x-absolute-encoder:v1.0.0

Use this command to list all the versions of the available firmware packages:

.. code-block:: console

    bcf list --all

Use this command to search in the available packages (in their title and description):

.. code-block:: console

    bcf search <searched term>


***************
Firmware Upload
***************

There are two bootloaders in MCU ROM:

- DFU - in case of USB device in MCU is used (e.g. for Core Module R1.3)
- UART - in case of USB-UART chip device is used (e.g. for Radio Dongle or Core Module R2.x)

.. tip::

    If you are interested, you can go and see the different between the Core Modules


.. warning::

    In case you need to upload the firmware into the Core Module R1, you must first put it in the DFU mode. Moreover,
    the flash command must be in the ``bcf flash --device dfu`` format.

Firmware upload can be done using the ``bcf flash`` command. The firmware can be obtained from 3 different sources:

Source firmware package, for instance
*************************************

.. code-block:: console

    bcf flash hardwario/bcf-radio-push-button:latest

Source local disk file, for instance
************************************

.. code-block:: console

    bcf flash firmware.bin

Source file from the specified URL, for instance
************************************************

.. code-block:: console

    bcf flash https://github.com/hardwario/bcf-radio-push-button/releases/download/v1.4.1/bcf-radio-push-button-v1.4.1.bin

You can list the USB UART devices connected to your host using this command:

.. code-block:: console

    bcf devices

...and then use the device from the list altogether with the ``--device`` parameter, e.g.:

.. code-block:: console

    bcf flash --device /dev/ttyUSB0 hardwario/bcf-gateway-usb-dongle:latest

this way the ``bcf`` will not ask you which serial port to use every time.


**********************
Firmware Package Cache
**********************

If the firmware does not exist in the local cache, it is download first with the first ``bcf flash`` command.

Also, if you need to download the firmware package and work with it later offline, you can download it using the ``bcf pull`` command, for instance:

.. code-block:: console

    bcf pull hardwario/bcf-gateway-usb-dongle:latest

If you want to clean the cache of the firmware package list and all the downloaded packages, use this command:

.. code-block:: console

    bcf clean

*****************************
Create Blank Firmware Project
*****************************

Go to the directory where you want to create a firmware directory
*****************************************************************

Create a blank project
**********************

.. code-block:: console

    bcf create <firmware-name>

.. important::

    The starting point for developing your own firmware is the file app/application.c.

The bcf program cloned the basic firmware skeleton, which is ready to build immediately (see description below)
***************************************************************************************************************

**************
Build Firmware
**************

Firmware build is done using the traditional traditional build system **GNU Make**,
which follows the recipe given in the file ``Makefile`` (found in the firmware root directory).

There are 2 target configurations to build the firmware:

- ``debug``

    This configuration is implicit and is suitable for firmware development. The built-in firmware is ready for debugging.

- ``release``

    This configuration is suitable for final deployment.
    It has build some optimizations turned on and is not suitable for firmware debugging due to these optimizations.
    The resulting program in this configuration can run faster and show lower power consumption than the one in ``debug`` configuration.

You can build the firmware by following these steps:

Go to the firmware directory you want to build
**********************************************

Run the build command
*********************

.. code-block:: console

    make

.. tip::

    Build process can be accelerated by specifying the number of parallel compiler processes through the parameter ``-j <number>``.
    The number should match the number of cores in your processor. Example: ``make -j4``

Upon successful completion of the build process, you will receive a similar listing at the end
**********************************************************************************************

.. code-block:: console
    :linenos:

    Linking object files...
    Size of sections:
        text    data     bss     dec     hex filename
        74332    2776    7328   84436   149d4 out/debug/firmware.elf
    Creating out/debug/firmware.bin from out/debug/firmware.elf...

The program called linker created two important files
*****************************************************

- ``out/debug/firmware.elf``

    This is the file in ELF format containing symbols necessary for a debugger.

- ``out/debug/firmware.bin``

    This is the binary image necessary for programming (the ELF file also contains this binary image).

In order to build the firmware in release configuration, use this command
*************************************************************************

.. code-block:: console

    make release

This command generates the file ``out/release/firmware.bin``.

.. _switch-to-dfu:

***********************************
Switching Core Module into DFU Mode
***********************************

To program the **Core Module**, we must first enter the DFU mode.

We can do this by following this procedure

Check that the USB cable is plugged into the Core Module and your computer
**************************************************************************

Press and hold the BOOT button on the Core Module
*************************************************

.. tip::

    The BOOT button is on the right and is marked with a letter ``B``.

Press and release the RESET button on the Core Module. At this point, you still have to hold the BOOT button
************************************************************************************************************

.. tip::

    The RESET button is on the left and is marked with a letter ``9``.

Release the BOOT button
************************

.. note::

    Now the **Core Module** is connected to your computer as a DFU USB device and is ready for programming.

**********************************
Windows DFU Driver Troubleshooting
**********************************

Incorrect DFU Driver
********************

In case you get ``Cannot open DFU device 0483:df11`` while running the **bcf flash --device dfu** command, you have the incorrect DFU drivers installed.

.. thumbnail:: ../_static/firmware/toolchain-guide/windows-dfu-wrong-driver.png
    :width: 60%


Execute ``zadig`` from Toolchain or Playground shell (from cmd.exe HARDWARIO window)
====================================================================================

.. caution::

    Keep the **Core Module** connected with the DFU mode activated.

Allow admin rigths in the User Acess Control pop-up
===================================================

Select Options -> List All Devices
==================================

.. thumbnail:: ../_static/firmware/toolchain-guide/windows-zadig-list-all-devices.png
    :width: 60%


Choose STM32 BOOTLOADER
=======================

.. thumbnail:: ../_static/firmware/toolchain-guide/windows-zadig-select.png
    :width: 60%


Choose WinUSB
=============

.. thumbnail:: ../_static/firmware/toolchain-guide/windows-zadig-winusb.png
    :width: 60%


Click on Replace Driver
=======================

.. thumbnail:: ../_static/firmware/toolchain-guide/windows-zadig-replace.png
    :width: 60%


.. important::

    You will get The driver was installed successfully notification.

.. thumbnail:: ../_static/firmware/toolchain-guide/windows-zadig-installed.png
    :width: 60%


Exit Zadig and get back to firmware flashing. The DFU driver repair procedure is finished
=========================================================================================

You can check DFU readiness using the ``dfu-util -l`` command from HARDWARIO Toolchain Prompt
=============================================================================================

.. thumbnail:: ../_static/firmware/toolchain-guide/windows-dfu-list.png
    :width: 60%


No DFU Device Found
*******************

There is not ``Cannot open DFU device 0483:df11`` between:

.. code-block:: console
    :linenos:

    A valid DFU suffix will be required in a future dfu-util release
    No DFU capable USB device available

.. thumbnail:: ../_static/firmware/toolchain-guide/windows-dfu-no-device.png
    :width: 60%


There can be various reasons:

DFU mode is not activated on the Core Module
============================================

Follow the instructions in the chapter :ref:`Switching Core Module into DFU Mode <switch-to-dfu>`.

Defective USB cable, USB hub, USB port or Core Module
=====================================================

- Try different hardware.
- Try connection without a USB hub.
- Make sure the USB cable used has data wires (some USB cables are for powering only).

Connection mismatch - the Core Module is connected to different host than where bcf is executed
===============================================================================================

- Connect the **Core Module** to the right host.

