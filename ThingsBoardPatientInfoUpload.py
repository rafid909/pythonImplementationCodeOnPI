import paho.mqtt.client as mqtt
import json

#MQTT Connection to thingsboard.io 

#iot_hub = "demo.thingsboard.io"
iot_hub = "demo.thingsboard.io"
port = 1883
#username = "device_user_name"   #Patient Info Device IoT Device
#Need TO Configure IoT Server Based on you need DEMO on  demo.thingsboard.io
username = "device_user_name" #IoT Device User name
password = "device_password" #IoT Device Password
topic = "v1/devices/me/telemetry"  #Device Path Location
client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(iot_hub, port)
print("IoT Server Connection Success")
data = dict()

data["Patient ID"] = "100000520"
data["Patient Name"] = "Md. Abdur Rahim"
data["Patient Gender"] = "Male"
data["Patient Age"] = "22"
data["Description"] = "Patient Information Description"

data_out = json.dumps(data)
client.publish(topic, data_out, 0)