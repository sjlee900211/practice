import requests
from bs4 import BeautifulSoup

url = "https://www.alexa.com/topsites/countries/KR"

html_website_ranking = requests.get(url).text
soup_website_ranking = BeautifulSoup(html_website_ranking, "lxml")

# p태그 요소 안에서 a 태그 요소를 찾음
website_ranking = soup_website_ranking.select('p a')

# website_ranking[0:7]

# website_ranking[1].get_text()

website_ranking_address = [website_ranking_element.get_text() for website_ranking_element in website_ranking[1:]]

# website_ranking_address[0:6]
print("[Top Sites in South Korea]")
for k in range(6):
    print("{0}: {1}".format(k+1, website_ranking_address[k]))