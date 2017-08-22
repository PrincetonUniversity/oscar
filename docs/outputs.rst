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

Simulated radiative forcings
----------------------------

RF_CO2 : np.array
    Radiative forcing of carbon [W m^-2]
RF_CH4 : np.array
    Radiative forcing of methane [W m^-2]
RF_H2Os : np.array
    Radiative forcing of stratospheric water vapor [W m^-2]
RF_N2O : np.array
    Radiative forcing of nitrous oxide [W m^-2]
RF_SO4 : np.array
    Radiative forcing of sulfate aerosols [W m^-2]
RF_BC : np.array
    Radiative forcing of black carbon aerosols [W m^-2]
RF_POA : np.array
    Radiative forcing of primary organic aerosols [W m^-2]
RF_cloud : np.array
    Radiative forcing of aerosol cloud interactions [W m^-2]
RF_BCsnow : np.array
    Radiative forcing of black carbon on snow [W m^-2]
RF_LCC : np.array
    Radiative forcing of land cover change [W m^-2]
RF_O3t : np.array
    Radiative forcing of tropospheric ozone [W m^-2]
RF_O3s : np.array
    Radiative forcing of stratospheric ozone [W m^-2]
RF_NO3 : np.array
    Radiative forcing of nitrate aerosols [W m^-2]
RF_SOA : np.array
    Radiative forcing of secondary organic aerosols [W m^-2]
    
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

Halogenated compounds
---------------------

EHFC : dict
    Hydrofluorocarbon emissions [kt yr^-1]
EPFC : dict
    Perfluorocarbon emissions [kt yr^-1]
EODS : dict
    Ozone-depleting substance emissions [kt yr^-1]
    
Radiative forcing drivers
=========================

``OSCAR`` is also driven by inputs of radiative forcings from various
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

Albedo
======

The albedo (percent of incident solar radiation reflected) is an important
parameter controlling the climate.  The albedo is prescribed in the model; it
can be adjusted in the ``OSCAR`` constructor (see the `albedo page
<albedo.html>`_ for more information). These three diagnostics describe the albedo
used in the model.

global_mean_alb : float
    Global mean albedo
biome_mean_alb : dict
    Dictionary mapping biome names to biome-average albedos
region_mean_alb : dict
    Dictionary mapping region names to region-average albedos

