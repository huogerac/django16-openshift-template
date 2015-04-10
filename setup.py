from setuptools import setup

# Put here main required packages
# additional packages, see /wsgi/requirements/base.pip
packages = ['Django==1.6.6', ]

setup(name='myproject',
      version='1.0',
      description='OpenShift App',
      author='Roger Camargo',
      author_email='huogeac@gmail.com',
      url='https://pypi.python.org/pypi',
      install_requires=packages,
      )
