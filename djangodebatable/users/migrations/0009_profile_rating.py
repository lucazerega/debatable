# Generated by Django 3.2.5 on 2021-07-17 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210715_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rating',
            field=models.SmallIntegerField(default=-1),
        ),
    ]