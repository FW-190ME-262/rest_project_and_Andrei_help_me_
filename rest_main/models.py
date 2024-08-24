from django.db import models


# Create your models here.

class Planes(models.Model):

    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    info = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name
