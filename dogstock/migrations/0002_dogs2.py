# Generated by Django 2.2.2 on 2019-07-03 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogstock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dogs2',
            fields=[
                ('dogId', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('dogName', models.TextField()),
                ('dogBreed', models.TextField()),
                ('dogAge', models.TextField()),
                ('ownerId', models.TextField()),
            ],
        ),
    ]
