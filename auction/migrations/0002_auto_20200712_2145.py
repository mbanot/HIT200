# Generated by Django 3.0.5 on 2020-07-12 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='auction_length',
            field=models.DurationField(),
        ),
    ]
