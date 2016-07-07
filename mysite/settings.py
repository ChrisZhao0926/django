"""
Django settings for mysite project.

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

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0*dd3tp^zlv#h-v0sc5c8b9)s*tsa7t+!u=l2wpflfnybls=i+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'userena',
    'guardian',
    'easy_thumbnails',
    'accounts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtpem1.sonyericsson.net'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'chris.zhao@sonymobile.com'
EMAIL_USE_TLS = False
EMAIL_SUBJECT_PREFIX = '[Test]'
SERVER_EMAIL = 'chris.zhao@sonymobile.com'


ANONYMOUS_USER_ID = -1

AUTH_PROFILE_MODULE = 'accounts.MyProfile'
USERENA_SIGNIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'


USERENA_SIGNIN_AFTER_SIGNUP = True
USERENA_SIGNIN_REDIRECT_URL = '/polls/'
USERENA_ACTIVATION_REQUIRED = False
# USERENA_ACTIVATION_DAYS = 7
# USERENA_ACTIVATION_NOTIFY = True
# USERENA_ACTIVATION_NOTIFY_DAYS = 2
# USERENA_ACTIVATED = "ALREADY_ACTIVATED"
# USERENA_REMEMBER_ME_DAYS = ('a month', 30)
# USERENA_FORBIDDEN_USERNAMES = ('signup', 'signout', 'signin', 'activate', 'me', 'password')
# USERENA_MUGSHOT_GRAVATAR = True
# USERENA_MUGSHOT_GRAVATAR_SECURE = False
#
# USERENA_MUGSHOT_DEFAULT = "mm"
# USERENA_MUGSHOT_SIZE = 50
# USERENA_MUGSHOT_PATH = "mugshots/%(username)s/"
# USERENA_USE_HTTPS = False
#
# USERENA_DEFAULT_PRIVACY = "registered"
# USERENA_PROFILE_DETAIL_TEMPLATE = "userena/profile_detail.html"
# USERENA_PROFILE_LIST_TEMPLATE = "userena/profile_list.html"
# USERENA_DISABLE_PROFILE_LIST = False
# USERENA_DISABLE_SIGNUP = False
# USERENA_USE_MESSAGES = True
# USERENA_LANGUAGE_FIELD = "language"
# USERENA_WITHOUT_USERNAMES = False
# USERENA_HIDE_EMAIL = False
# USERENA_HTML_EMAIL = False
# USERENA_USE_PLAIN_TEMPLATE = True
