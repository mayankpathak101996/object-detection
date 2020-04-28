

import paho.mqtt.client as paho
import time

'''def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass'''
def publish_server(user_input):
    #establish connection
    print('mmmm')
    client1.publish("inayaA13vb4yj7dhjqad7",user_input) 
    print('kkkk')
def on_message(client,userdata, msg):
    print('ppppp')
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    print('llllll')	

broker="test.mosquitto.org"
port=1883
client1= paho.Client(str(int(round(time.time() * 1000))))


client1.on_message=on_message
client1.connect(broker,port) 
client1.subscribe("inayaA13vb4yj7dhjqad7",1) 
             
    