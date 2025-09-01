from django.urls import path
from .views import register_user, update_user

urlpatterns = [
    path('/register', register_user, name="register"),
    path('/update_user', update_user, name="update_user"),
]
