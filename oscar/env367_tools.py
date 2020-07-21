# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 21:56:48 2020

@author: danjr
"""

import numpy as np
import xarray as xr

res_folder = r'C:\Users\danjr\Documents\Teaching\ENV367_Fall2020\oscar-exercises\saved-data\\'

def save_run_model_output(output,name_start):
    for key in output:
        if output[key] is not None:
            output[key].to_netcdf(res_folder+name_start+'_'+key+'.nc', encoding={var:{'zlib':True, 'dtype':np.float32} for var in output[key]})
        
def load_model_output(name_start):
    '''load saved data into a dictionary, as if the model was just run'''
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
            fpath = res_folder+name_start+'_'+key+'.nc'
            with xr.open_dataset(fpath) as TMP: x = TMP.load()
            loaded_model_output[key] = x
        except FileNotFoundError:
            print('File for '+key+' not found')
        
    return loaded_model_output