# Generated by Django 4.0.2 on 2022-02-27 09:51

import django.core.validators
from django.db import migrations, models
import exam.web.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), exam.web.validators.validation_positive_float_price]),
        ),
    ]
