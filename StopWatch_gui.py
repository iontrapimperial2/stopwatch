# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stopwatch.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StopWatch_gui(object):
    def setupUi(self, StopWatch):
        StopWatch.setObjectName("StopWatch")
        StopWatch.resize(403, 287)
        self.centralWidget = QtWidgets.QWidget(StopWatch)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_Start = QtWidgets.QPushButton(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Start.setFont(font)
        self.pushButton_Start.setObjectName("pushButton_Start")
        self.gridLayout.addWidget(self.pushButton_Start, 1, 1, 1, 1)
        self.pushButton_Stop = QtWidgets.QPushButton(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Stop.setFont(font)
        self.pushButton_Stop.setObjectName("pushButton_Stop")
        self.gridLayout.addWidget(self.pushButton_Stop, 1, 2, 1, 1)
        self.label_time = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_time.setFont(font)
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.gridLayout.addWidget(self.label_time, 0, 1, 1, 2)
        self.pushButton_Reset = QtWidgets.QPushButton(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Reset.setFont(font)
        self.pushButton_Reset.setObjectName("pushButton_Reset")
        self.gridLayout.addWidget(self.pushButton_Reset, 2, 1, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
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
        self.pushButton_Start.setText(_translate("StopWatch", "Start"))
        self.pushButton_Stop.setText(_translate("StopWatch", "Stop"))
        self.label_time.setText(_translate("StopWatch", "00:00:00"))
        self.pushButton_Reset.setText(_translate("StopWatch", "Reset"))
        self.menuStop_Watch.setTitle(_translate("StopWatch", "Stop Watch"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StopWatch = QtWidgets.QMainWindow()
    ui = Ui_StopWatch()
    ui.setupUi(StopWatch)
    StopWatch.show()
    sys.exit(app.exec_())
