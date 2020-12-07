# -*- coding: utf-8 -*-
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser


# Ref: https://stackoverflow.com/questions/32311048/change-the-type-of-user-id-to-uuid/32311120
# class SysUser(AbstractUser):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # 自定義user_id為uuid


# class InOutLog(models.Model):
#     user = models.ForeignKey(SysUser, on_delete=models.CASCADE)
#     act_type = models.CharField(max_length=7,
#                                 choices=(
#                                     ('login', 'login'),
#                                     ('refresh', 'refresh'),
#                                     ('logout', 'logout')))
#     at_time = models.DateTimeField(auto_now_add=True)


# class Action(models.Model):
#     app_name = models.CharField(max_length=15)
#     endpoint = models.URLField()
#     method = models.CharField(
#         choices=(
#             ('get', 'get'),
#             ('post', 'post'),
#         ),
#         blank=True, null=True,
#         max_length=4
#     )
#     description = models.CharField(max_length=50, blank=True, null=True)
#
#
# class GroupActionPermission(models.Model):
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     action = models.ForeignKey('Action', on_delete=models.CASCADE)