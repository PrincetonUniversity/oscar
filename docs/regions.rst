######################
Description of regions
######################

While ``OSCAR`` produces strictly global diagnostics of its variables,
internally it depends on the regional distribution of emissions.  ``OSCAR``
comes built with a number of different options for regional aggregation.  These
can be set using the ``mod_regionI`` keyword argument in the ``OSCAR`` constructor.

Optional Arrangements of Internal Regions
=========================================

A visual representation of the correspondence between the internal model
regions and their geographic locations can be found in the maps below.

Houghton
--------

.. image:: graphics/Houghton-globe.png

IMACLIM
-------
           
.. image:: graphics/IMACLIM-globe.png

Kyoto
-----

.. image:: graphics/Kyoto-globe.png

Raupach*
--------
           
.. image:: graphics/Raupach*-globe.png

RCP5
----
           
.. image:: graphics/RCP5-globe.png

RCP10*
------
           
.. image:: graphics/RCP10*-globe.png

RECCAP*
-------
           
.. image:: graphics/RECCAP*-globe.png

SRES4
-----
           
.. image:: graphics/SRES4-globe.png

SRES11
------
           
.. image:: graphics/SRES11-globe.png
           
GTAP Regions
============

These larger regions are all constructed as aggregates of finer-scale regions defined in the
Global Trade Analysis Project (GTAP) version 7 [#GTAP]_.  For reference, the GTAPv7
regions, and how they relate to ``OSCAR`` region options, are tabulated below.

+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|Code |Country    |GTAP |SRES4    |SRES11     |RECCAP*  |Raupach*|Houghton  |IMACLIM|Kyoto    |RCP5     |RCP10*   |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|AUS  |Australia  |1    |OECD     |Pacific    |Oceania  |D1      |Pacific   |Pacific|Annex    |OECD     |Pacific  |
|     |           |     |Countries|OECD       |         |        |Developing|OECD   |B        |Countries|OECD     |
|     |           |     |(1990)   |           |         |        |Countries |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|NZL  |New        |2    |OECD     |Pacific    |Oceania  |D1      |Pacific   |Pacific|Annex    |OECD     |Pacific  |
|     |Zealand    |     |Countries|OECD       |         |        |Developing|OECD   |B        |Countries|OECD     |
|     |           |     |(1990)   |           |         |        |Countries |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|XOC  |Rest of    |3    |Asia     |Pacific    |Oceania  |D2      |Pacific   |Rest of|Non-Annex|OECD     |Pacific  |
|     |Oceania    |     |         |Asia       |         |        |Developing|Asia   |B        |Countries|OECD     |
|     |           |     |         |           |         |        |Countries |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|CHN  |China      |4    |Asia     |Centrally  |China    |China   |China     |China  |Non-Annex|Asia     |China    |
|     |           |     |         |Planned    |         |        |          |       |B        |         |         |
|     |           |     |         |Asia and   |         |        |          |       |         |         |         |
|     |           |     |         |China      |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|HKG  |Hong Kong  |5    |Asia     |Centrally  |China    |China   |China     |Rest of|Non-Annex|Asia     |China    |
|     |           |     |         |Planned    |         |        |          |Asia   |B        |         |         |
|     |           |     |         |Asia and   |         |        |          |       |         |         |         |
|     |           |     |         |China      |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|JPN  |Japan      |6    |OECD     |Pacific    |China    |Japan   |Pacific   |Pacific|Annex B  |OECD     |Pacific  |
|     |           |     |Countries|OECD       |         |        |Developing|OECD   |         |Countries|OECD     |
|     |           |     |(1990)   |           |         |        |Countries |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|KOR  |Korea      |7    |Asia     |Pacific    |China    |D1      |Pacific   |Pacific|Non-Annex|Asia     |Rest of  |
|     |           |     |         |Asia       |         |        |Developing|OECD   |B        |         |Asia     |
|     |           |     |         |           |         |        |Countries |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|TWN  |Taiwan     |8    |Asia     |Centrally  |China    |D1      |Pacific   |Rest of|Non-Annex|Asia     |China    |
|     |           |     |         |Planned    |         |        |Developing|Asia   |B        |         |         |
|     |           |     |         |Asia and   |         |        |Countries |       |         |         |         |
|     |           |     |         |China      |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|XEA  |Rest of    |9    |Asia     |Centrally  |China    |D2      |China     |Rest of|Non-Annex|Asia     |China    |
|     |East Asia  |     |         |Planned    |         |        |          |Asia   |B        |         |         |
|     |           |     |         |Asia and   |         |        |          |       |         |         |         |
|     |           |     |         |China      |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|KHM  |Cambodia   |10   |Asia     |Centrally  |Southeast|D3      |South and |Rest of|Non-Annex|Asia     |Rest of  |
|     |           |     |         |Planned    |Asia     |        |Southeast |Asia   |B        |         |Asia     |
|     |           |     |         |Asia and   |         |        |Asia      |       |         |         |         |
|     |           |     |         |China      |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|IDN  |Indonesia  |11   |Asia     |Pacific    |Southeast|D2      |South and |Rest of|Non-Annex|Asia     |Rest of  |
|     |           |     |         |Asia       |Asia     |        |Southeast |Asia   |B        |         |Asia     |
|     |           |     |         |           |         |        |Asia      |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|LAO  |Lao        |12   |Asia     |Centrally  |Southeast|D3      |South and |Rest of|Non-Annex|Asia     |Rest of  |
|     |People's   |     |         |Planned    |Asia     |        |Southeast |Asia   |B        |         |Asia     |
|     |Democratic |     |         |Asia and   |         |        |Asia      |       |         |         |         |
|     |Republic   |     |         |China      |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|MMR  |Myanmar    |13   |Asia     |Pacific    |Southeast|D3      |South and |Rest of|Non-Annex|Asia     |Rest of  |
|     |           |     |         |Asia       |Asia     |        |Southeast |Asia   |B        |         |Asia     |
|     |           |     |         |           |         |        |Asia      |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|MYS  |Malaysia   |14   |Asia     |Pacific    |Southeast|D2      |South and |Rest of|Non-Annex|Asia     |Rest of  |
|     |           |     |         |Asia       |Asia     |        |Southeast |Asia   |B        |         |Asia     |
|     |           |     |         |           |         |        |Asia      |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|PHL  |Philippines|15   |Asia     |Pacific    |Southeast|D2      |South and |Rest of|Non-Annex|Asia     |Rest of  |
|     |           |     |         |Asia       |Asia     |        |Southeast |Asia   |B        |         |Asia     |
|     |           |     |         |           |         |        |Asia      |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|SGP  |Singapore  |16   |Asia     |Pacific    |Southeast|D1      |South and |Rest of|Non-Annex|Asia     |Rest of  |
|     |           |     |         |Asia       |Asia     |        |Southeast |Asia   |B        |         |Asia     |
|     |           |     |         |           |         |        |Asia      |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|THA  |Thailand   |17   |Asia     |Pacific    |Southeast|D2      |South and |Rest of|Non-Annex|Asia     |Rest of  |
|     |           |     |         |Asia       |Asia     |        |Southeast |Asia   |B        |         |Asia     |
|     |           |     |         |           |         |        |Asia      |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|VNM  |Vietnam    |18   |Asia     |Pacific    |Southeast|D2      |South and |Rest of|Non-Annex|Asia     |Rest of  |
|     |           |     |         |Asia       |Asia     |        |Southeast |Asia   |B        |         |Asia     |
|     |           |     |         |           |         |        |Asia      |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|XSE  |Rest of    |19   |Asia     |Pacific    |Southeast|D3      |South and |Rest of|Non-Annex|Asia     |Rest of  |
|     |Southeast  |     |         |Asia       |Asia     |        |Southeast |Asia   |B        |         |Asia     |
|     |Asia       |     |         |           |         |        |Asia      |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|BGD  |Bangladesh |20   |Asia     |South      |South    |D3      |South and |Rest of|Non-Annex|Asia     |India    |
|     |           |     |         |Asia       |Asia     |        |Southeast |Asia   |B        |         |         |
|     |           |     |         |           |         |        |Asia      |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|IND  |India      |21   |Asia     |South      |South    |India   |South and |India  |Non-Annex|Asia     |India    |
|     |           |     |         |Asia       |Asia     |        |Southeast |       |B        |         |         |
|     |           |     |         |           |         |        |Asia      |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|PAK  |Pakistan   |22   |Asia     |South      |South    |D2      |South and |Rest of|Non-Annex|Asia     |India    |
|     |           |     |         |Asia       |Asia     |        |Southeast |Asia   |B        |         |         |
|     |           |     |         |           |         |        |Asia      |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|LKA  |Sri Lanka  |23   |Asia     |South      |South    |D2      |South and |Rest of|Non-Annex|Asia     |India    |
|     |           |     |         |Asia       |Asia     |        |Southeast |Asia   |B        |         |         |
|     |           |     |         |           |         |        |Asia      |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|XSA  |Rest of    |24   |Asia     |South      |South    |D3      |South and |Rest of|Non-Annex|Asia     |India    |
|     |South Asia |     |         |Asia       |Asia     |        |Southeast |Asia   |B        |         |         |
|     |           |     |         |           |         |        |Asia      |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|CAN  |Canada     |25   |OECD     |North      |North    |D1      |North     |Canada |Annex B  |OECD     |Northern |
|     |           |     |Countries|America    |America  |        |America   |       |         |Countries|America  |
|     |           |     |(1990)   |           |         |        |          |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|USA  |United     |26   |OECD     |North      |North    |United  |North     |United |Annex B  |OECD     |Northern |
|     |States of  |     |Countries|America    |America  |States  |America   |States |         |Countries|America  |
|     |America    |     |(1990)   |           |         |        |          |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|MEX  |Mexico     |27   |Africa   |Latin      |North    |D2      |South and |Rest of|Non-Annex|Latin    |Latin    |
|     |           |     |Latin    |America    |America  |        |Central   |Latin  |B        |America  |America  |
|     |           |     |America  |and the    |         |        |America   |America|         |         |         |
|     |           |     |Middle   |Caribbean  |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|XNA  |Rest of    |28   |OECD     |Western    |North    |D1      |Europe    |Rest of|Non-Annex|OECD     |Western  |
|     |North      |     |Countries|Europe     |America  |        |          |Latin  |B        |Countries|Europe   |
|     |America    |     |(1990)   |           |         |        |          |America|         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|ARG  |Argentina  |29   |Africa   |Latin      |South    |D2      |South and |Rest of|Non-Annex|Latin    |Latin    |
|     |           |     |Latin    |America    |America  |        |Central   |Latin  |B        |America  |America  |
|     |           |     |America  |and the    |         |        |America   |America|         |         |         |
|     |           |     |Middle   |Caribbean  |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|BOL  |Bolivia    |30   |Africa   |Latin      |South    |D2      |South and |Rest of|Non-Annex|Latin    |Latin    |
|     |           |     |Latin    |America    |America  |        |Central   |Latin  |B        |America  |America  |
|     |           |     |America  |and the    |         |        |America   |America|         |         |         |
|     |           |     |Middle   |Caribbean  |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|BRA  |Brazil     |31   |Africa   |Latin      |South    |D2      |South and |Brazil |Non-Annex|Latin    |Latin    |
|     |           |     |Latin    |America    |America  |        |Central   |       |B        |America  |America  |
|     |           |     |America  |and the    |         |        |America   |       |         |         |         |
|     |           |     |Middle   |Caribbean  |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|CHL  |Chile      |32   |Africa   |Latin      |South    |D2      |South and |Rest of|Non-Annex|Latin    |Latin    |
|     |           |     |Latin    |America    |America  |        |Central   |Latin  |B        |America  |America  |
|     |           |     |America  |and the    |         |        |America   |America|         |         |         |
|     |           |     |Middle   |Caribbean  |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|COL  |Colombia   |33   |Africa   |Latin      |South    |D2      |South and |Rest of|Non-Annex|Latin    |Latin    |
|     |           |     |Latin    |America    |America  |        |Central   |Latin  |B        |America  |America  |
|     |           |     |America  |and the    |         |        |America   |America|         |         |         |
|     |           |     |Middle   |Caribbean  |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|ECU  |Ecuador    |34   |Africa   |Latin      |South    |D2      |South and |Rest of|Non-Annex|Latin    |Latin    |
|     |           |     |Latin    |America    |America  |        |Central   |Latin  |B        |America  |America  |
|     |           |     |America  |and the    |         |        |America   |America|         |         |         |
|     |           |     |Middle   |Caribbean  |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|PRY  |Paraguay   |35   |Africa   |Latin      |South    |D2      |South and |Rest of|Non-Annex|Latin    |Latin    |
|     |           |     |Latin    |America    |America  |        |Central   |Latin  |B        |America  |America  |
|     |           |     |America  |and the    |         |        |America   |America|         |         |         |
|     |           |     |Middle   |Caribbean  |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|PER  |Peru       |36   |Africa   |Latin      |South    |D2      |South and |Rest of|Non-Annex|Latin    |Latin    |
|     |           |     |Latin    |America    |America  |        |Central   |Latin  |B        |America  |America  |
|     |           |     |America  |and the    |         |        |America   |America|         |         |         |
|     |           |     |Middle   |Caribbean  |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|URY  |Uruguay    |37   |Africa   |Latin      |South    |D2      |South and |Rest of|Non-Annex|Latin    |Latin    |
|     |           |     |Latin    |America    |America  |        |Central   |Latin  |B        |America  |America  |
|     |           |     |America  |and the    |         |        |America   |America|         |         |         |
|     |           |     |Middle   |Caribbean  |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|VEN  |Venezuela  |38   |Africa   |Latin      |South    |D2      |South and |Rest of|Non-Annex|Latin    |Latin    |
|     |           |     |Latin    |America    |America  |        |Central   |Latin  |B        |America  |America  |
|     |           |     |America  |and the    |         |        |America   |America|         |         |         |
|     |           |     |Middle   |Caribbean  |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|XSM  |Rest of    |39   |Africa   |Latin      |South    |D2      |South and |Rest of|Non-Annex|Latin    |Latin    |
|     |South      |     |Latin    |America    |America  |        |Central   |Latin  |B        |America  |America  |
|     |America    |     |America  |and the    |         |        |America   |America|         |         |         |
|     |           |     |Middle   |Caribbean  |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|CRI  |Costa Rica |40   |Africa   |Latin      |Other    |D2      |South and |Rest of|Non-Annex|Latin    |Latin    |
|     |           |     |Latin    |America    |         |        |Central   |Latin  |B        |America  |America  |
|     |           |     |America  |and the    |         |        |America   |America|         |         |         |
|     |           |     |Middle   |Caribbean  |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|GTM  |Guatemala  |41   |Africa   |Latin      |Other    |D2      |South and |Rest of|Non-Annex|Latin    |Latin    |
|     |           |     |Latin    |America    |         |        |Central   |Latin  |B        |America  |America  |
|     |           |     |America  |and the    |         |        |America   |America|         |         |         |
|     |           |     |Middle   |Caribbean  |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|NIC  |Nicaragua  |42   |Africa   |Latin      |Other    |D2      |South and |Rest of|Non-Annex|Latin    |Latin    |
|     |           |     |Latin    |America    |         |        |Central   |Latin  |B        |America  |America  |
|     |           |     |America  |and the    |         |        |America   |America|         |         |         |
|     |           |     |Middle   |Caribbean  |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|PAN  |Panama     |43   |Africa   |Latin      |Other    |D2      |South and |Rest of|Non-Annex|Latin    |Latin    |
|     |           |     |Latin    |America    |         |        |Central   |Latin  |B        |America  |America  |
|     |           |     |America  |and the    |         |        |America   |America|         |         |         |
|     |           |     |Middle   |Caribbean  |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|XCA  |Rest of    |44   |Africa   |Latin      |Other    |D2      |South and |Rest of|Non-Annex|Latin    |Latin    |
|     |Central    |     |Latin    |America    |         |        |Central   |Latin  |B        |America  |America  |
|     |America    |     |America  |and the    |         |        |America   |America|         |         |         |
|     |           |     |Middle   |Caribbean  |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|XCB  |Caribbean  |45   |Africa   |Latin      |Other    |D2      |South and |Rest of|Non-Annex|Latin    |Latin    |
|     |           |     |Latin    |America    |         |        |Central   |Latin  |B        |America  |America  |
|     |           |     |America  |and the    |         |        |America   |America|         |         |         |
|     |           |     |Middle   |Caribbean  |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|AUT  |Austria    |46   |OECD     |Western    |Europe   |Europe  |Europe    |Europe |Annex B  |OECD     |Western  |
|     |           |     |Countries|Europe     |         |        |          |       |         |Countries|Europe   |
|     |           |     |(1990)   |           |         |        |          |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|BEL  |Belgium    |47   |OECD     |Western    |Europe   |Europe  |Europe    |Europe |Annex B  |OECD     |Western  |
|     |           |     |Countries|Europe     |         |        |          |       |         |Countries|Europe   |
|     |           |     |(1990)   |           |         |        |          |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|CYP  |Cyprus     |48   |OECD     |Western    |Europe   |Europe  |North     |Europe |Annex B  |Reforming|Reforming|
|     |           |     |Countries|Europe     |         |        |Africa and|       |         |Countries|Countries|
|     |           |     |(1990)   |           |         |        |Middle    |       |         |         |         |
|     |           |     |         |           |         |        |East      |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|CZE  |Czech      |49   |Reformed |Central    |Europe   |Europe  |Europe    |Europe |Annex B  |Reforming|Reforming|
|     |Republic   |     |Countries|and        |         |        |          |       |         |Countries|Countries|
|     |           |     |         |Eastern    |         |        |          |       |         |         |         |
|     |           |     |         |Europe     |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|DNK  |Denmark    |50   |OECD     |Western    |Europe   |Europe  |Europe    |Europe |Annex B  |OECD     |Western  |
|     |           |     |Countries|Europe     |         |        |          |       |         |Countries|Europe   |
|     |           |     |(1990)   |           |         |        |          |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|EST  |Estonia    |51   |Reformed |Former     |Europe   |Former  |Former    |Europe |Annex B  |Reforming|Reforming|
|     |           |     |Countries|Soviet     |         |Soviet  |Soviet    |       |         |Countries|Countries|
|     |           |     |         |Union      |         |Union   |Union     |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|FIN  |Finland    |52   |OECD     |Western    |Europe   |Europe  |Europe    |Europe |Annex B  |OECD     |Western  |
|     |           |     |Countries|Europe     |         |        |          |       |         |Countries|Europe   |
|     |           |     |(1990)   |           |         |        |          |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|FRA  |France     |53   |OECD     |Western    |Europe   |Europe  |Europe    |Europe |Annex B  |OECD     |Western  |
|     |           |     |Countries|Europe     |         |        |          |       |         |Countries|Europe   |
|     |           |     |(1990)   |           |         |        |          |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|DEU  |Germany    |54   |OECD     |Western    |Europe   |Europe  |Europe    |Europe |Annex B  |OECD     |Western  |
|     |           |     |Countries|Europe     |         |        |          |       |         |Countries|Europe   |
|     |           |     |(1990)   |           |         |        |          |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|GRC  |Greece     |55   |OECD     |Western    |Europe   |Europe  |Europe    |Europe |Annex B  |OECD     |Western  |
|     |           |     |Countries|Europe     |         |        |          |       |         |Countries|Europe   |
|     |           |     |(1990)   |           |         |        |          |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|HUN  |Hungary    |56   |Reformed |Central    |Europe   |Europe  |Europe    |Europe |Annex B  |Reforming|Reforming|
|     |           |     |Countries|and        |         |        |          |       |         |Countries|Countries|
|     |           |     |         |Eastern    |         |        |          |       |         |         |         |
|     |           |     |         |Europe     |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|IRL  |Ireland    |57   |OECD     |Western    |Europe   |Europe  |Europe    |Europe |Annex B  |OECD     |Western  |
|     |           |     |Countries|Europe     |         |        |          |       |         |Countries|Europe   |
|     |           |     |(1990)   |           |         |        |          |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|ITA  |Italy      |58   |OECD     |Western    |Europe   |Europe  |Europe    |Europe |Annex B  |OECD     |Western  |
|     |           |     |Countries|Europe     |         |        |          |       |         |Countries|Europe   |
|     |           |     |(1990)   |           |         |        |          |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|LVA  |Latvia     |59   |Reformed |Former     |Europe   |Former  |Former    |Europe |Annex B  |Reforming|Reforming|
|     |           |     |Countries|Soviet     |         |Soviet  |Soviet    |       |         |Countries|Countries|
|     |           |     |         |Union      |         |Union   |Union     |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|LTU  |Lithuania  |60   |Reformed |Former     |Europe   |Former  |Former    |Europe |Annex B  |Reforming|Reforming|
|     |           |     |Countries|Soviet     |         |Soviet  |Soviet    |       |         |Countries|Countries|
|     |           |     |         |Union      |         |Union   |Union     |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|LUX  |Luxembourg |61   |OECD     |Western    |Europe   |Europe  |Europe    |Europe |Annex B  |OECD     |Western  |
|     |           |     |Countries|Europe     |         |        |          |       |         |Countries|Europe   |
|     |           |     |(1990)   |           |         |        |          |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|MLT  |Malta      |62   |OECD     |Western    |Europe   |Europe  |Europe    |Europe |Annex B  |Reforming|Reforming|
|     |           |     |Countries|Europe     |         |        |          |       |         |Countries|Countries|
|     |           |     |(1990)   |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|NLD  |Netherlands|63   |OECD     |Western    |Europe   |Europe  |Europe    |Europe |Annex B  |OECD     |Western  |
|     |           |     |Countries|Europe     |         |        |          |       |         |Countries|Europe   |
|     |           |     |(1990)   |           |         |        |          |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|POL  |Poland     |64   |Reformed |Central    |Europe   |Europe  |Europe    |Europe |Annex B  |Reforming|Reforming|
|     |           |     |Countries|and        |         |        |          |       |         |Countries|Countries|
|     |           |     |         |Eastern    |         |        |          |       |         |         |         |
|     |           |     |         |Europe     |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|PRT  |Portugal   |65   |OECD     |Western    |Europe   |Europe  |Europe    |Europe |Annex B  |OECD     |Western  |
|     |           |     |Countries|Europe     |         |        |          |       |         |Countries|Europe   |
|     |           |     |(1990)   |           |         |        |          |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|SVK  |Slovakia   |66   |Reformed |Central    |Europe   |Europe  |Europe    |Europe |Annex B  |Reforming|Reforming|
|     |           |     |Countries|and        |         |        |          |       |         |Countries|Countries|
|     |           |     |         |Eastern    |         |        |          |       |         |         |         |
|     |           |     |         |Europe     |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|SVN  |Slovenia   |67   |Reformed |Central    |Europe   |Europe  |Europe    |Europe |Annex B  |Reforming|Reforming|
|     |           |     |Countries|and        |         |        |          |       |         |Countries|Countries|
|     |           |     |         |Eastern    |         |        |          |       |         |         |         |
|     |           |     |         |Europe     |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|ESP  |Spain      |68   |OECD     |Western    |Europe   |Europe  |Europe    |Europe |Annex B  |OECD     |Western  |
|     |           |     |Countries|Europe     |         |        |          |       |         |Countries|Europe   |
|     |           |     |(1990)   |           |         |        |          |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|SWE  |Sweden     |69   |OECD     |Western    |Europe   |Europe  |Europe    |Europe |Annex B  |OECD     |Western  |
|     |           |     |Countries|Europe     |         |        |          |       |         |Countries|Europe   |
|     |           |     |(1990)   |           |         |        |          |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|GBR  |United     |70   |OECD     |Western    |Europe   |Europe  |Europe    |Europe |Annex B  |OECD     |Western  |
|     |Kingdom    |     |Countries|Europe     |         |        |          |       |         |Countries|Europe   |
|     |           |     |(1990)   |           |         |        |          |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|CHE  |Switzerland|71   |OECD     |Western    |Europe   |D1      |Europe    |Europe |Annex B  |OECD     |Western  |
|     |           |     |Countries|Europe     |         |        |          |       |         |Countries|Europe   |
|     |           |     |(1990)   |           |         |        |          |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|NOR  |Norway     |72   |OECD     |Western    |Europe   |D1      |Europe    |Europe |Annex B  |OECD     |Western  |
|     |           |     |Countries|Europe     |         |        |          |       |         |Countries|Europe   |
|     |           |     |(1990)   |           |         |        |          |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|XEF  |Rest of    |73   |OECD     |Western    |Europe   |D1      |Europe    |Europe |Annex B  |OECD     |Western  |
|     |EFTA       |     |Countries|Europe     |         |        |          |       |         |Countries|Europe   |
|     |           |     |(1990)   |           |         |        |          |       |         |(1990)   |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|ALB  |Albania    |74   |Reformed |Central    |Other    |D2      |Europe    |Europe |Non-Annex|Reforming|Reforming|
|     |           |     |Countries|and        |         |        |          |       |B        |Countries|Countries|
|     |           |     |         |Eastern    |         |        |          |       |         |         |         |
|     |           |     |         |Europe     |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|BGR  |Bulgaria   |75   |Reformed |Central    |Other    |D2      |Europe    |Europe |Non-Annex|Reforming|Reforming|
|     |           |     |Countries|and        |         |        |          |       |B        |Countries|Countries|
|     |           |     |         |Eastern    |         |        |          |       |         |         |         |
|     |           |     |         |Europe     |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|BLR  |Belarus    |76   |Reformed |Former     |Russia   |Former  |Former    |CEI    |Non-Annex|Reforming|Reforming|
|     |           |     |Countries|Soviet     |         |Soviet  |Soviet    |       |B        |Countries|Countries|
|     |           |     |         |Union      |         |Union   |Union     |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|HRV  |Croatia    |77   |Reformed |Central    |Other    |D2      |Europe    |Europe |Annex B  |Reforming|Reforming|
|     |           |     |Countries|and        |         |        |          |       |         |Countries|Countries|
|     |           |     |         |Eastern    |         |        |          |       |         |         |         |
|     |           |     |         |Europe     |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|ROU  |Romania    |78   |Reformed |Central    |Other    |D2      |Europe    |Europe |Annex B  |Reforming|Reforming|
|     |           |     |Countries|and        |         |        |          |       |         |Countries|Countries|
|     |           |     |         |Eastern    |         |        |          |       |         |         |         |
|     |           |     |         |Europe     |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|RUS  |Russian    |79   |Reformed |Former     |Russia   |Former  |Former    |CEI    |Annex B  |Reforming|Reforming|
|     |Federation |     |Countries|Soviet     |         |Soviet  |Soviet    |       |         |Countries|Countries|
|     |           |     |         |Union      |         |Union   |Union     |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|UKR  |Ukraine    |80   |Reformed |Former     |Russia   |Former  |Former    |CEI    |Annex B  |Reforming|Reforming|
|     |           |     |Countries|Soviet     |         |Soviet  |Soviet    |       |         |Countries|Countries|
|     |           |     |         |Union      |         |Union   |Union     |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|XEE  |Rest of    |81   |Reformed |Former     |Other    |Former  |Former    |Europe |Non-Annex|Reforming|Reforming|
|     |Eastern    |     |Countries|Soviet     |         |Soviet  |Soviet    |       |B        |Countries|Countries|
|     |Europe     |     |         |Union      |         |Union   |Union     |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|XER  |Rest of    |82   |Reformed |Central    |Other    |D2      |Europe    |Europe |Non-Annex|Reforming|Reforming|
|     |Europe     |     |Countries|and        |         |        |          |       |B        |Countries|Countries|
|     |           |     |         |Eastern    |         |        |          |       |         |         |         |
|     |           |     |         |Europe     |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|KAZ  |Kazakhstan |83   |Reformed |Former     |Other    |Former  |Former    |CEI    |Non-Annex|Reforming|Reforming|
|     |           |     |Countries|Soviet     |         |Soviet  |Soviet    |       |B        |Countries|Countries|
|     |           |     |         |Union      |         |Union   |Union     |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|KGZ  |Kyrgyzstan |84   |Reformed |Former     |Other    |Former  |Former    |CEI    |Non-Annex|Reforming|Reforming|
|     |           |     |Countries|Soviet     |         |Soviet  |Soviet    |       |B        |Countries|Countries|
|     |           |     |         |Union      |         |Union   |Union     |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|XSU  |Rest of    |85   |Reformed |Former     |Other    |Former  |Former    |CEI    |Non-Annex|Reforming|Reforming|
|     |Former     |     |Countries|Soviet     |         |Soviet  |Soviet    |       |B        |Countries|Countries|
|     |Soviet     |     |         |Union      |         |Union   |Union     |       |         |         |         |
|     |Union      |     |         |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|ARM  |Armenia    |86   |Reformed |Former     |Other    |Former  |Former    |CEI    |Non-Annex|Reforming|Reforming|
|     |           |     |Countries|Soviet     |         |Soviet  |Soviet    |       |B        |Countries|Countries|
|     |           |     |         |Union      |         |Union   |Union     |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|AZE  |Azerbaijan |87   |Reformed |Former     |Other    |Former  |Former    |CEI    |Non-Annex|Reforming|Reforming|
|     |           |     |Countries|Soviet     |         |Soviet  |Soviet    |       |B        |Countries|Countries|
|     |           |     |         |Union      |         |Union   |Union     |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|GEO  |Georgia    |88   |Reformed |Former     |Other    |Former  |Former    |CEI    |Non-Annex|Reforming|Reforming|
|     |           |     |Countries|Soviet     |         |Soviet  |Soviet    |       |B        |Countries|Countries|
|     |           |     |         |Union      |         |Union   |Union     |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|IRN  |Iran       |89   |Africa   |Middle     |Other    |D2      |North     |Middle |Non-Annex|Middle   |Middle   |
|     |           |     |Latin    |East and   |         |        |Africa and|East   |B        |East and |East     |
|     |           |     |America  |North      |         |        |Middle    |       |         |Africa   |         |
|     |           |     |Middle   |Africa     |         |        |East      |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|TUR  |Turkey     |90   |OECD     |Western    |Other    |D2      |North     |Europe |Non-Annex|OECD     |Western  |
|     |           |     |Countries|Europe     |         |        |Africa and|       |B        |Countries|Europe   |
|     |           |     |(1990)   |           |         |        |Middle    |       |         |(1990)   |         |
|     |           |     |         |           |         |        |East      |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|XWS  |Rest of    |91   |Africa   |Middle     |Other    |D2      |North     |Middle |Non-Annex|Middle   |Middle   |
|     |Western    |     |Latin    |East and   |         |        |Africa and|East   |B        |East and |East     |
|     |Asia       |     |America  |North      |         |        |Middle    |       |         |Africa   |         |
|     |           |     |Middle   |Africa     |         |        |East      |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|EGY  |Egypt      |92   |Africa   |Middle     |Africa   |D2      |North     |Africa |Non-Annex|Middle   |Africa   |
|     |           |     |Latin    |East and   |         |        |Africa and|       |B        |East and |         |
|     |           |     |America  |North      |         |        |Middle    |       |         |Africa   |         |
|     |           |     |Middle   |Africa     |         |        |East      |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|MAR  |Morocco    |93   |Africa   |Middle     |Africa   |D2      |North     |Africa |Non-Annex|Middle   |Africa   |
|     |           |     |Latin    |East and   |         |        |Africa and|       |B        |East and |         |
|     |           |     |America  |North      |         |        |Middle    |       |         |Africa   |         |
|     |           |     |Middle   |Africa     |         |        |East      |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|TUN  |Tunisia    |94   |Africa   |Middle     |Africa   |D2      |North     |Africa |Non-Annex|Middle   |Africa   |
|     |           |     |Latin    |East and   |         |        |Africa and|       |B        |East and |         |
|     |           |     |America  |North      |         |        |Middle    |       |         |Africa   |         |
|     |           |     |Middle   |Africa     |         |        |East      |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|XNF  |Rest of    |95   |Africa   |Middle     |Africa   |D2      |North     |Africa |Non-Annex|Middle   |Africa   |
|     |North      |     |Latin    |East and   |         |        |Africa and|       |B        |East and |         |
|     |Africa     |     |America  |North      |         |        |Middle    |       |         |Africa   |         |
|     |           |     |Middle   |Africa     |         |        |East      |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|NGA  |Nigeria    |96   |Africa   |Sub-Saharan|Africa   |D2      |Tropical  |Africa |Non-Annex|Middle   |Africa   |
|     |           |     |Latin    |Africa     |         |        |Africa    |       |B        |East and |         |
|     |           |     |America  |           |         |        |          |       |         |Africa   |         |
|     |           |     |Middle   |           |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|SEN  |Senegal    |97   |Africa   |Sub-Saharan|Africa   |D3      |Tropical  |Africa |Non-Annex|Middle   |Africa   |
|     |           |     |Latin    |Africa     |         |        |Africa    |       |B        |East and |         |
|     |           |     |America  |           |         |        |          |       |         |Africa   |         |
|     |           |     |Middle   |           |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|XWF  |Rest of    |98   |Africa   |Sub-Saharan|Africa   |D3      |Tropical  |Africa |Non-Annex|Middle   |Africa   |
|     |Western    |     |Latin    |Africa     |         |        |Africa    |       |B        |East and |         |
|     |Africa     |     |America  |           |         |        |          |       |         |Africa   |         |
|     |           |     |Middle   |           |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|XCF  |Rest of    |99   |Africa   |Sub-Saharan|Africa   |D3      |Tropical  |Africa |Non-Annex|Middle   |Africa   |
|     |Central    |     |Latin    |Africa     |         |        |Africa    |       |B        |East and |         |
|     |Africa     |     |America  |           |         |        |          |       |         |Africa   |         |
|     |           |     |Middle   |           |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|XAC  |Rest of    |100  |Africa   |Sub-Saharan|Africa   |D3      |Tropical  |Africa |Non-Annex|Middle   |Africa   |
|     |South      |     |Latin    |Africa     |         |        |Africa    |       |B        |East and |         |
|     |Central    |     |America  |           |         |        |          |       |         |Africa   |         |
|     |Africa     |     |Middle   |           |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|ETH  |Ethiopia   |101  |Africa   |Sub-Saharan|Africa   |D3      |Tropical  |Africa |Non-Annex|Middle   |Africa   |
|     |           |     |Latin    |Africa     |         |        |Africa    |       |B        |East and |         |
|     |           |     |America  |           |         |        |          |       |         |Africa   |         |
|     |           |     |Middle   |           |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|MDG  |Madagascar |102  |Africa   |Sub-Saharan|Africa   |D3      |Tropical  |Africa |Non-Annex|Middle   |Africa   |
|     |           |     |Latin    |Africa     |         |        |Africa    |       |B        |East and |         |
|     |           |     |America  |           |         |        |          |       |         |Africa   |         |
|     |           |     |Middle   |           |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|MWI  |Malawi     |103  |Africa   |Sub-Saharan|Africa   |D3      |Tropical  |Africa |Non-Annex|Middle   |Africa   |
|     |           |     |Latin    |Africa     |         |        |Africa    |       |B        |East and |         |
|     |           |     |America  |           |         |        |          |       |         |Africa   |         |
|     |           |     |Middle   |           |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|MUS  |Mauritius  |104  |Africa   |Sub-Saharan|Africa   |D3      |Tropical  |Africa |Non-Annex|Middle   |Africa   |
|     |           |     |Latin    |Africa     |         |        |Africa    |       |B        |East and |         |
|     |           |     |America  |           |         |        |          |       |         |Africa   |         |
|     |           |     |Middle   |           |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|MOZ  |Mozambique |105  |Africa   |Sub-Saharan|Africa   |D3      |Tropical  |Africa |Non-Annex|Middle   |Africa   |
|     |           |     |Latin    |Africa     |         |        |Africa    |       |B        |East and |         |
|     |           |     |America  |           |         |        |          |       |         |Africa   |         |
|     |           |     |Middle   |           |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|TZA  |Tanzania   |106  |Africa   |Sub-Saharan|Africa   |D3      |Tropical  |Africa |Non-Annex|Middle   |Africa   |
|     |           |     |Latin    |Africa     |         |        |Africa    |       |B        |East and |         |
|     |           |     |America  |           |         |        |          |       |         |Africa   |         |
|     |           |     |Middle   |           |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|UGA  |Uganda     |107  |Africa   |Sub-Saharan|Africa   |D3      |Tropical  |Africa |Non-Annex|Middle   |Africa   |
|     |           |     |Latin    |Africa     |         |        |Africa    |       |B        |East and |         |
|     |           |     |America  |           |         |        |          |       |         |Africa   |         |
|     |           |     |Middle   |           |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|ZMB  |Zambia     |108  |Africa   |Sub-Saharan|Africa   |D3      |Tropical  |Africa |Non-Annex|Middle   |Africa   |
|     |           |     |Latin    |Africa     |         |        |Africa    |       |B        |East and |         |
|     |           |     |America  |           |         |        |          |       |         |Africa   |         |
|     |           |     |Middle   |           |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|ZWE  |Zimbabwe   |109  |Africa   |Sub-Saharan|Africa   |D2      |Tropical  |Africa |Non-Annex|Middle   |Africa   |
|     |           |     |Latin    |Africa     |         |        |Africa    |       |B        |East and |         |
|     |           |     |America  |           |         |        |          |       |         |Africa   |         |
|     |           |     |Middle   |           |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|XEC  |Rest of    |110  |Africa   |Sub-Saharan|Africa   |D2      |Tropical  |Africa |Non-Annex|Middle   |Africa   |
|     |Eastern    |     |Latin    |Africa     |         |        |Africa    |       |B        |East and |         |
|     |Africa     |     |America  |           |         |        |          |       |         |Africa   |         |
|     |           |     |Middle   |           |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|BWA  |Botswana   |111  |Africa   |Sub-Saharan|Africa   |D2      |Tropical  |Africa |Non-Annex|Middle   |Africa   |
|     |           |     |Latin    |Africa     |         |        |Africa    |       |B        |East and |         |
|     |           |     |America  |           |         |        |          |       |         |Africa   |         |
|     |           |     |Middle   |           |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|ZAF  |South      |112  |Africa   |Sub-Saharan|Africa   |D2      |Tropical  |Africa |Non-Annex|Middle   |Africa   |
|     |Africa     |     |Latin    |Africa     |         |        |Africa    |       |B        |East and |         |
|     |           |     |America  |           |         |        |          |       |         |Africa   |         |
|     |           |     |Middle   |           |         |        |          |       |         |         |         |
|     |           |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|XSC  |Rest of    |113  |Africa   |Sub-Saharan|Africa   |D2      |Tropical  |Africa |Non-Annex|Middle   |Africa   |
|     |South      |     |Latin    |Africa     |         |        |Africa    |       |B        |East and |         |
|     |African    |     |America  |           |         |        |          |       |         |Africa   |         |
|     |Customs    |     |Middle   |           |         |        |          |       |         |         |         |
|     |Union      |     |East     |           |         |        |          |       |         |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+
|XXA  |Antartica  |114  |0        |0          |Other    |0       |0         |0      |Non-Annex|0        |0        |
|     |           |     |         |           |         |        |          |       |B        |         |         |
+-----+-----------+-----+---------+-----------+---------+--------+----------+-------+---------+---------+---------+

.. [#GTAP]
   `https://www.gtap.agecon.purdue.edu/databases/regions.asp?Version=7.211 <https://www.gtap.agecon.purdue.edu/databases/regions.asp?Version=7.211>`_
