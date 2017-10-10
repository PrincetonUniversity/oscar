"""Basic integration tests for OSCAR

These tests verify that we have not broken any aspect of OSCAR 
in adapting it for our needs.  These tests do not, however, test for any
possible bugs that already exist in OSCAR.  The values that are tested against
here are computed using the direct version of OSCAR from GitHub:
https://github.com/tgasser/OSCAR
"""
from collections import OrderedDict
import os

import numpy as np
import pandas as pd
import pytest

import oscar
from oscar import OSCAR, _TIME_DIAGNOSTICS

_TEST_PARAMS = [
        OrderedDict([('data_EFF', 'EDGAR')]),
        OrderedDict([('scen_ECH4', 'RCP8.5')]),
        OrderedDict([('data_EFF', 'EDGAR'),
                     ('mod_regionI', 'Kyoto')])
]
_IDS = ['-'.join(params.keys()) for params in _TEST_PARAMS]


def load_expected_data(end_year, parameter):
    path = 'data/{}-{}.csv'.format(parameter, end_year)
    data = np.loadtxt(path, skiprows=1)
    variables = _TIME_DIAGNOSTICS

    results = {}
    for j, v in enumerate(variables):
        results[v] = data[:, j]
    return results


@pytest.mark.parametrize('kwargs', _TEST_PARAMS, ids=_IDS)
def test_oscar(kwargs):
    end_year = 2100
    simulation = OSCAR(**kwargs)
    result = simulation.run(end_year)
    expected = load_expected_data(end_year, ' '.join(kwargs.keys()))
    for key, value in expected.iteritems():
        np.testing.assert_equal(value, result[key])


# Eventually it would be good to parametrize this to test all constituents
def test_custom_scenario_EFF_prescribed():
    ROOT = os.path.join(oscar.__path__[0], 'data')
    PATH = os.path.join(ROOT, 'EFossil_RCP/'
                        '#DATA.EFossil_RCP.2000-2100_5reg0.rcp85_EFF.csv')
    EFF_projection = np.loadtxt(PATH, delimiter=',', dtype=np.float32)
    global_EFF = np.sum(EFF_projection, axis=1)
    emissions = np.linspace(global_EFF[0], global_EFF[0] * 2., 101)
    result = OSCAR(scen_EFF=emissions,
                   mod_DATAscen='prescribed').run(2100)['EFF']['Total']
    np.testing.assert_allclose(result[300:], emissions, atol=1.0e-7)


def test_custom_scenario_EFF():
    ROOT = os.path.join(oscar.__path__[0], 'data')
    PATH = os.path.join(ROOT, 'EFossil_RCP/'
                        '#DATA.EFossil_RCP.2000-2100_5reg0.rcp85_EFF.csv')
    EFF_projection = np.loadtxt(PATH, delimiter=',', dtype=np.float32)
    global_EFF = np.sum(EFF_projection, axis=1)

    expected = OSCAR(scen_EFF='RCP8.5').run(2100)['D_gst']
    result = OSCAR(scen_EFF=global_EFF).run(2100)['D_gst']
    np.testing.assert_allclose(result, expected, atol=1.0e-5)


def test_custom_scenario_ECH4():
    built_in = OSCAR(scen_ECH4='ECH4', mod_DATAscen='raw').run(2100)
    global_ECH4 = built_in['ECH4']['Total'][300:]

    expected = built_in['D_gst']
    result = OSCAR(scen_ECH4=global_ECH4,
                   mod_DATAscen='raw').run(2100)['D_gst']
    np.testing.assert_allclose(result, expected, atol=1.0e-5)


def test_complex_custom_scenario():
    # Here we will test reproducing RCP results
    # directly from synthetic emissions defined for all 113 GTAP regions
    # plus Antarctica.
    ROOT = os.path.join(oscar.__path__[0], 'data')
    PATH = os.path.join(ROOT, 'EFossil_RCP/'
                        '#DATA.EFossil_RCP.2000-2100_5reg0.rcp85_EFF.csv')
    EFF_projection = np.loadtxt(PATH, delimiter=',', dtype=np.float32)

    regions = pd.read_csv(
        os.path.join(ROOT, 'Regions_GTAP/#DATA.Regions_GTAP.csv'))

    n_regions = len(regions['RCP5'].unique())
    partitions_per_region = {code:
                             regions['RCP5'][regions['RCP5'] == code].count()
                             for code in range(n_regions)}

    for i in range(n_regions):
        EFF_projection[:, i] /= partitions_per_region[i]
    GTAP_mapped_emissions = np.zeros((101, 115)).astype(np.float32)

    for i, code in enumerate(regions['RCP5']):
        GTAP_mapped_emissions[:, i + 1] = EFF_projection[:, code]

    result = OSCAR(scen_EFF=GTAP_mapped_emissions,
                   mod_regionI='RCP5').run(2100)['D_gst']
    expected = OSCAR(scen_EFF='RCP8.5', mod_regionI='RCP5').run(2100)['D_gst']
    np.testing.assert_allclose(result, expected, atol=1.0e-5)


def test_year_too_small_error():
    with pytest.raises(ValueError):
        OSCAR().run(2009)


def test_bad_scenario_input():
    case = OSCAR(scen_EFF=np.zeros((100, 2)))
    with pytest.raises(ValueError):
        case.run(2100)


@pytest.mark.parametrize(
    'biome',
    ['alb_des', 'alb_for', 'alb_shr', 'alb_gra', 'alb_cro', 'alb_pas'])
def test_albedo_error_global_biome_specific(biome):
    with pytest.raises(ValueError):
        OSCAR(**{'alb_global': 0.4, biome: 0.1})


def test_albedo_error_wFOR_wDES():
    with pytest.raises(ValueError):
        OSCAR(mod_biomeSHR='w/FOR',
              mod_biomeURB='w/DES',
              alb_for=0.1).run(2100)


def test_albedo_error_wFOR_URB():
    with pytest.raises(ValueError):
        OSCAR(mod_biomeSHR='w/FOR',
              mod_biomeURB='URB',
              alb_for=0.1).run(2100)


def test_albedo_error_wGRA_wDES():
    with pytest.raises(ValueError):
        OSCAR(mod_biomeSHR='w/GRA',
              mod_biomeURB='w/DES',
              alb_gra=0.1).run(2100)


def test_albedo_error_wGRA_URB():
    with pytest.raises(ValueError):
        OSCAR(mod_biomeSHR='w/GRA',
              mod_biomeURB='URB',
              alb_gra=0.1).run(2100)


def test_albedo_error_SHR_wDES():
    result = OSCAR(mod_biomeSHR='SHR',
                   mod_biomeURB='w/DES',
                   alb_for=0.1, alb_gra=0.1).run(2100)


def test_albedo_error_SHR_URB():
    result = OSCAR(mod_biomeSHR='SHR',
                   mod_biomeURB='URB',
                   alb_for=0.1, alb_gra=0.1).run(2100)


def test_set_global_mean_alb():
    result = OSCAR(alb_global=0.1).run(2100)
    assert np.abs(result['GLOBAL_MEAN_ALB'] - 0.1) < 0.0000001


def test_set_biome_mean_alb():
    result = OSCAR(alb_cro=0.1).run(2100)
    assert np.abs(result['BIOME_MEAN_ALB']['CRO'] - 0.1) < 0.0000001
