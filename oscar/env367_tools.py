# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 21:56:48 2020

@author: danjr
"""

import numpy as np
import xarray as xr

# hard-coded path to the read-only data directory
dir_windows_dan = r'C:\Users\danjr\Documents\Teaching\ENV367_Fall2020\oscar-exercises\saved-data\\'
dir_adroit_dan = r'/home/druth/ENV367_Fall2020/oscar-exercises/saved-data//'
dir_adroit_shared = r'/scratch/network/climate/oscar-exercises/saved-data//'
default_dir = dir_adroit_shared

def save_run_model_output(output,name_start,data_dir=default_dir):
    '''
    Save each DataSet of the run_model output dictionary as a .nc file. Only
    saves values that are not None.
    
    
    Parameters
    ----------
    output : dict
        The dictionary output by run_model
        
    name_start : str
        The start of the filename for each saved file
        
    data_dir : str, optional
        The path to the directory in which the file is saved; defaults to a
        directory that is read-only for students on Adroit
    '''
    
    # save each dictionary value (which is not None) as an .nc file
    for key in output:
        if output[key] is not None:
            output[key].to_netcdf(data_dir+name_start+'_'+key+'.nc', encoding={var:{'zlib':True, 'dtype':np.float32} for var in output[key]})
        
def load_model_output(name_start,data_dir=default_dir):
    '''
    Load model output that was saved in a dict (in the same format that
    run_model returns)
    
    Parameters
    ----------
    name_start : str
        The start of the filename for each of the saved files to load
    
    data_dir : str, optional
        The path to the directory in which the file is saved; defaults to a
        directory that is read-only for students on Adroit
        
    Returns
    -------
    loaded_model_output : dict
        A dict that resembles the output of run_model
    '''

    keys = ['Par',
            'For_hist',
            'Ini_hist',
            'Out_hist',
            'For_scen',
            'Ini_scen',
            'Out_scen']
    loaded_model_output = {}
    for key in keys:
        try:
            fpath = data_dir+name_start+'_'+key+'.nc'
            print(fpath)
            with xr.open_dataset(fpath) as TMP: x = TMP.load()
            loaded_model_output[key] = x
        except FileNotFoundError:
            print('File for '+key+' not found')
        
    return loaded_model_output