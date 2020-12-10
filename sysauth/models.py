# -*- coding: utf-8 -*-
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Operation(models.Model):
    operation = models.CharField(max_length=10)


class Role(models.Model):
    role_name = models.CharField(max_length=20)


class Resource(models.Model):
    resource_class = models.CharField(max_length=10)
    name = models.CharField(max_length=10)


class Permission(models.Model):
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    operation = models.ForeignKey('Operation', on_delete=models.CASCADE)
    resource = models.ForeignKey('Resource', on_delete=models.CASCADE)


class SysUser(AbstractUser):
    """
    Reference: https://github.com/RuiCoreSci/auth/blob/master/orm/user.py
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # 自定義user_id為uuid
    role = models.ForeignKey('Role', on_delete=models.CASCADE, blank=True, null=True)

    def get_permission(self):
        if self.role_id is not None:
            print('debug: user\'s role_id is None.')

        perms = Permission.objects.get(id=self.role_id).all()
        return perms







