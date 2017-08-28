#########################################
Running with built-in emissions scenarios
#########################################

By default emissions are set to stop in year 2011 (e.g. see the plot of regional
fossil fuel emissions above).  This of course is
unrealistic.  There are a variety of built-in emissions scenarios one can
use for each chemical species that will define a time series for the emissions
of that species post-2011.  Some of these scenarios are more extreme than
others (for more information on the RCP emissions scenarios see [#RCP]_; for
more information  on the
SRES scenarios see [#SRES]_).

Convenience parameter
---------------------

For convenience, if one would like to set all emissions to be derived from a
certain scenario, one can use the ``scen_ALL`` option:

scen_ALL : None or str
    Option to set the scenario for all emissions.  Options are ``None``,
    ``'stop'``, ``'cst'``, ``'RCP8.5'``, ``'RCP6.0'``, ``'RCP4.5'``,
    ``'RCP2.6'``.  If ``None``, options must be set on an emissions species by
    emissions species basis.  Default is ``None``.

If one would like to configure emissions scenarios on a per-species basis, the
full list of configurable options within ``OSCAR`` for built-in emissions scenarios is
below:

Greenhouse gases
----------------

scen_EFF : str
    Scenario for fossil fuel emissions.  Options are ``'stop'``, ``'cst'``, 
    ``'SRES-A1B'``, ``'SRES-A1FI'``, ``'SRES-A1T'``, ``'SRES-A2'``, ``'SRES-B1'``,
    ``'SRES-B2'``, ``'RCP8.5'``, ``'RCP6.0'``, ``'RCP4.5'``, or ``'RCP2.6'``.  Default
    is ``'stop'``.
scen_ECH4 : str
    Scenario for methane emissions.  Options are ``'stop'``, ``'cst'``, 
    ``'SRES-A1B'``, ``'SRES-A1FI'``, ``'SRES-A1T'``, ``'SRES-A2'``, ``'SRES-B1'``,
    ``'SRES-B2'``, ``'RCP8.5'``, ``'RCP6.0'``, ``'RCP4.5'``, or ``'RCP2.6'``.  Default
    is ``'stop'``.
scen_N2O : str
    Scenario for nitrious oxide emissions.  Options are ``'stop'``, ``'cst'``,
    ``'SRES-A1B'``, ``'SRES-A1FI'``, ``'SRES-A1T'``, ``'SRES-A2'``, ``'SRES-B1'``,
    ``'SRES-B2'``, ``'RCP8.5'``, ``'RCP6.0'``, ``'RCP4.5'``, or ``'RCP2.6'``.  Default
    is ``'stop'``.

Aerosols
--------

scen_ESO2 : str
    Scenario for sulfur dioxide emissions.  Options are ``'stop'``, ``'cst'``,
    ``'SRES-A1B'``, ``'SRES-A1FI'``, ``'SRES-A1T'``, ``'SRES-A2'``, ``'SRES-B1'``,
    ``'SRES-B2'``, ``'RCP8.5'``, ``'RCP6.0'``, ``'RCP4.5'``, or ``'RCP2.6'``.  Default
    is ``'stop'``.
scen_ENH3 : str
    Scenario for ammonia emissions.  Options are ``'stop'``,
    ``'cst'``, ``'RCP8.5'``, ``'RCP6.0'``, ``'RCP4.5'``, or ``'RCP2.6'``.  Default is
    ``'stop'``.
scen_EOC : str
    Scenario for organic carbon aerosol emissions.  Options are ``'stop'``,
    ``'cst'``, ``'RCP8.5'``, ``'RCP6.0'``, ``'RCP4.5'``, or ``'RCP2.6'``.  Default is
    ``'stop'``.
scen_EBC : str
    Scenario for black carbon aerosol emissions.  Options are ``'stop'``,
    ``'cst'``, ``'RCP8.5'``, ``'RCP6.0'``, ``'RCP4.5'``, or ``'RCP2.6'``.  Default is
    ``'stop'``.
    
Halogenated compounds
---------------------

scen_Ehalo : str
    Scenario for halogenated compound emissions.  Options are ``'stop'``,
    ``'cst'``, ``'RCP8.5'``, ``'RCP6.0'``, ``'RCP4.5'``, or ``'RCP2.6'``.  Default is
    ``'stop'``.

Short-lived species
-------------------

scen_ENOX : str
    Scenario for nitrogen oxide emissions.  Options are ``'stop'``, ``'cst'``,
    ``'SRES-A1B'``, ``'SRES-A1FI'``, ``'SRES-A1T'``, ``'SRES-A2'``, ``'SRES-B1'``,
    ``'SRES-B2'``, ``'RCP8.5'``, ``'RCP6.0'``, ``'RCP4.5'``, or ``'RCP2.6'``.  Default
    is ``'stop'``.
scen_ECO : str
    Scenario for carbon monoxide emissions.  Options are ``'stop'``, ``'cst'``,
    ``'SRES-A1B'``, ``'SRES-A1FI'``, ``'SRES-A1T'``, ``'SRES-A2'``, ``'SRES-B1'``,
    ``'SRES-B2'``, ``'RCP8.5'``, ``'RCP6.0'``, ``'RCP4.5'``, or ``'RCP2.6'``.  Default
    is ``'stop'``.
scen_EVOC : str
    Scenario for volatile organic compounds.  Options are ``'stop'``, ``'cst'``,
    ``'SRES-A1B'``, ``'SRES-A1FI'``, ``'SRES-A1T'``, ``'SRES-A2'``, ``'SRES-B1'``,
    ``'SRES-B2'``, ``'RCP8.5'``, ``'RCP6.0'``, ``'RCP4.5'``, or ``'RCP2.6'``.  Default
    is ``'stop'``.

Anthropogenic forcings
----------------------

scen_LULCC : str
    Scenario for land-use and land-cover change.  Options are ``'stop'``,
    ``'cst'``, ``'RCP8.5'``, ``'RCP6.0'``, ``'RCP4.5'``, or ``'RCP2.6'``.  Default is
    ``'stop'``.
scen_HARV : str
    Scenario for wood harvest.  Options are ``'stop'``,
    ``'cst'``, ``'RCP8.5'``, ``'RCP6.0'``, ``'RCP4.5'``, or ``'RCP2.6'``.  Default is
    ``'stop'``.
scen_SHIFT : str
    Scenario for shifting cultivation.  Options are ``'stop'``,
    ``'cst'``, ``'RCP8.5'``, ``'RCP6.0'``, ``'RCP4.5'``, or ``'RCP2.6'``.  Default is
    ``'stop'``.
scen_RFant : str
    Scenario for other anthropogenic radiative forcing.  Options are
    ``'stop'`` and ``'cst'``.  Default is ``'stop'``.

Natural forcings
----------------

scen_RFnat : str
    Scenario for natural radiative forcing.  Options are ``'stop'`` and
    ``'cst'``.  Default is ``'stop'``.

.. [#RCP]
   Vuuren, D. P. van, Edmonds, J., Kainuma, M., Riahi, K., Thomson, A.,
   Hibbard, K., ... Rose, S. K. (2011). The representative concentration
   pathways: an overview. Climatic Change, 109(1–2), 5.
   `https://doi.org/10.1007/s10584-011-0148-z <https://doi.org/10.1007/s10584-011-0148-z>`_
   
.. [#SRES]
   Nakicenovic, N., & Swart, R. (2000). Special Report Emissions Scenarios.
   Cambridge University Press. Retrieved from
   `http://www.ipcc.ch/ipccreports/sres/emission/index.php?idp=0 <http://www.ipcc.ch/ipccreports/sres/emission/index.php?idp=0>`_
