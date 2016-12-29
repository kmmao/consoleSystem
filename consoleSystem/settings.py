# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import logging.handlers
import os
import sys

import django.utils.log

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Include BOOTSTRAP3_FOLDER in path
BOOTSTRAP3_FOLDER = os.path.abspath(os.path.join(BASE_DIR, '.', 'bootstrap3'))
if BOOTSTRAP3_FOLDER not in sys.path:
	sys.path.insert(0, BOOTSTRAP3_FOLDER)

DEBUG = True

ADMINS = ()

DATABASES = {
	'default': {
		# 'ENGINE': 'django.db.backends.sqlite3',
		# 'NAME': ':memory:',
		# 'NAME':os.path.join(BASE_DIR,'.','consoleDb'),
	}
}

SHIVA_URL = r'127.0.0.1'
SHIVA_VERSION = r'/shiva/api/v1.0'
SHIVA_PORT = 5000
SHIVA_OUTTIME = 30

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', ]
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/static/"
MEDIA_ROOT = ''

# URL that handles the static served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
	# Put strings here, like "/home/html/static" or "C:/www/django/static".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
	os.path.join(BASE_DIR, 'bootstrap3/static'),
	os.path.join(BASE_DIR, 'console/static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	# 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8s)l4^2s&&0*31-)+6lethmfy3#r1egh^6y^=b9@g!q63r649_'

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	# 这里这个要禁用掉
	# 'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'consoleSystem.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'consoleSystem.wsgi.application'

TEMPLATES = [{
	'BACKEND': 'django.template.backends.django.DjangoTemplates',
	'APP_DIRS': True,
	'OPTIONS': {
		'context_processors': [
			"django.contrib.auth.context_processors.auth",
			"django.template.context_processors.debug",
			"django.template.context_processors.i18n",
			"django.template.context_processors.static",
			"django.template.context_processors.static",
			"django.template.context_processors.tz",
			"django.contrib.messages.context_processors.messages"
		]
	}
}]

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	'bootstrap3',
	'console',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
	'version': 1,
	'disable_existing_loggers': True,
	'formatters': {
		'standard': {
			'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
		# 日志格式
	},
	'filters': {
	},
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
			'class': 'django.utils.log.AdminEmailHandler',
			'include_html': True,
		},
		'default': {
			'level': 'DEBUG',
			'class': 'logging.handlers.RotatingFileHandler',
			'filename': os.path.join(BASE_DIR, '.', 'log/all.log'),  # 日志输出文件
			'maxBytes': 1024 * 1024 * 5,  # 文件大小
			'backupCount': 5,  # 备份份数
			'formatter': 'standard',  # 使用哪种formatters日志格式
		},
		'error': {
			'level': 'ERROR',
			'class': 'logging.handlers.RotatingFileHandler',
			'filename': os.path.join(BASE_DIR, '.', 'log/error.log'),
			'maxBytes': 1024 * 1024 * 5,
			'backupCount': 5,
			'formatter': 'standard',
		},
		'console': {
			'level': 'DEBUG',
			'class': 'logging.StreamHandler',
			'formatter': 'standard'
		},
		'request_handler': {
			'level': 'DEBUG',
			'class': 'logging.handlers.RotatingFileHandler',
			'filename': os.path.join(BASE_DIR, '.', 'log/script.log'),
			'maxBytes': 1024 * 1024 * 5,
			'backupCount': 5,
			'formatter': 'standard',
		},
		'scprits_handler': {
			'level': 'DEBUG',
			'class': 'logging.handlers.RotatingFileHandler',
			'filename': os.path.join(BASE_DIR, '.', 'log/script.log'),
			'maxBytes': 1024 * 1024 * 5,
			'backupCount': 5,
			'formatter': 'standard',
		}
	},
	'loggers': {
		'django': {
			'handlers': ['default'],
			'level': 'DEBUG',
			'propagate': False
		},
		'django.request': {
			'handlers': ['request_handler','console'],
			'level': 'DEBUG',
			'propagate': False,
		},
		'scripts': {
			'handlers': ['scprits_handler','console'],
			'level': 'DEBUG',
			'propagate': False
		},
		'console': {
			'handlers': ['default', 'error','console'],
			'level': 'DEBUG',
			'propagate': True
		},
		'httpTohno': {
			'handlers': ['default', 'error','console'],
			'level': 'DEBUG',
			'propagate': True
		}
	}
	# 'version': 1,
	# 'disable_existing_loggers': False,
	# 'filters': {
	#     'require_debug_false': {
	#         '()': 'django.utils.log.RequireDebugFalse'
	#     }
	# },
	# 'handlers': {
	#     'mail_admins': {
	#         'level': 'ERROR',
	#         'filters': ['require_debug_false'],
	#         'class': 'django.utils.log.AdminEmailHandler'
	#     }
	# },
	# 'loggers': {
	#     'django.request': {
	#         'handlers': ['mail_admins'],
	#         'level': 'ERROR',
	#         'propagate': True,
	#     },
	# }
}

# Settings for django-bootstrap3
BOOTSTRAP3 = {
	'error_css_class': 'bootstrap3-error',
	'required_css_class': 'bootstrap3-required',
	'javascript_in_head': True,
}
