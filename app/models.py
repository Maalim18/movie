from . import db
from datetime import datetime
class Movie:
    '''
    Movie class to define Movie Objects
    '''
    def __init__(self,id,title,overview,poster,vote_average,vote_count, release_date):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count
        self.release_date= release_date


class Genres:
    def __init__(self,id,name):
        self.id = id
        self.name = name    
class Trailer:
    def __init__(self,key):
        
        self.key=key   
     