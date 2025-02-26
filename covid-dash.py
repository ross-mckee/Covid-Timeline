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
# Set column index to Country/Region
df.columns = df.iloc[0]
df.drop('Country/Region', inplace=True)

df_gb = df.groupby(by='Country/Region', axis=1).sum() #Combines columns with the same index, thus combining all sub-territories within a country/region.
df = df_gb.copy()

df.reset_index(inplace=True)

# Get this line to print all of the country names.
#print(df.columns[0])

app = dash.Dash()

# -----------------------------------------------

# Design Dash Layout
app.layout = html.Div(children=[
    html.H1("Covid-19 Dashboard",
        style={'textAlign':'center', 'color':'red','font-size':40}),
    html.Div(["Input:",
        dcc.Dropdown(id='input-country',
            options=["Australia","Austria","Vietnam"],
            multi=False,
            value="Austria",
            style={'height':'50px','font-size':35}),],
        style={'font-size':40}),
    html.Br(),
    html.Br(),
    html.Div(dcc.Graph(id='line-plot')),
])

# ------------------------------------------------

# Plotly callback
@app.callback(
    Output(component_id='line-plot', component_property='figure'),
    Input(component_id='input-country', component_property='value')
)
def update_line_chart(entered_country):
    #select data
    #df_line = df[[entered_country]] #original idea, seems unnecessary
    #plot the graph
    fig1 = px.line(df, x='index', y=entered_country,
                   title="Total Confirmed CoViD-19 Cases in "+entered_country+" Over Time")
    return fig1

# ------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)