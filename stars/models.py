from django.db import models


class Actor(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    picture = models.CharField(max_length=255)
    biography = models.TextField(default='')

    def __str__(self):
        return self.firstname + ' ' + self.lastname
