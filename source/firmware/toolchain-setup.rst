###############
Toolchain Setup
###############

In this document we will describe the installation of tools for working with firmware - the firmware toolchain.
The toolchain is designed to allow the firmware operations on all the supported operating systems using a command line in a **uniform manner**.

.. note::

    Orientation on a command line interface has the advantage to build your firmware automatically on server, e.g. on commit to GitHub via
    Travis CI continuous integration service.

The firmware toolchain consists of several fundamental components:

- Compiler **GCC ARM Embedded**
- Version control system **Git**
- Interpret for scripting language **Python 3**
- DFU upload utility **dfu-util**
- Program **HARDWARIO Firmware Tool**

At the end of the article, we'll show how to develop and compile firmware with popular editors like **Atom** or **Visual Studio Code**.

To install, go to one of the supported platforms:

- :ref:`Setup on Windows <windows-setup>`
- :ref:`Setup on macOS <macos-setup>`
- :ref:`Setup on Ubuntu <ubuntu-setup>`
- :ref:`Setup on Generic Linux <linux-setup>`

To upgrade an existing installation, go to one of the supported platforms:

- :ref:`Update on Windows <windows-update>`
- :ref:`Update on macOS <macos-update>`
- :ref:`Update on Ubuntu <ubuntu-update>`
- :ref:`Update on Generic Linux <linux-update>`

.. _windows-setup:

****************
Setup on Windows
****************

.. caution::

    You will need **administrator** rights to install.

Download the current version of the HARDWARIO Toolchain Windows installer
*************************************************************************

`Releases on GitHub <https://github.com/hardwario/bch-toolchain-windows/releases>`_

Launch the downloaded installer and choose the destination directory
********************************************************************

.. thumbnail:: ../_static/firmware/toolchain-setup/windows-location.png
   :width: 40%
   :alt: Windows location


Now you can adjust the desired Path environment variable (we recommend to leave the default settings if in doubt) and proceed with the installation
***************************************************************************************************************************************************

.. thumbnail:: ../_static/firmware/toolchain-setup/setup-windows-paths.png
   :width: 40%
   :alt: Windows PATH

The FTDI driver setup will launch automatically during the installation - install it
************************************************************************************

.. thumbnail:: ../_static/firmware/toolchain-setup/setup-windows-ftdi.png
   :width: 40%
   :alt: FTDI

After finishing the installation, launch the HARDWARIO Toolchain using one these 3 ways
***************************************************************************************

- From the **Desktop**
- From the **Start menu**
- From the **context menu** on the selected directory (using a right-click)

.. tip::

    The advantage of the context menu is to open the HARDWARIO Toolchain directly in the directory location you need to work with.

.. thumbnail:: ../_static/firmware/toolchain-setup/setup-windows-toolchain.png
   :width: 60%
   :alt: CMD Toolchain


Continue on the document :doc:`Toolchain Guide <toolchain-guide>`. You may also try
***********************************************************************************

- :ref:`Integration with Visual Studio Code <visual-studio-integration>`

.. _windows-update:

*****************
Update on Windows
*****************

- Download and install the new version according to the chapter :ref:`Setup on Windows <windows-setup>`.

********************
Uninstall on Windows
********************

Uninstall **Apps & features**:

.. thumbnail:: ../_static/firmware/toolchain-setup/setup-windows-uninstall.png
   :width: 60%
   :alt: Windows Uninstall

.. _macos-setup:

**************
Setup on macOS
**************

.. warning::

    The following procedure has been tested on **macOS 10.12.**

Open the Terminal application
*****************************

Install `Homebrew <https://brew.sh>`_ (unless you already have it)
******************************************************************

.. note::

    Homebrew is the package management system and the ecosystem of packages for macOS.

Install GCC ARM Embedded
************************

.. code-block:: console

    brew tap armmbed/formulae

.. code-block:: console

    brew install armmbed/formulae/arm-none-eabi-gcc

Install Git
***********

.. code-block:: console

    brew install git

Install dfu-util
****************

.. code-block:: console

    brew install dfu-util

Install Python 3
****************

.. code-block:: console

    brew install python3

Update pip (Python Package Manager) to the latest version
*********************************************************

.. code-block:: console

    sudo pip3 install --upgrade --no-cache-dir pip

