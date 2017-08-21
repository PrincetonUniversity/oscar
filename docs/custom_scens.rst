#######################################
Running with custom emissions scenarios
#######################################

In addition to the built-in scenarios, ``OSCAR`` can be configured to run with
custom scenarios of future emissions.  This gives the user complete control
over where, when, and how much of a particular chemical species is emitted in
the future (i.e. post year 2000).  This can be done by specifying an array
to one or more of the ``scen`` parameters in the ``OSCAR`` constructor.  The
array can either be one or two dimensional.  If the array is one-dimensional,
the emissions of a particular species will be distributed uniformly across the
globe, with the first value representing the emissions rate for the year 2000.

If the array is two-dimensional, the second dimension must have length 115; in
this case the array consists of 115 time series -- one time series of zeros (to
pad the array to allow for column numbers in numpy, which start at zero, to align with GTAP region
numbers, which start at one), one time series of emissions
rates for each region in the GTAP dataset, plus one for Antarctica. The
one-dimensional method is simplest, but the two-dimensional method allows for
finer-grained control of where the emissions are concentrated, which *can* have
an impact on the simulated results; the impact, however, is negligible and
therefore it is recommended to use the simpler global method.  Note in the real
world the regional distribution of emissions, particularly for species with short
atmospheric lifetimes, like aerosols, likely does have a significant impact on
climate. [#SHI2009]_

Custom emissions can be specified for the following keyword arguments in the
``OSCAR`` constructor: ``scen_EFF``, ``scen_ECH4``, ``scen_EN2O``, ``scen_ESO2``, ``scen_ENH3``,
``scen_EOC``, ``scen_EBC``, ``scen_ENOX``, ``scen_ECO``, ``scen_EVOC``.

Global method
=============

Here will we demonstrate specifying a custom emissions scenario for fossil fuel
emissions globally.  We'll see what happens if we double the emissions released
during the built-in RCP8.5 emissions scenario.

We'll start out by creating and running a case using the ``'RCP8.5'`` emissions
scenario for fossil fuel emissions, and we'll pick off the total fossil fuel emissions from
the results of the run.

.. ipython:: python

    from oscar import OSCAR

    rcp85 = OSCAR(scen_EFF='RCP8.5')
    rcp85_results = rcp85.run(2100)
    rcp85_EFF = rcp85_results['EFF']['Total']

Then we'll create a new instance of ``OSCAR``, but this time specify double the
fossil fuel emissions from the previously created case.  Note that when
specifying a new emissions scenario, the emissions start in the year 2000, but
the emissions reported from running the model start in the year 1700.
Therefore we need to slice the emissions array from index 300 onward to select
just the emissions post year 1999.  In addition, we will set the
``mod_DATAscen`` keyword to ``'raw'`` to indicate that we do not want any
smoothing to take place at the boundary between the historical (pre-2000) and
future emissions (post-2000).

.. ipython:: python

    double_rcp85 = OSCAR(scen_EFF=2. * rcp85_EFF[300:], mod_DATAscen='raw')
    double_rcp85_results = double_rcp85.run(2100)

Finally, if we plot the results we can see (as expected) that the temperature
is significantly warmer in the case with twice the fossil fuel emissions.

.. ipython:: python

    import numpy as np
    import matplotlib.pyplot as plt

    time = 1700 + np.arange(len(rcp85_EFF))

    fig, ax = plt.subplots(1, 1)
    ax.plot(time, rcp85_results['D_gst'], label='Standard RCP8.5 EFF')
    ax.plot(time, double_rcp85_results['D_gst'], label='Double RCP8.5 EFF')
    ax.set_xlabel('Year')
    ax.set_ylabel('$\Delta T$ [K]')
    
    @savefig plot_double_rcp85_EFF.png width=100%
    ax.legend(loc='upper left')


Regional method
===============

To demonstrate the regional method of specifying future emissions, we will do
a sensitivity experiment.  We will see how sensitive the solution in deviation
in global temperature is to the region where sulfate aerosols
are emitted.  We will compare the solution from the default built-in emissions
scenario for sulfate aerosols released realistically across regions, to the same total of emissions
emitted in each of the RCP5 regions alone.

Again, we'll start with the basic simulation and pick off the total emissions
from the last 101 years of the simulation.

.. ipython:: python

    import numpy as np
    from oscar import OSCAR

    rcp85 = OSCAR(scen_ESO2='RCP8.5', mod_regionI='RCP5')
    rcp85_results = rcp85.run(2100)
    rcp85_ESO2 = rcp85_results['ESO2']['Total'][300:]
    time = np.arange(len(rcp85_results['D_gst'])) + 1700

This time though, we'll place these emissions in particular locations.  To do
so we'll need to identify 6 GTAP regions that are in the 6 RCP5 regions (Bunker
fuels, Asia region, Latin America, Middle-East & Africa, OECD countries in 1990, and
Reforming countries); we can do so by looking at the table in `GTAP Regions
<regions.html>`_.

