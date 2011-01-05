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

Prerequisitements
=================

You need to know basics of working with UNIX command line.

You need to have installed

* `Google App Engine SDK for Python <http://code.google.com/appengine/downloads.html#Download_the_Google_App_Engine_SDK>`_ 

* git command

* hg command (Mercurial tools)

* Python, at least 2.5

Your OS Python setuptools or Distribute package which is used to automatically download and install packages from PyPi repository,
must be new enough version or you get funny error messages.

Usage
=====

Clone this project from Github according to Github instructions.

Run bootstrap.py to generate ``bin/buildout`` command::

        python bootstrap.py 

Then make buildout to do the all the hard work of downloading and setting up configuration files for you::
        bin/buildout

.. note::

        You need to re-run buildout command if you change ``settings.py``. This is because
        by default ``settings.py`` is copied to generated directory under ``parts/``.

Before running App Engine version of Django, make sure Google App Engine is included in your shell environment command PATH.
This step is *only needed if you have Google App Engine SDK in non-standard location*::

        export PATH=~/google_appengine:$PATH

Now you can run django-admin wrapper which is configured to used Python package setup as described in ``buildout.cfg``::

        bin/django --version

                1.3 alpha 1

You also see that Google App Engine specific commands in the management::

        bin/django --help

                Usage: django subcommand [options] [args]

                Options:
                  -v VERBOSITY, --verbosity=VERBOSITY
                                        Verbosity level; 0=minimal output, 1=normal output,

                ...

                Available subcommands:
                  changepassword
                  cleanup
                  compilemessages
                  ...
                  remote

The buildout ships with a sample project skeleton called ``my.sampleproject``. You can clone this
skeleton and modify it to start building your won application.

To deploy your own application you can create a ``buildout.cfg`` which extends this existing buildout.
Edit ``buildout.cfg``.

Notes
=====

Currently uses patched ``djangoappengine`` and ``djc.recipe`` packages. Patches pushed upstream / merge requests created.

Further reading
===============

* http://www.allbuttonspressed.com/projects/djangoappengine

* http://pypi.python.org/pypi/djc.recipe

* http://pypi.python.org/pypi/mr.developer

