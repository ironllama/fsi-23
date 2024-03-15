import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.imdb.com/chart/top/', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# Use bs4 with CSS selectors to get specific content from the HTML
movies = soup.select('li.ipc-metadata-list-summary-item')

# Looping through the movies -- Top 10
for movie in movies[:10]:
  # First, let's get the title of the movie
  movie_title = movie.select_one('.ipc-title__text').text
  print(movie_title)
