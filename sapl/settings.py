"""
Django settings for sapl project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
from unipath import Path

from .temp_suppress_crispy_form_warnings import \
    SUPRESS_CRISPY_FORM_WARNINGS_LOGGING

BASE_DIR = Path(__file__).ancestor(2)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!9g1-#la+#(oft(v-y1qhy$jk-2$24pdk69#b_jfqyv!*%a_)t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',  # must come before django.contrib.admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # sapl modules
    'base',
    'parlamentares',
    'comissoes',
    'compilacao',
    'sessao',
    'materia',
    'norma',
    'lexml',
    'painel',
    'protocoloadm',

    # more
    'django_extensions',
    'djangobower',
    'bootstrap3',  # basically for django_admin_bootstrapped
    'crispy_forms',
    'crispy_forms_foundation',
    'sass_processor',
)
if DEBUG:
    INSTALLED_APPS += ('debug_toolbar',)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'sapl.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sapl.context_processors.parliament_info',
            ],
            'debug': DEBUG
        },
    },
]

WSGI_APPLICATION = 'sapl.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sapl',
        'USER': 'sapl',
        'PASSWORD': 'sapl',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = False
USE_L10N = False
USE_TZ = True
# DATE_FORMAT = 'N j, Y'
DATE_FORMAT = 'd/m/Y'
SHORT_DATE_FORMAT = 'd/m/Y'
DATE_INPUT_FORMATS = ('%d/%m/%Y', '%m-%d-%Y', '%Y-%m-%d')

LOCALE_PATHS = (
    'locale',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.child("collected_static")
STATICFILES_DIRS = (BASE_DIR.child("static"),)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'sass_processor.finders.CssFinder',
)

MEDIA_ROOT = BASE_DIR.child("media")

DAB_FIELD_RENDERER = \
    'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'
CRISPY_TEMPLATE_PACK = 'foundation-5'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'foundation-5'
CRISPY_FAIL_SILENTLY = not DEBUG

BOWER_COMPONENTS_ROOT = BASE_DIR.child("bower")
BOWER_INSTALLED_APPS = (
    'foundation',
    'foundation-datepicker',
    'components-font-awesome',
    'foundation-icon-fonts',
    'tinymce',
    'jquery-ui',
    'jquery-runner',
    'jQuery-Mask-Plugin',
)

# Additional search paths for SASS files when using the @import statement
SASS_PROCESSOR_INCLUDE_DIRS = (
    BOWER_COMPONENTS_ROOT.child('bower_components', 'foundation', 'scss'),
)

# hack to suppress many annoying warnings from crispy_forms
# see sapl.temp_suppress_crispy_form_warnings
LOGGING = SUPRESS_CRISPY_FORM_WARNINGS_LOGGING
