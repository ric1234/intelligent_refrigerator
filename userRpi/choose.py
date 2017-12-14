# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import firstwin as fi
import second as sc
import service as ser
class Ui_choose(object):
    def setupUi(self, choose):
        choose.setObjectName("choose")
        choose.resize(800, 480)
        #choose.setStyleSheet("background-color: rgb(123, 123, 167);")
        #choose.setStyleSheet("background-image:url(\"fridge.jpg\"); ")
        self.centralwidget = QtWidgets.QWidget(choose)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 270, 311, 121))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(208, 255,205);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 270, 341, 121))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(208, 255, 205);")
        self.pushButton.setObjectName("pushButton")
        choose.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(choose)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        choose.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(choose)
        self.statusbar.setObjectName("statusbar")
        choose.setStatusBar(self.statusbar)
##        choose.setWindowTitle("choose")
##        self.pushButton_2.setText( " FOR AUDIO INPUT")
##        self.pushButton.setText( "FOR PUSH BUTTONS")
##        self.pushButton.setStyleSheet("background-color: rgb(208, 255, 205);")
        self.retranslateUi(choose)
        #global abcd = choose
        self.pushButton_2.clicked.connect(lambda:self.sec(choose))
        self.pushButton.clicked.connect(lambda:self.click(choose))
        QtCore.QMetaObject.connectSlotsByName(choose)
    def sec(self,first_win):
        #print ("abc")
        Ui_choose.MainWindow2 = QtWidgets.QMainWindow()
        ui2 = sc.Ui_MainWindow()
        ui2.setupUi(Ui_choose.MainWindow2)
        Ui_choose.MainWindow2.show()
        first_win.close()
        
    def click(self,first_win):
        print ("abc")
        Ui_choose.MainWindow2= QtWidgets.QMainWindow()
        ui2 = ser.Ui_service()
        ui2.setupUi(Ui_choose.MainWindow2 )
        Ui_choose.MainWindow2.show()
        first_win.close()
        
    def retranslateUi(self, choose):
        _translate1 = QtCore.QCoreApplication.translate
        choose.setWindowTitle(_translate1("choose", "MainWindow"))
        self.pushButton_2.setText(_translate1("choose", " FOR AUDIO INPUT"))
        self.pushButton.setText(_translate1("choose", "FOR PUSH BUTTONS"))
        self.pushButton.setStyleSheet("background-color: rgb(208, 255, 205);")
        
        #self.pushButton.setIcon(QtGui.QIcon('grey.jpg'))
        self.pushButton.setStyleSheet("background-image:url(\"grey.jpg\"); ")
        choose.setStyleSheet("background-image:url(\"fridge.jpg\"); ")
        #self.pushButton.setIconSize(QtCore.QSize(300,115))
        self.pushButton_2.setStyleSheet("background-image:url(\"grey.jpg\");")
        #print("def")
        #self.pushButton_2.clicked.connect(self.sec)

if __name__ == "__main__":
#def choice(): 
    import sys
##    app = QtWidgets.QApplication.instance()
##    if not app:
    app = QtWidgets.QApplication(sys.argv)
    choose = QtWidgets.QMainWindow()
    ui = Ui_choose()
    ui.setupUi(choose)
    choose.show()
    sys.exit(app.exec_())
#choice()