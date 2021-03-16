# Generated by Django 3.1.5 on 2021-03-16 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Megan', '0013_newdataset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newdataset',
            name='name',
        ),
        migrations.AddField(
            model_name='newdataset',
            name='_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='newdataset',
            name='sentiment',
            field=models.IntegerField(default=None),
        ),
    ]
