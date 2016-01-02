# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticlesManagement', '0006_auto_20160101_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='AuthorName',
            field=models.CharField(max_length=50, verbose_name=b'\xd9\x86\xd8\xa7\xd9\x85 \xd9\x86\xd9\x88\xdb\x8c\xd8\xb3\xd9\x86\xd8\xaf\xd9\x87'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publication_date',
            field=models.DateField(verbose_name=b'\xd8\xaa\xd8\xa7\xd8\xb1\xdb\x8c\xd8\xae \xd8\xa7\xd9\x86\xd8\xaa\xd8\xb4\xd8\xa7\xd8\xb1'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'\xd8\xb9\xd9\x86\xd9\x88\xd8\xa7\xd9\x86 \xd9\x85\xd9\x82\xd8\xa7\xd9\x84\xd9\x87'),
        ),
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.CharField(default=b'RA', max_length=2, verbose_name=b'\xd9\x86\xd9\x88\xd8\xb9 \xd9\x85\xd9\x82\xd8\xa7\xd9\x84\xd9\x87', choices=[(b'RA', b'\xd8\xb9\xd9\x84\xd9\x85\xdb\x8c \xd9\xbe\xda\x98\xd9\x88\xd9\x87\xd8\xb4\xdb\x8c'), (b'AN', b'\xd8\xaa\xd8\xad\xd9\x84\xdb\x8c\xd9\x84\xdb\x8c'), (b'OT', b'\xd8\xb3\xd8\xa7\xdb\x8c\xd8\xb1')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(verbose_name=b'\xd8\xaa\xd8\xa7\xd8\xb1\xdb\x8c\xd8\xad \xd8\xaa\xd9\x88\xd9\x84\xd8\xaf'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=10, verbose_name=b'\xd8\xb4\xd9\x85\xd8\xa7\xd8\xb1\xd9\x87 \xd8\xaa\xd9\x85\xd8\xa7\xd8\xb3'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(upload_to=b'profile_images', verbose_name=b'\xd8\xb9\xda\xa9\xd8\xb3 \xd8\xae\xd9\x88\xd8\xaf \xd8\xb1\xd8\xa7 \xd8\xa2\xd9\xbe\xd9\x84\xd9\x88\xd8\xaf \xda\xa9\xd9\x86\xdb\x8c\xd8\xaf'),
        ),
    ]
