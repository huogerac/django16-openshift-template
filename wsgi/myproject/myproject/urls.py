# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',  # noqa

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('core.urls')),

)
