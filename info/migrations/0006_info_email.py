# Generated by Django 3.0.3 on 2020-02-18 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_auto_20200218_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]