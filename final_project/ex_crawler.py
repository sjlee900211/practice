from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

baseurl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
search = input('searching keyword:')
url = baseurl + quote_plus(search)
# url = baseurl + quote_plus('집밥이미지')

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all(class_='_image _listImage')

print(img)

n = 1
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open('./food_img/' + search + str(n)+'.jpg', 'wb') as l:
            img = f.read()
            l.write(img)
    n += 1
    print(imgUrl)
    
print('done!')