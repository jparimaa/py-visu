import plotly.express as px

df = px.data.gapminder().query("year==2007")
print(df.columns)
fig = px.choropleth(df,
                    locations="iso_alpha",
                    color="gdpPercap",
                    range_color=(0, 50000),
                    hover_name="country",
                    color_continuous_scale="Blues")
fig.show()
