import pika
import service as ser
import mqtt_subscribe as sub
#connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.21.77.95'))
def rabbit():
    
    parameters = pika.URLParameters('amqp://user:pass@192.168.141.129:5672/%2F')
    connection = pika.BlockingConnection()
    #connection = pika.BlockingConnection()
    channel = connection.channel()
    #print("bijli")
    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='ncajcnioancio')
    str="AMQP Data sent"
    print(str)
    ser.info(str)
    connection.close()
    sub.subscribe()
#rabbit()