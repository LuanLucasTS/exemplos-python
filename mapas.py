import folium
#Cria o mapa
mapa = folium.Map(
    location = [-23.550093493433984, -46.6341472592547],
    tiles = 'Stamen Terrain', #Estilo do mapa
    zoom_start = 16
)
#Adiciona marcador
folium.Marker(
    [-23.550093493433984, -46.6341472592547],
    popup = '<i>Praça da Sé</i>',
    tooltip='Clique aqui!'
).add_to(mapa)
#Salva o html
mapa.save(r'mapa.html')

