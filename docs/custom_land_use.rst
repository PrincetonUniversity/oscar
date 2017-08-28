#############################################
Running with custom land use change scenarios
#############################################

Changes in land use and land coverage have a powerful impact on climate.  While
built-in scenarios exist for prescribing future changes in land use, wood
harvest, and land cultivation, in can be interesting to create your own.  The
process for creating a custom land-use change scenario begins with creating any
of three scenario objects:

1. ``LULCCScenario``: land use and land cover change scenario (requires
   prescribing transitions of land use between biomes)
2. ``HARVScenario``: wood harvest scenario (requires prescribing a mass of carbon
   harvested for wood in specific biomes)
3. ``SHIFTScenario``: shifting cultivation scenario (requires prescribing
   shifts in cultivation between biomes)

We will demonstrate the use of one of these objects through an experiment where
we look at the impact of *reversing* the changes in land use that occured
during the 20th century, but using the RCP8.5 scenario for all other climate
drivers in the 21st century.

The impact of reversing land use changes
----------------------------------------

To start out, we'll create a reference control simulation (just RCP8.5 for all
21st century drivers, including land use change):

.. ipython:: python

    from oscar import OSCAR

    control = OSCAR(scen_ALL='RCP8.5').run(2100)

Next, we'll load in the data used to prescribe the land use changes in the
historical period, and create a ``LULCCScenario`` object with the last 100
years of that data, but inverted; inverting the data requires reversing the
time series and swapping the arrays used for the transitions (e.g. ``cro2gra``
<-> ``gra2cro``).  In total, there are 42 possible transitions; we can create
these using the built-in ``itertools`` library:

.. ipython:: python

    from itertools import permutations

    biomes = ['des', 'for', 'shr', 'gra', 'cro', 'pas', 'urb']
    transitions = ['{}2{}'.format(*pair) for pair in permutations(biomes, 2)]
    print transitions

``transitions`` is now a list of all possible transition strings (which are
used to identify where the data is stored in reference files).  We'll now load
in the data from the files:

.. ipython:: python

    import os
    import oscar

    root = os.path.join(oscar.__path__[0], 'data')
    path = os.path.join(
        root, 'LandUse_LUH1',
        '#DATA.LandUse_LUH1_mean-TRENDYv2.1501-2015_114reg1.LUC_{}.csv')

These preliminaries allow us to construct a path to the reference data file for
the historical period transition between grassland and shrubland with the
following command:

.. ipython:: python

    example = path.format('gra2shr')

We can now put together our list of transitions and generic file path to
construct a dictionary mapping argument names to arrays read in from files:

.. ipython:: python

    import numpy as np
             
    reference = {}
    for transition in transitions:
        try:
            filename = path.format(transition)
            data = np.loadtxt(filename, delimiter=',')
            reference[transition] = np.pad(data, [(0, 0), (1, 0)], 'constant')
        except IOError:
            reference[transition] = None  # Not all transitions occur in the data

Here, we are sure to make sure the array is padded with a column of zeros in
the begninning using the ``np.pad`` function; this formats the array such that
time increases with increasing row index, and (as for custom emissions
scenarios) columns at index 1 to 114 (inclusive) represent the GTAP regions
described in `regions <regions.html>`_.  Now we will construct the
``LULCCScenario`` object.  We'll start by creating a dictionary mapping a
transition key (e.g. ``'gra2shr'``) to its reverse (``'shr2gra'``).  Then we'll
create a dictionary storing the arguments we'll provide to the
``LULCCScenario`` constructor:

.. ipython:: python

    reverses = {t: '{}2{}'.format(t[4:], t[:3]) for t in transitions}
    scenario_kwargs = {}
    for transition, reverse in reverses.iteritems():
        if reference[transition] is not None:
            scenario_kwargs[reverse] = reference[transition][-100:, :][::-1, :]
        else:
            scenario_kwargs[reverse] = reference[transition]
    
Now, we'll construct the ``LULCCScenario`` object, configure all other drivers
to use the RCP8.5 scenario, and run the simulation:

.. ipython:: python

    from oscar import LULCCScenario

    scenario = LULCCScenario(**scenario_kwargs)
    experiment = OSCAR(scen_LULCC=scenario, scen_EFF='RCP8.5',
                       scen_ECH4='RCP8.5', scen_EN2O='RCP8.5',
                       scen_ESO2='RCP8.5', scen_ENH3='RCP8.5',
                       scen_EOC='RCP8.5', scen_EBC='RCP8.5',
                       scen_Ehalo='RCP8.5', scen_ENOX='RCP8.5',
                       scen_ECO='RCP8.5', scen_EVOC='RCP8.5',
                       scen_HARV='RCP8.5', scen_SHIFT='RCP8.5',
                       scen_RFant='RCP8.5', scen_RFnat='RCP8.5')
    result = experiment.run(2100)

Finally, we can plot the results to see the difference:

.. ipython:: python

    import matplotlib.pyplot as plt

    time = 1700 + np.arange(len(control['D_gst']))

    fig, ax = plt.subplots(1, 1)
    ax.plot(time, control['D_gst'], label='Standard RCP8.5')
    ax.plot(time, result['D_gst'], label='Land Use Reversed')
    ax.set_xlabel('Year')
    ax.set_ylabel('$\Delta T$ [K]')
    
    @savefig plot_reverse_land_use_temp.png width=100%
    ax.legend(loc='upper left')

To verify that our transitions were done properly, let's plot the deviation in
area for the cropland biome in Europe:

 .. ipython:: python

    fig, ax = plt.subplots(1, 1)
    ax.plot(time, control['D_AREA']['Europe']['Cropland'], label='Standard RCP8.5')
    ax.plot(time, result['D_AREA']['Europe']['Cropland'], label='Land Use Reversed')
    ax.set_xlabel('Year')
    ax.set_ylabel('Deviation in Area [Mha]')

    @savefig plot_reverse_land_use_area.png width=100%
    ax.legend(loc='upper left')

Did the change in land use have little effect on all regions or were the
offsetting differences that led the solutions to be very similar for global
temperature?  Let's look at regional temperature deviations.
    
.. ipython:: python

    import matplotlib.pyplot as plt

    time = 1700 + np.arange(len(control['D_gst']))

    fig, ax = plt.subplots(1, 1)
    ax.plot(time, control['D_lst']['Europe'], label='Standard RCP8.5')
    ax.plot(time, result['D_lst']['Europe'], label='Land Use Reversed')
    ax.set_xlabel('Year')
    ax.set_ylabel('$\Delta T$ [K]')
    
    @savefig plot_reverse_land_use_europe_temp.png width=100%
    ax.legend(loc='upper left')
