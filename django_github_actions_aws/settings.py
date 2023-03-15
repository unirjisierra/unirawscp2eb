import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wi=al1*#b$k)56&%cw+(^v6jms1v4&evk174y!w&u^f%1h8^pv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'unirawscp2eb.contrib.admin',
    'unirawscp2eb.contrib.auth',
    'unirawscp2eb.contrib.contenttypes',
    'unirawscp2eb.contrib.sessions',
    'unirawscp2eb.contrib.messages',
    'unirawscp2eb.contrib.staticfiles',

    # Developer apps
    'core',
]

MIDDLEWARE = [
    'unirawscp2eb.middleware.security.SecurityMiddleware',
    'unirawscp2eb.contrib.sessions.middleware.SessionMiddleware',
    'unirawscp2eb.middleware.common.CommonMiddleware',
    'unirawscp2eb.middleware.csrf.CsrfViewMiddleware',
    'unirawscp2eb.contrib.auth.middleware.AuthenticationMiddleware',
    'unirawscp2eb.contrib.messages.middleware.MessageMiddleware',
    'unirawscp2eb.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'unirawscp2eb.urls'

TEMPLATES = [
    {
        'BACKEND': 'unirawscp2eb.template.backends.unirawscp2eb.unirawscp2ebTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'unirawscp2eb.template.context_processors.debug',
                'unirawscp2eb.template.context_processors.request',
                'unirawscp2eb.contrib.auth.context_processors.auth',
                'unirawscp2eb.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'unirawscp2eb.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'unirawscp2eb.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'unirawscp2eb.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'unirawscp2eb.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'unirawscp2eb.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'unirawscp2eb.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
