# -*- coding: utf-8 -*-
import pytz
from datetime import datetime as dt

import jwt
from django.conf import settings

from ..settings import JWT_ALGORITHM, JWT_SECRET_KEY
from ..models import SysUser
from ..validations import PayLoad
tz = pytz.timezone(settings.TIME_ZONE)


class Token:
    @staticmethod
    def encode(user: SysUser, exp: dt, device: str = 'pc') -> str:
        payload = {'user_id': user.id, 'device': device, 'exp': exp, 'iat': dt.now(tz)}
        return jwt.encode(payload, JWT_SECRET_KEY, JWT_ALGORITHM).decode('utf-8')

    @staticmethod
    def decode(token: str, verify_exp: bool = True) -> PayLoad:
        payload = jwt.decode(
            token,
            key=JWT_SECRET_KEY,
            options={'verify_exp': verify_exp},
            algorithms=[JWT_ALGORITHM],
        )
        return PayLoad(**payload)