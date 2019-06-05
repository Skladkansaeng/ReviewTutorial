from django.conf import settings
from django.db import models


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=None)
    score = models.SmallIntegerField(default=0)
    review = models.CharField(max_length=255, default='')