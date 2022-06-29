from django.db import models


# Create your models here.
class BlizzardToken(models.Model):
    access_token = models.CharField(max_length=150)
    token_type = models.CharField(max_length=150)
    expires_in = models.IntegerField()

