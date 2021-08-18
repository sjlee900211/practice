import webbrowser

naver_search_url = "http://search.naver.com/search.naver?query="
search_word = '파이썬'
url = naver_search_url + search_word

webbrowser.open_new(url)