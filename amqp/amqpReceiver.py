import pika
import sys
import os
import subprocess

from pika.adapters import BlockingConnection
sys.path.append('/home/pi/Amazon-DRS-master')
print("b4 include")
import CloudGatewayServer as wh


#callback called when amqp message received
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    wh.run_webhost()
    
##    p = subprocess.Popen(["python", "/home/pi/Amazon-DRS-master/webhost_v3.py"], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
##    print (p.communicate()[0])

##    os.system("python /home/pi/Amazon-DRS-master/webhost_v3.py")
    
#defining parameters for amqp connection and receiving messages
def para():
    print("in para")
    
    #connect to publisher using user and password of publisher and IP
    parameters = pika.URLParameters('amqp://user:pass@192.168.141.195:5672/%2F') 

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='hello')
    
    channel.basic_consume(callback,
                          queue='hello',
                          no_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    print("para b4")
    while True:
        para()
