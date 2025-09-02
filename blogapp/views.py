from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from blogapp.models import Blog
from blogapp.serializer import BlogSerializer, UpdateBlogSerializer


@extend_schema(request=BlogSerializer, responses=BlogSerializer)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_blog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(responses=BlogSerializer(many=True))
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_blogs(request):
    blogs = Blog.objects.filter(is_draft=False)
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


@extend_schema(responses=BlogSerializer)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)


@extend_schema(request=UpdateBlogSerializer, responses=BlogSerializer)
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    serializer = UpdateBlogSerializer(blog, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(responses={204: None})
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    blog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
