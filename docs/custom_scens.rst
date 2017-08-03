#######################################
Running with custom emissions scenarios
#######################################

In addition to the built-in scenarios, ``OSCAR`` can be configured to run with
custom scenarios of future emissions.  This gives the user complete control
over where, when, and how much of a particular chemical species is emitted in
the future (i.e. post year 2000).  This can be done by specifying an array
to one or more of the `scen` parameters in the ``OSCAR`` constructor.  The
array can either be one or two dimensional.  If the array is one-dimensional,
the emissions of a particular species will be distributed uniformly across the
globe, with the first value representing the emissions rate for the year 2000.
If the array is two-dimensional, the second dimension must have length 115; in
this case the array consists of 115 time series -- one time series of emissions
rates for each region in the GTAP dataset, plus one for Antarctica. The one-dimensional method is simplest, but the two-dimensional method allows
for finer-grained control of where the emissions are concentrated, which *can* have
an impact on the simulated results.

Custom emissions can be specified for the following keyword arguments in the
``OSCAR`` constructor: ``scen_EFF``, ``scen_ECH4``, ``scen_EN2O``, ``scen_SO2``, ``scen_ENH3``,
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

TODO(Spencer): Write documentation for regional method.
