#!/usr/bin/env bash
from flask import Flask, render_template, redirect, url_for, request
from dash import Dash
from flask.helpers import flash
from plotly_dash import *
import pickle

# Flask app전역객체로 사용가능하게 선언(인스턴스 생성)
app = Flask(__name__) # 단일 모듈의 형태

# plotly_dash 코드 쪽 앱 생성 후 app 인스턴스 생성
dash_app = Dash(__name__, server=app, url_base_pathname='/dash/')
plotlydash(dash_app)

# db_backup app 인스턴스 생성
@app.route('/db_backup')
def db_backup(): 
    exec(open("db_backup.py", encoding='UTF-8').read())
    return redirect(url_for('done', title = 'MongoDB 백업'))

# 첫 화면
@app.route('/') 

#  home화면
@app.route('/home')
def home():
    return render_template("stock.html")

# 크롤링, 디비백업 완료 후 완료표시용 화면
@app.route('/done')
def done():
    title = request.args.get("title", "구동")
    now = datetime.datetime.now()
    return render_template("done.html", current_time = now, title=title)

# 웹크롤링 실행 호출
@app.route('/crawling') 
def start_crawling():
    crawling()
    return redirect(url_for('done', title = '크롤링'))

# # 쿼리조회용 페이지 이동
# @app.route('/query_page')
# def query_page():
#     return render_template("query.html")

# @app.route('/query', methods=['GET', 'POST'])
# def query():
#     doc = db.col.find()
#     # querys = db.col
#     query = ''
#     if query is None:
#         query = request.form.get('query')
#     # query = querys.find_all({'query'})
    
#     return redirect(url_for('query_page', query=query))    
    
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