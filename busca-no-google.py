from googlesearch import search
#pip install googlesearch-python
#texto de busca
busca = 'anime'

#faz a busca e cria lista com links dos resultados
resultado = list(
    search(
        busca,
        lang='pt-br',
        num_results=5
    )
)

#mostra os resultados
print(resultado)