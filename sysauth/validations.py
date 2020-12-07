# -*- coding: utf-8 -*-
import uuid
from datetime import datetime as dt
from typing import Optional, Text

from pydantic import BaseModel


class User(BaseModel):
    id: Optional[uuid.uuid4]
    name: Optional[Text]
    password: Optional[Text]


class PayLoad(BaseModel):
    user_id: uuid.uuid4
    device: Text
    exp: dt
    iat: dt


class CreateUser(BaseModel):
    name: Text
    password: Optional[Text]
