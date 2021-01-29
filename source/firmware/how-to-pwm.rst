###########
How to: PWM
###########

Pulse Width Modulation (PWM) is a method to create analog-like signal from the microcontroller digital output.
It will achieve that by fast toggling of the pin with different ration of logic **HIGH** and **LOW**. This ratio is called **duty cycle**.

Please check the :doc:`Core Module pinout <../hardware/header-pinout>` to see which pins allows PWM.

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__pwm.html>`_


*****************
SDK PWM functions
*****************

Here are the main functions. You need to call all three of them for every PWM output.

.. code-block:: c
    :linenos:

    void twr_pwm_init(twr_pwm_channel_t channel);
    void twr_pwm_enable(twr_pwm_channel_t channel);
    void twr_pwm_set(twr_pwm_channel_t channel, uint16_t pwm_value);

The ``channel`` parameter can be one of the output pins.

.. code-block:: c
    :linenos:

    TWR_PWM_P0
    TWR_PWM_P1
    TWR_PWM_P2
    TWR_PWM_P3
    TWR_PWM_P6
    TWR_PWM_P7
    TWR_PWM_P8
    TWR_PWM_P12
    TWR_PWM_P14

The ``value`` is a number between ``0`` and ``255``.
I choose this to be the same like in Arduino ``analogWrite()`` function.
But by calling ``twr_pwm_tim_configure()`` function you can simply change period of the PWM.

************
Example code
************

Enable PWM signal on P6, P7 and P8 outputs. Every output has different duty cycle: 180, 210 and 255 (which is permanent **HIGH**).

.. code-block:: c
    :linenos:

    void application_init()
    {
        twr_pwm_init(TWR_PWM_P6);
        twr_pwm_set(TWR_PWM_P6, 180);
        twr_pwm_enable(TWR_PWM_P6);

        twr_pwm_init(TWR_PWM_P7);
        twr_pwm_set(TWR_PWM_P7, 210);
        twr_pwm_enable(TWR_PWM_P7);

        twr_pwm_init(TWR_PWM_P8);
        twr_pwm_set(TWR_PWM_P8, 255);
        twr_pwm_enable(TWR_PWM_P8);
    }
