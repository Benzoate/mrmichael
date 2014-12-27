# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0002_auto_20141227_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='type',
            field=models.CharField(default=b'NORMAL', max_length=6, choices=[(b'NORMAL', b'Normal Album'), (b'PAGE', b'Page images'), (b'HEAD', b'Page headers')]),
            preserve_default=True,
        ),
    ]
