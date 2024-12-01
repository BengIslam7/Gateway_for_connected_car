import tkinter as tk
from tkinter import PhotoImage
import paho.mqtt.client as paho
from paho import mqtt
import datetime
title="Gateway of connected vehicle"
title2="ClimApp"
global client
client = paho.Client(client_id='55', clean_session=True, userdata=None, protocol=paho.MQTTv31)
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("islam", "4.vkP8n2gJh4Dv!")
co=client.connect("60e29047349d4b7ab36cced231cad6ee.s1.eu.hivemq.cloud", 8883)
def Ouvrir(event) :
    x=client.publish("etat", payload="o", qos=1)
    print(x)
    etat.config(text="ON",foreground="green")
def Fermer(event):
    x=client.publish("etat", payload="f", qos=1)
    print(x)
    etat.config(text="OFF",foreground="red")
def Program(event):
    txt=time_entry.get()
    tm=txt.split(":")
    current_time = datetime.datetime.now()
    h=current_time.hour
    m=current_time.minute
    s=current_time.second
    while True:
    	current_time = datetime.datetime.now()
    	h=current_time.hour
    	m=current_time.minute
    	s=current_time.second
    	if(h==int(tm[0]) and m==int(tm[1]) and s==int(tm[2])):
    		break
    e=etat.cget("text")
    if(e=="OFF"):
    	x=client.publish("etat", payload="o", qos=1)
    	print(x)
    	etat.config(text="ON",foreground="green")
    else :
    	y=client.publish("etat", payload="o", qos=1)
    	print(y)
    	etat.config(text="ON",foreground="green")

root = tk.Tk()
root.title(title)
root.geometry("400x550")
frame = tk.Frame(root)
l2 = tk.Label(root, width=27, text=title2,font=("Arial", 20),foreground="blue")
l2.pack(pady=5)
if(co==0):
    l = tk.Label(root, width=27, text="CONNECTED",font=("Arial", 26),foreground="green")
    l.pack(pady=10)
else:
    l = tk.Label(root, width=27, text="FAILED TO CONNECT",font=("Arial", 26),foreground="red")
    l.pack(pady=10)
etat = tk.Label(root, width=27, text="OFF",font=("Arial",20),foreground="red")
etat.pack()
image_path = "clim.png"  # Change this to the path of your image file
img = PhotoImage(file=image_path)
# Create a label and set the image
label = tk.Label(root, image=img)
label.pack()
button = tk.Button(frame, text="ON")
button2 = tk.Button(frame, text="OFF")
time_entry = tk.Entry(root,text ="", font=('calibre',12,'normal'))
time_entry.insert(0,"HH:MM:SS to program") 
button3 = tk.Button(root, text="PROGRAM")
button.bind("<Button-1>", Ouvrir)
button2.bind("<Button-1>", Fermer)
button3.bind("<Button-1>", Program)
button.pack(side=tk.LEFT, padx=10)
button2.pack(side=tk.LEFT, padx=5)
time_entry.pack(pady=5)
button3.pack(pady=10)
frame.pack()
root.mainloop()
