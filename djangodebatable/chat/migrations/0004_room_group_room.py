# Generated by Django 3.2.5 on 2021-08-13 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_room_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='group_room',
            field=models.BooleanField(default=False),
        ),
    ]