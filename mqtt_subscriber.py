#importing the necessary packages
import paho.mqtt.client as mqtt
import time

#a function to print the received message with client data and message received
def on_message(client,userdata,message):
	print("Recieved message: ",str(message.payload.decode("utf-8")))

#setting up the ip address and port of the server to communicate
mqttBroker = "192.168.64.2"
client = mqtt.Client("Smartphone")
client.connect(mqttBroker, 1883)

#subscribing to the topic temperature
client.loop_start()
client.subscribe("TEMPERATURE")
client.on_message = on_message
time.sleep(30)
client.loop_stop()

