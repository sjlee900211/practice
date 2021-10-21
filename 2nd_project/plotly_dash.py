import dash
from dash import dcc as dcc
from dash import html, callback_context, Input, Output
import plotly.express as px
import pymongo
import pandas as pd
import datetime
from crawler import *  # crawler.py 


def plotlydash(app):
    # MongoDB 연결
    client = pymongo.MongoClient(host='mongodb://52.197.26.81', port=27017, username = 'admin', password = '1234')
    db = client['네이버']
    col = db["네이버주식정보"]

    # dash layout-----------------------------------------------------------
    app.layout = html.Center([ 
        html.Br(),
        html.H1('주식 현재가'),
        html.Br(),
        
        # 종목 선택 드롭다운----------
        html.Div([
            # 시장 선택
            html.Div(
                dcc.Dropdown( 
                    id="market", 
                    options=[{"label": x, "value": x} for x in ['KOSPI', 'KOSDAQ']], 
                    placeholder="Select a market",
                ), 
                style={'width':'50%',  'text-align':'center'}),

            # 회사 선택
            html.Div(
                dcc.Dropdown( 
                    id="company",
                    placeholder="Select a company"
                ),
                style={'width':'50%',  'text-align':'center'}), 
        ], style={"width":"80%", "display":"inline-flex"}),    
    

        # 크롤링 버튼----------------
        html.Div([
            html.Button(
                'Update', 
                id='crawling_button',
                title='실시간 데이터 가져오기', 
                n_clicks=0, 
                style={
                    'background-color':'#eee', 
                    'color':'#aaa',
                    'height': '36px',
                    'border':'1px solid #eee',
                    'border-radius': '8px',
                }
            ), 
            # 완료 메세지 출력
            html.Div(
                id='output-message', 
                style={'color':'#888', 'align-items': 'center', 'margin-left':'2px'}),  
        ], style={"width":"80%", "height":"50px", "display":"inline-flex", "align-items": "center"}),
        html.Br(),
        html.Br(),

        # 로딩 표시------------------
        html.Div(
            dcc.Loading(
                id="loading",
                children=[html.Div(id="loading-output")],#, style={'color':'#aaa', 'display':'flex', 'flex-direction':'row-reverse', 'vertical-align': 'top'})],
                type="circle")),

        html.Br(),

        # 그래프 그리기---------------
        html.Div(
            dcc.Graph(id="line"),
            style={"width":"90%"})
    ]) 


    # 그래프 함수-------------------------------------------------------------
    def draw_chart(company):
        df = pd.DataFrame()
        # 선택한 회사의 데이터를 dataframe으로 생성
        for data in col.find({'종목명':company}):
            df = df.append(data, ignore_index=True)
        # 그래프 그리기
        fig = px.line(df, x='시간', y='현재가', hover_data=['전일비', '등락률','액면가', '시가총액', '상장주식수', '외국인비율', '거래량', 'PER', 'ROE']) 
        fig.update_layout(
            title = company,
            yaxis={'tickformat':',d'}
        )
        return fig


    # 회사 선택--------------------------------------------------------------
    @app.callback(
        Output('company', 'options'),
        Input('market', 'value'))
    def get_company_options(selected_market):
        companies = []
        # 선택한 시장에 속한 회사 목록 생성
        for company in col.distinct("종목명", {'시장':selected_market}):
            companies.append(company)
        return [{'label': x, 'value': x} for x in companies]

    # 회사 목록 중 첫 번째 항목 자동 선택
    @app.callback(
        Output('company', 'value'),
        Input('company', 'options'))
    def get_company_values(companies):
        if companies:
            return companies[0]['value']


    # 크롤링 버튼, 그래프 그리기-----------------------------------------------
    @app.callback(
        Output("line", "figure"),
        Output("output-message", "children"),
        Output("loading-output", "children"),
        Input("company", "value"),
        Input("crawling_button", "n_clicks")) 
    def display_chart(selected_company, n_clicks):
        changed_id = [p['prop_id'] for p in callback_context.triggered][0]
        # 크롤링 버튼 누른 후 동작
        if 'crawling_button' in changed_id:
            crawling()  # 크롤링 시작
            now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
            if selected_company:  # 선택되어 있는 회사가 있으면 그래프 새로 그림         
                return draw_chart(selected_company), f'완료! {now}', None  # 그래프와 크롤링 완료 메세지 반환
            else:
                fig = px.line()  # 빈 그래프 생성
                return fig, f'\t완료! {now}', None
        
        # 초기 화면, 선택한 회사의 그래프 생성
        else:
            if selected_company:
                return draw_chart(selected_company), None, None
            else:
                fig = px.line()
                return fig, None, None
