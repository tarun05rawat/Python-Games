import requests
import json

url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"
headers = {
    "accept": "application/json",
    "Authorization": #YOUR AUTHORIZATION BEARER
}

response = requests.get(url=url,headers=headers)
top_rated_movies = response.text
movie_details = json.loads(top_rated_movies)
movie_info_list = movie_details["results"]

movie_titles_list = [movie_dict["title"] for movie_dict in movie_info_list]








