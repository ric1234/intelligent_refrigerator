from gpiozero import DistanceSensor
import RPi.GPIO as GPIO
import time
import boto3
import sys
import os
import datetime



##def initialize():
# Get the service resource.
##print("Before dynamo defined")
##dynamodb = boto3.resource('dynamodb')


from flask import Flask, render_template, redirect

def run_webhost():
    
    print("Before dynamo defined")
    dynamodb = boto3.resource('dynamodb')


    print("Before app defined")
    app = Flask(__name__)
    
    #Create instance of DynamoDB table "FridgeItem"
    table = dynamodb.Table('FridgeItem')
    print("Table creation time:")
    print(table.creation_date_time)

    dis = 0.24#ultrasonic.distance
##    dis = float(input("Enter dis:"))
    current_time = str(datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S"))
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
                'Date': current_time,
            }
        )
        print(table.item_count)
        homepage = 'replenish.html'

#tell flask what function should be triggered for a particular url
    @app.route('/')
    def index():
        return render_template(homepage)

    @app.route('/authresponse')
    def authresponse():
        return render_template('response.html')

    @app.route('/accesstoken/<var>')
    def accesstoken(var):
        import requests
        r = requests.post("https://api.amazon.com/auth/o2/token", data={'grant_type': 'authorization_code', 'code': var, 'client_id': 'amzn1.application-oa2-client.d615ccdea7524fa7853fe3d45659570a', 'client_secret':'a5261a83e8a998ca7c1354fc2844e994c3387bfef8e900564064276105fbe648','redirect_uri':'https://192.168.141.129:8100/authresponse'})
        data = r.json()
        accesstoken = data['access_token']
        token = 'Bearer ' + accesstoken
        x = requests.post("https://dash-replenishment-service-na.amazon.com/replenish/f76f5d12-1404-483a-97b1-f3fdc1dcf869", headers={'Authorization': token, 'x-amzn-accept-type': 'com.amazon.dash.replenishment.DrsReplenishResult@1.0', 'x-amzn-type-version': 'com.amazon.dash.replenishment.DrsReplenishInput@1.0'})
        print("After post")
        return redirect("https://192.168.141.129:8100/sucess")

    @app.route('/sucess')
    def sucess():
        return render_template('sucess.html')
        quit()
        
        
    context = ('/home/pi/Amazon-DRS-master/server.crt','/home/pi/Amazon-DRS-master/server.key')
##    Start flask server 
    app.run(host='192.168.141.129', debug=False, port=8100, ssl_context=context)

    ##def main_old():
    ##    context = ('/home/pi/Amazon-DRS-master/server.crt','/home/pi/Amazon-DRS-master/server.key')
    ##    app.run(host='192.168.141.129', debug=False, port=8100, ssl_context=context)


    ##if __name__ == '__main__':
    ##    main_old()
    ##    context = ('/home/pi/Amazon-DRS-master/server.crt','/home/pi/Amazon-DRS-master/server.key')
    ##    app.run(host='192.168.141.129', debug=False, port=8100, ssl_context=context)
        
