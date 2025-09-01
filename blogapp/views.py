from blogapp.models import Blog
from blogapp.serializer import BlogSerializer, UpdateBlogSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


# Create a blog
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_blog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List all blogs
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_blogs(request):
    blogs = Blog.objects.all().filter(is_draft=False)
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


# Get a single blog
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)

# Update a blog
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    serializer = UpdateBlogSerializer(blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Delete a blog
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    blog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)