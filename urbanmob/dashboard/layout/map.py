import plotly.express as px
from dash import dcc

px.set_mapbox_access_token(open("/Users/mkhachatryan/Codes/ASDS-Data-Visualisation/data/mapbox_token.txt").read())
df = px.data.carshare()
fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon", color="peak_hour",
                        size="car_hours",
                        color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)

map_layout = dcc.Graph(id="example_map", figure=fig)
