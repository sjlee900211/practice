import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.alexa.com/topsites/countries/KR"

html_website_ranking = requests.get(url).text
soup_website_ranking = BeautifulSoup(html_website_ranking, "lxml")

# p태그 요소 안에서 a 태그 요소를 찾음
website_ranking = soup_website_ranking.select('p a')

website_ranking_address = [website_ranking_element.get_text() for website_ranking_element in website_ranking[1:]]

website_ranking_dict = {'Website': website_ranking_address}
df = pd.DataFrame(website_ranking_dict, columns=['Website'], index=range(1, len(website_ranking_address)+1))
df[0:6]