from django.db import models
from django.db.models.fields import CharField

class Hero(models.Model):
    name = models.CharField(max_length=60)
    aliasname = models.CharField(max_length=60)

    def __str__(self):
        return self.name