# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demetadataapp', '0002_auto_20160427_0818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coverage',
            name='geotable',
        ),
        migrations.AlterField(
            model_name='sourcedatainventory',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
