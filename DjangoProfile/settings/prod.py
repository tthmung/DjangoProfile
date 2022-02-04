from DjangoProfile.settings.base import *

# Override base.py settings here
DEBUG = False

ALLOWED_HOSTS = ["3.19.224.219", "tthmung.xyz", "www.tthmung.xyz", "localhost"]

# Production only

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': str(os.getenv("POST_PORJ")),
        'USER': str(os.getenv("POST_USER")),
        'PASSWORD': str(os.getenv("POST_PASS")),
        'HOST': 'localhost',
        'PORT': '',
    }
}

# HTTPS settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# HSTS settings
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
