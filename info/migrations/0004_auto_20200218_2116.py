# Generated by Django 3.0.3 on 2020-02-18 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_info_col_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='latitude',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='info',
            name='longitude',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
