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
from list_class import lists

g = gen()
l = lists()
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
        
        
    def simple_plotter(self,line,data,header,save_flag,pflag):
        g.tprinter('Running simple_plotter',pflag)
#         plt.xlim(0,100000)
        self.plotname = line[l.find_val('file_name',header,0)].split(".")[0]
        g.printer(self.plotname,pflag) 
        plt.plot(data[:,0],data[:,1])
        plt.title(self.plotname)
        plt.xlabel('time (s)')
        plt.ylabel('signal (V)')
        
        if save_flag == 1:
            file_name = os.path.join(self.save_path,str(self.plotname)+'_plot.png')
            g.printer(file_name,pflag) 
            plt.savefig(file_name)
        else:
            plt.show()
        plt.close()
     
     
    def simple_plotter_zoom(self,line,data,header,date_string,xlow,xup,save_flag,pflag):
        g.tprinter('Running simple_plotter',pflag)
#         plt.xlim(0,100000)
        self.plotname = line[l.find_val('file_name',header,0)].split(".")[0]
        g.printer(self.plotname,pflag) 
        plt.title(self.plotname+'\n'+str(date_string))
        plt.xlabel('time (s)')
        plt.ylabel('signal (V)')
        plt.xlim([xlow,xup])
#         plt.xmin = -1e-6
#         plt.xmax = 1e-6
        plt.plot(data[:,0],data[:,1])
        
        if save_flag == 1:
            file_name = os.path.join(self.save_path,str(self.plotname)+'_'+str(xlow)+'_to_'+str(xup)+'_plot.png')
            g.printer(file_name,pflag) 
            plt.savefig(file_name)
        else:
            plt.show()
        plt.close()   
        
        
    def zoom_plotter(self,line,data,header,poi,n,save_flag,pflag):
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