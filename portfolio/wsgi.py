"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

application = get_wsgi_application()
