from django.db import models

# Create your models here.
class Sitesetting(models.Model):
    banner=models.ImageField(upload_to='media/site/')
    captions=models.TextField()