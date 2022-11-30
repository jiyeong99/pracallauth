from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    role = models.BooleanField(default=False)
    nickname = models.CharField(max_length=20)
