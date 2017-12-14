from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import QMessageBox
import sys
class MainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        #set name for window
        self.setWindowTitle("Fridge data")
        self.browser=QWebView()
        #set URL for web view
        self.browser.setUrl(QUrl("http://192.168.141.143:8001"))
        self.setCentralWidget(self.browser)


##app=QApplication(sys.argv)
##window=MainWindow()
##window.show()
##app.exec()
