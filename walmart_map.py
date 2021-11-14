import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/1962_2006_walmart_store_openings.csv')

print(df.head())

layout = dict(title='New Walmart Stores per year 1962-2006',
              # showlegend = False,
              autosize=False,
              width=1000,
              height=900,
              hovermode=False,
              legend=dict(x=0.7,
                          y=-0.1,
                          bgcolor="rgba(255, 255, 255, 0)",
                          font=dict(size=11),
                          )
              )

years_unique = df['YEAR'].unique()
data = []

for i in range(len(years_unique)):
    geo_key = 'geo'+str(i+1) if i != 0 else 'geo'
    list_for_year = df['YEAR'] == years_unique[i]
    lons = list(df[list_for_year]['LON'])
    lats = list(df[list_for_year]['LAT'])
    # Walmart store data
    data.append(dict(type='scattergeo',
                     showlegend=False,
                     lon=lons,
                     lat=lats,
                     geo=geo_key,
                     name=int(years_unique[i]),
                     marker=dict(color="rgb(0, 0, 255)",
                                 opacity=0.5
                                 )
                     )
                )
    # Year markers
    data.append(dict(type='scattergeo',
                     showlegend=False,
                     lon=[-78],
                     lat=[47],
                     geo=geo_key,
                     text=[years_unique[i]],
                     mode='text',
                     )
                )
    layout[geo_key] = dict(scope='usa',
                           showland=True,
                           landcolor='rgb(229, 229, 229)',
                           showcountries=False,
                           domain=dict(x=[], y=[]),
                           subunitcolor="rgb(255, 255, 255)",
                           )


def draw_sparkline(domain, lataxis, lonaxis):
    ''' Returns a sparkline layout object for geo coordinates  '''
    return dict(
        showland=False,
        showframe=False,
        showcountries=False,
        showcoastlines=False,
        domain=domain,
        lataxis=lataxis,
        lonaxis=lonaxis,
        bgcolor='rgba(255,200,200,0.0)'
    )


# Stores per year sparkline
# layout['geo44'] = draw_sparkline({'x': [0.6, 0.8], 'y': [0, 0.15]},
#                                  {'range': [-5.0, 30.0]}, {'range': [0.0, 40.0]})

# data.append(dict(type='scattergeo',
#                  mode='lines',
#                  lat=list(df.groupby(by=['YEAR']).count()['storenum']/1e1),
#                  lon=list(
#                      range(len(df.groupby(by=['YEAR']).count()['storenum']/1e1))),
#                  line=dict(color="rgb(0, 0, 255)"),
#                  name="New stores per year<br>Peak of 178 stores per year in 1990",
#                  geo='geo44',
#                  )
#             )

# Cumulative sum sparkline
# layout['geo45'] = draw_sparkline({'x': [0.8, 1], 'y': [0, 0.15]},
#                                  {'range': [-5.0, 50.0]}, {'range': [0.0, 50.0]})

# data.append(dict(type='scattergeo',
#                  mode='lines',
#                  lat=list(df.groupby(by=['YEAR']).count().cumsum()[
#                           'storenum']/1e2),
#                  lon=list(
#                      range(len(df.groupby(by=['YEAR']).count()['storenum']/1e1))),
#                  line=dict(color="rgb(214, 39, 40)"),
#                  name="Cumulative sum<br>3176 stores total in 2006",
#                  geo='geo45',
#                  )
#             )

z = 0
COLS = 5
ROWS = 9
for y in reversed(range(ROWS)):
    for x in range(COLS):
        geo_key = 'geo'+str(z+1) if z != 0 else 'geo'
        layout[geo_key]['domain']['x'] = [
            float(x)/float(COLS), float(x+1)/float(COLS)]
        layout[geo_key]['domain']['y'] = [
            float(y)/float(ROWS), float(y+1)/float(ROWS)]
        z = z+1
        if z > 42:
            break

fig = go.Figure(data=data, layout=layout)
fig.update_layout(width=800)
fig.show()
