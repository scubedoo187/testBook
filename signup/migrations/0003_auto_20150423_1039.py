# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_signup_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='first_name',
            field=models.CharField(default=datetime.datetime(2015, 4, 23, 1, 39, 14, 106403, tzinfo=utc), max_length=120, blank=True),
            preserve_default=False,
        ),
    ]
