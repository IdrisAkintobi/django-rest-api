import uuid
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.utils import timezone
    
class Blog(models.Model):
    CATEGORY = (
        ('Technology', 'Technology'),
        ('Health', 'Health'),
        ('Travel', 'Travel'),
        ('Food', 'Food'),
        ('Fashion', 'Fashion'),
        ('Sports', 'Sports'),
        ('Politics', 'Politics'),
        ('Business', 'Business'),
        ('Lifestyle', 'Lifestyle'),
        ('Other', 'Other'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=225, unique=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured_image = models.ImageField(upload_to='blog_images', null=True, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY, default='Other')
    published_at = models.DateTimeField(null=True)
    is_draft = models.BooleanField(default=False)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)
        num = 1
        slug = base_slug
        while Blog.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{num}"
            num += 1
        self.slug = slug
        
        if not self.is_draft and not self.published_at:
            self.published_at = timezone.now()

        super().save(*args, **kwargs)

