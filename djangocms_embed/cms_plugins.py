# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.template.loader import select_template

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .conf import settings
from .models import Embed


class EmbedPlugin(CMSPluginBase):
    model = Embed
    module = settings.DJANGOCMS_EMBED_PLUGIN_MODULE
    name = settings.DJANGOCMS_EMBED_PLUGIN_NAME

    fieldsets = (
        (None, {
            'fields': ('url', 'plugin_template')
        }),
    )

    def get_render_template(self, context, instance, placeholder):
        # returns the first template that exists, falling back to bundled template
        return select_template([
            instance.plugin_template,
            'djangocms_embed/default.html'
        ])

    def render(self, context, instance, placeholder):
        context = super(EmbedPlugin, self).render(context, instance, placeholder)
        context.update({
            'api_key': settings.DJANGOCMS_EMBED_API_KEY
        })
        return context

plugin_pool.register_plugin(EmbedPlugin)
