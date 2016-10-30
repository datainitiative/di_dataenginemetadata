# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('demetadataapp', '0007_auto_20160603_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourcedatainventory',
            name='subject_matter',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, to='demetadataapp.SubjectMatter', chained_model_field=b'macro_domain', chained_field=b'macro_domain', verbose_name=b'Subdomain'),
        ),
        migrations.AlterField(
            model_name='sourcedatainventory',
            name='year',
            field=models.IntegerField(null=True, verbose_name=b'Year', choices=[(None, b'---------'), (0, b'No Data'), (1980, b'1980'), (1981, b'1981'), (1982, b'1982'), (1983, b'1983'), (1984, b'1984'), (1985, b'1985'), (1986, b'1986'), (1987, b'1987'), (1988, b'1988'), (1989, b'1989'), (1990, b'1990'), (1991, b'1991'), (1992, b'1992'), (1993, b'1993'), (1994, b'1994'), (1995, b'1995'), (1996, b'1996'), (1997, b'1997'), (1998, b'1998'), (1999, b'1999'), (2000, b'2000'), (2001, b'2001'), (2002, b'2002'), (2003, b'2003'), (2004, b'2004'), (2005, b'2005'), (2006, b'2006'), (2007, b'2007'), (2008, b'2008'), (2009, b'2009'), (2010, b'2010'), (2011, b'2011'), (2012, b'2012'), (2013, b'2013'), (2014, b'2014'), (2015, b'2015'), (2016, b'2016')]),
        ),
    ]
