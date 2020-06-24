# Generated by Django 3.0.5 on 2020-06-24 09:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='bid_time',
            new_name='created',
        ),
        migrations.AddField(
            model_name='bid',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='bid',
            name='amount',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only numerics are allowed.')], verbose_name='bid amount'),
        ),
    ]