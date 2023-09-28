import os
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from datetime import datetime

st.title('BHAVCOPY ANALYZER')

path = "P:\DEPROJECT\Analyzed_Company_file"
li = [os.path.splitext(filename)[0] for filename in os.listdir(path)]

select_event = st.selectbox('', li)
df = pd.read_csv(f"P:/DEPROJECT/Analyzed_Company_file/{select_event}.csv")
df

fig = go.Figure(data=[go.Candlestick(x=df['DATE'],
                                     open=df['OPEN_PRICE'],
                                     high=df['HIGH_PRICE'],
                                     low=df['LOW_PRICE'],
                                     close=df['CLOSE_PRICE'])])

fig
lst = [
    'Total treaded quantity',
    'Delivery percentage(in %)',
    'Delivery vs treading',
    'Intradey volume',
    'Number of treades'
]

op = st.selectbox('', lst)

if op == 'Total treaded quantity':
    fig = go.Figure(
        data=[go.Bar(y=df['TTL_TRD_QNTY'].iloc[:-1], x=df["DATE"])],
        layout_title_text=""
    )
    fig
elif op == 'Delivery percentage(in %)':
    fig = go.Figure(
        data=[go.Bar(y=df['DELIV_PER'].iloc[:-1], x=df["DATE"])],
        layout_title_text=""
    )
    fig
elif op == 'Delivery vs treading':
    fig = go.Figure(
        data=[go.Bar(name='Delivery', y=df['DELIV_QTY'].iloc[:-1], x=df["DATE"]),
              go.Bar(name='treading', y=df['TTL_TRD_QNTY'].iloc[:-1], x=df["DATE"])
              ],
        layout_title_text=""
    )
    fig
elif op == 'Intradey volume':
    fig = go.Figure(
        data=[go.Bar(y=df['Intraday_volume'].iloc[:-1], x=df["DATE"])],
        layout_title_text=""
    )
    fig
elif op == 'Number of treades':
    fig = go.Figure(
        data=[go.Bar(y=df['NO_OF_TRADES'].iloc[:-1], x=df["DATE"])],
        layout_title_text=""
    )
    fig
