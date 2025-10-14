# passenger_wsgi.py
import os, sys

PROJECT_ROOT = "/home/host1836067/api.optivora-group.com/htdocs/www"
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
