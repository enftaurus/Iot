#server
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("connected with MQTT server " + str(rc))
    client.subscribe("iot/topic179")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()

#client
import time
import sys
import paho.mqtt.publish as publish

sys.path.append("/home/pi/ETS_IoT_KIT_demo/DemoCode/BME280")

import BME280lib as b

while True:
    t, p, h = b.readBME280All()
    print(t)

    publish.single(
        "iot/topic179",
        "Temperature:%s" % t,
        hostname="test.mosquitto.org"
    )

    time.sleep(1)

print('done')