from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['martoz.pythonanywhere.com']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# Static y Media files
STATIC_ROOT = '/home/Martoz/NewPortfolio/staticfiles'
MEDIA_ROOT = '/home/Martoz/NewPortfolio/media'

# ... rest of the code ...