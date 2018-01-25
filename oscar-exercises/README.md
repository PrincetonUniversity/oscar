oscar-exercises
===============

This repository contains the lab exercises used in teaching ENV367 in the Fall
semester of 2017.  `instructor-versions` contains fully implemented "solution"
notebooks.  `student-versions` contains just the markdown descriptions of the
exercises as well as a few code snippets.  The notebooks contained in
`instructor-versions` should be able to be executed through to completion,
assuming the Python environment is set up properly and `OSCAR` is appropriately
installed.  

Downloading the repository and running tests
--------------------------------------------

You can download the repository by cloning it:
```
$ git clone https://github.com/PrincetonUniversity/oscar-exercises.git
```

Then you can check that the environment is setup properly by running the test suite.  This will run
each notebook individually (from the command line) and note whether there were
any errors and in which notebook(s) those errors occurred.  To run the test
suite start from the root of the repository and navigate to the `tests`
directory and execute the tests file using `pytest`.
```
$ cd oscar-exercises
$ cd tests
$ pytest -vv test_instructor_notebooks.py
```
Note that this requires that the `pytest` module is installed in your Python
environment.  This can be done via the following:
```
$ conda install -c conda-forge pytest
```
If successful, the output will look something like the following:
```
$ pytest -vv test_instructor_notebooks.py
================================================================ test session starts ================================================================
platform darwin -- Python 2.7.13, pytest-3.1.3, py-1.4.34, pluggy-0.4.0 -- //anaconda/envs/oscar-dev/bin/python
cachedir: .cache
rootdir:
/path/to/oscar-exercises/tests, inifile: collected 12 items

test_instructor_notebooks.py::test_notebooks[Lab1.1 (Instructor Version).ipynb] PASSED
test_instructor_notebooks.py::test_notebooks[Lab1.2 (Instructor Version).ipynb] PASSED
test_instructor_notebooks.py::test_notebooks[Lab2.1 (Instructor Version).ipynb] PASSED
test_instructor_notebooks.py::test_notebooks[Lab2.2 (Instructor Version).ipynb] PASSED
test_instructor_notebooks.py::test_notebooks[Lab3.1 (Instructor Version).ipynb] PASSED
test_instructor_notebooks.py::test_notebooks[Lab4.1 (Instructor Version).ipynb] PASSED
test_instructor_notebooks.py::test_notebooks[Lab5.1 (Instructor Version).ipynb] PASSED
test_instructor_notebooks.py::test_notebooks[Lab6.1 (Instructor Version).ipynb] PASSED
test_instructor_notebooks.py::test_notebooks[Lab7.2 (Instructor Version)-simplified.ipynb] PASSED
test_instructor_notebooks.py::test_notebooks[Reading data from a netCDF file.ipynb] PASSED
test_instructor_notebooks.py::test_notebooks[Lab7.1 (Instructor Version).ipynb] PASSED
test_instructor_notebooks.py::test_notebooks[Lab7.2 (Instructor Version) - complex version.ipynb] PASSED

======================================================= 12 passed in 2139.51 seconds ================================================================
```
