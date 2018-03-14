from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=100)
    tag_number = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)