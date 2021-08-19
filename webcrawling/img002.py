import requests
from bs4 import BeautifulSoup
import os

URL = 'https://reshot.com/search/animal'

html_reshot_image = requests.get(URL).text
soup_reshot_image = BeautifulSoup(html_reshot_image, "lxml")
reshot_image_elements = soup_reshot_image.select('a img')
reshot_image_elements[0:4]

reshot_image_url = reshot_image_elements[1].get('src')
reshot_image_url

html_image = requests.get(reshot_image_url)
folder = "C:/Users/Celine/practice/webcrawling"

# os.path.basename(URL)는 웹사이트나 폴더가 포함된 파일명에서 파일명만 분리하는 방법
imageFile = open(os.path.join(folder, os.path.basename(reshot_image_url)), 'wb')

# 이미지 데이터를 1000000 바이트씩 나눠서 저장하는 방법
chunk_size = 1000000
for chunk in html_image.iter_content(chunk_size):
    imageFile.write(chunk)
imageFile.close()