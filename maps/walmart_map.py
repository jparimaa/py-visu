import plotly.graph_objects as go
import pandas as pd

def get_geo_key(i):
    return 'geo' + str(i+1) if i > 0 else 'geo' 

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
    geo_key = get_geo_key(i)
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

z = 0
COLS = 5
ROWS = 9
NUM_YEARS = len(years_unique)
for y in reversed(range(ROWS)):
    for x in range(COLS):
        geo_key = get_geo_key(z)
        layout[geo_key]['domain']['x'] = [float(x)/float(COLS), float(x+1)/float(COLS)]
        layout[geo_key]['domain']['y'] = [float(y)/float(ROWS), float(y+1)/float(ROWS)]
        z = z+1
        if z >= NUM_YEARS:
            break

fig = go.Figure(data=data, layout=layout)
#fig.update_layout(width=800)
fig.show()
