'''
Created on May 21, 2015

@author: Oli
'''
import sys
import os
import numpy as np
import datetime
import time

# import str









from log_file_setup import log_files
# from analysis_modules import data
from log_file_setup import Tee
import matplotlib.pyplot as plt
from gen_class import gen
from data_import import imp
from plotter_class import plotter
from list_class import lists

l = lists()
g = gen()
# l = log_files()
i = imp() 
p = plotter()


class ana_data():
    def __init__(self):
        self.counts = 0
        self.counts_old = 0
        self.time = 0
        self.time_old = 0
        self.time_zero = 0
        self.set_zero_flag = 0
        
    
    def header_set(self,header,pflag):
        self.header = header
        self.pass_flag = 0
        print self.header
        
    def tba_check(self,line,fflag,pflag):
        g.tprinter('Running tba_check',pflag)
        if line[l.find_val('analysed',self.header,0)] == str(1):
            g.printer('file is analysed',pflag)
            if fflag == 1:
                g.printer('Forced analysis',pflag)
                return 1
            else:
                return 0
        else:
            g.printer('file needs to be analysed',pflag)
            return 1
    
#     def name_info_scope(self,line,pflag):
#         g.tprinter('Running name_info_for_scopes',pflag)
#         self.fname = line[l.find_val('file_name',self.header,0)] 
#         self.fname_list=self.fname.split('_')
#         self.daq_name = self.fname_list[1]
#         self.time_stamp = self.fname_list[0]
#         self.channel = self.fname_list[2]
#         self.meas_nr = self.fname_list[3] 
#         
#         g.printer('time stamp: '+str(self.time_stamp),pflag)
#         g.printer('meas nr: '+str(self.meas_nr),pflag)
#         g.printer('daq name: '+str(self.daq_name),pflag)
#         g.printer('channel: '+str(self.channel),pflag)
#         
#         line[l.find_val('time_stamp',self.header,0)] = self.time_stamp
#         line[l.find_val('meas_nr',self.header,0)] = self.meas_nr
#         line[l.find_val('daq_name',self.header,0)] = self.daq_name
#         line[l.find_val('channel',self.header,0)] = self.channel
# #         print self.fname_list    
    
    def name_info_hist(self,line,rdef,pflag):
        g.tprinter('Running name_info',pflag)
        
        self.rdef = rdef
        
        self.fname = line[l.find_val('file_name',self.header,0)] 
        self.fname_list=self.fname.split('_')
        self.daq_name = self.fname_list[1]
        self.time_stamp = self.fname_list[0]
        self.mode = self.fname_list[2].split('.')[0]
#         self.meas_nr = self.fname_list[3] 
        
        g.printer('time stamp: '+str(self.time_stamp),pflag)
#         g.printer('meas nr: '+str(self.meas_nr),pflag)
        g.printer('daq name: '+str(self.daq_name),pflag)
        g.printer('mode: '+str(self.mode),pflag)
        
        line[l.find_val('time_stamp',self.header,0)] = self.time_stamp
#         line[l.find_val('meas_nr',self.header,0)] = self.meas_nr
        line[l.find_val('daq_name',self.header,0)] = self.daq_name
        line[l.find_val('mode',self.header,0)] = self.mode
#         print self.fname_list    
        self.rdefdaq = []
        for i in self.rdef:
            self.rdefdaq.append(i[0])
            
#         print self.rdefdaq
        self.daq_ind=l.find_val(self.daq_name,self.rdefdaq,0)
        self.ip=self.rdef[self.daq_ind][1]
        self.beam=self.rdef[self.daq_ind][2]
        self.loc=self.rdef[self.daq_ind][3]
        self.dcum=self.rdef[self.daq_ind][4]
        self.type=self.rdef[self.daq_ind][5]
        
        line[l.find_val('ip',self.header,0)] = self.ip
        line[l.find_val('loc',self.header,0)] = self.loc
        line[l.find_val('dcum',self.header,0)] = self.dcum
        line[l.find_val('type',self.header,0)] = self.type
        line[l.find_val('beam',self.header,0)] = self.beam
        
        
    def name_info_scope(self,line,rdef,pflag):
        g.tprinter('Running name_info for scopes',pflag)
        
        self.rdef = rdef
        
        self.fname = line[l.find_val('file_name',self.header,0)] 
        self.fname_list=self.fname.split('_')
        self.daq_name = self.fname_list[1]+'_'+self.fname_list[2]
        self.time_stamp = self.fname_list[0]
