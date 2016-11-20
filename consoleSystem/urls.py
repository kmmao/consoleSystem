# -*- coding: utf-8 -*-
"""consoleSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from __future__ import unicode_literals

from django.conf.urls import url

from console.views import HomePageView, FormHorizontalView, FormInlineView, PaginationView, FormWithFilesView, \
    DefaultFormView, MiscView, DefaultFormsetView, DefaultFormByFieldView, showRealStudents, indexView, \
    configFileManage, templatesManage,test,dirScan

urlpatterns = [
    url(r'^dirScan$',dirScan),
    url(r'^test$', test),
    url(r'^$', indexView.as_view(), name='indexView'),
    url(r'^configFileManage$', configFileManage.as_view(), name='configFileManage'),
    url(r'^templatesManage$', templatesManage.as_view(), name='templatesManage'),
    url(r'^home$', HomePageView.as_view(), name='home'),
    url(r'^formset$', DefaultFormsetView.as_view(), name='formset_default'),
    url(r'^form$', DefaultFormView.as_view(), name='form_default'),
    url(r'^form_by_field$', DefaultFormByFieldView.as_view(), name='form_by_field'),
    url(r'^form_horizontal$', FormHorizontalView.as_view(), name='form_horizontal'),
    url(r'^form_inline$', FormInlineView.as_view(), name='form_inline'),
    url(r'^form_with_files$', FormWithFilesView.as_view(), name='form_with_files'),
    url(r'^pagination$', PaginationView.as_view(), name='pagination'),
    url(r'^misc$', MiscView.as_view(), name='misc'),
    url(r'^showRealStudents/$', showRealStudents),
    #url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
]
