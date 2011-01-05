from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='my.sampleproject',
      version=version,
      description="Sample django-nonrel Google Appengine app as Python egg",
      long_description="",
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='mFabrik Research Oy',
      author_email='info@mfabrik.com',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=["my"], 
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
