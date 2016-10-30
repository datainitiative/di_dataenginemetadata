# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demetadataapp', '0005_auto_20160602_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spatialtable',
            name='db_table_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='spatialtable',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
