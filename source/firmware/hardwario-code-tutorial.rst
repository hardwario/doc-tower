############################################
HARDWARIO Tower Visual Studio Code extension
############################################

.. note::
    This tutorial expects that you have a running Visual Studio Code with our HARDWARIO Tower extension installed.
    If you don't please visit the :doc:`Installation guide <developement-hardwario-code>`.

This extension makes it possible to simply develop, flash and debug firmware for HARDWARIO Tower.

It runs in two modes:

- If you have anything else of nothing open (**Basic Mode**)
- If you have some HARDWARIO Tower firmware open (**Firmware Mode**)

In both modes you should see the HARDWARIO logo on the side panel.

**********
Basic Mode
**********

If you didn't open folder with HARDWARIO Tower firmware the extension will activate but will provide fewer options.

You will get access to some basic commands that will lead you to our websites and then two commands for cloning firmware from our GitHub.

You can use these commands to get started with firmware development.

After you clone the firmware the window will be reopened with the firmware.

*************
Firwmare Mode
*************

In this mode you will get some additional controls on the bottom panel and in the side panel.

On the bottom panel there are some additional controls that you can use:

- Device selection - with this you will have to select device that you want to work with. If you have no HARDWARIO devices connected there will be a **No Device** prompt. If you have multiple devices connected, you can browse through them by clicking on the text.
- Firmware type selection - you can choose if you want to build in **debug** or **release** mode. For normal development we recommend to use the default **debug** setting.
- There are other symbols that you can use which will be described with the commands that they call.

Build & Flash & Attach
**********************

This command will do basically the whole cycle that you can use while developing. It will build the firmware, flash it to the selected device and then attach the console
for the device to see the log messages.

You can use this most of the times.

.. tip::
    This command is represented by a Little play button with a bug on the bottom panel.

Build & Flash & Debug
*********************

This command will not attach the console like the previous one but will instead try to attach to JLink debugger for some advanced debugging.

Clean All Outputs
*****************

This command will clean all the outputs so you can recompile everything from scratch.

.. tip::
    This command is represented by a Trash bin icon on the bottom panel.

Build Firmware
**************

This command runs **make** on the code. You can check if you have some errors or warnings in the code before you flash it into the device.

.. tip::
    This command is represented by a Tick icon on the bottom panel.

Flash Firmware
**************

This command will flash the firmware onto the selected device. It will also run build in case you didn't do that before or forgot to rebuild the changes.

.. tip::
    This command is represented by an Up arrow icon on the bottom panel.

Attach Console
**************

This command will attach console to the selected device so you can view the log messages.

.. tip::
    This command is represented by a Plug icon on the bottom panel.

Start Debugging
***************

.. important::
    You have to have ``arm-none-eabi-gdb`` and ``JLinkGDBServerCL`` in PATH for this to work if you are using extension in your installed VSCode.
    If you are using our portable version you don't have to worry about anything and it will work just fine.

This command will try to connect with a connected JLink for advanced debugging

Debugging can be started multiple ways.

Press F5 button with some \*.c or \*.h file in focus
====================================================
.. important::
    There has to be no ``launch.json`` present in the ``.vscode`` folder.

If you want to just run the debug and not change anything in the ``launch.json`` you can just press F5 and select HARDWARIO TOWER Debug.
Debugging will start with no problem

.. thumbnail:: ../_static/firmware/hardwario-code/debuggingWithF5.png
    :width: 70%

Go to **Run and Debug** and create launch.json
==============================================
If you want to have your custom ``launch.json`` you can go to the Run and Debug window on the side panel and click `create a launch.json file`
or add this configuration to an existing one.

.. code-block:: json

    {
        "name": "HARDWARIO TOWER Debug",
        "request": "launch",
        "type": "cortex-debug",
        "preLaunchCommands": [
            "make -j"
        ],
        "cwd": "${workspaceFolder}",
        "device": "STM32L083CZ",
        "servertype": "jlink",
        "jlinkscript": "./sdk/tools/jlink/flash.jlink",
        "interface": "swd",
        "serverpath": "${command:hardwario-tower.locate_jlink}",
        "svdFile": "./sdk/sys/svd/stm32l0x3.svd",
        "MIMode": "gdb",
        "logging": {
            "engineLogging": true
        },
        "executable": "${workspaceFolder}\\out\\debug\\firmware.elf",
        "miDebuggerPath": "${command:hardwario-tower.locate_toolchain}",
        "serverLaunchTimeout": 10000,
        "windows": {
            "miDebuggerPath": "${command:hardwario-tower.locate_toolchain}.exe",
            "serverpath": "${command:hardwario-tower.locate_jlink}.exe"
        }
    }


Press Start Debugging in the HARDWARIO Extension command palette
================================================================
You can use this option if you don't want to worry about the launch.json or any other options mentioned before.
Just select the HARDWARIO logo on the side panel and select **Start Debugging** option.

.. thumbnail:: ../_static/firmware/hardwario-code/startDebugging.png
    :width: 40%
