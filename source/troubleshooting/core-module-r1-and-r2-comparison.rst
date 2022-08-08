################################
Core Module R1 and R2 Comparison
################################

We have released the new Core Module 2. Everything is the same, only the flash process is now easier and faster.

With Core R2 you can use the `HARDWARIO Playground <https://www.hardwario.com/download/>`_ GUI tool to program nodes,
manage radio network and create rules in Node-RED.

********************************
Technical and visual differences
********************************

The most significant change is that R2 has only single button. This is the ``B`` button.
It has moved and you can use it for your program.
The ``R`` reset button is not necessary anymore because communication and firmware flashing is now done automatically over **FTDI** chip.

.. |core-r1| thumbnail:: ../_static/hardware/core-module-r1-and-r2-comparison/core-module-r1.png
    :width: 300em
    :height: 300em

.. |core-r2| thumbnail:: ../_static/hardware/core-module-r1-and-r2-comparison/core-module-r2.png
    :width: 300em
    :height: 300em

+-----------+-----------+
| Core R1   | Core R2   |
+===========+===========+
| |core-r1| | |core-r2| |
+-----------+-----------+

The new **Core Module 2** is not using DFU mode anymore.
We have added new flashing over FTDI chip and virtual serial port over USB.
This means that the flashing procedure is now the same as with the Radio Dongle.
Please, use the **--device <PORT>** (e.g. COM4 or /dev/ttyUSB0) parameters instead of the former **--dfu or --device dfu** parameter.

************
Improvements
************

- No need to press any button to start firmware update.
- Faster firmware uploads over **FTDI** chip
- Smaller firmware because USB stack is now handled by **FTDI** chip.
- Simple debugging over serial port. The UART2 is connected to the FTDI so you can use `twr_log_* <https://sdk.hardwario.com/group__twr__log.html>`_ functions.
- No issues with DFU drivers on Windows.

***********************
Flashing Core Module R1
***********************

Step 1: Connect the Micro USB cable to the Core Module and your computer
************************************************************************

Step 2: You have to switch to DFU mode
**************************************

.. :ref:`Core Module to the DFU mode. <switch-to-dfu>`

Step 3: Upload firmware with following command
**********************************************

.. code-block:: console

    bcf flash --device dfu [firmware]:[version]

Example which flashes wireless-motion-detector firmware from `Radio Motion Detector project <https://www.hackster.io/filip-hanel/smart-photo-trap-with-climate-data-in-terrarium-7e4e8f>`_:

.. code-block:: console

    bcf flash --device dfu hardwario/bcf-radio-motion-detector:latest

***********************
Flashing Core Module R2
***********************

To flash this version of Core module we are using HARDWARIO Code or HARDWARIO Playground.

- :doc:`HARDWARIO Playground <../basics/hardwario-playground>`.
- :doc:`HARDWARIO Code <../firmware/hardwario-code-installation>`.
