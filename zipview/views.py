# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import zipfile
from io import BytesIO

from django.views.generic import View
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper


class BaseZipView(View):
    """A base view to zip and stream several files."""

    http_method_names = ['get']
    zipfile_name = 'download.zip'

    def get_files(self):
        """Must return a list of django's `File` objects."""
        raise NotImplementedError()

    def get(self, request, *args, **kwargs):
        temp_file = BytesIO()
        with zipfile.ZipFile(temp_file, mode='w', compression=zipfile.ZIP_DEFLATED) as zip_file:
            files = self.get_files()
            for file_ in files:
                path = file_.name
                name = os.path.basename(path)
                zip_file.write(path, name)

        file_size = temp_file.tell()
        temp_file.seek(0)
        wrapper = FileWrapper(temp_file)

        response = HttpResponse(wrapper, content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=%s' % self.zipfile_name
        response['Content-Length'] = file_size
        return response
