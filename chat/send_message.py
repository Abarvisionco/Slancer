import datetime
from kavenegar import *
from random import randint
from . import models

def sent(mobile, name, yaro, chat):
    mobile = [mobile,]
    try:
        api = KavenegarAPI('57725246434A74555663544635727A44686C4C7442705571693476694B4164584575555A4964723454384D3D')
        params = {
            'receptor': mobile,
            'template': 'new-message-slancer',
            'token': name,
            'token2':yaro,
            'token3':chat,
            'type': 'sms',  # sms vs call
        }
        response = api.verify_lookup(params)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
