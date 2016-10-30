# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demetadataapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('db_table', models.CharField(max_length=100)),
                ('file_path', models.CharField(max_length=200, null=True)),
                ('has_metadata', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['db_table'],
                'db_table': 'table_upload',
            },
        ),
        migrations.DeleteModel(
            name='VisualizationType',
        ),
    ]
