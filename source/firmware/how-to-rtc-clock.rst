#################
How to: RTC clock
#################

.. caution::

    If you are using the sdk that still uses ``bc_*`` prefixes for the function please visit :doc:`legacy document <../troubleshooting/how-to-rtc-clock>`.
    The older SDK API with ``bc_*`` is using its own RTC structure, the ``twr_*`` is using standard ``tm`` C structure.

Real Time Clock (RTC) is a hardware peripheral in STM32 microcontroller. It is used in scheduler for task planning and also can measure real time.
You can save date and time into its hardware registers and the clock is running even if you reflash or reset the processor.

Because the STM32 in LQFP48 package does not have battery backup pin, you have to keep connected at least single source of power if you would like to keep the RTC counting.
So if you need to change the batterry module you can keep the Core Module connected over USB to keep the RTC running.

Core Module has 32 768 Hz crystal which is connected to the RTC peripheral.

.. tip::

    Visit `documentation for this SDK module <https://sdk.hardwario.com/group__twr__rtc.html>`_

*************
RTC Structure
*************

RTC library uses standard `C language structure for time <https://www.tutorialspoint.com/c_standard_library/time_h.htm>`_.

It contains seconds, minutes, hours, day, month, year.
If you read the RTC then the ``timestamp`` is fileld with proper UNIX timestamp.

.. code-block:: c
    :linenos:

    struct tm {
        int tm_sec;         /* seconds,  range 0 to 59          */
        int tm_min;         /* minutes, range 0 to 59           */
        int tm_hour;        /* hours, range 0 to 23             */
        int tm_mday;        /* day of the month, range 1 to 31  */
        int tm_mon;         /* month, range 0 to 11             */
        int tm_year;        /* The number of years since 1900   */
        int tm_wday;        /* day of the week, range 0 to 6    */
        int tm_yday;        /* day in the year, range 0 to 365  */
        int tm_isdst;       /* daylight saving time             */
    };

**************
Initialization
**************

Initialization of RTC is automatic. The RTC is initialized everytime the YEAR register is set to zero.
So if you use just the time registers you should set at least value 1 to the year register.
This way the RTC is not reinitialized after reset which has a side-effect of stopping RTC counter for a second.

*************
Year register
*************

.. important::

    The year register counts from year 1900 so if you want to set year 2020 you should write the value 120 to the tm_year variable.

Year register value **0** stands for 1900 and value **199** stands for 2099.

*****************
Set date and time
*****************

This example sets up the RTC to **10.5.2020 18:26:10**

.. code-block:: c
    :linenos:

    struct tm datetime;

    datetime.tm_hour = 18;
    datetime.tm_min = 26;
    datetime.tm_sec = 10;

    datetime.tm_mon = 10;
    datetime.tm_mday = 5;
    datetime.tm_year = 120;

    twr_rtc_set_datetime(&datetime, 0);

******************
Read date and time
******************

.. code-block:: c
    :linenos:

    struct tm datetime;
    twr_rtc_get_datetime(&datetime);
    twr_log_debug("$DATE: \"%d-%02d-%02dT%02d:%02d:%02dZ\"", datetime.tm_year, datetime.tm_mon, datetime.tm_mday, datetime.tm_hour, datetime.tm_min, datetime.tm_sec);

.. tip::

    To get the exact year in normal format you can just add **1900** to the value in ``datetime.tm_year``.
