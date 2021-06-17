import os

class Config:
    '''
    General configuration parent class
    '''
    MOVIE_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    GENRES_URL ='https://api.themoviedb.org/3/genre/movie/list?api_key={}'
    GENRE_MOVIES_URL = 'https://api.themoviedb.org/3/discover/movie?api_key={}&with_genres={}'
    YOUTUBE_URL = 'http://api.themoviedb.org/3/movie/{}/videos?api_key={}'
    
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
  
