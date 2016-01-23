import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = '@)#)^e@-66*e9+m#srm)c3)0)4*o)y=#0@$wt6wis6wt@glx2@'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'mondo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static')

MONDO_AUTH_URL = 'https://staging-auth.getmondo.co.uk'
MONDO_API_URL = 'https://staging-api.getmondo.co.uk'
MONDO_CLIENT_ID = 'oauthclient_000094RmbmkvjhMwyzx0Gf'
MONDO_CLIENT_SECRET = 'aZ/XRhXQrAhAbzuHUIQi3HIoDi8mlKxa9htThSi0vGKChNS3WFLwQC7AdvHtFO6tgGTGY3VaTsfecD2hG+tE'
MONDO_REDIRECT_URL = 'http://localhost:8000/mondo/authorize/'
