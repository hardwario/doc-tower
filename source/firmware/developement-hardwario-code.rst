################################
Developement with HARDWARIO Code
################################

.. attention::
    The extension is still in development and you might experience some issues with it. If you do, please let us know on `our forum <https://forum.hardwario.com>`_
    or directly on `GitHub <https://github.com/hardwario/hardwario-tower-vscode-extension/issues>`_.

There are two ways how to develop with the new extension. You can use your own Visual Studio Code and install the extension into it
or you can download the portable version of Visual Studio Code.

***********************************************
HARDWARIO Tower extension to Visual Studio Code
***********************************************

For the extension to work with the standalone version of Visual Studio Code, you will need to install the extension and set up the environment of your PC.

Installation
************
To install the extension you will have to download the latest release from `GitHub Releases <https://github.com/hardwario/hardwario-tower-vscode-extension/releases>`_.

To install the downloaded .vsix extension file just go to the **Extensions tab**, click the **three dots** and **Install from VSIX.\.\.**

.. |install-extension| thumbnail:: ../_static/firmware/hardwario-code/InstallGuide.png
    :width: 50%

Additional setup
****************

You will need some dependencies for the extension to work as intended:

- **make** - for compiling the firmware
- **python** - our flashing and logging tool is made in python
- **bcf** - our flashing and logging tool made in pythonK
- **arm-none-eabi-gcc**
- **git** - for cloning submodules and firmwares
- **Linux commands** - you will need commands like rm and mkdir

You have to have all these things in the PATH for the extension to register it. If you don't have these already, you can download the HARDWARIO Code portable version and
you will find all the needed tools in the /data/tower/ folder. You will just have to add the correct folders to PATH.

Folders to add to PATH (Windows):

- python/
- python/Scripts/
- toolchain/make/bin/
- toolchain/gcc/bin/
- toolchain/gcc/arm-none-eabi/bin/
- toolchain/git/cmd/
- toolchain/git/usr/bin/
- toolchain/git/mingw64/bin

.. note::
    If you are using a Linux version you will have to install git and add it to PATH, we are not using portable version for Linux.

.. tip::
    You can now start using the Visual Studio Code for developing HARDWARIO Tower Firmware.
    To get some basic information on how to use the extension visit :doc:`HARWARIO Code tutorial <hardwario-code-tutorial>`.

**************************************
Portable version of Visual Studio Code
**************************************

There is a possibility to use the whole Visual Studio Code on its own.

This approach is good if you want to start developing quickly without setting up the environment.

You will have to do just a few simple steps:

- Download HARDWARIO Code
- Unpack the ZIP wherever you want
- Run the Code.exe (Windows) or code (Linux)
- You should see HARDWARIO Logo on the side panel

.. tip::
    You can now start using the Visual Studio Code for developing HARDWARIO Tower Firmware.
    To get some basic information on how to use the extension visit :doc:`HARWARIO Code tutorial <hardwario-code-tutorial>`.

***************
Firmware update
***************

In this stat you might encounter the warning that you are using a deprecated firmware version. You will get a warning on the bottom right corner.
In this case just click the Update button on the warning message and after a while the firmware should be updated and ready to use.

.. tip::
    After the update you should reload the window for everything to work correctly.

If you encounter problems with compiling and uploading the firmware you can check these things:

- there is a **sdk** folder present and filled
- Makefile in sdk folder has this line at the beggining: ``APP_DIR ?= src``
- Makefile in the root folder looks something like this:

.. code-block:: none

    SDK_DIR ?= sdk
    VERSION ?= vdev

    CFLAGS += -D'VERSION="${VERSION}"'

    -include sdk/Makefile.mk

    .PHONY: all
    all: debug

    .PHONY: sdk
    sdk: sdk/Makefile.mk

    .PHONY: update
    update:
        @git submodule update --remote --merge sdk

    sdk/Makefile.mk:
        @git submodule update --init sdk


