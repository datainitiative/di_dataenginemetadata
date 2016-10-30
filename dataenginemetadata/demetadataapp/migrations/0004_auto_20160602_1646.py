# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demetadataapp', '0003_auto_20160602_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='spatialtable',
            name='db_table_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='spatialtable',
            name='db_table_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
