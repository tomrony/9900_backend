from django.db import models

# class User(models.Model):
#     username = models.CharField(unique=True, max_length=20)
#     password = models.CharField(max_length=20)

class Variant(models.Model):
    label = models.CharField(max_length=20, unique=True)

class City(models.Model):
    city = models.CharField(max_length=20, unique=True)

class Province(models.Model):
    province = models.CharField(max_length=20, unique=True)


class GISAID(models.Model):
    variant = models.ForeignKey(to="Variant", to_field="label", null=True, blank=True, on_delete=models.SET_NULL)
    city = models.ForeignKey(to="City", to_field="city", null=True, blank=True, on_delete=models.SET_NULL)
    province = models.ForeignKey(to="Province", to_field="province", null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField()


