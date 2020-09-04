from django.db import models

# Create your models here.
class MyURL(models.Model):
    former_url = models.CharField(max_length=255)
    new_url = models.CharField(max_length=1000)