There we find that simple candidate locations to place the emissions are:

- Bunker fuels: Antarctica (index 114)
- Asia region: China (index 4)
- Latin America:  Mexico (index 27)
- Middle-East & Africa: Iran (index 89)
- OECD countries in 1990: Australia (index 1)
- Reforming countries: Cyprus (index 48)

We'll store these index values in a dictionary for future use:

.. ipython:: python

    rcp_to_gtap = {'Bunker fuels': 114,         # Antarctica
                   'Asia region': 4,            # China
                   'Latin America': 27,         # Mexico
                   'Middle-East & Africa': 89,  # Iran
                   'OECD countries in 1990': 1, # Australia
                   'Reforming countries': 48}   # Cyprus

Then we'll create a dictionary to store the regional emission patterns of
sulfur dioxide.  For each region, we'll place the total sulfur dioxide
emissions from the reference case in the appropriate GTAP region column. 
                   
.. ipython:: python
             
    regional_ESO2 = {region: np.zeros((101, 115)) for region in rcp_to_gtap}
    for region in regional_ESO2:
        regional_ESO2[region][:, rcp_to_gtap[region]] = rcp85_ESO2

Then we'll run the simulations, storing the results in a
dictionary mapping the region where all emissions were released to the results
dictionary produced by running each simulation.
        
.. ipython:: python
        
    results = {region: OSCAR(scen_ESO2=regional_ESO2[region],
                             mod_regionI='RCP5').run(2100)
               for region in regional_ESO2}

We can show that the emissions (post year 2000) were emitted in the appropriate
regions by plotting the emissions.
               
.. ipython:: python

    fig, axes = plt.subplots(2, 3, sharex=True, sharey=True)
    fig.set_size_inches(8, 4)

    axes = axes.flatten()  # Convert to a 1D list
    
    for ax, (region, data) in zip(axes, results.iteritems()):
        ax.set_title(region)
        for reg, emissions in data['ESO2'].iteritems():
            ax.plot(time, emissions, label=reg)

    axes[4].legend(loc='upper center',
                   bbox_to_anchor=(0.5, -0.17),
                   ncol=5, fancybox=True, fontsize=8)
    axes[0].set_ylabel('SO2 Emissions [Mt yr$\mathregular{^{-1}}$]')
    axes[3].set_ylabel('SO2 Emissions [Mt yr$\mathregular{^{-1}}$]')

    @savefig plot_regional_emissions_ESO2.png width=100%
    fig.tight_layout()

Finally, what impact does this have on the results of the simulation (e.g. the
deviation in global mean temperature)?  We can determine this by plotting the
difference in simulated temperature deviation in the cases with regionally
concentrated emissions and the default case with a realistic regional
distribution of emissions.

.. ipython:: python

   fig, ax = plt.subplots(1, 1)
   for region in results:
       ax.plot(time, results[region]['D_gst'] - rcp85_results['D_gst'],
               label=region)
   ax.legend()

   @savefig plot_regional_temp_ESO2.png width=100%   
   ax.set_ylabel('$\mathregular{\Delta T}$ [K]')

We find that the region of sulfur dioxide emissions only produces differences
in simulated temperature deviation, *in this particular model*, on the order of
one-hundredth of a degree Kelvin.  How does this compare with the difference in
temperature deviation between a case with RCP8.5 sulfur dioxide emissions and a
case with no future emissions?

.. ipython:: python

   no_emissions = OSCAR(mod_regionI='RCP5')
   results_no_emissions = no_emissions.run(2100)

   fig, ax = plt.subplots(1, 1)
   ax.plot(time, rcp85_results['D_gst'] - results_no_emissions['D_gst'])

   @savefig plot_diff_no_emissions.png width=100%
   ax.set_ylabel('$\mathregular{\Delta T}$ [K]')

As expected, the addition of sulfate aerosols into the atmosphere cools the
climate; the maximum cooling observed is about 0.25 K.  This means that the
difference in regional distribution of emissions creates a range of solutions
within about 5% of the total change.  This is more or less negligible.
Therefore it is recommended to stick with the simpler global method specifying emissions.
   
.. [#SHI2009] Shindell, D., & Faluvegi, G. (2009). Climate response to regional
              radiative forcing during the twentieth century. Nature Geoscience, 2(4),
              294–300. https://doi.org/10.1038/ngeo473
