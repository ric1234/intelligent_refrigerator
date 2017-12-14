from aiocoap import *
from PyQt5 import  QtCore,QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import asyncio
import service as ser
def coap():
    print ("waiting for data from fridge")
    
    run=asyncio.get_event_loop().run_until_complete
    protocol=run(Context.create_client_context())
    msg = Message(code=GET, uri="coap://192.168.141.143/receive")
    response = run(protocol.request(msg).response)
    print(response.payload.decode('utf-8'))
    str="Data received Via Coap"
    ser.info(str)
##    msg = QtWidgets.QMessageBox()
##    msg.setMaximumSize(QtCore.QSize(281, 16777215))
##    msg.setGeometry(QtCore.QRect(510, 330, 581, 281))
##    msg.setInformativeText("Data received Via Coap")
##    msg.setStandardButtons(QMessageBox.Ok)
##    msg.exec_()
#coap()