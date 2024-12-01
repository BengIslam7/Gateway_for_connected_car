import paho.mqtt.client as paho
from paho import mqtt
import os
import time
os.system("sudo ifconfig eth0 down")
time.sleep(5)
client = paho.Client()
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("islam", "4.vkP8n2gJh4Dv!")
client.connect("60e29047349d4b7ab36cced231cad6ee.s1.eu.hivemq.cloud", 8883)

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    if(str(msg.payload)=="b'o'"):
    	print("ouvrir")
    	with open("UDP.py") as file:
    		exec(file.read())
        
    if(str(msg.payload)=="b'f'"):
    	print("fermer")
    	with open("UDPf.py") as file:
    		exec(file.read()) 

client.on_subscribe = on_subscribe
client.on_message = on_message
client.subscribe('etat', qos=1)

client.loop_forever()

