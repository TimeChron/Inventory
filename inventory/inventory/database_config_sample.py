## This File is to keep database config
# Add the required configurations here

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
