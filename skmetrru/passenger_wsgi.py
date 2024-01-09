"""
WSGI config for skmetrru project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os,sys
site_user_root_dir = '/home/s/skmetrlv/skmetrlv.beget.tech/public_html'
sys.path.insert(0, site_user_root_dir + '/skmetrru')
sys.path.insert(1, site_user_root_dir + '/venv/lib/python3.11/site-packages/')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skmetrru.settings')

application = get_wsgi_application()
