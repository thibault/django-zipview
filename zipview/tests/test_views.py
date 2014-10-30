# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os

from django.test import TestCase
from django.core.files import File
from django.http import HttpResponse
from django.test.client import RequestFactory

from zipview.views import BaseZipView


class ZipView(BaseZipView):
    """Test ZipView basic implementation."""
    _files = None

    def get_files(self):
        if self._files is None:
            basename = os.path.basename(__file__)
            self._files = [
                File(open(os.path.join(basename, 'test_file.txt'))),
                File(open(os.path.join(basename, 'test_file.odt'))),
            ]
        return self._files


class ZipViewTests(TestCase):
    def setUp(self):
        self.view = ZipView()
        self.request = RequestFactory()

    def test_response_type(self):
        response = self.view.get(self.request)
        self.assertTrue(isinstance(response, HttpResponse))

    def test_response_params(self):
        response = self.view.get(self.request)
        self.assertEqual(response['Content-Type'], 'application/zip')
        self.assertEqual(response['Content-Disposition'], 'attachment; filename=download.zip')
