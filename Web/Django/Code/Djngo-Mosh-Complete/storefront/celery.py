import os
from celery import Celery

# we are setting the environment variable 'DJANGO_SETTINGS_MODULE' to storefront dot settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings.dev')

celery = Celery('storefront')
# where celery can find th configuration variables
# we are going to go in this module: 'django.conf', and load the 'settings' object
# namespace='CELERY': if we set this to celery, that means all our configuration settings to start with celery
# settings ---> CELERY_BROKER_URL = 'redis://local:6379/1', /1: is the name of the database
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()
