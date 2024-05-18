"""
WSGI config for diagxpert project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Установите переменную окружения DJANGO_SETTINGS_MODULE в ваш файл settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diagxpert.settings')

# Получение экземпляра приложения WSGI для вашего проекта Django
application = get_wsgi_application()
