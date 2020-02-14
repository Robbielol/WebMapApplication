import folium
import pandas

data = pandas.read_csv("C:/Programming Projects/Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """<h4>Volcano information:</h4>
Height: %s m
"""

map = folium.Map([0, 0], zoom_start=2, tiles="Stamen Terrain")
featureGroup = folium.FeatureGroup(name="Mappy")


def color_producer(elev):
    if elev < 1000:
        return "green"
    elif 1000 <= elev < 3000:
        return "orange"
    else:
        return "red"


fgVolcanoes = folium.FeatureGroup("Volcaneos")

for lt, ln, el, n in zip(lat, lon, elev, name):
    fgVolcanoes.add_child(
        folium.CircleMarker(location=(lt, ln), radius=10, popup=n + "\n" + str(el) + "m", fill_color=color_producer(el),
                            color=color_producer(el), fill_opacity=0.7))


fgPopulation = folium.FeatureGroup("Population")
fgPopulation.add_child(folium.GeoJson(data=open("C:/Programming Projects/world.json", "r", encoding="utf-8-sig").read(),
                                      style_function=lambda y: {
                                          "fillColor": "green" if y["properties"]["POP2005"] < 10000000
                                          else "orange" if 10000000 <= y["properties"]["POP2005"] < 20000000 else "red"
                                      }))

map.add_child(fgVolcanoes)
map.add_child(fgPopulation)
map.add_child(folium.LayerControl())
map.save("Map.html")
