# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Nov 11 13:46:19 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

import sys
import os.path
from PySide import QtCore, QtGui
import time
import Queue

import mainhub
import pod

default_values = {}
default_values['stop_system'] = "stop_system"
default_values['insert_station'] = "insert_station"

class MainWindow(QtGui.QWidget):
    pushed = QtCore.Signal()

    def __init__(self):
	super(MainWindow,self).__init__()
        self.source = None
        self.destination = None
        self.queue = Queue.Queue()
        self.initUI()

    def initUI(self):
        self.source = None
        self.destination = None
        self.queue = Queue.Queue()
        self.setUpFrame()

    def setUpFrame(self):
        #Main Window
        #self.setGeometry(0,0,600,400)
        self.setObjectName("MainWindow")
        self.resize(600, 400)
        self.centralWidget = QtGui.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")

        #TEST
        self.tab = QtGui.QTabWidget(self)
        #self.tab.setGeometry(QtCore.QRect(30, 45, 540, 340))
        self.tab.setGeometry(QtCore.QRect(30, 45, 200, 20))
        self.tab_bar = QtGui.QTabBar(self.tab)
        tab_1 = self.tab_bar.addTab("Scheduler")
        tab_2 = self.tab_bar.addTab("Pod Information")

        #'Welcome to the Spartan Superway' Title
        self.title = QtGui.QLabel(self.centralWidget)
        self.title.setGeometry(QtCore.QRect(68, 0, 464, 50))
        self.title.setObjectName("label")
        self.title.setStyleSheet("font: 30pt;")

        #'Select source' Message
        self.source = QtGui.QLabel(self.centralWidget)
        self.source.setGeometry(QtCore.QRect(30, 50, 300, 50))
        self.source.setObjectName("source")
        self.source.setStyleSheet("font: 18pt;")

        #'Select destination' Message
        self.destination = QtGui.QLabel(self.centralWidget)
        self.destination.setGeometry(QtCore.QRect(30, 175, 300, 50))
        self.destination.setObjectName("destination")
        self.destination.setStyleSheet("font: 18pt;")

        self.print_source = QtGui.QLabel(self.centralWidget)
        self.print_source.setGeometry(QtCore.QRect(45,310, 350, 50))
        self.print_source.setObjectName("print_source")
        self.print_source.setStyleSheet("font: 18pt;")

        self.print_destination = QtGui.QLabel(self.centralWidget)
        self.print_destination.setGeometry(QtCore.QRect(45, 350, 350, 50))
        self.print_destination.setObjectName("print_destination")
        self.print_destination.setStyleSheet("font: 18pt;")

        #'Station 1' source
        self.source_station_1 = QtGui.QPushButton(self.centralWidget)
        self.source_station_1.setGeometry(QtCore.QRect(30, 100, 80, 20))
        self.source_station_1.setObjectName("source_station_1")

        #'Station 2' source
        self.source_station_2 = QtGui.QPushButton(self.centralWidget)
        self.source_station_2.setGeometry(QtCore.QRect(120, 100, 80, 20))
        self.source_station_2.setObjectName("source_station_2")

        #'Station 3' source
        self.source_station_3 = QtGui.QPushButton(self.centralWidget)
        self.source_station_3.setGeometry(QtCore.QRect(210, 100, 80, 20))
        self.source_station_3.setObjectName("source_station_3")

        #'Station 4' source
        self.source_station_4 = QtGui.QPushButton(self.centralWidget)
        self.source_station_4.setGeometry(QtCore.QRect(30, 130, 80, 20))
        self.source_station_4.setObjectName("source_station_4")

        #'Station 5' source
        self.source_station_5 = QtGui.QPushButton(self.centralWidget)
        self.source_station_5.setGeometry(QtCore.QRect(120, 130, 80, 20))
        self.source_station_5.setObjectName("source_station_5")

        #'Station 6' source
        self.source_station_6 = QtGui.QPushButton(self.centralWidget)
        self.source_station_6.setGeometry(QtCore.QRect(210, 130, 80, 20))
        self.source_station_6.setObjectName("source_station_6")

        #'Station 1' destination
        self.destination_station_1 = QtGui.QPushButton(self.centralWidget)
        self.destination_station_1.setGeometry(QtCore.QRect(30, 225, 80, 20))
        self.destination_station_1.setObjectName("source_station_1")

        #'Station 2' destination
        self.destination_station_2 = QtGui.QPushButton(self.centralWidget)
        self.destination_station_2.setGeometry(QtCore.QRect(120, 225, 80, 20))
        self.destination_station_2.setObjectName("source_station_2")

        #'Station 3' destination
        self.destination_station_3 = QtGui.QPushButton(self.centralWidget)
        self.destination_station_3.setGeometry(QtCore.QRect(210, 225, 80, 20))
        self.destination_station_3.setObjectName("source_station_3")

        #'Station 4' destination
        self.destination_station_4 = QtGui.QPushButton(self.centralWidget)
        self.destination_station_4.setGeometry(QtCore.QRect(30, 255, 80, 20))
        self.destination_station_4.setObjectName("source_station_4")

        #'Station 5' destination
        self.destination_station_5 = QtGui.QPushButton(self.centralWidget)
        self.destination_station_5.setGeometry(QtCore.QRect(120, 255, 80, 20))
        self.destination_station_5.setObjectName("source_station_5")

        #'Station 6' destination
        self.destination_station_6 = QtGui.QPushButton(self.centralWidget)
        self.destination_station_6.setGeometry(QtCore.QRect(210, 255, 80, 20))
        self.destination_station_6.setObjectName("source_station_6")

        self.confirm = QtGui.QPushButton(self.centralWidget)
        self.confirm.setGeometry(QtCore.QRect(380, 320, 100, 75))
        self.confirm.setObjectName("confirm")

        self.cancel = QtGui.QPushButton(self.centralWidget)
        self.cancel.setGeometry(QtCore.QRect(480, 320, 100, 75))
        self.cancel.setObjectName("cancel")

        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(30, 300, 540, 20))
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName("line")

        #self.setCentralWidget(self.centralWidget)

        self.retranslateUi()
        self.source_station_1.clicked.connect(self.source1)
        self.source_station_2.clicked.connect(self.source2)
        self.source_station_3.clicked.connect(self.source3)
        self.source_station_4.clicked.connect(self.source4)
        self.source_station_5.clicked.connect(self.source5)
        self.source_station_6.clicked.connect(self.source6)
        self.destination_station_1.clicked.connect(self.destination1)
        self.destination_station_2.clicked.connect(self.destination2)
        self.destination_station_3.clicked.connect(self.destination3)
        self.destination_station_4.clicked.connect(self.destination4)
        self.destination_station_5.clicked.connect(self.destination5)
        self.destination_station_6.clicked.connect(self.destination6)
        self.cancel.clicked.connect(self.cancel_press)
        #self.confirm.clicked.connect(self.confirmSignal)
        self.confirm.clicked.connect(self.confirm_press)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def confirmSignal(self):
        print "Temp Source: "+self.source
        print "Temp Destination: "+self.destination
        self.pushed.emit()

    def source1(self):
        self.source = "Station 1"
        print "Station 1"
        self.update_source()

    def source2(self):
        self.source = "Station 2"
        print "Station 2"
        self.update_source()

    def source3(self):
        self.source = "Station 3"
        print "Station 3"
        self.update_source()

    def source4(self):
        self.source = "Station 4"
        print "Station 4"
        self.update_source()

    def source5(self):
        self.source = "Station 5"
        print "Station 5"
        self.update_source()

    def source6(self):
        self.source = "Station 6"
        print "Station 6"
        self.update_source()

    def destination1(self):
        self.destination = "Station 1"
        print "Station 1"
        self.update_destination()
	   
    def destination2(self):
        self.destination = "Station 2"
        print "Station 2"
        self.update_destination()

    def destination3(self):
        self.destination = "Station 3"
        print "Station 3"
        self.update_destination()

    def destination4(self):
        self.destination = "Station 4"
        print "Station 4"
        self.update_destination()

    def destination5(self):
        self.destination = "Station 5"
        print "Station 5"
        self.update_destination()

    def destination6(self):
        self.destination = "Station 6"
        print "Station 6"
        self.update_destination()

    def update_source(self):
        text = 'Start destination: \t\t'+self.source
        self.print_source.setText(text)

    def update_destination(self):
        text = 'Desired destination: \t'+self.destination
        self.print_destination.setText(text)
    
    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setText(QtGui.QApplication.translate("MainWindow", "Welcome to the Spartan Superway", None, QtGui.QApplication.UnicodeUTF8))
        self.source.setText(QtGui.QApplication.translate("MainWindow", "Please select your source station:", None, QtGui.QApplication.UnicodeUTF8))
        self.destination.setText(QtGui.QApplication.translate("MainWindow", "Please select your destination station:", None, QtGui.QApplication.UnicodeUTF8))
        self.print_source.setText(QtGui.QApplication.translate("MainWindow", "Start destination: \t\tNot selected", None, QtGui.QApplication.UnicodeUTF8))
        self.print_destination.setText(QtGui.QApplication.translate("MainWindow", "Desired destination: \tNot selected", None, QtGui.QApplication.UnicodeUTF8))
        self.source_station_1.setText(QtGui.QApplication.translate("MainWindow", "Station 1", None, QtGui.QApplication.UnicodeUTF8))
        self.source_station_2.setText(QtGui.QApplication.translate("MainWindow", "Station 2", None, QtGui.QApplication.UnicodeUTF8))
        self.source_station_3.setText(QtGui.QApplication.translate("MainWindow", "Station 3", None, QtGui.QApplication.UnicodeUTF8))
        self.source_station_4.setText(QtGui.QApplication.translate("MainWindow", "Station 4", None, QtGui.QApplication.UnicodeUTF8))
        self.source_station_5.setText(QtGui.QApplication.translate("MainWindow", "Station 5", None, QtGui.QApplication.UnicodeUTF8))
        self.source_station_6.setText(QtGui.QApplication.translate("MainWindow", "Station 6", None, QtGui.QApplication.UnicodeUTF8))
        self.destination_station_1.setText(QtGui.QApplication.translate("MainWindow", "Station 1", None, QtGui.QApplication.UnicodeUTF8))
        self.destination_station_2.setText(QtGui.QApplication.translate("MainWindow", "Station 2", None, QtGui.QApplication.UnicodeUTF8))
        self.destination_station_3.setText(QtGui.QApplication.translate("MainWindow", "Station 3", None, QtGui.QApplication.UnicodeUTF8))
        self.destination_station_4.setText(QtGui.QApplication.translate("MainWindow", "Station 4", None, QtGui.QApplication.UnicodeUTF8))
        self.destination_station_5.setText(QtGui.QApplication.translate("MainWindow", "Station 5", None, QtGui.QApplication.UnicodeUTF8))
        self.destination_station_6.setText(QtGui.QApplication.translate("MainWindow", "Station 6", None, QtGui.QApplication.UnicodeUTF8))
        self.confirm.setText(QtGui.QApplication.translate("MainWindow", "Confirm", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

    def cancel_press(self):
        self.source = "Not selected"
        self.destination = "Not selected"
        self.update_source()
        self.update_destination()
        self.source = None
        self.destination = None

    def confirm_press(self):
        # self.queue.put((self.source, self.destination))
        # print self.queue.get()
        self.pushed.emit()

def main():
   app = QtGui.QApplication(sys.argv)
   ex = MainWindow()
   ex.setWindowTitle("Spartan Superway Ticket System")
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()