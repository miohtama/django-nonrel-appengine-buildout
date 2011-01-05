==============================================
 django-nonrel and Google App Engine buildout
==============================================

.. contents ::

Introduction
============

Easily install and manage django-nonrel based Google App Engine applications using buildout command.

The buildout configuration uses Mr. Developer extension to pull all ``django-nonrel``
and ``djangoappengine`` bits together and set-up them for you.

This buildout is supported only on UNIX based systems. 

Usage
=====

You must use App Engine compatible Python version (Python 2.5 and Python 2.6 should be fine)::

        python bootstrap.py 

Then::
        bin/buildout

.. note::

        You need to re-run buildout command if you change ``settings.py``. This is because
        by default ``settings.py`` is copied to generated directory under ``parts/``.

Before running App Engine version of Django, make sure Google App Engine is included in your shell environment command PATH.
This step is *only needed if you have Google App Engine SDK in non-standard location*::

        export PATH=~/google_appengine:$PATH

Now you can run django-admin wrapper which is configured to used Python package setup as described in ``buildout.cfg``::

        bin/django --version

                1.2.4

The buildout ships with a sample project skeleton called ``my.sampleproject``. You can clone this
skeleton and modify it to start building your won application.

To deploy your own application you can create a ``buildout.cfg`` which extends this existing buildout.
Edit ``buildout.cfg``.



