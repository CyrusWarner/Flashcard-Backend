from django.db import models


class CollectionOfFlashCards(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True, default='')
