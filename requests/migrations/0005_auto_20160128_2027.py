# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0004_auto_20160128_2024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='last_whatsapp_id',
            options={'verbose_name': 'LastID', 'verbose_name_plural': 'LastID'},
        ),
    ]
