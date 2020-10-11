######################
About micro:bit Module
######################

This document will help you to understand the micro:bit module integration with some elements of HARDWARIO IoT Kit and extension that we made for it.

----------------------------------------------------------------

***********
First steps
***********

Before we start to explore the extension itself, we will introduce the modules and tags that are supported by it:

- Battery Module
- Mini Battery Module
- PIR Module
- CO2 Module
- Climate Module
- Relay Module
- Temperature Tag
- Humidity Tag
- Barometer Tag
- Lux Meter Tag
- VOC Tag
- VOC-LP Tag

You can get all of these in `our shop <https://shop.hardwario.com/micro-bit/>`_ separately or there are some bundles available if you want to buy more of them at once.

You can watch the video for more explaining about each thing on the list. I go over all of them one by one.

.. youtube:: https://www.youtube.com/watch?v=gdahgHwgJ3E

**************************
Setting up the environment
**************************

After you have your micro:bit, our micro:bit module and some sensor to plug into it, you can start using our extension to connect it all on the programming part.
You will need some micro-USB cable to connect the device to your PC.

Next I recommend downloading a **Google Chrome browser**, I will get to why it is the best one to go with in the next few lines.

Go to `micro:bit makecode page <https://makecode.microbit.org>`_, click a **New Project** button and give your project some good name.

You will be able to get back to your projects on this page so it will be a lot easier if you keep it organized.

.. thumbnail:: ../_static/hardware/about-microbit-module/microbit-homepage.png
    :width: 60%

You will be redirected into the makecode environment, where you can start your coding.

To get HARDWARIO extension, you just need to click **Advanced** on the left side of the editor and then all the way down,
click on **Extensions** and you should see a screen that looks something like this one.

.. thumbnail:: ../_static/hardware/about-microbit-module/microbit-extensions.png
    :width: 60%


Type **HARDWARIO** into the search box and you should see just one extension and that will be the one you are looking for,
just click on it and you will see a new selection available on the left side where all the blocks are located.

.. thumbnail:: ../_static/hardware/about-microbit-module/hardwario-extension.png
    :width: 20%


After all this is done you are ready to explore the extension block by block.

I will again talk about all that is in this chapter in the video below.

.. youtube:: https://www.youtube.com/watch?v=XAdz79VjOH4

***********************
Exploring the extension
***********************

If you never worked with the **micro:bit makecode editor** I will try and explain as much as I can in the paragraphs below but
I recommend you to watch this chapter's video.

On the start of each project you will see this screen that has Two blocks: **on start** and **forever**.

.. thumbnail:: ../_static/hardware/about-microbit-module/extension-basic.png
    :width: 60%



This is the first type of block that we also have in the extension.
You can put more blocks into those and they will run each time that the event occurs.
The **on start** block and all blocks in it will fire as you can guess by the name on the start of the code,
that is if you restart the micro:bit by giving it power or by the hardware button on the bottom of it.

The **forever** block just executes over and over again.

****************
Extension blocks
****************

Now that we know the basics about the makecode for micro:bit we can talk about blocks that are actually in our developed extension.

You can see the blocks ordered in categories for easier orientation. I will explain the category followed by a short example.

Tags
****

We will start from top to bottom with the tags. On the image below you can see all the possible values that you can read with appropriate tags.
The last one is for when you want to change how frequently some of the sensors read the data, the value is in **milliseconds**.

The oval blocks are functions that return some value, in this case the value from the last measurement on the respective Tag.
You will work with them just like with the variables, they can be placed into the serial print out or into the **if statement**, etc.

.. thumbnail:: ../_static/hardware/about-microbit-module/extension-tags.png
    :width: 40%


This example code will change the measurement on Temperature Tag to 500ms and every 2 seconds
you will get a line printed to the **Serial** console with the Temperature value:

.. thumbnail:: ../_static/hardware/about-microbit-module/extension-tags-example.png
    :width: 60%


You can try this with all the bubbles in this category if you have another tag than the Temperature one or a **CO2 Module**.

CO2 Module
==========

Basically everything said before about the tags applies here, the only difference is that the module needs 60 seconds
to charge the first time you plug it in so be patient because the first measurement will take a while.

