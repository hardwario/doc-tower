##########################
Blynk - Mobile App Builder
##########################

`The Blynk <http://www.blynk.cc/>`_ is a mobile front end builder and signaling relay (MQTT). This let's you quicky create control and display for your IoT things.
Here we will guide you the process of putting together the hardware and connecting it to the cloud.
The cloud in turn gets interconnected with the project on your phone withing the Blynk app.
The local side of the project is hosted on the HARDWARIO Raspian which has all the necessary components prepared for interconnection.
When everything will be finished then you would have an ability to turn on and off the relay, switch the LED strip on and off,
change the light intensity using slider and also you would be able to watch the temperature (and other values collected) acompanied by graphs.

*************************************
Blynk example projects with HARDWARIO
*************************************

- You can find a lot of projects on our `hackster page <https://www.hackster.io/hardwario/projects?category_id=299>`_.

*********
Blynk app
*********

.. thumbnail:: ../_static/integrations/blynk/blynk-for-mobile-applications-blynk.png
   :width: 60%
   :alt: Blynk App Example

***************
Setup Blynk app
***************

The very first step needed is to install and configure the application on your mobile device. In order to interconnect things you would have to create account.
The Blynk gives you two options either create account by email or use OAuth2 login of Facebook. Decide yourself which is better for you.

.. tip::

    If you do not want to share your email, which we would consider quite safe in this case, then just create a testing email account for this purpose.

Step 1: If you do not want to share your email, which I would consider quite safe in this case, then just create a testing email account for this purpose.
**********************************************************************************************************************************************************

Step 2: After starting the app you have to create account. No email confirmation is needed, it is up to you to be careful when filling in the email address, typos might lead to unrecoverable account. The email address is used for token distribution, thus pretty important.
********************************************************************************************************************************************************************************************************************************************************************************

.. tip::

    Blynk also offers the off-line version of the server called `Local blynk server <http://docs.blynk.cc/#blynk-server>`_
    with `Github sources <https://github.com/blynkkk/blynk-server>`_. The off-line here stands for no-Internet setup.

********************
Create Blynk project
********************

In order to create a UI for your application you have to first create a project.

- Choose the project name
- Choose **HARDWARIO** device
- Connection type is **WiFi**

**************
Node-RED setup
**************

In node red, install the Blynk package ``node-red-contrib-blynk-ws`` if you cannot see **Blynk** nodes.
Also follow one of the project tutorials above where installation and creating and connecting of nodes is explained.

Here you can watch a video with the Blynk Example:

.. raw:: html

    <iframe width="750" height="422" src="https://www.youtube.com/embed/cVC_tFuCYTM?list=PLfRfhTxkuiVw0s9UQ8x5irref-EBwOghF" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**********************************
ZeRGBA to hex RGB values - Example
**********************************

Blynk color values needs to be transformed to proper hexadecimal RGB string. You can use **function** block in the **Node-RED** and paste the code below.
Remember to configure ZeRGBa to **MERGE mode** and the range of values has to be **set for all three channels to 0 - 255**

Paste this code to the Playground.

