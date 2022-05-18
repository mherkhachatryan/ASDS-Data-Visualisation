import plotly.express as px
from dash import dcc

from data_processing import data


px.set_mapbox_access_token(
        open(
                "/Users/mkhachatryan/Codes/ASDS-Data-Visualisation/data/mapbox_token.txt").read(

                ))

fig = px.scatter_mapbox(data, lat="pickup_latitude", lon="pickup_longitude", color="passenger_count",
                        size="trip_duration",
                        color_continuous_scale=px.colors.cyclical.IceFire)

map_layout = dcc.Graph(id="example_map", figure=fig)
