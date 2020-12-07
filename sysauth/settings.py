# -*- coding: utf-8 -*-
from pathlib import Path

SQLITE_URI = Path(__file__).parent.parent / 'db.sqlite3'
JWT_ALGORITHM = 'HS256'
JWT_SECRET_KEY = '8f1bd7696ffb482d8486dfbc6e7d16dd-secret-key'  # TODO: copy from git: https://github.com/RuiCoreSci/auth
JWT_LIFE_SPAN = 24 * 60 * 60  # seconds
JWT_AUTH_HEADER = 'Auth'
