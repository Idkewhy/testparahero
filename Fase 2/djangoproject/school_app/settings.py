"""
Django settings for school_app project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "__$1ud47e&nyso5h5o3fwnqu4+hfqcply9h$k*h2s34)hn5@nc"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.vercel.app', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "widget_tweaks",
    "apps.corecode",
    "apps.students",
    "apps.staffs",
    "apps.finance",
    "apps.result",
    "apps.teachers",
    "apps.representatives",
    "apps.content",
    "ckeditor",
    "ckeditor_uploader"
]

X_FRAME_OPTIONS = "SAMEORIGIN"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "apps.corecode.middleware.SiteWideConfigs",
    "apps.teachers.middleware.TeacherID",
    "apps.students.middleware.StudentID",
    "apps.representatives.middleware.RepresentativesID",
]

ROOT_URLCONF = "school_app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.corecode.context_processors.site_defaults",
            ],
            
            "libraries":{
                "custom_templatetag": 'apps.templatetags.user_groups',
                "student_extras": 'apps.templatetags.student_extras',
                "custom_tags": 'apps.templatetags.custom_tag',
                }
        },
    },
]

WSGI_APPLICATION = "school_app.wsgi.app"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "es-mx"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_ALLOW_NONIMAGE_FILES = True

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'extraPlugins': ','.join(['image']),
    },
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240

STATIC_URL = "/static/"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = "/media/"

LOGIN_REDIRECT_URL = "/"

LOGOUT_REDIRECT_URL = "/"

LOGIN_URL = '/accounts/login/'

SESSION_SAVE_EVERY_REQUEST = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_COOKIE_AGE = 10800

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "lrojaspaila@gmail.com"
EMAIL_HOST_PASSWORD = "lmjc gapy ucye uvbe"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

CKEDITOR_RESTRICT_BY_USER = False



# Configuración de LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # Enviar logs a la consola
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],  # Por defecto, enviar logs a la consola
        'level': 'WARNING',
    },
    'django': {
        'handlers': ['console'],  # Logs de Django también se envían a la consola
        'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),  # Nivel de logs configurado por variable de entorno
        'propagate': False,
    },
}

# Configuración adicional para entornos locales
if not os.getenv('VERCEL', False):  # Si NO estamos en Vercel
    LOGGING['handlers']['file'] = {
        'level': 'DEBUG',
        'class': 'logging.FileHandler',
        'filename': os.path.join(BASE_DIR, 'debug.log'),  # Ruta al archivo de logs en local
        'formatter': 'verbose',
    }
    LOGGING['root']['handlers'].append('file')  # Agregar el handler de archivo a los logs raíz


DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Site Default values