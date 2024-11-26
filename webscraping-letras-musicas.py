import requests
from bs4 import BeautifulSoup

def search_lyrics(query):
    query = 'more+kda'
    url = f"https://www.megalobiz.com/search/all?qry={query}"  # Substitua pelo URL correto do site megalobiz
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        results = []

        # Substitua essa parte com a estrutura HTML real do site megalobiz
        # Encontre os elementos que contêm as informações das músicas
        # e extraia os títulos e links das letras
        for item in soup.find_all("div", class_="entity_full_member_box"):
            title = link["title"] if link else "Título não encontrado"
            link = item.find("a", class_="entity_name")["href"]
            results.append({"title": title, "link": link})

        return results
    else:
        print("Erro ao buscar a página")
        return []

# Chame a função de busca passando o termo desejado
search_results = search_lyrics("Nome da música")

for result in search_results:
    print(result["title"], result["link"])
