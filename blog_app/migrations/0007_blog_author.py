# Generated by Django 2.0.2 on 2019-01-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_auto_20190122_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default='author', max_length=20),
        ),
    ]