#         self.mode = self.fname_list[2].split('.')[0]
#         self.meas_nr = self.fname_list[3] 
        
        g.printer('time stamp: '+str(self.time_stamp),pflag)
#         g.printer('meas nr: '+str(self.meas_nr),pflag)
        g.printer('daq name: '+str(self.daq_name),pflag)
#         g.printer('mode: '+str(self.mode),pflag)
        
        line[l.find_val('time_stamp',self.header,0)] = self.time_stamp
#         line[l.find_val('meas_nr',self.header,0)] = self.meas_nr
#         line[l.find_val('daq_name',self.header,0)] = self.daq_name
#         line[l.find_val('mode',self.header,0)] = self.mode
#         print self.fname_list    
        self.rdefdaq = []
        for i in self.rdef:
            self.rdefdaq.append(i[0])
            
#         print self.rdefdaq
        self.daq_ind=l.find_val(self.daq_name,self.rdefdaq,0)
        self.ip=self.rdef[self.daq_ind][1]
        self.beam=self.rdef[self.daq_ind][2]
        self.loc=self.rdef[self.daq_ind][3]
        self.dcum=self.rdef[self.daq_ind][4]
        self.type=self.rdef[self.daq_ind][5]
        self.channel=self.rdef[self.daq_ind][6]
        self.name=self.rdef[self.daq_ind][7]
        
        
        line[l.find_val('ip',self.header,0)] = self.ip
        line[l.find_val('loc',self.header,0)] = self.loc
        line[l.find_val('dcum',self.header,0)] = self.dcum
        line[l.find_val('type',self.header,0)] = self.type
        line[l.find_val('beam',self.header,0)] = self.beam
        line[l.find_val('channel',self.header,0)] = self.channel
        line[l.find_val('daq_name',self.header,0)] = self.name
        
            
#     def time_cor(self,line,pflag):
#         g.tprinter('Running time_cor',pflag)
#         g.printer('Timestamps in UTC!',pflag)
#         
#         self.time_stamp_list = [self.time_stamp[:4],self.time_stamp[4:6],self.time_stamp[6:8],self.time_stamp[8:10],self.time_stamp[10:12],self.time_stamp[12:14]]
#         self.time_stamp_string=str(self.time_stamp[:4])+'-'+str(self.time_stamp[4:6])+'-'+str(self.time_stamp[6:8])+'_'+str(self.time_stamp[8:10])+':'+str(self.time_stamp[10:12])+':'+str(self.time_stamp[12:14])
#         line[l.find_val('year',self.header,0)] = self.time_stamp_list[0]
#         line[l.find_val('month',self.header,0)] = self.time_stamp_list[1]
#         line[l.find_val('day',self.header,0)] = self.time_stamp_list[2]
#         line[l.find_val('hour',self.header,0)] = self.time_stamp_list[3]
#         line[l.find_val('minute',self.header,0)] = self.time_stamp_list[4]
#         line[l.find_val('second',self.header,0)] = self.time_stamp_list[5]


    def time_cor(self,line,pflag):
        g.tprinter('Running time_cor',pflag)
        g.printer('Timestamps in UTC!',pflag)
        
        self.fname = line[l.find_val('file_name',self.header,0)] 
        self.fname_list=self.fname.split('_')
        self.daq_name = self.fname_list[1]+'_'+self.fname_list[2]
        self.time_stamp_sec = self.fname_list[0]
        
        self.time_stamp = time.gmtime(float(str(self.time_stamp_sec)[:-9]))
        self.time_stamp_string=time.strftime('%Y%m%d%H%M%S',self.time_stamp)
        line[l.find_val('year',self.header,0)] = time.strftime('%Y',self.time_stamp)
        line[l.find_val('month',self.header,0)] = time.strftime('%m',self.time_stamp)
        line[l.find_val('day',self.header,0)] = time.strftime('%d',self.time_stamp)
        line[l.find_val('hour',self.header,0)] = time.strftime('%H',self.time_stamp)
        line[l.find_val('minute',self.header,0)] = time.strftime('%M',self.time_stamp)
        line[l.find_val('second',self.header,0)] = time.strftime('%S',self.time_stamp)
        line[l.find_val('sub sec',self.header,0)] = float(str(self.time_stamp_sec)[-9:])
