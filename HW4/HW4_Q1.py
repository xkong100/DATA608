import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np



url = 'https://data.cityofnewyork.us/resource/nwxe-4ae8.json'


#Bronx
boro = 'Bronx'
Bronx_soql_url = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?' +\
        '$select=health,count(tree_id)' +\
        '&$where=boroname=\'Bronx\'' +\
        '&$group=health').replace(' ', '%20')
Bronx_soql_trees = pd.read_json(Bronx_soql_url)

print(Bronx_soql_trees)


#Brooklyn
boro = 'Brooklyn'
Brooklyn_ql_url = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?' +\
        '$select=health,count(tree_id)' +\
        '&$where=boroname=\'Brooklyn\'' +\
        '&$group=health').replace(' ', '%20')
Brooklyn_ql_trees = pd.read_json(Brooklyn_ql_url)

print(Brooklyn_ql_trees)

#Queens

boro = 'Queens'
Queens_ql_url = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?' +\
        '$select=health,count(tree_id)' +\
        '&$where=boroname=\'Queens\'' +\
        '&$group=health').replace(' ', '%20')
Queens_ql_trees = pd.read_json(Queens_ql_url)

print(Queens_ql_trees)

#Manhattan

boro = 'Manhattan'
Manhattan_ql_url = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?' +\
        '$select=health,count(tree_id)' +\
        '&$where=boroname=\'Manhattan\'' +\
        '&$group=health').replace(' ', '%20')
Manhattan_ql_trees = pd.read_json(Manhattan_ql_url)

print(Manhattan_ql_trees)

#Staten Island

boro = 'Staten Island'
SI_ql_url = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?' +\
        '$select=health,count(tree_id)' +\
        '&$where=boroname=\'Staten Island\'' +\
        '&$group=health').replace(' ', '%20')
SI_ql_trees = pd.read_json(SI_ql_url)

print(SI_ql_trees)








external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Proportion of Trees health'),

    html.Div(children='''
        Dash: A bar graph of the proportions of different boroughs
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': ['Good', 'Fair', 'Poor'], 'y': [78.17, 12.78, 3.63], 'type': 'bar', 'name': 'Bronx'},
                {'x': ['Good', 'Fair', 'Poor'], 'y': [77.96, 14.14, 3.64], 'type': 'bar', 'name': u'Brooklyn'},
                {'x': ['Good', 'Fair', 'Poor'], 'y': [77.43, 13.79, 3.76], 'type': 'bar', 'name': u'Queens'},
                {'x': ['Good', 'Fair', 'Poor'], 'y': [72.39, 17.52, 5.52], 'type': 'bar', 'name': u'Manhattan'},
                {'x': ['Good', 'Fair', 'Poor'], 'y': [78.49, 13.80, 4.02], 'type': 'bar', 'name': u'Staten Island'}
            ],
            'layout': {
                'title': 'Health condition of Trees in different borough of NY'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)