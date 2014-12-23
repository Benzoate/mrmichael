# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Streamable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_updated_date', models.DateTimeField()),
                ('published', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Streamable',
                'verbose_name_plural': 'Streamables',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('streamable_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Streamable')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
            bases=('pages.streamable',),
        ),
        migrations.CreateModel(
            name='Translatable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=7, choices=[(b'en', b'English'), (b'ja', b'Japanese')])),
            ],
            options={
                'verbose_name': 'Translatable',
                'verbose_name_plural': 'Translatables',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageText',
            fields=[
                ('translatable_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Translatable')),
                ('title', models.TextField()),
                ('text', models.TextField()),
                ('page', models.ForeignKey(to='pages.Page')),
            ],
            options={
                'verbose_name': 'PageText',
                'verbose_name_plural': 'PageTexts',
            },
            bases=('pages.translatable',),
        ),
    ]
