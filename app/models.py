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

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer,primary_key = True)
    movie_id = db.Column(db.Integer)
    movie_title = db.Column(db.String)
    image_path = db.Column(db.String)
    movie_review = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    all_reviews = []
    
    def save_review(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()
    @classmethod
    def get_reviews(cls,id):
        reviews = Review.query.filter_by(movie_id=id).all()
        return reviews

class Genres:
    def __init__(self,id,name):
        self.id = id
        self.name = name    
class Trailer:
    def __init__(self,key):
        
        self.key=key   
     