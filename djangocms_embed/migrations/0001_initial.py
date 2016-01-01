# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
from jsonfield import JSONField

from djangocms_embed.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Embed',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(
                    parent_link=True, auto_created=True, primary_key=True,
                    serialize=False, to='cms.CMSPlugin')),
                ('url', models.URLField(
                    verbose_name='URL', help_text='Paste a URL to create an Embed')),
                ('plugin_template', models.CharField(
                    max_length=255, verbose_name='Template',
                    default=settings.DJANGOCMS_EMBED_TEMPLATES[0][0],
                    choices=settings.DJANGOCMS_EMBED_TEMPLATES)),
                ('data', JSONField(null=True, verbose_name='Data', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
