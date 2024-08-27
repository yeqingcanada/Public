import os
from celery import Celery

# we are setting the environment variable 'DJANGO_SETTINGS_MODULE' to storefront dot settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings')

celery = Celery('storefront')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()
