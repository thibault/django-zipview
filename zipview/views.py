# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic import View
from django.http import HttpResponse


class BaseZipView(View):
    """A base view to zip and stream several files."""

    http_method_names = ['get']
    zipfile_name = 'download.zip'

    def get_files(self):
        raise NotImplementedError()

    def get(self, request, *args, **kwargs):
        response = HttpResponse('', content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=%s' % self.zipfile_name
        response['Content-Length'] = 0
        return response
