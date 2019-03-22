import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go


boro = 'Staten Island'
SI_qls_url = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?' +\
        '$select=health,steward,count(tree_id)' +\
        '&$where=boroname=\'Staten Island\'' +\
        '&$group=steward,health').replace(' ', '%20')
SI_qls_trees = pd.read_json(SI_qls_url)

print(SI_qls_trees)


boro = 'Bronx'
bronx_qls_url = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?' +\
        '$select=health,steward,count(tree_id)' +\
        '&$where=boroname=\'Bronx\'' +\
        '&$group=steward,health').replace(' ', '%20')
bronx_qls_trees = pd.read_json(bronx_qls_url)

print(bronx_qls_trees)


boro = 'Brooklyn'
brooklyn_qls_url = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?' +\
        '$select=health,steward,count(tree_id)' +\
        '&$where=boroname=\'Brooklyn\'' +\
        '&$group=steward,health').replace(' ', '%20')
brooklyn_qls_trees = pd.read_json(brooklyn_qls_url)

print(brooklyn_qls_trees)

boro = 'Manhattan'
Manhattan_qls_url = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?' +\
        '$select=health,steward,count(tree_id)' +\
        '&$where=boroname=\'Manhattan\'' +\
        '&$group=steward,health').replace(' ', '%20')
Manhattan_qls_trees = pd.read_json(Manhattan_qls_url)

print(Manhattan_qls_trees)


boro = 'Queens'
Queens_qls_url = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?' +\
        '$select=health,steward,count(tree_id)' +\
        '&$where=boroname=\'Queens\'' +\
        '&$group=steward,health').replace(' ', '%20')
Queens_qls_trees = pd.read_json(Queens_qls_url)

print(Queens_qls_trees)


trace0 = go.Scatter (
        x = ['None', '1 or 2', '3 or 4','4 or more'],
        y = [65869, 15458, 1244,98],
        name = 'Good/Staten Island')

trace1= go.Scatter(
        x = ['None', '1 or 2', '3 or 4','4 or more'],
        y = [11722, 2673, 129,11],
        name= 'Fair/Staten Island')

trace2 = go.Scatter(
        x=['None', '1 or 2', '3 or 4','4 or more'],
        y=[3514, 698, 23,3],
        name='Poor/Staten Island')

trace3 = go.Scatter (
        x = ['None', '1 or 2', '3 or 4','4 or more'],
        y = [53814, 12038, 1244,62],
        name = 'Good/Bronx')

trace4 = go.Scatter(
        x = ['None', '1 or 2', '3 or 4','4 or more'],
        y = [8625, 2130, 125,7],
        name= 'Fair/Bronx')

trace5 = go.Scatter(
        x=['None', '1 or 2', '3 or 4','4 or more'],
        y=[2412, 640, 41,2],
        name='Poor/Bronx')

trace6= go.Scatter(
        x=['None', '1 or 2', '3 or 4','4 or more'],
        y=[96852, 35749, 5147,464],
        name='Good/Brooklyn')

trace7= go.Scatter(
        x=['None', '1 or 2', '3 or 4','4 or more'],
        y=[17764, 6490, 760,59],
        name='Fair/Brooklyn')

trace8= go.Scatter(
        x=['None', '1 or 2', '3 or 4','4 or more'],
        y=[4668, 1638, 143,10],
        name='Poor/Brooklyn')

trace9= go.Scatter(
        x=['None', '1 or 2', '3 or 4','4 or more'],
        y=[22687, 18241, 5974,456],
        name='Good/Manhattan')

trace10 = go.Scatter(
        x=['None', '1 or 2', '3 or 4','4 or more'],
        y=[5494, 4471, 1415,80],
        name='Fair/Manhattan')

trace11=go.Scatter(
        x=['None', '1 or 2', '3 or 4','4 or more'],
        y=[1700, 1463, 428,18],
        name='Poor/Manhattan')

trace12 = go.Scatter(
        x=['None', '1 or 2', '3 or 4','4 or more'],
        y=[157289, 33886, 2552,281],
        name='Good/Queens')

trace13 = go.Scatter(
        x=['None', '1 or 2', '3 or 4','4 or more'],
        y=[27967, 6138, 401,43],
        name='Fair/Queens')

trace14 = go.Scatter(
        x=['None', '1 or 2', '3 or 4','4 or more'],
        y=[7445, 1844, 112,16],
        name='Poor/Queens')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Steward VS. Health'),

    html.Div(children='''
        A plot graph of the relationships between steward and health of different boroughs
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace0,trace1,trace2,trace3,trace4,trace5,trace6,trace7,trace8,trace9,trace10,trace11,trace12,trace13,trace14],
            'layout': {
                'title': 'Steward VS. Health'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
    
# By oberving the graph, I believe that there is a relationship between the steward and the health of the trees.
# Through out all of the boroughs, we can tell that Good health has more "None" steward. 
# To find the actual relationship, we need to look at the data closely, and run Chi-square test but the graph encourage us to do so because it seems a strong relationship.
