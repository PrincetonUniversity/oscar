"""Helper class for managing custom emissions scenarios
"""
import numpy as np

_CDIAC_REGIONS = 115
_BIOMES = {'des', 'for', 'shr', 'gra', 'cro', 'pas', 'urb'}
_TOL = 10.


class LULCCScenario(object):
    def __init__(self, des2for=None, des2shr=None, des2gra=None, des2cro=None,
                 des2pas=None, des2urb=None, for2shr=None, for2gra=None,
                 for2cro=None, for2pas=None, for2urb=None, shr2gra=None,
                 shr2cro=None, shr2pas=None, shr2urb=None, gra2cro=None,
                 gra2pas=None, gra2urb=None, cro2pas=None, cro2urb=None,
                 pas2urb=None,
                 for2des=None, shr2des=None, gra2des=None, cro2des=None,
                 pas2des=None, urb2des=None, shr2for=None, gra2for=None,
                 cro2for=None, pas2for=None, urb2for=None, gra2shr=None,
                 cro2shr=None, pas2shr=None, urb2shr=None, cro2gra=None,
                 pas2gra=None, urb2gra=None, pas2cro=None, urb2cro=None,
                 urb2pas=None):
        """Create a new LULCCScenario object

        All arguments must contain only positive values.

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
        for2des : np.ndarray
            Transition from forest to desert biome [Mha yr^-1]
        shr2des : np.ndarray
            Transition from shrubland to desert biome [Mha yr^-1]
        gra2des : np.ndarray
            Transition from grassland to desert biome [Mha yr^-1]
        cro2des : np.ndarray
            Transition from cropland to desert biome [Mha yr^-1]
        pas2des : np.ndarray
            Transition from pasture to desert biome [Mha yr^-1]
        urb2des : np.ndarray
            Transition from urban to desert biome [Mha yr^-1]
        shr2for : np.ndarray
            Transition from shrubland to forest biome [Mha yr^-1]
        gra2for : np.ndarray
            Transition from grassland to forest biome [Mha yr^-1]
        cro2for : np.ndarray
            Transition from cropland to forest biome [Mha yr^-1]
        pas2for : np.ndarray
            Transition from pasture to forest biome [Mha yr^-1]
        urb2for : np.ndarray
            Transition from urban to forest biome [Mha yr^-1]
        gra2shr : np.ndarray
            Transition from grassland to shrubland biome [Mha yr^-1]
        cro2shr : np.ndarray
            Transition from cropland to shrubland biome [Mha yr^-1]
        pas2shr : np.ndarray
            Transition from pasture to shrubland biome [Mha yr^-1]
        urb2shr : np.ndarray
            Transition from urban to shrubland biome [Mha yr^-1]
        cro2gra : np.ndarray
            Transition from cropland to grassland biome [Mha yr^-1]
        pas2gra : np.ndarray
            Transition from pasture to grassland biome [Mha yr^-1]
        urb2gra : np.ndarray
            Transition from urban to grassland biome [Mha yr^-1]
        pas2cro : np.ndarray
            Transition from pasture to cropland biome [Mha yr^-1]
        urb2cro : np.ndarray
            Transition from urban to cropland biome [Mha yr^-1]
        urb2pas : np.ndarray
            Transition from urban to pasture biome [Mha yr^-1]
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
            ('pas', 'urb'): pas2urb,

            # Reverse transitions
            ('for', 'des'): for2des,
            ('shr', 'des'): shr2des,
            ('gra', 'des'): gra2des,
            ('cro', 'des'): cro2des,
            ('pas', 'des'): pas2des,
            ('urb', 'des'): urb2des,
            ('shr', 'for'): shr2for,
            ('gra', 'for'): gra2for,
            ('cro', 'for'): cro2for,
            ('pas', 'for'): pas2for,
            ('urb', 'for'): urb2for,
            ('gra', 'shr'): gra2shr,
            ('cro', 'shr'): cro2shr,
            ('pas', 'shr'): pas2shr,
            ('urb', 'shr'): urb2shr,
            ('cro', 'gra'): cro2gra,
            ('pas', 'gra'): pas2gra,
            ('urb', 'gra'): urb2gra,
            ('pas', 'cro'): pas2cro,
            ('urb', 'cro'): urb2cro,
            ('urb', 'pas'): urb2pas
        }
        reference_shape = self._assert_matching_shapes()
        self._zero_pad(reference_shape)
        self._assert_all_positive()
        self._assert_valid_pattern()

    def __contains__(self, obj):
        """This is so we don't need to change logic that checks if 'RCP' is in  
        a string specified to the scen_LULCC argument"""
        return False

    def _zero_pad(self, reference_shape):
        """Pad transitions dict with zeros wherever a value is None

        Parameters
        ----------
        reference_shape : tuple
            Shape to match in transitions dict
        """
        self.transitions_check = {}
        for key in self.transitions:
            if self.transitions[key] is None:
                self.transitions_check[key] = np.zeros(reference_shape)
            else:
                self.transitions_check[key] = self.transitions[key]

    def _assert_matching_shapes(self):
        """Raise a ValueError if there is a shape mismatch among transition
        timeseries arrays

        Returns
        -------
        reference_shape : tuple
            Shape of arrays in transitions dictionary
        """
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
        return reference_shape

    def _assert_all_positive(self):
        """All transition matrices must have positive values only"""
        for key, value in self.transitions_check.iteritems():
            if not all((value >= 0.0).ravel()):
                raise ValueError(
                    'All specified transition arrays must contain'
                    'positive values.  Offending array found for '
                    '{}2{}.  If one would like to specify area leaving '
                    '{} for a particular year one needs to specify a positive '
                    ' value for {}2{} and 0.0 for the year in {}2{}'.format(
                        key[0], key[1], key[1], key[1], key[0], key[0], key[1])
                )

    def _assert_valid_pattern(self):
        """Area must be approximately conserved across all regions and
        timesteps"""
        outgoing = {
            biome: [self.transitions_check[(biome, dest)] for dest in (_BIOMES - {biome})]
            for biome in _BIOMES
        }
        incoming = {
            biome: [self.transitions_check[(source, biome)] for source in (_BIOMES - {biome})]
            for biome in _BIOMES
        }
        for biome in _BIOMES:
            mean_residual = np.mean(np.abs(sum(incoming[biome]) -
                                           sum(outgoing[biome])))
            if mean_residual > _TOL:
                raise ValueError('Area not conserved in prescribed land use '
                                 'change scenario.  Problem in biome {}.  Mean '
                                 'residual of {:0.2f}'.format(
                                     biome, mean_residual))


class SHIFTScenario(LULCCScenario):
    pass


class HARVScenario(object):
    def __init__(self, desert=None, forest=None, shrubland=None,
                 grassland=None, cropland=None, pasture=None, urban=None):
        self.patterns = {
            'des': desert,
            'for': forest,
            'cro': cropland,
            'shr': shrubland,
            'gra': grassland,
            'pas': pasture,
            'urb': urban
        }
        reference_shape = self._assert_matching_shapes()

    def _assert_matching_shapes(self):
        """Raise a ValueError if there is a shape mismatch among
        timeseries arrays

        Returns
        -------
        reference_shape : tuple
            Shape of arrays in transitions dictionary
        """
        same = True
        reference_shape = None
        for key, value in self.patterns.iteritems():
            if (value is not None) and (reference_shape is None):
                reference_shape = value.shape
            if value is not None:
                same = (same & (value.shape == reference_shape))
        if not same:
            raise ValueError('All non-none transition fields must have the '
                             'same shape')
        return reference_shape

    def __contains__(self, obj):
        """This is so we don't need to change logic that checks if 'RCP' is in  
        a string specified to the scen_LULCC argument"""
        return False
