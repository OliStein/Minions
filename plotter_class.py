'''
Created on May 21, 2015

@author: Oli
'''

import sys
import os
import numpy as np

from log_file_setup import log_files
# from analysis_modules import data
from log_file_setup import Tee
import matplotlib.pyplot as plt
from gen_class import gen
from data_import import imp

g = gen()
l = log_files()
i = imp() 



class plotter():
    
    def set_save_path(self,path,pflag):
        g.tprinter('Running set_save_path',pflag)
        g.printer('Setting save_path to:',pflag)
        g.printer(str(path),pflag)
        self.save_path = path
        if os.path.isdir(self.save_path) == False:
            g.printer(str(self.save_path)+' not existing.',pflag)
            g.printer('creating directory',pflag)
            
            os.mkdir(self.save_path)
        else:
            g.printer('path ok',pflag) 
               
#         g.printer(str(os.path.isdir(self.save_path)),pflag)
        
        
    def simple_plotter(self,data,fn,save_flag,pflag):
        g.tprinter('Running simple_plotter',pflag)
#         plt.xlim(0,100000)
        plt.plot(data[:,0],data[:,1])
        
        if save_flag == 1:
            file_name = os.path.join(self.save_path,str(fn)+'.png')
            g.printer(file_name,pflag) 
            plt.savefig(file_name)
        else:
            plt.show()
        plt.close()
        
    def zoom_plotter(self,data,fn,poi,n,save_flag,pflag):
        g.tprinter('Running zoom_plotter',pflag)
#         plt.xlim(0,100000)
        xdata = data[poi-n:poi+n,0]
        print len(xdata)
        ydata = data[poi-n:poi+n,1]
        plt.plot(xdata,ydata)
        
        if save_flag == 1:
            file_name = os.path.join(self.save_path,str(fn)+'_zoomed.png')
            g.printer(file_name,pflag) 
            plt.savefig(file_name)
        else:
            plt.show()
        plt.close()    