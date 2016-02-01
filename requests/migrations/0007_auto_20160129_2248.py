# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0006_request_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
