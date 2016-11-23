# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages

from console.models import Student, sever_url_info
from httpTohno.httpTohnoUtils import httpTohnoUtils
from httpTohno.methodEnum import methodEnum
from httpTohno.requestDict import requestDict
from .forms import ContactForm, FilesForm, ContactFormSet


# http://yuji.wordpress.com/2013/01/30/django-form-field-in-initial-data-requires-a-fieldfile-instance/
class FakeField(object):
    storage = default_storage


fieldfile = FieldFile(None, FakeField, 'dummy.txt')


def test(request):
    return HttpResponse('abc')

def dir(request,action):
	if request.is_ajax() and request.method == 'POST':
		if action == 'scan':
			params = requestDict().dirScanDict(request.POST['dirPath'])
			jsonData = httpTohnoUtils(params, methodEnum.dir_scan).httpTohnoWithPost()
			return HttpResponse(jsonData)
		if action == 'addDir':
			params = requestDict().dirCreateDict(request.POST['dirPath'])
			jsonData = httpTohnoUtils(params, methodEnum.dir_create).httpTohnoWithPost()
			return HttpResponse(jsonData)
		if action == 'deleteDir':
			params = requestDict().dirDeleteDict(request.POST['dirPath'])
			jsonData = httpTohnoUtils(params, methodEnum.dir_delete).httpTohnoWithPost()
			return HttpResponse(jsonData)
		if action == 'renameDir':
			params = requestDict().dirRenameDict(request.POST['parentDir'],request.POST['newName'],request.POST['oldName'])
			jsonData = httpTohnoUtils(params, methodEnum.dir_rename).httpTohnoWithPost()
			return HttpResponse(jsonData)

def fileHandle(request,action):
	if request.is_ajax() and request.method == 'POST':
		if action == 'renameFile':
			params = requestDict().fileRenameDict(request.POST['parentDir'], request.POST['newName'],request.POST['oldName'])
			jsonData = httpTohnoUtils(params, methodEnum.dir_rename).httpTohnoWithPost()
			return HttpResponse(jsonData)

def showRealStudents(request):
    list = Student.objects.all()
    return render_to_response('console/other/student.html', {'students': list})


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
