from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=128, null=False, default=None)
    description = models.CharField(max_length=256, null=True)
    # use null=True because there are tasks without user in the DB
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
