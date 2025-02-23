import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc
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

app = dash.Dash()

# Design Dash Layout
app.layout = html.Div(children=[
    html.H1("Covid-19 Dashboard",
        style={'textAlign':'center', 'color':'red','font-size':40}),
    html.Div(["Input:", dcc.Input(id='input-country',value='Austria',type='string',
        style={'height':'50px','font-size':35}),],
        style={'font-size':40}),
    html.Br(),
    html.Br(),
    html.Div(dcc.Graph(id='bar-plot')),
])

if __name__ == "__main__":
    app.run(debug=True)