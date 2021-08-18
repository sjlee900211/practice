from bs4 import BeautifulSoup

html2 = """
<html>
 <head>
  <title>작품과 작가 모음</title>
 </head>
 <body>
  <h1>책 정보</h1>
  <p id="book_title">토지</p>
  <p id="author">박경리</p>
  
  <p id="book_title">태백산맥</p>
  <p id="author">조정래</p>

  <p id="book_title">감옥으로부터의 사색</p>
  <p id="author">신영복</p>
 </body>
</html>
"""

soup2 = BeautifulSoup(html2, "lxml")

soup2.title

soup2.body

soup2.body.h1

soup2.find_all('p')

soup2.find('p', {"id":"book_title"})

soup2.find('p', {"id":"author"})

soup2.find_all('p', {"id":"author"})

book_titles = soup2.find_all('p', {"id":"book_title"})
authors = soup2.find_all('p',{"id":"author"})

for book_title, author in zip(book_titles, authors):
    print(book_title.get_text() + '/' + author.get_text())