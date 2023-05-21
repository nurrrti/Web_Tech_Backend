from django.db import models
from distutils.dep_util import newer_pairwise
from django.contrib.auth.models import AbstractUser
class Book(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    pages = models.IntegerField()
    description = models.TextField(max_length=20)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta2:
        verbose_name = 'Book'