.. code-block:: json

    [{"id":"702c9447.9b790c","type":"blynk-ws-in-write","z":"aaf5722e.dfdca","name":"","pin":"1","client":"746d7fe1.2a0be","x":330,"y":280,"wires":[["4da0fdbd.a3c614"]]},{"id":"4da0fdbd.a3c614","type":"function","z":"aaf5722e.dfdca","name":"Convert to BC format","func":"var finalString = '\"#'\nvar colorToSave = \"\";\nmsg.arrayOfValues.forEach((color) => {\n    var carry = (parseInt(color)).toString(16)\n    if(carry.length == 1) carry = \"0\" + carry;\n    finalString += carry;\n    colorToSave += carry;\n});\n\nflow.set(\"color\", colorToSave);\n\nif((flow.get(\"ledstrip\")) == false){\n    msg.payload = '\"#000000(00)\"'\n}\nelse{\n    var white = flow.get(\"white\");\n    if(white == null) white = \"00\";\n    msg.payload = finalString + '(' + white + ')\"'; \n}\n\n\nmsg.topic = \"node/power-controller:0/led-strip/-/color/set\";\nreturn msg;\n","outputs":1,"noerr":0,"x":600,"y":280,"wires":[["a7ef9db0.cc602"]]},{"id":"a7ef9db0.cc602","type":"mqtt out","z":"aaf5722e.dfdca","name":"","topic":"","qos":"","retain":"","broker":"71afb0a.14d505","x":870,"y":420,"wires":[]},{"id":"b596fcc7.b5206","type":"blynk-ws-in-write","z":"aaf5722e.dfdca","name":"","pin":"4","client":"746d7fe1.2a0be","x":330,"y":460,"wires":[["80140f23.46bf6"]]},{"id":"80140f23.46bf6","type":"function","z":"aaf5722e.dfdca","name":"String to bool parser","func":"if(msg.payload == true)\n{\n    msg.payload = true;\n}\nelse{\n    msg.payload = false;\n}\nmsg.topic = \"node/power-controller:0/relay/-/state/set\";\nreturn msg;","outputs":1,"noerr":0,"x":600,"y":460,"wires":[["a7ef9db0.cc602"]]},{"id":"62416cd0.a6dbf4","type":"blynk-ws-in-write","z":"aaf5722e.dfdca","name":"","pin":"3","client":"746d7fe1.2a0be","x":330,"y":400,"wires":[["3bce27cc.257308"]]},{"id":"3bce27cc.257308","type":"function","z":"aaf5722e.dfdca","name":"Handler","func":"var lastColor = flow.get(\"color\")|| \"000000(00)\";\n\nif(msg.payload == false) {\n    msg.payload = '\"#000000(00)\"';\n    flow.set(\"ledstrip\", false);\n}\nelse {\n    msg.payload = '\"#' + '' + lastColor + '\"';\n    flow.set(\"ledstrip\", true);\n}\nmsg.topic = \"node/power-controller:0/led-strip/-/color/set\";\n\nreturn msg;","outputs":1,"noerr":0,"x":640,"y":400,"wires":[["a7ef9db0.cc602"]]},{"id":"d619d828.3e1bf8","type":"blynk-ws-in-write","z":"aaf5722e.dfdca","name":"","pin":"5","client":"746d7fe1.2a0be","x":330,"y":520,"wires":[["9b87dc69.53d55"]]},{"id":"e267bf2d.7e292","type":"blynk-ws-in-write","z":"aaf5722e.dfdca","name":"","pin":"6","client":"746d7fe1.2a0be","x":330,"y":580,"wires":[["81fcc52c.023c08"]]},{"id":"3121623b.8b75de","type":"blynk-ws-in-write","z":"aaf5722e.dfdca","name":"","pin":"2","client":"746d7fe1.2a0be","x":330,"y":340,"wires":[["99a36ea2.e29bf"]]},{"id":"9b87dc69.53d55","type":"function","z":"aaf5722e.dfdca","name":"Rainbow","func":"if(msg.payload == true && flow.get(\"ledstrip\")||true){\n    msg.payload = '{\"type\":\"rainbow\", \"wait\":50}';\n    msg.topic = \"node/power-controller:0/led-strip/-/effect/set\"   \n}\n\nreturn msg;","outputs":1,"noerr":0,"x":640,"y":520,"wires":[["a7ef9db0.cc602"]]},{"id":"81fcc52c.023c08","type":"function","z":"aaf5722e.dfdca","name":"Theater chase","func":"if(msg.payload == true && flow.get(\"ledstrip\")||true){\n    msg.payload = '{\"type\":\"theater-chase-rainbow\", \"wait\":50}';\n    msg.topic = \"node/power-controller:0/led-strip/-/effect/set\"   \n}\n\nreturn msg;","outputs":1,"noerr":0,"x":620,"y":580,"wires":[["a7ef9db0.cc602"]]},{"id":"99a36ea2.e29bf","type":"function","z":"aaf5722e.dfdca","name":"White color handler","func":"var carry = (parseInt(msg.payload)).toString(16)\nif(carry.length == 1) carry = \"0\" + carry;\n\nflow.set(\"white\", carry);\n\nvar color = flow.get(\"color\");\nif(color == null) color = \"000000\";\n\nmsg.payload = '\"#' + color +'(' + carry + ')\"';\nmsg.topic = \"node/power-controller:0/led-strip/-/color/set\";\nreturn msg;","outputs":1,"noerr":0,"x":610,"y":340,"wires":[["a7ef9db0.cc602"]]},{"id":"d40dc7b0.acf648","type":"blynk-ws-in-write","z":"aaf5722e.dfdca","name":"","pin":"7","client":"746d7fe1.2a0be","x":330,"y":640,"wires":[["a03ff4eb.de9fd8"]]},{"id":"a03ff4eb.de9fd8","type":"function","z":"aaf5722e.dfdca","name":"Brightness handler","func":"if(msg.payload == true && flow.get(\"ledstrip\")||true){\n    msg.payload = msg.payload;\n    msg.topic = \"node/power-controller:0/led-strip/-/brightness/set\"   \n}\n\nreturn msg;","outputs":1,"noerr":0,"x":610,"y":640,"wires":[["a7ef9db0.cc602"]]},{"id":"746d7fe1.2a0be","type":"blynk-ws-client","z":"","name":"","path":"ws://blynk-cloud.com/websockets","key":"","dbg_all":false,"dbg_read":false,"dbg_write":false,"dbg_notify":false,"dbg_mail":false,"dbg_prop":false,"dbg_low":false,"dbg_pins":""},{"id":"71afb0a.14d505","type":"mqtt-broker","z":"","broker":"127.0.0.1","port":"1883","clientid":"","usetls":false,"compatmode":true,"keepalive":"60","cleansession":true,"willTopic":"","willQos":"0","willPayload":"","birthTopic":"","birthQos":"0","birthPayload":""}]

You will see this node

.. thumbnail:: ../_static/integrations/blynk/node-red.png
   :width: 60%


Now you are ready to scan the QR code to the Blynk app

.. thumbnail:: ../_static/integrations/blynk/led-strip-blynk-qr.png
   :width: 40%


The Blynk project should look like this

.. thumbnail:: ../_static/integrations/blynk/led-strip-blynk-3.png
   :width: 40%

.. code-block:: javascript
    :linenos:

    var node = "generic-node:3"
    msg.topic = "node/" + node + "/led-strip/-/color/set";

    var r = Number(msg.arrayOfValues[0]).toString(16);
    var g = Number(msg.arrayOfValues[1]).toString(16);
    var b = Number(msg.arrayOfValues[2]).toString(16);

    r = (r.length < 2) ? "0" + r : r;
    g = (g.length < 2) ? "0" + g : g;
    b = (b.length < 2) ? "0" + b : b;

    msg.payload = "\"#" + r + g + b + "\"";

    return msg;
