# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 13:14:43 2020

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

## choose a regional aggregation
mod_region = 'RCP_5reg'

nMC = 3
inds = (1750, 1750, 2014)

## load primary parameters and drivers
Par0 = load_all_param(mod_region)
For0 = load_all_hist(mod_region)
hist_drivers = create_hist_drivers(For0, inds=inds)
For_hist = generate_drivers(hist_drivers, nMC=nMC)
For_rcp = load_all_scen(mod_region,group_scen=['RCP6.0','RCP8.5'])

fig,ax = plt.subplots()

ax.plot(For0['year'],For0['Eff'].sel(data_Eff='PRIMAP').sum('reg_land'),color='gray',lw=1)
ax.plot(hist_drivers['year'],hist_drivers['Eff'].sel(data_Eff='CEDS PRIMAP *EDGARv42-FT2010* CDIAC').sum('reg_land'),color='k',lw=2)
for i in range(nMC):
    ax.plot(For_hist['year'],For_hist['Eff'].sel(config=i).sum('reg_land'),color='r',lw=1)



stophere

#run = run_model(OSCAR, (2010, 2010, 2014, 2100), mod_region='Houghton_2001', nMC=1, output=True,Par0='RCP8.5')

fig,ax = plt.subplots()
ax.plot(For0['year'],For0['Eff'].sel(data_Eff='PRIMAP').sum('reg_land'),'o-',color='k',label='historical from PRIMAP')
for rcp_scen in For_rcp['scen']:
    ax.plot(For_rcp['year'],For_rcp['Eff'].sel(scen=rcp_scen).sum('reg_land'),'-',label=rcp_scen)
ax.legend()
ax.set_xlabel('year')
ax.set_ylabel('$E_\mathrm{FF}$')

