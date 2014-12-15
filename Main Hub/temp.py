import os
from PySide import QtCore, QtGui
from multiprocessing import Process

import core

default_values = {}
default_values['working_directory'] = os.path.dirname(os.path.realpath(__file__))
default_values['log_directory'] = os.path.join(default_values['working_directory'],"logs/GUI.txt")
default_values['admin_password'] = "0195"
default_values['image_directory'] = os.path.join(default_values['working_directory'], "images/map.jpg")

class GUI(QtGui.QWidget, core.Core):
    confirm_signal = QtCore.Signal()
    close_signal = QtCore.Signal()

    def __init__(self):
	super(GUI,self).__init__()
        self.source = None
        self.destination = None
        self.current_password = ""
        self.tries = 1

        #self.make_directory(os.path.dirname(default_values['log_directory']))
        self.f = open(default_values['log_directory'], 'w')

        self.logger("---INITIALIZING GUI SYSTEM---\n")

        
        self.init_ui_main()


    def init_ui_main(self):
#Main Window
        self.setObjectName("main_window")
        self.resize(600, 400)
        self.central_widget = QtGui.QWidget(self)
        self.central_widget.setObjectName("central_widget")

#STATIC TEXT MESSAGES
        self.welcome_text = QtGui.QLabel(self.central_widget)
        self.welcome_text.setGeometry(QtCore.QRect(68, 0, 464, 50))
        self.welcome_text.setObjectName("welcome_text")
        self.welcome_text.setStyleSheet("font: 30pt;")

        self.source_text = QtGui.QLabel(self.central_widget)
        self.source_text.setGeometry(QtCore.QRect(30, 50, 300, 50))
        self.source_text.setObjectName("source_text")
        self.source_text.setStyleSheet("font: 18pt;")

        self.destination_text = QtGui.QLabel(self.central_widget)
        self.destination_text.setGeometry(QtCore.QRect(30, 175, 300, 50))
        self.destination_text.setObjectName("destination_text")
        self.destination_text.setStyleSheet("font: 18pt;")

        self.current_source_text = QtGui.QLabel(self.central_widget)
        self.current_source_text.setGeometry(QtCore.QRect(45,310, 350, 50))
        self.current_source_text.setObjectName("current_source_text")
        self.current_source_text.setStyleSheet("font: 18pt;")

        self.current_destination_text = QtGui.QLabel(self.central_widget)
        self.current_destination_text.setGeometry(QtCore.QRect(45, 350, 350, 50))
        self.current_destination_text.setObjectName("current_destination_text")
        self.current_destination_text.setStyleSheet("font: 18pt;")

