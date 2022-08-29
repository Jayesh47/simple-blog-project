# Create your models here.
from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    desc = models.TextField()
    timestamp = models.DateTimeField(blank=True)
    slug = models.CharField(max_length=150)

    def __str__(self):
        return self.title