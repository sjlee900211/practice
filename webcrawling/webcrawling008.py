import requests

html = requests.get("https://www.google.co.kr").text
html[0:100]