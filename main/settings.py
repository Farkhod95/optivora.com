import os
from datetime import timedelta
from django.utils.translation import gettext_lazy as _
from corsheaders.defaults import default_headers
import environ
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = 'django-insecure-12345yourkeyhere54321'

DEBUG = False

ALLOWED_HOSTS = ["api.optivora-group.com", "localhost", "127.0.0.1"]

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'restapp',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'rest_framework_simplejwt.token_blacklist',
    'django_filters',
    'corsheaders',
    # 'optivora',
    'directory',
    'django_celery_results',
    'django_celery_beat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # for front
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'restapp.middlewares.middlewares.RequestMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # for translation
]

CORS_ORIGIN_ALLOW_ALL = False

CORS_ALLOWED_ORIGINS = [
    "optivora-group.com",
    "http://localhost:3000",  # agar lokalda ishlayotgan bo‘lsa
    "https:optivora-group.com",  # agar lokalda ishlayotgan bo‘lsa
]


ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'staticfiles': 'django.templatetags.static',
            }
        },
    },
]

# WSGI_APPLICATION = 'main.wsgi.application'
ASGI_APPLICATION = 'main.asgi.application'

### Local Host uchun

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': env("DB_NAME"),
#         'USER': env("DB_USER"),
#         'PASSWORD': env("DB_PASSWORD"),
#         'HOST': env("DB_HOST"),
#         'PORT': env("DB_PORT"),
#     }
# }

### Server uchun


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # Loyihaning ildizida db.sqlite3 faylini yaratadi
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Django REST framework simplejwt

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ),
    'UNICODE_JSON': True,
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'EXCEPTION_HANDLER': 'restapp.exceptions.custom_exception_handler',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=120),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=14),
    'BLACKLIST_AFTER_ROTATION': True,
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },
}

LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'

LANGUAGES = (
    ('en', _('Ingliz')),
    ('uz', _('O‘zbek (Lotin)')),
    ('ru', _('Русский')),

)

# Internationalization

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGE_CODE = 'uz'

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# WhiteNoise’ga tavsiya etiladigan storage:
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

AUTH_USER_MODEL = 'users.User'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# media fayllar (upload qilingan rasm, fayl, video)
MEDIA_URL = '/assets/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'