#         print self.time_stamp_list
    
    def time_cor_scope(self,line,pflag):
        g.tprinter('Running time_cor',pflag)
        g.printer('Timestamps in UTC!',pflag)
        
        self.fname = line[l.find_val('file_name',self.header,0)] 
        self.fname_list=self.fname.split('_')
        self.daq_name = self.fname_list[1]+'_'+self.fname_list[2]
        self.time_stamp = self.fname_list[0]
        
        self.time_stamp_sec  = time.mktime((int(self.time_stamp[0:4]),int(self.time_stamp[4:6]),int(self.time_stamp[6:8]),int(self.time_stamp[8:10]),int(self.time_stamp[10:12]),int(self.time_stamp[12:14]),0,0,0))
        self.time_stamp = time.gmtime(float(str(self.time_stamp_sec)))
        self.time_stamp_string=time.strftime('%Y%m%d%H%M%S',self.time_stamp)
        self.time_stamp_string_nice=time.strftime('%Y.%m.%d_%H:%M:%S',self.time_stamp)
        line[l.find_val('year',self.header,0)] = time.strftime('%Y',self.time_stamp)
        line[l.find_val('month',self.header,0)] = time.strftime('%m',self.time_stamp)
        line[l.find_val('day',self.header,0)] = time.strftime('%d',self.time_stamp)
        line[l.find_val('hour',self.header,0)] = time.strftime('%H',self.time_stamp)
        line[l.find_val('minute',self.header,0)] = time.strftime('%M',self.time_stamp)
        line[l.find_val('second',self.header,0)] = time.strftime('%S',self.time_stamp)
        line[l.find_val('time stamp',self.header,0)] = self.time_stamp_string_nice
#         line[l.find_val('sub sec',self.header,0)] = self.time_stamp[9:10]    
        
#         t=time.mktime(t)

        line[l.find_val('sec',self.header,0)] = self.time_stamp_sec
    
    def c_counter(self,line,pflag):
        g.tprinter('Running c_counter',pflag)
        self.counts =0
        for i in self.data:
            self.counts+= i[1]
        line[l.find_val('counts',self.header,0)] = self.counts
        g.printer('Total counts: '+str(self.counts),pflag)
        
    def dc_counter(self,line,pflag):
        g.tprinter('Running dc_counter',pflag)
        self.dcounter = self.counts - self.counts_old
        self.counts_old = self.counts 
        line[l.find_val('dcounts',self.header,0)] = self.dcounter
        g.printer('Delta counts: '+str(self.dcounter),pflag)
        
        
        
    
    def dt_counter(self,line,pflag):
        g.tprinter('Running dt_counter',pflag)
        self.dtime = 0

#         print self.time_stamp
        t= (int(self.time_stamp_list[0]),
            int(self.time_stamp_list[1]),
            int(self.time_stamp_list[2]),
            int(self.time_stamp_list[3]),
            int(self.time_stamp_list[4]),
            int(self.time_stamp_list[5]),0,0,0)
#         print t
        self.time = time.mktime(t)
        
#         print self.time
        if self.time_old == 0:
            
            self.dtime = 0 
        else:
            self.dtime = self.time - self.time_old
        
        line[l.find_val('dtime',self.header,0)] = self.dtime
        
        
        self.time_old = self.time 
        
        g.printer('Delta time: ' +str(self.dtime),pflag)
        
        
#     def time_sec(self,line,pflag):
#         g.tprinter('Running time_sec',pflag)
#     
#         t= (int(self.time_stamp_list[0]),
#             int(self.time_stamp_list[1]),
#             int(self.time_stamp_list[2]),
#             int(self.time_stamp_list[3]),
#             int(self.time_stamp_list[4]),
#             int(self.time_stamp_list[5]),0,0,0)
# 
#         self.time_s = time.mktime(t)
#     
#         
#         line[l.find_val('time sec',self.header,0)] = self.time_s  
#           
#         g.printer('Time stamp in sec: '+str(self.time_s),pflag)
    
    def set_t(self,line,pflag):
        g.tprinter('Running set_t',pflag)
        
        self.fname = line[l.find_val('file_name',self.header,0)] 
        self.fname_list=self.fname.split('_')
   
        
        self.time_stamp_sec = self.fname_list[0]
