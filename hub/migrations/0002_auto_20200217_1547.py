# Generated by Django 3.0.3 on 2020-02-17 14:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membershipinproject',
            name='time_allocated_by_member',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Temps allouee'),
        ),
    ]