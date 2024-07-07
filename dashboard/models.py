from django.contrib.auth.models import AbstractUser
from django.db import models

# class User(models.Model):
#     username = models.CharField(unique=True, max_length=20)
#     password = models.CharField(max_length=20)

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='customuser',
    )
class Pangolin(models.Model):
    pangolin = models.CharField(max_length=100, unique=True)

class Location(models.Model):
    location = models.CharField(max_length=100, unique=True)

class Division(models.Model):
    division = models.CharField(max_length=100, unique=True)


class GISAID(models.Model):
    ei = models.CharField(max_length=100, unique=True)
    division = models.ForeignKey(to="Division", to_field="division", null=True, blank=True, on_delete=models.SET_NULL)
    location = models.ForeignKey(to="Location", to_field="location", null=True, blank=True, on_delete=models.SET_NULL)
    pangolin = models.ForeignKey(to="Pangolin", to_field="pangolin", null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField()


