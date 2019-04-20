from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Blog(models.Model):
    title = models.CharField(default='title', max_length=50)
    tags = models.CharField(default='tag', max_length=120, null=True, blank=True)
    abstract = models.CharField(default='abstract', max_length=300, blank=True, null=True)
    content = RichTextField(default='content')
    image = models.ImageField(default='default.png', upload_to='blog_image/')
    date = models.DateTimeField()
    author = models.CharField(default='author', max_length=20)

    def short_content(self):
        return self.content[:50]+'....'

    def __str__(self):
        return self.title
