import paho.mqtt.client as mqtt

class SmartHome:
    def __init__(self):
        self.client = mqtt.Client("NOVA")
        self.client.connect("homeassistant.local", 1883)

    def control_light(self, state):
        self.client.publish("home/lights", "ON" if state else "OFF")