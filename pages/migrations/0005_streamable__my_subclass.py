# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20141223_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='streamable',
            name='_my_subclass',
            field=models.CharField(default='page', max_length=200),
            preserve_default=False,
        ),
    ]
