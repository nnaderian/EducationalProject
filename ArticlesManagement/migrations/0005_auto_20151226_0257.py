# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticlesManagement', '0004_auto_20151226_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.CharField(default=b'RA', max_length=2, choices=[(b'RA', b'\xd8\xb9\xd9\x84\xd9\x85\xdb\x8c \xd9\xbe\xda\x98\xd9\x88\xd9\x87\xd8\xb4\xdb\x8c'), (b'AN', b'\xd8\xaa\xd8\xad\xd9\x84\xdb\x8c\xd9\x84\xdb\x8c'), (b'OT', b'\xd8\xb3\xd8\xa7\xdb\x8c\xd8\xb1')]),
        ),
    ]
