Django ZipView
==============

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

from reviews import Review


class CommentsArchiveView(BaseZipView):
    """Download at once all comments for a review."""

    def get_files(self):
        document_key = self.kwargs.get('document_key')
        reviews = Review.objects \
            .filter(document__document_key=document_key) \
            .exclude(comments__isnull=True)

        return [review.comments.file for review in reviews if review.comments.name]
```

Testing
-------

Django ZipView uses [tox, the testing automation tool](https://tox.readthedocs.org/en/latest/),
to run tests.

To launch tests:

    pip install tox
    tox


Author
------

Crafted with love by [Thibault Jouannic](http://www.miximum.fr). You can
contact him for [Python / Django freelancing gigs](http://www.miximum.fr/a-propos/).
