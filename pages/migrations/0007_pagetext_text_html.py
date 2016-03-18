# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20141224_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagetext',
            name='text_html',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
