import pika
import service as ser
import mqtt_subscribe as sub
#connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.21.77.95'))
def rabbit():
    #passing the receiver's IP using url method
    #print ( data)
    parameters = pika.URLParameters('amqp://user:pass@192.168.141.129:5672/%2F')
    connection = pika.BlockingConnection()
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    #send required data
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body="bucket =1")
    str="AMQP Data sent"
    print(str)
    #call information message box
    ser.info(str)
    #close amqp connection
    connection.close()
    #subscribe for mqtt
    sub.subscribe()
#rabbit()