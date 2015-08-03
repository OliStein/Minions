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
    def __init__(self):
        self.num = 0
    
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
     
     
    def simple_plotter_zoom(self,line,data,header,xlow,xup,info,save_flag,pflag):
        g.tprinter('Running simple_plotter',pflag)
#         plt.xlim(0,100000)
        self.plotname = line[l.find_val('file_name',header,0)].split(".")[0]
        self.date_string = line[l.find_val('time stamp',header,0)]
        g.printer(self.plotname,pflag) 
#         plt.title(self.plotname+'\n'+str(self.date_string))
#         plt.xlabel('time (ns)')
#         plt.ylabel('signal (V)')
#         plt.xlim([xlow,xup])
#         
#         major_ticks = np.arange(-5001, 5001, 500) 
#         plt.xticks(major_ticks)  
#         plt.grid(which='both')
# #         plt.xmin = -1e-6
# #         plt.xmax = 1e-6
#         plt.plot(data[:,0],data[:,1])
        
        fig = plt.figure()                                                               
        ax = fig.add_subplot(1,1,1)                                                      

        title = self.plotname+'\n'+str(self.date_string)+'\n'+str(info)
        ax.set_title(title,fontsize = 11)
        ax.set_xlabel('time (ns)')
        ax.set_ylabel('signal (V)')
        
        
        
        data_x_max = np.max(data[:,0])
        data_x_min = np.min(data[:,0])
    
        if not xlow < data_x_min:
            data_x_min = xlow
        else:
            pass
        
        if not xup > data_x_max:
            data_x_max = xup
        else:
            pass
        
        
        data_y_max = np.max(data[:,1])
        data_y_min = np.min(data[:,1])
        g.printer('y max: '+str(data_y_max),pflag)
        g.printer('y max: '+str(data_y_min),pflag)
        g.printer('x max: '+str(data_x_max),pflag)
        g.printer('x min: '+str(data_x_min),pflag)
        
        x_ticks_max = 5e6
        y_ticks_max = 5
        
        ax.plot(data[:,0],data[:,1])
        # major ticks every 20, minor ticks every 5
        
        
        if (xup-xlow)>50000:                
            d_1 = 45000
            d_2 = 10000
                                  
            x_major_ticks = np.arange(xlow-d_1, xup+d_1, d_1)                                              
            x_minor_ticks = np.arange(xlow-d_2, xup+d_2, d_2)
        elif (xup-xlow)>20000:                
            d_1 = 10000
            d_2 = 2500
                                  
            x_major_ticks = np.arange(xlow-d_1, xup+d_1, d_1)                                              
            x_minor_ticks = np.arange(xlow-d_2, xup+d_2, d_2)
        elif (xup-xlow)>3000:
            d_1 = 2000
            d_2 = 500
                                  
            x_major_ticks = np.arange(xlow-d_1, xup+d_1, d_1)                                              
            x_minor_ticks = np.arange(xlow-d_2, xup+d_2, d_2)                                      
            
        elif (xup-xlow) >900:
            d_1 = 500
            d_2 = 250
                                  
            x_major_ticks = np.arange(xlow-d_1, xup+d_1, d_1)                                              
            x_minor_ticks = np.arange(xlow-d_2, xup+d_2, d_2)
            
        else:
            d_1 = 50
            d_2 = 25
                                  
            x_major_ticks = np.arange(xlow-d_1, xup+d_1, d_1)                                              
            x_minor_ticks = np.arange(xlow-d_2, xup+d_2, d_2)
            
        if (data_y_max-data_y_min)>1.5:
            g.printer('super large y scale',pflag)
            data_y_max = 8.25
            data_y_min = -1.25                                     
            y_major_ticks = np.arange(-y_ticks_max, y_ticks_max, .1)                                              
            y_minor_ticks = np.arange(-y_ticks_max, y_ticks_max, .05)
        elif (data_y_max-data_y_min)>0.5:
            g.printer('large y scale',pflag)
            data_y_max = 1.5
            data_y_min = -.25                                     
            y_major_ticks = np.arange(-y_ticks_max, y_ticks_max, .1)                                              
            y_minor_ticks = np.arange(-y_ticks_max, y_ticks_max, .05)
        elif(data_y_max-data_y_min)>0.2: 
            g.printer('small y scale',pflag)
            data_y_max = .3
            data_y_min = -.1
            y_major_ticks = np.arange(-y_ticks_max, y_ticks_max, .05)                                              
            y_minor_ticks = np.arange(-y_ticks_max, y_ticks_max, .025)    
        else:
            g.printer('small y scale',pflag)
            data_y_max = .2
            data_y_min = -.05
            y_major_ticks = np.arange(-y_ticks_max, y_ticks_max, .05)                                              
            y_minor_ticks = np.arange(-y_ticks_max, y_ticks_max, .025) 
                          
