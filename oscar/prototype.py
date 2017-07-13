import os
import warnings

_PATH = os.path.dirname(__file__)
_DEFAULT_OUTPUT_DIAGNOSTICS = [
    'D_CO2', 'D_CH4', 'D_N2O', 'RF_halo', 'D_O3t',
    'D_O3s', 'D_SO4', 'D_POA', 'D_BC', 'D_NO3',
    'D_SOA', 'D_AERh', 'RF', 'D_gst', 'D_OHC'
]
_SIMPLE_EMISSIONS = [
    'EFF', 'ECH4', 'EN2O', 'ENOX', 'ECO', 'EVOC', 'ESO2', 'ENH3',
    'EOC', 'EBC'
]
_RF_DRIVERS = [
    'RFsolar', 'RFvolc', 'RFcon'
]


def unpack_regions(data, regions):
    """Converts a 2D array of columns with regional data to a dictionary
    mapping region names to 1D arrays"""
    result = {}
    for i, region in enumerate(regions):
        result[region] = data[:, i]
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
                 scen_EFF='stop', scen_LULCC='stop', scen_ECH4='stop',
                 scen_EN2O='stop', scen_Ehalo='stop', scen_ENOX='stop',
                 scen_ECO='stop', scen_EVOC='stop', scen_ESO2='stop',
                 scen_ENH3='stop', scen_EOC='stop', scen_EBC='stop',
                 scen_RFant='stop', scen_RFnat='stop'):
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
            defined.  Options are 'raw', 'offset', 'smoothX' (X in years), or 
            'trends'.  Default is 'trends'.
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
        self.scen_ALL = scen_ALL

        if scen_ALL is not None:
            self.scen_EFF = scen_ALL
            self.scen_LULCC = scen_ALL
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

    def run(self, end_year, var_output=_DEFAULT_OUTPUT_DIAGNOSTICS):
        """Run model for specified number of years

        Parameters
        ----------
        end_year : int
            Final year of simulation [> 1700 (simulation start)]
        var_output : list
            List of variable names to output

        Returns
        -------
        dict
            A mapping of variable names to 1D timeseries arrays or dictionaries
            of 1D timeseries arrays
        """
        # Suppress numpy divide by zero warnings
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            locals()['_PATH'] = _PATH

            execfile(os.path.join(_PATH, 'OSCAR.py'), locals())

            ind_final = end_year - 1700
            if ind_final < 0:
                raise ValueError('end_year must be greater than 1700; '
                                 'got {}'.format(end_year))

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

            execfile(os.path.join(_PATH, 'OSCAR-loadD.py'), locals())
            execfile(os.path.join(_PATH, 'OSCAR-loadP.py'), locals())
            execfile(os.path.join(_PATH, 'OSCAR-format.py'), locals())
            execfile(os.path.join(_PATH, 'OSCAR-fct.py'), locals())

            # Based on TPCLIMAT_Vfinal; TODO: add complex emissions
            reference_vars = locals().copy()
            regions = locals()['regionI_name']
            regions[0] = 'Bunker fuels'
            input_data = {name: unpack_regions(reference_vars[name], regions)
                          for name in _SIMPLE_EMISSIONS}
            for name in input_data:
                input_data[name]['Total'] = sum_dict(input_data[name])

            rf_drivers = {name: reference_vars[name] for name in _RF_DRIVERS}

            result = locals()['OSCAR_lite'](var_output=var_output)
            output_data = {name: values for name, values in zip(var_output,
                                                                result)}
            return _merge_dicts(input_data, output_data, rf_drivers)
