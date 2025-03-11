from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field  # Asegúrate de que solo uses este import

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = CKEditor5Field(config_name='default')  # Añadido config_name
    image = models.ImageField(upload_to='blog_images/')
    date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Image for {self.post.title}"

