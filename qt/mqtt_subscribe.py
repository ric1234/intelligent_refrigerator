# Import package
import paho.mqtt.client as mqtt
import ssl
import service as ser
def subscribe():
    # Define Variables
    MQTT_PORT = 8883
    MQTT_KEEPALIVE_INTERVAL = 45
    MQTT_TOPIC = "helloTopic1"
    MQTT_MSG = "hello1 MQTT"

    MQTT_HOST = "a2rgr0dnnz0h89.iot.us-west-2.amazonaws.com"
    CA_ROOT_CERT_FILE = "/home/pi/EID/Qt/aiocoap/paho/root-CA.crt"
    THING_CERT_FILE = "/home/pi/EID/Qt/aiocoap/paho/RaspberryUser.cert.pem"
    THING_PRIVATE_KEY = "/home/pi/EID/Qt/aiocoap/paho/RaspberryUser.private.key"

    # Define on connect event function
    # We shall subscribe to our Topic in this function
    def on_connect(self, mosq, obj, rc):
        mqttc.subscribe(MQTT_TOPIC, 0)

    # Define on_message event function. 
    # This function will be invoked every time,
    # a new message arrives for the subscribed topic 
    def on_message(mosq, obj, msg):
            print("Topic: " + str(msg.topic))
            print("QoS: " + str(msg.qos))
            print("Payload: " + str(msg.payload))
            mqttc.loop_stop()
            ser.info("Order placed on DRS")
            
            

    def on_subscribe(mosq, obj, mid, granted_qos):
        print("Subscribed to Topic: " + 
            MQTT_MSG + " with QoS: " + str(granted_qos))

    # Initiate MQTT Client
    mqttc = mqtt.Client()

    # Assign event callbacks
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_subscribe = on_subscribe

    # Configure TLS Set
    mqttc.tls_set(CA_ROOT_CERT_FILE, certfile=THING_CERT_FILE, keyfile=THING_PRIVATE_KEY, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)


    # Connect with MQTT Broker
    mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

    #mqttc.loop(1)
    # Continue monitoring the incoming messages for subscribed topic
    mqttc.loop_start()
    #mqttc.loop(1)
    return
#subscribe()