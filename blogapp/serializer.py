from rest_framework import serializers
from django.contrib.auth import get_user_model
from blogapp.models import Blog

    
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "first_name", "last_name"]
    
class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ["slug", "title", "content", "author", "featured_image", "category"]
        # make slug read only
        extra_kwargs = {
            "slug": {
                "read_only": True
            }
        }

class UpdateBlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ["slug", "title", "content", "author", "featured_image", "category"]
        # make slug read only
        extra_kwargs = {
            "title": {
                "read_only": True
            },
            "slug": {
                "read_only": True
            },
            "author": {
                "read_only": True
            
            }
        }