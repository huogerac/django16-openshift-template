#!/usr/bin/env python

import os
import sys

sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR']))

os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python2.7/site-packages')

virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
