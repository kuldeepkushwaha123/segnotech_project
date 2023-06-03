from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images',default='a.png')

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images',default='a.png')

    def __str__(self):
        return self.title


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images', default="a.png")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    tag = models.ManyToManyField(Tag,blank=True)
    slug = models.SlugField(null=True,blank=True,unique=True)
    text = models.TextField()
    author = models.CharField(max_length=15)
    timeStamp = models.DateTimeField(blank=True)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    


    def __str__(self):
        return self.title + ' by ' + self.author

class Blogcomment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username