#BUTTONS
        self.source_station_1_button = QtGui.QPushButton(self.central_widget)
        self.source_station_1_button.setGeometry(QtCore.QRect(30, 100, 80, 20))
        self.source_station_1_button.setObjectName("source_station_1_button")

        self.source_station_2_button = QtGui.QPushButton(self.central_widget)
        self.source_station_2_button.setGeometry(QtCore.QRect(120, 100, 80, 20))
        self.source_station_2_button.setObjectName("source_station_2_button")

        self.source_station_3_button = QtGui.QPushButton(self.central_widget)
        self.source_station_3_button.setGeometry(QtCore.QRect(210, 100, 80, 20))
        self.source_station_3_button.setObjectName("source_station_3_button")

        self.source_station_4_button = QtGui.QPushButton(self.central_widget)
        self.source_station_4_button.setGeometry(QtCore.QRect(30, 130, 80, 20))
        self.source_station_4_button.setObjectName("source_station_4_button")

        self.source_station_5_button = QtGui.QPushButton(self.central_widget)
        self.source_station_5_button.setGeometry(QtCore.QRect(120, 130, 80, 20))
        self.source_station_5_button.setObjectName("source_station_5_button")

        self.source_station_6_button = QtGui.QPushButton(self.central_widget)
        self.source_station_6_button.setGeometry(QtCore.QRect(210, 130, 80, 20))
        self.source_station_6_button.setObjectName("source_station_6_button")

        self.destination_station_1_button = QtGui.QPushButton(self.central_widget)
        self.destination_station_1_button.setGeometry(QtCore.QRect(30, 225, 80, 20))
        self.destination_station_1_button.setObjectName("destination_station_1_button")

        self.destination_station_2_button = QtGui.QPushButton(self.central_widget)
        self.destination_station_2_button.setGeometry(QtCore.QRect(120, 225, 80, 20))
        self.destination_station_2_button.setObjectName("destination_station_2_button")

        self.destination_station_3_button = QtGui.QPushButton(self.central_widget)
        self.destination_station_3_button.setGeometry(QtCore.QRect(210, 225, 80, 20))
        self.destination_station_3_button.setObjectName("destination_station_3_button")

        self.destination_station_4_button = QtGui.QPushButton(self.central_widget)
        self.destination_station_4_button.setGeometry(QtCore.QRect(30, 255, 80, 20))
        self.destination_station_4_button.setObjectName("destination_station_4_button")

        self.destination_station_5_button = QtGui.QPushButton(self.central_widget)
        self.destination_station_5_button.setGeometry(QtCore.QRect(120, 255, 80, 20))
        self.destination_station_5_button.setObjectName("destination_station_5_button")

        self.destination_station_6_button = QtGui.QPushButton(self.central_widget)
        self.destination_station_6_button.setGeometry(QtCore.QRect(210, 255, 80, 20))
        self.destination_station_6_button.setObjectName("destination_station_6_button")

        self.confirm_button= QtGui.QPushButton(self.central_widget)
        self.confirm_button.setGeometry(QtCore.QRect(380, 320, 100, 75))
        self.confirm_button.setObjectName("confirm_button")

        self.cancel_button = QtGui.QPushButton(self.central_widget)
        self.cancel_button.setGeometry(QtCore.QRect(480, 320, 100, 75))
        self.cancel_button.setObjectName("cancel_button")

#LINES
        self.line = QtGui.QFrame(self.central_widget)
        self.line.setGeometry(QtCore.QRect(30, 300, 540, 20))
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName("line")

#images
        self.image = QtGui.QLabel(self.central_widget)
        self.image.setGeometry(QtCore.QRect(340,75,230,200))
        self.image.setPixmap(QtGui.QPixmap(default_values['image_directory']))
        self.image.setObjectName("map")

        

