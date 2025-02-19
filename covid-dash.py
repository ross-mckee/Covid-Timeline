import pandas as pd
import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

# Read data
covid_data = pd.read_csv("time_series_covid19_confirmed_global.csv")

# Transpose data, so that countries are columns and rows are dates
df = covid_data.copy()
df = df.transpose()
df.drop('Province/State', inplace = True)
df.drop('Lat', inplace = True)
df.drop('Long', inplace = True)
df.columns = df.iloc[0]
df.drop('Country/Region', inplace=True)

print(df.head())