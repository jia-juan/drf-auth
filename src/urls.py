"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# FIXME: AppRegistryNotReady: Apps aren't loaded yet.
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')
django.setup()

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from rbac.views import LoginView
from rbac.views import TokenRefreshView
from rbac.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    # jwt/rbac
    path('user/login/', LoginView.as_view()),
    path('user/token-refresh/', TokenRefreshView.as_view()),
    path('user/logout/', LogoutView.as_view()),
    path('api-token-verify/', verify_jwt_token),  # 驗證token是否有效

    # app0
    path('', include('app0.urls')),

    # rbac
    path('rbac/', include('rbac.urls')),

    # djoser
    # path('user/', include('djoser.urls')),
]

# static path
# urlpatterns += [static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)]

from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="2020ELK API",
      default_version='v1',
      description="systex B85B project",
      # terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="juansun@systex.com"),
      # license=openapi.License(name="BSD License"),
   ),
   # public=True,
   # patterns=[url(r"^api/", include((es_urls, 'api'), namespace='v1'))],
   permission_classes=(permissions.AllowAny, ),
)

urlpatterns += [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]