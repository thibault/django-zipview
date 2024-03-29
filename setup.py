import os
from setuptools import setup

from zipview import __version__


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-zipview',
    version=__version__,
    packages=['zipview'],
    include_package_data=True,
    license='MIT License',  # example license
    description='A simple Django base view to zip and stream several files.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/thibault/django-zipview/',
    author='Thibault Jouannic',
    author_email='thibault@miximum.fr',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
