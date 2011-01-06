==============================================
 django-nonrel and Google App Engine buildout
==============================================

.. contents ::

Introduction
============

Easily install and manage django-nonrel based Google App Engine applications using buildout command.

The `buildout <http://www.buildout.org>`_ configuration uses Mr. Developer extension to pull all ``django-nonrel``
and ``djangoappengine`` bits together and set-up them for you, so you can instantly start developing 
Google App Engine applications.

This buildout is supported only on UNIX based systems. 

Buildout uses ``buildout.cfg`` configuration file to describe how to set up a Python software project 

* Download required dependencies from `PyPi <http://pypi.python.org>`_ (Python egg packages)

* Checkout and manage source code from version control systems - public and your private repositores

* Create start up scripts and set environment variables

Buildout benefits include

* Repeatability: All project developers can start quickly (no more one day setting up dependencies)

* Repeatability: Easily move your project between different folders, computers or servers

* Standard: Part of advanced Python developer toolkit. Provides more reusability than ad hoc shell scripts.

Buildout works around some Google App Engine deployment problems. 

This buildout will check out a sample Google App Engine + django-nonrel application called ``my.sampleproject``.
To work with your own project, just make your Django application available 

Using ``django-nonrel`` over stock Google App Engine modules and templates provide additional benefits

* Maintained versions: Google App Engine stock Python modules are **old**

* Vendor independence: You can move your code to some other NoSQL or SQL database on one day 

* Reuse: You can plug-in existing Django applications and modules easily. With buildout, it is just
  including the package egg name in buildout.cfg file and the Django application will be downloaded for you automatically.

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

Installation
=============

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

>Now you can run django-admin wrapper which is configured to used Python package setup as described in ``buildout.cfg``::

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

Usage 
=====

Start Google App Engine service with a sample database::

        bin/django runserver

.. note ::

        Never run manage.py runserver together with other management commands at the same time. The changes won't take effect. 
        That's an App Engine SDK limitation which might get fixed in a later release.        

Extending
=========

Currently the suggested way to reuse is this buildout is just to make your own copy of it
and put in your own project to 

* eggs section - you need to package your Python source code as egg (see ``setup.py`` in ``my.sampleproject``)

* Alternative you need to put source code eggs to ``develop-eggs`` in ``[buildout]`` section or use
  ``[sources]`` section and `Mr. Developer <http://pypi.python.org/pypi/mr.developer>`_ to manage the checkout

... or as a dummy alternative, replace ``my.samplerproject`` everywhere with your own package name.


Notes
=====

When you run ``buildout`` its ``[flatten-eggs]`` recipe will create a flat, symlinked, directory
structure of available eggs. This makes the code deployable on Google App Engine, 
because App Engine does not support egg deployments. Later, this flattened folder is added
to ``PYTHONPATH`` in ``bootstrap.py`` of ``my.sampleproject``, making eggs importable. 
``flattened-eggs`` folder is  automatically cleared, so if you remove eggs, you do not need to purge the folder manually.

Currently uses patched ``djangoappengine`` and ``djc.recipe`` packages. Patches pushed upstream / merge requests created.

Author
======

* Contact mikko at mfabrik dot com

* `Follow in Twitter <http://twitter.com/moo9000>`_

Further reading
===============

* http://www.allbuttonspressed.com/projects/djangoappengine

* http://pypi.python.org/pypi/djc.recipe

* http://pypi.python.org/pypi/mr.developer

