from hellowebapp.settings import *

# everything below will override our standard settings:
# parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# set debug to False
DEBUG = False

# Static asset Configuration
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
