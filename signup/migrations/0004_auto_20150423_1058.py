# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_auto_20150423_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contents', models.TextField(max_length=1000)),
                ('imgup', models.ImageField(height_field=600, width_field=800, upload_to=b'')),
                ('like', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='signup',
            name='first_name',
            field=models.CharField(max_length=120),
        ),
        migrations.AddField(
            model_name='posting',
            name='publisher',
            field=models.ForeignKey(to='signup.SignUp'),
        ),
    ]
