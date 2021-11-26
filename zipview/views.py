import zipfile

from django.views.generic import View
from django.http import HttpResponse
from django.core.files.base import ContentFile


class BaseZipView(View):
    """A base view to zip and stream several files."""

    http_method_names = ['get']
    zipfile_name = 'download.zip'

    def get_files(self):
        """Must return a list of django's `File` objects."""
        raise NotImplementedError()

    def get_archive_name(self, request):
        return self.zipfile_name

    def build_zip(self, request):
        temp_file = ContentFile(b"", name=self.zipfile_name)
        with zipfile.ZipFile(temp_file, mode='w', compression=zipfile.ZIP_DEFLATED) as zip_file:
            files = self.get_files()
            for file_ in files:
                path = file_.name
                zip_file.writestr(path, file_.read())

        temp_file.seek(0)
        return temp_file

    def get(self, request, *args, **kwargs):
        temp_file = self.build_zip(request)
        file_size = temp_file.tell()

        response = HttpResponse(temp_file, content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=%s' % self.get_archive_name(request)
        response['Content-Length'] = file_size
        return response
