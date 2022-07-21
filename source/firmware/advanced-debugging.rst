##################
Advanced Debugging
##################

.. important::
    This chapter is about debugging with `JLink <https://www.segger.com/products/debug-probes/j-link/>`_,
    if you don't have one you can always :doc:`debug with console printing <debugging>`.

If you have JLink probe, you can use our Visual Studio Code extension to debug your firmware with it.
You will need to install the extension first, for it we have a :doc:`special chapter in this documentation <hardwario-code-installation>`.

There is a little difference between installation with the Portable version and standalone extension.

*******************************
Debugging with Portable Version
*******************************

If you downloaded our Portable version of Visual Studio Code you should have all the required programs in the ``/data`` (Windows/Linux) or ``code-portable-data`` (macOS) folder.

The only thing that you will need to install are JLink drivers if you don't have them already.

Windows
*******

On Windows you can just go to ``hardwario-code/data/tower/toolchain/SEGGER/JLink/USBDriver/`` and run the ``InstDrivers.exe`` binary.
After that you should be good to go.

Linux
*****

On Linux you have to update the UDEV rules for the JLink to work.
Just copy the command below and replace **PATH_TO_HARDWARIO_CODE** with the actual path to the **harwdario-code** folder

``sudo cp PATH_TO_HARDWARIO_CODE/hardwario-code/data/tower/toolchain/SEGGER/JLink/99-jlink.rules /etc/udev/rules.d/99-jlink.rule``

You can unplug and plug the JLink and reboot your system after executing the command.
After that you should be able to start debugging with JLink.

macOS
*****

On macOS the JLink should be detected automatically so there is no additional steps needed.


**************************************
Debugging with Visual Studio extension
**************************************

If you did choose to use your own Visual Studio Code with our extension
installed you will have to follow `JLink installation <https://eclipse-embed-cdt.github.io/debug/jlink/install/>`_ for your system.

























