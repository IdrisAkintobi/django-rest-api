from django.contrib import admin

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'is_draft')
    list_filter = ('category', 'is_draft')
    search_fields = ('title', 'content')


admin.site.register(Blog, BlogAdmin)
