# Stripped down sample settings for django-spambayes project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG


DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'data.db' 

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
ADMIN_MEDIA_PREFIX = '/media/'
SECRET_KEY = '$hh4h!xor*cp9fb03a$0ew06_ou3qpx7vn!_ub@(z1b$=wtw!#'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'django-spambayes.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.comments',
    'djangobayes',
    'commentbayes',
    'sb_demo',
)
