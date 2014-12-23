# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_page_header_bg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='header_bg',
            field=models.CharField(default=b'', max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.CharField(default=b'', max_length=20, blank=True),
            preserve_default=True,
        ),
    ]
