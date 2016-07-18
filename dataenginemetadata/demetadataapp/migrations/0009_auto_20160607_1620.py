# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demetadataapp', '0008_auto_20160607_1606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subjectmatter',
            options={'ordering': ['macro_domain', 'name']},
        ),
        migrations.RenameField(
            model_name='subjectmatter',
            old_name='macrodomain',
            new_name='macro_domain',
        ),
    ]
