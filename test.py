'''
Created on May 22, 2015

@author: Oli
'''
import sys
import os
import numpy as np
# import str









from log_file_setup import log_files
# from analysis_modules import data
from log_file_setup import Tee
import matplotlib.pyplot as plt
from gen_class import gen
from data_import import imp
from plotter_class import plotter
from ana_data import ana_data

a = ana_data()
g = gen()
l = log_files()
i = imp() 
p = plotter()

h = np.array([['hallo', 'peng',0,1],['hallo', 'peng',0,2]])
print h[:,1]
if 'hallo' in h:
    print 1
else:
    print 0


# x = np.arange(6).reshape(2,3)
# print x
# print x[0:,1]
# 
# print np.argwhere(x[0:,1]>2)
