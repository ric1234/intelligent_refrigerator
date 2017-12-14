from aiocoap import *
from PyQt5 import  QtCore,QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import asyncio
import service as ser
def coap():
    print ("waiting for data from fridge")
    #receive data as a coap client
    run=asyncio.get_event_loop().run_until_complete
    protocol=run(Context.create_client_context())
    msg = Message(code=GET, uri="coap://192.168.141.143/receive")
    response = run(protocol.request(msg).response)
    print (str(response.payload.decode('utf-8')))
    string1="Data received Via Coap"
    ser.info(string1)
    #return data received
    return str(response.payload.decode('utf-8'))
