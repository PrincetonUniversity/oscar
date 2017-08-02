"""Basic integration tests for OSCAR

These tests verify that we have not broken any aspect of OSCAR 
in adapting it for our needs.  These tests do not, however, test for any
possible bugs that already exist in OSCAR.  The values that are tested against
here are computed using the direct version of OSCAR from GitHub:
https://github.com/tgasser/OSCAR
"""
from collections import OrderedDict

import numpy as np
import pytest

from oscar import OSCAR, _DEFAULT_OUTPUT_DIAGNOSTICS

_TEST_PARAMS = [
        OrderedDict([('data_EFF', 'EDGAR')]),
        OrderedDict([('scen_ECH4', 'RCP8.5')]),
        OrderedDict([('data_EFF', 'EDGAR'),
                     ('mod_regionI', 'Kyoto')])
]


def load_expected_data(end_year, parameter):
    path = 'data/{}-{}.csv'.format(parameter, end_year)
    data = np.loadtxt(path, skiprows=1)
    variables = _DEFAULT_OUTPUT_DIAGNOSTICS

    results = {}
    for j, v in enumerate(variables):
        results[v] = data[:, j]
    return results


@pytest.mark.parametrize(
    'kwargs',
    _TEST_PARAMS,
    ids=['-'.join(params.keys()) for params in _TEST_PARAMS])
def test_oscar(kwargs):
    end_year = 2100
    simulation = OSCAR(**kwargs)
    result = simulation.run(end_year)
    expected = load_expected_data(end_year, ' '.join(kwargs.keys()))
    for key, value in expected.iteritems():
        np.testing.assert_equal(value, result[key])
