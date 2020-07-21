# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 16:21:20 2020

@author: danjr
"""

from oscar.fct_wrap import run_model
from oscar.fct_process import OSCAR
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from oscar.fct_loadD import load_all_hist, load_all_scen
from oscar.fct_loadP import load_all_param
from oscar.fct_genD import create_hist_drivers, create_scen_drivers
from oscar.fct_genMC import generate_config, generate_drivers
import time
import xarray as xr

## choose a regional aggregation
mod_region = 'RCP_5reg'

scens = ['RCP2.6', 'RCP4.5', 'RCP6.0', 'RCP8.5']
For_rcp = load_all_scen(mod_region=mod_region, group_scen=scens, LCC='gross')

fig,ax = plt.subplots()
for scen in scens:
    ax.plot(For_rcp['year'],For_rcp['RF_solar'].sel(scen=scen),label=scen)


For_hist = load_all_hist(mod_region)
ax.plot(For_hist['year'],For_hist['RF_solar'],color='g',ls='--',lw=2)

ax.legend()


with xr.open_dataset(r'C:\Users\danjr\Documents\Teaching\ENV367_Fall2020\OSCAR\oscar\input_data\drivers\\solar-activity_CMIP6.nc') as TMP: x = TMP.load()

plt.figure()
plt.plot(x['year'],x['TSI'])