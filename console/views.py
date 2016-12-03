# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import logging

from django.core import serializers
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages

from console.CJsonEncoder import CJsonEncoder
from console.models import Student, sever_url_info, templates_file_info
from httpTohno.httpTohnoUtils import httpTohnoUtils
from httpTohno.methodEnum import methodEnum
from httpTohno.requestDict import requestDict
from .forms import ContactForm, FilesForm, ContactFormSet

import base64


# http://yuji.wordpress.com/2013/01/30/django-form-field-in-initial-data-requires-a-fieldfile-instance/
class FakeField(object):
    storage = default_storage


fieldfile = FieldFile(None, FakeField, 'dummy.txt')
logger = logging.getLogger('console')

def test(request):
    return HttpResponse('abc')

def dir(request,action,env):
	if request.is_ajax() and request.method == 'POST':
		if action == 'scan':
			params = requestDict().dirScanDict(request.POST['dirPath'])
			jsonData = httpTohnoUtils(params, methodEnum.dir_scan,env).httpTohnoWithPost()
			return HttpResponse(jsonData)
		if action == 'addDir':
			params = requestDict().dirCreateDict(request.POST['dirPath'])
			jsonData = httpTohnoUtils(params, methodEnum.dir_create,env).httpTohnoWithPost()
			return HttpResponse(jsonData)
		if action == 'deleteDir':
			params = requestDict().dirDeleteDict(request.POST['dirPath'])
			jsonData = httpTohnoUtils(params, methodEnum.dir_delete,env).httpTohnoWithPost()
			return HttpResponse(jsonData)
		if action == 'renameDir':
			params = requestDict().dirRenameDict(request.POST['parentDir'],request.POST['newName'],request.POST['oldName'])
			jsonData = httpTohnoUtils(params, methodEnum.dir_rename,env).httpTohnoWithPost()
			return HttpResponse(jsonData)

def fileHandle(request,action,env):
	if request.is_ajax() and request.method == 'POST':
		if action == 'renameFile':
			params = requestDict().fileRenameDict(request.POST['parentDir'], request.POST['newName'],request.POST['oldName'])
			jsonData = httpTohnoUtils(params, methodEnum.dir_rename,env).httpTohnoWithPost()
			return HttpResponse(jsonData)
		if action == 'createFile':
			params = requestDict().fileCreateDict(json.loads(request.POST['configFileInfo']))
			#params['content'] = base64.b64encode(params['content'])
			jsonData = httpTohnoUtils(params, methodEnum.file_create,env).httpTohnoWithPost()
			return HttpResponse(jsonData)
		if action == 'updateFile':
			params = requestDict().fileUpdateDict(json.loads(request.POST['configFileInfo']))
			#params['content'] = base64.b64encode(params['content'])
			jsonData = httpTohnoUtils(params, methodEnum.file_update,env).httpTohnoWithPost()
			return HttpResponse(jsonData)
		if action == 'getFile':
			params = requestDict().fileGetDict(request.POST['filePath'])
			jsonData = httpTohnoUtils(params, methodEnum.file_get,env).httpTohnoWithPost()
			return HttpResponse(jsonData)
		if action == 'getFileBackup':
			params = requestDict().fileGetBackupDict(request.POST['filePath'],request.POST['backupfile'])
			jsonData = httpTohnoUtils(params, methodEnum.file_backupget,env).httpTohnoWithPost()
			return HttpResponse(jsonData)
		if action == 'deleteFile':
			params = requestDict().fileDeleteDict(request.POST['filePath'])
			jsonData = httpTohnoUtils(params, methodEnum.file_delete,env).httpTohnoWithPost()
			return HttpResponse(jsonData)

