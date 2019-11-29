from .common import * # noqa


DEBUG = False

SECRET_KEY = '{{ dj_secret_key }}'
YOUTUBE_API_KEY = '{{ dj_youtube_secret_key }}'

ALLOWED_HOSTS = ['*']
SITE_HOST = 'cisco.haltode.fr'

STATIC_ROOT = '{{ dj_static_dir }}'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cisco',
    }
}
