from dash import html

from dashboard.index import app
from dashboard.layout.header import header
from dashboard.layout.map import map_layout

app.layout = html.Div([header[0],
                       header[1],
                       map_layout
                       ])
