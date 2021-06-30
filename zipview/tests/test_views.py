from __future__ import unicode_literals

import os
import zipfile
from io import BytesIO

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
            dirname = os.path.dirname(__file__)
            self._files = [
                File(
                    open(os.path.join(dirname, 'files', 'test_file.txt'), 'rb'),
                    name='files/test_file.txt',
                ),
                File(
                    open(os.path.join(dirname, 'files', 'test_file.odt'), 'rb'),
                    name='files/test_file.odt',
                ),
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

    def test_response_content_length(self):
        response = self.view.get(self.request)
        self.assertEqual(response['Content-Length'], '19819')

    def test_valid_zipfile(self):
        response = self.view.get(self.request)
        content = BytesIO(response.content)
        self.assertTrue(zipfile.is_zipfile(content))

        zip_file = zipfile.ZipFile(content)
        self.assertEqual(
            zip_file.namelist(),
            ['files/test_file.txt', 'files/test_file.odt'])

    def test_custom_archive_name(self):
        self.view.get_archive_name = lambda request: 'toto.zip'
        response = self.view.get(self.request)
        self.assertEqual(response['Content-Disposition'], 'attachment; filename=toto.zip')
