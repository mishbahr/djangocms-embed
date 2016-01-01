# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging

from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from embedly import Embedly
from jsonfield import JSONField

from .conf import settings


logger = logging.getLogger('djangocms_embed')


@python_2_unicode_compatible
class Embed(CMSPlugin):
    url = models.URLField(_('URL'), help_text=_('Paste a URL to create an Embed'))
    plugin_template = models.CharField(
        _('Template'), max_length=255,
        choices=settings.DJANGOCMS_EMBED_TEMPLATES,
        default=settings.DJANGOCMS_EMBED_TEMPLATES[0][0],
    )
    data = JSONField(verbose_name=_('Data'), blank=True, null=True)

    def __str__(self):
        return self.url

    def clean(self):
        # http://embed.ly/docs/api/extract/endpoints/1/extract#error-codes
        self.data = {}
        if settings.EMBEDLY_OEMBED_API_KEY is None:
            msg = _('EMBEDLY_OEMBED_API_KEY is not defined in the project settings.')
            logger.error(msg)
            raise ImproperlyConfigured(msg)

        client = Embedly(settings.EMBEDLY_OEMBED_API_KEY)

        try:
            data = client.extract(self.url)
        except ValueError, e:
            raise ValidationError(str(e))

        error_msgs = {
            400: _('Invalid URL format.'),
            401: _('URL is private or restricted.'),
            404: _('URL Not Found.'),
            500: _('Embedly is having trouble with this url. Please try again.'),
            503: _('Embedly API service is down. Please try again later.')
        }
        error = data.get('error', False)
        if error:
            msg = _('Something unexpected has happened. '
                    'We\'re having trouble with this url. Please try gain later.')

            error_code = data.get('error_code', None)
            if error_code and 500 <= error_code <= 599:  # server error
                msg = _('Embedly API Error - Code: {error_code}').format(
                    error_code=error_code)
                logger.error(msg)
            raise ValidationError(error_msgs.get(error_code, msg))

        self.data = data

    def get_title(self):
        return self.data.get('title', '')

    def get_description(self):
        return self.data.get('description', '')

    def get_provider(self):
        return self.data.get('provider_name', '')

    def get_type(self):
        return self.data.get('type', '')
