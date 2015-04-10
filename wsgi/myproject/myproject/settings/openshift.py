# -*- coding: utf-8 -*-

from .base import *

import imp
from os import environ


if environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True

default_keys = { 'SECRET_KEY': 'vm4rl5*ymb@2&d_(gc$gb-^twq9w(u69hi--%$5xrh!xk(t%hw' }
use_keys = default_keys
if ON_OPENSHIFT:
    imp.find_module('openshiftlibs')
    import openshiftlibs
    use_keys = openshiftlibs.openshift_secure(default_keys)

SECRET_KEY = use_keys['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(environ['OPENSHIFT_DATA_DIR'], 'db.sqlite3'),
    }
}
