from bs4 import BeautifulSoup

f = open('C:\\Users\\Celine\\practice\\webcrawling\\br_example_constitution.html', encoding='utf-8')

html_source = f.read()
f.close()

soup = BeautifulSoup(html_source, "lxml")

title = soup.find('p', {"id":"title"})
contents = soup.find_all('p', {"id":"content"})

print(title.get_text())
for content in contents:
    print(content.get_text())
    
html1 = '<p id="content">제1조 <br/>①대한민국은 민주공화국이다.<br/>②대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.</p>'
soup1 = BeautifulSoup(html1, "lxml")

print("==> 태그 p로 찾은 요소")
content1 = soup1.find('p',{"id":"content"})
print(content1)

br_content = content1.find("br")
print("==> 결과에서 태그 br로 찾은 요소:", br_content)

br_content.replace_with("\n")
print("==> 태그 br을 개행문자로 바꾼 결과")
print(content1)

soup2 = BeautifulSoup(html1, "lxml")
content2 = soup2.find('p',{"id":"content"})

br_contents = content2.find_all("br")
for br_content in br_contents:
    br_content.replace_with("\n")
print(content2)

def replace_newline(soup_html):
    br_to_newlines = soup_html.find_all("br")
    for br_to_newline in br_to_newlines:
        br_to_newline.replace_with("\n")
    return soup_html

soup2 = BeautifulSoup(html1, "lxml")
content2 = soup2.find('p', {"id":"content"})
content3 = replace_newline(content2)
print(content3.get_text())