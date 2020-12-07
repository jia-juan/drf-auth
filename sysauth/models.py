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


class SysUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # 自定義user_id為uuid
    role = models.ForeignKey('Role', on_delete=models.CASCADE, blank=True, null=True)


class Permission(models.Model):
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    operation = models.ForeignKey('Operation', on_delete=models.CASCADE)
    resource = models.ForeignKey('Resource', on_delete=models.CASCADE)


