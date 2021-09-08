# Generated by Django 3.2.5 on 2021-07-20 02:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0012_auto_20210719_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='bot',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='report',
            name='discrimination',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='report',
            name='inappropriate',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='report',
            name='message',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='report',
            name='sexual',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),
                ('following', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]