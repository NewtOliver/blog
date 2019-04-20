from django.db import models

# Create your models here.


class Picture(models.Model):
    image = models.ImageField(default='default.png', upload_to='picture_image/')
    title = models.CharField(default='title', max_length=50)
    description = models.CharField(default='description', max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.title
