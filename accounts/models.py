# -*- coding: utf-8 -*-
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class Operation(models.Model):
    operation = models.CharField(max_length=10)


class Role(models.Model):
    name = models.CharField(max_length=20)


class Endpoint(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=100)


class Permission(models.Model):
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    operation = models.ForeignKey('Operation', on_delete=models.CASCADE)
    endpoint = models.ForeignKey('Endpoint', on_delete=models.CASCADE)


class SysUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # 自定義user_id為uuid
    role = models.ForeignKey('Role', on_delete=models.CASCADE, blank=True, null=True)



