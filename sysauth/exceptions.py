# -*- coding: utf-8 -*-
class SysAuthException(BaseException):
    def __init__(self, msg):
        super(SysAuthException, self).__init__(msg)


class InvalidToken(SysAuthException):
    pass


class ObjectNotExist(SysAuthException):
    pass


class OperationNotAllowed(SysAuthException):
    pass


class InvalidPassword(SysAuthException):
    pass

