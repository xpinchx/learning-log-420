"""
WSGI config for learning_log project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling
# from whitenoise import WhiteNoise



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")
application = Cling(get_wsgi_application())
# application = WhiteNoise(application, root='/learning_log/learning_log/static')
# application.add_files('/learning_log/learning_log/static', prefix='more-files/')