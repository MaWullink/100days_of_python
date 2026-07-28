from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

movies = soup.find_all("h3", class_="title")

movie_titles = [movie.get_text() for movie in movies][::-1]

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")

