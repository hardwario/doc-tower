###########################
HARDWARIO Code Installation
###########################

.. attention::
    The extension is still in development and you might experience some issues with it. If you do, please let us know on `our forum <https://forum.hardwario.com>`_
    or directly on `GitHub <https://github.com/hardwario/hardwario-tower-vscode-extension/issues>`_.

There are two ways how to develop with the new extension. You can use your :ref:`own Visual Studio Code and install the extension <hardwario-tower-extension>` into it
or you can download the :ref:`portable version of Visual Studio Code <portable-hardwario-code>`.

.. _portable-hardwario-code:

**************************************
Portable version of Visual Studio Code
**************************************

There is a possibility to use the whole Visual Studio Code on its own.

This approach is good if you want to start developing quickly without setting up the environment.

You will have to do just a few simple steps based on your operating system.

Linux
*****

- Download `HARDWARIO Code <https://drive.google.com/drive/u/3/folders/1gC91vzSR0O1RONRX6LMJ8_ug1_UOikpt>`_
- Unpack the archive wherever you want
- Run the **code** binary
- You should see HARDWARIO Logo on the side panel

.. warning::
    If you don't have a **git** installed on your system, you will have to `install it <https://github.com/git-guides/install-git#install-git-on-linux>`_ for the extension to work fully.

.. tip::
    You can now start using the Visual Studio Code for developing HARDWARIO TOWER Firmware.
    To get some basic information on how to use the extension visit :doc:`HARWARIO Code tutorial <hardwario-code-tutorial>`
    or you can go straight to the :doc:`Firmware Quick Start chapter <firmware-quick-start>`.

Windows
*******

- Download `HARDWARIO Code <https://drive.google.com/drive/u/3/folders/1gC91vzSR0O1RONRX6LMJ8_ug1_UOikpt>`_
- Unpack the archive wherever you want
- Run the **Code.exe**
- You should see HARDWARIO Logo on the side panel

.. tip::
    You can now start using the Visual Studio Code for developing HARDWARIO TOWER Firmware.
    To get some basic information on how to use the extension visit :doc:`HARWARIO Code tutorial <hardwario-code-tutorial>`
    or you can go straight to the :doc:`Firmware Quick Start chapter <firmware-quick-start>`.

OSX
***

- Download `HARDWARIO Code installation package <https://drive.google.com/drive/u/3/folders/1gC91vzSR0O1RONRX6LMJ8_ug1_UOikpt>`_ for macOS
- Run the installer by double clicking it
- Follow the installer instruction
- You should see a HARDWARIO_Code folder in your Applications folder
- Run ``HARDWARIO_Code/hardwario-code/Visual Studio Code``
- You should see HARDWARIO Logo on the side panel

.. tip::
    You can now start using the Visual Studio Code for developing HARDWARIO TOWER Firmware.
    To get some basic information on how to use the extension visit :doc:`HARWARIO Code tutorial <hardwario-code-tutorial>`
    or you can go straight to the :doc:`Firmware Quick Start chapter <firmware-quick-start>`.

.. _hardwario-tower-extension:

***********************************************
HARDWARIO TOWER extension to Visual Studio Code
***********************************************

For the extension to work with the standalone version of Visual Studio Code, you will need to install the extension and set up the environment of your PC.

Installation
************
To install the extension you will have to download the latest release from `GitHub Releases <https://github.com/hardwario/hardwario-tower-vscode-extension/releases>`_.

To install the downloaded .vsix extension file just go to the **Extensions tab**, click the **three dots** and **Install from VSIX.\.\.**

.. thumbnail:: ../_static/firmware/hardwario-code/InstallGuide.png
    :width: 70%

Additional setup
****************

You will need some dependencies for the extension to work as intended:

- **cmake**

    - `Installation for all systems <https://cmake.org/install/>`_

- **ninja** - used build system

    - `Installation for all systems <https://github.com/ninja-build/ninja/releases>`_


- **arm-none-eabi-gcc**

    - `Windows installation arm-none-eabi-gcc <https://mynewt.apache.org/latest/get_started/native_install/cross_tools.html#installing-the-arm-toolchain-for-windows>`_
    - `Linux installation arm-none-eabi-gcc <https://mynewt.apache.org/latest/get_started/native_install/cross_tools.html#installing-the-arm-toolchain-for-linux>`_
    - `macOS installation arm-none-eabi-gcc <https://mynewt.apache.org/latest/get_started/native_install/cross_tools.html#installing-the-arm-toolchain-for-mac-os-x>`_

- **git** - for cloning submodules and firmwares

    - `All installations for git <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_


- **Linux commands** - you will need commands like ``rm`` and ``mkdir`` (*Windows only*)

    - You have to install git to your machine and then add the ``\usr\bin\`` folder to PATH. The folder path should look something like ``C:\Program Files\Git\usr\bin\``

- **make** - for compiling the firmware (LEGACY)

    - `Windows installation make <https://www.technewstoday.com/install-and-use-make-in-windows/>`_
    - `Linux installation make <https://linuxhint.com/install-make-ubuntu/>`_
    - `macOS installation make <https://formulae.brew.sh/formula/make>`_

.. tip::
    The extension will warn you that you are missing some of those and provide you with a corresponding link.

You have to have all these things in the PATH for the extension to register it. If you don't have these already, you can download the `HARDWARIO Code portable version <https://drive.google.com/drive/u/3/folders/1gC91vzSR0O1RONRX6LMJ8_ug1_UOikpt>`_ and
you will find all the needed tools in the ``/data/tower/`` folder. You will just have to add the correct folders to PATH.

Folders to add to PATH:

- ``toolchain/make/bin/``
- ``toolchain/gcc/bin/``
- ``toolchain/gcc/arm-none-eabi/bin/``
- ``toolchain/git/cmd/``
- ``toolchain/git/usr/bin/``
- ``toolchain/git/mingw64/bin``

.. note::
    If you are using a Linux version you will have to install git, we are not using portable version of git for Linux.

.. tip::
    You can now start using the Visual Studio Code for developing HARDWARIO TOWER Firmware.
    To get some basic information on how to use the extension visit :doc:`HARWARIO Code tutorial <hardwario-code-tutorial>`
    or you can go straight to the :doc:`Firmware Quick Start chapter <firmware-quick-start>`.


****************
Firmware upgrade
****************

.. important::
    This feature makes it possible to upgrade the project from PlatformIO project to the new HARDWARIO Code project structure.

In the start you might encounter the warning that you are using a deprecated firmware version. You will get a warning on the bottom right corner.
In this case just click the Upgrade button on the warning message and after a while the firmware should be upgraded and ready to use.

You can also use ``Upgrade Firmware Project`` button in the extension side panel if you missed the warning message.

.. thumbnail:: ../_static/firmware/hardwario-code/upgradeFirmware.png
    :width: 40%

.. tip::
    After the upgrade you should reload the window for everything to work correctly.

If you encounter problems with compiling and uploading the firmware you can check these things:

- there is a **sdk** folder present and filled
- There should be a CMakeLists.txt in the `root` folder and in the `src` folder
- You can check if all the \*.c files are listed in the src/CMakeLists.txt on the first line

