import os
import warnings

from functools import partial

import numpy as np

_PATH = os.path.dirname(__file__)

# Diagnosed fields (can be passed to the var_output argument of OSCAR_lite)
_TIME_DIAGNOSTICS = [
    'D_mld', 'D_dic', 'D_pH', 'OSNK', 'LSNK', 'D_OHSNK_CH4', 'D_HVSNK_CH4',
    'D_XSNK_CH4', 'D_HVSNK_N2O', 'D_O3t', 'D_EESC', 'D_O3s',
    'D_SO4', 'D_POA', 'D_BC', 'D_NO3', 'D_SOA', 'D_AERh', 'D_CO2', 'D_CH4',
    'D_CH4_lag', 'D_N2O', 'D_N2O_lag', 'RF', 'RF_warm', 'RF_atm', 'RF_CO2',
    'RF_CH4', 'RF_H2Os', 'RF_N2O', 'RF_halo', 'RF_O3t', 'RF_O3s', 'RF_SO4',
    'RF_POA', 'RF_BC', 'RF_NO3', 'RF_SOA', 'RF_cloud', 'RF_BCsnow', 'RF_LCC',
    'D_gst', 'D_sst', 'D_gyp', 'D_OHC', 'D_gst0'
]
_TIME_REGION_BIOME_DIAGNOSTICS = [
    'D_AREA', 'D_npp', 'D_efire', 'D_fmort', 'D_rh1', 'D_fmet', 'D_rh2',
    'D_cveg', 'D_csoil1', 'D_csoil2'
]
_TIME_REGION_DIAGNOSTICS = [
    'D_AWET', 'D_EWET', 'D_ewet', 'D_EBB_CO2', 'D_EBB_CH4',
    'D_EBB_N2O', 'D_EBB_NOX', 'D_EBB_CO', 'D_EBB_VOC', 'D_EBB_SO2',
    'D_EBB_NH3', 'D_EBB_OC', 'D_EBB_BC', 'D_lst', 'D_lyp'
]
_OUTPUT_DIAGNOSTICS = (_TIME_DIAGNOSTICS + _TIME_REGION_DIAGNOSTICS +
                       _TIME_REGION_BIOME_DIAGNOSTICS)
_VAR_TYPES = {}
for var in _TIME_DIAGNOSTICS:
    _VAR_TYPES[var] = 'time'
for var in _TIME_REGION_DIAGNOSTICS:
    _VAR_TYPES[var] = 'time-region'
for var in _TIME_REGION_BIOME_DIAGNOSTICS:
    _VAR_TYPES[var] = 'time-region-biome'

# Prescribed fields (need to be extracted from OSCAR-loadD.py)
_SIMPLE_EMISSIONS = [
    'EFF', 'ECH4', 'EN2O', 'ENOX', 'ECO', 'EVOC', 'ESO2', 'ENH3',
    'EOC', 'EBC'
]
_COMPLEX_EMISSIONS = [
    'EHFC', 'EPFC', 'EODS'
]
_RF_DRIVERS = [
    'RFsolar', 'RFvolc', 'RFcon', 'RFprescribed'
]
_ALBEDO = [
    'BIOME_MEAN_ALB', 'REGION_MEAN_ALB', 'GLOBAL_MEAN_ALB'
]


def unpack_regions(regions, data, simple=True):
    """Converts a 2D array of columns with regional data to a dictionary
    mapping region names to 1D arrays"""
    result = {}
    for i, region in enumerate(regions):
        if simple:
            result[region] = data[:, i]
        else:
            result[region] = np.sum(data[:, i, :], axis=1)
    return result


def unpack_regions_and_biomes(regions, biomes, data):
    """Converts a 3D array to a nested dictionary mapping region names to
    dictionaries mapping biome names to 1D time series arrays"""
    result = {}
    for i, region in enumerate(regions):
        result[region] = {biome: data[..., i, j]
                          for j, biome in enumerate(biomes)}
    return result


def sum_dict(data):
    """Sums arrays stored in a dict"""
    return sum([values for key, values in data.items()])


