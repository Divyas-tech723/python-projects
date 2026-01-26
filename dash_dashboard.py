# Interactive Data Dashboard using Dash and Plotly
import dash 
from dash import html, dcc  
from dash.dependencies import Input,Output 
import plotly.express as px  
import pandas as pd

#Load sample dataset  
df = px.data.gapminder().query("year == 2007")

#Initialize Dash app
app = dash.Dash(__name__)

#App layout  
app.layout = html.Div([
    html.H1("Global Stats Dashboard"),

    dcc.Dropdown(
        id='continent',
        options=[{'label': c, 'value': c} for c in df['continent'].unique()],
        value='Asia'
    ),

    dcc.Graph(id='life-exp-chart')
])

#Callback to update graph  
@app.callback(
    Output('life-exp-chart', 'figure'),
    [Input('continent', 'value')]
)
def update_chart(selected_continent):
    filtered_df = df[df['continent'] == selected_continent]
    fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp',size='pop', color='country', hover_name='country',
                     log_x=True, size_max=60)
    return fig
#Run server  
if __name__ == '__main__':  
    app.run(debug=True)
