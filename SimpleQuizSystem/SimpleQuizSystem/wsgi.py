"""full form wsgi-webserver gateway interface
explaination-this file is used we are deploy our application in production server
WSGI config for SimpleQuizSystem project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SimpleQuizSystem.settings')

application = get_wsgi_application()
