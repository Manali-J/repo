# Generated by Django 2.1.3 on 2018-11-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IMOS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lob', models.CharField(max_length=30)),
                ('seal_id', models.IntegerField()),
                ('application_name', models.CharField(max_length=100)),
                ('environment', models.CharField(max_length=100)),
                ('details', models.TextField()),
            ],
        ),
    ]
