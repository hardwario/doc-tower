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
#. Type ``Git: Clone``, press Enter, paste following URL and hit Enter again

    .. code-block:: console

        https://github.com/hardwario/twr-skeleton.git

    .. thumbnail:: ../_static/firmware/firmware-quick-start/git-clone-recursive.png
        :width: 100%

    .. tip::

        You can also import the twr-skeleton by going into the PlatformIO extension in VSCode. In the extensions menu go to the

        ``Platforms -> Installed -> HARDWARIO TOWER - Industrial IoT Kit -> Examples -> twr-skeleton`` and then hit import.

        Your project will be opened after importing. It will put some numbers to the name, you can rename it later.

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

.. tip::

    You can get even more examples by going to the installed platform.
    How to get there is mentioned in the green tip bubble. You can find this tip in the third step of the list on this page.

    All the examples are verified and should work without issues.
