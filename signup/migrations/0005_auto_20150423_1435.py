# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_auto_20150423_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='comment',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='posting',
            name='imgup',
            field=models.ImageField(height_field=600, width_field=800, upload_to=b'/home/jungyg/repo/testBook/static/media'),
        ),
    ]
