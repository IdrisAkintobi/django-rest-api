from django.urls import path
from .views import list_blogs, create_blog

urlpatterns = [
    path('/create_blog', create_blog, name="create_blog"),
    path('/list_blogs', list_blogs, name="list_blogs"),
]
