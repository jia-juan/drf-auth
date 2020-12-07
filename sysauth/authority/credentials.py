# -*- coding: utf-8 -*-
import uuid
from typing import List, Optional, Text

from pydantic import BaseModel


class Permission(BaseModel):
    name: Text


class AuthCredentials(BaseModel):
    user_id: Optional[uuid.uuid4] = None
    scopes: Optional[set] = {}
    logged_in: bool = False
    error_message: str = ""

    @property
    def is_admin(self):
        return True

    def permissions(self) -> List[Permission]:
        assert self.user_id is not None, "請先登入"
        return NotImplemented()


class AuthUser(BaseModel):
    user_id: Optional[uuid.uuid4]

    @property
    def is_authenticated(self) -> bool:
        return self.user_id is not None

    @property
    def display_id(self) -> int:
        return self.user_id
