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
from time import strftime, localtime
import time
import glob

from gen_class import gen
# from list_class import lists
# from problem_handler import prob_handler

# import of plotting class
g = gen()
# prob = prob_handler()

# import list class
# obsolete
# li = lists()

# class for dealing with csv files
class csv_list():
    # module for loading a .csv file
    def csv_file_loader(self,path,fname,pflag):
        g.printer('running csv_file_loader',pflag)

        # Checks in path for fname 
        if os.path.isfile(os.path.join(path,fname)):
            g.printer(fname+' found',pflag)
            
            # Loads fname and writes it into data
            data = []
            with open(os.path.join(path,fname),'rU') as f:
                for line in csv.reader(f,delimiter = ',', skipinitialspace = True, dialect=csv.excel_tab):
                    data.append(line)
            f.close()
            self
           
        else:
            g.printer('no '+fname+' found',pflag)
           
       
        
        print ''
        return data       
    
    # Saves data_list to fname in path as .csv
    # flag indicates if existing file will be overwritten 
    def csv_file_saver(self,path,fname,data_list,flag,pflag):
        g.printer('running csv_file_saver',pflag)
        
        if os.path.isdir(path) == False:
            os.mkdir(path)
        else:
            pass
         

        if os.path.isfile(os.path.join(path,fname)):

            g.printer(fname+' existing',pflag)
        
            if flag == 1:
                g.printer('file will be overwritten '+fname,pflag)
                   
            
                with open(os.path.join(path,fname),'wb') as f:
                    writer = csv.writer(f)
                    writer.writerows(data_list)
                f.close()
            else:
                g.printer('no writing',pflag)
           
        else:
            g.printer(fname+' not existing',pflag)
            g.printer('writing to '+fname,pflag)

           
            with open(os.path.join(path,fname),'wb') as f:
                writer = csv.writer(f)
                writer.writerows(data_list)
            f.close()
       
        
        print ''
     
    # saves the analyzed data to the ana_data folder     
    def analyzed_save(self,header,data_out,i,pflag):
        g.tprinter('Running analyzed_save',pflag)
        save_folder =  os.path.split(os.path.split(os.path.split(i[self.find_val('file',header,0)])[0])[-1])[-1]
        save_path = os.path.join(os.path.split(os.path.split(os.path.split(i[self.find_val('file',header,0)])[0])[0])[0],'ana_data')
        save_path_comp = os.path.join(save_path,save_folder)
#         file_name ='analyzed_'+os.path.split(i[self.find_val('file',header,0)])[-1]
        file_name =os.path.split(i[self.find_val('file',header,0)])[-1]
        g.printer('save path:',pflag)
        g.printer(save_path_comp,pflag)
        g.printer('file name:',pflag)
        g.printer(file_name,pflag)
        self.csv_file_saver(save_path_comp,file_name,data_out,1,pflag)
#         g.printer(save_folder,1)

    # loads the to be analyzed file 
    def data_grabber(self,i,header,channel,pflag):
        g.tprinter('running data_grabber',pflag)
        
        pos = self.find_val('file',header,pflag)
        
        file_name = os.path.split(i[pos])[-1]
        file_path = os.path.split(i[pos])[0]
        g.printer(file_name,pflag)
        g.printer(file_path,pflag)
        info_string= 'file ok'
        data_comp = []
#         g.printer('prob flag '+str(prob.flag_ret()),1)
        # tries to load the data and checks the format
        try:
            data=self.csv_file_loader(file_path,file_name,1)
            flag = 1
            data_comp = [flag,data,info_string]
            g.printer('data file successfully loaded',pflag)
            
            try:
#                 g.printer('next',pflag)
#                 g.printer(data[1][0],pflag)
#                 g.printer('next 2',pflag)
#                 g.printer(data[1][0],pflag)
#                 g.printer(str(str('Revision:')==str(data[1][0])[0:9]),pflag)
#                 g.printer('next 3',pflag)
                if str('Revision:')==(str(data[1][0])[0:9]):
#                     g.printer('next 4',pflag)
                    flag = 1
                    info_string = 'data fine'
                    data_comp = [flag,data,info_string]
                else:
                    flag = 0
                    data_comp[0]=0
                    info_string = 'data not correct'
                    
                
            except:     
                flag = 0
                data_comp[0]=0
                info_string = 'data no list'
        except:
            g.printer('no data file loaded',pflag)
            info_string= 'not loaded'
            data=0
            flag = 0
            data_comp = [flag,data,info_string]
            data_comp=[flag,data,info_string]
#             prob.flag_set()
            #sys.exit('program stop')
#         g.printer('prob info '+prob.info,1)    
        return data_comp   
    
    # returns the index of cname in a list
    def find_val(self,cname,lists,pflag):
        g.tprinter('running find_val',pflag)
#         llists = lists.tolist
        ind = np.where(lists == cname)[0][0]
        g.printer('searched string: '+str(cname),pflag)
        g.printer('position of: '+str(cname)+' is: '+str(ind),pflag)
        return ind  
    
    # checks which files in the ana_file have to be analyzed
    # if analyze_all == 1, all files will be analyzed
    # if in i in ana_file the analyzed flag is !=1 then the file is included in the analysis 
    
    
    def tba(self,ana_file,analyze_all,pflag):
        g.tprinter('running tba',pflag)
        header = ana_file[0]
        naf = 0
        if analyze_all == 1:
            g.printer('analyze all files',pflag)
        else:
            pass
        for i in ana_file[1:]:
#             g.printer(float(i[self.find_val('analyzed',header,0)])==1.,pflag)
            if float(i[self.find_val('analyzed',header,0)])!=1. or analyze_all == 1:
                naf +=1
            else:
                pass
        
        g.printer(str(naf)+' of '+str(len(ana_file)-1)+' data sets have to be analyzed',pflag)
        
        return naf  
#     
#     def problem_init(self):
#         self.prob = 'no' 
#         
#     def problem_check(self):
#         if self.prob != 'no':
#              return break 
#         
#     def problem_flag_set(self,set,header):
#         self.prob = set
#         self.problem_check()   