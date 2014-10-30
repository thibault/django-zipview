# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic import View


class ZipView(View):
    """A base view to zip and stream several files."""

    http_method_names = ['get']

    def get_files(self):
        raise NotImplementedError()

    def get(self, request, *args, **kwargs):
        pass
