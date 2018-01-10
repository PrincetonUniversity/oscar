################
Output variables
################

``OSCAR`` generates output for a wide range of variables. Most variables are given as deviations
from the start year of the simulation (1700).  

The variable names listed here can be used as string keys to the dictionary
returned by running ``OSCAR``.  As an example, we'll plot the deviation in
temperature from the start of the simulation with the default configuration.
Here we are using ``'D_gst'`` as a key to the ``results`` dictionary.

.. ipython:: python

   from oscar import OSCAR
   simulation = OSCAR()
   results = simulation.run(2100)

   import matplotlib.pyplot as plt
   fig, ax = plt.subplots(1, 1)
   time = 1700 + np.arange(len(results['D_gst']))
   
   ax.plot(time, results['D_gst'])
   ax.set_xlabel('Year')
   
   @savefig plot_basic_gst2.png width=100%
   ax.set_ylabel('$\Delta T$ [K]')

A comprehensive list of outputs can be found below.
   
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

Precipitation
-------------

D_gyp : np.array
    Deviation in global yearly precipitation [mm yr^-1]
D_lyp : dict
    Dictionary mapping region names to deviations in precipitation [mm yr^-1]
    
Temperature
-----------

D_gst : np.array
    Deviation in global mean surface temperature [K]
D_lst : dict
    Dictionary mapping region names to deviations in temperature [K]

Ocean properties
----------------

D_mld : np.array
    Deviation in ocean mixed layer depth [m]
D_dic : np.array
    Deviation of dissolved inorganic carbon [micro-mol kg^-1]
D_pH : np.array
    Deviation of pH of ocean [pH units]
OSNK : np.array
    Deviation in flux of carbon into ocean [Gt Carbon yr^-1]
D_sst : np.array
    Deviation in sea surface temperature [K]
D_OHC : np.array
    Deviation in ocean heat content [ZJ]
D_gst0 : np.array
    Deviation in global mean temperature of the deep ocean [K]

Simulated radiative forcings
----------------------------

RF : np.array
    Total radiative forcing of all forcing agents [W m^-2]
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
RF_halo : np.array
    Radiative forcing of halogenated compounds [W m^-2]
    
Atmospheric chemistry diagnostics
---------------------------------

D_OHSNK_CH4 : np.array
    Deviation in removal flux of methane due to tropospheric oxidation [Mt Carbon yr^-1]
D_HVSNK_CH4 : np.array
    Deviation in removal flux of methane due to stratospheric oxidation [Mt Carbon yr^-1]
D_XSNK_CH4 : np.array
    Deviation in removal flux of methane due to oxidation in dry soils and the oceanic boundary layer [Mt Carbon yr^-1]
D_HVSNK_N2O : np.array
    Deviation in removal flux of nitrous oxide due to stratospheric oxidation [Mt Nitrogen yr^-1]
D_EESC : np.array
    Deviation in equivalent effective stratospheric chlorine [ppt]
D_CH4_lag : np.array
    Deviation in stratospheric methane concentration [ppb]
D_N2O_lag : np.array
    Deviation in stratospheric nitrous oxide concentration [ppb]

Land surface diagnostics
------------------------

D_AREA : dict
    Dictionary mapping region names to dictionaries mapping biome names to deviations in area covered [Mha]
D_npp : dict
    Dictionary mapping region names to dictionaries mapping biome names to deviations in net primary productivity [Gt Carbon Mha^-1 yr^-1]
D_efire : dict
    Dictionary mapping region names to dictionaries mapping biome names to deviations in carbon flux from fires into the atmosphere [Gt Carbon Mha^-1 yr^-1]
D_fmort : dict
    Dictionary mapping region names to dictionaries mapping biome names to deviations in flux of carbon into carbon litter pool due to mortality [Gt Carbon Mha^-1 yr^-1]
D_rh1 : dict
    Dictionary mapping region names to dictionaries mapping biome names to deviations in heterotrophic respiration rate [Gt Carbon Mha^-1 yr^-1]
