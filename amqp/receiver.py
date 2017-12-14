import pika
import sys
from pika.adapters import BlockingConnection
##sys.path.append('/home/pi/Amazon-DRS-master')
##import webhost as wh


#connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.21.77.95'))
'''credentials = pika.PlainCredentials('rpi_ts', 'raspberry')
parameters = pika.ConnectionParameters('172.21.78.149',
                                       5672,
                                       '/',
                                       credentials)'''
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
##    wh.main_old()
    
##def para():
##print("in para")
parameters = pika.URLParameters('amqp://user:pass@172.21.77.95:5672/%2F')

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

##if __name__ == '__main__':
##    para()
