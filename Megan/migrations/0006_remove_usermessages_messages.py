# Generated by Django 3.1.5 on 2021-02-26 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Megan', '0005_auto_20210226_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermessages',
            name='messages',
        ),
    ]
