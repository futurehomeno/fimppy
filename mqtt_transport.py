from paho.mqtt import publish
from paho.mqtt import client
from message import Message, PreMessage
import threading
import time
import json
import logging

class MqttTransport(object):
    """docstring for MqttTransport"""
    def __init__(self, hostname: str = "localhost", port: int = 1883, qos: int = 1, keepalive=60):
        super(MqttTransport, self).__init__()
        self.hostname = hostname
        self.port = port
        self.qos = qos
        self.keepalive = keepalive
        self.mqtt = client.Client(client_id=None, clean_session=True)
        self.active_requests = {}
        self.sub_list = []

    def connect(self):
        self.mqtt.on_connect = self.on_connect
        self.mqtt.on_message = self.on_message
        self.mqtt.connect(self.hostname, self.port, keepalive=self.keepalive)
        self.mqtt.loop_start()

    def stop(self):
        self.mqtt.loop_stop()

    def subscribe(self, topic, qos=-1):
        if qos == -1:
            qos = self.qos
        self.sub_list.append({"topic": topic, "qos": qos})
        self.mqtt.subscribe(topic, qos)

    def publish(self, topic, msg: Message, qos=-1):
        msg_str = json.dumps(msg.to_dict())
        if qos == -1:
            qos = self.qos
        self.mqtt.publish(topic, msg_str, qos=qos, retain=False)
        
    def on_connect(self, client, userdata, flags, rc):
        logging.info("Connected with result code "+str(rc))
        # subscribing previous topics in case of reconnection
        for sub in self.sub_list:
            self.mqtt.subscribe(sub["topic"], sub["qos"])

    def on_message(self, client, userdata, msg):
        fimp_msg = Message.from_string(msg.payload.decode('utf-8','ignore'))
        if len(self.active_requests) > 0:
            for key, val in self.active_requests.items():
                if val["resp_topic"] == msg.topic:
                    logging.info('Respond to %s arrived.'%val["resp_topic"])
                    val["resp_msg"] = fimp_msg
                    val["event"].set()
                    break

    def send_request(self, req_topic, req_msg: Message, resp_topic: str, timeout: int = 5):
        event = threading.Event()
        self.active_requests[req_msg.uid] = {"resp_topic": resp_topic, "event": event, "resp_msg": None}
        self.subscribe(resp_topic)
        self.publish(req_topic, req_msg)
        if event.wait(3):
            resp_msg = self.active_requests[req_msg.uid]["resp_msg"]
            del self.active_requests[req_msg.uid]
            return resp_msg
        del self.active_requests[req_msg.uid]
        return None