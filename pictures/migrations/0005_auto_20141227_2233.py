# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_thumbs.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0004_auto_20141227_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albumimage',
            name='thumb',
        ),
        migrations.AlterField(
            model_name='albumimage',
            name='image',
            field=django_thumbs.db.models.ImageWithThumbsField(upload_to=b''),
            preserve_default=True,
        ),
    ]
