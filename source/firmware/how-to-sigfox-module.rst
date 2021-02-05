#####################
How to: Sigfox Module
#####################

Sigfox module provides a simple way how to connect your kit to the Sigfox network.
As any other TOWER module, Sigfox module can be controlled with the SDK.

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__module__sigfox.html>`_

********************
MySigfox.com Service
********************

**How Does it Work?**

- message is sent from device
- Sigfox network receives the message which is processed by the Backend
- Backend sends the message to MySigfox.com
- MySigfox.com resends the message to your server

It is pretty easy to set it all up. For more information, there is a :doc:`different article. <../tutorials/mysigfox.com-service>`

*******
Example
*******

This example does nothing interesting - just sends a message containing this data "000102030405" every time button is pressed.
When message is sent, LED on Core module lights up for three second. If something went wrong, LED will blink three times.
This serves mainly for testing out that Sigfox module is working or that mysigfox.com does what you want it to do.

.. code-block:: c
    :linenos:

    #include <application.h>

    twr_led_t led;
    twr_button_t button;
    twr_module_sigfox_t sigfox;

    static void disableLCD(void* param) {
        (void) param;
        twr_led_set_mode(&led, TWR_LED_MODE_OFF);
    }

    void button_event_handler(twr_button_t *self, twr_button_event_t event, void *event_param)
    {
        if (event == TWR_BUTTON_EVENT_PRESS)
        {
            if (twr_module_sigfox_is_ready(&sigfox)) {
                uint8_t buffer[6];
                buffer[0] = 0x00;
                buffer[1] = 0x01;
                buffer[2] = 0x02;
                buffer[3] = 0x03;
                buffer[4] = 0x04;
                buffer[5] = 0x05;

                if (twr_module_sigfox_send_rf_frame(&sigfox, buffer, sizeof(buffer))) {
                    twr_led_set_mode(&led, TWR_LED_MODE_ON);
                    twr_scheduler_register(disableLCD, NULL, twr_tick_get() + 3000);
                } else {
                    twr_led_set_mode(&led, TWR_LED_MODE_BLINK);
                    twr_scheduler_register(disableLCD, NULL, twr_tick_get() + 2000);
                }
            } else {
                twr_led_set_mode(&led, TWR_LED_MODE_BLINK);
                twr_scheduler_register(disableLCD, NULL, twr_tick_get() + 2000);
            }
        }
    }

    void application_init(void)
    {

        twr_led_init(&led, TWR_GPIO_LED, false, false);
        twr_led_set_mode(&led, TWR_LED_MODE_OFF);

        twr_button_init(&button, TWR_GPIO_BUTTON, TWR_GPIO_PULL_DOWN, false);
        twr_button_set_event_handler(&button, button_event_handler, NULL);

        twr_module_sigfox_init(&sigfox, TWR_MODULE_SIGFOX_REVISION_R2);
    }
