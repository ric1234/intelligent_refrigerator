# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstwin.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import  QtCore,QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QSize
import Read as rd
import choose as ch
import service as ser
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 480)
        # setting background image for the main window
        MainWindow.setStyleSheet("background-image:url(\"other.jpg\");")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 350,300, 81))
        self.pushButton.setMaximumSize(QtCore.QSize(281, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(25, 105, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 30, 281, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(195, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 110, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 110, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 110, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        p = QtGui.QPalette()
        brush1 = QtGui.QBrush(QtCore.Qt.white,QtGui.QPixmap('fridge.jpg'))
        p.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Window,brush1)
        p.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Window,brush1)
        p.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Window,brush1)
        self.label.setPalette(p)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        #set font
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionExit.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionExit.setPriority(QtWidgets.QAction.HighPriority)
        self.actionExit.setObjectName("actionExit")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #background image for push buttons
        self.pushButton.setStyleSheet("background-image:url(\"grey.jpg\");")
        self.label.setStyleSheet("background-image:url(\"grey.jpg\");")
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Press for RFID Authentication"))
        #go to info if button clicked
        self.pushButton.clicked.connect(self.info)
        #set text to label
        self.label.setText(_translate("MainWindow", "INTELLIGENT REFRIGERATOR"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
     #informative message box 
    def info(self):
        msg = QtWidgets.QMessageBox()
        msg.setMaximumSize(QtCore.QSize(281, 16777215))
        msg.setGeometry(QtCore.QRect(510, 330, 581, 281))
        msg.setInformativeText("Hold the tag near the RFID reader")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        #call functin for authentication
        ret=rd.rfid()
        print (ret)
        if ret == 1:
            self.choice()
     
    def choice(self):
        #open a different class for new window
        self.MainWindow1 = QtWidgets.QMainWindow()
        #make an object
        ui1 = ch.Ui_choose()
        ui1.setupUi(self.MainWindow1)
        #open the other window
        self.MainWindow1.show()
        #close the current window
        MainWindow.close()
        
#message for failed authentication     
def fail():
    msg = QtWidgets.QMessageBox()
    msg.warning(msg,"Fail:"," please try again")


if __name__ == "__main__":
 
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # call the first window
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
##    timer = QtCore.QTimer()
##    timer.timeout.connect(ser.update_label)
##    timer.start(1000)  # every 1000 milliseconds
    sys.exit(app.exec_())

