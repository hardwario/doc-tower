########
Firebase
########

.. note::

    Firebase is online platform by Google, that has lots of useful functions such as Realtime Database,
    Cloud Messaging, Cloud Storage and many other. It hosts Google on his own servers.
    You can access services right from web, mobile apps or many other ways.

In our integration with HARDWARIO we will be using Realtime Database and send data there.
You will learn how to connect and send data to firebase from Node-RED and try real example with sending data from motion sensor.

Dependencies:

- Installed Playground or our Raspbian (:doc:`Raspbian <../tutorials/raspberry-pi-installation>`)
- Installed nodejs (on our Raspbian preinstalled, other operating systems `download website <https://nodejs.org/en/download/>`_)

***********************
Install firebase plugin
***********************

Open command line
*****************

- Windows – cmd, Linux and macOS – Terminal, on our Raspbian login with user
  pi and password raspberry (:doc:`more about logging on our Raspbian <../tutorials/raspberry-pi-login>`)

Install firebase plugin to Node-RED via
***************************************

.. tabs::

    .. tab:: Node-RED
        :title: Node-RED

            Install Firebase plugin in Node-RED **Menu > Manage palette** and search for ``node-red-contrib-firebase``.

    .. tab:: Command-line
        :title: Command Line

            .. code-block:: console

                sudo npm install -g node-red-contrib-firebase

            .. code-block:: console

                sudo reboot

            Wait until system reboots.

*************
Open Node-RED
*************

.. tabs::

    .. tab:: Playground
        :title: HARDWARIO Playground

            In HARDWARIO Playground just open **Functions tab**.


    .. tab:: Hub
        :title: HARDWARIO Hub

            Connect to your HARDWARIO Hub via :ref:`IP address <ip-adress-login>` or :ref:`DNS name <dns-name-login>`.

***********************
Create Firebase project
***********************

Create project
**************

Go to `Firebase Console <https://console.firebase.google.com/>`_ and Click to **"Add project"**.



Name your project
*****************

Give your project whatever name you want, we will use for our example hardwariodemo and click Create project.



Click continue after Fireabse tells you that new project is ready.
******************************************************************


Get started
***********

At the bottom of your screen you will see three Cards, click **"Get started"** on third Card called Database.


Choose Realtime Database
************************



Database rules
**************

For our demo, we will use choice Test mode, which is totally not secure and we recommend to change
the settings of read/write rights (you can find more about it on Firebase documentation).
However, for our demo it is sufficient. Click Enable.



Finish database setting up
**************************

Now you must see database itself. Click on “dismiss” on red bar.
Point on name of database and then click on plus symbol right next to name of your database.
In field bellow fill Name with test, value with 0 and again click **"Add"** bellow.
That’s all for Firebase part but keep it open. Link of your database you will need later, you can find it on top of Database card.
Mine is https://hardwariodemo-932c9.firebaseio.com/.

****************************************
Connect Node-RED to our Firebase project
****************************************

Create flow
***********

Open the Node-RED, click on **"Hamburger menu" next to Deploy button > Import > Clipboard**. Paste text bellow.

.. code-block:: json

    [{"id":"1e3fc559.61706b","type":"inject","z":"641e3ee5.52876","name":"Set 1 to Firebase","topic":"","payload":"","payloadType":"date","repeat":"","crontab":"","once":false,"onceDelay":0.1,"x":160,"y":220,"wires":[["e605003b.cc1a5"]]},{"id":"dcca267f.911ee8","type":"inject","z":"641e3ee5.52876","name":"Set 0 to Firebase","topic":"","payload":"","payloadType":"date","repeat":"","crontab":"","once":false,"onceDelay":0.1,"x":160,"y":280,"wires":[["31e96545.b948ca"]]},{"id":"e605003b.cc1a5","type":"firebase modify","z":"641e3ee5.52876","name":"Set 1 to Firebase","firebaseconfig":"","childpath":"test","method":"set","value":"1","priority":"msg.priority","x":410,"y":220,"wires":[[]]},{"id":"31e96545.b948ca","type":"firebase modify","z":"641e3ee5.52876","name":"Set 0 to Firebase","firebaseconfig":"","childpath":"test","method":"set","value":"0","priority":"msg.priority","x":410,"y":280,"wires":[[]]}]

Set up test
***********

Double click on Firebase called **"Set value to 1"**, then click on pencil next to the Firebase line and fill it with your own.
In my case I’ve just typed hardwariodemo-932c9, in Auth choose None, then click **"Add"**.
Click Done on next page. Do the same on second Firebase named Set 0 to Firebase.

Test out
********

Click deploy. After deploying. Click on **"Set 1 to Firebase"**. Open your Firebase Database.
You have to see 1 in test child, do the same thing with second button and you have to see 0 in child in your database.


******************************************
Sends data from motion sensor to Firebase.
******************************************

Dependencies:

- Had working Wireless Motion Detector (not IFTTT part)

