from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.afi.com/afis-100-years-100-movies/")
movie_list = response.text
soup = BeautifulSoup(movie_list, "html.parser")
all_movies = soup.find_all(class_="q_title")

movies_title = [movie.getText() for movie in all_movies]

print(movies_title)