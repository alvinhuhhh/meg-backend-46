# Generated by Django 3.1.5 on 2021-03-16 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Megan', '0012_auto_20210227_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewDataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='user', max_length=50)),
                ('sentence', models.TextField(default='')),
                ('sentiment', models.IntegerField()),
            ],
        ),
    ]