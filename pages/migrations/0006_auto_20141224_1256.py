# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_streamable__my_subclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamable',
            name='_my_subclass',
            field=models.CharField(max_length=200, editable=False),
            preserve_default=True,
        ),
    ]
