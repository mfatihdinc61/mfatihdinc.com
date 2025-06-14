import os
import sys

# Add your project directory to the Python path
path = '/home/seribbag/mfatihdinc.com/mysite'
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')  # Adjust 'mysite' to your actual project name

# This application object is used by the development server
# and any WSGI server configured to use this file
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
