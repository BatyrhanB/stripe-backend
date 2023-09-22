# Imports
import os
from pathlib import Path
from decouple import config
from django.utils.translation import gettext_lazy as _


BASE_DIR = Path(__file__).resolve().parent.parent.parent

DOCS_URL = config("DOCS_URL")

ADMIN_URL = config("ADMIN_URL")

PRODUCTION = config("PRODUCTION", default=False, cast=bool)

LOCAL_APPS = [
    "common.apps.CommonConfig",
    "item.apps.ItemConfig",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "corsheaders",
    "debug_toolbar",
    "drf_yasg",

]

THEME_APPS = [
    "jazzmin",
]


INSTALLED_APPS = [
    *THEME_APPS,
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

STRIPE_SECRET_KEY = config("STRIPE_API_KEY")
STRIPE_SUCCESS_URL = config("STRIPE_SUCCESS_URL")
STRIPE_CANCEL_URL = config("STRIPE_CANCEL_URL")

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"


TIME_ZONE = "Asia/Bishkek"
DATE_FORMAT = "%Y-%m-%d"
USE_TZ = True

LANGUAGE_CODE = "en-US"
USE_I18N = True
USE_L10N = True
LANGUAGES = (("en", _("English")),)

# Static files
STATIC_URL = "/back_static/"
STATIC_ROOT = os.path.join(BASE_DIR, "back_static")

# Media files
MEDIA_URL = "/back_media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "back_media")

X_FRAME_OPTIONS = "SAMEORIGIN"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 15,
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DATE_FORMAT": "%d.%m.%Y",
    "TIME_FORMAT": "%H:%M",
    "DEFAULT_RENDERER_CLASSES": (
        ["rest_framework.renderers.JSONRenderer"]
        if PRODUCTION
        else [
            "rest_framework.renderers.JSONRenderer",
            "rest_framework.renderers.BrowsableAPIRenderer",
        ]
    ),
}


AUTH_USER_MODEL = "auth.User"
AUTH_PASSWORD_VALIDATORS = [
    # {
    #     "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    # },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'pretty': {
            'format': '\033[1;36m{levelname}\033[0m \033[1;34m{asctime}\033[0m \033[1m{module}\033[0m {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'pretty',
            'level': 'INFO',
        },
        'error_file': {
            'class': 'logging.FileHandler',
            'filename': f"{BASE_DIR}/errors.log",
            'level': 'ERROR',
            'formatter': 'verbose',
        },
        'warning_file': {
            'class': 'logging.FileHandler',
            'filename': f"{BASE_DIR}/warnings.log",
            'level': 'WARNING',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console', 'error_file', 'warning_file'],
        'level': 'DEBUG',
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'error_file', 'warning_file'],
            'level': "DEBUG",
            'propagate': False,
        },
    },
}


from config.settings.cors import * # noqa
from config.settings.themes import * # noqa

if not PRODUCTION:
    from config.settings.dev import * # noqa
else:
    from config.settings.production import * # noqa


if DEBUG: # noqa
    import socket
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
