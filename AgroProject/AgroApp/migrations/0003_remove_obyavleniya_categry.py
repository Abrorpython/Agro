# Generated by Django 3.1.7 on 2021-03-11 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AgroApp', '0002_news_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obyavleniya',
            name='categry',
        ),
    ]
