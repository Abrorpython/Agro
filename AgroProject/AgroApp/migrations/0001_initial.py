# Generated by Django 3.1.7 on 2021-03-05 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserNameOne', models.CharField(choices=[('1', 'Jismoniy shaxs'), ('2', 'Yuridik shaxs')], max_length=50)),
                ('UserNameTwo', models.CharField(max_length=50)),
                ('UserEmail', models.EmailField(max_length=100)),
                ('UserPassword', models.CharField(max_length=100)),
                ('UserPhone', models.CharField(max_length=100)),
                ('UserOferta', models.CharField(blank=True, choices=[('1', 'True'), ('2', 'False')], max_length=50)),
            ],
        ),
    ]