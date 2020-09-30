from django.db import models
from user.models import Users


# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=300)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

