####################
Timing and Scheduler
####################

Knowing how to schedule tasks is a key knowledge crucial for developing low-power hardware setup with HARDWARIO TOWERS.

For this, it is important to be able to do event-driven programming easily.
To achieve this, `HARDWARIO TOWER SDK <https://sdk.hardwario.com>`_ provides tools for your application to be fully asynchronous.
Key component is the *Scheduler*. Simply said, it holds pointers to functions with exact time when they should be run.

*********
Scheduler
*********

We've developed our own scheduler based on our need for simplicity, and low-power efficiency.
It plans which task needs to be run and when. This scheduler is not the full-blown RTOS (Real Time Operating System) and it doesn't have the real co-operative multi-tasking.
One task is run and when this task exits, then another task is run.

It is important to **not block the task** but do the necessary operation quickly and let the scheduler to run other tasks.
In case you need to create some delay, then the one solution is to create for example a state machine and schedule to call the task later.

***********************************
Get Time Since Start of the Program
***********************************

Time since program started (timestamp, number of millisecond since start) can be retrieved by using ``twr_tick_t twr_tick_get()`` function.


.. note::

    **As you can see in SDK**

    ``twr_tick_t`` is a custom type based on *uint64_t*

******************
Registering a Task
******************

First thing you will probably run into when working with Scheduler is registering a simple task to be run in *"x second(s) from now"*.
Let's say, you have a function that will disable LCD display and do some other things when called.

.. code-block:: c
    :linenos:

    static void disableLCD(void* param) {
        (void) param;
        twr_module_lcd_off();
        // other things to do
    }

Inside your code you will decide that you want to run this function in 5 second from now.
This can be simply achieved by registering this function with ``twr_scheduler_register()``:

.. code-block:: c

    twr_scheduler_register(disableLCD, NULL, twr_tick_get() + 5000);

This function has a return type ``twr_scheduler_task_id_t``. It returns ID of the task that had been registered by Scheduler.
This ID can be used for unregistering from Scheduler.

********************
Unregistering a Task
********************

To unregister task from scheduler (for example when it is not needed to be run anymore) you have to use
the ``void twr_scheduler_unregister(twr_scheduler_task_id_t task_id)`` function. This takes ID of the to-be-unregistered task as a parameter.

*******************************
Planning to Run Registered Task
*******************************

One time
********

To run registered task one more time in the future, you have to use one of these functions.

Functions with ``current`` in the name controls the current task from the function is called. This way you don't need to know or pass the task ID value and the only parameter is ``twr_tick_t`` value:

- ``void twr_scheduler_plan_current_now``
- ``void twr_scheduler_plan_current_absolute``
- ``void twr_scheduler_plan_current_relative``
- ``void twr_scheduler_plan_current_from_now``


If you need to control another task, you can use functions without ``current`` in the name (taking task ID and number of milliseconds(ticks) as parameters):

- ``void twr_scheduler_plan_now``
- ``void twr_scheduler_plan_absolute``
- ``void twr_scheduler_plan_relative``
- ``void twr_scheduler_plan_from_now``

.. tip::

    To see full list of available functions, please see `SDK documentation <https://sdk.hardwario.com/group__twr__scheduler.html>`_

**Example**

To run task with ID 31415 in 5 seconds from now, you would simply call:

.. code-block:: c

    twr_scheduler_plan_from_now(31415, 5000);

Repeatedly
**********

Tasks can be run repeatedly, given absolute or relative time to be run.
Absolute time says that task will be run in x seconds, no matter how long did the previous run of the function take.
Relative time defines that task will be run exactly x seconds after this definition.

**Example**

If task with ID 31415 is in fact the function *disableLCD* from our first example, we need to only add one line to this function.
In this example, *disableLCD* will be always called exactly 2000 milliseconds after finishing previous run.

.. code-block:: c
    :linenos:

    static void disableLCD(void* param) {
        (void) param;
        twr_module_lcd_off();
        // other things to do
        twr_scheduler_plan_current_from_now(2000);
    }
