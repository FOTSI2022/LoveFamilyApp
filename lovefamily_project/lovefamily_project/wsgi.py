"""
WSGI config for lovefamily_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

from whitenoise.django import DjangoWhiteNoise

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lovefamily_project.settings')

application = get_wsgi_application()


application = DjangoWhiteNoise(application)
