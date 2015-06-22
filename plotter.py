'''
Created on Jun 15, 2015

@author: Oli
'''


import sys
import os
import numpy as np
import csv
import pandas as pd
import matplotlib as plt



from log_file_setup import log_files
# from analysis_modules import data
from log_file_setup import Tee
import matplotlib.pyplot as plt
from gen_class import gen
from data_import import imp
from plotter_class import plotter
from ana_data import ana_data
from ana_res import ana_res

# from rdmstores import * 

a = ana_data()
ar = ana_res()
g = gen()
l = log_files()
i = imp() 
p = plotter()


class histplot():
    
    def shist(self,data,sflag,spath,sname,pflag):
        g.tprinter('Running sist',pflag)
        xdata=data[:,0]
        ydata=data[:,1]
        plt.plot(xdata,ydata,'ro')
        plt.savefig(os.path.join(spath,str(sname))+'.pdf')
        plt.close()
        
        
        
        
        
        
        
        
        
        
        
    
    