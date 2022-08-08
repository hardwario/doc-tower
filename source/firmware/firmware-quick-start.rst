####################
Firmware Quick Start
####################

.. attention::

    This document assumes that you already have portable :ref:`HARDWARIO Code <portable-hardwario-code>` or :ref:`HARDWARIO TOWER extension <hardwario-tower-extension>` installed on you computer.


You can easily edit or create your custom firmware for HARDWARIO TOWER Core Module on every major operating system

****************************************************
Getting your first HARDWARIO TOWER firmware skeleton
****************************************************


.. tip::
    If you are returning to the project use **Open folder** option in VSCode. Go to the ``File -> Open Folder...`` or use ``Ctrl + K`` then ``Ctrl + O``


#. Open VSCode and the HARDWARIO icon on the left side bar

    .. thumbnail:: ../_static/firmware/firmware-quick-start/hardwario-extension-icon.png
        :width: 40%

#. In the section **Start New TOWER Firmware** select ``From Skeleton Project...``

    .. thumbnail:: ../_static/firmware/firmware-quick-start/from-skeleton-project.png
        :width: 40%

#. Select **folder** where the new firmware project folder should be created
#. You will be prompted to name the folder, default **twr-skeleton** is just fine for now
#. Wait for the firmware to download
#. Visual Studio Code will reopen with the new firmware opened
#. Connect the Core Module into the computer with USB cable and click the **Flash firmware** button ``↑`` at the blue bar on the bottom of the VSCode window
#. The Core Module is flashed. The red LED will turn on, when you press the button the LED toggles

.. tip::

    If you did some changes to the code in the ``src/application.c`` you don't have to click **Build** button every time,
    the **Upload** button will detect the changes and compile all changed files before uploading to the device.




*********
Next step
*********
Now that you know that everything is set up correctly, you can start developing.

If you are not sure how to do that, keep your **twr-skeleton** project open and go to see how to work with your :doc:`First firmware <blank-start>`.

.. tip::

    You can get even more examples clicking on ``From Existing Project...`` in the second step and selecting the firmware that you like.
