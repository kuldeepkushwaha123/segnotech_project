from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return self.title
