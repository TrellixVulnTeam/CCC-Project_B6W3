# Generated by Django 2.1.1 on 2018-09-16 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180916_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
