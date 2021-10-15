import dash
from dash import dcc as dcc
from dash import html, callback_context, Input, Output
import plotly.express as px
import pymongo
import pandas as pd
import datetime
from plotly_webcrawling import *


# client = pymongo.MongoClient("mongodb+srv://testdb:multi@cluster0.jxvfb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
client = pymongo.MongoClient(host='mongodb://52.197.26.81', port=27017, username = 'admin', password = '1234')

db = client['네이버']
col = db["네이버주식정보"]

def draw_chart(company):
    df = pd.DataFrame()
    for data in col.find({'종목명':company}):
        df = df.append(data, ignore_index=True)
    fig = px.line(df, x='시간', y='현재가', hover_data=['전일비', '등락률'], markers=True) 
    fig.update_layout(
        title = company,
        yaxis={'tickformat':',d'}
    )
    return fig


app = dash.Dash(__name__)

app.layout = html.Div([ 
    html.Br(),
    html.H2('주식 현재가'), 
    html.Button('실시간 데이터 가져오기', id='crawling_button', n_clicks=0),
    html.Span(),html.Span(),html.Span(),
    html.Span(id='output'),
    html.Br(), html.Br(),
    
    # 시장 선택
    html.Div(
    dcc.Dropdown( 
        id="market", 
        options=[{"label": x, "value": x} for x in ['KOSPI', 'KOSDAQ']], 
        #value='KOSPI',
        #clearable=True,
        placeholder="Select a market",
        style=dict(
            width='500px'
        )
    )),

    # 회사 선택
    html.Div(
    dcc.Dropdown( 
        id="company",
        placeholder="Select a company",
        style=dict(
            width='500px'
        )
    )),
    html.Br(),
    dcc.Graph(id="line"),  # 그래프 그리기
    html.Br()
    # dash_table.DataTable( 
    #     id='df-stack-table', 
    #     columns=[{"name": i, "id": i} for i in df.head().columns], 
    #     data=df.head(15).to_dict('records'),) 
            
]) 



# 회사 선택
@app.callback(
	Output('company', 'options'),
	Input('market', 'value'))
def get_company_options(selected_market):
    companies = []
    for i in col.find({'시장':selected_market}):
        companies.append(i.get('종목명'))
    companies =list(set(companies))  # 중복 제거
    companies.sort()
    return [{'label': x, 'value': x} for x in companies]

@app.callback(
    Output('company', 'value'),
    Input('company', 'options'))
def get_company_values(companies):
    if companies:
        return companies[0]['value']



# 크롤링 버튼, 그래프 그리기
@app.callback(
    Output("line", "figure"),
    Output("output", "children"),
    Input("company", "value"),
    Input("crawling_button", "n_clicks")) 
def display_chart(selected_company, n_clicks):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    if 'button' in changed_id:
        crawling()
        now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
        if selected_company:            
            return draw_chart(selected_company), f'\t완료! {now}'
        else:
            fig = px.line()
            return fig, f'\t완료! {now}'
    else:
        if selected_company:            
            return draw_chart(selected_company), None
        else:
            fig = px.line()
            return fig, None


app.run_server(host='0.0.0.0', port=8000,debug=True)