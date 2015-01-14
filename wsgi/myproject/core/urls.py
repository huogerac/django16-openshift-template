# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url

urlpatterns = patterns('',  # noqa

    url(r'^$', 'core.views.home', name='home'),
)
