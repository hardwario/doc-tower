##################
How to: LCD Module
##################

.. important::

    We have an :doc:`advanced and universal GFX library <how-to-gfx-graphics-library>` in SDK now for the displays.
    It is advised to use that instead of the twr_module_lcd_* functions from this document

Our `LCD Module <https://shop.hardwario.com/lcd-module-bg/>`_ provides simple way to show needed information without connecting to computer or any network.
It is *ultra-low-power device* - its usage should not bring you much trouble when powered with batteries.

It may be a bit hard to get used to draw things or show text at the beginning,
but little bit of training (and reading through this article) should help you.

.. note::

    Printing dots, writing strings and drawing lines - everything means ``draw`` in SDK.

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__module__lcd.html>`_

*********************
What you need to know
*********************

LCD Module Life Cycle
*********************

**First step**: LCD module initialization - happens once, possibly inside ``application_init()``

**Cycle:**

- LCD module On
- drawing, setting font, clearing, rotating
- LCD module Update
    - makes all changes (like drawing) visible on LCD
- LCD module Off
    - switches off the LCD module for power saving

Remember to Update
******************

Every change you make - draw a string or a line, rotate the display, etc is done internally
and no changes are visible until you call the ``twr_module_lcd_update()`` function.

This has a simple purpose - if every change you make would cause an update, it would increase the power consumption rapidly.

LCD Module Power
****************

The module can be switched *on* and *off* for power saving (mostly used to prolong battery life when used).

It is as simple as calling

``twr_module_lcd_off()``

and

``twr_module_lcd_on()``

functions.

.. caution::

    Remember that LCD needs to be switched ON if you want to show something and ``twr_module_lcd_off()`` was called. It is not enough to call the update function.

Pixel State / Color
*******************

When (for example) a string is drawn, the SDK will not draw only requested characters pixel by pixel, but entire "block" of pixels around the chars.
You can choose, which part of the block will be black and which one will be not. This can be achieved with a function parameter *bool color*.

In the *draw string* example, for this code

.. code-block:: c
    :linenos:

    twr_module_lcd_draw_string(5, 5, "false", false);
    twr_module_lcd_draw_string(5, 20, "true", true);
    twr_module_lcd_update();

the block containing the "false" string will be black and the text itself will be white and the "true" string vice versa.

Clear the LCD
*************

You can clear the LCD panel (which means set all pixels to show nothing) by calling the ``twr_module_lcd_update()`` function.

You have to call the update function ``twr_module_lcd_update()`` to make the clear process visible on LCD panel.

Rotation
********

Because the LCD is a square panel (128x128 pixels), you can
always rotate the displayed information for 0, 90, 180 and 270 degrees without the need to re-draw anything.

This is done by calling ``void twr_module_lcd_set_rotation(twr_module_lcd_rotation_t rotation)``. You can use one of these enums as the parameter:

- ``TWR_MODULE_LCD_ROTATION_0``
- ``TWR_MODULE_LCD_ROTATION_90``
- ``TWR_MODULE_LCD_ROTATION_180``
- ``TWR_MODULE_LCD_ROTATION_270``

.. important::

    Remember that rotating LCD will not clear the display nor update it.

So if you want to create function that will draw string "Hello" rotated for 90 degrees you would create something like this:

.. code-block:: c
    :linenos:

    void helloDraw()
    {
        twr_module_lcd_clear();
        twr_module_lcd_draw_string(5, 5, "Hello", false);
        twr_module_lcd_set_rotation(TWR_MODULE_LCD_ROTATION_90);
        twr_module_lcd_update();
    }

**Relative and absolute rotation**

Unfortunately the SDK does not offer any function to do rotation relative to actual
position - so if you would repeatedly call ``twr_module_lcd_set_rotation(TWR_MODULE_LCD_ROTATION_90);``
the display would be rotated **absolutely** to the right for 90 degrees. You have to implement the relative rotation yourself.

*******
Drawing
*******

Now you should know everything you need to use the LCD module so we can take a look at drawing.

As we said earlier, everything you display on your LCD is called drawing. Let's begin.

Draw a String
*************

To draw a string you need to use function

.. code-block::
    :linenos:

    with parameters:

    - `left` - number of pixels from left edge (you can set this to `2` for better readability - the text won't stick to the left edge of LCD)
    - `top` - number of pixels from the top edge
    - `*str` - string to be printed
    - `color` - in other words - what should be black (see *Pixel state* above)


    ### Draw a Line
    Drawing a line is as simple as calling function form [SDK](https://sdk.hardwario.com/group__twr__module__lcd.html#ga9eb9b7c644a7cdec4be4e97fffb6be2a). **Remember that parameters for this function are not absolute coordinates, but a relative distance from top and left edges.**

    **Examples**

    // draws a line from the bottom left to the top right corner
    twr_module_lcd_draw_line(0, 128, 128, 0, true);

    // draws a line from the bottom left to the top right corner
    twr_module_lcd_draw_line(0, 0, 128, 128, true);

*******************
LCD integrated LEDs
*******************

LCD includes 6 small RGB LEDs. They usually serve as a notifier for some action that happened. There is no way to use them as a backlight for the LCD panel.

You can control them with standard functions from ``twr_led_*`` from SDK right after you get their driver.

To get the driver you have to use function ``const twr_led_driver_t* twr_module_lcd_get_led_driver(void)`` which returns pointer to the driver.
Then you have to init the virtual LED with void ``twr_led_init_virtual(twr_led_t *self, int channel, const twr_led_driver_t *driver, int idle_state)``.

The ``channel`` parameter is equal to LED color:

- 0 is RED light
- 1 is GREEN light
- 2 is BLUE light

The ``idle_state`` sets the *default on/off* behavior.

- 0 means that LEDs are default on
- 1 means that LEDs are default off

**Example**

This example prints out some text and line and, which is the most important - lights up LCD LEDs with **blue color** for 1500 milliseconds after any LCD button is pressed.

.. code-block:: c
    :linenos:

    #include <application.h>

    twr_button_t button;
    twr_led_t lcdLed;

    void button_event_handler(twr_button_t *self, twr_button_event_t event, void *event_param)
    {
        (void) self;
        (void) event_param;

        if (event == TWR_BUTTON_EVENT_PRESS)
        {
            twr_led_pulse(&lcdLed, 1500);

            char hello[6] = "Hello";
            twr_module_lcd_draw_string(10, 5, hello, true);
            twr_module_lcd_draw_line(0, 21, 128, 23, true);

            twr_module_lcd_update();
        }
    }

    void application_init(void)
    {
        twr_button_init(&button, TWR_GPIO_BUTTON, TWR_GPIO_PULL_DOWN, false);
        twr_button_set_event_handler(&button, button_event_handler, NULL);

        const twr_led_driver_t* driver = twr_module_lcd_get_led_driver();
        twr_led_init_virtual(&lcdLed, TWR_MODULE_LCD_LED_BLUE, driver, 1);

        twr_module_lcd_init();
        twr_module_lcd_set_font(&twr_font_ubuntu_15);
    }

***********
LCD Buttons
***********

LCD module gives you two separate buttons you can use for controlling your application.
Usage is similar to LED mentioned above: first you need to get a driver and make an initialization of "virtual button".
Then you are free to use any ``twr_button_*`` functions from the SDK.

To get the button driver you can use ``const twr_button_driver_t* twr_module_lcd_get_button_driver(void)`` which returns pointer to the driver.

The initialization is achieved by calling ``void twr_button_init_virtual(twr_button_t *self, int channel, const twr_button_driver_t *driver, int idle_state)`` function.

The ``channel`` parameter tells which button you want to assign:

- 0 is the left button
- 1 is the right button

**Example**

In this example we are going to switch the LCD integrated LEDs on and off.
You can switch then on by pressing the left button and switch them of by pressing the one on the right.

.. code-block:: c
    :linenos:

    #include <application.h>

    twr_button_t button_left;
    twr_button_t button_right;
    twr_led_t lcdLed;

    void button_event_handler(twr_button_t *self, twr_button_event_t event, void *event_param)
    {
        (void) self;

        if (event == TWR_BUTTON_EVENT_PRESS && (int) event_param == 0) {
            twr_led_set_mode(&lcdLed, TWR_LED_MODE_ON);
        } else if (event == TWR_BUTTON_EVENT_PRESS && (int) event_param == 1) {
            twr_led_set_mode(&lcdLed, TWR_LED_MODE_OFF);
        }

    }

    void application_init(void)
    {
        const twr_led_driver_t* driver = twr_module_lcd_get_led_driver();
        twr_led_init_virtual(&lcdLed, 2, driver, 1);

        const twr_button_driver_t* lcdButtonDriver =  twr_module_lcd_get_button_driver();
        twr_button_init_virtual(&button_left, 0, lcdButtonDriver, 0);
        twr_button_init_virtual(&button_right, 1, lcdButtonDriver, 0);

        twr_button_set_event_handler(&button_left, button_event_handler, (int*)0);
        twr_button_set_event_handler(&button_right, button_event_handler, (int*)1);

        twr_module_lcd_init();
        twr_module_lcd_set_font(&twr_font_ubuntu_15);
    }
