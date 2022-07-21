from pathlib import Path
from tkinter.tix import Tree
from decouple import config, Csv
from cryptography.fernet import Fernet
import os


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-y7^!=kd+=uu92oeomhku!0-@+b4%efav(ff0y8xe&7+tbo$o&^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'registration',            
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'ckeditor',
    'dashboard',
    'web',
    'main',
    'users',
    'products',
    'customers',
    'mptt',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eqbay.urls'

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
                'main.context_processors.main_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'eqbay.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

PASSWORD_ENCRYPTION_KEY = Fernet.generate_key()


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOGIN_URL = '/app/accounts/login/'
LOGOUT_URL = '/app/accounts/logout/'
LOGIN_REDIRECT_URL = '/app/'
LOGOUT_REDIRECT_URL = '/app/accounts/login/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_URL = '/static/'
STATICFILES_DIRS = (BASE_DIR / 'static',)
STATIC_ROOT = (BASE_DIR / 'static'/ 'static')


#DJANGO REGISTRATION REDUX SETTINGS
REGISTRATION_OPEN = True
REGISTRATION_FORM = 'customers.form.RegistrationForm'
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
SITE_ID=5
ACCOUNT_AUTHENTICATED_REGISTRATION_REDIRECTS = True



EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ambrodeveloper@gmail.com'
EMAIL_HOST_PASSWORD = 'sactdbsqrfknzwsx'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'