################
Output variables
################

``OSCAR`` generates output for a wide range of variables.  This is a
comprehensive list of possible outputs.  All variables are given as deviations
from the start year of the simulation (1700).  

TODO(Spencer): Include all possible outputs from the manual, not just the
default output diagnostics.

Simulated variables
===================

Greenhouse gas concentrations
-----------------------------

D_CO2 : np.array
    Deviation in concentration of carbon dioxide in the atmosphere [ppm]
D_CH4 : np.array
    Deviation of methane in the atmosphere [ppb]
D_N2O : np.array
    Deviation of nitrous oxide in the atmosphere [ppb]

Ozone
-----
D_O3t : np.array
    Deviation in tropospheric ozone [Dobson units]
D_O3s : np.array
    Deviation in stratospheric ozone [Dobson units]
    
Aerosol concentrations
----------------------

D_SO4 : np.array
    Deviation of sulfate aerosol in the atmosphere [Tg]
D_POA : np.array
    Deviation of primary organic aerosol in the atmosphere [Tg]
D_BC : np.array
    Deviation of black carbon aerosol in the atmosphere [Tg]
D_NO3 : np.array
    Deviation of nitrate aerosol in the atmosphere [Tg]
D_SOA : np.array
    Deviation of secondary organic aerosol in the atmosphere [Tg]
D_AERh : np.array
    Deviation of burden of all soluble aerosols [Tg]

Radiative forcings
------------------

RF : np.array
    Total radiative forcing of all forcing agents [W m^-2]
RF_halo : np.array
    Radiative forcing of halogenated compounds [W m^-2]
    
Temperature
-----------

D_gst : np.array
    Deviation in global mean surface temperature [K]

Ocean heat content
------------------

D_OHC : np.array
    Deviation in ocean heat content [ZJ]

Emissions
=========

``OSCAR`` is forced in part through emissions of greenhouse gases and aerosols.
These emissions are prescribed as inputs to the model depending on the data
source and emissions scenario used.  As part of the output dictionary ``OSCAR``
returns when it runs, ``OSCAR`` makes available the timeseries of emissions for
the following sources as dictionaries mapping region names to 1D-arrays
representing the time series of emissions for the respective region:

Greenhouse gases
----------------

EFF : dict
    Fossil fuel emissions [Gt yr^-1]
ECH4 : dict
    Methane emissions [Mt yr^-1]
EN2O : dict
    Nitrous oxide emissions [Mt yr^-1]

Aerosols
--------

ESO2 : dict
    Sulfur dioxide emissions [Mt yr^-1]
EOC : dict
    Organic carbon aerosol emissions [Mt yr^-1]
EBC : dict
    Black carbon aerosol emissions [Mt yr^-1]
ENH3 : dict
    Ammonia emissions [Mt yr^-1]
    
Short-lived species
-------------------

ENOX : dict
    Nitrogen oxide emissions [Mt yr^-1]
EVOC : dict
    Volatile organic compound emissions [Mt yr^-1]
ECO : dict
    Carbon monoxide emissions [Mt yr^-1]

Radiative forcing drivers
=========================

Finally, ``OSCAR`` is also driven by inputs of radiative forcings from various
natural and anthropogenic sources.  One can access the values used in a
particular simulation by selecting the following variables.

Natural
-------

RFsolar : np.array
    Timeseries of radiative forcing due to variations in solar output [W m^-2]
RFvolc : np.array
    Timeseries of radiative forcing due to volcanoes [W m^-2]

Anthropogenic
-------------

RFcon : np.array
    Radiative forcing of aviation contrails [W m^-2]
