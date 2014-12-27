# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20141224_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('streamable_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Streamable')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
            bases=('pages.streamable',),
        ),
        migrations.CreateModel(
            name='AlbumImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(upload_to=b'')),
                ('album', models.ForeignKey(to='pictures.Album')),
            ],
            options={
                'verbose_name': 'AlbumImage',
                'verbose_name_plural': 'AlbumImages',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AlbumInformation',
            fields=[
                ('translatable_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Translatable')),
                ('title', models.TextField()),
                ('subtitle', models.TextField()),
                ('album', models.ForeignKey(to='pictures.Album')),
            ],
            options={
            },
            bases=('pages.translatable',),
        ),
        migrations.AddField(
            model_name='album',
            name='thumbnail',
            field=models.ForeignKey(related_name='thumbnail', to='pictures.AlbumImage'),
            preserve_default=True,
        ),
    ]
