from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='images', null=True,
                              height_field='height_field',
                              width_field='width_field', blank=True)
    url = models.CharField(max_length=256, blank=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

