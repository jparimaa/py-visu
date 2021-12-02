import plotly.graph_objects as go
import pandas as pd

quakes = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')

fig = go.Figure(go.Densitymapbox(lat=quakes.Latitude,
                                 lon=quakes.Longitude,
                                 z=quakes.Magnitude,
                                 radius=10))                                 
fig.update_layout(mapbox_style="open-street-map",
                  mapbox_center_lon=0)
fig.show()
