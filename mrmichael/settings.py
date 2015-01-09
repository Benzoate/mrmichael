"""
Django settings for mrmichael project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ON_HEROKU = os.environ.get('ON_HEROKU')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
DEFAULT_SECRET_KEY = 'q47ul@#_&s!8fif!k2j78v6twp9srf^^s@9(wl1&)#@7epfu91'
SECRET_KEY = os.environ.get('SECRET_KEY', DEFAULT_SECRET_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', True) != 'False'
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'pages',
    'pictures',
    'compressor'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mrmichael.urls'

WSGI_APPLICATION = 'mrmichael.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
if ON_HEROKU:
    DATABASES['default'] = dj_database_url.config()


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (('en', 'English'),
             ('ja', 'Japanese'),)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',
                        'compressor.filters.cssmin.CSSMinFilter']

if ON_HEROKU:
    STATICFILES_STORAGE = 'mrmichael.storage.CachedS3BotoStorage'
    COMPRESS_STORAGE = STATICFILES_STORAGE
    DEFAULT_FILE_STORAGE = 'mrmichael.storage.CachedS3BotoStorage'
    AWS_QUERYSTRING_AUTH = False
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    MEDIA_URL = 'http://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
