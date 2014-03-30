"""
Django settings for social_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/
#----------------------------------------------------------------------------------
## SECURITY WARNING: keep the secret key used in production secret!
#----------------------------------------------------------------------------------
SECRET_KEY = 'lsxe(i_evzxe4p$qptxz8+)iiuqg33+tom*-sj!63c!+h&j&-z'
#----------------------------------------------------------------------------------
## SECURITY WARNING: keep the secret key used in production secret!
#----------------------------------------------------------------------------------

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Ashley McNamara', 'ashleymcnamara1@gmail.com'),
)

MANAGERS = ADMINS


ALLOWED_HOSTS = []

ROOT_URLCONF = 'social_project.urls'

WSGI_APPLICATION = 'social_project.wsgi.application'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# LOGIN_URL = '/social_list/'

# LOGIN_REDIRECT_URL = '/social_list/'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

SITE_ID = 1
gettext = lambda s: s

#----------------------------------------------------------------------------------
## APPS & BACKENDS
#----------------------------------------------------------------------------------
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3RD PARTY APPS
    'dajaxice',
    'dajax',
    'allaccess',
    # MY APPS
    'social_list',
    'apps.user',
    'social_project',
    'apps',
    'apps.lists',
    'apps.bootstrap',
)

AUTHENTICATION_BACKENDS = (
    # Default backend
    'django.contrib.auth.backends.ModelBackend',
    # Additional backend
    'allaccess.backends.AuthorizedServiceBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#----------------------------------------------------------------------------------
## TEMPLATE TOOLS
#----------------------------------------------------------------------------------

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
    'allaccess.context_processors.available_providers',
)

#----------------------------------------------------------------------------------
## DJANGO_PJAXR https://github.com/minddust/jquery-pjaxr
#----------------------------------------------------------------------------------

from django.template import add_to_builtins

add_to_builtins('django_pjaxr.templatetags.pjaxr_extends')

INSTALLED_APPS += ('django_pjaxr', 'widget_tweaks')

TEMPLATE_CONTEXT_PROCESSORS += ('django_pjaxr.context_processors.pjaxr_information',)

DEFAULT_PJAXR_TEMPLATE = "django_pjaxr/pjaxr.html"

LOGIN_URL = '/lists/'
LOGIN_REDIRECT_URL = '/lists/'
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

AUTH_PROFILE_MODULE = 'user.UserProfile'

#----------------------------------------------------------------------------------
## DATABASE https://docs.djangoproject.com/en/1.6/ref/settings/#databases
#----------------------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',     
    }
}

#----------------------------------------------------------------------------------
## INTERNATIONALIZATION  https://docs.djangoproject.com/en/1.6/topics/i18n/
#----------------------------------------------------------------------------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#----------------------------------------------------------------------------------
## STATIC FILES (CSS, JavaScript, Images) https://docs.djangoproject.com/en/1.6/howto/static-files/
#----------------------------------------------------------------------------------

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

#----------------------------------------------------------------------------------
## LOGGING
#----------------------------------------------------------------------------------
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'allaccess': {
            'handlers': ['console', ],
            'level': 'INFO',
        },
    }
}