#         self.start_time = 0
        
            
        self.time_sec =  float(str(self.time_stamp_sec)[:-9])
            
            
            
        line[l.find_val('time sec',self.header,0)] = self.time_sec
        
    def set_t_zero(self,k,line,pflag):
        g.tprinter('Running set_t_zero',pflag)
        
        self.fname = line[l.find_val('file_name',self.header,0)] 
        self.fname_list=self.fname.split('_')
        self.start = self.fname_list[-1]
        g.printer(str(self.start),pflag)
        
        self.time_stamp_sec = self.fname_list[0]
        
        g.printer(str(k),pflag)
#         self.start_time = 0
        if k==1 or self.start =='ST.csv':
            g.printer('Set start time to:',pflag)
            self.start_time =  float(str(self.time_stamp_sec)[:-9])
            g.printer(str(self.start_time),pflag)
            
        else:
            g.printer('Start time already set',pflag)
            
        line[l.find_val('start time',self.header,0)] = self.start_time
#             g.printer('setting time_zero',pflag)
#             t= (int(self.time_stamp_list[0]),
#                 int(self.time_stamp_list[1]),
#                 int(self.time_stamp_list[2]),
#                 int(self.time_stamp_list[3]),
#                 int(self.time_stamp_list[4]),
#                 int(self.time_stamp_list[5]),0,0,0)
#         
#             self.time_zero = time.mktime(t)
#             self.set_zero_flag =1
#             g.printer(str(self.time_zero),pflag)
#         else:
#             g.printer('time_zero already set',pflag)
#             g.printer(str(self.time_zero),pflag)
#         
#         line[l.find_val('time zero',self.header,0)] = self.time_zero
#         
    def delta_time_zero(self,line,pflag):
        g.tprinter('Running delta_time_zero',pflag)
        
        self.d_t_zero = self.time_s - self.time_zero

        line[l.find_val('delta time zero',self.header,0)] = self.d_t_zero
        g.printer('Delta time from zero in sec: '+str(self.d_t_zero),pflag)
    
        
    def data_loader(self,line,pflag):
        g.tprinter('Running data_loader',pflag)
        if self.pass_flag ==0:
            g.printer('Loading: '+str(line[l.find_val('file_name_path',self.header,0)]),pflag)
            dp = line[l.find_val('file_name_path',self.header,0)]
            try:
                self.data = np.loadtxt(dp,delimiter=',')
                g.printer('Data loaded',pflag)
            except:
                g.printer('No data loaded',pflag)
                self.pass_flag = 1
        else:
            g.printer('pass_flag = 1, skip',pflag)
            pass
    
    def data_check(self,pflag):
        g.tprinter('Running data_check',pflag)
        if self.pass_flag == 0:
            try:
                self.data[0]
                print len(self.data[0])
                if len(self.data[0]) == 2:                
                    self.pass_flag = 0
                    g.printer('data ok',pflag)
                else:
                    g.printer('data not ok')
                    self.pass_flag = 1
            except:
                self.pass_flag = 1
                g.printer('data not ok',pflag)
            
        else:
            g.printer('pass_flag = 1, skip',pflag)
            pass
    def time_info(self,line,data,pflag): 
        g.tprinter('Running time_info',pflag)
        
        self.time_total= data[-1][0]-data[0][0]
        self.time_start=data[0][0]
        self.time_end = data[-1][0]
        self.delta_time = (data[10][0]-data[0][0])/10
        
        
        line[l.find_val('t total',self.header,0)] =self.time_total
        line[l.find_val('t start',self.header,0)] =self.time_start
        line[l.find_val('t end',self.header,0)] =self.time_end
        line[l.find_val('t delta',self.header,0)] =self.delta_time
        
          
    def bin_time_cor(self,pflag): 
        g.tprinter('Running bin_time_cor',pflag)
        self.t_cor = np.array([1.6,1])
        self.data = np.multiply(self.data,self.t_cor)
        g.printer('Histogram length in ns: '+str(self.data[-1,0]),pflag)
        g.printer('Histogram shape: '+str(np.shape(self.data)),pflag)
           
    def t_delta(self,line,data,pflag):
        g.tprinter('Running t_delta',pflag)
        if self.pass_flag == 0:
            print self.data[1,0]-self.data[0,0]
            line[l.find_val('t_delta',self.header,0)] = self.data[1,0]-self.data[0,0]
            line[l.find_val('t_length',self.header,0)] = (self.data[1,0]-self.data[0,0])*len(self.data)
            
        else:
            g.printer('pass_flag = 1, skip')
            pass
        
    def offset_corr(self,line,data,pflag):
        g.tprinter('Running offset_corr',pflag)
        if self.pass_flag ==0:
            len_data = int(round(len(self.data)*.02))-1
