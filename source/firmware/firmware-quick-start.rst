####################
Firmware Quick Start
####################

You can easily edit or create your custom firmware for HARDWARIO TOWER Core Module on every major operating system

HARDARIO TOWER uses `PlatformIO <https://platformio.org>`_ for **building**, **uploading** and **debugging** firmware so it is easy for all the users.

.. important::

    This chapter assumes that you already have PlatformIO installed on you computer.
    If not please visit :doc:`PlatformIO installation <platformio-installation>`.

.. note::

    In the :doc:`next chapter in Firmware group <basic-overview>` you can find more details for each step explained here.

******************************************************
HARDWARIO TOWER with PlatformIO IDE (GUI installation)
******************************************************

.. |open-with-code| thumbnail:: ../_static/firmware/firmware-quick-start/open-vscode.png
        :width: 45%

.. |open-folder| thumbnail:: ../_static/firmware/firmware-quick-start/open-folder.png
        :width: 50%

#. (**OPTIONAL**) Create HARDWARIO folder where all your HARDWARIO projects will be located
#. Open VSCode
#. Open the Command Palette by pressing ``Ctrl + Shift + P`` or ``F1`` (``Cmd + Shift + P`` on Mac)
#. Type ``Git: Clone (Recursive)``, press Enter, paste following URL and hit Enter again

    .. code-block:: console

        https://github.com/hardwario/twr-skeleton.git

    .. thumbnail:: ../_static/firmware/firmware-quick-start/git-clone-recursive.png
        :width: 100%

    .. caution::

        Keep in mind the ``recursive`` option. If you don't include it, then you will not be able to build or flash the project

#. Open the twr-skeleton project in the VSCode by right clicking on the folder and selecting **Open with Code** (you have to enable this option while installing the VSCode) or by **Open folder** option in VSCode.

    .. tip::

        If you didn't close the VSCode after cloning you should be able to click open in the down right corner

    |open-with-code| |open-folder|

#. Connect the Core Module into the computer with USB cable and click the **Upload** button (arrow) at the bottom of the VSCode window

    .. tip::

        If you did some changes to the code, you don't have to click **Build** button every time,
        the **Upload** will detect the changes and compile all changed files before uploading to the device

.. attention::

    The Core Module is flashed. The red LED will turn on, when you press the button the LED toggles.

*********
Next step
*********
Now that you know that everything is set up correctly, you can start developing.

If you are not sure how to do that, keep your **twr-skeleton** project open and follow :doc:`another chapter <blank-start>`.


.. .. _linux-firmware:
..
.. ********************
.. |linux| Linux/Ubuntu
.. ********************
..
.. #. Install :ref:`GCC toolchain and tools <ubuntu-setup>`. Optionally install `VSCode IDE <https://code.visualstudio.com>`__.
.. #. Create a new project skeleton using :doc:`bcf <../tools/hardwario-firmware-flashing-tool>` by typing ``bcf create my_project``
.. #. Go to the new created folder by typing ``cd my_project``
.. #. Run VSCode by typing ``code .`` (note the dot ".") or open project folder in VSCode.
.. #. Build firmware by pressing ``Ctrl+Shift+B``
.. #. | Connect Core Module and flash the firmware by pressing ``Ctrl + P`` and typing ``task flash``.
..    | In the terminal window the flasher will ask for COM port, if you have just one, type zero ``0`` and press Enter
..
.. .. tip::
..
..     The Core Module is flashed. The red LED will turn on, when you press the button the LED toggles.
..
.. .. note::
..
..     You can continue by reading :doc:`Toolchain Guide <toolchain-guide>` chapter.
..
.. -------------------------------------------------------------------------------
..
.. .. _macos-firmware:
..
.. *************
.. |apple| macOS
.. *************
..
.. #. Install :ref:`GCC toolchain and tools <macos-setup>`. Optionally install `VSCode IDE <https://code.visualstudio.com>`__.
.. #. Create a new project skeleton using :doc:`bcf <../tools/hardwario-firmware-flashing-tool>` by typing ``bcf create my_project``
.. #. Go to the new created folder by typing ``cd my_project``
.. #. Run VSCode by typing ``code .`` (note the dot ".") or open project folder in VSCode.
.. #. Build firmware by pressing ``Ctrl+Shift+B``
.. #. | Connect Core Module and flash the firmware by pressing ``Ctrl + P`` and typing ``task flash``.
..    | In the terminal window the flasher will ask for COM port, if you have just one, type zero ``0`` and press Enter
..
.. .. tip::
..
..     The Core Module is flashed. The red LED will turn on, when you press the button the LED toggles.
..
.. .. note::
..
..     You can continue by reading :doc:`Toolchain Guide <toolchain-guide>` chapter.

