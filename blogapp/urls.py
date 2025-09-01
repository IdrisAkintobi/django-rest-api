from django.urls import path
from .views import delete_blog, list_blogs, create_blog, update_blog

urlpatterns = [
    path('/create_blog', create_blog, name="create_blog"),
    path('/list_blogs', list_blogs, name="list_blogs"),
    path('/update_blog/<slug:slug>', update_blog, name="update_blog"),
    path('/delete_blog/<slug:slug>', delete_blog, name="delete_blog"),
]
