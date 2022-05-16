from dash import html

from dashboard.index import app
from dashboard.layout.header import header

app.layout = html.Div([header[0],
                       header[1],
                       ])
