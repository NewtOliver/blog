# Generated by Django 2.0.2 on 2019-01-22 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='describe',
            field=models.TextField(default='describe'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='title',
            field=models.CharField(default='title', max_length=50),
        ),
    ]
