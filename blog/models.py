from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    date = models.DateField(datetime.date.today)
    def __str__(self):
        return self.title

