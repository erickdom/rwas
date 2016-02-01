# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0003_last_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Last_Whatsapp_Id',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('whatsapp_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='last_id',
        ),
    ]
