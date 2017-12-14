##from PyQt5.QtCore import *
##from PyQt5.QtWidgets import *
##from PyQt5.QtGui import *
##from PyQt5.QtWebKitWidgets import *
##import threading
##import sys
##class MainWindow(QMainWindow):
##    def __init__(self,*args,**kwargs):
##        super(MainWindow,self).__init__(*args,**kwargs)
##        self.setWindowTitle("Fridge data")
##        self.browser=QWebView()
##        thread1=mythread()
##        thread1.start()
##        thread1.join()
##        #self.browser.setUrl(QUrl("http://192.168.43.70:8001"))
##        self.browser.setUrl(QUrl("http://www.google.com"))
##        self.setCentralWidget(self.browser)
##
##class mythread(threading.Thread):
##    def __init(self):
##        threading.Thread.__init__(self)
##        
##    def run(self):
##        print ("Just for fun")
##            
###def view():
##
##app=QApplication(sys.argv)
##window=MainWindow()
###thread2=mythread()
###thread2.start()
###thread2.join()
##window.show()
##app.exec()
###view()

###function()
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebKitWidgets import *
import sys
class MainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        self.setWindowTitle("Fridge data")
        self.browser=QWebView()
        #self.browser.load(QUrl('http://192.168.141.129:8100'))
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)


app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()

