from django.urls import path
from .views import delete_user, register_user, update_user

urlpatterns = [
    path('/register', register_user, name="register"),
    path('/update_user', update_user, name="update_user"),
    path('/delete_user', delete_user, name="delete_user"),
]