D_fmet : dict
    Dictionary mapping region names to dictionaries mapping biome names to deviations in flux of carbon into soil organic carbon due to metabolization [Gt Carbon Mha^-1 yr^-1]
D_rh2 : dict
    Dictionary mapping region names to dictionaries mapping biome names to deviations in heterotropic respiration in the soil carbon pool [Gt Carbon Mha^-1 yr^-1]
D_cveg : dict
    Dictionary mapping region names to dictionaries mapping biome names to deviations in living biomass [Gt Carbon Mha^-1]
D_csoil1 : dict
    Dictionary mapping region names to dictionaries mapping biome names to deviations in the carbon litter pool [Gt Carbon Mha^-1]
D_csoil2 : dict
    Dictionary mapping region names to dictionaries mapping biome names to deviations in soil carbon pool [Gt Carbon Mha^-1]
D_AWET : dict
    Dictionary mapping region names to time series arrays of deviation in wetland area [Mha]
D_ewet : dict
    Dictionary mapping region names to time series arrays of deviation in wetland carbon emissions [Mt Carbon Mha^-1 yr^-1]
D_EWET : dict
    Dictionary mapping region names to time series arrays of deviation in wetland carbon emissions [Mt Carbon yr^-1]
ELUC : dict
    Dictionary mapping region names to carbon emissions associated with land
use change [Gt C yr^-1] 

Biomass burning emissions
-------------------------

D_EBB_CO2 : dict
    Dictionary mapping region names to time series arrays of deviation of carbon dioxide emissions from biomass burning [Mt Carbon yr^-1]
D_EBB_CH4 : dict
    Dictionary mapping region names to time series arrays of deviation of methane emissions from biomass burning [Mt Carbon yr^-1]
D_EBB_N2O : dict
    Dictionary mapping region names to time series arrays of deviation of nitrous oxide emissions from biomass burning [Mt Nitrogen yr^-1]
D_EBB_NOX : dict
    Dictionary mapping region names to time series arrays of deviation of nitrogen oxide emissions from biomass burning [Mt Nitrogen yr^-1]
D_EBB_CO : dict
    Dictionary mapping region names to time series arrays of deviation of carbon monoxide emissions from biomass burning [Mt Carbon yr^-1]
D_EBB_VOC : dict
    Dictionary mapping region names to time series arrays of deviation of volatile organic carbon emissions from biomass burning [Mt yr^-1]
D_EBB_SO2 : dict
    Dictionary mapping region names to time series arrays of deviation of sulfur dioxide emissions from biomass burning [Mt Sulfur yr^-1]
D_EBB_NH3 : dict
    Dictionary mapping region names to time series arrays of deviation of ammonia emissions from biomass burning [Mt Nitrogen yr^-1]
D_EBB_OC : dict
    Dictionary mapping region names to time series arrays of deviation of organic carbon aerosol emissions from biomass burning [Mt Carbon yr^-1]
D_EBB_BC : dict
    Dictionary mapping region names to time series arrays of deviation of black carbon aerosol emissions from biomass burning [Mt Carbon yr^-1]
LSNK : np.array
    Deviation in flux of carbon into land carbon stores [Gt Carbon yr^-1]

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

Prescribed
----------

RFprescribed : np.array
    Prescribed radiative forcing via ``scen_RF`` argument [W m^-2]
    
Albedo
======

The albedo (percent of incident solar radiation reflected) is an important
parameter controlling the climate.  The albedo is prescribed in the model; it
can be adjusted in the ``OSCAR`` constructor (see the `albedo page
<albedo.html>`_ for more information). These three diagnostics describe the albedo
used in the model.

GLOBAL_MEAN_ALB : float
    Global mean albedo
BIOME_MEAN_ALB : dict
    Dictionary mapping biome names to biome-average albedos
REGION_MEAN_ALB : dict
    Dictionary mapping region names to region-average albedos

