from django.db import models

# Create your models here.
class images(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='upload')
    upload_by = models.CharField(max_length=50)