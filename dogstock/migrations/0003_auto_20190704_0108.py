# Generated by Django 2.2.2 on 2019-07-04 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogstock', '0002_dogs2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogs2',
            name='dogAge',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dogs2',
            name='dogBreed',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='dogs2',
            name='dogName',
            field=models.TextField(max_length=60),
        ),
        migrations.AlterField(
            model_name='dogs2',
            name='ownerId',
            field=models.TextField(max_length=100),
        ),
    ]
