# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StopWatch.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StopWatch(object):
    def setupUi(self, StopWatch):
        StopWatch.setObjectName("StopWatch")
        StopWatch.resize(403, 287)
        self.centralWidget = QtWidgets.QWidget(StopWatch)
        self.centralWidget.setObjectName("centralWidget")
        self.label_time = QtWidgets.QLabel(self.centralWidget)
        self.label_time.setGeometry(QtCore.QRect(90, 50, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_time.setFont(font)
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.pushButton_Start = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Start.setGeometry(QtCore.QRect(70, 120, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Start.setFont(font)
        self.pushButton_Start.setObjectName("pushButton_Start")
        self.pushButton_Reset = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Reset.setGeometry(QtCore.QRect(140, 170, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Reset.setFont(font)
        self.pushButton_Reset.setObjectName("pushButton_Reset")
        self.pushButton_Stop = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Stop.setGeometry(QtCore.QRect(210, 120, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Stop.setFont(font)
        self.pushButton_Stop.setObjectName("pushButton_Stop")
        StopWatch.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(StopWatch)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 403, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuStop_Watch = QtWidgets.QMenu(self.menuBar)
        self.menuStop_Watch.setObjectName("menuStop_Watch")
        StopWatch.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(StopWatch)
        self.mainToolBar.setObjectName("mainToolBar")
        StopWatch.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(StopWatch)
        self.statusBar.setObjectName("statusBar")
        StopWatch.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuStop_Watch.menuAction())

        self.retranslateUi(StopWatch)
        QtCore.QMetaObject.connectSlotsByName(StopWatch)

    def retranslateUi(self, StopWatch):
        _translate = QtCore.QCoreApplication.translate
        StopWatch.setWindowTitle(_translate("StopWatch", "StopWatch"))
        self.label_time.setText(_translate("StopWatch", "00:00:00"))
        self.pushButton_Start.setText(_translate("StopWatch", "Start"))
        self.pushButton_Reset.setText(_translate("StopWatch", "Reset"))
        self.pushButton_Stop.setText(_translate("StopWatch", "Stop"))
        self.menuStop_Watch.setTitle(_translate("StopWatch", "Stop Watch"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StopWatch = QtWidgets.QMainWindow()
    ui = Ui_StopWatch()
    ui.setupUi(StopWatch)
    StopWatch.show()
    sys.exit(app.exec_())

