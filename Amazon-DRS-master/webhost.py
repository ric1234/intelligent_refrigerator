from gpiozero import DistanceSensor
import RPi.GPIO as GPIO
import time
import boto3


# Get the service resource.
dynamodb = boto3.resource('dynamodb')
GPIO.setmode(GPIO.BCM)
ultrasonic = DistanceSensor(echo=17, trigger=4, threshold_distance=0.2)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

from flask import Flask, render_template, redirect

app = Flask(__name__)
table = dynamodb.Table('FridgeItem')
print("Table creation time:")
print(table.creation_date_time)

#dis = ultrasonic.distance
dis = float(input("Enter dis:"))
if dis<0.15:
    #no replenishment, green led
    #GPIO.output(27,GPIO.LOW)
    #GPIO.output(18,GPIO.HIGH)
    homepage = 'index.html'
else:
    #replenish, red led
    #GPIO.output(27,GPIO.HIGH)
    #GPIO.output(18,GPIO.LOW)
    table.put_item(
        Item={
            'ASIN': 'B00NTCHCU2',
            'Date': '12/11',
        }
    )
    print(table.item_count)
    homepage = 'replenish.html'

@app.route('/')
def index():
    return render_template(homepage)

@app.route('/authresponse')
def authresponse():
    return render_template('response.html')

@app.route('/accesstoken/<var>')
def accesstoken(var):
    import requests
    r = requests.post("https://api.amazon.com/auth/o2/token", data={'grant_type': 'authorization_code', 'code': var, 'client_id': 'amzn1.application-oa2-client.d615ccdea7524fa7853fe3d45659570a', 'client_secret':'a5261a83e8a998ca7c1354fc2844e994c3387bfef8e900564064276105fbe648','redirect_uri':'https://10.201.29.204:8100/authresponse'})
    data = r.json()
    accesstoken = data['access_token']
    token = 'Bearer ' + accesstoken
    x = requests.post("https://dash-replenishment-service-na.amazon.com/replenish/f76f5d12-1404-483a-97b1-f3fdc1dcf869", headers={'Authorization': token, 'x-amzn-accept-type': 'com.amazon.dash.replenishment.DrsReplenishResult@1.0', 'x-amzn-type-version': 'com.amazon.dash.replenishment.DrsReplenishInput@1.0'})
    print("After post")
    return redirect("https://10.201.29.204:8100/sucess")

@app.route('/sucess')
def sucess():
    return render_template('sucess.html')

##def main_old():
    

if __name__ == '__main__':
    context = ('/home/pi/Amazon-DRS-master/server.crt','/home/pi/Amazon-DRS-master/server.key')
    app.run(host='10.201.29.204', debug=True, port=8100, ssl_context=context)
##    main_old()