.. thumbnail:: ../_static/hardware/about-microbit-module/extension-co2.png
    :width: 15%


Battery Module
==============

You can measure the voltage on all the the battery cells in the Battery Module.
Type of block is the same as most above, but you will have to select
if you have a Standard Battery Module with 4 cells or Mini Battery Module with only 2 of them.

.. thumbnail:: ../_static/hardware/about-microbit-module/extension-battery.png
    :width: 25%


Power Module and Relay Module
=============================

I will put these two into one category because the function is basically the same, the only thing that changes is the type of the relay.
Relay Module has a relay for less voltage and the Power Module can take up to **230V**.
With Power Module you can also use the LED strip but more on that later.

.. thumbnail:: ../_static/hardware/about-microbit-module/extension-relay.png
    :width: 30%


PIR Module
==========

Last of the categories is for Motion detection via PIR Module.
There are two blocks, one for configuration and one that fires every time the movement is detected and runs all the enclosed blocks in it.

I recommend to run the configuration one in the **on start** block if you want to use motion detection in your project.

.. thumbnail:: ../_static/hardware/about-microbit-module/extension-pir-example.png
    :width: 60%


This example will configure the PIR module and every time the movement is detected you will see it
printed out to the Serial monitor as well as you will get the beating heart animation on the LED display on the micro:bit.

********************************
Uploading your code to micro:bit
********************************

Thanks to a great micro:bit environment and the **Google Chrome browser** that you downloaded in the first steps.

After you completed your code, you can just **one click download** it to your device.

- Connect the micro:bit with usb into the computer.
- Pair the device

.. thumbnail:: ../_static/hardware/about-microbit-module/uploading-firmware.png
    :width: 60%


.. thumbnail:: ../_static/hardware/about-microbit-module/pairing-device.png
    :width: 60%


- After you click the Pair device, there should be one device that you should select.
- If you did everything right the icon on the Download button should change.

.. thumbnail:: ../_static/hardware/about-microbit-module/download-button.png
    :width: 20%


- If you now click Download you it will automatically be downloaded to your connected micro:bit.
- Also you will be able to access the console of the actual device, not just the simulator.
  You can get some nice stuff in there, like charts, serial output, pin states, etc.

.. thumbnail:: ../_static/hardware/about-microbit-module/serial-output.png
    :width: 60%


.. youtube:: https://www.youtube.com/watch?v=eFh9bphTq0w

*************
Code examples
*************

In this chapter you will learn about some use cases that you can try and do with micro:bit and **HARDWARIO TOWER - Industrial IoT Kit**.
You can try and make them by yourself or, if you are stuck, you can look at the solution here. There will be some challenges on the way.

Simple thermostat
*****************

This code should simulate some basic thermostat that can control the heating in your house.
Of course you don’t have to actually connect your heating to it.
Just visualize it with the icons on the LED matrix or some sound.

Challenge
=========

Try and make it adjustable so you can change the border temperature.

Next level can be maybe to use it with some actual heating device with a use of a relay.

You can make similar projects with different tags for example: Automatic lights, Mold fighter.

.. thumbnail:: ../_static/hardware/about-microbit-module/thermostat-example.png
    :width: 40%


*********
LED Stips
*********

You can use our LED Strips with the micro:bit module, and micro:bit. You will use the standart connector located on the Power Module and **neopixel** extension.

Download the neopixel extension just as you downloaded the HARDWARIO extension and you are ready to work with the LEDs.

Exploring the extension
***********************

.. thumbnail:: ../_static/hardware/about-microbit-module/extension-neopixel.png
    :width: 60%


You can use all of those blocks with our LED strip, there are a lot of possibilities.

Only thing you need to do is to set up the strip to the **PIN P1** and number of LEDs based on the strip, aslo set the type to **RGB+W**.

.. thumbnail:: ../_static/hardware/about-microbit-module/neopixel-example.png
    :width: 60%


With this done you can use all the other blocks from extension and start experimenting with all the colors and effects.

​There is a `tutorial <https://learn.adafruit.com/micro-bit-lesson-3-neopixels-with-micro-bit/software>`_ that you can visit so you can get the image
on what you can do with the strip.

