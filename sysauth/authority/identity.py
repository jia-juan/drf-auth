# -*- coding: utf-8 -*-
import uuid

from .password import Password
from ..models import SysUser
from ..exceptions import InvalidPassword, ObjectNotExist


class Identity:
    @staticmethod
    def identity(user_id: uuid.uuid4, password: str) -> SysUser:
        user = SysUser.objects.get(id=user_id)
        if not user:
            raise ObjectNotExist('用戶不存在')
        if not Password.verify(password, user.password):
            raise InvalidPassword('用戶密碼錯誤')
        return user

