import requests
from bs4 import BeautifulSoup

link = "https://www.megalobiz.com/lrc/maker/MORE.55556270"
requisicao = requests.get(link)
#print(requisicao.text)
site = BeautifulSoup(requisicao.text, "html.parser")
#print(site.prettify())

#titulo = site.find('title')
#print(titulo)

'''pesquisa = site.find_all("div", {"id": "lrc_55556270_details"})
print(pesquisa)
'''
pesquisa2 = site.find("div", class_="lyrics_details entity_more_info")
print(pesquisa2)