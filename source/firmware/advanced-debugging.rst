##################
Advanced Debugging
##################

.. important::
    This chapter is about debugging with `JLink <https://www.segger.com/products/debug-probes/j-link/>`_,
    if you don't have one you can always :doc:`debug with console printing <debugging>`.

If you have JLing probe, you can use our Visual Studio Code extension to debug your firmware with it.
You will need to install the extension first, for it we have a :doc:`special chapter in this documentation <hardwario-code-installation>`.

There is a little difference between installation with the Portable version and standalone extension.

*******************************
Debugging with Portable Version
*******************************

If you downloaded our Portable version of Visual Studio Code.
You should have all the required programs in the ``/data``(Windows/Linux) or ``code-portable-data``(OSX) folder.

The only thing that you will need to install are JLink drivers if you don't have them already.

Windows
*******
On Windows you can just go to ``hardwario-code/data/tower/toolchain/SEGGER/JLink/USBDriver/`` and run the ``InstDrivers.exe`` binary.
After that you should be good to go.


**************************************
Debugging with Visual Studio extension
**************************************

