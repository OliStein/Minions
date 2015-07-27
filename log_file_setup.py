'''
Created on May 20, 2015

@author: Oli
'''

# Import of libraries 
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


from list_class import lists
from csv_list_class import csv_list
from gen_class import gen

g = gen() 
c = csv_list()
# li = lists()  

# Class for writing the console output in a log file
class Tee(object):
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
            


          
# Class for analysing the data
class log_files():
    
    # Setting up the log file in the directory where the script is saved
    def log_file_set(self,path,name,pflag):
        g.tprinter('Running log_file_set',pflag)
        if not os.path.exists(os.path.join(path,'log_files')):
            os.mkdir(os.path.join(path,'log_files'))
        
        # Directory of the script 
        self.c_dir = os.getcwd()
        
        # Create time string
        self.creat_time = strftime("%Y%m%d_%H%M", localtime())
        
        # Path and name of the log file
        self.log_file_path=os.path.join(path,'log_files',str(name)+'_'+self.creat_time+'.txt')
        print self.log_file_path
        
        # Head of the log file
        print ''
        self.log_file=open(self.log_file_path,'w+')
        
        print >> self.log_file, '-------------------------------------------------------' 
        print >> self.log_file, 'Data analysis Log_file'
        print >> self.log_file, ''
        print >> self.log_file, 'Script_file dir: '+str(self.c_dir)
        print >> self.log_file, 'Log_file dir: '+str(path)
        print >> self.log_file, 'Log_file name: '+str(name)+'_'+self.creat_time+'.txt'
        print >> self.log_file, ''
        print >> self.log_file, 'date: '+strftime("%a, %d %b %Y", localtime())
        print >> self.log_file, 'time: '+strftime("%H:%M:%S", localtime())
        print >> self.log_file, ''
        print >> self.log_file, '-------------------------------------------------------'
#         print >> self.log_file, 'current directory: '+str(self.c_dir)
#         print >> self.log_file, 'root directory: '+str(self.start)
        print >> self.log_file, ''
#         print >> self.log_file, self.out
        print >> self.log_file, ''
    
        # Closing file
        self.log_file.close()
    
    # Returns the path of the log file
    def log_path(self):
        return self.log_file_path

    def log_file_cleaner(self, path):
        for fl in glob.glob(os.path.join(path,'log*.txt')):
            os.remove(fl)
            
            
            
