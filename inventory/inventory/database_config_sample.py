## Here is the sample to configure the database

"""
    def configure_database():
        DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.postgresql',
               'NAME': 'inventory',
               'USER': 'chron',
               'PASSWORD': 'qwerty',
               'HOST': 'localhost',
               'PORT': '5433',
           }
        }
        return DATABASES
"""

## Add this file to database_config
## And make sure its imported in settings.py
