# Generated by Django 3.1.5 on 2021-03-16 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Megan', '0014_auto_20210316_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newdataset',
            name='sentiment',
            field=models.IntegerField(default=9),
        ),
    ]