#         y_major_ticks = np.arange(-1, 1, .1)                                              
#         y_minor_ticks = np.arange(-1, 1, .01)                                               
        ax.set_xticks(x_major_ticks, minor=False)
        ax.set_xticks(x_minor_ticks, minor=True)
        ax.set_yticks(y_major_ticks, minor=False)
        ax.set_yticks(y_minor_ticks, minor=True)
#         ax.yaxis.grid(True, which='major')
#         ax.yaxis.grid(True, which='minor')
        ax.set_xlim([data_x_min,data_x_max])
        ax.set_ylim([data_y_min,data_y_max])
        
        ax.tick_params(axis = 'both', which = 'major', labelsize = 12)
        ax.tick_params(axis = 'both', which = 'minor', labelsize = 0)
#         ax.set_xticks(major_ticks)                                                       
#         ax.set_xticks(minor_ticks, minor=True)                                           
#         ax.set_yticks(major_ticks)                                                       
#         ax.set_yticks(minor_ticks, minor=True)                                           

#         # and a corresponding grid                                                       
#         ax.yaxis.grid(False)
#         ax.xaxis.grid(which='both')                                                            

        # or if you want differnet settings for the grids:                               
        ax.grid(which='minor', alpha=0.2)                                                
        ax.grid(which='major', alpha=0.5)                                                

        
        if save_flag == 1:
            file_name = os.path.join(self.save_path,str(self.plotname)+'_'+str(self.num)+'_'+str(xlow)+'_to_'+str(xup)+'_'+str(info)+'_plot.png')
            g.printer(file_name,pflag) 
            plt.savefig(file_name)
        else:
            plt.show()
        plt.close() 
        self.num += 1  
        
        
        
    def plotter_overview(self,line,data,header,save_flag,pflag):
        g.tprinter('Running plotter_overview',pflag)
    #         plt.xlim(0,100000)
        self.plot_name ='Overview' 
        self.file_name=line[l.find_val('file_name',header,0)].split(".")[0]
        self.date_string = line[l.find_val('time stamp',header,0)]
        g.printer(self.plot_name,pflag) 
    #         plt.title(self.plotname+'\n'+str(self.date_string))
    #         plt.xlabel('time (ns)')
    #         plt.ylabel('signal (V)')
    #         plt.xlim([xlow,xup])
    #         
    #         major_ticks = np.arange(-5001, 5001, 500) 
    #         plt.xticks(major_ticks)  
    #         plt.grid(which='both')
    # #         plt.xmin = -1e-6
    # #         plt.xmax = 1e-6
    #         plt.plot(data[:,0],data[:,1])
        
        
        
        fig = plt.figure()                                                               
        ax = fig.add_subplot(1,1,1)                                                      
        title = str(self.plot_name)+'\n'+str(self.file_name)+'\n'+str(self.date_string)
        save_name = str(self.file_name)+'_overview'
