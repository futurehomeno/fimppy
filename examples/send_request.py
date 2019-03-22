import logging
logging.basicConfig(filename='mqtt_logs.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
from fimppy.message import Message
from fimppy.mqtt_transport import MqttTransport

req_topic = 'pt:j1/mt:cmd/rt:app/rn:vinculum/ad:1'
resp_topic = 'pt:j1/mt:evt/rt:app/rn:vinculum/ad:1'

mq_transport = MqttTransport(hostname = 'dev-sdu-lg-beta.local')
mq_transport.connect()
msg = Message.from_prev(PreMessage.GET_DEVICELIST)
response = mq_transport.send_request(req_topic, msg, resp_topic)
print(response)

msg = Message.from_prev(PreMessage.GET_ROOMLIST)
response = mq_transport.send_request(req_topic, msg, resp_topic)
print(response)

msg = Message.from_prev(PreMessage.GET_AREALIST)
response = mq_transport.send_request(req_topic, msg, resp_topic)
print(response)

msg = Message.from_prev(PreMessage.GET_SHORTCUTLIST)
response = mq_transport.send_request(req_topic, msg, resp_topic)
print(response)

mq_transport.stop()