############################################
HARDWARIO TOWER Visual Studio Code extension
############################################

.. note::
    This tutorial expects that you have a running Visual Studio Code with our HARDWARIO TOWER extension installed.
    If you don't please visit the :doc:`Installation guide <hardwario-code-installation>`.

This extension makes it possible to simply develop, flash and debug firmware for HARDWARIO TOWER.

It runs in two modes:

- If you have anything else or nothing open (:ref:`Basic Mode<basic-mode>`)

    .. thumbnail:: ../_static/firmware/hardwario-code/basicMode.png
        :width: 30%

- If you have some HARDWARIO TOWER firmware open (:ref:`Firmware Mode<firmware-mode>`)

    .. thumbnail:: ../_static/firmware/hardwario-code/firmwareMode.png
        :width: 30%

In both modes you should see the HARDWARIO logo on the side panel.

.. thumbnail:: ../_static/firmware/firmware-quick-start/hardwario-extension-icon.png
        :width: 40%

.. _basic-mode:

**********
Basic Mode
**********

If you didn't open folder with HARDWARIO TOWER firmware the extension will activate but will provide fewer options.

You will get access to some basic commands that will lead you to our websites and then two commands for cloning firmware from our GitHub.

You can use these commands to get started with firmware development.

From Skeleton Project...
************************

You will be prompted to select a folder where the `twr-skeleton <https://github.com/hardwario/twr-skeleton>`_ firmware should be cloned (New folder for the firmware will be created).
After you select the folder you can name your firmware folder so you don't have some collisions with other firmware folders.

From Existing Project...
************************

You will be provided a list of existing firmware for `HARDWARIO TOWER available on our company GitHub <https://github.com/orgs/hardwario/repositories>`_.
You can select any of them based on the name and description of the firmware.

You will be prompted to select a folder where the selected firmware should be cloned (New folder for the firmware will be created).
After you select the folder you can name your firmware folder so you don't have some collisions with other firmware folders.

After you clone the firmware the window will be reopened with the firmware.

.. _firmware-mode:

*************
Firwmare Mode
*************

In this mode you will get some additional controls on the bottom panel and in the side panel.

On the bottom panel there are some important controls that you can quickly use so you can develop without the side panel:

.. thumbnail:: ../_static/firmware/hardwario-code/controls-panel.png
    :width: 100%

- **Device selection** - with this you will have to select device that you want to work with. If you have no HARDWARIO devices connected there will be a **No Device found!** prompt. If you have multiple devices connected, you can browse through them by clicking on the text.
- **Firmware type selection** - you can choose if you want to build in **debug** or **release** mode. For normal development we recommend to use the default **debug** setting because it enables logging.
- There are other symbols that you can use which will be described later, with the commands that they call.

Build + Flash (Console) |debug-alt|
***********************************

.. |debug-alt| thumbnail:: ../_static/firmware/hardwario-code/debug-alt.png
    :width: 3%

This command will do basically the whole cycle that you can use while developing. It will build the firmware, flash it to the selected device and then attach the console
for the device to see the log messages.

You can use this most of the times.

.. tip::
    To learn about debugging with the console you can visit :ref:`debugging with HARDWARIO Code <debug-hardwario-code>`.

Build + Flash (Debugger)
************************

.. warning::
    You have to have ``arm-none-eabi-gdb`` and ``JLinkGDBServerCL`` in PATH for this to work. If you are using our portable version you don't have to worry about that.

This command will not attach the console like the previous one but will instead try to attach to JLink debugger for some advanced debugging.
You can read more about JLink debugging in :doc:`Advanced Debugging chapter <advanced-debugging>`.

Clean All Outputs |trash|
*************************

.. |trash| thumbnail:: ../_static/firmware/hardwario-code/trash.png
    :width: 3%

This command will clean all the outputs so you can recompile everything from scratch.

Build Firmware |check|
**********************

.. |check| thumbnail:: ../_static/firmware/hardwario-code/check.png
    :width: 4%

This command runs **cmake** and **ninja** on the code. You can check if you have some errors or warnings in the code before you flash it into the device.

Flash Firmware |up-arrow|
*************************

.. |up-arrow| thumbnail:: ../_static/firmware/hardwario-code/up-arrow.png
    :width: 3%

This command will flash the firmware onto the selected device. It will also run build in case you didn't do that before or forgot to rebuild the changes.

Attach Console
**************

This command will attach console to the selected device so you can view the log messages.

.. tip::
    To learn about debugging with the console you can visit :ref:`debugging with HARDWARIO Code <debug-hardwario-code>`.


Attach Debugger
***************

.. important::
    You have to have ``arm-none-eabi-gdb`` and ``JLinkGDBServerCL`` in PATH for this to work.

This command will try to connect to a JLink for advanced debugging.

Debugging can be started multiple ways.

You can read more about JLink debugging in :doc:`Advanced Debugging chapter <advanced-debugging>`.

Press F5 button with some \*.c or \*.h file in focus
====================================================

.. important::
    There has to be no ``launch.json`` present in the ``.vscode`` folder.

If you want to just run the debug and not change anything in the ``launch.json`` you can just press F5 and select **HARDWARIO TOWER Debug**.
Debugging should start with no problem

.. thumbnail:: ../_static/firmware/hardwario-code/debuggingWithF5.png
    :width: 70%

Go to **Run and Debug** and create launch.json
==============================================
If you want to have your custom ``launch.json`` you can go to the Run and Debug window on the side panel and click `create a launch.json file` and select **HARDWARIO TOWER Debug**.
or add this configuration to an existing one.

.. code-block:: json

    {
        "name": "HARDWARIO TOWER Debug",
        "request": "launch",
        "type": "cortex-debug",
        "cwd": "${workspaceFolder}",
        "device": "STM32L083CZ",
        "servertype": "jlink",
        "jlinkscript": "./sdk/tools/jlink/flash.jlink",
        "interface": "swd",
        "serverpath": "${command:hardwario-tower.locate_jlink}",
        "svdFile": "./sdk/sys/svd/stm32l0x3.svd",
        "gdbPath": "${command:hardwario-tower.locate_toolchain}",
        "runToEntryPoint": "application_init",
        "executable": "${workspaceFolder}/out/debug/firmware.elf",
        "windows": {
            "gdbPath": "${command:hardwario-tower.locate_toolchain}.exe",
            "serverpath": "${command:hardwario-tower.locate_jlink}.exe"
        }
    }


Press Attach Debugger in the HARDWARIO Extension command palette
================================================================
You can use this option if you don't want to worry about the launch.json or any other options mentioned before.
Just select the HARDWARIO logo on the side panel and select **Attach Debugger** or **Build + Flash (Debugger)** option.
