from django.db import models
# from datetime import datetime
import django.utils.timezone as datetime


# Create your models here.
class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True, unique=True)
    password = models.CharField(max_length=230, null=False)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
