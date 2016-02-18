Django ZipView
==============

[![Build Status](https://travis-ci.org/thibault/django-zipview.svg?branch=master)](https://travis-ci.org/thibault/django-zipview)

A base view to zip and stream several files.

Installation
------------

    pip install django-zipview

Usage and examples
------------------

To create a zip download view:

 * Extend BaseZipView
 * implement `get_files`
 * That's it

The `get_files` method must return a list of Django's File objects.

Example:

```python
from zipview.views import BaseZipView

from emails import Email


class AttachmentsArchiveView(BaseZipView):
    """Download at once all comments for a review."""

    def get_files(self):
        emails = Email.objects \
            .filter(user=self.request.user) \
            .exclude(attachment__isnull=True)

        return [email.attachment.file for email in emails if email.attachment.name]
```

View configuration
------------------

By default, the downloaded file is named `download.zip` you can set a custom name
by setting the `zipfile_name` parameter.

```python

class ZipView(BaseZipView):
    zipfile_name = 'toto.zip'
```

In case you need to dynamically set the filename, you can override the
`get_archive_name` method. It takes the request as a parameter.

```python

def get_archive_name(self, request):
    import datetime
    today = datetime.date.today()
    return 'archive_{:%Y%m%d}.zip'.format(today)
```

Compatibility
-------------

Current supported django versions are 1.8 & 1.9.

Testing
-------

Django ZipView uses [tox, the testing automation
tool](https://tox.readthedocs.org/en/latest/), to run tests.

To launch tests:

    pip install -r requiments/test.txt
    tox


Author
------

Crafted with love by [Thibault Jouannic](http://www.miximum.fr). You can
contact him for [Python / Django freelancing
gigs](http://www.miximum.fr/a-propos/).
