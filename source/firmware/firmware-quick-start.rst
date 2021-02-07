####################
Firmware Quick Start
####################

You can easily edit or create your custom firmware for HARDWARIO TOWER Core Module on:

.. * |windows| :ref:`Windows <windows-firmware>`
.. * |linux| :ref:`Linux <linux-firmware>`
.. * |apple| :ref:`macOS <macos-firmware>`

HARDARIO TOWER uses `PlatformIO <https://platformio.org>`_ for building, uploading and debugging firmware so it is easy for all the users.

.. important::
    This chapter will go over installation and setup for all major operating systems. The instalation is more or less the same for all the systems.
    In case something will be for some systems only, it will be mentioned.

.. note::

    In the :doc:`next chapter in Firmware group <basic-overview>` you can find more details for each step explained here.

.. _windows-firmware:

******************************************************
HARDWARIO TOWER with PlatformIO IDE (GUI installation)
******************************************************

.. |open-with-code| thumbnail:: ../_static/firmware/firmware-quick-start/open-vscode.png
        :width: 45%

.. |open-folder| thumbnail:: ../_static/firmware/firmware-quick-start/open-folder.png
        :width: 50%

#. Download and Install `VSCode IDE <https://code.visualstudio.com/>`__ for your operating system
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

#. Click on **Extensions** in the VSCode ``Ctrl + Shift + X`` (``Cmd + Shift + X`` on Mac)

    .. thumbnail:: ../_static/firmware/firmware-quick-start/vscode-extensions.png

#. Type ``PlatformIO`` into the search bar, select and install the **PlatformIO IDE** Extension

    .. caution::

        Be paitient and wait for the installation to complete. If you close the VSCode while the installation is in progress, PlatformIO might not work properly.

    .. thumbnail:: ../_static/firmware/firmware-quick-start/platformio-install.png

#. Reload the VSCode, you should get prompted in the lower right corner

#. Now you can **build, upload and debug** the firmware fast with the little buttons on the bottom of your VSCode editor

    .. thumbnail:: ../_static/firmware/firmware-quick-start/vscode-platformio-buttons.png

#. `Alternatively you can use the PlatfomIO button on the left side bar and use the Build, Upload and Monitor under env:debug -> General`

#. Connect the Core Module into the computer with USB cable and click the **Upload** button (arrow) at the bottom of the VSCode window

    .. tip::

        If you did some changes to the code, you don't have to click **Build** button every time,
        the **Upload** will detect the changes and compile all changed files before uploading to the device

.. attention::

    The Core Module is flashed. The red LED will turn on, when you press the button the LED toggles.

******************************************
HARDWARIO TOWER with PlatformIO Core (CLI)
******************************************

If you don't want or can't use the the GUI you can install the PlatformIO Core on its own.

You can visit the `instalation guide <https://docs.platformio.org/en/latest/core/installation.html#unix-and-unix-like>`_ to see how to do that.
Other than that it is pretty similar to the GUI. You will just use commands instead of the buttons.

Most commonly used commands are:

* ``pio run`` - this will build the code and check for errors
* ``pio run --target upload`` - this will build the code if there are changes and then upload it to the connected device
* ``pio device monitor`` - this will open the serial monitor and start to print out the messages from the connected device. For more information visit the :doc:`Debugging section <debugging>`

.. important::

    If you already installed the PlatformIO IDE you can just add the PlatformIO scripts to the PATH.
    You can visit :ref:`tips and tricks <tips-tricks>` on how to do that on your system.


.. _tips-tricks:

***************
Tips and Tricks
***************
.. tip::

    For more information about PlatformIO you can visit `their documentation <https://docs.platformio.org/en/latest/what-is-platformio.html>`_.

* Windows only |windows|

    *   | You might get the ``Write Timeout`` message at the Upload.
        | To prevent this and also make uploading a lot faster, you can `change the COM port Latency Timer to a lower value. <https://www.loadstarsensors.com/assets/manuals/html/how-to-set-latency-timer/latency-timer.html>`_
    *   | If you want to use the PlatformIO CLI, you can just add the folder ``C:\Users\YOUR_USER_NAME\.platformio\penv\Scripts`` to the PATH system variable. Just change ``YOUR_USER_NAME`` to your actual user name.
        | You can read about `how to make a change to the PATH variable in many articles. <https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/>`_
        | After the setup you should be able to use commands in normal Windows CMD. Use ``pio run`` for build and ``pio run --target upload`` for uploading code to the device.

* Unix and Unix-like only |linux|

    *   | If you want to use the PlatformIO CLI, you can just add the symlink to the PlatformIO scripts. Just run the following commands.

            .. code-block:: console

                ln -s ~/.platformio/penv/bin/platformio /usr/local/bin/platformio
                ln -s ~/.platformio/penv/bin/pio /usr/local/bin/pio
                ln -s ~/.platformio/penv/bin/piodebuggdb /usr/local/bin/piodebuggdb

            .. caution::

                If you are not logged in as a root you will have to add the ``sudo`` to the beginning of each command.

        | After the setup you should be able to use commands in your terminal. Use ``pio run`` for build and ``pio run --target upload`` for uploading code to the device.


* There is a little annoying "feature" that every time you open the PlatformIO project you will get the PIO Home screen popup, you can easily disable it by unchecking the box ``Show at startup``.

  .. thumbnail:: ../_static/firmware/firmware-quick-start/tips-and-tricks.png
    :width: 100%



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

