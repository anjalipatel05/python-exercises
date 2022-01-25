import requests
from bs4 import BeautifulSoup

webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html', "html.parser")
soup = BeautifulSoup(webpage_response.content)


print(type(soup))