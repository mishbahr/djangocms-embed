# -*- coding: utf-8 -*-

from appconf import AppConf

from django.conf import settings  # noqa
from django.utils.translation import ugettext_lazy as _


class DjangoCMSEmbedConf(AppConf):
    PLUGIN_MODULE = _('Generic')
    PLUGIN_NAME = _('Embedly Embed')
    TEMPLATES = (
        ('djangocms_embed/default.html', _('Default')),
    )

    API_KEY = None

    class Meta:
        prefix = 'djangocms_embed'