import os

from unirawscp2eb.core.wsgi import get_wsgi_application

os.environ.setdefault('UNIRAWSCP2EB_SETTINGS_MODULE', 'unirawscp2eb.settings')

application = get_wsgi_application()
