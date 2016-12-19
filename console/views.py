# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import logging

import datetime
import time
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages

from console.models import Student, sever_url_info, templates_file_info
from consoleSystem.settings import SHIVA_URL, SHIVA_OUTTIME, SHIVA_PORT
from httpTohno.HttpHelper import HttpHelper
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

__shiva_url = 'http://%s:%s'%(SHIVA_URL,SHIVA_PORT)

def test(request):
	return HttpResponse('abc')

def dir(request,action,env):
	if request.is_ajax() and request.method == 'POST':
		url = str('%s%s' % (__shiva_url, methodEnum.server_url_info_get))
		severUrlInfo = HttpHelper().url(url).headers().post(json.dumps({'env':env}),HttpHelper().getData)
		kwargs = {
			'env': env,
			'url': severUrlInfo[0]['url'],
			'port': severUrlInfo[0]['port'],
			'out_time': severUrlInfo[0]['out_time']
		}
		if action == 'scan':
			params = requestDict().dirScanDict(request.POST['dirPath'])
			jsonData = httpTohnoUtils(params, methodEnum.dir_scan,**kwargs).httpTohnoWithPost()
			return HttpResponse(jsonData)
		if action == 'addDir':
			params = requestDict().dirCreateDict(request.POST['dirPath'])
			jsonData = httpTohnoUtils(params, methodEnum.dir_create,**kwargs).httpTohnoWithPost()
			return HttpResponse(jsonData)
		if action == 'deleteDir':
			params = requestDict().dirDeleteDict(request.POST['dirPath'])
			jsonData = httpTohnoUtils(params, methodEnum.dir_delete,**kwargs).httpTohnoWithPost()
			return HttpResponse(jsonData)
		if action == 'renameDir':
			params = requestDict().dirRenameDict(request.POST['parentDir'],request.POST['newName'],request.POST['oldName'])
			jsonData = httpTohnoUtils(params, methodEnum.dir_rename,**kwargs).httpTohnoWithPost()
			return HttpResponse(jsonData)

def fileHandle(request,action,env):
	if request.is_ajax() and request.method == 'POST':
		url = str('%s%s' % (__shiva_url, methodEnum.server_url_info_get))
		severUrlInfo = HttpHelper().url(url).headers().post(json.dumps({'env': env}), HttpHelper().getData)
		kwargs = {
			'env': env,
			'url': severUrlInfo[0]['url'],
			'port': severUrlInfo[0]['port'],
			'out_time': severUrlInfo[0]['out_time']
		}
		if action == 'renameFile':
			params = requestDict().fileRenameDict(request.POST['parentDir'], request.POST['newName'],request.POST['oldName'])
			jsonData = httpTohnoUtils(params, methodEnum.dir_rename,**kwargs).httpTohnoWithPost()
			return HttpResponse(jsonData)
		if action == 'createFile':
			params = requestDict().fileCreateDict(json.loads(request.POST['configFileInfo']))
			jsonData = httpTohnoUtils(params, methodEnum.file_create,**kwargs).httpTohnoWithPost()
			return HttpResponse(jsonData)
		if action == 'updateFile':
			params = requestDict().fileUpdateDict(json.loads(request.POST['configFileInfo']))
			jsonData = httpTohnoUtils(params, methodEnum.file_update,**kwargs).httpTohnoWithPost()
			return HttpResponse(jsonData)
		if action == 'getFile':
			params = requestDict().fileGetDict(request.POST['filePath'])
			jsonData = httpTohnoUtils(params, methodEnum.file_get,**kwargs).httpTohnoWithPost()
			return HttpResponse(jsonData)
		if action == 'getFileBackup':
			params = requestDict().fileGetBackupDict(request.POST['filePath'],request.POST['backupfile'])
			jsonData = httpTohnoUtils(params, methodEnum.file_backupget,**kwargs).httpTohnoWithPost()
			return HttpResponse(jsonData)
		if action == 'deleteFile':
			params = requestDict().fileDeleteDict(request.POST['filePath'])
			jsonData = httpTohnoUtils(params, methodEnum.file_delete,**kwargs).httpTohnoWithPost()
			return HttpResponse(jsonData)

