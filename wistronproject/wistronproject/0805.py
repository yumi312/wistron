
# import pymysql
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

import datetime
# external_stylesheets = ['Dash.css']

labor_colors = {
    'background': '#F5FDFF',
}

colors = {
    'background': '#FFF3F5',
    # 'background': '#FFF9F9',

}

# Step 1. 啟動應用程序
app = dash.Dash(__name__, external_stylesheets=[
                dbc.themes.BOOTSTRAP, 'project.css'], external_scripts=['0803.js'],)

st_gender_year = pd.read_csv('gender_year_data.csv')
st_gender_month = pd.read_csv('gender_month_data_02.csv')
st_labor_year = pd.read_csv('work_year_data.csv')
st_labor_month = pd.read_csv('work_month_data.csv')

app.layout = html.Div(children=[
    html.Div(children=[
        html.Button(children='人資永續', id='mainbutton', type="button"),
        html.Nav(className='navbar navbar-expand-lg navbar-light navbar-default',
                 style={'margin-left': "63%"}, children=[
                     html.Ul(className='nav navbar-nav navbar-right', children=[
                         html.Button(children='勞工關係',
                                     id='Labor', type="button"),
                         html.Button(children='多元共融',
                                     id='Diversity', type="button"),
                         html.Button(
                             children='薪資福利', type="button"),
                         html.Button(
                             children='健康安全', type="button"),
                     ]),
                 ]),
    ]),
    # 總覽
    html.Div(id='main', children=[
        html.Div(className='row', children=[
            html.Div([html.Img(src=app.get_asset_url(
                '人資永續logo.png'),  height='140', width='1100')], style={'margin': '32px 200px 0 200px '}),
            html.Video(autoPlay=True, controls=True, loop=True, children=[
                html.Source(src=app.get_asset_url('Comp.mp4')),
            ], style={'width': '1400px', 'margin': '-90px 50px', 'z-index': '-1'}),
        ]),
    ]),

    # 多元共融
    html.Div(id='DiversityInclusion', children=[
        html.Div(className='row', children=[
            html.Div([html.Img(src=app.get_asset_url(
                '多元共融logo.png'),  height='260', width='1400')], style={'margin': '32px 50px'}),
        ]),

        # 多元共融年現況
        # 多年現一
        html.Div(id='Diversitynowyear', children=[
            html.Div(className='row', children=[
                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='新進員工性別比', style={
                               'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='1.87', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#E73A5F'},),
                            html.P(children=' ➚', style={
                                   'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='61.90%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'width': '470px'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='新男員工人數', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='1,443', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#E73A5F'}),
                            html.P(children='➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='6.81%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'width': '470px'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='新女員工人數', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='773', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#E73A5F'}),
                            html.P(children='➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='11.86%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'width': '470px'}),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多年現二
            html.Div(className='row', children=[
                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='離職員工性別比', style={
                               'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='0.84', style={
                                'font-size': '60px', 'font-family': '字體'},),
                            html.P(children='➘', style={
                                   'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                            html.P(children='13.40%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'width': '470px'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='男員工離職率', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='15.58%', style={
                                'font-size': '60px', 'font-family': '字體', }),
                            html.P(children='➘', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                            html.P(children='9.41%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'width': '470px'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='女員工離職率', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='18.63%', style={
                                'font-size': '60px', 'font-family': '字體', }),
                            html.P(children='➘', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                            html.P(children='26.31%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'width': '470px'}),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多年現三
            html.Div(className='row', children=[
                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='留任員工性別比', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='1', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#E73A5F'}),
                            html.P(children='➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='0.99%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'width': '470px'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='男員工留任率', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='86.73%', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#E73A5F'},),
                            html.P(children='➚', style={
                                   'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='2.57%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'width': '470px'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='女員工留任率', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='86.70%', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#E73A5F'}),
                            html.P(children='➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='3.56%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'width': '470px'}),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多年現四
            html.Div(className='row', children=[
                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='每日工時(男)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='9.29', style={
                                'font-size': '60px', 'font-family': '字體', }),
                            html.P(children='➘', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px', 'visibility': 'hidden'}),
                            html.P(children='123', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px', 'visibility': 'hidden'})
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'background': '#FFEAEE'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='每日工時(女)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='8.89', style={
                                'font-size': '60px', 'font-family': '字體'},),
                            html.P(children='➘', style={
                                   'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px', 'visibility': 'hidden'}),
                            html.P(children='123', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px', 'visibility': 'hidden'})
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#FFEAEE'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='年均月加班時數(男)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='12.16/人', style={
                                'font-size': '60px', 'font-family': '字體', }),
                            html.P(children='➘', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                            html.P(children='4.29%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#FFEAEE'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='年均月加班時數(女)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='6.32/人', style={
                                'font-size': '60px', 'font-family': '字體', }),
                            html.P(children='➘', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                            html.P(children='10.49%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#FFEAEE'}),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多年現五
            html.Div(className='row', children=[
                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='男員工晉升率', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='22.64%', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#E73A5F'}),
                            html.P(children='➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='0.67%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'background': '#FFEAEE'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='女員工晉升率', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='22.47%', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#E73A5F'},),
                            html.P(children='➚', style={
                                   'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='10.15%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#FFEAEE'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='主管性別比', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='24.94%', style={
                                'font-size': '60px', 'font-family': '字體', }),
                            html.P(children='➚', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px', 'visibility': 'hidden'}),
                            html.P(children='123', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px', 'visibility': 'hidden'})
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#FFEAEE'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='性別平均薪酬比(非管理職)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='1:1.087', style={
                                'font-size': '60px', 'font-family': '字體', }),
                            html.P(children='➚', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px', 'visibility': 'hidden'}),
                            html.P(children='123', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px', 'visibility': 'hidden'})
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#FFEAEE'}),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            html.P(children='-育嬰假統計-',
                   style={'font-size': '36px', 'font-family': '字體', 'margin-left': '40px'}),
            # 多年現六
            html.Div(className='row', children=[
                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='今年符合申請資格人數(男)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='515', style={
                                'font-size': '60px', 'font-family': '字體', }),
                            html.P(children='', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'})
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='今年實際申請人數(男)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='11', style={
                                'font-size': '60px', 'font-family': '字體'},),
                            html.P(children='', style={
                                   'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'})
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='今年申請率(男)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='2%', style={
                                'font-size': '60px', 'font-family': '字體', }),
                            html.P(children='', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                            html.P(children='', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'})
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='去年申請率(男)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='3%', style={
                                'font-size': '60px', 'font-family': '字體', }),
                            html.P(children='', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                            html.P(children='', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'})
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多年現七
            html.Div(className='row', children=[
                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                     html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='今年符合申請資格人數(女)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='208', style={
                                'font-size': '60px', 'font-family': '字體', }),
                         html.P(children='', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                         html.P(children='', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'})
                     ], style={'margin': 'auto'}),
                     ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                     html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='今年實際申請人數(女)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='29', style={
                                'font-size': '60px', 'font-family': '字體'},),
                         html.P(children='', style={
                             'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                         html.P(children='', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'})
                     ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='今年申請率(女)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='14%', style={
                                'font-size': '60px', 'font-family': '字體', }),
                         html.P(children='', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                         html.P(children='', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'})
                         ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='去年申請率(女)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='49%', style={
                                'font-size': '60px', 'font-family': '字體', }),
                         html.P(children='', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                         html.P(children='', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'})
                         ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多年現八
            html.Div(className='row', children=[
                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                     html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='今年預計復職人數(男)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='11', style={
                                'font-size': '60px', 'font-family': '字體', }),
                         html.P(children='', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                         html.P(children='', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'})
                     ], style={'margin': 'auto'}),
                     ], style={'padding': '20px'}),
                ], style={'background': '#FFEAEE'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='今年實際復職人數(男)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='4', style={
                                'font-size': '60px', 'font-family': '字體'},),
                         html.P(children='', style={
                             'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                         html.P(children='', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'})
                         ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#FFEAEE'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='今年復職率(男)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='36%', style={
                                'font-size': '60px', 'font-family': '字體', }),
                         html.P(children='', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                         html.P(children='', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'})
                         ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#FFEAEE'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='去年復職率(男)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='36%', style={
                                'font-size': '60px', 'font-family': '字體', }),
                         html.P(children='', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                         html.P(children='', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'})
                         ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#FFEAEE'}),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多年現九
            html.Div(className='row', children=[
                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                     html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='今年預計復職人數(女)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='47', style={
                                'font-size': '60px', 'font-family': '字體', }),
                         html.P(children='', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                         html.P(children='', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'})
                     ], style={'margin': 'auto'}),
                     ], style={'padding': '20px'}),
                ], style={'background': '#FFEAEE'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='今年實際復職人數(女)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='33', style={
                                'font-size': '60px', 'font-family': '字體'},),
                         html.P(children='', style={
                             'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                         html.P(children='', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'})
                         ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#FFEAEE'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='今年復職率(女)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='70%', style={
                                'font-size': '60px', 'font-family': '字體', }),
                         html.P(children='', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                         html.P(children='', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'})
                         ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#FFEAEE'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='去年復職率(女)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='86%', style={
                                'font-size': '60px', 'font-family': '字體', }),
                         html.P(children='', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                         html.P(children='', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'})
                         ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#FFEAEE'}),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多年現十
            html.Div(className='row', children=[
                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                     html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='去年實際復職人數(男)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='4', style={
                                'font-size': '60px', 'font-family': '字體', }),
                         html.P(children='123', style={
                             'font-size': '18px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px', 'line-height': '20px', 'visibility': 'hidden'})
                     ], style={'margin': 'auto'}),
                     ], style={'padding': '20px'}),
                ], style={'background': '#F8D6DC'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='去年實際復職且一年後仍在職人數(男)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='2', style={
                                'font-size': '60px', 'font-family': '字體'},),
                         ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#F8D6DC'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='今年留任率(男)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='50%', style={
                                'font-size': '60px', 'font-family': '字體', }),
                         html.P(children='123', style={
                             'font-size': '18px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px', 'line-height': '20px', 'visibility': 'hidden'})
                         ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#F8D6DC'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='去年留任率(男)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='100%', style={
                                'font-size': '60px', 'font-family': '字體', }),
                         html.P(children='123', style={
                             'font-size': '18px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px', 'line-height': '20px', 'visibility': 'hidden'})
                         ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#F8D6DC'}),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多年現十一
            html.Div(className='row', children=[
                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                     html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='去年實際復職人數(女)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='19', style={
                                'font-size': '60px', 'font-family': '字體', }),
                         html.P(children='123', style={
                             'font-size': '18px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px', 'line-height': '20px', 'visibility': 'hidden'})
                     ], style={'margin': 'auto'}),
                     ], style={'padding': '20px'}),
                ], style={'background': '#F8D6DC'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='去年實際復職且一年後仍在職人數(女)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='18', style={
                                'font-size': '60px', 'font-family': '字體'},),
                         ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#F8D6DC'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='今年留任率(女)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='95%', style={
                                'font-size': '60px', 'font-family': '字體', }),
                         html.P(children='123', style={
                             'font-size': '18px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px', 'line-height': '20px', 'visibility': 'hidden'})
                         ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#F8D6DC'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='去年留任率(女)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='62%', style={
                                'font-size': '60px', 'font-family': '字體', }),
                         html.P(children='123', style={
                             'font-size': '18px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px', 'line-height': '20px', 'visibility': 'hidden'})
                         ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#F8D6DC'}),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),
        ]),

        # 多元共融月現況
        # 多月現一
        html.Div(id='Diversitynowmonth', children=[
            html.Div(className='row', children=[
                    html.Div(className='col-3 d-inline-block h-50', children=[
                        html.Div(className='row', children=[
                            html.Div(className='col d-inline-block text-center', children=[
                                html.P(children='現員工性別比', style={
                                    'font-size': '24px', 'font-family': '字體'}),
                                html.P(children='2.23', style={
                                    'font-size': '60px', 'font-family': '字體', 'color': '#E73A5F'}),
                                html.P(children=' ➚', style={
                                    'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                                html.P(children='0.89%', style={
                                    'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                                html.P(children='MoM', style={
                                    'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                            ], style={'margin': 'auto'}),
                        ], style={'padding': '20px'}),
                    ], style={'width': '470px'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='現男員工人數', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='5,932', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#E73A5F'}),
                            html.P(children=' ➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='0.76%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block'}),
                            html.P(children='MoM', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'width': '470px'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='現女員工人數', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='2,666', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#E73A5F'}),
                            html.P(children=' ➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='1.76%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='MoM', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'width': '470px'}),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多月現二
            html.Div(className='row', children=[
                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='新員工性別比', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='1.5', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#E73A5F'}),
                            html.P(children=' ➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='26.83%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='MoM', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'width': '470px'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='新男員工人數', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='132', style={
                                'font-size': '60px', 'font-family': '字體', }),
                            html.P(children='➘', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                            html.P(children='20.48%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='MoM', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'width': '470px'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='新女員工人數', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='88', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#E73A5F'}),
                            html.P(children='➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='8.64%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='MoM', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'width': '470px'}),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多月現三
            html.Div(className='row', children=[
                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='離職員工性別比', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='0.93', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#E73A5F'}),
                            html.P(children=' ➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='20.78%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='MoM', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'width': '470px'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='男員工離職率', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='1.47%', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#E73A5F'}),
                            html.P(children='➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='14.04%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='MoM', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'width': '470px'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='女員工離職率', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='1.59%', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#E73A5F'}),
                            html.P(children='➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='28.38%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='MoM', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'width': '470px'}),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多月現四
            html.Div(className='row', children=[
                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='每日工時(男)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='9.14', style={
                                'font-size': '60px', 'font-family': '字體'}),
                            html.P(children='➘', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px', 'visibility': 'hidden'}),
                            html.P(children='123', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px', 'visibility': 'hidden'})
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'background': '#FFEAEE'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='每日工時(女)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='8.72', style={
                                'font-size': '60px', 'font-family': '字體', }),
                            html.P(children='➘', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px', 'visibility': 'hidden'}),
                            html.P(children='123', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px', 'visibility': 'hidden'})
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#FFEAEE'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='月加班時數(男)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='13.16/人', style={
                                'font-size': '60px', 'font-family': '字體'}),
                            html.P(children='➘', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                            html.P(children='17.82%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='MoM', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#FFEAEE'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='月加班時數(女)', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='6.83/人', style={
                                'font-size': '60px', 'font-family': '字體', }),
                            html.P(children='➘', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                            html.P(children='20.25%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='MoM', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#FFEAEE'}),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),
        ]),

        # 多元共融近三年
        # 多近三年一
        html.Div(id='Diversitythreey', children=[
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity-threey_1', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.threeyear, 'y': st_gender_year['new_grate'],
                                     'type': 'scatter', 'name': '新員工性別比', },
                                ],
                                'layout': {
                                    'title': '新員工性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity_threey_2', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.threeyear, 'y': st_gender_year['new_male'],
                                     'type': 'scatter', 'name': '新男員工人數', },
                                ],
                                'layout': {
                                    'title': '新男員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity_threey_3', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.threeyear, 'y': st_gender_year['new_female'],
                                     'type': 'scatter', 'name': '新女員工人數', },
                                ],
                                'layout': {
                                    'title': '新女員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近三年二
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threey_4', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.threeyear, 'y': st_gender_year['leave_grate'],
                                     'type': 'scatter', 'name': '離職員工性別比', },
                                ],
                                'layout': {
                                    'title': '離職員工性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threey_5', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.threeyear, 'y': st_gender_year['leave_male'],
                                     'type': 'scatter', 'name': '男員工離職率', },
                                ],
                                'layout': {
                                    'title': '男員工離職率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threey_6', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_year.threeyear, 'y': st_gender_year['leave_female'],
                                           'type': 'scatter', 'name': '女員工離職率', },
                                      ],
                                      'layout': {
                                          'title': '女員工離職率',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近三年三
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threey_7', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.threeyear, 'y': st_gender_year['still_grate'],
                                     'type': 'scatter', 'name': '留任員工性別比', },
                                ],
                                'layout': {
                                    'title': '留任員工性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threey_8', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.threeyear, 'y': st_gender_year['still_male'],
                                     'type': 'scatter', 'name': '男員工留任率', },
                                ],
                                'layout': {
                                    'title': '男員工留任率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threey_9', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_year.threeyear, 'y': st_gender_year['still_female'],
                                           'type': 'scatter', 'name': '女員工留任率', },
                                      ],
                                      'layout': {
                                          'title': '女員工留任率',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近三年四
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threey_10', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.threeyear, 'y': st_gender_year['avg_punch_male'],
                                     'type': 'scatter', 'name': '每日工時(男)', },
                                ],
                                'layout': {
                                    'title': '每日工時(男)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px', }),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threey_11', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.threeyear, 'y': st_gender_year['avg_ot_male'],
                                     'type': 'scatter', 'name': '年均月加班時數(男)', },
                                ],
                                'layout': {
                                    'title': '年均月加班時數(男)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px', }),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threey_12', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_year.threeyear, 'y': st_gender_year['grade_male'],
                                           'type': 'scatter', 'name': '男員工晉升率', },
                                      ],
                                      'layout': {
                                          'title': '男員工晉升率',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px', }),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近三年五
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threey_13', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.threeyear, 'y': st_gender_year['avg_punch_female'],
                                     'type': 'scatter', 'name': '每日工時(女)', },
                                ],
                                'layout': {
                                    'title': '每日工時(女)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threey_14', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.threeyear, 'y': st_gender_year['avg_ot_female'],
                                     'type': 'scatter', 'name': '年均月加班時數(女)', },
                                ],
                                'layout': {
                                    'title': '年均月加班時數(女)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threey_15', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_year.threeyear, 'y': st_gender_year['grade_female'],
                                           'type': 'scatter', 'name': '女員工晉升率', },
                                      ],
                                      'layout': {
                                          'title': '女員工晉升率',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近三年六
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threey_16', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.threeyear, 'y': st_gender_year['director_grate'],
                                     'type': 'scatter', 'name': '主管性別比', },
                                ],
                                'layout': {
                                    'title': '主管性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            html.P(children='-育嬰假統計-',
                   style={'font-size': '36px', 'font-family': '字體', 'margin-left': '40px'}),

            # 多近三年七
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threey_19', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.threeyear, 'y': st_gender_year['applicants_male'],
                                     'type': 'scatter', 'name': '申請人數(男)', },
                                ],
                                'layout': {
                                    'title': '申請人數(男)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threey_20', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.threeyear, 'y': st_gender_year['reins_male'],
                                     'type': 'scatter', 'name': '復職率(男)', },
                                ],
                                'layout': {
                                    'title': '復職率(男)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threey_21', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_year.threeyear, 'y': st_gender_year['sti_male'],
                                           'type': 'scatter', 'name': '留任率(男)', },
                                      ],
                                      'layout': {
                                          'title': '留任率(男)',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近三年八
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threey_22', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.threeyear, 'y': st_gender_year['applicants_female'],
                                     'type': 'scatter', 'name': '申請人數(女)', },
                                ],
                                'layout': {
                                    'title': '申請人數(女)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threey_23', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.threeyear, 'y': st_gender_year['reins_female'],
                                     'type': 'scatter', 'name': '復職率(女)', },
                                ],
                                'layout': {
                                    'title': '復職率(女)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threey_24', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_year.threeyear, 'y': st_gender_year['sti_female'],
                                           'type': 'scatter', 'name': '留任率(女)', },
                                      ],
                                      'layout': {
                                          'title': '留任率(女)',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),
        ]),

        # 多元共融近五年
        # 多近五年一
        html.Div(id='Diversityfivey', children=[
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity-fivey_1', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.fiveyear, 'y': st_gender_year['new_grate'],
                                     'type': 'scatter', 'name': '新員工性別比', },
                                ],
                                'layout': {
                                    'title': '新員工性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity_fivey_2', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.fiveyear, 'y': st_gender_year['new_male'],
                                     'type': 'scatter', 'name': '新男員工人數', },
                                ],
                                'layout': {
                                    'title': '新男員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity_fivey_3', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.fiveyear, 'y': st_gender_year['new_female'],
                                     'type': 'scatter', 'name': '新女員工人數', },
                                ],
                                'layout': {
                                    'title': '新女員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近五年二
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_fivey_4', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.fiveyear, 'y': st_gender_year['leave_grate'],
                                     'type': 'scatter', 'name': '離職員工性別比', },
                                ],
                                'layout': {
                                    'title': '離職員工性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_fivey_5', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.fiveyear, 'y': st_gender_year['leave_male'],
                                     'type': 'scatter', 'name': '男員工離職率', },
                                ],
                                'layout': {
                                    'title': '男員工離職率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_fivey_6', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_year.fiveyear, 'y': st_gender_year['leave_female'],
                                           'type': 'scatter', 'name': '女員工離職率', },
                                      ],
                                      'layout': {
                                          'title': '女員工離職率',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近五年三
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_fivey_7', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.fiveyear, 'y': st_gender_year['still_grate'],
                                     'type': 'scatter', 'name': '留任員工性別比', },
                                ],
                                'layout': {
                                    'title': '留任員工性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_fivey_8', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.fiveyear, 'y': st_gender_year['still_male'],
                                     'type': 'scatter', 'name': '男員工留任率', },
                                ],
                                'layout': {
                                    'title': '男員工留任率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_fivey_9', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_year.fiveyear, 'y': st_gender_year['still_female'],
                                           'type': 'scatter', 'name': '女員工留任率', },
                                      ],
                                      'layout': {
                                          'title': '女員工留任率',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近五年四
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_fivey_10', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.fiveyear, 'y': st_gender_year['avg_punch_male'],
                                     'type': 'scatter', 'name': '平均打卡時數(男)', },
                                ],
                                'layout': {
                                    'title': '平均打卡時數(男)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_fivey_11', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.fiveyear, 'y': st_gender_year['avg_ot_male'],
                                     'type': 'scatter', 'name': '年均月加班時數(男)', },
                                ],
                                'layout': {
                                    'title': '年均月加班時數(男)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_fivey_12', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_year.fiveyear, 'y': st_gender_year['grade_male'],
                                           'type': 'scatter', 'name': '男員工晉升率', },
                                      ],
                                      'layout': {
                                          'title': '男員工晉升率',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近五年五
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_fivey_13', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.fiveyear, 'y': st_gender_year['avg_punch_female'],
                                     'type': 'scatter', 'name': '平均打卡時數(女)', },
                                ],
                                'layout': {
                                    'title': '平均打卡時數(女)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_fivey_14', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.fiveyear, 'y': st_gender_year['avg_ot_female'],
                                     'type': 'scatter', 'name': '年均月加班時數(女)', },
                                ],
                                'layout': {
                                    'title': '年均月加班時數(女)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_fivey_15', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_year.fiveyear, 'y': st_gender_year['grade_female'],
                                           'type': 'scatter', 'name': '女員工晉升率', },
                                      ],
                                      'layout': {
                                          'title': '女員工晉升率',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近五年六
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_fivey_16', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.fiveyear, 'y': st_gender_year['director_grate'],
                                     'type': 'scatter', 'name': '主管性別比', },
                                ],
                                'layout': {
                                    'title': '主管性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                # html.Div(className='col-4 d-inline-block h-50', children=[
                #     html.Div(className='row', children=[
                #         html.Div(className='col d-inline-block text-center', children=[
                #             # html.P(children='專案人數', style={
                #             #     'font-size': '24px', 'font-family': '字體'}),
                #             dcc.Graph(id='diversity_fivey_17', style={'width': '430px', 'height': '320px'},
                #                       figure={
                #                 'data': [
                #                     {'x': st_gender_year.fiveyear, 'y': st_gender_year['avg_ot_female'],
                #                      'type': 'scatter', 'name': '平均薪酬比', },
                #                 ],
                #                 'layout': {
                #                     'title': '平均薪酬比',
                #                     'color': '#E73A5F',
                #                     'scatter_color': '#E73A5F',
                #                     'plot_bgcolor': colors['background'],
                #                     'paper_bgcolor': colors['background'],
                #                     'font': {'color': 'black', 'size': 16, 'family': '字體'},
                #                     # 'height': 10
                #                 }
                #             },
                #             ),
                #         ], style={'margin': 'auto'}),
                #     ], style={'padding': '20px'}),
                # ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            html.P(children='-育嬰假統計-',
                   style={'font-size': '36px', 'font-family': '字體', 'margin-left': '40px'}),

            # 多近五年七
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_fivey_19', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.fiveyear, 'y': st_gender_year['applicants_male'],
                                     'type': 'scatter', 'name': '申請人數(男)', },
                                ],
                                'layout': {
                                    'title': '申請人數(男)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_fivey_20', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.fiveyear, 'y': st_gender_year['reins_male'],
                                     'type': 'scatter', 'name': '復職率(男)', },
                                ],
                                'layout': {
                                    'title': '復職率(男)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_fivey_21', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_year.fiveyear, 'y': st_gender_year['sti_male'],
                                           'type': 'scatter', 'name': '留任率(男)', },
                                      ],
                                      'layout': {
                                          'title': '留任率(男)',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近五年八
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_fivey_22', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.fiveyear, 'y': st_gender_year['applicants_female'],
                                     'type': 'scatter', 'name': '申請人數(女)', },
                                ],
                                'layout': {
                                    'title': '申請人數(女)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_fivey_23', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.fiveyear, 'y': st_gender_year['reins_female'],
                                     'type': 'scatter', 'name': '復職率(女)', },
                                ],
                                'layout': {
                                    'title': '復職率(女)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_fivey_24', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_year.fiveyear, 'y': st_gender_year['sti_female'],
                                           'type': 'scatter', 'name': '留任率(女)', },
                                      ],
                                      'layout': {
                                          'title': '留任率(女)',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),
        ]),

        # 多元共融近十年
        # 多近十年一
        html.Div(id='Diversityteny', children=[
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity-teny_1', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.tenyear, 'y': st_gender_year['new_grate'],
                                     'type': 'scatter', 'name': '新員工性別比', },
                                ],
                                'layout': {
                                    'title': '新員工性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity_teny_2', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.tenyear, 'y': st_gender_year['new_male'],
                                     'type': 'scatter', 'name': '新男員工人數', },
                                ],
                                'layout': {
                                    'title': '新男員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity_teny_3', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.tenyear, 'y': st_gender_year['new_female'],
                                     'type': 'scatter', 'name': '新女員工人數', },
                                ],
                                'layout': {
                                    'title': '新女員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近十年二
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_teny_4', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.tenyear, 'y': st_gender_year['leave_grate'],
                                     'type': 'scatter', 'name': '離職員工性別比', },
                                ],
                                'layout': {
                                    'title': '離職員工性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_teny_5', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.tenyear, 'y': st_gender_year['leave_male'],
                                     'type': 'scatter', 'name': '男員工離職率', },
                                ],
                                'layout': {
                                    'title': '男員工離職率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_teny_6', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_year.tenyear, 'y': st_gender_year['leave_female'],
                                           'type': 'scatter', 'name': '女員工離職率', },
                                      ],
                                      'layout': {
                                          'title': '女員工離職率',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近五年三
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_teny_7', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.tenyear, 'y': st_gender_year['still_grate'],
                                     'type': 'scatter', 'name': '留任員工性別比', },
                                ],
                                'layout': {
                                    'title': '留任員工性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_teny_8', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.tenyear, 'y': st_gender_year['still_male'],
                                     'type': 'scatter', 'name': '男員工留任率', },
                                ],
                                'layout': {
                                    'title': '男員工留任率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_teny_9', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_year.tenyear, 'y': st_gender_year['still_female'],
                                           'type': 'scatter', 'name': '女員工留任率', },
                                      ],
                                      'layout': {
                                          'title': '女員工留任率',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近五年四
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_teny_10', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.tenyear, 'y': st_gender_year['avg_punch_male'],
                                     'type': 'scatter', 'name': '平均打卡時數(男)', },
                                ],
                                'layout': {
                                    'title': '平均打卡時數(男)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_teny_11', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.tenyear, 'y': st_gender_year['avg_ot_male'],
                                     'type': 'scatter', 'name': '年均月加班時數(男)', },
                                ],
                                'layout': {
                                    'title': '年均月加班時數(男)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_teny_12', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_year.tenyear, 'y': st_gender_year['grade_male'],
                                           'type': 'scatter', 'name': '男員工晉升率', },
                                      ],
                                      'layout': {
                                          'title': '男員工晉升率',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近五年五
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_teny_13', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.tenyear, 'y': st_gender_year['avg_punch_female'],
                                     'type': 'scatter', 'name': '平均打卡時數(女)', },
                                ],
                                'layout': {
                                    'title': '平均打卡時數(女)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_teny_14', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.tenyear, 'y': st_gender_year['avg_ot_female'],
                                     'type': 'scatter', 'name': '年均月加班時數(女)', },
                                ],
                                'layout': {
                                    'title': '年均月加班時數(女)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_teny_15', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_year.tenyear, 'y': st_gender_year['grade_female'],
                                           'type': 'scatter', 'name': '女員工晉升率', },
                                      ],
                                      'layout': {
                                          'title': '女員工晉升率',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近五年六
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_teny_16', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.tenyear, 'y': st_gender_year['director_grate'],
                                     'type': 'scatter', 'name': '主管性別比', },
                                ],
                                'layout': {
                                    'title': '主管性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            html.P(children='-育嬰假統計-',
                   style={'font-size': '36px', 'font-family': '字體', 'margin-left': '40px'}),

            # 多近五年七
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_teny_19', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.tenyear, 'y': st_gender_year['applicants_male'],
                                     'type': 'scatter', 'name': '申請人數(男)', },
                                ],
                                'layout': {
                                    'title': '申請人數(男)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_teny_20', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.tenyear, 'y': st_gender_year['reins_male'],
                                     'type': 'scatter', 'name': '復職率(男)', },
                                ],
                                'layout': {
                                    'title': '復職率(男)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_teny_21', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_year.tenyear, 'y': st_gender_year['sti_male'],
                                           'type': 'scatter', 'name': '留任率(男)', },
                                      ],
                                      'layout': {
                                          'title': '留任率(男)',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近五年八
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_teny_22', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.tenyear, 'y': st_gender_year['applicants_female'],
                                     'type': 'scatter', 'name': '申請人數(女)', },
                                ],
                                'layout': {
                                    'title': '申請人數(女)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_teny_23', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_year.tenyear, 'y': st_gender_year['reins_female'],
                                     'type': 'scatter', 'name': '復職率(女)', },
                                ],
                                'layout': {
                                    'title': '復職率(女)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_teny_24', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_year.tenyear, 'y': st_gender_year['sti_female'],
                                           'type': 'scatter', 'name': '留任率(女)', },
                                      ],
                                      'layout': {
                                          'title': '留任率(女)',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),
        ]),

        # 多元共融近三月
        # 多近三月一
        html.Div(id='Diversitythreem', children=[
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity-threem_1', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.threemonth, 'y': st_gender_month['now_em_grate'],
                                     'type': 'scatter', 'name': '現員工性別比', },
                                ],
                                'layout': {
                                    'title': '現員工性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[9, 10, 11], ticktext=['9', '10', '11'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity_threem_2', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.threemonth, 'y': st_gender_month['now_male'],
                                     'type': 'scatter', 'name': '現男員工人數', },
                                ],
                                'layout': {
                                    'title': '現男員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[9, 10, 11], ticktext=['9', '10', '11'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity_threem_3', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.threemonth, 'y': st_gender_month['now_female'],
                                     'type': 'scatter', 'name': '現女員工人數', },
                                ],
                                'layout': {
                                    'title': '現女員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[9, 10, 11], ticktext=['9', '10', '11'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近三月二
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threem_4', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.threemonth, 'y': st_gender_month['new_grate'],
                                     'type': 'scatter', 'name': '新員工性別比', },
                                ],
                                'layout': {
                                    'title': '新員工性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[9, 10, 11], ticktext=['9', '10', '11'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threem_5', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.threemonth, 'y': st_gender_month['new_male'],
                                     'type': 'scatter', 'name': '新男員工人數', },
                                ],
                                'layout': {
                                    'title': '新男員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[9, 10, 11], ticktext=['9', '10', '11'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity_threem_6', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_month.threemonth, 'y': st_gender_month['new_female'],
                                           'type': 'scatter', 'name': '新女員工人數', },
                                      ],
                                      'layout': {
                                          'title': '新女員工人數',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          'xaxis': dict(tickvals=[9, 10, 11], ticktext=['9', '10', '11'], tickmode='array'),
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近三月三
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threem_7', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.threemonth, 'y': st_gender_month['leave_grate'],
                                     'type': 'scatter', 'name': '離職員工性別比', },
                                ],
                                'layout': {
                                    'title': '離職員工性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[9, 10, 11], ticktext=['9', '10', '11'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threem_8', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.threemonth, 'y': st_gender_month['leave_male'],
                                     'type': 'scatter', 'name': '男員工離職率', },
                                ],
                                'layout': {
                                    'title': '男員工離職率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[9, 10, 11], ticktext=['9', '10', '11'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threem_9', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_month.threemonth, 'y': st_gender_month['leave_female'],
                                           'type': 'scatter', 'name': '女員工離職率', },
                                      ],
                                      'layout': {
                                          'title': '女員工離職率',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          'xaxis': dict(tickvals=[9, 10, 11], ticktext=['9', '10', '11'], tickmode='array'),
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            html.Hr(),

            # 多近三月四
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threem_10', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.threemonth, 'y': st_gender_month['avg_ot_male'],
                                     'type': 'scatter', 'name': '月加班時數(男)', },
                                ],
                                'layout': {
                                    'title': '月加班時數(男)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[9, 10, 11], ticktext=['9', '10', '11'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_threem_11', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.threemonth, 'y': st_gender_month['avg_ot_female'],
                                     'type': 'scatter', 'name': '月加班時數(女)', },
                                ],
                                'layout': {
                                    'title': '月加班時數(女)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[9, 10, 11], ticktext=['9', '10', '11'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),
        ]),

        # 多元共融近六月
        # 多近六月一
        html.Div(id='Diversitysixm', children=[
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity-sixm_1', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.sixmonth, 'y': st_gender_month['now_em_grate'],
                                     'type': 'scatter', 'name': '現員工性別比', },
                                ],
                                'layout': {
                                    'title': '現員工性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity_sixm_2', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.sixmonth, 'y': st_gender_month['now_male'],
                                     'type': 'scatter', 'name': '現男員工人數', },
                                ],
                                'layout': {
                                    'title': '現男員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity_sixm_3', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.sixmonth, 'y': st_gender_month['now_female'],
                                     'type': 'scatter', 'name': '現女員工人數', },
                                ],
                                'layout': {
                                    'title': '現女員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近六月二
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_sixm_4', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.sixmonth, 'y': st_gender_month['new_grate'],
                                     'type': 'scatter', 'name': '新員工性別比', },
                                ],
                                'layout': {
                                    'title': '新員工性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_sixm_5', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.sixmonth, 'y': st_gender_month['new_male'],
                                     'type': 'scatter', 'name': '新男員工人數', },
                                ],
                                'layout': {
                                    'title': '新男員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity_sixm_6', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_month.sixmonth, 'y': st_gender_month['new_female'],
                                           'type': 'scatter', 'name': '新女員工人數', },
                                      ],
                                      'layout': {
                                          'title': '新女員工人數',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近六月三
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_sixm_7', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.sixmonth, 'y': st_gender_month['leave_grate'],
                                     'type': 'scatter', 'name': '離職員工性別比', },
                                ],
                                'layout': {
                                    'title': '離職員工性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_sixm_8', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.sixmonth, 'y': st_gender_month['leave_male'],
                                     'type': 'scatter', 'name': '男員工離職率', },
                                ],
                                'layout': {
                                    'title': '男員工離職率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_sixm_9', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_month.sixmonth, 'y': st_gender_month['leave_female'],
                                           'type': 'scatter', 'name': '女員工離職率', },
                                      ],
                                      'layout': {
                                          'title': '女員工離職率',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            html.Hr(),

            # 多近六月四
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_sixm_10', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.sixmonth, 'y': st_gender_month['avg_ot_male'],
                                     'type': 'scatter', 'name': '月加班時數(男)', },
                                ],
                                'layout': {
                                    'title': '月加班時數(男)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_sixm_11', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.sixmonth, 'y': st_gender_month['avg_ot_female'],
                                     'type': 'scatter', 'name': '月加班時數(女)', },
                                ],
                                'layout': {
                                    'title': '月加班時數(女)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),
        ]),

        # 多元共融近十月
        # 多近十月一
        html.Div(id='Diversitytenm', children=[
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity-tenm_1', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.tenmonth, 'y': st_gender_month['now_em_grate'],
                                     'type': 'scatter', 'name': '現員工性別比', },
                                ],
                                'layout': {
                                    'title': '現員工性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity_tenm_2', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.tenmonth, 'y': st_gender_month['now_male'],
                                     'type': 'scatter', 'name': '現男員工人數', },
                                ],
                                'layout': {
                                    'title': '現男員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity_tenm_3', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.tenmonth, 'y': st_gender_month['now_female'],
                                     'type': 'scatter', 'name': '現女員工人數', },
                                ],
                                'layout': {
                                    'title': '現女員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近十月二
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_tenm_4', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.tenmonth, 'y': st_gender_month['new_grate'],
                                     'type': 'scatter', 'name': '新員工性別比', },
                                ],
                                'layout': {
                                    'title': '新員工性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_tenm_5', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.tenmonth, 'y': st_gender_month['new_male'],
                                     'type': 'scatter', 'name': '新男員工人數', },
                                ],
                                'layout': {
                                    'title': '新男員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='diversity_tenm_6', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_month.tenmonth, 'y': st_gender_month['new_female'],
                                           'type': 'scatter', 'name': '新女員工人數', },
                                      ],
                                      'layout': {
                                          'title': '新女員工人數',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 多近十月三
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_tenm_7', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.tenmonth, 'y': st_gender_month['leave_grate'],
                                     'type': 'scatter', 'name': '離職員工性別比', },
                                ],
                                'layout': {
                                    'title': '離職員工性別比',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_tenm_8', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.tenmonth, 'y': st_gender_month['leave_male'],
                                     'type': 'scatter', 'name': '男員工離職率', },
                                ],
                                'layout': {
                                    'title': '男員工離職率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_tenm_9', style={'width': '430px', 'height': '320px'},
                                      figure={
                                      'data': [
                                          {'x': st_gender_month.tenmonth, 'y': st_gender_month['leave_female'],
                                           'type': 'scatter', 'name': '女員工離職率', },
                                      ],
                                      'layout': {
                                          'title': '女員工離職率',
                                          'color': '#E73A5F',
                                          'scatter_color': '#E73A5F',
                                          'plot_bgcolor': colors['background'],
                                          'paper_bgcolor': colors['background'],
                                          'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                          # 'height': 10
                                      }
                                      },
                                      ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            html.Hr(),

            # 多近十月四
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='現員工性別比', style={
                            #    'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_tenm_10', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.tenmonth, 'y': st_gender_month['avg_ot_male'],
                                     'type': 'scatter', 'name': '月加班時數(男)', },
                                ],
                                'layout': {
                                    'title': '月加班時數(男)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            # html.P(children='專案人數', style={
                            #     'font-size': '24px', 'font-family': '字體'}),
                            dcc.Graph(id='diversity_tenm_11', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_gender_month.tenmonth, 'y': st_gender_month['avg_ot_female'],
                                     'type': 'scatter', 'name': '月加班時數(女)', },
                                ],
                                'layout': {
                                    'title': '月加班時數(女)',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': colors['background'],
                                    'paper_bgcolor': colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),
        ]),

        # 多元共融時間軸
        html.Div([
            html.Img(id='DiversityNowend', src=app.get_asset_url(
                '多元共融現況.png'),  height='20', width='160', style={'position': 'absolute', 'margin-top': '10px'}),
            html.Button(id='DiversityChangeNowend', children='現況', type="button",
                        style={'width': '160px', 'position': 'relative', 'border': 'none', 'opacity': '0%'}),
            html.Button(id='Diversitythreemonth', children='近三月', type="button",
                        style={'margin-left': '310px'}),
            html.Button(id='Diversitysixmonth', children='近六月', type="button",
                        style={'margin-left': '60px'}),
            html.Button(id='Diversitytenmonth', children='近十月', type="button",
                        style={'margin-left': '60px'}),
            html.Img(id='DiversityMonthyear', src=app.get_asset_url(
                '多元共融月.png'),  height='20', width='160', style={'position': 'absolute', 'margin-top': '10px', 'right': 0}),
            html.Button(id='DiversityChangeMonthyear', children='月', type="button",
                        style={'width': '140px', 'position': 'absolute', 'border': 'none', 'opacity': '0%', 'right': 0}),
        ],
            style={
            'padding': '8px',
            'backgroundColor': 'rgba(255, 255, 255, 0.7)',
            'box-shadow': '0px -2px 4px rgba(0, 0, 0, 0.25)',
            'backdrop-filter': 'blur(5px)',
            'width': '100%',
            'fontSize': '18px',
            'color': '#11111',
            'display': 'inline-block',
            'position': 'sticky',
            'bottom': '0'
        }
        ),


    ]),

    # 勞工關係
    html.Div(id='LaborRelations', children=[
        html.Div(className='row', children=[
             html.Div([html.Img(src=app.get_asset_url(
                '勞工關係logo.png'),  height='260', width='1400')], style={'margin': '32px 50px'}),

             ]),


        # 勞工關係年現況
        # 勞年現一
        html.Div(id='Labornowyear', children=[
            html.Div(className='row', children=[
                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='新員工人數', style={
                               'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='2,216', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#117B9E'},),
                            html.P(children=' ➚', style={
                                   'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='8.52%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='今年離職人數', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='1,372', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#117B9E'}),
                            html.P(children=' ➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='28.95%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='去年離職人數', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='1,064', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#117B9E'}),
                            html.P(children=' ➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='7.69%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='今年留任率', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='86.72%', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#117B9E'}),
                            html.P(children=' ➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='2.91%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

            ], style={'margin': '20px 40px'}),

            # 勞年現二
            html.Div(className='row', children=[
                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='新員工率', style={
                               'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='26.68%', style={
                                'font-size': '60px', 'font-family': '字體'},),
                            html.P(children='➘', style={
                                   'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                            html.P(children='3.40%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='今年離職率', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='16.52%', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#117B9E'}),
                            html.P(children=' ➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='14.80%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='去年離職率', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='14.39%', style={
                                'font-size': '60px', 'font-family': '字體', }),
                            html.P(children='➘', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                            html.P(children='1.98%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='去年留任率', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='84.27%', style={
                                'font-size': '60px', 'font-family': '字體', }),
                            html.P(children='➘', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                            html.P(children='0.92%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

            ], style={'margin': '20px 40px'}),

            # 勞年現三
            html.Div(className='row', children=[
                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='年均月加班時數', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='10.36/人', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#117B9E'}),
                            html.P(children=' ➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='4.95%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'background': '#EAFBFF'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='新員工培訓程度', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='29.8%', style={
                                'font-size': '60px', 'font-family': '字體'},),
                            html.P(children='➘', style={
                                   'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px', 'visibility': 'hidden'}),
                            html.P(children='123', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px', 'visibility': 'hidden'})
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#EAFBFF'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='現留職停薪人數', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='8', style={
                                'font-size': '60px', 'font-family': '字體', }),
                            html.P(children='➘', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px', 'visibility': 'hidden'}),
                            html.P(children='123', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px', 'visibility': 'hidden'})
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#EAFBFF'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='現育嬰假人數', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='43', style={
                                'font-size': '60px', 'font-family': '字體', }),
                            html.P(children='➘', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                            html.P(children='2.27%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='YoY', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#EAFBFF'}),  # 左半邊的畫面調整),

            ], style={'margin': '20px 40px'}),
        ]),

        # 勞工關係月現況
        # 勞月現一
        html.Div(id='Labornowmonth', children=[
            html.Div(className='row', children=[
                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='本月離職人數', style={
                               'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='129', style={
                                'font-size': '60px', 'font-family': '字體'},),
                            html.P(children='➘', style={
                                   'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                            html.P(children='20.86%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='MoM', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='本月離職率', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='1.51%', style={
                                'font-size': '60px', 'font-family': '字體', }),
                            html.P(children='➘', style={
                                   'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                            html.P(children='21.35%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='MoM', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='上個月離職人數', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='163', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#117B9E'}),
                            html.P(children=' ➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='42.98%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='MoM', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='上個月離職率', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='1.93%', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#117B9E'}),
                            html.P(children=' ➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='41.91%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='MoM', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

            ], style={'margin': '20px 40px'}),

            # 勞月現二
            html.Div(className='row', children=[
                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='現專案人數', style={
                               'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='5,606', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#117B9E'},),
                            html.P(children=' ➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='0.72%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='MoM', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'background': '#EAFBFF'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='現非專案人數', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='5,402', style={
                                'font-size': '60px', 'font-family': '字體'},),
                            html.P(children='➘', style={
                                   'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                            html.P(children='4.94%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='MoM', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#EAFBFF'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='現留資停薪人數', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='8', style={
                                'font-size': '60px', 'font-family': '字體', }),
                         html.P(children='➘', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px', 'visibility': 'hidden'}),
                         html.P(children='123', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px', 'visibility': 'hidden'})
                         ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#EAFBFF'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='現育嬰假人數', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='3', style={
                                'font-size': '60px', 'font-family': '字體', }),
                            html.P(children='', style={
                                'display': 'inline-block', 'font-size': '36px'}),
                            html.P(children='0.00%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#117B9E', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='MoM', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#EAFBFF'}),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),

            # 勞月現三
            html.Div(className='row', children=[
                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                     html.Div(className='col d-inline-block text-center', children=[
                         html.P(children='平均打卡時數', style={
                                'font-size': '24px', 'font-family': '字體'}),
                         html.P(children='9.01', style={
                                'font-size': '60px', 'font-family': '字體', }),
                         html.P(children='➘', style={
                                'display': 'inline-block', 'color': '#86AE42', 'font-size': '36px'}),
                         html.P(children='0.66%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#86AE42', 'display': 'inline-block', 'margin-left': '5px'}),
                         html.P(children='MoM', style={
                             'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                     ], style={'margin': 'auto'}),
                     ], style={'padding': '20px'}),
                ], style={'background': '#EAFBFF'}),  # 左半邊的畫面調整),

                html.Div(className='col-3 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            html.P(children='月加班時數', style={
                                'font-size': '24px', 'font-family': '字體'}),
                            html.P(children='11.19/人', style={
                                'font-size': '60px', 'font-family': '字體', 'color': '#117B9E'}),
                            html.P(children='➚', style={
                                'display': 'inline-block', 'color': '#E73A5F', 'font-size': '36px'}),
                            html.P(children='18.16%', style={
                                'font-size': '28px', 'font-family': '字體', 'color': '#E73A5F', 'display': 'inline-block', 'margin-left': '5px'}),
                            html.P(children='MoM', style={
                                'font-size': '16px', 'font-family': '字體', 'color': '#6D707C', 'display': 'inline-block', 'position': 'absolute', 'margin-left': '10px'}),
                        ], style={'margin': 'auto'}),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', 'background': '#EAFBFF'}),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),
        ]),

        # 勞工關係近三年
        # 勞近三年一
        html.Div(id='Laborthreey', children=[
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor-threey_1', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_year.threeyear, 'y': st_labor_year['now_em'],
                                     'type': 'scatter', 'name': '員工人數', },
                                ],
                                'layout': {
                                    'title': '員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_threey_2', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_year.threeyear, 'y': st_labor_year['new_in'],
                                     'type': 'scatter', 'name': '新員工人數', },
                                ],
                                'layout': {
                                    'title': '新員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_threey_3', style={'width': '430px', 'height': '320px'},
                                                      figure={
                                'data': [
                                    {'x': st_labor_year.threeyear, 'y': st_labor_year['now_leave'],
                                     'type': 'scatter', 'name': '離職人數', },
                                ],
                                'layout': {
                                    'title': '離職人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

            ], style={'margin': '20px 40px'}),

            # 勞近三年二
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor-threey_4', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_year.threeyear, 'y': st_labor_year['now_still_rate'],
                                     'type': 'scatter', 'name': '員工留任率', },
                                ],
                                'layout': {
                                    'title': '員工留任率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_threey_5', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_year.threeyear, 'y': st_labor_year['new_in_rate'],
                                     'type': 'scatter', 'name': '新員工率', },
                                ],
                                'layout': {
                                    'title': '新員工率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_threey_6', style={'width': '430px', 'height': '320px'},
                                                      figure={
                                'data': [
                                    {'x': st_labor_year.threeyear, 'y': st_labor_year['now_leave_rate'],
                                     'type': 'scatter', 'name': '離職率', },
                                ],
                                'layout': {
                                    'title': '離職率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

            ], style={'margin': '20px 40px'}),

            html.Hr(),

            # 勞近三年三
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor-threey_7', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_year.threeyear, 'y': st_labor_year['avg_punch'],
                                     'type': 'scatter', 'name': '平均打卡時數', },
                                ],
                                'layout': {
                                    'title': '平均打卡時數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_threey_8', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_year.threeyear, 'y': st_labor_year['avg_ot'],
                                     'type': 'scatter', 'name': '年均月加班時數', },
                                ],
                                'layout': {
                                    'title': '年均月加班時數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_threey_9', style={'width': '430px', 'height': '320px'},
                                                      figure={
                                'data': [
                                    {'x': st_labor_year.threeyear, 'y': st_labor_year['baby_vac'],
                                     'type': 'scatter', 'name': '現育嬰假人數', },
                                ],
                                'layout': {
                                    'title': '現育嬰假人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[2019, 2020, 2021], ticktext=['2019', '2020', '2021'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

            ], style={'margin': '20px 40px'}),
        ]),

        # 勞工關係近五年
        # 勞近五年一
        html.Div(id='Laborfivey', children=[
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_fivey_1', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_year.fiveyear, 'y': st_labor_year['now_em'],
                                     'type': 'scatter', 'name': '員工人數', },
                                ],
                                'layout': {
                                    'title': '員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_fivey_2', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_year.fiveyear, 'y': st_labor_year['new_in'],
                                     'type': 'scatter', 'name': '新員工人數', },
                                ],
                                'layout': {
                                    'title': '新員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_fivey_3', style={'width': '430px', 'height': '320px'},
                                                      figure={
                                'data': [
                                    {'x': st_labor_year.fiveyear, 'y': st_labor_year['now_leave'],
                                     'type': 'scatter', 'name': '離職人數', },
                                ],
                                'layout': {
                                    'title': '離職人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

            ], style={'margin': '20px 40px'}),

            # 勞近五年二
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_fivey_4', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_year.fiveyear, 'y': st_labor_year['now_still_rate'],
                                     'type': 'scatter', 'name': '員工留任率', },
                                ],
                                'layout': {
                                    'title': '員工留任率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_fivey_5', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_year.fiveyear, 'y': st_labor_year['new_in_rate'],
                                     'type': 'scatter', 'name': '新員工率', },
                                ],
                                'layout': {
                                    'title': '新員工率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_fivey_6', style={'width': '430px', 'height': '320px'},
                                                      figure={
                                'data': [
                                    {'x': st_labor_year.fiveyear, 'y': st_labor_year['now_leave_rate'],
                                     'type': 'scatter', 'name': '離職率', },
                                ],
                                'layout': {
                                    'title': '離職率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

            ], style={'margin': '20px 40px'}),

            html.Hr(),

            # 勞近五年三
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_fivey_7', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_year.fiveyear, 'y': st_labor_year['avg_punch'],
                                     'type': 'scatter', 'name': '平均打卡時數', },
                                ],
                                'layout': {
                                    'title': '平均打卡時數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_fivey_8', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_year.fiveyear, 'y': st_labor_year['avg_ot'],
                                     'type': 'scatter', 'name': '年均月加班時數', },
                                ],
                                'layout': {
                                    'title': '年均月加班時數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_fivey_9', style={'width': '430px', 'height': '320px'},
                                                      figure={
                                'data': [
                                    {'x': st_labor_year.fiveyear, 'y': st_labor_year['baby_vac'],
                                     'type': 'scatter', 'name': '現育嬰假人數', },
                                ],
                                'layout': {
                                    'title': '現育嬰假人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

            ], style={'margin': '20px 40px'}),
        ]),

        # 勞工關係近十年
        # 勞近十年一
        html.Div(id='Laborteny', children=[
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_teny_1', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_year.tenyear, 'y': st_labor_year['now_em'],
                                     'type': 'scatter', 'name': '員工人數', },
                                ],
                                'layout': {
                                    'title': '員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_teny_2', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_year.tenyear, 'y': st_labor_year['new_in'],
                                     'type': 'scatter', 'name': '新員工人數', },
                                ],
                                'layout': {
                                    'title': '新員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_teny_3', style={'width': '430px', 'height': '320px'},
                                                      figure={
                                'data': [
                                    {'x': st_labor_year.tenyear, 'y': st_labor_year['now_leave'],
                                     'type': 'scatter', 'name': '離職人數', },
                                ],
                                'layout': {
                                    'title': '離職人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

            ], style={'margin': '20px 40px'}),

            # 勞近十年二
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_teny_4', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_year.tenyear, 'y': st_labor_year['now_still_rate'],
                                     'type': 'scatter', 'name': '員工留任率', },
                                ],
                                'layout': {
                                    'title': '員工留任率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_teny_5', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_year.tenyear, 'y': st_labor_year['new_in_rate'],
                                     'type': 'scatter', 'name': '新員工率', },
                                ],
                                'layout': {
                                    'title': '新員工率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_teny_6', style={'width': '430px', 'height': '320px'},
                                                      figure={
                                'data': [
                                    {'x': st_labor_year.tenyear, 'y': st_labor_year['now_leave_rate'],
                                     'type': 'scatter', 'name': '離職率', },
                                ],
                                'layout': {
                                    'title': '離職率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

            ], style={'margin': '20px 40px'}),

            html.Hr(),

            # 勞近十年三
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_teny_7', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_year.tenyear, 'y': st_labor_year['avg_ot'],
                                     'type': 'scatter', 'name': '年均月加班時數', },
                                ],
                                'layout': {
                                    'title': '年均月加班時數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_teny_8', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_year.tenyear, 'y': st_labor_year['baby_vac'],
                                     'type': 'scatter', 'name': '現育嬰假人數', },
                                ],
                                'layout': {
                                    'title': '現育嬰假人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),
        ]),

        # 勞工關係近三月
        # 勞近三月一
        html.Div(id='Laborthreem', children=[
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_threem_1', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_month.threemonth, 'y': st_labor_month['now_em'],
                                     'type': 'scatter', 'name': '員工人數', },
                                ],
                                'layout': {
                                    'title': '員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[9, 10, 11], ticktext=['9', '10', '11'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_threem_2', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_month.threemonth, 'y': st_labor_month['now_leave'],
                                     'type': 'scatter', 'name': '月離職人數', },
                                ],
                                'layout': {
                                    'title': '月離職人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[9, 10, 11], ticktext=['9', '10', '11'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_threem_3', style={'width': '430px', 'height': '320px'},
                                                      figure={
                                'data': [
                                    {'x': st_labor_month.threemonth, 'y': st_labor_month['now_leave_rate'],
                                     'type': 'scatter', 'name': '月離職率', },
                                ],
                                'layout': {
                                    'title': '月離職率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[9, 10, 11], ticktext=['9', '10', '11'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

            ], style={'margin': '20px 40px'}),

            html.Hr(),

            # 勞近三月二
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_threem_4', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_month.threemonth, 'y': st_labor_month['now_proj'],
                                     'type': 'scatter', 'name': '現專案人數', },
                                ],
                                'layout': {
                                    'title': '現專案人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[9, 10, 11], ticktext=['9', '10', '11'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_threem_5', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_month.threemonth, 'y': st_labor_month['avg_ot'],
                                     'type': 'scatter', 'name': '月加班時數', },
                                ],
                                'layout': {
                                    'title': '月加班時數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[9, 10, 11], ticktext=['9', '10', '11'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_threem_6', style={'width': '430px', 'height': '320px'},
                                                      figure={
                                'data': [
                                    {'x': st_labor_month.threemonth, 'y': st_labor_month['baby_vac'],
                                     'type': 'scatter', 'name': '現育嬰假人數', },
                                ],
                                'layout': {
                                    'title': '現育嬰假人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[9, 10, 11], ticktext=['9', '10', '11'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

            ], style={'margin': '20px 40px'}),

            # 勞近三月三
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_threem_7', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_month.threemonth, 'y': st_labor_month['pre_nonproj'],
                                     'type': 'scatter', 'name': '現非專案人數', },
                                ],
                                'layout': {
                                    'title': '現非專案人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    'xaxis': dict(tickvals=[9, 10, 11], ticktext=['9', '10', '11'], tickmode='array'),
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

            ], style={'margin': '20px 40px'}),
        ]),

        # 勞工關係近六月
        # 勞近六月一
        html.Div(id='Laborsixm', children=[
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_sixm_1', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_month.sixmonth, 'y': st_labor_month['now_em'],
                                     'type': 'scatter', 'name': '員工人數', },
                                ],
                                'layout': {
                                    'title': '員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_sixm_2', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_month.sixmonth, 'y': st_labor_month['now_leave'],
                                     'type': 'scatter', 'name': '月離職人數', },
                                ],
                                'layout': {
                                    'title': '月離職人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_sixm_3', style={'width': '430px', 'height': '320px'},
                                                      figure={
                                'data': [
                                    {'x': st_labor_month.sixmonth, 'y': st_labor_month['now_leave_rate'],
                                     'type': 'scatter', 'name': '月離職率', },
                                ],
                                'layout': {
                                    'title': '月離職率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

            ], style={'margin': '20px 40px'}),

            html.Hr(),

            # 勞近三月二
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_sixm_4', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_month.sixmonth, 'y': st_labor_month['now_proj'],
                                     'type': 'scatter', 'name': '現專案人數', },
                                ],
                                'layout': {
                                    'title': '現專案人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_sixm_5', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_month.sixmonth, 'y': st_labor_month['avg_ot'],
                                     'type': 'scatter', 'name': '月加班時數', },
                                ],
                                'layout': {
                                    'title': '月加班時數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_sixm_6', style={'width': '430px', 'height': '320px'},
                                                      figure={
                                'data': [
                                    {'x': st_labor_month.sixmonth, 'y': st_labor_month['baby_vac'],
                                     'type': 'scatter', 'name': '現育嬰假人數', },
                                ],
                                'layout': {
                                    'title': '現育嬰假人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

            ], style={'margin': '20px 40px'}),

            # 勞近三月三
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_sixm_7', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_month.sixmonth, 'y': st_labor_month['pre_nonproj'],
                                     'type': 'scatter', 'name': '現非專案人數', },
                                ],
                                'layout': {
                                    'title': '現非專案人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),
            ], style={'margin': '20px 40px'}),
        ]),

        # 勞工關係近十月
        # 勞近十月一
        html.Div(id='Labortenm', children=[
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_tenm_1', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_month.tenmonth, 'y': st_labor_month['now_em'],
                                     'type': 'scatter', 'name': '員工人數', },
                                ],
                                'layout': {
                                    'title': '員工人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_tenm_2', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_month.tenmonth, 'y': st_labor_month['now_leave'],
                                     'type': 'scatter', 'name': '月離職人數', },
                                ],
                                'layout': {
                                    'title': '月離職人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_tenm_3', style={'width': '430px', 'height': '320px'},
                                                      figure={
                                'data': [
                                    {'x': st_labor_month.tenmonth, 'y': st_labor_month['now_leave_rate'],
                                     'type': 'scatter', 'name': '月離職率', },
                                ],
                                'layout': {
                                    'title': '月離職率',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

            ], style={'margin': '20px 40px'}),

            html.Hr(),

            # 勞近三月二
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_tenm_4', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_month.tenmonth, 'y': st_labor_month['now_proj'],
                                     'type': 'scatter', 'name': '現專案人數', },
                                ],
                                'layout': {
                                    'title': '現專案人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_tenm_5', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_month.tenmonth, 'y': st_labor_month['avg_ot'],
                                     'type': 'scatter', 'name': '月加班時數', },
                                ],
                                'layout': {
                                    'title': '月加班時數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_tenm_6', style={'width': '430px', 'height': '320px'},
                                                      figure={
                                'data': [
                                    {'x': st_labor_month.tenmonth, 'y': st_labor_month['baby_vac'],
                                     'type': 'scatter', 'name': '現育嬰假人數', },
                                ],
                                'layout': {
                                    'title': '現育嬰假人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ]),
                    ], style={'padding': '20px'}),
                ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

            ], style={'margin': '20px 40px'}),

            # 勞近三月三
            html.Div(className='row', children=[
                html.Div(className='col-4 d-inline-block h-50', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col d-inline-block text-center', children=[
                            dcc.Graph(id='labor_tenm_7', style={'width': '430px', 'height': '320px'},
                                      figure={
                                'data': [
                                    {'x': st_labor_month.tenmonth, 'y': st_labor_month['pre_nonproj'],
                                     'type': 'scatter', 'name': '現非專案人數', },
                                ],
                                'layout': {
                                    'title': '現非專案人數',
                                    'color': '#E73A5F',
                                    'scatter_color': '#E73A5F',
                                    'plot_bgcolor': labor_colors['background'],
                                    'paper_bgcolor': labor_colors['background'],
                                    'font': {'color': 'black', 'size': 16, 'family': '字體'},
                                    # 'height': 10
                                }
                            },
                            ),
                        ], ),
                    ], style={'padding': '20px'}),
                ]),  # 左半邊的畫面調整),

                # html.Div(className='col-4 d-inline-block h-50', children=[
                #     html.Div(className='row', children=[
                #         html.Div(className='col d-inline-block text-center', children=[
                #             dcc.Graph(id='labor_tenm_8', style={'width': '430px', 'height': '320px'},
                #                       figure={
                #                 'data': [
                #                     {'x': st_labor_month.tenmonth, 'y': st_labor_month['avg_ot'],
                #                      'type': 'scatter', 'name': '離職預測人數', },
                #                 ],
                #                 'layout': {
                #                     'title': '離職預測人數',
                #                     'color': '#E73A5F',
                #                     'scatter_color': '#E73A5F',
                #                     'plot_bgcolor': labor_colors['background'],
                #                     'paper_bgcolor': labor_colors['background'],
                #                     'font': {'color': 'black', 'size': 16, 'family': '字體'},
                #                     # 'height': 10
                #                 }
                #             },
                #             ),
                #         ]),
                #     ], style={'padding': '20px'}),
                # ], style={'margin-left': '10px', }),  # 左半邊的畫面調整),

            ], style={'margin': '20px 40px'}),
        ]),

        # 勞工關係時間軸
        html.Div([
            html.Img(id='LaborNowend', src=app.get_asset_url(
                 '勞工關係現況.png'),  height='20', width='160', style={'position': 'absolute', 'margin-top': '10px'}),
            html.Button(id='LaborChangeNowend', children='現況', type="button",
                        style={'width': '160px', 'position': 'relative', 'border': 'none', 'opacity': '0%'}),
            html.Button(id='Laborthreemonth', children='近三月', type="button",
                        style={'margin-left': '310px'}),
            html.Button(id='Laborsixmonth', children='近六月', type="button",
                        style={'margin-left': '60px'}),
            html.Button(id='Labortenmonth', children='近十月', type="button",
                        style={'margin-left': '60px'}),
            html.Img(id='LaborMonthyear', src=app.get_asset_url(
                '勞工關係月.png'),  height='20', width='160', style={'position': 'absolute', 'margin-top': '10px', 'right': 0}),
            html.Button(id='LaborChangeMonthyear', children='月', type="button",
                        style={'width': '140px', 'position': 'absolute', 'border': 'none', 'opacity': '0%', 'right': 0}),
        ],
            style={
                'padding': '8px',
                'backgroundColor': 'rgba(255, 255, 255, 0.7)',
                'box-shadow': '0px -2px 4px rgba(0, 0, 0, 0.25)',
                'backdrop-filter': 'blur(5px)',
                'width': '100%',
                'fontSize': '18px',
                'color': '#11111',
                'display': 'inline-block',
                'position': 'sticky',
                'bottom': '0'
        }
        ),

    ]),


])


# Step 6. 完成 Server工作
if __name__ == '__main__':
    app.run_server(debug=False)
