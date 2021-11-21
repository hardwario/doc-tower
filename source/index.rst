############################################################
HARDWARIO TOWER - Industrial IoT Kit Developer Documentation
############################################################

.. thumbnail:: _static/index/logo.png
   :width: 100%
   :alt: HARDWARIO logo

Welcome to our developer documentation where you will find all the needed information about `our IoT Kit <https://www.hardwario.com/kit/>`_.

**************
Where to Begin
**************

- To start with the kit itself visit :doc:`Quick Start Guide </basics/quick-start-guide>`
- If you want to know more about our desktop GUI tool go to :doc:`HARDWARIO Playground </basics/hardwario-playground>`
- If you want to upgrade and start your own server make your own :doc:`HARDWARIO Gateway on Raspberry Pi </tutorials/raspberry-pi-installation>`
- For the developers that want to create their own firmware there is :doc:`Firmware Basic Overview </firmware/basic-overview>`

.. tip::

    For even more support and help also visit `our forum <https://forum.hardwario.com/>`_.

.. toctree::
   :caption: Basics
   :maxdepth: 2
   :hidden:

   basics/quick-start-guide
   basics/about-hardwario
   basics/hardwario-playground
   basics/module-overview
   basics/enclosures
   basics/projects
   basics/github-repositories

.. toctree::
    :caption: Tutorials
    :maxdepth: 2
    :hidden:

    tutorials/raspberry-pi-installation
    tutorials/raspberry-pi-login

    tutorials/mqtt-to-influxdb

.. toctree::
    :caption: Installation
    :maxdepth: 2
    :hidden:

    tutorials/custom-setup-on-ubuntu
    tutorials/custom-setup-on-macos
    tutorials/custom-setup-on-raspberry-pi
    tutorials/custom-setup-on-synology
    tutorials/custom-setup-on-turris

.. toctree::
   :caption: Interfaces
   :maxdepth: 2
   :hidden:

   interfaces/mqtt-protocol
   interfaces/mqtt-topics
   interfaces/wireless-network-overview
   interfaces/sub-ghz-radio
   interfaces/sigfox-iot-radio
   interfaces/lora-iot-radio
   interfaces/serial-port-json

.. toctree::
   :caption: Integrations
   :maxdepth: 2
   :hidden:

   integrations/grafana-for-visualization
   integrations/blynk-mobile-app-builder
   integrations/ubidots
   integrations/homekit-and-siri
   integrations/google-assistant
   integrations/google-firebase
   integrations/google-sheets
   integrations/azure-iot-central

.. toctree::
   :caption: Hardware
   :maxdepth: 1
   :hidden:

   hardware/basic-principles
   hardware/header-pinout
   hardware/power-management
   hardware/i-c-address-space
   hardware/about-1-wire-module
   hardware/about-barometer-tag
   hardware/about-base-module
   hardware/about-battery-module
   hardware/about-breadboard-module
   hardware/about-button-module
   hardware/about-climate-module
   hardware/about-cloony
   hardware/about-co2-module
   hardware/about-core-module
   hardware/about-cover-module
   hardware/about-encoder-module
   hardware/about-ethernet-module
   hardware/about-gps-module
   hardware/about-humidity-tag
   hardware/about-infra-grid-module
   hardware/about-lcd-module
   hardware/about-lora-module
   hardware/about-lux-meter-tag
   hardware/about-microbit-module
   hardware/about-mini-battery-module
   hardware/about-mini-cover-module
   hardware/about-nfc-tag
   hardware/about-pir-module
   hardware/about-power-module
   hardware/about-probe-module
   hardware/about-radio-dongle
   hardware/about-relay-module
   hardware/about-rs-485-module
   hardware/about-sensor-module
   hardware/about-sigfox-module
   hardware/about-soil-sensor
   hardware/about-tag-module
   hardware/about-temperature-tag
   hardware/about-voc-tag

.. toctree::
   :caption: Firmware
   :maxdepth: 2
   :hidden:

   firmware/basic-overview
   firmware/platformio-installation
   firmware/firmware-quick-start
   firmware/blank-start
   firmware/debugging
   firmware/advanced-firmware-information
   firmware/low-power-measurements-and-radio
   firmware/timing-and-scheduler
   firmware/how-to-1-wire-relay
   firmware/how-to-a-d-converter
   firmware/how-to-accelerometer
   firmware/how-to-battery-module
   firmware/how-to-co2-module
   firmware/how-to-d-a-converter
   firmware/how-to-eeprom
   firmware/how-to-eeprom-twr_config
   firmware/how-to-gfx-graphics-library
   firmware/how-to-gpio-pins
   firmware/how-to-gps-module
   firmware/how-to-i-c-bus
   firmware/how-to-lcd-module
   firmware/how-to-led-control
   firmware/how-to-lora-module
   firmware/how-to-pir-module
   firmware/how-to-power-module
   firmware/how-to-push-button
   firmware/how-to-pwm
   firmware/how-to-relay-module
   firmware/how-to-rs-485-module
   firmware/how-to-rtc-clock
   firmware/how-to-servo-motor
   firmware/how-to-sigfox-module
   firmware/how-to-smart-led-strip
   firmware/how-to-soil-sensor
   firmware/how-to-spi-bus
   firmware/how-to-temperature-sensor
   firmware/how-to-uart-interface

.. toctree::
   :caption: Tools
   :maxdepth: 2
   :hidden:

   tools/hardwario-firmware-flashing-tool
   tools/hardwario-gateway
   tools/hardwario-host-tool

.. toctree::
   :caption: LPWAN
   :maxdepth: 2
   :hidden:

   tutorials/mysigfox.com-service
   tutorials/lora-at-commands-configuration
   tutorials/connect-to-ttn


.. toctree::
   :caption: Troubleshooting (Legacy)
   :maxdepth: 2
   :hidden:

   troubleshooting/how-to-usb-console
   troubleshooting/core-module-r1-debugging
   troubleshooting/core-module-r1-and-r2-comparison
   troubleshooting/how-to-rtc-clock

