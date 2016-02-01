# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0005_auto_20160128_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='description',
            field=models.TextField(default=datetime.datetime(2016, 1, 29, 18, 45, 57, 179597, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
