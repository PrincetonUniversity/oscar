##########
Quickstart
##########

A simulation of ``OSCAR`` with its default parameters can be
created by creating an ``OSCAR`` object:

.. ipython:: python

   from oscar import OSCAR
   simulation = OSCAR()

Running ``OSCAR`` is as simple as executing the ``run`` command while providing
an end year:

.. ipython:: python

   results = simulation.run(2100)

``OSCAR`` stores the results in a Python dictionary, which maps variable names
to their values.  For instance, if we wanted to plot the change in temperature
from the start of the simulation we could write:

.. ipython:: python

   import matplotlib.pyplot as plt
   fig, ax = plt.subplots(1, 1)
   time = 1700 + np.arange(len(results['D_gst']))
   
   ax.plot(time, results['D_gst'])
   ax.set_xlabel('Year')
   
   @savefig plot_basic_gst.png width=100%
   ax.set_ylabel('$\Delta T$ [K]')

Output variables of ``OSCAR`` are stored as one-dimensional time series arrays.
They represent the annual mean deviation from the variable's value in the year
of the start of the simulation (1700).  Some drivers of the model are
partitioned among regions [e.g. ``'EFF'`` (fossil fuel emissions)].  These
variables are stored as dictionaries themselves, whose keys are region names
(e.g. ``'North America'``) mapping to one-dimensional time series arrays
representing the value of the variable over the given region.  To view all
regions included one can print the result of the ``keys`` method.  

.. ipython:: python

   print results['EFF'].keys()
   
If we would like to plot lines for each region's timeseries, we could write
something like this:

.. ipython:: python

   fig, ax = plt.subplots(1, 1)
   for region in results['EFF']:
       ax.plot(time, results['EFF'][region], label=region)

   ax.legend(loc='upper left', frameon=False)
   ax.set_ylabel('Emissions [Gt yr$^{-1}$]')
   ax.set_xlabel('Year')

   @savefig plot_EFF_regions.png width=100%
   ax.set_title('Fossil Fuel Emissions')

Configuring ``OSCAR``
---------------------

A simple experiment one can do is compare the projected evolution of future
temperature change between a simulation where emissions stop in 2011, and a simulation
where emissions follow an extreme emissions scenario (RCP8.5).  We can run the
model with the RCP8.5 scenario applied to all emissions with the following
code:

.. ipython:: python

   fig, ax = plt.subplots(1, 1)
   rcp85 = OSCAR(scen_ALL='RCP8.5')
   results_rcp85 = rcp85.run(2100)
   ax.plot(time, results['D_gst'], label='Stop in 2011')
   ax.plot(time, results_rcp85['D_gst'], label='RCP8.5')
   ax.set_xlabel('Year')
   ax.legend(loc='upper left')
   
   @savefig plot_compare_gst.png width=100%
   ax.set_ylabel('$\Delta T$ [K]')    

More advanced usage
-------------------
   
``OSCAR`` can be configured using a diverse set of options to simulate a wide range
of climates, reflecting uncertainty in both past and future Earth system
forcing agents.  Have a look at the remaining documentation for how to
customize individual ``OSCAR`` simulation instances to simulate a wide range
of future climates.