def _merge_dicts(*dict_args):
    """Merge the given dictionaries into single dict.
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    From http://stackoverflow.com/a/26853961/1706640
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


class OSCAR(object):
    """Wrapper class to safely run OSCAR in a notebook setting"""
    def __init__(self, fT=1, mod_regionI='Houghton', mod_biomeSHR='w/GRA',
                 mod_biomeURB='w/DES', data_EFF='CDIAC', data_LULCC='LUH1',
                 data_ECH4='EDGAR', data_EN2O='EDGAR', data_Ehalo='EDGAR',
                 data_ENOX='EDGAR', data_ECO='EDGAR', data_EVOC='EDGAR',
                 data_ESO2='EDGAR', data_ENH3='EDGAR', data_EOC='ACCMIP',
                 data_EBC='ACCMIP', data_RFant='IPCC-AR5',
                 data_RFnat='IPCC-AR5', mod_DATAscen='trends', scen_ALL=None,
                 scen_EFF='stop', scen_LULCC='stop', scen_HARV='stop',
                 scen_SHIFT='stop', scen_ECH4='stop',
                 scen_EN2O='stop', scen_Ehalo='stop', scen_ENOX='stop',
                 scen_ECO='stop', scen_EVOC='stop', scen_ESO2='stop',
                 scen_ENH3='stop', scen_EOC='stop', scen_EBC='stop',
                 scen_RFant='stop', scen_RFnat='stop', scen_RF=None,
                 alb_des=None, alb_for=None, alb_shr=None, alb_gra=None,
                 alb_cro=None, alb_pas=None, alb_global=None):
        """Create and configure an instance of OSCAR

        Parameters
        ----------
        fT : int
            Flag to turn climate feedbacks on (1) or off (0).  Default is 1.
        mod_regionI : str
            Regional aggregation setting.  Options are ``'SRES4'``, 'SRES11',
            'RECCAP*', 'Raupach*', 'Houghton', 'IMACLIM', 'Kyoto', 'RCP5',
            'RCP10*'.  Default is 'Houghton'.
        mod_biomeSHR : str
            Shrubland biome classification.  Options are 'SHR', 'w/GRA' or
            'w/FOR'. Default is 'w/GRA'.
        mod_biomeURB : str
            Urban biome classification.  Options are 'URB' or 'w/DES'.  Default
            is 'w/DES'.
        data_EFF : str
            Dataset for fossil fuel emissions.  Options are 'CDIAC' or 'EDGAR'.
            Default is 'CDIAC'.
        data_LULCC : str
            Dataset for land-use and land-cover change drivers.  Only option is
            'LUH1'
        data_ECH4 : str
            Dataset for methane emissions.  Options are 'EDGAR', 'ACCMIP', or 
            'EPA'.  Default is 'EDGAR'.
        data_EN2O : str
            Dataset for nitrous oxide emissions.  Options are 'EDGAR' or 'EPA'.
            Default is 'EDGAR'.
        data_Ehalo : str
            Dataset for halogenated compound emissions.  Only option is
            'EDGAR'.
        data_ENOX : str
            Dataset for nitrogen oxide emissions.  Options are 'EDGAR' or
            'ACCMIP'.  Default is 'EDGAR'.
        data_ECO : str
            Dataset for carbon monoxide emissions.  Options are 'EDGAR' or
            'ACCMIP'.  Default is 'EDGAR'.
        data_EVOC : str
            Dataset for volotile organic compound emissions.  Options are 
            'EDGAR' or 'ACCMIP'.  Default is 'EDGAR'.
        data_ESO2 : str
            Dataset for sulfur dioxide emissions.  Options are 'EDGAR' or 
            'ACCMIP'.  Default is 'EDGAR'.
        data_ENH3 : str
            Dataset for ammonia emissions.  Options are 'EDGAR' or 'ACCMIP'.
            Default is 'EDGAR'.
        data_EOC : str
            Dataset for organic carbon emissions.  Only option is 'ACCMIP'.
        data_EBC : str
            Dataset for black carbon emissions.  Only option is 'ACCMIP'.
        data_RFant : str
            Dataset for other anthropogenic radiative forcings.  Options are
            '', or 'IPCC-AR5'.  Default is 'IPCC-AR5'.
        data_RFnat : str
            Dataset for natural radiative forcings.  Options are '', or
            'IPCC-AR5'.  Default is 'IPCC-AR5'.
        mod_DATAscen : str
            How the transition between historical emissions and scenarios is
            defined.  Options are 'raw', 'offset', 'smoothX' (X in years),
            'trends', or 'prescribed'.  Default is 'trends'.
        scen_ALL : None or str
            Option to set the scenario for all emissions.  Options are None,
            'stop', 'cst', 'RCP8.5', 'RCP6.0', 'RCP4.5', 'RCP2.6'.  If None,
            options must be set on an emissions species by emissions species
            basis.  Default is None.
        scen_EFF : str
            Scenario for fossil fuel emissions.  Options are 'stop', 'cst', 
            'SRES-A1B', 'SRES-A1FI', 'SRES-A1T', 'SRES-A2', 'SRES-B1',
            'SRES-B2', 'RCP8.5', 'RCP6.0', 'RCP4.5', or 'RCP2.6'.  Default
            is 'stop'.
        scen_LULCC : str
            Scenario for land-use and land-cover change.  Options are 'stop',
            'cst', 'RCP8.5', 'RCP6.0', 'RCP4.5', or 'RCP2.6'.  Default is
            'stop'.
        scen_HARV : str
            Scenario for wood harvest.  Options are 'stop',
            'cst', 'RCP8.5', 'RCP6.0', 'RCP4.5', or 'RCP2.6'.  Default is
            'stop'.
        scen_SHIFT : str
            Scenario for shifting cultivation.  Options are 'stop',
            'cst', 'RCP8.5', 'RCP6.0', 'RCP4.5', or 'RCP2.6'.  Default is
            'stop'.
        scen_ECH4 : str
            Scenario for methane emissions.  Options are 'stop', 'cst', 
            'SRES-A1B', 'SRES-A1FI', 'SRES-A1T', 'SRES-A2', 'SRES-B1',
            'SRES-B2', 'RCP8.5', 'RCP6.0', 'RCP4.5', or 'RCP2.6'.  Default
            is 'stop'.
        scen_N2O : str
            Scenario for nitrious oxide emissions.  Options are 'stop', 'cst',
            'SRES-A1B', 'SRES-A1FI', 'SRES-A1T', 'SRES-A2', 'SRES-B1',
            'SRES-B2', 'RCP8.5', 'RCP6.0', 'RCP4.5', or 'RCP2.6'.  Default
            is 'stop'.
        scen_Ehalo : str
            Scenario for halogenated compound emissions.  Options are 'stop',
            'cst', 'RCP8.5', 'RCP6.0', 'RCP4.5', or 'RCP2.6'.  Default is
            'stop'.
        scen_ENOX : str
            Scenario for nitrogen oxide emissions.  Options are 'stop', 'cst',
            'SRES-A1B', 'SRES-A1FI', 'SRES-A1T', 'SRES-A2', 'SRES-B1',
            'SRES-B2', 'RCP8.5', 'RCP6.0', 'RCP4.5', or 'RCP2.6'.  Default
            is 'stop'.
        scen_ECO : str
            Scenario for carbon monoxide emissions.  Options are 'stop', 'cst',
            'SRES-A1B', 'SRES-A1FI', 'SRES-A1T', 'SRES-A2', 'SRES-B1',
            'SRES-B2', 'RCP8.5', 'RCP6.0', 'RCP4.5', or 'RCP2.6'.  Default
            is 'stop'.
        scen_EVOC : str
            Scenario for volatile organic compounds.  Options are 'stop', 'cst',
            'SRES-A1B', 'SRES-A1FI', 'SRES-A1T', 'SRES-A2', 'SRES-B1',
            'SRES-B2', 'RCP8.5', 'RCP6.0', 'RCP4.5', or 'RCP2.6'.  Default
            is 'stop'.
        scen_ESO2 : str
            Scenario for sulfur dioxide emissions.  Options are 'stop', 'cst',
            'SRES-A1B', 'SRES-A1FI', 'SRES-A1T', 'SRES-A2', 'SRES-B1',
            'SRES-B2', 'RCP8.5', 'RCP6.0', 'RCP4.5', or 'RCP2.6'.  Default
            is 'stop'.
        scen_ENH3 : str
            Scenario for ammonia emissions.  Options are 'stop',
            'cst', 'RCP8.5', 'RCP6.0', 'RCP4.5', or 'RCP2.6'.  Default is
            'stop'.
        scen_EOC : str
            Scenario for organic carbon aerosol emissions.  Options are 'stop',
            'cst', 'RCP8.5', 'RCP6.0', 'RCP4.5', or 'RCP2.6'.  Default is
            'stop'.
        scen_EBC : str
            Scenario for black carbon aerosol emissions.  Options are 'stop',
            'cst', 'RCP8.5', 'RCP6.0', 'RCP4.5', or 'RCP2.6'.  Default is
            'stop'.
        scen_RFant : str
            Scenario for other anthropogenic radiative forcing.  Options are
            'stop' and 'cst'.  Default is 'stop'.
        scen_RFnat : str
            Scenario for natural radiative forcing.  Options are 'stop' and
            'cst'.  Default is 'stop'.
        scen_RF : np.ndarray or None
            Scenario for prescribed radiative forcing.  Must be a np.ndarray or
            None.  Prescribed radiative forcing starts in year 2000.
            'cst'.  Default is None.
        alb_des : float
            Albedo of desert biome (must be between 0 and 1 or None)
        alb_for : float
            Albedo of forest biome (must be between 0 and 1 or None)
        alb_shr : float
            Albedo of shrubland biome (must be between 0 and 1 or None)
        alb_gra : float
            Albedo of grassland biome (must be between 0 and 1 or None)
        alb_cro : float
            Albedo of cropland biome (must be between 0 and 1 or None)
        alb_pas : float
            Albedo of pasture biome (must be between 0 and 1 or None)
        alb_global : float
            Albedo of the globe (must be between 0 and 1 or None)
        """
        self.fT = fT
        self.mod_regionI = mod_regionI
        self.data_EFF = data_EFF
        self.data_LULCC = data_LULCC
        self.data_ECH4 = data_ECH4
        self.data_EN2O = data_EN2O
        self.data_Ehalo = data_Ehalo
        self.data_ENOX = data_ENOX
        self.data_ECO = data_ECO
        self.data_EVOC = data_EVOC
        self.data_ESO2 = data_ESO2
        self.data_ENH3 = data_ENH3
        self.data_EOC = data_EOC
        self.data_EBC = data_EBC
        self.data_RFant = data_RFant
        self.data_RFnat = data_RFnat
        self.mod_DATAscen = mod_DATAscen
        self.mod_biomeSHR = mod_biomeSHR
        self.mod_biomeURB = mod_biomeURB
        self.scen_ALL = scen_ALL

        # Albedos
        self.albedos = {
            'des': alb_des,
            'for': alb_for,
            'shr': alb_shr,
            'gra': alb_gra,
            'cro': alb_cro,
            'pas': alb_pas
        }
        self.alb_global = alb_global
        if (alb_global is not None) and not all(alb is None for alb in
                                                self.albedos.values()):
            raise ValueError('Cannot set both biome-specific albedos and a '
                             'global mean albedo in the same simulation.')

        if scen_ALL is not None:
            self.scen_EFF = scen_ALL
            self.scen_LULCC = scen_ALL
            self.scen_HARV = scen_ALL
            self.scen_SHIFT = scen_ALL
            self.scen_ECH4 = scen_ALL
            self.scen_EN2O = scen_ALL
            self.scen_Ehalo = scen_ALL
            self.scen_ENOX = scen_ALL
            self.scen_ECO = scen_ALL
            self.scen_EVOC = scen_ALL
            self.scen_ESO2 = scen_ALL
            self.scen_ENH3 = scen_ALL
            self.scen_EOC = scen_ALL
            self.scen_EBC = scen_ALL
            self.scen_RFant = scen_ALL
            self.scen_RFnat = scen_ALL
        else:
            self.scen_EFF = scen_EFF
            self.scen_LULCC = scen_LULCC
            self.scen_HARV = scen_HARV
            self.scen_SHIFT = scen_SHIFT
            self.scen_ECH4 = scen_ECH4
            self.scen_EN2O = scen_EN2O
            self.scen_Ehalo = scen_Ehalo
            self.scen_ENOX = scen_ENOX
            self.scen_ECO = scen_ECO
            self.scen_EVOC = scen_EVOC
            self.scen_ESO2 = scen_ESO2
            self.scen_ENH3 = scen_ENH3
            self.scen_EOC = scen_EOC
            self.scen_EBC = scen_EBC
            self.scen_RFant = scen_RFant
            self.scen_RFnat = scen_RFnat
            self.scen_RF = scen_RF

    def run(self, end_year):
        """Run model for specified number of years

        Parameters
        ----------
        end_year : int
            Final year of simulation [> 1700 (simulation start)]

        Returns
        -------
        dict
            A mapping of variable names to 1D timeseries arrays or dictionaries
        """
        # Suppress numpy divide by zero warnings
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            locals()['_PATH'] = _PATH

            execfile(os.path.join(_PATH, 'OSCAR.py'), locals())

            ind_final = end_year - 1700
            if ind_final < 310:
                raise ValueError('For the model to run properly, the end_year '
                                 'must be greater than 2009; '
                                 'got end_year = {}.'.format(end_year))

            fT = self.fT
            mod_regionI = self.mod_regionI
            data_EFF = self.data_EFF
            data_LULCC = self.data_LULCC
            data_ECH4 = self.data_ECH4
            data_EN2O = self.data_EN2O
            data_Ehalo = self.data_Ehalo
            data_ENOX = self.data_ENOX
            data_ECO = self.data_ECO
            data_EVOC = self.data_EVOC
            data_ESO2 = self.data_ESO2
            data_ENH3 = self.data_ENH3
            data_EOC = self.data_EOC
            data_EBC = self.data_EBC
            data_RFant = self.data_RFant
            data_RFnat = self.data_RFnat
            mod_DATAscen = self.mod_DATAscen
            scen_ALL = self.scen_ALL
            scen_EFF = self.scen_EFF
            scen_LULCC = self.scen_LULCC
            scen_HARV = self.scen_HARV
            scen_SHIFT = self.scen_SHIFT
            scen_ECH4 = self.scen_ECH4
            scen_EN2O = self.scen_EN2O
            scen_Ehalo = self.scen_Ehalo
            scen_ENOX = self.scen_ENOX
            scen_ECO = self.scen_ECO
            scen_EVOC = self.scen_EVOC
            scen_ESO2 = self.scen_ESO2
            scen_ENH3 = self.scen_ENH3
            scen_EOC = self.scen_EOC
            scen_EBC = self.scen_EBC
            scen_RFant = self.scen_RFant
            scen_RFnat = self.scen_RFnat
            scen_RF = self.scen_RF

            mod_biomeSHR = self.mod_biomeSHR
            mod_biomeURB = self.mod_biomeURB
            ALBEDOS = self.albedos
            alb_global = self.alb_global

            execfile(os.path.join(_PATH, 'OSCAR-loadD.py'), locals())
            execfile(os.path.join(_PATH, 'OSCAR-loadP.py'), locals())
            execfile(os.path.join(_PATH, 'OSCAR-format.py'), locals())
            execfile(os.path.join(_PATH, 'OSCAR-fct.py'), locals())

            # Unpack prescribed variables
            reference_vars = locals().copy()
            regions = locals()['regionI_name']
            biomes = locals()['biome_name']
            regions[0] = 'Bunker fuels'

            input_data = {
                name: unpack_regions(regions, reference_vars[name])
                for name in _SIMPLE_EMISSIONS
            }

            input_data_complex = {
                name: unpack_regions(
                    regions, reference_vars[name], simple=False)
                for name in _COMPLEX_EMISSIONS
            }

            for name in input_data:
                input_data[name]['Total'] = sum_dict(input_data[name])

            for name in input_data_complex:
                input_data_complex[name]['Total'] = sum_dict(
                    input_data_complex[name])

            rf_drivers = {name: reference_vars[name] for name in _RF_DRIVERS}
            albedo_vars = {name: reference_vars[name] for name in _ALBEDO}

            # Unpack diagnostics
            _POSTPROCESS = {
                'time': lambda x: x,
                'time-region': partial(unpack_regions, regions),
                'time-region-biome': partial(unpack_regions_and_biomes,
                                             regions, biomes)
            }

            result = locals()['OSCAR_lite'](var_output=_OUTPUT_DIAGNOSTICS)
            output_data = {name: values for name, values in
                           zip(_OUTPUT_DIAGNOSTICS, result)}
            for var in output_data:
                var_type = _VAR_TYPES[var]
                f = _POSTPROCESS[var_type]
                output_data[var] = f(output_data[var])
                if var_type == 'time-region':
                    output_data[var]['Total'] = sum_dict(output_data[var])

            return _merge_dicts(input_data, output_data, rf_drivers,
                                input_data_complex, albedo_vars)