#         ax.rcParams["axes.titlesize"] = 10
        ax.set_title(title,fontsize = 11)
        ax.set_xlabel('time (ns)')
        ax.set_ylabel('signal (V)')
    
        ax.plot(data[:,0],data[:,1])
        # major ticks every 20, minor ticks every 5
        
        data_x_max = np.max(data[:,0])
        data_x_min = np.min(data[:,0])
    
        
        
        
        data_y_max = np.max(data[:,1])
        data_y_min = np.min(data[:,1])
        g.printer('y max: '+str(data_y_max),pflag)
        g.printer('y max: '+str(data_y_min),pflag)
        g.printer('x max: '+str(data_x_max),pflag)
        g.printer('x min: '+str(data_x_min),pflag)
        
        x_ticks_max = 1
        y_ticks_max = 5
         
        if (data_x_max-data_x_min)>6e4:  
            g.printer('long x scale',pflag) 
            off_set = 0
            data_x_max = 5e5
            data_x_min = -1e5                                 
            x_major_ticks = np.arange(data_x_min-off_set, data_x_max+off_set, 10000)                                              
            x_minor_ticks = np.arange(data_x_min-off_set, data_x_max+off_set, 5000)
        elif (data_x_max-data_x_min)>1e4:
            off_set = 0
            data_x_max = 5e4
            data_x_min = -1e4
            g.printer('mid x scale',pflag)
            x_major_ticks = np.arange(data_x_min-off_set, data_x_max+off_set, 10000)                                              
            x_minor_ticks = np.arange(data_x_min-off_set, data_x_max+off_set, 2500) 
        else:
            g.printer('short x scale',pflag)
            off_set = 0
            data_x_max = 5e3
            data_x_min = -1e3
            x_major_ticks = np.arange(data_x_min-off_set, data_x_max+off_set,500)                                              
            x_minor_ticks = np.arange(data_x_min-off_set, data_x_max+off_set, 250)     
        
        if (data_y_max-data_y_min)>1.5:
            g.printer('super large y scale',pflag)
            data_y_max = 8.25
            data_y_min = -1.25                                     
            y_major_ticks = np.arange(-y_ticks_max, y_ticks_max, .1)                                              
            y_minor_ticks = np.arange(-y_ticks_max, y_ticks_max, .05)
        elif (data_y_max-data_y_min)>0.5:
            g.printer('large y scale',pflag)
            data_y_max = 1.5
            data_y_min = -.25                                     
            y_major_ticks = np.arange(-y_ticks_max, y_ticks_max, .1)                                              
            y_minor_ticks = np.arange(-y_ticks_max, y_ticks_max, .05)
        elif(data_y_max-data_y_min)>0.2: 
            g.printer('small y scale',pflag)
            data_y_max = .3
            data_y_min = -.1
            y_major_ticks = np.arange(-y_ticks_max, y_ticks_max, .05)                                              
            y_minor_ticks = np.arange(-y_ticks_max, y_ticks_max, .025)    
        else:
            g.printer('small y scale',pflag)
            data_y_max = .1
            data_y_min = -.05
            y_major_ticks = np.arange(-y_ticks_max, y_ticks_max, .05)                                              
            y_minor_ticks = np.arange(-y_ticks_max, y_ticks_max, .025) 
        
        
        
            
                          
#         y_major_ticks = np.arange(-1, 1, .1)                                              
#         y_minor_ticks = np.arange(-1, 1, .01)                                               
        ax.set_xticks(x_major_ticks, minor=False)
        ax.set_xticks(x_minor_ticks, minor=True)
        ax.set_yticks(y_major_ticks, minor=False)
        ax.set_yticks(y_minor_ticks, minor=True)
    #         ax.yaxis.grid(True, which='major')
    #         ax.yaxis.grid(True, which='minor')
        ax.set_xlim([data_x_min,data_x_max])
        ax.set_ylim([data_y_min,data_y_max])
        
        ax.tick_params(axis = 'both', which = 'major', labelsize = 12)
        ax.tick_params(axis = 'both', which = 'minor', labelsize = 0)
    #         ax.set_xticks(major_ticks)                                                       
    #         ax.set_xticks(minor_ticks, minor=True)                                           
    #         ax.set_yticks(major_ticks)                                                       
    #         ax.set_yticks(minor_ticks, minor=True)                                           
    
    #         # and a corresponding grid                                                       
    #         ax.yaxis.grid(False)
    #         ax.xaxis.grid(which='both')                                                            
    
        # or if you want differnet settings for the grids:                               
        ax.grid(which='minor', alpha=0.2)                                                
        ax.grid(which='major', alpha=0.5)                                                
    
        
        if save_flag == 1:
            file_name = os.path.join(self.save_path,save_name+'_plot.png')
            g.printer(file_name,pflag) 
            plt.savefig(file_name)
        else:
            plt.show()
        plt.close() 
        self.num += 1     
        
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
        
        
    def hist_plotter(self,line,data,header,save_flag,pflag):
        g.tprinter('Running hist_plotter',pflag)
        xdata=data[:,0]
        ydata=data[:,1]
        plt.title('Histogram plot \n'+str(line[-2]))
        plt.xlabel('time (ns)')
        plt.ylabel('counts (#)')
        plt.plot(xdata,ydata)
        
        
        if save_flag == 1:
            plot_name  = str(line[-2]).split('.')[0]
            file_name = os.path.join(self.save_path,str(plot_name)+'_hist_plot.png')
            g.printer(file_name,pflag) 
            plt.savefig(file_name)
        else:
            plt.show()
        plt.close()  