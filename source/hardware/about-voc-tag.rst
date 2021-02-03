#############
About VOC Tag
#############



.. container:: twocol

   .. container:: leftside

        .. thumbnail:: ../_static/hardware/about-voc/voc-lp-tag.png
            :width: 100%


   .. container:: rightside

        The **VOC Tag** is a gas sensor for measuring **volatile organic compounds (VOC) concentration**.
        This is useful for indoor air quality monitoring applications.
        This module uses a metal-oxide multi-pixel sensor SGP30 from Sensirion measuring total VOC level.

        VOC (Volatile Organic Compounds) sensor is a great technology for indoor air quality measurement applications.
        Elevated VOC levels can have a negative impact on well being, comfort, and cognitive abilities.
        Typical VOC sources are cosmetics, detergents containing alcohols or aldehydes, carpets and flooring, paints, human and animal occupants.
        Measuring Total VOC (TVOC) level can helps to increase the efficiency of ventilation and air purification, and increases awareness of VOC sources and indoor air pollution.

.. .. |pic1| thumbnail:: ../_static/hardware/about-voc/voc-lp-tag.png
..     :width: 300em
..     :height: 300em
..
.. +------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
.. | |pic1|                 | | The **VOC Tag** is a gas sensor for measuring **volatile organic compounds (VOC) concentration**.                                                                              |
.. |                        | | This is useful for indoor air quality monitoring applications.                                                                                                                 |
.. |                        | | This module uses a metal-oxide multi-pixel sensor SGP30 from Sensirion measuring total VOC level.                                                                              |
.. |                        | |                                                                                                                                                                                |
.. |                        | | VOC (Volatile Organic Compounds) sensor is a great technology for indoor air quality measurement applications.                                                                 |
.. |                        | | Elevated VOC levels can have a negative impact on well being, comfort, and cognitive abilities.                                                                                |
.. |                        | | Typical VOC sources are cosmetics, detergents containing alcohols or aldehydes, carpets and flooring, paints, human and animal occupants.                                      |
.. |                        | | Measuring Total VOC (TVOC) level can helps to increase the efficiency of ventilation and air purification, and increases awareness of VOC sources and indoor air pollution.    |
.. +------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| |shopping-cart| `Shop <https://shop.hardwario.com/voc-tag/>`_         | |microchip| `Schematics <https://github.com/hardwario/bc-hardware/tree/master/out/bc-tag-voc>`_              | |folder-open| `SDK Library <https://sdk.hardwario.com/group__twr__sgp30>`_   | |code| `Header File <https://github.com/hardwario/twr-sdk/blob/master/bcl/inc/twr_sgp30.h>`_   | |code| `Source File <https://github.com/hardwario/twr-sdk/blob/master/bcl/src/twr_sgp30.c>`_   | |book| `Projects <https://www.hackster.io/hardwario/projects?part_id=108578>`_ |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

+------------------+--------------------+-------------------------------+-------------------------------------------------+------------------------+
| Level            | TVOC (ppb)         | Hygienic Rating               | Recommendation                                  | Exposure Limit         |
+==================+====================+===============================+=================================================+========================+
| 5 - Unhealty     | 2200 - 5500        | Situation not acceptable      | | Use only if unavoidable                       | Hours                  |
|                  |                    |                               | | Intense ventilation necessary                 |                        |
+------------------+--------------------+-------------------------------+-------------------------------------------------+------------------------+
| 4 - Poor         | 660 - 2200         | Major objections              | | Intensified ventilation                       | < 1 month              |
|                  |                    |                               | | airing necessary, search for sources          |                        |
+------------------+--------------------+-------------------------------+-------------------------------------------------+------------------------+
| 3 - Moderate     | 220 - 660          | Some objections               | | Intensified ventilation                       | < 12 months            |
|                  |                    |                               | | airing recommended, search for sources        |                        |
+------------------+--------------------+-------------------------------+-------------------------------------------------+------------------------+
| 4 - Good         | 65 - 220           | No relevant objections        | | Ventilation                                   | No limit               |
|                  |                    |                               | | airing recommended                            |                        |
+------------------+--------------------+-------------------------------+-------------------------------------------------+------------------------+
| 5 - Excellent    | 0 - 65             | No objections                 | | Target value                                  | No limit               |
|                  |                    |                               | |                                               |                        |
+------------------+--------------------+-------------------------------+-------------------------------------------------+------------------------+

<<<<<<< HEAD
=======
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| |shopping-cart| `Shop <https://shop.hardwario.com/voc-tag/>`_         | |microchip| `Schematics <https://github.com/hardwario/bc-hardware/tree/master/out/bc-tag-voc>`_              | |folder-open| `SDK Library <https://sdk.hardwario.com/group__twr__sgp30>`_   | |code| `Header File <https://github.com/hardwario/twr-sdk/blob/master/twr/inc/twr_sgp30.h>`_   | |code| `Source File <https://github.com/hardwario/twr-sdk/blob/master/twr/src/twr_sgp30.c>`_   | |book| `Projects <https://www.hackster.io/hardwario/projects?part_id=108578>`_ |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------

>>>>>>> 3bebc229feab51c57e1cb46bb852da1f8966a0c8
********
Features
********

- VOC multi-pixel gas sensor SGP30 (Sensirion)
- Suitable for indoor air quality monitoring applications
- Measurement range of TVOC: 0 to 60 000 ppb (part per billion)
- The typical Measurement accuracy of ethanol signals: 15 % of reading
- The typical Measurement accuracy of H₂ signals: 10 % of reading
- Communication using I²C digital bus interface
- Operating current: 48 mA (power supply using the DC adapter is recommended)
- Operating voltage range: 1.9 V to 6.5 V (LDO equipped module)
- Operating temperature range: -45 to 85 °C
- Mechanical dimensions: 16 x 16 mm

