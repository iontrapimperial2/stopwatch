# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:55:10 2019

@author: yudiw
"""

from apscheduler.schedulers.qt import QtScheduler # ----------------------------------- to use the scheduler for the execution of jobs
import time


# starts the scheduler for our program -----------------------------------------------------------------
program_scheduler = QtScheduler()
program_scheduler.start()

class c_program:
    def __init__(self):
                
        
        # this value will be updated
        self.time_now  = time.time()
        
        #++ scheduled job, updates each 0.1 seconds the time self.time_now +++++++++++++++++++++++++++++#          
        program_scheduler.add_job(self.set_time_now, 'interval', seconds=0.1, id='set_time_now_id')
        

        
    #~~ function: updates the time saved in self.time_now with the current time ~~~~~~~~~~~~~~~~~~~~~~~#   
    def set_time_now(self):
        
        self.time_now = time.time()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
    