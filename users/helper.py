import datetime
from kavenegar import *
from random import randint
from . import models

def sent_otp(mobile, otp):
    mobile = [mobile,]
    try:
        api = KavenegarAPI('57725246434A74555663544635727A44686C4C7442705571693476694B4164584575555A4964723454384D3D')
        params = {
            'receptor': mobile,
            'template': 'test',
            'token': otp,
            'type': 'sms',  # sms vs call
        }
        response = api.verify_lookup(params)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


def get_random_otp():
    return randint(1000,9999)


def check_otp_expire(mobile):
    try:
        user = models.User.objects.get(mobile=mobile)
        now = datetime.datetime.now().astimezone()
        otp_time = user.otp_create_time.astimezone()
        print(otp_time)
        print(now)
        diff_time = now - otp_time

        print("OTP Time: ",diff_time)
        if diff_time.seconds > 120:
            return False
        else:
            return True
    except models.User.DoesNotExist:
        return False
