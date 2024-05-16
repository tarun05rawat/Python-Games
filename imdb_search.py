
from imdb import IMDb
from inspect import getmembers, isfunction  



ia = IMDb()
# Search for a movie
movies = ia.search_movie('Barsaat')
for movie in movies:
    print(f'Movie: {movie["title"]} - Year: {movie.get("year", "Unknown")}')
