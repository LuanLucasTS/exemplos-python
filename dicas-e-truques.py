#criar uma STRING a partir de uma LISTA
lista = ["essa", "é", "uma", "lista", "de", "palavras"]
print(" ".join(lista))

#armazenar elementos de uma LISTA diretamente em variaveis
lista = [-35, 2, 43]
minimo, medio, maximo = lista
print(minimo, medio, maximo)

#imprimir uma string N vezes
print("Python\n" * 5)

#atribuir MULTIPLOS VALORES a MULTIPLAS VARIAVEIS em apenas uma linha
codigo, nome, erro = 201, " HTTP CREATED", False
print(codigo, nome, erro)

#formatar string usando f-string
codigo, nome, erro = 201, " HTTP CREATED", False
print(f"Código = {codigo}\nNome = {nome}\nErro = {erro} ")

#reverter string usando fatiamento de listas
string = "The book is on the table"
print(f'string reversa: {string[::-1]}')

#trocar o valor de duas variaveis apenas com uma linha de codigo
x, y = 10, 20
print(f'antes: x={x}, y={y}')
x, y = y, x
print(f'depois: x={x}, y={y}')
