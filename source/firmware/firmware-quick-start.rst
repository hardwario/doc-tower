####################
Firmware Quick Start
####################

You can easily edit or create your custom firmware for HARDWARIO Core Module on :ref:`Windows <windows-firmware>`, :ref:`Linux <linux-firmware>` or :ref:`macOS <macos-firmware>`.

.. note::

    In the :doc:`next chapters in Firmware group <basic-overview>` you can find more details for each step explained here.

.. _windows-firmware:

*******
Windows
*******

#. Download and Install `VSCode IDE <https://code.visualstudio.com/>`__ first
#. Download and Install `HARDWARIO Toolchain <https://github.com/hardwario/bch-toolchain-windows/releases>`_,  keep the default install options if in doubt (:ref:`details <windows-setup>`)
#. Create HARDWARIO folder where all your HARDWARIO projects will be located and right-click on that folder and choose Open with Toolchain
#. Create a new project skeleton using bcf by typing ``bcf create my_project``
#. Go to the new created folder by typing ``cd my_project``
#. Run VSCode by typing ``code .`` (note the dot ".")
#. | Build firmware by pressing ``Ctrl+Shift+B``, VSCode may ask in the bottom right corner if you would like to use different Shell.
   | Confirm that and try to build project again.
#. | Connect Core Module and flash the firmware by pressing ``Ctrl + P`` and typing ``task flash``.
   | In the terminal window the flasher will ask for COM port, if you have just one, type zero ``0`` and press Enter

.. tip::

    The Core Module is flashed. The red LED will turn on, when you press the button the LED toggles.

.. note::

    You can also follow a detailed Windows toolchain installation guide and :doc:`Toolchain Guide <toolchain-guide>` chapter.

**Detailed explanation**

If you install HARDWARIO Toolchain with default options, then the compiler and make tool will not be added to the ``PATH`` environment variable,
but only in the HARDWARIO Toolchain Console.
That's why you have to run VSCode from the Toolchain command line so the VSCode will know where to look for ``make`` and ``bcf`` tool.

You can upgrade any Windows command line to HARDWARIO Toolchain command line by typing ``bct``.

If you you check all the options during installation of the HARDWARIO Toolchain,
then the paths of the installed tools is added to ``PATH`` environment variable.
Then you can open the VSCode from start menu and it will know how to compile and
flash because ``make`` and ``bcf`` will be also available in the default Windows command line.

.. important::

    VSCode now uses PowerShell, that's why you have to confirm that you would like to use normal Windows command line.

.. _linux-firmware:

************
Linux/Ubuntu
************

#. Install :ref:`GCC toolchain and tools <ubuntu-setup>`. Optionally install `VSCode IDE <https://code.visualstudio.com>`__.
#. Create a new project skeleton using :doc:`bcf <../tools/hardwario-firmware-flashing-tool>` by typing ``bcf create my_project``
#. Go to the new created folder by typing ``cd my_project``
#. Run VSCode by typing ``code .`` (note the dot ".") or open project folder in VSCode.
#. Build firmware by pressing ``Ctrl+Shift+B``
#. | Connect Core Module and flash the firmware by pressing ``Ctrl + P`` and typing ``task flash``.
   | In the terminal window the flasher will ask for COM port, if you have just one, type zero ``0`` and press Enter

.. tip::

    The Core Module is flashed. The red LED will turn on, when you press the button the LED toggles.

.. note::

    You can continue by reading :doc:`Toolchain Guide <toolchain-guide>` chapter.

.. _macos-firmware:

*****
macOS
*****

#. Install :ref:`GCC toolchain and tools <macos-setup>`. Optionally install `VSCode IDE <https://code.visualstudio.com>`__.
#. Create a new project skeleton using :doc:`bcf <../tools/hardwario-firmware-flashing-tool>` by typing ``bcf create my_project``
#. Go to the new created folder by typing ``cd my_project``
#. Run VSCode by typing ``code .`` (note the dot ".") or open project folder in VSCode.
#. Build firmware by pressing ``Ctrl+Shift+B``
#. | Connect Core Module and flash the firmware by pressing ``Ctrl + P`` and typing ``task flash``.
   | In the terminal window the flasher will ask for COM port, if you have just one, type zero ``0`` and press Enter

.. tip::

    The Core Module is flashed. The red LED will turn on, when you press the button the LED toggles.

.. note::

    You can continue by reading :doc:`Toolchain Guide <toolchain-guide>` chapter.

