"""Script that runs the instructor notebooks for each week through to
completion. Tests to make sure instructor notebooks are compatible with the
installed version of OSCAR."""
import os
import sys

import nbformat
import pytest


from collections import OrderedDict
from glob import glob
from nbconvert.preprocessors import ExecutePreprocessor


FILE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
ROOT, DIR = os.path.split(FILE_PATH)
WEEK_PATH = os.path.join(ROOT, 'oscar-exercises',
                         'instructor-versions', 'Week-{:d}')


def run_notebook(notebook):
    """Execute all cells in order in a notebook

    Parameters
    ----------
    notebooks : str
        Absolute path to a Jupyter notebook
    """
    nb_path, _ = os.path.split(notebook)
    with open(notebook) as nb_file:
        nb = nbformat.read(nb_file, as_version=nbformat.NO_CONVERT)
    kernel_name = 'python{}'.format(str(sys.version[0]))
    ep = ExecutePreprocessor(timeout=1200, kernel_name=kernel_name)
    ep.preprocess(nb, {'metadata': {'path': nb_path}})


def find_notebooks(n_weeks):
    """Find all notebooks for the given number of weeks

    Parameters
    ----------
    n_weeks : int
        Number of weeks in the course

    Returns
    -------
    OrderedDict mapping notebook names to the absolute path to each notebook
    """
    notebooks = []
    for week in range(1, n_weeks + 1):
        week_path = WEEK_PATH.format(week)
        nb_paths = glob(os.path.join(week_path, '*.ipynb'))
        if nb_paths:
            nb_dirs, nb_names = zip(*[os.path.split(nb) for nb in nb_paths])
            notebooks.extend(zip(nb_names, nb_paths))
    return OrderedDict(notebooks)


N_WEEKS = 7
_NOTEBOOKS = find_notebooks(N_WEEKS)


@pytest.mark.parametrize(
    'notebook', _NOTEBOOKS.values(), ids=_NOTEBOOKS.keys())
def test_notebooks(notebook):
    run_notebook(notebook)
