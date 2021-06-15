import os

class Config:
    '''
    General configuration parent class
    '''
    MOVIE_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
   
    pass
class ProdConfig(Config):
    '''
    Production configuration 

    Args:
    Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args: 
    Config The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:josie@localhost/watchlist'
    DEBUG = True

class TestConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:josie@localhost/watchlist'



config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
  
