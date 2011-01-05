==============================================
 django-nonrel and Google App Engine buildout
==============================================

.. contents ::

Introduction
============

Easily install and manage django-nonrel based Google App Engine applications using buildout command.

The buildout configuration uses Mr. Developer extension to pull all ``django-nonrel``
and ``djangoappengine`` bits together and set-up them for you.

Usage
=====

You must use App Engine compatible Python version::

        python bootstrap.py 

Then::
        bin/buildout

Now you can run Django manage::

        bin/django --version

        1.2.4

The buildout ships with a sample project skeleton called ``my.sampleproject``. You can clone this
skeleton and modify it to start building your won application.

To deploy your own application you can create a ``buildout.cfg`` which extends this existing buildout.
Edit ``buildout.cfg``.



