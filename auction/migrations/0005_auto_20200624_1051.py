# Generated by Django 3.0.5 on 2020-06-24 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_auto_20200624_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='reserve_price',
            field=models.IntegerField(default=1, verbose_name='reserve price'),
        ),
    ]
