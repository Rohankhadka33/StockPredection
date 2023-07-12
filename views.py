from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

from plotly.offline import plot
import plotly.graph_objects as go
import plotly.express as px
from plotly.graph_objs import Scatter

import pandas as pd
import numpy as np
import json

import yfinance as yf
import datetime as dt
import qrcode

from .models import Project

from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, model_selection, svm




# The Home page when Server loads up
def index(request):
    # ================================================= Left Card Plot =========================================================
    # Here we use yf.download function
    data = yf.download(
        
        # passes the ticker
        tickers=['AAPL', 'AMZN', 'QCOM', 'META', 'NVDA', 'JPM'],
        
        group_by = 'ticker',
        
        threads=True, # Set thread value to true
        
        # used for access data[ticker]
        period='1mo', 
        interval='1d'
    
    )

    data.reset_index(level=0, inplace=True)



    fig_left = go.Figure()
    fig_left.add_trace(
                go.Scatter(x=data['Date'], y=data['AAPL']['Adj Close'], name="AAPL")
            )
    fig_left.add_trace(
                go.Scatter(x=data['Date'], y=data['AMZN']['Adj Close'], name="AMZN")
            )
    fig_left.add_trace(
                go.Scatter(x=data['Date'], y=data['QCOM']['Adj Close'], name="QCOM")
            )
    fig_left.add_trace(
                go.Scatter(x=data['Date'], y=data['META']['Adj Close'], name="META")
            )
    fig_left.add_trace(
                go.Scatter(x=data['Date'], y=data['NVDA']['Adj Close'], name="NVDA")
            )
    fig_left.add_trace(
                go.Scatter(x=data['Date'], y=data['JPM']['Adj Close'], name="JPM")
            )
    fig_left.update_layout(paper_bgcolor="#14151b", plot_bgcolor="#14151b", font_color="white")

    plot_div_left = plot(fig_left, auto_open=False, output_type='div')

