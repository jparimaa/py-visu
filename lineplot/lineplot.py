import plotly.express as px

df = px.data.gapminder().query("country in ['Finland','Sweden','Denmark', 'United States','Canada','New Zealand']")
fig = px.line(df, x="year", y="gdpPercap", title='GDP per capita', color='country')
fig.show()
