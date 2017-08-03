"""Helper class for managing custom emissions scenarios

A good test case for this would be trying to reproduce the RCP
emissions scenarios (from the array interface rather than 
the built-in interface).
"""
import numpy as np

_CDIAC_REGIONS = 115


class Projection(object):
    def __init__(self, values, region_index, n_regions, n_sectors, n_kinds,
                 kind, var):
        """Create a new projection object

        Parameters
        ----------
        values : np.ndarray
            Array of values representing emissions for each year 
            starting in the year 2000.  Optionally can be provided 
            as an array with 115 columns (one for each fine-grain
            region in the CDIAC data).  This allows emissions to be 
            controlled on a regional basis.  
        region_index : dict
            Dictionary mapping fine-grain region index to coarse-grain
            region index used in the model (the coarse-grain regional
            groupings are options in the model).  
        n_regions : int
            Number of coarse-grain regions used.
        n_sectors : int
            Number of sectors used.
        n_kinds : int
            Number of kinds used
        kind : int
            Index for kind used
        var : str
            String label for variable in question
        """
        self.values = values
        self.region_index = region_index
        self.n_regions = n_regions
        self.n_sectors = n_sectors
        self.n_kinds = n_kinds
        self.kind = kind
        self.var = var

        self.n_years = self.values.shape[0]

    def coarsen(self):
        """Coarsen the data to the specified set of regions"""
        coarsened = np.zeros((self.n_years, self.n_regions, self.n_sectors,
                              self.n_kinds, self.n_regions))
        one_dimensional = len(self.values.shape) == 1
        two_dimensional = len(self.values.shape) == 2
        if two_dimensional and (self.values.shape[1] == _CDIAC_REGIONS):
            for i in range(1, _CDIAC_REGIONS):
                # Sector always seems to be index zero
                coarsened[:, 0, 0, self.kind,
                          self.region_index[i]] += self.values[:, i]
        elif one_dimensional:
            # All emissions go into global region
            coarsened[:, 0, 0, self.kind, 0] = self.values
        else:
            raise ValueError('Specified emissions array for {} has improper shape.'
                             'Emissions must be either column vector specifying'
                             'global emissions with'
                             'length number of years since the year 2000'
                             'or it must be a 2D array specifying fine-grain'
                             'regional emissions for each region in the CDIAC'
                             'dataset.  Got array of shape {}'.format(self.var,
                                                                      self.values.shape)
            )
        return coarsened
