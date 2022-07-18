##############
First Firmware
##############

.. attention::
    We are migrating to our own **Visual Studio Code extension** and a portable version of Visual Studio Code. For more information on how to install and use it visit
    :doc:`Developement with HARDWARIO Code <hardwario-code-installation>`.

This document will guide you through a blank firmware creation,
explains the structure of the created project and the typical development cycle.

.. warning::

    This document assumes that you already have **HARDWARIO CODE** or **HARDWARIO TOWER extension** installed on you computer.
    If not please visit :doc:`HARDWARIO CODE Installation chapter <hardwario-code-installation>`.

***********
Hello World
***********

If you did follow the :doc:`Firmware quick start <firmware-quick-start>` you should have **twr-skeleton** cloned from the GitHub.

This repository serves as a blank project.

.. note::

    It is a good idea to clone this repository every time you are starting a new project. It has a correct file structure and all files needed to start from scratch.

*****************
Project Structure
*****************

This is the file structure of your ``hello-world`` project. It is a Git-initialized repository ready to be used *out of the box*.

.. code-block:: console
    :linenos:

    .
    ├── .git
    │   └── ...skipped
    ├── .github
    │   └── ...skipped
    ├── .vscode
    │   └── ...skipped
    ├── sdk
    │   └── a lot of files (mostly not important for normal user)
    ├── src
    │   └── application.c
    |   └── application.h
    |   └── CMakeLists.txt
    ├── .editorconfig
    ├── .gitignore
    ├── .gitmodules
    ├── CMakeLists.txt
    ├── LICENSE
    └── README.md

This project can be immediately compiled and flashed to the **Core Module**, **Radio Dongle** or **Cloony**.

The place where you should edit your code is in the ``src`` directory.

Usually you will not need to modify other files than those..

Therefore your first step most likely will be to open the ``src/application.c``
file.

.. tip::

    If you want to see some firmware examples, you can visit `our GitHub repository <https://github.com/hardwario/twr-sdk/tree/master/_examples>`_
    or some of the **How to:** chapters in the Firmware group.

*****************
Development Cycle
*****************

Normally, the development cycle is the repetition of the following 4 steps:

- Edit the file ``src/application.c``.
- Build the project to check for the errors.
- Upload the code into the **Core Module** or **Radio Dongle**.
- Test your firmware

    .. important::
        To see how to do these steps with HARDWARIO CODE, you can visit the :doc:`HARDWARIO CODE tutorial <hardwario-code-tutorial>`

    .. tip::

        If you need to debug your application, please follow the chapter :doc:`Debugging <debugging>`.

********************
Programming Language
********************

Firmware is implemented in pure **C language**, which is an industrially accepted language for embedded and low-power devices.
There are the main reasons for choosing this technology:

- Efficient use of hardware resources
- Stability and long time available development environment
- Simple and understandable syntax

.. note::

    Effective use of hardware resources is important for developing of low-power devices. This is primary goal of HARDWARIO ecosystem.

You can use all known C language structures and also our SDK that is implemented so you can quickly and easily,
without any problems with compatibility, create your custom firmware.

**********
Next steps
**********

From now you should be able to create firmware and update existing ones.

To know more about our modules and see some examples, there are a lot of chapters after this one that goes over our modules and examples for them.

If you are interested in more information about SDK and firmware development you can visit :doc:`Advanced firmware information <advanced-firmware-information>`.
