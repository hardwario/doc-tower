###########
Blank Start
###########

This document will guide you through a blank firmware creation,
explains the structure of the created project and the typical development cycle.

.. warning::

    This document assumes that you have necessary tools installed according to the chapter :doc:`PlatformIO installation <platformio-installation>`.

***********
Hello World
***********

If you did follow the :doc:`Firmware quick start <firmware-quick-start>` you should have **twr-skeleton** cloned from the github.

This repository serves as a blank project with some of our structures.

It is a good idea to clone this repository every time you are starting a new project. It has a correct file structure and all files needed to start from scratch.

*****************
Project Structure
*****************

This is the file structure of your ``hello-world`` project. It is a Git-initialized repository ready to be used with the PlatformIO.

.. code-block:: console
    :linenos:

    .
    ├── .git
    │   └── ...skipped
    ├── .pio
    │   └── ...skipped
    ├── lib
    │   └── twr-sdk
    ├── src
    │   └── application.c
    ├── include
    |   └── application.h
    ├── LICENSE
    ├── Makefile
    ├── platformio.ini
    └── README.md


This project can be immediately compiled and flashed to the **Core Module**, **Radio Dongle** or **Cloony**.

The place where you should edit your code is in the ``src`` directory or if you need to edit something in the header file you can do it in the ``include`` directory.

Usually you will not need to modify other files than those in there.

Therefore your first step most likely will be to open the ``src/application.c``
file in your favorite editor - for instance **Atom, Visual Studio Code, Sublime Text, etc.**

.. note::

    The Visual Studio Code is advised because of the PlatformIO extension that is available for it, but you can always use the CLI version.

.. tip::

    If you want to see some firmware examples, you can visit `our github repository <https://github.com/hardwario/twr-sdk/tree/master/_examples>`_
    or some of the **How to:** chapters in the Firmware group.

*****************
Development Cycle
*****************

Normally, the development cycle is the repetition of the following 4 steps:

- Edit the file ``src/application.c``.
- Build the project to check for the errors.
- Upload the code into the **Core Module** or **Radio Dongle**.
- Test your firmware

    .. tip::

        If you need to debug your application, please follow the chapter :doc:`Debugging <debugging>`.

