import dash  #helps us make interactive web pages (graps,dropdowns)
from dash import html, dcc #html--> toolbox for making headings.divs,paragraphs(like web HTML)  dcc--> dash core components: drophs graphs sliders 
from dash.dependencies import Input,Output 
import plotly.express as px  #is a simple plotting tool to make chart fast(scatter,line,bar)
import pandas as pd  #helps store  an filter tables of data(dataframes)

#Load sample dataset  
df = px.data.gapminder().query("year == 2007") #gapminder --> data about countries, ex--> px.data.iris()--> data about flowers and px.data.tips()--> restaurant tips data , px.data.carshare()--> car sharing data

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