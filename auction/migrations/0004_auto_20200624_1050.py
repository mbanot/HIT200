# Generated by Django 3.0.5 on 2020-06-24 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_auto_20200624_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='amount',
            field=models.IntegerField(verbose_name='bid amount'),
        ),
    ]
