from flask import Flask, render_template
import runpy
from dash import Dash
from plotly_dash import *

# Flask app전역객체로 사용가능하게 선언(인스턴스 생성)
app = Flask(__name__) # 단일 모듈의 형태

# plotly_dash 코드 쪽 앱 생성 후 app 인스턴스 생성
dash_app = Dash(__name__, server=app, url_base_pathname='/dash/')
plotlydash(dash_app)
 
#  home화면
@app.route('/')
def home():
    return render_template("stock.html")

# 크롤링 완료 후 완료표시용 화면(아직 미구현상태)
@app.route('/done')
def done():
    return render_template("done.html")

# 웹크롤링 실행 호출(runpy 모듈 사용)
@app.route('/crawling') 
def start_crawling():
    try:
        file_globals = runpy.run_path('stock_webcrawling.py')
    except SystemExit:
        pass
    
# 삼성전자 시각화 대시보드 호출용 url
@app.route('/insight001') # 호출시 해당 url로 할당
def insight001():
    return render_template("insight001.html") # 해당 시각화 html파일은 templates 폴더 안에 있어야 호출이 가능함

# LG화학 시각화 대시보드 호출용 url
@app.route('/insight002') 
def insight002():
    return render_template("insight002.html")

# 카카오 시각화 대시보드 호출용 url
@app.route('/insight003')
def insight003():
    return render_template("insight003.html")

# 하이닉스 시각화 대시보드 호출용 url
@app.route('/insight004')
def insight004():
    return render_template("insight004.html")

# 셀트리온 시각화 대시보드 호출용 url
@app.route('/insight005')
def insight005():
    return render_template("insight005.html")
 
# Flask app 구동(host와 포트 지정을 하지 않을 경우 127.0.0.1:5000으로 할당됨)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000, debug=True) #모든 외부에서 접속 가능하게 0.0.0.0으로 host 할당 및 디버깅 가능하게 설정