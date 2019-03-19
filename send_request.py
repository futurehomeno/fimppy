from fimppy.message import Message, ValueType
from fimppy.address import Address, MsgType, ResourceType
from fimppy.mqtt_transport import MqttTransport


fimp = '''{
    "type" : "cmd.area.get_list",
    "serv" : "vinc_db",
    "val_t" : "null",
    "val" :null,
    "tags" : null,
    "props" : null,
    "ver" : "1",
    "corid" : "",
    "ctime" : "2019-02-09T21:56:43.273561+01:00",
    "uid": "4ed2f969-6a8e-4d55-b73c-dfb5ad900432"
}'''

mq_transport = MqttTransport(hostname = '192.168.1.17')
mq_transport.connect()
msg = Message.from_string(fimp)
req_topic = 'pt:j1/mt:cmd/rt:app/rn:vinculum/ad:1'
resp_topic = 'pt:j1/mt:evt/rt:app/rn:vinculum/ad:1'
response = mq_transport.send_request(req_topic, msg, resp_topic)
print(response)
mq_transport.stop()