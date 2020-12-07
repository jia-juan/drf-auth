# -*- coding: utf-8 -*-
import pytz
from datetime import datetime as dt
from datetime import timedelta
from django.conf import settings

from .token import Token
from ..settings import JWT_LIFE_SPAN
from ..models import SysUser
tz = pytz.timezone(settings.TIME_ZONE)


class Authorize:
    @staticmethod
    def authorize(user: SysUser, device: str = "pc", auto_delete=True) -> str:
        """
        :param user:
        :param device:
        :param auto_delete: 過期是否刪除，默認為 True
        :return:
        TODO: redis部分暫時
        """
        exp = dt.now(tz) + timedelta(seconds=JWT_LIFE_SPAN)
        token = Token.encode(user, exp=exp, device=device)
        # await redis.execute("SET", f"{user.id}-{token}", "True")
        if auto_delete:
            expire_at = (exp + timedelta(seconds=JWT_LIFE_SPAN)).timestamp()
            # await redis.execute("EXPIREAT", f"{user.id}-{token}", int(expire_at))
        return token

    @staticmethod
    def revoke(token: str) -> bool:
        try:
            payload = Token.decode(token)
        except:  # noqa
            pass
        else:
            pass
            # await redis.execute("DEL", f"{payload.id}-{token}")
        return True

    @staticmethod
    def revoke_all(user: SysUser):
        pass
        # tokens = await redis.execute("KEYS", f"{user.id}-*")
        # await redis.execute("DEL", *tokens)