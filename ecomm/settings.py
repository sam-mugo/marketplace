# from datetime import timedelta
from pathlib import Path
# import os
# from telnetlib import AUTHENTICATION
import django_heroku
import cloudinary
import cloudinary.uploader
import cloudinary.api
import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!scp9ls%hj6zqx1zy=9ybn*b=#mhdt_fvu5m=0zk6385=gf+nq'

AUTH_USER_MODEL = 'accounts.User'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# heroku config:set DEBUG_VALUE="False"

ALLOWED_HOSTS = ['*', 'farmers-marketsite.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'accounts',
    'corsheaders',
    'django_filters',
    'django_daraja',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'catalog',
    'apis',
    'cloudinary',
    'order',
    'payments',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware', 
]

MIDDLEWARE += ['whitenoise.middleware.WhiteNoseMiddleware']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':
    ('rest_framework_simplejwt.authentication.JWTAuthentication',),
    'DEFAULT_PERMISSION_CLASSES':
    ('rest_framework.permissions.AllowAny',),
    'DEFAULT_SCHEMA_CLASS': 
    ('drf_spectacular.openapi.AutoSchema',),
    
    
    # 'DEFAULT_FILTER_BACKENDS':
    # ('django_filters.rest_framework.DjangoFiltersBackend',),
}

SIMPLE_JWT = {
    'AUTH_HEADERS_TYPES': ('JWT', 'Bearer'),
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Farmers Marketplace',
    'DESCRIPTION': 'Ecommerce API documentation',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    # OTHER SETTINGS
}

SIMPLE_JWT = {
    'AUTH_HEADERS_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
}

# DJOSER = {
#     'LOGIN_FIELD': 'email',
#     'SOCIAL_AUTH_TOKEN_STRATEGY': 'djoser.social.token.jwt.TokenStrategy',
#     'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': ['http://127.0.0.1:3000', 'http://127.0.0.1:3000/home/', 'http://127.0.0.1:3000/accounts/login']
# }

AUTHENTICATION_BACKENDS = {
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend'
}

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '863847179001-n19054vvrr0l3tuk0mdks41va26lqd3g.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
#     'https://www.googleapis.com/auth/userinfo.email',
#     'https://www.googleapis.com/auth/userinfo.profile',
#     'openid'
# ]

# SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ['first_name', 'last_name']



# CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
"http://localhost:3000",
"http://127.0.0.1:3000",
)
# CORS_ORIGIN_WHITELIST = [
#     "http://localhost:3000",
#     "http://127.0.0.1:8000",
# ]

# CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'ecomm.urls'

cloudinary.config( 
  cloud_name = "", 
  api_key = "", 
  api_secret = "" 
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'social_django.context_processors.backends',
                # 'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecomm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# VENV_PATH = os.path.dirname(BASE_DIR)
# STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# MEDIA_URL = '/media/'

STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

django_heroku.settings(locals())

# django_heroku.settings(locals())
# The Mpesa environment to use
# Possible values: sandbox, production

MPESA_ENVIRONMENT = 'sandbox'

# Credentials for the daraja app

MPESA_CONSUMER_KEY = ''
MPESA_CONSUMER_SECRET = ''

#Shortcode to use for transactions. For sandbox  use the Shortcode 1 provided on test credentials page

MPESA_SHORTCODE = '1'

# Shortcode to use for Lipa na MPESA Online (MPESA Express) transactions
# This is only used on sandbox, do not set this variable in production
# For sandbox use the Lipa na MPESA Online Shorcode provided on test credentials page

MPESA_EXPRESS_SHORTCODE = ''

# Type of shortcode
# Possible values:
# - paybill (For Paybill)
# - till_number (For Buy Goods Till Number)

MPESA_SHORTCODE_TYPE = ''
LNM_PHONE_NUMBER = ''
# Lipa na MPESA Online passkey
# Sandbox passkey is available on test credentials page
# Production passkey is sent via email once you go live

MPESA_PASSKEY = ''

# Username for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)

MPESA_INITIATOR_USERNAME = 'Farmers MarketPlace'

# Plaintext password for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)

MPESA_INITIATOR_SECURITY_CREDENTIAL = ''