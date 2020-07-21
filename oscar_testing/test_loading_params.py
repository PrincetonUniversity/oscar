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
import time
import xarray as xr

## choose a regional aggregation
mod_region = 'RCP_5reg'

nMC = 3
inds = (1750, 1750, 2014)

## load primary parameters and drivers
t0 = time.time()
Par0 = load_all_param(mod_region)
t1 = time.time()
For0 = load_all_hist(mod_region)
t2 = time.time()
hist_drivers = create_hist_drivers(For0, inds=inds)
t3 = time.time()
For_hist = generate_drivers(hist_drivers, nMC=nMC)
t4 = time.time()
