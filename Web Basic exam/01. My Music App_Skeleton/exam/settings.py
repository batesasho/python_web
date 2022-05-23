from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-l8i*n8xd0r8x4y&dnca8fppm-3z)+=z+37bt@awpuc$7ptv$3s'

DEBUG = True

ALLOWED_HOSTS = [
        '127.0.0.1',
        'localhost',
]

# Application definition

DJANGO_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
)

WEB_APP = (
        'exam.web',
)

INSTALLED_APPS = DJANGO_APPS + WEB_APP

MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'exam.urls'

TEMPLATES = [
        {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [BASE_DIR / 'templates']
                ,
                'APP_DIRS': True,
                'OPTIONS': {
                        'context_processors': [
                                'django.template.context_processors.debug',
                                'django.template.context_processors.request',
                                'django.contrib.auth.context_processors.auth',
                                'django.contrib.messages.context_processors.messages',
                        ],
                },
        },
]

WSGI_APPLICATION = 'exam.wsgi.application'



# DATABASES = {
#         'default': {
#                 'ENGINE': 'django.db.backends.sqlite3',
#                 'NAME': BASE_DIR / 'db.sqlite3',
#         }
# }

DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'expenses_tracker',
                'USER': 'postgres',
                'PASSWORD': '1123QwER',
                'HOST': '192.168.0.209',
                'PORT': '5432',
        }
}



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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




STATIC_URL = 'static/'
STATICFILES_DIRS = (
        BASE_DIR / 'static',
)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
