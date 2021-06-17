import urllib.request,json
from .models import Movie,Genres,Trailer

# Getting api key
api_key = None
# Getting the movie base url
base_url = None
genres_url = None
genre_movies_url = None
youtube_trailer_url=None
def configure_request(app):
    global api_key,base_url, genres_url,genre_movies_url,youtube_trailer_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_BASE_URL']
    genres_url = app.config['GENRES_URL']
    genre_movies_url = app.config['GENRE_MOVIES_URL']
    youtube_trailer_url=app.config['YOUTUBE_URL']
def get_movies(category):

    '''
    Function that gets the json response to our url request
    '''
    get_movies_url= base_url.format(category, api_key)
    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

    return movie_results


def get_movie(id):
    get_movie_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')
            release_date = movie_details_response.get('release_date')

            movie_object = Movie(id,title,overview,poster,vote_average,vote_count,release_date)

    return movie_object

    

def process_results(movie_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')
        release_date=movie_item.get('release_date')

        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count,release_date)
            movie_results.append(movie_object)

    return movie_results    

def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None

        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)


    return search_movie_results   


def youtube_trailer(id):
    get_youtube_trailer_url=youtube_trailer_url.formart(id, api_key)
    with urllib.request.urlopen(get_youtube_trailer_url)as url:
        get_youtube_trailer_data = url.read()
        get_youtube_trailer_response = json.loads(get_youtube_trailer_data)

        youtube_trailer_results = None

        if get_youtube_trailer_response['results']:
            youtube_trailer_list = get_youtube_trailer_response['results']
            youtube_trailer_results = process_trailer_results(youtube_trailer_list)

    return youtube_trailer_results    



def get_genres():
    get_genres_url = genres_url.format(api_key)
    with urllib.request.urlopen(get_genres_url) as url:
        get_genres_data = url.read()
        get_genres_response = json.loads(get_genres_data)
        genres_results = None
        if get_genres_response['genres']:
            genres_results_list = get_genres_response['genres']
            genres_results = process_genres_results(genres_results_list)
    return genres_results



def process_genres_results(genres_results_list):
    genres_results = []
    for genre_item in genres_results_list:
        id = genre_item.get('id')
        name = genre_item.get('name')
        genre_object = Genres(id,name)
        genres_results.append(genre_object)
    return genres_results

def get_genre_movies(id):
    get_genre_movies_url = genre_movies_url.format(api_key,id)
    with urllib.request.urlopen(get_genre_movies_url) as url:
        genre_movies_data = url.read()
        genre_movies_response = json.loads(genre_movies_data)
        genre_movies_results = None
        if genre_movies_response['results']:
            genre_movies_list = genre_movies_response['results']
            genre_movies_results = process_results(genre_movies_list)
    return genre_movies_results            