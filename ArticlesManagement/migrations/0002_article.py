# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticlesManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('AuthorName', models.CharField(max_length=50)),
                ('publication_date', models.DateField()),
                ('type', models.CharField(default=b'RA', max_length=2, choices=[(b'RA', b'\xd8\xb9\xd9\x84\xd9\x85\xdb\x8c \xd9\xbe\xda\x98\xd9\x88\xd9\x87\xd8\xb4\xdb\x8c'), (b'AN', b'\xd8\xaa\xd8\xad\xd9\x84\xdb\x8c\xd9\x84\xdb\x8c'), (b'OT', b'\xd8\xb3\xd8\xa7\xdb\x8c\xd8\xb1')])),
            ],
        ),
    ]
