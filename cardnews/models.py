from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title