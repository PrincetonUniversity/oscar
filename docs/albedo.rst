######
Albedo
######

In the real world, the albedo (fraction of incoming solar radiation reflected)
varies depending on the surface type; the darker the surface, the lower the
albedo.  In general, if more solar radiation is absorbed at the surface, the
planet will warm more.  In ``OSCAR`` a change in the global mean albedo can be induced by changes
in the partitioning of the area covered by various biomes (this is the
so-called "land-use and land-cover change" component of climate change).  

By default, ``OSCAR`` uses albedos derived from the GlobAlbedo [#Mul2012]_ or
MODIS [#LPDAAC]_ data
products.  If one would like to prescribe albedos, either for the entire globe,
or for specific biomes, one can do so within the ``OSCAR`` constructor.  Note
that setting both the albedo for specific biomes and for the global mean at the
same time is not enabled.  The relevant keyword arguments are:

alb_global : float
    Global mean albedo (must be between 0 and 1 or ``None``, default ``None``)
alb_des : float
    Albedo of desert biome (must be between 0 and 1 or ``None``, default ``None``)
alb_for : float
    Albedo of forest biome (must be between 0 and 1 or ``None``, default ``None``)
alb_shr : float
    Albedo of shrubland biome (must be between 0 and 1 or ``None``, default ``None``)
alb_gra : float
    Albedo of grassland biome (must be between 0 and 1 or ``None``, default ``None``)
alb_cro : float
    Albedo of cropland biome (must be between 0 and 1 or ``None``, default ``None``)
alb_pas : float
    Albedo of pasture biome (must be between 0 and 1 or ``None``, default ``None``)

Examples
========

To illustrate the impact of prescribing the albedo in the model (as well as the
albedo diagnostics), we will do two experiments.  In the first, we will simply
set the global albedo to be substantially greater than the default (which in
theory should cool the climate).  In the second, we will set the albedo of a
specific biome.

Increasing the global mean albedo
---------------------------------

.. ipython:: python

    from oscar import OSCAR

    default = OSCAR(scen_ALL='RCP8.5')
    results_default = default.run(2100)
    print(results_default['global_mean_alb'])

Here we can see that the global mean albedo is about 0.2.  Let's set the global
mean albedo to 0.5, and observe how this changes the temperature response of
the model.

.. ipython:: python

    from oscar import OSCAR

    higher_alb = OSCAR(scen_ALL='RCP8.5', alb_global=0.5)
    results_higher_alb = higher_alb.run(2100)

First, we'll verify that indeed the global mean albedo is what we prescribed it
to be:

.. ipython:: python

    print(results_higher_alb['global_mean_alb'])

Next, we'll plot the time series in global mean temperature deviation for each
simulation:

.. ipython:: python

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(1, 1)
    time = 1700 + np.arange(len(results_default['D_gst']))
    
    ax.plot(time, results_default['D_gst'], label='Default')
    ax.plot(time, results_higher_alb['D_gst'], label='Albedo = 0.5')
    ax.legend(loc='lower right')
    ax.set_xlabel('Year')
   
    @savefig plot_global_alb.png width=100%
    ax.set_ylabel('$\Delta T$ [K]')

Here it is clear that increasing the albedo (making the surface more
reflective) decreases the temperature relative to a simulation with the default
albedo. 

Decreasing the albedo of cropland
---------------------------------

Here we will decrease the albedo of cropland to half of its default value and
see its impact on temperature.  First we'll show what the default albedo of
cropland is by printing out the ``biome_mean_alb`` diagnostic from the
simulation wtih default parameters:

.. ipython:: python

    print(results_default['biome_mean_alb'])

Next, we'll run a simulation cutting that value in half, and plot the time
series of global mean temperature deviation:
    
.. ipython:: python

    half_alb_cro = OSCAR(scen_ALL='RCP8.5',
                         alb_cro=0.5 * results_default['biome_mean_alb']['CRO'])
    results_half_alb_cro = half_alb_cro.run(2100)
    fig, ax = plt.subplots(1, 1)
    ax.plot(time, results_default['D_gst'], label='Default')
    ax.plot(time, results_half_alb_cro['D_gst'],
            label='Cropland Albedo = {:0.3f}'.format(results_half_alb_cro['biome_mean_alb']['CRO']))
    ax.legend(loc='lower right')
    ax.set_xlabel('Year')
             
    @savefig plot_biome_alb_gst.png width=100%
    ax.set_ylabel('$\Delta T$ [K]')

So, as expected, decreasing the cropland albedo increases the global temperature.
    
.. [#Mul2012]
   Muller, J.-P., López, G., Watson, G., Shane, N., Kennedy, T., Yuen, P.,
   Lewis, P., Fischer, J., Guanter, L., Domench, C., Preusker, R., North, P.,
   Heckel, A., Danne, O., Krämer, U., M., Z., Brockmann, C., and Pinnock, S.:
   The ESA GlobAlbedo project for mapping the Earth’s land surface albedo for
   15 years from European sensors, available at:
   `http://www.globalbedo.org/global.php <http://www.globalbedo.org/global.php>`_, 2012.

.. [#LPDAAC]
   LPDAAC: Albedo 16-Day L3 Global 0.05Deg CMG, available at:
   `https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43c3
   <https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mcd43c3>`_.
