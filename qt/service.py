# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import amqpsend as amqp
import web as wb
class Ui_service(object):
    def setupUi(self, service):
        service.setObjectName("service")
        service.resize(800, 480)
        service.setStyleSheet("background-color: rgb(224, 245, 255);")
        self.centralwidget = QtWidgets.QWidget(service)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 230, 220, 91))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(71, 13, 216);\n"
"background-color: rgb(179, 226, 255);\n"
"border-color: rgb(0, 0, 127);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 230, 220, 91))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(71, 13, 216);\n"
"background-color: rgb(179, 226, 255);\n"
"border-color: rgb(0, 0, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 230, 220, 91))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(71, 13, 216);\n"
"background-color: rgb(179, 226, 255);\n"
"border-color: rgb(0, 0, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(239, 255, 255);\n"
"color: rgb(0, 0, 127);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 10, 141, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 731, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(97, 181, 255);\n"
"border-color: rgb(58, 23, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        service.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(service)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        service.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(service)
        self.statusbar.setObjectName("statusbar")
        service.setStatusBar(self.statusbar)
        timer = QtCore.QTimer()
        timer.timeout.connect(update_label)
        timer.start(1000)  # every 1000 milliseconds
        self.pushButton_2.clicked.connect(amqp.rabbit)
        self.pushButton_3.clicked.connect(Ui_service.fridgedata)
        self.retranslateUi(service)
        QtCore.QMetaObject.connectSlotsByName(service)

    def retranslateUi(self, service):
        _translate = QtCore.QCoreApplication.translate
        service.setWindowTitle(_translate("service", "MainWindow"))
        self.pushButton.setText(_translate("service", "Update Order List"))
        self.pushButton_2.setText(_translate("service", "Place Order"))
        self.pushButton_3.setText(_translate("service", "View Item List"))
        self.pushButton_4.setText(_translate("service", "Back"))
        self.label.setText(_translate("service", "TIME HERE"))
        self.label_2.setText(_translate("service", "Hello Amazon Dash User! Please select a service."))
        
    def fridgedata(self):
        Ui_service.window=wb.MainWindow()
        Ui_service.window.show()
##        Ui_choose.MainWindow4= QtWidgets.QMainWindow()
##        ui2 = ser.Ui_service()
##        ui2.setupUi(Ui_choose.MainWindow2 )
##        Ui_choose.MainWindow2.show()
##        self.setWindowTitle("Fridge data")
##        self.browser=QWebView()
##        self.browser.setUrl(QUrl("http://192.168.43.70:8001"))
##        self.setCentralWidget(self.browser)
def update_label():
    global current_time
    current_time = str(datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S"))
    ui.label.setText(current_time)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    service = QtWidgets.QMainWindow()
    ui = Ui_service()
    ui.setupUi(service)
    service.show()
    timer = QtCore.QTimer()
    timer.timeout.connect(update_label)
    timer.start(1000)  # every 1000 milliseconds
    sys.exit(app.exec_())
    


