# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='thumbnail',
            field=models.ForeignKey(related_name='thumbnail', blank=True, to='pictures.AlbumImage', null=True),
            preserve_default=True,
        ),
    ]
