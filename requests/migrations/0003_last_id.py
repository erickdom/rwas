# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0002_auto_20160128_0454'),
    ]

    operations = [
        migrations.CreateModel(
            name='last_id',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_id_received', models.CharField(default=0, max_length=2)),
            ],
        ),
    ]
