import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Config:
    '''Set flask configuration from .env file.'''

    SECRET_KEY = os.environ.get('SECRET_KEY')