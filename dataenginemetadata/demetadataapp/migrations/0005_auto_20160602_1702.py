# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demetadataapp', '0004_auto_20160602_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spatialtable',
            name='db_table_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='spatialtable',
            name='name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
