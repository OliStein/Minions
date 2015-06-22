'''
Created on May 20, 2015

@author: Oli
'''
import sys
import os
import numpy as np
import csv
import pandas as pd
# import str









from log_file_setup import log_files
# from analysis_modules import data
from log_file_setup import Tee
import matplotlib.pyplot as plt
from gen_class import gen
from data_import import imp
from plotter_class import plotter
from ana_data import ana_data
from ana_res import ana_res

a = ana_data()
ar = ana_res()
g = gen()
l = log_files()
i = imp() 
p = plotter()
# d = data()
# c = csv_list()


cwd = '/Users/Oli/work/dBLM_readout/LHC_data_analysis_scope'

data_fold = 'data'
plot_fold = 'plots' 
ana_res_fold = 'ana_res' 

data_path  = '/Users/Oli/work/LeCroy/test_env/data'
# data_path = os.path.join(cwd,data_fold)
plot_path = os.path.join(cwd,plot_fold)
ana_res_path = os.path.join(cwd,ana_res_fold) 


l.log_file_set(cwd,'log')
  
f = open(l.log_path(),'a')
original = sys.stdout
sys.stdout = Tee(sys.stdout, f)


pflag=1
ana_file_save_interval = 5


g.printer(data_path,pflag)

i.path(data_path,pflag)
i.path_check(pflag)

i.data_list_creator(pflag)
p.set_save_path(plot_path,pflag)
ar.infrastruc(ana_res_path,pflag)
ar.ana_file_check(pflag)
ar.ana_file_loader(pflag)
ar.ana_file_writer(i.data_list,pflag)
ar.ana_file_saver(1,pflag)

# sys.exit('stop')
max_it = len(ar.ana_file)
print ar.ana_file[0]

a.header(ar.ana_file[0],pflag)
# sys.exit('stop')
for k in range(1,max_it):
# for k in range(len(i.data_list)):
    g.loop_info(k,i.len_data_list,pflag)
    print ar.ana_file[k]
    line = ar.ana_file[k]
    ana_flag = a.tba_check(line,1,pflag)
    if ana_flag == 1:
        g.tprinter('start analysis',pflag)
        a.name_info(line,pflag)
        a.data_loader(line,pflag)
        a.data_check(a.data,pflag)
        a.t_delta(line,a.data,pflag)
        a.offset_corr(line,a.data,pflag)
        a.noise_finder(line,a.data,pflag)
        a.max_finder(line,a.data,pflag)
    else:
        pass
    
    
    a.analysed(ar.ana_file[k],pflag)
 
ar.ana_file_saver(1,pflag)   
    
# for i in ar.ana_file:
#     print i    
#     i.data_importer(i.data_list[k][0],pflag)
#     p.set_save_path(plot_path,pflag)
# #     for q in range(10):
# #         print i.data[q,3:]
#     p.simple_plotter(i.data[:,3:],i.data_list[k][1],0,pflag)
#     max_y_index=a.max_find(i.data[:,3:],1,pflag)
#     p.zoom_plotter(i.data[:,3:],i.data_list[k][1],max_y_index,1000,0,pflag)
#     print a.trig_finder(i.data[:,3:],1,2,pflag)











