# -*- coding: utf-8 -*-

from django.conf import settings  # noqa
from django.utils.translation import ugettext_lazy as _

from appconf import AppConf


class DjangoCMSEmbedConf(AppConf):
    PLUGIN_MODULE = _('Generic')
    PLUGIN_NAME = _('Embedly Embed')
    TEMPLATES = (
        ('djangocms_embed/default.html', _('Default')),
    )

    API_KEY = None

    class Meta:
        prefix = 'djangocms_embed'
