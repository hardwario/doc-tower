##################
Raspberry Pi Login
##################

.. _introduction-chapter:

************
Introduction
************

This document describes how to log in to Raspberry Pi using a remote terminal via SSH protocol.

.. note::

    The SSH stands for **"Secure Shell"**. In a simple way, this can be seen as a secure connection to the Raspberry Pi command line over the network.

If you do not already have Raspberry Pi installed, first go to the document Raspberry Pi Installation.

You can log in two ways:

***********
Log in via:
***********

.. _ip-adress-login:

IP adress
*********

In this case, you need to find out what address the DHCP server assigned to your Raspberry Pi.


.. tip::

    **Finding Raspberry Pi IP address**

    The client's IP address can usually be found through the configuration interface of your router in the section DHCP Clients, eventually LAN Status, etc.

    On your computer use utility like `Advanced IP scanner (Windows) <https://www.advanced-ip-scanner.com/cz/>`_ or
    `IP Scaner (Mac) <https://apps.apple.com/us/app/ip-scanner/id404167149?mt=12>`_.

    On your Android or iOS phone you can use `Fing <https://www.fing.com>`_ utility which can detect Raspberry Pi and show an raspberry icon with the device.

.. _dns-name-login:

DNS name
********

- For our HARDWARIO Raspbian we are using ``hub.local``
- Original Raspbian using ``raspberry.local``

*******
Connect
*******

Windows
*******

- Download the `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_ program.

.. thumbnail:: ../_static/tutorials/raspberry-pi-login/putty-login.png
   :width: 40%


Then log in with following login:

- username: ``pi``
- password: ``raspberry``

Linux and macOS
***************

- Open Terminal application and enter following command:
    - ``ssh pi@hub.local``
    - Or with IP adress instead of DNS name ``ssh pi@IP_ADRESS`` instead of IP_ADRESS fill ip adress from finder in :ref:`Introduction chapter <introduction-chapter>`
- Log in with following login:
    - username: ``pi``
    - password: ``raspberry``

*********************
Changing the password
*********************

Remember to change the default password when you first login. You can make the change using the following command:

.. code-block:: console

    passwd

*************
System Update
*************

For reasons of security and stability, it is important to keep the system up to date.
The system consists of packages and you can update them with the following command:

.. code-block:: console

    sudo apt update && sudo apt upgrade
