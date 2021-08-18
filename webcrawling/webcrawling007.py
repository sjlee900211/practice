import requests

r = requests.get("https://www.google.co.kr")
r

r.text[0:100]