# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('number', models.CharField(max_length=50)),
                ('date_request', models.DateTimeField()),
                ('request_type', models.IntegerField()),
                ('response', models.CharField(max_length=2)),
                ('code', models.IntegerField()),
                ('date_received', models.DateTimeField()),
                ('date_sent', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Request',
                'verbose_name_plural': 'Requests',
            },
        ),
    ]
