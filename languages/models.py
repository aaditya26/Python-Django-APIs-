from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=20)
    paradigm = models.CharField(max_length=150)

    def __str__(self):
        return self.name
