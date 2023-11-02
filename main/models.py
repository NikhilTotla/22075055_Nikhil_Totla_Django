from django.db import models

class short_urls(models.Model):
    short_url = models.CharField(max_length=20)
    long_url = models.URLField()