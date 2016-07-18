# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demetadataapp', '0006_auto_20160602_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sourcedatainventory',
            name='file_name',
        ),
        migrations.RemoveField(
            model_name='sourcedatainventory',
            name='file_size',
        ),
        migrations.RemoveField(
            model_name='sourcedatainventory',
            name='format',
        ),
    ]
