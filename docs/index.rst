.. oscar documentation master file, created by
   sphinx-quickstart on Sat Jun 10 10:31:00 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _main-page:

###################################
oscar: a compact Earth system model
###################################

This documentation describes an adaptation of the OSCAR compact Earth system model for use in
the Princeton course, `Modeling the Earth System: Assessing Strategies for
Mitigating Climate Change (ENV367) <https://registrar.princeton.edu/course-offerings/course_details.xml?courseid=014229&term=1182>`_.  The model was originally developed by Gasser et al. in 2017
[#GMD]_.  This is a work in progress.  

TODO(Spencer): add high-level summary of the model here

Documentation
=============
.. toctree::
   :maxdepth: 1

   quickstart.rst
   outputs.rst
   data_sources.rst
   built_in_scens.rst
   custom_scens.rst
   regions.rst
   albedo.rst
   api.rst

Resources
=========

- For learning the fundamentals of the Python language, a nice introduction can
  be found in Jake VanderPlas's `A Whirlwind Tour of Python
  <http://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf>`_.
  The PDF is accompanied by `18 Jupyter notebooks <http://nbviewer.jupyter.org/github/jakevdp/WhirlwindTourOfPython/blob/master/Index.ipynb>`_, with code snippets
  demonstrating key concepts.
- For learning how to use ``matplotlib``, the recommended plotting library for
  use in plotting data produced by ``OSCAR``,  the
  `tutorial <https://matplotlib.org/users/pyplot_tutorial.html>`_ in
  ``matplotlib``'s official documentation is a good starting point.
- Similarly, for an introduction to ``numpy``, the `Quickstart tutorial
  <https://docs.scipy.org/doc/numpy-dev/user/quickstart.html>`_ in ``numpy``'s
  official documentation is also helpful.
  
See also
========

- The original source code for the model used in this course is based on `can be found on GitHub <https://github.com/tgasser/OSCAR>`_.
- The source code was released as a companion to a paper that appeared in
  Geoscientific Model Development in 2017 [#GMD]_

.. [#GMD]
   Gasser, T., Ciais, P., Boucher, O., Quilcaille, Y., Tortora, M., Bopp, L., &
   Hauglustaine, D. (2017). The compact Earth system model OSCAR v2.2:
   description and first results. Geosci. Model Dev., 10(1), 271–319.
   `https://doi.org/10.5194/gmd-10-271-2017 <https://doi.org/10.5194/gmd-10-271-2017>`_
   
