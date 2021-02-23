#############################
Advanced Firmware Information
#############################

.. note::

    This chapter is here for advanced developers. If you want to update our sdk or make some new module, this chapter is for you.

*************
SDK Framework
*************

Software Development Kit or **SDK** is a package of software libraries that simplifies programming of HARDWARIO hardware.
This libraries contains functions to easily create your application skeleton and for easy communication with the hardware.

HARDWARIO TOWER SDK has clean design and unified access to the hardware, sensors and peripherals.

The complete package is tested together and therefore you wouldn't have software or peripheral resources conflicts.

We try to stick to these principles while working the **SDK** development:

- Consistent and clear API design
- Modular and object oriented approach
- We prefer asynchronous, event-driven programming
- Well-named functions, data types, variables, etc.
- Simple way of access to low level hardware

SDK Integration
***************

To your project, SDK is integrated as a **Git Submodule**. This has one advantage - your firmware can be "linked and locked" to a specific version of the **SDK**.

This makes sure that it will be possible to compile your firmware at any time in the future.

But if you need to, the **SDK** can be updated to most recent version by simple ``make update`` command.

.. caution::

    Please DO NOT integrate the SDK to your project as files extracted from the downloaded ZIP file from GitHub.
    Although this will work and firmware will compile,
    for getting technical support you will have to provide the exact version of the SDK used (a commit hash).

References
**********

.. tip::

    If you encounter some issues with the SDK you can suggest new problem to be added on `Github Issues <https://github.com/hardwario/bc-website/issues>`_

- `SDK repository on GitHub <https://github.com/hardwario/twr-sdk>`_
- `Generated Doxygen documentation <https://sdk.hardwario.com>`_
- `Examples of using the SDK <https://github.com/hardwario/twr-sdk/tree/master/_examples>`_

