from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.




class Question(models.Model):
    question_text = models.CharField(max_length=200)
    slug = models.SlugField(null=True,unique=True)
    pub_date = models.DateTimeField("date published")

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.question_text)
        return super().save(*args, **kwargs)

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


    def __str__(self):
        return self.question_text


    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text