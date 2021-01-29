############################
How to: GFX Graphics Library
############################

With more and more types of LCD displays types in HARDWARIO TOWER we have developed universal graphics library which can be used with many types of displays.
Starting with our LCD Module, SSD1306, ST7735, MAX7219 or even using WS2812B digital LED strip in matrix configuration as a display.

You can still use LCD Module API for drawing text and primitives, but with GFX you can also draw dithered rectangles and more.

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__gfx.html>`_

GFX is universal and needs to be initialized with a GFX driver.
The driver is a `function that returns structure <https://github.com/hubmartin/bcf-led-matrix-max7219/blob/master/app/application.c#L144>`_
with function pointers for different drawing methods.

.. caution::

    You always need to set the font first before printing any text. Otherwise nothing is displayed.
    This is because only the used fonts are linked to the binary and other are removed by optimizer.

    twr_gfx_set_font(pgfx, &twr_font_ubuntu_13);

*************************
Using GFX with LCD Module
*************************

`Example project <https://github.com/hardwario/bcf-infra-grid-lcd-mirror/tree/master/app>`__

In the latest SDK the LCD Module is now using GFX under the hood, but you can still use old ``twr_lcd_module_draw_..`` functions.
You can get the LCD Module driver and use the GFX API.

Because ``twr_module_lcd_get_gfx()`` returns already the created GFX instance,
in this example we create just the pointer ``pgfx`` and then we don't need to add an ampersand in the GFX functions in the first parameter.
In other custom drivers you have to create the instance, not just the pointer of ``twr_gfx_t``.

.. code-block:: c
    :linenos:

    // Pointer to GFX instance
    twr_gfx_t *pgfx;

    void application_init(void)
    {
        // LCD Module
        twr_module_lcd_init();
        pgfx = twr_module_lcd_get_gfx();

        twr_gfx_set_font(pgfx, &twr_font_ubuntu_13);
        twr_gfx_draw_string(pgfx, 50, 50, "Hello world", true);
        twr_gfx_update(pgfx);
    }

***************************
Using GFX with SSD1303 OLED
***************************

`Example project <https://github.com/blavka/bcf-example-gfx-ssd1306/tree/master/app>`__

.. code-block:: c
    :linenos:

    twr_gfx_t gfx;
    twr_ssd1306_t ssd1306;
    TWR_SSD1306_FRAMEBUFFER(ssd1306_framebuffer, 128, 64)

    void application_init(void)
    {
        twr_ssd1306_init(&ssd1306, TWR_I2C_I2C0, TWR_SSD1306_ADDRESS_I2C_ADDRESS_DEFAULT, &ssd1306_framebuffer);
        twr_gfx_init(&gfx, &ssd1306, twr_ssd1306_get_driver());

        twr_gfx_set_font(&gfx, &twr_font_ubuntu_13);
        twr_gfx_draw_string(&gfx, 50, 50, "Hello world", true);
        twr_gfx_update(&gfx);
    }

*****************
Custom GFX driver
*****************

`Example project <https://github.com/hubmartin/bcf-led-matrix-max7219/tree/master/app>`_

The driver needs to implement at least these 5 functions.

.. code-block:: c
    :linenos:

    static const twr_gfx_driver_t driver =
    {
        .is_ready = (bool (*)(void *)) led_matrix_is_ready,
        .clear = (void (*)(void *)) led_matrix_clear,
        .draw_pixel = (void (*)(void *, int, int, uint32_t)) led_matrix_draw_pixel,
        .update = (bool (*)(void *)) led_matrix_update,
        .get_caps = (twr_gfx_caps_t (*)(void *)) led_matrix_get_caps
    };

The function ``led_matrix_get_caps`` returns the capabilities of the display. Right now it is only width and height.

.. code-block:: c
    :linenos:

    bool led_matrix_is_ready(void *param)
    {
        return true;
    }

    void led_matrix_clear(void *param)
    {
        memset(framebuffer, 0x00, sizeof(framebuffer));
    }

    void led_matrix_draw_pixel(void *param, uint8_t x, uint8_t y, uint32_t enabled)
    {
        uint8_t sub = LED_MODULES_COUNT-1;

        if(enabled)
        {
            framebuffer[(sub - (x / 8)) + (8-y) * LED_MODULES_COUNT] |= 1 << (x % 8);
        }
        else
        {
            framebuffer[(sub - (x / 8)) + (8-y) * LED_MODULES_COUNT] &= ~(1 << (x % 8));
        }
    }

    twr_gfx_caps_t led_matrix_get_caps(twr_ls013b7dh03_t *self)
    {
        (void) self;
        static const twr_gfx_caps_t caps = { .width = 32, .height = 8 };
        return caps;
    }

    const twr_gfx_driver_t *led_matrix_get_driver(void)
    {
        static const twr_gfx_driver_t driver =
        {
            .is_ready = (bool (*)(void *)) led_matrix_is_ready,
            .clear = (void (*)(void *)) led_matrix_clear,
            .draw_pixel = (void (*)(void *, int, int, uint32_t)) led_matrix_draw_pixel,
            .update = (bool (*)(void *)) led_matrix_update,
            .get_caps = (twr_gfx_caps_t (*)(void *)) led_matrix_get_caps
        };

        return &driver;
    }

