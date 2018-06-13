#! /usr/bin/env python2.6

import matplotlib
matplotlib.use('Agg')

import denudationRateAnalysis as dra
import numpy as np

data = dra.read_csv('portengadata.csv')
del(data[0])
ksn_vec, area_vec = dra.calculate_ksn_for_data(data,1000000,0.5)

np.savez_compressed('ksn_area_data_0_5.npz', ksn_vec = ksn_vec, area_vec = area_vec)
