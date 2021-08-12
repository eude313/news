import os
from flask.config import Config

NEWS_API_SOURCE_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey=API_KEY={}'
ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}