import urllib.request as req

# 파일 URL
img_url = "http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg"
html_url = "http://www.google.com"

# 다운받을 경로
save_path1 = "C:\\Users\\Celine\\practice\\webcrawling\\test1.jpg"
save_path2 = "C:\\Users\Celine\\practice\\webcrawling\\index.html"

# 예외처리
try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print("Download failed.")
    print(e)
else:
    # Header 정보 출력
    print(header1)
    print(header2)