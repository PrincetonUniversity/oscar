############
Data sources
############

To simulate past climate, ``OSCAR`` relies on historical estimates of
greenhouse gas concentrations, aerosol concentrations, volcanic eruptions,
changes in anthropegenic land use patterns, and more.  There is uncertainty
associated with these historical estimates, and there is often more than one
source for each estimate.  ``OSCAR`` enables users to experiment using different
historical data sources for the following parameters.

Greenhouse gases
----------------

data_EFF: str
    Dataset for fossil fuel emissions. Options are ``'CDIAC'`` or ``'EDGAR'``. Default is ``'CDIAC'``.
data_ECH4: str
    Dataset for methane emissions.  Options are ``'EDGAR'``, ``'ACCMIP'``, or ``'EPA'``.  Default is ``'EDGAR'``.
data_EN2O: str
    Dataset for nitrous oxide emissions.  Options are ``'EDGAR'`` or ``'EPA'``. Default is ``'EDGAR'``.

Aerosols
--------

data_ESO2: str
    Dataset for sulfur dioxide emissions.  Options are ``'EDGAR'`` or ``'ACCMIP'``.  Default is ``'EDGAR'``.
data_ENH3: str
    Dataset for ammonia emissions.  Options are ``'EDGAR'`` or ``'ACCMIP'``. Default is ``'EDGAR'``.
data_EOC: str
    Dataset for organic carbon emissions.  Only option is ``'ACCMIP'``.
data_EBC: str
    Dataset for black carbon emissions.  Only option is ``'ACCMIP'``.

Halogenated compounds
---------------------
data_Ehalo: str
    Dataset for halogenated compound emissions.  Only option is ``'EDGAR'``.

Short-lived species
-------------------

data_ENOX: str
    Dataset for nitrogen oxide emissions.  Options are ``'EDGAR'`` or ``'ACCMIP'``.  Default is ``'EDGAR'``.
data_ECO: str
    Dataset for carbon monoxide emissions.  Options are ``'EDGAR'`` or ``'ACCMIP'``.  Default is ``'EDGAR'``.
data_EVOC: str
    Dataset for volatile organic compound emissions.  Options are ``'EDGAR'`` or ``'ACCMIP'``.  Default is ``'EDGAR'``.

Radiative forcings
------------------

data_RFant: str
    Dataset for other anthropogenic radiative forcings.  Options are ``''``, or ``'IPCC-AR5'``.  Default is ``'IPCC-AR5'``.
data_RFnat: str
    Dataset for natural radiative forcings.  Options are ``''``, or ``'IPCC-AR5'``.  Default is ``'IPCC-AR5'``.
