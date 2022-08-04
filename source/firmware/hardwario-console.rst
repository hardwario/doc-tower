#################
HARDWARIO Console
#################

.. note::
    This tutorial expects that you have a running Visual Studio Code with our HARDWARIO TOWER extension installed.
    If you don't please visit the :doc:`Installation guide <hardwario-code-installation>`.

For logging with the HARDWARIO TOWER Visual Studio Code extension there is an available tab in the bottom panel of Visual Studio Code.

.. thumbnail:: ../_static/firmware/debugging/hardwario-console-prewiev.png
    :width: 100%

In this console there will be some logs displayed from your connected device.

For the firmware to print something to this console you will have to include some log messages in it.
You can read more about that in :doc:`Debugging chapter <debugging>`.

There are several buttons on the right side if you open the HARDWARIO TOWER Console. They will be listed from left to right:

.. thumbnail:: ../_static/firmware/debugging/console-buttons.png
    :width: 25%

- **Clear console** - this will just clear all the log messages that you received.
- **Connect/Disconnect console** - this will attach console to the device that is selected on the bottom panel. If the console is already attached it will disconnect it. You don't have to use this button if you are using extension commands :ref:`Build + Flash (Console) <build-flash-console>` or :ref:`Attach console <attach-console>`.

    .. tip::
        You can read more about mentioned commands in :doc:`HARDWARIO CODE tutorial <hardwario-code-tutorial>`.
- **Scrool to bottom** - by default the console will scroll automatically with the messages. If you scroll to view some message autoscrool will turn off. To start it again, just click this button.
- **Save Log** - this will save the displayed log.
- **Allow Input** - this will allow to send input to the device. Usable for AT commands.
- **Maximize window** - this will make the console bigger. It is a standard Visual Studio Code button available on most panels.
- **Close panel** - this will close the whole panel, not just HARDWARIO TOWER Console.
