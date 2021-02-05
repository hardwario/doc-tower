###################
How to: Servo Motor
###################

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__servo.html>`_

First initialize the servo output by calling function

.. code-block:: c

    twr_servo_init (twr_servo_t *self, twr_pwm_channel_t channel)

The ``channel`` parameter can be one of the output pins. Please check the :doc:`Core Module pinout <../hardware/header-pinout>` to see which pins allows PWM.

.. code-block:: c
    :linenos:

    TWR_PWM_P0
    TWR_PWM_P1  // Power Module LED connector
    TWR_PWM_P2
    TWR_PWM_P3
    TWR_PWM_P6
    TWR_PWM_P7
    TWR_PWM_P8
    TWR_PWM_P12
    TWR_PWM_P14

.. note::

    The TWR_PWM_P1 is special, because it's connected to the **DATA** signal on the `Power Module <https://shop.hardwario.com/power-module/>`_.
    This way you can connect the servo directly to the 3 pins instead of digital LEDs.
    **You have to use power adapter to power the servo! The USB +5V is not connected to the Power Module.**

Then you can control the servo signal and the servo movement.
You can use function to set the pulse length in microseconds or you can write directly the desired angle between the ``0-180`` degrees.

.. code-block:: c
    :linenos:

    twr_servo_set_microseconds (twr_servo_t *self, uint16_t us)
    twr_servo_get_angle (twr_servo_t *self)

In case you need to tune the pulse length limits. Use ``twr_servo_set_pulse_limits()`` function.

************
Example code
************

.. code-block:: c
    :linenos:

    twr_servo_t servo;

    void application_init()
    {
        twr_servo_init(&servo, TWR_PWM_P0);
        twr_servo_set_microseconds(&servo, 1500);
    }

.. tip::

    You can check `example project on Github <https://github.com/blavka/bcf-test-servo/blob/master/app/application.c>`_ for full code example.



