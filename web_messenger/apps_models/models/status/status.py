from django.db import models

class Status(models.Model):
    title = models.CharField()
    color = models.CharField()