Install HARDWARIO Firmware Tool
*******************************

.. code-block:: console

    sudo pip3 install --upgrade --no-cache-dir bcf

Continue on the document :doc:`Toolchain Guide <toolchain-guide>`. You may also try
***********************************************************************************

- :ref:`Integration with Visual Studio Code <visual-studio-integration>`

.. _macos-update:

***************
Update on macOS
***************

Update of packages
******************

.. code-block:: console

    brew update && brew upgrade

HARDWARIO Firmware tool update
******************************

.. code-block:: console

    sudo pip3 install --upgrade --no-cache-dir bcf

.. _ubuntu-setup:

***************
Setup on Ubuntu
***************

.. warning::

    The following procedure has been tested on **Ubuntu 20.04 LTS.**

Open the Terminal application
*****************************

Download libisl15 library
*************************

.. code-block:: console

    wget http://mirrors.kernel.org/ubuntu/pool/main/i/isl/libisl15_0.16.1-1_amd64.deb

Install libisl15 library
************************

.. code-block:: console

    sudo dpkg -i libisl15_0.16.1-1_amd64.deb

Add team-gcc-arm-embedded-ubuntu repository to source list
**********************************************************

.. code-block:: console

    echo "deb http://ppa.launchpad.net/team-gcc-arm-embedded/ppa/ubuntu bionic main" | sudo tee /etc/apt/sources.list.d/team-gcc-arm-embedded-ubuntu-ppa-eoan.list

Update the index of the available packages
******************************************

.. code-block:: console

    sudo apt update

Install common software properties
**********************************

.. code-block:: console

    sudo apt-get install software-properties-common

Install compiler & necessary tools
**********************************

.. code-block:: console

    sudo apt install gcc-arm-embedded git dfu-util python3 python3-pip python3-setuptools

Update pip (Python Package Manager) to the latest version
*********************************************************

.. code-block:: console

    sudo pip3 install --upgrade --no-cache-dir pip

Install HARDWARIO Firmware Tool
*******************************

.. code-block:: console

    sudo pip3 install --upgrade --no-cache-dir --ignore-installed bcf

Add user to dialout group
*************************

.. code-block:: console

    sudo adduser $USER dialout

Continue on the document :doc:`Toolchain Guide <toolchain-guide>`. You may also try
************************************************************************************

- :ref:`Integration with Visual Studio Code <visual-studio-integration>`

.. _ubuntu-update:

****************
Update on Ubuntu
****************

Update of packages
******************

.. code-block:: console

    sudo apt update && sudo apt upgrade

HARDWARIO Firmware tool update
******************************

.. code-block:: console

    sudo pip3 install --upgrade --no-cache-dir bcf

.. _linux-setup:

**********************
Setup on Generic Linux
**********************

If you have other Linux distribution or unsupported Ubuntu version, we recommend to use official
*GNU Embedded Toolchain for ARM* from `developer.arm.com <https://developer.arm.com/>`_ pages. This package is validated by ARM and tested by us.

Go to `ARM website <https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads>`_ and download Linux 64-bit package
******************************************************************************************************************************

Extract package to filesystem, e.g. into ``/opt`` folder (available for all users, you will need root privileges) or into ``~/.local/opt`` folder (available only for you)
**************************************************************************************************************************************************************************

**Step 1: /opt version**

.. code-block:: console
    :linenos:

    cd <folder with package> # go to folder with downloaded file
    sudo cp gcc-arm-none-eabi-6-*-update-linux.tar.bz2 /opt  # copy to destination folder
    cd /opt  # go there
    sudo tar xjf gcc-arm-none-eabi-6-*-update-linux.tar.bz2  # unpack file

**Step 2: ~/.local/opt version**

.. code-block:: console
    :linenos:

    mkdir -p ~/.local/opt  # create folder
    cd <folder with package> # go to folder with downloaded file
    cp gcc-arm-none-eabi-6-*-update-linux.tar.bz2 ~/.local/opt  # copy to destination folder
    cd ~/.local/opt  # go there
    tar xjf gcc-arm-none-eabi-6-*-update-linux.tar.bz2  # unpack file

Create a symbolic link ``gcc-arm-none-eabi-6``
**********************************************

.. code-block:: console

    sudo ln -s gcc-arm-none-eabi-6-<version>-update gcc-arm-none-eabi-6  # where <version> could be: 2017-q2

