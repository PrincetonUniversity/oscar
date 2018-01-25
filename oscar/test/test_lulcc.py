"""Integration tests of land use and land cover change module
"""
from itertools import permutations
import os

import numpy as np
import pytest

import oscar
from oscar import OSCAR, LULCCScenario, SHIFTScenario, HARVScenario


_BIOMES = ['des', 'for', 'shr', 'gra', 'cro', 'pas', 'urb']
_HARV_ARGS = ['desert', 'forest', 'shrubland', 'grassland', 'cropland',
              'pasture', 'urban']
_OPTIONS = ['{}2{}'.format(*pair) for pair in permutations(_BIOMES, 2)]


@pytst.mark.skip
def test_custom_scenario_LULCC():
    ROOT = os.path.join(oscar.__path__[0], 'data')
    PATH = os.path.join(
        ROOT,
        'LandUse_RCP/'
        '#DATA.LandUse_RCP_mean-TRENDYv2.2006-2100_114reg1.rcp85_LUC_{}.csv')
    transitions = {}
    for t in _OPTIONS:
        try:
            transitions[t] = np.pad(
                np.loadtxt(PATH.format(t), delimiter=','), [(0, 0), (1, 0)],
                'constant'
            )
        except IOError:
            transitions[t] = None
    scen_LULCC = LULCCScenario(**transitions)

    expected = OSCAR(scen_LULCC='RCP8.5').run(2100)['D_gst']
    result = OSCAR(scen_LULCC=scen_LULCC).run(2100)['D_gst']
    np.testing.assert_allclose(result, expected, atol=1.0e-5)


@pytest.mark.skip
def test_custom_scenario_SHIFT():
    ROOT = os.path.join(oscar.__path__[0], 'data')
    PATH = os.path.join(
        ROOT,
        'LandUse_RCP/'
        '#DATA.LandUse_RCP_mean-TRENDYv2.2006-2100_114reg1.rcp85_SHIFT_{}.csv')
    transitions = {}
    for t in _OPTIONS:
        try:
            transitions[t] = np.pad(
                np.loadtxt(PATH.format(t), delimiter=','), [(0, 0), (1, 0)],
                'constant'
            )
        except IOError:
            transitions[t] = None
    scen_SHIFT = SHIFTScenario(**transitions)

    expected = OSCAR(scen_SHIFT='RCP8.5').run(2100)['D_gst']
    result = OSCAR(scen_SHIFT=scen_SHIFT).run(2100)['D_gst']
    np.testing.assert_allclose(result, expected, atol=1.0e-5)


@pytest.mark.skip
def test_custom_scenario_HARV():
    ROOT = os.path.join(oscar.__path__[0], 'data')
    PATH = os.path.join(
        ROOT,
        'LandUse_RCP/'
        '#DATA.LandUse_RCP_mean-TRENDYv2.2006-2100_114reg1.rcp85_HARV_{}.csv')
    patterns = {}
    for t, b in zip(_HARV_ARGS, _BIOMES):
        try:
            patterns[t] = np.pad(
                np.loadtxt(PATH.format(b), delimiter=','), [(0, 0), (1, 0)],
                'constant'
            )
        except IOError:
            patterns[t] = None
    scen_HARV = HARVScenario(**patterns)

    expected = OSCAR(scen_HARV='RCP8.5').run(2100)['D_gst']
    result = OSCAR(scen_HARV=scen_HARV).run(2100)['D_gst']
    np.testing.assert_allclose(result, expected, atol=1.0e-5)