def tpHandle(request,action):
		if request.is_ajax() and request.method == 'POST':
			if action == 'get':
				objDict = templates_file_info.objects.get(id=request.POST['id']).toDict()
				objDict['content'] = base64.b64decode(objDict['content'])
				#print json.dumps(objDict,cls=CJsonEncoder)
				return HttpResponse(json.dumps(objDict,cls=CJsonEncoder))
			if action == 'getTpList':
				list = serializers.serialize("json", templates_file_info.objects.all())
				return  HttpResponse(list)
			if action == 'save':
				jsonDataDict = {}
				try:
					fileInfo = json.loads(request.POST['fileInfo'])
					jsonDataDict['code'] = 0
					jsonDataDict['msg'] = '处理成功'
					tp = templates_file_info()
					tp.name = fileInfo['fileName']
					tp.content = fileInfo['fileContent']
					if len(fileInfo['id']) > 0:
						tp.id = fileInfo['id']
					tp.save()
					return HttpResponse(json.dumps(jsonDataDict))
				except Exception,e:
					logging.error('tpHandle-exception:%s' % e)
					jsonDataDict['code'] = -1
					jsonDataDict['msg'] = '异常：%s'%e
					return HttpResponse(json.dumps(jsonDataDict))
			if action == 'delete':
				jsonDataDict = {}
				try:
					jsonDataDict['code'] = 0
					jsonDataDict['msg'] = '处理成功'
					tp = templates_file_info()
					tp.id = request.POST['id']
					tp.delete()
					return HttpResponse(json.dumps(jsonDataDict))
				except Exception,e:
					logging.error('tpHandle-exception:%s' % e)
					jsonDataDict['code'] = -1
					jsonDataDict['msg'] = '异常：%s' % e
					return HttpResponse(json.dumps(jsonDataDict))


class fileIframe(TemplateView):
	template_name = 'console/config/fileIframe.html'

	def get_context_data(self, **kwargs):
		context = super(fileIframe, self).get_context_data(**kwargs)
		messages.info(self.request, 'hello http://example.com')
		return context

def showRealStudents(request):
    list = Student.objects.all()
    return render_to_response('console/other/student.html', {'students': list})

def getServerUrlInfo(request,env):
	jsonData = httpTohnoUtils(None, methodEnum.server_infos, env).httpTohonWithGet()
	res = set()
	for item in jsonData['hostinfos']:
			res.add(item['groupname'])
			res.update(item['hosts'])
	return HttpResponse('|'.join(res))
	#obj = sever_url_info.objects.get(name__exact='qa')
	# list = serializers.serialize("json", sever_url_info.objects.all())
	# return  HttpResponse(list)

def getTplist(request):
	"""
	:param request:
	:return: 返回模板文件列表
	"""
	listSet = []
	dic = {}
	for obj in templates_file_info.objects.all():
		listSet.append([obj.name,obj.modify_time.strftime('%Y-%m-%d %H:%M:%S'),obj.id])
	dic['data'] = listSet
	return HttpResponse(json.dumps(dic))


class HomePageView(TemplateView):
    template_name = 'console/other/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'hello http://example.com')
        return context

class indexView(FormView):
    template_name = 'console/index.html'
    form_class = ContactFormSet

class configFileManage(TemplateView):
    template_name = 'console/config/configFileManage.html'
    #form_class = ContactFormSet

    def get_context_data(self, **kwargs):
        context = super(configFileManage, self).get_context_data(**kwargs)
        context['serverUrlInfos'] = sever_url_info.objects.all()
        return context

class templatesManage(FormView):
    template_name = 'console/config/templatesManage.html'
    form_class = ContactFormSet

class DefaultFormsetView(FormView):
    template_name = 'console/other/formset.html'
    form_class = ContactFormSet


class DefaultFormView(FormView):
    template_name = 'console/other/form.html'
    form_class = ContactForm


class DefaultFormByFieldView(FormView):
    template_name = 'console/other/form_by_field.html'
    form_class = ContactForm


class FormHorizontalView(FormView):
    template_name = 'console/other/form_horizontal.html'
    form_class = ContactForm


class FormInlineView(FormView):
    template_name = 'console/other/form_inline.html'
    form_class = ContactForm


class FormWithFilesView(FormView):
    template_name = 'console/other/form_with_files.html'
    form_class = FilesForm

    def get_context_data(self, **kwargs):
        context = super(FormWithFilesView, self).get_context_data(**kwargs)
        context['layout'] = self.request.GET.get('layout', 'vertical')
        return context

    def get_initial(self):
        return {
            'file4': fieldfile,
        }


class PaginationView(TemplateView):
    template_name = 'console/other/pagination.html'

    def get_context_data(self, **kwargs):
        context = super(PaginationView, self).get_context_data(**kwargs)
        lines = []
        for i in range(200):
            lines.append('Line %s' % (i + 1))
        paginator = Paginator(lines, 10)
        page = self.request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_lines = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            show_lines = paginator.page(paginator.num_pages)
        context['lines'] = show_lines
        return context


class MiscView(TemplateView):
    template_name = 'console/other/misc.html'
