#######################
PlatformIO Installation
#######################

.. attention::
    We are migrating to our own **Visual Studio Code extension** and a portable version of Visual Studio Code. For more information on how to install and use it visit
    :doc:`Developement with HARDWARIO Code <hardwario-code-installation>`.

If you want to create your custom firmware or update some existing one to your needs you will need to install PlatformIO.

.. tip::

    If you want to upload some existing firmware without changes to the Core Module,
    it is advised to use :doc:`HARDWARIO Playground <../basics/hardwario-playground>`.

.. important::

    This chapter will go over installation and setup for all major operating systems. The instalation is more or less the same for all the systems.
    In case something will be for some systems only, it will be mentioned.

******************************************************
HARDWARIO TOWER with PlatformIO IDE (GUI installation)
******************************************************

#. Download and Install `VSCode IDE <https://code.visualstudio.com/>`__ for your operating system
#. Open VSCode
#. Click on **Extensions** or press ``Ctrl + Shift + X`` (``Cmd + Shift + X`` on Mac)

    .. thumbnail:: ../_static/firmware/firmware-quick-start/vscode-extensions.png

#. Type ``PlatformIO`` into the search bar, select and install the **PlatformIO IDE** Extension

    .. caution::

        Be paitient and wait for the installation to complete. If you close the VSCode while the installation is in progress, PlatformIO might not work properly.

    .. thumbnail:: ../_static/firmware/firmware-quick-start/platformio-install.png

#. Reload the VSCode, you should get prompted in the lower right-hand corner
#. Now you can **build, upload and debug** the firmware fast with the little buttons on the bottom of your VSCode editor

    .. thumbnail:: ../_static/firmware/firmware-quick-start/vscode-platformio-buttons.png

.. tip::

    After these few steps you can follow the :doc:`next chapter <firmware-quick-start>` and start creating your firmware.

---------------------------------------------------------------------------------------------------

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

* There is an alternative way to execute the PlatformIO commands. You can use the PlatfomIO button on the left side bar and use the Build, Upload and Monitor under env:debug -> General


* There is a little annoying "feature" that every time you open the PlatformIO project you will get the PIO Home screen popup, you can easily disable it by unchecking the box ``Show at startup``.

  .. thumbnail:: ../_static/firmware/firmware-quick-start/tips-and-tricks.png
    :width: 100%
