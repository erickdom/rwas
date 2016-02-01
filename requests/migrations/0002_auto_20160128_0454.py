# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='code',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='date_received',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='date_sent',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='response',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
