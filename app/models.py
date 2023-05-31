from django.db import models
from django.utils import timezone
from . utils import generate_slug

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(auto_now=True)


    def save(self,*args,**kwargs):
        self.slug = generate_slug(self.title)

        super(Post , self).save(*args,**kwargs)
    


    def __str__(self):
        return self.title