#CONNECTORS
        #source stations
        self.source_station_1_button.clicked.connect(self.source_station_1)
        self.source_station_2_button.clicked.connect(self.source_station_2)
        self.source_station_3_button.clicked.connect(self.source_station_3)
        self.source_station_4_button.clicked.connect(self.source_station_4)
        self.source_station_5_button.clicked.connect(self.source_station_5)
        self.source_station_6_button.clicked.connect(self.source_station_6)

        #destination stations
        self.destination_station_1_button.clicked.connect(self.destination_station_1)
        self.destination_station_2_button.clicked.connect(self.destination_station_2)
        self.destination_station_3_button.clicked.connect(self.destination_station_3)
        self.destination_station_4_button.clicked.connect(self.destination_station_4)
        self.destination_station_5_button.clicked.connect(self.destination_station_5)
        self.destination_station_6_button.clicked.connect(self.destination_station_6)

        #cancel/confirm 
        self.cancel_button.clicked.connect(self.cancel_press)
        self.confirm_button.clicked.connect(self.confirm_press)

        #translate UIElements
        self.retranslate_ui_main()


    def source_station_1(self):
        self.source = "station_1"
        self.update_source()


    def source_station_2(self):
        self.source = "station_2"
        self.update_source()


    def source_station_3(self):
        self.source = "station_3"
        self.update_source()


    def source_station_4(self):
        self.source = "station_4"
        self.update_source()


    def source_station_5(self):
        self.source = "station_5"
        self.update_source()


    def source_station_6(self):
        self.source = "station_6"
        self.update_source()


    def destination_station_1(self):
        self.destination = "station_1"
        self.update_destination()
	   

    def destination_station_2(self):
        self.destination = "station_2"
        self.update_destination()


    def destination_station_3(self):
        self.destination = "station_3"
        self.update_destination()


    def destination_station_4(self):
        self.destination = "station_4"
        self.update_destination()


    def destination_station_5(self):
        self.destination = "station_5"
        self.update_destination()


    def destination_station_6(self):
        self.destination = "station_6"
        self.update_destination()


    def update_source(self):
        self.current_source_text.setText('Start destination: \t\t'+self.source.capitalize().replace("_"," "))


    def update_destination(self):
        self.current_destination_text.setText('Desired destination: \t'+self.destination.capitalize().replace("_", " "))
    

    def retranslate_ui_main(self):
        self.setWindowTitle(QtGui.QApplication.translate("main_window", "main_window", None, QtGui.QApplication.UnicodeUTF8))
        
        self.welcome_text.setText(QtGui.QApplication.translate("main_window", "Welcome to the Spartan Superway", None, QtGui.QApplication.UnicodeUTF8))
        self.source_text.setText(QtGui.QApplication.translate("main_window", "Please select your source station:", None, QtGui.QApplication.UnicodeUTF8))
        self.destination_text.setText(QtGui.QApplication.translate("main_window", "Please select your destination station:", None, QtGui.QApplication.UnicodeUTF8))
        self.current_source_text.setText(QtGui.QApplication.translate("main_window", "Start destination: \t\tNot selected", None, QtGui.QApplication.UnicodeUTF8))
        self.current_destination_text.setText(QtGui.QApplication.translate("main_window", "Desired destination: \tNot selected", None, QtGui.QApplication.UnicodeUTF8))
        
        self.source_station_1_button.setText(QtGui.QApplication.translate("main_window", "Station 1", None, QtGui.QApplication.UnicodeUTF8))
        self.source_station_2_button.setText(QtGui.QApplication.translate("main_window", "Station 2", None, QtGui.QApplication.UnicodeUTF8))
        self.source_station_3_button.setText(QtGui.QApplication.translate("main_window", "Station 3", None, QtGui.QApplication.UnicodeUTF8))
        self.source_station_4_button.setText(QtGui.QApplication.translate("main_window", "Station 4", None, QtGui.QApplication.UnicodeUTF8))
        self.source_station_5_button.setText(QtGui.QApplication.translate("main_window", "Station 5", None, QtGui.QApplication.UnicodeUTF8))
        self.source_station_6_button.setText(QtGui.QApplication.translate("main_window", "Station 6", None, QtGui.QApplication.UnicodeUTF8))
        self.destination_station_1_button.setText(QtGui.QApplication.translate("main_window", "Station 1", None, QtGui.QApplication.UnicodeUTF8))
        self.destination_station_2_button.setText(QtGui.QApplication.translate("main_window", "Station 2", None, QtGui.QApplication.UnicodeUTF8))
        self.destination_station_3_button.setText(QtGui.QApplication.translate("main_window", "Station 3", None, QtGui.QApplication.UnicodeUTF8))
        self.destination_station_4_button.setText(QtGui.QApplication.translate("main_window", "Station 4", None, QtGui.QApplication.UnicodeUTF8))
        self.destination_station_5_button.setText(QtGui.QApplication.translate("main_window", "Station 5", None, QtGui.QApplication.UnicodeUTF8))
        self.destination_station_6_button.setText(QtGui.QApplication.translate("main_window", "Station 6", None, QtGui.QApplication.UnicodeUTF8))
        self.confirm_button.setText(QtGui.QApplication.translate("main_window", "Confirm\nSelection", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_button.setText(QtGui.QApplication.translate("main_window", "Cancel\nSelection", None, QtGui.QApplication.UnicodeUTF8))

    
    def cancel_press(self):
        self.source = "Not selected"
        self.destination = "Not selected"
        self.update_source()
        self.update_destination()
        self.source = None
        self.destination = None

    
    def confirm_press(self):
        self.confirm_signal.emit()

    
    def closeEvent(self, event):
        self.init_ui_admin()


    def init_ui_admin(self):
#ADMIN WINDOW
        self.admin_window = QtGui.QWidget()
        self.admin_window.resize(350, 250)
        self.admin_window.setWindowTitle('Admin Window')

#WINDOW TITLE
        self.admin_window.setWindowFlags(self.admin_window.windowFlags() | QtCore.Qt.CustomizeWindowHint) 
        self.admin_window.setWindowFlags(self.admin_window.windowFlags() & ~QtCore.Qt.WindowTitleHint)
        self.admin_window.setWindowFlags(self.admin_window.windowFlags() & ~QtCore.Qt.WindowSystemMenuHint)
        self.admin_window.setWindowFlags(self.admin_window.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        self.admin_window.setWindowFlags(self.admin_window.windowFlags() & ~QtCore.Qt.WindowMinimizeButtonHint)
        self.admin_window.setWindowFlags(self.admin_window.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

#STATIC TEXTS
        self.admin_window.instruction_text = QtGui.QLabel(self.admin_window)
        self.admin_window.instruction_text.setGeometry(QtCore.QRect(10, 80, 150, 150))
        self.admin_window.instruction_text.setObjectName("instruction_text")
        self.admin_window.instruction_text.setStyleSheet("font: 30pt;")

        self.admin_window.code_text = QtGui.QLineEdit(self.admin_window)
        self.admin_window.code_text.setStyleSheet("font: 30pt;")
        self.admin_window.code_text.setGeometry(QtCore.QRect(15, 30, 150, 50))
        
#BUTTONS
        self.admin_window.cancel_button = QtGui.QPushButton(self.admin_window)
        self.admin_window.cancel_button.setGeometry(QtCore.QRect(180, 180, 50, 50))
        self.admin_window.cancel_button.setObjectName("cancel_button")
        self.admin_window.cancel_button.clicked.connect(self.press_cancel)

        self.admin_window.enter_button = QtGui.QPushButton(self.admin_window)
        self.admin_window.enter_button.setGeometry(QtCore.QRect(280, 180, 50, 50))
        self.admin_window.enter_button.setObjectName("enter_button")
        self.admin_window.enter_button.clicked.connect(self.press_enter)

        self.admin_window.num_0_button = QtGui.QPushButton(self.admin_window)
        self.admin_window.num_0_button.setGeometry(QtCore.QRect(230, 180, 50, 50))
        self.admin_window.num_0_button.setObjectName("num_0_button")
        self.admin_window.num_0_button.clicked.connect(self.press_0)

        self.admin_window.num_1_button = QtGui.QPushButton(self.admin_window)
        self.admin_window.num_1_button.setGeometry(QtCore.QRect(180, 30, 50, 50))
        self.admin_window.num_1_button.setObjectName("num_1_button")
        self.admin_window.num_1_button.clicked.connect(self.press_1)

        self.admin_window.num_2_button = QtGui.QPushButton(self.admin_window)
        self.admin_window.num_2_button.setGeometry(QtCore.QRect(230, 30, 50, 50))
        self.admin_window.num_2_button.setObjectName("num_2_button")
        self.admin_window.num_2_button.clicked.connect(self.press_2)

        self.admin_window.num_3_button = QtGui.QPushButton(self.admin_window)
        self.admin_window.num_3_button.setGeometry(QtCore.QRect(280, 30, 50, 50))
        self.admin_window.num_3_button.setObjectName("num_3_button")
        self.admin_window.num_3_button.clicked.connect(self.press_3)

        self.admin_window.num_4_button = QtGui.QPushButton(self.admin_window)
        self.admin_window.num_4_button.setGeometry(QtCore.QRect(180, 80, 50, 50))
        self.admin_window.num_4_button.setObjectName("num_4_button")
        self.admin_window.num_4_button.clicked.connect(self.press_4)

        self.admin_window.num_5_button = QtGui.QPushButton(self.admin_window)
        self.admin_window.num_5_button.setGeometry(QtCore.QRect(230, 80, 50, 50))
        self.admin_window.num_5_button.setObjectName("num_5_button")
        self.admin_window.num_5_button.clicked.connect(self.press_5)

        self.admin_window.num_6_button = QtGui.QPushButton(self.admin_window)
        self.admin_window.num_6_button.setGeometry(QtCore.QRect(280, 80, 50, 50))
        self.admin_window.num_6_button.setObjectName("num_6_button")
        self.admin_window.num_6_button.clicked.connect(self.press_6)

        self.admin_window.num_7_button = QtGui.QPushButton(self.admin_window)
        self.admin_window.num_7_button.setGeometry(QtCore.QRect(180, 130, 50, 50))
        self.admin_window.num_7_button.setObjectName("num_7_button")
        self.admin_window.num_7_button.clicked.connect(self.press_7)

        self.admin_window.num_8_button = QtGui.QPushButton(self.admin_window)
        self.admin_window.num_8_button.setGeometry(QtCore.QRect(230, 130, 50, 50))
        self.admin_window.num_8_button.setObjectName("num_8_button")
        self.admin_window.num_8_button.clicked.connect(self.press_8)

        self.admin_window.num_9_button = QtGui.QPushButton(self.admin_window)
        self.admin_window.num_9_button.setGeometry(QtCore.QRect(280, 130, 50, 50))
        self.admin_window.num_9_button.setObjectName("num_9_button")
        self.admin_window.num_9_button.clicked.connect(self.press_9)

        self.retranslate_ui_admin()

    def retranslate_ui_admin(self):
        self.admin_window.instruction_text.setText(QtGui.QApplication.translate("admin_window", "Enter \nShutdown \nCode \nAbove", None, QtGui.QApplication.UnicodeUTF8))
        self.admin_window.code_text.setText(QtGui.QApplication.translate("admin_window", "", None, QtGui.QApplication.UnicodeUTF8))
        self.admin_window.num_0_button.setText(QtGui.QApplication.translate("admin_window", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.admin_window.num_1_button.setText(QtGui.QApplication.translate("admin_window", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.admin_window.num_2_button.setText(QtGui.QApplication.translate("admin_window", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.admin_window.num_3_button.setText(QtGui.QApplication.translate("admin_window", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.admin_window.num_4_button.setText(QtGui.QApplication.translate("admin_window", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.admin_window.num_5_button.setText(QtGui.QApplication.translate("admin_window", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.admin_window.num_6_button.setText(QtGui.QApplication.translate("admin_window", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.admin_window.num_7_button.setText(QtGui.QApplication.translate("admin_window", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.admin_window.num_8_button.setText(QtGui.QApplication.translate("admin_window", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.admin_window.num_9_button.setText(QtGui.QApplication.translate("admin_window", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.admin_window.cancel_button.setText(QtGui.QApplication.translate("admin_window", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.admin_window.enter_button.setText(QtGui.QApplication.translate("admin_window", "E", None, QtGui.QApplication.UnicodeUTF8))

        self.admin_window.show()


    def press_0(self):
        self.update_keypad()
        self.current_password = self.current_password + "0"


    def press_1(self):
        self.update_keypad()
        self.current_password = self.current_password + "1"


    def press_2(self):
        self.update_keypad()
        self.current_password = self.current_password + "2"


    def press_3(self):
        self.update_keypad()
        self.current_password = self.current_password + "3"


    def press_4(self):
        self.update_keypad()
        self.current_password = self.current_password + "4"


    def press_5(self):
        self.update_keypad()
        self.current_password = self.current_password + "5"


    def press_6(self):
        self.update_keypad()
        self.current_password = self.current_password + "6"


    def press_7(self):
        self.update_keypad()
        self.current_password = self.current_password + "7"


    def press_8(self):
        self.update_keypad()
        self.current_password = self.current_password + "8"


    def press_9(self):
        self.update_keypad()
        self.current_password = self.current_password + "9"


    def press_cancel(self):
        self.current_password = ""
        self.admin_window.code_text.setText("")


    def press_enter(self):
        self.logger("Attempt System Shutdown: %s" % self.tries)
        self.logger("Check Passcode: %s\n" % (self.current_password == default_values['admin_password']))
        if self.current_password == default_values['admin_password']:
            self.current_password = ""
            self.tries = 1
            self.close_signal.emit()
        else:
            self.press_cancel()
            self.tries += 1
            if self.tries >= 4:
                self.tries = 1
                self.show()


    def update_keypad(self):
        self.admin_window.code_text.setText(self.admin_window.code_text.text() + "*")


    def close_system(self):
        self.logger("---SHUTING DOWN GUI SYSTEM---\n")
        self.f.close()