# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='header_bg',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
    ]