def tpHandle(request,action):
	if request.is_ajax() and request.method == 'POST':
		if action == 'get':
			try:
				url = str('%s%s/%s' % (__shiva_url, methodEnum.templateFile,request.POST['id']))
				obj = HttpHelper().url(url).get(func=HttpHelper().getData)
				obj[0]['content'] = base64.b64decode(obj[0]['content'])
				return HttpResponse(json.dumps(obj[0]))
			except Exception,e:
				logging.error('tpHandle>get>exception:%s' % e)
		if action == 'getTpList':
			try:
				data = HttpHelper().url('%s%s' % (__shiva_url, methodEnum.templateFileList)).get(func=HttpHelper().getData)
				return HttpResponse(json.dumps(data))
			except Exception,e:
				logging.error('tpHandle>getTpList>exception:%s' % e)
		if action == 'save':
			jsonDataDict = {}
			try:
				fileInfo = json.loads(request.POST['fileInfo'])
				requestData = {}
				jsonDataDict['code'] = 0
				jsonDataDict['msg'] = '处理成功'
				requestData['name'] = fileInfo['fileName']
				requestData['content'] = fileInfo['fileContent']
				requestData['modify_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
				if len(fileInfo['id']) > 0:
					requestData['id'] = fileInfo['id']
					url = str('%s%s/%s' % (__shiva_url, methodEnum.templateFile,fileInfo['id']))
					rowCount = HttpHelper().url(url).headers().put(json.dumps(requestData),func=HttpHelper().getData)
					if not rowCount:
						jsonDataDict['code'] = -1
						jsonDataDict['msg'] = '系统异常，请联系管理员'
					return HttpResponse(json.dumps(jsonDataDict))
				else:
					url = str('%s%s' % (__shiva_url, methodEnum.templateFile))
					rowCount = HttpHelper().url(url).headers().post(json.dumps(requestData), func=HttpHelper().getData)
					if not rowCount:
						jsonDataDict['code'] = -1
						jsonDataDict['msg'] = '系统异常，请联系管理员'
					return HttpResponse(json.dumps(jsonDataDict))
			except Exception,e:
				logging.error('tpHandle>save>exception:%s' % e)
				jsonDataDict['code'] = -1
				jsonDataDict['msg'] = '异常：%s'%e
				return HttpResponse(json.dumps(jsonDataDict))
		if action == 'delete':
			jsonDataDict = {}
			try:
				url = '%s%s/%s' % (__shiva_url, methodEnum.templateFile, request.POST['id'])
				jsonDataDict['code'] = 0
				jsonDataDict['msg'] = '处理成功'
				rowCount = HttpHelper().url(url).delete(None,func=HttpHelper().getData)
				if not rowCount:
					jsonDataDict['code'] = -1
					jsonDataDict['msg'] = '系统异常，请联系管理员'
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
	serverUrlInfo = httpTohnoUtils({'env':env}, methodEnum.server_url_info_get, 'shiva', SHIVA_URL,SHIVA_PORT,
								   SHIVA_OUTTIME).httpTohnoWithPost()
	jsonData = httpTohnoUtils(None, methodEnum.server_infos, env,serverUrlInfo[0]['url'],
							  serverUrlInfo[0]['port'],serverUrlInfo[0]['out_time']).httpTohonWithGet()
	res = set()
	for item in jsonData['hostinfos']:
		if item['groupname']:
			res.add('file:%s' % item['groupname'])
		if item['hosts']:
			res.update(map(conventForFile,item['hosts']))
	for item in jsonData['zkinfos']:
		if item['zkname']:
			res.add('zk:%s' % item['zkname'])
	return HttpResponse('|'.join(res))

def conventForFile(x):
	return 'file:%s' % x

def getTplist(request):
	"""
	:param request:
	:return: 返回模板文件列表
	"""
	try:
		url = '%s%s' % (__shiva_url, methodEnum.templateFileList)
		data = HttpHelper().url(url).get(func=HttpHelper().getData)
		listSet = []
		dic = {}
		for obj in data:#%Y-%m-%d %H:%M:%S
			listSet.append([obj['name'],datetime.datetime.strptime(obj['modify_time'], "%a, %d %b %Y %H:%M:%S GMT").
						   strftime('%Y-%m-%d %H:%M:%S'),obj['id']])
		dic['data'] = listSet
		return HttpResponse(json.dumps(dic))
	except Exception,e:
		logging.error('getTplist>exception:%s' % e)

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

	def get_context_data(self,**kwargs):
		context = super(configFileManage, self).get_context_data(**kwargs)
		jsonData = httpTohnoUtils(None, methodEnum.server_url_infos, 'shiva', SHIVA_URL,SHIVA_PORT, SHIVA_OUTTIME).httpTohonWithGet()
		context['serverUrlInfos'] = jsonData
		return context

class templatesManage(TemplateView):
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
