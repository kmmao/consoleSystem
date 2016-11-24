# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from importlib import import_module
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Default settings
BOOTSTRAP3_DEFAULTS = {
    'jquery_url': '/static/jquery/jquery.min.js',
    'base_url': '/static/bootstrap/',
    'metisMenu_url':'/static/metisMenu/',
    'sco_url':'/static/sco/',
    'layer_url':'/static/layer/layer.js',
    'jquery_steps':'/static/jquery-steps/',
    'jquery_validate':'/static/jquery-validate/',
    'datatables_url':'/static/datatables/',
    'datatables_plugins_url':'/static/datatables-plugins/',
    'datatables_responsive_url':'/static/datatables-responsive/',
    'css_url': None,
    'theme_url': None,
    'javascript_url': None,
    'javascript_in_head': False,
    'include_jquery': False,
    'horizontal_label_class': 'col-md-3',
    'horizontal_field_class': 'col-md-9',
    'set_placeholder': True,
    'required_css_class': '',
    'error_css_class': 'has-error',
    'success_css_class': 'has-success',
    'font_awesome_css':'/static/font-awesome/css/font-awesome.min.css',
    'formset_renderers': {
        'default': 'bootstrap3.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'bootstrap3.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'bootstrap3.renderers.FieldRenderer',
        'inline': 'bootstrap3.renderers.InlineFieldRenderer',
    },
}

# Start with a copy of default settings
BOOTSTRAP3 = BOOTSTRAP3_DEFAULTS.copy()

# Override with user settings from settings.py
BOOTSTRAP3.update(getattr(settings, 'BOOTSTRAP3', {}))


def get_bootstrap_setting(setting, default=None):
    """
    Read a setting
    """
    return BOOTSTRAP3.get(setting, default)


def bootstrap_url(postfix):
    """
    Prefix a relative url with the bootstrap base url
    """
    return get_bootstrap_setting('base_url') + postfix

def metisMenu_url():
    return get_bootstrap_setting('metisMenu_url')

def sco_url():
    return get_bootstrap_setting('sco_url')

def layer_url():
    return get_bootstrap_setting('layer_url')

def jquery_validate_url():
    return get_bootstrap_setting('jquery_validate')

def jquery_steps_url():
    return get_bootstrap_setting('jquery_steps')

def datatables_url():
    return get_bootstrap_setting('datatables_url')

def datatables_plugins_url():
    return get_bootstrap_setting('datatables_plugins_url')

def datatables_responsive_url():
    return get_bootstrap_setting('datatables_responsive_url')


def jquery_url():
    """
    Return the full url to jQuery file to use
    """
    return get_bootstrap_setting('jquery_url')


def javascript_url():
    """
    Return the full url to the Bootstrap JavaScript file
    """
    return get_bootstrap_setting('javascript_url') or \
        bootstrap_url('js/bootstrap.min.js')

def fontAwesome_url():
    return get_bootstrap_setting('font_awesome_css')


def css_url():
    """
    Return the full url to the Bootstrap CSS file
    """
    return get_bootstrap_setting('css_url') or \
        bootstrap_url('css/bootstrap.min.css')


def theme_url():
    """
    Return the full url to the theme CSS file
    """
    return get_bootstrap_setting('theme_url')


def get_renderer(renderers, **kwargs):
    layout = kwargs.get('layout', '')
    path = renderers.get(layout, renderers['default'])
    mod, cls = path.rsplit(".", 1)
    return getattr(import_module(mod), cls)


def get_formset_renderer(**kwargs):
    renderers = get_bootstrap_setting('formset_renderers')
    return get_renderer(renderers, **kwargs)


def get_form_renderer(**kwargs):
    renderers = get_bootstrap_setting('form_renderers')
    return get_renderer(renderers, **kwargs)


def get_field_renderer(**kwargs):
    renderers = get_bootstrap_setting('field_renderers')
    return get_renderer(renderers, **kwargs)
