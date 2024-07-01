from django.contrib.auth.models import AbstractUser
from django.db import models

# class User(models.Model):
#     username = models.CharField(unique=True, max_length=20)
#     password = models.CharField(max_length=20)

class CustomUser(AbstractUser):
    pass

class Pangolin(models.Model):
    pangolin = models.CharField(max_length=20, unique=True)

class Location(models.Model):
    location = models.CharField(max_length=20, unique=True)

class Division(models.Model):
    division = models.CharField(max_length=20, unique=True)


class GISAID(models.Model):
    ei = models.CharField(max_length=20, unique=True)
    division = models.ForeignKey(to="Division", to_field="division", null=True, blank=True, on_delete=models.SET_NULL)
    location = models.ForeignKey(to="Location", to_field="location", null=True, blank=True, on_delete=models.SET_NULL)
    pangolin = models.ForeignKey(to="Pangolin", to_field="pangolin", null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField()


