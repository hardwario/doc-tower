###################
How to: Servo motor
###################

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__bc__servo.html>`_

First initialize the servo output by calling function

.. code-block:: c

    bc_servo_init (bc_servo_t *self, bc_pwm_channel_t channel)

The ``channel`` parameter can be one of the output pins. Please check the :doc:`Core Module pinout <../hardware/header-pinout>` to see which pins allows PWM.

.. code-block:: c
    :linenos:

    BC_PWM_P0
    BC_PWM_P1  // Power Module LED connector
    BC_PWM_P2
    BC_PWM_P3
    BC_PWM_P6
    BC_PWM_P7
    BC_PWM_P8
    BC_PWM_P12
    BC_PWM_P14

.. note::

    The BC_PWM_P1 is special, because it's connected to the **DATA** signal on the `Power Module <https://shop.hardwario.com/power-module/>`_.
    This way you can connect the servo directly to the 3 pins instead of digital LEDs.
    **You have to use power adapter to power the servo! The USB +5V is not connected to the Power Module.**

Then you can control the servo signal and the servo movement.
You can use function to set the pulse length in microseconds or you can write directly the desired angle between the ``0-180`` degrees.

.. code-block:: c
    :linenos:

    bc_servo_set_microseconds (bc_servo_t *self, uint16_t us)
    bc_servo_get_angle (bc_servo_t *self)

In case you need to tune the pulse length limits. Use ``bc_servo_set_pulse_limits()`` function.

************
Example code
************

.. code-block:: c
    :linenos:

    bc_servo_t servo;

    void application_init()
    {
        bc_servo_init(&servo, BC_PWM_P0);
        bc_servo_set_microseconds(&servo, 1500);
    }

*****************************************************************************************************
`Example project on Github <https://github.com/blavka/bcf-test-servo/blob/master/app/application.c>`_
*****************************************************************************************************


