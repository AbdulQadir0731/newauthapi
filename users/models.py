# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.email


class Client(models.Model):
    user = models.OneToOneField(CustomUser , on_delete = models.CASCADE , related_name = 'client')
    name = models.CharField(blank= True  , max_length=500)
    avatar = models.CharField(max_length=500)
    address = models.CharField(blank= True , max_length=255)
    def __str__(self):
        return self.user.get_full_name()


class Agent(models.Model):
    user = models.OneToOneField(CustomUser , on_delete = models.CASCADE , related_name = 'agent')
    name = models.CharField(blank= True  , max_length=500)
    avatar = models.CharField(blank= True  , max_length=500)
    mls_id = models.IntegerField(default=0)
    address = models.CharField(blank= True , max_length=255)
    def __str__(self):
        return self.user.get_full_name()
