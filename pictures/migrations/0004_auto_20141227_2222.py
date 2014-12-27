# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0003_album_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumimage',
            name='thumb',
            field=models.ImageField(null=True, upload_to=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='albumimage',
            name='image',
            field=models.ImageField(upload_to=b''),
            preserve_default=True,
        ),
    ]
