# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticlesManagement', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_date',
            field=models.DateTimeField(default=None),
        ),
    ]
