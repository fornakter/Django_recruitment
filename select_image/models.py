from django.db import models

class ImgFiles(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='')
