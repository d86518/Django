"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
#
# application = get_wsgi_application()

# 部屬要做調整
import os
import sys
from django.core.wsgi import get_wsgi_application
from dj_static import Cling
sys.path.append(r"C:\Users\黃大祐\django\mysite")
sys.path.append(r"C:\Users\黃大祐\django\mysite\mysite")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
application = Cling(get_wsgi_application())
