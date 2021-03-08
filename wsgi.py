import logging
import sys
print(sys.path)
import pymongo
sys.stdout=sys.stderr
print("wsgi started")
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/cpxroot/skan/api/platform/app')
from main import app as application
application.root_path = '/home/cpxroot/skan/api/platform/app'
application.secret_key = '$S1kan@app'

