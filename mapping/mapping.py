import folium
import pandas

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles='Mapbox Bright')

fg = folium.FeatureGroup(name='Volcanos')
lc = folium.LayerControl(position='topright')

df0 = pandas.read_csv('Volcanoes_USA.txt')


def elevation(meters):
    if 0 < meters <= int(1000):
        return 'green'
    elif int(1000) < meters <= int(3000):
        return 'orange'
    else:
        return 'red'


lat = list(df0['LAT'])
lon = list(df0['LON'])
elev = list(df0['ELEV'])


for lt, ln, el in zip(lat, lon, elev):
        fg.add_child(folium.CircleMarker(location=[lt, ln], color='gray', radius=6, fill=True, fill_opacity=0.7,
                                         popup=folium.Popup(str('{} m.'.format(el)), parse_html=True),
                                         fill_color=elevation(el)))

gj = folium.GeoJson(name='Population', data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green'
                             if x['properties']['POP2005'] < 10000000 else 'orange'
                             if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'})


map.add_child(gj)
map.add_child(fg)
map.add_child(lc)

map.save('Map1.html')