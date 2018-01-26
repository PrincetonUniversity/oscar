# OSCAR
The compact Earth system model used in teaching ENV367.

[![Build Status](https://jenkins.princeton.edu/buildStatus/icon?job=ENV367/oscar)](https://jenkins.princeton.edu/job/ENV367/job/oscar/)

**Installation**

One can install `OSCAR` by cloning the repository and installing via `pip`:
```
$ git clone https://github.com/PrincetonUniversity/oscar.git
$ cd oscar
$ pip install -e .
```

**Running the test suite**

To make sure the installation went properly, run the test suite in the command
line.  Note this requires the `pytest` utility, which one can install via:
```
$ conda install -c conda-forge pytest
```
To run the test suite from the root `oscar` directory, run:
```
$ pytest -vv oscar
```
If all the tests pass, then things should be all set!

**Reference**:

Gasser, T., P. Ciais, O. Boucher, Y. Quilcaille, M. Tortora, L. Bopp & D. Hauglustaine. "The compact Earth system model OSCAR v2.2: description and first results." *Geoscientific Model Development* 10: 271-319 (2017). [doi:10.5194/gmd-10-271-2017](https://doi.org/doi:10.5194/gmd-10-271-2017)