Update ``PATH`` variable so you can use arm-none-eabi-* binaries directly
*************************************************************************

.. code-block:: console
    :linenos:

    cd  # go to user home folder
    # use your favorite editor and edit ".profile" file
    # find line with PATH variable. e.g.:

        export PATH="$PATH:/…"

.. caution::

    Please note that three dots (…) represents some text there.

.. code-block:: console
    :linenos:

    # and add to your path to the end (/opt version):

    export PATH="$PATH:/…:/opt/gcc-arm-none-eabi-6/bin"

    # or (~/.local/opt version)

    export PATH="$PATH:/…:~/.local/opt/gcc-arm-none-eabi-6/bin"

    # if there is no PATH line, add it

    export PATH="$PATH:/opt/gcc-arm-none-eabi-6/bin"

    # or

    export PATH="$PATH:~/.local/opt/gcc-arm-none-eabi-6/bin"

Use your distribution package manager and install
*************************************************

- **Git**
- **Python 3**
- **dfu-util**

Install HARDWARIO Firmware Tool
*******************************

.. code-block:: console

    sudo pip3 install --upgrade --no-cache-dir bcf

Continue on the document :doc:`Toolchain Guide <toolchain-guide>`. You may also try
***********************************************************************************

- :ref:`Integration with Visual Studio Code <visual-studio-integration>`

.. _linux-update:

***********************
Update on Generic Linux
***********************

Update Toolchain
****************

- Download updated **Linux 64-bit** package from https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads
- Extract it into proper folder (``/opt``, ``~/.local/opt`` or other)
- Update symbolic link

.. code-block:: console

    sudo ln -sf gcc-arm-none-eabi-6-<version>-update gcc-arm-none-eabi-6  # where <version> could be: 2017-q2

or

.. code-block:: console

    ln -sf gcc-arm-none-eabi-6-<version>-update gcc-arm-none-eabi-6  # where <version> could be: 2017-q2

Update packages
***************

- Use your distribution package manager
- HARDWARIO Firmware tool update:

.. code-block:: console

    sudo pip3 install --upgrade bcf

.. _visual-studio-integration:

***********************************
Integration with Visual Studio Code
***********************************

Every HARDWARIO project contains ``.vscode`` configuration folder
so you just open the project folder in **Visual Studio Code** and you're ready to go.

We also suggest to install `C/C++ Intellisense and debug extentsion from Microsoft <https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools>`_.

In file ``.vscode/tasks.json`` there are some tasks which you can run by pressing ``Ctrl+P`` and typing ``task``.

+--------+-----------------------------------------------------------+
| Task   | Description                                               |
+========+===========================================================+
| build  | Build active project                                      |
+--------+-----------------------------------------------------------+
| clean  | Clean active project                                      |
+--------+-----------------------------------------------------------+
| dfu    | Flash compiled firmware with dfu-util to the Core Module  |
+--------+-----------------------------------------------------------+
| ozone  | Run Ozone debugger which can be used with J-Link debugger |
+--------+-----------------------------------------------------------+
| update | Update SDK folder/submodule to the latest version         |
+--------+-----------------------------------------------------------+

.. tip::

    Project make file allows quicker parallel compilation.
    This can be set in ``.vscode/tasks.json`` where you set ``"args": ["-j4"]``,
    parameter, where the number 4 is the number of your CPU cores.

********************************
Integration with J-Link debugger
********************************

To debug the running code on Core Module you can use Ozone debugger with J-Link debug probe.
It is also possible to use GDB/OpenOCD with other debug probes but this is not documented yet.

Download the `Ozone debugger <https://www.segger.com/downloads/jlink#Ozone>`_.

.. note::

    **For Windows users**: Ozone folder also needs to be set in ``PATH`` environment
    variable or you can simply edit ``Makefile`` and set absolute path to the ``Ozone.exe`` file.
    It is also possible to open project directly in **Ozone**, please see the options below.

How to start debugging the project:

- In the **command line** by typing ``make ozone``
- In **Visual Studio Code** by pressing ``F5`` or ``Ctrl+P`` and typing ``task ozone``
- In **Ozone** by loading project configuration file ``sdk/tools/ozone/ozone.jdebug``.
