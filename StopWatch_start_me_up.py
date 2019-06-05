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
        self.flag = 1  #flag for timer display to continue to count up when start is pressed after stop is pressed
        self.flag1 = 1 #flag to make reset button do nothing while the timer is running
        self.flag2 = 1 #flag to make start button do nothing while timer is running
        self.time_dif_end = time.time()
        self.time_dif = the_program.time_now - self.time_start
        #================ PUSH BUTTONS Start/Stop/Reset =====================================================#  
        self.pushButton_Start.clicked.connect(self.Start_time)
        self.pushButton_Reset.clicked.connect(self.Reset_time)
        self.pushButton_Stop.clicked.connect(self.Stop_time)
        
        
        
    def Start_time(self):
        if self.flag2 == 1:
            self.time_start = time.time()
            
            self.timer = QtCore.QTimer()
            self.timer.setInterval(100)
            self.timer.setTimerType(QtCore.Qt.PreciseTimer)
            self.timer.timeout.connect(self.t_dependent_updates)
            self.timer.start()   #starts timer   
            self.flag1 = 1
            self.flag2 = 0
        else:
            None #Start button does nothing while the timer is running

    def Stop_time(self):
        self.timer.stop()   #stops timer        
        self.time_dif_end = self.time_dif  #saves end time
        self.flag = 0
        self.flag1 = 0
        self.flag2 = 1

        
    def Reset_time(self):
        if self.flag1 == 0:
            self.label_time.setText("00" + ":" + "00" + ":" + "00")  #resets time display
            self.flag = 1
        else:
            None   # Reset button does nothing while the timer is running
            
        
    def t_dependent_updates(self):           #method to update the time display
        if self.flag == 1:
            self.time_dif = the_program.time_now - self.time_start
        
        else:
            self.time_dif = the_program.time_now - self.time_start + self.time_dif_end
        uptime = datetime.timedelta(seconds=int(self.time_dif))
        
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
