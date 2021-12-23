import plotly.express as px
import numpy as np

df = px.data.gapminder().query("year == 2007")
fig = px.sunburst(df,
                  path=['continent', 'country'],
                  values='pop',
                  color='gdpPercap',
                  hover_data=['iso_alpha'],
                  color_continuous_scale='Blues',
                  color_continuous_midpoint=np.max(df['gdpPercap']) / 2)
fig.show()
