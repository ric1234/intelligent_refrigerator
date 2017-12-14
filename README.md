This project is a joint collaboration of Richard Norhonna, Riya Biswas and Tejas Shanbhag for ECEN 5053-002 Embedded Interface and Design course at University of Colorado Boulder


The project is an intelligent refrigerator which reorders stuff required from the amazon DRS automatically without much interference of the user.  
The project consists of three raspberry pi's forming three machines, one handling it's computations at the fridge, one stays as device with the user and the last one acts as a cloud-gateway.  
The rpi at the fridge has a camera interfaced and is placed inside the fridge and uses machine learning(tensor flow) and Image processing(Open Cv) to estimate the kind and amount of dara.  
The same rpi then forms a table and transmits the data to a webserver which is an html interface.  
It then sends the data to the user rpi via CoAP whenever requested.  
The User RPI has a user interface which starts with an RFID authentication and then takes input from the user either tangibly or with voice.  
Now the user rpi either receives data from the fridge rpi, views data uploaded on the html interface or sends data to the cloud-gateway.  
The cloud-gateway receives the data and simultaneosly runs a python webserver sending the data to DRS and also is saved to dynamo DB as a log of it.  
Once the user confirms the order, a Lambda is triggered which sends an acknowledgement to the user via MQTT.  
Also, an email is received to the user via SNS.  

Now, for the initialization part:  
Fridge RPi: 
For this RPi, the OpenCV library first needs to be installed on the RaspberryPi.  
The PiCamera library needs to be installed to use the PiCamera via the ports provided on the RaspberryPi.   
TensorFlow is a Machine Learning Library that needs to be installed to identify the various items present in the fridge.  
NodeJs needs to be installed to compile the NodeJs server.  
The Aiocoap library was installed to implement the Coap communication between the FridgeRpi and the Rpi User.  
Before implementing the final interface, we need to make sure that the IP addresses are set properly in the /fridge/node/index.html, /fridge/node/fridge_image.jpg file and the /fridge/node/webserver.js file  
Three processes need to be run to get the fridge Rpi to work as described in the Functional Description.   
The first file to be run is /fridgeRpi/tensor/main.py using the command:  
python3 main.py  
This will run the camera with OpenCV, run TensorFlow to identify the objects, save this data into the text file and HTML file   
The second file to be run is the coap server which can be found in the /fridgeRpi/node/my_server.py
python3 my_server.py  
This will run the server for coap which the client coap on the userRpi can connect to, to obtain the data from the fridge  


The third file to be run is the NodeJs server to send data to a web interface. This can be found in the /fridge/node/webserver.js file
node webserver.py  
This will run the NodeJS server which serves the client with the an HTML page. This HTML page can be viewed by any browser on the local area network with access to the Rpi.   
The IP and the port need to be entered to the address bar. Port has been set to 8001 but can be changed when modifying the ip. The HTML contains some Javascript with AJAX to make asynchronous requests to the NodeJS server. The NodeJS server is also capable of displaying the CSS files and Javascript and AJAX queries.  


User Pi :   
The codes for this part are found in the folder qt.  
Enable the SPI interface using raspi-config and reboot the raspberry pi for the SPI to be functional with the interfacing with the RFID sensor.  
Use the Read.py code to read or verify the id on any RFID tag.  
For the USB mouse, since it is a microphone, after you connect it, follow the commands  nano ~/.asoundrc and change card 0 to card 1 as shown below  
pcm.!default { type hw card 1 } ctl.!default { type hw card 1 }  
Similarly do  sudo nano /usr/share/alsa/alsa.conf  
Scroll below and change  defaults.ctl.card 0 defaults.pcm.card 0  
to defaults.ctl.card 1 defaults.pcm.card 1.  
Check your microphone before proceeding. Get PyQt5 installed on your device along with any version of python 3.  
To run the whole sequence, just run python3 firstwin.py and use the Gui to move ahead.  
Install the certificates for AMQP and MQTT as explained in the next section.  

 
RPi CloudGateway:  
This uses Raspbian Stretch OS and Python 3.5.3  
Set up Rpi for MQTT  
Use package installer pip3 to install MQTT Paho client to subscribe and publish MQTT message. Since Amazon Web Services acts as our broker, we do not need to install any packages to configure our Raspberry Pi as one.  
Install the AWS CLI for Python 3.5  
Set up an AWS IoT thing, create certificate and key, and store them.  
Create a AWS IoT policy and attach a certificate to it. Then attach the certificate to the AWS IoT thing created earlier.  
For more informtion: https://www.hackster.io/mariocannistra/python-and-paho-for-mqtt-with-aws-iot-921e41  

Set up Rpi for AMQP:  
Install the RabbitMQ server and the Python 3.5 package ‘pika’ to subscribe and publish AMQP messages.  

Run web host for Amazon DRS:  
cloudGatewayRpi contains the folder ‘amqp’. Run the amqpReceiver.py file to start the AMQP server.   
It calls the run_webhost() function from the CloudGatewayServer.py file (in Amazon-DRS-master folder).  
All the certificates necessary for Amazon Dash Replenishment Service are present in the Amazon-DRS-master folder.  
The cloudGatewayRpi/Amazon-DRS-master/templates/ folder contains the HTML pages to connect, authorization and redirect to Amazon DRS website.  





As for the requirements for the course:  
Almost all of the super-project requirements were met with additional functions  

The basic requirements met are:  
Two raspberry pi modules communicating with each other.  
Using OpenCv to process the image   
Use of camera module.  
MQTT protocol from lambda to user pi  
CoAP protocol for communication between Pi’s  
Websockets using NodeJS  
RFID sensor using SPI interface for authentication  
Amazon DRS ordering items  
Microphone as USB voice input with Google speech recognition  
DynamoDB for logging  
A screen interface  
PyQt interface  
HTML interface   
A acknowledgement email received through SNS  

The extra-credit requirements accomplished are:  
Use of Machine Learning(TensorFlow) for identification and counting of object  
Addition of another websocket which is python based.   
Use of Javascript and AJAX for updating the html data sent to the server  
Addition of the 3rd pi as a cloud-gateway  
Addition of AMQP(RabitMQ) for communication between the user and the cloud-gateway.  

