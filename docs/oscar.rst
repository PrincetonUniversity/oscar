#####
Oscar
#####

Oscar can be configured using a diverse set of options to simulate a wide range
of climates, reflecting uncertainty in both past and future Earth system
forcing agents.

A simulation of ``OSCAR`` with its default parameters (see below) can be
created by creating an ``OSCAR`` object:

.. ipython:: python

   from oscar import OSCAR
   simulation = OSCAR()


Data sources
============

To simulate past climate, ``OSCAR`` relies on historical estimates of
greenhouse gas concentrations, aersol concentrations, volcanic eruptions,
changes in anthropegenic land use patterns, and more.  There is uncertainty
associated with these historical estimates, and there is often more than one
source for each estimate.  ``OSCAR`` enables users to experiment using different
historical data sources for the following parameters.

Greenhouse gases
----------------

data_EFF: str
    Dataset for fossil fuel emissions. Options are 'CDIAC' or 'EDGAR'. Default is 'CDIAC'.
