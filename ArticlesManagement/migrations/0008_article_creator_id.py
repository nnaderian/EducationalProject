# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticlesManagement', '0007_auto_20160101_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='creator_id',
            field=models.IntegerField(default=0),
        ),
    ]
