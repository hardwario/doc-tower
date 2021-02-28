####################
Firmware Quick Start
####################

You can easily edit or create your custom firmware for HARDWARIO TOWER Core Module on every major operating system

HARDARIO TOWER uses `PlatformIO <https://platformio.org>`_ for **building**, **uploading** and **debugging** firmware so it is easy for all the users.

****************************************************
Getting your first HARDWARIO TOWER firmware skeleton
****************************************************

.. |open-with-code| thumbnail:: ../_static/firmware/firmware-quick-start/open-vscode.png
        :width: 45%

.. |open-folder| thumbnail:: ../_static/firmware/firmware-quick-start/open-folder.png
        :width: 50%

.. important::

    This chapter assumes that you already have PlatformIO installed on you computer.
    If not please visit :doc:`PlatformIO installation <platformio-installation>`.

#. Open VSCode
#. Open the Command Palette by pressing ``Ctrl + Shift + P`` or ``F1`` (``Cmd + Shift + P`` on Mac)
#. Type ``Git: Clone (Recursive)``, press Enter, paste following URL and hit Enter again

    .. code-block:: console

        https://github.com/hardwario/twr-skeleton.git

    .. thumbnail:: ../_static/firmware/firmware-quick-start/git-clone-recursive.png
        :width: 100%

    .. caution::

        Keep in mind the ``recursive`` option. If you don't include it, then you will not be able to build or flash the project

#. | Click open in the down right corner of VSCode after the cloning is done
   | If you are returning to the project use **Open folder** option in VSCode.

    |open-with-code| |open-folder|

#. Connect the Core Module into the computer with USB cable and click the **Upload** button (arrow) at the bottom of the VSCode window

    .. tip::

        If you did some changes to the code, you don't have to click **Build** button every time,
        the **Upload** button will detect the changes and compile all changed files before uploading to the device.

.. attention::

    The Core Module is flashed. The red LED will turn on, when you press the button the LED toggles.

*********
Next step
*********
Now that you know that everything is set up correctly, you can start developing.

If you are not sure how to do that, keep your **twr-skeleton** project open and go to see how to work with your :doc:`First firmware <blank-start>`.

