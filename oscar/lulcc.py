"""Helper class for managing custom emissions scenarios

A good test case for this would be trying to reproduce the RCP
emissions scenarios (from the array interface rather than 
the built-in interface).
"""
import numpy as np

_CDIAC_REGIONS = 115


class LULCCScenario(object):
    def __init__(self, des2for=None, des2shr=None, des2gra=None, des2cro=None,
                 des2pas=None, des2urb=None, for2shr=None, for2gra=None,
                 for2cro=None, for2pas=None, for2urb=None, shr2gra=None,
                 shr2cro=None, shr2pas=None, shr2urb=None, gra2cro=None,
                 gra2pas=None, gra2urb=None, cro2pas=None, cro2urb=None,
                 pas2urb=None):
        """Create a new projection object

        Parameters
        ----------
        des2for : np.ndarray
            Transition from desert to forest biome [Mha yr^-1]
        des2shr : np.ndarray
            Transition from desert to shrubland biome [Mha yr^-1]
        des2gra : np.ndarray
            Transition from desert to grassland biome [Mha yr^-1]
        des2cro : np.ndarray
            Transition from desert to cropland biome [Mha yr^-1]
        des2pas : np.ndarray
            Transition from desert to pasture biome [Mha yr^-1]
        des2urb : np.ndarray
            Transition from desert to urban biome [Mha yr^-1]
        for2shr : np.ndarray
            Transition from forest to shrubland biome [Mha yr^-1]
        for2gra : np.ndarray
            Transition from forest to grassland biome [Mha yr^-1]
        for2cro : np.ndarray
            Transition from forest to cropland biome [Mha yr^-1]
        for2pas : np.ndarray
            Transition from forest to pasture biome [Mha yr^-1]
        for2urb : np.ndarray
            Transition from forest to urban biome [Mha yr^-1]
        shr2gra : np.ndarray
            Transition from shrubland to grassland biome [Mha yr^-1]
        shr2cro : np.ndarray
            Transition from shrubland to cropland biome [Mha yr^-1]
        shr2pas : np.ndarray
            Transition from shrubland to pasture biome [Mha yr^-1]
        shr2urb : np.ndarray
            Transition from shrubland to urban biome [Mha yr^-1]
        gra2cro : np.ndarray
            Transition from grassland to cropland biome [Mha yr^-1]
        gra2pas : np.ndarray
            Transition from grassland to pasture biome [Mha yr^-1]
        gra2urb : np.ndarray
            Transition from grassland to urban biome [Mha yr^-1]
        cro2pas : np.ndarray
            Transition from cropland to pasture biome [Mha yr^-1]
        cro2urb : np.ndarray
            Transition from cropland to urban biome [Mha yr^-1]
        pas2urb : np.ndarray
            Transition from pasture to urban biome [Mha yr^-1]
        """
        self.transitions = {
            ('des', 'for'): des2for,
            ('des', 'shr'): des2shr,
            ('des', 'gra'): des2gra,
            ('des', 'cro'): des2cro,
            ('des', 'pas'): des2pas,
            ('des', 'urb'): des2urb,
            ('for', 'shr'): for2shr,
            ('for', 'gra'): for2gra,
            ('for', 'cro'): for2cro,
            ('for', 'pas'): for2pas,
            ('for', 'urb'): for2urb,
            ('shr', 'gra'): shr2gra,
            ('shr', 'cro'): shr2cro,
            ('shr', 'pas'): shr2pas,
            ('shr', 'urb'): shr2urb,
            ('gra', 'cro'): gra2cro,
            ('gra', 'pas'): gra2pas,
            ('gra', 'urb'): gra2urb,
            ('cro', 'pas'): cro2pas,
            ('cro', 'urb'): cro2urb,
            ('pas', 'urb'): pas2urb
        }
        # Check shape of all specified transitions
        same = True
        reference_shape = None
        for key, value in self.transitions.iteritems():
            if (value is not None) and (reference_shape is None):
                reference_shape = value.shape
            if value is not None:
                same = (same & (value.shape == reference_shape))
        if not same:
            raise ValueError('All non-none transition fields must have the '
                             'same shape')

    def __contains__(self, obj):
        return False
