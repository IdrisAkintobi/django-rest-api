from rest_framework import serializers
from django.contrib.auth import get_user_model
from blogapp.models import Blog

    
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "first_name", "last_name"]
    
class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ["id", "title", "content", "author", "featured_image", "category"]