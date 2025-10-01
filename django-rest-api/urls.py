"""
URL configuration for django-rest-api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView

from .utils.custom_token_refresh_view import CustomTokenRefreshView
from .views import health_check

urlpatterns = [
    path('admin', admin.site.urls),
    path('api/auth', include('authapp.urls')),
    path('api/blog', include('blogapp.urls')),
    path('api/auth/login', TokenObtainPairView.as_view(), name='token'),
    path('api/auth/refresh_token', CustomTokenRefreshView.as_view(), name='refresh_token'),
    # Add root health check
    path('healthz', health_check, name='health_check'),
    path('', health_check, name='root_check'),
    # API Doc
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    path('swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
