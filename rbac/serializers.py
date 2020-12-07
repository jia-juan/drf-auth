# -*- coding: utf-8 -*-
# from rest_framework import serializers
#
# from .models import SysUser
# from .models import InOutLog
#
#
# class InOutLogSerializer(serializers.ModelSerializer):
#     user = serializers.SerializerMethodField()
#
#     class Meta:
#         model = InOutLog
#         fields = []
#
#     def get_user(self):
#         return SysUser.objects.get(id=self.context.get('request').user.id).value('user')