# # -*- coding: utf-8 -*-
# import pytz
# import datetime
#
# from django.conf import settings
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import permissions
# from rest_framework_jwt.views import ObtainJSONWebTokenView
# from rest_framework_jwt.views import RefreshJSONWebTokenView
# from rest_framework_jwt.blacklist.models import BlacklistedToken
#
# from .models import InOutLog
# from .serializers import InOutLogSerializer
# from .utils import refresh_token
# tz = pytz.timezone(settings.TIME_ZONE)
#
#
# class LoginView(ObtainJSONWebTokenView):
#     pass
#     # def post(self, request, *args, **kwargs):
#         # try:
#         #     InOutLog.objects.create(user=request.user, act_type='login')
#         # except Exception:
#         #     raise RuntimeError('login log write failed.')
#
#
# class TokenRefreshView(RefreshJSONWebTokenView):
#
#     serializer_class = InOutLogSerializer
#     permission_classes = (permissions.AllowAny, )  # TODO: 記得改掉, permissions.AllowAny方便測試
#
#     def post(self, request, *args, **kwargs):
#
#         try:
#             serializer = InOutLogSerializer(user=request.user, act_type='refresh')
#             if serializer.is_valid():
#                 serializer.save()
#         except Exception:
#             raise RuntimeError('refresh log write failed.')
#
#
# class LogoutView(APIView):
#
#     permission_classes = (permissions.AllowAny, )  # TODO: 記得改掉, permissions.AllowAny方便測試
#
#     def post(self, request, *args, **kwargs):
#         try:
#             current_token = request.data['token']
#             refresh_res = refresh_token(current_token)
#             exp = datetime.datetime.fromtimestamp(refresh_res['issued_at'], tz).isoformat()
#             BlacklistedToken.objects.get_or_create(token=refresh_res['token'],
#                                                    user=refresh_res['user'],
#                                                    expires_at=exp)
#             try:
#                 InOutLog.objects.create(user=request.user, act_type='logout')
#             except Exception:
#                 raise RuntimeError('logout log write failed.')
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except RuntimeError:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#
#
