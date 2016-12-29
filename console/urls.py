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

from console.views import indexView, configFileManage, templatesManage, dir, fileHandle, fileIframe, \
	getServerUrlInfo, getTplist, tpHandle, host, hostManage, HomePageView, DefaultFormsetView, DefaultFormView, \
	DefaultFormByFieldView, FormHorizontalView, FormInlineView, FormWithFilesView, \
	PaginationView, MiscView, hostEdit,hostgroupManage, hostInfo,hostgroupAdd,hostgroupInfo

urlpatterns = [
	url(r'^host/(?P<action>\w+)/$', host),
	url(r'^dir/(?P<action>\w+)/(?P<env>\w+)$', dir),
	url(r'^file/(?P<action>\w+)/(?P<env>\w+)$', fileHandle),
	url(r'^fileIframe$', fileIframe.as_view(), name='fileIframe'),
	url(r'^tp/(?P<action>\w+)/$', tpHandle),
	url(r'^getServerUrlInfo/(?P<env>\w+)$', getServerUrlInfo),
	url(r'^$', indexView.as_view(), name='indexView'),
	url(r'^hostManage$', hostManage.as_view(), name='hostManage'),
	url(r'^hostInfo$', hostInfo.as_view(), name='hostInfo'),
	url(r'^hostgroupManage$', hostgroupManage.as_view(), name='hostgroupManage'),
	url(r'^hostgroupAdd$', hostgroupAdd.as_view(), name='hostgroupAdd'),
	url(r'^hostgroupInfo$', hostgroupInfo.as_view(), name='hostgroupInfo'),
	url(r'^hostEdit$',hostEdit.as_view()),
	url(r'^configFileManage$', configFileManage.as_view(), name='configFileManage'),
	url(r'^templatesManage$', templatesManage.as_view(), name='templatesManage'),
	url(r'^getTplist/$', getTplist),
	url(r'^home$', HomePageView.as_view(), name='home'),
	url(r'^formset$', DefaultFormsetView.as_view(), name='formset_default'),
	url(r'^form$', DefaultFormView.as_view(), name='form_default'),
	url(r'^form_by_field$', DefaultFormByFieldView.as_view(), name='form_by_field'),
	url(r'^form_horizontal$', FormHorizontalView.as_view(), name='form_horizontal'),
	url(r'^form_inline$', FormInlineView.as_view(), name='form_inline'),
	url(r'^form_with_files$', FormWithFilesView.as_view(), name='form_with_files'),
	url(r'^pagination$', PaginationView.as_view(), name='pagination'),
	url(r'^misc$', MiscView.as_view(), name='misc'),
	# url(r'^showRealStudents/$', showRealStudents),
]
