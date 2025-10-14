# optivoraback/settings.py
import os
from datetime import timedelta
from django.utils.translation import gettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-12345yourkeyhere54321'
DEBUG = False

ALLOWED_HOSTS = [
    "api.optivora-group.com", "optivora-group.com", "www.optivora-group.com",
    "localhost", "127.0.0.1"
]

CSRF_TRUSTED_ORIGINS = [
    "https://optivora-group.com",
    "https://www.optivora-group.com",
    "https://api.optivora-group.com",
]

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

    'optivora',
    'directory',

    'django_celery_results',
    'django_celery_beat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # static ni prod’da beradi
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'restapp.middlewares.middlewares.RequestMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOWED_ORIGINS = [
    "https://optivora-group.com",
    "https://www.optivora-group.com",
    "https://api.optivora-group.com",
    "http://localhost:3000",
]

ROOT_URLCONF = 'optivoraback.urls'
WSGI_APPLICATION = 'optivoraback.wsgi.application'

# Hozircha sqlite (ishlaydi). Keyin MySQL/MariaDB ga o‘tasiz.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'UNICODE_JSON': True,
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'EXCEPTION_HANDLER': 'restapp.exceptions.custom_exception_handler',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=120),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=14),
    'BLACKLIST_AFTER_ROTATION': True,
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {'basic': {'type': 'basic'}}
}

LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'

LANGUAGES = (
    ('en', _('Ingliz')),
    ('uz', _('O‘zbek (Lotin)')),
    ('ru', _('Русский')),
)

TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGE_CODE = 'uz'

# === MUHIM: STATIC & MEDIA ===
STATIC_URL = '/static/'  # boshida slash BO‘LSIN!
STATIC_ROOT = "/home/host1836067/api.optivora-group.com/htdocs/www/static/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = '/assets/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

AUTH_USER_MODEL = 'users.User'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)
