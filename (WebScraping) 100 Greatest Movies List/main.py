from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
emp_webpage = response.text

soup = BeautifulSoup(emp_webpage,"html.parser")

movie_titles = []
movies = soup.findAll(name="h3",class_="title")
for movie in movies:
  movie_name = movie.getText()
  movie_titles.append(movie_name)
movie_titles = movie_titles[::-1]

for movie_title in  movie_titles:
  print(movie_title)

