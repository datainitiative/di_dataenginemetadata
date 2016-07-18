# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'dataset_contributor',
            },
        ),
        migrations.CreateModel(
            name='Coverage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'inventory_coverage',
            },
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nid', models.IntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=500)),
                ('large_dataset', models.IntegerField(default=0, choices=[(1, b'Yes'), (0, b'No')])),
                ('update_date', models.DateField(auto_now=True)),
                ('contributor', models.ForeignKey(to='demetadataapp.Contributor')),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'dataset',
            },
        ),
        migrations.CreateModel(
            name='DatasetMetadata',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('metadata', models.TextField(verbose_name=b'Original Dataset Metadata in JSON')),
            ],
            options={
                'db_table': 'dataset_metadata',
            },
        ),
        migrations.CreateModel(
            name='DataTable',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('db_table', models.TextField(verbose_name=b'Database Table')),
                ('table_name', models.TextField(null=True, verbose_name=b'Table Name')),
            ],
            options={
                'db_table': 'data_tables',
            },
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('extension', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'inventory_format',
            },
        ),
        migrations.CreateModel(
            name='Geography',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'inventory_geography',
            },
        ),
        migrations.CreateModel(
            name='MacroDomain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'inventory_macrodomain',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'inventory_source',
            },
        ),
        migrations.CreateModel(
            name='SourceDataInventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_name', models.CharField(max_length=200, null=True, verbose_name=b'File Name')),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('year', models.IntegerField(null=True, verbose_name=b'Year', choices=[(None, b'---------'), (0, b'No Data'), (1980, b'1980'), (1981, b'1981'), (1982, b'1982'), (1983, b'1983'), (1984, b'1984'), (1985, b'1985'), (1986, b'1986'), (1987, b'1987'), (1988, b'1988'), (1989, b'1989'), (1990, b'1990'), (1991, b'1991'), (1992, b'1992'), (1993, b'1993'), (1994, b'1994'), (1995, b'1995'), (1996, b'1996'), (1997, b'1997'), (1998, b'1998'), (1999, b'1999'), (2000, b'2000'), (2001, b'2001'), (2002, b'2002'), (2003, b'2003'), (2004, b'2004'), (2005, b'2005'), (2006, b'2006'), (2007, b'2007'), (2008, b'2008'), (2009, b'2009'), (2010, b'2010'), (2011, b'2011'), (2012, b'2012'), (2013, b'2013'), (2014, b'2014'), (2015, b'2015')])),
                ('source_website', models.URLField(max_length=5000, null=True, blank=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('file_size', models.FloatField(default=0, null=True, verbose_name=b'File Size', blank=True)),
                ('description', models.CharField(max_length=500, null=True, blank=True)),
                ('data_consideration', models.CharField(max_length=500, null=True, blank=True)),
                ('process_notes', models.CharField(max_length=5000, null=True, blank=True)),
                ('coverage', models.ForeignKey(verbose_name=b'Geography', to='demetadataapp.Coverage', null=True)),
                ('format', models.ForeignKey(blank=True, to='demetadataapp.Format', null=True)),
                ('geography', models.ForeignKey(verbose_name=b'Geographic Level', to='demetadataapp.Geography', null=True)),
            ],
            options={
                'ordering': ['title'],
                'db_table': 'source_data_inventory',
            },
        ),
        migrations.CreateModel(
            name='SpatialTable',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'spatial_table',
            },
        ),
        migrations.CreateModel(
            name='SubjectMatter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('macrodomain', models.ForeignKey(to='demetadataapp.MacroDomain')),
            ],
            options={
                'ordering': ['macrodomain', 'name'],
                'db_table': 'inventory_subjectmatter',
            },
        ),
        migrations.CreateModel(
            name='TableMetadata',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('metadata', models.TextField(verbose_name=b'Original Table Metadata in JSON')),
            ],
            options={
                'db_table': 'table_metadata',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'dataset_tag',
            },
        ),
        migrations.CreateModel(
            name='VisualizationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'visualization_type',
            },
        ),
        migrations.AddField(
            model_name='sourcedatainventory',
            name='geometry',
            field=models.ForeignKey(verbose_name=b'Spatial Table', to='demetadataapp.SpatialTable', null=True),
        ),
        migrations.AddField(
            model_name='sourcedatainventory',
            name='macro_domain',
            field=models.ForeignKey(verbose_name=b'Domain', to='demetadataapp.MacroDomain', null=True),
        ),
        migrations.AddField(
            model_name='sourcedatainventory',
            name='metadata',
            field=models.ForeignKey(blank=True, to='demetadataapp.TableMetadata', null=True),
        ),
        migrations.AddField(
            model_name='sourcedatainventory',
            name='source',
            field=models.ForeignKey(to='demetadataapp.Source', null=True),
        ),
        migrations.AddField(
            model_name='sourcedatainventory',
            name='subject_matter',
            field=models.ForeignKey(verbose_name=b'Subdomain', to='demetadataapp.SubjectMatter', null=True),
        ),
        migrations.AddField(
            model_name='dataset',
            name='metadata',
            field=models.ForeignKey(blank=True, to='demetadataapp.DatasetMetadata', null=True),
        ),
        migrations.AddField(
            model_name='dataset',
            name='tables',
            field=models.ManyToManyField(to='demetadataapp.SourceDataInventory'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='tags',
            field=models.ManyToManyField(to='demetadataapp.Tag'),
        ),
        migrations.AddField(
            model_name='coverage',
            name='geotable',
            field=models.ForeignKey(verbose_name=b'Spatial Table', to='demetadataapp.SpatialTable'),
        ),
    ]
