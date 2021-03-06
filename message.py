from enum import Enum
import uuid
import json
from datetime import datetime

class ValueType(Enum):
    STRING = 'string'
    INT = 'int'
    FLOAT = 'float'
    BOOL = 'bool'
    NULL = 'null'
    STR_ARRAY = 'str_array'
    INT_ARRAY = 'int_array'
    FLOAT_ARRAY = 'float_array'
    BOOL_ARRAY = 'bool_array'
    STR_MAP = 'str_map'
    INT_MAP = 'int_map'
    FLOAT_MAP = 'float_map'
    BOOL_MAP = 'bool_map'
    OBJECT = 'object'

class PreMessage(Enum):
    GET_AREALIST = {'serv': 'vinc_db', 'type': 'cmd.area.get_list'}
    GET_ROOMLIST = {'serv': 'vinc_db', 'type': 'cmd.room.get_list'}
    GET_DEVICELIST = {'serv': 'vinc_db', 'type': 'cmd.device.get_list'}
    GET_SHORTCUTLIST = {'serv': 'vinc_shortcut', 'type': 'cmd.shortcut.get_list'}

class Message:
    def __init__(self, service='', msg_type='', value=None, value_type: ValueType='string', props={}, request_msg=None, ctime=None, uid:str=''):
        self.service = service
        self.msg_type = msg_type
        self.value = value
        self.value_type = value_type
        self.tags = []
        self.props = props
        if ctime:
            self.mctime = ctime
        else:
            self.mctime = self.get_timestamp()

        if uid:
            self.uid = uid
        else:
            self.uid = str(uuid.uuid4())
        self.ver = '1.0'
        self.corid = ''

        if request_msg:
            self.corid = request_msg.uid

    @classmethod
    def from_dict(cls, fimp):
        assert type(fimp) == dict, 'datatype for fimp can be dict'
        print(fimp)
        msgobj = cls(service = fimp['serv'], 
                        msg_type = fimp['type'], 
                        value_type = fimp['val_t'], 
                        value = fimp['val'], 
                        props = fimp['props'])
        msgobj.tags = fimp['tags']
        if 'ctime' in fimp :
            msgobj.mctime = fimp['ctime']
        if 'uid' in fimp :
            msgobj.uid = fimp['uid']
        if 'corid' in fimp :
            msgobj.corid = fimp['corid']
        return msgobj

    @classmethod
    def from_string(cls, fimp):
        assert type(fimp) == str, 'datatype for fimp can be str'
        return cls.from_dict(json.loads(fimp))

    @classmethod
    def from_prev(cls, prev: PreMessage):
        jmsg = dict()
        jmsg['serv'] = prev.value['serv']
        jmsg['type'] = prev.value['type']
        jmsg['val_t'] = None
        jmsg['val'] = None
        jmsg['tags'] = None
        jmsg['props'] = None
        jmsg['ctime'] = Message.get_timestamp()
        jmsg['ver'] = '1.0'
        jmsg['uid'] = str(uuid.uuid4())
        return cls.from_dict(jmsg)

    def __str__(self):
        return 'service = %s , msg_type = %s , val_type = %s \n value = %s  \n props : %s \n uuid : %s \n corid : %s \n'%(
            self.service, self.msg_type, self.value_type , self.value , self.props , self.uid ,self.corid
        )

    def __eq__(self, other):
        return self.msg_type == other.msg_type and self.value == other.value and self.props == other.props

    def __ne__(self, other):
        return not self.__eq__(other)

    def to_dict(self):
        jmsg = dict()
        jmsg['serv'] = self.service
        jmsg['type'] = self.msg_type
        jmsg['val_t'] = str(self.value_type)
        jmsg['val'] = self.value
        jmsg['tags'] = self.tags
        jmsg['props'] = self.props
        jmsg['ctime'] = self.mctime
        jmsg['ver'] = self.ver
        jmsg['uid'] = self.uid
        return jmsg

    @staticmethod
    def get_uuid():
        return str(uuid.uuid4())

    @staticmethod
    def get_timestamp():
        return datetime.now().isoformat()