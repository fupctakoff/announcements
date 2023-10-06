import os
from dotenv import load_dotenv

load_dotenv()

USERMANAGER_SECRET = os.environ.get('USERMANAGER_SECRET')
JWT_SECRET = os.environ.get('JWT_SECRET')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
