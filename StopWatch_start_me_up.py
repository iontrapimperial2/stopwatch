# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:05:30 2019

@author: yudiw
"""

# import python classes --------------------------------------------------------------------------------
import sys # -------------------------------------------------------------------------- import for stuff i guess? i don't really know... 
from PyQt5 import QtCore, QtGui, QtWidgets # ------------------------------------------ imports for the GUI
 
import time # ------------------------------------------------------------------------- time


import datetime
from apscheduler.schedulers.qt import QtScheduler # ----------------------------------- similar to above

# import custom classes --------------------------------------------------------------------------------
from StopWatch_gui import Ui_StopWatch_gui # ------------------------------------------------ import the layout generated with QtDesigner
from StopWatch__main import c_program # ------------------------------------------- the program which collects the controll over all the devices


starttime=time.time()
scheduler = QtScheduler()
scheduler.start()


class window(Ui_StopWatch_gui):
    def __init__(self, dialog, the_program):
        Ui_StopWatch_gui.__init__(self)
        self.setupUi(dialog)
        self.label_time.setText("00" + ":" + "00" + ":" + "00")
        self.time_start = time.time()  # save start time of program
        self.flag = 1
        self.time_dif_end = time.time()
        #================ PUSH BUTTONS Start/Stop =====================================================#  
        self.pushButton_Start.clicked.connect(self.Start_time)
        self.pushButton_Reset.clicked.connect(self.Reset_time)
        self.pushButton_Stop.clicked.connect(self.Stop_time)
        
        
        
    def Start_time(self):
        self.time_start = time.time()
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1)
        self.timer.setTimerType(QtCore.Qt.PreciseTimer)
        self.timer.timeout.connect(self.t_dependent_updates)
        self.timer.start()   #starts timer
        


    def Stop_time(self):
        self.timer.stop()   #stops timer        
        self.time_dif_end = the_program.time_now - self.time_start
        self.flag = 0
        #uptime = datetime.timedelta(seconds=int(self.time_dif_end))  #time when stop is pressed
       
        #self.label_time.setText(str(uptime)) #display final time
        
    def Reset_time(self):
        
        self.label_time.setText("00" + ":" + "00" + ":" + "00")  #resets time display
        self.flag = 1
        
    def t_dependent_updates(self):           #method to update the time display
        if self.flag == 1:
            time_dif = the_program.time_now - self.time_start
        
        else:
            time_dif = the_program.time_now - self.time_start+ self.time_dif_end
        uptime = datetime.timedelta(seconds=int(time_dif))
        
        self.label_time.setText(str(uptime))
        
        





if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    
    # create instance of parameters 
    the_program = c_program()
        
    # set up window   
    dialog_sequ = QtWidgets.QMainWindow()
    prog_sequ = window(dialog_sequ,the_program)    
    dialog_sequ.show()

 
    sys.exit(app.exec_())
