from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager


class Contenuto(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    published = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)
    tags = TaggableManager()
    image = models.ImageField(upload_to='images/', default='')
    originale = models.FileField(upload_to='video/originale/', default='')
    video_480 = models.FileField(upload_to='video/mp4_480', blank=True, null=True)
    video_720 = models.FileField(upload_to='video/mp4_720',blank=True, null=True)

    def __str__(self):
        return self.title