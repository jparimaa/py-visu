import plotly.express as px
from urllib.request import urlopen
import json
import pandas as pd

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv", dtype={"fips": str})

fig = px.choropleth(df,
                    geojson=counties,
                    locations='fips',
                    color='unemp',
                    color_continuous_scale="Blues",
                    range_color=(0, 8),
                    scope="usa",
                    labels={'unemp': 'unemployment rate'}
                    )
fig.show()
