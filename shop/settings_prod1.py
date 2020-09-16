DEBUG = False
ALLOWED_HOSTS = ['*']

#settings for db on server
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tango_shop_db',
        'USER': 'tango_db_u',
        'PASSWORD': 'VjqYjdsqGfhjkm2020',
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
}