#             print len_data
                          
            self.offset = np.mean(self.data[:len_data,1])
            g.printer('Offset: '+str(self.offset),pflag)
            for i in self.data:
                i[1]=i[1]-self.offset
                
              
            line[l.find_val('offset',self.header,0)] =self.offset
            line[l.find_val('offset_corr',self.header,0)] =1
            offset = np.mean(self.data[-len_data:,1])
            g.printer('New offset: '+str(offset),pflag)  
            
        else:
            g.printer('pass_flag = 1, skip')
            pass
            
    def ns_convert(self,line,pflag):
        g.tprinter('Running ns_convert',pflag)
        
        ydata = self.data[:,1]
        xdata = self.data[:,0]*1e9
        
        self.data=np.array ([(xdata[i],ydata[i]) for i in range(len(ydata))])
        line[l.find_val('ns convert',self.header,0)] =1
    
    def noise_finder(self,line,data,pflag):
        g.tprinter('Running noise_finder',pflag)
        if self.pass_flag==0:
            len_data = int(round(len(self.data)*.05))-1
            noise_min=np.min(self.data[:len_data,1])
            noise_max=np.max(self.data[:len_data,1])
            g.printer('noise min: '+str(noise_min),pflag)
            g.printer('noise max: '+str(noise_max),pflag)
            self.noise = np.max(self.data[:len_data,1])-np.min(self.data[:len_data,1])
            g.printer('noise level: '+str(self.noise),pflag)
            line[l.find_val('noise',self.header,0)] =self.noise
        else:
            g.printer('pass_flag = 1, skip')
            pass 
    
    def moving_average(self,line,n=3):
        
        ydata = self.data[:,1]
        xdata = self.data[:,0]
        ret = np.cumsum(ydata, dtype=float)
   
        ret[n:] = ret[n:] - ret[:-n]
        
        ydata = ret[n - 1:] / n
        
        self.data=np.array ([(xdata[i],ydata[i]) for i in range(len(ydata))])
        line[l.find_val('moving average',self.header,0)] =1
        line[l.find_val('num pts moving average',self.header,0)] =n
        
    def sig_above(self,line,data,lim,pflag):
        g.tprinter('Running sig_above',pflag)
        self.sigab = 0
        g.printer('limit '+str(lim),pflag)
        rlim = (lim*0.001)
        for i in data:
            
            if i[1] >= rlim:
                
                self.sigab +=1
            
            
        line[l.find_val('sig '+str(lim)+' pt',self.header,0)] =self.sigab
        line[l.find_val('sig '+str(lim)+' t',self.header,0)] =self.sigab*self.delta_time      
        
        
        
    def max_finder(self,line,data,pflag):
        g.tprinter('Running max_finder',pflag)
        if self.pass_flag ==0:
            self.max_list=[]
            
            
            pass
        
        
        else:
            g.printer('pass_flag =1, skip')
            pass    
        
                
    def analysed(self,line,pflag):
        g.tprinter('Setting line to analysed',pflag)
        line[l.find_val('analysed',self.header,0)] = 1
        
        
    def max_find(self,data,n,pflag):
        maxind = np.argmax(data,)
        return maxind
        
        
    def trig_finder(self,data,nup,ndow,pflag):
        g.tprinter('Running trig_finder',pflag)
        trig = np.argwhere(data[0:,0] == 0)
        return trig
        
        