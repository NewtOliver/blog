from django.db import models

# Create your models here.


class Account(models.Model):
    name = models.CharField(default='username', max_length=20)
    email = models.CharField(default='email', max_length=20)
    password = models.CharField(default='password', max_length=20)
    date = models.DateField()

    def __str__(self):
        return self.name