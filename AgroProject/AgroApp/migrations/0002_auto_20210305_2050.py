# Generated by Django 3.1.7 on 2021-03-05 15:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AgroApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='UserTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='UserOferta',
            field=models.BooleanField(blank=True, choices=[('1', True), ('2', False)], max_length=50),
        ),
    ]