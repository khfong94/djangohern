from __future__ import unicode_literals
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Hello
class Dog(models.Model):
	color = models.CharField(max_length=15)
	breed = models.CharField(max_length=20)
	weight = models.IntegerField()
	owner = models.ForeignKey(User, default=1)
