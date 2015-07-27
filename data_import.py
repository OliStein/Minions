'''
Created on May 20, 2015

@author: Oli
'''




import os
import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
import shutil as st
import pickle 
from time import strftime, localtime, time
import time
import glob
# import str

from list_class import lists
from csv_list_class import csv_list
from gen_class import gen
from matplotlib.font_manager import path

g = gen() 
c = csv_list()


class imp():
    
    def path_data(self,d_path,pflag):
        g.tprinter('Running path',pflag)
        g.printer('data path: '+d_path,pflag)
        self.path = d_path
         
    def path_check(self,pflag):
        g.tprinter('Running path check',pflag)
#         try:
        try:
            os.chdir(self.path)
            g.printer('path exists',pflag)
        except:
            try:
                os.mkdir(self.path)
                g.printer('path created',pflag)
            except:
                g.printer('Could not create path',pflag)
                sys.exit('script stop')
#         except:
#             g.printer('no correct path',pflag)
#             sys.exit('script stop')
#             
    
    def data_list_creator(self,ident,pflag):
        g.tprinter('Running data_list_creator',pflag)
        
#         self.f = []
# #         for (dirpath, dirnames, filenames) in os.walk(self.path):
#         for (dirpath, dirnames, filenames) in os.walk(cwd):
#             self.f.extend(filenames)
# #             print self.f
#             break
        self.f = os.listdir(self.path)
        print 'self.f'
        print self.f
        k = []
        print 'len(self.f)'
        print len(self.f)
        for i in self.f:
#             print i
            if i.endswith(str(ident)):
#                 k.append([os.path.join(self.path,i),i])
                k.append([os.path.join(self.path,i),i])
#                 k.append(i)
#             print k
        
        g.printer('Length data_list '+str(k),pflag)
        
        self.data_list=k    
        
        
        
        if len(self.data_list)==0:
            g.printer('no data found length data_list == 0',pflag)
            sys.exit('script stop')
        else:
            g.printer(str(len(self.data_list))+' data file found',pflag)
        self.len_data_list = len(self.data_list)
        g.printer('length of data_list',pflag)
        g.printer(str(self.len_data_list),pflag)
        
    def data_importer(self,fname,pflag):
        g.tprinter('Running data importer',pflag)
        g.printer('importing file',pflag)
        g.printer(str(fname),pflag)
        try:
            self.data = np.genfromtxt(fname,delimiter=',',skip_header=6)
        except:
            g.printer('no data imported',pflag)
            sys.exit('script stop')
#         for i in range(10):
#             g.printer(str(self.data[i,3:]),pflag) 
        
           
        
        
        
        