from django.db import models


class Dataset(models.Model):
    class Gender (models.IntegerChoices):
        FEMALE = (1, "Female")
        MALE = (2, "MALE")
        UNKNOWN = (3, "UNKNOWN")

    category = models.CharField(max_length=30, blank=True, null=True)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    gender = models.IntegerField(choices=Gender.choices, blank=True, null=True)
    birthDate = models.DateField(blank=True, null=True, default=None)